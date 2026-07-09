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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+12.32%)</td><td>0.04 (+12.88%)</td><td>0.04 (+17.94%)</td><td>0.03 (+1.22%)</td><td>0.01 <b>(+44.53%)</b></td><td>208.00 (-1.23%)</td><td>165.24 (-10.26%)</td><td>157.90 (-15.20%)</td><td>130.60 (-10.97%)</td><td>31.01 <b>(+30.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>184.14 (n/a)</td><td>186.20 (n/a)</td><td>146.70 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (-13.89%)</td><td>0.03 (-15.91%)</td><td>0.03 <b>(-25.41%)</b></td><td>0.03 (-1.66%)</td><td>0.00 <b>(-30.25%)</b></td><td>209.70 (+1.70%)</td><td>183.68 (+17.73%)</td><td>189.90 <b>(+34.11%)</b></td><td>159.20 (+16.12%)</td><td>23.38 (-19.99%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>156.02 (n/a)</td><td>141.60 (n/a)</td><td>137.10 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(-20.30%)</b></td><td>0.03 (-12.45%)</td><td>0.04 (-0.70%)</td><td>0.03 <b>(-20.40%)</b></td><td>0.01 (-3.52%)</td><td>238.20 <b>(+25.63%)</b></td><td>187.28 (+15.19%)</td><td>163.80 (+0.74%)</td><td>160.00 <b>(+25.49%)</b></td><td>35.33 <b>(+51.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>162.58 (n/a)</td><td>162.60 (n/a)</td><td>127.50 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(-22.25%)</b></td><td>0.03 (-12.52%)</td><td>0.03 (-19.72%)</td><td>0.03 (+7.60%)</td><td>0.00 <b>(-77.80%)</b></td><td>194.60 (-7.07%)</td><td>182.40 (+9.72%)</td><td>186.80 <b>(+24.53%)</b></td><td>169.50 <b>(+28.60%)</b></td><td>10.27 <b>(-73.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>166.24 (n/a)</td><td>150.00 (n/a)</td><td>131.80 (n/a)</td><td>39.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 <b>(+44.65%)</b></td><td>0.04 (+6.26%)</td><td>0.03 (-11.14%)</td><td>0.03 (-8.79%)</td><td>0.01 <b>(+196.06%)</b></td><td>226.20 (+9.65%)</td><td>175.52 (+0.67%)</td><td>185.40 (+12.57%)</td><td>106.10 <b>(-30.88%)</b></td><td>50.78 <b>(+127.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.30 (n/a)</td><td>174.36 (n/a)</td><td>164.70 (n/a)</td><td>153.50 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(-21.60%)</b></td><td>0.03 (-4.50%)</td><td>0.03 (-8.74%)</td><td>0.03 <b>(+47.58%)</b></td><td>0.00 <b>(-69.03%)</b></td><td>215.10 <b>(-32.23%)</b></td><td>198.94 (-2.32%)</td><td>206.80 (+9.59%)</td><td>174.20 <b>(+27.53%)</b></td><td>17.56 <b>(-74.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>317.40 (n/a)</td><td>203.66 (n/a)</td><td>188.70 (n/a)</td><td>136.60 (n/a)</td><td>68.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+4.23%)</td><td>0.03 (-10.76%)</td><td>0.03 <b>(-20.46%)</b></td><td>0.03 (-4.43%)</td><td>0.01 <b>(+33.24%)</b></td><td>230.80 (+4.62%)</td><td>202.68 (+14.01%)</td><td>223.20 <b>(+25.75%)</b></td><td>135.50 (-4.10%)</td><td>39.98 <b>(+32.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>177.78 (n/a)</td><td>177.50 (n/a)</td><td>141.30 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+2.51%)</td><td>0.04 (-6.39%)</td><td>0.03 <b>(-25.09%)</b></td><td>0.03 <b>(+40.58%)</b></td><td>0.01 (-19.49%)</td><td>230.10 <b>(-28.87%)</b></td><td>180.50 (+0.48%)</td><td>190.70 <b>(+33.45%)</b></td><td>131.80 (-2.44%)</td><td>42.81 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>323.50 (n/a)</td><td>179.64 (n/a)</td><td>142.90 (n/a)</td><td>135.10 (n/a)</td><td>80.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (+6.48%)</td><td>0.08 (-2.36%)</td><td>0.08 (-13.94%)</td><td>0.07 (-2.14%)</td><td>0.01 (+4.76%)</td><td>175.30 (+2.16%)</td><td>149.58 (+2.41%)</td><td>156.50 (+16.18%)</td><td>116.10 (-6.07%)</td><td>22.22 (-4.21%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.60 (n/a)</td><td>146.06 (n/a)</td><td>134.70 (n/a)</td><td>123.60 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (+8.08%)</td><td>0.08 (-10.70%)</td><td>0.07 (-13.58%)</td><td>0.05 <b>(-28.34%)</b></td><td>0.02 <b>(+85.68%)</b></td><td>228.30 <b>(+39.55%)</b></td><td>167.98 (+15.90%)</td><td>169.80 (+15.67%)</td><td>118.40 (-7.50%)</td><td>39.93 <b>(+143.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>163.60 (n/a)</td><td>144.94 (n/a)</td><td>146.80 (n/a)</td><td>128.00 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (+2.59%)</td><td>0.08 (+0.40%)</td><td>0.07 (+3.43%)</td><td>0.06 (+11.07%)</td><td>0.01 <b>(-24.37%)</b></td><td>189.40 (-9.94%)</td><td>160.84 (-2.22%)</td><td>165.40 (-3.27%)</td><td>123.70 (-2.52%)</td><td>23.69 <b>(-33.33%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>164.50 (n/a)</td><td>171.00 (n/a)</td><td>126.90 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (-3.35%)</td><td>0.08 (-2.93%)</td><td>0.09 (-4.68%)</td><td>0.06 (-4.66%)</td><td>0.01 (-13.38%)</td><td>202.10 (+4.88%)</td><td>157.46 (+2.45%)</td><td>143.10 (+4.91%)</td><td>130.10 (+3.50%)</td><td>28.99 (-5.96%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>153.70 (n/a)</td><td>136.40 (n/a)</td><td>125.70 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 <b>(+30.43%)</b></td><td>0.08 (+14.61%)</td><td>0.08 (+11.92%)</td><td>0.07 (+16.13%)</td><td>0.02 <b>(+74.98%)</b></td><td>173.40 (-13.86%)</td><td>150.82 (-11.69%)</td><td>151.70 (-10.66%)</td><td>112.60 <b>(-23.30%)</b></td><td>24.43 (+14.98%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>170.78 (n/a)</td><td>169.80 (n/a)</td><td>146.80 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (+15.03%)</td><td>0.07 (-9.75%)</td><td>0.07 (-17.09%)</td><td>0.04 <b>(-36.00%)</b></td><td>0.02 <b>(+170.13%)</b></td><td>292.00 <b>(+56.23%)</b></td><td>192.30 (+18.24%)</td><td>186.10 <b>(+20.61%)</b></td><td>128.10 (-13.09%)</td><td>61.37 <b>(+275.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>162.64 (n/a)</td><td>154.30 (n/a)</td><td>147.40 (n/a)</td><td>16.33 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (+16.48%)</td><td>0.08 (+9.97%)</td><td>0.07 (+13.72%)</td><td>0.06 (+6.55%)</td><td>0.02 <b>(+40.28%)</b></td><td>204.90 (-6.18%)</td><td>166.60 (-7.82%)</td><td>164.80 (-12.06%)</td><td>122.40 (-14.11%)</td><td>34.13 (+15.46%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>180.74 (n/a)</td><td>187.40 (n/a)</td><td>142.50 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 <b>(+27.81%)</b></td><td>0.07 (+19.75%)</td><td>0.07 <b>(+24.51%)</b></td><td>0.05 <b>(+25.08%)</b></td><td>0.02 <b>(+39.73%)</b></td><td>247.90 <b>(-20.06%)</b></td><td>183.18 (-15.83%)</td><td>166.80 (-19.69%)</td><td>133.90 <b>(-21.79%)</b></td><td>46.74 (-14.26%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>310.10 (n/a)</td><td>217.62 (n/a)</td><td>207.70 (n/a)</td><td>171.20 (n/a)</td><td>54.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (-12.34%)</td><td>0.14 (-12.78%)</td><td>0.16 (+7.06%)</td><td>0.07 <b>(-45.63%)</b></td><td>0.04 <b>(+48.13%)</b></td><td>353.90 <b>(+83.94%)</b></td><td>198.90 <b>(+24.95%)</b></td><td>154.80 (-6.58%)</td><td>144.70 (+14.12%)</td><td>88.34 <b>(+224.82%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.40 (n/a)</td><td>159.18 (n/a)</td><td>165.70 (n/a)</td><td>126.80 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (-9.01%)</td><td>0.14 (+5.57%)</td><td>0.14 (+0.02%)</td><td>0.12 <b>(+22.89%)</b></td><td>0.02 <b>(-35.60%)</b></td><td>202.10 (-18.61%)</td><td>173.04 (-7.70%)</td><td>181.20 (-0.06%)</td><td>147.60 (+9.90%)</td><td>23.80 <b>(-43.90%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>248.30 (n/a)</td><td>187.48 (n/a)</td><td>181.30 (n/a)</td><td>134.30 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (-0.21%)</td><td>0.13 (-6.42%)</td><td>0.14 (-1.03%)</td><td>0.08 <b>(-27.48%)</b></td><td>0.03 <b>(+51.05%)</b></td><td>322.40 <b>(+37.90%)</b></td><td>205.92 (+12.44%)</td><td>170.40 (+1.07%)</td><td>149.10 (+0.20%)</td><td>70.13 <b>(+111.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>183.14 (n/a)</td><td>168.60 (n/a)</td><td>148.80 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (-17.25%)</td><td>0.15 (-1.62%)</td><td>0.15 (+2.85%)</td><td>0.14 (+13.13%)</td><td>0.01 <b>(-74.74%)</b></td><td>170.20 (-11.58%)</td><td>161.82 (-0.04%)</td><td>160.60 (-2.78%)</td><td>153.20 <b>(+20.92%)</b></td><td>6.48 <b>(-72.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>161.88 (n/a)</td><td>165.20 (n/a)</td><td>126.70 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 <b>(+34.84%)</b></td><td>0.15 <b>(+32.69%)</b></td><td>0.15 <b>(+30.27%)</b></td><td>0.11 <b>(+39.60%)</b></td><td>0.03 <b>(+31.06%)</b></td><td>216.60 <b>(-28.35%)</b></td><td>165.56 <b>(-24.89%)</b></td><td>164.50 <b>(-23.20%)</b></td><td>132.10 <b>(-25.83%)</b></td><td>34.08 <b>(-31.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>302.30 (n/a)</td><td>220.42 (n/a)</td><td>214.20 (n/a)</td><td>178.10 (n/a)</td><td>49.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (+15.40%)</td><td>0.14 (+17.89%)</td><td>0.14 (+6.76%)</td><td>0.11 <b>(+47.89%)</b></td><td>0.02 <b>(-28.63%)</b></td><td>216.70 <b>(-32.39%)</b></td><td>181.60 (-18.21%)</td><td>178.10 (-6.31%)</td><td>148.10 (-13.34%)</td><td>25.31 <b>(-58.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>320.50 (n/a)</td><td>222.02 (n/a)</td><td>190.10 (n/a)</td><td>170.90 (n/a)</td><td>61.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (+0.23%)</td><td>0.13 (-3.62%)</td><td>0.14 (-1.75%)</td><td>0.10 (-8.99%)</td><td>0.02 (+16.82%)</td><td>244.70 (+9.88%)</td><td>195.46 (+4.62%)</td><td>176.50 (+1.79%)</td><td>161.20 (-0.19%)</td><td>35.49 <b>(+28.70%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.70 (n/a)</td><td>186.82 (n/a)</td><td>173.40 (n/a)</td><td>161.50 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 <b>(-25.45%)</b></td><td>0.14 (-0.39%)</td><td>0.13 (+18.82%)</td><td>0.11 (+2.78%)</td><td>0.02 <b>(-60.66%)</b></td><td>220.10 (-2.70%)</td><td>182.86 (-4.08%)</td><td>182.40 (-15.83%)</td><td>159.60 <b>(+34.12%)</b></td><td>23.35 <b>(-47.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>226.20 (n/a)</td><td>190.64 (n/a)</td><td>216.70 (n/a)</td><td>119.00 (n/a)</td><td>44.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 (-1.37%)</td><td>0.28 (+3.19%)</td><td>0.29 (+7.67%)</td><td>0.25 <b>(+23.52%)</b></td><td>0.03 <b>(-40.16%)</b></td><td>194.20 (-19.05%)</td><td>174.90 (-4.68%)</td><td>167.40 (-7.10%)</td><td>156.30 (+1.43%)</td><td>16.40 <b>(-51.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>239.90 (n/a)</td><td>183.48 (n/a)</td><td>180.20 (n/a)</td><td>154.10 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.38 (+8.82%)</td><td>0.32 (+9.40%)</td><td>0.29 (+1.81%)</td><td>0.25 (+0.61%)</td><td>0.06 <b>(+53.45%)</b></td><td>196.20 (-0.61%)</td><td>159.98 (-7.32%)</td><td>169.70 (-1.79%)</td><td>129.50 (-8.09%)</td><td>28.68 <b>(+37.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>197.40 (n/a)</td><td>172.62 (n/a)</td><td>172.80 (n/a)</td><td>140.90 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.36 (+1.61%)</td><td>0.33 (+14.14%)</td><td>0.33 (+12.42%)</td><td>0.28 <b>(+38.96%)</b></td><td>0.03 <b>(-52.06%)</b></td><td>175.00 <b>(-28.04%)</b></td><td>152.20 (-15.18%)</td><td>150.90 (-11.08%)</td><td>136.40 (-1.59%)</td><td>14.15 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>243.20 (n/a)</td><td>179.44 (n/a)</td><td>169.70 (n/a)</td><td>138.60 (n/a)</td><td>41.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.42 (+10.01%)</td><td>0.31 (+10.80%)</td><td>0.30 (+12.67%)</td><td>0.24 (+0.65%)</td><td>0.06 (+16.35%)</td><td>203.60 (-0.63%)</td><td>161.42 (-9.24%)</td><td>162.70 (-11.24%)</td><td>118.00 (-9.09%)</td><td>30.31 (+7.07%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>204.90 (n/a)</td><td>177.86 (n/a)</td><td>183.30 (n/a)</td><td>129.80 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.35 (-6.47%)</td><td>0.30 (-1.06%)</td><td>0.29 (+2.46%)</td><td>0.27 (+3.38%)</td><td>0.03 <b>(-30.21%)</b></td><td>179.80 (-3.23%)</td><td>167.16 (+0.36%)</td><td>169.70 (-2.36%)</td><td>140.80 (+6.91%)</td><td>15.37 <b>(-27.54%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>185.80 (n/a)</td><td>166.56 (n/a)</td><td>173.80 (n/a)</td><td>131.70 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.36 (+1.62%)</td><td>0.31 (+10.81%)</td><td>0.30 (+7.12%)</td><td>0.23 (+7.19%)</td><td>0.05 (-8.95%)</td><td>210.30 (-6.74%)</td><td>164.50 (-10.38%)</td><td>165.10 (-6.67%)</td><td>136.40 (-1.66%)</td><td>28.59 (-16.08%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>225.50 (n/a)</td><td>183.56 (n/a)</td><td>176.90 (n/a)</td><td>138.70 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (-14.02%)</td><td>0.25 (+2.20%)</td><td>0.25 (+10.94%)</td><td>0.23 <b>(+36.16%)</b></td><td>0.02 <b>(-67.91%)</b></td><td>215.30 <b>(-26.54%)</b></td><td>198.54 (-6.60%)</td><td>196.20 (-9.83%)</td><td>178.20 (+16.32%)</td><td>15.31 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>293.10 (n/a)</td><td>212.56 (n/a)</td><td>217.60 (n/a)</td><td>153.20 (n/a)</td><td>54.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.30 (-1.31%)</td><td>0.26 (+10.91%)</td><td>0.26 (+19.16%)</td><td>0.21 <b>(+28.02%)</b></td><td>0.04 <b>(-49.82%)</b></td><td>232.30 <b>(-21.89%)</b></td><td>192.88 (-14.85%)</td><td>188.50 (-16.11%)</td><td>162.50 (+1.31%)</td><td>27.04 <b>(-59.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>297.40 (n/a)</td><td>226.52 (n/a)</td><td>224.70 (n/a)</td><td>160.40 (n/a)</td><td>66.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (-6.88%)</td><td>0.02 (-18.31%)</td><td>0.02 (-17.84%)</td><td>0.01 <b>(-30.29%)</b></td><td>0.00 <b>(+199.93%)</b></td><td>193.30 <b>(+43.40%)</b></td><td>155.58 <b>(+26.24%)</b></td><td>148.40 <b>(+21.74%)</b></td><td>125.00 (+7.39%)</td><td>31.98 <b>(+354.52%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>134.80 (n/a)</td><td>123.24 (n/a)</td><td>121.90 (n/a)</td><td>116.40 (n/a)</td><td>7.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (-9.33%)</td><td>0.02 (-7.34%)</td><td>0.02 (-8.73%)</td><td>0.01 (+5.76%)</td><td>0.00 <b>(-27.77%)</b></td><td>217.70 (-5.43%)</td><td>174.12 (+5.87%)</td><td>172.20 (+9.61%)</td><td>140.00 (+10.24%)</td><td>30.10 <b>(-25.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>230.20 (n/a)</td><td>164.46 (n/a)</td><td>157.10 (n/a)</td><td>127.00 (n/a)</td><td>40.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (+0.70%)</td><td>0.02 (-5.04%)</td><td>0.02 <b>(-26.40%)</b></td><td>0.01 <b>(+91.83%)</b></td><td>0.00 <b>(-49.46%)</b></td><td>182.20 <b>(-47.88%)</b></td><td>161.70 (-8.64%)</td><td>168.90 <b>(+35.88%)</b></td><td>119.60 (-0.66%)</td><td>25.63 <b>(-74.02%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>349.60 (n/a)</td><td>177.00 (n/a)</td><td>124.30 (n/a)</td><td>120.40 (n/a)</td><td>98.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (+8.97%)</td><td>0.02 (-0.72%)</td><td>0.02 (+4.67%)</td><td>0.01 (+0.57%)</td><td>0.00 (+0.33%)</td><td>189.00 (-0.58%)</td><td>159.78 (+0.40%)</td><td>163.60 (-4.44%)</td><td>114.20 (-8.20%)</td><td>28.23 (-9.73%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>159.14 (n/a)</td><td>171.20 (n/a)</td><td>124.40 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 <b>(-24.16%)</b></td><td>0.01 <b>(-22.26%)</b></td><td>0.02 <b>(-21.75%)</b></td><td>0.01 (-19.42%)</td><td>0.00 <b>(-33.60%)</b></td><td>227.30 <b>(+24.07%)</b></td><td>182.78 <b>(+27.51%)</b></td><td>172.60 <b>(+27.76%)</b></td><td>147.50 <b>(+31.81%)</b></td><td>31.09 (+8.75%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.20 (n/a)</td><td>143.34 (n/a)</td><td>135.10 (n/a)</td><td>111.90 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (-5.03%)</td><td>0.02 (-8.66%)</td><td>0.01 <b>(-23.93%)</b></td><td>0.01 <b>(+22.56%)</b></td><td>0.00 <b>(-29.03%)</b></td><td>197.70 (-18.41%)</td><td>177.30 (+6.90%)</td><td>193.50 <b>(+31.45%)</b></td><td>145.80 (+5.27%)</td><td>25.60 <b>(-40.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>165.86 (n/a)</td><td>147.20 (n/a)</td><td>138.50 (n/a)</td><td>43.15 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 <b>(-27.27%)</b></td><td>0.01 <b>(-24.49%)</b></td><td>0.01 <b>(-28.37%)</b></td><td>0.01 (-8.84%)</td><td>0.00 <b>(-53.14%)</b></td><td>230.90 (+9.69%)</td><td>203.14 <b>(+28.18%)</b></td><td>208.30 <b>(+39.61%)</b></td><td>159.50 <b>(+37.50%)</b></td><td>26.82 <b>(-31.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.50 (n/a)</td><td>158.48 (n/a)</td><td>149.20 (n/a)</td><td>116.00 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.01 (-16.46%)</td><td>0.01 (-6.80%)</td><td>0.01 (-2.74%)</td><td>0.01 (-0.81%)</td><td>0.00 <b>(-35.52%)</b></td><td>257.20 (+0.82%)</td><td>218.06 (+5.58%)</td><td>220.20 (+2.85%)</td><td>175.30 (+19.74%)</td><td>31.97 (-19.99%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>255.10 (n/a)</td><td>206.54 (n/a)</td><td>214.10 (n/a)</td><td>146.40 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (-6.81%)</td><td>0.03 (+11.09%)</td><td>0.04 <b>(+34.30%)</b></td><td>0.03 (+17.62%)</td><td>0.01 <b>(-20.19%)</b></td><td>187.90 (-14.98%)</td><td>157.92 (-11.15%)</td><td>140.00 <b>(-25.53%)</b></td><td>137.90 (+7.32%)</td><td>25.72 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>177.74 (n/a)</td><td>188.00 (n/a)</td><td>128.50 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(-20.56%)</b></td><td>0.03 (-4.21%)</td><td>0.03 (-14.61%)</td><td>0.02 <b>(+38.81%)</b></td><td>0.01 <b>(-49.56%)</b></td><td>268.60 <b>(-27.97%)</b></td><td>184.08 (-10.91%)</td><td>171.30 (+17.09%)</td><td>139.60 <b>(+25.88%)</b></td><td>51.68 <b>(-54.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>372.90 (n/a)</td><td>206.62 (n/a)</td><td>146.30 (n/a)</td><td>110.90 (n/a)</td><td>112.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (+4.88%)</td><td>0.03 (+7.82%)</td><td>0.03 (+6.85%)</td><td>0.03 (+1.20%)</td><td>0.00 <b>(+21.14%)</b></td><td>190.50 (-1.19%)</td><td>162.76 (-6.95%)</td><td>167.40 (-6.43%)</td><td>140.40 (-4.68%)</td><td>20.60 (+12.57%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.80 (n/a)</td><td>174.92 (n/a)</td><td>178.90 (n/a)</td><td>147.30 (n/a)</td><td>18.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (+9.50%)</td><td>0.03 (+1.73%)</td><td>0.03 (+12.25%)</td><td>0.02 (-13.94%)</td><td>0.01 (+19.33%)</td><td>264.60 (+16.15%)</td><td>182.78 (+0.16%)</td><td>171.60 (-10.90%)</td><td>128.40 (-8.68%)</td><td>50.01 <b>(+34.16%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>182.48 (n/a)</td><td>192.60 (n/a)</td><td>140.60 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(-30.52%)</b></td><td>0.03 (-18.69%)</td><td>0.03 (-15.36%)</td><td>0.02 (-9.55%)</td><td>0.00 <b>(-50.85%)</b></td><td>221.20 (+10.54%)</td><td>187.90 (+18.88%)</td><td>186.80 (+18.15%)</td><td>151.30 <b>(+43.96%)</b></td><td>30.91 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>158.06 (n/a)</td><td>158.10 (n/a)</td><td>105.10 (n/a)</td><td>39.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-5.51%)</td><td>0.03 (-6.62%)</td><td>0.03 (-8.03%)</td><td>0.02 (-6.79%)</td><td>0.00 (-14.10%)</td><td>229.80 (+7.33%)</td><td>197.64 (+6.90%)</td><td>195.10 (+8.75%)</td><td>170.10 (+5.85%)</td><td>21.68 (-2.24%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>184.88 (n/a)</td><td>179.40 (n/a)</td><td>160.70 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-10.69%)</td><td>0.02 (-17.75%)</td><td>0.02 (-17.21%)</td><td>0.02 <b>(-26.65%)</b></td><td>0.01 <b>(+23.32%)</b></td><td>303.70 <b>(+36.31%)</b></td><td>231.58 <b>(+25.11%)</b></td><td>233.30 <b>(+20.82%)</b></td><td>159.60 (+12.00%)</td><td>56.30 <b>(+90.36%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>185.10 (n/a)</td><td>193.10 (n/a)</td><td>142.50 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (+0.25%)</td><td>0.02 (-5.27%)</td><td>0.02 (-8.91%)</td><td>0.02 (-11.52%)</td><td>0.00 <b>(+40.87%)</b></td><td>253.70 (+13.01%)</td><td>215.60 (+6.57%)</td><td>224.30 (+9.79%)</td><td>171.30 (-0.23%)</td><td>30.64 <b>(+59.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>202.30 (n/a)</td><td>204.30 (n/a)</td><td>171.70 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (-10.34%)</td><td>0.06 (-11.02%)</td><td>0.06 (-13.46%)</td><td>0.04 <b>(-22.43%)</b></td><td>0.01 (+11.32%)</td><td>253.70 <b>(+28.91%)</b></td><td>185.68 (+13.94%)</td><td>178.40 (+15.54%)</td><td>154.90 (+11.52%)</td><td>40.16 <b>(+61.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>162.96 (n/a)</td><td>154.40 (n/a)</td><td>138.90 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (-9.52%)</td><td>0.06 (-8.20%)</td><td>0.06 (-8.02%)</td><td>0.05 <b>(-20.39%)</b></td><td>0.01 (+14.15%)</td><td>229.30 <b>(+25.58%)</b></td><td>176.54 (+10.78%)</td><td>170.30 (+8.75%)</td><td>134.60 (+10.51%)</td><td>39.23 <b>(+56.13%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>159.36 (n/a)</td><td>156.60 (n/a)</td><td>121.80 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (-6.54%)</td><td>0.06 (-6.75%)</td><td>0.06 (-11.31%)</td><td>0.05 (-4.68%)</td><td>0.01 (-4.89%)</td><td>191.70 (+4.93%)</td><td>167.70 (+7.33%)</td><td>176.40 (+12.79%)</td><td>127.00 (+6.99%)</td><td>25.73 (+8.46%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>156.24 (n/a)</td><td>156.40 (n/a)</td><td>118.70 (n/a)</td><td>23.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (-8.28%)</td><td>0.05 (-10.19%)</td><td>0.05 (-16.08%)</td><td>0.04 (+10.62%)</td><td>0.01 <b>(-27.87%)</b></td><td>257.80 (-9.61%)</td><td>209.02 (+7.71%)</td><td>213.20 (+19.17%)</td><td>149.00 (+9.08%)</td><td>41.49 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>285.20 (n/a)</td><td>194.06 (n/a)</td><td>178.90 (n/a)</td><td>136.60 (n/a)</td><td>59.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (-10.08%)</td><td>0.06 (-11.58%)</td><td>0.06 (-9.98%)</td><td>0.04 (-6.92%)</td><td>0.01 (-4.85%)</td><td>242.60 (+7.39%)</td><td>188.78 (+13.50%)</td><td>180.30 (+11.09%)</td><td>146.60 (+11.23%)</td><td>43.84 (+14.11%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>166.32 (n/a)</td><td>162.30 (n/a)</td><td>131.80 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (+3.33%)</td><td>0.06 (-12.35%)</td><td>0.07 (-8.88%)</td><td>0.03 <b>(-53.45%)</b></td><td>0.02 <b>(+240.77%)</b></td><td>342.90 <b>(+114.85%)</b></td><td>186.76 <b>(+28.08%)</b></td><td>156.80 (+9.73%)</td><td>128.10 (-3.25%)</td><td>88.21 <b>(+661.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>159.60 (n/a)</td><td>145.82 (n/a)</td><td>142.90 (n/a)</td><td>132.40 (n/a)</td><td>11.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (+0.73%)</td><td>0.07 (+2.54%)</td><td>0.07 (+5.75%)</td><td>0.06 (+8.73%)</td><td>0.01 (-14.20%)</td><td>183.30 (-7.98%)</td><td>159.28 (-2.98%)</td><td>159.60 (-5.39%)</td><td>139.80 (-0.71%)</td><td>18.89 <b>(-21.02%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>164.18 (n/a)</td><td>168.70 (n/a)</td><td>140.80 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 <b>(+24.56%)</b></td><td>0.05 (+6.19%)</td><td>0.06 (+16.10%)</td><td>0.03 <b>(-40.94%)</b></td><td>0.02 <b>(+475.07%)</b></td><td>393.70 <b>(+69.33%)</b></td><td>225.80 (+4.27%)</td><td>184.50 (-13.83%)</td><td>162.70 (-19.73%)</td><td>96.26 <b>(+706.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>232.50 (n/a)</td><td>216.56 (n/a)</td><td>214.10 (n/a)</td><td>202.70 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (-7.30%)</td><td>0.14 (+8.66%)</td><td>0.15 <b>(+41.27%)</b></td><td>0.11 (+19.99%)</td><td>0.02 <b>(-33.93%)</b></td><td>193.90 (-16.67%)</td><td>157.84 (-11.48%)</td><td>136.60 <b>(-29.22%)</b></td><td>134.30 (+7.87%)</td><td>30.31 <b>(-38.44%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>232.70 (n/a)</td><td>178.32 (n/a)</td><td>193.00 (n/a)</td><td>124.50 (n/a)</td><td>49.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (-19.40%)</td><td>0.12 (-6.19%)</td><td>0.12 (+6.53%)</td><td>0.09 (+5.19%)</td><td>0.02 <b>(-49.35%)</b></td><td>240.70 (-4.94%)</td><td>177.36 (+0.66%)</td><td>169.80 (-6.08%)</td><td>146.90 <b>(+24.07%)</b></td><td>37.17 <b>(-35.10%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>253.20 (n/a)</td><td>176.20 (n/a)</td><td>180.80 (n/a)</td><td>118.40 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (+8.88%)</td><td>0.15 (+12.45%)</td><td>0.14 <b>(+21.07%)</b></td><td>0.11 (+2.60%)</td><td>0.03 (+12.32%)</td><td>189.20 (-2.57%)</td><td>147.90 (-10.85%)</td><td>152.90 (-17.40%)</td><td>110.70 (-8.21%)</td><td>33.59 (-4.20%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>194.20 (n/a)</td><td>165.90 (n/a)</td><td>185.10 (n/a)</td><td>120.60 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 <b>(-22.65%)</b></td><td>0.13 (+3.50%)</td><td>0.12 (+16.03%)</td><td>0.12 (+12.00%)</td><td>0.01 <b>(-63.62%)</b></td><td>182.00 (-10.74%)</td><td>167.18 (-7.13%)</td><td>172.60 (-13.83%)</td><td>149.40 <b>(+29.24%)</b></td><td>15.84 <b>(-57.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>180.02 (n/a)</td><td>200.30 (n/a)</td><td>115.60 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-18.00%)</td><td>0.11 (-8.83%)</td><td>0.12 (-3.49%)</td><td>0.10 (+6.75%)</td><td>0.01 <b>(-52.06%)</b></td><td>210.90 (-6.31%)</td><td>187.22 (+7.42%)</td><td>180.50 (+3.62%)</td><td>170.00 <b>(+21.95%)</b></td><td>18.53 <b>(-45.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>225.10 (n/a)</td><td>174.28 (n/a)</td><td>174.20 (n/a)</td><td>139.40 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (-4.63%)</td><td>0.11 (-9.50%)</td><td>0.11 (-18.11%)</td><td>0.10 (-2.02%)</td><td>0.01 (-15.48%)</td><td>212.90 (+2.11%)</td><td>186.44 (+10.15%)</td><td>192.30 <b>(+22.10%)</b></td><td>160.00 (+4.85%)</td><td>20.82 (-10.62%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>208.50 (n/a)</td><td>169.26 (n/a)</td><td>157.50 (n/a)</td><td>152.60 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (-6.50%)</td><td>0.12 (+0.15%)</td><td>0.11 (-0.81%)</td><td>0.10 (+5.31%)</td><td>0.01 <b>(-37.54%)</b></td><td>208.50 (-5.01%)</td><td>181.36 (-1.63%)</td><td>184.80 (+0.82%)</td><td>159.30 (+6.91%)</td><td>19.99 <b>(-37.55%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>184.36 (n/a)</td><td>183.30 (n/a)</td><td>149.00 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+11.71%)</td><td>0.10 (+11.77%)</td><td>0.10 (+6.33%)</td><td>0.07 <b>(+37.35%)</b></td><td>0.02 (-10.58%)</td><td>280.50 <b>(-27.18%)</b></td><td>222.76 (-13.09%)</td><td>218.40 (-5.94%)</td><td>166.00 (-10.46%)</td><td>41.69 <b>(-45.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>385.20 (n/a)</td><td>256.30 (n/a)</td><td>232.20 (n/a)</td><td>185.40 (n/a)</td><td>76.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>181.80 (n/a)</td><td>159.22 (n/a)</td><td>167.20 (n/a)</td><td>138.30 (n/a)</td><td>19.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>176.22 (n/a)</td><td>171.80 (n/a)</td><td>166.40 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>284.00 (n/a)</td><td>243.92 (n/a)</td><td>263.30 (n/a)</td><td>134.00 (n/a)</td><td>62.15 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.60 (n/a)</td><td>211.16 (n/a)</td><td>196.50 (n/a)</td><td>140.60 (n/a)</td><td>70.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>189.18 (n/a)</td><td>198.00 (n/a)</td><td>145.30 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>170.62 (n/a)</td><td>185.50 (n/a)</td><td>124.20 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>169.58 (n/a)</td><td>179.20 (n/a)</td><td>135.80 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>207.00 (n/a)</td><td>202.50 (n/a)</td><td>169.00 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>179.70 (n/a)</td><td>155.40 (n/a)</td><td>153.90 (n/a)</td><td>129.20 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.10 (n/a)</td><td>170.32 (n/a)</td><td>171.30 (n/a)</td><td>128.40 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.90 (n/a)</td><td>176.10 (n/a)</td><td>181.70 (n/a)</td><td>149.10 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.20 (n/a)</td><td>176.40 (n/a)</td><td>167.90 (n/a)</td><td>132.30 (n/a)</td><td>45.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.34 (-10.40%)</td><td>0.24 <b>(-23.74%)</b></td><td>0.24 <b>(-23.55%)</b></td><td>0.16 <b>(-41.36%)</b></td><td>0.06 <b>(+66.24%)</b></td><td>300.00 <b>(+70.55%)</b></td><td>214.70 <b>(+37.10%)</b></td><td>202.50 <b>(+30.81%)</b></td><td>145.70 (+11.56%)</td><td>56.92 <b>(+216.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>175.90 (n/a)</td><td>156.60 (n/a)</td><td>154.80 (n/a)</td><td>130.60 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>204.70 (n/a)</td><td>179.70 (n/a)</td><td>176.50 (n/a)</td><td>159.30 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>195.30 (n/a)</td><td>173.26 (n/a)</td><td>173.30 (n/a)</td><td>147.00 (n/a)</td><td>17.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>297.70 (n/a)</td><td>201.86 (n/a)</td><td>189.00 (n/a)</td><td>158.90 (n/a)</td><td>55.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>140.06 (n/a)</td><td>126.30 (n/a)</td><td>103.30 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>279.20 (n/a)</td><td>189.08 (n/a)</td><td>166.80 (n/a)</td><td>120.20 (n/a)</td><td>60.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>150.18 (n/a)</td><td>153.00 (n/a)</td><td>122.20 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>183.82 (n/a)</td><td>177.30 (n/a)</td><td>164.20 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>149.12 (n/a)</td><td>135.00 (n/a)</td><td>124.90 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>154.42 (n/a)</td><td>157.70 (n/a)</td><td>120.00 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>267.90 (n/a)</td><td>200.42 (n/a)</td><td>195.20 (n/a)</td><td>131.10 (n/a)</td><td>54.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>182.42 (n/a)</td><td>176.70 (n/a)</td><td>162.50 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.40 (n/a)</td><td>158.28 (n/a)</td><td>156.00 (n/a)</td><td>124.20 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.40 (n/a)</td><td>151.48 (n/a)</td><td>150.80 (n/a)</td><td>120.30 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>248.10 (n/a)</td><td>188.64 (n/a)</td><td>200.40 (n/a)</td><td>129.10 (n/a)</td><td>50.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.50 (n/a)</td><td>185.16 (n/a)</td><td>181.10 (n/a)</td><td>162.80 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>208.70 (n/a)</td><td>165.48 (n/a)</td><td>174.30 (n/a)</td><td>129.90 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>188.80 (n/a)</td><td>141.18 (n/a)</td><td>126.90 (n/a)</td><td>113.20 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.01 (n/a)</td><td>175.00 (n/a)</td><td>162.26 (n/a)</td><td>159.20 (n/a)</td><td>155.40 (n/a)</td><td>7.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>175.06 (n/a)</td><td>174.00 (n/a)</td><td>137.90 (n/a)</td><td>31.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.40 (n/a)</td><td>204.44 (n/a)</td><td>211.00 (n/a)</td><td>138.40 (n/a)</td><td>46.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.60 (n/a)</td><td>200.06 (n/a)</td><td>197.80 (n/a)</td><td>150.30 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>171.30 (n/a)</td><td>165.70 (n/a)</td><td>129.30 (n/a)</td><td>33.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>179.56 (n/a)</td><td>187.00 (n/a)</td><td>133.50 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>178.14 (n/a)</td><td>171.00 (n/a)</td><td>146.00 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>191.68 (n/a)</td><td>197.20 (n/a)</td><td>168.10 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.70 (n/a)</td><td>216.50 (n/a)</td><td>214.40 (n/a)</td><td>182.50 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>157.64 (n/a)</td><td>137.50 (n/a)</td><td>128.30 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>167.08 (n/a)</td><td>154.50 (n/a)</td><td>135.80 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>169.08 (n/a)</td><td>164.40 (n/a)</td><td>141.80 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>163.20 (n/a)</td><td>156.10 (n/a)</td><td>146.50 (n/a)</td><td>22.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>167.06 (n/a)</td><td>169.50 (n/a)</td><td>130.10 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.00 (n/a)</td><td>236.30 (n/a)</td><td>238.30 (n/a)</td><td>164.10 (n/a)</td><td>50.73 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>189.92 (n/a)</td><td>181.80 (n/a)</td><td>160.70 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>247.50 (n/a)</td><td>221.30 (n/a)</td><td>187.90 (n/a)</td><td>69.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.20 (n/a)</td><td>198.74 (n/a)</td><td>209.20 (n/a)</td><td>125.90 (n/a)</td><td>43.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>186.46 (n/a)</td><td>173.50 (n/a)</td><td>169.50 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>182.44 (n/a)</td><td>183.10 (n/a)</td><td>140.20 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>186.26 (n/a)</td><td>184.10 (n/a)</td><td>160.90 (n/a)</td><td>19.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>241.10 (n/a)</td><td>199.26 (n/a)</td><td>196.00 (n/a)</td><td>176.80 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>188.66 (n/a)</td><td>181.00 (n/a)</td><td>173.70 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>241.70 (n/a)</td><td>221.30 (n/a)</td><td>219.30 (n/a)</td><td>205.20 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>298.20 (n/a)</td><td>235.14 (n/a)</td><td>229.70 (n/a)</td><td>187.80 (n/a)</td><td>40.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>224.20 (n/a)</td><td>204.16 (n/a)</td><td>206.40 (n/a)</td><td>172.60 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>184.24 (n/a)</td><td>180.70 (n/a)</td><td>176.10 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>194.82 (n/a)</td><td>191.70 (n/a)</td><td>186.80 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.20 (n/a)</td><td>191.64 (n/a)</td><td>210.10 (n/a)</td><td>148.90 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>238.30 (n/a)</td><td>205.24 (n/a)</td><td>209.50 (n/a)</td><td>168.30 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>203.38 (n/a)</td><td>196.30 (n/a)</td><td>190.00 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>353.70 (n/a)</td><td>256.50 (n/a)</td><td>232.90 (n/a)</td><td>215.50 (n/a)</td><td>55.73 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.90 (+10.42%)</td><td>4.09 (-1.09%)</td><td>4.10 (-1.82%)</td><td>3.25 (-10.15%)</td><td>0.58 <b>(+86.27%)</b></td><td>2894.00 (+11.29%)</td><td>2339.42 (+2.32%)</td><td>2292.50 (+1.85%)</td><td>1921.00 (-9.44%)</td><td>349.63 <b>(+88.11%)</b></td><td>1925.73 (+10.42%)</td><td>1608.36 (-1.09%)</td><td>1613.68 (-1.82%)</td><td>1278.29 (-10.15%)</td><td>229.02 <b>(+86.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>4.43 (n/a)</td><td>4.13 (n/a)</td><td>4.18 (n/a)</td><td>3.62 (n/a)</td><td>0.31 (n/a)</td><td>2600.30 (n/a)</td><td>2286.32 (n/a)</td><td>2250.80 (n/a)</td><td>2121.30 (n/a)</td><td>185.86 (n/a)</td><td>1743.96 (n/a)</td><td>1626.03 (n/a)</td><td>1643.57 (n/a)</td><td>1422.65 (n/a)</td><td>122.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.11 (-10.57%)</td><td>0.94 (-15.95%)</td><td>0.95 (-14.17%)</td><td>0.78 <b>(-20.58%)</b></td><td>0.12 (+4.54%)</td><td>282.10 <b>(+25.94%)</b></td><td>237.40 (+19.50%)</td><td>234.00 (+16.48%)</td><td>198.90 (+11.80%)</td><td>29.73 <b>(+50.21%)</b></td><td>47.45 (-10.57%)</td><td>40.25 (-15.95%)</td><td>40.33 (-14.17%)</td><td>33.45 <b>(-20.58%)</b></td><td>4.98 (+4.54%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.24 (n/a)</td><td>1.12 (n/a)</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>0.11 (n/a)</td><td>224.00 (n/a)</td><td>198.66 (n/a)</td><td>200.90 (n/a)</td><td>177.90 (n/a)</td><td>19.79 (n/a)</td><td>53.06 (n/a)</td><td>47.88 (n/a)</td><td>46.98 (n/a)</td><td>42.13 (n/a)</td><td>4.77 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.16 (-12.92%)</td><td>0.98 (-8.40%)</td><td>1.10 (+6.38%)</td><td>0.61 <b>(-33.79%)</b></td><td>0.23 <b>(+38.12%)</b></td><td>361.60 <b>(+51.04%)</b></td><td>238.10 (+13.56%)</td><td>201.80 (-6.01%)</td><td>190.20 (+14.86%)</td><td>71.78 <b>(+143.87%)</b></td><td>49.62 (-12.92%)</td><td>41.95 (-8.40%)</td><td>46.76 (+6.38%)</td><td>26.10 <b>(-33.79%)</b></td><td>9.72 <b>(+38.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.34 (n/a)</td><td>1.07 (n/a)</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td><td>0.16 (n/a)</td><td>239.40 (n/a)</td><td>209.66 (n/a)</td><td>214.70 (n/a)</td><td>165.60 (n/a)</td><td>29.43 (n/a)</td><td>56.98 (n/a)</td><td>45.79 (n/a)</td><td>43.95 (n/a)</td><td>39.41 (n/a)</td><td>7.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.52 (+0.03%)</td><td>0.52 (+0.03%)</td><td>0.52 (+0.01%)</td><td>0.52 (+0.03%)</td><td>0.00 (+8.67%)</td><td>48672.00 (-0.03%)</td><td>48641.44 (-0.03%)</td><td>48648.20 (-0.01%)</td><td>48614.70 (-0.03%)</td><td>24.81 (+8.53%)</td><td>353.39 (+0.03%)</td><td>353.19 (+0.03%)</td><td>353.15 (+0.01%)</td><td>352.97 (+0.03%)</td><td>0.18 (+8.69%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48687.60 (n/a)</td><td>48654.26 (n/a)</td><td>48655.20 (n/a)</td><td>48630.20 (n/a)</td><td>22.85 (n/a)</td><td>353.28 (n/a)</td><td>353.10 (n/a)</td><td>353.09 (n/a)</td><td>352.86 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (+0.39%)</td><td>0.21 (+1.39%)</td><td>0.21 (+1.59%)</td><td>0.21 (+2.13%)</td><td>0.00 <b>(-65.42%)</b></td><td>118633.00 (-2.09%)</td><td>118282.30 (-1.37%)</td><td>118331.30 (-1.57%)</td><td>117917.90 (-0.39%)</td><td>346.60 <b>(-66.24%)</b></td><td>145.69 (+0.39%)</td><td>145.25 (+1.39%)</td><td>145.18 (+1.59%)</td><td>144.82 (+2.13%)</td><td>0.43 <b>(-65.42%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>121163.60 (n/a)</td><td>119929.88 (n/a)</td><td>120213.40 (n/a)</td><td>118375.00 (n/a)</td><td>1026.77 (n/a)</td><td>145.13 (n/a)</td><td>143.26 (n/a)</td><td>142.91 (n/a)</td><td>141.79 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.90 (+1.98%)</td><td>0.89 (+1.24%)</td><td>0.89 (+0.88%)</td><td>0.88 (+0.90%)</td><td>0.01 <b>(+85.08%)</b></td><td>28713.10 (-0.89%)</td><td>28301.36 (-1.21%)</td><td>28378.30 (-0.87%)</td><td>27895.20 (-1.94%)</td><td>348.41 <b>(+79.36%)</b></td><td>615.87 (+1.98%)</td><td>607.11 (+1.24%)</td><td>605.39 (+0.88%)</td><td>598.33 (+0.90%)</td><td>7.48 <b>(+85.08%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28970.70 (n/a)</td><td>28649.40 (n/a)</td><td>28628.50 (n/a)</td><td>28448.50 (n/a)</td><td>194.25 (n/a)</td><td>603.89 (n/a)</td><td>599.68 (n/a)</td><td>600.10 (n/a)</td><td>593.01 (n/a)</td><td>4.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.57 (+0.95%)</td><td>3.43 (-0.72%)</td><td>3.40 (-3.16%)</td><td>3.33 (+0.07%)</td><td>0.10 (-1.07%)</td><td>7548.50 (-0.07%)</td><td>7349.78 (+0.73%)</td><td>7406.40 (+3.26%)</td><td>7057.80 (-0.94%)</td><td>208.74 (-1.83%)</td><td>2434.17 (+0.95%)</td><td>2339.00 (-0.72%)</td><td>2319.59 (-3.16%)</td><td>2275.93 (+0.07%)</td><td>67.21 (-1.07%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.53 (n/a)</td><td>3.45 (n/a)</td><td>3.51 (n/a)</td><td>3.33 (n/a)</td><td>0.10 (n/a)</td><td>7553.70 (n/a)</td><td>7296.80 (n/a)</td><td>7172.40 (n/a)</td><td>7125.00 (n/a)</td><td>212.63 (n/a)</td><td>2411.22 (n/a)</td><td>2356.03 (n/a)</td><td>2395.29 (n/a)</td><td>2274.37 (n/a)</td><td>67.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>2.84 (-0.39%)</td><td>2.80 (+1.96%)</td><td>2.82 (+4.12%)</td><td>2.69 (+0.06%)</td><td>0.06 (-7.70%)</td><td>9364.80 (-0.06%)</td><td>8994.48 (-1.93%)</td><td>8928.30 (-3.95%)</td><td>8851.50 (+0.39%)</td><td>211.15 (-7.02%)</td><td>1940.90 (-0.39%)</td><td>1910.87 (+1.96%)</td><td>1924.20 (+4.12%)</td><td>1834.52 (+0.06%)</td><td>43.62 (-7.70%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>2.85 (n/a)</td><td>2.75 (n/a)</td><td>2.71 (n/a)</td><td>2.69 (n/a)</td><td>0.07 (n/a)</td><td>9370.00 (n/a)</td><td>9171.74 (n/a)</td><td>9295.90 (n/a)</td><td>8817.20 (n/a)</td><td>227.10 (n/a)</td><td>1948.46 (n/a)</td><td>1874.07 (n/a)</td><td>1848.11 (n/a)</td><td>1833.49 (n/a)</td><td>47.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.31 (-0.52%)</td><td>3.18 (-0.66%)</td><td>3.16 (-2.13%)</td><td>3.12 (+1.54%)</td><td>0.08 <b>(-33.65%)</b></td><td>8058.00 (-1.52%)</td><td>7908.20 (+0.60%)</td><td>7970.30 (+2.17%)</td><td>7600.20 (+0.52%)</td><td>182.54 <b>(-34.69%)</b></td><td>2260.46 (-0.52%)</td><td>2173.36 (-0.66%)</td><td>2155.49 (-2.13%)</td><td>2132.01 (+1.54%)</td><td>51.37 <b>(-33.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.33 (n/a)</td><td>3.20 (n/a)</td><td>3.23 (n/a)</td><td>3.08 (n/a)</td><td>0.11 (n/a)</td><td>8182.20 (n/a)</td><td>7860.72 (n/a)</td><td>7800.90 (n/a)</td><td>7560.80 (n/a)</td><td>279.50 (n/a)</td><td>2272.23 (n/a)</td><td>2187.74 (n/a)</td><td>2202.30 (n/a)</td><td>2099.65 (n/a)</td><td>77.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.78 (+0.21%)</td><td>0.78 (+0.01%)</td><td>0.78 (+0.01%)</td><td>0.78 (-0.07%)</td><td>0.00 <b>(+146.33%)</b></td><td>96651.00 (+0.07%)</td><td>96464.64 (-0.01%)</td><td>96440.70 (-0.01%)</td><td>96224.00 (-0.21%)</td><td>161.63 <b>(+145.88%)</b></td><td>714.16 (+0.21%)</td><td>712.38 (+0.01%)</td><td>712.56 (+0.01%)</td><td>711.01 (-0.07%)</td><td>1.19 <b>(+146.34%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96586.50 (n/a)</td><td>96470.88 (n/a)</td><td>96446.90 (n/a)</td><td>96423.00 (n/a)</td><td>65.74 (n/a)</td><td>712.69 (n/a)</td><td>712.33 (n/a)</td><td>712.51 (n/a)</td><td>711.48 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.73 (-0.04%)</td><td>0.73 (-0.09%)</td><td>0.73 (-0.06%)</td><td>0.73 (-0.17%)</td><td>0.00 <b>(+114.07%)</b></td><td>103840.80 (+0.17%)</td><td>103715.18 (+0.09%)</td><td>103686.90 (+0.06%)</td><td>103627.60 (+0.04%)</td><td>80.79 <b>(+114.44%)</b></td><td>663.14 (-0.04%)</td><td>662.58 (-0.09%)</td><td>662.76 (-0.06%)</td><td>661.78 (-0.17%)</td><td>0.52 <b>(+114.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103664.70 (n/a)</td><td>103625.06 (n/a)</td><td>103620.30 (n/a)</td><td>103586.70 (n/a)</td><td>37.68 (n/a)</td><td>663.40 (n/a)</td><td>663.16 (n/a)</td><td>663.19 (n/a)</td><td>662.90 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.69 (+0.09%)</td><td>0.69 (+0.17%)</td><td>0.69 (+0.17%)</td><td>0.69 (+0.20%)</td><td>0.00 (-19.79%)</td><td>109552.80 (-0.20%)</td><td>109385.24 (-0.17%)</td><td>109393.20 (-0.17%)</td><td>109110.30 (-0.09%)</td><td>176.45 <b>(-20.01%)</b></td><td>629.82 (+0.09%)</td><td>628.23 (+0.17%)</td><td>628.19 (+0.17%)</td><td>627.27 (+0.20%)</td><td>1.01 (-19.79%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109767.40 (n/a)</td><td>109566.36 (n/a)</td><td>109577.30 (n/a)</td><td>109209.50 (n/a)</td><td>220.60 (n/a)</td><td>629.24 (n/a)</td><td>627.20 (n/a)</td><td>627.13 (n/a)</td><td>626.05 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.63 (+6.33%)</td><td>7.33 (+8.09%)</td><td>7.32 (+8.01%)</td><td>7.10 (+9.07%)</td><td>0.23 (-11.11%)</td><td>1255.50 (-8.31%)</td><td>1216.50 (-7.51%)</td><td>1218.10 (-7.42%)</td><td>1168.20 (-5.95%)</td><td>38.62 <b>(-23.06%)</b></td><td>459.56 (+6.33%)</td><td>441.69 (+8.09%)</td><td>440.74 (+8.01%)</td><td>427.63 (+9.07%)</td><td>14.08 (-11.11%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.18 (n/a)</td><td>6.78 (n/a)</td><td>6.77 (n/a)</td><td>6.51 (n/a)</td><td>0.26 (n/a)</td><td>1369.30 (n/a)</td><td>1315.34 (n/a)</td><td>1315.70 (n/a)</td><td>1242.10 (n/a)</td><td>50.20 (n/a)</td><td>432.22 (n/a)</td><td>408.64 (n/a)</td><td>408.05 (n/a)</td><td>392.07 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.08 (+1.54%)</td><td>6.73 (-1.64%)</td><td>6.85 (+0.02%)</td><td>6.39 (-4.45%)</td><td>0.29 <b>(+141.67%)</b></td><td>1395.10 (+4.66%)</td><td>1325.56 (+1.79%)</td><td>1301.40 (-0.02%)</td><td>1259.50 (-1.52%)</td><td>56.46 <b>(+150.81%)</b></td><td>426.27 (+1.54%)</td><td>405.60 (-1.64%)</td><td>412.53 (+0.02%)</td><td>384.82 (-4.45%)</td><td>17.17 <b>(+141.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>6.97 (n/a)</td><td>6.85 (n/a)</td><td>6.85 (n/a)</td><td>6.69 (n/a)</td><td>0.12 (n/a)</td><td>1333.00 (n/a)</td><td>1302.24 (n/a)</td><td>1301.70 (n/a)</td><td>1278.90 (n/a)</td><td>22.51 (n/a)</td><td>419.80 (n/a)</td><td>412.37 (n/a)</td><td>412.44 (n/a)</td><td>402.74 (n/a)</td><td>7.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>6.81 (-3.86%)</td><td>6.02 (-12.11%)</td><td>6.36 (-7.92%)</td><td>4.19 <b>(-34.62%)</b></td><td>1.06 <b>(+284.82%)</b></td><td>2129.50 <b>(+52.95%)</b></td><td>1528.22 (+17.29%)</td><td>1400.40 (+8.60%)</td><td>1309.10 (+4.00%)</td><td>341.01 <b>(+528.52%)</b></td><td>410.09 (-3.86%)</td><td>362.66 (-12.11%)</td><td>383.36 (-7.92%)</td><td>252.11 <b>(-34.62%)</b></td><td>63.87 <b>(+284.82%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.08 (n/a)</td><td>6.85 (n/a)</td><td>6.91 (n/a)</td><td>6.40 (n/a)</td><td>0.28 (n/a)</td><td>1392.30 (n/a)</td><td>1302.92 (n/a)</td><td>1289.50 (n/a)</td><td>1258.70 (n/a)</td><td>54.26 (n/a)</td><td>426.54 (n/a)</td><td>412.61 (n/a)</td><td>416.35 (n/a)</td><td>385.59 (n/a)</td><td>16.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.06 (-4.77%)</td><td>7.71 (-2.83%)</td><td>7.84 (-0.67%)</td><td>7.13 (-2.01%)</td><td>0.36 <b>(-20.62%)</b></td><td>4887.00 (+2.05%)</td><td>4531.40 (+2.83%)</td><td>4445.80 (+0.68%)</td><td>4325.00 (+5.01%)</td><td>217.30 (-14.51%)</td><td>496.53 (-4.77%)</td><td>474.75 (-2.83%)</td><td>483.03 (-0.67%)</td><td>439.43 (-2.01%)</td><td>21.92 <b>(-20.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.47 (n/a)</td><td>7.93 (n/a)</td><td>7.90 (n/a)</td><td>7.28 (n/a)</td><td>0.45 (n/a)</td><td>4788.70 (n/a)</td><td>4406.70 (n/a)</td><td>4415.90 (n/a)</td><td>4118.60 (n/a)</td><td>254.19 (n/a)</td><td>521.41 (n/a)</td><td>488.59 (n/a)</td><td>486.31 (n/a)</td><td>448.44 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.76 (+0.09%)</td><td>7.52 (-0.14%)</td><td>7.57 (+1.09%)</td><td>7.28 (+0.38%)</td><td>0.18 (-7.93%)</td><td>4789.30 (-0.38%)</td><td>4636.86 (+0.13%)</td><td>4603.50 (-1.08%)</td><td>4490.40 (-0.09%)</td><td>113.99 (-8.09%)</td><td>478.23 (+0.09%)</td><td>463.36 (-0.14%)</td><td>466.49 (+1.09%)</td><td>448.39 (+0.38%)</td><td>11.37 (-7.93%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.76 (n/a)</td><td>7.53 (n/a)</td><td>7.49 (n/a)</td><td>7.25 (n/a)</td><td>0.20 (n/a)</td><td>4807.50 (n/a)</td><td>4630.66 (n/a)</td><td>4653.90 (n/a)</td><td>4494.60 (n/a)</td><td>124.02 (n/a)</td><td>477.79 (n/a)</td><td>464.02 (n/a)</td><td>461.44 (n/a)</td><td>446.70 (n/a)</td><td>12.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>7.86 (+0.53%)</td><td>7.30 (-0.96%)</td><td>7.34 (-1.79%)</td><td>6.56 (-2.61%)</td><td>0.47 (+19.60%)</td><td>5312.80 (+2.68%)</td><td>4791.40 (+1.08%)</td><td>4750.80 (+1.82%)</td><td>4438.20 (-0.52%)</td><td>322.47 <b>(+22.18%)</b></td><td>483.86 (+0.53%)</td><td>449.76 (-0.96%)</td><td>452.02 (-1.79%)</td><td>404.21 (-2.61%)</td><td>29.04 (+19.60%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.81 (n/a)</td><td>7.37 (n/a)</td><td>7.47 (n/a)</td><td>6.74 (n/a)</td><td>0.39 (n/a)</td><td>5174.00 (n/a)</td><td>4740.00 (n/a)</td><td>4665.70 (n/a)</td><td>4461.60 (n/a)</td><td>263.94 (n/a)</td><td>481.32 (n/a)</td><td>454.14 (n/a)</td><td>460.27 (n/a)</td><td>415.05 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.79 (+0.01%)</td><td>0.79 (-0.00%)</td><td>0.79 (-0.06%)</td><td>0.79 (+0.01%)</td><td>0.00 (-8.79%)</td><td>95889.60 (-0.01%)</td><td>95803.78 (+0.00%)</td><td>95805.70 (+0.06%)</td><td>95717.70 (-0.01%)</td><td>77.97 (-8.79%)</td><td>717.94 (+0.01%)</td><td>717.29 (-0.00%)</td><td>717.28 (-0.06%)</td><td>716.65 (+0.01%)</td><td>0.58 (-8.79%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95900.40 (n/a)</td><td>95800.36 (n/a)</td><td>95749.60 (n/a)</td><td>95724.30 (n/a)</td><td>85.48 (n/a)</td><td>717.89 (n/a)</td><td>717.32 (n/a)</td><td>717.70 (n/a)</td><td>716.57 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.74 (+0.42%)</td><td>0.73 (+0.12%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.12%)</td><td>0.00 <b>(+174.22%)</b></td><td>102968.20 (-0.12%)</td><td>102836.82 (-0.12%)</td><td>102908.60 (-0.03%)</td><td>102461.80 (-0.42%)</td><td>211.11 <b>(+172.59%)</b></td><td>670.68 (+0.42%)</td><td>668.24 (+0.12%)</td><td>667.77 (+0.03%)</td><td>667.39 (+0.12%)</td><td>1.38 <b>(+174.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103092.60 (n/a)</td><td>102963.44 (n/a)</td><td>102944.20 (n/a)</td><td>102895.00 (n/a)</td><td>77.44 (n/a)</td><td>667.86 (n/a)</td><td>667.42 (n/a)</td><td>667.54 (n/a)</td><td>666.58 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.70 (-0.13%)</td><td>0.70 (-0.11%)</td><td>0.70 (-0.07%)</td><td>0.70 (-0.18%)</td><td>0.00 <b>(+21.62%)</b></td><td>108374.80 (+0.18%)</td><td>108113.32 (+0.11%)</td><td>108099.00 (+0.07%)</td><td>107973.30 (+0.13%)</td><td>161.06 <b>(+22.02%)</b></td><td>636.45 (-0.13%)</td><td>635.63 (-0.11%)</td><td>635.71 (-0.07%)</td><td>634.09 (-0.18%)</td><td>0.95 <b>(+21.63%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108174.70 (n/a)</td><td>107995.38 (n/a)</td><td>108020.50 (n/a)</td><td>107831.50 (n/a)</td><td>131.99 (n/a)</td><td>637.29 (n/a)</td><td>636.32 (n/a)</td><td>636.17 (n/a)</td><td>635.26 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.25 (+12.15%)</td><td>3.80 (+4.62%)</td><td>3.99 (+10.51%)</td><td>3.09 (-11.28%)</td><td>0.48 <b>(+290.24%)</b></td><td>2611.20 (+12.72%)</td><td>2148.68 (-3.17%)</td><td>2018.00 (-9.51%)</td><td>1896.60 (-10.83%)</td><td>294.23 <b>(+293.80%)</b></td><td>1114.58 (+12.15%)</td><td>997.51 (+4.62%)</td><td>1047.55 (+10.51%)</td><td>809.57 (-11.28%)</td><td>125.34 <b>(+290.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.79 (n/a)</td><td>3.64 (n/a)</td><td>3.61 (n/a)</td><td>3.48 (n/a)</td><td>0.12 (n/a)</td><td>2316.50 (n/a)</td><td>2219.08 (n/a)</td><td>2230.10 (n/a)</td><td>2127.00 (n/a)</td><td>74.71 (n/a)</td><td>993.87 (n/a)</td><td>953.48 (n/a)</td><td>947.90 (n/a)</td><td>912.54 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.38 <b>(-25.89%)</b></td><td>0.34 (-8.20%)</td><td>0.33 (-7.26%)</td><td>0.32 (+5.02%)</td><td>0.02 <b>(-69.73%)</b></td><td>3901.90 (-4.78%)</td><td>3652.48 (+5.89%)</td><td>3761.30 (+7.82%)</td><td>3280.50 <b>(+34.93%)</b></td><td>253.74 <b>(-59.92%)</b></td><td>20.46 <b>(-25.89%)</b></td><td>18.45 (-8.20%)</td><td>17.84 (-7.26%)</td><td>17.20 (+5.02%)</td><td>1.33 <b>(-69.73%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>4097.80 (n/a)</td><td>3449.44 (n/a)</td><td>3488.40 (n/a)</td><td>2431.20 (n/a)</td><td>633.12 (n/a)</td><td>27.60 (n/a)</td><td>20.10 (n/a)</td><td>19.24 (n/a)</td><td>16.38 (n/a)</td><td>4.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>4.82 (-8.80%)</td><td>4.71 (+4.26%)</td><td>4.81 (+0.80%)</td><td>4.41 (+19.05%)</td><td>0.18 <b>(-74.55%)</b></td><td>1510.00 (-16.00%)</td><td>1415.08 (-5.84%)</td><td>1384.00 (-0.80%)</td><td>1379.60 (+9.65%)</td><td>55.31 <b>(-76.91%)</b></td><td>1489.67 (-8.80%)</td><td>1454.06 (+4.26%)</td><td>1484.99 (+0.80%)</td><td>1361.10 (+19.05%)</td><td>54.48 <b>(-74.55%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.29 (n/a)</td><td>4.51 (n/a)</td><td>4.77 (n/a)</td><td>3.70 (n/a)</td><td>0.69 (n/a)</td><td>1797.60 (n/a)</td><td>1502.92 (n/a)</td><td>1395.10 (n/a)</td><td>1258.20 (n/a)</td><td>239.48 (n/a)</td><td>1633.43 (n/a)</td><td>1394.69 (n/a)</td><td>1473.17 (n/a)</td><td>1143.30 (n/a)</td><td>214.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 <b>(-22.51%)</b></td><td>0.19 (-17.81%)</td><td>0.20 (-15.80%)</td><td>0.14 (-13.00%)</td><td>0.04 <b>(-27.37%)</b></td><td>0.22 <b>(-22.51%)</b></td><td>0.19 (-17.81%)</td><td>0.19 (-15.80%)</td><td>0.14 (-13.00%)</td><td>0.03 <b>(-27.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>13.52 (+1.84%)</td><td>12.96 (+3.47%)</td><td>12.84 (+4.83%)</td><td>12.62 (+8.26%)</td><td>0.39 <b>(-44.77%)</b></td><td>13.51 (+1.84%)</td><td>12.95 (+3.47%)</td><td>12.83 (+4.83%)</td><td>12.61 (+8.26%)</td><td>0.39 <b>(-44.77%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.28 (n/a)</td><td>12.52 (n/a)</td><td>12.24 (n/a)</td><td>11.65 (n/a)</td><td>0.71 (n/a)</td><td>13.27 (n/a)</td><td>12.52 (n/a)</td><td>12.24 (n/a)</td><td>11.65 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>24.89 (+1.30%)</td><td>24.47 (+0.07%)</td><td>24.38 (-0.53%)</td><td>24.25 (+0.04%)</td><td>0.26 <b>(+105.43%)</b></td><td>24.87 (+1.30%)</td><td>24.46 (+0.07%)</td><td>24.36 (-0.53%)</td><td>24.24 (+0.04%)</td><td>0.26 <b>(+105.43%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>24.57 (n/a)</td><td>24.46 (n/a)</td><td>24.50 (n/a)</td><td>24.24 (n/a)</td><td>0.13 (n/a)</td><td>24.55 (n/a)</td><td>24.44 (n/a)</td><td>24.49 (n/a)</td><td>24.23 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>40.87 (-0.23%)</td><td>39.79 (+0.28%)</td><td>40.32 (+2.16%)</td><td>36.68 (-6.20%)</td><td>1.76 <b>(+137.85%)</b></td><td>40.85 (-0.23%)</td><td>39.76 (+0.28%)</td><td>40.29 (+2.16%)</td><td>36.66 (-6.20%)</td><td>1.76 <b>(+137.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>40.97 (n/a)</td><td>39.68 (n/a)</td><td>39.46 (n/a)</td><td>39.10 (n/a)</td><td>0.74 (n/a)</td><td>40.94 (n/a)</td><td>39.65 (n/a)</td><td>39.44 (n/a)</td><td>39.08 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>44.90 (-1.41%)</td><td>42.76 (-4.53%)</td><td>42.08 (-7.45%)</td><td>40.90 (-5.11%)</td><td>1.64 <b>(+51.18%)</b></td><td>44.88 (-1.41%)</td><td>42.73 (-4.53%)</td><td>42.06 (-7.45%)</td><td>40.87 (-5.11%)</td><td>1.64 <b>(+51.19%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>45.55 (n/a)</td><td>44.79 (n/a)</td><td>45.47 (n/a)</td><td>43.10 (n/a)</td><td>1.08 (n/a)</td><td>45.52 (n/a)</td><td>44.76 (n/a)</td><td>45.44 (n/a)</td><td>43.07 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>13.41 (-1.46%)</td><td>12.44 (-1.07%)</td><td>12.35 (-6.59%)</td><td>11.14 (+4.74%)</td><td>0.92 <b>(-23.88%)</b></td><td>13.40 (-1.46%)</td><td>12.43 (-1.07%)</td><td>12.34 (-6.59%)</td><td>11.14 (+4.74%)</td><td>0.92 <b>(-23.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.61 (n/a)</td><td>12.57 (n/a)</td><td>13.22 (n/a)</td><td>10.64 (n/a)</td><td>1.21 (n/a)</td><td>13.60 (n/a)</td><td>12.57 (n/a)</td><td>13.21 (n/a)</td><td>10.63 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>25.04 (-2.65%)</td><td>23.68 (-4.80%)</td><td>24.55 (-1.47%)</td><td>20.02 (-17.57%)</td><td>2.10 <b>(+285.34%)</b></td><td>25.03 (-2.65%)</td><td>23.67 (-4.80%)</td><td>24.53 (-1.47%)</td><td>20.01 (-17.57%)</td><td>2.09 <b>(+285.34%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>25.72 (n/a)</td><td>24.88 (n/a)</td><td>24.91 (n/a)</td><td>24.29 (n/a)</td><td>0.54 (n/a)</td><td>25.71 (n/a)</td><td>24.86 (n/a)</td><td>24.90 (n/a)</td><td>24.27 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>41.78 (-4.80%)</td><td>39.58 (-3.86%)</td><td>39.30 (-3.77%)</td><td>37.08 (-5.90%)</td><td>1.96 (+11.90%)</td><td>41.75 (-4.80%)</td><td>39.56 (-3.86%)</td><td>39.27 (-3.77%)</td><td>37.06 (-5.90%)</td><td>1.95 (+11.90%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>43.88 (n/a)</td><td>41.17 (n/a)</td><td>40.84 (n/a)</td><td>39.41 (n/a)</td><td>1.75 (n/a)</td><td>43.86 (n/a)</td><td>41.15 (n/a)</td><td>40.81 (n/a)</td><td>39.39 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>47.99 (+4.66%)</td><td>44.12 (-0.76%)</td><td>43.99 (-1.90%)</td><td>40.71 (-3.45%)</td><td>2.58 <b>(+71.89%)</b></td><td>47.96 (+4.66%)</td><td>44.09 (-0.76%)</td><td>43.97 (-1.90%)</td><td>40.69 (-3.45%)</td><td>2.58 <b>(+71.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>45.85 (n/a)</td><td>44.46 (n/a)</td><td>44.85 (n/a)</td><td>42.17 (n/a)</td><td>1.50 (n/a)</td><td>45.83 (n/a)</td><td>44.43 (n/a)</td><td>44.82 (n/a)</td><td>42.14 (n/a)</td><td>1.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.50 (n/a)</td><td>170.50 (n/a)</td><td>175.20 (n/a)</td><td>146.60 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>161.08 (n/a)</td><td>166.40 (n/a)</td><td>136.30 (n/a)</td><td>14.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>361.30 (n/a)</td><td>204.68 (n/a)</td><td>177.00 (n/a)</td><td>127.40 (n/a)</td><td>91.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>168.28 (n/a)</td><td>179.80 (n/a)</td><td>111.50 (n/a)</td><td>32.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.30 (n/a)</td><td>146.94 (n/a)</td><td>149.60 (n/a)</td><td>126.70 (n/a)</td><td>12.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>295.10 (n/a)</td><td>190.32 (n/a)</td><td>173.10 (n/a)</td><td>126.70 (n/a)</td><td>63.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>192.90 (n/a)</td><td>188.00 (n/a)</td><td>178.70 (n/a)</td><td>13.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>337.70 (n/a)</td><td>235.50 (n/a)</td><td>219.10 (n/a)</td><td>188.80 (n/a)</td><td>58.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>166.28 (n/a)</td><td>170.10 (n/a)</td><td>125.50 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>158.90 (n/a)</td><td>147.30 (n/a)</td><td>142.00 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>165.64 (n/a)</td><td>162.20 (n/a)</td><td>116.70 (n/a)</td><td>36.80 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>168.34 (n/a)</td><td>160.10 (n/a)</td><td>124.30 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>158.30 (n/a)</td><td>165.40 (n/a)</td><td>119.50 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.40 (n/a)</td><td>199.76 (n/a)</td><td>180.60 (n/a)</td><td>152.80 (n/a)</td><td>57.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>159.46 (n/a)</td><td>152.90 (n/a)</td><td>134.30 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.40 (n/a)</td><td>202.56 (n/a)</td><td>198.60 (n/a)</td><td>179.00 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>179.56 (n/a)</td><td>189.90 (n/a)</td><td>140.60 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>184.70 (n/a)</td><td>174.90 (n/a)</td><td>163.20 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.90 (n/a)</td><td>176.14 (n/a)</td><td>174.90 (n/a)</td><td>146.10 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.20 (n/a)</td><td>184.50 (n/a)</td><td>187.40 (n/a)</td><td>141.50 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>251.40 (n/a)</td><td>199.74 (n/a)</td><td>188.20 (n/a)</td><td>180.60 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>190.72 (n/a)</td><td>193.00 (n/a)</td><td>152.40 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.60 (n/a)</td><td>169.92 (n/a)</td><td>156.20 (n/a)</td><td>142.60 (n/a)</td><td>41.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>199.10 (n/a)</td><td>188.70 (n/a)</td><td>172.00 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 <b>(+37.89%)</b></td><td>0.19 <b>(+20.13%)</b></td><td>0.19 <b>(+22.37%)</b></td><td>0.15 (-0.61%)</td><td>0.03 <b>(+410.86%)</b></td><td>225.00 (+0.63%)</td><td>181.10 (-14.74%)</td><td>174.30 (-18.28%)</td><td>145.30 <b>(-27.50%)</b></td><td>32.51 <b>(+275.49%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>212.40 (n/a)</td><td>213.30 (n/a)</td><td>200.40 (n/a)</td><td>8.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>172.28 (n/a)</td><td>179.80 (n/a)</td><td>140.60 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.10 (n/a)</td><td>178.14 (n/a)</td><td>181.60 (n/a)</td><td>136.80 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.00 (n/a)</td><td>170.12 (n/a)</td><td>164.00 (n/a)</td><td>148.80 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>211.70 (n/a)</td><td>175.40 (n/a)</td><td>168.40 (n/a)</td><td>152.40 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>198.90 (n/a)</td><td>174.34 (n/a)</td><td>181.70 (n/a)</td><td>129.70 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>191.90 (n/a)</td><td>167.98 (n/a)</td><td>163.40 (n/a)</td><td>144.50 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.10 (n/a)</td><td>188.26 (n/a)</td><td>191.80 (n/a)</td><td>137.90 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-12.63%)</td><td>0.02 (-2.07%)</td><td>0.02 (-0.77%)</td><td>0.02 (-16.42%)</td><td>0.01 (-9.79%)</td><td>252.50 (+19.61%)</td><td>178.16 (+2.59%)</td><td>172.00 (+0.82%)</td><td>140.90 (+14.46%)</td><td>44.34 <b>(+24.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>173.66 (n/a)</td><td>170.60 (n/a)</td><td>123.10 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-11.00%)</td><td>0.02 (-12.15%)</td><td>0.03 (-11.46%)</td><td>0.02 <b>(-25.76%)</b></td><td>0.00 <b>(+23.91%)</b></td><td>234.50 <b>(+34.69%)</b></td><td>173.92 (+15.67%)</td><td>163.40 (+13.00%)</td><td>147.50 (+12.42%)</td><td>35.24 <b>(+90.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.10 (n/a)</td><td>150.36 (n/a)</td><td>144.60 (n/a)</td><td>131.20 (n/a)</td><td>18.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (-14.94%)</td><td>0.02 (-6.75%)</td><td>0.02 (-8.72%)</td><td>0.02 (+7.89%)</td><td>0.00 <b>(-48.56%)</b></td><td>262.10 (-7.32%)</td><td>222.20 (+4.24%)</td><td>218.50 (+9.52%)</td><td>191.30 (+17.58%)</td><td>27.35 <b>(-44.01%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>282.80 (n/a)</td><td>213.16 (n/a)</td><td>199.50 (n/a)</td><td>162.70 (n/a)</td><td>48.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(+31.30%)</b></td><td>0.02 (-3.45%)</td><td>0.02 (-14.26%)</td><td>0.02 (-12.49%)</td><td>0.01 <b>(+190.33%)</b></td><td>238.60 (+14.27%)</td><td>205.62 (+7.90%)</td><td>220.90 (+16.63%)</td><td>131.00 <b>(-23.84%)</b></td><td>43.01 <b>(+141.90%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.80 (n/a)</td><td>190.56 (n/a)</td><td>189.40 (n/a)</td><td>172.00 (n/a)</td><td>17.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-5.36%)</td><td>0.02 (-5.59%)</td><td>0.03 (+6.60%)</td><td>0.02 <b>(-22.88%)</b></td><td>0.00 <b>(+34.94%)</b></td><td>226.80 <b>(+29.67%)</b></td><td>173.42 (+7.41%)</td><td>161.30 (-6.22%)</td><td>144.70 (+5.62%)</td><td>31.92 <b>(+88.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.90 (n/a)</td><td>161.46 (n/a)</td><td>172.00 (n/a)</td><td>137.00 (n/a)</td><td>16.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(+31.61%)</b></td><td>0.03 (+9.57%)</td><td>0.02 (+1.30%)</td><td>0.02 (-0.02%)</td><td>0.00 <b>(+295.44%)</b></td><td>184.90 (+0.05%)</td><td>164.84 (-7.04%)</td><td>176.10 (-1.29%)</td><td>125.10 <b>(-24.00%)</b></td><td>24.12 <b>(+196.54%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.80 (n/a)</td><td>177.32 (n/a)</td><td>178.40 (n/a)</td><td>164.60 (n/a)</td><td>8.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(+31.31%)</b></td><td>0.02 (+10.51%)</td><td>0.02 (-5.59%)</td><td>0.02 <b>(+20.85%)</b></td><td>0.01 <b>(+57.15%)</b></td><td>249.40 (-17.25%)</td><td>191.08 (-6.87%)</td><td>193.20 (+5.92%)</td><td>125.60 <b>(-23.88%)</b></td><td>57.76 (+1.40%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>301.40 (n/a)</td><td>205.18 (n/a)</td><td>182.40 (n/a)</td><td>165.00 (n/a)</td><td>56.96 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-4.67%)</td><td>0.03 (+1.94%)</td><td>0.02 (+4.79%)</td><td>0.02 (-10.38%)</td><td>0.00 (-6.39%)</td><td>199.90 (+11.55%)</td><td>161.90 (-1.84%)</td><td>166.30 (-4.54%)</td><td>127.50 (+4.94%)</td><td>27.04 (+10.21%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.20 (n/a)</td><td>164.94 (n/a)</td><td>174.20 (n/a)</td><td>121.50 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-12.62%)</td><td>0.02 (-9.73%)</td><td>0.02 (-11.34%)</td><td>0.02 (-4.35%)</td><td>0.00 <b>(-21.36%)</b></td><td>224.70 (+4.51%)</td><td>188.22 (+10.03%)</td><td>191.90 (+12.82%)</td><td>151.80 (+14.48%)</td><td>29.27 (-6.51%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>171.06 (n/a)</td><td>170.10 (n/a)</td><td>132.60 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(+50.89%)</b></td><td>0.03 <b>(+22.59%)</b></td><td>0.02 (+0.19%)</td><td>0.02 (+7.45%)</td><td>0.01 <b>(+182.33%)</b></td><td>216.80 (-6.91%)</td><td>170.20 (-15.42%)</td><td>186.20 (-0.21%)</td><td>120.90 <b>(-33.72%)</b></td><td>39.09 <b>(+72.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>201.22 (n/a)</td><td>186.60 (n/a)</td><td>182.40 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(+22.94%)</b></td><td>0.02 (-1.62%)</td><td>0.02 (-6.15%)</td><td>0.02 (-18.79%)</td><td>0.01 <b>(+99.94%)</b></td><td>262.60 <b>(+23.11%)</b></td><td>195.20 (+7.68%)</td><td>204.30 (+6.57%)</td><td>118.50 (-18.67%)</td><td>56.58 <b>(+99.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>181.28 (n/a)</td><td>191.70 (n/a)</td><td>145.70 (n/a)</td><td>28.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (+0.31%)</td><td>0.03 (+7.67%)</td><td>0.02 (+7.74%)</td><td>0.02 (+19.90%)</td><td>0.01 (-5.51%)</td><td>201.50 (-16.60%)</td><td>165.80 (-8.37%)</td><td>180.60 (-7.19%)</td><td>123.70 (-0.32%)</td><td>36.83 <b>(-21.01%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.60 (n/a)</td><td>180.94 (n/a)</td><td>194.60 (n/a)</td><td>124.10 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 <b>(-20.69%)</b></td><td>0.02 (-14.31%)</td><td>0.02 (-14.67%)</td><td>0.02 (-13.83%)</td><td>0.00 <b>(-29.91%)</b></td><td>239.20 (+16.06%)</td><td>199.72 (+16.04%)</td><td>192.60 (+17.15%)</td><td>176.30 <b>(+26.11%)</b></td><td>26.86 (-0.00%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>172.12 (n/a)</td><td>164.40 (n/a)</td><td>139.80 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(+37.67%)</b></td><td>0.03 (+6.55%)</td><td>0.02 (-1.05%)</td><td>0.02 (-14.89%)</td><td>0.01 <b>(+241.84%)</b></td><td>222.20 (+17.50%)</td><td>171.28 (-1.66%)</td><td>174.60 (+1.04%)</td><td>112.80 <b>(-27.37%)</b></td><td>41.02 <b>(+180.95%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.10 (n/a)</td><td>174.18 (n/a)</td><td>172.80 (n/a)</td><td>155.30 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-10.74%)</td><td>0.02 (+8.27%)</td><td>0.03 <b>(+20.21%)</b></td><td>0.02 <b>(+22.57%)</b></td><td>0.00 <b>(-31.03%)</b></td><td>217.20 (-18.41%)</td><td>177.10 (-9.89%)</td><td>161.00 (-16.80%)</td><td>154.20 (+12.06%)</td><td>28.93 <b>(-37.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>266.20 (n/a)</td><td>196.54 (n/a)</td><td>193.50 (n/a)</td><td>137.60 (n/a)</td><td>46.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (+3.75%)</td><td>0.02 (+6.14%)</td><td>0.02 (+8.43%)</td><td>0.02 (+15.39%)</td><td>0.00 <b>(-22.27%)</b></td><td>190.30 (-13.30%)</td><td>174.78 (-6.29%)</td><td>173.50 (-7.76%)</td><td>154.90 (-3.61%)</td><td>14.64 <b>(-34.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>186.52 (n/a)</td><td>188.10 (n/a)</td><td>160.70 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 <b>(+20.83%)</b></td><td>0.05 (+9.23%)</td><td>0.05 (-1.38%)</td><td>0.04 (-1.51%)</td><td>0.01 <b>(+111.80%)</b></td><td>188.60 (+1.51%)</td><td>157.50 (-7.09%)</td><td>163.50 (+1.43%)</td><td>130.10 (-17.24%)</td><td>24.98 <b>(+72.53%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.80 (n/a)</td><td>169.52 (n/a)</td><td>161.20 (n/a)</td><td>157.20 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (+17.27%)</td><td>0.05 (+7.89%)</td><td>0.06 (+12.63%)</td><td>0.04 (+3.17%)</td><td>0.01 <b>(+54.02%)</b></td><td>184.40 (-3.10%)</td><td>151.90 (-6.55%)</td><td>144.80 (-11.22%)</td><td>125.80 (-14.71%)</td><td>22.52 <b>(+29.11%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>162.54 (n/a)</td><td>163.10 (n/a)</td><td>147.50 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (-15.62%)</td><td>0.04 (-12.68%)</td><td>0.04 (-9.11%)</td><td>0.03 (-9.25%)</td><td>0.00 <b>(-58.70%)</b></td><td>239.40 (+10.17%)</td><td>229.12 (+14.00%)</td><td>230.00 (+10.00%)</td><td>216.00 (+18.55%)</td><td>9.17 <b>(-45.70%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.30 (n/a)</td><td>200.98 (n/a)</td><td>209.10 (n/a)</td><td>182.20 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (-12.73%)</td><td>0.04 (-6.03%)</td><td>0.04 (-1.13%)</td><td>0.03 (-7.97%)</td><td>0.01 (-16.02%)</td><td>257.30 (+8.66%)</td><td>210.88 (+6.14%)</td><td>196.10 (+1.13%)</td><td>174.70 (+14.56%)</td><td>35.03 (+5.46%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>198.68 (n/a)</td><td>193.90 (n/a)</td><td>152.50 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (-4.76%)</td><td>0.05 (-0.08%)</td><td>0.05 (+2.50%)</td><td>0.04 (+8.94%)</td><td>0.01 <b>(-31.21%)</b></td><td>207.00 (-8.20%)</td><td>171.08 (-1.34%)</td><td>159.00 (-2.45%)</td><td>152.40 (+4.96%)</td><td>22.26 <b>(-32.85%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>173.40 (n/a)</td><td>163.00 (n/a)</td><td>145.20 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (+9.61%)</td><td>0.06 (+8.18%)</td><td>0.06 (+15.21%)</td><td>0.05 (+13.19%)</td><td>0.01 (-6.85%)</td><td>170.50 (-11.66%)</td><td>139.58 (-8.46%)</td><td>141.80 (-13.22%)</td><td>107.30 (-8.76%)</td><td>23.82 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>152.48 (n/a)</td><td>163.40 (n/a)</td><td>117.60 (n/a)</td><td>31.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (+1.33%)</td><td>0.06 (+6.08%)</td><td>0.06 (+1.82%)</td><td>0.05 <b>(+50.62%)</b></td><td>0.01 <b>(-40.81%)</b></td><td>177.80 <b>(-33.61%)</b></td><td>146.94 (-11.18%)</td><td>145.20 (-1.83%)</td><td>118.00 (-1.26%)</td><td>21.38 <b>(-63.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>267.80 (n/a)</td><td>165.44 (n/a)</td><td>147.90 (n/a)</td><td>119.50 (n/a)</td><td>58.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (+12.42%)</td><td>0.06 (+5.39%)</td><td>0.06 (+2.97%)</td><td>0.04 (-13.00%)</td><td>0.01 <b>(+50.95%)</b></td><td>203.80 (+14.95%)</td><td>148.72 (-3.00%)</td><td>147.20 (-2.90%)</td><td>114.00 (-11.08%)</td><td>34.66 <b>(+53.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.30 (n/a)</td><td>153.32 (n/a)</td><td>151.60 (n/a)</td><td>128.20 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (-1.90%)</td><td>0.05 (-0.24%)</td><td>0.05 (-6.88%)</td><td>0.05 (+14.32%)</td><td>0.00 <b>(-37.68%)</b></td><td>177.60 (-12.51%)</td><td>163.70 (-0.63%)</td><td>168.40 (+7.40%)</td><td>149.20 (+1.91%)</td><td>12.15 <b>(-45.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>164.74 (n/a)</td><td>156.80 (n/a)</td><td>146.40 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (+9.87%)</td><td>0.05 (+4.57%)</td><td>0.05 (+4.37%)</td><td>0.05 (+4.03%)</td><td>0.01 <b>(+24.32%)</b></td><td>170.50 (-3.84%)</td><td>151.88 (-4.16%)</td><td>155.60 (-4.19%)</td><td>130.00 (-8.96%)</td><td>14.97 (+8.58%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>158.48 (n/a)</td><td>162.40 (n/a)</td><td>142.80 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-9.02%)</td><td>0.05 (+4.21%)</td><td>0.05 (+12.52%)</td><td>0.04 (+1.89%)</td><td>0.01 <b>(-25.80%)</b></td><td>198.30 (-1.83%)</td><td>158.50 (-4.83%)</td><td>150.10 (-11.13%)</td><td>144.00 (+9.92%)</td><td>22.46 (-17.68%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>166.54 (n/a)</td><td>168.90 (n/a)</td><td>131.00 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-8.33%)</td><td>0.05 (+15.74%)</td><td>0.05 <b>(+23.21%)</b></td><td>0.04 <b>(+28.87%)</b></td><td>0.00 <b>(-55.49%)</b></td><td>182.30 <b>(-22.39%)</b></td><td>159.00 (-16.67%)</td><td>151.30 (-18.83%)</td><td>146.80 (+9.14%)</td><td>15.50 <b>(-63.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>190.80 (n/a)</td><td>186.40 (n/a)</td><td>134.50 (n/a)</td><td>42.81 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+4.11%)</td><td>0.05 (+12.89%)</td><td>0.04 (+8.90%)</td><td>0.04 (+17.89%)</td><td>0.01 <b>(-21.10%)</b></td><td>207.10 (-15.16%)</td><td>183.60 (-12.36%)</td><td>191.20 (-8.17%)</td><td>154.10 (-3.93%)</td><td>21.21 <b>(-35.98%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>209.50 (n/a)</td><td>208.20 (n/a)</td><td>160.40 (n/a)</td><td>33.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-15.68%)</td><td>0.05 (+9.56%)</td><td>0.05 <b>(+20.50%)</b></td><td>0.04 (+5.87%)</td><td>0.01 <b>(-38.13%)</b></td><td>209.50 (-5.55%)</td><td>161.52 (-10.62%)</td><td>151.00 (-17.03%)</td><td>145.20 (+18.63%)</td><td>27.04 <b>(-25.92%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>180.72 (n/a)</td><td>182.00 (n/a)</td><td>122.40 (n/a)</td><td>36.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (-16.26%)</td><td>0.04 (-13.87%)</td><td>0.04 (-14.05%)</td><td>0.03 (-14.44%)</td><td>0.01 <b>(-30.14%)</b></td><td>245.90 (+16.87%)</td><td>197.00 (+14.84%)</td><td>189.80 (+16.30%)</td><td>159.40 (+19.40%)</td><td>33.29 (-4.21%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>171.54 (n/a)</td><td>163.20 (n/a)</td><td>133.50 (n/a)</td><td>34.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(-30.57%)</b></td><td>0.04 (-11.50%)</td><td>0.04 (-17.51%)</td><td>0.04 (+13.59%)</td><td>0.00 <b>(-85.37%)</b></td><td>197.80 (-11.97%)</td><td>192.18 (+8.19%)</td><td>197.40 <b>(+21.25%)</b></td><td>184.00 <b>(+43.97%)</b></td><td>7.42 <b>(-82.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>177.64 (n/a)</td><td>162.80 (n/a)</td><td>127.80 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 <b>(+20.33%)</b></td><td>0.10 (+3.01%)</td><td>0.10 (+0.59%)</td><td>0.08 (-7.26%)</td><td>0.01 <b>(+225.71%)</b></td><td>195.50 (+7.83%)</td><td>165.52 (-1.66%)</td><td>164.90 (-0.60%)</td><td>133.90 (-16.94%)</td><td>21.85 <b>(+185.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>181.30 (n/a)</td><td>168.32 (n/a)</td><td>165.90 (n/a)</td><td>161.20 (n/a)</td><td>7.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (-15.14%)</td><td>0.10 (-6.62%)</td><td>0.10 (-3.46%)</td><td>0.08 (-13.68%)</td><td>0.01 <b>(-21.32%)</b></td><td>209.90 (+15.84%)</td><td>170.30 (+6.74%)</td><td>169.40 (+3.55%)</td><td>146.50 (+17.86%)</td><td>25.11 (+6.82%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.20 (n/a)</td><td>159.54 (n/a)</td><td>163.60 (n/a)</td><td>124.30 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (-14.21%)</td><td>0.08 (-8.41%)</td><td>0.07 (-6.65%)</td><td>0.07 (+5.98%)</td><td>0.01 <b>(-37.50%)</b></td><td>233.20 (-5.66%)</td><td>205.96 (+6.57%)</td><td>219.90 (+7.16%)</td><td>159.70 (+16.57%)</td><td>30.14 <b>(-30.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.20 (n/a)</td><td>193.26 (n/a)</td><td>205.20 (n/a)</td><td>137.00 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 <b>(-24.37%)</b></td><td>0.08 (-11.88%)</td><td>0.08 (-6.62%)</td><td>0.07 (-4.93%)</td><td>0.01 <b>(-60.95%)</b></td><td>228.50 (+5.15%)</td><td>201.34 (+10.68%)</td><td>199.60 (+7.14%)</td><td>181.80 <b>(+32.22%)</b></td><td>18.71 <b>(-46.72%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>181.92 (n/a)</td><td>186.30 (n/a)</td><td>137.50 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+0.97%)</td><td>0.11 <b>(+34.53%)</b></td><td>0.11 <b>(+59.03%)</b></td><td>0.08 <b>(+69.68%)</b></td><td>0.02 <b>(-45.61%)</b></td><td>203.80 <b>(-41.06%)</b></td><td>157.78 <b>(-34.26%)</b></td><td>145.20 <b>(-37.09%)</b></td><td>129.90 (-0.99%)</td><td>30.31 <b>(-69.35%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>345.80 (n/a)</td><td>240.00 (n/a)</td><td>230.80 (n/a)</td><td>131.20 (n/a)</td><td>98.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 <b>(+29.66%)</b></td><td>0.11 <b>(+26.79%)</b></td><td>0.11 <b>(+29.87%)</b></td><td>0.08 (+3.11%)</td><td>0.02 <b>(+78.91%)</b></td><td>201.20 (-2.99%)</td><td>150.48 (-19.38%)</td><td>147.80 <b>(-22.98%)</b></td><td>112.30 <b>(-22.92%)</b></td><td>33.27 <b>(+39.01%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>186.66 (n/a)</td><td>191.90 (n/a)</td><td>145.70 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-7.79%)</td><td>0.10 (+2.65%)</td><td>0.10 (+8.11%)</td><td>0.09 <b>(+24.16%)</b></td><td>0.01 <b>(-54.86%)</b></td><td>185.00 (-19.46%)</td><td>159.88 (-5.90%)</td><td>159.20 (-7.50%)</td><td>140.20 (+8.43%)</td><td>16.28 <b>(-59.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.70 (n/a)</td><td>169.90 (n/a)</td><td>172.10 (n/a)</td><td>129.30 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 <b>(+28.43%)</b></td><td>0.12 (+14.29%)</td><td>0.11 (+7.24%)</td><td>0.10 <b>(+30.43%)</b></td><td>0.02 (+17.49%)</td><td>171.30 <b>(-23.32%)</b></td><td>146.10 (-12.97%)</td><td>145.10 (-6.75%)</td><td>106.90 <b>(-22.14%)</b></td><td>26.01 <b>(-28.50%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.40 (n/a)</td><td>167.88 (n/a)</td><td>155.60 (n/a)</td><td>137.30 (n/a)</td><td>36.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+7.57%)</td><td>0.09 (-2.01%)</td><td>0.09 (+0.49%)</td><td>0.08 (-6.37%)</td><td>0.02 <b>(+25.81%)</b></td><td>215.80 (+6.83%)</td><td>177.72 (+3.04%)</td><td>177.00 (-0.45%)</td><td>130.40 (-7.06%)</td><td>31.25 <b>(+22.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>172.48 (n/a)</td><td>177.80 (n/a)</td><td>140.30 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+9.23%)</td><td>0.10 (-5.14%)</td><td>0.10 (-1.18%)</td><td>0.08 (-16.10%)</td><td>0.02 <b>(+100.25%)</b></td><td>210.20 (+19.23%)</td><td>173.52 (+7.99%)</td><td>169.00 (+1.20%)</td><td>130.40 (-8.49%)</td><td>33.49 <b>(+125.01%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>160.68 (n/a)</td><td>167.00 (n/a)</td><td>142.50 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-17.56%)</td><td>0.10 (-1.32%)</td><td>0.10 (+6.33%)</td><td>0.08 (+14.43%)</td><td>0.01 <b>(-43.85%)</b></td><td>197.20 (-12.59%)</td><td>163.90 (-1.56%)</td><td>156.20 (-5.96%)</td><td>140.80 <b>(+21.27%)</b></td><td>23.46 <b>(-40.03%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.60 (n/a)</td><td>166.50 (n/a)</td><td>166.10 (n/a)</td><td>116.10 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-5.95%)</td><td>0.10 (-8.73%)</td><td>0.09 (-3.80%)</td><td>0.08 (-14.01%)</td><td>0.02 (-3.54%)</td><td>207.40 (+16.26%)</td><td>173.34 (+9.78%)</td><td>178.50 (+3.96%)</td><td>133.40 (+6.29%)</td><td>27.18 (+15.81%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.40 (n/a)</td><td>157.90 (n/a)</td><td>171.70 (n/a)</td><td>125.50 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.10 (-14.99%)</td><td>0.09 (-8.05%)</td><td>0.09 (-9.25%)</td><td>0.08 (-3.93%)</td><td>0.01 <b>(-40.23%)</b></td><td>211.00 (+4.09%)</td><td>182.56 (+7.60%)</td><td>177.70 (+10.17%)</td><td>162.50 (+17.67%)</td><td>18.93 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.70 (n/a)</td><td>169.66 (n/a)</td><td>161.30 (n/a)</td><td>138.10 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 <b>(+23.05%)</b></td><td>0.10 (+3.79%)</td><td>0.09 (-0.43%)</td><td>0.08 (-9.22%)</td><td>0.02 <b>(+119.81%)</b></td><td>217.20 (+10.20%)</td><td>173.82 (-1.17%)</td><td>177.90 (+0.45%)</td><td>123.90 (-18.70%)</td><td>33.63 <b>(+90.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>175.88 (n/a)</td><td>177.10 (n/a)</td><td>152.40 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-3.76%)</td><td>0.10 (-2.92%)</td><td>0.09 (-0.46%)</td><td>0.08 (-14.80%)</td><td>0.02 (+11.67%)</td><td>215.70 (+17.36%)</td><td>174.50 (+3.89%)</td><td>173.50 (+0.46%)</td><td>134.70 (+3.94%)</td><td>30.67 <b>(+37.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.80 (n/a)</td><td>167.96 (n/a)</td><td>172.70 (n/a)</td><td>129.60 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+3.88%)</td><td>0.10 (-9.20%)</td><td>0.10 (-7.58%)</td><td>0.07 (-13.07%)</td><td>0.02 (+17.01%)</td><td>231.10 (+15.03%)</td><td>170.06 (+11.57%)</td><td>163.30 (+8.15%)</td><td>124.50 (-3.71%)</td><td>38.44 <b>(+31.77%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.90 (n/a)</td><td>152.42 (n/a)</td><td>151.00 (n/a)</td><td>129.30 (n/a)</td><td>29.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (-13.33%)</td><td>0.20 (-3.26%)</td><td>0.19 (+0.30%)</td><td>0.16 (+3.07%)</td><td>0.03 <b>(-33.00%)</b></td><td>203.40 (-3.00%)</td><td>170.52 (+1.13%)</td><td>176.70 (-0.28%)</td><td>131.40 (+15.36%)</td><td>28.13 <b>(-24.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>209.70 (n/a)</td><td>168.62 (n/a)</td><td>177.20 (n/a)</td><td>113.90 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (+8.11%)</td><td>0.22 (+8.74%)</td><td>0.22 (+7.34%)</td><td>0.18 (+7.60%)</td><td>0.03 (-1.27%)</td><td>183.70 (-7.03%)</td><td>149.62 (-8.35%)</td><td>149.10 (-6.81%)</td><td>121.70 (-7.52%)</td><td>22.81 (-14.98%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.60 (n/a)</td><td>163.26 (n/a)</td><td>160.00 (n/a)</td><td>131.60 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 <b>(-23.17%)</b></td><td>0.14 (-8.88%)</td><td>0.14 (-8.02%)</td><td>0.13 <b>(+22.68%)</b></td><td>0.01 <b>(-81.14%)</b></td><td>250.00 (-18.46%)</td><td>235.42 (+5.84%)</td><td>235.70 (+8.72%)</td><td>221.90 <b>(+30.15%)</b></td><td>10.00 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>306.60 (n/a)</td><td>222.42 (n/a)</td><td>216.80 (n/a)</td><td>170.50 (n/a)</td><td>51.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (-14.20%)</td><td>0.18 (+2.37%)</td><td>0.19 (+16.98%)</td><td>0.15 (+8.48%)</td><td>0.02 <b>(-35.04%)</b></td><td>219.40 (-7.82%)</td><td>189.30 (-3.87%)</td><td>176.20 (-14.55%)</td><td>164.80 (+16.55%)</td><td>26.35 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.00 (n/a)</td><td>196.92 (n/a)</td><td>206.20 (n/a)</td><td>141.40 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (-14.88%)</td><td>0.19 (-2.09%)</td><td>0.19 (+4.99%)</td><td>0.16 (+11.44%)</td><td>0.03 <b>(-44.19%)</b></td><td>208.70 (-10.24%)</td><td>172.84 (-1.91%)</td><td>176.80 (-4.74%)</td><td>135.30 (+17.45%)</td><td>27.20 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>232.50 (n/a)</td><td>176.20 (n/a)</td><td>185.60 (n/a)</td><td>115.20 (n/a)</td><td>46.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (+16.15%)</td><td>0.20 (+12.17%)</td><td>0.19 (+5.24%)</td><td>0.16 (+13.17%)</td><td>0.03 <b>(+38.65%)</b></td><td>202.60 (-11.64%)</td><td>169.64 (-10.40%)</td><td>168.60 (-4.96%)</td><td>144.60 (-13.88%)</td><td>24.88 (+2.12%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.30 (n/a)</td><td>189.34 (n/a)</td><td>177.40 (n/a)</td><td>167.90 (n/a)</td><td>24.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (-15.04%)</td><td>0.20 (-1.45%)</td><td>0.19 (-4.20%)</td><td>0.17 (+6.61%)</td><td>0.02 <b>(-36.70%)</b></td><td>188.10 (-6.18%)</td><td>168.90 (+0.09%)</td><td>173.50 (+4.39%)</td><td>147.70 (+17.69%)</td><td>19.97 <b>(-29.01%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.50 (n/a)</td><td>168.74 (n/a)</td><td>166.20 (n/a)</td><td>125.50 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (-13.08%)</td><td>0.21 (-8.31%)</td><td>0.21 (-9.79%)</td><td>0.19 (+4.99%)</td><td>0.01 <b>(-58.52%)</b></td><td>170.80 (-4.74%)</td><td>155.58 (+7.53%)</td><td>152.80 (+10.80%)</td><td>143.40 (+15.00%)</td><td>10.16 <b>(-54.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>179.30 (n/a)</td><td>144.68 (n/a)</td><td>137.90 (n/a)</td><td>124.70 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (+2.42%)</td><td>0.22 (+5.87%)</td><td>0.19 (+7.07%)</td><td>0.18 (+19.39%)</td><td>0.04 (-12.24%)</td><td>182.70 (-16.23%)</td><td>156.08 (-7.02%)</td><td>169.10 (-6.63%)</td><td>117.80 (-2.40%)</td><td>29.05 <b>(-26.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.10 (n/a)</td><td>167.86 (n/a)</td><td>181.10 (n/a)</td><td>120.70 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (-10.62%)</td><td>0.21 (+3.45%)</td><td>0.21 (+6.29%)</td><td>0.19 (+13.02%)</td><td>0.01 <b>(-58.59%)</b></td><td>172.20 (-11.51%)</td><td>159.04 (-4.88%)</td><td>159.40 (-5.90%)</td><td>143.60 (+11.93%)</td><td>10.32 <b>(-58.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.60 (n/a)</td><td>167.20 (n/a)</td><td>169.40 (n/a)</td><td>128.30 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-10.83%)</td><td>0.20 (-4.83%)</td><td>0.20 (-6.53%)</td><td>0.19 (+5.12%)</td><td>0.01 <b>(-40.41%)</b></td><td>176.60 (-4.85%)</td><td>165.28 (+4.44%)</td><td>167.30 (+6.97%)</td><td>153.10 (+12.08%)</td><td>11.11 <b>(-37.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>158.26 (n/a)</td><td>156.40 (n/a)</td><td>136.60 (n/a)</td><td>17.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (+4.65%)</td><td>0.22 (-3.20%)</td><td>0.20 (-8.88%)</td><td>0.18 (-2.84%)</td><td>0.04 (+3.59%)</td><td>180.00 (+2.92%)</td><td>154.44 (+3.40%)</td><td>163.20 (+9.75%)</td><td>118.50 (-4.44%)</td><td>24.28 (+0.49%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>174.90 (n/a)</td><td>149.36 (n/a)</td><td>148.70 (n/a)</td><td>124.00 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 <b>(-26.72%)</b></td><td>0.20 (-4.27%)</td><td>0.20 (+5.16%)</td><td>0.19 (+8.18%)</td><td>0.01 <b>(-78.71%)</b></td><td>175.30 (-7.59%)</td><td>164.58 (+1.07%)</td><td>164.10 (-4.92%)</td><td>155.10 <b>(+36.41%)</b></td><td>8.36 <b>(-72.95%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>189.70 (n/a)</td><td>162.84 (n/a)</td><td>172.60 (n/a)</td><td>113.70 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (-17.03%)</td><td>0.19 (-1.35%)</td><td>0.18 (+1.01%)</td><td>0.16 (+6.48%)</td><td>0.02 <b>(-47.95%)</b></td><td>204.30 (-6.11%)</td><td>178.80 (-0.95%)</td><td>179.50 (-0.99%)</td><td>152.40 <b>(+20.57%)</b></td><td>20.82 <b>(-39.13%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.60 (n/a)</td><td>180.52 (n/a)</td><td>181.30 (n/a)</td><td>126.40 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (+11.32%)</td><td>0.19 (+12.59%)</td><td>0.19 (-2.01%)</td><td>0.15 (+19.78%)</td><td>0.03 (-11.90%)</td><td>218.50 (-16.51%)</td><td>172.88 (-12.67%)</td><td>176.20 (+2.09%)</td><td>139.60 (-10.17%)</td><td>30.26 <b>(-34.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>261.70 (n/a)</td><td>197.96 (n/a)</td><td>172.60 (n/a)</td><td>155.40 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 (-1.05%)</td><td>0.18 (-3.96%)</td><td>0.18 (+2.07%)</td><td>0.15 (-5.82%)</td><td>0.02 (+3.66%)</td><td>213.90 (+6.21%)</td><td>188.64 (+4.32%)</td><td>187.10 (-2.04%)</td><td>160.00 (+1.07%)</td><td>23.26 (+14.67%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>180.82 (n/a)</td><td>191.00 (n/a)</td><td>158.30 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-2.99%)</td><td>0.03 (-12.01%)</td><td>0.02 (-18.54%)</td><td>0.02 (-19.68%)</td><td>0.01 <b>(+63.85%)</b></td><td>205.30 <b>(+24.50%)</b></td><td>165.96 (+16.38%)</td><td>178.70 <b>(+22.82%)</b></td><td>125.40 (+3.04%)</td><td>33.06 <b>(+107.48%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.90 (n/a)</td><td>142.60 (n/a)</td><td>145.50 (n/a)</td><td>121.70 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+17.20%)</td><td>0.04 (+3.15%)</td><td>0.04 (+10.79%)</td><td>0.03 (-6.55%)</td><td>0.01 <b>(+103.29%)</b></td><td>214.00 (+7.00%)</td><td>168.02 (+0.01%)</td><td>152.10 (-9.73%)</td><td>123.80 (-14.68%)</td><td>38.70 <b>(+89.73%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>168.00 (n/a)</td><td>168.50 (n/a)</td><td>145.10 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-18.99%)</td><td>0.02 (-14.51%)</td><td>0.02 (-11.85%)</td><td>0.02 (-9.51%)</td><td>0.00 <b>(-23.96%)</b></td><td>215.60 (+10.51%)</td><td>182.56 (+16.46%)</td><td>171.90 (+13.39%)</td><td>158.30 <b>(+23.38%)</b></td><td>26.04 (+2.92%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>156.76 (n/a)</td><td>151.60 (n/a)</td><td>128.30 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-5.96%)</td><td>0.03 (+4.40%)</td><td>0.03 (+1.03%)</td><td>0.03 (+18.09%)</td><td>0.00 <b>(-27.33%)</b></td><td>195.10 (-15.32%)</td><td>172.82 (-5.56%)</td><td>172.90 (-1.03%)</td><td>150.50 (+6.29%)</td><td>22.00 <b>(-34.98%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>183.00 (n/a)</td><td>174.70 (n/a)</td><td>141.60 (n/a)</td><td>33.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (+14.77%)</td><td>0.03 (-0.98%)</td><td>0.03 (-8.33%)</td><td>0.02 (-2.92%)</td><td>0.01 <b>(+36.01%)</b></td><td>208.40 (+3.02%)</td><td>159.54 (+2.64%)</td><td>162.80 (+9.04%)</td><td>109.40 (-12.83%)</td><td>35.93 (+18.48%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>155.44 (n/a)</td><td>149.30 (n/a)</td><td>125.50 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (+7.69%)</td><td>0.04 <b>(+26.52%)</b></td><td>0.04 <b>(+34.28%)</b></td><td>0.03 (+19.69%)</td><td>0.00 (-13.49%)</td><td>170.30 (-16.48%)</td><td>135.02 <b>(-21.87%)</b></td><td>125.00 <b>(-25.51%)</b></td><td>122.00 (-7.15%)</td><td>20.35 <b>(-34.45%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>172.82 (n/a)</td><td>167.80 (n/a)</td><td>131.40 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-0.13%)</td><td>0.02 (-5.02%)</td><td>0.02 <b>(-20.76%)</b></td><td>0.02 (+16.77%)</td><td>0.00 <b>(-22.18%)</b></td><td>213.50 (-14.36%)</td><td>181.44 (+3.29%)</td><td>190.50 <b>(+26.24%)</b></td><td>148.70 (+0.07%)</td><td>28.59 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.30 (n/a)</td><td>175.66 (n/a)</td><td>150.90 (n/a)</td><td>148.60 (n/a)</td><td>43.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 <b>(+29.56%)</b></td><td>0.03 <b>(+20.67%)</b></td><td>0.03 <b>(+24.93%)</b></td><td>0.02 (-1.84%)</td><td>0.01 <b>(+145.58%)</b></td><td>213.30 (+1.86%)</td><td>166.16 (-14.89%)</td><td>160.50 (-19.99%)</td><td>127.90 <b>(-22.77%)</b></td><td>34.52 <b>(+94.72%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.40 (n/a)</td><td>195.22 (n/a)</td><td>200.60 (n/a)</td><td>165.60 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-2.40%)</td><td>0.02 (-7.42%)</td><td>0.02 (-13.08%)</td><td>0.02 (+5.29%)</td><td>0.00 <b>(-20.07%)</b></td><td>194.80 (-5.02%)</td><td>175.36 (+7.19%)</td><td>177.10 (+15.07%)</td><td>142.00 (+2.45%)</td><td>20.79 <b>(-23.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>163.60 (n/a)</td><td>153.90 (n/a)</td><td>138.60 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.04 (+14.46%)</td><td>0.03 (+7.07%)</td><td>0.03 (-1.67%)</td><td>0.03 <b>(+32.84%)</b></td><td>0.01 (-13.13%)</td><td>183.90 <b>(-24.72%)</b></td><td>158.90 (-9.73%)</td><td>170.20 (+1.73%)</td><td>109.40 (-12.62%)</td><td>29.52 <b>(-43.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>176.02 (n/a)</td><td>167.30 (n/a)</td><td>125.20 (n/a)</td><td>51.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-4.81%)</td><td>0.02 (-0.52%)</td><td>0.02 (-4.72%)</td><td>0.02 <b>(+30.73%)</b></td><td>0.00 <b>(-59.37%)</b></td><td>187.80 <b>(-23.50%)</b></td><td>176.88 (-2.07%)</td><td>183.40 (+4.92%)</td><td>159.80 (+5.06%)</td><td>12.44 <b>(-67.43%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.50 (n/a)</td><td>180.62 (n/a)</td><td>174.80 (n/a)</td><td>152.10 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (+1.26%)</td><td>0.02 (+0.28%)</td><td>0.02 (+11.69%)</td><td>0.02 (-17.53%)</td><td>0.00 <b>(+34.63%)</b></td><td>270.20 <b>(+21.27%)</b></td><td>202.96 (+1.60%)</td><td>190.10 (-10.50%)</td><td>158.20 (-1.25%)</td><td>44.23 <b>(+60.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>199.76 (n/a)</td><td>212.40 (n/a)</td><td>160.20 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 (-18.07%)</td><td>0.02 (-12.95%)</td><td>0.02 (-7.03%)</td><td>0.02 (-5.77%)</td><td>0.00 <b>(-42.54%)</b></td><td>217.90 (+6.14%)</td><td>185.52 (+12.14%)</td><td>188.70 (+7.58%)</td><td>153.50 <b>(+22.02%)</b></td><td>28.49 <b>(-23.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>165.44 (n/a)</td><td>175.40 (n/a)</td><td>125.80 (n/a)</td><td>37.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.03 <b>(-25.89%)</b></td><td>0.02 (-7.40%)</td><td>0.02 (-2.40%)</td><td>0.02 (+9.31%)</td><td>0.00 <b>(-50.81%)</b></td><td>229.90 (-8.52%)</td><td>198.26 (+3.37%)</td><td>205.40 (+2.44%)</td><td>155.80 <b>(+34.89%)</b></td><td>31.91 <b>(-34.60%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.30 (n/a)</td><td>191.80 (n/a)</td><td>200.50 (n/a)</td><td>115.50 (n/a)</td><td>48.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.02 (-12.43%)</td><td>0.02 (-10.62%)</td><td>0.02 (+0.64%)</td><td>0.01 <b>(-31.55%)</b></td><td>0.00 <b>(+26.01%)</b></td><td>325.50 <b>(+46.10%)</b></td><td>231.98 (+14.37%)</td><td>216.00 (-0.64%)</td><td>189.60 (+14.22%)</td><td>53.82 <b>(+117.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>202.84 (n/a)</td><td>217.40 (n/a)</td><td>166.00 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (+9.01%)</td><td>0.05 <b>(+20.81%)</b></td><td>0.06 <b>(+28.10%)</b></td><td>0.04 <b>(+53.62%)</b></td><td>0.01 (-11.09%)</td><td>225.40 <b>(-34.91%)</b></td><td>163.60 <b>(-21.03%)</b></td><td>140.30 <b>(-21.93%)</b></td><td>134.10 (-8.28%)</td><td>38.69 <b>(-51.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.30 (n/a)</td><td>207.18 (n/a)</td><td>179.70 (n/a)</td><td>146.20 (n/a)</td><td>79.33 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (-4.85%)</td><td>0.08 (+2.36%)</td><td>0.08 (+8.81%)</td><td>0.06 (+0.60%)</td><td>0.01 (-17.71%)</td><td>222.30 (-0.63%)</td><td>165.48 (-3.16%)</td><td>156.10 (-8.07%)</td><td>140.30 (+5.09%)</td><td>32.79 (-10.03%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>223.70 (n/a)</td><td>170.88 (n/a)</td><td>169.80 (n/a)</td><td>133.50 (n/a)</td><td>36.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (-0.84%)</td><td>0.05 (+18.19%)</td><td>0.05 (+16.49%)</td><td>0.04 <b>(+53.32%)</b></td><td>0.01 <b>(-21.57%)</b></td><td>213.10 <b>(-34.77%)</b></td><td>160.12 <b>(-20.44%)</b></td><td>159.90 (-14.17%)</td><td>116.70 (+0.78%)</td><td>38.64 <b>(-49.82%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>326.70 (n/a)</td><td>201.26 (n/a)</td><td>186.30 (n/a)</td><td>115.80 (n/a)</td><td>76.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (+4.25%)</td><td>0.06 (-8.27%)</td><td>0.05 (-13.67%)</td><td>0.04 (-10.19%)</td><td>0.01 <b>(+20.98%)</b></td><td>230.70 (+11.34%)</td><td>189.50 (+10.55%)</td><td>190.30 (+15.82%)</td><td>125.30 (-4.13%)</td><td>40.69 <b>(+21.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>171.42 (n/a)</td><td>164.30 (n/a)</td><td>130.70 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (+10.80%)</td><td>0.05 (+14.55%)</td><td>0.05 <b>(+20.87%)</b></td><td>0.04 <b>(+37.22%)</b></td><td>0.01 (-15.76%)</td><td>196.70 <b>(-27.15%)</b></td><td>166.62 (-14.82%)</td><td>159.40 (-17.28%)</td><td>129.10 (-9.78%)</td><td>27.36 <b>(-44.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.00 (n/a)</td><td>195.62 (n/a)</td><td>192.70 (n/a)</td><td>143.10 (n/a)</td><td>48.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.08 (+5.18%)</td><td>0.06 (+1.45%)</td><td>0.06 (+6.05%)</td><td>0.05 (-17.78%)</td><td>0.01 <b>(+54.99%)</b></td><td>224.10 <b>(+21.60%)</b></td><td>165.22 (+0.99%)</td><td>160.10 (-5.71%)</td><td>126.30 (-4.97%)</td><td>37.74 <b>(+81.50%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>163.60 (n/a)</td><td>169.80 (n/a)</td><td>132.90 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 <b>(-25.10%)</b></td><td>0.04 (-1.13%)</td><td>0.04 (+11.05%)</td><td>0.03 (+10.55%)</td><td>0.01 <b>(-56.34%)</b></td><td>243.90 (-9.57%)</td><td>191.26 (-4.00%)</td><td>185.10 (-9.97%)</td><td>163.70 <b>(+33.52%)</b></td><td>30.79 <b>(-43.84%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.70 (n/a)</td><td>199.22 (n/a)</td><td>205.60 (n/a)</td><td>122.60 (n/a)</td><td>54.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-16.23%)</td><td>0.05 (-9.59%)</td><td>0.06 (+3.52%)</td><td>0.04 (-2.04%)</td><td>0.01 <b>(-35.59%)</b></td><td>224.20 (+2.09%)</td><td>177.76 (+8.42%)</td><td>161.10 (-3.42%)</td><td>151.70 (+19.35%)</td><td>31.40 (-18.66%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>163.96 (n/a)</td><td>166.80 (n/a)</td><td>127.10 (n/a)</td><td>38.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 <b>(+20.98%)</b></td><td>0.05 (+8.99%)</td><td>0.04 (+3.26%)</td><td>0.04 (+10.31%)</td><td>0.01 <b>(+59.47%)</b></td><td>206.00 (-9.37%)</td><td>177.92 (-7.02%)</td><td>190.30 (-3.16%)</td><td>130.10 (-17.34%)</td><td>31.01 (+19.35%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>191.36 (n/a)</td><td>196.50 (n/a)</td><td>157.40 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 (+5.50%)</td><td>0.06 (-7.30%)</td><td>0.05 (-16.19%)</td><td>0.05 (-15.02%)</td><td>0.01 <b>(+147.36%)</b></td><td>186.00 (+17.65%)</td><td>162.56 (+10.36%)</td><td>179.90 (+19.30%)</td><td>125.30 (-5.22%)</td><td>28.34 <b>(+182.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>158.10 (n/a)</td><td>147.30 (n/a)</td><td>150.80 (n/a)</td><td>132.20 (n/a)</td><td>10.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-4.44%)</td><td>0.05 (+10.17%)</td><td>0.05 (+14.25%)</td><td>0.04 <b>(+20.48%)</b></td><td>0.01 <b>(-38.65%)</b></td><td>203.30 (-16.99%)</td><td>175.94 (-11.55%)</td><td>178.10 (-12.48%)</td><td>142.30 (+4.63%)</td><td>21.79 <b>(-45.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.90 (n/a)</td><td>198.92 (n/a)</td><td>203.50 (n/a)</td><td>136.00 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 (-14.76%)</td><td>0.05 (-7.84%)</td><td>0.05 (+5.05%)</td><td>0.02 <b>(-40.61%)</b></td><td>0.01 (+19.34%)</td><td>380.40 <b>(+68.39%)</b></td><td>214.14 (+16.70%)</td><td>175.90 (-4.76%)</td><td>150.00 (+17.37%)</td><td>95.10 <b>(+150.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>183.50 (n/a)</td><td>184.70 (n/a)</td><td>127.80 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.07 <b>(+30.54%)</b></td><td>0.05 (+4.93%)</td><td>0.04 (-6.57%)</td><td>0.03 (-6.13%)</td><td>0.01 <b>(+84.16%)</b></td><td>238.30 (+6.53%)</td><td>181.34 (-1.39%)</td><td>182.80 (+7.03%)</td><td>120.90 <b>(-23.38%)</b></td><td>45.18 <b>(+50.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>183.90 (n/a)</td><td>170.80 (n/a)</td><td>157.80 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.06 <b>(+20.14%)</b></td><td>0.05 <b>(+27.73%)</b></td><td>0.05 <b>(+30.22%)</b></td><td>0.04 <b>(+29.01%)</b></td><td>0.01 (+19.02%)</td><td>199.90 <b>(-22.49%)</b></td><td>173.70 <b>(-21.79%)</b></td><td>179.60 <b>(-23.18%)</b></td><td>142.00 (-16.76%)</td><td>26.00 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>222.10 (n/a)</td><td>233.80 (n/a)</td><td>170.60 (n/a)</td><td>32.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.05 (+7.02%)</td><td>0.04 (+4.43%)</td><td>0.04 (-1.23%)</td><td>0.03 (-5.38%)</td><td>0.01 <b>(+61.91%)</b></td><td>239.50 (+5.69%)</td><td>199.04 (-3.17%)</td><td>203.90 (+1.24%)</td><td>167.10 (-6.54%)</td><td>30.23 <b>(+54.72%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.60 (n/a)</td><td>205.56 (n/a)</td><td>201.40 (n/a)</td><td>178.80 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (+7.72%)</td><td>0.11 (+12.09%)</td><td>0.10 (+0.40%)</td><td>0.08 (+7.01%)</td><td>0.03 (+18.86%)</td><td>210.00 (-6.54%)</td><td>158.54 (-10.25%)</td><td>167.70 (-0.36%)</td><td>119.70 (-7.21%)</td><td>37.86 (-2.94%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.70 (n/a)</td><td>176.64 (n/a)</td><td>168.30 (n/a)</td><td>129.00 (n/a)</td><td>39.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-2.30%)</td><td>0.16 (+8.47%)</td><td>0.18 <b>(+23.97%)</b></td><td>0.11 (+13.45%)</td><td>0.04 <b>(-22.07%)</b></td><td>217.10 (-11.86%)</td><td>156.30 (-10.81%)</td><td>137.40 (-19.32%)</td><td>118.60 (+2.33%)</td><td>38.91 <b>(-27.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>246.30 (n/a)</td><td>175.24 (n/a)</td><td>170.30 (n/a)</td><td>115.90 (n/a)</td><td>54.01 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+5.45%)</td><td>0.10 (-3.62%)</td><td>0.10 (-8.38%)</td><td>0.08 (+1.40%)</td><td>0.02 (+1.67%)</td><td>206.40 (-1.39%)</td><td>167.40 (+3.59%)</td><td>167.30 (+9.13%)</td><td>123.00 (-5.17%)</td><td>31.17 (-5.72%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>161.60 (n/a)</td><td>153.30 (n/a)</td><td>129.70 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 <b>(+59.63%)</b></td><td>0.15 <b>(+37.76%)</b></td><td>0.14 <b>(+38.00%)</b></td><td>0.12 <b>(+26.31%)</b></td><td>0.03 <b>(+199.91%)</b></td><td>175.30 <b>(-20.86%)</b></td><td>145.78 <b>(-25.40%)</b></td><td>141.50 <b>(-27.51%)</b></td><td>105.70 <b>(-37.38%)</b></td><td>29.46 <b>(+53.75%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>195.42 (n/a)</td><td>195.20 (n/a)</td><td>168.80 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 <b>(+33.74%)</b></td><td>0.10 (+15.12%)</td><td>0.10 (+14.53%)</td><td>0.07 (-2.30%)</td><td>0.02 <b>(+145.71%)</b></td><td>218.60 (+2.34%)</td><td>168.30 (-10.76%)</td><td>162.00 (-12.72%)</td><td>124.30 <b>(-25.26%)</b></td><td>35.03 <b>(+87.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>188.60 (n/a)</td><td>185.60 (n/a)</td><td>166.30 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 <b>(+24.09%)</b></td><td>0.12 (+7.54%)</td><td>0.11 (-5.30%)</td><td>0.09 (-3.81%)</td><td>0.03 <b>(+153.25%)</b></td><td>218.40 (+3.95%)</td><td>172.48 (-3.87%)</td><td>181.50 (+5.65%)</td><td>129.70 (-19.44%)</td><td>38.31 <b>(+103.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>179.42 (n/a)</td><td>171.80 (n/a)</td><td>161.00 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 <b>(+25.02%)</b></td><td>0.10 (+15.59%)</td><td>0.10 <b>(+24.61%)</b></td><td>0.07 (-16.49%)</td><td>0.02 <b>(+120.01%)</b></td><td>247.40 (+19.75%)</td><td>169.24 (-10.24%)</td><td>158.50 (-19.75%)</td><td>130.50 (-19.99%)</td><td>45.40 <b>(+120.71%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>188.54 (n/a)</td><td>197.50 (n/a)</td><td>163.10 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (+15.51%)</td><td>0.13 <b>(+29.12%)</b></td><td>0.14 <b>(+47.00%)</b></td><td>0.10 <b>(+21.87%)</b></td><td>0.02 (-12.58%)</td><td>176.30 (-17.96%)</td><td>141.78 <b>(-23.36%)</b></td><td>132.40 <b>(-31.96%)</b></td><td>129.40 (-13.39%)</td><td>19.58 <b>(-36.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>185.00 (n/a)</td><td>194.60 (n/a)</td><td>149.40 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (+4.47%)</td><td>0.08 (-9.06%)</td><td>0.08 (-8.22%)</td><td>0.04 <b>(-44.96%)</b></td><td>0.03 <b>(+136.44%)</b></td><td>383.00 <b>(+81.69%)</b></td><td>234.68 <b>(+24.41%)</b></td><td>214.60 (+8.99%)</td><td>140.70 (-4.29%)</td><td>100.52 <b>(+310.25%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>188.64 (n/a)</td><td>196.90 (n/a)</td><td>147.00 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-4.77%)</td><td>0.11 (-3.69%)</td><td>0.11 (-2.66%)</td><td>0.10 (-6.68%)</td><td>0.01 (-5.43%)</td><td>193.70 (+7.19%)</td><td>165.12 (+3.82%)</td><td>160.60 (+2.69%)</td><td>147.50 (+4.98%)</td><td>18.21 (+7.28%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>159.04 (n/a)</td><td>156.40 (n/a)</td><td>140.50 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (+6.69%)</td><td>0.09 (+9.77%)</td><td>0.09 (+7.04%)</td><td>0.07 (-2.86%)</td><td>0.02 <b>(+26.36%)</b></td><td>228.70 (+2.93%)</td><td>178.20 (-8.12%)</td><td>180.10 (-6.54%)</td><td>145.10 (-6.33%)</td><td>32.56 <b>(+21.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>193.94 (n/a)</td><td>192.70 (n/a)</td><td>154.90 (n/a)</td><td>26.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-7.36%)</td><td>0.10 (-0.73%)</td><td>0.10 (+2.23%)</td><td>0.08 (+6.81%)</td><td>0.02 <b>(-24.47%)</b></td><td>212.70 (-6.38%)</td><td>176.48 (-0.75%)</td><td>173.40 (-2.14%)</td><td>139.50 (+7.97%)</td><td>28.58 <b>(-22.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>177.82 (n/a)</td><td>177.20 (n/a)</td><td>129.20 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (+19.34%)</td><td>0.09 (+6.91%)</td><td>0.09 (+7.13%)</td><td>0.07 (-7.14%)</td><td>0.02 <b>(+192.74%)</b></td><td>226.50 (+7.70%)</td><td>187.68 (-4.45%)</td><td>187.10 (-6.68%)</td><td>150.70 (-16.23%)</td><td>32.69 <b>(+165.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>196.42 (n/a)</td><td>200.50 (n/a)</td><td>179.90 (n/a)</td><td>12.33 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+18.21%)</td><td>0.09 (+10.66%)</td><td>0.09 (+2.34%)</td><td>0.07 <b>(+53.82%)</b></td><td>0.02 (-11.85%)</td><td>236.90 <b>(-35.01%)</b></td><td>192.32 (-13.94%)</td><td>188.70 (-2.28%)</td><td>136.40 (-15.44%)</td><td>39.12 <b>(-52.83%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>364.50 (n/a)</td><td>223.48 (n/a)</td><td>193.10 (n/a)</td><td>161.30 (n/a)</td><td>82.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.09 (+16.27%)</td><td>0.08 (+13.73%)</td><td>0.09 (+14.25%)</td><td>0.07 (-1.25%)</td><td>0.01 <b>(+116.57%)</b></td><td>242.80 (+1.29%)</td><td>196.72 (-11.12%)</td><td>191.10 (-12.50%)</td><td>175.00 (-13.96%)</td><td>27.85 <b>(+87.70%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>239.70 (n/a)</td><td>221.32 (n/a)</td><td>218.40 (n/a)</td><td>203.40 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 (+0.30%)</td><td>0.20 (+8.69%)</td><td>0.20 (+17.59%)</td><td>0.17 (+5.33%)</td><td>0.02 (-15.47%)</td><td>188.60 (-5.08%)</td><td>166.26 (-8.39%)</td><td>160.30 (-14.96%)</td><td>144.80 (-0.34%)</td><td>17.80 (-18.49%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>198.70 (n/a)</td><td>181.48 (n/a)</td><td>188.50 (n/a)</td><td>145.30 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (+11.60%)</td><td>0.23 (+13.28%)</td><td>0.23 (+13.20%)</td><td>0.19 (+10.59%)</td><td>0.03 (-0.78%)</td><td>176.10 (-9.60%)</td><td>144.02 (-12.09%)</td><td>142.10 (-11.68%)</td><td>121.20 (-10.36%)</td><td>20.90 (-19.34%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.80 (n/a)</td><td>163.82 (n/a)</td><td>160.90 (n/a)</td><td>135.20 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (-8.80%)</td><td>0.22 (-9.93%)</td><td>0.23 (-4.02%)</td><td>0.18 (-16.01%)</td><td>0.03 <b>(+20.48%)</b></td><td>224.40 (+19.05%)</td><td>187.50 (+11.78%)</td><td>179.50 (+4.18%)</td><td>160.70 (+9.69%)</td><td>25.49 <b>(+58.87%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>188.50 (n/a)</td><td>167.74 (n/a)</td><td>172.30 (n/a)</td><td>146.50 (n/a)</td><td>16.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-12.77%)</td><td>0.19 (+11.35%)</td><td>0.18 (+8.58%)</td><td>0.18 <b>(+74.40%)</b></td><td>0.02 <b>(-68.31%)</b></td><td>184.10 <b>(-42.65%)</b></td><td>171.30 (-16.62%)</td><td>177.20 (-7.90%)</td><td>156.00 (+14.71%)</td><td>13.98 <b>(-80.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>321.00 (n/a)</td><td>205.44 (n/a)</td><td>192.40 (n/a)</td><td>136.00 (n/a)</td><td>70.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.28 (-4.87%)</td><td>0.24 (-1.14%)</td><td>0.23 (-1.77%)</td><td>0.19 (-8.85%)</td><td>0.04 (-0.47%)</td><td>219.80 (+9.74%)</td><td>176.42 (+1.39%)</td><td>176.80 (+1.84%)</td><td>145.90 (+5.12%)</td><td>28.87 (+13.29%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>200.30 (n/a)</td><td>174.00 (n/a)</td><td>173.60 (n/a)</td><td>138.80 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-10.90%)</td><td>0.19 (-5.68%)</td><td>0.20 (-2.59%)</td><td>0.15 (-13.07%)</td><td>0.03 (+3.13%)</td><td>219.10 (+15.01%)</td><td>171.34 (+6.53%)</td><td>162.10 (+2.66%)</td><td>153.40 (+12.22%)</td><td>27.24 <b>(+34.76%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>190.50 (n/a)</td><td>160.84 (n/a)</td><td>157.90 (n/a)</td><td>136.70 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (+19.80%)</td><td>0.21 (+17.85%)</td><td>0.22 <b>(+26.44%)</b></td><td>0.16 (+9.00%)</td><td>0.04 <b>(+41.00%)</b></td><td>229.40 (-8.28%)</td><td>178.36 (-14.13%)</td><td>164.40 <b>(-20.89%)</b></td><td>141.00 (-16.52%)</td><td>37.70 (+9.21%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>250.10 (n/a)</td><td>207.72 (n/a)</td><td>207.80 (n/a)</td><td>168.90 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (+17.90%)</td><td>0.19 (+0.33%)</td><td>0.18 (-0.42%)</td><td>0.14 (-16.99%)</td><td>0.04 <b>(+149.67%)</b></td><td>227.00 <b>(+20.49%)</b></td><td>180.48 (+2.45%)</td><td>180.80 (+0.39%)</td><td>129.20 (-15.17%)</td><td>34.88 <b>(+152.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.40 (n/a)</td><td>176.16 (n/a)</td><td>180.10 (n/a)</td><td>152.30 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.23 <b>(-23.51%)</b></td><td>0.20 (-14.84%)</td><td>0.20 (-9.40%)</td><td>0.15 (-11.68%)</td><td>0.03 <b>(-34.47%)</b></td><td>238.30 (+13.21%)</td><td>191.98 (+16.22%)</td><td>180.70 (+10.38%)</td><td>159.40 <b>(+30.76%)</b></td><td>31.44 (-0.96%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>210.50 (n/a)</td><td>165.18 (n/a)</td><td>163.70 (n/a)</td><td>121.90 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.22 (+8.32%)</td><td>0.19 (+3.13%)</td><td>0.20 (+4.16%)</td><td>0.16 (+0.74%)</td><td>0.03 <b>(+45.44%)</b></td><td>209.20 (-0.71%)</td><td>175.20 (-2.01%)</td><td>162.10 (-4.03%)</td><td>145.80 (-7.66%)</td><td>29.01 <b>(+35.47%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>178.80 (n/a)</td><td>168.90 (n/a)</td><td>157.90 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (+5.58%)</td><td>0.19 (-3.00%)</td><td>0.17 (-10.76%)</td><td>0.15 (-4.75%)</td><td>0.04 <b>(+34.08%)</b></td><td>225.80 (+4.97%)</td><td>191.46 (+4.52%)</td><td>206.10 (+12.01%)</td><td>147.40 (-5.33%)</td><td>36.51 <b>(+35.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>215.10 (n/a)</td><td>183.18 (n/a)</td><td>184.00 (n/a)</td><td>155.70 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-6.66%)</td><td>0.18 (-5.86%)</td><td>0.18 (+6.66%)</td><td>0.15 (-7.05%)</td><td>0.02 <b>(-33.17%)</b></td><td>220.20 (+7.57%)</td><td>186.92 (+5.00%)</td><td>183.90 (-6.22%)</td><td>155.20 (+7.18%)</td><td>23.52 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.70 (n/a)</td><td>178.02 (n/a)</td><td>196.10 (n/a)</td><td>144.80 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (-14.28%)</td><td>0.16 (-16.67%)</td><td>0.17 (-16.96%)</td><td>0.11 (-4.07%)</td><td>0.03 <b>(-29.09%)</b></td><td>327.30 (+4.24%)</td><td>225.56 (+16.81%)</td><td>205.60 <b>(+20.45%)</b></td><td>179.20 (+16.67%)</td><td>59.04 (-13.29%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>314.00 (n/a)</td><td>193.10 (n/a)</td><td>170.70 (n/a)</td><td>153.60 (n/a)</td><td>68.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 <b>(+39.97%)</b></td><td>0.16 (+2.29%)</td><td>0.15 (-1.87%)</td><td>0.09 <b>(-37.13%)</b></td><td>0.06 <b>(+237.28%)</b></td><td>377.20 <b>(+59.09%)</b></td><td>230.40 (+8.93%)</td><td>224.30 (+1.91%)</td><td>131.80 <b>(-28.56%)</b></td><td>91.85 <b>(+293.52%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.10 (n/a)</td><td>211.52 (n/a)</td><td>220.10 (n/a)</td><td>184.50 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (-6.71%)</td><td>0.15 (+15.56%)</td><td>0.15 <b>(+27.14%)</b></td><td>0.11 (+8.41%)</td><td>0.02 <b>(-29.22%)</b></td><td>179.60 (-7.76%)</td><td>141.32 (-14.85%)</td><td>132.20 <b>(-21.36%)</b></td><td>126.50 (+7.20%)</td><td>22.07 <b>(-28.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>194.70 (n/a)</td><td>165.96 (n/a)</td><td>168.10 (n/a)</td><td>118.00 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (-10.24%)</td><td>0.13 <b>(+25.26%)</b></td><td>0.13 <b>(+57.36%)</b></td><td>0.10 <b>(+33.36%)</b></td><td>0.02 <b>(-52.25%)</b></td><td>203.30 <b>(-25.01%)</b></td><td>161.38 <b>(-24.50%)</b></td><td>152.50 <b>(-36.43%)</b></td><td>144.80 (+11.38%)</td><td>23.70 <b>(-58.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>271.10 (n/a)</td><td>213.76 (n/a)</td><td>239.90 (n/a)</td><td>130.00 (n/a)</td><td>56.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (+0.31%)</td><td>0.12 (+3.39%)</td><td>0.13 (+10.51%)</td><td>0.09 (+10.77%)</td><td>0.02 (-8.70%)</td><td>221.40 (-9.71%)</td><td>175.78 (-4.17%)</td><td>162.60 (-9.52%)</td><td>137.80 (-0.29%)</td><td>35.75 (-15.96%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>245.20 (n/a)</td><td>183.42 (n/a)</td><td>179.70 (n/a)</td><td>138.20 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-19.22%)</td><td>0.10 <b>(-21.65%)</b></td><td>0.11 (-13.63%)</td><td>0.07 <b>(-22.71%)</b></td><td>0.02 (-6.45%)</td><td>290.30 <b>(+29.37%)</b></td><td>216.96 <b>(+29.48%)</b></td><td>183.50 (+15.77%)</td><td>169.50 <b>(+23.81%)</b></td><td>55.49 <b>(+52.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>167.56 (n/a)</td><td>158.50 (n/a)</td><td>136.90 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (-9.03%)</td><td>0.11 (+3.13%)</td><td>0.11 (-9.70%)</td><td>0.10 <b>(+91.22%)</b></td><td>0.01 <b>(-68.91%)</b></td><td>200.40 <b>(-47.69%)</b></td><td>180.32 (-14.49%)</td><td>180.60 (+10.73%)</td><td>155.30 (+9.91%)</td><td>17.71 <b>(-82.42%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>383.10 (n/a)</td><td>210.88 (n/a)</td><td>163.10 (n/a)</td><td>141.30 (n/a)</td><td>100.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (+6.78%)</td><td>0.13 (+3.32%)</td><td>0.12 (-2.26%)</td><td>0.11 <b>(+24.33%)</b></td><td>0.02 (-14.97%)</td><td>193.00 (-19.58%)</td><td>166.08 (-4.91%)</td><td>165.90 (+2.28%)</td><td>128.50 (-6.34%)</td><td>26.02 <b>(-36.41%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>240.00 (n/a)</td><td>174.66 (n/a)</td><td>162.20 (n/a)</td><td>137.20 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.16 (+2.64%)</td><td>0.13 (+5.51%)</td><td>0.12 (+9.27%)</td><td>0.11 (+5.82%)</td><td>0.02 (+1.85%)</td><td>189.70 (-5.48%)</td><td>166.20 (-5.20%)</td><td>164.10 (-8.48%)</td><td>131.30 (-2.52%)</td><td>24.24 (-1.73%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>200.70 (n/a)</td><td>175.32 (n/a)</td><td>179.30 (n/a)</td><td>134.70 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (-5.00%)</td><td>0.10 (-16.96%)</td><td>0.10 (-15.57%)</td><td>0.06 <b>(-33.32%)</b></td><td>0.03 <b>(+81.62%)</b></td><td>321.80 <b>(+49.95%)</b></td><td>219.24 <b>(+27.49%)</b></td><td>196.10 (+18.42%)</td><td>160.50 (+5.31%)</td><td>69.03 <b>(+174.73%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>171.96 (n/a)</td><td>165.60 (n/a)</td><td>152.40 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (+4.30%)</td><td>0.17 (+15.50%)</td><td>0.18 (+18.51%)</td><td>0.13 (+18.49%)</td><td>0.03 (-4.74%)</td><td>189.20 (-15.61%)</td><td>149.14 (-14.05%)</td><td>140.20 (-15.59%)</td><td>127.80 (-4.13%)</td><td>25.19 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>224.20 (n/a)</td><td>173.52 (n/a)</td><td>166.10 (n/a)</td><td>133.30 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 (+1.82%)</td><td>0.15 (+1.64%)</td><td>0.14 (-4.94%)</td><td>0.12 (+5.98%)</td><td>0.03 (+13.36%)</td><td>197.70 (-5.63%)</td><td>167.86 (-1.18%)</td><td>180.00 (+5.20%)</td><td>131.20 (-1.80%)</td><td>29.78 (+5.08%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>209.50 (n/a)</td><td>169.86 (n/a)</td><td>171.10 (n/a)</td><td>133.60 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (+17.19%)</td><td>0.16 <b>(+30.05%)</b></td><td>0.19 <b>(+52.47%)</b></td><td>0.09 (+11.31%)</td><td>0.05 <b>(+46.43%)</b></td><td>262.40 (-10.17%)</td><td>164.08 <b>(-20.35%)</b></td><td>126.20 <b>(-34.44%)</b></td><td>118.40 (-14.70%)</td><td>61.96 (+9.07%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>292.10 (n/a)</td><td>206.00 (n/a)</td><td>192.50 (n/a)</td><td>138.80 (n/a)</td><td>56.81 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.19 <b>(+39.64%)</b></td><td>0.15 <b>(+36.88%)</b></td><td>0.14 <b>(+25.01%)</b></td><td>0.12 <b>(+42.06%)</b></td><td>0.04 <b>(+81.28%)</b></td><td>206.10 <b>(-29.59%)</b></td><td>168.56 <b>(-25.79%)</b></td><td>180.00 <b>(-20.00%)</b></td><td>128.30 <b>(-28.40%)</b></td><td>37.07 (-11.95%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>292.70 (n/a)</td><td>227.14 (n/a)</td><td>225.00 (n/a)</td><td>179.20 (n/a)</td><td>42.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.20 <b>(+33.97%)</b></td><td>0.14 (+0.94%)</td><td>0.14 (-6.36%)</td><td>0.10 <b>(-22.75%)</b></td><td>0.04 <b>(+271.65%)</b></td><td>253.10 <b>(+29.40%)</b></td><td>181.10 (+4.07%)</td><td>179.60 (+6.78%)</td><td>122.40 <b>(-25.37%)</b></td><td>46.99 <b>(+257.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>174.02 (n/a)</td><td>168.20 (n/a)</td><td>164.00 (n/a)</td><td>13.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 (+9.74%)</td><td>0.16 (+11.68%)</td><td>0.16 (+5.32%)</td><td>0.15 <b>(+31.40%)</b></td><td>0.01 <b>(-40.41%)</b></td><td>167.80 <b>(-23.90%)</b></td><td>151.82 (-11.64%)</td><td>152.90 (-5.03%)</td><td>138.60 (-8.88%)</td><td>11.10 <b>(-59.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>171.82 (n/a)</td><td>161.00 (n/a)</td><td>152.10 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (-1.89%)</td><td>0.13 (-2.18%)</td><td>0.14 (-2.88%)</td><td>0.10 (-7.76%)</td><td>0.02 (+5.36%)</td><td>242.70 (+8.45%)</td><td>192.84 (+2.63%)</td><td>178.90 (+2.99%)</td><td>163.70 (+1.93%)</td><td>34.35 (+13.94%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>223.80 (n/a)</td><td>187.90 (n/a)</td><td>173.70 (n/a)</td><td>160.60 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.18 <b>(-23.10%)</b></td><td>0.14 (-15.74%)</td><td>0.14 (-13.07%)</td><td>0.10 <b>(-24.07%)</b></td><td>0.03 <b>(-28.16%)</b></td><td>247.10 <b>(+31.65%)</b></td><td>184.86 (+18.35%)</td><td>180.80 (+15.09%)</td><td>139.20 <b>(+30.09%)</b></td><td>39.58 <b>(+29.31%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>187.70 (n/a)</td><td>156.20 (n/a)</td><td>157.10 (n/a)</td><td>107.00 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (+1.24%)</td><td>0.12 (+6.83%)</td><td>0.12 (+8.03%)</td><td>0.08 (-12.83%)</td><td>0.03 <b>(+31.66%)</b></td><td>234.90 (+14.75%)</td><td>162.30 (-4.18%)</td><td>154.30 (-7.44%)</td><td>128.00 (-1.23%)</td><td>43.28 <b>(+50.99%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>169.38 (n/a)</td><td>166.70 (n/a)</td><td>129.60 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+2.52%)</td><td>0.10 (-6.18%)</td><td>0.10 (-8.93%)</td><td>0.07 <b>(-20.48%)</b></td><td>0.02 <b>(+30.34%)</b></td><td>252.60 <b>(+25.73%)</b></td><td>184.02 (+8.64%)</td><td>178.60 (+9.77%)</td><td>139.30 (-2.52%)</td><td>42.00 <b>(+63.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>200.90 (n/a)</td><td>169.38 (n/a)</td><td>162.70 (n/a)</td><td>142.90 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (+14.33%)</td><td>0.10 (-3.68%)</td><td>0.09 (-7.51%)</td><td>0.08 (-17.12%)</td><td>0.03 <b>(+86.16%)</b></td><td>242.10 <b>(+20.69%)</b></td><td>191.56 (+7.63%)</td><td>198.50 (+8.12%)</td><td>122.70 (-12.48%)</td><td>43.07 <b>(+90.98%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>200.60 (n/a)</td><td>177.98 (n/a)</td><td>183.60 (n/a)</td><td>140.20 (n/a)</td><td>22.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.15 (-1.92%)</td><td>0.11 (+0.54%)</td><td>0.11 (+9.07%)</td><td>0.08 (-8.26%)</td><td>0.03 (+10.42%)</td><td>239.20 (+9.02%)</td><td>181.50 (+1.18%)</td><td>167.00 (-8.29%)</td><td>124.40 (+1.97%)</td><td>47.51 <b>(+31.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>219.40 (n/a)</td><td>179.38 (n/a)</td><td>182.10 (n/a)</td><td>122.00 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (-8.87%)</td><td>0.11 (-0.60%)</td><td>0.10 (-4.56%)</td><td>0.09 (+15.23%)</td><td>0.01 <b>(-40.05%)</b></td><td>206.20 (-13.22%)</td><td>175.10 (-1.62%)</td><td>176.20 (+4.76%)</td><td>146.70 (+9.72%)</td><td>21.25 <b>(-43.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>237.60 (n/a)</td><td>177.98 (n/a)</td><td>168.20 (n/a)</td><td>133.70 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.11 (-14.64%)</td><td>0.10 (-3.73%)</td><td>0.10 (+5.21%)</td><td>0.08 (+7.90%)</td><td>0.01 <b>(-39.28%)</b></td><td>217.80 (-7.32%)</td><td>191.82 (+2.41%)</td><td>178.60 (-4.95%)</td><td>173.20 (+17.19%)</td><td>21.68 <b>(-33.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>187.30 (n/a)</td><td>187.90 (n/a)</td><td>147.80 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.12 (-6.47%)</td><td>0.10 (-6.65%)</td><td>0.10 (-15.21%)</td><td>0.07 (-0.86%)</td><td>0.02 (-12.11%)</td><td>273.40 (+0.85%)</td><td>198.48 (+6.07%)</td><td>190.30 (+17.91%)</td><td>155.50 (+6.95%)</td><td>48.83 (-7.20%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>271.10 (n/a)</td><td>187.12 (n/a)</td><td>161.40 (n/a)</td><td>145.40 (n/a)</td><td>52.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.14 (+13.29%)</td><td>0.11 (+11.23%)</td><td>0.11 (+1.36%)</td><td>0.08 <b>(+33.85%)</b></td><td>0.02 (-11.64%)</td><td>225.80 <b>(-25.28%)</b></td><td>174.08 (-12.58%)</td><td>168.90 (-1.34%)</td><td>136.50 (-11.71%)</td><td>34.06 <b>(-43.18%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>302.20 (n/a)</td><td>199.12 (n/a)</td><td>171.20 (n/a)</td><td>154.60 (n/a)</td><td>59.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.72 (-1.79%)</td><td>0.58 (-2.47%)</td><td>0.59 (+4.09%)</td><td>0.44 (+0.06%)</td><td>0.13 (+5.65%)</td><td>223.70 (-0.04%)</td><td>177.84 (+3.25%)</td><td>165.60 (-3.94%)</td><td>136.40 (+1.79%)</td><td>41.84 (+12.72%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.73 (n/a)</td><td>0.59 (n/a)</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.12 (n/a)</td><td>223.80 (n/a)</td><td>172.24 (n/a)</td><td>172.40 (n/a)</td><td>134.00 (n/a)</td><td>37.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.79 (+19.64%)</td><td>0.60 (+8.32%)</td><td>0.56 (+0.60%)</td><td>0.52 <b>(+27.44%)</b></td><td>0.11 (+5.99%)</td><td>187.50 <b>(-21.55%)</b></td><td>166.52 (-8.38%)</td><td>176.80 (-0.62%)</td><td>124.90 (-16.40%)</td><td>25.20 <b>(-30.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.66 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.10 (n/a)</td><td>239.00 (n/a)</td><td>181.76 (n/a)</td><td>177.90 (n/a)</td><td>149.40 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.74 (+4.99%)</td><td>0.59 (+5.90%)</td><td>0.55 (+3.95%)</td><td>0.49 (+11.93%)</td><td>0.10 (-8.39%)</td><td>202.30 (-10.68%)</td><td>169.16 (-6.37%)</td><td>178.90 (-3.82%)</td><td>133.10 (-4.72%)</td><td>26.80 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.11 (n/a)</td><td>226.50 (n/a)</td><td>180.66 (n/a)</td><td>186.00 (n/a)</td><td>139.70 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.82 (+15.44%)</td><td>0.59 (+3.77%)</td><td>0.54 (-7.22%)</td><td>0.48 (+5.96%)</td><td>0.14 <b>(+24.08%)</b></td><td>205.50 (-5.65%)</td><td>173.74 (-3.03%)</td><td>183.10 (+7.77%)</td><td>119.50 (-13.41%)</td><td>35.03 (-2.81%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.71 (n/a)</td><td>0.57 (n/a)</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.11 (n/a)</td><td>217.80 (n/a)</td><td>179.16 (n/a)</td><td>169.90 (n/a)</td><td>138.00 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.59 (+13.54%)</td><td>0.45 (+11.87%)</td><td>0.47 (+4.32%)</td><td>0.22 (+2.17%)</td><td>0.15 <b>(+23.96%)</b></td><td>342.80 (-2.11%)</td><td>185.06 (-8.02%)</td><td>155.70 (-4.18%)</td><td>125.70 (-11.91%)</td><td>89.98 (+5.68%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>350.20 (n/a)</td><td>201.20 (n/a)</td><td>162.50 (n/a)</td><td>142.70 (n/a)</td><td>85.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.60 (-0.06%)</td><td>0.46 (+5.46%)</td><td>0.44 (+15.79%)</td><td>0.33 (-4.82%)</td><td>0.11 (+1.53%)</td><td>223.80 (+5.07%)</td><td>168.36 (-4.87%)</td><td>166.50 (-13.64%)</td><td>122.70 (+0.08%)</td><td>39.36 (+7.43%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>213.00 (n/a)</td><td>176.98 (n/a)</td><td>192.80 (n/a)</td><td>122.60 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.49 (-13.59%)</td><td>0.44 (+4.63%)</td><td>0.47 (+8.23%)</td><td>0.35 <b>(+77.87%)</b></td><td>0.06 <b>(-58.92%)</b></td><td>208.50 <b>(-43.79%)</b></td><td>170.22 (-15.21%)</td><td>158.00 (-7.60%)</td><td>149.60 (+15.70%)</td><td>24.59 <b>(-74.84%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>370.90 (n/a)</td><td>200.76 (n/a)</td><td>171.00 (n/a)</td><td>129.30 (n/a)</td><td>97.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.54 (+16.42%)</td><td>0.43 (+6.54%)</td><td>0.47 <b>(+20.40%)</b></td><td>0.28 <b>(-25.20%)</b></td><td>0.10 <b>(+170.01%)</b></td><td>262.30 <b>(+33.69%)</b></td><td>179.58 (-2.01%)</td><td>158.50 (-16.93%)</td><td>137.60 (-14.11%)</td><td>48.96 <b>(+222.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.04 (n/a)</td><td>196.20 (n/a)</td><td>183.26 (n/a)</td><td>190.80 (n/a)</td><td>160.20 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (+7.38%)</td><td>0.22 (+2.29%)</td><td>0.22 (+0.15%)</td><td>0.16 (+9.33%)</td><td>0.04 (-7.67%)</td><td>225.50 (-8.56%)</td><td>171.12 (-3.34%)</td><td>170.70 (-0.18%)</td><td>129.10 (-6.92%)</td><td>35.23 (-19.59%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>246.60 (n/a)</td><td>177.04 (n/a)</td><td>171.00 (n/a)</td><td>138.70 (n/a)</td><td>43.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (+1.73%)</td><td>0.22 (+2.90%)</td><td>0.23 (+14.68%)</td><td>0.17 (-2.63%)</td><td>0.04 (+19.50%)</td><td>211.60 (+2.72%)</td><td>173.86 (-1.97%)</td><td>161.70 (-12.78%)</td><td>141.10 (-1.74%)</td><td>32.36 <b>(+23.91%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>206.00 (n/a)</td><td>177.36 (n/a)</td><td>185.40 (n/a)</td><td>143.60 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.31 <b>(+26.86%)</b></td><td>0.23 (+3.92%)</td><td>0.22 (+5.18%)</td><td>0.16 (-19.96%)</td><td>0.05 <b>(+222.60%)</b></td><td>229.90 <b>(+24.95%)</b></td><td>169.62 (+0.13%)</td><td>164.40 (-4.92%)</td><td>118.70 <b>(-21.13%)</b></td><td>39.70 <b>(+218.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>184.00 (n/a)</td><td>169.40 (n/a)</td><td>172.90 (n/a)</td><td>150.50 (n/a)</td><td>12.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.30 (+18.81%)</td><td>0.22 (+1.09%)</td><td>0.21 (-0.52%)</td><td>0.16 (-15.62%)</td><td>0.05 <b>(+107.66%)</b></td><td>233.30 (+18.49%)</td><td>175.02 (+2.00%)</td><td>172.30 (+0.53%)</td><td>123.60 (-15.80%)</td><td>38.97 <b>(+105.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>171.58 (n/a)</td><td>171.40 (n/a)</td><td>146.80 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (+16.72%)</td><td>0.22 (+15.92%)</td><td>0.24 <b>(+28.58%)</b></td><td>0.14 (-12.90%)</td><td>0.04 <b>(+100.62%)</b></td><td>258.10 (+14.81%)</td><td>176.80 (-10.85%)</td><td>155.90 <b>(-22.21%)</b></td><td>143.80 (-14.30%)</td><td>46.54 <b>(+105.38%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>198.32 (n/a)</td><td>200.40 (n/a)</td><td>167.80 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 <b>(+21.13%)</b></td><td>0.21 (+12.26%)</td><td>0.22 (+10.24%)</td><td>0.14 (-11.82%)</td><td>0.05 <b>(+132.19%)</b></td><td>257.90 (+13.41%)</td><td>180.24 (-7.65%)</td><td>170.30 (-9.27%)</td><td>144.40 (-17.44%)</td><td>46.61 <b>(+116.40%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>195.18 (n/a)</td><td>187.70 (n/a)</td><td>174.90 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (-11.39%)</td><td>0.23 (-0.00%)</td><td>0.23 (+12.13%)</td><td>0.18 (+5.18%)</td><td>0.04 <b>(-31.29%)</b></td><td>202.60 (-4.93%)</td><td>165.16 (-1.92%)</td><td>158.10 (-10.78%)</td><td>139.00 (+12.92%)</td><td>27.30 <b>(-25.98%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>213.10 (n/a)</td><td>168.40 (n/a)</td><td>177.20 (n/a)</td><td>123.10 (n/a)</td><td>36.88 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (-18.44%)</td><td>0.20 (-17.14%)</td><td>0.18 <b>(-21.12%)</b></td><td>0.17 (-16.60%)</td><td>0.04 (-8.15%)</td><td>219.30 (+19.90%)</td><td>187.44 <b>(+21.54%)</b></td><td>206.20 <b>(+26.74%)</b></td><td>141.40 <b>(+22.64%)</b></td><td>35.45 <b>(+39.57%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>182.90 (n/a)</td><td>154.22 (n/a)</td><td>162.70 (n/a)</td><td>115.30 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 <b>(+42.85%)</b></td><td>0.25 (+15.88%)</td><td>0.23 (+7.12%)</td><td>0.21 (+9.03%)</td><td>0.04 <b>(+275.14%)</b></td><td>192.70 (-8.28%)</td><td>170.26 (-11.92%)</td><td>177.40 (-6.68%)</td><td>127.60 <b>(-29.97%)</b></td><td>26.86 <b>(+139.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>193.30 (n/a)</td><td>190.10 (n/a)</td><td>182.20 (n/a)</td><td>11.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (+15.61%)</td><td>0.22 (-3.15%)</td><td>0.23 (+3.46%)</td><td>0.12 <b>(-39.93%)</b></td><td>0.07 <b>(+136.12%)</b></td><td>337.90 <b>(+66.45%)</b></td><td>204.18 (+12.48%)</td><td>180.00 (-3.38%)</td><td>129.40 (-13.50%)</td><td>79.28 <b>(+257.05%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>203.00 (n/a)</td><td>181.52 (n/a)</td><td>186.30 (n/a)</td><td>149.60 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.32 (-1.05%)</td><td>0.24 (-5.86%)</td><td>0.22 (-5.02%)</td><td>0.20 (-6.11%)</td><td>0.05 (+6.02%)</td><td>201.90 (+6.54%)</td><td>178.40 (+6.65%)</td><td>186.90 (+5.30%)</td><td>128.30 (+1.02%)</td><td>29.25 (+10.23%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>189.50 (n/a)</td><td>167.28 (n/a)</td><td>177.50 (n/a)</td><td>127.00 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.35 <b>(+53.44%)</b></td><td>0.26 <b>(+24.28%)</b></td><td>0.23 (+10.60%)</td><td>0.23 <b>(+21.99%)</b></td><td>0.05 <b>(+246.89%)</b></td><td>178.70 (-18.03%)</td><td>160.40 (-17.69%)</td><td>175.60 (-9.58%)</td><td>116.10 <b>(-34.81%)</b></td><td>26.61 <b>(+82.93%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>194.88 (n/a)</td><td>194.20 (n/a)</td><td>178.10 (n/a)</td><td>14.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (+1.53%)</td><td>0.23 (-0.67%)</td><td>0.25 (+13.27%)</td><td>0.15 (-19.27%)</td><td>0.05 <b>(+33.21%)</b></td><td>266.20 <b>(+23.87%)</b></td><td>186.42 (+3.45%)</td><td>164.10 (-11.73%)</td><td>139.30 (-1.55%)</td><td>49.99 <b>(+67.11%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>214.90 (n/a)</td><td>180.20 (n/a)</td><td>185.90 (n/a)</td><td>141.50 (n/a)</td><td>29.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.29 (-0.94%)</td><td>0.24 <b>(+20.93%)</b></td><td>0.25 <b>(+29.20%)</b></td><td>0.19 <b>(+48.45%)</b></td><td>0.04 <b>(-37.35%)</b></td><td>214.30 <b>(-32.63%)</b></td><td>171.52 <b>(-21.17%)</b></td><td>162.20 <b>(-22.58%)</b></td><td>141.40 (+0.93%)</td><td>27.57 <b>(-56.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>318.10 (n/a)</td><td>217.58 (n/a)</td><td>209.50 (n/a)</td><td>140.10 (n/a)</td><td>63.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (+2.03%)</td><td>0.24 (+7.24%)</td><td>0.24 (+2.33%)</td><td>0.22 (+13.07%)</td><td>0.02 <b>(-33.03%)</b></td><td>186.70 (-11.56%)</td><td>169.18 (-7.33%)</td><td>171.20 (-2.28%)</td><td>157.30 (-1.99%)</td><td>11.83 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>211.10 (n/a)</td><td>182.56 (n/a)</td><td>175.20 (n/a)</td><td>160.50 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 (+9.06%)</td><td>0.28 (+1.41%)</td><td>0.26 (-4.73%)</td><td>0.20 (-1.39%)</td><td>0.08 <b>(+20.36%)</b></td><td>208.40 (+1.41%)</td><td>156.54 (-0.19%)</td><td>158.70 (+4.96%)</td><td>100.70 (-8.29%)</td><td>38.16 (+8.12%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>205.50 (n/a)</td><td>156.84 (n/a)</td><td>151.20 (n/a)</td><td>109.80 (n/a)</td><td>35.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.27 (+2.05%)</td><td>0.21 (-2.71%)</td><td>0.20 (-16.15%)</td><td>0.14 (+1.55%)</td><td>0.05 (-4.81%)</td><td>241.10 (-1.51%)</td><td>176.22 (+2.14%)</td><td>177.00 (+19.27%)</td><td>131.20 (-2.02%)</td><td>41.44 (-8.26%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>244.80 (n/a)</td><td>172.52 (n/a)</td><td>148.40 (n/a)</td><td>133.90 (n/a)</td><td>45.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (+3.79%)</td><td>0.20 (-4.74%)</td><td>0.18 (-10.21%)</td><td>0.17 (-7.39%)</td><td>0.04 <b>(+28.52%)</b></td><td>205.90 (+7.97%)</td><td>176.02 (+6.19%)</td><td>189.30 (+11.35%)</td><td>133.10 (-3.69%)</td><td>31.14 <b>(+34.58%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>190.70 (n/a)</td><td>165.76 (n/a)</td><td>170.00 (n/a)</td><td>138.20 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 (-7.84%)</td><td>0.20 (-16.28%)</td><td>0.18 <b>(-21.29%)</b></td><td>0.13 <b>(-34.16%)</b></td><td>0.06 <b>(+45.35%)</b></td><td>267.80 <b>(+51.90%)</b></td><td>185.78 <b>(+25.24%)</b></td><td>190.60 <b>(+27.07%)</b></td><td>132.40 (+8.52%)</td><td>55.43 <b>(+131.59%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>176.30 (n/a)</td><td>148.34 (n/a)</td><td>150.00 (n/a)</td><td>122.00 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 (-15.24%)</td><td>0.20 (-5.51%)</td><td>0.21 (+5.85%)</td><td>0.17 (-8.61%)</td><td>0.03 <b>(-35.77%)</b></td><td>206.20 (+9.45%)</td><td>173.14 (+4.62%)</td><td>169.00 (-5.53%)</td><td>145.10 (+17.97%)</td><td>22.69 (-16.38%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>188.40 (n/a)</td><td>165.50 (n/a)</td><td>178.90 (n/a)</td><td>123.00 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.24 <b>(-23.32%)</b></td><td>0.21 (-2.77%)</td><td>0.23 (+16.95%)</td><td>0.16 (+13.07%)</td><td>0.04 <b>(-45.43%)</b></td><td>215.20 (-11.55%)</td><td>167.22 (-1.92%)</td><td>149.80 (-14.50%)</td><td>142.60 <b>(+30.47%)</b></td><td>31.98 <b>(-37.39%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>243.30 (n/a)</td><td>170.50 (n/a)</td><td>175.20 (n/a)</td><td>109.30 (n/a)</td><td>51.08 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 <b>(-22.34%)</b></td><td>0.19 (-9.08%)</td><td>0.20 (-5.99%)</td><td>0.16 (-1.38%)</td><td>0.02 <b>(-56.85%)</b></td><td>214.00 (+1.37%)</td><td>182.78 (+7.50%)</td><td>175.80 (+6.35%)</td><td>165.30 <b>(+28.74%)</b></td><td>18.61 <b>(-42.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>170.02 (n/a)</td><td>165.30 (n/a)</td><td>128.40 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 <b>(-22.27%)</b></td><td>0.18 (-19.53%)</td><td>0.21 (-4.29%)</td><td>0.10 <b>(-39.16%)</b></td><td>0.05 <b>(+24.91%)</b></td><td>332.40 <b>(+64.39%)</b></td><td>206.54 <b>(+31.00%)</b></td><td>162.70 (+4.43%)</td><td>162.40 <b>(+28.68%)</b></td><td>73.64 <b>(+156.10%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>202.20 (n/a)</td><td>157.66 (n/a)</td><td>155.80 (n/a)</td><td>126.20 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.25 (-2.05%)</td><td>0.21 (-3.88%)</td><td>0.22 (-4.61%)</td><td>0.16 (-6.62%)</td><td>0.03 (-3.54%)</td><td>215.20 (+7.12%)</td><td>166.08 (+4.16%)</td><td>159.80 (+4.79%)</td><td>139.00 (+2.13%)</td><td>28.90 (+9.63%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>200.90 (n/a)</td><td>159.44 (n/a)</td><td>152.50 (n/a)</td><td>136.10 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>1.07 (-2.32%)</td><td>0.85 (+13.01%)</td><td>0.85 (+17.06%)</td><td>0.73 <b>(+33.77%)</b></td><td>0.13 <b>(-36.36%)</b></td><td>180.70 <b>(-25.24%)</b></td><td>156.06 (-14.63%)</td><td>153.40 (-14.59%)</td><td>122.90 (+2.33%)</td><td>22.06 <b>(-50.52%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.09 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.54 (n/a)</td><td>0.21 (n/a)</td><td>241.70 (n/a)</td><td>182.80 (n/a)</td><td>179.60 (n/a)</td><td>120.10 (n/a)</td><td>44.59 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.75 <b>(-30.30%)</b></td><td>0.70 (-8.36%)</td><td>0.71 (+4.72%)</td><td>0.64 (-2.61%)</td><td>0.05 <b>(-72.34%)</b></td><td>204.40 (+2.71%)</td><td>188.68 (+5.83%)</td><td>184.60 (-4.50%)</td><td>174.50 <b>(+43.50%)</b></td><td>13.55 <b>(-58.25%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>1.08 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.18 (n/a)</td><td>199.00 (n/a)</td><td>178.28 (n/a)</td><td>193.30 (n/a)</td><td>121.60 (n/a)</td><td>32.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.88 <b>(+23.96%)</b></td><td>0.78 (+14.65%)</td><td>0.85 <b>(+26.39%)</b></td><td>0.60 (-1.83%)</td><td>0.13 <b>(+235.64%)</b></td><td>217.60 (+1.87%)</td><td>173.30 (-10.77%)</td><td>153.40 <b>(-20.89%)</b></td><td>148.20 (-19.37%)</td><td>32.19 <b>(+170.69%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.71 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.04 (n/a)</td><td>213.60 (n/a)</td><td>194.22 (n/a)</td><td>193.90 (n/a)</td><td>183.80 (n/a)</td><td>11.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.00 (+2.27%)</td><td>0.00 (-1.38%)</td><td>0.00 (+0.00%)</td><td>0.00 (-6.98%)</td><td>0.00 <b>(+265.15%)</b></td><td>1033.64 (+8.79%)</td><td>959.47 (+1.75%)</td><td>940.92 (-0.04%)</td><td>920.01 (-2.01%)</td><td>44.60 <b>(+858.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>950.10 (n/a)</td><td>943.00 (n/a)</td><td>941.28 (n/a)</td><td>938.90 (n/a)</td><td>4.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.01 (+1.22%)</td><td>0.01 (+0.50%)</td><td>0.01 (+1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 (+10.55%)</td><td>1082.79 (+0.42%)</td><td>1016.00 (-0.29%)</td><td>996.83 (-0.83%)</td><td>986.05 (-1.45%)</td><td>39.05 (+17.39%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1078.25 (n/a)</td><td>1018.92 (n/a)</td><td>1005.17 (n/a)</td><td>1000.57 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.96 (-0.14%)</td><td>0.95 (+0.01%)</td><td>0.95 (+0.22%)</td><td>0.93 (-0.98%)</td><td>0.01 <b>(+24.73%)</b></td><td>2264.04 (+0.99%)</td><td>2216.23 (-0.01%)</td><td>2207.98 (-0.22%)</td><td>2188.92 (+0.13%)</td><td>28.49 <b>(+26.44%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2241.83 (n/a)</td><td>2216.45 (n/a)</td><td>2212.95 (n/a)</td><td>2185.98 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.44 (-11.82%)</td><td>4.78 (-11.73%)</td><td>4.69 (-9.00%)</td><td>3.97 (-18.74%)</td><td>0.57 (+0.36%)</td><td>264.40 <b>(+23.03%)</b></td><td>221.82 (+13.67%)</td><td>223.40 (+9.89%)</td><td>192.70 (+13.42%)</td><td>27.88 <b>(+40.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>6.17 (n/a)</td><td>5.42 (n/a)</td><td>5.16 (n/a)</td><td>4.88 (n/a)</td><td>0.57 (n/a)</td><td>214.90 (n/a)</td><td>195.14 (n/a)</td><td>203.30 (n/a)</td><td>169.90 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.13 (-0.02%)</td><td>4.72 (+6.94%)</td><td>4.97 (+11.40%)</td><td>4.08 (+6.94%)</td><td>0.49 (+2.65%)</td><td>256.80 (-6.48%)</td><td>224.00 (-6.50%)</td><td>211.00 (-10.21%)</td><td>204.50 (+0.00%)</td><td>24.32 (-4.52%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.13 (n/a)</td><td>4.42 (n/a)</td><td>4.46 (n/a)</td><td>3.82 (n/a)</td><td>0.48 (n/a)</td><td>274.60 (n/a)</td><td>239.58 (n/a)</td><td>235.00 (n/a)</td><td>204.50 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.57 (-4.98%)</td><td>4.82 (-8.78%)</td><td>5.15 (-1.16%)</td><td>3.51 <b>(-27.11%)</b></td><td>0.82 <b>(+82.46%)</b></td><td>299.00 <b>(+37.16%)</b></td><td>223.62 (+12.02%)</td><td>203.40 (+1.14%)</td><td>188.40 (+5.25%)</td><td>44.73 <b>(+167.37%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.86 (n/a)</td><td>5.28 (n/a)</td><td>5.22 (n/a)</td><td>4.81 (n/a)</td><td>0.45 (n/a)</td><td>218.00 (n/a)</td><td>199.62 (n/a)</td><td>201.10 (n/a)</td><td>179.00 (n/a)</td><td>16.73 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.40 (-3.40%)</td><td>4.89 (+0.41%)</td><td>5.10 (+8.60%)</td><td>4.12 (-5.04%)</td><td>0.49 (-15.17%)</td><td>254.50 (+5.30%)</td><td>216.18 (-0.63%)</td><td>205.80 (-7.92%)</td><td>194.20 (+3.52%)</td><td>23.41 (-6.54%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.59 (n/a)</td><td>4.87 (n/a)</td><td>4.69 (n/a)</td><td>4.34 (n/a)</td><td>0.58 (n/a)</td><td>241.70 (n/a)</td><td>217.56 (n/a)</td><td>223.50 (n/a)</td><td>187.60 (n/a)</td><td>25.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.37 (+8.08%)</td><td>7.95 (+12.37%)</td><td>7.98 (+15.56%)</td><td>7.18 (+15.00%)</td><td>0.47 <b>(-27.84%)</b></td><td>292.00 (-13.04%)</td><td>264.72 (-11.35%)</td><td>262.90 (-13.46%)</td><td>250.70 (-7.46%)</td><td>16.37 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>7.74 (n/a)</td><td>7.07 (n/a)</td><td>6.90 (n/a)</td><td>6.25 (n/a)</td><td>0.65 (n/a)</td><td>335.80 (n/a)</td><td>298.62 (n/a)</td><td>303.80 (n/a)</td><td>270.90 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.64 (-2.20%)</td><td>7.75 (+0.42%)</td><td>7.78 (+4.40%)</td><td>6.65 (-1.40%)</td><td>0.71 <b>(-26.74%)</b></td><td>315.50 (+1.41%)</td><td>272.62 (-0.95%)</td><td>269.50 (-4.23%)</td><td>242.70 (+2.28%)</td><td>26.48 <b>(-22.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.84 (n/a)</td><td>7.72 (n/a)</td><td>7.45 (n/a)</td><td>6.74 (n/a)</td><td>0.97 (n/a)</td><td>311.10 (n/a)</td><td>275.24 (n/a)</td><td>281.40 (n/a)</td><td>237.30 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.57 (+6.19%)</td><td>7.82 (+6.96%)</td><td>7.97 (+13.76%)</td><td>6.58 (-1.09%)</td><td>0.79 <b>(+21.22%)</b></td><td>318.60 (+1.11%)</td><td>270.48 (-6.26%)</td><td>263.10 (-12.09%)</td><td>244.70 (-5.81%)</td><td>29.45 (+17.51%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.07 (n/a)</td><td>7.31 (n/a)</td><td>7.01 (n/a)</td><td>6.66 (n/a)</td><td>0.65 (n/a)</td><td>315.10 (n/a)</td><td>288.54 (n/a)</td><td>299.30 (n/a)</td><td>259.80 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>9.30 (+3.52%)</td><td>8.71 (+6.89%)</td><td>8.87 (+11.46%)</td><td>7.88 (+4.89%)</td><td>0.58 (-4.52%)</td><td>266.10 (-4.66%)</td><td>241.58 (-6.50%)</td><td>236.50 (-10.28%)</td><td>225.50 (-3.38%)</td><td>16.49 (-11.83%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>8.99 (n/a)</td><td>8.15 (n/a)</td><td>7.96 (n/a)</td><td>7.51 (n/a)</td><td>0.60 (n/a)</td><td>279.10 (n/a)</td><td>258.38 (n/a)</td><td>263.60 (n/a)</td><td>233.40 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.92 (-5.73%)</td><td>7.92 (-2.81%)</td><td>8.59 (+2.87%)</td><td>6.37 (-7.96%)</td><td>1.20 <b>(+25.21%)</b></td><td>329.40 (+8.64%)</td><td>270.10 (+3.79%)</td><td>244.10 (-2.79%)</td><td>235.10 (+6.09%)</td><td>43.68 <b>(+41.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.46 (n/a)</td><td>8.15 (n/a)</td><td>8.35 (n/a)</td><td>6.92 (n/a)</td><td>0.96 (n/a)</td><td>303.20 (n/a)</td><td>260.24 (n/a)</td><td>251.10 (n/a)</td><td>221.60 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>10.53 (+15.47%)</td><td>9.10 (+6.09%)</td><td>8.89 (+2.78%)</td><td>7.33 (-5.12%)</td><td>1.21 <b>(+103.36%)</b></td><td>286.20 (+5.38%)</td><td>234.00 (-4.68%)</td><td>235.90 (-2.72%)</td><td>199.10 (-13.40%)</td><td>33.22 <b>(+88.48%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.12 (n/a)</td><td>8.58 (n/a)</td><td>8.65 (n/a)</td><td>7.72 (n/a)</td><td>0.60 (n/a)</td><td>271.60 (n/a)</td><td>245.50 (n/a)</td><td>242.50 (n/a)</td><td>229.90 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>12.02 (-3.99%)</td><td>10.86 (-6.54%)</td><td>10.98 (-6.39%)</td><td>9.59 (-7.16%)</td><td>0.90 (-5.56%)</td><td>437.60 (+7.73%)</td><td>388.58 (+7.02%)</td><td>382.20 (+6.85%)</td><td>348.90 (+4.15%)</td><td>33.12 (+7.86%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>12.52 (n/a)</td><td>11.62 (n/a)</td><td>11.72 (n/a)</td><td>10.32 (n/a)</td><td>0.96 (n/a)</td><td>406.20 (n/a)</td><td>363.10 (n/a)</td><td>357.70 (n/a)</td><td>335.00 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>12.29 (-8.13%)</td><td>10.94 (-1.94%)</td><td>11.32 (+6.38%)</td><td>9.58 (-5.31%)</td><td>1.29 (-2.47%)</td><td>438.00 (+5.62%)</td><td>387.68 (+2.11%)</td><td>370.40 (-5.99%)</td><td>341.20 (+8.84%)</td><td>46.80 (+15.63%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.38 (n/a)</td><td>11.16 (n/a)</td><td>10.64 (n/a)</td><td>10.11 (n/a)</td><td>1.32 (n/a)</td><td>414.70 (n/a)</td><td>379.66 (n/a)</td><td>394.00 (n/a)</td><td>313.50 (n/a)</td><td>40.48 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>11.85 (-9.82%)</td><td>10.87 (-5.64%)</td><td>10.71 (-10.15%)</td><td>10.14 (+4.50%)</td><td>0.78 <b>(-41.03%)</b></td><td>413.70 (-4.32%)</td><td>387.26 (+5.25%)</td><td>391.50 (+11.28%)</td><td>354.10 (+10.90%)</td><td>27.26 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.14 (n/a)</td><td>11.52 (n/a)</td><td>11.92 (n/a)</td><td>9.70 (n/a)</td><td>1.32 (n/a)</td><td>432.40 (n/a)</td><td>367.96 (n/a)</td><td>351.80 (n/a)</td><td>319.30 (n/a)</td><td>43.69 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.27 (-1.34%)</td><td>12.73 (-3.63%)</td><td>12.48 (-4.75%)</td><td>11.35 (+0.08%)</td><td>1.53 (-8.55%)</td><td>369.50 (-0.08%)</td><td>332.94 (+3.55%)</td><td>336.00 (+5.00%)</td><td>274.70 (+1.37%)</td><td>36.36 (-9.05%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>15.48 (n/a)</td><td>13.21 (n/a)</td><td>13.11 (n/a)</td><td>11.34 (n/a)</td><td>1.67 (n/a)</td><td>369.80 (n/a)</td><td>321.52 (n/a)</td><td>320.00 (n/a)</td><td>271.00 (n/a)</td><td>39.98 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.57 (+7.58%)</td><td>12.95 (+3.43%)</td><td>12.40 (+4.91%)</td><td>11.35 (-3.60%)</td><td>1.65 <b>(+41.73%)</b></td><td>369.50 (+3.73%)</td><td>327.80 (-2.75%)</td><td>338.20 (-4.68%)</td><td>269.40 (-7.04%)</td><td>38.89 <b>(+34.49%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>14.47 (n/a)</td><td>12.52 (n/a)</td><td>11.82 (n/a)</td><td>11.77 (n/a)</td><td>1.17 (n/a)</td><td>356.20 (n/a)</td><td>337.08 (n/a)</td><td>354.80 (n/a)</td><td>289.80 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>15.25 (+11.61%)</td><td>13.09 (-0.36%)</td><td>12.55 (-6.23%)</td><td>11.16 (-9.15%)</td><td>1.79 <b>(+211.48%)</b></td><td>375.90 (+10.07%)</td><td>325.10 (+1.70%)</td><td>334.20 (+6.64%)</td><td>275.00 (-10.42%)</td><td>43.63 <b>(+203.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>13.66 (n/a)</td><td>13.14 (n/a)</td><td>13.38 (n/a)</td><td>12.28 (n/a)</td><td>0.58 (n/a)</td><td>341.50 (n/a)</td><td>319.66 (n/a)</td><td>313.40 (n/a)</td><td>307.00 (n/a)</td><td>14.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>14.37 (-5.04%)</td><td>13.22 (+4.91%)</td><td>13.72 (+11.60%)</td><td>11.39 (+0.35%)</td><td>1.27 (-15.07%)</td><td>368.30 (-0.35%)</td><td>319.72 (-4.91%)</td><td>305.60 (-10.38%)</td><td>291.90 (+5.30%)</td><td>32.52 (-10.05%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>15.13 (n/a)</td><td>12.60 (n/a)</td><td>12.30 (n/a)</td><td>11.35 (n/a)</td><td>1.50 (n/a)</td><td>369.60 (n/a)</td><td>336.24 (n/a)</td><td>341.00 (n/a)</td><td>277.20 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>14.01 (-4.64%)</td><td>12.22 (-5.06%)</td><td>12.68 (-11.19%)</td><td>9.21 (+4.20%)</td><td>1.79 <b>(-29.39%)</b></td><td>455.40 (-4.05%)</td><td>350.32 (+3.46%)</td><td>330.80 (+12.63%)</td><td>299.40 (+4.87%)</td><td>60.62 <b>(-25.32%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>14.69 (n/a)</td><td>12.87 (n/a)</td><td>14.28 (n/a)</td><td>8.84 (n/a)</td><td>2.54 (n/a)</td><td>474.60 (n/a)</td><td>338.60 (n/a)</td><td>293.70 (n/a)</td><td>285.50 (n/a)</td><td>81.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.46 (-11.76%)</td><td>3.22 (+15.87%)</td><td>3.39 <b>(+33.93%)</b></td><td>2.78 <b>(+37.43%)</b></td><td>0.30 <b>(-58.42%)</b></td><td>188.70 <b>(-27.26%)</b></td><td>164.22 (-17.28%)</td><td>154.70 <b>(-25.34%)</b></td><td>151.50 (+13.31%)</td><td>16.36 <b>(-65.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.92 (n/a)</td><td>2.78 (n/a)</td><td>2.53 (n/a)</td><td>2.02 (n/a)</td><td>0.73 (n/a)</td><td>259.40 (n/a)</td><td>198.52 (n/a)</td><td>207.20 (n/a)</td><td>133.70 (n/a)</td><td>47.10 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>5.38 (+2.66%)</td><td>4.49 (-2.25%)</td><td>4.54 (-6.56%)</td><td>3.78 (+10.87%)</td><td>0.65 (-9.00%)</td><td>277.30 (-9.82%)</td><td>237.50 (+1.63%)</td><td>230.90 (+7.00%)</td><td>195.00 (-2.60%)</td><td>33.86 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>5.24 (n/a)</td><td>4.59 (n/a)</td><td>4.86 (n/a)</td><td>3.41 (n/a)</td><td>0.71 (n/a)</td><td>307.50 (n/a)</td><td>233.68 (n/a)</td><td>215.80 (n/a)</td><td>200.20 (n/a)</td><td>42.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>8.81 (-5.23%)</td><td>7.96 (+4.14%)</td><td>8.11 (+11.67%)</td><td>6.58 (-5.46%)</td><td>0.84 (-12.30%)</td><td>318.90 (+5.77%)</td><td>265.96 (-4.08%)</td><td>258.70 (-10.45%)</td><td>238.00 (+5.54%)</td><td>30.99 (+1.99%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>9.30 (n/a)</td><td>7.65 (n/a)</td><td>7.26 (n/a)</td><td>6.96 (n/a)</td><td>0.95 (n/a)</td><td>301.50 (n/a)</td><td>277.26 (n/a)</td><td>288.90 (n/a)</td><td>225.50 (n/a)</td><td>30.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>3.52 (-0.19%)</td><td>3.03 (-1.85%)</td><td>3.18 (+1.52%)</td><td>2.27 (-14.14%)</td><td>0.47 <b>(+23.78%)</b></td><td>230.80 (+16.51%)</td><td>177.04 (+2.92%)</td><td>164.80 (-1.49%)</td><td>149.10 (+0.20%)</td><td>31.58 <b>(+48.67%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>3.52 (n/a)</td><td>3.08 (n/a)</td><td>3.13 (n/a)</td><td>2.65 (n/a)</td><td>0.38 (n/a)</td><td>198.10 (n/a)</td><td>172.02 (n/a)</td><td>167.30 (n/a)</td><td>148.80 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.26 <b>(+20.58%)</b></td><td>0.21 (+13.16%)</td><td>0.21 <b>(+20.42%)</b></td><td>0.16 <b>(+20.13%)</b></td><td>0.04 (+8.25%)</td><td>206.10 (-16.76%)</td><td>163.18 (-12.14%)</td><td>156.20 (-16.96%)</td><td>123.80 (-17.02%)</td><td>30.89 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>247.60 (n/a)</td><td>185.72 (n/a)</td><td>188.10 (n/a)</td><td>149.20 (n/a)</td><td>40.20 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.21 (-18.67%)</td><td>0.19 (-6.14%)</td><td>0.19 (+1.26%)</td><td>0.16 (+2.17%)</td><td>0.02 <b>(-49.40%)</b></td><td>208.90 (-2.15%)</td><td>175.62 (+4.29%)</td><td>170.00 (-1.28%)</td><td>155.10 <b>(+23.00%)</b></td><td>20.51 <b>(-37.65%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.50 (n/a)</td><td>168.40 (n/a)</td><td>172.20 (n/a)</td><td>126.10 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.49 (+3.20%)</td><td>0.38 (-1.51%)</td><td>0.40 (-5.65%)</td><td>0.28 <b>(+32.94%)</b></td><td>0.08 <b>(-28.01%)</b></td><td>234.30 <b>(-24.78%)</b></td><td>177.96 (-3.94%)</td><td>165.70 (+5.95%)</td><td>133.70 (-3.05%)</td><td>37.71 <b>(-48.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>311.50 (n/a)</td><td>185.26 (n/a)</td><td>156.40 (n/a)</td><td>137.90 (n/a)</td><td>72.59 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 <b>(-29.14%)</b></td><td>0.36 <b>(-22.25%)</b></td><td>0.36 (-13.01%)</td><td>0.30 <b>(-25.23%)</b></td><td>0.04 <b>(-43.75%)</b></td><td>216.00 <b>(+33.75%)</b></td><td>182.64 <b>(+27.51%)</b></td><td>179.90 (+14.95%)</td><td>157.90 <b>(+41.11%)</b></td><td>23.23 (+4.38%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.08 (n/a)</td><td>161.50 (n/a)</td><td>143.24 (n/a)</td><td>156.50 (n/a)</td><td>111.90 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.41 (-13.36%)</td><td>0.39 (-1.95%)</td><td>0.38 (-1.15%)</td><td>0.35 (+16.81%)</td><td>0.03 <b>(-60.87%)</b></td><td>185.60 (-14.39%)</td><td>169.88 (+0.01%)</td><td>172.50 (+1.11%)</td><td>158.40 (+15.45%)</td><td>11.25 <b>(-62.23%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.06 (n/a)</td><td>216.80 (n/a)</td><td>169.86 (n/a)</td><td>170.60 (n/a)</td><td>137.20 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.98 (+5.19%)</td><td>0.84 (-1.61%)</td><td>0.90 (+7.07%)</td><td>0.67 (-16.05%)</td><td>0.14 <b>(+167.58%)</b></td><td>197.10 (+19.17%)</td><td>159.70 (+3.73%)</td><td>145.80 (-6.60%)</td><td>133.50 (-4.91%)</td><td>27.81 <b>(+206.87%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.93 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td><td>165.40 (n/a)</td><td>153.96 (n/a)</td><td>156.10 (n/a)</td><td>140.40 (n/a)</td><td>9.06 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.89 (+6.04%)</td><td>0.79 (+12.46%)</td><td>0.79 (+10.03%)</td><td>0.62 (+11.83%)</td><td>0.11 (+4.17%)</td><td>210.70 (-10.57%)</td><td>167.78 (-11.23%)</td><td>165.80 (-9.15%)</td><td>147.00 (-5.71%)</td><td>25.60 (-12.89%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.72 (n/a)</td><td>0.56 (n/a)</td><td>0.10 (n/a)</td><td>235.60 (n/a)</td><td>189.00 (n/a)</td><td>182.50 (n/a)</td><td>155.90 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.91 (-1.30%)</td><td>0.76 (-3.47%)</td><td>0.74 (-3.70%)</td><td>0.66 (-6.54%)</td><td>0.10 (+19.47%)</td><td>197.90 (+7.03%)</td><td>174.02 (+4.03%)</td><td>177.30 (+3.81%)</td><td>143.80 (+1.34%)</td><td>20.60 <b>(+30.89%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.92 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.71 (n/a)</td><td>0.08 (n/a)</td><td>184.90 (n/a)</td><td>167.28 (n/a)</td><td>170.80 (n/a)</td><td>141.90 (n/a)</td><td>15.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.90 (-0.96%)</td><td>0.73 (+14.45%)</td><td>0.79 <b>(+30.06%)</b></td><td>0.51 <b>(+30.78%)</b></td><td>0.16 <b>(-20.51%)</b></td><td>256.00 <b>(-23.54%)</b></td><td>187.40 (-16.00%)</td><td>166.20 <b>(-23.13%)</b></td><td>145.70 (+0.97%)</td><td>45.02 <b>(-38.28%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.91 (n/a)</td><td>0.64 (n/a)</td><td>0.61 (n/a)</td><td>0.39 (n/a)</td><td>0.20 (n/a)</td><td>334.80 (n/a)</td><td>223.10 (n/a)</td><td>216.20 (n/a)</td><td>144.30 (n/a)</td><td>72.93 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:16:08</td><td>0.13 (+3.68%)</td><td>0.11 (+9.22%)</td><td>0.10 (-5.74%)</td><td>0.10 <b>(+23.26%)</b></td><td>0.02 <b>(-20.45%)</b></td><td>171.90 (-18.88%)</td><td>150.60 (-10.31%)</td><td>158.20 (+6.10%)</td><td>123.70 (-3.51%)</td><td>22.88 <b>(-40.02%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:38:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>167.92 (n/a)</td><td>149.10 (n/a)</td><td>128.20 (n/a)</td><td>38.15 (n/a)</td>
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
