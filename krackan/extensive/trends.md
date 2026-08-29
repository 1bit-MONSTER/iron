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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (-5.73%)</td><td>0.04 (-10.32%)</td><td>0.04 (-10.65%)</td><td>0.03 (-14.06%)</td><td>0.01 (+8.74%)</td><td>201.30 (+16.36%)</td><td>162.98 (+12.15%)</td><td>163.30 (+11.93%)</td><td>134.90 (+6.05%)</td><td>25.34 <b>(+36.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>173.00 (n/a)</td><td>145.32 (n/a)</td><td>145.90 (n/a)</td><td>127.20 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+1.24%)</td><td>0.04 (-6.56%)</td><td>0.04 (-5.01%)</td><td>0.03 (-15.69%)</td><td>0.01 <b>(+51.19%)</b></td><td>222.40 (+18.61%)</td><td>164.04 (+11.49%)</td><td>153.00 (+5.23%)</td><td>113.00 (-1.22%)</td><td>46.88 <b>(+78.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>147.14 (n/a)</td><td>145.40 (n/a)</td><td>114.40 (n/a)</td><td>26.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+1.58%)</td><td>0.04 (-7.28%)</td><td>0.04 (-16.99%)</td><td>0.03 (-6.54%)</td><td>0.01 (+1.05%)</td><td>188.20 (+6.99%)</td><td>158.60 (+7.85%)</td><td>161.10 <b>(+20.40%)</b></td><td>118.60 (-1.58%)</td><td>25.80 (+0.23%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>147.06 (n/a)</td><td>133.80 (n/a)</td><td>120.50 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+5.91%)</td><td>0.04 (-3.37%)</td><td>0.04 (-5.76%)</td><td>0.03 (-11.62%)</td><td>0.01 <b>(+67.81%)</b></td><td>186.50 (+13.17%)</td><td>154.36 (+5.18%)</td><td>153.40 (+6.09%)</td><td>123.70 (-5.57%)</td><td>26.64 <b>(+79.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>164.80 (n/a)</td><td>146.76 (n/a)</td><td>144.60 (n/a)</td><td>131.00 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+5.95%)</td><td>0.04 (+1.05%)</td><td>0.05 (+6.22%)</td><td>0.03 (-8.45%)</td><td>0.01 <b>(+69.06%)</b></td><td>211.70 (+9.24%)</td><td>159.18 (+2.86%)</td><td>135.80 (-5.89%)</td><td>120.20 (-5.65%)</td><td>44.48 <b>(+74.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>154.76 (n/a)</td><td>144.30 (n/a)</td><td>127.40 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-13.05%)</td><td>0.03 <b>(-21.74%)</b></td><td>0.03 <b>(-27.21%)</b></td><td>0.02 <b>(-26.66%)</b></td><td>0.01 (-2.96%)</td><td>260.40 <b>(+36.34%)</b></td><td>192.38 <b>(+29.24%)</b></td><td>183.50 <b>(+37.35%)</b></td><td>148.40 (+14.95%)</td><td>41.89 <b>(+57.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>148.86 (n/a)</td><td>133.60 (n/a)</td><td>129.10 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-17.24%)</td><td>0.03 (-12.70%)</td><td>0.03 (-8.30%)</td><td>0.02 (-1.33%)</td><td>0.01 <b>(-30.65%)</b></td><td>250.70 (+1.37%)</td><td>205.10 (+12.62%)</td><td>194.00 (+9.05%)</td><td>158.00 <b>(+20.80%)</b></td><td>36.57 (-14.69%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>182.12 (n/a)</td><td>177.90 (n/a)</td><td>130.80 (n/a)</td><td>42.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-0.67%)</td><td>0.03 (-2.36%)</td><td>0.03 (-7.52%)</td><td>0.03 (-0.98%)</td><td>0.00 (-14.19%)</td><td>203.60 (+0.99%)</td><td>177.88 (+2.19%)</td><td>176.50 (+8.15%)</td><td>158.70 (+0.70%)</td><td>16.67 (-11.91%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.60 (n/a)</td><td>174.06 (n/a)</td><td>163.20 (n/a)</td><td>157.60 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (-4.61%)</td><td>0.08 (-4.66%)</td><td>0.07 (-8.04%)</td><td>0.07 (+4.90%)</td><td>0.01 <b>(-32.70%)</b></td><td>185.40 (-4.68%)</td><td>164.08 (+3.16%)</td><td>173.00 (+8.74%)</td><td>132.50 (+4.83%)</td><td>20.55 <b>(-33.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.50 (n/a)</td><td>159.06 (n/a)</td><td>159.10 (n/a)</td><td>126.40 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (-19.97%)</td><td>0.07 (-3.30%)</td><td>0.07 (+4.37%)</td><td>0.05 <b>(+54.23%)</b></td><td>0.01 <b>(-59.52%)</b></td><td>240.70 <b>(-35.16%)</b></td><td>189.92 (-7.59%)</td><td>178.80 (-4.18%)</td><td>163.50 <b>(+25.00%)</b></td><td>30.76 <b>(-68.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>371.20 (n/a)</td><td>205.52 (n/a)</td><td>186.60 (n/a)</td><td>130.80 (n/a)</td><td>96.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (+11.56%)</td><td>0.08 (+15.64%)</td><td>0.07 (+3.65%)</td><td>0.06 <b>(+25.48%)</b></td><td>0.02 (+8.85%)</td><td>194.60 <b>(-20.31%)</b></td><td>158.68 (-14.01%)</td><td>175.10 (-3.53%)</td><td>113.70 (-10.40%)</td><td>33.33 <b>(-21.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.20 (n/a)</td><td>184.54 (n/a)</td><td>181.50 (n/a)</td><td>126.90 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (-4.63%)</td><td>0.08 (+0.66%)</td><td>0.08 (+7.95%)</td><td>0.05 (-6.12%)</td><td>0.02 (-8.03%)</td><td>227.80 (+6.50%)</td><td>162.08 (-0.75%)</td><td>158.00 (-7.33%)</td><td>131.10 (+4.88%)</td><td>39.39 (+6.48%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.90 (n/a)</td><td>163.30 (n/a)</td><td>170.50 (n/a)</td><td>125.00 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(-26.74%)</b></td><td>0.05 <b>(-30.19%)</b></td><td>0.06 <b>(-21.18%)</b></td><td>0.03 <b>(-50.96%)</b></td><td>0.01 <b>(+50.40%)</b></td><td>366.30 <b>(+103.95%)</b></td><td>246.14 <b>(+51.19%)</b></td><td>217.10 <b>(+26.88%)</b></td><td>183.70 <b>(+36.48%)</b></td><td>75.46 <b>(+321.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.60 (n/a)</td><td>162.80 (n/a)</td><td>171.10 (n/a)</td><td>134.60 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (-1.67%)</td><td>0.08 (+6.51%)</td><td>0.08 (+12.80%)</td><td>0.06 (-6.99%)</td><td>0.01 (-1.30%)</td><td>215.80 (+7.52%)</td><td>160.30 (-5.92%)</td><td>155.20 (-11.36%)</td><td>133.40 (+1.68%)</td><td>32.39 (+10.74%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>170.38 (n/a)</td><td>175.10 (n/a)</td><td>131.20 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (-5.00%)</td><td>0.06 (+1.28%)</td><td>0.06 (-1.82%)</td><td>0.05 (-0.51%)</td><td>0.01 (-12.31%)</td><td>245.70 (+0.53%)</td><td>200.14 (-1.61%)</td><td>200.60 (+1.88%)</td><td>171.20 (+5.22%)</td><td>29.12 (-7.22%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.40 (n/a)</td><td>203.42 (n/a)</td><td>196.90 (n/a)</td><td>162.70 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (-11.80%)</td><td>0.06 (-5.83%)</td><td>0.06 (-15.03%)</td><td>0.05 <b>(+34.63%)</b></td><td>0.01 <b>(-52.30%)</b></td><td>227.70 <b>(-25.71%)</b></td><td>209.86 (+2.08%)</td><td>221.80 (+17.67%)</td><td>183.20 (+13.37%)</td><td>21.92 <b>(-61.90%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>306.50 (n/a)</td><td>205.58 (n/a)</td><td>188.50 (n/a)</td><td>161.60 (n/a)</td><td>57.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (-6.47%)</td><td>0.13 <b>(-20.32%)</b></td><td>0.12 <b>(-23.10%)</b></td><td>0.11 <b>(-28.46%)</b></td><td>0.03 <b>(+74.06%)</b></td><td>230.30 <b>(+39.75%)</b></td><td>192.64 <b>(+28.50%)</b></td><td>198.00 <b>(+30.01%)</b></td><td>137.90 (+6.90%)</td><td>34.99 <b>(+155.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>164.80 (n/a)</td><td>149.92 (n/a)</td><td>152.30 (n/a)</td><td>129.00 (n/a)</td><td>13.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (-5.66%)</td><td>0.13 (-9.25%)</td><td>0.14 (-1.12%)</td><td>0.10 <b>(-27.58%)</b></td><td>0.02 <b>(+255.96%)</b></td><td>237.80 <b>(+38.10%)</b></td><td>187.40 (+12.20%)</td><td>170.40 (+1.19%)</td><td>166.50 (+5.98%)</td><td>30.62 <b>(+422.65%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>167.02 (n/a)</td><td>168.40 (n/a)</td><td>157.10 (n/a)</td><td>5.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (+14.40%)</td><td>0.15 (-9.74%)</td><td>0.14 (-17.05%)</td><td>0.12 (-16.02%)</td><td>0.04 <b>(+69.04%)</b></td><td>207.90 (+19.07%)</td><td>168.04 (+14.52%)</td><td>174.90 <b>(+20.54%)</b></td><td>105.90 (-12.55%)</td><td>37.48 <b>(+64.89%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>174.60 (n/a)</td><td>146.74 (n/a)</td><td>145.10 (n/a)</td><td>121.10 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 <b>(-20.69%)</b></td><td>0.13 (-12.39%)</td><td>0.13 (-10.07%)</td><td>0.12 (-4.22%)</td><td>0.01 <b>(-46.26%)</b></td><td>209.30 (+4.39%)</td><td>187.72 (+12.91%)</td><td>183.30 (+11.23%)</td><td>171.00 <b>(+26.01%)</b></td><td>17.43 <b>(-29.45%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>166.26 (n/a)</td><td>164.80 (n/a)</td><td>135.70 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (-1.91%)</td><td>0.14 (+3.55%)</td><td>0.13 (-1.41%)</td><td>0.13 <b>(+50.55%)</b></td><td>0.03 <b>(-36.33%)</b></td><td>194.90 <b>(-33.57%)</b></td><td>175.64 (-8.51%)</td><td>190.20 (+1.44%)</td><td>131.80 (+1.93%)</td><td>26.41 <b>(-57.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>293.40 (n/a)</td><td>191.98 (n/a)</td><td>187.50 (n/a)</td><td>129.30 (n/a)</td><td>62.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (-7.02%)</td><td>0.13 (-9.71%)</td><td>0.11 (-16.02%)</td><td>0.08 (+18.86%)</td><td>0.04 (-19.82%)</td><td>302.60 (-15.85%)</td><td>210.80 (+4.67%)</td><td>217.80 (+19.08%)</td><td>132.40 (+7.55%)</td><td>63.77 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>359.60 (n/a)</td><td>201.40 (n/a)</td><td>182.90 (n/a)</td><td>123.10 (n/a)</td><td>93.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 <b>(+48.05%)</b></td><td>0.15 (+11.86%)</td><td>0.15 <b>(+21.47%)</b></td><td>0.09 <b>(-21.39%)</b></td><td>0.05 <b>(+167.73%)</b></td><td>277.70 <b>(+27.21%)</b></td><td>181.14 (-3.22%)</td><td>161.20 (-17.67%)</td><td>107.20 <b>(-32.49%)</b></td><td>63.06 <b>(+137.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.30 (n/a)</td><td>187.16 (n/a)</td><td>195.80 (n/a)</td><td>158.80 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 <b>(+44.58%)</b></td><td>0.16 (+17.25%)</td><td>0.15 (+5.71%)</td><td>0.12 (+6.41%)</td><td>0.04 <b>(+119.79%)</b></td><td>201.10 (-6.03%)</td><td>155.68 (-12.31%)</td><td>159.90 (-5.44%)</td><td>106.90 <b>(-30.81%)</b></td><td>33.89 <b>(+38.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.00 (n/a)</td><td>177.54 (n/a)</td><td>169.10 (n/a)</td><td>154.50 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.35 (-7.46%)</td><td>0.31 (+10.06%)</td><td>0.32 (+18.91%)</td><td>0.28 <b>(+35.77%)</b></td><td>0.03 <b>(-53.86%)</b></td><td>174.10 <b>(-26.32%)</b></td><td>159.10 (-11.94%)</td><td>155.30 (-15.92%)</td><td>139.60 (+8.05%)</td><td>14.66 <b>(-62.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>236.30 (n/a)</td><td>180.68 (n/a)</td><td>184.70 (n/a)</td><td>129.20 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.36 (-1.68%)</td><td>0.29 (-4.46%)</td><td>0.27 (-7.93%)</td><td>0.23 (-7.33%)</td><td>0.05 (-0.95%)</td><td>215.60 (+7.91%)</td><td>176.32 (+4.79%)</td><td>184.10 (+8.61%)</td><td>137.40 (+1.70%)</td><td>29.64 (+7.31%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>199.80 (n/a)</td><td>168.26 (n/a)</td><td>169.50 (n/a)</td><td>135.10 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.34 (-9.88%)</td><td>0.30 (+2.28%)</td><td>0.29 (+7.79%)</td><td>0.26 (+16.52%)</td><td>0.03 <b>(-45.71%)</b></td><td>191.40 (-14.17%)</td><td>166.62 (-4.55%)</td><td>168.10 (-7.23%)</td><td>142.70 (+10.96%)</td><td>18.33 <b>(-47.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>223.00 (n/a)</td><td>174.56 (n/a)</td><td>181.20 (n/a)</td><td>128.60 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (-18.88%)</td><td>0.27 (-8.74%)</td><td>0.27 (+1.41%)</td><td>0.23 (-1.76%)</td><td>0.03 <b>(-56.63%)</b></td><td>216.90 (+1.78%)</td><td>183.16 (+5.52%)</td><td>182.30 (-1.41%)</td><td>154.00 <b>(+23.30%)</b></td><td>22.42 <b>(-45.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>213.10 (n/a)</td><td>173.58 (n/a)</td><td>184.90 (n/a)</td><td>124.90 (n/a)</td><td>41.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.42 <b>(+35.69%)</b></td><td>0.31 (+11.57%)</td><td>0.28 (-1.90%)</td><td>0.27 (+15.08%)</td><td>0.06 <b>(+111.59%)</b></td><td>184.20 (-13.07%)</td><td>161.68 (-8.76%)</td><td>173.90 (+1.99%)</td><td>115.70 <b>(-26.26%)</b></td><td>27.09 <b>(+28.98%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>211.90 (n/a)</td><td>177.20 (n/a)</td><td>170.50 (n/a)</td><td>156.90 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (+1.54%)</td><td>0.27 (-8.56%)</td><td>0.28 (-11.31%)</td><td>0.17 <b>(-22.43%)</b></td><td>0.09 <b>(+23.91%)</b></td><td>283.00 <b>(+28.93%)</b></td><td>195.50 (+13.80%)</td><td>174.70 (+12.78%)</td><td>125.60 (-1.49%)</td><td>64.87 <b>(+53.83%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>219.50 (n/a)</td><td>171.80 (n/a)</td><td>154.90 (n/a)</td><td>127.50 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (-2.29%)</td><td>0.30 (+0.55%)</td><td>0.28 <b>(-23.76%)</b></td><td>0.22 <b>(+37.52%)</b></td><td>0.07 <b>(-34.92%)</b></td><td>225.00 <b>(-27.28%)</b></td><td>168.52 (-8.64%)</td><td>176.00 <b>(+31.15%)</b></td><td>127.60 (+2.33%)</td><td>39.11 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>309.40 (n/a)</td><td>184.46 (n/a)</td><td>134.20 (n/a)</td><td>124.70 (n/a)</td><td>80.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (-1.20%)</td><td>0.25 (-13.99%)</td><td>0.26 (-11.09%)</td><td>0.15 <b>(-37.18%)</b></td><td>0.09 <b>(+81.70%)</b></td><td>319.30 <b>(+59.17%)</b></td><td>214.74 <b>(+26.17%)</b></td><td>191.10 (+12.48%)</td><td>134.20 (+1.21%)</td><td>77.14 <b>(+201.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>200.60 (n/a)</td><td>170.20 (n/a)</td><td>169.90 (n/a)</td><td>132.60 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-9.59%)</td><td>0.02 (-7.50%)</td><td>0.02 (+3.23%)</td><td>0.01 (-18.88%)</td><td>0.00 (+4.28%)</td><td>229.40 <b>(+23.27%)</b></td><td>168.06 (+9.97%)</td><td>148.20 (-3.14%)</td><td>121.00 (+10.60%)</td><td>43.16 <b>(+46.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>152.82 (n/a)</td><td>153.00 (n/a)</td><td>109.40 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+11.44%)</td><td>0.02 (-6.62%)</td><td>0.02 (-16.09%)</td><td>0.01 (-7.80%)</td><td>0.01 <b>(+21.03%)</b></td><td>229.90 (+8.44%)</td><td>176.12 (+8.93%)</td><td>168.20 (+19.21%)</td><td>103.30 (-10.25%)</td><td>49.08 (+9.30%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.00 (n/a)</td><td>161.68 (n/a)</td><td>141.10 (n/a)</td><td>115.10 (n/a)</td><td>44.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(+42.25%)</b></td><td>0.02 <b>(+27.09%)</b></td><td>0.02 (+5.82%)</td><td>0.01 <b>(+29.90%)</b></td><td>0.01 <b>(+93.19%)</b></td><td>188.30 <b>(-23.02%)</b></td><td>148.92 (-19.24%)</td><td>162.90 (-5.51%)</td><td>103.90 <b>(-29.70%)</b></td><td>36.87 (+0.47%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>244.60 (n/a)</td><td>184.40 (n/a)</td><td>172.40 (n/a)</td><td>147.80 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (+4.95%)</td><td>0.02 (+10.93%)</td><td>0.02 (+16.35%)</td><td>0.01 (+5.29%)</td><td>0.00 (+18.68%)</td><td>214.10 (-5.01%)</td><td>158.82 (-8.55%)</td><td>151.50 (-14.07%)</td><td>112.60 (-4.66%)</td><td>42.50 (+11.76%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.40 (n/a)</td><td>173.66 (n/a)</td><td>176.30 (n/a)</td><td>118.10 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (+16.94%)</td><td>0.02 (+11.34%)</td><td>0.02 <b>(+40.00%)</b></td><td>0.01 <b>(-41.67%)</b></td><td>0.01 <b>(+165.81%)</b></td><td>370.60 <b>(+71.42%)</b></td><td>192.38 (+4.46%)</td><td>133.70 <b>(-28.58%)</b></td><td>125.90 (-14.47%)</td><td>104.53 <b>(+283.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.20 (n/a)</td><td>184.16 (n/a)</td><td>187.20 (n/a)</td><td>147.20 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-13.62%)</td><td>0.02 (+11.16%)</td><td>0.02 (+17.63%)</td><td>0.02 <b>(+68.00%)</b></td><td>0.00 <b>(-64.93%)</b></td><td>172.70 <b>(-40.49%)</b></td><td>161.70 (-17.43%)</td><td>171.00 (-15.01%)</td><td>134.80 (+15.81%)</td><td>16.08 <b>(-75.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>290.20 (n/a)</td><td>195.84 (n/a)</td><td>201.20 (n/a)</td><td>116.40 (n/a)</td><td>65.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 <b>(+23.31%)</b></td><td>0.02 (+0.72%)</td><td>0.01 (-13.01%)</td><td>0.01 (+4.36%)</td><td>0.00 <b>(+50.44%)</b></td><td>207.50 (-4.16%)</td><td>179.14 (+0.95%)</td><td>191.10 (+14.98%)</td><td>118.70 (-18.92%)</td><td>35.53 (+12.44%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.50 (n/a)</td><td>177.46 (n/a)</td><td>166.20 (n/a)</td><td>146.40 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (+7.67%)</td><td>0.01 (+5.71%)</td><td>0.01 (+6.81%)</td><td>0.01 (+11.93%)</td><td>0.00 (-11.16%)</td><td>233.70 (-10.67%)</td><td>202.88 (-6.56%)</td><td>204.10 (-6.38%)</td><td>154.20 (-7.16%)</td><td>31.61 <b>(-28.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>261.60 (n/a)</td><td>217.12 (n/a)</td><td>218.00 (n/a)</td><td>166.10 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-15.06%)</td><td>0.03 (-12.10%)</td><td>0.03 (-9.10%)</td><td>0.02 (-11.25%)</td><td>0.00 <b>(-27.27%)</b></td><td>218.50 (+12.69%)</td><td>174.42 (+12.86%)</td><td>174.90 (+10.00%)</td><td>142.60 (+17.75%)</td><td>28.72 (-1.50%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>154.54 (n/a)</td><td>159.00 (n/a)</td><td>121.10 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-34.54%)</b></td><td>0.03 (-19.17%)</td><td>0.03 (-10.64%)</td><td>0.03 (-11.60%)</td><td>0.00 <b>(-61.16%)</b></td><td>209.30 (+13.14%)</td><td>185.16 (+19.98%)</td><td>188.00 (+11.90%)</td><td>157.40 <b>(+52.82%)</b></td><td>22.08 <b>(-30.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>154.32 (n/a)</td><td>168.00 (n/a)</td><td>103.00 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-41.11%)</b></td><td>0.03 <b>(-33.92%)</b></td><td>0.03 <b>(-24.80%)</b></td><td>0.02 <b>(-47.62%)</b></td><td>0.01 <b>(-23.69%)</b></td><td>312.10 <b>(+90.89%)</b></td><td>207.94 <b>(+54.90%)</b></td><td>185.20 <b>(+32.95%)</b></td><td>174.80 <b>(+69.87%)</b></td><td>58.39 <b>(+159.26%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>163.50 (n/a)</td><td>134.24 (n/a)</td><td>139.30 (n/a)</td><td>102.90 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-27.07%)</b></td><td>0.03 (-17.64%)</td><td>0.03 (-18.26%)</td><td>0.02 (+2.17%)</td><td>0.00 <b>(-62.11%)</b></td><td>225.40 (-2.13%)</td><td>186.88 (+15.61%)</td><td>186.90 <b>(+22.32%)</b></td><td>162.80 <b>(+37.15%)</b></td><td>24.32 <b>(-47.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>161.64 (n/a)</td><td>152.80 (n/a)</td><td>118.70 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-28.55%)</b></td><td>0.03 (-13.37%)</td><td>0.03 (-6.48%)</td><td>0.01 (+3.50%)</td><td>0.01 <b>(-40.80%)</b></td><td>356.80 (-3.38%)</td><td>223.64 (+7.55%)</td><td>203.90 (+6.98%)</td><td>152.10 <b>(+39.93%)</b></td><td>78.78 (-18.59%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>369.30 (n/a)</td><td>207.94 (n/a)</td><td>190.60 (n/a)</td><td>108.70 (n/a)</td><td>96.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-2.41%)</td><td>0.03 (-14.51%)</td><td>0.03 <b>(-22.90%)</b></td><td>0.02 (-19.83%)</td><td>0.01 <b>(+23.31%)</b></td><td>253.10 <b>(+24.74%)</b></td><td>200.88 (+18.82%)</td><td>202.10 <b>(+29.72%)</b></td><td>148.30 (+2.49%)</td><td>39.99 <b>(+55.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>169.06 (n/a)</td><td>155.80 (n/a)</td><td>144.70 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (+5.87%)</td><td>0.03 (-0.91%)</td><td>0.03 (-0.49%)</td><td>0.02 (-14.15%)</td><td>0.01 <b>(+46.16%)</b></td><td>220.80 (+16.46%)</td><td>172.36 (+2.88%)</td><td>171.30 (+0.47%)</td><td>127.70 (-5.55%)</td><td>35.33 <b>(+59.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>167.54 (n/a)</td><td>170.50 (n/a)</td><td>135.20 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+2.85%)</td><td>0.03 (-4.14%)</td><td>0.02 (-12.15%)</td><td>0.02 (+1.18%)</td><td>0.00 (-3.07%)</td><td>235.60 (-1.17%)</td><td>207.02 (+4.11%)</td><td>213.10 (+13.84%)</td><td>165.60 (-2.76%)</td><td>25.91 (-9.63%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>198.84 (n/a)</td><td>187.20 (n/a)</td><td>170.30 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (-2.12%)</td><td>0.07 (+4.32%)</td><td>0.06 (+3.15%)</td><td>0.05 (-8.22%)</td><td>0.01 (+9.28%)</td><td>215.50 (+8.95%)</td><td>164.24 (-3.45%)</td><td>167.50 (-3.01%)</td><td>131.60 (+2.17%)</td><td>33.72 (+18.49%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>170.10 (n/a)</td><td>172.70 (n/a)</td><td>128.80 (n/a)</td><td>28.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (-7.63%)</td><td>0.07 (-6.51%)</td><td>0.07 (-3.20%)</td><td>0.05 (-12.40%)</td><td>0.01 (-3.62%)</td><td>190.90 (+14.17%)</td><td>153.44 (+7.20%)</td><td>148.70 (+3.26%)</td><td>131.60 (+8.22%)</td><td>22.82 <b>(+22.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>167.20 (n/a)</td><td>143.14 (n/a)</td><td>144.00 (n/a)</td><td>121.60 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (+12.83%)</td><td>0.07 (+6.98%)</td><td>0.07 (+3.25%)</td><td>0.06 (+5.28%)</td><td>0.01 <b>(+33.04%)</b></td><td>184.00 (-5.01%)</td><td>153.30 (-5.65%)</td><td>150.30 (-3.16%)</td><td>122.20 (-11.32%)</td><td>28.22 (+13.47%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>162.48 (n/a)</td><td>155.20 (n/a)</td><td>137.80 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (+19.46%)</td><td>0.06 (+7.30%)</td><td>0.06 (+6.65%)</td><td>0.05 (+12.04%)</td><td>0.02 <b>(+26.84%)</b></td><td>217.30 (-10.76%)</td><td>172.88 (-5.95%)</td><td>166.20 (-6.21%)</td><td>122.50 (-16.27%)</td><td>40.11 (-0.67%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.50 (n/a)</td><td>183.82 (n/a)</td><td>177.20 (n/a)</td><td>146.30 (n/a)</td><td>40.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (+10.57%)</td><td>0.07 (+4.30%)</td><td>0.06 (+3.12%)</td><td>0.06 (+0.11%)</td><td>0.01 <b>(+23.76%)</b></td><td>185.70 (-0.16%)</td><td>157.28 (-3.56%)</td><td>164.40 (-3.07%)</td><td>116.50 (-9.62%)</td><td>25.95 (+7.86%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>163.08 (n/a)</td><td>169.60 (n/a)</td><td>128.90 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 <b>(+25.74%)</b></td><td>0.06 (+10.81%)</td><td>0.06 (+2.38%)</td><td>0.05 (+3.56%)</td><td>0.02 <b>(+71.38%)</b></td><td>227.20 (-3.40%)</td><td>176.70 (-7.37%)</td><td>178.50 (-2.30%)</td><td>124.00 <b>(-20.46%)</b></td><td>41.84 <b>(+30.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>190.76 (n/a)</td><td>182.70 (n/a)</td><td>155.90 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 <b>(+25.60%)</b></td><td>0.07 (+7.57%)</td><td>0.07 (+4.29%)</td><td>0.06 (+9.44%)</td><td>0.01 <b>(+65.16%)</b></td><td>186.00 (-8.60%)</td><td>155.28 (-5.90%)</td><td>148.70 (-4.13%)</td><td>119.90 <b>(-20.39%)</b></td><td>26.58 <b>(+20.37%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>165.02 (n/a)</td><td>155.10 (n/a)</td><td>150.60 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(+24.03%)</b></td><td>0.06 <b>(+25.92%)</b></td><td>0.06 (+9.42%)</td><td>0.05 <b>(+51.90%)</b></td><td>0.01 (-11.36%)</td><td>224.10 <b>(-34.17%)</b></td><td>183.64 <b>(-22.75%)</b></td><td>187.00 (-8.60%)</td><td>149.90 (-19.37%)</td><td>28.94 <b>(-53.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>340.40 (n/a)</td><td>237.72 (n/a)</td><td>204.60 (n/a)</td><td>185.90 (n/a)</td><td>62.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 <b>(+32.03%)</b></td><td>0.14 (+16.68%)</td><td>0.14 (+17.49%)</td><td>0.10 (+10.53%)</td><td>0.03 <b>(+70.08%)</b></td><td>217.30 (-9.50%)</td><td>159.32 (-12.57%)</td><td>147.30 (-14.90%)</td><td>119.00 <b>(-24.25%)</b></td><td>37.86 (+14.39%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>182.22 (n/a)</td><td>173.10 (n/a)</td><td>157.10 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (-8.94%)</td><td>0.14 <b>(+20.85%)</b></td><td>0.14 <b>(+28.89%)</b></td><td>0.12 <b>(+57.85%)</b></td><td>0.02 <b>(-53.92%)</b></td><td>168.80 <b>(-36.66%)</b></td><td>149.34 <b>(-23.31%)</b></td><td>153.60 <b>(-22.42%)</b></td><td>125.90 (+9.76%)</td><td>19.61 <b>(-67.74%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>266.50 (n/a)</td><td>194.72 (n/a)</td><td>198.00 (n/a)</td><td>114.70 (n/a)</td><td>60.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (-6.51%)</td><td>0.10 (+0.86%)</td><td>0.11 (-9.16%)</td><td>0.07 <b>(+25.55%)</b></td><td>0.02 <b>(-30.99%)</b></td><td>300.70 <b>(-20.34%)</b></td><td>209.38 (-6.73%)</td><td>198.40 (+10.10%)</td><td>157.00 (+6.95%)</td><td>54.12 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>377.50 (n/a)</td><td>224.48 (n/a)</td><td>180.20 (n/a)</td><td>146.80 (n/a)</td><td>91.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (-8.42%)</td><td>0.12 (+2.25%)</td><td>0.12 (+0.65%)</td><td>0.10 (+12.96%)</td><td>0.01 <b>(-45.41%)</b></td><td>204.20 (-11.49%)</td><td>180.22 (-4.25%)</td><td>182.40 (-0.65%)</td><td>153.40 (+9.26%)</td><td>18.36 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>188.22 (n/a)</td><td>183.60 (n/a)</td><td>140.40 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 <b>(+23.29%)</b></td><td>0.13 <b>(+21.12%)</b></td><td>0.11 (+10.75%)</td><td>0.09 (+16.16%)</td><td>0.03 <b>(+57.54%)</b></td><td>241.40 (-13.91%)</td><td>176.46 (-15.63%)</td><td>183.60 (-9.69%)</td><td>127.30 (-18.92%)</td><td>46.57 (+4.45%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>280.40 (n/a)</td><td>209.14 (n/a)</td><td>203.30 (n/a)</td><td>157.00 (n/a)</td><td>44.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (-18.34%)</td><td>0.10 (-1.31%)</td><td>0.10 (+6.94%)</td><td>0.10 (+14.34%)</td><td>0.00 <b>(-73.49%)</b></td><td>217.50 (-12.55%)</td><td>207.02 (-0.65%)</td><td>202.80 (-6.50%)</td><td>198.90 <b>(+22.48%)</b></td><td>9.48 <b>(-71.19%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>208.38 (n/a)</td><td>216.90 (n/a)</td><td>162.40 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (-16.38%)</td><td>0.11 (-8.47%)</td><td>0.11 (-13.13%)</td><td>0.09 (-4.20%)</td><td>0.02 <b>(-22.93%)</b></td><td>232.80 (+4.39%)</td><td>188.80 (+8.36%)</td><td>194.40 (+15.10%)</td><td>155.00 (+19.60%)</td><td>32.21 (-5.83%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>174.24 (n/a)</td><td>168.90 (n/a)</td><td>129.60 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (+10.51%)</td><td>0.10 (+6.46%)</td><td>0.10 (-1.94%)</td><td>0.09 (+0.63%)</td><td>0.02 <b>(+78.86%)</b></td><td>246.60 (-0.64%)</td><td>207.58 (-4.51%)</td><td>216.00 (+1.98%)</td><td>168.50 (-9.51%)</td><td>36.25 <b>(+57.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>217.38 (n/a)</td><td>211.80 (n/a)</td><td>186.20 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>143.54 (n/a)</td><td>123.20 (n/a)</td><td>111.20 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>160.76 (n/a)</td><td>161.20 (n/a)</td><td>130.30 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>179.26 (n/a)</td><td>174.70 (n/a)</td><td>157.40 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.40 (n/a)</td><td>207.08 (n/a)</td><td>211.90 (n/a)</td><td>180.00 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>174.80 (n/a)</td><td>164.80 (n/a)</td><td>134.50 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.50 (n/a)</td><td>176.82 (n/a)</td><td>155.40 (n/a)</td><td>136.90 (n/a)</td><td>42.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>171.56 (n/a)</td><td>173.80 (n/a)</td><td>137.60 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>253.20 (n/a)</td><td>191.52 (n/a)</td><td>171.90 (n/a)</td><td>133.10 (n/a)</td><td>57.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>183.06 (n/a)</td><td>182.60 (n/a)</td><td>158.00 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>376.40 (n/a)</td><td>217.04 (n/a)</td><td>180.60 (n/a)</td><td>152.40 (n/a)</td><td>92.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>236.90 (n/a)</td><td>189.60 (n/a)</td><td>199.20 (n/a)</td><td>127.50 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>242.00 (n/a)</td><td>211.80 (n/a)</td><td>216.20 (n/a)</td><td>150.00 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.40 <b>(+21.82%)</b></td><td>0.31 (+10.90%)</td><td>0.29 (+5.60%)</td><td>0.24 (+14.68%)</td><td>0.06 <b>(+46.68%)</b></td><td>201.40 (-12.78%)</td><td>164.80 (-8.77%)</td><td>167.90 (-5.30%)</td><td>124.40 (-17.89%)</td><td>32.78 (+4.82%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>230.90 (n/a)</td><td>180.64 (n/a)</td><td>177.30 (n/a)</td><td>151.50 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>178.70 (n/a)</td><td>142.70 (n/a)</td><td>144.80 (n/a)</td><td>106.40 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>215.80 (n/a)</td><td>182.48 (n/a)</td><td>197.20 (n/a)</td><td>131.40 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>251.20 (n/a)</td><td>193.52 (n/a)</td><td>204.80 (n/a)</td><td>112.70 (n/a)</td><td>50.47 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>155.86 (n/a)</td><td>159.20 (n/a)</td><td>123.40 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>181.24 (n/a)</td><td>187.00 (n/a)</td><td>147.50 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>147.30 (n/a)</td><td>129.00 (n/a)</td><td>109.10 (n/a)</td><td>40.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>182.30 (n/a)</td><td>191.20 (n/a)</td><td>153.10 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>152.20 (n/a)</td><td>151.20 (n/a)</td><td>109.60 (n/a)</td><td>35.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.00 (n/a)</td><td>152.48 (n/a)</td><td>140.10 (n/a)</td><td>114.00 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>172.72 (n/a)</td><td>163.10 (n/a)</td><td>116.00 (n/a)</td><td>42.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>276.60 (n/a)</td><td>198.94 (n/a)</td><td>170.30 (n/a)</td><td>160.00 (n/a)</td><td>49.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>196.60 (n/a)</td><td>158.88 (n/a)</td><td>153.00 (n/a)</td><td>113.30 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>161.32 (n/a)</td><td>173.80 (n/a)</td><td>124.40 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>235.70 (n/a)</td><td>187.30 (n/a)</td><td>204.70 (n/a)</td><td>127.50 (n/a)</td><td>45.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.20 (n/a)</td><td>191.22 (n/a)</td><td>193.70 (n/a)</td><td>130.60 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>245.10 (n/a)</td><td>154.76 (n/a)</td><td>132.30 (n/a)</td><td>125.80 (n/a)</td><td>50.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.04 (n/a)</td><td>160.90 (n/a)</td><td>143.26 (n/a)</td><td>149.00 (n/a)</td><td>125.80 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>204.90 (n/a)</td><td>166.48 (n/a)</td><td>164.00 (n/a)</td><td>128.90 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>141.16 (n/a)</td><td>121.70 (n/a)</td><td>109.40 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>274.40 (n/a)</td><td>171.94 (n/a)</td><td>159.70 (n/a)</td><td>119.30 (n/a)</td><td>59.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>168.50 (n/a)</td><td>185.40 (n/a)</td><td>105.20 (n/a)</td><td>51.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>280.70 (n/a)</td><td>204.02 (n/a)</td><td>210.60 (n/a)</td><td>137.90 (n/a)</td><td>53.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>179.68 (n/a)</td><td>171.40 (n/a)</td><td>156.50 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.10 (n/a)</td><td>195.36 (n/a)</td><td>211.30 (n/a)</td><td>157.80 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.40 (n/a)</td><td>188.02 (n/a)</td><td>177.30 (n/a)</td><td>148.00 (n/a)</td><td>36.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.60 (n/a)</td><td>249.58 (n/a)</td><td>229.20 (n/a)</td><td>216.00 (n/a)</td><td>43.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.00 (n/a)</td><td>178.08 (n/a)</td><td>172.70 (n/a)</td><td>162.00 (n/a)</td><td>14.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>268.10 (n/a)</td><td>174.72 (n/a)</td><td>167.80 (n/a)</td><td>101.90 (n/a)</td><td>59.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>172.48 (n/a)</td><td>183.80 (n/a)</td><td>138.10 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>176.78 (n/a)</td><td>191.20 (n/a)</td><td>122.10 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.00 (n/a)</td><td>209.86 (n/a)</td><td>217.40 (n/a)</td><td>179.20 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>196.22 (n/a)</td><td>203.20 (n/a)</td><td>179.80 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>182.78 (n/a)</td><td>160.80 (n/a)</td><td>126.10 (n/a)</td><td>49.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>308.90 (n/a)</td><td>239.34 (n/a)</td><td>231.90 (n/a)</td><td>196.70 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>270.90 (n/a)</td><td>216.70 (n/a)</td><td>217.60 (n/a)</td><td>183.40 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>241.50 (n/a)</td><td>194.56 (n/a)</td><td>177.10 (n/a)</td><td>167.70 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.30 (n/a)</td><td>185.42 (n/a)</td><td>188.60 (n/a)</td><td>150.50 (n/a)</td><td>34.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.80 (n/a)</td><td>172.78 (n/a)</td><td>172.00 (n/a)</td><td>129.10 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.50 (n/a)</td><td>180.42 (n/a)</td><td>160.60 (n/a)</td><td>150.20 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>189.48 (n/a)</td><td>186.10 (n/a)</td><td>138.00 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.60 (n/a)</td><td>208.94 (n/a)</td><td>201.50 (n/a)</td><td>150.10 (n/a)</td><td>48.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>292.80 (n/a)</td><td>215.04 (n/a)</td><td>206.40 (n/a)</td><td>173.80 (n/a)</td><td>47.79 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.00 (n/a)</td><td>159.52 (n/a)</td><td>165.70 (n/a)</td><td>120.20 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>217.50 (n/a)</td><td>150.36 (n/a)</td><td>133.30 (n/a)</td><td>105.00 (n/a)</td><td>44.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.80 (n/a)</td><td>156.36 (n/a)</td><td>150.30 (n/a)</td><td>123.90 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>175.00 (n/a)</td><td>145.40 (n/a)</td><td>146.10 (n/a)</td><td>123.50 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.00 (n/a)</td><td>149.90 (n/a)</td><td>153.10 (n/a)</td><td>118.80 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.00 (n/a)</td><td>195.40 (n/a)</td><td>205.80 (n/a)</td><td>156.50 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.00 (n/a)</td><td>177.30 (n/a)</td><td>176.70 (n/a)</td><td>138.20 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>272.10 (n/a)</td><td>220.14 (n/a)</td><td>225.80 (n/a)</td><td>170.20 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.28 (+0.93%)</td><td>3.88 (+1.26%)</td><td>4.17 (+12.42%)</td><td>3.24 (-6.64%)</td><td>0.50 <b>(+37.62%)</b></td><td>2903.40 (+7.12%)</td><td>2458.00 (-0.54%)</td><td>2253.30 (-11.05%)</td><td>2198.90 (-0.92%)</td><td>334.08 <b>(+45.61%)</b></td><td>1682.37 (+0.93%)</td><td>1526.35 (+1.26%)</td><td>1641.79 (+12.42%)</td><td>1274.17 (-6.64%)</td><td>196.16 <b>(+37.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>4.24 (n/a)</td><td>3.83 (n/a)</td><td>3.71 (n/a)</td><td>3.47 (n/a)</td><td>0.36 (n/a)</td><td>2710.50 (n/a)</td><td>2471.46 (n/a)</td><td>2533.10 (n/a)</td><td>2219.30 (n/a)</td><td>229.44 (n/a)</td><td>1666.90 (n/a)</td><td>1507.42 (n/a)</td><td>1460.43 (n/a)</td><td>1364.83 (n/a)</td><td>142.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.22 (+7.66%)</td><td>0.90 (+1.42%)</td><td>0.93 (-0.86%)</td><td>0.68 (+3.29%)</td><td>0.23 (+8.20%)</td><td>324.50 (-3.19%)</td><td>257.44 (-1.09%)</td><td>237.00 (+0.85%)</td><td>180.90 (-7.09%)</td><td>63.56 (-0.84%)</td><td>52.18 (+7.66%)</td><td>38.55 (+1.42%)</td><td>39.81 (-0.86%)</td><td>29.08 (+3.29%)</td><td>9.71 (+8.20%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.14 (n/a)</td><td>0.89 (n/a)</td><td>0.94 (n/a)</td><td>0.66 (n/a)</td><td>0.21 (n/a)</td><td>335.20 (n/a)</td><td>260.28 (n/a)</td><td>235.00 (n/a)</td><td>194.70 (n/a)</td><td>64.10 (n/a)</td><td>48.47 (n/a)</td><td>38.01 (n/a)</td><td>40.16 (n/a)</td><td>28.15 (n/a)</td><td>8.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.11 (-11.63%)</td><td>0.99 (+2.49%)</td><td>1.09 (+1.33%)</td><td>0.70 (+0.97%)</td><td>0.18 <b>(-29.43%)</b></td><td>317.20 (-0.97%)</td><td>231.68 (-5.18%)</td><td>202.10 (-1.32%)</td><td>198.80 (+13.15%)</td><td>50.78 <b>(-25.97%)</b></td><td>47.47 (-11.63%)</td><td>42.07 (+2.49%)</td><td>46.69 (+1.33%)</td><td>29.75 (+0.97%)</td><td>7.67 <b>(-29.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.26 (n/a)</td><td>0.96 (n/a)</td><td>1.08 (n/a)</td><td>0.69 (n/a)</td><td>0.25 (n/a)</td><td>320.30 (n/a)</td><td>244.34 (n/a)</td><td>204.80 (n/a)</td><td>175.70 (n/a)</td><td>68.60 (n/a)</td><td>53.72 (n/a)</td><td>41.05 (n/a)</td><td>46.08 (n/a)</td><td>29.46 (n/a)</td><td>10.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.52 (-0.10%)</td><td>0.52 (+0.06%)</td><td>0.52 (+0.06%)</td><td>0.52 (+0.21%)</td><td>0.00 <b>(-58.97%)</b></td><td>48529.00 (-0.21%)</td><td>48475.22 (-0.06%)</td><td>48467.60 (-0.06%)</td><td>48434.40 (+0.10%)</td><td>42.30 <b>(-58.99%)</b></td><td>354.70 (-0.10%)</td><td>354.41 (+0.06%)</td><td>354.46 (+0.06%)</td><td>354.01 (+0.21%)</td><td>0.31 <b>(-58.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48632.10 (n/a)</td><td>48504.70 (n/a)</td><td>48498.60 (n/a)</td><td>48388.10 (n/a)</td><td>103.15 (n/a)</td><td>355.04 (n/a)</td><td>354.19 (n/a)</td><td>354.23 (n/a)</td><td>353.26 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (-0.37%)</td><td>0.21 (-0.40%)</td><td>0.21 (-0.42%)</td><td>0.21 (-0.61%)</td><td>0.00 (+1.70%)</td><td>119550.40 (+0.62%)</td><td>118234.82 (+0.40%)</td><td>118795.60 (+0.42%)</td><td>115329.20 (+0.37%)</td><td>1662.24 (+2.57%)</td><td>148.96 (-0.37%)</td><td>145.33 (-0.40%)</td><td>144.62 (-0.42%)</td><td>143.70 (-0.61%)</td><td>2.08 (+1.70%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118818.00 (n/a)</td><td>117764.06 (n/a)</td><td>118294.10 (n/a)</td><td>114904.30 (n/a)</td><td>1620.64 (n/a)</td><td>149.51 (n/a)</td><td>145.91 (n/a)</td><td>145.23 (n/a)</td><td>144.59 (n/a)</td><td>2.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.91 (+0.15%)</td><td>0.89 (-0.29%)</td><td>0.90 (+0.51%)</td><td>0.87 (-1.31%)</td><td>0.01 <b>(+52.18%)</b></td><td>28801.10 (+1.32%)</td><td>28232.64 (+0.30%)</td><td>28114.10 (-0.50%)</td><td>27619.70 (-0.15%)</td><td>468.75 <b>(+54.27%)</b></td><td>622.02 (+0.15%)</td><td>608.64 (-0.29%)</td><td>611.08 (+0.51%)</td><td>596.50 (-1.31%)</td><td>10.11 <b>(+52.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28425.20 (n/a)</td><td>28148.38 (n/a)</td><td>28256.40 (n/a)</td><td>27661.90 (n/a)</td><td>303.86 (n/a)</td><td>621.07 (n/a)</td><td>610.39 (n/a)</td><td>608.00 (n/a)</td><td>604.39 (n/a)</td><td>6.65 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.66 (+0.87%)</td><td>3.49 (-0.60%)</td><td>3.54 (+0.66%)</td><td>3.36 (-2.13%)</td><td>0.13 <b>(+73.85%)</b></td><td>7496.40 (+2.17%)</td><td>7210.56 (+0.68%)</td><td>7108.10 (-0.66%)</td><td>6875.80 (-0.86%)</td><td>269.88 <b>(+77.73%)</b></td><td>2498.62 (+0.87%)</td><td>2385.27 (-0.60%)</td><td>2416.93 (+0.66%)</td><td>2291.76 (-2.13%)</td><td>89.23 <b>(+73.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.63 (n/a)</td><td>3.52 (n/a)</td><td>3.52 (n/a)</td><td>3.43 (n/a)</td><td>0.08 (n/a)</td><td>7336.90 (n/a)</td><td>7161.80 (n/a)</td><td>7155.40 (n/a)</td><td>6935.70 (n/a)</td><td>151.85 (n/a)</td><td>2477.03 (n/a)</td><td>2399.69 (n/a)</td><td>2400.97 (n/a)</td><td>2341.58 (n/a)</td><td>51.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.13 (-4.90%)</td><td>2.97 (-1.18%)</td><td>3.05 (+0.78%)</td><td>2.75 (-2.88%)</td><td>0.17 (-9.94%)</td><td>9162.20 (+2.96%)</td><td>8509.40 (+1.15%)</td><td>8263.60 (-0.78%)</td><td>8043.90 (+5.15%)</td><td>498.53 (-3.05%)</td><td>2135.77 (-4.90%)</td><td>2024.37 (-1.18%)</td><td>2078.98 (+0.78%)</td><td>1875.08 (-2.88%)</td><td>116.13 (-9.94%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.29 (n/a)</td><td>3.00 (n/a)</td><td>3.02 (n/a)</td><td>2.83 (n/a)</td><td>0.19 (n/a)</td><td>8898.60 (n/a)</td><td>8412.66 (n/a)</td><td>8328.20 (n/a)</td><td>7649.90 (n/a)</td><td>514.20 (n/a)</td><td>2245.78 (n/a)</td><td>2048.44 (n/a)</td><td>2062.85 (n/a)</td><td>1930.62 (n/a)</td><td>128.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.32 (-1.03%)</td><td>3.20 (-0.47%)</td><td>3.18 (-0.22%)</td><td>3.15 (+0.56%)</td><td>0.07 <b>(-20.63%)</b></td><td>7990.10 (-0.55%)</td><td>7862.40 (+0.45%)</td><td>7918.00 (+0.22%)</td><td>7577.40 (+1.04%)</td><td>162.85 <b>(-20.30%)</b></td><td>2267.25 (-1.03%)</td><td>2185.84 (-0.47%)</td><td>2169.73 (-0.22%)</td><td>2150.15 (+0.56%)</td><td>46.43 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.36 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.13 (n/a)</td><td>0.09 (n/a)</td><td>8034.60 (n/a)</td><td>7827.28 (n/a)</td><td>7900.90 (n/a)</td><td>7499.20 (n/a)</td><td>204.34 (n/a)</td><td>2290.89 (n/a)</td><td>2196.09 (n/a)</td><td>2174.41 (n/a)</td><td>2138.24 (n/a)</td><td>58.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.79 (+0.40%)</td><td>0.79 (+0.04%)</td><td>0.79 (-0.03%)</td><td>0.78 (-0.12%)</td><td>0.00 <b>(+2202.97%)</b></td><td>96238.30 (+0.12%)</td><td>96069.52 (-0.04%)</td><td>96137.30 (+0.03%)</td><td>95714.10 (-0.40%)</td><td>206.95 <b>(+2198.02%)</b></td><td>717.97 (+0.40%)</td><td>715.31 (+0.04%)</td><td>714.81 (-0.03%)</td><td>714.06 (-0.12%)</td><td>1.54 <b>(+2203.49%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96120.50 (n/a)</td><td>96106.24 (n/a)</td><td>96104.50 (n/a)</td><td>96096.00 (n/a)</td><td>9.01 (n/a)</td><td>715.11 (n/a)</td><td>715.04 (n/a)</td><td>715.05 (n/a)</td><td>714.93 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.73 (-0.05%)</td><td>0.73 (-0.08%)</td><td>0.73 (-0.10%)</td><td>0.73 (-0.11%)</td><td>0.00 <b>(+67.27%)</b></td><td>103461.40 (+0.11%)</td><td>103385.74 (+0.08%)</td><td>103398.40 (+0.10%)</td><td>103309.50 (+0.05%)</td><td>59.02 <b>(+67.59%)</b></td><td>665.18 (-0.05%)</td><td>664.69 (-0.08%)</td><td>664.61 (-0.10%)</td><td>664.20 (-0.11%)</td><td>0.38 <b>(+67.29%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103343.00 (n/a)</td><td>103299.72 (n/a)</td><td>103296.10 (n/a)</td><td>103260.90 (n/a)</td><td>35.22 (n/a)</td><td>665.49 (n/a)</td><td>665.24 (n/a)</td><td>665.27 (n/a)</td><td>664.96 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.69 (-0.45%)</td><td>0.69 (-0.67%)</td><td>0.69 (-0.65%)</td><td>0.69 (-1.09%)</td><td>0.00 <b>(+303.18%)</b></td><td>109772.30 (+1.10%)</td><td>109223.54 (+0.68%)</td><td>109170.20 (+0.65%)</td><td>108869.60 (+0.45%)</td><td>344.45 <b>(+309.55%)</b></td><td>631.21 (-0.45%)</td><td>629.17 (-0.67%)</td><td>629.47 (-0.65%)</td><td>626.02 (-1.09%)</td><td>1.98 <b>(+303.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108573.30 (n/a)</td><td>108487.10 (n/a)</td><td>108464.30 (n/a)</td><td>108379.30 (n/a)</td><td>84.10 (n/a)</td><td>634.06 (n/a)</td><td>633.43 (n/a)</td><td>633.57 (n/a)</td><td>632.93 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.42 (-4.00%)</td><td>6.55 (-3.79%)</td><td>6.59 (-8.73%)</td><td>5.05 (+3.66%)</td><td>0.91 (-19.50%)</td><td>1764.30 (-3.54%)</td><td>1385.26 (+2.94%)</td><td>1352.60 (+9.57%)</td><td>1201.10 (+4.16%)</td><td>221.79 (-19.61%)</td><td>446.97 (-4.00%)</td><td>394.54 (-3.79%)</td><td>396.92 (-8.73%)</td><td>304.30 (+3.66%)</td><td>54.82 (-19.50%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.73 (n/a)</td><td>6.81 (n/a)</td><td>7.22 (n/a)</td><td>4.87 (n/a)</td><td>1.13 (n/a)</td><td>1829.00 (n/a)</td><td>1345.68 (n/a)</td><td>1234.50 (n/a)</td><td>1153.10 (n/a)</td><td>275.89 (n/a)</td><td>465.60 (n/a)</td><td>410.09 (n/a)</td><td>434.90 (n/a)</td><td>293.54 (n/a)</td><td>68.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.09 (+5.12%)</td><td>6.55 (+10.63%)</td><td>6.91 (+5.79%)</td><td>4.84 (+0.33%)</td><td>0.96 (-2.33%)</td><td>1840.30 (-0.32%)</td><td>1389.68 (-9.80%)</td><td>1289.50 (-5.48%)</td><td>1257.80 (-4.87%)</td><td>252.35 (-7.03%)</td><td>426.84 (+5.12%)</td><td>394.72 (+10.63%)</td><td>416.34 (+5.79%)</td><td>291.73 (+0.33%)</td><td>57.79 (-2.33%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.74 (n/a)</td><td>5.92 (n/a)</td><td>6.53 (n/a)</td><td>4.83 (n/a)</td><td>0.98 (n/a)</td><td>1846.30 (n/a)</td><td>1540.64 (n/a)</td><td>1364.20 (n/a)</td><td>1322.20 (n/a)</td><td>271.43 (n/a)</td><td>406.03 (n/a)</td><td>356.81 (n/a)</td><td>393.55 (n/a)</td><td>290.78 (n/a)</td><td>59.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>6.91 (+0.53%)</td><td>6.56 (+0.23%)</td><td>6.51 (-0.96%)</td><td>6.15 (-1.63%)</td><td>0.32 <b>(+40.00%)</b></td><td>1449.30 (+1.66%)</td><td>1361.20 (-0.14%)</td><td>1370.10 (+0.97%)</td><td>1289.00 (-0.53%)</td><td>66.35 <b>(+40.97%)</b></td><td>416.49 (+0.53%)</td><td>395.16 (+0.23%)</td><td>391.86 (-0.96%)</td><td>370.43 (-1.63%)</td><td>19.17 <b>(+40.00%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.88 (n/a)</td><td>6.54 (n/a)</td><td>6.57 (n/a)</td><td>6.25 (n/a)</td><td>0.23 (n/a)</td><td>1425.70 (n/a)</td><td>1363.12 (n/a)</td><td>1356.90 (n/a)</td><td>1295.90 (n/a)</td><td>47.07 (n/a)</td><td>414.28 (n/a)</td><td>394.23 (n/a)</td><td>395.67 (n/a)</td><td>376.57 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>8.02 (+0.24%)</td><td>7.65 (-2.82%)</td><td>7.96 (+0.10%)</td><td>7.12 (-6.02%)</td><td>0.47 <b>(+171.97%)</b></td><td>4897.30 (+6.40%)</td><td>4568.88 (+3.18%)</td><td>4380.10 (-0.10%)</td><td>4348.20 (-0.24%)</td><td>285.37 <b>(+187.53%)</b></td><td>493.88 (+0.24%)</td><td>471.46 (-2.82%)</td><td>490.28 (+0.10%)</td><td>438.50 (-6.02%)</td><td>28.79 <b>(+171.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.00 (n/a)</td><td>7.88 (n/a)</td><td>7.95 (n/a)</td><td>7.58 (n/a)</td><td>0.17 (n/a)</td><td>4602.60 (n/a)</td><td>4428.28 (n/a)</td><td>4384.70 (n/a)</td><td>4358.50 (n/a)</td><td>99.25 (n/a)</td><td>492.71 (n/a)</td><td>485.14 (n/a)</td><td>489.77 (n/a)</td><td>466.58 (n/a)</td><td>10.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.69 (-0.13%)</td><td>7.63 (+4.16%)</td><td>7.63 (+3.04%)</td><td>7.58 (+11.33%)</td><td>0.04 <b>(-88.95%)</b></td><td>4600.00 (-10.17%)</td><td>4571.16 (-4.18%)</td><td>4571.90 (-2.95%)</td><td>4536.00 (+0.12%)</td><td>23.38 <b>(-90.07%)</b></td><td>473.43 (-0.12%)</td><td>469.80 (+4.16%)</td><td>469.71 (+3.04%)</td><td>466.85 (+11.33%)</td><td>2.41 <b>(-88.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.70 (n/a)</td><td>7.32 (n/a)</td><td>7.40 (n/a)</td><td>6.81 (n/a)</td><td>0.35 (n/a)</td><td>5121.00 (n/a)</td><td>4770.36 (n/a)</td><td>4711.10 (n/a)</td><td>4530.40 (n/a)</td><td>235.53 (n/a)</td><td>474.02 (n/a)</td><td>451.03 (n/a)</td><td>455.83 (n/a)</td><td>419.35 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.47 (-4.80%)</td><td>7.26 (-0.15%)</td><td>7.31 (+0.55%)</td><td>6.78 (+2.08%)</td><td>0.28 <b>(-36.15%)</b></td><td>5142.90 (-2.04%)</td><td>4811.02 (-0.02%)</td><td>4772.40 (-0.55%)</td><td>4669.20 (+5.04%)</td><td>193.23 <b>(-34.28%)</b></td><td>459.92 (-4.80%)</td><td>446.92 (-0.15%)</td><td>449.98 (+0.55%)</td><td>417.56 (+2.08%)</td><td>17.21 <b>(-36.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.84 (n/a)</td><td>7.27 (n/a)</td><td>7.27 (n/a)</td><td>6.64 (n/a)</td><td>0.44 (n/a)</td><td>5250.00 (n/a)</td><td>4811.96 (n/a)</td><td>4798.90 (n/a)</td><td>4445.20 (n/a)</td><td>294.04 (n/a)</td><td>483.10 (n/a)</td><td>447.60 (n/a)</td><td>447.50 (n/a)</td><td>409.05 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.79 (-0.01%)</td><td>0.79 (-0.01%)</td><td>0.79 (-0.01%)</td><td>0.79 (-0.02%)</td><td>0.00 (+9.72%)</td><td>95467.20 (+0.02%)</td><td>95420.62 (+0.01%)</td><td>95419.90 (+0.01%)</td><td>95391.90 (+0.01%)</td><td>30.08 (+9.88%)</td><td>720.39 (-0.01%)</td><td>720.17 (-0.01%)</td><td>720.18 (-0.01%)</td><td>719.82 (-0.02%)</td><td>0.23 (+9.73%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95447.50 (n/a)</td><td>95411.92 (n/a)</td><td>95412.10 (n/a)</td><td>95385.10 (n/a)</td><td>27.38 (n/a)</td><td>720.44 (n/a)</td><td>720.24 (n/a)</td><td>720.24 (n/a)</td><td>719.97 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.74 (-0.02%)</td><td>0.74 (-0.00%)</td><td>0.74 (-0.00%)</td><td>0.74 (+0.03%)</td><td>0.00 <b>(-63.01%)</b></td><td>102604.20 (-0.03%)</td><td>102587.02 (+0.00%)</td><td>102584.80 (+0.00%)</td><td>102577.80 (+0.02%)</td><td>10.04 <b>(-62.94%)</b></td><td>669.93 (-0.02%)</td><td>669.87 (-0.00%)</td><td>669.88 (-0.00%)</td><td>669.75 (+0.03%)</td><td>0.07 <b>(-63.00%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102630.50 (n/a)</td><td>102586.70 (n/a)</td><td>102582.80 (n/a)</td><td>102555.80 (n/a)</td><td>27.10 (n/a)</td><td>670.07 (n/a)</td><td>669.87 (n/a)</td><td>669.89 (n/a)</td><td>669.58 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.70 (+0.17%)</td><td>0.70 (+0.06%)</td><td>0.70 (+0.04%)</td><td>0.70 (-0.00%)</td><td>0.00 <b>(+99.59%)</b></td><td>107555.50 (+0.00%)</td><td>107410.04 (-0.06%)</td><td>107448.50 (-0.04%)</td><td>107207.80 (-0.17%)</td><td>135.38 <b>(+99.24%)</b></td><td>640.99 (+0.17%)</td><td>639.79 (+0.06%)</td><td>639.56 (+0.04%)</td><td>638.92 (-0.00%)</td><td>0.81 <b>(+99.57%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107555.30 (n/a)</td><td>107470.92 (n/a)</td><td>107495.70 (n/a)</td><td>107391.60 (n/a)</td><td>67.95 (n/a)</td><td>639.90 (n/a)</td><td>639.42 (n/a)</td><td>639.28 (n/a)</td><td>638.92 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>3.66 (-8.83%)</td><td>3.27 (-10.60%)</td><td>3.17 (-15.08%)</td><td>2.90 (-9.20%)</td><td>0.37 (+16.93%)</td><td>2780.60 (+10.13%)</td><td>2486.44 (+12.27%)</td><td>2540.60 (+17.76%)</td><td>2200.90 (+9.69%)</td><td>273.14 <b>(+37.70%)</b></td><td>960.49 (-8.83%)</td><td>858.60 (-10.60%)</td><td>832.05 (-15.08%)</td><td>760.23 (-9.20%)</td><td>95.90 (+16.93%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>4.02 (n/a)</td><td>3.66 (n/a)</td><td>3.74 (n/a)</td><td>3.19 (n/a)</td><td>0.31 (n/a)</td><td>2524.80 (n/a)</td><td>2214.60 (n/a)</td><td>2157.50 (n/a)</td><td>2006.50 (n/a)</td><td>198.36 (n/a)</td><td>1053.55 (n/a)</td><td>960.40 (n/a)</td><td>979.79 (n/a)</td><td>837.25 (n/a)</td><td>82.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.35 <b>(-30.09%)</b></td><td>0.32 <b>(-21.16%)</b></td><td>0.33 (-10.08%)</td><td>0.28 (-19.34%)</td><td>0.03 <b>(-62.77%)</b></td><td>4412.10 <b>(+23.98%)</b></td><td>3880.88 <b>(+24.64%)</b></td><td>3824.10 (+11.21%)</td><td>3514.90 <b>(+43.04%)</b></td><td>337.39 <b>(-33.83%)</b></td><td>19.09 <b>(-30.09%)</b></td><td>17.39 <b>(-21.16%)</b></td><td>17.55 (-10.08%)</td><td>15.21 (-19.34%)</td><td>1.45 <b>(-62.77%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>3558.60 (n/a)</td><td>3113.76 (n/a)</td><td>3438.50 (n/a)</td><td>2457.20 (n/a)</td><td>509.85 (n/a)</td><td>27.31 (n/a)</td><td>22.06 (n/a)</td><td>19.52 (n/a)</td><td>18.86 (n/a)</td><td>3.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.94 (-1.82%)</td><td>4.76 (+14.59%)</td><td>4.82 <b>(+28.20%)</b></td><td>4.56 <b>(+32.16%)</b></td><td>0.18 <b>(-76.87%)</b></td><td>1459.30 <b>(-24.33%)</b></td><td>1399.72 (-14.88%)</td><td>1380.70 <b>(-22.00%)</b></td><td>1346.50 (+1.85%)</td><td>52.46 <b>(-81.74%)</b></td><td>1526.38 (-1.82%)</td><td>1469.96 (+14.59%)</td><td>1488.57 <b>(+28.20%)</b></td><td>1408.39 <b>(+32.16%)</b></td><td>54.65 <b>(-76.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.03 (n/a)</td><td>4.15 (n/a)</td><td>3.76 (n/a)</td><td>3.45 (n/a)</td><td>0.76 (n/a)</td><td>1928.50 (n/a)</td><td>1644.34 (n/a)</td><td>1770.10 (n/a)</td><td>1322.00 (n/a)</td><td>287.29 (n/a)</td><td>1554.60 (n/a)</td><td>1282.84 (n/a)</td><td>1161.09 (n/a)</td><td>1065.70 (n/a)</td><td>236.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.03 (n/a)</td><td>12.60 (n/a)</td><td>12.58 (n/a)</td><td>12.06 (n/a)</td><td>0.37 (n/a)</td><td>13.02 (n/a)</td><td>12.59 (n/a)</td><td>12.57 (n/a)</td><td>12.05 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>25.28 (+0.46%)</td><td>24.44 (+1.09%)</td><td>24.37 (-0.99%)</td><td>23.73 (+8.36%)</td><td>0.62 <b>(-52.10%)</b></td><td>25.27 (+0.46%)</td><td>24.42 (+1.09%)</td><td>24.36 (-0.99%)</td><td>23.72 (+8.36%)</td><td>0.62 <b>(-52.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>25.17 (n/a)</td><td>24.17 (n/a)</td><td>24.62 (n/a)</td><td>21.90 (n/a)</td><td>1.29 (n/a)</td><td>25.15 (n/a)</td><td>24.16 (n/a)</td><td>24.60 (n/a)</td><td>21.89 (n/a)</td><td>1.29 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>40.43 (-0.69%)</td><td>38.89 (-3.34%)</td><td>38.50 (-4.50%)</td><td>38.02 (-4.20%)</td><td>0.96 <b>(+106.98%)</b></td><td>40.41 (-0.69%)</td><td>38.87 (-3.34%)</td><td>38.48 (-4.50%)</td><td>38.00 (-4.20%)</td><td>0.96 <b>(+106.98%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>40.71 (n/a)</td><td>40.24 (n/a)</td><td>40.32 (n/a)</td><td>39.69 (n/a)</td><td>0.46 (n/a)</td><td>40.69 (n/a)</td><td>40.21 (n/a)</td><td>40.29 (n/a)</td><td>39.67 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>44.48 (-3.38%)</td><td>42.10 (+5.08%)</td><td>43.05 (-0.52%)</td><td>37.81 <b>(+49.58%)</b></td><td>2.79 <b>(-67.11%)</b></td><td>44.45 (-3.38%)</td><td>42.07 (+5.08%)</td><td>43.02 (-0.52%)</td><td>37.78 <b>(+49.58%)</b></td><td>2.79 <b>(-67.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>46.03 (n/a)</td><td>40.06 (n/a)</td><td>43.27 (n/a)</td><td>25.27 (n/a)</td><td>8.49 (n/a)</td><td>46.00 (n/a)</td><td>40.04 (n/a)</td><td>43.24 (n/a)</td><td>25.26 (n/a)</td><td>8.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.50 (n/a)</td><td>12.89 (n/a)</td><td>13.21 (n/a)</td><td>11.55 (n/a)</td><td>0.78 (n/a)</td><td>13.49 (n/a)</td><td>12.88 (n/a)</td><td>13.20 (n/a)</td><td>11.54 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>24.75 (-1.62%)</td><td>23.92 (-2.63%)</td><td>24.29 (-1.73%)</td><td>21.90 (-8.77%)</td><td>1.15 <b>(+133.09%)</b></td><td>24.74 (-1.62%)</td><td>23.91 (-2.63%)</td><td>24.27 (-1.73%)</td><td>21.89 (-8.77%)</td><td>1.15 <b>(+133.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>25.16 (n/a)</td><td>24.57 (n/a)</td><td>24.72 (n/a)</td><td>24.00 (n/a)</td><td>0.49 (n/a)</td><td>25.15 (n/a)</td><td>24.55 (n/a)</td><td>24.70 (n/a)</td><td>23.99 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>40.70 (-5.89%)</td><td>39.00 (-3.99%)</td><td>38.86 (-3.25%)</td><td>37.57 (-3.82%)</td><td>1.23 <b>(-28.20%)</b></td><td>40.68 (-5.89%)</td><td>38.98 (-3.99%)</td><td>38.84 (-3.25%)</td><td>37.55 (-3.82%)</td><td>1.23 <b>(-28.20%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>43.25 (n/a)</td><td>40.62 (n/a)</td><td>40.17 (n/a)</td><td>39.06 (n/a)</td><td>1.71 (n/a)</td><td>43.22 (n/a)</td><td>40.60 (n/a)</td><td>40.14 (n/a)</td><td>39.04 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>45.36 (+3.08%)</td><td>43.03 (-0.27%)</td><td>43.63 (+0.96%)</td><td>38.24 (-9.90%)</td><td>2.86 <b>(+374.17%)</b></td><td>45.34 (+3.08%)</td><td>43.00 (-0.27%)</td><td>43.60 (+0.96%)</td><td>38.22 (-9.90%)</td><td>2.86 <b>(+374.17%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>44.01 (n/a)</td><td>43.15 (n/a)</td><td>43.21 (n/a)</td><td>42.44 (n/a)</td><td>0.60 (n/a)</td><td>43.98 (n/a)</td><td>43.12 (n/a)</td><td>43.19 (n/a)</td><td>42.42 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.53 (-3.12%)</td><td>8.75 (-2.39%)</td><td>8.62 (-1.81%)</td><td>8.16 (-2.06%)</td><td>0.63 (-5.21%)</td><td>9.51 (-3.12%)</td><td>8.73 (-2.39%)</td><td>8.60 (-1.81%)</td><td>8.14 (-2.06%)</td><td>0.63 (-5.21%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.83 (n/a)</td><td>8.97 (n/a)</td><td>8.78 (n/a)</td><td>8.33 (n/a)</td><td>0.66 (n/a)</td><td>9.82 (n/a)</td><td>8.95 (n/a)</td><td>8.76 (n/a)</td><td>8.31 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.91 (-6.95%)</td><td>0.86 (-4.23%)</td><td>0.86 (-4.40%)</td><td>0.73 (-12.60%)</td><td>0.08 <b>(+20.67%)</b></td><td>0.90 (-6.95%)</td><td>0.84 (-4.23%)</td><td>0.85 (-4.40%)</td><td>0.72 (-12.60%)</td><td>0.07 <b>(+20.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.83 (n/a)</td><td>0.06 (n/a)</td><td>0.96 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.82 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.38 (-7.16%)</td><td>1.13 (-6.03%)</td><td>1.04 (-11.60%)</td><td>0.95 (+1.49%)</td><td>0.19 (-9.41%)</td><td>1.36 (-7.16%)</td><td>1.12 (-6.03%)</td><td>1.02 (-11.60%)</td><td>0.94 (+1.49%)</td><td>0.18 (-9.41%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.48 (n/a)</td><td>1.20 (n/a)</td><td>1.17 (n/a)</td><td>0.93 (n/a)</td><td>0.21 (n/a)</td><td>1.47 (n/a)</td><td>1.19 (n/a)</td><td>1.16 (n/a)</td><td>0.92 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>17.83 (-2.95%)</td><td>16.73 (-5.69%)</td><td>16.47 (-7.08%)</td><td>15.62 (-9.60%)</td><td>1.03 <b>(+131.53%)</b></td><td>17.62 (-2.95%)</td><td>16.54 (-5.69%)</td><td>16.28 (-7.08%)</td><td>15.44 (-9.60%)</td><td>1.02 <b>(+131.53%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>18.37 (n/a)</td><td>17.74 (n/a)</td><td>17.73 (n/a)</td><td>17.28 (n/a)</td><td>0.45 (n/a)</td><td>18.16 (n/a)</td><td>17.54 (n/a)</td><td>17.52 (n/a)</td><td>17.08 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.68 (-4.65%)</td><td>13.52 (+11.67%)</td><td>13.63 (+2.23%)</td><td>13.20 <b>(+77.58%)</b></td><td>0.21 <b>(-92.41%)</b></td><td>13.44 (-4.65%)</td><td>13.28 (+11.67%)</td><td>13.39 (+2.23%)</td><td>12.97 <b>(+77.58%)</b></td><td>0.21 <b>(-92.41%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.35 (n/a)</td><td>12.11 (n/a)</td><td>13.34 (n/a)</td><td>7.43 (n/a)</td><td>2.75 (n/a)</td><td>14.10 (n/a)</td><td>11.90 (n/a)</td><td>13.10 (n/a)</td><td>7.30 (n/a)</td><td>2.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.08 (-10.53%)</td><td>7.23 (-9.27%)</td><td>7.14 (-4.49%)</td><td>5.54 <b>(-24.40%)</b></td><td>1.26 (+2.99%)</td><td>8.93 (-10.53%)</td><td>7.11 (-9.27%)</td><td>7.02 (-4.49%)</td><td>5.45 <b>(-24.40%)</b></td><td>1.24 (+2.99%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>10.15 (n/a)</td><td>7.97 (n/a)</td><td>7.48 (n/a)</td><td>7.33 (n/a)</td><td>1.22 (n/a)</td><td>9.98 (n/a)</td><td>7.83 (n/a)</td><td>7.35 (n/a)</td><td>7.20 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.73 (-10.52%)</td><td>5.39 (-11.15%)</td><td>5.47 (-11.69%)</td><td>4.83 (-7.97%)</td><td>0.34 <b>(-27.82%)</b></td><td>5.64 (-10.52%)</td><td>5.30 (-11.15%)</td><td>5.38 (-11.69%)</td><td>4.75 (-7.97%)</td><td>0.33 <b>(-27.82%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.41 (n/a)</td><td>6.06 (n/a)</td><td>6.19 (n/a)</td><td>5.25 (n/a)</td><td>0.47 (n/a)</td><td>6.30 (n/a)</td><td>5.97 (n/a)</td><td>6.09 (n/a)</td><td>5.16 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.39 (n/a)</td><td>12.56 (n/a)</td><td>13.32 (n/a)</td><td>10.43 (n/a)</td><td>1.28 (n/a)</td><td>13.38 (n/a)</td><td>12.55 (n/a)</td><td>13.31 (n/a)</td><td>10.42 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.60 (n/a)</td><td>12.30 (n/a)</td><td>12.07 (n/a)</td><td>11.00 (n/a)</td><td>1.11 (n/a)</td><td>13.59 (n/a)</td><td>12.29 (n/a)</td><td>12.06 (n/a)</td><td>10.99 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.20 (n/a)</td><td>150.06 (n/a)</td><td>148.70 (n/a)</td><td>140.30 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.60 (n/a)</td><td>188.02 (n/a)</td><td>188.80 (n/a)</td><td>141.90 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>298.00 (n/a)</td><td>193.94 (n/a)</td><td>184.60 (n/a)</td><td>140.80 (n/a)</td><td>61.12 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>181.66 (n/a)</td><td>189.80 (n/a)</td><td>139.10 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.50 (n/a)</td><td>185.22 (n/a)</td><td>169.80 (n/a)</td><td>139.80 (n/a)</td><td>50.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>190.96 (n/a)</td><td>202.70 (n/a)</td><td>146.50 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>289.20 (n/a)</td><td>195.78 (n/a)</td><td>192.80 (n/a)</td><td>127.90 (n/a)</td><td>61.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>365.70 (n/a)</td><td>268.00 (n/a)</td><td>223.40 (n/a)</td><td>204.70 (n/a)</td><td>73.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>174.98 (n/a)</td><td>182.80 (n/a)</td><td>149.80 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>175.70 (n/a)</td><td>185.30 (n/a)</td><td>139.20 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>169.00 (n/a)</td><td>163.70 (n/a)</td><td>143.50 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>185.46 (n/a)</td><td>195.90 (n/a)</td><td>148.00 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>247.30 (n/a)</td><td>169.14 (n/a)</td><td>133.20 (n/a)</td><td>125.50 (n/a)</td><td>56.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>159.56 (n/a)</td><td>150.10 (n/a)</td><td>111.50 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>166.96 (n/a)</td><td>187.30 (n/a)</td><td>99.70 (n/a)</td><td>50.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>203.26 (n/a)</td><td>209.90 (n/a)</td><td>147.90 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>167.70 (n/a)</td><td>151.58 (n/a)</td><td>148.90 (n/a)</td><td>136.20 (n/a)</td><td>13.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.90 (n/a)</td><td>169.54 (n/a)</td><td>166.20 (n/a)</td><td>112.20 (n/a)</td><td>42.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>138.46 (n/a)</td><td>125.70 (n/a)</td><td>112.10 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.20 (n/a)</td><td>191.08 (n/a)</td><td>197.10 (n/a)</td><td>134.30 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>177.22 (n/a)</td><td>187.50 (n/a)</td><td>139.40 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.70 (n/a)</td><td>193.28 (n/a)</td><td>207.00 (n/a)</td><td>142.60 (n/a)</td><td>46.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>221.00 (n/a)</td><td>181.40 (n/a)</td><td>188.90 (n/a)</td><td>118.00 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>283.80 (n/a)</td><td>221.06 (n/a)</td><td>210.10 (n/a)</td><td>169.80 (n/a)</td><td>52.37 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>186.00 (n/a)</td><td>183.60 (n/a)</td><td>162.20 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.20 (n/a)</td><td>165.40 (n/a)</td><td>170.30 (n/a)</td><td>133.10 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.10 (n/a)</td><td>184.88 (n/a)</td><td>178.40 (n/a)</td><td>157.90 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.00 (n/a)</td><td>164.02 (n/a)</td><td>170.00 (n/a)</td><td>129.10 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>310.60 (n/a)</td><td>198.18 (n/a)</td><td>172.30 (n/a)</td><td>136.00 (n/a)</td><td>66.96 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.30 (n/a)</td><td>183.24 (n/a)</td><td>183.20 (n/a)</td><td>130.50 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>210.20 (n/a)</td><td>174.72 (n/a)</td><td>197.80 (n/a)</td><td>112.70 (n/a)</td><td>43.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>243.90 (n/a)</td><td>218.20 (n/a)</td><td>229.00 (n/a)</td><td>173.50 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-17.64%)</td><td>0.02 (-4.74%)</td><td>0.02 (+2.24%)</td><td>0.01 (-14.97%)</td><td>0.00 (-17.22%)</td><td>289.90 (+17.61%)</td><td>202.34 (+5.00%)</td><td>178.70 (-2.19%)</td><td>161.90 <b>(+21.36%)</b></td><td>52.29 <b>(+20.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.50 (n/a)</td><td>192.70 (n/a)</td><td>182.70 (n/a)</td><td>133.40 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-14.86%)</td><td>0.03 (+0.05%)</td><td>0.02 (+3.72%)</td><td>0.02 (-0.11%)</td><td>0.01 <b>(-24.98%)</b></td><td>199.00 (+0.15%)</td><td>162.76 (-1.36%)</td><td>165.90 (-3.55%)</td><td>126.40 (+17.36%)</td><td>31.69 (-7.45%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>165.00 (n/a)</td><td>172.00 (n/a)</td><td>107.70 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(+21.86%)</b></td><td>0.03 (+14.74%)</td><td>0.02 (+0.70%)</td><td>0.02 (+15.04%)</td><td>0.01 <b>(+31.30%)</b></td><td>199.70 (-13.06%)</td><td>165.96 (-12.44%)</td><td>178.80 (-0.72%)</td><td>120.10 (-17.96%)</td><td>30.70 (-9.75%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.70 (n/a)</td><td>189.54 (n/a)</td><td>180.10 (n/a)</td><td>146.40 (n/a)</td><td>34.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(+48.49%)</b></td><td>0.03 <b>(+24.11%)</b></td><td>0.03 (+19.99%)</td><td>0.02 (+16.02%)</td><td>0.01 <b>(+189.59%)</b></td><td>193.30 (-13.82%)</td><td>162.84 (-17.54%)</td><td>162.40 (-16.68%)</td><td>120.80 <b>(-32.63%)</b></td><td>29.68 <b>(+68.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.30 (n/a)</td><td>197.48 (n/a)</td><td>194.90 (n/a)</td><td>179.30 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (+9.94%)</td><td>0.03 (+6.24%)</td><td>0.03 (+5.46%)</td><td>0.02 (-8.08%)</td><td>0.01 <b>(+66.43%)</b></td><td>202.50 (+8.81%)</td><td>158.66 (-2.45%)</td><td>154.00 (-5.17%)</td><td>113.60 (-8.97%)</td><td>41.33 <b>(+69.98%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>162.64 (n/a)</td><td>162.40 (n/a)</td><td>124.80 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-25.74%)</b></td><td>0.02 (-15.60%)</td><td>0.02 (+9.67%)</td><td>0.01 (-19.25%)</td><td>0.01 <b>(-27.00%)</b></td><td>301.70 <b>(+23.85%)</b></td><td>216.20 (+17.64%)</td><td>175.30 (-8.79%)</td><td>160.20 <b>(+34.74%)</b></td><td>65.74 <b>(+22.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.60 (n/a)</td><td>183.78 (n/a)</td><td>192.20 (n/a)</td><td>118.90 (n/a)</td><td>53.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+8.12%)</td><td>0.02 (+3.72%)</td><td>0.02 (+9.53%)</td><td>0.02 (-0.15%)</td><td>0.00 (+18.98%)</td><td>215.30 (+0.14%)</td><td>171.22 (-2.93%)</td><td>168.90 (-8.70%)</td><td>127.00 (-7.50%)</td><td>32.36 (+10.11%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>176.38 (n/a)</td><td>185.00 (n/a)</td><td>137.30 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-11.32%)</td><td>0.02 (-4.81%)</td><td>0.02 (+1.85%)</td><td>0.02 (-5.68%)</td><td>0.00 <b>(-34.43%)</b></td><td>261.70 (+6.04%)</td><td>225.62 (+4.37%)</td><td>217.20 (-1.81%)</td><td>206.60 (+12.77%)</td><td>22.11 <b>(-20.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.80 (n/a)</td><td>216.18 (n/a)</td><td>221.20 (n/a)</td><td>183.20 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (+5.51%)</td><td>0.06 (+16.82%)</td><td>0.06 (+13.86%)</td><td>0.05 <b>(+34.37%)</b></td><td>0.00 <b>(-43.65%)</b></td><td>152.20 <b>(-25.57%)</b></td><td>137.68 (-15.91%)</td><td>135.80 (-12.16%)</td><td>125.60 (-5.21%)</td><td>11.20 <b>(-60.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>163.72 (n/a)</td><td>154.60 (n/a)</td><td>132.50 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-9.00%)</td><td>0.04 (-9.95%)</td><td>0.04 (-6.05%)</td><td>0.04 (-2.93%)</td><td>0.01 (-17.20%)</td><td>218.90 (+3.01%)</td><td>191.42 (+10.48%)</td><td>191.60 (+6.44%)</td><td>148.60 (+9.91%)</td><td>26.62 (-7.66%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>173.26 (n/a)</td><td>180.00 (n/a)</td><td>135.20 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(+24.10%)</b></td><td>0.05 (+0.21%)</td><td>0.04 (-9.90%)</td><td>0.04 (-0.67%)</td><td>0.01 <b>(+116.11%)</b></td><td>200.50 (+0.65%)</td><td>176.22 (+2.44%)</td><td>193.30 (+10.96%)</td><td>120.50 (-19.40%)</td><td>33.19 <b>(+73.37%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>172.02 (n/a)</td><td>174.20 (n/a)</td><td>149.50 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 <b>(-23.39%)</b></td><td>0.05 (-16.04%)</td><td>0.05 (-7.50%)</td><td>0.04 <b>(-21.71%)</b></td><td>0.00 <b>(-23.21%)</b></td><td>199.60 <b>(+27.70%)</b></td><td>175.00 (+19.10%)</td><td>164.40 (+8.16%)</td><td>160.10 <b>(+30.48%)</b></td><td>17.82 <b>(+29.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>156.30 (n/a)</td><td>146.94 (n/a)</td><td>152.00 (n/a)</td><td>122.70 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-5.42%)</td><td>0.05 (-6.93%)</td><td>0.04 (-9.89%)</td><td>0.04 (-5.87%)</td><td>0.01 (+9.01%)</td><td>225.80 (+6.26%)</td><td>182.44 (+8.09%)</td><td>183.30 (+10.96%)</td><td>145.60 (+5.74%)</td><td>32.45 (+19.03%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>168.78 (n/a)</td><td>165.20 (n/a)</td><td>137.70 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (-3.74%)</td><td>0.05 (-9.95%)</td><td>0.05 (-6.85%)</td><td>0.02 <b>(-43.11%)</b></td><td>0.02 <b>(+22.84%)</b></td><td>387.40 <b>(+75.77%)</b></td><td>209.70 <b>(+21.78%)</b></td><td>174.00 (+7.34%)</td><td>121.50 (+3.93%)</td><td>104.55 <b>(+125.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>172.20 (n/a)</td><td>162.10 (n/a)</td><td>116.90 (n/a)</td><td>46.36 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (+7.13%)</td><td>0.05 (+0.94%)</td><td>0.05 (-4.31%)</td><td>0.04 (+5.92%)</td><td>0.01 (-15.10%)</td><td>203.60 (-5.61%)</td><td>170.72 (-2.02%)</td><td>168.10 (+4.54%)</td><td>134.10 (-6.62%)</td><td>25.11 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>174.24 (n/a)</td><td>160.80 (n/a)</td><td>143.60 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+14.04%)</td><td>0.05 (+7.12%)</td><td>0.05 (+11.04%)</td><td>0.03 (-11.77%)</td><td>0.01 <b>(+105.47%)</b></td><td>247.60 (+13.32%)</td><td>186.50 (-4.32%)</td><td>173.50 (-9.92%)</td><td>151.60 (-12.32%)</td><td>39.58 <b>(+102.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>194.92 (n/a)</td><td>192.60 (n/a)</td><td>172.90 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+0.20%)</td><td>0.04 (+3.63%)</td><td>0.04 (+3.40%)</td><td>0.04 (+14.27%)</td><td>0.00 <b>(-33.30%)</b></td><td>211.60 (-12.49%)</td><td>186.26 (-4.41%)</td><td>185.30 (-3.29%)</td><td>170.00 (-0.18%)</td><td>16.52 <b>(-42.17%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>194.86 (n/a)</td><td>191.60 (n/a)</td><td>170.30 (n/a)</td><td>28.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+14.32%)</td><td>0.04 <b>(+21.95%)</b></td><td>0.04 (+15.28%)</td><td>0.04 <b>(+51.63%)</b></td><td>0.00 <b>(-38.68%)</b></td><td>215.90 <b>(-34.06%)</b></td><td>195.20 <b>(-20.02%)</b></td><td>193.10 (-13.29%)</td><td>170.70 (-12.51%)</td><td>17.93 <b>(-65.30%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>327.40 (n/a)</td><td>244.06 (n/a)</td><td>222.70 (n/a)</td><td>195.10 (n/a)</td><td>51.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (-11.68%)</td><td>0.10 (+6.43%)</td><td>0.10 (+19.89%)</td><td>0.08 (+9.92%)</td><td>0.01 <b>(-49.58%)</b></td><td>195.10 (-9.00%)</td><td>168.88 (-7.94%)</td><td>164.30 (-16.60%)</td><td>153.50 (+13.20%)</td><td>16.80 <b>(-47.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>183.44 (n/a)</td><td>197.00 (n/a)</td><td>135.60 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (+11.36%)</td><td>0.10 (-9.24%)</td><td>0.10 (-17.43%)</td><td>0.08 (-0.56%)</td><td>0.02 <b>(+30.44%)</b></td><td>199.70 (+0.55%)</td><td>164.98 (+11.58%)</td><td>164.40 <b>(+21.15%)</b></td><td>120.10 (-10.24%)</td><td>33.89 (+19.39%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.60 (n/a)</td><td>147.86 (n/a)</td><td>135.70 (n/a)</td><td>133.80 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (-2.82%)</td><td>0.09 (-5.53%)</td><td>0.09 (-13.53%)</td><td>0.09 (+10.47%)</td><td>0.01 <b>(-34.69%)</b></td><td>192.50 (-9.45%)</td><td>175.90 (+3.28%)</td><td>186.90 (+15.66%)</td><td>136.90 (+2.93%)</td><td>23.38 <b>(-39.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>170.32 (n/a)</td><td>161.60 (n/a)</td><td>133.00 (n/a)</td><td>38.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (+12.96%)</td><td>0.10 (+10.05%)</td><td>0.10 (+18.63%)</td><td>0.07 (-18.55%)</td><td>0.03 <b>(+104.14%)</b></td><td>235.10 <b>(+22.77%)</b></td><td>169.86 (-4.36%)</td><td>157.30 (-15.70%)</td><td>122.20 (-11.45%)</td><td>49.60 <b>(+122.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>177.60 (n/a)</td><td>186.60 (n/a)</td><td>138.00 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (+15.12%)</td><td>0.12 <b>(+22.74%)</b></td><td>0.13 (+16.23%)</td><td>0.08 <b>(+63.83%)</b></td><td>0.02 (-17.22%)</td><td>206.20 <b>(-38.96%)</b></td><td>144.42 <b>(-24.00%)</b></td><td>128.10 (-13.97%)</td><td>119.50 (-13.15%)</td><td>36.21 <b>(-57.06%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>337.80 (n/a)</td><td>190.02 (n/a)</td><td>148.90 (n/a)</td><td>137.60 (n/a)</td><td>84.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (-15.10%)</td><td>0.09 (-5.50%)</td><td>0.10 (+3.97%)</td><td>0.05 (-12.20%)</td><td>0.02 (-2.14%)</td><td>304.30 (+13.88%)</td><td>198.24 (+7.10%)</td><td>162.80 (-3.78%)</td><td>158.50 (+17.84%)</td><td>62.66 <b>(+24.96%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>267.20 (n/a)</td><td>185.10 (n/a)</td><td>169.20 (n/a)</td><td>134.50 (n/a)</td><td>50.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (+7.25%)</td><td>0.10 (-7.18%)</td><td>0.10 (-10.69%)</td><td>0.08 (-12.80%)</td><td>0.02 <b>(+44.57%)</b></td><td>208.80 (+14.66%)</td><td>166.38 (+9.37%)</td><td>163.70 (+11.97%)</td><td>125.90 (-6.81%)</td><td>30.66 <b>(+55.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>152.12 (n/a)</td><td>146.20 (n/a)</td><td>135.10 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (+8.20%)</td><td>0.08 (-6.80%)</td><td>0.07 (-17.66%)</td><td>0.05 (-0.17%)</td><td>0.02 (+17.06%)</td><td>308.70 (+0.19%)</td><td>225.20 (+8.10%)</td><td>227.60 <b>(+21.45%)</b></td><td>145.50 (-7.56%)</td><td>58.33 (+0.11%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>308.10 (n/a)</td><td>208.32 (n/a)</td><td>187.40 (n/a)</td><td>157.40 (n/a)</td><td>58.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (+3.03%)</td><td>0.20 (+11.66%)</td><td>0.19 (+8.68%)</td><td>0.18 <b>(+47.21%)</b></td><td>0.03 <b>(-33.13%)</b></td><td>180.30 <b>(-32.09%)</b></td><td>163.54 (-13.54%)</td><td>173.10 (-7.97%)</td><td>129.30 (-2.93%)</td><td>21.27 <b>(-56.50%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>265.50 (n/a)</td><td>189.16 (n/a)</td><td>188.10 (n/a)</td><td>133.20 (n/a)</td><td>48.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (-7.24%)</td><td>0.22 (-3.02%)</td><td>0.22 (+2.12%)</td><td>0.19 (-4.17%)</td><td>0.03 (-11.52%)</td><td>176.20 (+4.38%)</td><td>150.84 (+2.95%)</td><td>150.30 (-2.08%)</td><td>127.80 (+7.76%)</td><td>19.24 (+0.99%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.80 (n/a)</td><td>146.52 (n/a)</td><td>153.50 (n/a)</td><td>118.60 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+6.93%)</td><td>0.21 (-2.33%)</td><td>0.20 (-8.22%)</td><td>0.19 (-8.12%)</td><td>0.03 <b>(+64.03%)</b></td><td>176.80 (+8.80%)</td><td>155.44 (+3.59%)</td><td>166.90 (+8.94%)</td><td>121.70 (-6.46%)</td><td>22.28 <b>(+64.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>162.50 (n/a)</td><td>150.06 (n/a)</td><td>153.20 (n/a)</td><td>130.10 (n/a)</td><td>13.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (+11.50%)</td><td>0.20 (-8.58%)</td><td>0.17 (-17.30%)</td><td>0.14 <b>(-28.91%)</b></td><td>0.06 <b>(+119.85%)</b></td><td>236.60 <b>(+40.67%)</b></td><td>175.28 (+16.22%)</td><td>189.30 <b>(+20.96%)</b></td><td>109.60 (-10.31%)</td><td>49.64 <b>(+176.03%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>168.20 (n/a)</td><td>150.82 (n/a)</td><td>156.50 (n/a)</td><td>122.20 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 (-0.14%)</td><td>0.16 <b>(-20.88%)</b></td><td>0.15 <b>(-31.20%)</b></td><td>0.14 (-19.23%)</td><td>0.03 <b>(+67.39%)</b></td><td>241.40 <b>(+23.79%)</b></td><td>211.66 <b>(+29.12%)</b></td><td>224.70 <b>(+45.34%)</b></td><td>149.50 (+0.13%)</td><td>37.28 <b>(+101.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>163.92 (n/a)</td><td>154.60 (n/a)</td><td>149.30 (n/a)</td><td>18.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 <b>(-26.89%)</b></td><td>0.18 (-6.76%)</td><td>0.18 (-3.02%)</td><td>0.14 <b>(+23.67%)</b></td><td>0.02 <b>(-61.81%)</b></td><td>231.90 (-19.14%)</td><td>189.30 (+1.29%)</td><td>181.50 (+3.12%)</td><td>173.90 <b>(+36.82%)</b></td><td>24.24 <b>(-59.26%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>286.80 (n/a)</td><td>186.88 (n/a)</td><td>176.00 (n/a)</td><td>127.10 (n/a)</td><td>59.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (-7.21%)</td><td>0.15 (+1.51%)</td><td>0.16 (+6.11%)</td><td>0.14 (-0.70%)</td><td>0.01 <b>(-34.38%)</b></td><td>233.60 (+0.69%)</td><td>215.44 (-1.72%)</td><td>209.00 (-5.73%)</td><td>207.40 (+7.74%)</td><td>11.37 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>219.20 (n/a)</td><td>221.70 (n/a)</td><td>192.50 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-32.11%)</b></td><td>0.02 (-2.10%)</td><td>0.03 (+5.91%)</td><td>0.02 <b>(+26.17%)</b></td><td>0.00 <b>(-78.97%)</b></td><td>188.50 <b>(-20.73%)</b></td><td>166.16 (-6.61%)</td><td>163.60 (-5.60%)</td><td>151.20 <b>(+47.37%)</b></td><td>13.76 <b>(-75.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>177.92 (n/a)</td><td>173.30 (n/a)</td><td>102.60 (n/a)</td><td>56.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-21.56%)</b></td><td>0.03 (-2.75%)</td><td>0.03 (+11.49%)</td><td>0.02 (+6.67%)</td><td>0.00 <b>(-48.26%)</b></td><td>192.70 (-6.23%)</td><td>160.94 (-1.11%)</td><td>156.90 (-10.29%)</td><td>133.90 <b>(+27.52%)</b></td><td>25.32 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>162.74 (n/a)</td><td>174.90 (n/a)</td><td>105.00 (n/a)</td><td>40.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-5.79%)</td><td>0.02 (+7.96%)</td><td>0.02 (+19.33%)</td><td>0.02 (+14.44%)</td><td>0.00 <b>(-49.70%)</b></td><td>213.40 (-12.61%)</td><td>190.24 (-9.47%)</td><td>190.80 (-16.21%)</td><td>164.30 (+6.14%)</td><td>17.45 <b>(-54.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.20 (n/a)</td><td>210.14 (n/a)</td><td>227.70 (n/a)</td><td>154.80 (n/a)</td><td>38.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (+6.85%)</td><td>0.02 (+10.21%)</td><td>0.02 (+10.58%)</td><td>0.02 (+15.23%)</td><td>0.00 <b>(-30.51%)</b></td><td>201.90 (-13.24%)</td><td>189.06 (-9.70%)</td><td>194.40 (-9.58%)</td><td>173.50 (-6.42%)</td><td>11.63 <b>(-43.26%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>209.38 (n/a)</td><td>215.00 (n/a)</td><td>185.40 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+1.62%)</td><td>0.02 (+8.21%)</td><td>0.03 <b>(+31.23%)</b></td><td>0.01 <b>(-27.88%)</b></td><td>0.01 <b>(+48.22%)</b></td><td>352.50 <b>(+38.67%)</b></td><td>202.22 (-1.12%)</td><td>161.70 <b>(-23.80%)</b></td><td>147.90 (-1.60%)</td><td>85.39 <b>(+114.73%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.20 (n/a)</td><td>204.52 (n/a)</td><td>212.20 (n/a)</td><td>150.30 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-19.12%)</td><td>0.03 (-10.28%)</td><td>0.02 (-5.56%)</td><td>0.02 (-1.77%)</td><td>0.01 <b>(-31.92%)</b></td><td>233.00 (+1.79%)</td><td>169.34 (+8.20%)</td><td>170.20 (+5.85%)</td><td>131.60 <b>(+23.68%)</b></td><td>41.12 (-14.87%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>156.50 (n/a)</td><td>160.80 (n/a)</td><td>106.40 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-8.34%)</td><td>0.03 (-11.13%)</td><td>0.03 (-14.65%)</td><td>0.02 <b>(-20.99%)</b></td><td>0.00 (+5.03%)</td><td>226.80 <b>(+26.56%)</b></td><td>168.32 (+13.62%)</td><td>159.20 (+17.14%)</td><td>138.90 (+9.11%)</td><td>33.82 <b>(+51.33%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.20 (n/a)</td><td>148.14 (n/a)</td><td>135.90 (n/a)</td><td>127.30 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+14.18%)</td><td>0.03 (+6.00%)</td><td>0.03 (+9.34%)</td><td>0.02 (-5.87%)</td><td>0.00 <b>(+212.05%)</b></td><td>173.90 (+6.23%)</td><td>146.80 (-4.60%)</td><td>138.30 (-8.59%)</td><td>128.50 (-12.47%)</td><td>18.89 <b>(+190.68%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>163.70 (n/a)</td><td>153.88 (n/a)</td><td>151.30 (n/a)</td><td>146.80 (n/a)</td><td>6.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-7.21%)</td><td>0.03 (+16.13%)</td><td>0.03 (+19.14%)</td><td>0.02 <b>(+30.03%)</b></td><td>0.00 <b>(-40.41%)</b></td><td>164.40 <b>(-23.07%)</b></td><td>141.42 (-16.46%)</td><td>143.00 (-16.08%)</td><td>121.50 (+7.81%)</td><td>18.59 <b>(-48.82%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>169.28 (n/a)</td><td>170.40 (n/a)</td><td>112.70 (n/a)</td><td>36.32 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(-35.14%)</b></td><td>0.02 (-19.92%)</td><td>0.02 (-6.35%)</td><td>0.02 (-0.41%)</td><td>0.00 <b>(-82.11%)</b></td><td>184.40 (+0.44%)</td><td>168.80 (+18.67%)</td><td>164.70 (+6.81%)</td><td>158.90 <b>(+54.12%)</b></td><td>10.30 <b>(-71.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>142.24 (n/a)</td><td>154.20 (n/a)</td><td>103.10 (n/a)</td><td>35.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-19.92%)</td><td>0.02 (-16.68%)</td><td>0.03 (-13.73%)</td><td>0.02 (-15.99%)</td><td>0.00 (-18.12%)</td><td>227.60 (+19.04%)</td><td>171.96 (+19.93%)</td><td>152.60 (+15.87%)</td><td>142.90 <b>(+24.91%)</b></td><td>35.92 (+18.95%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>143.38 (n/a)</td><td>131.70 (n/a)</td><td>114.40 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+6.91%)</td><td>0.03 (+5.90%)</td><td>0.03 (+9.87%)</td><td>0.02 (-4.62%)</td><td>0.00 <b>(+61.13%)</b></td><td>179.00 (+4.86%)</td><td>147.74 (-4.82%)</td><td>143.10 (-8.97%)</td><td>128.20 (-6.49%)</td><td>19.50 <b>(+62.19%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.70 (n/a)</td><td>155.22 (n/a)</td><td>157.20 (n/a)</td><td>137.10 (n/a)</td><td>12.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-18.48%)</td><td>0.02 (-10.23%)</td><td>0.02 (-9.31%)</td><td>0.02 (-10.63%)</td><td>0.00 <b>(-29.94%)</b></td><td>250.40 (+11.94%)</td><td>206.96 (+10.60%)</td><td>211.40 (+10.28%)</td><td>176.40 <b>(+22.67%)</b></td><td>29.25 (-3.05%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.70 (n/a)</td><td>187.12 (n/a)</td><td>191.70 (n/a)</td><td>143.80 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-6.63%)</td><td>0.03 (+5.59%)</td><td>0.03 (+8.54%)</td><td>0.02 (-5.40%)</td><td>0.01 (-11.39%)</td><td>230.20 (+5.74%)</td><td>157.28 (-5.64%)</td><td>141.10 (-7.84%)</td><td>131.20 (+7.10%)</td><td>41.04 (+2.56%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>166.68 (n/a)</td><td>153.10 (n/a)</td><td>122.50 (n/a)</td><td>40.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-13.72%)</td><td>0.02 (-9.09%)</td><td>0.02 (-1.77%)</td><td>0.02 (-19.31%)</td><td>0.00 (+11.77%)</td><td>252.10 <b>(+23.94%)</b></td><td>188.46 (+11.42%)</td><td>174.20 (+1.81%)</td><td>159.70 (+15.98%)</td><td>38.19 <b>(+61.42%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>169.14 (n/a)</td><td>171.10 (n/a)</td><td>137.70 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-15.68%)</td><td>0.02 (-1.07%)</td><td>0.02 (+4.87%)</td><td>0.02 (-0.97%)</td><td>0.00 <b>(-43.75%)</b></td><td>198.60 (+0.97%)</td><td>168.84 (-0.02%)</td><td>164.20 (-4.65%)</td><td>154.70 (+18.54%)</td><td>17.12 <b>(-28.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.70 (n/a)</td><td>168.88 (n/a)</td><td>172.20 (n/a)</td><td>130.50 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (-8.14%)</td><td>0.05 (+4.33%)</td><td>0.05 (+9.48%)</td><td>0.04 (+10.71%)</td><td>0.01 <b>(-21.92%)</b></td><td>188.00 (-9.66%)</td><td>157.44 (-5.50%)</td><td>152.30 (-8.64%)</td><td>125.20 (+8.87%)</td><td>28.11 (-19.17%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>166.60 (n/a)</td><td>166.70 (n/a)</td><td>115.00 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 <b>(-27.09%)</b></td><td>0.05 (-7.62%)</td><td>0.05 (-8.29%)</td><td>0.04 <b>(+34.59%)</b></td><td>0.01 <b>(-65.74%)</b></td><td>189.10 <b>(-25.73%)</b></td><td>170.36 (+1.30%)</td><td>173.70 (+9.04%)</td><td>149.40 <b>(+37.19%)</b></td><td>18.44 <b>(-65.88%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>254.60 (n/a)</td><td>168.18 (n/a)</td><td>159.30 (n/a)</td><td>108.90 (n/a)</td><td>54.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (-6.85%)</td><td>0.04 (+10.27%)</td><td>0.04 (+10.69%)</td><td>0.04 <b>(+47.09%)</b></td><td>0.01 <b>(-42.82%)</b></td><td>225.60 <b>(-32.01%)</b></td><td>191.04 (-13.77%)</td><td>192.30 (-9.63%)</td><td>159.60 (+7.33%)</td><td>27.23 <b>(-59.70%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.80 (n/a)</td><td>221.54 (n/a)</td><td>212.80 (n/a)</td><td>148.70 (n/a)</td><td>67.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (-16.30%)</td><td>0.04 (-3.76%)</td><td>0.05 (+7.86%)</td><td>0.04 (+5.57%)</td><td>0.00 <b>(-50.18%)</b></td><td>221.50 (-5.26%)</td><td>191.96 (+1.75%)</td><td>180.90 (-7.33%)</td><td>175.20 (+19.51%)</td><td>20.36 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>188.66 (n/a)</td><td>195.20 (n/a)</td><td>146.60 (n/a)</td><td>35.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 <b>(-26.91%)</b></td><td>0.04 <b>(-21.30%)</b></td><td>0.05 (-12.44%)</td><td>0.03 <b>(-25.43%)</b></td><td>0.01 (-18.09%)</td><td>265.40 <b>(+34.11%)</b></td><td>202.36 <b>(+28.08%)</b></td><td>177.60 (+14.21%)</td><td>159.80 <b>(+36.82%)</b></td><td>44.81 <b>(+54.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>158.00 (n/a)</td><td>155.50 (n/a)</td><td>116.80 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 <b>(-24.13%)</b></td><td>0.05 (+7.86%)</td><td>0.05 (+7.77%)</td><td>0.05 <b>(+109.87%)</b></td><td>0.01 <b>(-66.25%)</b></td><td>178.50 <b>(-52.35%)</b></td><td>154.90 <b>(-21.47%)</b></td><td>153.80 (-7.24%)</td><td>131.80 <b>(+31.80%)</b></td><td>20.99 <b>(-79.90%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>374.60 (n/a)</td><td>197.26 (n/a)</td><td>165.80 (n/a)</td><td>100.00 (n/a)</td><td>104.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 <b>(-38.89%)</b></td><td>0.05 (-14.60%)</td><td>0.05 (-7.83%)</td><td>0.05 (+11.99%)</td><td>0.00 <b>(-94.76%)</b></td><td>181.30 (-10.69%)</td><td>178.98 (+11.42%)</td><td>180.20 (+8.49%)</td><td>174.30 <b>(+63.66%)</b></td><td>2.90 <b>(-92.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>160.64 (n/a)</td><td>166.10 (n/a)</td><td>106.50 (n/a)</td><td>37.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-3.56%)</td><td>0.04 (-4.23%)</td><td>0.05 (-5.06%)</td><td>0.02 (-4.24%)</td><td>0.01 (-5.26%)</td><td>370.30 (+4.46%)</td><td>209.60 (+4.29%)</td><td>180.50 (+5.37%)</td><td>142.80 (+3.70%)</td><td>91.69 (+4.18%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>354.50 (n/a)</td><td>200.98 (n/a)</td><td>171.30 (n/a)</td><td>137.70 (n/a)</td><td>88.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-2.11%)</td><td>0.05 (+7.45%)</td><td>0.05 (+12.24%)</td><td>0.04 (+11.99%)</td><td>0.01 <b>(-34.35%)</b></td><td>191.10 (-10.74%)</td><td>164.70 (-8.57%)</td><td>167.20 (-10.92%)</td><td>144.10 (+2.13%)</td><td>19.62 <b>(-41.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>180.14 (n/a)</td><td>187.70 (n/a)</td><td>141.10 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (+1.71%)</td><td>0.05 (-2.64%)</td><td>0.05 (+7.04%)</td><td>0.03 (-18.86%)</td><td>0.01 (+15.48%)</td><td>253.10 <b>(+23.22%)</b></td><td>175.24 (+4.72%)</td><td>163.10 (-6.53%)</td><td>132.60 (-1.70%)</td><td>46.27 <b>(+50.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>167.34 (n/a)</td><td>174.50 (n/a)</td><td>134.90 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-11.29%)</td><td>0.05 (-2.23%)</td><td>0.05 (-13.45%)</td><td>0.04 (+18.38%)</td><td>0.01 <b>(-44.26%)</b></td><td>196.80 (-15.50%)</td><td>167.04 (-1.60%)</td><td>174.50 (+15.56%)</td><td>141.80 (+12.72%)</td><td>23.55 <b>(-48.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>169.76 (n/a)</td><td>151.00 (n/a)</td><td>125.80 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(+31.91%)</b></td><td>0.05 (+15.00%)</td><td>0.05 (+18.01%)</td><td>0.04 (-0.48%)</td><td>0.01 <b>(+109.32%)</b></td><td>217.80 (+0.51%)</td><td>163.94 (-10.70%)</td><td>155.80 (-15.28%)</td><td>122.20 <b>(-24.19%)</b></td><td>36.37 <b>(+62.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>183.58 (n/a)</td><td>183.90 (n/a)</td><td>161.20 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-0.55%)</td><td>0.05 (+1.10%)</td><td>0.05 (+6.27%)</td><td>0.03 <b>(-24.97%)</b></td><td>0.01 <b>(+27.96%)</b></td><td>321.40 <b>(+33.25%)</b></td><td>191.08 (+4.21%)</td><td>171.40 (-5.93%)</td><td>130.60 (+0.54%)</td><td>74.81 <b>(+87.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>183.36 (n/a)</td><td>182.20 (n/a)</td><td>129.90 (n/a)</td><td>39.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (-1.32%)</td><td>0.05 (+15.78%)</td><td>0.05 <b>(+22.92%)</b></td><td>0.05 <b>(+49.23%)</b></td><td>0.00 <b>(-76.94%)</b></td><td>167.30 <b>(-33.00%)</b></td><td>158.48 (-16.53%)</td><td>156.60 (-18.65%)</td><td>150.60 (+1.28%)</td><td>6.53 <b>(-83.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.70 (n/a)</td><td>189.86 (n/a)</td><td>192.50 (n/a)</td><td>148.70 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+12.24%)</td><td>0.05 (+18.55%)</td><td>0.05 (+9.94%)</td><td>0.04 <b>(+86.40%)</b></td><td>0.00 <b>(-56.97%)</b></td><td>191.00 <b>(-46.35%)</b></td><td>170.52 <b>(-21.19%)</b></td><td>169.60 (-9.01%)</td><td>152.30 (-10.88%)</td><td>15.52 <b>(-80.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>356.00 (n/a)</td><td>216.36 (n/a)</td><td>186.40 (n/a)</td><td>170.90 (n/a)</td><td>78.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 <b>(+20.55%)</b></td><td>0.05 (+15.45%)</td><td>0.05 (+6.56%)</td><td>0.04 (+13.88%)</td><td>0.01 <b>(+53.78%)</b></td><td>191.60 (-12.19%)</td><td>161.80 (-12.51%)</td><td>168.20 (-6.14%)</td><td>131.00 (-17.04%)</td><td>27.76 (+10.01%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>184.94 (n/a)</td><td>179.20 (n/a)</td><td>157.90 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 <b>(+21.75%)</b></td><td>0.11 (+15.89%)</td><td>0.12 (+19.08%)</td><td>0.08 (-3.61%)</td><td>0.02 <b>(+84.64%)</b></td><td>198.70 (+3.71%)</td><td>150.42 (-11.97%)</td><td>140.70 (-16.00%)</td><td>120.40 (-17.87%)</td><td>31.04 <b>(+55.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>170.88 (n/a)</td><td>167.50 (n/a)</td><td>146.60 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (-17.31%)</td><td>0.11 (-17.63%)</td><td>0.11 (-18.18%)</td><td>0.08 (-18.35%)</td><td>0.02 (-8.18%)</td><td>208.00 <b>(+22.50%)</b></td><td>157.28 <b>(+22.00%)</b></td><td>150.50 <b>(+22.26%)</b></td><td>130.80 <b>(+21.00%)</b></td><td>31.16 <b>(+31.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.80 (n/a)</td><td>128.92 (n/a)</td><td>123.10 (n/a)</td><td>108.10 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (+14.84%)</td><td>0.09 (+19.95%)</td><td>0.09 (+18.92%)</td><td>0.08 <b>(+49.46%)</b></td><td>0.01 <b>(-29.88%)</b></td><td>216.20 <b>(-33.09%)</b></td><td>186.58 (-19.05%)</td><td>179.40 (-15.93%)</td><td>161.20 (-12.96%)</td><td>23.42 <b>(-58.64%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>323.10 (n/a)</td><td>230.48 (n/a)</td><td>213.40 (n/a)</td><td>185.20 (n/a)</td><td>56.61 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 <b>(+21.80%)</b></td><td>0.09 (+10.11%)</td><td>0.09 (+1.44%)</td><td>0.05 (-3.80%)</td><td>0.03 <b>(+40.37%)</b></td><td>328.50 (+3.96%)</td><td>201.74 (-5.79%)</td><td>176.40 (-1.45%)</td><td>139.90 (-17.90%)</td><td>76.11 <b>(+23.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>316.00 (n/a)</td><td>214.14 (n/a)</td><td>179.00 (n/a)</td><td>170.40 (n/a)</td><td>61.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+16.46%)</td><td>0.11 (-4.17%)</td><td>0.09 <b>(-22.94%)</b></td><td>0.08 (+9.74%)</td><td>0.03 <b>(+39.69%)</b></td><td>209.90 (-8.90%)</td><td>165.64 (+6.40%)</td><td>183.10 <b>(+29.77%)</b></td><td>110.30 (-14.10%)</td><td>43.93 (+4.37%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>155.68 (n/a)</td><td>141.10 (n/a)</td><td>128.40 (n/a)</td><td>42.09 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (+5.06%)</td><td>0.10 (-8.70%)</td><td>0.10 (-7.51%)</td><td>0.07 <b>(-29.19%)</b></td><td>0.02 <b>(+96.48%)</b></td><td>245.80 <b>(+41.18%)</b></td><td>174.20 (+14.36%)</td><td>164.70 (+8.07%)</td><td>124.10 (-4.76%)</td><td>46.89 <b>(+166.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.10 (n/a)</td><td>152.32 (n/a)</td><td>152.40 (n/a)</td><td>130.30 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 <b>(+24.72%)</b></td><td>0.10 (+7.99%)</td><td>0.10 (+9.17%)</td><td>0.08 (-3.57%)</td><td>0.02 <b>(+113.46%)</b></td><td>215.60 (+3.70%)</td><td>171.18 (-4.53%)</td><td>162.90 (-8.38%)</td><td>122.10 (-19.78%)</td><td>37.82 <b>(+80.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>179.30 (n/a)</td><td>177.80 (n/a)</td><td>152.20 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+13.69%)</td><td>0.12 (+6.64%)</td><td>0.13 (+12.80%)</td><td>0.09 (-8.46%)</td><td>0.02 <b>(+39.59%)</b></td><td>185.50 (+9.25%)</td><td>137.84 (-4.82%)</td><td>130.30 (-11.36%)</td><td>109.00 (-12.03%)</td><td>28.83 <b>(+41.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.80 (n/a)</td><td>144.82 (n/a)</td><td>147.00 (n/a)</td><td>123.90 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (-10.52%)</td><td>0.12 (+13.94%)</td><td>0.13 <b>(+30.65%)</b></td><td>0.11 <b>(+39.32%)</b></td><td>0.01 <b>(-54.60%)</b></td><td>155.90 <b>(-28.22%)</b></td><td>133.52 (-16.78%)</td><td>129.90 <b>(-23.45%)</b></td><td>118.00 (+11.74%)</td><td>16.08 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>217.20 (n/a)</td><td>160.44 (n/a)</td><td>169.70 (n/a)</td><td>105.60 (n/a)</td><td>43.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (+15.17%)</td><td>0.11 (+10.42%)</td><td>0.12 <b>(+22.18%)</b></td><td>0.09 (+0.57%)</td><td>0.02 <b>(+39.46%)</b></td><td>185.70 (-0.59%)</td><td>148.86 (-8.44%)</td><td>141.40 (-18.12%)</td><td>113.60 (-13.15%)</td><td>26.92 <b>(+21.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>162.58 (n/a)</td><td>172.70 (n/a)</td><td>130.80 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 <b>(+42.91%)</b></td><td>0.11 <b>(+29.11%)</b></td><td>0.11 <b>(+21.29%)</b></td><td>0.10 <b>(+30.63%)</b></td><td>0.01 <b>(+60.97%)</b></td><td>168.80 <b>(-23.45%)</b></td><td>150.98 <b>(-22.26%)</b></td><td>148.50 (-17.55%)</td><td>125.00 <b>(-30.01%)</b></td><td>18.26 (-11.63%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>194.22 (n/a)</td><td>180.10 (n/a)</td><td>178.60 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (+4.61%)</td><td>0.12 (+17.29%)</td><td>0.12 (+13.22%)</td><td>0.09 <b>(+30.89%)</b></td><td>0.02 (-18.61%)</td><td>187.60 <b>(-23.58%)</b></td><td>143.94 (-16.79%)</td><td>142.10 (-11.68%)</td><td>118.40 (-4.44%)</td><td>26.46 <b>(-40.82%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.50 (n/a)</td><td>172.98 (n/a)</td><td>160.90 (n/a)</td><td>123.90 (n/a)</td><td>44.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (+6.16%)</td><td>0.11 (+17.43%)</td><td>0.10 <b>(+43.20%)</b></td><td>0.08 (+14.97%)</td><td>0.03 (-3.86%)</td><td>209.30 (-13.01%)</td><td>161.48 (-16.24%)</td><td>156.20 <b>(-30.17%)</b></td><td>118.20 (-5.74%)</td><td>40.84 <b>(-21.77%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.60 (n/a)</td><td>192.78 (n/a)</td><td>223.70 (n/a)</td><td>125.40 (n/a)</td><td>52.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (+18.48%)</td><td>0.09 <b>(+27.95%)</b></td><td>0.09 (+18.32%)</td><td>0.08 <b>(+74.79%)</b></td><td>0.01 <b>(-37.04%)</b></td><td>193.80 <b>(-42.80%)</b></td><td>177.84 <b>(-24.52%)</b></td><td>186.60 (-15.49%)</td><td>155.10 (-15.61%)</td><td>17.49 <b>(-70.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>338.80 (n/a)</td><td>235.60 (n/a)</td><td>220.80 (n/a)</td><td>183.80 (n/a)</td><td>60.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 <b>(+23.81%)</b></td><td>0.10 <b>(+20.85%)</b></td><td>0.10 <b>(+26.85%)</b></td><td>0.08 <b>(+27.72%)</b></td><td>0.01 (+2.05%)</td><td>205.50 <b>(-21.68%)</b></td><td>168.30 (-17.93%)</td><td>161.20 <b>(-21.17%)</b></td><td>137.20 (-19.25%)</td><td>25.09 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>262.40 (n/a)</td><td>205.06 (n/a)</td><td>204.50 (n/a)</td><td>169.90 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 <b>(+27.72%)</b></td><td>0.12 <b>(+48.27%)</b></td><td>0.13 <b>(+62.89%)</b></td><td>0.09 <b>(+58.82%)</b></td><td>0.02 (+6.18%)</td><td>187.60 <b>(-37.03%)</b></td><td>141.54 <b>(-34.00%)</b></td><td>129.80 <b>(-38.63%)</b></td><td>113.60 <b>(-21.71%)</b></td><td>29.27 <b>(-46.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>297.90 (n/a)</td><td>214.44 (n/a)</td><td>211.50 (n/a)</td><td>145.10 (n/a)</td><td>54.80 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (+15.51%)</td><td>0.19 (+11.60%)</td><td>0.18 (+13.27%)</td><td>0.16 (+11.81%)</td><td>0.04 <b>(+25.01%)</b></td><td>207.30 (-10.53%)</td><td>175.96 (-9.97%)</td><td>179.00 (-11.74%)</td><td>126.30 (-13.43%)</td><td>30.28 (-3.73%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.70 (n/a)</td><td>195.44 (n/a)</td><td>202.80 (n/a)</td><td>145.90 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (-3.12%)</td><td>0.22 (+11.91%)</td><td>0.22 <b>(+27.98%)</b></td><td>0.16 (+13.09%)</td><td>0.04 <b>(-22.44%)</b></td><td>201.50 (-11.58%)</td><td>154.04 (-12.62%)</td><td>148.30 <b>(-21.87%)</b></td><td>128.40 (+3.22%)</td><td>30.29 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>227.90 (n/a)</td><td>176.28 (n/a)</td><td>189.80 (n/a)</td><td>124.40 (n/a)</td><td>42.73 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (-2.41%)</td><td>0.15 (-1.46%)</td><td>0.14 (-2.90%)</td><td>0.11 (-19.75%)</td><td>0.03 <b>(+32.48%)</b></td><td>302.50 <b>(+24.59%)</b></td><td>228.18 (+3.58%)</td><td>236.20 (+3.01%)</td><td>174.00 (+2.47%)</td><td>49.88 <b>(+73.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>242.80 (n/a)</td><td>220.30 (n/a)</td><td>229.30 (n/a)</td><td>169.80 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 <b>(+24.93%)</b></td><td>0.19 (+18.60%)</td><td>0.19 (+19.76%)</td><td>0.15 (+3.84%)</td><td>0.03 <b>(+81.70%)</b></td><td>220.60 (-3.71%)</td><td>178.10 (-14.78%)</td><td>177.00 (-16.51%)</td><td>149.30 (-19.95%)</td><td>27.26 <b>(+41.03%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>208.98 (n/a)</td><td>212.00 (n/a)</td><td>186.50 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (-5.95%)</td><td>0.21 (-4.84%)</td><td>0.20 (-6.06%)</td><td>0.17 (-7.92%)</td><td>0.03 (-8.62%)</td><td>191.70 (+8.61%)</td><td>160.64 (+4.98%)</td><td>162.10 (+6.43%)</td><td>129.80 (+6.31%)</td><td>23.15 (+3.93%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.50 (n/a)</td><td>153.02 (n/a)</td><td>152.30 (n/a)</td><td>122.10 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (-4.89%)</td><td>0.21 (+11.47%)</td><td>0.22 <b>(+24.51%)</b></td><td>0.18 (+16.50%)</td><td>0.03 <b>(-35.89%)</b></td><td>183.50 (-14.13%)</td><td>155.00 (-12.68%)</td><td>149.80 (-19.72%)</td><td>128.70 (+5.15%)</td><td>22.25 <b>(-42.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.70 (n/a)</td><td>177.50 (n/a)</td><td>186.60 (n/a)</td><td>122.40 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (-8.67%)</td><td>0.21 (-2.73%)</td><td>0.21 (-4.87%)</td><td>0.18 (+17.04%)</td><td>0.03 <b>(-37.91%)</b></td><td>185.80 (-14.54%)</td><td>156.44 (+0.13%)</td><td>158.00 (+5.12%)</td><td>127.80 (+9.51%)</td><td>21.05 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>217.40 (n/a)</td><td>156.24 (n/a)</td><td>150.30 (n/a)</td><td>116.70 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (-4.61%)</td><td>0.21 (-2.05%)</td><td>0.19 (-2.89%)</td><td>0.17 (-1.96%)</td><td>0.03 (-16.13%)</td><td>190.30 (+1.98%)</td><td>162.20 (+1.40%)</td><td>170.90 (+3.01%)</td><td>128.80 (+4.80%)</td><td>24.30 (-12.54%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.60 (n/a)</td><td>159.96 (n/a)</td><td>165.90 (n/a)</td><td>122.90 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (+13.20%)</td><td>0.20 (+17.02%)</td><td>0.19 (+5.82%)</td><td>0.16 <b>(+49.67%)</b></td><td>0.04 (-8.45%)</td><td>199.10 <b>(-33.21%)</b></td><td>165.60 (-17.29%)</td><td>176.20 (-5.47%)</td><td>123.80 (-11.70%)</td><td>32.10 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>298.10 (n/a)</td><td>200.22 (n/a)</td><td>186.40 (n/a)</td><td>140.20 (n/a)</td><td>60.84 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.22 <b>(-20.83%)</b></td><td>0.20 (-12.07%)</td><td>0.20 (-6.71%)</td><td>0.18 (+0.95%)</td><td>0.02 <b>(-60.44%)</b></td><td>182.70 (-0.98%)</td><td>165.28 (+11.12%)</td><td>161.90 (+7.22%)</td><td>148.30 <b>(+26.32%)</b></td><td>14.26 <b>(-49.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.50 (n/a)</td><td>148.74 (n/a)</td><td>151.00 (n/a)</td><td>117.40 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 <b>(+23.40%)</b></td><td>0.21 (+6.58%)</td><td>0.21 (+11.50%)</td><td>0.15 (-17.37%)</td><td>0.05 <b>(+193.98%)</b></td><td>220.10 <b>(+21.07%)</b></td><td>163.80 (-2.10%)</td><td>154.70 (-10.32%)</td><td>119.60 (-18.92%)</td><td>40.76 <b>(+190.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>181.80 (n/a)</td><td>167.32 (n/a)</td><td>172.50 (n/a)</td><td>147.50 (n/a)</td><td>14.03 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 <b>(+39.37%)</b></td><td>0.23 <b>(+37.73%)</b></td><td>0.25 <b>(+33.20%)</b></td><td>0.15 <b>(+71.31%)</b></td><td>0.06 <b>(+30.09%)</b></td><td>216.70 <b>(-41.62%)</b></td><td>153.56 <b>(-29.47%)</b></td><td>130.00 <b>(-24.94%)</b></td><td>117.30 <b>(-28.26%)</b></td><td>45.39 <b>(-48.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>371.20 (n/a)</td><td>217.72 (n/a)</td><td>173.20 (n/a)</td><td>163.50 (n/a)</td><td>87.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 <b>(-22.99%)</b></td><td>0.17 (-10.14%)</td><td>0.18 (+9.74%)</td><td>0.14 (-10.94%)</td><td>0.02 <b>(-33.36%)</b></td><td>229.40 (+12.29%)</td><td>197.88 (+10.36%)</td><td>177.80 (-8.87%)</td><td>176.90 <b>(+29.88%)</b></td><td>28.10 (-3.54%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.30 (n/a)</td><td>179.30 (n/a)</td><td>195.10 (n/a)</td><td>136.20 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (-6.31%)</td><td>0.18 (-5.62%)</td><td>0.18 (-2.39%)</td><td>0.14 (-14.99%)</td><td>0.03 (+4.12%)</td><td>226.50 (+17.66%)</td><td>182.82 (+6.63%)</td><td>178.90 (+2.40%)</td><td>141.70 (+6.78%)</td><td>30.80 <b>(+33.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>171.46 (n/a)</td><td>174.70 (n/a)</td><td>132.70 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (+9.55%)</td><td>0.19 (+17.64%)</td><td>0.20 (+16.74%)</td><td>0.17 <b>(+20.06%)</b></td><td>0.01 <b>(-30.32%)</b></td><td>195.50 (-16.70%)</td><td>172.98 (-15.56%)</td><td>167.20 (-14.34%)</td><td>165.70 (-8.71%)</td><td>12.75 <b>(-46.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.70 (n/a)</td><td>204.86 (n/a)</td><td>195.20 (n/a)</td><td>181.50 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (-3.07%)</td><td>0.22 (+18.78%)</td><td>0.23 (+19.43%)</td><td>0.16 <b>(+30.16%)</b></td><td>0.04 <b>(-30.02%)</b></td><td>207.30 <b>(-23.17%)</b></td><td>154.56 (-19.02%)</td><td>141.60 (-16.26%)</td><td>131.00 (+3.15%)</td><td>30.85 <b>(-43.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>269.80 (n/a)</td><td>190.86 (n/a)</td><td>169.10 (n/a)</td><td>127.00 (n/a)</td><td>55.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (-0.73%)</td><td>0.18 (-0.31%)</td><td>0.18 (-0.13%)</td><td>0.18 (-0.26%)</td><td>0.00 <b>(-34.32%)</b></td><td>47651.90 (+0.26%)</td><td>47496.22 (+0.31%)</td><td>47502.40 (+0.13%)</td><td>47298.30 (+0.74%)</td><td>152.02 <b>(-33.59%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47527.00 (n/a)</td><td>47347.24 (n/a)</td><td>47441.80 (n/a)</td><td>46950.90 (n/a)</td><td>228.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (+0.08%)</td><td>0.18 (-0.05%)</td><td>0.18 (-0.08%)</td><td>0.18 (-0.39%)</td><td>0.00 <b>(+43.72%)</b></td><td>47606.20 (+0.39%)</td><td>47326.78 (+0.06%)</td><td>47365.70 (+0.08%)</td><td>47008.30 (-0.08%)</td><td>215.38 <b>(+44.17%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47421.70 (n/a)</td><td>47300.50 (n/a)</td><td>47326.70 (n/a)</td><td>47046.90 (n/a)</td><td>149.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (+0.01%)</td><td>0.11 (+0.01%)</td><td>0.11 (+0.01%)</td><td>0.11 (-0.02%)</td><td>0.00 <b>(+40.93%)</b></td><td>374609.50 (+0.02%)</td><td>374395.58 (-0.01%)</td><td>374357.00 (-0.01%)</td><td>374312.80 (-0.01%)</td><td>121.56 <b>(+40.92%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374539.30 (n/a)</td><td>374426.16 (n/a)</td><td>374384.60 (n/a)</td><td>374336.20 (n/a)</td><td>86.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 <b>(+24.23%)</b></td><td>0.03 (+1.27%)</td><td>0.03 (-4.26%)</td><td>0.02 <b>(-24.22%)</b></td><td>0.01 <b>(+106.99%)</b></td><td>254.90 <b>(+31.94%)</b></td><td>169.92 (+4.35%)</td><td>159.80 (+4.44%)</td><td>110.00 (-19.53%)</td><td>52.97 <b>(+120.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.20 (n/a)</td><td>162.84 (n/a)</td><td>153.00 (n/a)</td><td>136.70 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (+0.47%)</td><td>0.04 (-5.13%)</td><td>0.04 (-4.93%)</td><td>0.03 (-18.14%)</td><td>0.01 <b>(+99.64%)</b></td><td>190.50 <b>(+22.19%)</b></td><td>154.90 (+6.81%)</td><td>149.10 (+5.22%)</td><td>133.30 (-0.45%)</td><td>23.01 <b>(+140.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>155.90 (n/a)</td><td>145.02 (n/a)</td><td>141.70 (n/a)</td><td>133.90 (n/a)</td><td>9.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+12.05%)</td><td>0.02 (-4.48%)</td><td>0.02 (-11.54%)</td><td>0.02 (-16.55%)</td><td>0.01 <b>(+91.28%)</b></td><td>229.10 (+19.82%)</td><td>170.86 (+7.91%)</td><td>176.10 (+13.10%)</td><td>124.80 (-10.79%)</td><td>39.26 <b>(+99.98%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>158.34 (n/a)</td><td>155.70 (n/a)</td><td>139.90 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (+10.88%)</td><td>0.03 (-7.03%)</td><td>0.03 (-13.74%)</td><td>0.03 (-19.83%)</td><td>0.01 <b>(+207.37%)</b></td><td>194.60 <b>(+24.74%)</b></td><td>159.42 (+10.82%)</td><td>165.50 (+15.98%)</td><td>120.00 (-9.77%)</td><td>31.25 <b>(+244.39%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>156.00 (n/a)</td><td>143.86 (n/a)</td><td>142.70 (n/a)</td><td>133.00 (n/a)</td><td>9.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 <b>(+28.41%)</b></td><td>0.03 (+2.53%)</td><td>0.02 (-12.90%)</td><td>0.02 (+10.20%)</td><td>0.01 <b>(+87.70%)</b></td><td>183.10 (-9.27%)</td><td>164.26 (-0.29%)</td><td>177.70 (+14.79%)</td><td>109.40 <b>(-22.14%)</b></td><td>30.93 <b>(+28.20%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>164.74 (n/a)</td><td>154.80 (n/a)</td><td>140.50 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (+6.68%)</td><td>0.03 (-8.50%)</td><td>0.03 (-12.28%)</td><td>0.02 <b>(-36.00%)</b></td><td>0.01 <b>(+127.75%)</b></td><td>280.00 <b>(+56.25%)</b></td><td>187.28 (+15.99%)</td><td>189.90 (+13.99%)</td><td>131.50 (-6.27%)</td><td>58.21 <b>(+233.79%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>179.20 (n/a)</td><td>161.46 (n/a)</td><td>166.60 (n/a)</td><td>140.30 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+6.76%)</td><td>0.02 (-8.25%)</td><td>0.02 (-16.54%)</td><td>0.02 (-5.26%)</td><td>0.01 <b>(+23.25%)</b></td><td>207.10 (+5.56%)</td><td>180.36 (+10.19%)</td><td>192.10 (+19.84%)</td><td>121.10 (-6.34%)</td><td>34.10 (+15.04%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.20 (n/a)</td><td>163.68 (n/a)</td><td>160.30 (n/a)</td><td>129.30 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 <b>(+25.28%)</b></td><td>0.02 (-4.60%)</td><td>0.02 (-14.17%)</td><td>0.02 (-9.42%)</td><td>0.01 <b>(+122.60%)</b></td><td>229.50 (+10.39%)</td><td>199.94 (+8.56%)</td><td>208.70 (+16.53%)</td><td>128.30 <b>(-20.16%)</b></td><td>41.36 <b>(+87.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.90 (n/a)</td><td>184.18 (n/a)</td><td>179.10 (n/a)</td><td>160.70 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-16.86%)</td><td>0.02 (-12.94%)</td><td>0.02 (-19.84%)</td><td>0.02 (-5.42%)</td><td>0.00 <b>(-38.90%)</b></td><td>201.90 (+5.76%)</td><td>170.06 (+13.28%)</td><td>169.30 <b>(+24.76%)</b></td><td>147.20 <b>(+20.26%)</b></td><td>21.60 <b>(-23.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>150.12 (n/a)</td><td>135.70 (n/a)</td><td>122.40 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 <b>(+26.40%)</b></td><td>0.03 (+17.78%)</td><td>0.03 <b>(+23.50%)</b></td><td>0.02 (-6.28%)</td><td>0.01 <b>(+123.69%)</b></td><td>234.90 (+6.68%)</td><td>159.56 (-11.72%)</td><td>140.40 (-19.03%)</td><td>127.80 <b>(-20.92%)</b></td><td>44.89 <b>(+87.51%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.20 (n/a)</td><td>180.74 (n/a)</td><td>173.40 (n/a)</td><td>161.60 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 <b>(-24.18%)</b></td><td>0.02 <b>(-20.86%)</b></td><td>0.02 <b>(-24.60%)</b></td><td>0.02 (-5.92%)</td><td>0.00 <b>(-57.43%)</b></td><td>236.30 (+6.30%)</td><td>207.42 <b>(+21.94%)</b></td><td>211.50 <b>(+32.60%)</b></td><td>170.30 <b>(+31.91%)</b></td><td>24.79 <b>(-40.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>170.10 (n/a)</td><td>159.50 (n/a)</td><td>129.10 (n/a)</td><td>41.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-3.77%)</td><td>0.02 (-13.29%)</td><td>0.02 <b>(-23.68%)</b></td><td>0.01 <b>(-23.43%)</b></td><td>0.00 <b>(+21.59%)</b></td><td>324.50 <b>(+30.58%)</b></td><td>226.90 (+18.28%)</td><td>226.30 <b>(+31.04%)</b></td><td>164.90 (+3.91%)</td><td>60.81 <b>(+66.26%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.50 (n/a)</td><td>191.84 (n/a)</td><td>172.70 (n/a)</td><td>158.70 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-1.84%)</td><td>0.02 (-10.62%)</td><td>0.02 (-8.81%)</td><td>0.02 (-19.84%)</td><td>0.00 <b>(+24.07%)</b></td><td>272.50 <b>(+24.71%)</b></td><td>205.34 (+13.88%)</td><td>197.00 (+9.63%)</td><td>151.30 (+1.82%)</td><td>44.76 <b>(+59.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>180.32 (n/a)</td><td>179.70 (n/a)</td><td>148.60 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-15.07%)</td><td>0.02 (-13.21%)</td><td>0.02 (-11.34%)</td><td>0.02 (-10.58%)</td><td>0.00 <b>(-31.86%)</b></td><td>272.80 (+11.85%)</td><td>229.60 (+14.30%)</td><td>229.60 (+12.83%)</td><td>190.20 (+17.77%)</td><td>29.31 (-9.81%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.90 (n/a)</td><td>200.88 (n/a)</td><td>203.50 (n/a)</td><td>161.50 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 (-11.42%)</td><td>0.02 (-9.65%)</td><td>0.02 (-8.90%)</td><td>0.02 (-10.70%)</td><td>0.00 (-6.74%)</td><td>234.30 (+12.00%)</td><td>204.40 (+10.83%)</td><td>203.40 (+9.77%)</td><td>173.70 (+12.87%)</td><td>24.31 <b>(+20.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.20 (n/a)</td><td>184.42 (n/a)</td><td>185.30 (n/a)</td><td>153.90 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (+10.57%)</td><td>0.06 (+14.47%)</td><td>0.06 <b>(+25.99%)</b></td><td>0.05 (+2.62%)</td><td>0.01 (+17.63%)</td><td>176.10 (-2.55%)</td><td>136.74 (-12.28%)</td><td>129.50 <b>(-20.65%)</b></td><td>116.70 (-9.53%)</td><td>24.59 (+4.25%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>155.88 (n/a)</td><td>163.20 (n/a)</td><td>129.00 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 <b>(+24.65%)</b></td><td>0.09 <b>(+34.60%)</b></td><td>0.09 <b>(+36.39%)</b></td><td>0.07 <b>(+51.14%)</b></td><td>0.02 (+12.65%)</td><td>182.60 <b>(-33.84%)</b></td><td>143.08 <b>(-26.84%)</b></td><td>134.50 <b>(-26.70%)</b></td><td>111.70 (-19.81%)</td><td>29.55 <b>(-41.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>276.00 (n/a)</td><td>195.58 (n/a)</td><td>183.50 (n/a)</td><td>139.30 (n/a)</td><td>50.17 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(+20.70%)</b></td><td>0.05 (+10.82%)</td><td>0.05 (+5.41%)</td><td>0.04 (+2.59%)</td><td>0.01 <b>(+50.88%)</b></td><td>191.10 (-2.55%)</td><td>155.32 (-8.73%)</td><td>161.40 (-5.11%)</td><td>117.10 (-17.13%)</td><td>27.14 (+18.78%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>170.18 (n/a)</td><td>170.10 (n/a)</td><td>141.30 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (-17.41%)</td><td>0.06 (-8.11%)</td><td>0.06 (-17.79%)</td><td>0.06 (+11.55%)</td><td>0.00 <b>(-69.96%)</b></td><td>183.00 (-10.34%)</td><td>174.34 (+5.38%)</td><td>182.10 <b>(+21.64%)</b></td><td>159.40 <b>(+21.03%)</b></td><td>11.30 <b>(-68.22%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>165.44 (n/a)</td><td>149.70 (n/a)</td><td>131.70 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 <b>(+22.16%)</b></td><td>0.06 (+10.19%)</td><td>0.06 (+13.96%)</td><td>0.03 <b>(-35.04%)</b></td><td>0.02 <b>(+190.29%)</b></td><td>307.40 <b>(+53.93%)</b></td><td>168.88 (+1.71%)</td><td>144.70 (-12.25%)</td><td>115.70 (-18.12%)</td><td>79.61 <b>(+269.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>166.04 (n/a)</td><td>164.90 (n/a)</td><td>141.30 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 <b>(+24.03%)</b></td><td>0.06 (-3.02%)</td><td>0.06 (-3.55%)</td><td>0.05 (-18.73%)</td><td>0.02 <b>(+209.73%)</b></td><td>214.70 <b>(+23.04%)</b></td><td>175.68 (+8.11%)</td><td>173.70 (+3.70%)</td><td>113.30 (-19.36%)</td><td>41.04 <b>(+211.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>174.50 (n/a)</td><td>162.50 (n/a)</td><td>167.50 (n/a)</td><td>140.50 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (+19.38%)</td><td>0.06 (+16.38%)</td><td>0.05 (+14.88%)</td><td>0.04 (+1.96%)</td><td>0.01 <b>(+64.52%)</b></td><td>202.50 (-1.89%)</td><td>153.72 (-11.99%)</td><td>153.40 (-12.94%)</td><td>116.00 (-16.25%)</td><td>36.56 <b>(+31.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>174.66 (n/a)</td><td>176.20 (n/a)</td><td>138.50 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (+15.38%)</td><td>0.05 (+3.56%)</td><td>0.05 (+4.71%)</td><td>0.03 (-19.15%)</td><td>0.01 <b>(+81.56%)</b></td><td>296.60 <b>(+23.69%)</b></td><td>206.00 (+0.70%)</td><td>196.10 (-4.48%)</td><td>146.60 (-13.36%)</td><td>58.58 <b>(+95.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>204.56 (n/a)</td><td>205.30 (n/a)</td><td>169.20 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (+14.06%)</td><td>0.05 (+9.62%)</td><td>0.05 (+1.81%)</td><td>0.04 (+5.09%)</td><td>0.01 <b>(+38.59%)</b></td><td>186.50 (-4.85%)</td><td>157.98 (-7.69%)</td><td>172.40 (-1.77%)</td><td>118.50 (-12.35%)</td><td>30.16 (+14.18%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>171.14 (n/a)</td><td>175.50 (n/a)</td><td>135.20 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 <b>(-23.41%)</b></td><td>0.05 (-8.96%)</td><td>0.05 (-3.07%)</td><td>0.04 (+4.46%)</td><td>0.00 <b>(-65.76%)</b></td><td>220.30 (-4.30%)</td><td>203.58 (+7.53%)</td><td>198.30 (+3.17%)</td><td>190.50 <b>(+30.57%)</b></td><td>14.03 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>189.32 (n/a)</td><td>192.20 (n/a)</td><td>145.90 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.07 (+6.28%)</td><td>0.05 (-9.48%)</td><td>0.05 (+3.47%)</td><td>0.03 <b>(-24.48%)</b></td><td>0.01 <b>(+55.58%)</b></td><td>257.80 <b>(+32.41%)</b></td><td>184.00 (+15.36%)</td><td>160.90 (-3.36%)</td><td>125.70 (-5.91%)</td><td>52.96 <b>(+104.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>159.50 (n/a)</td><td>166.50 (n/a)</td><td>133.60 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (+5.75%)</td><td>0.04 (-9.20%)</td><td>0.04 <b>(-21.59%)</b></td><td>0.03 <b>(-23.62%)</b></td><td>0.01 <b>(+58.96%)</b></td><td>299.90 <b>(+30.96%)</b></td><td>214.82 (+14.72%)</td><td>225.10 <b>(+27.54%)</b></td><td>143.90 (-5.45%)</td><td>59.17 <b>(+92.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>187.26 (n/a)</td><td>176.50 (n/a)</td><td>152.20 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.06 (+4.83%)</td><td>0.05 (-5.17%)</td><td>0.05 (-9.91%)</td><td>0.04 (+3.68%)</td><td>0.01 (+16.62%)</td><td>218.70 (-3.57%)</td><td>183.58 (+6.05%)</td><td>180.50 (+11.01%)</td><td>133.90 (-4.56%)</td><td>34.24 (+4.83%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>173.10 (n/a)</td><td>162.60 (n/a)</td><td>140.30 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.05 (-1.24%)</td><td>0.05 (-3.12%)</td><td>0.05 (-9.56%)</td><td>0.04 (+15.31%)</td><td>0.01 <b>(-35.24%)</b></td><td>227.20 (-13.25%)</td><td>192.66 (+1.34%)</td><td>187.30 (+10.57%)</td><td>169.90 (+1.25%)</td><td>22.92 <b>(-43.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.90 (n/a)</td><td>190.12 (n/a)</td><td>169.40 (n/a)</td><td>167.80 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (-3.39%)</td><td>0.04 (-6.35%)</td><td>0.04 (+5.52%)</td><td>0.02 <b>(-34.76%)</b></td><td>0.01 <b>(+89.11%)</b></td><td>368.10 <b>(+53.31%)</b></td><td>232.60 (+12.65%)</td><td>194.30 (-5.22%)</td><td>188.70 (+3.51%)</td><td>77.02 <b>(+208.94%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>206.48 (n/a)</td><td>205.00 (n/a)</td><td>182.30 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 <b>(+21.83%)</b></td><td>0.09 (-4.55%)</td><td>0.09 (-13.57%)</td><td>0.08 (-13.07%)</td><td>0.02 <b>(+183.68%)</b></td><td>215.20 (+15.02%)</td><td>183.68 (+8.16%)</td><td>190.70 (+15.72%)</td><td>127.70 (-17.88%)</td><td>36.06 <b>(+166.41%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>169.82 (n/a)</td><td>164.80 (n/a)</td><td>155.50 (n/a)</td><td>13.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (-17.20%)</td><td>0.13 (-9.23%)</td><td>0.13 (-14.39%)</td><td>0.12 (+12.67%)</td><td>0.01 <b>(-63.82%)</b></td><td>205.60 (-11.23%)</td><td>190.34 (+7.91%)</td><td>194.40 (+16.83%)</td><td>177.50 <b>(+20.75%)</b></td><td>12.15 <b>(-62.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>176.38 (n/a)</td><td>166.40 (n/a)</td><td>147.00 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (+9.72%)</td><td>0.10 (+5.74%)</td><td>0.09 (-6.02%)</td><td>0.08 (+12.08%)</td><td>0.02 (+5.48%)</td><td>196.30 (-10.77%)</td><td>166.00 (-5.75%)</td><td>174.80 (+6.39%)</td><td>124.60 (-8.85%)</td><td>27.42 (-16.95%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>176.12 (n/a)</td><td>164.30 (n/a)</td><td>136.70 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (+7.49%)</td><td>0.13 <b>(+22.66%)</b></td><td>0.12 <b>(+26.74%)</b></td><td>0.11 <b>(+41.99%)</b></td><td>0.02 <b>(-20.81%)</b></td><td>191.10 <b>(-29.56%)</b></td><td>164.50 <b>(-20.50%)</b></td><td>166.00 <b>(-21.10%)</b></td><td>132.10 (-6.91%)</td><td>25.32 <b>(-46.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>271.30 (n/a)</td><td>206.92 (n/a)</td><td>210.40 (n/a)</td><td>141.90 (n/a)</td><td>47.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (-8.57%)</td><td>0.09 (-5.80%)</td><td>0.08 (-15.67%)</td><td>0.07 (-0.51%)</td><td>0.02 (-7.50%)</td><td>220.50 (+0.50%)</td><td>178.70 (+5.98%)</td><td>194.40 (+18.54%)</td><td>132.30 (+9.43%)</td><td>36.08 (+1.46%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>168.62 (n/a)</td><td>164.00 (n/a)</td><td>120.90 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+8.93%)</td><td>0.12 (+2.91%)</td><td>0.12 (+7.03%)</td><td>0.09 (-8.19%)</td><td>0.02 <b>(+40.32%)</b></td><td>240.20 (+8.93%)</td><td>183.60 (-1.08%)</td><td>172.10 (-6.57%)</td><td>137.70 (-8.20%)</td><td>39.84 <b>(+41.53%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>185.60 (n/a)</td><td>184.20 (n/a)</td><td>150.00 (n/a)</td><td>28.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 (-17.43%)</td><td>0.08 <b>(-27.93%)</b></td><td>0.08 <b>(-33.25%)</b></td><td>0.06 <b>(-42.07%)</b></td><td>0.02 <b>(+79.15%)</b></td><td>280.20 <b>(+72.64%)</b></td><td>212.10 <b>(+42.69%)</b></td><td>214.80 <b>(+49.79%)</b></td><td>166.50 <b>(+21.09%)</b></td><td>44.58 <b>(+270.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>162.30 (n/a)</td><td>148.64 (n/a)</td><td>143.40 (n/a)</td><td>137.50 (n/a)</td><td>12.04 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+17.26%)</td><td>0.12 (+12.83%)</td><td>0.14 <b>(+32.08%)</b></td><td>0.06 <b>(-31.03%)</b></td><td>0.04 <b>(+159.06%)</b></td><td>303.20 <b>(+45.00%)</b></td><td>178.32 (-1.75%)</td><td>133.30 <b>(-24.30%)</b></td><td>124.70 (-14.71%)</td><td>76.85 <b>(+209.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>181.50 (n/a)</td><td>176.10 (n/a)</td><td>146.20 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (+12.56%)</td><td>0.10 (+10.28%)</td><td>0.09 (-1.67%)</td><td>0.08 <b>(+25.26%)</b></td><td>0.01 (+5.13%)</td><td>193.00 <b>(-20.18%)</b></td><td>169.20 (-9.77%)</td><td>178.00 (+1.71%)</td><td>138.60 (-11.15%)</td><td>24.00 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>187.52 (n/a)</td><td>175.00 (n/a)</td><td>156.00 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+17.85%)</td><td>0.11 (-4.28%)</td><td>0.10 (-13.56%)</td><td>0.09 (-7.43%)</td><td>0.02 <b>(+130.43%)</b></td><td>195.70 (+8.00%)</td><td>169.08 (+6.38%)</td><td>176.50 (+15.74%)</td><td>126.70 (-15.14%)</td><td>26.54 <b>(+103.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>158.94 (n/a)</td><td>152.50 (n/a)</td><td>149.30 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 <b>(+34.71%)</b></td><td>0.10 (+14.46%)</td><td>0.10 (+10.68%)</td><td>0.08 (+5.83%)</td><td>0.03 <b>(+77.36%)</b></td><td>210.70 (-5.52%)</td><td>169.32 (-10.24%)</td><td>169.60 (-9.64%)</td><td>110.50 <b>(-25.74%)</b></td><td>39.59 <b>(+20.80%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>188.64 (n/a)</td><td>187.70 (n/a)</td><td>148.80 (n/a)</td><td>32.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.10 <b>(-21.94%)</b></td><td>0.09 (-11.83%)</td><td>0.09 (-12.60%)</td><td>0.08 (+9.95%)</td><td>0.01 <b>(-59.54%)</b></td><td>226.20 (-9.05%)</td><td>200.18 (+9.78%)</td><td>192.60 (+14.44%)</td><td>175.60 <b>(+28.08%)</b></td><td>19.96 <b>(-53.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>182.34 (n/a)</td><td>168.30 (n/a)</td><td>137.10 (n/a)</td><td>42.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (-2.73%)</td><td>0.09 (+7.15%)</td><td>0.09 (-7.38%)</td><td>0.08 <b>(+44.44%)</b></td><td>0.01 <b>(-57.11%)</b></td><td>197.00 <b>(-30.78%)</b></td><td>184.60 (-11.93%)</td><td>189.70 (+7.97%)</td><td>153.20 (+2.82%)</td><td>17.84 <b>(-71.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.60 (n/a)</td><td>209.60 (n/a)</td><td>175.70 (n/a)</td><td>149.00 (n/a)</td><td>61.79 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 <b>(+23.93%)</b></td><td>0.09 (+9.57%)</td><td>0.09 (+11.55%)</td><td>0.08 (+4.46%)</td><td>0.01 <b>(+95.69%)</b></td><td>229.60 (-4.25%)</td><td>200.24 (-7.68%)</td><td>196.00 (-10.34%)</td><td>158.00 (-19.31%)</td><td>28.10 <b>(+51.67%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>216.90 (n/a)</td><td>218.60 (n/a)</td><td>195.80 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.09 (-8.90%)</td><td>0.08 (-0.48%)</td><td>0.08 (+5.77%)</td><td>0.08 (+4.72%)</td><td>0.01 <b>(-48.03%)</b></td><td>214.20 (-4.55%)</td><td>200.20 (-0.64%)</td><td>203.90 (-5.47%)</td><td>180.90 (+9.77%)</td><td>14.52 <b>(-45.93%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>201.48 (n/a)</td><td>215.70 (n/a)</td><td>164.80 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (+8.74%)</td><td>0.20 (+4.12%)</td><td>0.21 (+10.26%)</td><td>0.15 (-12.96%)</td><td>0.04 <b>(+58.99%)</b></td><td>223.70 (+14.89%)</td><td>168.06 (-1.77%)</td><td>158.60 (-9.32%)</td><td>135.30 (-8.02%)</td><td>37.43 <b>(+66.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.70 (n/a)</td><td>171.08 (n/a)</td><td>174.90 (n/a)</td><td>147.10 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.23 (-7.41%)</td><td>0.18 (-10.11%)</td><td>0.20 (-1.85%)</td><td>0.10 <b>(-41.10%)</b></td><td>0.05 <b>(+70.23%)</b></td><td>325.30 <b>(+69.78%)</b></td><td>195.46 (+18.92%)</td><td>167.70 (+1.88%)</td><td>143.80 (+8.04%)</td><td>73.50 <b>(+239.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.60 (n/a)</td><td>164.36 (n/a)</td><td>164.60 (n/a)</td><td>133.10 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (+14.33%)</td><td>0.24 (+17.68%)</td><td>0.24 (+15.35%)</td><td>0.22 (+19.99%)</td><td>0.02 (-16.45%)</td><td>188.20 (-16.65%)</td><td>173.06 (-15.32%)</td><td>170.70 (-13.31%)</td><td>158.10 (-12.51%)</td><td>11.53 <b>(-40.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>204.38 (n/a)</td><td>196.90 (n/a)</td><td>180.70 (n/a)</td><td>19.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+11.00%)</td><td>0.22 (+10.16%)</td><td>0.23 (+3.61%)</td><td>0.14 (+19.52%)</td><td>0.06 (+8.03%)</td><td>241.70 (-16.34%)</td><td>160.50 (-10.27%)</td><td>139.70 (-3.46%)</td><td>120.50 (-9.87%)</td><td>51.22 <b>(-21.05%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>288.90 (n/a)</td><td>178.86 (n/a)</td><td>144.70 (n/a)</td><td>133.70 (n/a)</td><td>64.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (-11.83%)</td><td>0.21 (-3.82%)</td><td>0.22 (-3.43%)</td><td>0.10 (-16.49%)</td><td>0.07 (-13.35%)</td><td>390.70 (+19.77%)</td><td>220.32 (+4.80%)</td><td>190.40 (+3.59%)</td><td>143.20 (+13.47%)</td><td>98.23 <b>(+24.04%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>326.20 (n/a)</td><td>210.22 (n/a)</td><td>183.80 (n/a)</td><td>126.20 (n/a)</td><td>79.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+9.53%)</td><td>0.20 (-5.64%)</td><td>0.21 (-10.30%)</td><td>0.16 (+12.18%)</td><td>0.04 (+0.50%)</td><td>210.40 (-10.85%)</td><td>169.26 (+5.14%)</td><td>158.30 (+11.48%)</td><td>123.60 (-8.65%)</td><td>34.85 (-18.39%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>236.00 (n/a)</td><td>160.98 (n/a)</td><td>142.00 (n/a)</td><td>135.30 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (-9.80%)</td><td>0.21 (-13.80%)</td><td>0.19 <b>(-28.17%)</b></td><td>0.17 (+19.13%)</td><td>0.04 <b>(-36.61%)</b></td><td>212.00 (-16.04%)</td><td>184.32 (+11.39%)</td><td>192.90 <b>(+39.28%)</b></td><td>137.70 (+10.87%)</td><td>30.27 <b>(-42.27%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>252.50 (n/a)</td><td>165.48 (n/a)</td><td>138.50 (n/a)</td><td>124.20 (n/a)</td><td>52.43 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (+12.09%)</td><td>0.23 (+9.51%)</td><td>0.22 (+16.36%)</td><td>0.19 (+8.90%)</td><td>0.04 (+7.69%)</td><td>170.40 (-8.14%)</td><td>145.56 (-8.79%)</td><td>149.00 (-14.07%)</td><td>112.20 (-10.74%)</td><td>24.08 (-11.05%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>185.50 (n/a)</td><td>159.58 (n/a)</td><td>173.40 (n/a)</td><td>125.70 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 <b>(+22.25%)</b></td><td>0.21 (-2.92%)</td><td>0.19 (-14.27%)</td><td>0.18 (+2.52%)</td><td>0.05 <b>(+89.88%)</b></td><td>208.80 (-2.48%)</td><td>182.98 (+5.42%)</td><td>195.20 (+16.68%)</td><td>123.00 (-18.22%)</td><td>34.13 <b>(+41.56%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>214.10 (n/a)</td><td>173.58 (n/a)</td><td>167.30 (n/a)</td><td>150.40 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (+8.69%)</td><td>0.21 (+9.77%)</td><td>0.21 (+18.77%)</td><td>0.16 (-3.68%)</td><td>0.03 <b>(+24.43%)</b></td><td>200.20 (+3.84%)</td><td>158.02 (-8.22%)</td><td>152.80 (-15.81%)</td><td>126.20 (-8.02%)</td><td>27.17 <b>(+21.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.80 (n/a)</td><td>172.18 (n/a)</td><td>181.50 (n/a)</td><td>137.20 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (-14.72%)</td><td>0.18 (-6.56%)</td><td>0.18 (-13.17%)</td><td>0.17 (+6.04%)</td><td>0.01 <b>(-69.44%)</b></td><td>208.50 (-5.70%)</td><td>194.26 (+5.30%)</td><td>195.10 (+15.17%)</td><td>183.00 (+17.31%)</td><td>9.49 <b>(-66.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>221.10 (n/a)</td><td>184.48 (n/a)</td><td>169.40 (n/a)</td><td>156.00 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (-10.53%)</td><td>0.18 (-5.76%)</td><td>0.18 (-11.24%)</td><td>0.16 <b>(+23.04%)</b></td><td>0.02 <b>(-47.94%)</b></td><td>207.50 (-18.72%)</td><td>181.84 (+2.57%)</td><td>182.70 (+12.71%)</td><td>152.60 (+11.79%)</td><td>20.75 <b>(-54.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>255.30 (n/a)</td><td>177.28 (n/a)</td><td>162.10 (n/a)</td><td>136.50 (n/a)</td><td>46.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (-6.98%)</td><td>0.18 (-11.61%)</td><td>0.19 (-9.43%)</td><td>0.16 (-10.73%)</td><td>0.02 (+17.15%)</td><td>215.80 (+12.05%)</td><td>192.78 (+13.68%)</td><td>187.20 (+10.44%)</td><td>162.30 (+7.55%)</td><td>22.91 <b>(+44.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>169.58 (n/a)</td><td>169.50 (n/a)</td><td>150.90 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (-2.23%)</td><td>0.16 (-2.58%)</td><td>0.16 (-12.66%)</td><td>0.15 <b>(+30.35%)</b></td><td>0.01 <b>(-65.62%)</b></td><td>214.40 <b>(-23.29%)</b></td><td>204.54 (+0.08%)</td><td>209.00 (+14.52%)</td><td>185.50 (+2.26%)</td><td>11.22 <b>(-73.57%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>279.50 (n/a)</td><td>204.38 (n/a)</td><td>182.50 (n/a)</td><td>181.40 (n/a)</td><td>42.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (-6.44%)</td><td>0.10 <b>(-25.20%)</b></td><td>0.10 <b>(-29.45%)</b></td><td>0.06 <b>(-52.91%)</b></td><td>0.03 <b>(+126.20%)</b></td><td>367.50 <b>(+112.43%)</b></td><td>217.36 <b>(+46.98%)</b></td><td>201.70 <b>(+41.74%)</b></td><td>140.30 (+6.94%)</td><td>88.24 <b>(+436.87%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>173.00 (n/a)</td><td>147.88 (n/a)</td><td>142.30 (n/a)</td><td>131.20 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (+4.15%)</td><td>0.12 (-8.83%)</td><td>0.12 (+3.34%)</td><td>0.06 <b>(-40.81%)</b></td><td>0.03 <b>(+91.68%)</b></td><td>330.40 <b>(+69.00%)</b></td><td>195.14 (+19.06%)</td><td>164.70 (-3.23%)</td><td>130.60 (-4.04%)</td><td>78.55 <b>(+235.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>195.50 (n/a)</td><td>163.90 (n/a)</td><td>170.20 (n/a)</td><td>136.10 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (-8.65%)</td><td>0.13 (-12.98%)</td><td>0.12 (-12.35%)</td><td>0.10 <b>(-20.46%)</b></td><td>0.03 (+4.10%)</td><td>201.50 <b>(+25.78%)</b></td><td>161.30 (+16.11%)</td><td>165.10 (+14.10%)</td><td>113.80 (+9.42%)</td><td>31.60 <b>(+39.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>160.20 (n/a)</td><td>138.92 (n/a)</td><td>144.70 (n/a)</td><td>104.00 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 <b>(-22.67%)</b></td><td>0.12 (-17.45%)</td><td>0.13 (-12.99%)</td><td>0.10 (-9.92%)</td><td>0.02 <b>(-38.10%)</b></td><td>199.90 (+10.99%)</td><td>168.16 (+19.89%)</td><td>159.70 (+14.97%)</td><td>145.60 <b>(+29.31%)</b></td><td>21.74 (-12.40%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>180.10 (n/a)</td><td>140.26 (n/a)</td><td>138.90 (n/a)</td><td>112.60 (n/a)</td><td>24.82 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (-13.85%)</td><td>0.14 (+16.39%)</td><td>0.15 <b>(+31.66%)</b></td><td>0.11 <b>(+28.03%)</b></td><td>0.02 <b>(-48.09%)</b></td><td>186.10 <b>(-21.87%)</b></td><td>150.32 (-18.19%)</td><td>136.90 <b>(-24.07%)</b></td><td>130.70 (+16.07%)</td><td>23.21 <b>(-51.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>238.20 (n/a)</td><td>183.74 (n/a)</td><td>180.30 (n/a)</td><td>112.60 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (+0.89%)</td><td>0.14 (+1.68%)</td><td>0.14 (-0.58%)</td><td>0.10 (-0.31%)</td><td>0.03 (+2.43%)</td><td>206.20 (+0.34%)</td><td>158.18 (-1.54%)</td><td>149.10 (+0.54%)</td><td>118.50 (-0.84%)</td><td>36.61 (+0.29%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>205.50 (n/a)</td><td>160.66 (n/a)</td><td>148.30 (n/a)</td><td>119.50 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 <b>(-29.30%)</b></td><td>0.12 (-2.29%)</td><td>0.11 (+8.03%)</td><td>0.10 (+9.38%)</td><td>0.02 <b>(-60.06%)</b></td><td>210.10 (-8.57%)</td><td>180.44 (-4.57%)</td><td>193.90 (-7.40%)</td><td>143.30 <b>(+41.46%)</b></td><td>27.63 <b>(-46.42%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>229.80 (n/a)</td><td>189.08 (n/a)</td><td>209.40 (n/a)</td><td>101.30 (n/a)</td><td>51.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (+1.06%)</td><td>0.10 (-1.65%)</td><td>0.11 (+2.12%)</td><td>0.08 (-5.37%)</td><td>0.02 <b>(+24.60%)</b></td><td>253.90 (+5.66%)</td><td>203.64 (+2.59%)</td><td>193.50 (-2.07%)</td><td>163.50 (-1.09%)</td><td>35.45 <b>(+30.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>198.50 (n/a)</td><td>197.60 (n/a)</td><td>165.30 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (-10.53%)</td><td>0.15 (-9.85%)</td><td>0.16 (-5.47%)</td><td>0.11 (-5.94%)</td><td>0.03 (-10.91%)</td><td>224.80 (+6.29%)</td><td>173.44 (+10.70%)</td><td>156.10 (+5.76%)</td><td>142.40 (+11.77%)</td><td>35.18 (+4.57%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>156.68 (n/a)</td><td>147.60 (n/a)</td><td>127.40 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (-3.62%)</td><td>0.15 (-2.17%)</td><td>0.14 (-1.76%)</td><td>0.12 (-0.40%)</td><td>0.03 (-0.88%)</td><td>201.40 (+0.40%)</td><td>167.30 (+2.25%)</td><td>173.70 (+1.76%)</td><td>135.80 (+3.74%)</td><td>28.04 (+2.38%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>200.60 (n/a)</td><td>163.62 (n/a)</td><td>170.70 (n/a)</td><td>130.90 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.19 (+10.08%)</td><td>0.15 (-0.15%)</td><td>0.15 (+8.29%)</td><td>0.10 <b>(-28.95%)</b></td><td>0.04 <b>(+182.28%)</b></td><td>248.80 <b>(+40.72%)</b></td><td>173.96 (+5.40%)</td><td>160.50 (-7.65%)</td><td>132.80 (-9.17%)</td><td>48.95 <b>(+247.89%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>165.04 (n/a)</td><td>173.80 (n/a)</td><td>146.20 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 (+8.57%)</td><td>0.15 (-10.38%)</td><td>0.13 <b>(-27.58%)</b></td><td>0.11 (-0.01%)</td><td>0.04 <b>(+24.40%)</b></td><td>226.30 (+0.00%)</td><td>175.38 (+13.16%)</td><td>189.70 <b>(+38.06%)</b></td><td>125.10 (-7.88%)</td><td>43.98 (+10.28%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.30 (n/a)</td><td>154.98 (n/a)</td><td>137.40 (n/a)</td><td>135.80 (n/a)</td><td>39.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (-17.45%)</td><td>0.14 (-3.57%)</td><td>0.14 (-1.51%)</td><td>0.11 (-1.35%)</td><td>0.02 <b>(-37.14%)</b></td><td>214.30 (+1.37%)</td><td>174.28 (+2.19%)</td><td>169.60 (+1.56%)</td><td>153.10 <b>(+21.12%)</b></td><td>24.73 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.40 (n/a)</td><td>170.54 (n/a)</td><td>167.00 (n/a)</td><td>126.40 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 (+11.31%)</td><td>0.13 (-9.27%)</td><td>0.13 (-9.65%)</td><td>0.10 <b>(-23.38%)</b></td><td>0.03 <b>(+132.59%)</b></td><td>247.70 <b>(+30.51%)</b></td><td>192.48 (+13.77%)</td><td>191.40 (+10.64%)</td><td>134.90 (-10.19%)</td><td>40.31 <b>(+166.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>169.18 (n/a)</td><td>173.00 (n/a)</td><td>150.20 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.17 (+2.68%)</td><td>0.14 (+10.94%)</td><td>0.14 <b>(+20.08%)</b></td><td>0.11 (-4.14%)</td><td>0.02 (+0.86%)</td><td>223.90 (+4.33%)</td><td>175.86 (-9.75%)</td><td>171.90 (-16.76%)</td><td>141.40 (-2.62%)</td><td>30.18 (+7.01%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>194.86 (n/a)</td><td>206.50 (n/a)</td><td>145.20 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (+10.67%)</td><td>0.13 (+2.76%)</td><td>0.13 (-0.89%)</td><td>0.10 (-1.37%)</td><td>0.02 <b>(+45.63%)</b></td><td>246.40 (+1.40%)</td><td>195.34 (-1.50%)</td><td>191.50 (+0.90%)</td><td>154.30 (-9.61%)</td><td>35.38 <b>(+30.61%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>198.32 (n/a)</td><td>189.80 (n/a)</td><td>170.70 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (-16.59%)</td><td>0.11 (-2.58%)</td><td>0.11 (-2.64%)</td><td>0.11 <b>(+34.44%)</b></td><td>0.00 <b>(-81.37%)</b></td><td>171.20 <b>(-25.63%)</b></td><td>163.32 (-1.59%)</td><td>165.40 (+2.67%)</td><td>153.00 (+19.91%)</td><td>6.74 <b>(-83.45%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>230.20 (n/a)</td><td>165.96 (n/a)</td><td>161.10 (n/a)</td><td>127.60 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (-16.15%)</td><td>0.11 (-9.53%)</td><td>0.11 (-12.68%)</td><td>0.10 (+14.24%)</td><td>0.01 <b>(-56.57%)</b></td><td>185.90 (-12.48%)</td><td>167.58 (+6.75%)</td><td>168.80 (+14.52%)</td><td>147.60 (+19.22%)</td><td>17.80 <b>(-53.15%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>212.40 (n/a)</td><td>156.98 (n/a)</td><td>147.40 (n/a)</td><td>123.80 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.14 (-3.40%)</td><td>0.12 (-7.72%)</td><td>0.11 (-13.83%)</td><td>0.10 (+12.33%)</td><td>0.01 <b>(-34.67%)</b></td><td>177.50 (-10.98%)</td><td>160.14 (+6.60%)</td><td>165.00 (+16.03%)</td><td>131.50 (+3.54%)</td><td>17.31 <b>(-41.46%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>199.40 (n/a)</td><td>150.22 (n/a)</td><td>142.20 (n/a)</td><td>127.00 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.16 (+11.45%)</td><td>0.10 <b>(-22.72%)</b></td><td>0.09 <b>(-27.94%)</b></td><td>0.07 <b>(-39.22%)</b></td><td>0.04 <b>(+231.59%)</b></td><td>266.40 <b>(+64.55%)</b></td><td>207.06 <b>(+39.58%)</b></td><td>205.40 <b>(+38.78%)</b></td><td>117.50 (-10.31%)</td><td>57.21 <b>(+370.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>161.90 (n/a)</td><td>148.34 (n/a)</td><td>148.00 (n/a)</td><td>131.00 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+16.12%)</td><td>0.12 (+8.16%)</td><td>0.10 (+3.11%)</td><td>0.09 (+1.65%)</td><td>0.02 <b>(+57.91%)</b></td><td>205.40 (-1.63%)</td><td>165.08 (-5.84%)</td><td>176.40 (-3.02%)</td><td>126.80 (-13.92%)</td><td>33.87 <b>(+32.68%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>175.32 (n/a)</td><td>181.90 (n/a)</td><td>147.30 (n/a)</td><td>25.53 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.13 (-10.10%)</td><td>0.11 (+2.53%)</td><td>0.11 (-0.90%)</td><td>0.09 <b>(+58.46%)</b></td><td>0.02 <b>(-45.90%)</b></td><td>206.20 <b>(-36.90%)</b></td><td>177.72 (-10.02%)</td><td>170.20 (+0.89%)</td><td>137.40 (+11.26%)</td><td>28.75 <b>(-62.99%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>326.80 (n/a)</td><td>197.50 (n/a)</td><td>168.70 (n/a)</td><td>123.50 (n/a)</td><td>77.68 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.15 (+1.35%)</td><td>0.12 (+19.84%)</td><td>0.11 (+18.07%)</td><td>0.10 <b>(+68.55%)</b></td><td>0.02 <b>(-28.80%)</b></td><td>193.10 <b>(-40.69%)</b></td><td>163.56 <b>(-21.53%)</b></td><td>170.10 (-15.29%)</td><td>125.90 (-1.33%)</td><td>30.13 <b>(-58.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>325.60 (n/a)</td><td>208.44 (n/a)</td><td>200.80 (n/a)</td><td>127.60 (n/a)</td><td>72.80 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.12 (+13.32%)</td><td>0.10 (+15.51%)</td><td>0.11 <b>(+20.55%)</b></td><td>0.09 (+4.34%)</td><td>0.01 <b>(+43.89%)</b></td><td>214.00 (-4.16%)</td><td>178.48 (-12.89%)</td><td>174.20 (-17.05%)</td><td>152.20 (-11.77%)</td><td>24.23 <b>(+24.54%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>204.88 (n/a)</td><td>210.00 (n/a)</td><td>172.50 (n/a)</td><td>19.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.80 (+9.27%)</td><td>0.64 <b>(+29.87%)</b></td><td>0.62 <b>(+39.08%)</b></td><td>0.54 <b>(+37.06%)</b></td><td>0.11 <b>(-22.36%)</b></td><td>182.50 <b>(-27.06%)</b></td><td>156.02 <b>(-25.23%)</b></td><td>159.60 <b>(-28.11%)</b></td><td>123.10 (-8.48%)</td><td>24.66 <b>(-47.11%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.73 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.14 (n/a)</td><td>250.20 (n/a)</td><td>208.66 (n/a)</td><td>222.00 (n/a)</td><td>134.50 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.02 <b>(+55.36%)</b></td><td>0.72 <b>(+27.90%)</b></td><td>0.73 <b>(+24.72%)</b></td><td>0.50 (+7.35%)</td><td>0.19 <b>(+120.22%)</b></td><td>196.80 (-6.86%)</td><td>144.30 (-19.10%)</td><td>135.40 (-19.79%)</td><td>96.60 <b>(-35.64%)</b></td><td>36.73 <b>(+29.10%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.65 (n/a)</td><td>0.56 (n/a)</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.09 (n/a)</td><td>211.30 (n/a)</td><td>178.36 (n/a)</td><td>168.80 (n/a)</td><td>150.10 (n/a)</td><td>28.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.75 (-3.36%)</td><td>0.55 (-6.95%)</td><td>0.52 (-0.28%)</td><td>0.46 (-9.07%)</td><td>0.12 (-4.49%)</td><td>214.20 (+9.96%)</td><td>182.84 (+7.45%)</td><td>189.40 (+0.26%)</td><td>131.30 (+3.47%)</td><td>33.16 (+4.85%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>194.80 (n/a)</td><td>170.16 (n/a)</td><td>188.90 (n/a)</td><td>126.90 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.57 (-12.03%)</td><td>0.51 (-6.58%)</td><td>0.51 (-9.67%)</td><td>0.47 <b>(+25.25%)</b></td><td>0.05 <b>(-60.58%)</b></td><td>210.70 <b>(-20.16%)</b></td><td>193.08 (+3.28%)</td><td>192.50 (+10.70%)</td><td>172.00 (+13.68%)</td><td>16.83 <b>(-63.72%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.65 (n/a)</td><td>0.55 (n/a)</td><td>0.57 (n/a)</td><td>0.37 (n/a)</td><td>0.11 (n/a)</td><td>263.90 (n/a)</td><td>186.94 (n/a)</td><td>173.90 (n/a)</td><td>151.30 (n/a)</td><td>46.40 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.55 (+13.16%)</td><td>0.45 (+8.44%)</td><td>0.45 (+5.72%)</td><td>0.35 (+10.32%)</td><td>0.08 <b>(+29.84%)</b></td><td>208.90 (-9.33%)</td><td>169.20 (-7.21%)</td><td>163.90 (-5.42%)</td><td>133.10 (-11.68%)</td><td>30.34 (+2.35%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>230.40 (n/a)</td><td>182.34 (n/a)</td><td>173.30 (n/a)</td><td>150.70 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.55 (-2.57%)</td><td>0.42 (-16.60%)</td><td>0.42 <b>(-24.47%)</b></td><td>0.31 (-19.92%)</td><td>0.08 (+5.37%)</td><td>237.50 <b>(+24.87%)</b></td><td>181.84 <b>(+21.08%)</b></td><td>174.70 <b>(+32.35%)</b></td><td>135.10 (+2.66%)</td><td>37.02 <b>(+39.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.56 (n/a)</td><td>0.50 (n/a)</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>190.20 (n/a)</td><td>150.18 (n/a)</td><td>132.00 (n/a)</td><td>131.60 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.49 (-8.77%)</td><td>0.42 (-4.32%)</td><td>0.43 (-2.79%)</td><td>0.31 (-3.52%)</td><td>0.07 <b>(-27.21%)</b></td><td>238.30 (+3.65%)</td><td>179.24 (+3.07%)</td><td>172.60 (+2.86%)</td><td>151.10 (+9.57%)</td><td>34.50 (-12.19%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>229.90 (n/a)</td><td>173.90 (n/a)</td><td>167.80 (n/a)</td><td>137.90 (n/a)</td><td>39.29 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.56 <b>(+26.42%)</b></td><td>0.42 (+7.76%)</td><td>0.38 (-2.02%)</td><td>0.37 (+13.76%)</td><td>0.08 <b>(+69.45%)</b></td><td>198.90 (-12.07%)</td><td>180.56 (-6.10%)</td><td>195.60 (+2.09%)</td><td>132.40 <b>(-20.91%)</b></td><td>28.01 (+17.64%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>226.20 (n/a)</td><td>192.28 (n/a)</td><td>191.60 (n/a)</td><td>167.40 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (-6.46%)</td><td>0.26 (+5.14%)</td><td>0.28 (+11.33%)</td><td>0.19 (+18.61%)</td><td>0.04 <b>(-25.84%)</b></td><td>191.60 (-15.67%)</td><td>148.02 (-7.17%)</td><td>134.00 (-10.19%)</td><td>123.30 (+6.94%)</td><td>27.42 <b>(-34.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>227.20 (n/a)</td><td>159.46 (n/a)</td><td>149.20 (n/a)</td><td>115.30 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 (-1.44%)</td><td>0.26 (+9.76%)</td><td>0.27 (+18.09%)</td><td>0.19 (+12.20%)</td><td>0.05 <b>(-22.08%)</b></td><td>196.30 (-10.85%)</td><td>144.18 (-11.16%)</td><td>134.30 (-15.27%)</td><td>112.50 (+1.44%)</td><td>31.78 <b>(-27.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>220.20 (n/a)</td><td>162.30 (n/a)</td><td>158.50 (n/a)</td><td>110.90 (n/a)</td><td>43.74 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 (-11.55%)</td><td>0.26 (-3.64%)</td><td>0.28 (+5.36%)</td><td>0.20 (-10.48%)</td><td>0.04 (-4.43%)</td><td>187.20 (+11.69%)</td><td>144.30 (+4.11%)</td><td>133.90 (-5.10%)</td><td>125.50 (+13.06%)</td><td>25.35 <b>(+22.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>167.60 (n/a)</td><td>138.60 (n/a)</td><td>141.10 (n/a)</td><td>111.00 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (-4.98%)</td><td>0.22 (+5.38%)</td><td>0.22 (+11.60%)</td><td>0.20 (+9.21%)</td><td>0.01 <b>(-47.11%)</b></td><td>180.10 (-8.44%)</td><td>169.94 (-5.98%)</td><td>169.50 (-10.41%)</td><td>152.60 (+5.24%)</td><td>10.83 <b>(-48.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>196.70 (n/a)</td><td>180.74 (n/a)</td><td>189.20 (n/a)</td><td>145.00 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (+0.95%)</td><td>0.25 (+19.14%)</td><td>0.28 <b>(+36.23%)</b></td><td>0.21 <b>(+27.46%)</b></td><td>0.04 (-19.49%)</td><td>179.00 <b>(-21.56%)</b></td><td>147.70 (-17.46%)</td><td>133.40 <b>(-26.62%)</b></td><td>130.00 (-0.99%)</td><td>22.58 <b>(-37.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>228.20 (n/a)</td><td>178.94 (n/a)</td><td>181.80 (n/a)</td><td>131.30 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (+17.31%)</td><td>0.21 (+0.19%)</td><td>0.20 (-7.20%)</td><td>0.16 (-9.38%)</td><td>0.04 <b>(+105.91%)</b></td><td>227.40 (+10.33%)</td><td>178.42 (+1.92%)</td><td>179.90 (+7.79%)</td><td>139.70 (-14.77%)</td><td>33.73 <b>(+90.97%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>206.10 (n/a)</td><td>175.06 (n/a)</td><td>166.90 (n/a)</td><td>163.90 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.25 (+18.17%)</td><td>0.21 (+12.01%)</td><td>0.21 (+17.59%)</td><td>0.18 (+8.61%)</td><td>0.03 <b>(+43.07%)</b></td><td>210.40 (-7.92%)</td><td>179.32 (-10.07%)</td><td>175.00 (-14.92%)</td><td>147.70 (-15.36%)</td><td>26.92 (+15.57%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>228.50 (n/a)</td><td>199.40 (n/a)</td><td>205.70 (n/a)</td><td>174.50 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+2.08%)</td><td>0.19 (-7.54%)</td><td>0.21 (+4.66%)</td><td>0.10 <b>(-44.34%)</b></td><td>0.07 <b>(+82.56%)</b></td><td>382.40 <b>(+79.70%)</b></td><td>217.00 <b>(+20.21%)</b></td><td>175.80 (-4.46%)</td><td>135.80 (-2.02%)</td><td>98.43 <b>(+237.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>212.80 (n/a)</td><td>180.52 (n/a)</td><td>184.00 (n/a)</td><td>138.60 (n/a)</td><td>29.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (-9.07%)</td><td>0.25 (-14.85%)</td><td>0.24 (-19.48%)</td><td>0.19 (-16.98%)</td><td>0.06 <b>(+33.89%)</b></td><td>213.50 <b>(+20.49%)</b></td><td>167.80 <b>(+20.30%)</b></td><td>168.90 <b>(+24.19%)</b></td><td>127.70 (+9.99%)</td><td>38.42 <b>(+68.62%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>177.20 (n/a)</td><td>139.48 (n/a)</td><td>136.00 (n/a)</td><td>116.10 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 (+5.47%)</td><td>0.25 (-14.80%)</td><td>0.25 (-16.87%)</td><td>0.13 <b>(-51.27%)</b></td><td>0.08 <b>(+240.11%)</b></td><td>320.10 <b>(+105.19%)</b></td><td>185.02 <b>(+30.74%)</b></td><td>162.80 <b>(+20.33%)</b></td><td>124.80 (-5.24%)</td><td>79.47 <b>(+572.77%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>156.00 (n/a)</td><td>141.52 (n/a)</td><td>135.30 (n/a)</td><td>131.70 (n/a)</td><td>11.81 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.30 (+6.35%)</td><td>0.26 (+5.19%)</td><td>0.25 (+2.03%)</td><td>0.20 (+11.22%)</td><td>0.04 (+5.90%)</td><td>200.20 (-10.06%)</td><td>162.70 (-5.11%)</td><td>166.20 (-2.00%)</td><td>135.40 (-5.97%)</td><td>27.24 (-13.22%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>222.60 (n/a)</td><td>171.46 (n/a)</td><td>169.60 (n/a)</td><td>144.00 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.34 (+15.55%)</td><td>0.30 <b>(+22.77%)</b></td><td>0.31 <b>(+36.36%)</b></td><td>0.24 (+16.44%)</td><td>0.04 (-9.61%)</td><td>168.50 (-14.16%)</td><td>138.42 (-19.26%)</td><td>133.30 <b>(-26.68%)</b></td><td>119.00 (-13.52%)</td><td>18.67 <b>(-32.14%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>196.30 (n/a)</td><td>171.44 (n/a)</td><td>181.80 (n/a)</td><td>137.60 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.24 (-16.85%)</td><td>0.20 (-13.57%)</td><td>0.22 (-7.38%)</td><td>0.15 (-18.65%)</td><td>0.04 (-2.06%)</td><td>276.80 <b>(+22.97%)</b></td><td>211.70 (+17.00%)</td><td>183.30 (+8.01%)</td><td>170.00 <b>(+20.31%)</b></td><td>47.65 <b>(+43.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>225.10 (n/a)</td><td>180.94 (n/a)</td><td>169.70 (n/a)</td><td>141.30 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 (-9.84%)</td><td>0.25 (-5.09%)</td><td>0.25 (-0.85%)</td><td>0.20 (+10.47%)</td><td>0.05 <b>(-29.35%)</b></td><td>209.60 (-9.50%)</td><td>168.16 (+2.65%)</td><td>165.80 (+0.85%)</td><td>128.30 (+10.89%)</td><td>30.40 <b>(-30.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>231.60 (n/a)</td><td>163.82 (n/a)</td><td>164.40 (n/a)</td><td>115.70 (n/a)</td><td>43.47 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.31 (-18.67%)</td><td>0.22 (-9.18%)</td><td>0.19 (-12.84%)</td><td>0.18 (+16.70%)</td><td>0.05 <b>(-38.67%)</b></td><td>232.00 (-14.30%)</td><td>196.80 (+4.27%)</td><td>210.90 (+14.74%)</td><td>132.00 <b>(+22.91%)</b></td><td>38.36 <b>(-36.31%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>270.70 (n/a)</td><td>188.74 (n/a)</td><td>183.80 (n/a)</td><td>107.40 (n/a)</td><td>60.23 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.26 (-13.63%)</td><td>0.23 (-3.80%)</td><td>0.24 (-4.06%)</td><td>0.19 (+3.38%)</td><td>0.03 <b>(-40.64%)</b></td><td>211.40 (-3.29%)</td><td>181.58 (+1.75%)</td><td>168.70 (+4.26%)</td><td>156.70 (+15.82%)</td><td>24.02 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>218.60 (n/a)</td><td>178.46 (n/a)</td><td>161.80 (n/a)</td><td>135.30 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+1.49%)</td><td>0.22 (-0.80%)</td><td>0.21 (+1.65%)</td><td>0.18 (-6.73%)</td><td>0.04 <b>(+22.03%)</b></td><td>191.30 (+7.23%)</td><td>160.66 (+1.80%)</td><td>162.90 (-1.63%)</td><td>128.50 (-1.53%)</td><td>29.40 <b>(+28.18%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>178.40 (n/a)</td><td>157.82 (n/a)</td><td>165.60 (n/a)</td><td>130.50 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (+6.73%)</td><td>0.24 (+11.81%)</td><td>0.25 <b>(+24.02%)</b></td><td>0.19 (+6.42%)</td><td>0.04 (+15.44%)</td><td>180.50 (-5.99%)</td><td>145.76 (-10.31%)</td><td>136.80 (-19.34%)</td><td>126.50 (-6.30%)</td><td>23.30 (+1.62%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>162.52 (n/a)</td><td>169.60 (n/a)</td><td>135.00 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.32 <b>(+41.82%)</b></td><td>0.25 <b>(+33.98%)</b></td><td>0.25 <b>(+37.67%)</b></td><td>0.20 <b>(+44.10%)</b></td><td>0.05 <b>(+44.87%)</b></td><td>169.90 <b>(-30.60%)</b></td><td>141.80 <b>(-25.26%)</b></td><td>137.90 <b>(-27.38%)</b></td><td>107.50 <b>(-29.51%)</b></td><td>26.11 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>244.80 (n/a)</td><td>189.72 (n/a)</td><td>189.90 (n/a)</td><td>152.50 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (-0.23%)</td><td>0.24 (+14.93%)</td><td>0.23 (+19.07%)</td><td>0.21 <b>(+20.72%)</b></td><td>0.02 <b>(-40.40%)</b></td><td>162.60 (-17.17%)</td><td>147.54 (-14.23%)</td><td>150.80 (-16.04%)</td><td>130.20 (+0.23%)</td><td>12.89 <b>(-49.25%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>196.30 (n/a)</td><td>172.02 (n/a)</td><td>179.60 (n/a)</td><td>129.90 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.29 <b>(+20.67%)</b></td><td>0.21 (+0.35%)</td><td>0.22 (+3.84%)</td><td>0.12 <b>(-29.15%)</b></td><td>0.06 <b>(+114.23%)</b></td><td>281.00 <b>(+41.14%)</b></td><td>180.40 (+6.63%)</td><td>160.30 (-3.67%)</td><td>119.90 (-17.14%)</td><td>62.58 <b>(+159.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>199.10 (n/a)</td><td>169.18 (n/a)</td><td>166.40 (n/a)</td><td>144.70 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.28 (-9.91%)</td><td>0.20 (-6.65%)</td><td>0.20 (+6.11%)</td><td>0.09 <b>(-39.69%)</b></td><td>0.07 (+17.76%)</td><td>372.70 <b>(+65.87%)</b></td><td>201.12 (+17.16%)</td><td>170.20 (-5.76%)</td><td>123.20 (+10.99%)</td><td>99.98 <b>(+134.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>224.70 (n/a)</td><td>171.66 (n/a)</td><td>180.60 (n/a)</td><td>111.00 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.21 (-18.91%)</td><td>0.18 (-12.43%)</td><td>0.18 (-14.04%)</td><td>0.15 (-3.69%)</td><td>0.02 <b>(-42.88%)</b></td><td>229.20 (+3.80%)</td><td>197.90 (+12.49%)</td><td>196.40 (+16.28%)</td><td>168.50 <b>(+23.26%)</b></td><td>22.95 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>220.80 (n/a)</td><td>175.92 (n/a)</td><td>168.90 (n/a)</td><td>136.70 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.18 <b>(-30.71%)</b></td><td>0.17 (-18.57%)</td><td>0.17 <b>(-28.61%)</b></td><td>0.16 <b>(+21.23%)</b></td><td>0.01 <b>(-90.51%)</b></td><td>211.50 (-17.51%)</td><td>205.06 (+15.18%)</td><td>204.80 <b>(+40.08%)</b></td><td>198.10 <b>(+44.39%)</b></td><td>6.25 <b>(-88.35%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>256.40 (n/a)</td><td>178.04 (n/a)</td><td>146.20 (n/a)</td><td>137.20 (n/a)</td><td>53.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.75 (-19.51%)</td><td>0.65 (-9.57%)</td><td>0.72 (+4.92%)</td><td>0.50 (-9.96%)</td><td>0.11 (-19.50%)</td><td>262.30 (+11.05%)</td><td>206.28 (+10.25%)</td><td>182.90 (-4.69%)</td><td>174.80 <b>(+24.24%)</b></td><td>39.27 (+10.64%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.93 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.55 (n/a)</td><td>0.14 (n/a)</td><td>236.20 (n/a)</td><td>187.10 (n/a)</td><td>191.90 (n/a)</td><td>140.70 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.92 (+1.26%)</td><td>0.75 (+9.45%)</td><td>0.70 (+10.56%)</td><td>0.61 (+15.00%)</td><td>0.12 (-14.49%)</td><td>213.10 (-13.06%)</td><td>179.06 (-9.68%)</td><td>186.40 (-9.51%)</td><td>142.20 (-1.25%)</td><td>28.23 <b>(-25.85%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.91 (n/a)</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>245.10 (n/a)</td><td>198.26 (n/a)</td><td>206.00 (n/a)</td><td>144.00 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.97 (+0.42%)</td><td>0.83 <b>(+31.22%)</b></td><td>0.80 <b>(+37.92%)</b></td><td>0.69 <b>(+40.74%)</b></td><td>0.12 <b>(-39.77%)</b></td><td>189.20 <b>(-28.95%)</b></td><td>160.08 <b>(-26.82%)</b></td><td>164.80 <b>(-27.50%)</b></td><td>134.60 (-0.44%)</td><td>22.12 <b>(-55.50%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.97 (n/a)</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.19 (n/a)</td><td>266.30 (n/a)</td><td>218.74 (n/a)</td><td>227.30 (n/a)</td><td>135.20 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.02 <b>(-23.59%)</b></td><td>0.02 (-18.80%)</td><td>0.02 (-18.05%)</td><td>0.02 (+0.74%)</td><td>0.00 <b>(-49.70%)</b></td><td>226.80 (-0.74%)</td><td>205.52 (+19.81%)</td><td>218.60 <b>(+22.05%)</b></td><td>164.30 <b>(+30.81%)</b></td><td>25.72 <b>(-34.48%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>171.54 (n/a)</td><td>179.10 (n/a)</td><td>125.60 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (-0.25%)</td><td>0.03 (-11.22%)</td><td>0.02 (-17.67%)</td><td>0.02 <b>(-22.06%)</b></td><td>0.01 <b>(+60.10%)</b></td><td>213.60 <b>(+28.37%)</b></td><td>167.90 (+15.92%)</td><td>178.90 <b>(+21.45%)</b></td><td>118.60 (+0.25%)</td><td>36.60 <b>(+105.78%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.40 (n/a)</td><td>144.84 (n/a)</td><td>147.30 (n/a)</td><td>118.30 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 <b>(+45.78%)</b></td><td>0.03 (+18.07%)</td><td>0.02 (+14.16%)</td><td>0.02 (+2.79%)</td><td>0.00 <b>(+380.34%)</b></td><td>199.00 (-2.74%)</td><td>167.30 (-13.40%)</td><td>170.10 (-12.41%)</td><td>124.30 <b>(-31.40%)</b></td><td>27.07 <b>(+208.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.60 (n/a)</td><td>193.18 (n/a)</td><td>194.20 (n/a)</td><td>181.20 (n/a)</td><td>8.77 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>18.11 (+10.58%)</td><td>14.18 <b>(+21.23%)</b></td><td>12.95 (+1.93%)</td><td>10.51 <b>(+54.28%)</b></td><td>3.08 (-16.52%)</td><td>199.70 <b>(-35.16%)</b></td><td>153.74 <b>(-21.86%)</b></td><td>162.10 (-1.88%)</td><td>115.90 (-9.52%)</td><td>33.30 <b>(-53.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>16.37 (n/a)</td><td>11.69 (n/a)</td><td>12.70 (n/a)</td><td>6.81 (n/a)</td><td>3.68 (n/a)</td><td>308.00 (n/a)</td><td>196.76 (n/a)</td><td>165.20 (n/a)</td><td>128.10 (n/a)</td><td>71.09 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.92 (-14.16%)</td><td>0.79 (-4.10%)</td><td>0.78 (-4.78%)</td><td>0.67 (+14.88%)</td><td>0.09 <b>(-50.23%)</b></td><td>198.00 (-12.93%)</td><td>169.92 (+1.15%)</td><td>170.00 (+5.00%)</td><td>143.50 (+16.57%)</td><td>19.38 <b>(-50.21%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.07 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.58 (n/a)</td><td>0.18 (n/a)</td><td>227.40 (n/a)</td><td>167.98 (n/a)</td><td>161.90 (n/a)</td><td>123.10 (n/a)</td><td>38.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.81 (-12.61%)</td><td>0.65 (-1.98%)</td><td>0.58 (-9.15%)</td><td>0.54 (+7.61%)</td><td>0.13 <b>(-20.70%)</b></td><td>243.60 (-7.09%)</td><td>208.36 (+0.78%)</td><td>228.30 (+10.08%)</td><td>163.00 (+14.47%)</td><td>37.87 (-13.64%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.93 (n/a)</td><td>0.67 (n/a)</td><td>0.64 (n/a)</td><td>0.50 (n/a)</td><td>0.16 (n/a)</td><td>262.20 (n/a)</td><td>206.74 (n/a)</td><td>207.40 (n/a)</td><td>142.40 (n/a)</td><td>43.85 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.10 (-9.85%)</td><td>0.78 <b>(-20.84%)</b></td><td>0.74 <b>(-27.78%)</b></td><td>0.50 <b>(-37.23%)</b></td><td>0.26 <b>(+34.55%)</b></td><td>266.50 <b>(+59.29%)</b></td><td>184.44 <b>(+34.10%)</b></td><td>179.00 <b>(+38.44%)</b></td><td>120.60 (+10.95%)</td><td>61.87 <b>(+125.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.22 (n/a)</td><td>0.99 (n/a)</td><td>1.02 (n/a)</td><td>0.79 (n/a)</td><td>0.19 (n/a)</td><td>167.30 (n/a)</td><td>137.54 (n/a)</td><td>129.30 (n/a)</td><td>108.70 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.80 <b>(-30.24%)</b></td><td>0.69 <b>(-25.87%)</b></td><td>0.69 <b>(-20.18%)</b></td><td>0.58 <b>(-27.17%)</b></td><td>0.09 <b>(-38.28%)</b></td><td>229.70 <b>(+37.30%)</b></td><td>194.70 <b>(+34.20%)</b></td><td>192.10 <b>(+25.31%)</b></td><td>166.00 <b>(+43.35%)</b></td><td>27.19 <b>(+20.43%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.14 (n/a)</td><td>0.93 (n/a)</td><td>0.86 (n/a)</td><td>0.79 (n/a)</td><td>0.15 (n/a)</td><td>167.30 (n/a)</td><td>145.08 (n/a)</td><td>153.30 (n/a)</td><td>115.80 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.16 (+8.18%)</td><td>0.84 (+4.94%)</td><td>0.85 (+7.02%)</td><td>0.57 (+2.07%)</td><td>0.22 (+1.23%)</td><td>233.20 (-2.02%)</td><td>165.84 (-5.12%)</td><td>155.40 (-6.55%)</td><td>114.20 (-7.53%)</td><td>45.56 (-7.22%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.07 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.56 (n/a)</td><td>0.22 (n/a)</td><td>238.00 (n/a)</td><td>174.78 (n/a)</td><td>166.30 (n/a)</td><td>123.50 (n/a)</td><td>49.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.04 (+8.75%)</td><td>0.03 (-3.90%)</td><td>0.03 (-11.69%)</td><td>0.02 (+3.23%)</td><td>0.01 <b>(+28.57%)</b></td><td>187.90 (-3.14%)</td><td>158.44 (+5.04%)</td><td>163.20 (+13.25%)</td><td>109.70 (-8.05%)</td><td>29.10 (+6.90%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>150.84 (n/a)</td><td>144.10 (n/a)</td><td>119.30 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.03 (+2.31%)</td><td>0.02 (+13.70%)</td><td>0.02 (+17.92%)</td><td>0.02 (+10.09%)</td><td>0.00 (-13.99%)</td><td>227.20 (-9.19%)</td><td>179.62 (-13.27%)</td><td>173.80 (-15.18%)</td><td>141.90 (-2.27%)</td><td>33.02 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.20 (n/a)</td><td>207.10 (n/a)</td><td>204.90 (n/a)</td><td>145.20 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.00 (-2.22%)</td><td>0.00 (-0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-13.98%)</td><td>1061.16 (+0.19%)</td><td>981.05 (-0.12%)</td><td>968.67 (-1.09%)</td><td>921.74 (+0.25%)</td><td>51.47 (+1.07%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1059.11 (n/a)</td><td>982.19 (n/a)</td><td>979.38 (n/a)</td><td>919.40 (n/a)</td><td>50.93 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.01 (-3.53%)</td><td>0.01 (-1.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(-35.15%)</b></td><td>1083.84 (+1.16%)</td><td>1038.76 (+1.33%)</td><td>1034.26 (+0.19%)</td><td>1004.71 (+4.73%)</td><td>28.49 <b>(-30.32%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1071.42 (n/a)</td><td>1025.12 (n/a)</td><td>1032.27 (n/a)</td><td>959.30 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.97 (+0.89%)</td><td>0.95 (+0.11%)</td><td>0.95 (-0.14%)</td><td>0.94 (-0.43%)</td><td>0.01 <b>(+105.62%)</b></td><td>2221.91 (+0.44%)</td><td>2201.28 (-0.10%)</td><td>2212.42 (+0.14%)</td><td>2164.60 (-0.88%)</td><td>24.85 <b>(+105.73%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2212.14 (n/a)</td><td>2203.45 (n/a)</td><td>2209.40 (n/a)</td><td>2183.86 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.41 (+2.00%)</td><td>0.39 (-1.85%)</td><td>0.39 (-3.34%)</td><td>0.36 (-2.47%)</td><td>0.02 <b>(+44.20%)</b></td><td>1445.88 (+2.54%)</td><td>1356.41 (+1.98%)</td><td>1361.05 (+3.45%)</td><td>1265.94 (-1.96%)</td><td>66.29 <b>(+43.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1410.04 (n/a)</td><td>1330.07 (n/a)</td><td>1315.61 (n/a)</td><td>1291.24 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.27 (+0.00%)</td><td>0.26 (-0.02%)</td><td>0.26 (-1.50%)</td><td>0.25 (+0.49%)</td><td>0.01 <b>(-26.79%)</b></td><td>2122.60 (-0.50%)</td><td>2044.05 (-0.04%)</td><td>2048.89 (+1.54%)</td><td>1966.95 (-0.01%)</td><td>59.97 <b>(-27.40%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2133.27 (n/a)</td><td>2044.77 (n/a)</td><td>2017.79 (n/a)</td><td>1967.11 (n/a)</td><td>82.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.37 (-2.00%)</td><td>0.37 (-0.03%)</td><td>0.37 (+0.50%)</td><td>0.36 (+0.39%)</td><td>0.00 <b>(-49.56%)</b></td><td>1445.41 (-0.40%)</td><td>1432.70 (+0.01%)</td><td>1435.78 (-0.48%)</td><td>1406.14 (+2.06%)</td><td>15.77 <b>(-49.07%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1451.21 (n/a)</td><td>1432.58 (n/a)</td><td>1442.70 (n/a)</td><td>1377.73 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.82 (-19.83%)</td><td>4.55 (-3.21%)</td><td>4.58 (+0.52%)</td><td>4.21 (+2.26%)</td><td>0.22 <b>(-71.04%)</b></td><td>249.00 (-2.20%)</td><td>230.76 (+1.62%)</td><td>229.10 (-0.52%)</td><td>217.70 <b>(+24.68%)</b></td><td>11.55 <b>(-63.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.01 (n/a)</td><td>4.70 (n/a)</td><td>4.55 (n/a)</td><td>4.12 (n/a)</td><td>0.77 (n/a)</td><td>254.60 (n/a)</td><td>227.08 (n/a)</td><td>230.30 (n/a)</td><td>174.60 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>4.83 (-12.57%)</td><td>4.34 (-7.32%)</td><td>4.31 (-12.38%)</td><td>3.94 (-0.09%)</td><td>0.37 <b>(-46.57%)</b></td><td>265.80 (+0.08%)</td><td>243.08 (+6.60%)</td><td>243.50 (+14.16%)</td><td>217.00 (+14.39%)</td><td>20.37 <b>(-40.52%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.53 (n/a)</td><td>4.68 (n/a)</td><td>4.91 (n/a)</td><td>3.95 (n/a)</td><td>0.69 (n/a)</td><td>265.60 (n/a)</td><td>228.02 (n/a)</td><td>213.30 (n/a)</td><td>189.70 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.57 (+6.47%)</td><td>4.52 (-4.66%)</td><td>4.09 (-11.86%)</td><td>4.03 (-7.52%)</td><td>0.68 <b>(+78.27%)</b></td><td>260.00 (+8.15%)</td><td>236.04 (+6.08%)</td><td>256.30 (+13.46%)</td><td>188.40 (-6.08%)</td><td>32.07 <b>(+83.76%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.23 (n/a)</td><td>4.74 (n/a)</td><td>4.64 (n/a)</td><td>4.36 (n/a)</td><td>0.38 (n/a)</td><td>240.40 (n/a)</td><td>222.52 (n/a)</td><td>225.90 (n/a)</td><td>200.60 (n/a)</td><td>17.45 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.67 (+11.08%)</td><td>5.13 (+6.82%)</td><td>5.32 (+10.51%)</td><td>4.48 (+1.04%)</td><td>0.53 <b>(+74.61%)</b></td><td>234.20 (-1.01%)</td><td>206.10 (-5.86%)</td><td>197.00 (-9.51%)</td><td>184.90 (-9.94%)</td><td>21.81 <b>(+57.16%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.11 (n/a)</td><td>4.80 (n/a)</td><td>4.82 (n/a)</td><td>4.43 (n/a)</td><td>0.30 (n/a)</td><td>236.60 (n/a)</td><td>218.94 (n/a)</td><td>217.70 (n/a)</td><td>205.30 (n/a)</td><td>13.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>9.00 (+12.47%)</td><td>8.07 (+5.30%)</td><td>7.90 (+3.04%)</td><td>6.95 (-2.70%)</td><td>0.82 <b>(+148.71%)</b></td><td>301.60 (+2.79%)</td><td>262.00 (-4.37%)</td><td>265.40 (-2.96%)</td><td>233.00 (-11.07%)</td><td>27.35 <b>(+125.01%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.00 (n/a)</td><td>7.67 (n/a)</td><td>7.67 (n/a)</td><td>7.15 (n/a)</td><td>0.33 (n/a)</td><td>293.40 (n/a)</td><td>273.98 (n/a)</td><td>273.50 (n/a)</td><td>262.00 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>8.60 (-7.07%)</td><td>7.82 (-2.18%)</td><td>7.56 (-9.76%)</td><td>7.18 (+10.53%)</td><td>0.58 <b>(-45.03%)</b></td><td>292.20 (-9.54%)</td><td>269.44 (+1.16%)</td><td>277.50 (+10.82%)</td><td>243.90 (+7.59%)</td><td>19.60 <b>(-47.38%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.25 (n/a)</td><td>7.99 (n/a)</td><td>8.37 (n/a)</td><td>6.49 (n/a)</td><td>1.05 (n/a)</td><td>323.00 (n/a)</td><td>266.36 (n/a)</td><td>250.40 (n/a)</td><td>226.70 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.66 (-16.72%)</td><td>6.91 (-13.49%)</td><td>6.78 (-13.52%)</td><td>5.96 (-5.49%)</td><td>0.67 <b>(-39.38%)</b></td><td>351.90 (+5.80%)</td><td>305.72 (+14.55%)</td><td>309.10 (+15.64%)</td><td>273.80 <b>(+20.09%)</b></td><td>30.84 <b>(-24.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.20 (n/a)</td><td>7.99 (n/a)</td><td>7.85 (n/a)</td><td>6.31 (n/a)</td><td>1.11 (n/a)</td><td>332.60 (n/a)</td><td>266.88 (n/a)</td><td>267.30 (n/a)</td><td>228.00 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.35 <b>(+23.75%)</b></td><td>8.68 (+6.30%)</td><td>7.80 (-4.27%)</td><td>7.40 (-7.70%)</td><td>1.42 <b>(+996.68%)</b></td><td>283.40 (+8.33%)</td><td>246.56 (-4.00%)</td><td>269.00 (+4.47%)</td><td>202.70 (-19.18%)</td><td>38.22 <b>(+841.75%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.36 (n/a)</td><td>8.17 (n/a)</td><td>8.14 (n/a)</td><td>8.02 (n/a)</td><td>0.13 (n/a)</td><td>261.60 (n/a)</td><td>256.84 (n/a)</td><td>257.50 (n/a)</td><td>250.80 (n/a)</td><td>4.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.32 (+9.38%)</td><td>8.57 (+5.48%)</td><td>8.08 (+2.69%)</td><td>7.77 (+3.78%)</td><td>1.07 <b>(+32.38%)</b></td><td>269.90 (-3.64%)</td><td>247.54 (-4.82%)</td><td>259.50 (-2.63%)</td><td>203.30 (-8.59%)</td><td>28.00 (+16.62%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.43 (n/a)</td><td>8.12 (n/a)</td><td>7.87 (n/a)</td><td>7.49 (n/a)</td><td>0.81 (n/a)</td><td>280.10 (n/a)</td><td>260.08 (n/a)</td><td>266.50 (n/a)</td><td>222.40 (n/a)</td><td>24.01 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>10.41 (+11.89%)</td><td>8.58 (+1.29%)</td><td>7.98 (-5.02%)</td><td>7.03 (-10.99%)</td><td>1.51 <b>(+172.10%)</b></td><td>298.30 (+12.35%)</td><td>250.44 (+0.78%)</td><td>262.80 (+5.25%)</td><td>201.40 (-10.65%)</td><td>42.47 <b>(+169.13%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.30 (n/a)</td><td>8.47 (n/a)</td><td>8.40 (n/a)</td><td>7.90 (n/a)</td><td>0.55 (n/a)</td><td>265.50 (n/a)</td><td>248.50 (n/a)</td><td>249.70 (n/a)</td><td>225.40 (n/a)</td><td>15.78 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>12.39 (+3.00%)</td><td>11.73 (+5.23%)</td><td>11.53 (+4.82%)</td><td>11.18 (+5.22%)</td><td>0.55 (+4.51%)</td><td>375.10 (-4.97%)</td><td>358.22 (-4.97%)</td><td>363.90 (-4.59%)</td><td>338.60 (-2.92%)</td><td>16.51 (-2.87%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.02 (n/a)</td><td>11.15 (n/a)</td><td>11.00 (n/a)</td><td>10.63 (n/a)</td><td>0.52 (n/a)</td><td>394.70 (n/a)</td><td>376.96 (n/a)</td><td>381.40 (n/a)</td><td>348.80 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>12.18 (-1.20%)</td><td>11.41 (+0.37%)</td><td>11.46 (+2.30%)</td><td>10.63 (-0.51%)</td><td>0.75 (+19.30%)</td><td>394.70 (+0.51%)</td><td>369.00 (-0.25%)</td><td>366.00 (-2.24%)</td><td>344.50 (+1.23%)</td><td>24.32 <b>(+22.12%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.32 (n/a)</td><td>11.36 (n/a)</td><td>11.20 (n/a)</td><td>10.68 (n/a)</td><td>0.63 (n/a)</td><td>392.70 (n/a)</td><td>369.94 (n/a)</td><td>374.40 (n/a)</td><td>340.30 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.19 (+8.10%)</td><td>11.09 (-3.56%)</td><td>10.78 (-6.13%)</td><td>9.91 (-9.35%)</td><td>1.26 <b>(+172.48%)</b></td><td>423.30 (+10.32%)</td><td>381.78 (+4.55%)</td><td>389.00 (+6.55%)</td><td>318.00 (-7.50%)</td><td>39.70 <b>(+174.08%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.20 (n/a)</td><td>11.50 (n/a)</td><td>11.49 (n/a)</td><td>10.93 (n/a)</td><td>0.46 (n/a)</td><td>383.70 (n/a)</td><td>365.16 (n/a)</td><td>365.10 (n/a)</td><td>343.80 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>15.03 (+16.93%)</td><td>13.80 (+13.14%)</td><td>13.45 (+5.96%)</td><td>12.70 (+18.80%)</td><td>0.94 (+0.47%)</td><td>330.30 (-15.83%)</td><td>305.04 (-11.73%)</td><td>311.90 (-5.63%)</td><td>279.00 (-14.47%)</td><td>20.46 <b>(-27.83%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.86 (n/a)</td><td>12.20 (n/a)</td><td>12.69 (n/a)</td><td>10.69 (n/a)</td><td>0.93 (n/a)</td><td>392.40 (n/a)</td><td>345.58 (n/a)</td><td>330.50 (n/a)</td><td>326.20 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>14.57 (+0.32%)</td><td>12.50 (-0.28%)</td><td>12.72 (+5.78%)</td><td>9.94 (-13.81%)</td><td>1.68 <b>(+31.72%)</b></td><td>422.10 (+16.03%)</td><td>340.76 (+1.08%)</td><td>329.70 (-5.45%)</td><td>287.90 (-0.31%)</td><td>49.69 <b>(+55.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.52 (n/a)</td><td>12.54 (n/a)</td><td>12.03 (n/a)</td><td>11.53 (n/a)</td><td>1.27 (n/a)</td><td>363.80 (n/a)</td><td>337.12 (n/a)</td><td>348.70 (n/a)</td><td>288.80 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.64 (-8.11%)</td><td>12.73 (-5.11%)</td><td>12.53 (-11.11%)</td><td>11.76 (+0.32%)</td><td>0.78 <b>(-42.71%)</b></td><td>356.80 (-0.31%)</td><td>330.56 (+4.81%)</td><td>334.80 (+12.50%)</td><td>307.40 (+8.81%)</td><td>20.18 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.85 (n/a)</td><td>13.41 (n/a)</td><td>14.09 (n/a)</td><td>11.72 (n/a)</td><td>1.35 (n/a)</td><td>357.90 (n/a)</td><td>315.40 (n/a)</td><td>297.60 (n/a)</td><td>282.50 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>13.28 (-6.45%)</td><td>12.40 (-3.90%)</td><td>12.35 (-2.83%)</td><td>11.39 (-7.19%)</td><td>0.69 (-13.02%)</td><td>368.20 (+7.72%)</td><td>339.10 (+4.01%)</td><td>339.70 (+2.91%)</td><td>316.00 (+6.90%)</td><td>19.15 (+0.43%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.19 (n/a)</td><td>12.90 (n/a)</td><td>12.71 (n/a)</td><td>12.27 (n/a)</td><td>0.79 (n/a)</td><td>341.80 (n/a)</td><td>326.02 (n/a)</td><td>330.10 (n/a)</td><td>295.60 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>14.83 (+16.07%)</td><td>12.30 (+5.45%)</td><td>13.24 (+8.57%)</td><td>9.71 (-2.99%)</td><td>2.20 <b>(+85.73%)</b></td><td>432.00 (+3.10%)</td><td>350.20 (-3.44%)</td><td>316.70 (-7.91%)</td><td>282.80 (-13.83%)</td><td>65.27 <b>(+68.69%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.78 (n/a)</td><td>11.67 (n/a)</td><td>12.20 (n/a)</td><td>10.01 (n/a)</td><td>1.18 (n/a)</td><td>419.00 (n/a)</td><td>362.66 (n/a)</td><td>343.90 (n/a)</td><td>328.20 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>2.65 <b>(-22.33%)</b></td><td>2.50 (-9.00%)</td><td>2.51 (-12.51%)</td><td>2.35 <b>(+20.58%)</b></td><td>0.11 <b>(-80.64%)</b></td><td>223.10 (-17.09%)</td><td>209.78 (+6.23%)</td><td>208.80 (+14.29%)</td><td>198.20 <b>(+28.78%)</b></td><td>8.85 <b>(-79.91%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.41 (n/a)</td><td>2.75 (n/a)</td><td>2.87 (n/a)</td><td>1.95 (n/a)</td><td>0.54 (n/a)</td><td>269.10 (n/a)</td><td>197.48 (n/a)</td><td>182.70 (n/a)</td><td>153.90 (n/a)</td><td>44.06 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>5.90 (+12.11%)</td><td>4.78 (-3.18%)</td><td>4.59 (-5.40%)</td><td>4.18 (-9.56%)</td><td>0.67 <b>(+159.03%)</b></td><td>251.10 (+10.57%)</td><td>222.60 (+4.54%)</td><td>228.70 (+5.73%)</td><td>177.60 (-10.80%)</td><td>27.98 <b>(+151.00%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.27 (n/a)</td><td>4.93 (n/a)</td><td>4.85 (n/a)</td><td>4.62 (n/a)</td><td>0.26 (n/a)</td><td>227.10 (n/a)</td><td>212.94 (n/a)</td><td>216.30 (n/a)</td><td>199.10 (n/a)</td><td>11.15 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>7.95 (-2.30%)</td><td>7.33 (-4.36%)</td><td>7.25 (-5.85%)</td><td>6.75 (-4.35%)</td><td>0.53 <b>(+33.00%)</b></td><td>310.80 (+4.58%)</td><td>287.22 (+4.77%)</td><td>289.20 (+6.21%)</td><td>263.70 (+2.37%)</td><td>20.78 <b>(+40.95%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.14 (n/a)</td><td>7.67 (n/a)</td><td>7.70 (n/a)</td><td>7.06 (n/a)</td><td>0.40 (n/a)</td><td>297.20 (n/a)</td><td>274.14 (n/a)</td><td>272.30 (n/a)</td><td>257.60 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>2.61 <b>(-28.14%)</b></td><td>2.47 (-13.80%)</td><td>2.50 (-8.72%)</td><td>2.25 (+2.62%)</td><td>0.14 <b>(-75.11%)</b></td><td>233.40 (-2.55%)</td><td>212.42 (+12.83%)</td><td>210.00 (+9.55%)</td><td>200.70 <b>(+39.09%)</b></td><td>12.58 <b>(-65.63%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.63 (n/a)</td><td>2.87 (n/a)</td><td>2.74 (n/a)</td><td>2.19 (n/a)</td><td>0.56 (n/a)</td><td>239.50 (n/a)</td><td>188.26 (n/a)</td><td>191.70 (n/a)</td><td>144.30 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.20 <b>(-30.91%)</b></td><td>0.17 (-15.41%)</td><td>0.17 (-10.42%)</td><td>0.14 <b>(+46.22%)</b></td><td>0.02 <b>(-69.83%)</b></td><td>237.80 <b>(-31.61%)</b></td><td>193.50 (+3.49%)</td><td>189.20 (+11.62%)</td><td>163.70 <b>(+44.74%)</b></td><td>27.05 <b>(-71.02%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>347.70 (n/a)</td><td>186.98 (n/a)</td><td>169.50 (n/a)</td><td>113.10 (n/a)</td><td>93.35 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.33 <b>(+56.56%)</b></td><td>0.20 (+6.71%)</td><td>0.17 (-10.11%)</td><td>0.16 (+5.57%)</td><td>0.07 <b>(+217.88%)</b></td><td>201.20 (-5.27%)</td><td>172.00 (-0.69%)</td><td>187.80 (+11.26%)</td><td>99.00 <b>(-36.13%)</b></td><td>42.11 <b>(+83.47%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>173.20 (n/a)</td><td>168.80 (n/a)</td><td>155.00 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.47 <b>(+32.04%)</b></td><td>0.38 (+17.58%)</td><td>0.35 (+9.81%)</td><td>0.34 (+15.83%)</td><td>0.06 <b>(+134.23%)</b></td><td>193.00 (-13.65%)</td><td>174.20 (-14.03%)</td><td>186.30 (-8.94%)</td><td>138.60 <b>(-24.26%)</b></td><td>22.37 <b>(+52.58%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.02 (n/a)</td><td>223.50 (n/a)</td><td>202.64 (n/a)</td><td>204.60 (n/a)</td><td>183.00 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.48 (+12.29%)</td><td>0.39 (+3.00%)</td><td>0.43 (+14.30%)</td><td>0.22 <b>(-34.48%)</b></td><td>0.11 <b>(+239.59%)</b></td><td>296.20 <b>(+52.60%)</b></td><td>183.14 (+4.90%)</td><td>153.10 (-12.51%)</td><td>137.00 (-10.92%)</td><td>66.81 <b>(+363.45%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.03 (n/a)</td><td>194.10 (n/a)</td><td>174.58 (n/a)</td><td>175.00 (n/a)</td><td>153.80 (n/a)</td><td>14.42 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.51 (-5.24%)</td><td>0.40 (-1.67%)</td><td>0.41 (+5.48%)</td><td>0.31 (-5.28%)</td><td>0.07 (-6.82%)</td><td>211.30 (+5.60%)</td><td>167.06 (+1.67%)</td><td>158.00 (-5.22%)</td><td>128.40 (+5.51%)</td><td>30.82 (+6.68%)</td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>200.10 (n/a)</td><td>164.32 (n/a)</td><td>166.70 (n/a)</td><td>121.70 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>1.03 (+4.45%)</td><td>0.80 (-0.33%)</td><td>0.77 (+4.44%)</td><td>0.55 (-8.75%)</td><td>0.20 <b>(+21.09%)</b></td><td>238.20 (+9.62%)</td><td>172.74 (+2.24%)</td><td>169.40 (-4.24%)</td><td>127.50 (-4.28%)</td><td>45.58 <b>(+29.24%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.98 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.60 (n/a)</td><td>0.17 (n/a)</td><td>217.30 (n/a)</td><td>168.96 (n/a)</td><td>176.90 (n/a)</td><td>133.20 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.89 (-13.96%)</td><td>0.78 (-0.83%)</td><td>0.78 (+1.59%)</td><td>0.65 (+9.49%)</td><td>0.10 <b>(-39.49%)</b></td><td>200.60 (-8.69%)</td><td>171.38 (-1.28%)</td><td>168.80 (-1.57%)</td><td>146.40 (+16.19%)</td><td>22.81 <b>(-35.36%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.04 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.17 (n/a)</td><td>219.70 (n/a)</td><td>173.60 (n/a)</td><td>171.50 (n/a)</td><td>126.00 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.88 (-7.40%)</td><td>0.69 (-13.06%)</td><td>0.73 (-9.35%)</td><td>0.43 <b>(-28.34%)</b></td><td>0.16 <b>(+25.80%)</b></td><td>302.50 <b>(+39.53%)</b></td><td>201.66 (+18.85%)</td><td>179.80 (+10.31%)</td><td>148.80 (+7.98%)</td><td>59.10 <b>(+96.83%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.95 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.60 (n/a)</td><td>0.13 (n/a)</td><td>216.80 (n/a)</td><td>169.68 (n/a)</td><td>163.00 (n/a)</td><td>137.80 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.90 (-18.64%)</td><td>0.67 (-10.18%)</td><td>0.58 <b>(-25.66%)</b></td><td>0.55 <b>(+35.57%)</b></td><td>0.15 <b>(-41.61%)</b></td><td>240.00 <b>(-26.24%)</b></td><td>204.52 (+3.21%)</td><td>226.60 <b>(+34.56%)</b></td><td>145.20 <b>(+22.84%)</b></td><td>41.13 <b>(-48.09%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.11 (n/a)</td><td>0.74 (n/a)</td><td>0.78 (n/a)</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>325.40 (n/a)</td><td>198.16 (n/a)</td><td>168.40 (n/a)</td><td>118.20 (n/a)</td><td>79.24 (n/a)</td>
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
<td><code>d9e4ec5</code> — 2026-08-29 05:27:01</td><td>0.11 (-5.52%)</td><td>0.11 (+7.71%)</td><td>0.11 <b>(+20.13%)</b></td><td>0.09 (+6.69%)</td><td>0.01 <b>(-35.54%)</b></td><td>173.20 (-6.28%)</td><td>156.46 (-7.92%)</td><td>149.90 (-16.77%)</td><td>143.30 (+5.83%)</td><td>13.45 <b>(-35.66%)</b></td>
</tr>
<tr>
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>169.92 (n/a)</td><td>180.10 (n/a)</td><td>135.40 (n/a)</td><td>20.90 (n/a)</td>
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
