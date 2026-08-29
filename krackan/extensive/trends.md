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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-15.04%)</td><td>0.04 (-8.19%)</td><td>0.04 (-5.25%)</td><td>0.03 (-8.29%)</td><td>0.00 <b>(-34.12%)</b></td><td>213.90 (+9.08%)</td><td>173.54 (+7.63%)</td><td>171.10 (+5.55%)</td><td>149.50 (+17.72%)</td><td>25.28 (-14.71%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>161.24 (n/a)</td><td>162.10 (n/a)</td><td>127.00 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-11.57%)</td><td>0.04 (-10.83%)</td><td>0.04 (-11.43%)</td><td>0.03 (-13.04%)</td><td>0.00 (-4.95%)</td><td>198.40 (+15.01%)</td><td>170.04 (+12.37%)</td><td>164.80 (+12.88%)</td><td>144.80 (+13.13%)</td><td>22.78 <b>(+22.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>151.32 (n/a)</td><td>146.00 (n/a)</td><td>128.00 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-6.69%)</td><td>0.04 (+4.18%)</td><td>0.04 (+12.75%)</td><td>0.03 (+14.75%)</td><td>0.00 <b>(-40.15%)</b></td><td>186.30 (-12.82%)</td><td>159.32 (-5.79%)</td><td>149.70 (-11.32%)</td><td>145.30 (+7.15%)</td><td>18.08 <b>(-43.73%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>169.12 (n/a)</td><td>168.80 (n/a)</td><td>135.60 (n/a)</td><td>32.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(-25.61%)</b></td><td>0.04 (-12.67%)</td><td>0.04 (-10.76%)</td><td>0.03 (+10.44%)</td><td>0.00 <b>(-64.94%)</b></td><td>185.10 (-9.44%)</td><td>162.84 (+9.89%)</td><td>164.60 (+12.05%)</td><td>142.40 <b>(+34.47%)</b></td><td>15.82 <b>(-57.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>148.18 (n/a)</td><td>146.90 (n/a)</td><td>105.90 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-14.66%)</td><td>0.04 (-11.70%)</td><td>0.04 (-9.85%)</td><td>0.03 (-1.28%)</td><td>0.00 <b>(-44.35%)</b></td><td>199.30 (+1.32%)</td><td>176.32 (+11.98%)</td><td>175.40 (+10.94%)</td><td>158.10 (+17.20%)</td><td>16.34 <b>(-33.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>157.46 (n/a)</td><td>158.10 (n/a)</td><td>134.90 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-2.28%)</td><td>0.03 (-9.88%)</td><td>0.04 (-8.22%)</td><td>0.03 (-15.62%)</td><td>0.01 <b>(+62.79%)</b></td><td>225.20 (+18.46%)</td><td>182.52 (+13.95%)</td><td>173.20 (+8.93%)</td><td>138.20 (+2.37%)</td><td>39.86 <b>(+103.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>160.18 (n/a)</td><td>159.00 (n/a)</td><td>135.00 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-3.85%)</td><td>0.03 (-4.22%)</td><td>0.03 (-4.29%)</td><td>0.03 (-12.33%)</td><td>0.01 (+7.18%)</td><td>242.00 (+14.10%)</td><td>188.48 (+5.26%)</td><td>180.10 (+4.47%)</td><td>143.80 (+3.98%)</td><td>37.71 <b>(+26.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>179.06 (n/a)</td><td>172.40 (n/a)</td><td>138.30 (n/a)</td><td>29.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(-20.29%)</b></td><td>0.03 <b>(-22.78%)</b></td><td>0.03 <b>(-23.96%)</b></td><td>0.03 (-19.32%)</td><td>0.00 <b>(-34.56%)</b></td><td>229.70 <b>(+23.96%)</b></td><td>196.46 <b>(+28.27%)</b></td><td>196.20 <b>(+31.50%)</b></td><td>154.30 <b>(+25.45%)</b></td><td>28.09 (-0.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>153.16 (n/a)</td><td>149.20 (n/a)</td><td>123.00 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (+0.04%)</td><td>0.08 (+3.92%)</td><td>0.07 (-8.65%)</td><td>0.07 (+16.42%)</td><td>0.01 (-3.34%)</td><td>183.60 (-14.13%)</td><td>160.82 (-4.32%)</td><td>174.40 (+9.41%)</td><td>131.00 (-0.08%)</td><td>25.78 (-18.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>168.08 (n/a)</td><td>159.40 (n/a)</td><td>131.10 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (-10.96%)</td><td>0.07 (-10.48%)</td><td>0.07 (-9.97%)</td><td>0.06 (-14.95%)</td><td>0.01 (-3.03%)</td><td>210.60 (+17.59%)</td><td>176.32 (+12.19%)</td><td>183.70 (+11.06%)</td><td>137.50 (+12.24%)</td><td>28.66 <b>(+28.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>157.16 (n/a)</td><td>165.40 (n/a)</td><td>122.50 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (+2.36%)</td><td>0.08 (+11.65%)</td><td>0.09 (+11.00%)</td><td>0.07 <b>(+58.23%)</b></td><td>0.02 <b>(-29.17%)</b></td><td>187.10 <b>(-36.79%)</b></td><td>151.98 (-15.73%)</td><td>141.70 (-9.92%)</td><td>123.30 (-2.30%)</td><td>29.24 <b>(-57.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>296.00 (n/a)</td><td>180.34 (n/a)</td><td>157.30 (n/a)</td><td>126.20 (n/a)</td><td>68.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (-10.28%)</td><td>0.07 (-15.91%)</td><td>0.07 (-12.69%)</td><td>0.06 <b>(-22.71%)</b></td><td>0.01 (+7.91%)</td><td>206.50 <b>(+29.39%)</b></td><td>173.26 (+19.85%)</td><td>175.80 (+14.53%)</td><td>132.20 (+11.47%)</td><td>26.66 <b>(+49.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>159.60 (n/a)</td><td>144.56 (n/a)</td><td>153.50 (n/a)</td><td>118.60 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (+2.09%)</td><td>0.07 (-7.66%)</td><td>0.06 (-13.03%)</td><td>0.06 (-12.24%)</td><td>0.02 <b>(+33.40%)</b></td><td>205.60 (+13.97%)</td><td>175.62 (+10.22%)</td><td>191.40 (+14.95%)</td><td>119.90 (-2.12%)</td><td>33.69 <b>(+46.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>159.34 (n/a)</td><td>166.50 (n/a)</td><td>122.50 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (+0.85%)</td><td>0.07 (-0.92%)</td><td>0.07 (-9.57%)</td><td>0.06 (+9.53%)</td><td>0.01 (-11.74%)</td><td>219.10 (-8.71%)</td><td>179.92 (-0.33%)</td><td>179.40 (+10.60%)</td><td>133.80 (-0.89%)</td><td>32.02 <b>(-22.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.00 (n/a)</td><td>180.52 (n/a)</td><td>162.20 (n/a)</td><td>135.00 (n/a)</td><td>41.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (-5.31%)</td><td>0.07 (-15.57%)</td><td>0.06 <b>(-23.93%)</b></td><td>0.04 <b>(-40.64%)</b></td><td>0.03 <b>(+29.80%)</b></td><td>334.30 <b>(+68.50%)</b></td><td>211.76 <b>(+27.69%)</b></td><td>221.70 <b>(+31.49%)</b></td><td>118.40 (+5.62%)</td><td>81.18 <b>(+125.81%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>198.40 (n/a)</td><td>165.84 (n/a)</td><td>168.60 (n/a)</td><td>112.10 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (+13.89%)</td><td>0.06 (-9.05%)</td><td>0.06 (-10.90%)</td><td>0.04 <b>(-36.56%)</b></td><td>0.02 <b>(+143.31%)</b></td><td>332.90 <b>(+57.62%)</b></td><td>221.34 (+17.21%)</td><td>214.60 (+12.18%)</td><td>142.60 (-12.14%)</td><td>69.52 <b>(+241.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>188.84 (n/a)</td><td>191.30 (n/a)</td><td>162.30 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 <b>(-29.94%)</b></td><td>0.14 (-17.95%)</td><td>0.14 <b>(-23.32%)</b></td><td>0.12 (-0.34%)</td><td>0.02 <b>(-62.07%)</b></td><td>208.10 (+0.34%)</td><td>176.76 (+17.08%)</td><td>176.00 <b>(+30.47%)</b></td><td>156.30 <b>(+42.74%)</b></td><td>20.77 <b>(-46.84%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>207.40 (n/a)</td><td>150.98 (n/a)</td><td>134.90 (n/a)</td><td>109.50 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 <b>(-20.94%)</b></td><td>0.14 <b>(-20.77%)</b></td><td>0.13 <b>(-30.25%)</b></td><td>0.12 (-5.06%)</td><td>0.02 <b>(-52.20%)</b></td><td>203.40 (+5.33%)</td><td>180.30 <b>(+22.75%)</b></td><td>189.50 <b>(+43.34%)</b></td><td>148.20 <b>(+26.45%)</b></td><td>21.62 <b>(-36.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>193.10 (n/a)</td><td>146.88 (n/a)</td><td>132.20 (n/a)</td><td>117.20 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (-4.26%)</td><td>0.16 (+4.48%)</td><td>0.14 (-1.49%)</td><td>0.13 (+14.49%)</td><td>0.03 (-17.37%)</td><td>188.70 (-12.68%)</td><td>162.30 (-5.76%)</td><td>176.60 (+1.55%)</td><td>131.10 (+4.46%)</td><td>27.95 <b>(-26.41%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.10 (n/a)</td><td>172.22 (n/a)</td><td>173.90 (n/a)</td><td>125.50 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (-7.84%)</td><td>0.14 (-0.75%)</td><td>0.14 (+10.31%)</td><td>0.10 <b>(+30.17%)</b></td><td>0.03 <b>(-41.77%)</b></td><td>244.50 <b>(-23.16%)</b></td><td>185.44 (-8.31%)</td><td>175.60 (-9.30%)</td><td>130.50 (+8.48%)</td><td>41.74 <b>(-49.84%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>318.20 (n/a)</td><td>202.24 (n/a)</td><td>193.60 (n/a)</td><td>120.30 (n/a)</td><td>83.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-9.30%)</td><td>0.15 (+3.56%)</td><td>0.15 (-6.92%)</td><td>0.13 <b>(+58.91%)</b></td><td>0.02 <b>(-60.20%)</b></td><td>185.10 <b>(-37.06%)</b></td><td>160.52 (-10.89%)</td><td>161.60 (+7.38%)</td><td>135.30 (+10.27%)</td><td>17.79 <b>(-73.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>294.10 (n/a)</td><td>180.14 (n/a)</td><td>150.50 (n/a)</td><td>122.70 (n/a)</td><td>67.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-14.45%)</td><td>0.15 (-6.03%)</td><td>0.14 (-11.21%)</td><td>0.12 (+18.22%)</td><td>0.03 <b>(-36.10%)</b></td><td>206.90 (-15.41%)</td><td>168.22 (+1.40%)</td><td>172.00 (+12.57%)</td><td>133.20 (+16.94%)</td><td>34.18 <b>(-37.60%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>244.60 (n/a)</td><td>165.90 (n/a)</td><td>152.80 (n/a)</td><td>113.90 (n/a)</td><td>54.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (+4.00%)</td><td>0.15 (+10.72%)</td><td>0.14 (+17.69%)</td><td>0.12 (+10.73%)</td><td>0.03 (-6.00%)</td><td>211.40 (-9.66%)</td><td>171.56 (-10.28%)</td><td>170.30 (-15.02%)</td><td>130.30 (-3.84%)</td><td>30.29 (-15.95%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>234.00 (n/a)</td><td>191.22 (n/a)</td><td>200.40 (n/a)</td><td>135.50 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 <b>(-29.03%)</b></td><td>0.14 (-4.56%)</td><td>0.13 (+3.05%)</td><td>0.12 (+19.02%)</td><td>0.01 <b>(-72.42%)</b></td><td>197.40 (-16.00%)</td><td>180.08 (-1.91%)</td><td>184.50 (-2.95%)</td><td>154.90 <b>(+40.95%)</b></td><td>16.24 <b>(-67.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>235.00 (n/a)</td><td>183.58 (n/a)</td><td>190.10 (n/a)</td><td>109.90 (n/a)</td><td>49.64 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.40 (+0.80%)</td><td>0.30 (-1.18%)</td><td>0.29 (-19.07%)</td><td>0.25 <b>(+74.55%)</b></td><td>0.06 <b>(-45.99%)</b></td><td>200.10 <b>(-42.70%)</b></td><td>168.12 (-10.63%)</td><td>168.10 <b>(+23.60%)</b></td><td>123.30 (-0.72%)</td><td>28.49 <b>(-70.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.36 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>349.20 (n/a)</td><td>188.12 (n/a)</td><td>136.00 (n/a)</td><td>124.20 (n/a)</td><td>95.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.44 <b>(+40.55%)</b></td><td>0.30 (+9.56%)</td><td>0.28 (-0.83%)</td><td>0.24 (+3.97%)</td><td>0.08 <b>(+152.70%)</b></td><td>204.10 (-3.82%)</td><td>168.38 (-5.90%)</td><td>175.10 (+0.86%)</td><td>113.00 <b>(-28.84%)</b></td><td>33.87 <b>(+62.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>212.20 (n/a)</td><td>178.94 (n/a)</td><td>173.60 (n/a)</td><td>158.80 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.37 (-7.75%)</td><td>0.29 (-3.47%)</td><td>0.28 (+6.25%)</td><td>0.23 (+4.78%)</td><td>0.06 <b>(-32.20%)</b></td><td>215.00 (-4.53%)</td><td>173.64 (+0.64%)</td><td>176.60 (-5.86%)</td><td>133.40 (+8.46%)</td><td>32.45 <b>(-27.47%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>225.20 (n/a)</td><td>172.54 (n/a)</td><td>187.60 (n/a)</td><td>123.00 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.42 (-6.45%)</td><td>0.34 (+8.00%)</td><td>0.30 (+5.31%)</td><td>0.27 (+11.55%)</td><td>0.07 (-13.47%)</td><td>180.20 (-10.35%)</td><td>151.44 (-8.32%)</td><td>163.20 (-5.01%)</td><td>117.20 (+6.84%)</td><td>29.19 (-12.93%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>201.00 (n/a)</td><td>165.18 (n/a)</td><td>171.80 (n/a)</td><td>109.70 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.38 <b>(+20.60%)</b></td><td>0.31 (+10.11%)</td><td>0.28 (+0.30%)</td><td>0.26 (+4.12%)</td><td>0.05 <b>(+136.58%)</b></td><td>187.80 (-3.99%)</td><td>163.40 (-7.66%)</td><td>175.30 (-0.34%)</td><td>130.60 (-17.08%)</td><td>25.97 <b>(+89.35%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>176.96 (n/a)</td><td>175.90 (n/a)</td><td>157.50 (n/a)</td><td>13.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.41 (+17.69%)</td><td>0.31 (+8.91%)</td><td>0.28 (+8.06%)</td><td>0.25 <b>(+20.79%)</b></td><td>0.06 (-4.16%)</td><td>194.50 (-17.20%)</td><td>165.92 (-9.58%)</td><td>176.00 (-7.47%)</td><td>118.60 (-15.04%)</td><td>29.42 <b>(-31.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>234.90 (n/a)</td><td>183.50 (n/a)</td><td>190.20 (n/a)</td><td>139.60 (n/a)</td><td>42.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (+8.55%)</td><td>0.25 (-1.60%)</td><td>0.21 (-15.48%)</td><td>0.20 (+4.99%)</td><td>0.05 <b>(+38.67%)</b></td><td>247.40 (-4.74%)</td><td>205.78 (+3.02%)</td><td>229.50 (+18.30%)</td><td>157.40 (-7.85%)</td><td>41.51 (+17.29%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>259.70 (n/a)</td><td>199.74 (n/a)</td><td>194.00 (n/a)</td><td>170.80 (n/a)</td><td>35.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (-1.07%)</td><td>0.25 (-1.40%)</td><td>0.22 (-3.72%)</td><td>0.16 (+11.32%)</td><td>0.07 (-10.08%)</td><td>304.10 (-10.19%)</td><td>211.46 (-0.85%)</td><td>219.50 (+3.83%)</td><td>150.00 (+1.08%)</td><td>61.28 (-19.61%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>338.60 (n/a)</td><td>213.28 (n/a)</td><td>211.40 (n/a)</td><td>148.40 (n/a)</td><td>76.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-2.22%)</td><td>0.02 (+1.93%)</td><td>0.02 (+5.30%)</td><td>0.01 (+5.62%)</td><td>0.00 (-19.42%)</td><td>183.80 (-5.36%)</td><td>149.94 (-3.08%)</td><td>146.20 (-5.06%)</td><td>120.70 (+2.29%)</td><td>24.31 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>154.70 (n/a)</td><td>154.00 (n/a)</td><td>118.00 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-8.53%)</td><td>0.02 (-6.68%)</td><td>0.02 (+3.18%)</td><td>0.01 <b>(-31.15%)</b></td><td>0.00 <b>(+100.40%)</b></td><td>209.90 <b>(+45.26%)</b></td><td>147.00 (+10.44%)</td><td>132.80 (-3.14%)</td><td>127.30 (+9.36%)</td><td>35.31 <b>(+229.17%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>144.50 (n/a)</td><td>133.10 (n/a)</td><td>137.10 (n/a)</td><td>116.40 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 <b>(+20.63%)</b></td><td>0.02 (+19.79%)</td><td>0.02 (+12.58%)</td><td>0.02 <b>(+27.97%)</b></td><td>0.00 (-8.35%)</td><td>152.30 <b>(-21.82%)</b></td><td>143.80 (-16.83%)</td><td>147.20 (-11.16%)</td><td>126.50 (-17.16%)</td><td>10.13 <b>(-41.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>172.90 (n/a)</td><td>165.70 (n/a)</td><td>152.70 (n/a)</td><td>17.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-10.04%)</td><td>0.01 (-4.41%)</td><td>0.02 (+10.06%)</td><td>0.01 <b>(-34.69%)</b></td><td>0.00 <b>(+46.37%)</b></td><td>312.00 <b>(+53.09%)</b></td><td>193.98 (+9.85%)</td><td>165.00 (-9.14%)</td><td>155.60 (+11.14%)</td><td>66.26 <b>(+160.65%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>176.58 (n/a)</td><td>181.60 (n/a)</td><td>140.00 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (+19.39%)</td><td>0.02 (+19.56%)</td><td>0.02 (+11.64%)</td><td>0.02 <b>(+32.77%)</b></td><td>0.00 (-16.55%)</td><td>164.20 <b>(-24.68%)</b></td><td>152.64 (-16.79%)</td><td>157.10 (-10.43%)</td><td>139.00 (-16.21%)</td><td>10.38 <b>(-48.72%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>183.44 (n/a)</td><td>175.40 (n/a)</td><td>165.90 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-1.04%)</td><td>0.02 (+3.37%)</td><td>0.02 (+8.03%)</td><td>0.01 (-15.54%)</td><td>0.00 <b>(+37.93%)</b></td><td>246.70 (+18.38%)</td><td>176.80 (-1.52%)</td><td>160.40 (-7.44%)</td><td>151.50 (+1.07%)</td><td>39.51 <b>(+68.68%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>179.52 (n/a)</td><td>173.30 (n/a)</td><td>149.90 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 <b>(+36.85%)</b></td><td>0.02 <b>(+30.04%)</b></td><td>0.02 <b>(+28.93%)</b></td><td>0.01 <b>(+30.30%)</b></td><td>0.00 <b>(+77.62%)</b></td><td>178.90 <b>(-23.25%)</b></td><td>156.68 <b>(-22.77%)</b></td><td>151.70 <b>(-22.44%)</b></td><td>139.10 <b>(-26.94%)</b></td><td>17.69 (-0.66%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>202.88 (n/a)</td><td>195.60 (n/a)</td><td>190.40 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 <b>(+47.35%)</b></td><td>0.01 <b>(+39.20%)</b></td><td>0.01 <b>(+22.27%)</b></td><td>0.01 <b>(+73.48%)</b></td><td>0.00 (-8.85%)</td><td>194.10 <b>(-42.35%)</b></td><td>178.96 <b>(-29.38%)</b></td><td>184.60 (-18.21%)</td><td>150.80 <b>(-32.13%)</b></td><td>17.62 <b>(-64.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>336.70 (n/a)</td><td>253.40 (n/a)</td><td>225.70 (n/a)</td><td>222.20 (n/a)</td><td>49.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (+17.34%)</td><td>0.03 (+7.06%)</td><td>0.03 (+7.38%)</td><td>0.03 (-9.37%)</td><td>0.01 <b>(+116.45%)</b></td><td>207.50 (+10.37%)</td><td>166.70 (-5.08%)</td><td>163.70 (-6.88%)</td><td>132.10 (-14.77%)</td><td>27.13 <b>(+104.35%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>175.62 (n/a)</td><td>175.80 (n/a)</td><td>155.00 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (+2.73%)</td><td>0.04 (+15.76%)</td><td>0.04 (+19.69%)</td><td>0.03 <b>(+27.91%)</b></td><td>0.00 <b>(-37.66%)</b></td><td>166.30 <b>(-21.81%)</b></td><td>149.56 (-14.97%)</td><td>145.20 (-16.46%)</td><td>134.70 (-2.67%)</td><td>13.95 <b>(-52.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>175.90 (n/a)</td><td>173.80 (n/a)</td><td>138.40 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(+46.73%)</b></td><td>0.03 <b>(+36.67%)</b></td><td>0.03 <b>(+31.19%)</b></td><td>0.03 <b>(+48.81%)</b></td><td>0.01 <b>(+41.26%)</b></td><td>206.90 <b>(-32.80%)</b></td><td>158.30 <b>(-27.13%)</b></td><td>151.40 <b>(-23.80%)</b></td><td>125.70 <b>(-31.87%)</b></td><td>32.79 <b>(-36.61%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>307.90 (n/a)</td><td>217.24 (n/a)</td><td>198.70 (n/a)</td><td>184.50 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-3.09%)</td><td>0.04 <b>(+26.36%)</b></td><td>0.03 <b>(+31.08%)</b></td><td>0.03 <b>(+52.32%)</b></td><td>0.00 <b>(-66.55%)</b></td><td>155.00 <b>(-34.35%)</b></td><td>146.70 <b>(-23.56%)</b></td><td>152.10 <b>(-23.72%)</b></td><td>135.70 (+3.19%)</td><td>9.01 <b>(-76.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>191.92 (n/a)</td><td>199.40 (n/a)</td><td>131.50 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-2.76%)</td><td>0.03 (+5.87%)</td><td>0.03 (+11.94%)</td><td>0.02 (-2.93%)</td><td>0.01 (-16.33%)</td><td>220.50 (+2.99%)</td><td>170.36 (-6.34%)</td><td>168.50 (-10.66%)</td><td>134.90 (+2.82%)</td><td>31.23 (-10.61%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>181.90 (n/a)</td><td>188.60 (n/a)</td><td>131.20 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-13.29%)</td><td>0.03 (-4.43%)</td><td>0.03 (+4.22%)</td><td>0.02 (-1.64%)</td><td>0.00 <b>(-28.57%)</b></td><td>224.20 (+1.63%)</td><td>178.22 (+3.28%)</td><td>164.20 (-4.03%)</td><td>151.70 (+15.27%)</td><td>29.75 (-15.64%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>172.56 (n/a)</td><td>171.10 (n/a)</td><td>131.60 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (+15.39%)</td><td>0.03 (+9.65%)</td><td>0.03 (+9.85%)</td><td>0.02 (-5.89%)</td><td>0.01 <b>(+32.57%)</b></td><td>226.80 (+6.28%)</td><td>164.34 (-7.51%)</td><td>158.10 (-8.98%)</td><td>128.80 (-13.32%)</td><td>37.05 <b>(+28.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>177.68 (n/a)</td><td>173.70 (n/a)</td><td>148.60 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-13.24%)</td><td>0.02 (-6.46%)</td><td>0.02 (-5.60%)</td><td>0.02 (-5.45%)</td><td>0.00 <b>(-36.07%)</b></td><td>245.80 (+5.77%)</td><td>225.56 (+6.16%)</td><td>233.80 (+5.94%)</td><td>191.90 (+15.26%)</td><td>20.63 <b>(-21.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.40 (n/a)</td><td>212.48 (n/a)</td><td>220.70 (n/a)</td><td>166.50 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (-11.65%)</td><td>0.07 (+1.12%)</td><td>0.07 (+17.56%)</td><td>0.06 (+7.41%)</td><td>0.01 <b>(-52.95%)</b></td><td>163.70 (-6.88%)</td><td>150.02 (-2.98%)</td><td>146.70 (-14.96%)</td><td>137.70 (+13.24%)</td><td>12.94 <b>(-50.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>154.62 (n/a)</td><td>172.50 (n/a)</td><td>121.60 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+7.05%)</td><td>0.06 (+5.33%)</td><td>0.06 (-0.34%)</td><td>0.04 (+12.67%)</td><td>0.01 (-2.05%)</td><td>270.50 (-11.25%)</td><td>185.32 (-6.25%)</td><td>169.80 (+0.30%)</td><td>140.60 (-6.58%)</td><td>50.28 (-18.93%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.80 (n/a)</td><td>197.68 (n/a)</td><td>169.30 (n/a)</td><td>150.50 (n/a)</td><td>62.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (+4.74%)</td><td>0.07 (+10.58%)</td><td>0.07 (+11.57%)</td><td>0.06 <b>(+20.16%)</b></td><td>0.01 <b>(-23.83%)</b></td><td>166.90 (-16.80%)</td><td>149.36 (-11.12%)</td><td>158.60 (-10.34%)</td><td>120.20 (-4.53%)</td><td>19.36 <b>(-39.93%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>168.04 (n/a)</td><td>176.90 (n/a)</td><td>125.90 (n/a)</td><td>32.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 <b>(+24.19%)</b></td><td>0.06 (+0.46%)</td><td>0.06 (+3.27%)</td><td>0.04 <b>(-24.28%)</b></td><td>0.02 <b>(+201.94%)</b></td><td>257.80 <b>(+32.07%)</b></td><td>184.50 (+4.20%)</td><td>175.80 (-3.14%)</td><td>126.90 (-19.48%)</td><td>47.33 <b>(+225.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>177.06 (n/a)</td><td>181.50 (n/a)</td><td>157.60 (n/a)</td><td>14.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (-13.32%)</td><td>0.06 (-5.66%)</td><td>0.06 (+18.69%)</td><td>0.05 (+0.63%)</td><td>0.01 <b>(-43.95%)</b></td><td>203.70 (-0.63%)</td><td>170.22 (+1.04%)</td><td>169.70 (-15.74%)</td><td>126.90 (+15.36%)</td><td>28.73 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>205.00 (n/a)</td><td>168.46 (n/a)</td><td>201.40 (n/a)</td><td>110.00 (n/a)</td><td>47.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+7.64%)</td><td>0.06 (-6.13%)</td><td>0.05 (-10.66%)</td><td>0.05 (-4.50%)</td><td>0.01 <b>(+30.98%)</b></td><td>229.30 (+4.70%)</td><td>193.28 (+7.87%)</td><td>196.00 (+11.94%)</td><td>143.40 (-7.12%)</td><td>36.10 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>179.18 (n/a)</td><td>175.10 (n/a)</td><td>154.40 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (-17.53%)</td><td>0.06 (+7.23%)</td><td>0.06 (+14.38%)</td><td>0.05 (+13.18%)</td><td>0.01 <b>(-42.67%)</b></td><td>227.30 (-11.63%)</td><td>170.58 (-11.03%)</td><td>166.30 (-12.57%)</td><td>134.50 <b>(+21.28%)</b></td><td>35.26 <b>(-33.64%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>257.20 (n/a)</td><td>191.72 (n/a)</td><td>190.20 (n/a)</td><td>110.90 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 <b>(+35.95%)</b></td><td>0.05 (+16.31%)</td><td>0.06 <b>(+25.16%)</b></td><td>0.04 (-10.14%)</td><td>0.01 <b>(+755.87%)</b></td><td>257.20 (+11.25%)</td><td>197.88 (-11.29%)</td><td>178.10 <b>(-20.10%)</b></td><td>158.00 <b>(-26.44%)</b></td><td>40.89 <b>(+604.10%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>231.20 (n/a)</td><td>223.06 (n/a)</td><td>222.90 (n/a)</td><td>214.80 (n/a)</td><td>5.81 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 <b>(+40.95%)</b></td><td>0.15 <b>(+22.40%)</b></td><td>0.14 (+13.69%)</td><td>0.12 (+9.28%)</td><td>0.03 <b>(+289.07%)</b></td><td>170.20 (-8.49%)</td><td>143.86 (-16.69%)</td><td>151.00 (-12.06%)</td><td>114.90 <b>(-29.03%)</b></td><td>23.16 <b>(+149.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>172.68 (n/a)</td><td>171.70 (n/a)</td><td>161.90 (n/a)</td><td>9.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 <b>(-33.36%)</b></td><td>0.14 (-8.51%)</td><td>0.13 (+5.15%)</td><td>0.12 (-0.25%)</td><td>0.01 <b>(-78.56%)</b></td><td>171.30 (+0.23%)</td><td>155.72 (+4.52%)</td><td>155.80 (-4.94%)</td><td>143.10 <b>(+50.00%)</b></td><td>10.35 <b>(-67.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>170.90 (n/a)</td><td>148.98 (n/a)</td><td>163.90 (n/a)</td><td>95.40 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (+2.97%)</td><td>0.13 (+11.09%)</td><td>0.14 (+17.82%)</td><td>0.10 (+7.06%)</td><td>0.02 (+3.88%)</td><td>211.90 (-6.57%)</td><td>164.00 (-10.01%)</td><td>154.90 (-15.12%)</td><td>141.90 (-2.87%)</td><td>28.75 (-5.48%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>182.24 (n/a)</td><td>182.50 (n/a)</td><td>146.10 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (-12.22%)</td><td>0.13 (-7.01%)</td><td>0.12 (-6.57%)</td><td>0.11 (+17.47%)</td><td>0.02 <b>(-43.61%)</b></td><td>189.70 (-14.86%)</td><td>166.24 (+4.04%)</td><td>173.20 (+6.98%)</td><td>133.30 (+13.93%)</td><td>21.79 <b>(-46.25%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>222.80 (n/a)</td><td>159.78 (n/a)</td><td>161.90 (n/a)</td><td>117.00 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (-1.14%)</td><td>0.14 (-0.03%)</td><td>0.14 (+8.43%)</td><td>0.12 (+1.86%)</td><td>0.02 (-9.60%)</td><td>177.30 (-1.83%)</td><td>153.30 (-0.22%)</td><td>146.80 (-7.79%)</td><td>129.70 (+1.17%)</td><td>18.60 (-8.90%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>180.60 (n/a)</td><td>153.64 (n/a)</td><td>159.20 (n/a)</td><td>128.20 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (+7.89%)</td><td>0.15 (+17.45%)</td><td>0.15 (+15.11%)</td><td>0.12 (+17.97%)</td><td>0.02 (-3.11%)</td><td>176.70 (-15.25%)</td><td>146.44 (-15.66%)</td><td>144.40 (-13.12%)</td><td>121.80 (-7.31%)</td><td>24.55 <b>(-27.99%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>208.50 (n/a)</td><td>173.64 (n/a)</td><td>166.20 (n/a)</td><td>131.40 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (+6.57%)</td><td>0.14 (+8.88%)</td><td>0.14 (+15.52%)</td><td>0.10 (-7.54%)</td><td>0.03 <b>(+32.98%)</b></td><td>209.80 (+8.14%)</td><td>155.14 (-6.80%)</td><td>149.60 (-13.43%)</td><td>123.20 (-6.17%)</td><td>33.00 <b>(+41.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>166.46 (n/a)</td><td>172.80 (n/a)</td><td>131.30 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (+0.77%)</td><td>0.10 (-0.26%)</td><td>0.10 (-9.63%)</td><td>0.09 <b>(+38.40%)</b></td><td>0.01 <b>(-47.73%)</b></td><td>225.00 <b>(-27.75%)</b></td><td>211.88 (-2.95%)</td><td>219.70 (+10.62%)</td><td>177.40 (-0.78%)</td><td>19.79 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>311.40 (n/a)</td><td>218.32 (n/a)</td><td>198.60 (n/a)</td><td>178.80 (n/a)</td><td>54.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>150.46 (n/a)</td><td>146.70 (n/a)</td><td>120.10 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>175.42 (n/a)</td><td>167.40 (n/a)</td><td>133.20 (n/a)</td><td>34.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>164.56 (n/a)</td><td>176.30 (n/a)</td><td>127.30 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>309.40 (n/a)</td><td>197.88 (n/a)</td><td>163.50 (n/a)</td><td>145.30 (n/a)</td><td>69.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>382.40 (n/a)</td><td>195.46 (n/a)</td><td>151.90 (n/a)</td><td>129.20 (n/a)</td><td>105.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>162.02 (n/a)</td><td>161.00 (n/a)</td><td>144.30 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>162.00 (n/a)</td><td>161.60 (n/a)</td><td>135.10 (n/a)</td><td>21.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>298.30 (n/a)</td><td>206.76 (n/a)</td><td>203.40 (n/a)</td><td>121.00 (n/a)</td><td>81.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>340.10 (n/a)</td><td>230.82 (n/a)</td><td>219.00 (n/a)</td><td>140.30 (n/a)</td><td>75.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>261.60 (n/a)</td><td>205.96 (n/a)</td><td>220.60 (n/a)</td><td>135.20 (n/a)</td><td>51.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>252.80 (n/a)</td><td>203.80 (n/a)</td><td>219.70 (n/a)</td><td>147.30 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>245.30 (n/a)</td><td>194.32 (n/a)</td><td>196.00 (n/a)</td><td>126.90 (n/a)</td><td>44.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.34 (+2.85%)</td><td>0.27 (-6.89%)</td><td>0.26 (-7.54%)</td><td>0.19 <b>(-28.22%)</b></td><td>0.07 <b>(+130.35%)</b></td><td>264.30 <b>(+39.33%)</b></td><td>193.68 (+12.28%)</td><td>188.10 (+8.17%)</td><td>144.10 (-2.77%)</td><td>50.24 <b>(+205.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>189.70 (n/a)</td><td>172.50 (n/a)</td><td>173.90 (n/a)</td><td>148.20 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>176.30 (n/a)</td><td>158.74 (n/a)</td><td>157.00 (n/a)</td><td>138.30 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>209.40 (n/a)</td><td>181.78 (n/a)</td><td>189.00 (n/a)</td><td>148.70 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>199.70 (n/a)</td><td>171.36 (n/a)</td><td>182.90 (n/a)</td><td>105.90 (n/a)</td><td>38.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>147.64 (n/a)</td><td>141.30 (n/a)</td><td>123.90 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>165.10 (n/a)</td><td>140.12 (n/a)</td><td>132.80 (n/a)</td><td>124.30 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.20 (n/a)</td><td>170.90 (n/a)</td><td>161.50 (n/a)</td><td>133.90 (n/a)</td><td>43.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>169.12 (n/a)</td><td>164.10 (n/a)</td><td>124.40 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.00 (n/a)</td><td>144.40 (n/a)</td><td>131.90 (n/a)</td><td>120.30 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>162.44 (n/a)</td><td>175.00 (n/a)</td><td>124.90 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>163.20 (n/a)</td><td>168.60 (n/a)</td><td>129.80 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>187.52 (n/a)</td><td>184.90 (n/a)</td><td>156.20 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>186.40 (n/a)</td><td>165.02 (n/a)</td><td>183.70 (n/a)</td><td>108.50 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.00 (n/a)</td><td>175.38 (n/a)</td><td>178.80 (n/a)</td><td>141.20 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>196.90 (n/a)</td><td>158.34 (n/a)</td><td>172.50 (n/a)</td><td>119.20 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>217.50 (n/a)</td><td>174.26 (n/a)</td><td>170.10 (n/a)</td><td>119.30 (n/a)</td><td>38.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>188.10 (n/a)</td><td>161.76 (n/a)</td><td>173.70 (n/a)</td><td>130.30 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>206.90 (n/a)</td><td>183.54 (n/a)</td><td>190.30 (n/a)</td><td>135.80 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>263.70 (n/a)</td><td>208.02 (n/a)</td><td>211.40 (n/a)</td><td>132.00 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>160.86 (n/a)</td><td>153.80 (n/a)</td><td>115.60 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.40 (n/a)</td><td>153.86 (n/a)</td><td>157.60 (n/a)</td><td>128.80 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>169.90 (n/a)</td><td>177.00 (n/a)</td><td>134.00 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.30 (n/a)</td><td>190.30 (n/a)</td><td>186.00 (n/a)</td><td>170.00 (n/a)</td><td>20.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>187.48 (n/a)</td><td>183.70 (n/a)</td><td>167.30 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.30 (n/a)</td><td>196.64 (n/a)</td><td>205.80 (n/a)</td><td>171.70 (n/a)</td><td>15.74 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>194.58 (n/a)</td><td>190.00 (n/a)</td><td>171.70 (n/a)</td><td>19.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.10 (n/a)</td><td>212.08 (n/a)</td><td>225.40 (n/a)</td><td>181.00 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>165.02 (n/a)</td><td>169.70 (n/a)</td><td>135.10 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>182.36 (n/a)</td><td>176.00 (n/a)</td><td>144.50 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>169.72 (n/a)</td><td>178.80 (n/a)</td><td>138.60 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>167.70 (n/a)</td><td>160.40 (n/a)</td><td>136.40 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.60 (n/a)</td><td>172.10 (n/a)</td><td>172.10 (n/a)</td><td>158.30 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>193.56 (n/a)</td><td>207.10 (n/a)</td><td>148.40 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>189.14 (n/a)</td><td>179.90 (n/a)</td><td>121.50 (n/a)</td><td>46.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.60 (n/a)</td><td>221.02 (n/a)</td><td>224.30 (n/a)</td><td>201.30 (n/a)</td><td>11.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>182.02 (n/a)</td><td>177.10 (n/a)</td><td>173.30 (n/a)</td><td>10.65 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>219.00 (n/a)</td><td>173.98 (n/a)</td><td>192.90 (n/a)</td><td>104.00 (n/a)</td><td>44.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>252.20 (n/a)</td><td>178.80 (n/a)</td><td>169.40 (n/a)</td><td>133.90 (n/a)</td><td>44.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>162.02 (n/a)</td><td>170.50 (n/a)</td><td>113.00 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.00 (n/a)</td><td>169.94 (n/a)</td><td>168.30 (n/a)</td><td>132.90 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>192.24 (n/a)</td><td>203.60 (n/a)</td><td>150.30 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>185.90 (n/a)</td><td>182.30 (n/a)</td><td>150.10 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.70 (n/a)</td><td>227.66 (n/a)</td><td>225.80 (n/a)</td><td>203.40 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>227.70 (n/a)</td><td>176.18 (n/a)</td><td>169.30 (n/a)</td><td>146.60 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>172.00 (n/a)</td><td>149.20 (n/a)</td><td>169.20 (n/a)</td><td>105.20 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>244.10 (n/a)</td><td>164.48 (n/a)</td><td>150.50 (n/a)</td><td>105.30 (n/a)</td><td>53.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.90 (n/a)</td><td>160.88 (n/a)</td><td>173.00 (n/a)</td><td>116.40 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>282.60 (n/a)</td><td>205.88 (n/a)</td><td>195.60 (n/a)</td><td>156.10 (n/a)</td><td>48.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>172.74 (n/a)</td><td>171.00 (n/a)</td><td>157.10 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>182.02 (n/a)</td><td>186.80 (n/a)</td><td>147.70 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>280.70 (n/a)</td><td>214.62 (n/a)</td><td>224.80 (n/a)</td><td>165.50 (n/a)</td><td>49.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>4.25 (+1.43%)</td><td>3.99 (-0.80%)</td><td>4.12 (+0.36%)</td><td>3.61 (-6.09%)</td><td>0.28 <b>(+78.03%)</b></td><td>2604.30 (+6.48%)</td><td>2365.86 (+1.10%)</td><td>2280.60 (-0.36%)</td><td>2210.70 (-1.41%)</td><td>174.07 <b>(+85.19%)</b></td><td>1673.39 (+1.43%)</td><td>1570.24 (-0.80%)</td><td>1622.09 (+0.36%)</td><td>1420.49 (-6.09%)</td><td>112.08 <b>(+78.03%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.19 (n/a)</td><td>4.02 (n/a)</td><td>4.11 (n/a)</td><td>3.85 (n/a)</td><td>0.16 (n/a)</td><td>2445.80 (n/a)</td><td>2340.18 (n/a)</td><td>2288.90 (n/a)</td><td>2242.30 (n/a)</td><td>93.99 (n/a)</td><td>1649.83 (n/a)</td><td>1582.83 (n/a)</td><td>1616.23 (n/a)</td><td>1512.55 (n/a)</td><td>62.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.12 (+7.34%)</td><td>0.95 (+0.04%)</td><td>0.95 (+2.03%)</td><td>0.67 (-18.13%)</td><td>0.18 <b>(+91.47%)</b></td><td>331.00 <b>(+22.14%)</b></td><td>240.58 (+2.62%)</td><td>232.00 (-1.99%)</td><td>197.50 (-6.84%)</td><td>54.02 <b>(+122.25%)</b></td><td>47.78 (+7.34%)</td><td>40.60 (+0.04%)</td><td>40.68 (+2.03%)</td><td>28.51 (-18.13%)</td><td>7.75 <b>(+91.47%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.04 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.09 (n/a)</td><td>271.00 (n/a)</td><td>234.44 (n/a)</td><td>236.70 (n/a)</td><td>212.00 (n/a)</td><td>24.31 (n/a)</td><td>44.51 (n/a)</td><td>40.59 (n/a)</td><td>39.87 (n/a)</td><td>34.82 (n/a)</td><td>4.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.06 (-12.68%)</td><td>0.85 (-5.39%)</td><td>0.92 (-9.28%)</td><td>0.64 (+6.77%)</td><td>0.19 <b>(-28.35%)</b></td><td>344.50 (-6.33%)</td><td>270.76 (+1.96%)</td><td>239.80 (+10.25%)</td><td>209.10 (+14.51%)</td><td>65.52 <b>(-24.21%)</b></td><td>45.14 (-12.68%)</td><td>36.46 (-5.39%)</td><td>39.36 (-9.28%)</td><td>27.39 (+6.77%)</td><td>8.31 <b>(-28.35%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.21 (n/a)</td><td>0.90 (n/a)</td><td>1.02 (n/a)</td><td>0.60 (n/a)</td><td>0.27 (n/a)</td><td>367.80 (n/a)</td><td>265.56 (n/a)</td><td>217.50 (n/a)</td><td>182.60 (n/a)</td><td>86.46 (n/a)</td><td>51.69 (n/a)</td><td>38.54 (n/a)</td><td>43.39 (n/a)</td><td>25.66 (n/a)</td><td>11.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.52 (+0.42%)</td><td>0.52 (-0.04%)</td><td>0.52 (-0.01%)</td><td>0.52 (-0.38%)</td><td>0.00 <b>(+1623.74%)</b></td><td>48644.30 (+0.38%)</td><td>48468.48 (+0.04%)</td><td>48456.70 (+0.01%)</td><td>48232.90 (-0.42%)</td><td>153.44 <b>(+1624.54%)</b></td><td>356.19 (+0.42%)</td><td>354.46 (-0.04%)</td><td>354.54 (-0.01%)</td><td>353.17 (-0.38%)</td><td>1.12 <b>(+1624.69%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48460.00 (n/a)</td><td>48449.92 (n/a)</td><td>48450.00 (n/a)</td><td>48435.90 (n/a)</td><td>8.90 (n/a)</td><td>354.69 (n/a)</td><td>354.59 (n/a)</td><td>354.59 (n/a)</td><td>354.52 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (+0.44%)</td><td>0.21 (+0.48%)</td><td>0.21 (+0.19%)</td><td>0.21 (+1.35%)</td><td>0.00 <b>(-40.21%)</b></td><td>119254.20 (-1.33%)</td><td>118282.04 (-0.48%)</td><td>118218.80 (-0.19%)</td><td>117447.20 (-0.44%)</td><td>691.15 <b>(-41.32%)</b></td><td>146.28 (+0.44%)</td><td>145.25 (+0.48%)</td><td>145.32 (+0.19%)</td><td>144.06 (+1.35%)</td><td>0.85 <b>(-40.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120861.50 (n/a)</td><td>118851.50 (n/a)</td><td>118439.60 (n/a)</td><td>117964.50 (n/a)</td><td>1177.81 (n/a)</td><td>145.64 (n/a)</td><td>144.56 (n/a)</td><td>145.05 (n/a)</td><td>142.15 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.90 (+0.64%)</td><td>0.89 (-0.04%)</td><td>0.89 (-0.10%)</td><td>0.88 (-0.42%)</td><td>0.01 <b>(+132.29%)</b></td><td>28490.20 (+0.42%)</td><td>28299.18 (+0.04%)</td><td>28317.90 (+0.10%)</td><td>28012.70 (-0.63%)</td><td>179.45 <b>(+131.59%)</b></td><td>613.29 (+0.64%)</td><td>607.10 (-0.04%)</td><td>606.68 (-0.10%)</td><td>603.01 (-0.42%)</td><td>3.87 <b>(+132.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28370.10 (n/a)</td><td>28287.10 (n/a)</td><td>28290.50 (n/a)</td><td>28190.90 (n/a)</td><td>77.48 (n/a)</td><td>609.41 (n/a)</td><td>607.34 (n/a)</td><td>607.27 (n/a)</td><td>605.56 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.53 (-0.22%)</td><td>3.41 (-1.30%)</td><td>3.38 (-3.32%)</td><td>3.34 (-0.29%)</td><td>0.08 (-7.54%)</td><td>7528.90 (+0.29%)</td><td>7381.44 (+1.31%)</td><td>7448.30 (+3.44%)</td><td>7122.30 (+0.22%)</td><td>175.53 (-7.03%)</td><td>2412.11 (-0.22%)</td><td>2328.51 (-1.30%)</td><td>2306.55 (-3.32%)</td><td>2281.87 (-0.29%)</td><td>56.12 (-7.54%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.54 (n/a)</td><td>3.46 (n/a)</td><td>3.49 (n/a)</td><td>3.35 (n/a)</td><td>0.09 (n/a)</td><td>7507.20 (n/a)</td><td>7285.68 (n/a)</td><td>7200.90 (n/a)</td><td>7106.60 (n/a)</td><td>188.81 (n/a)</td><td>2417.47 (n/a)</td><td>2359.30 (n/a)</td><td>2385.80 (n/a)</td><td>2288.45 (n/a)</td><td>60.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.17 (+4.96%)</td><td>2.92 (+4.27%)</td><td>2.87 (+4.01%)</td><td>2.81 (+5.68%)</td><td>0.15 (-2.49%)</td><td>8958.40 (-5.37%)</td><td>8641.14 (-4.12%)</td><td>8768.30 (-3.85%)</td><td>7929.90 (-4.73%)</td><td>415.61 (-12.85%)</td><td>2166.47 (+4.96%)</td><td>1992.04 (+4.27%)</td><td>1959.32 (+4.01%)</td><td>1917.73 (+5.68%)</td><td>101.14 (-2.49%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.02 (n/a)</td><td>2.80 (n/a)</td><td>2.76 (n/a)</td><td>2.66 (n/a)</td><td>0.15 (n/a)</td><td>9467.20 (n/a)</td><td>9012.80 (n/a)</td><td>9119.50 (n/a)</td><td>8323.40 (n/a)</td><td>476.89 (n/a)</td><td>2064.05 (n/a)</td><td>1910.55 (n/a)</td><td>1883.85 (n/a)</td><td>1814.67 (n/a)</td><td>103.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.32 (+0.40%)</td><td>3.18 (-0.28%)</td><td>3.16 (-0.26%)</td><td>3.08 (-1.73%)</td><td>0.09 <b>(+27.07%)</b></td><td>8157.50 (+1.76%)</td><td>7915.60 (+0.30%)</td><td>7959.60 (+0.26%)</td><td>7569.70 (-0.40%)</td><td>213.63 <b>(+28.58%)</b></td><td>2269.56 (+0.40%)</td><td>2171.67 (-0.28%)</td><td>2158.39 (-0.26%)</td><td>2106.01 (-1.73%)</td><td>59.79 <b>(+27.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.31 (n/a)</td><td>3.19 (n/a)</td><td>3.17 (n/a)</td><td>3.14 (n/a)</td><td>0.07 (n/a)</td><td>8016.10 (n/a)</td><td>7891.54 (n/a)</td><td>7938.60 (n/a)</td><td>7600.30 (n/a)</td><td>166.14 (n/a)</td><td>2260.41 (n/a)</td><td>2177.79 (n/a)</td><td>2164.10 (n/a)</td><td>2143.16 (n/a)</td><td>47.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.79 (+0.21%)</td><td>0.79 (+0.11%)</td><td>0.79 (+0.13%)</td><td>0.78 (+0.06%)</td><td>0.00 <b>(+31.96%)</b></td><td>96327.40 (-0.06%)</td><td>96117.82 (-0.11%)</td><td>96112.70 (-0.13%)</td><td>95903.80 (-0.21%)</td><td>150.56 <b>(+31.67%)</b></td><td>716.55 (+0.21%)</td><td>714.95 (+0.11%)</td><td>714.99 (+0.13%)</td><td>713.40 (+0.06%)</td><td>1.12 <b>(+31.96%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96380.50 (n/a)</td><td>96221.04 (n/a)</td><td>96234.50 (n/a)</td><td>96102.90 (n/a)</td><td>114.35 (n/a)</td><td>715.06 (n/a)</td><td>714.18 (n/a)</td><td>714.08 (n/a)</td><td>713.00 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.73 (+0.03%)</td><td>0.73 (+0.02%)</td><td>0.73 (+0.02%)</td><td>0.73 (+0.01%)</td><td>0.00 <b>(+24.77%)</b></td><td>103304.80 (-0.01%)</td><td>103290.16 (-0.02%)</td><td>103294.80 (-0.02%)</td><td>103256.70 (-0.03%)</td><td>19.21 <b>(+24.48%)</b></td><td>665.52 (+0.03%)</td><td>665.31 (+0.02%)</td><td>665.27 (+0.02%)</td><td>665.21 (+0.01%)</td><td>0.12 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103319.90 (n/a)</td><td>103306.78 (n/a)</td><td>103313.40 (n/a)</td><td>103285.20 (n/a)</td><td>15.43 (n/a)</td><td>665.34 (n/a)</td><td>665.20 (n/a)</td><td>665.16 (n/a)</td><td>665.11 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.70 (+0.64%)</td><td>0.70 (+0.20%)</td><td>0.69 (+0.09%)</td><td>0.69 (+0.06%)</td><td>0.00 <b>(+128.83%)</b></td><td>109054.50 (-0.06%)</td><td>108609.04 (-0.19%)</td><td>108793.40 (-0.09%)</td><td>107851.50 (-0.64%)</td><td>519.48 <b>(+127.33%)</b></td><td>637.17 (+0.64%)</td><td>632.74 (+0.20%)</td><td>631.65 (+0.09%)</td><td>630.14 (+0.06%)</td><td>3.03 <b>(+128.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109124.80 (n/a)</td><td>108821.16 (n/a)</td><td>108888.40 (n/a)</td><td>108543.10 (n/a)</td><td>228.51 (n/a)</td><td>633.11 (n/a)</td><td>631.49 (n/a)</td><td>631.10 (n/a)</td><td>629.73 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.27 (+1.39%)</td><td>6.76 (+1.45%)</td><td>6.92 (+5.15%)</td><td>5.89 (-2.77%)</td><td>0.57 <b>(+24.82%)</b></td><td>1513.00 (+2.85%)</td><td>1325.52 (-1.21%)</td><td>1287.70 (-4.90%)</td><td>1225.60 (-1.38%)</td><td>118.22 <b>(+27.42%)</b></td><td>438.04 (+1.39%)</td><td>407.46 (+1.45%)</td><td>416.92 (+5.15%)</td><td>354.83 (-2.77%)</td><td>34.25 <b>(+24.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.17 (n/a)</td><td>6.67 (n/a)</td><td>6.58 (n/a)</td><td>6.06 (n/a)</td><td>0.46 (n/a)</td><td>1471.10 (n/a)</td><td>1341.80 (n/a)</td><td>1354.00 (n/a)</td><td>1242.70 (n/a)</td><td>92.78 (n/a)</td><td>432.01 (n/a)</td><td>401.63 (n/a)</td><td>396.52 (n/a)</td><td>364.94 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.97 (+0.91%)</td><td>6.67 (+4.04%)</td><td>6.78 (-1.21%)</td><td>6.07 <b>(+20.63%)</b></td><td>0.36 <b>(-54.58%)</b></td><td>1467.50 (-17.10%)</td><td>1340.26 (-5.04%)</td><td>1315.00 (+1.22%)</td><td>1278.00 (-0.90%)</td><td>76.69 <b>(-62.71%)</b></td><td>420.10 (+0.91%)</td><td>401.58 (+4.04%)</td><td>408.26 (-1.21%)</td><td>365.85 <b>(+20.63%)</b></td><td>21.87 <b>(-54.58%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.91 (n/a)</td><td>6.41 (n/a)</td><td>6.86 (n/a)</td><td>5.04 (n/a)</td><td>0.80 (n/a)</td><td>1770.20 (n/a)</td><td>1411.42 (n/a)</td><td>1299.20 (n/a)</td><td>1289.60 (n/a)</td><td>205.65 (n/a)</td><td>416.31 (n/a)</td><td>385.98 (n/a)</td><td>413.24 (n/a)</td><td>303.29 (n/a)</td><td>48.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.97 (-3.15%)</td><td>6.67 (+9.40%)</td><td>6.82 (+11.25%)</td><td>6.17 <b>(+27.05%)</b></td><td>0.33 <b>(-60.78%)</b></td><td>1445.10 <b>(-21.29%)</b></td><td>1338.48 (-9.86%)</td><td>1307.00 (-10.11%)</td><td>1278.20 (+3.26%)</td><td>67.79 <b>(-68.74%)</b></td><td>420.04 (-3.15%)</td><td>401.90 (+9.40%)</td><td>410.77 (+11.25%)</td><td>371.51 <b>(+27.05%)</b></td><td>19.66 <b>(-60.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.20 (n/a)</td><td>6.10 (n/a)</td><td>6.13 (n/a)</td><td>4.85 (n/a)</td><td>0.83 (n/a)</td><td>1836.00 (n/a)</td><td>1484.82 (n/a)</td><td>1454.00 (n/a)</td><td>1237.90 (n/a)</td><td>216.83 (n/a)</td><td>433.71 (n/a)</td><td>367.37 (n/a)</td><td>369.24 (n/a)</td><td>292.41 (n/a)</td><td>50.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.23 (+3.25%)</td><td>7.73 (+0.12%)</td><td>7.90 (+1.11%)</td><td>7.28 (+1.67%)</td><td>0.41 <b>(+27.97%)</b></td><td>4789.50 (-1.64%)</td><td>4519.06 (-0.04%)</td><td>4414.40 (-1.10%)</td><td>4234.10 (-3.14%)</td><td>243.05 <b>(+22.10%)</b></td><td>507.19 (+3.25%)</td><td>476.30 (+0.12%)</td><td>486.47 (+1.11%)</td><td>448.37 (+1.67%)</td><td>25.48 <b>(+27.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.98 (n/a)</td><td>7.72 (n/a)</td><td>7.81 (n/a)</td><td>7.16 (n/a)</td><td>0.32 (n/a)</td><td>4869.30 (n/a)</td><td>4520.70 (n/a)</td><td>4463.30 (n/a)</td><td>4371.50 (n/a)</td><td>199.05 (n/a)</td><td>491.24 (n/a)</td><td>475.73 (n/a)</td><td>481.15 (n/a)</td><td>441.02 (n/a)</td><td>19.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.97 (+3.77%)</td><td>7.53 (+1.70%)</td><td>7.57 (-0.27%)</td><td>6.89 (-1.91%)</td><td>0.40 <b>(+34.16%)</b></td><td>5058.10 (+1.95%)</td><td>4643.32 (-1.57%)</td><td>4608.60 (+0.27%)</td><td>4377.10 (-3.63%)</td><td>257.15 <b>(+32.71%)</b></td><td>490.62 (+3.77%)</td><td>463.58 (+1.70%)</td><td>465.97 (-0.27%)</td><td>424.56 (-1.91%)</td><td>24.75 <b>(+34.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.68 (n/a)</td><td>7.40 (n/a)</td><td>7.59 (n/a)</td><td>7.03 (n/a)</td><td>0.30 (n/a)</td><td>4961.30 (n/a)</td><td>4717.18 (n/a)</td><td>4596.40 (n/a)</td><td>4542.10 (n/a)</td><td>193.77 (n/a)</td><td>472.80 (n/a)</td><td>455.86 (n/a)</td><td>467.21 (n/a)</td><td>432.85 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.35 (+0.17%)</td><td>7.08 (-1.44%)</td><td>7.27 (-0.35%)</td><td>6.72 (-1.30%)</td><td>0.32 <b>(+43.79%)</b></td><td>5191.30 (+1.31%)</td><td>4935.10 (+1.55%)</td><td>4798.50 (+0.35%)</td><td>4743.50 (-0.17%)</td><td>223.76 <b>(+45.45%)</b></td><td>452.72 (+0.17%)</td><td>435.85 (-1.44%)</td><td>447.53 (-0.35%)</td><td>413.67 (-1.30%)</td><td>19.45 <b>(+43.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.34 (n/a)</td><td>7.18 (n/a)</td><td>7.29 (n/a)</td><td>6.80 (n/a)</td><td>0.22 (n/a)</td><td>5124.00 (n/a)</td><td>4859.98 (n/a)</td><td>4781.90 (n/a)</td><td>4751.40 (n/a)</td><td>153.84 (n/a)</td><td>451.97 (n/a)</td><td>442.22 (n/a)</td><td>449.09 (n/a)</td><td>419.11 (n/a)</td><td>13.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.79 (-0.10%)</td><td>0.79 (-0.10%)</td><td>0.79 (-0.07%)</td><td>0.79 (-0.24%)</td><td>0.00 <b>(+156.03%)</b></td><td>95660.40 (+0.24%)</td><td>95484.46 (+0.10%)</td><td>95440.10 (+0.07%)</td><td>95432.00 (+0.10%)</td><td>98.86 <b>(+157.04%)</b></td><td>720.09 (-0.10%)</td><td>719.69 (-0.10%)</td><td>720.03 (-0.07%)</td><td>718.37 (-0.24%)</td><td>0.74 <b>(+156.03%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95431.10 (n/a)</td><td>95387.76 (n/a)</td><td>95374.30 (n/a)</td><td>95339.30 (n/a)</td><td>38.46 (n/a)</td><td>720.79 (n/a)</td><td>720.42 (n/a)</td><td>720.52 (n/a)</td><td>720.10 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.74 (+0.02%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.02%)</td><td>0.74 (+0.07%)</td><td>0.00 <b>(-42.85%)</b></td><td>102614.60 (-0.07%)</td><td>102592.74 (-0.02%)</td><td>102606.20 (+0.02%)</td><td>102553.30 (-0.02%)</td><td>26.37 <b>(-42.93%)</b></td><td>670.09 (+0.02%)</td><td>669.83 (+0.02%)</td><td>669.74 (-0.02%)</td><td>669.68 (+0.07%)</td><td>0.17 <b>(-42.84%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102689.10 (n/a)</td><td>102610.24 (n/a)</td><td>102587.90 (n/a)</td><td>102576.50 (n/a)</td><td>46.20 (n/a)</td><td>669.93 (n/a)</td><td>669.71 (n/a)</td><td>669.86 (n/a)</td><td>669.20 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.71 (+0.36%)</td><td>0.70 (+0.20%)</td><td>0.70 (+0.13%)</td><td>0.70 (+0.17%)</td><td>0.00 <b>(+38.12%)</b></td><td>107655.10 (-0.17%)</td><td>107363.34 (-0.20%)</td><td>107392.10 (-0.13%)</td><td>107043.10 (-0.36%)</td><td>221.29 <b>(+37.38%)</b></td><td>641.98 (+0.36%)</td><td>640.07 (+0.20%)</td><td>639.89 (+0.13%)</td><td>638.33 (+0.17%)</td><td>1.32 <b>(+38.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107839.40 (n/a)</td><td>107582.54 (n/a)</td><td>107526.60 (n/a)</td><td>107426.10 (n/a)</td><td>161.08 (n/a)</td><td>639.69 (n/a)</td><td>638.76 (n/a)</td><td>639.09 (n/a)</td><td>637.24 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>4.21 (+2.43%)</td><td>3.85 (+15.66%)</td><td>3.78 <b>(+25.19%)</b></td><td>3.59 <b>(+21.38%)</b></td><td>0.26 <b>(-46.72%)</b></td><td>2242.90 (-17.62%)</td><td>2102.36 (-14.60%)</td><td>2132.60 <b>(-20.12%)</b></td><td>1916.60 (-2.37%)</td><td>140.71 <b>(-57.43%)</b></td><td>1102.97 (+2.43%)</td><td>1009.19 (+15.66%)</td><td>991.23 <b>(+25.19%)</b></td><td>942.48 <b>(+21.38%)</b></td><td>68.98 <b>(-46.72%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.11 (n/a)</td><td>3.33 (n/a)</td><td>3.02 (n/a)</td><td>2.96 (n/a)</td><td>0.49 (n/a)</td><td>2722.60 (n/a)</td><td>2461.90 (n/a)</td><td>2669.90 (n/a)</td><td>1963.20 (n/a)</td><td>330.55 (n/a)</td><td>1076.77 (n/a)</td><td>872.53 (n/a)</td><td>791.77 (n/a)</td><td>776.45 (n/a)</td><td>129.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.50 (+3.63%)</td><td>0.36 (-3.86%)</td><td>0.33 (-3.50%)</td><td>0.30 (-11.69%)</td><td>0.08 <b>(+31.00%)</b></td><td>4129.50 (+13.23%)</td><td>3580.06 (+5.60%)</td><td>3739.70 (+3.62%)</td><td>2469.20 (-3.50%)</td><td>653.54 <b>(+39.80%)</b></td><td>27.18 (+3.63%)</td><td>19.39 (-3.86%)</td><td>17.94 (-3.50%)</td><td>16.25 (-11.69%)</td><td>4.45 <b>(+31.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>3646.90 (n/a)</td><td>3390.32 (n/a)</td><td>3609.00 (n/a)</td><td>2558.80 (n/a)</td><td>467.47 (n/a)</td><td>26.23 (n/a)</td><td>20.17 (n/a)</td><td>18.59 (n/a)</td><td>18.40 (n/a)</td><td>3.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>5.37 (+12.73%)</td><td>4.86 (+16.77%)</td><td>4.78 (+8.65%)</td><td>4.63 <b>(+38.65%)</b></td><td>0.30 <b>(-55.27%)</b></td><td>1437.60 <b>(-27.88%)</b></td><td>1372.76 (-15.96%)</td><td>1390.40 (-7.96%)</td><td>1239.80 (-11.29%)</td><td>78.87 <b>(-71.31%)</b></td><td>1657.64 (+12.73%)</td><td>1501.34 (+16.77%)</td><td>1478.16 (+8.65%)</td><td>1429.57 <b>(+38.65%)</b></td><td>91.60 <b>(-55.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>4.76 (n/a)</td><td>4.16 (n/a)</td><td>4.40 (n/a)</td><td>3.34 (n/a)</td><td>0.66 (n/a)</td><td>1993.30 (n/a)</td><td>1633.44 (n/a)</td><td>1510.60 (n/a)</td><td>1397.60 (n/a)</td><td>274.96 (n/a)</td><td>1470.51 (n/a)</td><td>1285.71 (n/a)</td><td>1360.49 (n/a)</td><td>1031.07 (n/a)</td><td>204.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.29 (n/a)</td><td>12.84 (n/a)</td><td>13.16 (n/a)</td><td>12.21 (n/a)</td><td>0.54 (n/a)</td><td>13.28 (n/a)</td><td>12.84 (n/a)</td><td>13.15 (n/a)</td><td>12.20 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>24.51 (-1.01%)</td><td>24.12 (-1.69%)</td><td>24.04 (-1.89%)</td><td>23.77 (-1.80%)</td><td>0.28 <b>(+28.48%)</b></td><td>24.50 (-1.01%)</td><td>24.11 (-1.69%)</td><td>24.03 (-1.89%)</td><td>23.76 (-1.80%)</td><td>0.28 <b>(+28.48%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>24.76 (n/a)</td><td>24.53 (n/a)</td><td>24.50 (n/a)</td><td>24.21 (n/a)</td><td>0.22 (n/a)</td><td>24.75 (n/a)</td><td>24.52 (n/a)</td><td>24.49 (n/a)</td><td>24.19 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>40.47 (-4.31%)</td><td>39.86 (-2.99%)</td><td>40.02 (-2.23%)</td><td>39.24 (-2.30%)</td><td>0.51 <b>(-46.41%)</b></td><td>40.44 (-4.31%)</td><td>39.83 (-2.99%)</td><td>40.00 (-2.23%)</td><td>39.21 (-2.30%)</td><td>0.51 <b>(-46.41%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>42.29 (n/a)</td><td>41.09 (n/a)</td><td>40.94 (n/a)</td><td>40.16 (n/a)</td><td>0.94 (n/a)</td><td>42.27 (n/a)</td><td>41.06 (n/a)</td><td>40.91 (n/a)</td><td>40.14 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>43.04 (-6.87%)</td><td>41.07 (-4.86%)</td><td>41.59 (-4.09%)</td><td>38.17 (-4.17%)</td><td>1.82 (-19.96%)</td><td>43.02 (-6.87%)</td><td>41.04 (-4.86%)</td><td>41.56 (-4.09%)</td><td>38.15 (-4.17%)</td><td>1.82 (-19.96%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>46.22 (n/a)</td><td>43.17 (n/a)</td><td>43.36 (n/a)</td><td>39.83 (n/a)</td><td>2.28 (n/a)</td><td>46.19 (n/a)</td><td>43.14 (n/a)</td><td>43.34 (n/a)</td><td>39.80 (n/a)</td><td>2.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.13 (n/a)</td><td>12.16 (n/a)</td><td>12.50 (n/a)</td><td>10.17 (n/a)</td><td>1.15 (n/a)</td><td>13.13 (n/a)</td><td>12.15 (n/a)</td><td>12.49 (n/a)</td><td>10.17 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>24.57 (-0.34%)</td><td>24.23 (-0.79%)</td><td>24.16 (-0.68%)</td><td>23.80 (-1.81%)</td><td>0.32 <b>(+79.15%)</b></td><td>24.56 (-0.34%)</td><td>24.21 (-0.79%)</td><td>24.15 (-0.68%)</td><td>23.79 (-1.81%)</td><td>0.32 <b>(+79.15%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>24.65 (n/a)</td><td>24.42 (n/a)</td><td>24.33 (n/a)</td><td>24.24 (n/a)</td><td>0.18 (n/a)</td><td>24.64 (n/a)</td><td>24.40 (n/a)</td><td>24.31 (n/a)</td><td>24.23 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>41.20 (-4.79%)</td><td>39.79 (+0.17%)</td><td>39.67 (-1.82%)</td><td>38.85 (+7.21%)</td><td>1.00 <b>(-67.70%)</b></td><td>41.17 (-4.79%)</td><td>39.77 (+0.17%)</td><td>39.65 (-1.82%)</td><td>38.83 (+7.21%)</td><td>1.00 <b>(-67.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>43.27 (n/a)</td><td>39.73 (n/a)</td><td>40.41 (n/a)</td><td>36.24 (n/a)</td><td>3.10 (n/a)</td><td>43.24 (n/a)</td><td>39.70 (n/a)</td><td>40.38 (n/a)</td><td>36.21 (n/a)</td><td>3.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>43.83 (-1.20%)</td><td>42.98 (+2.07%)</td><td>42.96 (+0.50%)</td><td>42.37 (+7.68%)</td><td>0.56 <b>(-71.93%)</b></td><td>43.80 (-1.20%)</td><td>42.96 (+2.07%)</td><td>42.93 (+0.50%)</td><td>42.34 (+7.68%)</td><td>0.56 <b>(-71.93%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>44.36 (n/a)</td><td>42.11 (n/a)</td><td>42.74 (n/a)</td><td>39.35 (n/a)</td><td>2.01 (n/a)</td><td>44.34 (n/a)</td><td>42.09 (n/a)</td><td>42.72 (n/a)</td><td>39.32 (n/a)</td><td>2.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.57 (+4.34%)</td><td>8.90 (-0.57%)</td><td>8.88 (-0.00%)</td><td>8.41 (-4.74%)</td><td>0.45 <b>(+219.79%)</b></td><td>9.55 (+4.34%)</td><td>8.89 (-0.57%)</td><td>8.86 (-0.00%)</td><td>8.40 (-4.74%)</td><td>0.45 <b>(+219.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.17 (n/a)</td><td>8.95 (n/a)</td><td>8.88 (n/a)</td><td>8.83 (n/a)</td><td>0.14 (n/a)</td><td>9.16 (n/a)</td><td>8.94 (n/a)</td><td>8.86 (n/a)</td><td>8.81 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.87 (-9.71%)</td><td>0.85 (-3.01%)</td><td>0.84 (-7.14%)</td><td>0.83 (+17.81%)</td><td>0.02 <b>(-81.41%)</b></td><td>0.86 (-9.71%)</td><td>0.83 (-3.01%)</td><td>0.83 (-7.14%)</td><td>0.82 (+17.81%)</td><td>0.02 <b>(-81.41%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.97 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>0.70 (n/a)</td><td>0.10 (n/a)</td><td>0.95 (n/a)</td><td>0.86 (n/a)</td><td>0.89 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.32 (+11.86%)</td><td>1.12 (+5.13%)</td><td>1.10 (-1.52%)</td><td>0.98 (+8.57%)</td><td>0.12 (+8.03%)</td><td>1.30 (+11.86%)</td><td>1.11 (+5.13%)</td><td>1.08 (-1.52%)</td><td>0.97 (+8.57%)</td><td>0.12 (+8.03%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.18 (n/a)</td><td>1.07 (n/a)</td><td>1.11 (n/a)</td><td>0.91 (n/a)</td><td>0.11 (n/a)</td><td>1.17 (n/a)</td><td>1.05 (n/a)</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>19.00 (-4.81%)</td><td>16.25 (-2.87%)</td><td>16.25 (+0.04%)</td><td>12.68 (-14.55%)</td><td>2.33 (+18.58%)</td><td>18.78 (-4.81%)</td><td>16.07 (-2.87%)</td><td>16.06 (+0.04%)</td><td>12.54 (-14.55%)</td><td>2.30 (+18.58%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>19.96 (n/a)</td><td>16.73 (n/a)</td><td>16.24 (n/a)</td><td>14.84 (n/a)</td><td>1.96 (n/a)</td><td>19.73 (n/a)</td><td>16.54 (n/a)</td><td>16.05 (n/a)</td><td>14.67 (n/a)</td><td>1.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.28 (-1.28%)</td><td>13.38 (-2.40%)</td><td>13.36 (-2.12%)</td><td>12.48 (-5.44%)</td><td>0.64 (+18.58%)</td><td>14.03 (-1.28%)</td><td>13.14 (-2.40%)</td><td>13.13 (-2.12%)</td><td>12.26 (-5.44%)</td><td>0.63 (+18.58%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.46 (n/a)</td><td>13.71 (n/a)</td><td>13.65 (n/a)</td><td>13.20 (n/a)</td><td>0.54 (n/a)</td><td>14.21 (n/a)</td><td>13.47 (n/a)</td><td>13.41 (n/a)</td><td>12.97 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.09 (+6.24%)</td><td>7.80 (+1.93%)</td><td>7.45 (-7.38%)</td><td>6.79 (+17.54%)</td><td>0.93 (-18.67%)</td><td>8.93 (+6.24%)</td><td>7.66 (+1.93%)</td><td>7.32 (-7.38%)</td><td>6.68 (+17.54%)</td><td>0.91 (-18.67%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>8.56 (n/a)</td><td>7.65 (n/a)</td><td>8.04 (n/a)</td><td>5.78 (n/a)</td><td>1.14 (n/a)</td><td>8.41 (n/a)</td><td>7.52 (n/a)</td><td>7.90 (n/a)</td><td>5.68 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.23 (-4.58%)</td><td>5.29 (-6.33%)</td><td>5.47 (-8.51%)</td><td>4.42 (-0.55%)</td><td>0.70 (-15.27%)</td><td>6.13 (-4.58%)</td><td>5.20 (-6.33%)</td><td>5.38 (-8.51%)</td><td>4.34 (-0.55%)</td><td>0.69 (-15.27%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.52 (n/a)</td><td>5.64 (n/a)</td><td>5.98 (n/a)</td><td>4.44 (n/a)</td><td>0.83 (n/a)</td><td>6.42 (n/a)</td><td>5.55 (n/a)</td><td>5.88 (n/a)</td><td>4.37 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.13 (n/a)</td><td>12.49 (n/a)</td><td>12.47 (n/a)</td><td>11.76 (n/a)</td><td>0.57 (n/a)</td><td>13.12 (n/a)</td><td>12.49 (n/a)</td><td>12.46 (n/a)</td><td>11.75 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>12.86 (n/a)</td><td>11.77 (n/a)</td><td>11.79 (n/a)</td><td>10.99 (n/a)</td><td>0.76 (n/a)</td><td>12.85 (n/a)</td><td>11.76 (n/a)</td><td>11.78 (n/a)</td><td>10.98 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>175.44 (n/a)</td><td>188.30 (n/a)</td><td>129.60 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>300.00 (n/a)</td><td>184.68 (n/a)</td><td>160.10 (n/a)</td><td>137.60 (n/a)</td><td>66.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>172.04 (n/a)</td><td>168.40 (n/a)</td><td>166.70 (n/a)</td><td>7.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>176.56 (n/a)</td><td>152.00 (n/a)</td><td>136.30 (n/a)</td><td>47.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.00 (n/a)</td><td>177.52 (n/a)</td><td>173.10 (n/a)</td><td>143.20 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.00 (n/a)</td><td>202.00 (n/a)</td><td>198.50 (n/a)</td><td>156.40 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>173.60 (n/a)</td><td>186.00 (n/a)</td><td>124.20 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>355.90 (n/a)</td><td>268.28 (n/a)</td><td>289.20 (n/a)</td><td>148.10 (n/a)</td><td>87.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.00 (n/a)</td><td>158.96 (n/a)</td><td>169.10 (n/a)</td><td>127.70 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>170.80 (n/a)</td><td>176.20 (n/a)</td><td>110.10 (n/a)</td><td>40.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>280.60 (n/a)</td><td>171.30 (n/a)</td><td>166.90 (n/a)</td><td>112.40 (n/a)</td><td>65.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>153.48 (n/a)</td><td>153.10 (n/a)</td><td>111.30 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>183.70 (n/a)</td><td>190.30 (n/a)</td><td>128.20 (n/a)</td><td>36.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>179.00 (n/a)</td><td>193.60 (n/a)</td><td>118.90 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>194.96 (n/a)</td><td>204.20 (n/a)</td><td>168.50 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>202.92 (n/a)</td><td>210.30 (n/a)</td><td>164.10 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>175.32 (n/a)</td><td>182.80 (n/a)</td><td>128.40 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>162.54 (n/a)</td><td>168.10 (n/a)</td><td>122.90 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>156.46 (n/a)</td><td>156.00 (n/a)</td><td>140.20 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.50 (n/a)</td><td>182.32 (n/a)</td><td>165.00 (n/a)</td><td>133.90 (n/a)</td><td>42.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>158.96 (n/a)</td><td>157.10 (n/a)</td><td>123.40 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>187.24 (n/a)</td><td>180.10 (n/a)</td><td>154.10 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>303.10 (n/a)</td><td>212.40 (n/a)</td><td>199.40 (n/a)</td><td>156.90 (n/a)</td><td>54.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>222.92 (n/a)</td><td>225.30 (n/a)</td><td>195.30 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>239.30 (n/a)</td><td>181.88 (n/a)</td><td>165.10 (n/a)</td><td>141.20 (n/a)</td><td>43.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>176.28 (n/a)</td><td>164.60 (n/a)</td><td>160.50 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.10 (n/a)</td><td>162.54 (n/a)</td><td>152.30 (n/a)</td><td>131.60 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>354.90 (n/a)</td><td>207.34 (n/a)</td><td>180.30 (n/a)</td><td>142.80 (n/a)</td><td>84.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>260.40 (n/a)</td><td>188.50 (n/a)</td><td>186.20 (n/a)</td><td>150.70 (n/a)</td><td>44.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>253.30 (n/a)</td><td>180.62 (n/a)</td><td>166.00 (n/a)</td><td>129.30 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.00 (n/a)</td><td>180.38 (n/a)</td><td>175.30 (n/a)</td><td>131.60 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>246.90 (n/a)</td><td>205.56 (n/a)</td><td>203.10 (n/a)</td><td>167.10 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+7.59%)</td><td>0.03 (+3.50%)</td><td>0.02 (-15.28%)</td><td>0.02 <b>(+24.92%)</b></td><td>0.00 (-15.52%)</td><td>177.60 (-19.93%)</td><td>159.50 (-4.84%)</td><td>174.20 (+18.02%)</td><td>126.10 (-7.07%)</td><td>22.77 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>167.62 (n/a)</td><td>147.60 (n/a)</td><td>135.70 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-14.16%)</td><td>0.02 (-8.94%)</td><td>0.02 (-12.13%)</td><td>0.02 (+3.19%)</td><td>0.00 <b>(-45.87%)</b></td><td>239.20 (-3.12%)</td><td>200.50 (+7.75%)</td><td>194.70 (+13.79%)</td><td>181.60 (+16.56%)</td><td>23.14 <b>(-38.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.90 (n/a)</td><td>186.08 (n/a)</td><td>171.10 (n/a)</td><td>155.80 (n/a)</td><td>37.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-14.35%)</td><td>0.02 (-19.53%)</td><td>0.02 <b>(-27.70%)</b></td><td>0.02 <b>(-21.70%)</b></td><td>0.00 (-16.82%)</td><td>249.90 <b>(+27.70%)</b></td><td>185.04 <b>(+24.51%)</b></td><td>178.70 <b>(+38.31%)</b></td><td>145.70 (+16.75%)</td><td>40.08 <b>(+28.52%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>148.62 (n/a)</td><td>129.20 (n/a)</td><td>124.80 (n/a)</td><td>31.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-15.88%)</td><td>0.02 (-11.74%)</td><td>0.03 (-8.34%)</td><td>0.02 (-7.66%)</td><td>0.00 (-15.16%)</td><td>205.40 (+8.33%)</td><td>176.26 (+13.16%)</td><td>163.60 (+9.07%)</td><td>153.90 (+18.84%)</td><td>25.11 (+9.55%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>155.76 (n/a)</td><td>150.00 (n/a)</td><td>129.50 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(+33.01%)</b></td><td>0.03 (+7.55%)</td><td>0.02 (-3.03%)</td><td>0.02 (+16.67%)</td><td>0.01 <b>(+65.76%)</b></td><td>202.20 (-14.29%)</td><td>169.52 (-5.78%)</td><td>176.80 (+3.09%)</td><td>117.20 <b>(-24.82%)</b></td><td>31.79 (-0.96%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.90 (n/a)</td><td>179.92 (n/a)</td><td>171.50 (n/a)</td><td>155.90 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-16.06%)</td><td>0.02 (-10.79%)</td><td>0.02 (-10.74%)</td><td>0.02 <b>(-22.43%)</b></td><td>0.00 (-6.47%)</td><td>265.00 <b>(+28.95%)</b></td><td>202.46 (+12.98%)</td><td>204.40 (+12.00%)</td><td>160.40 (+19.17%)</td><td>40.54 <b>(+46.46%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.50 (n/a)</td><td>179.20 (n/a)</td><td>182.50 (n/a)</td><td>134.60 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(+24.06%)</b></td><td>0.02 (-8.63%)</td><td>0.02 (-11.93%)</td><td>0.01 <b>(-25.67%)</b></td><td>0.01 <b>(+102.57%)</b></td><td>285.00 <b>(+34.50%)</b></td><td>192.98 (+18.15%)</td><td>180.00 (+13.49%)</td><td>107.30 (-19.44%)</td><td>65.34 <b>(+112.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.90 (n/a)</td><td>163.34 (n/a)</td><td>158.60 (n/a)</td><td>133.20 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-6.89%)</td><td>0.02 (+1.67%)</td><td>0.02 (+11.64%)</td><td>0.02 (-1.09%)</td><td>0.00 <b>(-22.13%)</b></td><td>222.40 (+1.14%)</td><td>198.60 (-2.01%)</td><td>190.80 (-10.42%)</td><td>175.00 (+7.36%)</td><td>20.03 (-12.46%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>202.68 (n/a)</td><td>213.00 (n/a)</td><td>163.00 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+8.58%)</td><td>0.05 (-8.94%)</td><td>0.05 (-7.27%)</td><td>0.03 <b>(-38.80%)</b></td><td>0.02 <b>(+101.17%)</b></td><td>300.80 <b>(+63.39%)</b></td><td>189.38 (+18.44%)</td><td>179.50 (+7.87%)</td><td>116.90 (-7.88%)</td><td>67.73 <b>(+219.48%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>159.90 (n/a)</td><td>166.40 (n/a)</td><td>126.90 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 <b>(+29.58%)</b></td><td>0.05 (+13.93%)</td><td>0.05 (+10.85%)</td><td>0.04 <b>(+31.31%)</b></td><td>0.01 <b>(+21.02%)</b></td><td>218.30 <b>(-23.83%)</b></td><td>172.46 (-12.92%)</td><td>167.00 (-9.78%)</td><td>124.70 <b>(-22.79%)</b></td><td>34.03 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.60 (n/a)</td><td>198.04 (n/a)</td><td>185.10 (n/a)</td><td>161.50 (n/a)</td><td>50.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (+12.20%)</td><td>0.06 <b>(+23.73%)</b></td><td>0.05 (+6.23%)</td><td>0.04 <b>(+99.24%)</b></td><td>0.01 (-15.89%)</td><td>191.70 <b>(-49.80%)</b></td><td>148.90 <b>(-26.89%)</b></td><td>162.10 (-5.87%)</td><td>107.90 (-10.90%)</td><td>34.49 <b>(-66.31%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>381.90 (n/a)</td><td>203.66 (n/a)</td><td>172.20 (n/a)</td><td>121.10 (n/a)</td><td>102.38 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (+11.73%)</td><td>0.06 (+9.18%)</td><td>0.05 (+10.44%)</td><td>0.04 (+0.74%)</td><td>0.01 (+19.94%)</td><td>200.20 (-0.69%)</td><td>152.54 (-7.59%)</td><td>150.70 (-9.44%)</td><td>104.80 (-10.50%)</td><td>34.57 (+5.78%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>165.06 (n/a)</td><td>166.40 (n/a)</td><td>117.10 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 <b>(+61.00%)</b></td><td>0.05 (+16.88%)</td><td>0.05 (+8.48%)</td><td>0.04 (-11.07%)</td><td>0.01 <b>(+808.14%)</b></td><td>217.10 (+12.43%)</td><td>164.80 (-10.39%)</td><td>167.30 (-7.82%)</td><td>110.20 <b>(-37.88%)</b></td><td>37.89 <b>(+508.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>183.90 (n/a)</td><td>181.50 (n/a)</td><td>177.40 (n/a)</td><td>6.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 <b>(-23.48%)</b></td><td>0.05 (-1.22%)</td><td>0.04 (+3.11%)</td><td>0.04 (+5.32%)</td><td>0.01 <b>(-42.92%)</b></td><td>206.20 (-5.02%)</td><td>175.44 (-2.09%)</td><td>185.90 (-3.03%)</td><td>142.70 <b>(+30.68%)</b></td><td>30.18 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>217.10 (n/a)</td><td>179.18 (n/a)</td><td>191.70 (n/a)</td><td>109.20 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 <b>(-21.21%)</b></td><td>0.05 (-13.82%)</td><td>0.04 <b>(-23.98%)</b></td><td>0.04 (+14.69%)</td><td>0.01 <b>(-58.55%)</b></td><td>195.20 (-12.82%)</td><td>177.00 (+11.13%)</td><td>185.30 <b>(+31.61%)</b></td><td>149.70 <b>(+26.97%)</b></td><td>19.75 <b>(-54.42%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>159.28 (n/a)</td><td>140.80 (n/a)</td><td>117.90 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 <b>(+27.68%)</b></td><td>0.05 (+15.35%)</td><td>0.04 (+8.15%)</td><td>0.04 (+11.30%)</td><td>0.01 <b>(+98.51%)</b></td><td>207.60 (-10.17%)</td><td>181.16 (-12.58%)</td><td>188.60 (-7.55%)</td><td>150.50 <b>(-21.66%)</b></td><td>22.61 <b>(+39.09%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>207.24 (n/a)</td><td>204.00 (n/a)</td><td>192.10 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(-31.25%)</b></td><td>0.04 (-6.01%)</td><td>0.04 (+5.68%)</td><td>0.04 (+1.18%)</td><td>0.00 <b>(-83.37%)</b></td><td>206.40 (-1.15%)</td><td>192.78 (+2.75%)</td><td>190.50 (-5.37%)</td><td>183.80 <b>(+45.41%)</b></td><td>8.51 <b>(-75.34%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>187.62 (n/a)</td><td>201.30 (n/a)</td><td>126.40 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-15.44%)</td><td>0.04 (-13.91%)</td><td>0.04 (-17.57%)</td><td>0.03 (-9.66%)</td><td>0.00 <b>(-33.89%)</b></td><td>248.30 (+10.70%)</td><td>222.04 (+15.66%)</td><td>222.50 <b>(+21.32%)</b></td><td>203.80 (+18.28%)</td><td>18.93 (-14.36%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.30 (n/a)</td><td>191.98 (n/a)</td><td>183.40 (n/a)</td><td>172.30 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (-0.61%)</td><td>0.10 (-2.61%)</td><td>0.10 (-9.82%)</td><td>0.09 (+17.31%)</td><td>0.01 <b>(-30.32%)</b></td><td>184.60 (-14.73%)</td><td>165.16 (+0.72%)</td><td>172.00 (+10.90%)</td><td>132.20 (+0.61%)</td><td>20.61 <b>(-40.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>163.98 (n/a)</td><td>155.10 (n/a)</td><td>131.40 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-4.96%)</td><td>0.11 (+0.01%)</td><td>0.10 (-5.97%)</td><td>0.09 (+7.44%)</td><td>0.02 (-12.49%)</td><td>183.00 (-6.96%)</td><td>153.02 (-0.71%)</td><td>158.50 (+6.38%)</td><td>123.90 (+5.18%)</td><td>24.38 (-15.63%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.70 (n/a)</td><td>154.12 (n/a)</td><td>149.00 (n/a)</td><td>117.80 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (-0.89%)</td><td>0.09 (-3.92%)</td><td>0.09 (-8.44%)</td><td>0.07 (-16.11%)</td><td>0.02 <b>(+61.55%)</b></td><td>228.60 (+19.19%)</td><td>179.02 (+6.50%)</td><td>182.90 (+9.19%)</td><td>142.20 (+0.92%)</td><td>37.28 <b>(+85.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>168.10 (n/a)</td><td>167.50 (n/a)</td><td>140.90 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-11.72%)</td><td>0.10 (-8.08%)</td><td>0.09 (-18.70%)</td><td>0.09 (+9.33%)</td><td>0.02 <b>(-36.59%)</b></td><td>192.70 (-8.54%)</td><td>167.90 (+4.71%)</td><td>188.00 <b>(+23.04%)</b></td><td>130.00 (+13.24%)</td><td>30.58 <b>(-33.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.70 (n/a)</td><td>160.34 (n/a)</td><td>152.80 (n/a)</td><td>114.80 (n/a)</td><td>46.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 <b>(-26.11%)</b></td><td>0.09 (-19.40%)</td><td>0.10 (-9.48%)</td><td>0.04 <b>(-50.42%)</b></td><td>0.03 (+18.00%)</td><td>379.90 <b>(+101.75%)</b></td><td>207.32 <b>(+35.89%)</b></td><td>161.50 (+10.54%)</td><td>148.90 <b>(+35.36%)</b></td><td>98.45 <b>(+229.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.30 (n/a)</td><td>152.56 (n/a)</td><td>146.10 (n/a)</td><td>110.00 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (+10.90%)</td><td>0.09 (+3.36%)</td><td>0.10 (+4.10%)</td><td>0.08 (+3.75%)</td><td>0.01 <b>(+40.15%)</b></td><td>199.20 (-3.58%)</td><td>176.36 (-2.72%)</td><td>171.30 (-3.93%)</td><td>147.40 (-9.79%)</td><td>21.77 <b>(+24.36%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>181.30 (n/a)</td><td>178.30 (n/a)</td><td>163.40 (n/a)</td><td>17.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 <b>(+22.62%)</b></td><td>0.10 (-0.71%)</td><td>0.08 (-19.32%)</td><td>0.07 (-14.19%)</td><td>0.03 <b>(+306.91%)</b></td><td>219.70 (+16.55%)</td><td>181.84 (+6.40%)</td><td>209.80 <b>(+24.00%)</b></td><td>126.90 (-18.44%)</td><td>46.16 <b>(+290.01%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>170.90 (n/a)</td><td>169.20 (n/a)</td><td>155.60 (n/a)</td><td>11.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (-1.72%)</td><td>0.07 (-7.87%)</td><td>0.07 (-6.61%)</td><td>0.05 <b>(-34.77%)</b></td><td>0.02 <b>(+116.41%)</b></td><td>360.80 <b>(+53.34%)</b></td><td>242.84 (+13.59%)</td><td>232.60 (+7.09%)</td><td>185.60 (+1.75%)</td><td>69.02 <b>(+258.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>213.78 (n/a)</td><td>217.20 (n/a)</td><td>182.40 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (-1.25%)</td><td>0.20 (-1.30%)</td><td>0.21 (-0.86%)</td><td>0.14 (+14.02%)</td><td>0.05 (-9.68%)</td><td>239.50 (-12.30%)</td><td>172.92 (-0.75%)</td><td>159.20 (+0.89%)</td><td>124.90 (+1.22%)</td><td>44.53 <b>(-23.05%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>273.10 (n/a)</td><td>174.22 (n/a)</td><td>157.80 (n/a)</td><td>123.40 (n/a)</td><td>57.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (-8.20%)</td><td>0.21 (-3.82%)</td><td>0.21 (+3.05%)</td><td>0.19 (+2.24%)</td><td>0.02 <b>(-44.96%)</b></td><td>171.40 (-2.17%)</td><td>156.84 (+2.75%)</td><td>157.90 (-2.95%)</td><td>138.60 (+8.96%)</td><td>13.28 <b>(-40.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.20 (n/a)</td><td>152.64 (n/a)</td><td>162.70 (n/a)</td><td>127.20 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (-4.04%)</td><td>0.17 (-10.65%)</td><td>0.17 (-5.98%)</td><td>0.10 <b>(-29.83%)</b></td><td>0.05 <b>(+20.69%)</b></td><td>314.10 <b>(+42.51%)</b></td><td>204.32 (+16.70%)</td><td>197.40 (+6.36%)</td><td>131.00 (+4.22%)</td><td>67.49 <b>(+87.10%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>220.40 (n/a)</td><td>175.08 (n/a)</td><td>185.60 (n/a)</td><td>125.70 (n/a)</td><td>36.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 <b>(+23.38%)</b></td><td>0.23 <b>(+21.10%)</b></td><td>0.23 <b>(+25.66%)</b></td><td>0.19 (+11.64%)</td><td>0.04 <b>(+73.85%)</b></td><td>171.50 (-10.44%)</td><td>146.82 (-16.55%)</td><td>143.80 <b>(-20.42%)</b></td><td>119.40 (-18.94%)</td><td>22.32 <b>(+30.73%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>191.50 (n/a)</td><td>175.94 (n/a)</td><td>180.70 (n/a)</td><td>147.30 (n/a)</td><td>17.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 <b>(-29.89%)</b></td><td>0.19 (-2.23%)</td><td>0.21 (+13.32%)</td><td>0.16 (+4.94%)</td><td>0.03 <b>(-59.72%)</b></td><td>211.30 (-4.69%)</td><td>173.54 (-2.91%)</td><td>158.50 (-11.75%)</td><td>152.00 <b>(+42.59%)</b></td><td>25.47 <b>(-44.04%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>221.70 (n/a)</td><td>178.74 (n/a)</td><td>179.60 (n/a)</td><td>106.60 (n/a)</td><td>45.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+16.70%)</td><td>0.20 <b>(+20.96%)</b></td><td>0.19 <b>(+22.40%)</b></td><td>0.17 (+14.57%)</td><td>0.03 <b>(+29.60%)</b></td><td>191.60 (-12.71%)</td><td>167.00 (-17.04%)</td><td>169.20 (-18.34%)</td><td>138.30 (-14.26%)</td><td>23.41 (-1.43%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>201.30 (n/a)</td><td>207.20 (n/a)</td><td>161.30 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (+18.18%)</td><td>0.14 (+5.52%)</td><td>0.15 (+4.94%)</td><td>0.10 (+12.76%)</td><td>0.03 (+13.23%)</td><td>334.20 (-11.31%)</td><td>239.48 (-5.51%)</td><td>225.10 (-4.70%)</td><td>173.90 (-15.38%)</td><td>59.28 (-15.84%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>376.80 (n/a)</td><td>253.44 (n/a)</td><td>236.20 (n/a)</td><td>205.50 (n/a)</td><td>70.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-12.34%)</td><td>0.03 (-11.41%)</td><td>0.02 (-11.45%)</td><td>0.02 (-5.36%)</td><td>0.00 <b>(-21.22%)</b></td><td>185.80 (+5.69%)</td><td>162.84 (+12.18%)</td><td>164.30 (+12.92%)</td><td>125.40 (+14.10%)</td><td>23.38 (-5.55%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>145.16 (n/a)</td><td>145.50 (n/a)</td><td>109.90 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+1.45%)</td><td>0.03 (-0.70%)</td><td>0.03 (-6.05%)</td><td>0.02 (+10.47%)</td><td>0.00 (-8.87%)</td><td>209.30 (-9.47%)</td><td>162.00 (-0.41%)</td><td>159.00 (+6.43%)</td><td>129.40 (-1.37%)</td><td>32.21 <b>(-20.71%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>162.66 (n/a)</td><td>149.40 (n/a)</td><td>131.20 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (-15.13%)</td><td>0.02 (-17.93%)</td><td>0.02 (-15.58%)</td><td>0.01 <b>(-33.18%)</b></td><td>0.00 (+18.62%)</td><td>301.90 <b>(+49.68%)</b></td><td>215.78 <b>(+24.61%)</b></td><td>205.40 (+18.45%)</td><td>169.80 (+17.83%)</td><td>50.54 <b>(+118.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>173.16 (n/a)</td><td>173.40 (n/a)</td><td>144.10 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-9.03%)</td><td>0.02 (-4.78%)</td><td>0.02 (+1.24%)</td><td>0.01 (-8.78%)</td><td>0.00 (-12.13%)</td><td>273.10 (+9.63%)</td><td>195.52 (+4.93%)</td><td>187.00 (-1.22%)</td><td>158.80 (+9.90%)</td><td>45.14 (+10.36%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.10 (n/a)</td><td>186.34 (n/a)</td><td>189.30 (n/a)</td><td>144.50 (n/a)</td><td>40.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 <b>(+20.06%)</b></td><td>0.03 (+8.07%)</td><td>0.02 (-9.85%)</td><td>0.02 <b>(+20.57%)</b></td><td>0.01 <b>(+24.00%)</b></td><td>224.70 (-17.08%)</td><td>166.88 (-7.39%)</td><td>179.50 (+10.94%)</td><td>101.60 (-16.72%)</td><td>46.88 (-18.62%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.00 (n/a)</td><td>180.20 (n/a)</td><td>161.80 (n/a)</td><td>122.00 (n/a)</td><td>57.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-7.08%)</td><td>0.03 (+6.11%)</td><td>0.03 (+16.00%)</td><td>0.02 (+9.23%)</td><td>0.00 <b>(-36.02%)</b></td><td>175.10 (-8.47%)</td><td>148.70 (-6.91%)</td><td>143.60 (-13.81%)</td><td>132.40 (+7.64%)</td><td>16.40 <b>(-34.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.30 (n/a)</td><td>159.74 (n/a)</td><td>166.60 (n/a)</td><td>123.00 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+4.32%)</td><td>0.03 (+4.37%)</td><td>0.03 (+0.57%)</td><td>0.03 (+0.74%)</td><td>0.00 <b>(+26.47%)</b></td><td>162.60 (-0.73%)</td><td>141.00 (-3.74%)</td><td>146.20 (-0.61%)</td><td>119.70 (-4.09%)</td><td>18.16 (+18.60%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>163.80 (n/a)</td><td>146.48 (n/a)</td><td>147.10 (n/a)</td><td>124.80 (n/a)</td><td>15.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 <b>(-27.47%)</b></td><td>0.02 <b>(-23.36%)</b></td><td>0.02 (-19.78%)</td><td>0.02 <b>(-21.34%)</b></td><td>0.00 <b>(-42.36%)</b></td><td>209.10 <b>(+27.11%)</b></td><td>188.28 <b>(+29.96%)</b></td><td>183.90 <b>(+24.59%)</b></td><td>171.60 <b>(+37.83%)</b></td><td>15.67 (+1.98%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.50 (n/a)</td><td>144.88 (n/a)</td><td>147.60 (n/a)</td><td>124.50 (n/a)</td><td>15.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-14.94%)</td><td>0.02 (-12.71%)</td><td>0.02 (-8.63%)</td><td>0.01 <b>(-29.92%)</b></td><td>0.00 (+5.69%)</td><td>291.00 <b>(+42.72%)</b></td><td>202.56 (+16.97%)</td><td>188.10 (+9.49%)</td><td>159.10 (+17.59%)</td><td>52.96 <b>(+75.74%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.90 (n/a)</td><td>173.18 (n/a)</td><td>171.80 (n/a)</td><td>135.30 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-4.84%)</td><td>0.02 (+0.29%)</td><td>0.02 (-0.15%)</td><td>0.02 (+12.99%)</td><td>0.00 <b>(-34.85%)</b></td><td>190.10 (-11.50%)</td><td>165.50 (-1.59%)</td><td>165.10 (+0.18%)</td><td>142.70 (+5.08%)</td><td>17.12 <b>(-40.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.80 (n/a)</td><td>168.18 (n/a)</td><td>164.80 (n/a)</td><td>135.80 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(+21.11%)</b></td><td>0.02 (-7.67%)</td><td>0.02 (-6.67%)</td><td>0.01 <b>(-33.24%)</b></td><td>0.01 <b>(+186.65%)</b></td><td>289.90 <b>(+49.82%)</b></td><td>200.44 (+17.02%)</td><td>184.90 (+7.13%)</td><td>118.70 (-17.45%)</td><td>63.41 <b>(+256.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.50 (n/a)</td><td>171.28 (n/a)</td><td>172.60 (n/a)</td><td>143.80 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+5.37%)</td><td>0.03 (+7.66%)</td><td>0.03 <b>(+26.60%)</b></td><td>0.02 (+0.02%)</td><td>0.01 <b>(+30.55%)</b></td><td>229.30 (-0.04%)</td><td>169.90 (-5.02%)</td><td>147.70 <b>(-20.97%)</b></td><td>127.80 (-5.12%)</td><td>46.72 <b>(+26.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>178.88 (n/a)</td><td>186.90 (n/a)</td><td>134.70 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(-27.79%)</b></td><td>0.02 (-12.75%)</td><td>0.02 (-6.14%)</td><td>0.01 (-13.27%)</td><td>0.00 <b>(-43.65%)</b></td><td>277.80 (+15.32%)</td><td>211.72 (+11.27%)</td><td>206.80 (+6.54%)</td><td>161.90 <b>(+38.49%)</b></td><td>44.57 (-7.09%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.90 (n/a)</td><td>190.28 (n/a)</td><td>194.10 (n/a)</td><td>116.90 (n/a)</td><td>47.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(+24.81%)</b></td><td>0.03 (+17.59%)</td><td>0.02 (+8.77%)</td><td>0.02 (+10.35%)</td><td>0.00 <b>(+117.83%)</b></td><td>180.60 (-9.38%)</td><td>156.58 (-13.56%)</td><td>164.50 (-8.05%)</td><td>128.70 (-19.91%)</td><td>26.08 <b>(+54.23%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>181.14 (n/a)</td><td>178.90 (n/a)</td><td>160.70 (n/a)</td><td>16.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(+26.80%)</b></td><td>0.02 (+18.53%)</td><td>0.03 <b>(+23.84%)</b></td><td>0.02 (+6.03%)</td><td>0.00 <b>(+169.89%)</b></td><td>204.80 (-5.67%)</td><td>169.10 (-14.06%)</td><td>155.30 (-19.28%)</td><td>143.50 <b>(-21.11%)</b></td><td>29.12 <b>(+101.14%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>196.76 (n/a)</td><td>192.40 (n/a)</td><td>181.90 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 <b>(-22.81%)</b></td><td>0.02 (-3.56%)</td><td>0.02 (+5.94%)</td><td>0.02 (+8.39%)</td><td>0.00 <b>(-82.44%)</b></td><td>174.30 (-7.73%)</td><td>165.56 (+0.88%)</td><td>165.10 (-5.60%)</td><td>158.00 <b>(+29.51%)</b></td><td>6.05 <b>(-79.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>164.12 (n/a)</td><td>174.90 (n/a)</td><td>122.00 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+6.80%)</td><td>0.05 (-5.50%)</td><td>0.05 (+6.69%)</td><td>0.02 <b>(-40.97%)</b></td><td>0.02 <b>(+72.84%)</b></td><td>331.80 <b>(+69.46%)</b></td><td>191.22 (+15.71%)</td><td>162.90 (-6.27%)</td><td>118.90 (-6.38%)</td><td>81.90 <b>(+196.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>165.26 (n/a)</td><td>173.80 (n/a)</td><td>127.00 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-0.96%)</td><td>0.05 (-3.72%)</td><td>0.05 (-6.94%)</td><td>0.04 (+3.25%)</td><td>0.01 (-16.58%)</td><td>186.90 (-3.16%)</td><td>161.34 (+3.03%)</td><td>158.70 (+7.45%)</td><td>128.60 (+1.02%)</td><td>22.65 (-19.35%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>156.60 (n/a)</td><td>147.70 (n/a)</td><td>127.30 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-5.22%)</td><td>0.04 (+0.52%)</td><td>0.04 (+0.57%)</td><td>0.04 (+2.59%)</td><td>0.00 <b>(-32.44%)</b></td><td>233.70 (-2.54%)</td><td>215.92 (-1.12%)</td><td>221.30 (-0.58%)</td><td>188.80 (+5.47%)</td><td>16.92 <b>(-31.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.80 (n/a)</td><td>218.36 (n/a)</td><td>222.60 (n/a)</td><td>179.00 (n/a)</td><td>24.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (+3.29%)</td><td>0.04 (+13.78%)</td><td>0.04 (+10.29%)</td><td>0.04 <b>(+52.34%)</b></td><td>0.00 <b>(-43.41%)</b></td><td>220.50 <b>(-34.36%)</b></td><td>193.30 (-15.43%)</td><td>192.00 (-9.31%)</td><td>167.40 (-3.18%)</td><td>21.14 <b>(-66.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>335.90 (n/a)</td><td>228.58 (n/a)</td><td>211.70 (n/a)</td><td>172.90 (n/a)</td><td>62.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 <b>(+23.37%)</b></td><td>0.06 (+18.24%)</td><td>0.06 (+16.75%)</td><td>0.05 (+12.10%)</td><td>0.01 <b>(+66.44%)</b></td><td>165.20 (-10.80%)</td><td>144.92 (-14.90%)</td><td>146.00 (-14.37%)</td><td>121.20 (-18.93%)</td><td>17.72 (+19.41%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.20 (n/a)</td><td>170.30 (n/a)</td><td>170.50 (n/a)</td><td>149.50 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+9.96%)</td><td>0.06 (+9.84%)</td><td>0.05 (+4.54%)</td><td>0.04 (+9.27%)</td><td>0.01 (+1.17%)</td><td>199.00 (-8.46%)</td><td>152.62 (-9.47%)</td><td>157.00 (-4.33%)</td><td>117.90 (-9.10%)</td><td>31.30 (-15.44%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>168.58 (n/a)</td><td>164.10 (n/a)</td><td>129.70 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+0.10%)</td><td>0.05 (-2.18%)</td><td>0.05 (-4.70%)</td><td>0.03 (-16.45%)</td><td>0.02 <b>(+27.55%)</b></td><td>278.50 (+19.68%)</td><td>175.62 (+6.84%)</td><td>167.10 (+4.96%)</td><td>115.20 (-0.09%)</td><td>64.43 <b>(+49.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>164.38 (n/a)</td><td>159.20 (n/a)</td><td>115.30 (n/a)</td><td>42.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+17.70%)</td><td>0.05 (-7.67%)</td><td>0.04 <b>(-23.82%)</b></td><td>0.03 <b>(-30.95%)</b></td><td>0.02 <b>(+220.89%)</b></td><td>244.90 <b>(+44.83%)</b></td><td>175.60 (+15.65%)</td><td>191.00 <b>(+31.27%)</b></td><td>117.90 (-15.06%)</td><td>51.49 <b>(+280.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>169.10 (n/a)</td><td>151.84 (n/a)</td><td>145.50 (n/a)</td><td>138.80 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+2.72%)</td><td>0.05 (+10.53%)</td><td>0.05 (+16.70%)</td><td>0.04 (+17.62%)</td><td>0.01 (-19.94%)</td><td>205.90 (-14.95%)</td><td>165.96 (-12.05%)</td><td>166.00 (-14.34%)</td><td>119.60 (-2.61%)</td><td>30.78 <b>(-35.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.10 (n/a)</td><td>188.70 (n/a)</td><td>193.80 (n/a)</td><td>122.80 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-2.83%)</td><td>0.05 (-0.35%)</td><td>0.05 (-4.67%)</td><td>0.04 <b>(+30.15%)</b></td><td>0.01 <b>(-39.64%)</b></td><td>192.20 <b>(-23.15%)</b></td><td>166.26 (-2.65%)</td><td>158.20 (+4.91%)</td><td>147.40 (+2.86%)</td><td>20.72 <b>(-53.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>170.78 (n/a)</td><td>150.80 (n/a)</td><td>143.30 (n/a)</td><td>44.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (-19.45%)</td><td>0.05 (-12.37%)</td><td>0.05 (-1.16%)</td><td>0.04 (-9.21%)</td><td>0.00 <b>(-53.44%)</b></td><td>185.60 (+10.15%)</td><td>170.70 (+12.96%)</td><td>163.60 (+1.18%)</td><td>158.40 <b>(+24.14%)</b></td><td>12.77 <b>(-35.66%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>151.12 (n/a)</td><td>161.70 (n/a)</td><td>127.60 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (+2.54%)</td><td>0.05 (-6.14%)</td><td>0.05 (-9.98%)</td><td>0.04 (+17.57%)</td><td>0.01 (-19.10%)</td><td>201.10 (-14.97%)</td><td>176.32 (+4.84%)</td><td>174.00 (+11.04%)</td><td>138.60 (-2.46%)</td><td>25.52 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>168.18 (n/a)</td><td>156.70 (n/a)</td><td>142.10 (n/a)</td><td>38.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 <b>(-22.72%)</b></td><td>0.04 (-18.20%)</td><td>0.04 <b>(-21.66%)</b></td><td>0.04 (-0.61%)</td><td>0.00 <b>(-68.42%)</b></td><td>199.90 (+0.65%)</td><td>184.66 (+19.58%)</td><td>184.90 <b>(+27.69%)</b></td><td>167.80 <b>(+29.48%)</b></td><td>11.92 <b>(-58.64%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>154.42 (n/a)</td><td>144.80 (n/a)</td><td>129.60 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+5.57%)</td><td>0.05 (+2.15%)</td><td>0.05 (-4.75%)</td><td>0.04 <b>(+31.56%)</b></td><td>0.01 <b>(-24.71%)</b></td><td>189.30 <b>(-24.01%)</b></td><td>155.98 (-5.25%)</td><td>156.60 (+4.96%)</td><td>122.20 (-5.27%)</td><td>24.78 <b>(-48.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>164.62 (n/a)</td><td>149.20 (n/a)</td><td>129.00 (n/a)</td><td>48.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-12.44%)</td><td>0.05 (-2.19%)</td><td>0.05 (-6.98%)</td><td>0.04 (+7.69%)</td><td>0.01 <b>(-42.47%)</b></td><td>189.50 (-7.11%)</td><td>168.30 (+0.38%)</td><td>168.50 (+7.53%)</td><td>146.80 (+14.24%)</td><td>18.68 <b>(-40.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>167.66 (n/a)</td><td>156.70 (n/a)</td><td>128.50 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-5.08%)</td><td>0.05 (-5.12%)</td><td>0.05 (-14.05%)</td><td>0.04 (+7.28%)</td><td>0.01 (-16.11%)</td><td>194.20 (-6.77%)</td><td>168.50 (+4.68%)</td><td>177.30 (+16.34%)</td><td>145.40 (+5.36%)</td><td>21.20 <b>(-22.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>160.96 (n/a)</td><td>152.40 (n/a)</td><td>138.00 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 <b>(+42.21%)</b></td><td>0.11 (+19.01%)</td><td>0.11 (+10.30%)</td><td>0.08 (+5.82%)</td><td>0.03 <b>(+102.72%)</b></td><td>216.70 (-5.49%)</td><td>159.30 (-13.31%)</td><td>150.00 (-9.37%)</td><td>114.10 <b>(-29.70%)</b></td><td>40.17 <b>(+37.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>183.76 (n/a)</td><td>165.50 (n/a)</td><td>162.30 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+10.37%)</td><td>0.11 (+17.19%)</td><td>0.11 (+9.60%)</td><td>0.10 <b>(+38.27%)</b></td><td>0.01 (-17.74%)</td><td>164.80 <b>(-27.69%)</b></td><td>145.80 (-15.93%)</td><td>154.20 (-8.76%)</td><td>125.70 (-9.37%)</td><td>17.01 <b>(-48.47%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.90 (n/a)</td><td>173.42 (n/a)</td><td>169.00 (n/a)</td><td>138.70 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 <b>(+33.01%)</b></td><td>0.09 <b>(+28.70%)</b></td><td>0.09 <b>(+20.73%)</b></td><td>0.07 <b>(+43.12%)</b></td><td>0.01 (+9.82%)</td><td>219.60 <b>(-30.11%)</b></td><td>180.86 <b>(-23.03%)</b></td><td>177.90 (-17.18%)</td><td>150.80 <b>(-24.83%)</b></td><td>25.68 <b>(-43.68%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>314.20 (n/a)</td><td>234.98 (n/a)</td><td>214.80 (n/a)</td><td>200.60 (n/a)</td><td>45.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (+14.09%)</td><td>0.09 <b>(+30.88%)</b></td><td>0.09 <b>(+32.11%)</b></td><td>0.08 <b>(+63.44%)</b></td><td>0.01 <b>(-52.29%)</b></td><td>196.50 <b>(-38.82%)</b></td><td>180.02 <b>(-25.46%)</b></td><td>174.90 <b>(-24.32%)</b></td><td>167.40 (-12.36%)</td><td>11.89 <b>(-75.20%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>321.20 (n/a)</td><td>241.52 (n/a)</td><td>231.10 (n/a)</td><td>191.00 (n/a)</td><td>47.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (+18.44%)</td><td>0.10 (+15.23%)</td><td>0.09 (+13.06%)</td><td>0.09 (+14.68%)</td><td>0.01 <b>(+74.35%)</b></td><td>183.70 (-12.81%)</td><td>170.88 (-13.03%)</td><td>172.50 (-11.54%)</td><td>156.70 (-15.57%)</td><td>12.02 <b>(+27.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>196.48 (n/a)</td><td>195.00 (n/a)</td><td>185.60 (n/a)</td><td>9.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 <b>(+22.61%)</b></td><td>0.11 <b>(+23.31%)</b></td><td>0.11 <b>(+33.18%)</b></td><td>0.10 <b>(+21.51%)</b></td><td>0.01 (-2.35%)</td><td>166.80 (-17.67%)</td><td>147.62 (-19.16%)</td><td>145.40 <b>(-24.90%)</b></td><td>130.80 (-18.40%)</td><td>13.29 <b>(-33.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>182.60 (n/a)</td><td>193.60 (n/a)</td><td>160.30 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 <b>(-45.16%)</b></td><td>0.11 (-2.73%)</td><td>0.11 <b>(+26.39%)</b></td><td>0.10 <b>(+22.83%)</b></td><td>0.01 <b>(-83.44%)</b></td><td>169.90 (-18.55%)</td><td>154.92 (-11.00%)</td><td>152.10 <b>(-20.86%)</b></td><td>137.50 <b>(+82.36%)</b></td><td>14.53 <b>(-73.91%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>208.60 (n/a)</td><td>174.06 (n/a)</td><td>192.20 (n/a)</td><td>75.40 (n/a)</td><td>55.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (-1.86%)</td><td>0.11 (+11.80%)</td><td>0.10 (+11.15%)</td><td>0.09 <b>(+103.99%)</b></td><td>0.02 <b>(-45.78%)</b></td><td>185.40 <b>(-50.98%)</b></td><td>158.56 <b>(-21.47%)</b></td><td>158.90 (-10.07%)</td><td>118.80 (+1.89%)</td><td>25.13 <b>(-75.43%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>378.20 (n/a)</td><td>201.92 (n/a)</td><td>176.70 (n/a)</td><td>116.60 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+2.24%)</td><td>0.10 (+3.45%)</td><td>0.09 (-2.08%)</td><td>0.07 (-9.77%)</td><td>0.03 <b>(+32.57%)</b></td><td>222.20 (+10.82%)</td><td>168.90 (-1.24%)</td><td>181.40 (+2.08%)</td><td>125.00 (-2.19%)</td><td>40.91 <b>(+37.65%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>171.02 (n/a)</td><td>177.70 (n/a)</td><td>127.80 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+16.12%)</td><td>0.11 (+16.29%)</td><td>0.10 (+5.31%)</td><td>0.08 (+14.18%)</td><td>0.02 <b>(+29.43%)</b></td><td>193.80 (-12.43%)</td><td>157.06 (-13.54%)</td><td>156.10 (-5.05%)</td><td>125.00 (-13.91%)</td><td>31.44 (-6.76%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.30 (n/a)</td><td>181.66 (n/a)</td><td>164.40 (n/a)</td><td>145.20 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+5.55%)</td><td>0.12 (+16.08%)</td><td>0.12 <b>(+29.27%)</b></td><td>0.10 (+7.71%)</td><td>0.02 (+8.71%)</td><td>169.30 (-7.13%)</td><td>139.82 (-13.80%)</td><td>131.20 <b>(-22.64%)</b></td><td>123.20 (-5.30%)</td><td>19.76 (-3.93%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>162.20 (n/a)</td><td>169.60 (n/a)</td><td>130.10 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (-9.47%)</td><td>0.11 (+7.64%)</td><td>0.13 <b>(+41.38%)</b></td><td>0.08 (-0.17%)</td><td>0.02 <b>(-23.39%)</b></td><td>201.70 (+0.15%)</td><td>148.66 (-8.91%)</td><td>129.50 <b>(-29.27%)</b></td><td>120.70 (+10.53%)</td><td>33.86 (-15.88%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>163.20 (n/a)</td><td>183.10 (n/a)</td><td>109.20 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (+17.55%)</td><td>0.10 (+17.14%)</td><td>0.09 (+9.69%)</td><td>0.08 (+19.90%)</td><td>0.02 <b>(+36.38%)</b></td><td>205.20 (-16.59%)</td><td>175.14 (-14.23%)</td><td>185.70 (-8.84%)</td><td>142.40 (-14.93%)</td><td>27.05 (-4.54%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>204.20 (n/a)</td><td>203.70 (n/a)</td><td>167.40 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 <b>(+52.23%)</b></td><td>0.11 <b>(+43.98%)</b></td><td>0.11 <b>(+38.37%)</b></td><td>0.09 <b>(+31.61%)</b></td><td>0.02 <b>(+180.56%)</b></td><td>172.80 <b>(-24.01%)</b></td><td>146.78 <b>(-29.58%)</b></td><td>150.10 <b>(-27.73%)</b></td><td>122.10 <b>(-34.32%)</b></td><td>22.17 <b>(+38.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>208.44 (n/a)</td><td>207.70 (n/a)</td><td>185.90 (n/a)</td><td>16.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (+5.72%)</td><td>0.09 <b>(+25.85%)</b></td><td>0.09 <b>(+29.00%)</b></td><td>0.08 <b>(+44.90%)</b></td><td>0.01 <b>(-28.31%)</b></td><td>199.40 <b>(-30.98%)</b></td><td>177.78 <b>(-22.56%)</b></td><td>187.30 <b>(-22.48%)</b></td><td>150.60 (-5.46%)</td><td>23.07 <b>(-51.98%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>288.90 (n/a)</td><td>229.58 (n/a)</td><td>241.60 (n/a)</td><td>159.30 (n/a)</td><td>48.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 <b>(+26.94%)</b></td><td>0.10 (+18.08%)</td><td>0.10 <b>(+28.97%)</b></td><td>0.08 (+18.86%)</td><td>0.02 <b>(+30.91%)</b></td><td>193.50 (-15.83%)</td><td>165.62 (-15.00%)</td><td>157.30 <b>(-22.47%)</b></td><td>129.50 <b>(-21.23%)</b></td><td>27.06 (-7.64%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>194.84 (n/a)</td><td>202.90 (n/a)</td><td>164.40 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (+12.80%)</td><td>0.19 (-1.88%)</td><td>0.25 (+19.94%)</td><td>0.09 <b>(-39.33%)</b></td><td>0.09 <b>(+128.66%)</b></td><td>371.20 <b>(+64.83%)</b></td><td>214.20 <b>(+24.35%)</b></td><td>132.50 (-16.61%)</td><td>119.60 (-11.34%)</td><td>120.69 <b>(+228.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.20 (n/a)</td><td>172.26 (n/a)</td><td>158.90 (n/a)</td><td>134.90 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 <b>(+47.51%)</b></td><td>0.25 <b>(+61.41%)</b></td><td>0.26 <b>(+63.21%)</b></td><td>0.22 <b>(+72.70%)</b></td><td>0.03 (+14.20%)</td><td>150.60 <b>(-42.10%)</b></td><td>130.14 <b>(-38.73%)</b></td><td>126.10 <b>(-38.76%)</b></td><td>110.80 <b>(-32.19%)</b></td><td>16.28 <b>(-54.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>260.10 (n/a)</td><td>212.42 (n/a)</td><td>205.90 (n/a)</td><td>163.40 (n/a)</td><td>35.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (+11.34%)</td><td>0.14 (+6.24%)</td><td>0.15 (+4.55%)</td><td>0.10 (-3.89%)</td><td>0.03 <b>(+33.42%)</b></td><td>316.30 (+4.05%)</td><td>237.80 (-4.51%)</td><td>220.10 (-4.35%)</td><td>184.40 (-10.18%)</td><td>53.01 <b>(+24.02%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>304.00 (n/a)</td><td>249.04 (n/a)</td><td>230.10 (n/a)</td><td>205.30 (n/a)</td><td>42.74 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (+2.57%)</td><td>0.16 (-6.46%)</td><td>0.17 (-0.47%)</td><td>0.10 <b>(-38.26%)</b></td><td>0.04 <b>(+246.58%)</b></td><td>329.40 <b>(+61.95%)</b></td><td>214.58 (+12.85%)</td><td>195.60 (+0.46%)</td><td>172.10 (-2.49%)</td><td>65.58 <b>(+463.90%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>190.14 (n/a)</td><td>194.70 (n/a)</td><td>176.50 (n/a)</td><td>11.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 <b>(+38.00%)</b></td><td>0.24 <b>(+37.24%)</b></td><td>0.22 <b>(+31.77%)</b></td><td>0.22 <b>(+41.81%)</b></td><td>0.02 <b>(+54.11%)</b></td><td>147.90 <b>(-29.47%)</b></td><td>139.62 <b>(-27.07%)</b></td><td>146.00 <b>(-24.12%)</b></td><td>124.90 <b>(-27.55%)</b></td><td>10.60 <b>(-20.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>191.44 (n/a)</td><td>192.40 (n/a)</td><td>172.40 (n/a)</td><td>13.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+15.34%)</td><td>0.21 <b>(+22.88%)</b></td><td>0.21 (+6.29%)</td><td>0.16 <b>(+62.89%)</b></td><td>0.04 <b>(-24.05%)</b></td><td>209.10 <b>(-38.61%)</b></td><td>162.26 <b>(-23.20%)</b></td><td>159.20 (-5.91%)</td><td>134.70 (-13.32%)</td><td>30.49 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>340.60 (n/a)</td><td>211.28 (n/a)</td><td>169.20 (n/a)</td><td>155.40 (n/a)</td><td>77.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (+8.21%)</td><td>0.21 (+3.12%)</td><td>0.20 (+3.14%)</td><td>0.16 (+4.68%)</td><td>0.05 (+19.38%)</td><td>202.90 (-4.47%)</td><td>164.66 (-2.31%)</td><td>166.30 (-3.03%)</td><td>115.00 (-7.63%)</td><td>33.11 (+4.74%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.40 (n/a)</td><td>168.56 (n/a)</td><td>171.50 (n/a)</td><td>124.50 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (+11.45%)</td><td>0.20 (+11.43%)</td><td>0.18 (-4.50%)</td><td>0.18 <b>(+107.96%)</b></td><td>0.03 <b>(-41.65%)</b></td><td>183.10 <b>(-51.90%)</b></td><td>167.20 (-19.05%)</td><td>179.80 (+4.72%)</td><td>129.20 (-10.28%)</td><td>22.84 <b>(-76.72%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>380.70 (n/a)</td><td>206.56 (n/a)</td><td>171.70 (n/a)</td><td>144.00 (n/a)</td><td>98.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 <b>(+20.83%)</b></td><td>0.24 <b>(+32.09%)</b></td><td>0.21 <b>(+32.97%)</b></td><td>0.18 (+17.74%)</td><td>0.06 <b>(+27.80%)</b></td><td>187.00 (-15.08%)</td><td>145.76 <b>(-23.87%)</b></td><td>157.20 <b>(-24.78%)</b></td><td>105.50 (-17.25%)</td><td>34.12 (-11.14%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>220.20 (n/a)</td><td>191.46 (n/a)</td><td>209.00 (n/a)</td><td>127.50 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 <b>(+20.42%)</b></td><td>0.23 <b>(+26.57%)</b></td><td>0.24 <b>(+28.70%)</b></td><td>0.18 <b>(+30.19%)</b></td><td>0.04 (+9.75%)</td><td>177.90 <b>(-23.19%)</b></td><td>146.50 <b>(-21.52%)</b></td><td>134.40 <b>(-22.31%)</b></td><td>123.80 (-16.91%)</td><td>24.85 <b>(-30.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.60 (n/a)</td><td>186.68 (n/a)</td><td>173.00 (n/a)</td><td>149.00 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 <b>(+29.66%)</b></td><td>0.24 <b>(+27.51%)</b></td><td>0.23 <b>(+24.25%)</b></td><td>0.20 <b>(+42.34%)</b></td><td>0.04 (+14.56%)</td><td>162.80 <b>(-29.74%)</b></td><td>139.72 <b>(-22.20%)</b></td><td>142.10 (-19.49%)</td><td>109.10 <b>(-22.90%)</b></td><td>21.34 <b>(-38.32%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.70 (n/a)</td><td>179.60 (n/a)</td><td>176.50 (n/a)</td><td>141.50 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 <b>(+45.47%)</b></td><td>0.22 <b>(+23.81%)</b></td><td>0.24 <b>(+34.67%)</b></td><td>0.17 (-4.86%)</td><td>0.04 <b>(+1752.73%)</b></td><td>196.80 (+5.07%)</td><td>152.98 (-16.38%)</td><td>135.30 <b>(-25.74%)</b></td><td>124.40 <b>(-31.27%)</b></td><td>32.99 <b>(+1224.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>182.94 (n/a)</td><td>182.20 (n/a)</td><td>181.00 (n/a)</td><td>2.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+6.33%)</td><td>0.20 (+7.44%)</td><td>0.20 (+5.68%)</td><td>0.16 (+12.99%)</td><td>0.03 (-6.18%)</td><td>207.00 (-11.50%)</td><td>165.52 (-7.50%)</td><td>161.00 (-5.35%)</td><td>138.70 (-5.97%)</td><td>25.06 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>233.90 (n/a)</td><td>178.94 (n/a)</td><td>170.10 (n/a)</td><td>147.50 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+16.02%)</td><td>0.21 (+11.18%)</td><td>0.21 (+11.07%)</td><td>0.18 (+5.54%)</td><td>0.03 <b>(+65.16%)</b></td><td>186.00 (-5.25%)</td><td>160.28 (-9.36%)</td><td>158.10 (-9.97%)</td><td>133.80 (-13.79%)</td><td>20.92 <b>(+35.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.30 (n/a)</td><td>176.84 (n/a)</td><td>175.60 (n/a)</td><td>155.20 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 <b>(+25.35%)</b></td><td>0.18 (-5.25%)</td><td>0.17 (-10.60%)</td><td>0.13 (-15.97%)</td><td>0.06 <b>(+135.35%)</b></td><td>257.40 (+19.00%)</td><td>198.62 (+11.42%)</td><td>198.00 (+11.86%)</td><td>122.50 <b>(-20.20%)</b></td><td>53.03 <b>(+119.43%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>178.26 (n/a)</td><td>177.00 (n/a)</td><td>153.50 (n/a)</td><td>24.17 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (-6.08%)</td><td>0.17 (-15.18%)</td><td>0.16 (-8.48%)</td><td>0.10 <b>(-37.83%)</b></td><td>0.05 <b>(+30.94%)</b></td><td>323.40 <b>(+60.82%)</b></td><td>212.98 <b>(+23.81%)</b></td><td>202.80 (+9.27%)</td><td>135.70 (+6.43%)</td><td>68.25 <b>(+131.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.10 (n/a)</td><td>172.02 (n/a)</td><td>185.60 (n/a)</td><td>127.50 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-0.10%)</td><td>0.18 (+0.00%)</td><td>0.18 (-0.10%)</td><td>0.18 (-0.04%)</td><td>0.00 <b>(-25.83%)</b></td><td>47636.90 (+0.04%)</td><td>47462.98 (-0.00%)</td><td>47432.80 (+0.10%)</td><td>47388.40 (+0.10%)</td><td>99.59 <b>(-25.72%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47619.70 (n/a)</td><td>47463.60 (n/a)</td><td>47384.60 (n/a)</td><td>47339.40 (n/a)</td><td>134.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (+0.10%)</td><td>0.18 (+0.17%)</td><td>0.18 (+0.13%)</td><td>0.18 (+0.25%)</td><td>0.00 <b>(-49.76%)</b></td><td>47494.90 (-0.25%)</td><td>47430.66 (-0.17%)</td><td>47423.00 (-0.13%)</td><td>47390.00 (-0.10%)</td><td>41.08 <b>(-49.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47615.80 (n/a)</td><td>47510.44 (n/a)</td><td>47484.30 (n/a)</td><td>47435.30 (n/a)</td><td>82.06 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (-0.00%)</td><td>0.11 (-0.03%)</td><td>0.11 (-0.03%)</td><td>0.11 (-0.05%)</td><td>0.00 <b>(+142.34%)</b></td><td>374669.70 (+0.05%)</td><td>374540.80 (+0.03%)</td><td>374564.80 (+0.03%)</td><td>374398.20 (+0.00%)</td><td>108.50 <b>(+142.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374498.60 (n/a)</td><td>374441.56 (n/a)</td><td>374447.50 (n/a)</td><td>374389.20 (n/a)</td><td>44.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-13.20%)</td><td>0.02 (-8.98%)</td><td>0.03 (+0.98%)</td><td>0.02 (-18.61%)</td><td>0.00 (-6.48%)</td><td>220.70 <b>(+22.88%)</b></td><td>169.96 (+10.51%)</td><td>160.10 (-0.99%)</td><td>135.60 (+15.21%)</td><td>32.29 <b>(+38.04%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.60 (n/a)</td><td>153.80 (n/a)</td><td>161.70 (n/a)</td><td>117.70 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (-13.78%)</td><td>0.04 (-9.56%)</td><td>0.04 (+0.50%)</td><td>0.03 (+10.57%)</td><td>0.01 <b>(-35.76%)</b></td><td>197.20 (-9.58%)</td><td>160.02 (+7.22%)</td><td>145.10 (-0.48%)</td><td>129.20 (+15.98%)</td><td>29.02 <b>(-31.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>149.24 (n/a)</td><td>145.80 (n/a)</td><td>111.40 (n/a)</td><td>42.35 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-14.14%)</td><td>0.03 (-3.77%)</td><td>0.03 (+2.86%)</td><td>0.02 (-11.10%)</td><td>0.00 <b>(-29.38%)</b></td><td>199.60 (+12.51%)</td><td>160.34 (+3.15%)</td><td>155.50 (-2.75%)</td><td>135.40 (+16.52%)</td><td>23.69 (-4.25%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.40 (n/a)</td><td>155.44 (n/a)</td><td>159.90 (n/a)</td><td>116.20 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-13.13%)</td><td>0.03 (-6.62%)</td><td>0.03 (+1.97%)</td><td>0.03 (-10.38%)</td><td>0.01 (-18.31%)</td><td>191.80 (+11.58%)</td><td>162.34 (+6.76%)</td><td>153.20 (-1.98%)</td><td>125.00 (+15.10%)</td><td>28.29 (+9.87%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>171.90 (n/a)</td><td>152.06 (n/a)</td><td>156.30 (n/a)</td><td>108.60 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+2.27%)</td><td>0.02 (+6.59%)</td><td>0.02 (-5.58%)</td><td>0.01 (+8.62%)</td><td>0.01 (+0.99%)</td><td>283.80 (-7.92%)</td><td>183.02 (-7.06%)</td><td>183.60 (+5.88%)</td><td>125.60 (-2.26%)</td><td>62.76 (-11.58%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>308.20 (n/a)</td><td>196.92 (n/a)</td><td>173.40 (n/a)</td><td>128.50 (n/a)</td><td>70.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (-4.58%)</td><td>0.03 (-7.43%)</td><td>0.03 <b>(-26.58%)</b></td><td>0.03 <b>(+73.70%)</b></td><td>0.01 <b>(-48.59%)</b></td><td>196.60 <b>(-42.41%)</b></td><td>169.52 (-4.62%)</td><td>176.00 <b>(+36.22%)</b></td><td>127.70 (+4.84%)</td><td>28.96 <b>(-69.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>341.40 (n/a)</td><td>177.74 (n/a)</td><td>129.20 (n/a)</td><td>121.80 (n/a)</td><td>93.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+10.89%)</td><td>0.03 (+4.79%)</td><td>0.02 (-5.17%)</td><td>0.02 (+0.13%)</td><td>0.01 <b>(+51.83%)</b></td><td>215.10 (-0.14%)</td><td>170.00 (-2.25%)</td><td>174.30 (+5.44%)</td><td>125.30 (-9.79%)</td><td>40.50 <b>(+33.81%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.40 (n/a)</td><td>173.92 (n/a)</td><td>165.30 (n/a)</td><td>138.90 (n/a)</td><td>30.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-12.45%)</td><td>0.03 (-8.78%)</td><td>0.02 (-8.28%)</td><td>0.02 (-3.17%)</td><td>0.00 <b>(-26.83%)</b></td><td>209.10 (+3.26%)</td><td>182.90 (+8.29%)</td><td>189.20 (+8.99%)</td><td>138.90 (+14.23%)</td><td>27.54 (-14.67%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>168.90 (n/a)</td><td>173.60 (n/a)</td><td>121.60 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+2.66%)</td><td>0.02 (-0.13%)</td><td>0.02 (-1.19%)</td><td>0.02 (-0.50%)</td><td>0.01 (-5.78%)</td><td>230.30 (+0.48%)</td><td>172.44 (-0.31%)</td><td>171.80 (+1.24%)</td><td>129.30 (-2.56%)</td><td>37.18 (-5.49%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>172.98 (n/a)</td><td>169.70 (n/a)</td><td>132.70 (n/a)</td><td>39.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-0.72%)</td><td>0.02 (-6.79%)</td><td>0.03 (+0.52%)</td><td>0.02 <b>(-27.57%)</b></td><td>0.01 <b>(+35.26%)</b></td><td>298.00 <b>(+38.09%)</b></td><td>199.54 (+10.90%)</td><td>183.30 (-0.54%)</td><td>148.60 (+0.75%)</td><td>57.31 <b>(+102.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>179.92 (n/a)</td><td>184.30 (n/a)</td><td>147.50 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-6.72%)</td><td>0.02 (-5.40%)</td><td>0.02 (-2.50%)</td><td>0.02 <b>(-22.61%)</b></td><td>0.01 <b>(+20.01%)</b></td><td>268.60 <b>(+29.20%)</b></td><td>184.22 (+10.19%)</td><td>173.20 (+2.55%)</td><td>121.60 (+7.23%)</td><td>59.70 <b>(+73.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>167.18 (n/a)</td><td>168.90 (n/a)</td><td>113.40 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-10.00%)</td><td>0.02 (+5.05%)</td><td>0.02 (+14.14%)</td><td>0.02 (+4.02%)</td><td>0.00 <b>(-34.69%)</b></td><td>212.70 (-3.89%)</td><td>188.30 (-6.14%)</td><td>184.60 (-12.39%)</td><td>159.00 (+11.11%)</td><td>23.71 <b>(-27.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.30 (n/a)</td><td>200.62 (n/a)</td><td>210.70 (n/a)</td><td>143.10 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (-2.43%)</td><td>0.02 (-1.69%)</td><td>0.02 <b>(-20.49%)</b></td><td>0.02 <b>(+55.71%)</b></td><td>0.00 <b>(-53.70%)</b></td><td>205.60 <b>(-35.79%)</b></td><td>180.90 (-5.86%)</td><td>191.60 <b>(+25.80%)</b></td><td>148.70 (+2.48%)</td><td>22.77 <b>(-69.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>320.20 (n/a)</td><td>192.16 (n/a)</td><td>152.30 (n/a)</td><td>145.10 (n/a)</td><td>74.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (+6.03%)</td><td>0.02 (-1.26%)</td><td>0.02 (-3.79%)</td><td>0.02 (+5.05%)</td><td>0.00 (+9.61%)</td><td>209.90 (-4.81%)</td><td>194.82 (+1.35%)</td><td>203.40 (+3.93%)</td><td>163.00 (-5.67%)</td><td>19.61 (-0.23%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>192.22 (n/a)</td><td>195.70 (n/a)</td><td>172.80 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 <b>(+20.88%)</b></td><td>0.02 (+2.71%)</td><td>0.02 (-3.87%)</td><td>0.01 (-4.88%)</td><td>0.00 <b>(+84.80%)</b></td><td>276.10 (+5.14%)</td><td>228.52 (-1.25%)</td><td>230.50 (+4.02%)</td><td>174.60 (-17.25%)</td><td>36.04 <b>(+57.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.60 (n/a)</td><td>231.42 (n/a)</td><td>221.60 (n/a)</td><td>211.00 (n/a)</td><td>22.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (-7.90%)</td><td>0.05 (-0.72%)</td><td>0.04 (-9.70%)</td><td>0.04 (-1.30%)</td><td>0.01 (-3.06%)</td><td>233.80 (+1.34%)</td><td>174.10 (+1.09%)</td><td>182.70 (+10.73%)</td><td>118.70 (+8.50%)</td><td>47.76 (+7.80%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>172.22 (n/a)</td><td>165.00 (n/a)</td><td>109.40 (n/a)</td><td>44.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (+10.12%)</td><td>0.08 (+2.86%)</td><td>0.07 (-11.67%)</td><td>0.07 (+5.45%)</td><td>0.02 <b>(+45.13%)</b></td><td>184.80 (-5.18%)</td><td>156.20 (-0.93%)</td><td>176.00 (+13.18%)</td><td>114.40 (-9.13%)</td><td>33.80 <b>(+26.23%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>157.66 (n/a)</td><td>155.50 (n/a)</td><td>125.90 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-15.56%)</td><td>0.05 (-2.12%)</td><td>0.06 (+5.24%)</td><td>0.04 (+7.08%)</td><td>0.01 <b>(-25.31%)</b></td><td>214.30 (-6.58%)</td><td>163.02 (+0.18%)</td><td>147.90 (-4.95%)</td><td>131.40 (+18.38%)</td><td>35.05 (-18.05%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>162.72 (n/a)</td><td>155.60 (n/a)</td><td>111.00 (n/a)</td><td>42.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (-7.82%)</td><td>0.06 (-6.48%)</td><td>0.07 (+9.97%)</td><td>0.05 (-11.53%)</td><td>0.01 (+4.83%)</td><td>217.30 (+13.00%)</td><td>171.08 (+7.65%)</td><td>150.40 (-9.07%)</td><td>146.00 (+8.47%)</td><td>31.77 <b>(+30.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>158.92 (n/a)</td><td>165.40 (n/a)</td><td>134.60 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 <b>(-22.71%)</b></td><td>0.05 (-4.18%)</td><td>0.05 (-0.08%)</td><td>0.04 (+2.07%)</td><td>0.01 <b>(-52.66%)</b></td><td>194.40 (-2.07%)</td><td>170.24 (+1.71%)</td><td>170.50 (+0.06%)</td><td>149.80 <b>(+29.36%)</b></td><td>19.61 <b>(-39.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>167.38 (n/a)</td><td>170.40 (n/a)</td><td>115.80 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (-2.46%)</td><td>0.06 (+2.04%)</td><td>0.06 (-2.78%)</td><td>0.05 (+10.57%)</td><td>0.01 (-4.70%)</td><td>197.20 (-9.58%)</td><td>167.36 (-2.44%)</td><td>175.60 (+2.81%)</td><td>131.80 (+2.49%)</td><td>29.23 (-11.21%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>171.54 (n/a)</td><td>170.80 (n/a)</td><td>128.60 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (-6.05%)</td><td>0.05 (+18.48%)</td><td>0.05 (+17.95%)</td><td>0.04 <b>(+85.11%)</b></td><td>0.01 <b>(-38.61%)</b></td><td>200.20 <b>(-45.96%)</b></td><td>155.14 <b>(-25.02%)</b></td><td>161.00 (-15.22%)</td><td>122.70 (+6.42%)</td><td>32.55 <b>(-67.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>370.50 (n/a)</td><td>206.92 (n/a)</td><td>189.90 (n/a)</td><td>115.30 (n/a)</td><td>98.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (+1.38%)</td><td>0.06 (-4.60%)</td><td>0.06 (-0.14%)</td><td>0.05 (-14.76%)</td><td>0.01 <b>(+47.63%)</b></td><td>202.80 (+17.29%)</td><td>166.70 (+6.49%)</td><td>158.70 (+0.13%)</td><td>127.50 (-1.32%)</td><td>29.44 <b>(+74.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.90 (n/a)</td><td>156.54 (n/a)</td><td>158.50 (n/a)</td><td>129.20 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-1.05%)</td><td>0.05 (+9.99%)</td><td>0.06 <b>(+22.03%)</b></td><td>0.05 (+7.31%)</td><td>0.00 <b>(-26.44%)</b></td><td>172.00 (-6.78%)</td><td>151.74 (-9.58%)</td><td>144.40 (-18.05%)</td><td>141.90 (+1.00%)</td><td>13.08 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>167.82 (n/a)</td><td>176.20 (n/a)</td><td>140.50 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-18.51%)</td><td>0.05 (+0.71%)</td><td>0.05 (+6.46%)</td><td>0.04 (+3.39%)</td><td>0.01 <b>(-40.89%)</b></td><td>221.90 (-3.27%)</td><td>180.96 (-3.21%)</td><td>171.00 (-6.04%)</td><td>155.30 <b>(+22.77%)</b></td><td>28.53 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>186.96 (n/a)</td><td>182.00 (n/a)</td><td>126.50 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (-13.36%)</td><td>0.05 (+7.32%)</td><td>0.05 (+18.94%)</td><td>0.04 (+5.67%)</td><td>0.01 <b>(-41.24%)</b></td><td>225.80 (-5.36%)</td><td>182.78 (-8.92%)</td><td>172.60 (-15.93%)</td><td>156.70 (+15.39%)</td><td>26.67 <b>(-31.77%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>200.68 (n/a)</td><td>205.30 (n/a)</td><td>135.80 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (+7.20%)</td><td>0.05 (-2.28%)</td><td>0.04 (-8.62%)</td><td>0.04 (-6.29%)</td><td>0.01 <b>(+105.65%)</b></td><td>214.60 (+6.71%)</td><td>193.36 (+3.33%)</td><td>207.90 (+9.42%)</td><td>161.80 (-6.69%)</td><td>23.60 <b>(+106.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>187.12 (n/a)</td><td>190.00 (n/a)</td><td>173.40 (n/a)</td><td>11.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (+8.39%)</td><td>0.05 (+12.36%)</td><td>0.05 (+11.39%)</td><td>0.04 <b>(+21.96%)</b></td><td>0.01 (-7.13%)</td><td>210.80 (-18.01%)</td><td>172.22 (-11.92%)</td><td>162.70 (-10.21%)</td><td>143.80 (-7.76%)</td><td>27.45 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.10 (n/a)</td><td>195.52 (n/a)</td><td>181.20 (n/a)</td><td>155.90 (n/a)</td><td>39.46 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (-2.30%)</td><td>0.05 (-12.36%)</td><td>0.04 (-10.00%)</td><td>0.04 (-8.67%)</td><td>0.01 (-4.98%)</td><td>212.90 (+9.46%)</td><td>191.96 (+14.11%)</td><td>209.30 (+11.09%)</td><td>135.70 (+2.42%)</td><td>32.48 (+5.38%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>168.22 (n/a)</td><td>188.40 (n/a)</td><td>132.50 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (-2.82%)</td><td>0.04 (-6.85%)</td><td>0.04 (-10.63%)</td><td>0.03 (-13.71%)</td><td>0.01 <b>(+38.82%)</b></td><td>279.40 (+15.89%)</td><td>218.76 (+9.07%)</td><td>219.30 (+11.89%)</td><td>176.50 (+2.92%)</td><td>42.36 <b>(+60.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.10 (n/a)</td><td>200.56 (n/a)</td><td>196.00 (n/a)</td><td>171.50 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+6.02%)</td><td>0.10 (+5.10%)</td><td>0.09 (-8.47%)</td><td>0.08 (+19.01%)</td><td>0.02 (-18.01%)</td><td>212.00 (-15.97%)</td><td>172.28 (-7.60%)</td><td>175.50 (+9.21%)</td><td>126.60 (-5.66%)</td><td>32.69 <b>(-37.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>252.30 (n/a)</td><td>186.46 (n/a)</td><td>160.70 (n/a)</td><td>134.20 (n/a)</td><td>52.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 <b>(-22.02%)</b></td><td>0.15 (-1.61%)</td><td>0.15 (+5.75%)</td><td>0.13 (+11.33%)</td><td>0.01 <b>(-62.89%)</b></td><td>184.60 (-10.21%)</td><td>169.30 (-1.05%)</td><td>168.30 (-5.40%)</td><td>155.20 <b>(+28.26%)</b></td><td>13.94 <b>(-55.75%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>171.10 (n/a)</td><td>177.90 (n/a)</td><td>121.00 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-11.25%)</td><td>0.11 (-0.83%)</td><td>0.11 (-8.10%)</td><td>0.10 <b>(+25.88%)</b></td><td>0.01 <b>(-49.65%)</b></td><td>169.30 <b>(-20.52%)</b></td><td>146.54 (-3.15%)</td><td>147.40 (+8.78%)</td><td>125.60 (+12.65%)</td><td>17.98 <b>(-55.72%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>213.00 (n/a)</td><td>151.30 (n/a)</td><td>135.50 (n/a)</td><td>111.50 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (+9.22%)</td><td>0.13 (+13.87%)</td><td>0.13 (+9.05%)</td><td>0.10 <b>(+35.97%)</b></td><td>0.02 <b>(-28.06%)</b></td><td>202.60 <b>(-26.43%)</b></td><td>162.96 (-15.08%)</td><td>160.20 (-8.35%)</td><td>134.00 (-8.47%)</td><td>25.70 <b>(-51.04%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>275.40 (n/a)</td><td>191.90 (n/a)</td><td>174.80 (n/a)</td><td>146.40 (n/a)</td><td>52.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (+5.13%)</td><td>0.11 (-2.83%)</td><td>0.10 <b>(-20.76%)</b></td><td>0.08 <b>(+38.63%)</b></td><td>0.02 <b>(-32.73%)</b></td><td>193.20 <b>(-27.88%)</b></td><td>159.40 (-2.83%)</td><td>165.00 <b>(+26.15%)</b></td><td>119.00 (-4.88%)</td><td>27.69 <b>(-54.48%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>267.90 (n/a)</td><td>164.04 (n/a)</td><td>130.80 (n/a)</td><td>125.10 (n/a)</td><td>60.83 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-5.95%)</td><td>0.12 (+0.95%)</td><td>0.12 (+1.91%)</td><td>0.11 (+7.66%)</td><td>0.01 <b>(-48.12%)</b></td><td>179.20 (-7.10%)</td><td>167.56 (-1.62%)</td><td>166.10 (-1.89%)</td><td>154.20 (+6.34%)</td><td>9.39 <b>(-48.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>170.32 (n/a)</td><td>169.30 (n/a)</td><td>145.00 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (-8.67%)</td><td>0.09 (-13.27%)</td><td>0.09 (-17.29%)</td><td>0.05 <b>(-35.58%)</b></td><td>0.04 <b>(+49.38%)</b></td><td>301.10 <b>(+55.21%)</b></td><td>197.28 <b>(+26.41%)</b></td><td>186.90 <b>(+20.89%)</b></td><td>120.30 (+9.56%)</td><td>78.14 <b>(+151.96%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>156.06 (n/a)</td><td>154.60 (n/a)</td><td>109.80 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (+5.97%)</td><td>0.12 <b>(+20.37%)</b></td><td>0.12 <b>(+23.98%)</b></td><td>0.10 <b>(+63.52%)</b></td><td>0.01 <b>(-38.95%)</b></td><td>190.00 <b>(-38.83%)</b></td><td>160.80 <b>(-20.90%)</b></td><td>154.40 (-19.33%)</td><td>141.10 (-5.62%)</td><td>21.22 <b>(-66.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>310.60 (n/a)</td><td>203.28 (n/a)</td><td>191.40 (n/a)</td><td>149.50 (n/a)</td><td>63.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 <b>(+31.69%)</b></td><td>0.11 (+16.22%)</td><td>0.11 (+11.26%)</td><td>0.09 (+9.96%)</td><td>0.02 <b>(+91.93%)</b></td><td>187.00 (-9.05%)</td><td>147.76 (-12.18%)</td><td>146.90 (-10.10%)</td><td>113.80 <b>(-24.03%)</b></td><td>30.21 <b>(+31.93%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>168.26 (n/a)</td><td>163.40 (n/a)</td><td>149.80 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 <b>(+43.69%)</b></td><td>0.11 <b>(+31.90%)</b></td><td>0.11 <b>(+20.71%)</b></td><td>0.09 <b>(+43.69%)</b></td><td>0.02 <b>(+53.48%)</b></td><td>203.80 <b>(-30.42%)</b></td><td>171.72 <b>(-24.02%)</b></td><td>174.10 (-17.13%)</td><td>136.60 <b>(-30.41%)</b></td><td>28.08 <b>(-27.52%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>292.90 (n/a)</td><td>226.00 (n/a)</td><td>210.10 (n/a)</td><td>196.30 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (+19.21%)</td><td>0.10 (+5.75%)</td><td>0.11 (+4.71%)</td><td>0.05 <b>(-31.80%)</b></td><td>0.03 <b>(+130.09%)</b></td><td>302.60 <b>(+46.61%)</b></td><td>176.66 (+2.06%)</td><td>150.30 (-4.51%)</td><td>131.20 (-16.11%)</td><td>70.88 <b>(+208.90%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>173.10 (n/a)</td><td>157.40 (n/a)</td><td>156.40 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (+17.93%)</td><td>0.10 <b>(+26.84%)</b></td><td>0.10 <b>(+23.09%)</b></td><td>0.08 <b>(+47.29%)</b></td><td>0.02 (-11.62%)</td><td>207.90 <b>(-32.10%)</b></td><td>175.88 <b>(-22.81%)</b></td><td>171.80 (-18.77%)</td><td>142.40 (-15.19%)</td><td>26.07 <b>(-49.43%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>306.20 (n/a)</td><td>227.86 (n/a)</td><td>211.50 (n/a)</td><td>167.90 (n/a)</td><td>51.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 <b>(-26.56%)</b></td><td>0.09 (-18.25%)</td><td>0.09 (-17.04%)</td><td>0.08 (-14.73%)</td><td>0.01 <b>(-45.09%)</b></td><td>210.20 (+17.30%)</td><td>185.32 <b>(+20.97%)</b></td><td>189.90 <b>(+20.57%)</b></td><td>155.50 <b>(+36.16%)</b></td><td>21.64 (-8.94%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>179.20 (n/a)</td><td>153.20 (n/a)</td><td>157.50 (n/a)</td><td>114.20 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (+10.46%)</td><td>0.09 (-4.32%)</td><td>0.08 (-13.33%)</td><td>0.07 (-7.77%)</td><td>0.03 <b>(+39.74%)</b></td><td>243.80 (+8.40%)</td><td>204.14 (+7.37%)</td><td>223.00 (+15.36%)</td><td>123.90 (-9.43%)</td><td>47.80 <b>(+30.92%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>224.90 (n/a)</td><td>190.12 (n/a)</td><td>193.30 (n/a)</td><td>136.80 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (-2.50%)</td><td>0.08 (-7.56%)</td><td>0.09 (+1.08%)</td><td>0.05 <b>(-34.26%)</b></td><td>0.02 <b>(+104.86%)</b></td><td>347.90 <b>(+52.12%)</b></td><td>220.70 (+13.96%)</td><td>191.00 (-1.09%)</td><td>177.10 (+2.55%)</td><td>71.57 <b>(+230.91%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>193.66 (n/a)</td><td>193.10 (n/a)</td><td>172.70 (n/a)</td><td>21.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (-13.50%)</td><td>0.19 (-14.72%)</td><td>0.17 (-14.87%)</td><td>0.14 <b>(-26.52%)</b></td><td>0.05 <b>(+29.50%)</b></td><td>229.30 <b>(+36.08%)</b></td><td>185.26 <b>(+20.64%)</b></td><td>191.60 (+17.47%)</td><td>136.30 (+15.61%)</td><td>43.09 <b>(+107.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.50 (n/a)</td><td>153.56 (n/a)</td><td>163.10 (n/a)</td><td>117.90 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (-11.07%)</td><td>0.20 (-8.08%)</td><td>0.21 (-10.94%)</td><td>0.13 <b>(-21.17%)</b></td><td>0.05 (-5.70%)</td><td>258.80 <b>(+26.86%)</b></td><td>172.94 (+10.03%)</td><td>158.00 (+12.30%)</td><td>127.70 (+12.41%)</td><td>51.91 <b>(+32.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.00 (n/a)</td><td>157.18 (n/a)</td><td>140.70 (n/a)</td><td>113.60 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 <b>(+20.22%)</b></td><td>0.24 (-5.56%)</td><td>0.23 (-12.62%)</td><td>0.19 (-18.80%)</td><td>0.05 <b>(+201.87%)</b></td><td>215.50 <b>(+23.14%)</b></td><td>174.30 (+9.02%)</td><td>176.20 (+14.42%)</td><td>124.40 (-16.79%)</td><td>33.18 <b>(+199.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>175.00 (n/a)</td><td>159.88 (n/a)</td><td>154.00 (n/a)</td><td>149.50 (n/a)</td><td>11.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (+10.40%)</td><td>0.22 (+3.75%)</td><td>0.20 (-4.70%)</td><td>0.16 (-9.76%)</td><td>0.06 <b>(+62.78%)</b></td><td>201.10 (+10.80%)</td><td>154.04 (-0.70%)</td><td>161.50 (+4.94%)</td><td>115.50 (-9.41%)</td><td>37.87 <b>(+52.93%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.50 (n/a)</td><td>155.12 (n/a)</td><td>153.90 (n/a)</td><td>127.50 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (+1.40%)</td><td>0.25 (-7.74%)</td><td>0.23 (-13.54%)</td><td>0.20 (-4.32%)</td><td>0.05 (+14.51%)</td><td>205.70 (+4.52%)</td><td>171.04 (+9.36%)</td><td>178.40 (+15.69%)</td><td>125.70 (-1.41%)</td><td>33.50 (+19.72%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>196.80 (n/a)</td><td>156.40 (n/a)</td><td>154.20 (n/a)</td><td>127.50 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (-6.17%)</td><td>0.20 (-13.44%)</td><td>0.19 <b>(-21.27%)</b></td><td>0.18 (+0.23%)</td><td>0.03 (-12.89%)</td><td>179.80 (-0.28%)</td><td>164.34 (+14.97%)</td><td>171.00 <b>(+26.95%)</b></td><td>125.30 (+6.64%)</td><td>22.63 (-9.45%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.30 (n/a)</td><td>142.94 (n/a)</td><td>134.70 (n/a)</td><td>117.50 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (-16.71%)</td><td>0.23 (-0.73%)</td><td>0.24 (-1.37%)</td><td>0.18 <b>(+26.42%)</b></td><td>0.03 <b>(-52.26%)</b></td><td>204.00 <b>(-20.90%)</b></td><td>161.54 (-5.03%)</td><td>156.40 (+1.36%)</td><td>136.20 <b>(+20.11%)</b></td><td>25.38 <b>(-54.32%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>257.90 (n/a)</td><td>170.10 (n/a)</td><td>154.30 (n/a)</td><td>113.40 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 <b>(-24.94%)</b></td><td>0.20 (-14.72%)</td><td>0.20 <b>(-24.43%)</b></td><td>0.18 (+12.63%)</td><td>0.02 <b>(-70.11%)</b></td><td>177.90 (-11.23%)</td><td>162.82 (+12.57%)</td><td>167.10 <b>(+32.30%)</b></td><td>148.10 <b>(+33.18%)</b></td><td>12.60 <b>(-65.37%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>200.40 (n/a)</td><td>144.64 (n/a)</td><td>126.30 (n/a)</td><td>111.20 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (-14.59%)</td><td>0.22 (-5.88%)</td><td>0.23 (+9.74%)</td><td>0.17 (-15.07%)</td><td>0.04 <b>(-21.99%)</b></td><td>223.00 (+17.74%)</td><td>168.86 (+5.84%)</td><td>157.70 (-8.84%)</td><td>136.90 (+17.11%)</td><td>32.74 (+11.71%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>189.40 (n/a)</td><td>159.54 (n/a)</td><td>173.00 (n/a)</td><td>116.90 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (-7.91%)</td><td>0.17 (-15.83%)</td><td>0.18 (-14.14%)</td><td>0.11 <b>(-40.19%)</b></td><td>0.04 <b>(+103.62%)</b></td><td>309.30 <b>(+67.19%)</b></td><td>203.44 <b>(+24.63%)</b></td><td>184.00 (+16.46%)</td><td>156.80 (+8.59%)</td><td>60.62 <b>(+289.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.00 (n/a)</td><td>163.24 (n/a)</td><td>158.00 (n/a)</td><td>144.40 (n/a)</td><td>15.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+3.95%)</td><td>0.20 (+0.61%)</td><td>0.21 (+9.82%)</td><td>0.17 (+0.10%)</td><td>0.03 (+17.66%)</td><td>210.70 (-0.09%)</td><td>180.20 (-0.09%)</td><td>169.50 (-8.97%)</td><td>145.70 (-3.76%)</td><td>27.36 (+16.66%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>210.90 (n/a)</td><td>180.36 (n/a)</td><td>186.20 (n/a)</td><td>151.40 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (-18.23%)</td><td>0.19 (-9.88%)</td><td>0.18 (-9.85%)</td><td>0.17 (-6.72%)</td><td>0.02 <b>(-49.28%)</b></td><td>194.90 (+7.21%)</td><td>176.00 (+9.68%)</td><td>179.30 (+10.88%)</td><td>154.50 <b>(+22.33%)</b></td><td>14.85 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.80 (n/a)</td><td>160.46 (n/a)</td><td>161.70 (n/a)</td><td>126.30 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 <b>(+24.17%)</b></td><td>0.18 (+2.51%)</td><td>0.17 (-10.75%)</td><td>0.16 (+0.75%)</td><td>0.04 <b>(+98.50%)</b></td><td>222.40 (-0.76%)</td><td>193.20 (-0.77%)</td><td>209.10 (+12.00%)</td><td>142.80 (-19.46%)</td><td>31.84 <b>(+57.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>194.70 (n/a)</td><td>186.70 (n/a)</td><td>177.30 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (-10.24%)</td><td>0.16 (-13.43%)</td><td>0.16 (-16.60%)</td><td>0.11 <b>(-26.76%)</b></td><td>0.04 (+15.21%)</td><td>302.20 <b>(+36.56%)</b></td><td>217.82 (+18.20%)</td><td>208.40 (+19.91%)</td><td>164.30 (+11.39%)</td><td>55.71 <b>(+68.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.30 (n/a)</td><td>184.28 (n/a)</td><td>173.80 (n/a)</td><td>147.50 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (-14.08%)</td><td>0.13 (-3.68%)</td><td>0.13 (+10.57%)</td><td>0.10 (-3.74%)</td><td>0.02 <b>(-39.18%)</b></td><td>209.20 (+3.87%)</td><td>165.40 (+1.68%)</td><td>157.10 (-9.56%)</td><td>140.20 (+16.45%)</td><td>26.41 <b>(-23.68%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>162.66 (n/a)</td><td>173.70 (n/a)</td><td>120.40 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-5.92%)</td><td>0.11 (-2.66%)</td><td>0.11 (-3.24%)</td><td>0.10 (+14.12%)</td><td>0.01 <b>(-41.83%)</b></td><td>210.70 (-12.35%)</td><td>189.98 (+1.01%)</td><td>188.20 (+3.35%)</td><td>162.90 (+6.33%)</td><td>18.36 <b>(-46.31%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.40 (n/a)</td><td>188.08 (n/a)</td><td>182.10 (n/a)</td><td>153.20 (n/a)</td><td>34.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 <b>(-26.23%)</b></td><td>0.12 (-18.36%)</td><td>0.11 (-19.64%)</td><td>0.11 (+6.64%)</td><td>0.01 <b>(-67.33%)</b></td><td>189.30 (-6.24%)</td><td>173.24 (+17.05%)</td><td>178.10 <b>(+24.46%)</b></td><td>147.30 <b>(+35.51%)</b></td><td>15.94 <b>(-58.61%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>201.90 (n/a)</td><td>148.00 (n/a)</td><td>143.10 (n/a)</td><td>108.70 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (+2.18%)</td><td>0.13 (-0.69%)</td><td>0.12 (-13.87%)</td><td>0.11 <b>(+21.57%)</b></td><td>0.02 <b>(-32.52%)</b></td><td>179.30 (-17.75%)</td><td>160.84 (-1.11%)</td><td>166.10 (+16.07%)</td><td>136.20 (-2.08%)</td><td>18.16 <b>(-45.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>162.64 (n/a)</td><td>143.10 (n/a)</td><td>139.10 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-14.96%)</td><td>0.12 (-8.10%)</td><td>0.12 (-0.20%)</td><td>0.09 (-8.61%)</td><td>0.02 (-10.44%)</td><td>218.40 (+9.42%)</td><td>181.04 (+8.96%)</td><td>167.80 (+0.18%)</td><td>153.60 (+17.61%)</td><td>28.91 (+18.11%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>199.60 (n/a)</td><td>166.16 (n/a)</td><td>167.50 (n/a)</td><td>130.60 (n/a)</td><td>24.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (-18.92%)</td><td>0.12 (+3.03%)</td><td>0.11 (-3.57%)</td><td>0.11 <b>(+36.85%)</b></td><td>0.01 <b>(-62.84%)</b></td><td>188.90 <b>(-26.95%)</b></td><td>172.32 (-8.01%)</td><td>181.30 (+3.72%)</td><td>149.70 <b>(+23.31%)</b></td><td>17.11 <b>(-66.15%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>258.60 (n/a)</td><td>187.32 (n/a)</td><td>174.80 (n/a)</td><td>121.40 (n/a)</td><td>50.57 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (-5.47%)</td><td>0.11 (+5.58%)</td><td>0.10 (+7.54%)</td><td>0.10 <b>(+28.58%)</b></td><td>0.01 <b>(-55.37%)</b></td><td>210.40 <b>(-22.22%)</b></td><td>191.16 (-9.24%)</td><td>196.10 (-7.02%)</td><td>166.40 (+5.79%)</td><td>19.93 <b>(-62.16%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>270.50 (n/a)</td><td>210.62 (n/a)</td><td>210.90 (n/a)</td><td>157.30 (n/a)</td><td>52.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (-8.25%)</td><td>0.12 (-5.86%)</td><td>0.12 (-9.91%)</td><td>0.10 (+7.17%)</td><td>0.02 <b>(-28.35%)</b></td><td>195.40 (-6.69%)</td><td>171.24 (+4.88%)</td><td>172.80 (+10.98%)</td><td>139.60 (+8.98%)</td><td>21.81 <b>(-28.26%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>209.40 (n/a)</td><td>163.28 (n/a)</td><td>155.70 (n/a)</td><td>128.10 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (-4.36%)</td><td>0.15 (+5.98%)</td><td>0.16 (+13.98%)</td><td>0.12 (+6.06%)</td><td>0.03 (-15.35%)</td><td>198.30 (-5.71%)</td><td>163.42 (-6.34%)</td><td>157.30 (-12.27%)</td><td>131.10 (+4.55%)</td><td>27.10 (-12.19%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>210.30 (n/a)</td><td>174.48 (n/a)</td><td>179.30 (n/a)</td><td>125.40 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-11.76%)</td><td>0.15 (-6.45%)</td><td>0.13 (-7.15%)</td><td>0.12 (-10.50%)</td><td>0.03 (-3.10%)</td><td>205.10 (+11.71%)</td><td>171.94 (+7.38%)</td><td>186.80 (+7.73%)</td><td>135.00 (+13.35%)</td><td>31.65 <b>(+21.70%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.60 (n/a)</td><td>160.12 (n/a)</td><td>173.40 (n/a)</td><td>119.10 (n/a)</td><td>26.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-4.71%)</td><td>0.15 (-11.38%)</td><td>0.15 (-9.64%)</td><td>0.12 <b>(-20.97%)</b></td><td>0.02 <b>(+56.04%)</b></td><td>205.50 <b>(+26.54%)</b></td><td>164.38 (+14.26%)</td><td>159.30 (+10.70%)</td><td>136.00 (+4.94%)</td><td>25.56 <b>(+110.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>162.40 (n/a)</td><td>143.86 (n/a)</td><td>143.90 (n/a)</td><td>129.60 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (-13.15%)</td><td>0.17 (+2.71%)</td><td>0.18 (+12.82%)</td><td>0.13 (+8.70%)</td><td>0.02 <b>(-31.17%)</b></td><td>182.30 (-8.02%)</td><td>150.80 (-3.90%)</td><td>137.90 (-11.32%)</td><td>135.90 (+15.17%)</td><td>20.60 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.20 (n/a)</td><td>156.92 (n/a)</td><td>155.50 (n/a)</td><td>118.00 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (-14.84%)</td><td>0.15 (-11.63%)</td><td>0.15 (-12.87%)</td><td>0.12 (+4.03%)</td><td>0.03 <b>(-28.80%)</b></td><td>205.10 (-3.84%)</td><td>172.94 (+10.48%)</td><td>169.20 (+14.71%)</td><td>122.70 (+17.42%)</td><td>33.56 (-19.16%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>213.30 (n/a)</td><td>156.54 (n/a)</td><td>147.50 (n/a)</td><td>104.50 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (+18.81%)</td><td>0.16 <b>(+25.53%)</b></td><td>0.17 <b>(+49.53%)</b></td><td>0.12 (+15.07%)</td><td>0.03 (+8.05%)</td><td>203.20 (-13.09%)</td><td>156.36 <b>(-20.73%)</b></td><td>144.70 <b>(-33.13%)</b></td><td>123.90 (-15.83%)</td><td>30.97 <b>(-20.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>233.80 (n/a)</td><td>197.24 (n/a)</td><td>216.40 (n/a)</td><td>147.20 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (+0.66%)</td><td>0.14 (+3.74%)</td><td>0.14 (+9.11%)</td><td>0.12 (-4.46%)</td><td>0.01 <b>(+32.45%)</b></td><td>208.70 (+4.66%)</td><td>181.60 (-3.34%)</td><td>172.80 (-8.38%)</td><td>168.30 (-0.71%)</td><td>16.80 <b>(+37.76%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>187.88 (n/a)</td><td>188.60 (n/a)</td><td>169.50 (n/a)</td><td>12.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (+3.37%)</td><td>0.12 (-8.60%)</td><td>0.12 (-11.65%)</td><td>0.11 (-8.33%)</td><td>0.02 <b>(+58.30%)</b></td><td>224.70 (+9.08%)</td><td>200.80 (+10.48%)</td><td>207.80 (+13.18%)</td><td>157.10 (-3.26%)</td><td>26.40 <b>(+62.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>181.76 (n/a)</td><td>183.60 (n/a)</td><td>162.40 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (-0.39%)</td><td>0.11 (+16.68%)</td><td>0.12 (+10.82%)</td><td>0.10 <b>(+93.93%)</b></td><td>0.01 <b>(-58.18%)</b></td><td>188.00 <b>(-48.44%)</b></td><td>161.96 <b>(-21.95%)</b></td><td>158.30 (-9.75%)</td><td>145.60 (+0.34%)</td><td>17.60 <b>(-80.20%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>364.60 (n/a)</td><td>207.50 (n/a)</td><td>175.40 (n/a)</td><td>145.10 (n/a)</td><td>88.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (+2.34%)</td><td>0.11 (+0.19%)</td><td>0.11 (-4.84%)</td><td>0.09 (+15.41%)</td><td>0.02 (-17.21%)</td><td>206.60 (-13.34%)</td><td>165.80 (-1.97%)</td><td>167.10 (+5.09%)</td><td>127.80 (-2.29%)</td><td>28.17 <b>(-32.46%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>238.40 (n/a)</td><td>169.14 (n/a)</td><td>159.00 (n/a)</td><td>130.80 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (+5.99%)</td><td>0.12 (+17.34%)</td><td>0.12 (+16.67%)</td><td>0.10 <b>(+31.14%)</b></td><td>0.02 <b>(-31.13%)</b></td><td>181.40 <b>(-23.75%)</b></td><td>153.48 (-17.30%)</td><td>154.50 (-14.26%)</td><td>124.40 (-5.61%)</td><td>21.03 <b>(-51.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>237.90 (n/a)</td><td>185.58 (n/a)</td><td>180.20 (n/a)</td><td>131.80 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (-15.03%)</td><td>0.11 (-7.33%)</td><td>0.11 (-0.67%)</td><td>0.08 (-16.19%)</td><td>0.02 <b>(-20.74%)</b></td><td>236.90 (+19.35%)</td><td>177.52 (+7.63%)</td><td>171.70 (+0.70%)</td><td>153.20 (+17.67%)</td><td>34.43 (+13.99%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.50 (n/a)</td><td>164.94 (n/a)</td><td>170.50 (n/a)</td><td>130.20 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (-3.91%)</td><td>0.11 (-8.24%)</td><td>0.09 (-7.12%)</td><td>0.08 (-7.56%)</td><td>0.03 (-2.32%)</td><td>220.00 (+8.21%)</td><td>182.88 (+9.12%)</td><td>197.60 (+7.68%)</td><td>111.90 (+4.09%)</td><td>41.84 (+4.19%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>203.30 (n/a)</td><td>167.60 (n/a)</td><td>183.50 (n/a)</td><td>107.50 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (+4.27%)</td><td>0.12 (+1.09%)</td><td>0.11 (-8.57%)</td><td>0.10 <b>(+66.57%)</b></td><td>0.03 <b>(-37.17%)</b></td><td>184.60 <b>(-39.97%)</b></td><td>158.34 (-10.19%)</td><td>163.80 (+9.42%)</td><td>111.70 (-4.12%)</td><td>27.48 <b>(-65.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>307.50 (n/a)</td><td>176.30 (n/a)</td><td>149.70 (n/a)</td><td>116.50 (n/a)</td><td>78.80 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (-17.66%)</td><td>0.09 (-3.08%)</td><td>0.09 (-11.49%)</td><td>0.09 <b>(+24.99%)</b></td><td>0.01 <b>(-66.39%)</b></td><td>214.60 (-19.99%)</td><td>199.82 (-0.37%)</td><td>207.80 (+12.93%)</td><td>183.90 <b>(+21.39%)</b></td><td>14.51 <b>(-68.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>268.20 (n/a)</td><td>200.56 (n/a)</td><td>184.00 (n/a)</td><td>151.50 (n/a)</td><td>45.61 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 <b>(+46.53%)</b></td><td>0.11 (+9.40%)</td><td>0.09 (-1.29%)</td><td>0.06 <b>(-28.29%)</b></td><td>0.04 <b>(+299.22%)</b></td><td>290.10 <b>(+39.47%)</b></td><td>191.00 (-0.17%)</td><td>197.80 (+1.28%)</td><td>114.70 <b>(-31.73%)</b></td><td>65.76 <b>(+274.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>191.32 (n/a)</td><td>195.30 (n/a)</td><td>168.00 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.78 (+6.07%)</td><td>0.58 (+5.67%)</td><td>0.55 (+5.70%)</td><td>0.43 (-8.80%)</td><td>0.14 <b>(+26.78%)</b></td><td>230.30 (+9.61%)</td><td>178.10 (-3.73%)</td><td>178.10 (-5.37%)</td><td>126.50 (-5.74%)</td><td>40.46 <b>(+32.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.73 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.11 (n/a)</td><td>210.10 (n/a)</td><td>185.00 (n/a)</td><td>188.20 (n/a)</td><td>134.20 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.82 (-7.65%)</td><td>0.68 (-3.22%)</td><td>0.66 (-9.71%)</td><td>0.48 (-15.96%)</td><td>0.14 (+9.22%)</td><td>202.80 (+19.01%)</td><td>150.18 (+4.52%)</td><td>149.80 (+10.72%)</td><td>119.80 (+8.32%)</td><td>34.01 <b>(+32.41%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.89 (n/a)</td><td>0.70 (n/a)</td><td>0.73 (n/a)</td><td>0.58 (n/a)</td><td>0.13 (n/a)</td><td>170.40 (n/a)</td><td>143.68 (n/a)</td><td>135.30 (n/a)</td><td>110.60 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.94 (+19.27%)</td><td>0.61 (+4.20%)</td><td>0.56 (+1.64%)</td><td>0.31 <b>(-25.01%)</b></td><td>0.23 <b>(+56.06%)</b></td><td>313.50 <b>(+33.35%)</b></td><td>183.52 (+3.75%)</td><td>175.70 (-1.62%)</td><td>104.40 (-16.14%)</td><td>78.60 <b>(+81.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.79 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.15 (n/a)</td><td>235.10 (n/a)</td><td>176.88 (n/a)</td><td>178.60 (n/a)</td><td>124.50 (n/a)</td><td>43.23 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.55 <b>(+27.90%)</b></td><td>0.50 <b>(+36.97%)</b></td><td>0.50 <b>(+30.34%)</b></td><td>0.47 <b>(+81.14%)</b></td><td>0.03 <b>(-48.69%)</b></td><td>209.80 <b>(-44.80%)</b></td><td>195.54 <b>(-29.10%)</b></td><td>196.90 <b>(-23.27%)</b></td><td>177.40 <b>(-21.82%)</b></td><td>13.19 <b>(-78.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>380.10 (n/a)</td><td>275.78 (n/a)</td><td>256.60 (n/a)</td><td>226.90 (n/a)</td><td>61.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.51 (-3.80%)</td><td>0.46 (+12.56%)</td><td>0.50 <b>(+21.70%)</b></td><td>0.36 <b>(+76.15%)</b></td><td>0.07 <b>(-46.73%)</b></td><td>205.40 <b>(-43.21%)</b></td><td>164.32 (-19.33%)</td><td>147.80 (-17.80%)</td><td>144.40 (+3.96%)</td><td>27.20 <b>(-70.15%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>361.70 (n/a)</td><td>203.70 (n/a)</td><td>179.80 (n/a)</td><td>138.90 (n/a)</td><td>91.14 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.60 (+13.61%)</td><td>0.54 (+19.07%)</td><td>0.56 <b>(+20.54%)</b></td><td>0.45 <b>(+30.89%)</b></td><td>0.07 (-6.33%)</td><td>165.00 <b>(-23.58%)</b></td><td>139.40 (-16.90%)</td><td>131.40 (-17.05%)</td><td>122.10 (-12.03%)</td><td>19.58 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>215.90 (n/a)</td><td>167.74 (n/a)</td><td>158.40 (n/a)</td><td>138.80 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.62 (+3.40%)</td><td>0.50 (+6.45%)</td><td>0.48 (+1.44%)</td><td>0.40 (+17.21%)</td><td>0.10 (-16.88%)</td><td>183.80 (-14.67%)</td><td>152.24 (-8.32%)</td><td>155.20 (-1.40%)</td><td>119.80 (-3.31%)</td><td>30.58 <b>(-31.48%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>215.40 (n/a)</td><td>166.06 (n/a)</td><td>157.40 (n/a)</td><td>123.90 (n/a)</td><td>44.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.57 <b>(+23.00%)</b></td><td>0.44 (+13.64%)</td><td>0.42 (+13.31%)</td><td>0.35 (+9.10%)</td><td>0.08 <b>(+51.01%)</b></td><td>212.00 (-8.34%)</td><td>172.60 (-11.07%)</td><td>174.20 (-11.71%)</td><td>129.50 (-18.71%)</td><td>30.23 (+11.08%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>231.30 (n/a)</td><td>194.08 (n/a)</td><td>197.30 (n/a)</td><td>159.30 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.29 (-0.71%)</td><td>0.24 (+2.79%)</td><td>0.25 (+8.51%)</td><td>0.18 (-7.50%)</td><td>0.05 <b>(+26.26%)</b></td><td>200.30 (+8.09%)</td><td>158.98 (-1.46%)</td><td>148.40 (-7.83%)</td><td>128.80 (+0.70%)</td><td>31.91 <b>(+35.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>185.30 (n/a)</td><td>161.34 (n/a)</td><td>161.00 (n/a)</td><td>127.90 (n/a)</td><td>23.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (-6.86%)</td><td>0.22 (-7.70%)</td><td>0.20 <b>(-23.87%)</b></td><td>0.19 (+13.23%)</td><td>0.04 <b>(-28.60%)</b></td><td>198.70 (-11.65%)</td><td>168.40 (+5.43%)</td><td>182.70 <b>(+31.34%)</b></td><td>131.60 (+7.34%)</td><td>29.59 <b>(-32.23%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>224.90 (n/a)</td><td>159.72 (n/a)</td><td>139.10 (n/a)</td><td>122.60 (n/a)</td><td>43.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (-19.95%)</td><td>0.21 (+3.72%)</td><td>0.21 (+6.66%)</td><td>0.19 <b>(+29.21%)</b></td><td>0.02 <b>(-68.68%)</b></td><td>193.20 <b>(-22.63%)</b></td><td>174.64 (-8.29%)</td><td>174.10 (-6.25%)</td><td>158.70 <b>(+24.96%)</b></td><td>14.48 <b>(-69.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>249.70 (n/a)</td><td>190.42 (n/a)</td><td>185.70 (n/a)</td><td>127.00 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (-9.16%)</td><td>0.22 (-8.27%)</td><td>0.21 (-15.73%)</td><td>0.18 (+19.93%)</td><td>0.04 <b>(-27.76%)</b></td><td>199.40 (-16.60%)</td><td>172.02 (+6.13%)</td><td>178.60 (+18.67%)</td><td>132.50 (+10.05%)</td><td>28.48 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>239.10 (n/a)</td><td>162.08 (n/a)</td><td>150.50 (n/a)</td><td>120.40 (n/a)</td><td>44.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 <b>(-40.24%)</b></td><td>0.21 (-19.77%)</td><td>0.22 (-1.21%)</td><td>0.16 <b>(-22.98%)</b></td><td>0.03 <b>(-59.83%)</b></td><td>236.30 <b>(+29.84%)</b></td><td>182.04 <b>(+20.25%)</b></td><td>166.60 (+1.22%)</td><td>161.30 <b>(+67.32%)</b></td><td>31.50 (-12.31%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>182.00 (n/a)</td><td>151.38 (n/a)</td><td>164.60 (n/a)</td><td>96.40 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (-4.20%)</td><td>0.22 (+0.16%)</td><td>0.21 (-7.43%)</td><td>0.20 <b>(+32.06%)</b></td><td>0.02 <b>(-57.65%)</b></td><td>186.50 <b>(-24.31%)</b></td><td>171.70 (-3.20%)</td><td>172.80 (+8.07%)</td><td>154.20 (+4.40%)</td><td>13.83 <b>(-66.43%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>246.40 (n/a)</td><td>177.38 (n/a)</td><td>159.90 (n/a)</td><td>147.70 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 <b>(+42.69%)</b></td><td>0.21 (+16.97%)</td><td>0.22 (+18.98%)</td><td>0.11 <b>(-30.93%)</b></td><td>0.07 <b>(+337.06%)</b></td><td>325.80 <b>(+44.74%)</b></td><td>193.50 (-4.62%)</td><td>170.70 (-15.95%)</td><td>123.20 <b>(-29.96%)</b></td><td>80.82 <b>(+356.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>225.10 (n/a)</td><td>202.88 (n/a)</td><td>203.10 (n/a)</td><td>175.90 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 <b>(+44.31%)</b></td><td>0.21 (+19.71%)</td><td>0.21 <b>(+22.18%)</b></td><td>0.15 (-10.01%)</td><td>0.05 <b>(+358.65%)</b></td><td>247.80 (+11.12%)</td><td>183.06 (-13.26%)</td><td>171.70 (-18.16%)</td><td>134.70 <b>(-30.71%)</b></td><td>42.17 <b>(+255.18%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>211.04 (n/a)</td><td>209.80 (n/a)</td><td>194.40 (n/a)</td><td>11.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (+6.16%)</td><td>0.25 (-6.05%)</td><td>0.24 (-9.65%)</td><td>0.21 (-9.05%)</td><td>0.04 <b>(+78.52%)</b></td><td>192.90 (+9.98%)</td><td>167.08 (+8.09%)</td><td>173.60 (+10.64%)</td><td>130.70 (-5.84%)</td><td>26.84 <b>(+87.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>175.40 (n/a)</td><td>154.58 (n/a)</td><td>156.90 (n/a)</td><td>138.80 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (-7.01%)</td><td>0.23 (-12.36%)</td><td>0.24 (-4.18%)</td><td>0.17 <b>(-28.08%)</b></td><td>0.05 <b>(+35.84%)</b></td><td>246.30 <b>(+39.00%)</b></td><td>183.36 (+17.33%)</td><td>167.60 (+4.36%)</td><td>134.10 (+7.54%)</td><td>43.81 <b>(+106.01%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>177.20 (n/a)</td><td>156.28 (n/a)</td><td>160.60 (n/a)</td><td>124.70 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (-3.05%)</td><td>0.23 (+0.41%)</td><td>0.23 (+3.57%)</td><td>0.21 (+1.02%)</td><td>0.02 (-17.90%)</td><td>192.70 (-1.03%)</td><td>176.90 (-0.67%)</td><td>176.60 (-3.44%)</td><td>153.40 (+3.16%)</td><td>14.94 (-15.55%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>194.70 (n/a)</td><td>178.10 (n/a)</td><td>182.90 (n/a)</td><td>148.70 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.36 <b>(+23.86%)</b></td><td>0.28 (+10.05%)</td><td>0.27 (+6.82%)</td><td>0.22 (+3.62%)</td><td>0.05 <b>(+73.11%)</b></td><td>188.80 (-3.53%)</td><td>150.68 (-7.82%)</td><td>149.10 (-6.40%)</td><td>113.40 (-19.29%)</td><td>26.73 <b>(+30.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>195.70 (n/a)</td><td>163.46 (n/a)</td><td>159.30 (n/a)</td><td>140.50 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (-4.10%)</td><td>0.24 (-5.76%)</td><td>0.23 (-4.44%)</td><td>0.21 (-8.27%)</td><td>0.03 (-2.66%)</td><td>198.90 (+8.99%)</td><td>174.00 (+6.16%)</td><td>177.70 (+4.65%)</td><td>147.20 (+4.25%)</td><td>19.37 (+10.23%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>182.50 (n/a)</td><td>163.90 (n/a)</td><td>169.80 (n/a)</td><td>141.20 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (-6.98%)</td><td>0.25 (+9.30%)</td><td>0.25 (+2.81%)</td><td>0.20 <b>(+28.23%)</b></td><td>0.03 <b>(-47.03%)</b></td><td>203.80 <b>(-22.01%)</b></td><td>167.76 (-11.78%)</td><td>164.60 (-2.78%)</td><td>151.40 (+7.53%)</td><td>21.28 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>261.30 (n/a)</td><td>190.16 (n/a)</td><td>169.30 (n/a)</td><td>140.80 (n/a)</td><td>48.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (+15.84%)</td><td>0.22 (+8.49%)</td><td>0.22 (+8.02%)</td><td>0.19 (-0.46%)</td><td>0.02 <b>(+173.44%)</b></td><td>218.20 (+0.46%)</td><td>190.92 (-7.26%)</td><td>188.20 (-7.43%)</td><td>171.10 (-13.67%)</td><td>18.59 <b>(+136.84%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>205.86 (n/a)</td><td>203.30 (n/a)</td><td>198.20 (n/a)</td><td>7.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (+3.26%)</td><td>0.19 (-12.69%)</td><td>0.17 (-14.64%)</td><td>0.16 (-9.93%)</td><td>0.04 <b>(+22.86%)</b></td><td>249.00 (+11.01%)</td><td>222.06 (+15.99%)</td><td>240.30 (+17.16%)</td><td>152.30 (-3.18%)</td><td>39.84 <b>(+31.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>224.30 (n/a)</td><td>191.44 (n/a)</td><td>205.10 (n/a)</td><td>157.30 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (-9.23%)</td><td>0.20 (+0.19%)</td><td>0.18 (-4.57%)</td><td>0.16 (+7.22%)</td><td>0.04 (-15.00%)</td><td>211.10 (-6.72%)</td><td>177.28 (-1.05%)</td><td>191.50 (+4.76%)</td><td>131.70 (+10.12%)</td><td>35.36 (-7.56%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>226.30 (n/a)</td><td>179.16 (n/a)</td><td>182.80 (n/a)</td><td>119.60 (n/a)</td><td>38.25 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (-7.48%)</td><td>0.19 (-16.07%)</td><td>0.18 <b>(-21.55%)</b></td><td>0.15 (-5.27%)</td><td>0.04 (-15.15%)</td><td>224.90 (+5.54%)</td><td>187.46 (+18.18%)</td><td>193.40 <b>(+27.49%)</b></td><td>133.10 (+8.12%)</td><td>33.39 (-7.53%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>213.10 (n/a)</td><td>158.62 (n/a)</td><td>151.70 (n/a)</td><td>123.10 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (-4.63%)</td><td>0.21 (-2.75%)</td><td>0.21 (+6.86%)</td><td>0.15 (-14.55%)</td><td>0.04 (+0.48%)</td><td>226.80 (+17.03%)</td><td>172.84 (+3.50%)</td><td>165.20 (-6.46%)</td><td>127.80 (+4.84%)</td><td>36.91 <b>(+23.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>193.80 (n/a)</td><td>167.00 (n/a)</td><td>176.60 (n/a)</td><td>121.90 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 <b>(-29.74%)</b></td><td>0.18 (-19.40%)</td><td>0.20 (-16.12%)</td><td>0.13 <b>(-20.50%)</b></td><td>0.03 <b>(-42.33%)</b></td><td>261.40 <b>(+25.79%)</b></td><td>200.34 <b>(+21.71%)</b></td><td>177.40 (+19.22%)</td><td>174.90 <b>(+42.31%)</b></td><td>37.76 (-3.21%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>207.80 (n/a)</td><td>164.60 (n/a)</td><td>148.80 (n/a)</td><td>122.90 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (+16.91%)</td><td>0.21 (+14.58%)</td><td>0.20 (+5.90%)</td><td>0.16 (+8.09%)</td><td>0.04 (+18.40%)</td><td>220.50 (-7.47%)</td><td>172.28 (-12.57%)</td><td>171.30 (-5.57%)</td><td>135.50 (-14.51%)</td><td>32.04 (-8.31%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>238.30 (n/a)</td><td>197.06 (n/a)</td><td>181.40 (n/a)</td><td>158.50 (n/a)</td><td>34.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (-11.33%)</td><td>0.19 (-18.40%)</td><td>0.17 <b>(-20.19%)</b></td><td>0.15 <b>(-21.66%)</b></td><td>0.04 <b>(+21.53%)</b></td><td>232.20 <b>(+27.65%)</b></td><td>193.08 <b>(+24.60%)</b></td><td>203.10 <b>(+25.29%)</b></td><td>146.00 (+12.83%)</td><td>36.67 <b>(+76.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>181.90 (n/a)</td><td>154.96 (n/a)</td><td>162.10 (n/a)</td><td>129.40 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 <b>(+31.77%)</b></td><td>0.20 (+19.82%)</td><td>0.19 (+14.85%)</td><td>0.14 (+11.97%)</td><td>0.05 <b>(+56.29%)</b></td><td>246.90 (-10.71%)</td><td>187.14 (-15.09%)</td><td>182.00 (-12.96%)</td><td>125.70 <b>(-24.09%)</b></td><td>43.52 (+2.62%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>276.50 (n/a)</td><td>220.40 (n/a)</td><td>209.10 (n/a)</td><td>165.60 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (-3.63%)</td><td>0.18 (+1.88%)</td><td>0.18 (-7.05%)</td><td>0.17 (+14.52%)</td><td>0.01 <b>(-55.02%)</b></td><td>209.80 (-12.66%)</td><td>189.98 (-4.07%)</td><td>190.90 (+7.61%)</td><td>168.50 (+3.76%)</td><td>14.84 <b>(-60.69%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>240.20 (n/a)</td><td>198.04 (n/a)</td><td>177.40 (n/a)</td><td>162.40 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.93 (-5.98%)</td><td>0.77 (+2.68%)</td><td>0.72 (+8.80%)</td><td>0.64 (+7.63%)</td><td>0.11 <b>(-32.78%)</b></td><td>204.00 (-7.10%)</td><td>173.74 (-4.61%)</td><td>181.70 (-8.09%)</td><td>140.20 (+6.37%)</td><td>24.49 <b>(-34.30%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.99 (n/a)</td><td>0.75 (n/a)</td><td>0.66 (n/a)</td><td>0.60 (n/a)</td><td>0.17 (n/a)</td><td>219.60 (n/a)</td><td>182.14 (n/a)</td><td>197.70 (n/a)</td><td>131.80 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.02 <b>(+23.61%)</b></td><td>0.92 (+18.48%)</td><td>0.99 <b>(+25.07%)</b></td><td>0.74 (+6.15%)</td><td>0.12 <b>(+149.85%)</b></td><td>177.00 (-5.80%)</td><td>144.16 (-14.56%)</td><td>132.50 <b>(-20.04%)</b></td><td>128.50 (-19.08%)</td><td>20.99 <b>(+85.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.05 (n/a)</td><td>187.90 (n/a)</td><td>168.72 (n/a)</td><td>165.70 (n/a)</td><td>158.80 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.12 <b>(+37.89%)</b></td><td>0.97 <b>(+44.54%)</b></td><td>0.89 <b>(+24.91%)</b></td><td>0.88 <b>(+130.68%)</b></td><td>0.11 <b>(-36.27%)</b></td><td>148.60 <b>(-56.65%)</b></td><td>136.92 <b>(-35.20%)</b></td><td>146.70 (-19.97%)</td><td>117.40 <b>(-27.49%)</b></td><td>14.77 <b>(-80.36%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.81 (n/a)</td><td>0.67 (n/a)</td><td>0.72 (n/a)</td><td>0.38 (n/a)</td><td>0.17 (n/a)</td><td>342.80 (n/a)</td><td>211.28 (n/a)</td><td>183.30 (n/a)</td><td>161.90 (n/a)</td><td>75.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.00 (+6.98%)</td><td>0.00 (+1.91%)</td><td>0.00 (+0.00%)</td><td>0.00 (-4.88%)</td><td>0.00 <b>(+244.34%)</b></td><td>1040.26 (+3.00%)</td><td>963.64 (-1.71%)</td><td>972.55 (-0.39%)</td><td>899.95 (-5.07%)</td><td>59.19 <b>(+157.52%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1009.93 (n/a)</td><td>980.41 (n/a)</td><td>976.38 (n/a)</td><td>948.01 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.01 (+3.66%)</td><td>0.01 (+0.00%)</td><td>0.01 (-2.47%)</td><td>0.01 (-3.95%)</td><td>0.00 <b>(+101.61%)</b></td><td>1128.58 (+5.07%)</td><td>1023.97 (+0.19%)</td><td>1035.75 (+2.99%)</td><td>959.74 (-3.78%)</td><td>69.76 <b>(+122.11%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1074.13 (n/a)</td><td>1021.98 (n/a)</td><td>1005.66 (n/a)</td><td>997.49 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.99 (+0.92%)</td><td>0.96 (+0.52%)</td><td>0.95 (-0.37%)</td><td>0.94 (+0.06%)</td><td>0.02 <b>(+58.36%)</b></td><td>2225.80 (-0.06%)</td><td>2181.24 (-0.49%)</td><td>2204.07 (+0.36%)</td><td>2123.04 (-0.91%)</td><td>49.03 <b>(+57.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2227.21 (n/a)</td><td>2192.00 (n/a)</td><td>2196.06 (n/a)</td><td>2142.61 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.40 (-2.49%)</td><td>0.39 (-1.85%)</td><td>0.39 (-0.60%)</td><td>0.38 (-0.97%)</td><td>0.01 <b>(-22.36%)</b></td><td>1385.74 (+0.96%)</td><td>1339.48 (+1.86%)</td><td>1328.43 (+0.61%)</td><td>1311.40 (+2.56%)</td><td>30.55 (-19.88%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1372.59 (n/a)</td><td>1315.00 (n/a)</td><td>1320.41 (n/a)</td><td>1278.61 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (+1.21%)</td><td>0.27 (+4.85%)</td><td>0.27 (+1.52%)</td><td>0.26 (+16.41%)</td><td>0.00 <b>(-89.37%)</b></td><td>1992.18 (-14.10%)</td><td>1971.62 (-4.97%)</td><td>1964.90 (-1.50%)</td><td>1961.11 (-1.22%)</td><td>12.99 <b>(-90.92%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>2319.28 (n/a)</td><td>2074.64 (n/a)</td><td>1994.88 (n/a)</td><td>1985.37 (n/a)</td><td>143.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.38 (-1.02%)</td><td>0.37 (-0.09%)</td><td>0.37 (-1.18%)</td><td>0.36 (+0.11%)</td><td>0.01 (-14.13%)</td><td>1449.94 (-0.10%)</td><td>1418.27 (+0.08%)</td><td>1426.91 (+1.20%)</td><td>1382.36 (+1.03%)</td><td>29.85 (-13.70%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1451.41 (n/a)</td><td>1417.08 (n/a)</td><td>1410.04 (n/a)</td><td>1368.21 (n/a)</td><td>34.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.05 <b>(+21.77%)</b></td><td>5.03 (+4.72%)</td><td>4.82 (+4.73%)</td><td>3.55 (-18.87%)</td><td>1.27 <b>(+124.12%)</b></td><td>295.20 <b>(+23.26%)</b></td><td>218.54 (-0.83%)</td><td>217.40 (-4.52%)</td><td>148.70 (-17.85%)</td><td>52.03 <b>(+127.98%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.79 (n/a)</td><td>4.80 (n/a)</td><td>4.60 (n/a)</td><td>4.38 (n/a)</td><td>0.56 (n/a)</td><td>239.50 (n/a)</td><td>220.38 (n/a)</td><td>227.70 (n/a)</td><td>181.00 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.01 (+3.90%)</td><td>5.08 (+3.38%)</td><td>5.14 (+7.90%)</td><td>3.99 (-10.41%)</td><td>0.77 <b>(+42.48%)</b></td><td>262.70 (+11.60%)</td><td>210.58 (-2.24%)</td><td>203.80 (-7.32%)</td><td>174.50 (-3.75%)</td><td>33.95 <b>(+54.67%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.78 (n/a)</td><td>4.91 (n/a)</td><td>4.77 (n/a)</td><td>4.46 (n/a)</td><td>0.54 (n/a)</td><td>235.40 (n/a)</td><td>215.40 (n/a)</td><td>219.90 (n/a)</td><td>181.30 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>5.63 (+4.44%)</td><td>5.11 (+3.40%)</td><td>5.21 (-0.99%)</td><td>4.41 (+0.64%)</td><td>0.54 (+5.69%)</td><td>238.00 (-0.63%)</td><td>206.90 (-3.25%)</td><td>201.30 (+1.00%)</td><td>186.10 (-4.27%)</td><td>22.45 (-1.21%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.39 (n/a)</td><td>4.95 (n/a)</td><td>5.26 (n/a)</td><td>4.38 (n/a)</td><td>0.51 (n/a)</td><td>239.50 (n/a)</td><td>213.84 (n/a)</td><td>199.30 (n/a)</td><td>194.40 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.09 (-0.56%)</td><td>5.22 (-1.41%)</td><td>5.35 (-2.12%)</td><td>4.14 (-3.25%)</td><td>0.70 (-0.79%)</td><td>253.60 (+3.38%)</td><td>204.14 (+1.50%)</td><td>196.00 (+2.19%)</td><td>172.30 (+0.58%)</td><td>29.99 (+4.68%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>6.12 (n/a)</td><td>5.29 (n/a)</td><td>5.47 (n/a)</td><td>4.27 (n/a)</td><td>0.71 (n/a)</td><td>245.30 (n/a)</td><td>201.12 (n/a)</td><td>191.80 (n/a)</td><td>171.30 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.06 <b>(+21.41%)</b></td><td>7.78 (+9.13%)</td><td>7.71 (+6.08%)</td><td>6.40 (+0.03%)</td><td>1.06 <b>(+142.90%)</b></td><td>327.70 (-0.03%)</td><td>273.56 (-7.24%)</td><td>272.20 (-5.72%)</td><td>231.60 (-17.61%)</td><td>38.22 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.46 (n/a)</td><td>7.13 (n/a)</td><td>7.26 (n/a)</td><td>6.40 (n/a)</td><td>0.44 (n/a)</td><td>327.80 (n/a)</td><td>294.92 (n/a)</td><td>288.70 (n/a)</td><td>281.10 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.22 (+6.55%)</td><td>8.17 (+2.37%)</td><td>7.90 (-5.62%)</td><td>7.31 (+9.71%)</td><td>0.79 (-5.66%)</td><td>287.00 (-8.86%)</td><td>258.68 (-2.55%)</td><td>265.50 (+5.95%)</td><td>227.40 (-6.15%)</td><td>24.30 (-19.80%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>8.66 (n/a)</td><td>7.98 (n/a)</td><td>8.37 (n/a)</td><td>6.66 (n/a)</td><td>0.83 (n/a)</td><td>314.90 (n/a)</td><td>265.46 (n/a)</td><td>250.60 (n/a)</td><td>242.30 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.17 (-2.82%)</td><td>8.23 (+2.78%)</td><td>7.97 (+2.84%)</td><td>7.58 (+9.74%)</td><td>0.65 <b>(-33.29%)</b></td><td>276.80 (-8.86%)</td><td>255.92 (-3.35%)</td><td>263.20 (-2.73%)</td><td>228.70 (+2.88%)</td><td>19.66 <b>(-37.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.43 (n/a)</td><td>8.01 (n/a)</td><td>7.75 (n/a)</td><td>6.90 (n/a)</td><td>0.98 (n/a)</td><td>303.70 (n/a)</td><td>264.78 (n/a)</td><td>270.60 (n/a)</td><td>222.30 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.91 (-4.73%)</td><td>8.22 (-3.63%)</td><td>8.25 (-5.59%)</td><td>7.49 (+2.76%)</td><td>0.56 <b>(-26.61%)</b></td><td>280.10 (-2.71%)</td><td>256.20 (+3.43%)</td><td>254.20 (+5.92%)</td><td>235.30 (+4.95%)</td><td>17.71 <b>(-26.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>9.35 (n/a)</td><td>8.53 (n/a)</td><td>8.74 (n/a)</td><td>7.28 (n/a)</td><td>0.77 (n/a)</td><td>287.90 (n/a)</td><td>247.70 (n/a)</td><td>240.00 (n/a)</td><td>224.20 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.77 (-14.62%)</td><td>7.99 (-14.56%)</td><td>7.91 (-14.99%)</td><td>7.05 (+4.57%)</td><td>1.07 <b>(-43.21%)</b></td><td>297.40 (-4.34%)</td><td>265.78 (+14.43%)</td><td>265.20 (+17.61%)</td><td>214.70 (+17.13%)</td><td>32.22 <b>(-36.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>11.44 (n/a)</td><td>9.36 (n/a)</td><td>9.30 (n/a)</td><td>6.74 (n/a)</td><td>1.88 (n/a)</td><td>310.90 (n/a)</td><td>232.26 (n/a)</td><td>225.50 (n/a)</td><td>183.30 (n/a)</td><td>50.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>10.66 (+0.29%)</td><td>9.18 (-0.63%)</td><td>8.59 (-10.26%)</td><td>7.91 (+7.37%)</td><td>1.30 (+7.94%)</td><td>265.20 (-6.85%)</td><td>232.06 (+0.70%)</td><td>244.20 (+11.46%)</td><td>196.70 (-0.30%)</td><td>31.81 (-3.75%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>10.63 (n/a)</td><td>9.24 (n/a)</td><td>9.57 (n/a)</td><td>7.37 (n/a)</td><td>1.21 (n/a)</td><td>284.70 (n/a)</td><td>230.44 (n/a)</td><td>219.10 (n/a)</td><td>197.30 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>12.51 (+2.16%)</td><td>11.43 (-4.23%)</td><td>10.98 (-9.24%)</td><td>10.54 (-7.63%)</td><td>0.96 <b>(+176.65%)</b></td><td>398.00 (+8.27%)</td><td>368.94 (+4.92%)</td><td>381.90 (+10.18%)</td><td>335.20 (-2.13%)</td><td>30.13 <b>(+190.95%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>12.25 (n/a)</td><td>11.94 (n/a)</td><td>12.10 (n/a)</td><td>11.41 (n/a)</td><td>0.35 (n/a)</td><td>367.60 (n/a)</td><td>351.64 (n/a)</td><td>346.60 (n/a)</td><td>342.50 (n/a)</td><td>10.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.03 (-3.21%)</td><td>11.83 (-9.55%)</td><td>12.41 (-5.90%)</td><td>9.96 (-19.55%)</td><td>1.33 <b>(+224.51%)</b></td><td>421.00 <b>(+24.30%)</b></td><td>358.30 (+11.68%)</td><td>338.00 (+6.29%)</td><td>321.80 (+3.31%)</td><td>42.85 <b>(+311.12%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.47 (n/a)</td><td>13.08 (n/a)</td><td>13.19 (n/a)</td><td>12.38 (n/a)</td><td>0.41 (n/a)</td><td>338.70 (n/a)</td><td>320.82 (n/a)</td><td>318.00 (n/a)</td><td>311.50 (n/a)</td><td>10.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>12.27 (-9.89%)</td><td>11.28 (-7.12%)</td><td>11.04 (-11.04%)</td><td>10.41 (-0.81%)</td><td>0.77 <b>(-32.46%)</b></td><td>403.10 (+0.83%)</td><td>373.16 (+7.28%)</td><td>379.80 (+12.40%)</td><td>341.80 (+10.97%)</td><td>25.20 <b>(-25.49%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>13.62 (n/a)</td><td>12.15 (n/a)</td><td>12.41 (n/a)</td><td>10.49 (n/a)</td><td>1.14 (n/a)</td><td>399.80 (n/a)</td><td>347.84 (n/a)</td><td>337.90 (n/a)</td><td>308.00 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.99 (-1.03%)</td><td>12.59 (-7.60%)</td><td>12.20 (-13.21%)</td><td>11.60 (-9.33%)</td><td>0.95 <b>(+42.81%)</b></td><td>361.60 (+10.28%)</td><td>334.62 (+8.49%)</td><td>343.80 (+15.21%)</td><td>299.80 (+1.04%)</td><td>24.46 <b>(+58.90%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.14 (n/a)</td><td>13.62 (n/a)</td><td>14.06 (n/a)</td><td>12.79 (n/a)</td><td>0.67 (n/a)</td><td>327.90 (n/a)</td><td>308.44 (n/a)</td><td>298.40 (n/a)</td><td>296.70 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.44 (+2.12%)</td><td>12.62 (-5.71%)</td><td>13.39 (-1.80%)</td><td>10.28 (-15.69%)</td><td>1.72 <b>(+133.35%)</b></td><td>408.10 (+18.60%)</td><td>337.72 (+7.49%)</td><td>313.30 (+1.85%)</td><td>290.50 (-2.06%)</td><td>48.99 <b>(+169.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.14 (n/a)</td><td>13.38 (n/a)</td><td>13.63 (n/a)</td><td>12.19 (n/a)</td><td>0.74 (n/a)</td><td>344.10 (n/a)</td><td>314.18 (n/a)</td><td>307.60 (n/a)</td><td>296.60 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.40 (-6.74%)</td><td>13.48 (-4.55%)</td><td>13.77 (-4.21%)</td><td>12.38 (-1.07%)</td><td>0.79 <b>(-32.80%)</b></td><td>338.80 (+1.07%)</td><td>311.94 (+4.46%)</td><td>304.60 (+4.39%)</td><td>291.20 (+7.22%)</td><td>18.76 <b>(-27.05%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>15.45 (n/a)</td><td>14.13 (n/a)</td><td>14.37 (n/a)</td><td>12.51 (n/a)</td><td>1.18 (n/a)</td><td>335.20 (n/a)</td><td>298.62 (n/a)</td><td>291.80 (n/a)</td><td>271.60 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>16.07 (+8.65%)</td><td>14.27 (+9.13%)</td><td>14.41 (+8.52%)</td><td>12.39 (+14.79%)</td><td>1.67 (+11.83%)</td><td>338.50 (-12.89%)</td><td>297.32 (-8.38%)</td><td>291.10 (-7.85%)</td><td>261.00 (-7.97%)</td><td>35.32 (-11.47%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.79 (n/a)</td><td>13.07 (n/a)</td><td>13.28 (n/a)</td><td>10.79 (n/a)</td><td>1.50 (n/a)</td><td>388.60 (n/a)</td><td>324.50 (n/a)</td><td>315.90 (n/a)</td><td>283.60 (n/a)</td><td>39.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>15.36 (+8.30%)</td><td>13.43 (+3.33%)</td><td>12.91 (-4.49%)</td><td>12.26 (+6.70%)</td><td>1.29 (+6.06%)</td><td>342.20 (-6.27%)</td><td>314.62 (-3.24%)</td><td>325.00 (+4.70%)</td><td>273.10 (-7.67%)</td><td>28.81 (-8.30%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>14.18 (n/a)</td><td>12.99 (n/a)</td><td>13.51 (n/a)</td><td>11.49 (n/a)</td><td>1.22 (n/a)</td><td>365.10 (n/a)</td><td>325.16 (n/a)</td><td>310.40 (n/a)</td><td>295.80 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.35 (-1.65%)</td><td>2.68 (-7.15%)</td><td>2.73 (-5.06%)</td><td>1.51 <b>(-40.31%)</b></td><td>0.73 <b>(+126.76%)</b></td><td>347.90 <b>(+67.58%)</b></td><td>212.06 (+15.80%)</td><td>192.30 (+5.37%)</td><td>156.60 (+1.62%)</td><td>78.26 <b>(+305.65%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.40 (n/a)</td><td>2.89 (n/a)</td><td>2.87 (n/a)</td><td>2.52 (n/a)</td><td>0.32 (n/a)</td><td>207.60 (n/a)</td><td>183.12 (n/a)</td><td>182.50 (n/a)</td><td>154.10 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.25 (+8.92%)</td><td>5.23 (+10.14%)</td><td>5.32 (+18.65%)</td><td>3.52 (-4.28%)</td><td>1.04 <b>(+25.34%)</b></td><td>298.10 (+4.49%)</td><td>208.68 (-7.88%)</td><td>197.30 (-15.72%)</td><td>167.80 (-8.21%)</td><td>51.67 <b>(+27.07%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>5.74 (n/a)</td><td>4.75 (n/a)</td><td>4.48 (n/a)</td><td>3.68 (n/a)</td><td>0.83 (n/a)</td><td>285.30 (n/a)</td><td>226.52 (n/a)</td><td>234.10 (n/a)</td><td>182.80 (n/a)</td><td>40.66 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.32 (+8.55%)</td><td>6.80 (+0.32%)</td><td>6.81 (+3.24%)</td><td>5.17 (-16.56%)</td><td>1.15 <b>(+98.79%)</b></td><td>405.80 (+19.85%)</td><td>316.10 (+1.57%)</td><td>308.10 (-3.14%)</td><td>252.00 (-7.89%)</td><td>57.06 <b>(+124.32%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>7.67 (n/a)</td><td>6.78 (n/a)</td><td>6.59 (n/a)</td><td>6.19 (n/a)</td><td>0.58 (n/a)</td><td>338.60 (n/a)</td><td>311.22 (n/a)</td><td>318.10 (n/a)</td><td>273.60 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.73 (+18.73%)</td><td>3.27 (+14.97%)</td><td>3.34 (+6.42%)</td><td>2.55 <b>(+36.45%)</b></td><td>0.44 <b>(-20.15%)</b></td><td>205.70 <b>(-26.69%)</b></td><td>163.20 (-15.10%)</td><td>157.20 (-6.04%)</td><td>140.60 (-15.76%)</td><td>25.03 <b>(-49.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>3.14 (n/a)</td><td>2.84 (n/a)</td><td>3.13 (n/a)</td><td>1.87 (n/a)</td><td>0.55 (n/a)</td><td>280.60 (n/a)</td><td>192.22 (n/a)</td><td>167.30 (n/a)</td><td>166.90 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (+12.70%)</td><td>0.22 (+18.38%)</td><td>0.22 (+18.25%)</td><td>0.18 (+15.56%)</td><td>0.04 <b>(+28.93%)</b></td><td>184.90 (-13.44%)</td><td>151.84 (-15.03%)</td><td>145.90 (-15.42%)</td><td>124.30 (-11.28%)</td><td>27.76 (-0.86%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.60 (n/a)</td><td>178.70 (n/a)</td><td>172.50 (n/a)</td><td>140.10 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (+6.94%)</td><td>0.17 (+5.70%)</td><td>0.17 (+4.63%)</td><td>0.15 (+7.51%)</td><td>0.02 (+6.14%)</td><td>212.80 (-6.99%)</td><td>190.44 (-5.43%)</td><td>189.80 (-4.43%)</td><td>163.20 (-6.53%)</td><td>18.15 (-8.54%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>228.80 (n/a)</td><td>201.38 (n/a)</td><td>198.60 (n/a)</td><td>174.60 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.44 (-9.37%)</td><td>0.37 (+0.97%)</td><td>0.38 (+4.48%)</td><td>0.29 <b>(+44.67%)</b></td><td>0.06 <b>(-47.74%)</b></td><td>228.20 <b>(-30.87%)</b></td><td>181.20 (-8.99%)</td><td>172.60 (-4.27%)</td><td>148.50 (+10.33%)</td><td>33.04 <b>(-58.97%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>330.10 (n/a)</td><td>199.10 (n/a)</td><td>180.30 (n/a)</td><td>134.60 (n/a)</td><td>80.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.39 (+0.73%)</td><td>0.34 (+4.09%)</td><td>0.37 (+19.88%)</td><td>0.27 (-6.79%)</td><td>0.05 <b>(+33.26%)</b></td><td>242.40 (+7.26%)</td><td>195.42 (-3.01%)</td><td>176.60 (-16.58%)</td><td>167.10 (-0.77%)</td><td>32.45 <b>(+42.87%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>226.00 (n/a)</td><td>201.48 (n/a)</td><td>211.70 (n/a)</td><td>168.40 (n/a)</td><td>22.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.50 (-5.02%)</td><td>0.42 (+3.03%)</td><td>0.42 <b>(+20.01%)</b></td><td>0.37 (+10.41%)</td><td>0.05 <b>(-45.59%)</b></td><td>178.00 (-9.41%)</td><td>155.92 (-5.57%)</td><td>154.90 (-16.63%)</td><td>130.50 (+5.33%)</td><td>17.90 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>196.50 (n/a)</td><td>165.12 (n/a)</td><td>185.80 (n/a)</td><td>123.90 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.04 (-4.31%)</td><td>0.80 (-11.01%)</td><td>0.78 (-17.46%)</td><td>0.69 (-1.15%)</td><td>0.14 (-16.51%)</td><td>191.10 (+1.16%)</td><td>167.40 (+11.42%)</td><td>169.00 <b>(+21.15%)</b></td><td>125.90 (+4.48%)</td><td>25.01 (-14.96%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.09 (n/a)</td><td>0.90 (n/a)</td><td>0.94 (n/a)</td><td>0.69 (n/a)</td><td>0.17 (n/a)</td><td>188.90 (n/a)</td><td>150.24 (n/a)</td><td>139.50 (n/a)</td><td>120.50 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.07 (+18.27%)</td><td>0.90 <b>(+20.48%)</b></td><td>0.87 (+12.90%)</td><td>0.71 <b>(+68.70%)</b></td><td>0.15 <b>(-20.34%)</b></td><td>183.80 <b>(-40.73%)</b></td><td>149.36 <b>(-21.22%)</b></td><td>150.20 (-11.44%)</td><td>122.50 (-15.46%)</td><td>25.51 <b>(-62.65%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.90 (n/a)</td><td>0.75 (n/a)</td><td>0.77 (n/a)</td><td>0.42 (n/a)</td><td>0.19 (n/a)</td><td>310.10 (n/a)</td><td>189.60 (n/a)</td><td>169.60 (n/a)</td><td>144.90 (n/a)</td><td>68.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.89 (-9.34%)</td><td>0.83 (-0.05%)</td><td>0.86 (+5.82%)</td><td>0.75 (+0.50%)</td><td>0.06 <b>(-37.02%)</b></td><td>174.90 (-0.51%)</td><td>158.16 (-0.43%)</td><td>152.70 (-5.45%)</td><td>147.20 (+10.26%)</td><td>11.18 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.98 (n/a)</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.09 (n/a)</td><td>175.80 (n/a)</td><td>158.84 (n/a)</td><td>161.50 (n/a)</td><td>133.50 (n/a)</td><td>15.81 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.95 (-11.95%)</td><td>0.83 (+2.76%)</td><td>0.82 (-2.76%)</td><td>0.77 <b>(+35.75%)</b></td><td>0.07 <b>(-67.99%)</b></td><td>170.90 <b>(-26.34%)</b></td><td>158.26 (-8.07%)</td><td>159.30 (+2.84%)</td><td>138.40 (+13.63%)</td><td>12.59 <b>(-74.10%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>1.08 (n/a)</td><td>0.81 (n/a)</td><td>0.85 (n/a)</td><td>0.57 (n/a)</td><td>0.22 (n/a)</td><td>232.00 (n/a)</td><td>172.16 (n/a)</td><td>154.90 (n/a)</td><td>121.80 (n/a)</td><td>48.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (+5.58%)</td><td>0.09 (-6.04%)</td><td>0.09 (-13.90%)</td><td>0.08 (-3.42%)</td><td>0.01 <b>(+23.70%)</b></td><td>208.30 (+3.53%)</td><td>179.52 (+7.04%)</td><td>182.70 (+16.15%)</td><td>143.00 (-5.30%)</td><td>25.62 <b>(+21.09%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 21:34:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>167.72 (n/a)</td><td>157.30 (n/a)</td><td>151.00 (n/a)</td><td>21.16 (n/a)</td>
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
