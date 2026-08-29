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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (+17.58%)</td><td>0.04 (+19.09%)</td><td>0.04 (+17.33%)</td><td>0.04 <b>(+23.62%)</b></td><td>0.01 (+8.96%)</td><td>173.00 (-19.12%)</td><td>145.32 (-16.26%)</td><td>145.90 (-14.73%)</td><td>127.20 (-14.92%)</td><td>18.59 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>213.90 (n/a)</td><td>173.54 (n/a)</td><td>171.10 (n/a)</td><td>149.50 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+26.52%)</b></td><td>0.04 (+16.78%)</td><td>0.04 (+13.40%)</td><td>0.03 (+5.81%)</td><td>0.01 <b>(+53.97%)</b></td><td>187.50 (-5.49%)</td><td>147.14 (-13.47%)</td><td>145.40 (-11.77%)</td><td>114.40 <b>(-20.99%)</b></td><td>26.20 (+14.99%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>170.04 (n/a)</td><td>164.80 (n/a)</td><td>144.80 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+20.65%)</b></td><td>0.04 (+9.90%)</td><td>0.05 (+11.90%)</td><td>0.03 (+5.87%)</td><td>0.01 <b>(+74.23%)</b></td><td>175.90 (-5.58%)</td><td>147.06 (-7.70%)</td><td>133.80 (-10.62%)</td><td>120.50 (-17.07%)</td><td>25.74 <b>(+42.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>159.32 (n/a)</td><td>149.70 (n/a)</td><td>145.30 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (+8.70%)</td><td>0.04 (+11.03%)</td><td>0.04 (+13.87%)</td><td>0.04 (+12.28%)</td><td>0.00 (+14.48%)</td><td>164.80 (-10.97%)</td><td>146.76 (-9.87%)</td><td>144.60 (-12.15%)</td><td>131.00 (-8.01%)</td><td>14.84 (-6.18%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>162.84 (n/a)</td><td>164.60 (n/a)</td><td>142.40 (n/a)</td><td>15.82 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+24.10%)</b></td><td>0.04 (+15.48%)</td><td>0.04 <b>(+21.54%)</b></td><td>0.03 (+2.81%)</td><td>0.01 <b>(+95.43%)</b></td><td>193.80 (-2.76%)</td><td>154.76 (-12.23%)</td><td>144.30 (-17.73%)</td><td>127.40 (-19.42%)</td><td>25.42 <b>(+55.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>176.32 (n/a)</td><td>175.40 (n/a)</td><td>158.10 (n/a)</td><td>16.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (+7.08%)</td><td>0.04 <b>(+20.72%)</b></td><td>0.05 <b>(+29.71%)</b></td><td>0.03 (+17.95%)</td><td>0.01 (-12.01%)</td><td>191.00 (-15.19%)</td><td>148.86 (-18.44%)</td><td>133.60 <b>(-22.86%)</b></td><td>129.10 (-6.58%)</td><td>26.54 <b>(-33.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>182.52 (n/a)</td><td>173.20 (n/a)</td><td>138.20 (n/a)</td><td>39.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (+9.95%)</td><td>0.04 (+4.70%)</td><td>0.03 (+1.26%)</td><td>0.02 (-2.17%)</td><td>0.01 <b>(+22.46%)</b></td><td>247.30 (+2.19%)</td><td>182.12 (-3.37%)</td><td>177.90 (-1.22%)</td><td>130.80 (-9.04%)</td><td>42.87 (+13.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>188.48 (n/a)</td><td>180.10 (n/a)</td><td>143.80 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (-2.11%)</td><td>0.04 (+11.87%)</td><td>0.04 <b>(+20.19%)</b></td><td>0.03 (+13.90%)</td><td>0.00 <b>(-25.91%)</b></td><td>201.60 (-12.23%)</td><td>174.06 (-11.40%)</td><td>163.20 (-16.82%)</td><td>157.60 (+2.14%)</td><td>18.93 <b>(-32.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>229.70 (n/a)</td><td>196.46 (n/a)</td><td>196.20 (n/a)</td><td>154.30 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (+3.71%)</td><td>0.08 (+1.98%)</td><td>0.08 (+9.66%)</td><td>0.06 (-5.60%)</td><td>0.02 (+17.09%)</td><td>194.50 (+5.94%)</td><td>159.06 (-1.09%)</td><td>159.10 (-8.77%)</td><td>126.40 (-3.51%)</td><td>30.69 (+19.07%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>160.82 (n/a)</td><td>174.40 (n/a)</td><td>131.00 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (+5.11%)</td><td>0.07 (-4.36%)</td><td>0.07 (-1.57%)</td><td>0.03 <b>(-43.27%)</b></td><td>0.02 <b>(+90.56%)</b></td><td>371.20 <b>(+76.26%)</b></td><td>205.52 (+16.56%)</td><td>186.60 (+1.58%)</td><td>130.80 (-4.87%)</td><td>96.38 <b>(+236.31%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>176.32 (n/a)</td><td>183.70 (n/a)</td><td>137.50 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (-2.80%)</td><td>0.07 (-16.30%)</td><td>0.07 <b>(-21.92%)</b></td><td>0.05 <b>(-23.40%)</b></td><td>0.02 (+11.32%)</td><td>244.20 <b>(+30.52%)</b></td><td>184.54 <b>(+21.42%)</b></td><td>181.50 <b>(+28.09%)</b></td><td>126.90 (+2.92%)</td><td>42.43 <b>(+45.13%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>151.98 (n/a)</td><td>141.70 (n/a)</td><td>123.30 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (+5.76%)</td><td>0.08 (+8.28%)</td><td>0.07 (+3.09%)</td><td>0.06 (-3.46%)</td><td>0.02 <b>(+42.75%)</b></td><td>213.90 (+3.58%)</td><td>163.30 (-5.75%)</td><td>170.50 (-3.01%)</td><td>125.00 (-5.45%)</td><td>37.00 <b>(+38.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>173.26 (n/a)</td><td>175.80 (n/a)</td><td>132.20 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (-10.88%)</td><td>0.08 (+5.08%)</td><td>0.07 (+11.86%)</td><td>0.07 (+14.44%)</td><td>0.01 <b>(-46.82%)</b></td><td>179.60 (-12.65%)</td><td>162.80 (-7.30%)</td><td>171.10 (-10.61%)</td><td>134.60 (+12.26%)</td><td>17.92 <b>(-46.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>205.60 (n/a)</td><td>175.62 (n/a)</td><td>191.40 (n/a)</td><td>119.90 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (+2.01%)</td><td>0.07 (+5.36%)</td><td>0.07 (+2.44%)</td><td>0.06 (+9.19%)</td><td>0.01 (-0.45%)</td><td>200.70 (-8.40%)</td><td>170.38 (-5.30%)</td><td>175.10 (-2.40%)</td><td>131.20 (-1.94%)</td><td>29.25 (-8.66%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>179.92 (n/a)</td><td>179.40 (n/a)</td><td>133.80 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 <b>(-27.20%)</b></td><td>0.06 (-5.80%)</td><td>0.06 (+12.57%)</td><td>0.05 <b>(+36.76%)</b></td><td>0.01 <b>(-62.02%)</b></td><td>244.40 <b>(-26.89%)</b></td><td>203.42 (-3.94%)</td><td>196.90 (-11.19%)</td><td>162.70 <b>(+37.42%)</b></td><td>31.39 <b>(-61.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>334.30 (n/a)</td><td>211.76 (n/a)</td><td>221.70 (n/a)</td><td>118.40 (n/a)</td><td>81.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (-11.79%)</td><td>0.06 (+5.02%)</td><td>0.07 (+13.90%)</td><td>0.04 (+8.61%)</td><td>0.01 <b>(-23.98%)</b></td><td>306.50 (-7.93%)</td><td>205.58 (-7.12%)</td><td>188.50 (-12.16%)</td><td>161.60 (+13.32%)</td><td>57.52 (-17.26%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>332.90 (n/a)</td><td>221.34 (n/a)</td><td>214.60 (n/a)</td><td>142.60 (n/a)</td><td>69.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 <b>(+21.18%)</b></td><td>0.17 (+17.51%)</td><td>0.16 (+15.60%)</td><td>0.15 <b>(+26.28%)</b></td><td>0.02 (+1.40%)</td><td>164.80 <b>(-20.81%)</b></td><td>149.92 (-15.18%)</td><td>152.30 (-13.47%)</td><td>129.00 (-17.47%)</td><td>13.71 <b>(-34.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>176.76 (n/a)</td><td>176.00 (n/a)</td><td>156.30 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (-5.63%)</td><td>0.15 (+6.72%)</td><td>0.15 (+12.48%)</td><td>0.14 (+18.07%)</td><td>0.01 <b>(-69.70%)</b></td><td>172.20 (-15.34%)</td><td>167.02 (-7.37%)</td><td>168.40 (-11.13%)</td><td>157.10 (+6.01%)</td><td>5.86 <b>(-72.90%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.40 (n/a)</td><td>180.30 (n/a)</td><td>189.50 (n/a)</td><td>148.20 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (+8.23%)</td><td>0.17 (+9.92%)</td><td>0.17 <b>(+21.72%)</b></td><td>0.14 (+8.06%)</td><td>0.03 (-6.73%)</td><td>174.60 (-7.47%)</td><td>146.74 (-9.59%)</td><td>145.10 (-17.84%)</td><td>121.10 (-7.63%)</td><td>22.73 (-18.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.70 (n/a)</td><td>162.30 (n/a)</td><td>176.60 (n/a)</td><td>131.10 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (-3.79%)</td><td>0.15 (+8.85%)</td><td>0.15 (+6.50%)</td><td>0.12 <b>(+21.94%)</b></td><td>0.02 <b>(-31.10%)</b></td><td>200.50 (-18.00%)</td><td>166.26 (-10.34%)</td><td>164.80 (-6.15%)</td><td>135.70 (+3.98%)</td><td>24.70 <b>(-40.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.50 (n/a)</td><td>185.44 (n/a)</td><td>175.60 (n/a)</td><td>130.50 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (+4.66%)</td><td>0.14 (-10.73%)</td><td>0.13 (-13.78%)</td><td>0.08 <b>(-36.93%)</b></td><td>0.04 <b>(+126.87%)</b></td><td>293.40 <b>(+58.51%)</b></td><td>191.98 (+19.60%)</td><td>187.50 (+16.03%)</td><td>129.30 (-4.43%)</td><td>62.75 <b>(+252.72%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>185.10 (n/a)</td><td>160.52 (n/a)</td><td>161.60 (n/a)</td><td>135.30 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (+8.20%)</td><td>0.14 (-7.80%)</td><td>0.13 (-5.92%)</td><td>0.07 <b>(-42.46%)</b></td><td>0.05 <b>(+57.42%)</b></td><td>359.60 <b>(+73.80%)</b></td><td>201.40 (+19.72%)</td><td>182.90 (+6.34%)</td><td>123.10 (-7.58%)</td><td>93.11 <b>(+172.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>206.90 (n/a)</td><td>168.22 (n/a)</td><td>172.00 (n/a)</td><td>133.20 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (-17.94%)</td><td>0.13 (-9.23%)</td><td>0.13 (-13.03%)</td><td>0.11 (-3.18%)</td><td>0.02 <b>(-28.97%)</b></td><td>218.30 (+3.26%)</td><td>187.16 (+9.09%)</td><td>195.80 (+14.97%)</td><td>158.80 <b>(+21.87%)</b></td><td>26.54 (-12.39%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.40 (n/a)</td><td>171.56 (n/a)</td><td>170.30 (n/a)</td><td>130.30 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (+0.21%)</td><td>0.14 (+2.19%)</td><td>0.15 (+9.14%)</td><td>0.11 (-7.73%)</td><td>0.02 <b>(+37.56%)</b></td><td>214.00 (+8.41%)</td><td>177.54 (-1.41%)</td><td>169.10 (-8.35%)</td><td>154.50 (-0.26%)</td><td>24.48 <b>(+50.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>180.08 (n/a)</td><td>184.50 (n/a)</td><td>154.90 (n/a)</td><td>16.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (-4.58%)</td><td>0.28 (-5.87%)</td><td>0.27 (-8.99%)</td><td>0.21 (-15.34%)</td><td>0.06 (+7.77%)</td><td>236.30 (+18.09%)</td><td>180.68 (+7.47%)</td><td>184.70 (+9.88%)</td><td>129.20 (+4.79%)</td><td>38.73 <b>(+35.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>200.10 (n/a)</td><td>168.12 (n/a)</td><td>168.10 (n/a)</td><td>123.30 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.36 (-16.40%)</td><td>0.30 (-1.75%)</td><td>0.29 (+3.32%)</td><td>0.25 (+2.14%)</td><td>0.05 <b>(-33.90%)</b></td><td>199.80 (-2.11%)</td><td>168.26 (-0.07%)</td><td>169.50 (-3.20%)</td><td>135.10 (+19.56%)</td><td>27.62 (-18.46%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>204.10 (n/a)</td><td>168.38 (n/a)</td><td>175.10 (n/a)</td><td>113.00 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (+3.72%)</td><td>0.29 (-0.04%)</td><td>0.27 (-2.51%)</td><td>0.22 (-3.61%)</td><td>0.06 (+8.89%)</td><td>223.00 (+3.72%)</td><td>174.56 (+0.53%)</td><td>181.20 (+2.60%)</td><td>128.60 (-3.60%)</td><td>35.17 (+8.38%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>215.00 (n/a)</td><td>173.64 (n/a)</td><td>176.60 (n/a)</td><td>133.40 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 (-6.15%)</td><td>0.30 (-11.20%)</td><td>0.27 (-11.75%)</td><td>0.23 (-15.45%)</td><td>0.08 (+10.71%)</td><td>213.10 (+18.26%)</td><td>173.58 (+14.62%)</td><td>184.90 (+13.30%)</td><td>124.90 (+6.57%)</td><td>41.37 <b>(+41.73%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>180.20 (n/a)</td><td>151.44 (n/a)</td><td>163.20 (n/a)</td><td>117.20 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 (-16.78%)</td><td>0.28 (-8.83%)</td><td>0.29 (+2.81%)</td><td>0.23 (-11.36%)</td><td>0.03 <b>(-41.43%)</b></td><td>211.90 (+12.83%)</td><td>177.20 (+8.45%)</td><td>170.50 (-2.74%)</td><td>156.90 <b>(+20.14%)</b></td><td>21.00 (-19.12%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>187.80 (n/a)</td><td>163.40 (n/a)</td><td>175.30 (n/a)</td><td>130.60 (n/a)</td><td>25.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 (-6.97%)</td><td>0.30 (-1.75%)</td><td>0.32 (+13.63%)</td><td>0.22 (-11.39%)</td><td>0.07 (+10.40%)</td><td>219.50 (+12.85%)</td><td>171.80 (+3.54%)</td><td>154.90 (-11.99%)</td><td>127.50 (+7.50%)</td><td>42.17 <b>(+43.35%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.41 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>194.50 (n/a)</td><td>165.92 (n/a)</td><td>176.00 (n/a)</td><td>118.60 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.39 <b>(+26.18%)</b></td><td>0.30 <b>(+22.26%)</b></td><td>0.37 <b>(+71.05%)</b></td><td>0.16 <b>(-20.06%)</b></td><td>0.11 <b>(+97.49%)</b></td><td>309.40 <b>(+25.06%)</b></td><td>184.46 (-10.36%)</td><td>134.20 <b>(-41.53%)</b></td><td>124.70 <b>(-20.78%)</b></td><td>80.36 <b>(+93.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>247.40 (n/a)</td><td>205.78 (n/a)</td><td>229.50 (n/a)</td><td>157.40 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.37 (+13.12%)</td><td>0.29 (+18.88%)</td><td>0.29 <b>(+29.21%)</b></td><td>0.25 <b>(+51.64%)</b></td><td>0.05 <b>(-29.04%)</b></td><td>200.60 <b>(-34.03%)</b></td><td>170.20 (-19.51%)</td><td>169.90 <b>(-22.60%)</b></td><td>132.60 (-11.60%)</td><td>25.61 <b>(-58.21%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>304.10 (n/a)</td><td>211.46 (n/a)</td><td>219.50 (n/a)</td><td>150.00 (n/a)</td><td>61.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (+10.33%)</td><td>0.02 (-0.63%)</td><td>0.02 (-4.42%)</td><td>0.01 (-1.23%)</td><td>0.00 <b>(+34.18%)</b></td><td>186.10 (+1.25%)</td><td>152.82 (+1.92%)</td><td>153.00 (+4.65%)</td><td>109.40 (-9.36%)</td><td>29.37 <b>(+20.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>149.94 (n/a)</td><td>146.20 (n/a)</td><td>120.70 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (+10.59%)</td><td>0.02 (-6.81%)</td><td>0.02 (-5.88%)</td><td>0.01 (-0.96%)</td><td>0.00 <b>(+35.16%)</b></td><td>212.00 (+1.00%)</td><td>161.68 (+9.99%)</td><td>141.10 (+6.25%)</td><td>115.10 (-9.58%)</td><td>44.90 <b>(+27.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>147.00 (n/a)</td><td>132.80 (n/a)</td><td>127.30 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-14.38%)</td><td>0.01 <b>(-20.13%)</b></td><td>0.02 (-14.60%)</td><td>0.01 <b>(-37.76%)</b></td><td>0.00 <b>(+85.71%)</b></td><td>244.60 <b>(+60.60%)</b></td><td>184.40 <b>(+28.23%)</b></td><td>172.40 (+17.12%)</td><td>147.80 (+16.84%)</td><td>36.70 <b>(+262.40%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>152.30 (n/a)</td><td>143.80 (n/a)</td><td>147.20 (n/a)</td><td>126.50 (n/a)</td><td>10.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 <b>(+31.73%)</b></td><td>0.02 (+9.05%)</td><td>0.01 (-6.39%)</td><td>0.01 <b>(+38.39%)</b></td><td>0.00 (+13.14%)</td><td>225.40 <b>(-27.76%)</b></td><td>173.66 (-10.48%)</td><td>176.30 (+6.85%)</td><td>118.10 <b>(-24.10%)</b></td><td>38.03 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>312.00 (n/a)</td><td>193.98 (n/a)</td><td>165.00 (n/a)</td><td>155.60 (n/a)</td><td>66.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-5.61%)</td><td>0.01 (-15.89%)</td><td>0.01 (-16.08%)</td><td>0.01 <b>(-24.02%)</b></td><td>0.00 <b>(+87.86%)</b></td><td>216.20 <b>(+31.67%)</b></td><td>184.16 <b>(+20.65%)</b></td><td>187.20 (+19.16%)</td><td>147.20 (+5.90%)</td><td>27.27 <b>(+162.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.20 (n/a)</td><td>152.64 (n/a)</td><td>157.10 (n/a)</td><td>139.00 (n/a)</td><td>10.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 <b>(+30.14%)</b></td><td>0.01 (-3.85%)</td><td>0.01 <b>(-20.26%)</b></td><td>0.01 (-14.98%)</td><td>0.01 <b>(+92.74%)</b></td><td>290.20 (+17.63%)</td><td>195.84 (+10.77%)</td><td>201.20 <b>(+25.44%)</b></td><td>116.40 <b>(-23.17%)</b></td><td>65.67 <b>(+66.20%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>246.70 (n/a)</td><td>176.80 (n/a)</td><td>160.40 (n/a)</td><td>151.50 (n/a)</td><td>39.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-4.98%)</td><td>0.02 (-10.41%)</td><td>0.02 (-8.72%)</td><td>0.01 (-17.37%)</td><td>0.00 <b>(+39.17%)</b></td><td>216.50 <b>(+21.02%)</b></td><td>177.46 (+13.26%)</td><td>166.20 (+9.56%)</td><td>146.40 (+5.25%)</td><td>31.60 <b>(+78.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>178.90 (n/a)</td><td>156.68 (n/a)</td><td>151.70 (n/a)</td><td>139.10 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-9.18%)</td><td>0.01 (-15.44%)</td><td>0.01 (-15.32%)</td><td>0.01 <b>(-25.81%)</b></td><td>0.00 <b>(+64.28%)</b></td><td>261.60 <b>(+34.78%)</b></td><td>217.12 <b>(+21.32%)</b></td><td>218.00 (+18.09%)</td><td>166.10 (+10.15%)</td><td>43.95 <b>(+149.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>178.96 (n/a)</td><td>184.60 (n/a)</td><td>150.80 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (+9.04%)</td><td>0.03 (+8.71%)</td><td>0.03 (+2.97%)</td><td>0.03 (+6.99%)</td><td>0.01 <b>(+27.66%)</b></td><td>193.90 (-6.55%)</td><td>154.54 (-7.29%)</td><td>159.00 (-2.87%)</td><td>121.10 (-8.33%)</td><td>29.15 (+7.48%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>166.70 (n/a)</td><td>163.70 (n/a)</td><td>132.10 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+30.75%)</b></td><td>0.04 (+0.41%)</td><td>0.03 (-13.58%)</td><td>0.03 (-10.10%)</td><td>0.01 <b>(+178.48%)</b></td><td>185.00 (+11.24%)</td><td>154.32 (+3.18%)</td><td>168.00 (+15.70%)</td><td>103.00 <b>(-23.53%)</b></td><td>31.70 <b>(+127.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>166.30 (n/a)</td><td>149.56 (n/a)</td><td>145.20 (n/a)</td><td>134.70 (n/a)</td><td>13.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+22.15%)</b></td><td>0.04 (+16.96%)</td><td>0.04 (+8.73%)</td><td>0.03 <b>(+26.56%)</b></td><td>0.01 (+7.48%)</td><td>163.50 <b>(-20.98%)</b></td><td>134.24 (-15.20%)</td><td>139.30 (-7.99%)</td><td>102.90 (-18.14%)</td><td>22.52 <b>(-31.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>158.30 (n/a)</td><td>151.40 (n/a)</td><td>125.70 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (+14.32%)</td><td>0.03 (-3.76%)</td><td>0.03 (-0.43%)</td><td>0.02 <b>(-32.71%)</b></td><td>0.01 <b>(+305.41%)</b></td><td>230.30 <b>(+48.58%)</b></td><td>161.64 (+10.18%)</td><td>152.80 (+0.46%)</td><td>118.70 (-12.53%)</td><td>46.44 <b>(+415.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.00 (n/a)</td><td>146.70 (n/a)</td><td>152.10 (n/a)</td><td>135.70 (n/a)</td><td>9.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(+24.07%)</b></td><td>0.03 (-7.05%)</td><td>0.03 (-11.63%)</td><td>0.01 <b>(-40.28%)</b></td><td>0.01 <b>(+126.59%)</b></td><td>369.30 <b>(+67.48%)</b></td><td>207.94 <b>(+22.06%)</b></td><td>190.60 (+13.12%)</td><td>108.70 (-19.42%)</td><td>96.77 <b>(+209.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>170.36 (n/a)</td><td>168.50 (n/a)</td><td>134.90 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (+4.85%)</td><td>0.03 (+5.13%)</td><td>0.03 (+5.41%)</td><td>0.03 (+10.50%)</td><td>0.00 (-0.03%)</td><td>202.90 (-9.50%)</td><td>169.06 (-5.14%)</td><td>155.80 (-5.12%)</td><td>144.70 (-4.61%)</td><td>25.73 (-13.53%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.20 (n/a)</td><td>178.22 (n/a)</td><td>164.20 (n/a)</td><td>151.70 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (-4.76%)</td><td>0.03 (-3.84%)</td><td>0.03 (-7.25%)</td><td>0.03 (+19.61%)</td><td>0.00 <b>(-29.34%)</b></td><td>189.60 (-16.40%)</td><td>167.54 (+1.95%)</td><td>170.50 (+7.84%)</td><td>135.20 (+4.97%)</td><td>22.14 <b>(-40.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>164.34 (n/a)</td><td>158.10 (n/a)</td><td>128.80 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+12.68%)</td><td>0.03 (+14.42%)</td><td>0.03 <b>(+24.91%)</b></td><td>0.02 (+3.13%)</td><td>0.00 <b>(+58.13%)</b></td><td>238.40 (-3.01%)</td><td>198.84 (-11.85%)</td><td>187.20 (-19.93%)</td><td>170.30 (-11.26%)</td><td>28.67 <b>(+38.98%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.80 (n/a)</td><td>225.56 (n/a)</td><td>233.80 (n/a)</td><td>191.90 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (+6.85%)</td><td>0.06 (-10.15%)</td><td>0.06 (-15.05%)</td><td>0.05 (-17.25%)</td><td>0.01 <b>(+94.00%)</b></td><td>197.80 <b>(+20.83%)</b></td><td>170.10 (+13.38%)</td><td>172.70 (+17.72%)</td><td>128.80 (-6.46%)</td><td>28.46 <b>(+119.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>163.70 (n/a)</td><td>150.02 (n/a)</td><td>146.70 (n/a)</td><td>137.70 (n/a)</td><td>12.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (+15.63%)</td><td>0.07 <b>(+25.02%)</b></td><td>0.07 (+17.96%)</td><td>0.06 <b>(+61.80%)</b></td><td>0.01 <b>(-26.95%)</b></td><td>167.20 <b>(-38.19%)</b></td><td>143.14 <b>(-22.76%)</b></td><td>144.00 (-15.19%)</td><td>121.60 (-13.51%)</td><td>18.68 <b>(-62.86%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>270.50 (n/a)</td><td>185.32 (n/a)</td><td>169.80 (n/a)</td><td>140.60 (n/a)</td><td>50.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (-12.81%)</td><td>0.07 (-7.75%)</td><td>0.07 (+2.21%)</td><td>0.05 (-13.84%)</td><td>0.01 (-3.81%)</td><td>193.70 (+16.06%)</td><td>162.48 (+8.78%)</td><td>155.20 (-2.14%)</td><td>137.80 (+14.64%)</td><td>24.87 <b>(+28.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>166.90 (n/a)</td><td>149.36 (n/a)</td><td>158.60 (n/a)</td><td>120.20 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (-13.29%)</td><td>0.06 (-1.12%)</td><td>0.06 (-0.82%)</td><td>0.04 (+5.88%)</td><td>0.01 (-19.66%)</td><td>243.50 (-5.55%)</td><td>183.82 (-0.37%)</td><td>177.20 (+0.80%)</td><td>146.30 (+15.29%)</td><td>40.38 (-14.68%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>257.80 (n/a)</td><td>184.50 (n/a)</td><td>175.80 (n/a)</td><td>126.90 (n/a)</td><td>47.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (-1.50%)</td><td>0.07 (+3.72%)</td><td>0.06 (+0.05%)</td><td>0.06 (+9.54%)</td><td>0.01 (-12.02%)</td><td>186.00 (-8.69%)</td><td>163.08 (-4.19%)</td><td>169.60 (-0.06%)</td><td>128.90 (+1.58%)</td><td>24.06 (-16.27%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>170.22 (n/a)</td><td>169.70 (n/a)</td><td>126.90 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (-7.98%)</td><td>0.06 (+0.45%)</td><td>0.06 (+7.25%)</td><td>0.04 (-2.53%)</td><td>0.01 (-19.79%)</td><td>235.20 (+2.57%)</td><td>190.76 (-1.30%)</td><td>182.70 (-6.79%)</td><td>155.90 (+8.72%)</td><td>31.94 (-11.52%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>193.28 (n/a)</td><td>196.00 (n/a)</td><td>143.40 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (-10.70%)</td><td>0.06 (+1.47%)</td><td>0.07 (+7.24%)</td><td>0.05 (+11.66%)</td><td>0.01 <b>(-37.02%)</b></td><td>203.50 (-10.47%)</td><td>165.02 (-3.26%)</td><td>155.10 (-6.73%)</td><td>150.60 (+11.97%)</td><td>22.08 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>170.58 (n/a)</td><td>166.30 (n/a)</td><td>134.50 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-14.98%)</td><td>0.05 (-15.44%)</td><td>0.05 (-12.97%)</td><td>0.03 <b>(-24.43%)</b></td><td>0.01 (-1.73%)</td><td>340.40 <b>(+32.35%)</b></td><td>237.72 <b>(+20.13%)</b></td><td>204.60 (+14.88%)</td><td>185.90 (+17.66%)</td><td>62.89 <b>(+53.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>257.20 (n/a)</td><td>197.88 (n/a)</td><td>178.10 (n/a)</td><td>158.00 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 <b>(-26.89%)</b></td><td>0.12 <b>(-21.04%)</b></td><td>0.12 (-12.76%)</td><td>0.09 <b>(-29.12%)</b></td><td>0.02 <b>(-29.21%)</b></td><td>240.10 <b>(+41.07%)</b></td><td>182.22 <b>(+26.66%)</b></td><td>173.10 (+14.64%)</td><td>157.10 <b>(+36.73%)</b></td><td>33.09 <b>(+42.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>170.20 (n/a)</td><td>143.86 (n/a)</td><td>151.00 (n/a)</td><td>114.90 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 <b>(+24.81%)</b></td><td>0.12 (-12.78%)</td><td>0.11 <b>(-21.30%)</b></td><td>0.08 <b>(-35.70%)</b></td><td>0.04 <b>(+374.38%)</b></td><td>266.50 <b>(+55.58%)</b></td><td>194.72 <b>(+25.04%)</b></td><td>198.00 <b>(+27.09%)</b></td><td>114.70 (-19.85%)</td><td>60.78 <b>(+487.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>171.30 (n/a)</td><td>155.72 (n/a)</td><td>155.80 (n/a)</td><td>143.10 (n/a)</td><td>10.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (-3.32%)</td><td>0.10 <b>(-20.47%)</b></td><td>0.12 (-14.06%)</td><td>0.06 <b>(-43.87%)</b></td><td>0.03 <b>(+66.61%)</b></td><td>377.50 <b>(+78.15%)</b></td><td>224.48 <b>(+36.88%)</b></td><td>180.20 (+16.33%)</td><td>146.80 (+3.45%)</td><td>91.66 <b>(+218.86%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>164.00 (n/a)</td><td>154.90 (n/a)</td><td>141.90 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (-5.10%)</td><td>0.11 (-10.36%)</td><td>0.11 (-5.62%)</td><td>0.09 (-17.77%)</td><td>0.02 <b>(+24.40%)</b></td><td>230.70 <b>(+21.61%)</b></td><td>188.22 (+13.22%)</td><td>183.60 (+6.00%)</td><td>140.40 (+5.33%)</td><td>35.31 <b>(+62.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>166.24 (n/a)</td><td>173.20 (n/a)</td><td>133.30 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (-17.42%)</td><td>0.10 <b>(-25.05%)</b></td><td>0.10 <b>(-27.77%)</b></td><td>0.07 <b>(-36.75%)</b></td><td>0.02 <b>(+23.50%)</b></td><td>280.40 <b>(+58.15%)</b></td><td>209.14 <b>(+36.43%)</b></td><td>203.30 <b>(+38.49%)</b></td><td>157.00 <b>(+21.05%)</b></td><td>44.59 <b>(+139.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.30 (n/a)</td><td>153.30 (n/a)</td><td>146.80 (n/a)</td><td>129.70 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 <b>(-25.03%)</b></td><td>0.10 <b>(-29.80%)</b></td><td>0.10 <b>(-33.44%)</b></td><td>0.08 <b>(-28.94%)</b></td><td>0.02 <b>(-28.82%)</b></td><td>248.70 <b>(+40.75%)</b></td><td>208.38 <b>(+42.30%)</b></td><td>216.90 <b>(+50.21%)</b></td><td>162.40 <b>(+33.33%)</b></td><td>32.88 <b>(+33.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>146.44 (n/a)</td><td>144.40 (n/a)</td><td>121.80 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (-4.93%)</td><td>0.12 (-11.00%)</td><td>0.12 (-11.43%)</td><td>0.09 (-5.91%)</td><td>0.02 (-4.22%)</td><td>223.00 (+6.29%)</td><td>174.24 (+12.31%)</td><td>168.90 (+12.90%)</td><td>129.60 (+5.19%)</td><td>34.21 (+3.64%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>209.80 (n/a)</td><td>155.14 (n/a)</td><td>149.60 (n/a)</td><td>123.20 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (-4.72%)</td><td>0.10 (-2.42%)</td><td>0.10 (+3.72%)</td><td>0.08 (-9.33%)</td><td>0.01 (-0.35%)</td><td>248.20 (+10.31%)</td><td>217.38 (+2.60%)</td><td>211.80 (-3.60%)</td><td>186.20 (+4.96%)</td><td>23.02 (+16.33%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>211.88 (n/a)</td><td>219.70 (n/a)</td><td>177.40 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>180.78 (n/a)</td><td>193.50 (n/a)</td><td>129.60 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>191.32 (n/a)</td><td>192.60 (n/a)</td><td>148.10 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>159.58 (n/a)</td><td>156.50 (n/a)</td><td>127.10 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>178.74 (n/a)</td><td>189.10 (n/a)</td><td>134.50 (n/a)</td><td>40.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>184.78 (n/a)</td><td>185.90 (n/a)</td><td>119.40 (n/a)</td><td>43.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>174.96 (n/a)</td><td>163.30 (n/a)</td><td>147.80 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>305.60 (n/a)</td><td>208.06 (n/a)</td><td>180.80 (n/a)</td><td>158.10 (n/a)</td><td>62.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>205.88 (n/a)</td><td>209.70 (n/a)</td><td>188.50 (n/a)</td><td>15.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>187.30 (n/a)</td><td>187.70 (n/a)</td><td>163.00 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>232.10 (n/a)</td><td>195.28 (n/a)</td><td>216.00 (n/a)</td><td>122.10 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.90 (n/a)</td><td>179.24 (n/a)</td><td>179.10 (n/a)</td><td>143.60 (n/a)</td><td>32.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>253.50 (n/a)</td><td>222.98 (n/a)</td><td>221.60 (n/a)</td><td>200.90 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (-4.89%)</td><td>0.28 (+4.03%)</td><td>0.28 (+6.09%)</td><td>0.21 (+14.44%)</td><td>0.04 <b>(-34.17%)</b></td><td>230.90 (-12.64%)</td><td>180.64 (-6.73%)</td><td>177.30 (-5.74%)</td><td>151.50 (+5.14%)</td><td>31.27 <b>(-37.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>264.30 (n/a)</td><td>193.68 (n/a)</td><td>188.10 (n/a)</td><td>144.10 (n/a)</td><td>50.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>216.50 (n/a)</td><td>172.26 (n/a)</td><td>151.70 (n/a)</td><td>148.20 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>207.40 (n/a)</td><td>182.14 (n/a)</td><td>187.90 (n/a)</td><td>149.30 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>223.20 (n/a)</td><td>191.66 (n/a)</td><td>198.80 (n/a)</td><td>134.20 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>155.14 (n/a)</td><td>131.30 (n/a)</td><td>118.60 (n/a)</td><td>45.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>158.80 (n/a)</td><td>141.90 (n/a)</td><td>125.40 (n/a)</td><td>37.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>230.20 (n/a)</td><td>184.60 (n/a)</td><td>176.00 (n/a)</td><td>158.30 (n/a)</td><td>28.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>227.40 (n/a)</td><td>204.62 (n/a)</td><td>213.20 (n/a)</td><td>172.90 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>185.06 (n/a)</td><td>178.80 (n/a)</td><td>154.10 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>231.80 (n/a)</td><td>166.50 (n/a)</td><td>176.60 (n/a)</td><td>111.00 (n/a)</td><td>50.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>220.30 (n/a)</td><td>187.86 (n/a)</td><td>204.70 (n/a)</td><td>115.00 (n/a)</td><td>42.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>195.04 (n/a)</td><td>185.30 (n/a)</td><td>173.80 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>166.24 (n/a)</td><td>157.50 (n/a)</td><td>123.50 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>345.10 (n/a)</td><td>191.10 (n/a)</td><td>162.40 (n/a)</td><td>122.80 (n/a)</td><td>90.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.70 (n/a)</td><td>166.46 (n/a)</td><td>168.30 (n/a)</td><td>127.10 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>197.92 (n/a)</td><td>202.40 (n/a)</td><td>181.90 (n/a)</td><td>13.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>197.18 (n/a)</td><td>199.00 (n/a)</td><td>181.60 (n/a)</td><td>9.42 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>190.90 (n/a)</td><td>158.86 (n/a)</td><td>149.40 (n/a)</td><td>119.70 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>256.20 (n/a)</td><td>217.20 (n/a)</td><td>214.30 (n/a)</td><td>188.30 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.10 (n/a)</td><td>155.78 (n/a)</td><td>155.40 (n/a)</td><td>139.50 (n/a)</td><td>13.68 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.70 (n/a)</td><td>159.82 (n/a)</td><td>161.80 (n/a)</td><td>141.70 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.10 (n/a)</td><td>152.86 (n/a)</td><td>148.20 (n/a)</td><td>136.30 (n/a)</td><td>15.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.90 (n/a)</td><td>143.30 (n/a)</td><td>134.00 (n/a)</td><td>113.90 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.60 (n/a)</td><td>154.66 (n/a)</td><td>154.60 (n/a)</td><td>138.60 (n/a)</td><td>13.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>178.12 (n/a)</td><td>170.20 (n/a)</td><td>139.60 (n/a)</td><td>35.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.80 (n/a)</td><td>179.80 (n/a)</td><td>184.10 (n/a)</td><td>141.00 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.30 (n/a)</td><td>211.66 (n/a)</td><td>193.40 (n/a)</td><td>168.40 (n/a)</td><td>41.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>149.46 (n/a)</td><td>161.20 (n/a)</td><td>113.70 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>145.26 (n/a)</td><td>142.60 (n/a)</td><td>129.30 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>155.88 (n/a)</td><td>145.90 (n/a)</td><td>114.10 (n/a)</td><td>36.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>159.54 (n/a)</td><td>156.80 (n/a)</td><td>127.10 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>163.58 (n/a)</td><td>176.90 (n/a)</td><td>133.10 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>256.90 (n/a)</td><td>179.88 (n/a)</td><td>184.40 (n/a)</td><td>114.40 (n/a)</td><td>59.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.30 (n/a)</td><td>163.06 (n/a)</td><td>159.50 (n/a)</td><td>147.10 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.10 (n/a)</td><td>200.28 (n/a)</td><td>178.20 (n/a)</td><td>166.80 (n/a)</td><td>54.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.00 (n/a)</td><td>143.96 (n/a)</td><td>147.10 (n/a)</td><td>116.90 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>236.00 (n/a)</td><td>168.64 (n/a)</td><td>178.80 (n/a)</td><td>110.30 (n/a)</td><td>47.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>182.08 (n/a)</td><td>181.00 (n/a)</td><td>140.20 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>170.62 (n/a)</td><td>171.70 (n/a)</td><td>143.30 (n/a)</td><td>18.63 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>183.18 (n/a)</td><td>202.60 (n/a)</td><td>143.80 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.40 (n/a)</td><td>178.86 (n/a)</td><td>176.20 (n/a)</td><td>130.20 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>246.80 (n/a)</td><td>189.72 (n/a)</td><td>211.70 (n/a)</td><td>129.60 (n/a)</td><td>52.33 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>278.30 (n/a)</td><td>214.06 (n/a)</td><td>212.20 (n/a)</td><td>181.30 (n/a)</td><td>39.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.40 (n/a)</td><td>180.44 (n/a)</td><td>183.80 (n/a)</td><td>154.70 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>294.60 (n/a)</td><td>207.52 (n/a)</td><td>192.90 (n/a)</td><td>165.00 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.60 (n/a)</td><td>177.02 (n/a)</td><td>167.40 (n/a)</td><td>139.20 (n/a)</td><td>36.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>199.24 (n/a)</td><td>204.30 (n/a)</td><td>162.10 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>258.50 (n/a)</td><td>178.18 (n/a)</td><td>144.40 (n/a)</td><td>115.30 (n/a)</td><td>64.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>194.36 (n/a)</td><td>183.90 (n/a)</td><td>163.50 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>183.46 (n/a)</td><td>189.10 (n/a)</td><td>159.00 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>310.60 (n/a)</td><td>238.80 (n/a)</td><td>217.10 (n/a)</td><td>192.30 (n/a)</td><td>54.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>4.24 (-0.39%)</td><td>3.83 (-4.00%)</td><td>3.71 (-9.97%)</td><td>3.47 (-3.92%)</td><td>0.36 <b>(+27.18%)</b></td><td>2710.50 (+4.08%)</td><td>2471.46 (+4.46%)</td><td>2533.10 (+11.07%)</td><td>2219.30 (+0.39%)</td><td>229.44 <b>(+31.81%)</b></td><td>1666.90 (-0.39%)</td><td>1507.42 (-4.00%)</td><td>1460.43 (-9.97%)</td><td>1364.83 (-3.92%)</td><td>142.54 <b>(+27.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>4.25 (n/a)</td><td>3.99 (n/a)</td><td>4.12 (n/a)</td><td>3.61 (n/a)</td><td>0.28 (n/a)</td><td>2604.30 (n/a)</td><td>2365.86 (n/a)</td><td>2280.60 (n/a)</td><td>2210.70 (n/a)</td><td>174.07 (n/a)</td><td>1673.39 (n/a)</td><td>1570.24 (n/a)</td><td>1622.09 (n/a)</td><td>1420.49 (n/a)</td><td>112.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.14 (+1.44%)</td><td>0.89 (-6.38%)</td><td>0.94 (-1.27%)</td><td>0.66 (-1.24%)</td><td>0.21 (+15.77%)</td><td>335.20 (+1.27%)</td><td>260.28 (+8.19%)</td><td>235.00 (+1.29%)</td><td>194.70 (-1.42%)</td><td>64.10 (+18.66%)</td><td>48.47 (+1.44%)</td><td>38.01 (-6.38%)</td><td>40.16 (-1.27%)</td><td>28.15 (-1.24%)</td><td>8.98 (+15.77%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.12 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.67 (n/a)</td><td>0.18 (n/a)</td><td>331.00 (n/a)</td><td>240.58 (n/a)</td><td>232.00 (n/a)</td><td>197.50 (n/a)</td><td>54.02 (n/a)</td><td>47.78 (n/a)</td><td>40.60 (n/a)</td><td>40.68 (n/a)</td><td>28.51 (n/a)</td><td>7.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.26 (+19.01%)</td><td>0.96 (+12.59%)</td><td>1.08 (+17.06%)</td><td>0.69 (+7.56%)</td><td>0.25 <b>(+30.71%)</b></td><td>320.30 (-7.02%)</td><td>244.34 (-9.76%)</td><td>204.80 (-14.60%)</td><td>175.70 (-15.97%)</td><td>68.60 (+4.70%)</td><td>53.72 (+19.01%)</td><td>41.05 (+12.59%)</td><td>46.08 (+17.06%)</td><td>29.46 (+7.56%)</td><td>10.86 <b>(+30.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.06 (n/a)</td><td>0.85 (n/a)</td><td>0.92 (n/a)</td><td>0.64 (n/a)</td><td>0.19 (n/a)</td><td>344.50 (n/a)</td><td>270.76 (n/a)</td><td>239.80 (n/a)</td><td>209.10 (n/a)</td><td>65.52 (n/a)</td><td>45.14 (n/a)</td><td>36.46 (n/a)</td><td>39.36 (n/a)</td><td>27.39 (n/a)</td><td>8.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.52 (-0.32%)</td><td>0.52 (-0.08%)</td><td>0.52 (-0.09%)</td><td>0.52 (+0.02%)</td><td>0.00 <b>(-32.99%)</b></td><td>48632.10 (-0.03%)</td><td>48504.70 (+0.07%)</td><td>48498.60 (+0.09%)</td><td>48388.10 (+0.32%)</td><td>103.15 <b>(-32.77%)</b></td><td>355.04 (-0.32%)</td><td>354.19 (-0.08%)</td><td>354.23 (-0.09%)</td><td>353.26 (+0.03%)</td><td>0.75 <b>(-32.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48644.30 (n/a)</td><td>48468.48 (n/a)</td><td>48456.70 (n/a)</td><td>48232.90 (n/a)</td><td>153.44 (n/a)</td><td>356.19 (n/a)</td><td>354.46 (n/a)</td><td>354.54 (n/a)</td><td>353.17 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (+2.21%)</td><td>0.21 (+0.45%)</td><td>0.21 (-0.06%)</td><td>0.21 (+0.37%)</td><td>0.00 <b>(+141.04%)</b></td><td>118818.00 (-0.37%)</td><td>117764.06 (-0.44%)</td><td>118294.10 (+0.06%)</td><td>114904.30 (-2.17%)</td><td>1620.64 <b>(+134.48%)</b></td><td>149.51 (+2.21%)</td><td>145.91 (+0.45%)</td><td>145.23 (-0.06%)</td><td>144.59 (+0.37%)</td><td>2.04 <b>(+141.05%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119254.20 (n/a)</td><td>118282.04 (n/a)</td><td>118218.80 (n/a)</td><td>117447.20 (n/a)</td><td>691.15 (n/a)</td><td>146.28 (n/a)</td><td>145.25 (n/a)</td><td>145.32 (n/a)</td><td>144.06 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.91 (+1.27%)</td><td>0.89 (+0.54%)</td><td>0.89 (+0.22%)</td><td>0.89 (+0.23%)</td><td>0.01 <b>(+71.87%)</b></td><td>28425.20 (-0.23%)</td><td>28148.38 (-0.53%)</td><td>28256.40 (-0.22%)</td><td>27661.90 (-1.25%)</td><td>303.86 <b>(+69.33%)</b></td><td>621.07 (+1.27%)</td><td>610.39 (+0.54%)</td><td>608.00 (+0.22%)</td><td>604.39 (+0.23%)</td><td>6.65 <b>(+71.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28490.20 (n/a)</td><td>28299.18 (n/a)</td><td>28317.90 (n/a)</td><td>28012.70 (n/a)</td><td>179.45 (n/a)</td><td>613.29 (n/a)</td><td>607.10 (n/a)</td><td>606.68 (n/a)</td><td>603.01 (n/a)</td><td>3.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.63 (+2.69%)</td><td>3.52 (+3.06%)</td><td>3.52 (+4.09%)</td><td>3.43 (+2.62%)</td><td>0.08 (-8.54%)</td><td>7336.90 (-2.55%)</td><td>7161.80 (-2.98%)</td><td>7155.40 (-3.93%)</td><td>6935.70 (-2.62%)</td><td>151.85 (-13.49%)</td><td>2477.03 (+2.69%)</td><td>2399.69 (+3.06%)</td><td>2400.97 (+4.09%)</td><td>2341.58 (+2.62%)</td><td>51.33 (-8.54%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.53 (n/a)</td><td>3.41 (n/a)</td><td>3.38 (n/a)</td><td>3.34 (n/a)</td><td>0.08 (n/a)</td><td>7528.90 (n/a)</td><td>7381.44 (n/a)</td><td>7448.30 (n/a)</td><td>7122.30 (n/a)</td><td>175.53 (n/a)</td><td>2412.11 (n/a)</td><td>2328.51 (n/a)</td><td>2306.55 (n/a)</td><td>2281.87 (n/a)</td><td>56.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.29 (+3.66%)</td><td>3.00 (+2.83%)</td><td>3.02 (+5.28%)</td><td>2.83 (+0.67%)</td><td>0.19 <b>(+27.50%)</b></td><td>8898.60 (-0.67%)</td><td>8412.66 (-2.64%)</td><td>8328.20 (-5.02%)</td><td>7649.90 (-3.53%)</td><td>514.20 <b>(+23.72%)</b></td><td>2245.78 (+3.66%)</td><td>2048.44 (+2.83%)</td><td>2062.85 (+5.28%)</td><td>1930.62 (+0.67%)</td><td>128.95 <b>(+27.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.17 (n/a)</td><td>2.92 (n/a)</td><td>2.87 (n/a)</td><td>2.81 (n/a)</td><td>0.15 (n/a)</td><td>8958.40 (n/a)</td><td>8641.14 (n/a)</td><td>8768.30 (n/a)</td><td>7929.90 (n/a)</td><td>415.61 (n/a)</td><td>2166.47 (n/a)</td><td>1992.04 (n/a)</td><td>1959.32 (n/a)</td><td>1917.73 (n/a)</td><td>101.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.36 (+0.94%)</td><td>3.22 (+1.12%)</td><td>3.19 (+0.74%)</td><td>3.13 (+1.53%)</td><td>0.09 (-2.16%)</td><td>8034.60 (-1.51%)</td><td>7827.28 (-1.12%)</td><td>7900.90 (-0.74%)</td><td>7499.20 (-0.93%)</td><td>204.34 (-4.35%)</td><td>2290.89 (+0.94%)</td><td>2196.09 (+1.12%)</td><td>2174.41 (+0.74%)</td><td>2138.24 (+1.53%)</td><td>58.49 (-2.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.32 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>3.08 (n/a)</td><td>0.09 (n/a)</td><td>8157.50 (n/a)</td><td>7915.60 (n/a)</td><td>7959.60 (n/a)</td><td>7569.70 (n/a)</td><td>213.63 (n/a)</td><td>2269.56 (n/a)</td><td>2171.67 (n/a)</td><td>2158.39 (n/a)</td><td>2106.01 (n/a)</td><td>59.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.79 (-0.20%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.01%)</td><td>0.79 (+0.22%)</td><td>0.00 <b>(-94.01%)</b></td><td>96120.50 (-0.21%)</td><td>96106.24 (-0.01%)</td><td>96104.50 (-0.01%)</td><td>96096.00 (+0.20%)</td><td>9.01 <b>(-94.02%)</b></td><td>715.11 (-0.20%)</td><td>715.04 (+0.01%)</td><td>715.05 (+0.01%)</td><td>714.93 (+0.22%)</td><td>0.07 <b>(-94.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96327.40 (n/a)</td><td>96117.82 (n/a)</td><td>96112.70 (n/a)</td><td>95903.80 (n/a)</td><td>150.56 (n/a)</td><td>716.55 (n/a)</td><td>714.95 (n/a)</td><td>714.99 (n/a)</td><td>713.40 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.73 (-0.00%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.00%)</td><td>0.73 (-0.04%)</td><td>0.00 <b>(+83.16%)</b></td><td>103343.00 (+0.04%)</td><td>103299.72 (+0.01%)</td><td>103296.10 (+0.00%)</td><td>103260.90 (+0.00%)</td><td>35.22 <b>(+83.36%)</b></td><td>665.49 (-0.00%)</td><td>665.24 (-0.01%)</td><td>665.27 (-0.00%)</td><td>664.96 (-0.04%)</td><td>0.23 <b>(+83.14%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103304.80 (n/a)</td><td>103290.16 (n/a)</td><td>103294.80 (n/a)</td><td>103256.70 (n/a)</td><td>19.21 (n/a)</td><td>665.52 (n/a)</td><td>665.31 (n/a)</td><td>665.27 (n/a)</td><td>665.21 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.70 (-0.49%)</td><td>0.70 (+0.11%)</td><td>0.70 (+0.30%)</td><td>0.70 (+0.44%)</td><td>0.00 <b>(-83.82%)</b></td><td>108573.30 (-0.44%)</td><td>108487.10 (-0.11%)</td><td>108464.30 (-0.30%)</td><td>108379.30 (+0.49%)</td><td>84.10 <b>(-83.81%)</b></td><td>634.06 (-0.49%)</td><td>633.43 (+0.11%)</td><td>633.57 (+0.30%)</td><td>632.93 (+0.44%)</td><td>0.49 <b>(-83.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109054.50 (n/a)</td><td>108609.04 (n/a)</td><td>108793.40 (n/a)</td><td>107851.50 (n/a)</td><td>519.48 (n/a)</td><td>637.17 (n/a)</td><td>632.74 (n/a)</td><td>631.65 (n/a)</td><td>630.14 (n/a)</td><td>3.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.73 (+6.29%)</td><td>6.81 (+0.64%)</td><td>7.22 (+4.31%)</td><td>4.87 (-17.27%)</td><td>1.13 <b>(+98.83%)</b></td><td>1829.00 <b>(+20.89%)</b></td><td>1345.68 (+1.52%)</td><td>1234.50 (-4.13%)</td><td>1153.10 (-5.92%)</td><td>275.89 <b>(+133.37%)</b></td><td>465.60 (+6.29%)</td><td>410.09 (+0.64%)</td><td>434.90 (+4.31%)</td><td>293.54 (-17.27%)</td><td>68.10 <b>(+98.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.27 (n/a)</td><td>6.76 (n/a)</td><td>6.92 (n/a)</td><td>5.89 (n/a)</td><td>0.57 (n/a)</td><td>1513.00 (n/a)</td><td>1325.52 (n/a)</td><td>1287.70 (n/a)</td><td>1225.60 (n/a)</td><td>118.22 (n/a)</td><td>438.04 (n/a)</td><td>407.46 (n/a)</td><td>416.92 (n/a)</td><td>354.83 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.74 (-3.35%)</td><td>5.92 (-11.15%)</td><td>6.53 (-3.60%)</td><td>4.83 <b>(-20.52%)</b></td><td>0.98 <b>(+170.55%)</b></td><td>1846.30 <b>(+25.81%)</b></td><td>1540.64 (+14.95%)</td><td>1364.20 (+3.74%)</td><td>1322.20 (+3.46%)</td><td>271.43 <b>(+253.91%)</b></td><td>406.03 (-3.35%)</td><td>356.81 (-11.15%)</td><td>393.55 (-3.60%)</td><td>290.78 <b>(-20.52%)</b></td><td>59.16 <b>(+170.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.97 (n/a)</td><td>6.67 (n/a)</td><td>6.78 (n/a)</td><td>6.07 (n/a)</td><td>0.36 (n/a)</td><td>1467.50 (n/a)</td><td>1340.26 (n/a)</td><td>1315.00 (n/a)</td><td>1278.00 (n/a)</td><td>76.69 (n/a)</td><td>420.10 (n/a)</td><td>401.58 (n/a)</td><td>408.26 (n/a)</td><td>365.85 (n/a)</td><td>21.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.88 (-1.37%)</td><td>6.54 (-1.91%)</td><td>6.57 (-3.68%)</td><td>6.25 (+1.36%)</td><td>0.23 <b>(-30.34%)</b></td><td>1425.70 (-1.34%)</td><td>1363.12 (+1.84%)</td><td>1356.90 (+3.82%)</td><td>1295.90 (+1.38%)</td><td>47.07 <b>(-30.56%)</b></td><td>414.28 (-1.37%)</td><td>394.23 (-1.91%)</td><td>395.67 (-3.68%)</td><td>376.57 (+1.36%)</td><td>13.70 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.97 (n/a)</td><td>6.67 (n/a)</td><td>6.82 (n/a)</td><td>6.17 (n/a)</td><td>0.33 (n/a)</td><td>1445.10 (n/a)</td><td>1338.48 (n/a)</td><td>1307.00 (n/a)</td><td>1278.20 (n/a)</td><td>67.79 (n/a)</td><td>420.04 (n/a)</td><td>401.90 (n/a)</td><td>410.77 (n/a)</td><td>371.51 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.00 (-2.85%)</td><td>7.88 (+1.86%)</td><td>7.95 (+0.68%)</td><td>7.58 (+4.06%)</td><td>0.17 <b>(-58.44%)</b></td><td>4602.60 (-3.90%)</td><td>4428.28 (-2.01%)</td><td>4384.70 (-0.67%)</td><td>4358.50 (+2.94%)</td><td>99.25 <b>(-59.17%)</b></td><td>492.71 (-2.85%)</td><td>485.14 (+1.86%)</td><td>489.77 (+0.68%)</td><td>466.58 (+4.06%)</td><td>10.59 <b>(-58.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.23 (n/a)</td><td>7.73 (n/a)</td><td>7.90 (n/a)</td><td>7.28 (n/a)</td><td>0.41 (n/a)</td><td>4789.50 (n/a)</td><td>4519.06 (n/a)</td><td>4414.40 (n/a)</td><td>4234.10 (n/a)</td><td>243.05 (n/a)</td><td>507.19 (n/a)</td><td>476.30 (n/a)</td><td>486.47 (n/a)</td><td>448.37 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.70 (-3.38%)</td><td>7.32 (-2.71%)</td><td>7.40 (-2.18%)</td><td>6.81 (-1.23%)</td><td>0.35 (-12.04%)</td><td>5121.00 (+1.24%)</td><td>4770.36 (+2.74%)</td><td>4711.10 (+2.22%)</td><td>4530.40 (+3.50%)</td><td>235.53 (-8.41%)</td><td>474.02 (-3.38%)</td><td>451.03 (-2.71%)</td><td>455.83 (-2.18%)</td><td>419.35 (-1.23%)</td><td>21.77 (-12.04%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.97 (n/a)</td><td>7.53 (n/a)</td><td>7.57 (n/a)</td><td>6.89 (n/a)</td><td>0.40 (n/a)</td><td>5058.10 (n/a)</td><td>4643.32 (n/a)</td><td>4608.60 (n/a)</td><td>4377.10 (n/a)</td><td>257.15 (n/a)</td><td>490.62 (n/a)</td><td>463.58 (n/a)</td><td>465.97 (n/a)</td><td>424.56 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>7.84 (+6.71%)</td><td>7.27 (+2.69%)</td><td>7.27 (-0.01%)</td><td>6.64 (-1.12%)</td><td>0.44 <b>(+38.57%)</b></td><td>5250.00 (+1.13%)</td><td>4811.96 (-2.50%)</td><td>4798.90 (+0.01%)</td><td>4445.20 (-6.29%)</td><td>294.04 <b>(+31.41%)</b></td><td>483.10 (+6.71%)</td><td>447.60 (+2.69%)</td><td>447.50 (-0.01%)</td><td>409.05 (-1.12%)</td><td>26.96 <b>(+38.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.35 (n/a)</td><td>7.08 (n/a)</td><td>7.27 (n/a)</td><td>6.72 (n/a)</td><td>0.32 (n/a)</td><td>5191.30 (n/a)</td><td>4935.10 (n/a)</td><td>4798.50 (n/a)</td><td>4743.50 (n/a)</td><td>223.76 (n/a)</td><td>452.72 (n/a)</td><td>435.85 (n/a)</td><td>447.53 (n/a)</td><td>413.67 (n/a)</td><td>19.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.79 (+0.05%)</td><td>0.79 (+0.08%)</td><td>0.79 (+0.03%)</td><td>0.79 (+0.22%)</td><td>0.00 <b>(-72.22%)</b></td><td>95447.50 (-0.22%)</td><td>95411.92 (-0.08%)</td><td>95412.10 (-0.03%)</td><td>95385.10 (-0.05%)</td><td>27.38 <b>(-72.31%)</b></td><td>720.44 (+0.05%)</td><td>720.24 (+0.08%)</td><td>720.24 (+0.03%)</td><td>719.97 (+0.22%)</td><td>0.21 <b>(-72.22%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95660.40 (n/a)</td><td>95484.46 (n/a)</td><td>95440.10 (n/a)</td><td>95432.00 (n/a)</td><td>98.86 (n/a)</td><td>720.09 (n/a)</td><td>719.69 (n/a)</td><td>720.03 (n/a)</td><td>718.37 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.74 (-0.00%)</td><td>0.74 (+0.01%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.02%)</td><td>0.00 (+2.76%)</td><td>102630.50 (+0.02%)</td><td>102586.70 (-0.01%)</td><td>102582.80 (-0.02%)</td><td>102555.80 (+0.00%)</td><td>27.10 (+2.77%)</td><td>670.07 (-0.00%)</td><td>669.87 (+0.01%)</td><td>669.89 (+0.02%)</td><td>669.58 (-0.02%)</td><td>0.18 (+2.73%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102614.60 (n/a)</td><td>102592.74 (n/a)</td><td>102606.20 (n/a)</td><td>102553.30 (n/a)</td><td>26.37 (n/a)</td><td>670.09 (n/a)</td><td>669.83 (n/a)</td><td>669.74 (n/a)</td><td>669.68 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.70 (-0.32%)</td><td>0.70 (-0.10%)</td><td>0.70 (-0.10%)</td><td>0.70 (+0.09%)</td><td>0.00 <b>(-69.37%)</b></td><td>107555.30 (-0.09%)</td><td>107470.92 (+0.10%)</td><td>107495.70 (+0.10%)</td><td>107391.60 (+0.33%)</td><td>67.95 <b>(-69.29%)</b></td><td>639.90 (-0.32%)</td><td>639.42 (-0.10%)</td><td>639.28 (-0.10%)</td><td>638.92 (+0.09%)</td><td>0.40 <b>(-69.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.71 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107655.10 (n/a)</td><td>107363.34 (n/a)</td><td>107392.10 (n/a)</td><td>107043.10 (n/a)</td><td>221.29 (n/a)</td><td>641.98 (n/a)</td><td>640.07 (n/a)</td><td>639.89 (n/a)</td><td>638.33 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>4.02 (-4.48%)</td><td>3.66 (-4.83%)</td><td>3.74 (-1.15%)</td><td>3.19 (-11.16%)</td><td>0.31 (+18.90%)</td><td>2524.80 (+12.57%)</td><td>2214.60 (+5.34%)</td><td>2157.50 (+1.17%)</td><td>2006.50 (+4.69%)</td><td>198.36 <b>(+40.97%)</b></td><td>1053.55 (-4.48%)</td><td>960.40 (-4.83%)</td><td>979.79 (-1.15%)</td><td>837.25 (-11.16%)</td><td>82.02 (+18.90%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>4.21 (n/a)</td><td>3.85 (n/a)</td><td>3.78 (n/a)</td><td>3.59 (n/a)</td><td>0.26 (n/a)</td><td>2242.90 (n/a)</td><td>2102.36 (n/a)</td><td>2132.60 (n/a)</td><td>1916.60 (n/a)</td><td>140.71 (n/a)</td><td>1102.97 (n/a)</td><td>1009.19 (n/a)</td><td>991.23 (n/a)</td><td>942.48 (n/a)</td><td>68.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.51 (+0.49%)</td><td>0.41 (+13.77%)</td><td>0.36 (+8.76%)</td><td>0.35 (+16.04%)</td><td>0.07 (-12.71%)</td><td>3558.60 (-13.82%)</td><td>3113.76 (-13.02%)</td><td>3438.50 (-8.05%)</td><td>2457.20 (-0.49%)</td><td>509.85 <b>(-21.99%)</b></td><td>27.31 (+0.49%)</td><td>22.06 (+13.77%)</td><td>19.52 (+8.76%)</td><td>18.86 (+16.04%)</td><td>3.88 (-12.71%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>4129.50 (n/a)</td><td>3580.06 (n/a)</td><td>3739.70 (n/a)</td><td>2469.20 (n/a)</td><td>653.54 (n/a)</td><td>27.18 (n/a)</td><td>19.39 (n/a)</td><td>17.94 (n/a)</td><td>16.25 (n/a)</td><td>4.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.03 (-6.22%)</td><td>4.15 (-14.55%)</td><td>3.76 <b>(-21.45%)</b></td><td>3.45 <b>(-25.45%)</b></td><td>0.76 <b>(+157.90%)</b></td><td>1928.50 <b>(+34.15%)</b></td><td>1644.34 (+19.78%)</td><td>1770.10 <b>(+27.31%)</b></td><td>1322.00 (+6.63%)</td><td>287.29 <b>(+264.26%)</b></td><td>1554.60 (-6.22%)</td><td>1282.84 (-14.55%)</td><td>1161.09 <b>(-21.45%)</b></td><td>1065.70 <b>(-25.45%)</b></td><td>236.25 <b>(+157.90%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>5.37 (n/a)</td><td>4.86 (n/a)</td><td>4.78 (n/a)</td><td>4.63 (n/a)</td><td>0.30 (n/a)</td><td>1437.60 (n/a)</td><td>1372.76 (n/a)</td><td>1390.40 (n/a)</td><td>1239.80 (n/a)</td><td>78.87 (n/a)</td><td>1657.64 (n/a)</td><td>1501.34 (n/a)</td><td>1478.16 (n/a)</td><td>1429.57 (n/a)</td><td>91.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>13.49 (n/a)</td><td>12.88 (n/a)</td><td>13.26 (n/a)</td><td>11.10 (n/a)</td><td>1.01 (n/a)</td><td>13.48 (n/a)</td><td>12.87 (n/a)</td><td>13.25 (n/a)</td><td>11.09 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>25.17 (+2.66%)</td><td>24.17 (+0.21%)</td><td>24.62 (+2.40%)</td><td>21.90 (-7.86%)</td><td>1.29 <b>(+357.51%)</b></td><td>25.15 (+2.66%)</td><td>24.16 (+0.21%)</td><td>24.60 (+2.40%)</td><td>21.89 (-7.86%)</td><td>1.29 <b>(+357.51%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>24.51 (n/a)</td><td>24.12 (n/a)</td><td>24.04 (n/a)</td><td>23.77 (n/a)</td><td>0.28 (n/a)</td><td>24.50 (n/a)</td><td>24.11 (n/a)</td><td>24.03 (n/a)</td><td>23.76 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>40.71 (+0.60%)</td><td>40.24 (+0.95%)</td><td>40.32 (+0.73%)</td><td>39.69 (+1.15%)</td><td>0.46 (-8.60%)</td><td>40.69 (+0.60%)</td><td>40.21 (+0.95%)</td><td>40.29 (+0.73%)</td><td>39.67 (+1.15%)</td><td>0.46 (-8.60%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>40.47 (n/a)</td><td>39.86 (n/a)</td><td>40.02 (n/a)</td><td>39.24 (n/a)</td><td>0.51 (n/a)</td><td>40.44 (n/a)</td><td>39.83 (n/a)</td><td>40.00 (n/a)</td><td>39.21 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>46.03 (+6.94%)</td><td>40.06 (-2.45%)</td><td>43.27 (+4.04%)</td><td>25.27 <b>(-33.78%)</b></td><td>8.49 <b>(+365.58%)</b></td><td>46.00 (+6.94%)</td><td>40.04 (-2.45%)</td><td>43.24 (+4.04%)</td><td>25.26 <b>(-33.78%)</b></td><td>8.49 <b>(+365.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>43.04 (n/a)</td><td>41.07 (n/a)</td><td>41.59 (n/a)</td><td>38.17 (n/a)</td><td>1.82 (n/a)</td><td>43.02 (n/a)</td><td>41.04 (n/a)</td><td>41.56 (n/a)</td><td>38.15 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>13.38 (n/a)</td><td>13.02 (n/a)</td><td>13.04 (n/a)</td><td>12.64 (n/a)</td><td>0.32 (n/a)</td><td>13.38 (n/a)</td><td>13.01 (n/a)</td><td>13.03 (n/a)</td><td>12.63 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>25.16 (+2.40%)</td><td>24.57 (+1.40%)</td><td>24.72 (+2.30%)</td><td>24.00 (+0.85%)</td><td>0.49 <b>(+55.24%)</b></td><td>25.15 (+2.40%)</td><td>24.55 (+1.40%)</td><td>24.70 (+2.30%)</td><td>23.99 (+0.85%)</td><td>0.49 <b>(+55.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>24.57 (n/a)</td><td>24.23 (n/a)</td><td>24.16 (n/a)</td><td>23.80 (n/a)</td><td>0.32 (n/a)</td><td>24.56 (n/a)</td><td>24.21 (n/a)</td><td>24.15 (n/a)</td><td>23.79 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>43.25 (+4.99%)</td><td>40.62 (+2.09%)</td><td>40.17 (+1.24%)</td><td>39.06 (+0.54%)</td><td>1.71 <b>(+70.73%)</b></td><td>43.22 (+4.99%)</td><td>40.60 (+2.09%)</td><td>40.14 (+1.24%)</td><td>39.04 (+0.54%)</td><td>1.71 <b>(+70.73%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>41.20 (n/a)</td><td>39.79 (n/a)</td><td>39.67 (n/a)</td><td>38.85 (n/a)</td><td>1.00 (n/a)</td><td>41.17 (n/a)</td><td>39.77 (n/a)</td><td>39.65 (n/a)</td><td>38.83 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>44.01 (+0.40%)</td><td>43.15 (+0.39%)</td><td>43.21 (+0.60%)</td><td>42.44 (+0.17%)</td><td>0.60 (+6.89%)</td><td>43.98 (+0.40%)</td><td>43.12 (+0.39%)</td><td>43.19 (+0.60%)</td><td>42.42 (+0.17%)</td><td>0.60 (+6.89%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>43.83 (n/a)</td><td>42.98 (n/a)</td><td>42.96 (n/a)</td><td>42.37 (n/a)</td><td>0.56 (n/a)</td><td>43.80 (n/a)</td><td>42.96 (n/a)</td><td>42.93 (n/a)</td><td>42.34 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.83 (+2.74%)</td><td>8.97 (+0.70%)</td><td>8.78 (-1.12%)</td><td>8.33 (-1.00%)</td><td>0.66 <b>(+48.15%)</b></td><td>9.82 (+2.74%)</td><td>8.95 (+0.70%)</td><td>8.76 (-1.12%)</td><td>8.31 (-1.00%)</td><td>0.66 <b>(+48.15%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.57 (n/a)</td><td>8.90 (n/a)</td><td>8.88 (n/a)</td><td>8.41 (n/a)</td><td>0.45 (n/a)</td><td>9.55 (n/a)</td><td>8.89 (n/a)</td><td>8.86 (n/a)</td><td>8.40 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.98 (+12.03%)</td><td>0.89 (+5.64%)</td><td>0.90 (+7.68%)</td><td>0.83 (+0.39%)</td><td>0.06 <b>(+235.42%)</b></td><td>0.96 (+12.03%)</td><td>0.88 (+5.64%)</td><td>0.89 (+7.68%)</td><td>0.82 (+0.39%)</td><td>0.06 <b>(+235.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.87 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.83 (n/a)</td><td>0.02 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.48 (+12.44%)</td><td>1.20 (+7.51%)</td><td>1.17 (+6.75%)</td><td>0.93 (-5.18%)</td><td>0.21 <b>(+65.80%)</b></td><td>1.47 (+12.44%)</td><td>1.19 (+7.51%)</td><td>1.16 (+6.75%)</td><td>0.92 (-5.18%)</td><td>0.20 <b>(+65.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.32 (n/a)</td><td>1.12 (n/a)</td><td>1.10 (n/a)</td><td>0.98 (n/a)</td><td>0.12 (n/a)</td><td>1.30 (n/a)</td><td>1.11 (n/a)</td><td>1.08 (n/a)</td><td>0.97 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>18.37 (-3.32%)</td><td>17.74 (+9.16%)</td><td>17.73 (+9.13%)</td><td>17.28 <b>(+36.21%)</b></td><td>0.45 <b>(-80.85%)</b></td><td>18.16 (-3.32%)</td><td>17.54 (+9.16%)</td><td>17.52 (+9.13%)</td><td>17.08 <b>(+36.21%)</b></td><td>0.44 <b>(-80.85%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>19.00 (n/a)</td><td>16.25 (n/a)</td><td>16.25 (n/a)</td><td>12.68 (n/a)</td><td>2.33 (n/a)</td><td>18.78 (n/a)</td><td>16.07 (n/a)</td><td>16.06 (n/a)</td><td>12.54 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.35 (+0.49%)</td><td>12.11 (-9.49%)</td><td>13.34 (-0.20%)</td><td>7.43 <b>(-40.44%)</b></td><td>2.75 <b>(+332.15%)</b></td><td>14.10 (+0.49%)</td><td>11.90 (-9.49%)</td><td>13.10 (-0.20%)</td><td>7.30 <b>(-40.44%)</b></td><td>2.71 <b>(+332.15%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.28 (n/a)</td><td>13.38 (n/a)</td><td>13.36 (n/a)</td><td>12.48 (n/a)</td><td>0.64 (n/a)</td><td>14.03 (n/a)</td><td>13.14 (n/a)</td><td>13.13 (n/a)</td><td>12.26 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>10.15 (+11.69%)</td><td>7.97 (+2.24%)</td><td>7.48 (+0.48%)</td><td>7.33 (+7.89%)</td><td>1.22 <b>(+31.97%)</b></td><td>9.98 (+11.69%)</td><td>7.83 (+2.24%)</td><td>7.35 (+0.48%)</td><td>7.20 (+7.89%)</td><td>1.20 <b>(+31.97%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.09 (n/a)</td><td>7.80 (n/a)</td><td>7.45 (n/a)</td><td>6.79 (n/a)</td><td>0.93 (n/a)</td><td>8.93 (n/a)</td><td>7.66 (n/a)</td><td>7.32 (n/a)</td><td>6.68 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.41 (+2.92%)</td><td>6.06 (+14.69%)</td><td>6.19 (+13.18%)</td><td>5.25 (+18.85%)</td><td>0.47 <b>(-33.47%)</b></td><td>6.30 (+2.92%)</td><td>5.97 (+14.69%)</td><td>6.09 (+13.18%)</td><td>5.16 (+18.85%)</td><td>0.46 <b>(-33.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.23 (n/a)</td><td>5.29 (n/a)</td><td>5.47 (n/a)</td><td>4.42 (n/a)</td><td>0.70 (n/a)</td><td>6.13 (n/a)</td><td>5.20 (n/a)</td><td>5.38 (n/a)</td><td>4.34 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.72 (n/a)</td><td>11.99 (n/a)</td><td>12.06 (n/a)</td><td>11.10 (n/a)</td><td>0.61 (n/a)</td><td>12.71 (n/a)</td><td>11.98 (n/a)</td><td>12.05 (n/a)</td><td>11.09 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>13.30 (n/a)</td><td>12.93 (n/a)</td><td>13.12 (n/a)</td><td>11.95 (n/a)</td><td>0.56 (n/a)</td><td>13.29 (n/a)</td><td>12.93 (n/a)</td><td>13.11 (n/a)</td><td>11.95 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>158.68 (n/a)</td><td>158.50 (n/a)</td><td>104.10 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>375.10 (n/a)</td><td>208.40 (n/a)</td><td>172.80 (n/a)</td><td>156.60 (n/a)</td><td>93.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>168.88 (n/a)</td><td>156.70 (n/a)</td><td>135.30 (n/a)</td><td>48.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>171.44 (n/a)</td><td>179.70 (n/a)</td><td>133.90 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>363.60 (n/a)</td><td>220.16 (n/a)</td><td>193.20 (n/a)</td><td>167.80 (n/a)</td><td>80.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.30 (n/a)</td><td>197.82 (n/a)</td><td>196.10 (n/a)</td><td>176.70 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>264.50 (n/a)</td><td>186.06 (n/a)</td><td>169.50 (n/a)</td><td>146.90 (n/a)</td><td>45.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.90 (n/a)</td><td>210.24 (n/a)</td><td>212.00 (n/a)</td><td>187.70 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>170.06 (n/a)</td><td>169.80 (n/a)</td><td>165.30 (n/a)</td><td>4.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>156.20 (n/a)</td><td>137.66 (n/a)</td><td>144.30 (n/a)</td><td>106.30 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>166.06 (n/a)</td><td>166.00 (n/a)</td><td>119.20 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>160.36 (n/a)</td><td>153.60 (n/a)</td><td>138.30 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>176.74 (n/a)</td><td>175.10 (n/a)</td><td>135.80 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>174.66 (n/a)</td><td>176.10 (n/a)</td><td>156.80 (n/a)</td><td>17.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>159.50 (n/a)</td><td>154.30 (n/a)</td><td>142.20 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>191.56 (n/a)</td><td>192.60 (n/a)</td><td>165.60 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>163.22 (n/a)</td><td>170.90 (n/a)</td><td>127.00 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>159.54 (n/a)</td><td>156.50 (n/a)</td><td>121.90 (n/a)</td><td>34.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.20 (n/a)</td><td>158.14 (n/a)</td><td>158.90 (n/a)</td><td>122.50 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.90 (n/a)</td><td>160.30 (n/a)</td><td>154.50 (n/a)</td><td>144.70 (n/a)</td><td>15.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>156.08 (n/a)</td><td>150.50 (n/a)</td><td>123.40 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>258.00 (n/a)</td><td>183.94 (n/a)</td><td>168.10 (n/a)</td><td>135.90 (n/a)</td><td>52.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>266.20 (n/a)</td><td>204.28 (n/a)</td><td>201.00 (n/a)</td><td>139.60 (n/a)</td><td>47.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>298.60 (n/a)</td><td>230.60 (n/a)</td><td>222.10 (n/a)</td><td>198.20 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>342.40 (n/a)</td><td>190.80 (n/a)</td><td>172.00 (n/a)</td><td>116.40 (n/a)</td><td>88.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>166.80 (n/a)</td><td>150.46 (n/a)</td><td>148.40 (n/a)</td><td>129.20 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>165.30 (n/a)</td><td>146.44 (n/a)</td><td>143.50 (n/a)</td><td>128.20 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.60 (n/a)</td><td>170.00 (n/a)</td><td>177.40 (n/a)</td><td>138.70 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.40 (n/a)</td><td>172.04 (n/a)</td><td>173.30 (n/a)</td><td>125.90 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>191.06 (n/a)</td><td>197.60 (n/a)</td><td>153.90 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>190.44 (n/a)</td><td>189.40 (n/a)</td><td>150.60 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>336.60 (n/a)</td><td>241.66 (n/a)</td><td>220.60 (n/a)</td><td>192.00 (n/a)</td><td>55.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-5.43%)</td><td>0.02 (-15.04%)</td><td>0.02 (-4.63%)</td><td>0.02 <b>(-27.97%)</b></td><td>0.01 <b>(+32.06%)</b></td><td>246.50 <b>(+38.80%)</b></td><td>192.70 <b>(+20.82%)</b></td><td>182.70 (+4.88%)</td><td>133.40 (+5.79%)</td><td>43.33 <b>(+90.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>159.50 (n/a)</td><td>174.20 (n/a)</td><td>126.10 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+68.65%)</b></td><td>0.03 <b>(+25.84%)</b></td><td>0.02 (+13.19%)</td><td>0.02 <b>(+20.37%)</b></td><td>0.01 <b>(+219.59%)</b></td><td>198.70 (-16.93%)</td><td>165.00 (-17.71%)</td><td>172.00 (-11.66%)</td><td>107.70 <b>(-40.69%)</b></td><td>34.24 <b>(+48.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>200.50 (n/a)</td><td>194.70 (n/a)</td><td>181.60 (n/a)</td><td>23.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-0.42%)</td><td>0.02 (-3.06%)</td><td>0.02 (-0.75%)</td><td>0.02 (+8.79%)</td><td>0.00 (-7.86%)</td><td>229.70 (-8.08%)</td><td>189.54 (+2.43%)</td><td>180.10 (+0.78%)</td><td>146.40 (+0.48%)</td><td>34.02 (-15.11%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.90 (n/a)</td><td>185.04 (n/a)</td><td>178.70 (n/a)</td><td>145.70 (n/a)</td><td>40.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-14.16%)</td><td>0.02 (-11.60%)</td><td>0.02 (-16.04%)</td><td>0.02 (-8.42%)</td><td>0.00 <b>(-44.66%)</b></td><td>224.30 (+9.20%)</td><td>197.48 (+12.04%)</td><td>194.90 (+19.13%)</td><td>179.30 (+16.50%)</td><td>17.57 <b>(-30.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.40 (n/a)</td><td>176.26 (n/a)</td><td>163.60 (n/a)</td><td>153.90 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-6.13%)</td><td>0.03 (+2.71%)</td><td>0.03 (+8.86%)</td><td>0.02 (+8.65%)</td><td>0.00 <b>(-25.00%)</b></td><td>186.10 (-7.96%)</td><td>162.64 (-4.06%)</td><td>162.40 (-8.14%)</td><td>124.80 (+6.48%)</td><td>24.32 <b>(-23.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>169.52 (n/a)</td><td>176.80 (n/a)</td><td>117.20 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 <b>(+34.87%)</b></td><td>0.02 (+15.30%)</td><td>0.02 (+6.35%)</td><td>0.02 (+8.77%)</td><td>0.01 <b>(+94.63%)</b></td><td>243.60 (-8.08%)</td><td>183.78 (-9.23%)</td><td>192.20 (-5.97%)</td><td>118.90 <b>(-25.87%)</b></td><td>53.72 <b>(+32.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>265.00 (n/a)</td><td>202.46 (n/a)</td><td>204.40 (n/a)</td><td>160.40 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 <b>(-21.81%)</b></td><td>0.02 (+1.05%)</td><td>0.02 (-2.68%)</td><td>0.02 <b>(+32.57%)</b></td><td>0.00 <b>(-54.04%)</b></td><td>215.00 <b>(-24.56%)</b></td><td>176.38 (-8.60%)</td><td>185.00 (+2.78%)</td><td>137.30 <b>(+27.96%)</b></td><td>29.39 <b>(-55.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>285.00 (n/a)</td><td>192.98 (n/a)</td><td>180.00 (n/a)</td><td>107.30 (n/a)</td><td>65.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-4.49%)</td><td>0.02 (-7.62%)</td><td>0.02 (-13.76%)</td><td>0.02 (-9.92%)</td><td>0.00 <b>(+21.98%)</b></td><td>246.80 (+10.97%)</td><td>216.18 (+8.85%)</td><td>221.20 (+15.93%)</td><td>183.20 (+4.69%)</td><td>27.87 <b>(+39.14%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.40 (n/a)</td><td>198.60 (n/a)</td><td>190.80 (n/a)</td><td>175.00 (n/a)</td><td>20.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-11.79%)</td><td>0.05 (+8.08%)</td><td>0.05 (+16.06%)</td><td>0.04 <b>(+47.11%)</b></td><td>0.01 <b>(-44.36%)</b></td><td>204.50 <b>(-32.01%)</b></td><td>163.72 (-13.55%)</td><td>154.60 (-13.87%)</td><td>132.50 (+13.34%)</td><td>28.43 <b>(-58.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>300.80 (n/a)</td><td>189.38 (n/a)</td><td>179.50 (n/a)</td><td>116.90 (n/a)</td><td>67.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-7.78%)</td><td>0.05 (-1.52%)</td><td>0.05 (-7.21%)</td><td>0.04 (+2.74%)</td><td>0.01 <b>(-20.45%)</b></td><td>212.50 (-2.66%)</td><td>173.26 (+0.46%)</td><td>180.00 (+7.78%)</td><td>135.20 (+8.42%)</td><td>28.83 (-15.29%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>172.46 (n/a)</td><td>167.00 (n/a)</td><td>124.70 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(-27.80%)</b></td><td>0.05 (-16.46%)</td><td>0.05 (-6.93%)</td><td>0.04 (-3.76%)</td><td>0.01 <b>(-62.18%)</b></td><td>199.20 (+3.91%)</td><td>172.02 (+15.53%)</td><td>174.20 (+7.46%)</td><td>149.50 <b>(+38.55%)</b></td><td>19.15 <b>(-44.49%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>148.90 (n/a)</td><td>162.10 (n/a)</td><td>107.90 (n/a)</td><td>34.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (-14.55%)</td><td>0.06 (+0.10%)</td><td>0.05 (-0.88%)</td><td>0.05 <b>(+28.07%)</b></td><td>0.01 <b>(-56.61%)</b></td><td>156.30 <b>(-21.93%)</b></td><td>146.94 (-3.67%)</td><td>152.00 (+0.86%)</td><td>122.70 (+17.08%)</td><td>13.78 <b>(-60.15%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>152.54 (n/a)</td><td>150.70 (n/a)</td><td>104.80 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-19.95%)</td><td>0.05 (-5.02%)</td><td>0.05 (+1.29%)</td><td>0.04 (+2.17%)</td><td>0.01 <b>(-44.34%)</b></td><td>212.50 (-2.12%)</td><td>168.78 (+2.42%)</td><td>165.20 (-1.26%)</td><td>137.70 <b>(+24.95%)</b></td><td>27.26 <b>(-28.06%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>164.80 (n/a)</td><td>167.30 (n/a)</td><td>110.20 (n/a)</td><td>37.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 <b>(+22.01%)</b></td><td>0.05 (+5.54%)</td><td>0.05 (+14.70%)</td><td>0.04 (-6.47%)</td><td>0.01 <b>(+62.38%)</b></td><td>220.40 (+6.89%)</td><td>172.20 (-1.85%)</td><td>162.10 (-12.80%)</td><td>116.90 (-18.08%)</td><td>46.36 <b>(+53.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>175.44 (n/a)</td><td>185.90 (n/a)</td><td>142.70 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+4.21%)</td><td>0.05 (+3.53%)</td><td>0.05 (+15.19%)</td><td>0.04 (-9.48%)</td><td>0.01 <b>(+63.78%)</b></td><td>215.70 (+10.50%)</td><td>174.24 (-1.56%)</td><td>160.80 (-13.22%)</td><td>143.60 (-4.07%)</td><td>34.13 <b>(+72.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>177.00 (n/a)</td><td>185.30 (n/a)</td><td>149.70 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-12.97%)</td><td>0.04 (-7.52%)</td><td>0.04 (-2.07%)</td><td>0.04 (-4.95%)</td><td>0.00 <b>(-29.37%)</b></td><td>218.50 (+5.25%)</td><td>194.92 (+7.60%)</td><td>192.60 (+2.12%)</td><td>172.90 (+14.88%)</td><td>19.54 (-13.60%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>181.16 (n/a)</td><td>188.60 (n/a)</td><td>150.50 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (+7.91%)</td><td>0.04 (+0.33%)</td><td>0.04 (-0.59%)</td><td>0.03 (-14.67%)</td><td>0.01 <b>(+209.91%)</b></td><td>241.80 (+17.15%)</td><td>194.86 (+1.08%)</td><td>191.60 (+0.58%)</td><td>170.30 (-7.34%)</td><td>28.57 <b>(+235.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>192.78 (n/a)</td><td>190.50 (n/a)</td><td>183.80 (n/a)</td><td>8.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (+4.43%)</td><td>0.03 (-6.62%)</td><td>0.04 (-0.07%)</td><td>0.03 <b>(-24.15%)</b></td><td>0.01 <b>(+108.31%)</b></td><td>327.40 <b>(+31.86%)</b></td><td>244.06 (+9.92%)</td><td>222.70 (+0.09%)</td><td>195.10 (-4.27%)</td><td>51.67 <b>(+172.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>248.30 (n/a)</td><td>222.04 (n/a)</td><td>222.50 (n/a)</td><td>203.80 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-2.50%)</td><td>0.09 (-8.71%)</td><td>0.08 (-12.69%)</td><td>0.08 (-13.93%)</td><td>0.02 <b>(+29.64%)</b></td><td>214.40 (+16.14%)</td><td>183.44 (+11.07%)</td><td>197.00 (+14.53%)</td><td>135.60 (+2.57%)</td><td>32.07 <b>(+55.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>165.16 (n/a)</td><td>172.00 (n/a)</td><td>132.20 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-7.35%)</td><td>0.11 (+3.78%)</td><td>0.12 (+16.75%)</td><td>0.08 (-7.82%)</td><td>0.02 (-2.85%)</td><td>198.60 (+8.52%)</td><td>147.86 (-3.37%)</td><td>135.70 (-14.38%)</td><td>133.80 (+7.99%)</td><td>28.38 (+16.41%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>153.02 (n/a)</td><td>158.50 (n/a)</td><td>123.90 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (+6.85%)</td><td>0.10 (+5.77%)</td><td>0.10 (+13.19%)</td><td>0.08 (+7.50%)</td><td>0.02 (+13.75%)</td><td>212.60 (-7.00%)</td><td>170.32 (-4.86%)</td><td>161.60 (-11.65%)</td><td>133.00 (-6.47%)</td><td>38.83 (+4.17%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.60 (n/a)</td><td>179.02 (n/a)</td><td>182.90 (n/a)</td><td>142.20 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-5.79%)</td><td>0.09 (-6.76%)</td><td>0.09 (+0.76%)</td><td>0.09 (+0.63%)</td><td>0.01 <b>(-28.84%)</b></td><td>191.50 (-0.62%)</td><td>177.60 (+5.78%)</td><td>186.60 (-0.74%)</td><td>138.00 (+6.15%)</td><td>22.27 <b>(-27.19%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>167.90 (n/a)</td><td>188.00 (n/a)</td><td>130.00 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (+8.18%)</td><td>0.10 (+7.57%)</td><td>0.11 (+8.40%)</td><td>0.05 (+12.47%)</td><td>0.03 (+2.54%)</td><td>337.80 (-11.08%)</td><td>190.02 (-8.34%)</td><td>148.90 (-7.80%)</td><td>137.60 (-7.59%)</td><td>84.33 (-14.34%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>379.90 (n/a)</td><td>207.32 (n/a)</td><td>161.50 (n/a)</td><td>148.90 (n/a)</td><td>98.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (+9.55%)</td><td>0.09 (-0.96%)</td><td>0.10 (+1.19%)</td><td>0.06 <b>(-25.46%)</b></td><td>0.02 <b>(+85.19%)</b></td><td>267.20 <b>(+34.14%)</b></td><td>185.10 (+4.96%)</td><td>169.20 (-1.23%)</td><td>134.50 (-8.75%)</td><td>50.14 <b>(+130.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>176.36 (n/a)</td><td>171.30 (n/a)</td><td>147.40 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-6.05%)</td><td>0.11 (+14.17%)</td><td>0.11 <b>(+43.51%)</b></td><td>0.09 <b>(+20.63%)</b></td><td>0.01 <b>(-50.48%)</b></td><td>182.10 (-17.11%)</td><td>152.12 (-16.34%)</td><td>146.20 <b>(-30.31%)</b></td><td>135.10 (+6.46%)</td><td>19.75 <b>(-57.21%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>181.84 (n/a)</td><td>209.80 (n/a)</td><td>126.90 (n/a)</td><td>46.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (+17.93%)</td><td>0.08 (+16.39%)</td><td>0.09 <b>(+24.10%)</b></td><td>0.05 (+17.09%)</td><td>0.02 (+15.03%)</td><td>308.10 (-14.61%)</td><td>208.32 (-14.22%)</td><td>187.40 (-19.43%)</td><td>157.40 (-15.19%)</td><td>58.26 (-15.59%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>360.80 (n/a)</td><td>242.84 (n/a)</td><td>232.60 (n/a)</td><td>185.60 (n/a)</td><td>69.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-6.24%)</td><td>0.18 (-8.54%)</td><td>0.17 (-15.37%)</td><td>0.12 (-9.80%)</td><td>0.04 (-6.90%)</td><td>265.50 (+10.86%)</td><td>189.16 (+9.39%)</td><td>188.10 (+18.15%)</td><td>133.20 (+6.65%)</td><td>48.89 (+9.78%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>239.50 (n/a)</td><td>172.92 (n/a)</td><td>159.20 (n/a)</td><td>124.90 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (+16.86%)</td><td>0.23 (+7.97%)</td><td>0.21 (+2.87%)</td><td>0.19 (+1.49%)</td><td>0.03 <b>(+73.03%)</b></td><td>168.80 (-1.52%)</td><td>146.52 (-6.58%)</td><td>153.50 (-2.79%)</td><td>118.60 (-14.43%)</td><td>19.05 <b>(+43.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>171.40 (n/a)</td><td>156.84 (n/a)</td><td>157.90 (n/a)</td><td>138.60 (n/a)</td><td>13.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (+0.73%)</td><td>0.22 <b>(+26.72%)</b></td><td>0.21 <b>(+28.87%)</b></td><td>0.20 <b>(+93.30%)</b></td><td>0.02 <b>(-60.12%)</b></td><td>162.50 <b>(-48.26%)</b></td><td>150.06 <b>(-26.56%)</b></td><td>153.20 <b>(-22.39%)</b></td><td>130.10 (-0.69%)</td><td>13.54 <b>(-79.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>314.10 (n/a)</td><td>204.32 (n/a)</td><td>197.40 (n/a)</td><td>131.00 (n/a)</td><td>67.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (-2.26%)</td><td>0.22 (-3.26%)</td><td>0.21 (-8.13%)</td><td>0.19 (+1.97%)</td><td>0.03 (-17.02%)</td><td>168.20 (-1.92%)</td><td>150.82 (+2.72%)</td><td>156.50 (+8.83%)</td><td>122.20 (+2.35%)</td><td>17.98 (-19.42%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>171.50 (n/a)</td><td>146.82 (n/a)</td><td>143.80 (n/a)</td><td>119.40 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (+1.78%)</td><td>0.20 (+5.14%)</td><td>0.21 (+2.50%)</td><td>0.17 (+8.35%)</td><td>0.02 <b>(-21.10%)</b></td><td>195.00 (-7.71%)</td><td>163.92 (-5.54%)</td><td>154.60 (-2.46%)</td><td>149.30 (-1.78%)</td><td>18.49 <b>(-27.39%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>211.30 (n/a)</td><td>173.54 (n/a)</td><td>158.50 (n/a)</td><td>152.00 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (+8.77%)</td><td>0.19 (-5.83%)</td><td>0.19 (-3.86%)</td><td>0.11 <b>(-33.20%)</b></td><td>0.05 <b>(+77.36%)</b></td><td>286.80 <b>(+49.69%)</b></td><td>186.88 (+11.90%)</td><td>176.00 (+4.02%)</td><td>127.10 (-8.10%)</td><td>59.51 <b>(+154.21%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.60 (n/a)</td><td>167.00 (n/a)</td><td>169.20 (n/a)</td><td>138.30 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (-9.67%)</td><td>0.15 (+4.92%)</td><td>0.15 (+1.53%)</td><td>0.14 <b>(+44.07%)</b></td><td>0.01 <b>(-63.99%)</b></td><td>232.00 <b>(-30.58%)</b></td><td>219.20 (-8.47%)</td><td>221.70 (-1.51%)</td><td>192.50 (+10.70%)</td><td>15.91 <b>(-73.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>334.20 (n/a)</td><td>239.48 (n/a)</td><td>225.10 (n/a)</td><td>173.90 (n/a)</td><td>59.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+22.17%)</b></td><td>0.03 (-1.24%)</td><td>0.02 (-5.21%)</td><td>0.02 <b>(-21.89%)</b></td><td>0.01 <b>(+121.48%)</b></td><td>237.80 <b>(+27.99%)</b></td><td>177.92 (+9.26%)</td><td>173.30 (+5.48%)</td><td>102.60 (-18.18%)</td><td>56.83 <b>(+143.04%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.80 (n/a)</td><td>162.84 (n/a)</td><td>164.30 (n/a)</td><td>125.40 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+23.17%)</b></td><td>0.03 (+2.41%)</td><td>0.02 (-9.09%)</td><td>0.02 (+1.84%)</td><td>0.01 <b>(+57.76%)</b></td><td>205.50 (-1.82%)</td><td>162.74 (+0.46%)</td><td>174.90 (+10.00%)</td><td>105.00 (-18.86%)</td><td>40.56 <b>(+25.91%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>162.00 (n/a)</td><td>159.00 (n/a)</td><td>129.40 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+9.71%)</td><td>0.02 (+1.96%)</td><td>0.02 (-9.80%)</td><td>0.02 <b>(+23.62%)</b></td><td>0.00 (+6.14%)</td><td>244.20 (-19.11%)</td><td>210.14 (-2.61%)</td><td>227.70 (+10.86%)</td><td>154.80 (-8.83%)</td><td>38.04 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>301.90 (n/a)</td><td>215.78 (n/a)</td><td>205.40 (n/a)</td><td>169.80 (n/a)</td><td>50.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.02 (-14.35%)</td><td>0.02 (-9.14%)</td><td>0.02 (-13.04%)</td><td>0.02 (+17.40%)</td><td>0.00 <b>(-52.26%)</b></td><td>232.70 (-14.79%)</td><td>209.38 (+7.09%)</td><td>215.00 (+14.97%)</td><td>185.40 (+16.75%)</td><td>20.50 <b>(-54.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>273.10 (n/a)</td><td>195.52 (n/a)</td><td>187.00 (n/a)</td><td>158.80 (n/a)</td><td>45.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 <b>(-32.41%)</b></td><td>0.02 <b>(-21.73%)</b></td><td>0.02 (-15.41%)</td><td>0.02 (-11.60%)</td><td>0.00 <b>(-50.05%)</b></td><td>254.20 (+13.13%)</td><td>204.52 <b>(+22.56%)</b></td><td>212.20 (+18.22%)</td><td>150.30 <b>(+47.93%)</b></td><td>39.76 (-15.17%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>166.88 (n/a)</td><td>179.50 (n/a)</td><td>101.60 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+24.44%)</b></td><td>0.03 (+1.32%)</td><td>0.03 (-10.66%)</td><td>0.02 <b>(-23.51%)</b></td><td>0.01 <b>(+189.81%)</b></td><td>228.90 <b>(+30.73%)</b></td><td>156.50 (+5.25%)</td><td>160.80 (+11.98%)</td><td>106.40 (-19.64%)</td><td>48.31 <b>(+194.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.10 (n/a)</td><td>148.70 (n/a)</td><td>143.60 (n/a)</td><td>132.40 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-6.03%)</td><td>0.03 (-4.48%)</td><td>0.03 (+7.59%)</td><td>0.02 (-9.26%)</td><td>0.00 (+2.98%)</td><td>179.20 (+10.21%)</td><td>148.14 (+5.06%)</td><td>135.90 (-7.05%)</td><td>127.30 (+6.35%)</td><td>22.35 <b>(+23.08%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.60 (n/a)</td><td>141.00 (n/a)</td><td>146.20 (n/a)</td><td>119.70 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+16.92%)</td><td>0.03 <b>(+21.87%)</b></td><td>0.03 <b>(+21.61%)</b></td><td>0.03 <b>(+27.73%)</b></td><td>0.00 <b>(-37.99%)</b></td><td>163.70 <b>(-21.71%)</b></td><td>153.88 (-18.27%)</td><td>151.30 (-17.73%)</td><td>146.80 (-14.45%)</td><td>6.50 <b>(-58.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>188.28 (n/a)</td><td>183.90 (n/a)</td><td>171.60 (n/a)</td><td>15.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+41.11%)</b></td><td>0.03 (+19.44%)</td><td>0.02 (+10.36%)</td><td>0.02 <b>(+36.13%)</b></td><td>0.01 <b>(+40.71%)</b></td><td>213.70 <b>(-26.56%)</b></td><td>169.28 (-16.43%)</td><td>170.40 (-9.41%)</td><td>112.70 <b>(-29.16%)</b></td><td>36.32 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>291.00 (n/a)</td><td>202.56 (n/a)</td><td>188.10 (n/a)</td><td>159.10 (n/a)</td><td>52.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 <b>(+38.48%)</b></td><td>0.03 <b>(+21.73%)</b></td><td>0.03 (+7.03%)</td><td>0.02 (+3.54%)</td><td>0.01 <b>(+209.93%)</b></td><td>183.60 (-3.42%)</td><td>142.24 (-14.05%)</td><td>154.20 (-6.60%)</td><td>103.10 <b>(-27.75%)</b></td><td>35.57 <b>(+107.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>165.50 (n/a)</td><td>165.10 (n/a)</td><td>142.70 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (+3.76%)</td><td>0.03 <b>(+32.37%)</b></td><td>0.03 <b>(+40.43%)</b></td><td>0.02 <b>(+51.63%)</b></td><td>0.01 <b>(-27.43%)</b></td><td>191.20 <b>(-34.05%)</b></td><td>143.38 <b>(-28.47%)</b></td><td>131.70 <b>(-28.77%)</b></td><td>114.40 (-3.62%)</td><td>30.20 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>289.90 (n/a)</td><td>200.44 (n/a)</td><td>184.90 (n/a)</td><td>118.70 (n/a)</td><td>63.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-6.78%)</td><td>0.03 (+3.88%)</td><td>0.03 (-6.10%)</td><td>0.02 <b>(+34.34%)</b></td><td>0.00 <b>(-67.18%)</b></td><td>170.70 <b>(-25.56%)</b></td><td>155.22 (-8.64%)</td><td>157.20 (+6.43%)</td><td>137.10 (+7.28%)</td><td>12.02 <b>(-74.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>169.90 (n/a)</td><td>147.70 (n/a)</td><td>127.80 (n/a)</td><td>46.72 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+12.56%)</td><td>0.02 (+11.85%)</td><td>0.02 (+7.90%)</td><td>0.02 <b>(+24.14%)</b></td><td>0.00 (-3.59%)</td><td>223.70 (-19.47%)</td><td>187.12 (-11.62%)</td><td>191.70 (-7.30%)</td><td>143.80 (-11.18%)</td><td>30.17 <b>(-32.30%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>277.80 (n/a)</td><td>211.72 (n/a)</td><td>206.80 (n/a)</td><td>161.90 (n/a)</td><td>44.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+5.10%)</td><td>0.03 (-3.97%)</td><td>0.03 (+7.43%)</td><td>0.02 (-17.08%)</td><td>0.01 <b>(+29.52%)</b></td><td>217.70 <b>(+20.54%)</b></td><td>166.68 (+6.45%)</td><td>153.10 (-6.93%)</td><td>122.50 (-4.82%)</td><td>40.01 <b>(+53.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.60 (n/a)</td><td>156.58 (n/a)</td><td>164.50 (n/a)</td><td>128.70 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+4.16%)</td><td>0.02 (-0.73%)</td><td>0.02 (-9.19%)</td><td>0.02 (+0.68%)</td><td>0.00 (-14.44%)</td><td>203.40 (-0.68%)</td><td>169.14 (+0.02%)</td><td>171.10 (+10.17%)</td><td>137.70 (-4.04%)</td><td>23.66 (-18.76%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>169.10 (n/a)</td><td>155.30 (n/a)</td><td>143.50 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 <b>(+21.13%)</b></td><td>0.02 (-0.26%)</td><td>0.02 (-4.10%)</td><td>0.02 (-11.41%)</td><td>0.00 <b>(+342.96%)</b></td><td>196.70 (+12.85%)</td><td>168.88 (+2.01%)</td><td>172.20 (+4.30%)</td><td>130.50 (-17.41%)</td><td>23.99 <b>(+296.40%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.30 (n/a)</td><td>165.56 (n/a)</td><td>165.10 (n/a)</td><td>158.00 (n/a)</td><td>6.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (+3.39%)</td><td>0.05 (+6.63%)</td><td>0.05 (-2.32%)</td><td>0.04 <b>(+59.42%)</b></td><td>0.01 <b>(-22.94%)</b></td><td>208.10 <b>(-37.28%)</b></td><td>166.60 (-12.88%)</td><td>166.70 (+2.33%)</td><td>115.00 (-3.28%)</td><td>34.78 <b>(-57.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>331.80 (n/a)</td><td>191.22 (n/a)</td><td>162.90 (n/a)</td><td>118.90 (n/a)</td><td>81.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (+18.06%)</td><td>0.05 (+1.77%)</td><td>0.05 (-0.38%)</td><td>0.03 <b>(-26.57%)</b></td><td>0.02 <b>(+102.02%)</b></td><td>254.60 <b>(+36.22%)</b></td><td>168.18 (+4.24%)</td><td>159.30 (+0.38%)</td><td>108.90 (-15.32%)</td><td>54.04 <b>(+138.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>161.34 (n/a)</td><td>158.70 (n/a)</td><td>128.60 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 <b>(+26.98%)</b></td><td>0.04 (+3.64%)</td><td>0.04 (+4.00%)</td><td>0.02 <b>(-29.56%)</b></td><td>0.01 <b>(+242.31%)</b></td><td>331.80 <b>(+41.98%)</b></td><td>221.54 (+2.60%)</td><td>212.80 (-3.84%)</td><td>148.70 <b>(-21.24%)</b></td><td>67.57 <b>(+299.45%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>215.92 (n/a)</td><td>221.30 (n/a)</td><td>188.80 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+14.18%)</td><td>0.04 (+4.53%)</td><td>0.04 (-1.63%)</td><td>0.04 (-5.70%)</td><td>0.01 <b>(+85.31%)</b></td><td>233.80 (+6.03%)</td><td>188.66 (-2.40%)</td><td>195.20 (+1.67%)</td><td>146.60 (-12.43%)</td><td>35.81 <b>(+69.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.50 (n/a)</td><td>193.30 (n/a)</td><td>192.00 (n/a)</td><td>167.40 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (+3.78%)</td><td>0.05 (-6.76%)</td><td>0.05 (-6.08%)</td><td>0.04 (-16.51%)</td><td>0.01 <b>(+44.57%)</b></td><td>197.90 (+19.79%)</td><td>158.00 (+9.03%)</td><td>155.50 (+6.51%)</td><td>116.80 (-3.63%)</td><td>28.95 <b>(+63.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.20 (n/a)</td><td>144.92 (n/a)</td><td>146.00 (n/a)</td><td>121.20 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (+17.93%)</td><td>0.05 (-10.27%)</td><td>0.05 (-5.28%)</td><td>0.02 <b>(-46.88%)</b></td><td>0.02 <b>(+96.36%)</b></td><td>374.60 <b>(+88.24%)</b></td><td>197.26 <b>(+29.25%)</b></td><td>165.80 (+5.61%)</td><td>100.00 (-15.18%)</td><td>104.41 <b>(+233.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>152.62 (n/a)</td><td>157.00 (n/a)</td><td>117.90 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (+8.16%)</td><td>0.05 (+4.51%)</td><td>0.05 (+0.60%)</td><td>0.04 <b>(+37.21%)</b></td><td>0.01 (-12.58%)</td><td>203.00 <b>(-27.11%)</b></td><td>160.64 (-8.53%)</td><td>166.10 (-0.60%)</td><td>106.50 (-7.55%)</td><td>37.20 <b>(-42.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>278.50 (n/a)</td><td>175.62 (n/a)</td><td>167.10 (n/a)</td><td>115.20 (n/a)</td><td>64.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-14.39%)</td><td>0.05 (-9.21%)</td><td>0.05 (+11.49%)</td><td>0.02 <b>(-30.92%)</b></td><td>0.01 (-7.62%)</td><td>354.50 <b>(+44.75%)</b></td><td>200.98 (+14.45%)</td><td>171.30 (-10.31%)</td><td>137.70 (+16.79%)</td><td>88.02 <b>(+70.93%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>244.90 (n/a)</td><td>175.60 (n/a)</td><td>191.00 (n/a)</td><td>117.90 (n/a)</td><td>51.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-15.24%)</td><td>0.05 (-8.04%)</td><td>0.04 (-11.52%)</td><td>0.04 (-3.84%)</td><td>0.01 (-14.74%)</td><td>214.10 (+3.98%)</td><td>180.14 (+8.54%)</td><td>187.70 (+13.07%)</td><td>141.10 (+17.98%)</td><td>33.28 (+8.13%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>165.96 (n/a)</td><td>166.00 (n/a)</td><td>119.60 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+9.28%)</td><td>0.05 (+0.91%)</td><td>0.05 (-9.35%)</td><td>0.04 (-6.44%)</td><td>0.01 <b>(+56.47%)</b></td><td>205.40 (+6.87%)</td><td>167.34 (+0.65%)</td><td>174.50 (+10.30%)</td><td>134.90 (-8.48%)</td><td>30.67 <b>(+48.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>166.26 (n/a)</td><td>158.20 (n/a)</td><td>147.40 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 <b>(+25.90%)</b></td><td>0.05 (+5.77%)</td><td>0.05 (+8.35%)</td><td>0.04 <b>(-20.32%)</b></td><td>0.01 <b>(+261.17%)</b></td><td>232.90 <b>(+25.48%)</b></td><td>169.76 (-0.55%)</td><td>151.00 (-7.70%)</td><td>125.80 <b>(-20.58%)</b></td><td>45.83 <b>(+258.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.60 (n/a)</td><td>170.70 (n/a)</td><td>163.60 (n/a)</td><td>158.40 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-14.02%)</td><td>0.05 (-4.60%)</td><td>0.04 (-5.37%)</td><td>0.04 (-7.20%)</td><td>0.01 <b>(-28.80%)</b></td><td>216.70 (+7.76%)</td><td>183.58 (+4.12%)</td><td>183.90 (+5.69%)</td><td>161.20 (+16.31%)</td><td>22.39 (-12.28%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>176.32 (n/a)</td><td>174.00 (n/a)</td><td>138.60 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 <b>(+29.18%)</b></td><td>0.05 (+4.39%)</td><td>0.04 (+1.47%)</td><td>0.03 (-17.12%)</td><td>0.01 <b>(+261.58%)</b></td><td>241.20 <b>(+20.66%)</b></td><td>183.36 (-0.70%)</td><td>182.20 (-1.46%)</td><td>129.90 <b>(-22.59%)</b></td><td>39.86 <b>(+234.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>184.66 (n/a)</td><td>184.90 (n/a)</td><td>167.80 (n/a)</td><td>11.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-17.78%)</td><td>0.04 (-16.63%)</td><td>0.04 (-18.64%)</td><td>0.03 <b>(-24.16%)</b></td><td>0.01 (+3.59%)</td><td>249.70 <b>(+31.91%)</b></td><td>189.86 <b>(+21.72%)</b></td><td>192.50 <b>(+22.92%)</b></td><td>148.70 <b>(+21.69%)</b></td><td>40.72 <b>(+64.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>155.98 (n/a)</td><td>156.60 (n/a)</td><td>122.20 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-14.13%)</td><td>0.04 (-17.03%)</td><td>0.04 (-9.62%)</td><td>0.02 <b>(-46.78%)</b></td><td>0.01 <b>(+84.89%)</b></td><td>356.00 <b>(+87.86%)</b></td><td>216.36 <b>(+28.56%)</b></td><td>186.40 (+10.62%)</td><td>170.90 (+16.42%)</td><td>78.52 <b>(+320.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>168.30 (n/a)</td><td>168.50 (n/a)</td><td>146.80 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-7.91%)</td><td>0.04 (-8.75%)</td><td>0.05 (-1.09%)</td><td>0.04 (-11.03%)</td><td>0.01 (-4.92%)</td><td>218.20 (+12.36%)</td><td>184.94 (+9.76%)</td><td>179.20 (+1.07%)</td><td>157.90 (+8.60%)</td><td>25.24 (+19.01%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>168.50 (n/a)</td><td>177.30 (n/a)</td><td>145.40 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 <b>(-22.18%)</b></td><td>0.10 (-10.30%)</td><td>0.10 (-10.47%)</td><td>0.09 (+13.13%)</td><td>0.01 <b>(-56.84%)</b></td><td>191.60 (-11.58%)</td><td>170.88 (+7.27%)</td><td>167.50 (+11.67%)</td><td>146.60 <b>(+28.48%)</b></td><td>19.97 <b>(-50.28%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.70 (n/a)</td><td>159.30 (n/a)</td><td>150.00 (n/a)</td><td>114.10 (n/a)</td><td>40.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (+16.23%)</td><td>0.13 (+14.44%)</td><td>0.13 <b>(+25.26%)</b></td><td>0.10 (-2.96%)</td><td>0.02 <b>(+49.54%)</b></td><td>169.80 (+3.03%)</td><td>128.92 (-11.58%)</td><td>123.10 <b>(-20.17%)</b></td><td>108.10 (-14.00%)</td><td>23.78 <b>(+39.79%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>164.80 (n/a)</td><td>145.80 (n/a)</td><td>154.20 (n/a)</td><td>125.70 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (-18.57%)</td><td>0.07 (-19.46%)</td><td>0.08 (-16.61%)</td><td>0.05 <b>(-32.05%)</b></td><td>0.02 <b>(+23.38%)</b></td><td>323.10 <b>(+47.13%)</b></td><td>230.48 <b>(+27.44%)</b></td><td>213.40 (+19.96%)</td><td>185.20 <b>(+22.81%)</b></td><td>56.61 <b>(+120.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>180.86 (n/a)</td><td>177.90 (n/a)</td><td>150.80 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (-1.75%)</td><td>0.08 (-11.46%)</td><td>0.09 (-2.26%)</td><td>0.05 <b>(-37.81%)</b></td><td>0.02 <b>(+221.74%)</b></td><td>316.00 <b>(+60.81%)</b></td><td>214.14 (+18.95%)</td><td>179.00 (+2.34%)</td><td>170.40 (+1.79%)</td><td>61.84 <b>(+419.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>180.02 (n/a)</td><td>174.90 (n/a)</td><td>167.40 (n/a)</td><td>11.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 <b>(+22.01%)</b></td><td>0.11 (+14.31%)</td><td>0.12 <b>(+22.29%)</b></td><td>0.07 <b>(-20.27%)</b></td><td>0.02 <b>(+225.36%)</b></td><td>230.40 <b>(+25.42%)</b></td><td>155.68 (-8.90%)</td><td>141.10 (-18.20%)</td><td>128.40 (-18.06%)</td><td>42.09 <b>(+250.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>170.88 (n/a)</td><td>172.50 (n/a)</td><td>156.70 (n/a)</td><td>12.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (+0.34%)</td><td>0.11 (-2.66%)</td><td>0.11 (-4.56%)</td><td>0.09 (-4.19%)</td><td>0.01 <b>(+27.53%)</b></td><td>174.10 (+4.38%)</td><td>152.32 (+3.18%)</td><td>152.40 (+4.81%)</td><td>130.30 (-0.38%)</td><td>17.59 <b>(+32.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>166.80 (n/a)</td><td>147.62 (n/a)</td><td>145.40 (n/a)</td><td>130.80 (n/a)</td><td>13.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (-9.69%)</td><td>0.09 (-13.27%)</td><td>0.09 (-14.49%)</td><td>0.08 (-18.28%)</td><td>0.01 (+8.69%)</td><td>207.90 <b>(+22.37%)</b></td><td>179.30 (+15.74%)</td><td>177.80 (+16.90%)</td><td>152.20 (+10.69%)</td><td>20.99 <b>(+44.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>154.92 (n/a)</td><td>152.10 (n/a)</td><td>137.50 (n/a)</td><td>14.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (-4.13%)</td><td>0.11 (+8.72%)</td><td>0.11 (+8.11%)</td><td>0.10 (+9.21%)</td><td>0.02 (-15.56%)</td><td>169.80 (-8.41%)</td><td>144.82 (-8.67%)</td><td>147.00 (-7.49%)</td><td>123.90 (+4.29%)</td><td>20.31 (-19.18%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.40 (n/a)</td><td>158.56 (n/a)</td><td>158.90 (n/a)</td><td>118.80 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (+18.43%)</td><td>0.11 (+6.97%)</td><td>0.10 (+6.93%)</td><td>0.08 (+2.28%)</td><td>0.03 <b>(+26.44%)</b></td><td>217.20 (-2.25%)</td><td>160.44 (-5.01%)</td><td>169.70 (-6.45%)</td><td>105.60 (-15.52%)</td><td>43.77 (+7.00%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.20 (n/a)</td><td>168.90 (n/a)</td><td>181.40 (n/a)</td><td>125.00 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (-4.45%)</td><td>0.10 (-4.99%)</td><td>0.09 (-9.65%)</td><td>0.09 (+3.75%)</td><td>0.02 <b>(-30.54%)</b></td><td>186.80 (-3.61%)</td><td>162.58 (+3.51%)</td><td>172.70 (+10.63%)</td><td>130.80 (+4.64%)</td><td>22.20 <b>(-29.39%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.80 (n/a)</td><td>157.06 (n/a)</td><td>156.10 (n/a)</td><td>125.00 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 <b>(-30.99%)</b></td><td>0.09 <b>(-28.45%)</b></td><td>0.09 <b>(-27.14%)</b></td><td>0.07 <b>(-23.25%)</b></td><td>0.01 <b>(-44.46%)</b></td><td>220.50 <b>(+30.24%)</b></td><td>194.22 <b>(+38.91%)</b></td><td>180.10 <b>(+37.27%)</b></td><td>178.60 <b>(+44.97%)</b></td><td>20.66 (+4.58%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.30 (n/a)</td><td>139.82 (n/a)</td><td>131.20 (n/a)</td><td>123.20 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (-2.58%)</td><td>0.10 (-13.05%)</td><td>0.10 (-19.53%)</td><td>0.07 (-17.84%)</td><td>0.02 (+2.87%)</td><td>245.50 <b>(+21.72%)</b></td><td>172.98 (+16.36%)</td><td>160.90 <b>(+24.25%)</b></td><td>123.90 (+2.65%)</td><td>44.71 <b>(+32.06%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>148.66 (n/a)</td><td>129.50 (n/a)</td><td>120.70 (n/a)</td><td>33.86 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (+13.52%)</td><td>0.09 (-4.63%)</td><td>0.07 (-16.98%)</td><td>0.07 (-14.71%)</td><td>0.03 <b>(+82.46%)</b></td><td>240.60 (+17.25%)</td><td>192.78 (+10.07%)</td><td>223.70 <b>(+20.46%)</b></td><td>125.40 (-11.94%)</td><td>52.21 <b>(+93.05%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>175.14 (n/a)</td><td>185.70 (n/a)</td><td>142.40 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 <b>(-33.55%)</b></td><td>0.07 <b>(-36.17%)</b></td><td>0.07 <b>(-32.02%)</b></td><td>0.05 <b>(-49.00%)</b></td><td>0.02 (-13.50%)</td><td>338.80 <b>(+96.06%)</b></td><td>235.60 <b>(+60.51%)</b></td><td>220.80 <b>(+47.10%)</b></td><td>183.80 <b>(+50.53%)</b></td><td>60.14 <b>(+171.22%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>172.80 (n/a)</td><td>146.78 (n/a)</td><td>150.10 (n/a)</td><td>122.10 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (-11.34%)</td><td>0.08 (-12.30%)</td><td>0.08 (-8.42%)</td><td>0.06 <b>(-24.03%)</b></td><td>0.01 (+12.30%)</td><td>262.40 <b>(+31.59%)</b></td><td>205.06 (+15.34%)</td><td>204.50 (+9.18%)</td><td>169.90 (+12.82%)</td><td>37.82 <b>(+63.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>177.78 (n/a)</td><td>187.30 (n/a)</td><td>150.60 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (-10.73%)</td><td>0.08 <b>(-20.40%)</b></td><td>0.08 <b>(-25.61%)</b></td><td>0.05 <b>(-35.07%)</b></td><td>0.02 <b>(+21.27%)</b></td><td>297.90 <b>(+53.95%)</b></td><td>214.44 <b>(+29.48%)</b></td><td>211.50 <b>(+34.46%)</b></td><td>145.10 (+12.05%)</td><td>54.80 <b>(+102.51%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>165.62 (n/a)</td><td>157.30 (n/a)</td><td>129.50 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (-18.02%)</td><td>0.17 (-11.10%)</td><td>0.16 <b>(-34.67%)</b></td><td>0.14 <b>(+60.19%)</b></td><td>0.03 <b>(-64.87%)</b></td><td>231.70 <b>(-37.58%)</b></td><td>195.44 (-8.76%)</td><td>202.80 <b>(+53.06%)</b></td><td>145.90 <b>(+21.99%)</b></td><td>31.45 <b>(-73.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>371.20 (n/a)</td><td>214.20 (n/a)</td><td>132.50 (n/a)</td><td>119.60 (n/a)</td><td>120.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (-10.97%)</td><td>0.20 <b>(-23.31%)</b></td><td>0.17 <b>(-33.56%)</b></td><td>0.14 <b>(-33.92%)</b></td><td>0.05 <b>(+58.73%)</b></td><td>227.90 <b>(+51.33%)</b></td><td>176.28 <b>(+35.45%)</b></td><td>189.80 <b>(+50.52%)</b></td><td>124.40 (+12.27%)</td><td>42.73 <b>(+162.53%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>150.60 (n/a)</td><td>130.14 (n/a)</td><td>126.10 (n/a)</td><td>110.80 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (+8.59%)</td><td>0.15 (+5.72%)</td><td>0.14 (-4.02%)</td><td>0.13 <b>(+30.29%)</b></td><td>0.02 <b>(-20.10%)</b></td><td>242.80 <b>(-23.24%)</b></td><td>220.30 (-7.36%)</td><td>229.30 (+4.18%)</td><td>169.80 (-7.92%)</td><td>28.82 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>316.30 (n/a)</td><td>237.80 (n/a)</td><td>220.10 (n/a)</td><td>184.40 (n/a)</td><td>53.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (-7.75%)</td><td>0.16 (-2.35%)</td><td>0.15 (-7.76%)</td><td>0.14 <b>(+43.80%)</b></td><td>0.01 <b>(-60.04%)</b></td><td>229.10 <b>(-30.45%)</b></td><td>208.98 (-2.61%)</td><td>212.00 (+8.38%)</td><td>186.50 (+8.37%)</td><td>19.33 <b>(-70.53%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>329.40 (n/a)</td><td>214.58 (n/a)</td><td>195.60 (n/a)</td><td>172.10 (n/a)</td><td>65.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (+2.28%)</td><td>0.22 (-7.56%)</td><td>0.22 (-4.13%)</td><td>0.19 (-16.23%)</td><td>0.03 <b>(+80.14%)</b></td><td>176.50 (+19.34%)</td><td>153.02 (+9.60%)</td><td>152.30 (+4.32%)</td><td>122.10 (-2.24%)</td><td>22.28 <b>(+110.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>147.90 (n/a)</td><td>139.62 (n/a)</td><td>146.00 (n/a)</td><td>124.90 (n/a)</td><td>10.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (+10.11%)</td><td>0.19 (-6.99%)</td><td>0.18 (-14.68%)</td><td>0.15 (-2.17%)</td><td>0.05 <b>(+32.51%)</b></td><td>213.70 (+2.20%)</td><td>177.50 (+9.39%)</td><td>186.60 (+17.21%)</td><td>122.40 (-9.13%)</td><td>38.52 <b>(+26.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.10 (n/a)</td><td>162.26 (n/a)</td><td>159.20 (n/a)</td><td>134.70 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (-1.44%)</td><td>0.22 (+5.82%)</td><td>0.22 (+10.61%)</td><td>0.15 (-6.70%)</td><td>0.05 (-1.11%)</td><td>217.40 (+7.15%)</td><td>156.24 (-5.11%)</td><td>150.30 (-9.62%)</td><td>116.70 (+1.48%)</td><td>37.52 (+13.32%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>202.90 (n/a)</td><td>164.66 (n/a)</td><td>166.30 (n/a)</td><td>115.00 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (+5.15%)</td><td>0.21 (+5.43%)</td><td>0.20 (+8.38%)</td><td>0.18 (-1.88%)</td><td>0.04 <b>(+23.45%)</b></td><td>186.60 (+1.91%)</td><td>159.96 (-4.33%)</td><td>165.90 (-7.73%)</td><td>122.90 (-4.88%)</td><td>27.78 <b>(+21.64%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.10 (n/a)</td><td>167.20 (n/a)</td><td>179.80 (n/a)</td><td>129.20 (n/a)</td><td>22.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 <b>(-24.71%)</b></td><td>0.17 <b>(-25.85%)</b></td><td>0.18 (-15.67%)</td><td>0.11 <b>(-37.25%)</b></td><td>0.05 (-19.61%)</td><td>298.10 <b>(+59.41%)</b></td><td>200.22 <b>(+37.36%)</b></td><td>186.40 (+18.58%)</td><td>140.20 <b>(+32.89%)</b></td><td>60.84 <b>(+78.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>187.00 (n/a)</td><td>145.76 (n/a)</td><td>157.20 (n/a)</td><td>105.50 (n/a)</td><td>34.12 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (+5.42%)</td><td>0.23 (-0.80%)</td><td>0.22 (-11.00%)</td><td>0.18 (-3.58%)</td><td>0.04 (+17.83%)</td><td>184.50 (+3.71%)</td><td>148.74 (+1.53%)</td><td>151.00 (+12.35%)</td><td>117.40 (-5.17%)</td><td>28.23 (+13.61%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>177.90 (n/a)</td><td>146.50 (n/a)</td><td>134.40 (n/a)</td><td>123.80 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 <b>(-26.02%)</b></td><td>0.20 (-17.69%)</td><td>0.19 (-17.63%)</td><td>0.18 (-10.50%)</td><td>0.02 <b>(-56.43%)</b></td><td>181.80 (+11.67%)</td><td>167.32 (+19.75%)</td><td>172.50 <b>(+21.39%)</b></td><td>147.50 <b>(+35.20%)</b></td><td>14.03 <b>(-34.25%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>162.80 (n/a)</td><td>139.72 (n/a)</td><td>142.10 (n/a)</td><td>109.10 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 <b>(-23.93%)</b></td><td>0.17 <b>(-25.54%)</b></td><td>0.19 <b>(-21.89%)</b></td><td>0.09 <b>(-46.98%)</b></td><td>0.05 (+4.28%)</td><td>371.20 <b>(+88.62%)</b></td><td>217.72 <b>(+42.32%)</b></td><td>173.20 <b>(+28.01%)</b></td><td>163.50 <b>(+31.43%)</b></td><td>87.66 <b>(+165.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.80 (n/a)</td><td>152.98 (n/a)</td><td>135.30 (n/a)</td><td>124.40 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (+1.86%)</td><td>0.19 (-7.03%)</td><td>0.17 (-17.48%)</td><td>0.16 (+1.32%)</td><td>0.03 <b>(+22.65%)</b></td><td>204.30 (-1.30%)</td><td>179.30 (+8.33%)</td><td>195.10 <b>(+21.18%)</b></td><td>136.20 (-1.80%)</td><td>29.13 (+16.22%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.00 (n/a)</td><td>165.52 (n/a)</td><td>161.00 (n/a)</td><td>138.70 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (+0.76%)</td><td>0.19 (-6.26%)</td><td>0.19 (-9.49%)</td><td>0.17 (-3.39%)</td><td>0.03 (+10.64%)</td><td>192.50 (+3.49%)</td><td>171.46 (+6.98%)</td><td>174.70 (+10.50%)</td><td>132.70 (-0.82%)</td><td>23.06 (+10.27%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.00 (n/a)</td><td>160.28 (n/a)</td><td>158.10 (n/a)</td><td>133.80 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 <b>(-32.54%)</b></td><td>0.16 (-8.44%)</td><td>0.17 (+1.43%)</td><td>0.14 (+9.69%)</td><td>0.02 <b>(-66.96%)</b></td><td>234.70 (-8.82%)</td><td>204.86 (+3.14%)</td><td>195.20 (-1.41%)</td><td>181.50 <b>(+48.16%)</b></td><td>24.06 <b>(-54.64%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>257.40 (n/a)</td><td>198.62 (n/a)</td><td>198.00 (n/a)</td><td>122.50 (n/a)</td><td>53.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (+6.89%)</td><td>0.18 (+10.45%)</td><td>0.19 (+19.93%)</td><td>0.12 (+19.87%)</td><td>0.05 (+4.10%)</td><td>269.80 (-16.57%)</td><td>190.86 (-10.39%)</td><td>169.10 (-16.62%)</td><td>127.00 (-6.41%)</td><td>55.01 (-19.39%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>323.40 (n/a)</td><td>212.98 (n/a)</td><td>202.80 (n/a)</td><td>135.70 (n/a)</td><td>68.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (+0.93%)</td><td>0.18 (+0.25%)</td><td>0.18 (-0.02%)</td><td>0.18 (+0.23%)</td><td>0.00 <b>(+132.84%)</b></td><td>47527.00 (-0.23%)</td><td>47347.24 (-0.24%)</td><td>47441.80 (+0.02%)</td><td>46950.90 (-0.92%)</td><td>228.92 <b>(+129.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47636.90 (n/a)</td><td>47462.98 (n/a)</td><td>47432.80 (n/a)</td><td>47388.40 (n/a)</td><td>99.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (+0.73%)</td><td>0.18 (+0.28%)</td><td>0.18 (+0.20%)</td><td>0.18 (+0.15%)</td><td>0.00 <b>(+266.99%)</b></td><td>47421.70 (-0.15%)</td><td>47300.50 (-0.27%)</td><td>47326.70 (-0.20%)</td><td>47046.90 (-0.72%)</td><td>149.39 <b>(+263.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47494.90 (n/a)</td><td>47430.66 (n/a)</td><td>47423.00 (n/a)</td><td>47390.00 (n/a)</td><td>41.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (+0.02%)</td><td>0.11 (+0.03%)</td><td>0.11 (+0.05%)</td><td>0.11 (+0.03%)</td><td>0.00 <b>(-20.50%)</b></td><td>374539.30 (-0.03%)</td><td>374426.16 (-0.03%)</td><td>374384.60 (-0.05%)</td><td>374336.20 (-0.02%)</td><td>86.26 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374669.70 (n/a)</td><td>374540.80 (n/a)</td><td>374564.80 (n/a)</td><td>374398.20 (n/a)</td><td>108.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-0.79%)</td><td>0.03 (+3.37%)</td><td>0.03 (+4.64%)</td><td>0.02 (+14.21%)</td><td>0.00 (-15.44%)</td><td>193.20 (-12.46%)</td><td>162.84 (-4.19%)</td><td>153.00 (-4.43%)</td><td>136.70 (+0.81%)</td><td>23.97 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.70 (n/a)</td><td>169.96 (n/a)</td><td>160.10 (n/a)</td><td>135.60 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-3.48%)</td><td>0.04 (+7.95%)</td><td>0.04 (+2.40%)</td><td>0.04 <b>(+26.49%)</b></td><td>0.00 <b>(-59.43%)</b></td><td>155.90 <b>(-20.94%)</b></td><td>145.02 (-9.37%)</td><td>141.70 (-2.34%)</td><td>133.90 (+3.64%)</td><td>9.57 <b>(-67.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>160.02 (n/a)</td><td>145.10 (n/a)</td><td>129.20 (n/a)</td><td>29.02 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-3.19%)</td><td>0.03 (+0.78%)</td><td>0.03 (-0.16%)</td><td>0.02 (+4.39%)</td><td>0.00 (-15.67%)</td><td>191.20 (-4.21%)</td><td>158.34 (-1.25%)</td><td>155.70 (+0.13%)</td><td>139.90 (+3.32%)</td><td>19.63 (-17.15%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.60 (n/a)</td><td>160.34 (n/a)</td><td>155.50 (n/a)</td><td>135.40 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (-6.01%)</td><td>0.04 (+10.37%)</td><td>0.04 (+7.36%)</td><td>0.03 <b>(+22.94%)</b></td><td>0.00 <b>(-61.86%)</b></td><td>156.00 (-18.67%)</td><td>143.86 (-11.38%)</td><td>142.70 (-6.85%)</td><td>133.00 (+6.40%)</td><td>9.07 <b>(-67.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>162.34 (n/a)</td><td>153.20 (n/a)</td><td>125.00 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-10.60%)</td><td>0.03 (+3.92%)</td><td>0.03 (+18.65%)</td><td>0.02 <b>(+40.66%)</b></td><td>0.00 <b>(-52.71%)</b></td><td>201.80 <b>(-28.89%)</b></td><td>164.74 (-9.99%)</td><td>154.80 (-15.69%)</td><td>140.50 (+11.86%)</td><td>24.13 <b>(-61.56%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>283.80 (n/a)</td><td>183.02 (n/a)</td><td>183.60 (n/a)</td><td>125.60 (n/a)</td><td>62.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (-8.98%)</td><td>0.03 (+3.29%)</td><td>0.03 (+5.68%)</td><td>0.03 (+9.71%)</td><td>0.00 <b>(-39.19%)</b></td><td>179.20 (-8.85%)</td><td>161.46 (-4.75%)</td><td>166.60 (-5.34%)</td><td>140.30 (+9.87%)</td><td>17.44 <b>(-39.77%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>169.52 (n/a)</td><td>176.00 (n/a)</td><td>127.70 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-3.12%)</td><td>0.03 (+1.69%)</td><td>0.03 (+8.71%)</td><td>0.02 (+9.64%)</td><td>0.00 <b>(-24.64%)</b></td><td>196.20 (-8.79%)</td><td>163.68 (-3.72%)</td><td>160.30 (-8.03%)</td><td>129.30 (+3.19%)</td><td>29.64 <b>(-26.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>170.00 (n/a)</td><td>174.30 (n/a)</td><td>125.30 (n/a)</td><td>40.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-13.55%)</td><td>0.03 (-1.63%)</td><td>0.03 (+5.65%)</td><td>0.02 (+0.60%)</td><td>0.00 <b>(-32.63%)</b></td><td>207.90 (-0.57%)</td><td>184.18 (+0.70%)</td><td>179.10 (-5.34%)</td><td>160.70 (+15.69%)</td><td>22.04 (-19.96%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>182.90 (n/a)</td><td>189.20 (n/a)</td><td>138.90 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+5.60%)</td><td>0.03 (+13.83%)</td><td>0.03 <b>(+26.54%)</b></td><td>0.02 <b>(+20.66%)</b></td><td>0.00 (-3.52%)</td><td>190.90 (-17.11%)</td><td>150.12 (-12.94%)</td><td>135.70 <b>(-21.01%)</b></td><td>122.40 (-5.34%)</td><td>28.13 <b>(-24.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>172.44 (n/a)</td><td>171.80 (n/a)</td><td>129.30 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-8.07%)</td><td>0.03 (+5.99%)</td><td>0.03 (+5.70%)</td><td>0.02 <b>(+35.34%)</b></td><td>0.00 <b>(-45.16%)</b></td><td>220.20 <b>(-26.11%)</b></td><td>180.74 (-9.42%)</td><td>173.40 (-5.40%)</td><td>161.60 (+8.75%)</td><td>23.94 <b>(-58.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>298.00 (n/a)</td><td>199.54 (n/a)</td><td>183.30 (n/a)</td><td>148.60 (n/a)</td><td>57.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (-5.87%)</td><td>0.03 (+4.65%)</td><td>0.03 (+8.65%)</td><td>0.02 <b>(+20.85%)</b></td><td>0.01 <b>(-20.02%)</b></td><td>222.30 (-17.24%)</td><td>170.10 (-7.66%)</td><td>159.50 (-7.91%)</td><td>129.10 (+6.17%)</td><td>41.95 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>184.22 (n/a)</td><td>173.20 (n/a)</td><td>121.60 (n/a)</td><td>59.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+0.18%)</td><td>0.02 (-0.50%)</td><td>0.03 (+6.90%)</td><td>0.02 (-14.38%)</td><td>0.00 <b>(+34.16%)</b></td><td>248.50 (+16.83%)</td><td>191.84 (+1.88%)</td><td>172.70 (-6.45%)</td><td>158.70 (-0.19%)</td><td>36.57 <b>(+54.23%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>188.30 (n/a)</td><td>184.60 (n/a)</td><td>159.00 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+0.10%)</td><td>0.02 (+0.89%)</td><td>0.02 (+6.61%)</td><td>0.02 (-5.87%)</td><td>0.00 (+15.84%)</td><td>218.50 (+6.27%)</td><td>180.32 (-0.32%)</td><td>179.70 (-6.21%)</td><td>148.60 (-0.07%)</td><td>28.07 <b>(+23.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>180.90 (n/a)</td><td>191.60 (n/a)</td><td>148.70 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+0.88%)</td><td>0.02 (-1.82%)</td><td>0.02 (-0.06%)</td><td>0.02 (-13.92%)</td><td>0.00 <b>(+44.38%)</b></td><td>243.90 (+16.20%)</td><td>200.88 (+3.11%)</td><td>203.50 (+0.05%)</td><td>161.50 (-0.92%)</td><td>32.50 <b>(+65.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>194.82 (n/a)</td><td>203.40 (n/a)</td><td>163.00 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.03 (+13.43%)</td><td>0.02 <b>(+22.50%)</b></td><td>0.02 <b>(+24.41%)</b></td><td>0.02 <b>(+31.97%)</b></td><td>0.00 (-16.85%)</td><td>209.20 <b>(-24.23%)</b></td><td>184.42 (-19.30%)</td><td>185.30 (-19.61%)</td><td>153.90 (-11.86%)</td><td>20.26 <b>(-43.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.10 (n/a)</td><td>228.52 (n/a)</td><td>230.50 (n/a)</td><td>174.60 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-7.98%)</td><td>0.05 (+6.78%)</td><td>0.05 (+11.97%)</td><td>0.05 <b>(+29.34%)</b></td><td>0.01 <b>(-41.61%)</b></td><td>180.70 <b>(-22.71%)</b></td><td>155.88 (-10.47%)</td><td>163.20 (-10.67%)</td><td>129.00 (+8.68%)</td><td>23.59 <b>(-50.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>174.10 (n/a)</td><td>182.70 (n/a)</td><td>118.70 (n/a)</td><td>47.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 (-17.88%)</td><td>0.07 (-19.59%)</td><td>0.07 (-4.07%)</td><td>0.04 <b>(-33.02%)</b></td><td>0.02 (-19.32%)</td><td>276.00 <b>(+49.35%)</b></td><td>195.58 <b>(+25.21%)</b></td><td>183.50 (+4.26%)</td><td>139.30 <b>(+21.77%)</b></td><td>50.17 <b>(+48.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>156.20 (n/a)</td><td>176.00 (n/a)</td><td>114.40 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-6.97%)</td><td>0.05 (-6.03%)</td><td>0.05 (-13.05%)</td><td>0.04 (+9.29%)</td><td>0.01 <b>(-34.29%)</b></td><td>196.10 (-8.49%)</td><td>170.18 (+4.39%)</td><td>170.10 (+15.01%)</td><td>141.30 (+7.53%)</td><td>22.85 <b>(-34.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>163.02 (n/a)</td><td>147.90 (n/a)</td><td>131.40 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.08 (+10.91%)</td><td>0.06 (+4.50%)</td><td>0.07 (+0.49%)</td><td>0.05 (+6.48%)</td><td>0.01 <b>(+26.14%)</b></td><td>204.10 (-6.07%)</td><td>165.44 (-3.30%)</td><td>149.70 (-0.47%)</td><td>131.70 (-9.79%)</td><td>35.56 (+11.93%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>171.08 (n/a)</td><td>150.40 (n/a)</td><td>146.00 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+6.00%)</td><td>0.05 (+2.77%)</td><td>0.05 (+3.42%)</td><td>0.04 (-2.63%)</td><td>0.01 (+10.71%)</td><td>199.70 (+2.73%)</td><td>166.04 (-2.47%)</td><td>164.90 (-3.28%)</td><td>141.30 (-5.67%)</td><td>21.56 (+9.98%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>170.24 (n/a)</td><td>170.50 (n/a)</td><td>149.80 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.07 (-6.17%)</td><td>0.06 (+0.94%)</td><td>0.06 (+4.84%)</td><td>0.06 (+13.06%)</td><td>0.01 <b>(-51.50%)</b></td><td>174.50 (-11.51%)</td><td>162.50 (-2.90%)</td><td>167.50 (-4.61%)</td><td>140.50 (+6.60%)</td><td>13.19 <b>(-54.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>167.36 (n/a)</td><td>175.60 (n/a)</td><td>131.80 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (-11.37%)</td><td>0.05 (-12.39%)</td><td>0.05 (-8.61%)</td><td>0.04 (-3.04%)</td><td>0.01 <b>(-29.70%)</b></td><td>206.40 (+3.10%)</td><td>174.66 (+12.58%)</td><td>176.20 (+9.44%)</td><td>138.50 (+12.88%)</td><td>27.83 (-14.51%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>155.14 (n/a)</td><td>161.00 (n/a)</td><td>122.70 (n/a)</td><td>32.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 <b>(-24.66%)</b></td><td>0.05 (-19.21%)</td><td>0.04 <b>(-22.70%)</b></td><td>0.04 (-15.41%)</td><td>0.01 <b>(-34.99%)</b></td><td>239.80 (+18.24%)</td><td>204.56 <b>(+22.71%)</b></td><td>205.30 <b>(+29.36%)</b></td><td>169.20 <b>(+32.71%)</b></td><td>29.89 (+1.52%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>166.70 (n/a)</td><td>158.70 (n/a)</td><td>127.50 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+5.01%)</td><td>0.05 (-10.02%)</td><td>0.05 (-17.72%)</td><td>0.04 (-12.25%)</td><td>0.01 <b>(+81.95%)</b></td><td>196.00 (+13.95%)</td><td>171.14 (+12.79%)</td><td>175.50 <b>(+21.54%)</b></td><td>135.20 (-4.72%)</td><td>26.42 <b>(+101.96%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>151.74 (n/a)</td><td>144.40 (n/a)</td><td>141.90 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+6.44%)</td><td>0.05 (-3.82%)</td><td>0.05 (-11.03%)</td><td>0.04 (-3.60%)</td><td>0.01 (+16.94%)</td><td>230.20 (+3.74%)</td><td>189.32 (+4.62%)</td><td>192.20 (+12.40%)</td><td>145.90 (-6.05%)</td><td>32.58 (+14.19%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>180.96 (n/a)</td><td>171.00 (n/a)</td><td>155.30 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+17.30%)</td><td>0.05 (+15.23%)</td><td>0.05 (+3.71%)</td><td>0.04 (+15.96%)</td><td>0.01 <b>(+39.17%)</b></td><td>194.70 (-13.77%)</td><td>159.50 (-12.74%)</td><td>166.50 (-3.53%)</td><td>133.60 (-14.74%)</td><td>25.85 (-3.08%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>182.78 (n/a)</td><td>172.60 (n/a)</td><td>156.70 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+6.31%)</td><td>0.05 (+4.14%)</td><td>0.05 (+17.80%)</td><td>0.04 (-6.29%)</td><td>0.01 <b>(+28.72%)</b></td><td>229.00 (+6.71%)</td><td>187.26 (-3.15%)</td><td>176.50 (-15.10%)</td><td>152.20 (-5.93%)</td><td>30.71 <b>(+30.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>193.36 (n/a)</td><td>207.90 (n/a)</td><td>161.80 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.06 (+2.51%)</td><td>0.05 (+0.09%)</td><td>0.05 (+0.04%)</td><td>0.04 (-7.06%)</td><td>0.01 (+10.85%)</td><td>226.80 (+7.59%)</td><td>173.10 (+0.51%)</td><td>162.60 (-0.06%)</td><td>140.30 (-2.43%)</td><td>32.67 (+19.01%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>172.22 (n/a)</td><td>162.70 (n/a)</td><td>143.80 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.05 (-19.14%)</td><td>0.05 (+0.97%)</td><td>0.05 <b>(+23.54%)</b></td><td>0.03 (-18.70%)</td><td>0.01 (-19.79%)</td><td>261.90 <b>(+23.02%)</b></td><td>190.12 (-0.96%)</td><td>169.40 (-19.06%)</td><td>167.80 <b>(+23.66%)</b></td><td>40.58 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>191.96 (n/a)</td><td>209.30 (n/a)</td><td>135.70 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.04 (-3.18%)</td><td>0.04 (+4.09%)</td><td>0.04 (+6.99%)</td><td>0.03 (+16.34%)</td><td>0.00 <b>(-34.01%)</b></td><td>240.10 (-14.07%)</td><td>206.48 (-5.61%)</td><td>205.00 (-6.52%)</td><td>182.30 (+3.29%)</td><td>24.93 <b>(-41.14%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.40 (n/a)</td><td>218.76 (n/a)</td><td>219.30 (n/a)</td><td>176.50 (n/a)</td><td>42.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (-18.62%)</td><td>0.10 (-1.20%)</td><td>0.10 (+6.52%)</td><td>0.09 (+13.31%)</td><td>0.01 <b>(-62.48%)</b></td><td>187.10 (-11.75%)</td><td>169.82 (-1.43%)</td><td>164.80 (-6.10%)</td><td>155.50 <b>(+22.83%)</b></td><td>13.54 <b>(-58.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>172.28 (n/a)</td><td>175.50 (n/a)</td><td>126.60 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (+5.60%)</td><td>0.14 (-2.22%)</td><td>0.15 (+1.11%)</td><td>0.11 <b>(-20.29%)</b></td><td>0.02 <b>(+91.21%)</b></td><td>231.60 <b>(+25.46%)</b></td><td>176.38 (+4.18%)</td><td>166.40 (-1.13%)</td><td>147.00 (-5.28%)</td><td>32.71 <b>(+134.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>169.30 (n/a)</td><td>168.30 (n/a)</td><td>155.20 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-8.10%)</td><td>0.10 (-15.47%)</td><td>0.10 (-10.25%)</td><td>0.07 <b>(-23.06%)</b></td><td>0.02 <b>(+27.66%)</b></td><td>220.00 <b>(+29.95%)</b></td><td>176.12 <b>(+20.19%)</b></td><td>164.30 (+11.47%)</td><td>136.70 (+8.84%)</td><td>33.02 <b>(+83.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.30 (n/a)</td><td>146.54 (n/a)</td><td>147.40 (n/a)</td><td>125.60 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (-5.60%)</td><td>0.10 (-19.15%)</td><td>0.10 <b>(-23.83%)</b></td><td>0.08 <b>(-25.35%)</b></td><td>0.03 <b>(+33.88%)</b></td><td>271.30 <b>(+33.91%)</b></td><td>206.92 <b>(+26.98%)</b></td><td>210.40 <b>(+31.34%)</b></td><td>141.90 (+5.90%)</td><td>47.24 <b>(+83.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>162.96 (n/a)</td><td>160.20 (n/a)</td><td>134.00 (n/a)</td><td>25.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (-1.56%)</td><td>0.10 (-4.47%)</td><td>0.10 (+0.66%)</td><td>0.07 (-11.92%)</td><td>0.02 (+10.36%)</td><td>219.40 (+13.56%)</td><td>168.62 (+5.78%)</td><td>164.00 (-0.61%)</td><td>120.90 (+1.60%)</td><td>35.56 <b>(+28.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.20 (n/a)</td><td>159.40 (n/a)</td><td>165.00 (n/a)</td><td>119.00 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (+2.80%)</td><td>0.11 (-8.24%)</td><td>0.11 (-9.86%)</td><td>0.09 (-18.74%)</td><td>0.02 <b>(+149.58%)</b></td><td>220.50 <b>(+23.05%)</b></td><td>185.60 (+10.77%)</td><td>184.20 (+10.90%)</td><td>150.00 (-2.72%)</td><td>28.15 <b>(+199.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>179.20 (n/a)</td><td>167.56 (n/a)</td><td>166.10 (n/a)</td><td>154.20 (n/a)</td><td>9.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-12.53%)</td><td>0.11 (+17.40%)</td><td>0.11 <b>(+30.34%)</b></td><td>0.10 <b>(+85.47%)</b></td><td>0.01 <b>(-76.00%)</b></td><td>162.30 <b>(-46.10%)</b></td><td>148.64 <b>(-24.66%)</b></td><td>143.40 <b>(-23.27%)</b></td><td>137.50 (+14.30%)</td><td>12.04 <b>(-84.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>301.10 (n/a)</td><td>197.28 (n/a)</td><td>186.90 (n/a)</td><td>120.30 (n/a)</td><td>78.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (-3.48%)</td><td>0.10 (-11.19%)</td><td>0.10 (-12.34%)</td><td>0.09 (-9.15%)</td><td>0.01 (+1.49%)</td><td>209.10 (+10.05%)</td><td>181.50 (+12.87%)</td><td>176.10 (+14.05%)</td><td>146.20 (+3.61%)</td><td>24.82 (+16.93%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>160.80 (n/a)</td><td>154.40 (n/a)</td><td>141.10 (n/a)</td><td>21.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 <b>(-27.07%)</b></td><td>0.09 <b>(-22.12%)</b></td><td>0.09 (-16.09%)</td><td>0.07 <b>(-22.67%)</b></td><td>0.01 <b>(-40.26%)</b></td><td>241.80 <b>(+29.30%)</b></td><td>187.52 <b>(+26.91%)</b></td><td>175.00 (+19.13%)</td><td>156.00 <b>(+37.08%)</b></td><td>33.02 (+9.31%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.00 (n/a)</td><td>147.76 (n/a)</td><td>146.90 (n/a)</td><td>113.80 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-8.47%)</td><td>0.12 (+6.18%)</td><td>0.12 (+14.11%)</td><td>0.10 (+12.50%)</td><td>0.01 <b>(-52.70%)</b></td><td>181.20 (-11.09%)</td><td>158.94 (-7.44%)</td><td>152.50 (-12.41%)</td><td>149.30 (+9.30%)</td><td>13.01 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>171.72 (n/a)</td><td>174.10 (n/a)</td><td>136.60 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (-11.85%)</td><td>0.09 (-12.19%)</td><td>0.09 (-19.94%)</td><td>0.07 <b>(+35.72%)</b></td><td>0.02 <b>(-41.84%)</b></td><td>223.00 <b>(-26.31%)</b></td><td>188.64 (+6.78%)</td><td>187.70 <b>(+24.88%)</b></td><td>148.80 (+13.41%)</td><td>32.77 <b>(-53.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>302.60 (n/a)</td><td>176.66 (n/a)</td><td>150.30 (n/a)</td><td>131.20 (n/a)</td><td>70.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 (+3.86%)</td><td>0.10 (-1.34%)</td><td>0.10 (+2.08%)</td><td>0.07 (-16.41%)</td><td>0.02 <b>(+40.77%)</b></td><td>248.70 (+19.62%)</td><td>182.34 (+3.67%)</td><td>168.30 (-2.04%)</td><td>137.10 (-3.72%)</td><td>42.78 <b>(+64.07%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>175.88 (n/a)</td><td>171.80 (n/a)</td><td>142.40 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 (+4.39%)</td><td>0.08 (-6.56%)</td><td>0.09 (+8.07%)</td><td>0.06 <b>(-26.15%)</b></td><td>0.02 <b>(+111.04%)</b></td><td>284.60 <b>(+35.39%)</b></td><td>209.60 (+13.10%)</td><td>175.70 (-7.48%)</td><td>149.00 (-4.18%)</td><td>61.79 <b>(+185.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>185.32 (n/a)</td><td>189.90 (n/a)</td><td>155.50 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.09 <b>(-36.74%)</b></td><td>0.08 (-10.88%)</td><td>0.08 (+1.99%)</td><td>0.07 (+1.67%)</td><td>0.01 <b>(-75.78%)</b></td><td>239.80 (-1.64%)</td><td>216.90 (+6.25%)</td><td>218.60 (-1.97%)</td><td>195.80 <b>(+58.03%)</b></td><td>18.53 <b>(-61.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>243.80 (n/a)</td><td>204.14 (n/a)</td><td>223.00 (n/a)</td><td>123.90 (n/a)</td><td>47.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.10 (+7.47%)</td><td>0.08 (+4.62%)</td><td>0.08 (-11.43%)</td><td>0.07 <b>(+55.06%)</b></td><td>0.01 <b>(-35.30%)</b></td><td>224.40 <b>(-35.50%)</b></td><td>201.48 (-8.71%)</td><td>215.70 (+12.93%)</td><td>164.80 (-6.95%)</td><td>26.86 <b>(-62.48%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>347.90 (n/a)</td><td>220.70 (n/a)</td><td>191.00 (n/a)</td><td>177.10 (n/a)</td><td>71.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (-7.36%)</td><td>0.19 (+4.91%)</td><td>0.19 (+9.55%)</td><td>0.17 (+17.77%)</td><td>0.03 <b>(-42.13%)</b></td><td>194.70 (-15.09%)</td><td>171.08 (-7.65%)</td><td>174.90 (-8.72%)</td><td>147.10 (+7.92%)</td><td>22.54 <b>(-47.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.30 (n/a)</td><td>185.26 (n/a)</td><td>191.60 (n/a)</td><td>136.30 (n/a)</td><td>43.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-4.08%)</td><td>0.20 (+0.50%)</td><td>0.20 (-4.04%)</td><td>0.17 <b>(+35.05%)</b></td><td>0.03 <b>(-44.09%)</b></td><td>191.60 <b>(-25.97%)</b></td><td>164.36 (-4.96%)</td><td>164.60 (+4.18%)</td><td>133.10 (+4.23%)</td><td>21.66 <b>(-58.28%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>258.80 (n/a)</td><td>172.94 (n/a)</td><td>158.00 (n/a)</td><td>127.70 (n/a)</td><td>51.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 <b>(-31.16%)</b></td><td>0.20 (-16.89%)</td><td>0.21 (-10.53%)</td><td>0.18 (-4.55%)</td><td>0.02 <b>(-63.72%)</b></td><td>225.80 (+4.78%)</td><td>204.38 (+17.26%)</td><td>196.90 (+11.75%)</td><td>180.70 <b>(+45.26%)</b></td><td>19.23 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>215.50 (n/a)</td><td>174.30 (n/a)</td><td>176.20 (n/a)</td><td>124.40 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-13.65%)</td><td>0.20 (-11.18%)</td><td>0.23 (+11.58%)</td><td>0.11 <b>(-30.37%)</b></td><td>0.05 (-3.50%)</td><td>288.90 <b>(+43.66%)</b></td><td>178.86 (+16.11%)</td><td>144.70 (-10.40%)</td><td>133.70 (+15.76%)</td><td>64.88 <b>(+71.30%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>201.10 (n/a)</td><td>154.04 (n/a)</td><td>161.50 (n/a)</td><td>115.50 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (-0.39%)</td><td>0.22 (-12.28%)</td><td>0.22 (-2.98%)</td><td>0.13 <b>(-36.94%)</b></td><td>0.08 <b>(+46.76%)</b></td><td>326.20 <b>(+58.58%)</b></td><td>210.22 <b>(+22.91%)</b></td><td>183.80 (+3.03%)</td><td>126.20 (+0.40%)</td><td>79.19 <b>(+136.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>205.70 (n/a)</td><td>171.04 (n/a)</td><td>178.40 (n/a)</td><td>125.70 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (-7.44%)</td><td>0.21 (+4.73%)</td><td>0.23 <b>(+20.45%)</b></td><td>0.14 <b>(-23.81%)</b></td><td>0.04 <b>(+29.16%)</b></td><td>236.00 <b>(+31.26%)</b></td><td>160.98 (-2.04%)</td><td>142.00 (-16.96%)</td><td>135.30 (+7.98%)</td><td>42.70 <b>(+88.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>179.80 (n/a)</td><td>164.34 (n/a)</td><td>171.00 (n/a)</td><td>125.30 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (+9.65%)</td><td>0.24 (+2.39%)</td><td>0.27 (+12.89%)</td><td>0.15 (-19.20%)</td><td>0.06 <b>(+85.24%)</b></td><td>252.50 <b>(+23.77%)</b></td><td>165.48 (+2.44%)</td><td>138.50 (-11.45%)</td><td>124.20 (-8.81%)</td><td>52.43 <b>(+106.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>204.00 (n/a)</td><td>161.54 (n/a)</td><td>156.40 (n/a)</td><td>136.20 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (+17.80%)</td><td>0.21 (+4.09%)</td><td>0.19 (-3.61%)</td><td>0.18 (-4.12%)</td><td>0.04 <b>(+140.84%)</b></td><td>185.50 (+4.27%)</td><td>159.58 (-1.99%)</td><td>173.40 (+3.77%)</td><td>125.70 (-15.12%)</td><td>27.07 <b>(+114.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>162.82 (n/a)</td><td>167.10 (n/a)</td><td>148.10 (n/a)</td><td>12.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-8.96%)</td><td>0.22 (-3.96%)</td><td>0.22 (-5.79%)</td><td>0.17 (+4.14%)</td><td>0.03 <b>(-29.98%)</b></td><td>214.10 (-3.99%)</td><td>173.58 (+2.80%)</td><td>167.30 (+6.09%)</td><td>150.40 (+9.86%)</td><td>24.11 <b>(-26.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>223.00 (n/a)</td><td>168.86 (n/a)</td><td>157.70 (n/a)</td><td>136.90 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (+14.34%)</td><td>0.19 (+13.56%)</td><td>0.18 (+1.40%)</td><td>0.17 <b>(+60.42%)</b></td><td>0.03 <b>(-27.76%)</b></td><td>192.80 <b>(-37.67%)</b></td><td>172.18 (-15.37%)</td><td>181.50 (-1.36%)</td><td>137.20 (-12.50%)</td><td>22.33 <b>(-63.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>309.30 (n/a)</td><td>203.44 (n/a)</td><td>184.00 (n/a)</td><td>156.80 (n/a)</td><td>60.62 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (-6.64%)</td><td>0.19 (-2.39%)</td><td>0.21 (+0.08%)</td><td>0.16 (-4.70%)</td><td>0.03 (-6.80%)</td><td>221.10 (+4.94%)</td><td>184.48 (+2.38%)</td><td>169.40 (-0.06%)</td><td>156.00 (+7.07%)</td><td>28.35 (+3.62%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>210.70 (n/a)</td><td>180.20 (n/a)</td><td>169.50 (n/a)</td><td>145.70 (n/a)</td><td>27.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (+13.19%)</td><td>0.19 (+3.22%)</td><td>0.20 (+10.60%)</td><td>0.13 <b>(-23.69%)</b></td><td>0.04 <b>(+155.30%)</b></td><td>255.30 <b>(+30.99%)</b></td><td>177.28 (+0.73%)</td><td>162.10 (-9.59%)</td><td>136.50 (-11.65%)</td><td>46.07 <b>(+210.34%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>176.00 (n/a)</td><td>179.30 (n/a)</td><td>154.50 (n/a)</td><td>14.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (-5.42%)</td><td>0.21 (+11.83%)</td><td>0.21 <b>(+23.36%)</b></td><td>0.18 (+15.46%)</td><td>0.02 <b>(-46.39%)</b></td><td>192.60 (-13.40%)</td><td>169.58 (-12.23%)</td><td>169.50 (-18.94%)</td><td>150.90 (+5.67%)</td><td>15.90 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>222.40 (n/a)</td><td>193.20 (n/a)</td><td>209.10 (n/a)</td><td>142.80 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (-9.40%)</td><td>0.16 (+4.41%)</td><td>0.18 (+14.20%)</td><td>0.12 (+8.12%)</td><td>0.03 <b>(-26.61%)</b></td><td>279.50 (-7.51%)</td><td>204.38 (-6.17%)</td><td>182.50 (-12.43%)</td><td>181.40 (+10.41%)</td><td>42.45 <b>(-23.81%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>302.20 (n/a)</td><td>217.82 (n/a)</td><td>208.40 (n/a)</td><td>164.30 (n/a)</td><td>55.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (+6.80%)</td><td>0.14 (+10.86%)</td><td>0.14 (+10.43%)</td><td>0.12 <b>(+20.92%)</b></td><td>0.01 (-18.27%)</td><td>173.00 (-17.30%)</td><td>147.88 (-10.59%)</td><td>142.30 (-9.42%)</td><td>131.20 (-6.42%)</td><td>16.44 <b>(-37.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>209.20 (n/a)</td><td>165.40 (n/a)</td><td>157.10 (n/a)</td><td>140.20 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (+19.70%)</td><td>0.13 (+16.90%)</td><td>0.12 (+10.56%)</td><td>0.10 (+7.73%)</td><td>0.02 <b>(+65.42%)</b></td><td>195.50 (-7.21%)</td><td>163.90 (-13.73%)</td><td>170.20 (-9.56%)</td><td>136.10 (-16.45%)</td><td>23.38 <b>(+27.35%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>189.98 (n/a)</td><td>188.20 (n/a)</td><td>162.90 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 <b>(+41.65%)</b></td><td>0.15 <b>(+26.86%)</b></td><td>0.14 <b>(+23.13%)</b></td><td>0.13 (+18.16%)</td><td>0.03 <b>(+135.49%)</b></td><td>160.20 (-15.37%)</td><td>138.92 (-19.81%)</td><td>144.70 (-18.75%)</td><td>104.00 <b>(-29.40%)</b></td><td>22.67 <b>(+42.27%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>173.24 (n/a)</td><td>178.10 (n/a)</td><td>147.30 (n/a)</td><td>15.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 <b>(+20.98%)</b></td><td>0.15 (+16.12%)</td><td>0.15 (+19.56%)</td><td>0.11 (-0.40%)</td><td>0.02 <b>(+61.31%)</b></td><td>180.10 (+0.45%)</td><td>140.26 (-12.80%)</td><td>138.90 (-16.38%)</td><td>112.60 (-17.33%)</td><td>24.82 <b>(+36.66%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>179.30 (n/a)</td><td>160.84 (n/a)</td><td>166.10 (n/a)</td><td>136.20 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 <b>(+36.40%)</b></td><td>0.12 (+3.26%)</td><td>0.11 (-6.90%)</td><td>0.09 (-8.30%)</td><td>0.04 <b>(+114.40%)</b></td><td>238.20 (+9.07%)</td><td>183.74 (+1.49%)</td><td>180.30 (+7.45%)</td><td>112.60 <b>(-26.69%)</b></td><td>48.00 <b>(+66.08%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>181.04 (n/a)</td><td>167.80 (n/a)</td><td>153.60 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 <b>(+25.26%)</b></td><td>0.13 (+10.84%)</td><td>0.14 <b>(+22.26%)</b></td><td>0.10 (-8.08%)</td><td>0.03 <b>(+139.46%)</b></td><td>205.50 (+8.79%)</td><td>160.66 (-6.77%)</td><td>148.30 (-18.20%)</td><td>119.50 <b>(-20.17%)</b></td><td>36.51 <b>(+113.32%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>172.32 (n/a)</td><td>181.30 (n/a)</td><td>149.70 (n/a)</td><td>17.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.20 <b>(+64.25%)</b></td><td>0.12 (+9.62%)</td><td>0.10 (-6.38%)</td><td>0.09 (-8.48%)</td><td>0.05 <b>(+308.47%)</b></td><td>229.80 (+9.22%)</td><td>189.08 (-1.09%)</td><td>209.40 (+6.78%)</td><td>101.30 <b>(-39.12%)</b></td><td>51.57 <b>(+158.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>191.16 (n/a)</td><td>196.10 (n/a)</td><td>166.40 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (-15.55%)</td><td>0.10 (-13.68%)</td><td>0.10 (-12.58%)</td><td>0.09 (-18.69%)</td><td>0.01 (-15.45%)</td><td>240.30 <b>(+22.98%)</b></td><td>198.50 (+15.92%)</td><td>197.60 (+14.35%)</td><td>165.30 (+18.41%)</td><td>27.21 <b>(+24.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>171.24 (n/a)</td><td>172.80 (n/a)</td><td>139.60 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (+2.88%)</td><td>0.16 (+5.38%)</td><td>0.17 (+6.56%)</td><td>0.12 (-6.23%)</td><td>0.03 (+19.63%)</td><td>211.50 (+6.66%)</td><td>156.68 (-4.12%)</td><td>147.60 (-6.17%)</td><td>127.40 (-2.82%)</td><td>33.64 <b>(+24.12%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.30 (n/a)</td><td>163.42 (n/a)</td><td>157.30 (n/a)</td><td>131.10 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (+3.15%)</td><td>0.15 (+4.43%)</td><td>0.14 (+9.45%)</td><td>0.12 (+2.26%)</td><td>0.03 (-9.39%)</td><td>200.60 (-2.19%)</td><td>163.62 (-4.84%)</td><td>170.70 (-8.62%)</td><td>130.90 (-3.04%)</td><td>27.38 (-13.47%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>171.94 (n/a)</td><td>186.80 (n/a)</td><td>135.00 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (-7.00%)</td><td>0.15 (-1.59%)</td><td>0.14 (-8.36%)</td><td>0.14 (+16.28%)</td><td>0.01 <b>(-39.69%)</b></td><td>176.80 (-13.97%)</td><td>165.04 (+0.40%)</td><td>173.80 (+9.10%)</td><td>146.20 (+7.50%)</td><td>14.07 <b>(-44.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>205.50 (n/a)</td><td>164.38 (n/a)</td><td>159.30 (n/a)</td><td>136.00 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.18 (+0.04%)</td><td>0.17 (-0.11%)</td><td>0.18 (+0.36%)</td><td>0.11 (-19.42%)</td><td>0.03 <b>(+51.91%)</b></td><td>226.30 <b>(+24.14%)</b></td><td>154.98 (+2.77%)</td><td>137.40 (-0.36%)</td><td>135.80 (-0.07%)</td><td>39.88 <b>(+93.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>150.80 (n/a)</td><td>137.90 (n/a)</td><td>135.90 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.19 (-2.96%)</td><td>0.15 (+0.88%)</td><td>0.15 (+1.31%)</td><td>0.12 (-3.00%)</td><td>0.03 (-9.65%)</td><td>211.40 (+3.07%)</td><td>170.54 (-1.39%)</td><td>167.00 (-1.30%)</td><td>126.40 (+3.02%)</td><td>31.64 (-5.73%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>172.94 (n/a)</td><td>169.20 (n/a)</td><td>122.70 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.16 (-17.50%)</td><td>0.15 (-9.65%)</td><td>0.14 (-16.31%)</td><td>0.13 (+7.07%)</td><td>0.01 <b>(-56.07%)</b></td><td>189.80 (-6.59%)</td><td>169.18 (+8.20%)</td><td>173.00 (+19.56%)</td><td>150.20 <b>(+21.23%)</b></td><td>15.14 <b>(-51.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>156.36 (n/a)</td><td>144.70 (n/a)</td><td>123.90 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.17 (+15.91%)</td><td>0.13 (-5.46%)</td><td>0.12 (-16.30%)</td><td>0.11 (-2.76%)</td><td>0.02 <b>(+94.20%)</b></td><td>214.60 (+2.83%)</td><td>194.86 (+7.30%)</td><td>206.50 (+19.50%)</td><td>145.20 (-13.73%)</td><td>28.20 <b>(+67.85%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>181.60 (n/a)</td><td>172.80 (n/a)</td><td>168.30 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (-7.97%)</td><td>0.13 (+1.01%)</td><td>0.13 (+9.48%)</td><td>0.10 (-7.53%)</td><td>0.02 (-16.52%)</td><td>243.00 (+8.14%)</td><td>198.32 (-1.24%)</td><td>189.80 (-8.66%)</td><td>170.70 (+8.66%)</td><td>27.08 (+2.58%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>224.70 (n/a)</td><td>200.80 (n/a)</td><td>207.80 (n/a)</td><td>157.10 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (+14.12%)</td><td>0.12 (+1.02%)</td><td>0.11 (-1.71%)</td><td>0.08 (-18.31%)</td><td>0.03 <b>(+114.38%)</b></td><td>230.20 <b>(+22.45%)</b></td><td>165.96 (+2.47%)</td><td>161.10 (+1.77%)</td><td>127.60 (-12.36%)</td><td>40.74 <b>(+131.44%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>161.96 (n/a)</td><td>158.30 (n/a)</td><td>145.60 (n/a)</td><td>17.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (+3.20%)</td><td>0.12 (+7.77%)</td><td>0.13 (+13.38%)</td><td>0.09 (-2.73%)</td><td>0.03 <b>(+38.38%)</b></td><td>212.40 (+2.81%)</td><td>156.98 (-5.32%)</td><td>147.40 (-11.79%)</td><td>123.80 (-3.13%)</td><td>38.00 <b>(+34.89%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>165.80 (n/a)</td><td>167.10 (n/a)</td><td>127.80 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (-2.09%)</td><td>0.13 (+3.32%)</td><td>0.13 (+8.61%)</td><td>0.09 (-9.02%)</td><td>0.02 <b>(+23.70%)</b></td><td>199.40 (+9.92%)</td><td>150.22 (-2.12%)</td><td>142.20 (-7.96%)</td><td>127.00 (+2.09%)</td><td>29.57 <b>(+40.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>181.40 (n/a)</td><td>153.48 (n/a)</td><td>154.50 (n/a)</td><td>124.40 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 (+16.94%)</td><td>0.12 (+17.33%)</td><td>0.12 (+16.02%)</td><td>0.11 <b>(+46.31%)</b></td><td>0.01 <b>(-38.77%)</b></td><td>161.90 <b>(-31.66%)</b></td><td>148.34 (-16.44%)</td><td>148.00 (-13.80%)</td><td>131.00 (-14.49%)</td><td>12.16 <b>(-64.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>177.52 (n/a)</td><td>171.70 (n/a)</td><td>153.20 (n/a)</td><td>34.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.13 <b>(-24.05%)</b></td><td>0.11 (+0.17%)</td><td>0.10 (+8.64%)</td><td>0.09 (+5.35%)</td><td>0.02 <b>(-52.64%)</b></td><td>208.80 (-5.09%)</td><td>175.32 (-4.13%)</td><td>181.90 (-7.95%)</td><td>147.30 <b>(+31.64%)</b></td><td>25.53 <b>(-38.99%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>220.00 (n/a)</td><td>182.88 (n/a)</td><td>197.60 (n/a)</td><td>111.90 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.15 (-9.58%)</td><td>0.10 (-13.77%)</td><td>0.11 (-2.92%)</td><td>0.06 <b>(-43.51%)</b></td><td>0.03 <b>(+31.51%)</b></td><td>326.80 <b>(+77.03%)</b></td><td>197.50 <b>(+24.73%)</b></td><td>168.70 (+2.99%)</td><td>123.50 (+10.56%)</td><td>77.68 <b>(+182.75%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>158.34 (n/a)</td><td>163.80 (n/a)</td><td>111.70 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.14 <b>(+44.16%)</b></td><td>0.10 (+4.50%)</td><td>0.09 (+3.49%)</td><td>0.06 <b>(-34.08%)</b></td><td>0.03 <b>(+362.48%)</b></td><td>325.60 <b>(+51.72%)</b></td><td>208.44 (+4.31%)</td><td>200.80 (-3.37%)</td><td>127.60 <b>(-30.61%)</b></td><td>72.80 <b>(+401.72%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>199.82 (n/a)</td><td>207.80 (n/a)</td><td>183.90 (n/a)</td><td>14.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.11 <b>(-33.52%)</b></td><td>0.09 (-14.57%)</td><td>0.09 (-5.80%)</td><td>0.08 <b>(+29.92%)</b></td><td>0.01 <b>(-74.16%)</b></td><td>223.30 <b>(-23.03%)</b></td><td>204.88 (+7.27%)</td><td>210.00 (+6.17%)</td><td>172.50 <b>(+50.39%)</b></td><td>19.45 <b>(-70.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>290.10 (n/a)</td><td>191.00 (n/a)</td><td>197.80 (n/a)</td><td>114.70 (n/a)</td><td>65.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.73 (-5.95%)</td><td>0.50 (-14.04%)</td><td>0.44 (-19.80%)</td><td>0.39 (-7.94%)</td><td>0.14 (+0.93%)</td><td>250.20 (+8.64%)</td><td>208.66 (+17.16%)</td><td>222.00 <b>(+24.65%)</b></td><td>134.50 (+6.32%)</td><td>46.62 (+15.21%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.78 (n/a)</td><td>0.58 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.14 (n/a)</td><td>230.30 (n/a)</td><td>178.10 (n/a)</td><td>178.10 (n/a)</td><td>126.50 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.65 <b>(-20.20%)</b></td><td>0.56 (-17.31%)</td><td>0.58 (-11.28%)</td><td>0.47 (-4.03%)</td><td>0.09 <b>(-38.46%)</b></td><td>211.30 (+4.19%)</td><td>178.36 (+18.76%)</td><td>168.80 (+12.68%)</td><td>150.10 <b>(+25.29%)</b></td><td>28.45 (-16.35%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.82 (n/a)</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>202.80 (n/a)</td><td>150.18 (n/a)</td><td>149.80 (n/a)</td><td>119.80 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.77 (-17.73%)</td><td>0.60 (-2.06%)</td><td>0.52 (-6.98%)</td><td>0.50 <b>(+60.94%)</b></td><td>0.12 <b>(-46.32%)</b></td><td>194.80 <b>(-37.86%)</b></td><td>170.16 (-7.28%)</td><td>188.90 (+7.51%)</td><td>126.90 <b>(+21.55%)</b></td><td>31.63 <b>(-59.76%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.94 (n/a)</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>313.50 (n/a)</td><td>183.52 (n/a)</td><td>175.70 (n/a)</td><td>104.40 (n/a)</td><td>78.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.65 (+17.25%)</td><td>0.55 (+8.68%)</td><td>0.57 (+13.22%)</td><td>0.37 <b>(-20.51%)</b></td><td>0.11 <b>(+229.38%)</b></td><td>263.90 <b>(+25.79%)</b></td><td>186.94 (-4.40%)</td><td>173.90 (-11.68%)</td><td>151.30 (-14.71%)</td><td>46.40 <b>(+251.79%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.03 (n/a)</td><td>209.80 (n/a)</td><td>195.54 (n/a)</td><td>196.90 (n/a)</td><td>177.40 (n/a)</td><td>13.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.49 (-4.16%)</td><td>0.41 (-9.95%)</td><td>0.43 (-14.74%)</td><td>0.32 (-10.88%)</td><td>0.06 (-10.76%)</td><td>230.40 (+12.17%)</td><td>182.34 (+10.97%)</td><td>173.30 (+17.25%)</td><td>150.70 (+4.36%)</td><td>29.64 (+8.96%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>205.40 (n/a)</td><td>164.32 (n/a)</td><td>147.80 (n/a)</td><td>144.40 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.56 (-7.19%)</td><td>0.50 (-6.45%)</td><td>0.56 (-0.45%)</td><td>0.39 (-13.28%)</td><td>0.08 (+11.77%)</td><td>190.20 (+15.27%)</td><td>150.18 (+7.73%)</td><td>132.00 (+0.46%)</td><td>131.60 (+7.78%)</td><td>26.60 <b>(+35.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.60 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>165.00 (n/a)</td><td>139.40 (n/a)</td><td>131.40 (n/a)</td><td>122.10 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.53 (-13.13%)</td><td>0.44 (-11.99%)</td><td>0.44 (-7.55%)</td><td>0.32 <b>(-20.07%)</b></td><td>0.09 (-8.66%)</td><td>229.90 <b>(+25.08%)</b></td><td>173.90 (+14.23%)</td><td>167.80 (+8.12%)</td><td>137.90 (+15.11%)</td><td>39.29 <b>(+28.45%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.62 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.10 (n/a)</td><td>183.80 (n/a)</td><td>152.24 (n/a)</td><td>155.20 (n/a)</td><td>119.80 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.44 <b>(-22.64%)</b></td><td>0.39 (-11.53%)</td><td>0.38 (-9.12%)</td><td>0.33 (-6.28%)</td><td>0.05 <b>(-43.47%)</b></td><td>226.20 (+6.70%)</td><td>192.28 (+11.40%)</td><td>191.60 (+9.99%)</td><td>167.40 <b>(+29.27%)</b></td><td>23.81 <b>(-21.24%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>212.00 (n/a)</td><td>172.60 (n/a)</td><td>174.20 (n/a)</td><td>129.50 (n/a)</td><td>30.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.32 (+11.71%)</td><td>0.24 (+1.51%)</td><td>0.25 (-0.52%)</td><td>0.16 (-11.84%)</td><td>0.06 <b>(+24.60%)</b></td><td>227.20 (+13.43%)</td><td>159.46 (+0.30%)</td><td>149.20 (+0.54%)</td><td>115.30 (-10.48%)</td><td>41.69 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>200.30 (n/a)</td><td>158.98 (n/a)</td><td>148.40 (n/a)</td><td>128.80 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 (+18.70%)</td><td>0.24 (+7.24%)</td><td>0.23 (+15.23%)</td><td>0.17 (-9.78%)</td><td>0.07 <b>(+57.05%)</b></td><td>220.20 (+10.82%)</td><td>162.30 (-3.62%)</td><td>158.50 (-13.25%)</td><td>110.90 (-15.73%)</td><td>43.74 <b>(+47.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>168.40 (n/a)</td><td>182.70 (n/a)</td><td>131.60 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.33 <b>(+42.95%)</b></td><td>0.27 <b>(+27.62%)</b></td><td>0.26 <b>(+23.44%)</b></td><td>0.22 (+15.32%)</td><td>0.04 <b>(+135.53%)</b></td><td>167.60 (-13.25%)</td><td>138.60 <b>(-20.64%)</b></td><td>141.10 (-18.95%)</td><td>111.00 <b>(-30.06%)</b></td><td>20.66 <b>(+42.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>193.20 (n/a)</td><td>174.64 (n/a)</td><td>174.10 (n/a)</td><td>158.70 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-8.60%)</td><td>0.21 (-5.88%)</td><td>0.19 (-5.57%)</td><td>0.19 (+1.39%)</td><td>0.03 <b>(-29.78%)</b></td><td>196.70 (-1.35%)</td><td>180.74 (+5.07%)</td><td>189.20 (+5.94%)</td><td>145.00 (+9.43%)</td><td>21.10 <b>(-25.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>199.40 (n/a)</td><td>172.02 (n/a)</td><td>178.60 (n/a)</td><td>132.50 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 <b>(+22.84%)</b></td><td>0.21 (+3.14%)</td><td>0.20 (-8.34%)</td><td>0.16 (+3.54%)</td><td>0.05 <b>(+48.90%)</b></td><td>228.20 (-3.43%)</td><td>178.94 (-1.70%)</td><td>181.80 (+9.12%)</td><td>131.30 (-18.60%)</td><td>36.19 (+14.90%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>236.30 (n/a)</td><td>182.04 (n/a)</td><td>166.60 (n/a)</td><td>161.30 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.22 (-5.90%)</td><td>0.21 (-1.73%)</td><td>0.22 (+3.51%)</td><td>0.18 (-9.48%)</td><td>0.02 (+8.01%)</td><td>206.10 (+10.51%)</td><td>175.06 (+1.96%)</td><td>166.90 (-3.41%)</td><td>163.90 (+6.29%)</td><td>17.66 <b>(+27.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>186.50 (n/a)</td><td>171.70 (n/a)</td><td>172.80 (n/a)</td><td>154.20 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 <b>(-29.37%)</b></td><td>0.19 (-12.62%)</td><td>0.18 (-17.04%)</td><td>0.16 <b>(+42.58%)</b></td><td>0.02 <b>(-69.85%)</b></td><td>228.50 <b>(-29.86%)</b></td><td>199.40 (+3.05%)</td><td>205.70 <b>(+20.50%)</b></td><td>174.50 <b>(+41.64%)</b></td><td>23.30 <b>(-71.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>325.80 (n/a)</td><td>193.50 (n/a)</td><td>170.70 (n/a)</td><td>123.20 (n/a)</td><td>80.82 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (-2.78%)</td><td>0.21 (-0.35%)</td><td>0.20 (-6.65%)</td><td>0.17 (+16.45%)</td><td>0.04 <b>(-20.13%)</b></td><td>212.80 (-14.12%)</td><td>180.52 (-1.39%)</td><td>184.00 (+7.16%)</td><td>138.60 (+2.90%)</td><td>29.16 <b>(-30.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>247.80 (n/a)</td><td>183.06 (n/a)</td><td>171.70 (n/a)</td><td>134.70 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.35 (+12.63%)</td><td>0.30 (+19.43%)</td><td>0.30 <b>(+27.65%)</b></td><td>0.23 (+8.85%)</td><td>0.04 (+2.42%)</td><td>177.20 (-8.14%)</td><td>139.48 (-16.52%)</td><td>136.00 <b>(-21.66%)</b></td><td>116.10 (-11.17%)</td><td>22.79 (-15.11%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>192.90 (n/a)</td><td>167.08 (n/a)</td><td>173.60 (n/a)</td><td>130.70 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 (+1.86%)</td><td>0.29 <b>(+24.66%)</b></td><td>0.30 <b>(+23.89%)</b></td><td>0.26 <b>(+57.92%)</b></td><td>0.02 <b>(-56.00%)</b></td><td>156.00 <b>(-36.66%)</b></td><td>141.52 <b>(-22.82%)</b></td><td>135.30 (-19.27%)</td><td>131.70 (-1.79%)</td><td>11.81 <b>(-73.04%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>246.30 (n/a)</td><td>183.36 (n/a)</td><td>167.60 (n/a)</td><td>134.10 (n/a)</td><td>43.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.28 (+6.53%)</td><td>0.24 (+5.05%)</td><td>0.24 (+4.16%)</td><td>0.18 (-13.44%)</td><td>0.04 <b>(+91.27%)</b></td><td>222.60 (+15.52%)</td><td>171.46 (-3.08%)</td><td>169.60 (-3.96%)</td><td>144.00 (-6.13%)</td><td>31.39 <b>(+110.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>176.90 (n/a)</td><td>176.60 (n/a)</td><td>153.40 (n/a)</td><td>14.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (-17.57%)</td><td>0.24 (-12.46%)</td><td>0.23 (-17.96%)</td><td>0.21 (-3.78%)</td><td>0.04 <b>(-20.25%)</b></td><td>196.30 (+3.97%)</td><td>171.44 (+13.78%)</td><td>181.80 <b>(+21.93%)</b></td><td>137.60 <b>(+21.34%)</b></td><td>27.51 (+2.92%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>188.80 (n/a)</td><td>150.68 (n/a)</td><td>149.10 (n/a)</td><td>113.40 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.29 (+4.15%)</td><td>0.23 (-2.23%)</td><td>0.24 (+4.71%)</td><td>0.18 (-11.65%)</td><td>0.04 <b>(+55.03%)</b></td><td>225.10 (+13.17%)</td><td>180.94 (+3.99%)</td><td>169.70 (-4.50%)</td><td>141.30 (-4.01%)</td><td>33.28 <b>(+71.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>198.90 (n/a)</td><td>174.00 (n/a)</td><td>177.70 (n/a)</td><td>147.20 (n/a)</td><td>19.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.35 <b>(+30.86%)</b></td><td>0.26 (+6.73%)</td><td>0.25 (+0.13%)</td><td>0.18 (-12.01%)</td><td>0.07 <b>(+134.80%)</b></td><td>231.60 (+13.64%)</td><td>163.82 (-2.35%)</td><td>164.40 (-0.12%)</td><td>115.70 <b>(-23.58%)</b></td><td>43.47 <b>(+104.30%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>203.80 (n/a)</td><td>167.76 (n/a)</td><td>164.60 (n/a)</td><td>151.40 (n/a)</td><td>21.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 <b>(+59.41%)</b></td><td>0.24 (+10.28%)</td><td>0.22 (+2.40%)</td><td>0.15 (-19.40%)</td><td>0.09 <b>(+329.88%)</b></td><td>270.70 <b>(+24.06%)</b></td><td>188.74 (-1.14%)</td><td>183.80 (-2.34%)</td><td>107.40 <b>(-37.23%)</b></td><td>60.23 <b>(+223.96%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>190.92 (n/a)</td><td>188.20 (n/a)</td><td>171.10 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.30 (+12.57%)</td><td>0.24 <b>(+24.63%)</b></td><td>0.25 <b>(+48.51%)</b></td><td>0.19 (+13.94%)</td><td>0.05 (+11.93%)</td><td>218.60 (-12.21%)</td><td>178.46 (-19.63%)</td><td>161.80 <b>(-32.67%)</b></td><td>135.30 (-11.16%)</td><td>37.39 (-6.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>249.00 (n/a)</td><td>222.06 (n/a)</td><td>240.30 (n/a)</td><td>152.30 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (+0.98%)</td><td>0.22 (+10.42%)</td><td>0.21 (+15.66%)</td><td>0.20 (+18.30%)</td><td>0.03 <b>(-22.47%)</b></td><td>178.40 (-15.49%)</td><td>157.82 (-10.98%)</td><td>165.60 (-13.52%)</td><td>130.50 (-0.91%)</td><td>22.94 <b>(-35.12%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>177.28 (n/a)</td><td>191.50 (n/a)</td><td>131.70 (n/a)</td><td>35.36 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.26 (-1.41%)</td><td>0.22 (+13.72%)</td><td>0.21 (+14.03%)</td><td>0.18 (+17.12%)</td><td>0.03 <b>(-23.37%)</b></td><td>192.00 (-14.63%)</td><td>162.52 (-13.30%)</td><td>169.60 (-12.31%)</td><td>135.00 (+1.43%)</td><td>22.93 <b>(-31.32%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.90 (n/a)</td><td>187.46 (n/a)</td><td>193.40 (n/a)</td><td>133.10 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.23 (-16.20%)</td><td>0.19 (-9.70%)</td><td>0.18 (-12.98%)</td><td>0.14 (-7.33%)</td><td>0.03 <b>(-23.82%)</b></td><td>244.80 (+7.94%)</td><td>189.72 (+9.77%)</td><td>189.90 (+14.95%)</td><td>152.50 (+19.33%)</td><td>36.01 (-2.43%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>226.80 (n/a)</td><td>172.84 (n/a)</td><td>165.20 (n/a)</td><td>127.80 (n/a)</td><td>36.91 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 <b>(+34.63%)</b></td><td>0.21 (+15.94%)</td><td>0.19 (-1.21%)</td><td>0.18 <b>(+33.17%)</b></td><td>0.04 <b>(+21.93%)</b></td><td>196.30 <b>(-24.90%)</b></td><td>172.02 (-14.14%)</td><td>179.60 (+1.24%)</td><td>129.90 <b>(-25.73%)</b></td><td>25.41 <b>(-32.72%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>261.40 (n/a)</td><td>200.34 (n/a)</td><td>177.40 (n/a)</td><td>174.90 (n/a)</td><td>37.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.24 (-6.36%)</td><td>0.21 (+0.77%)</td><td>0.21 (+2.92%)</td><td>0.17 (+10.77%)</td><td>0.03 <b>(-20.94%)</b></td><td>199.10 (-9.71%)</td><td>169.18 (-1.80%)</td><td>166.40 (-2.86%)</td><td>144.70 (+6.79%)</td><td>24.11 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>220.50 (n/a)</td><td>172.28 (n/a)</td><td>171.30 (n/a)</td><td>135.50 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.31 <b>(+31.51%)</b></td><td>0.21 (+15.41%)</td><td>0.19 (+12.44%)</td><td>0.15 (+3.33%)</td><td>0.06 <b>(+62.36%)</b></td><td>224.70 (-3.23%)</td><td>171.66 (-11.09%)</td><td>180.60 (-11.08%)</td><td>111.00 <b>(-23.97%)</b></td><td>42.64 (+16.29%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>232.20 (n/a)</td><td>193.08 (n/a)</td><td>203.10 (n/a)</td><td>146.00 (n/a)</td><td>36.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 (-8.03%)</td><td>0.20 (+4.06%)</td><td>0.21 (+7.80%)</td><td>0.16 (+11.84%)</td><td>0.04 <b>(-27.95%)</b></td><td>220.80 (-10.57%)</td><td>175.92 (-6.00%)</td><td>168.90 (-7.20%)</td><td>136.70 (+8.75%)</td><td>31.49 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>246.90 (n/a)</td><td>187.14 (n/a)</td><td>182.00 (n/a)</td><td>125.70 (n/a)</td><td>43.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.25 <b>(+22.77%)</b></td><td>0.21 (+13.30%)</td><td>0.24 <b>(+30.58%)</b></td><td>0.14 (-18.20%)</td><td>0.05 <b>(+272.47%)</b></td><td>256.40 <b>(+22.21%)</b></td><td>178.04 (-6.28%)</td><td>146.20 <b>(-23.42%)</b></td><td>137.20 (-18.58%)</td><td>53.69 <b>(+261.89%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>189.98 (n/a)</td><td>190.90 (n/a)</td><td>168.50 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.93 (-0.34%)</td><td>0.72 (-5.91%)</td><td>0.68 (-5.30%)</td><td>0.55 (-13.62%)</td><td>0.14 <b>(+24.66%)</b></td><td>236.20 (+15.78%)</td><td>187.10 (+7.69%)</td><td>191.90 (+5.61%)</td><td>140.70 (+0.36%)</td><td>35.49 <b>(+44.95%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.93 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.64 (n/a)</td><td>0.11 (n/a)</td><td>204.00 (n/a)</td><td>173.74 (n/a)</td><td>181.70 (n/a)</td><td>140.20 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.91 (-10.75%)</td><td>0.68 <b>(-26.04%)</b></td><td>0.64 <b>(-35.69%)</b></td><td>0.53 <b>(-27.78%)</b></td><td>0.14 (+17.84%)</td><td>245.10 <b>(+38.47%)</b></td><td>198.26 <b>(+37.53%)</b></td><td>206.00 <b>(+55.47%)</b></td><td>144.00 (+12.06%)</td><td>38.07 <b>(+81.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.02 (n/a)</td><td>0.92 (n/a)</td><td>0.99 (n/a)</td><td>0.74 (n/a)</td><td>0.12 (n/a)</td><td>177.00 (n/a)</td><td>144.16 (n/a)</td><td>132.50 (n/a)</td><td>128.50 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.97 (-13.16%)</td><td>0.63 <b>(-34.44%)</b></td><td>0.58 <b>(-35.44%)</b></td><td>0.49 <b>(-44.20%)</b></td><td>0.19 <b>(+74.64%)</b></td><td>266.30 <b>(+79.21%)</b></td><td>218.74 <b>(+59.76%)</b></td><td>227.30 <b>(+54.94%)</b></td><td>135.20 (+15.16%)</td><td>49.72 <b>(+236.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.12 (n/a)</td><td>0.97 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.11 (n/a)</td><td>148.60 (n/a)</td><td>136.92 (n/a)</td><td>146.70 (n/a)</td><td>117.40 (n/a)</td><td>14.77 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.00 (-2.17%)</td><td>0.00 (-1.41%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-22.38%)</b></td><td>1059.11 (+1.81%)</td><td>982.19 (+1.92%)</td><td>979.38 (+0.70%)</td><td>919.40 (+2.16%)</td><td>50.93 (-13.96%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1040.26 (n/a)</td><td>963.64 (n/a)</td><td>972.55 (n/a)</td><td>899.95 (n/a)</td><td>59.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.01 (+0.00%)</td><td>0.01 (-0.50%)</td><td>0.01 (+0.00%)</td><td>0.01 (+4.11%)</td><td>0.00 <b>(-34.84%)</b></td><td>1071.42 (-5.06%)</td><td>1025.12 (+0.11%)</td><td>1032.27 (-0.34%)</td><td>959.30 (-0.05%)</td><td>40.89 <b>(-41.39%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1128.58 (n/a)</td><td>1023.97 (n/a)</td><td>1035.75 (n/a)</td><td>959.74 (n/a)</td><td>69.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.96 (-2.78%)</td><td>0.95 (-1.05%)</td><td>0.95 (-0.24%)</td><td>0.95 (+0.62%)</td><td>0.01 <b>(-75.87%)</b></td><td>2212.14 (-0.61%)</td><td>2203.45 (+1.02%)</td><td>2209.40 (+0.24%)</td><td>2183.86 (+2.86%)</td><td>12.08 <b>(-75.36%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2225.80 (n/a)</td><td>2181.24 (n/a)</td><td>2204.07 (n/a)</td><td>2123.04 (n/a)</td><td>49.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.41 (+1.55%)</td><td>0.39 (+0.76%)</td><td>0.40 (+0.96%)</td><td>0.37 (-1.72%)</td><td>0.01 <b>(+48.99%)</b></td><td>1410.04 (+1.75%)</td><td>1330.07 (-0.70%)</td><td>1315.61 (-0.97%)</td><td>1291.24 (-1.54%)</td><td>46.11 <b>(+50.94%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1385.74 (n/a)</td><td>1339.48 (n/a)</td><td>1328.43 (n/a)</td><td>1311.40 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.27 (-0.30%)</td><td>0.26 (-3.45%)</td><td>0.26 (-2.62%)</td><td>0.25 (-6.61%)</td><td>0.01 <b>(+493.38%)</b></td><td>2133.27 (+7.08%)</td><td>2044.77 (+3.71%)</td><td>2017.79 (+2.69%)</td><td>1967.11 (+0.31%)</td><td>82.60 <b>(+536.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.00 (n/a)</td><td>1992.18 (n/a)</td><td>1971.62 (n/a)</td><td>1964.90 (n/a)</td><td>1961.11 (n/a)</td><td>12.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.38 (+0.32%)</td><td>0.37 (-1.00%)</td><td>0.36 (-1.09%)</td><td>0.36 (-0.08%)</td><td>0.01 (+3.76%)</td><td>1451.21 (+0.09%)</td><td>1432.58 (+1.01%)</td><td>1442.70 (+1.11%)</td><td>1377.73 (-0.33%)</td><td>30.97 (+3.75%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1449.94 (n/a)</td><td>1418.27 (n/a)</td><td>1426.91 (n/a)</td><td>1382.36 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>6.01 (-14.82%)</td><td>4.70 (-6.51%)</td><td>4.55 (-5.60%)</td><td>4.12 (+15.93%)</td><td>0.77 <b>(-39.49%)</b></td><td>254.60 (-13.75%)</td><td>227.08 (+3.91%)</td><td>230.30 (+5.93%)</td><td>174.60 (+17.42%)</td><td>32.01 <b>(-38.47%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>7.05 (n/a)</td><td>5.03 (n/a)</td><td>4.82 (n/a)</td><td>3.55 (n/a)</td><td>1.27 (n/a)</td><td>295.20 (n/a)</td><td>218.54 (n/a)</td><td>217.40 (n/a)</td><td>148.70 (n/a)</td><td>52.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.53 (-8.03%)</td><td>4.68 (-7.81%)</td><td>4.91 (-4.47%)</td><td>3.95 (-1.09%)</td><td>0.69 (-10.21%)</td><td>265.60 (+1.10%)</td><td>228.02 (+8.28%)</td><td>213.30 (+4.66%)</td><td>189.70 (+8.71%)</td><td>34.25 (+0.88%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.01 (n/a)</td><td>5.08 (n/a)</td><td>5.14 (n/a)</td><td>3.99 (n/a)</td><td>0.77 (n/a)</td><td>262.70 (n/a)</td><td>210.58 (n/a)</td><td>203.80 (n/a)</td><td>174.50 (n/a)</td><td>33.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.23 (-7.22%)</td><td>4.74 (-7.39%)</td><td>4.64 (-10.89%)</td><td>4.36 (-1.01%)</td><td>0.38 <b>(-29.44%)</b></td><td>240.40 (+1.01%)</td><td>222.52 (+7.55%)</td><td>225.90 (+12.22%)</td><td>200.60 (+7.79%)</td><td>17.45 <b>(-22.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>5.63 (n/a)</td><td>5.11 (n/a)</td><td>5.21 (n/a)</td><td>4.41 (n/a)</td><td>0.54 (n/a)</td><td>238.00 (n/a)</td><td>206.90 (n/a)</td><td>201.30 (n/a)</td><td>186.10 (n/a)</td><td>22.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.11 (-16.10%)</td><td>4.80 (-7.94%)</td><td>4.82 (-10.00%)</td><td>4.43 (+7.15%)</td><td>0.30 <b>(-56.98%)</b></td><td>236.60 (-6.70%)</td><td>218.94 (+7.25%)</td><td>217.70 (+11.07%)</td><td>205.30 (+19.15%)</td><td>13.88 <b>(-53.74%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.09 (n/a)</td><td>5.22 (n/a)</td><td>5.35 (n/a)</td><td>4.14 (n/a)</td><td>0.70 (n/a)</td><td>253.60 (n/a)</td><td>204.14 (n/a)</td><td>196.00 (n/a)</td><td>172.30 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.00 (-11.62%)</td><td>7.67 (-1.51%)</td><td>7.67 (-0.47%)</td><td>7.15 (+11.69%)</td><td>0.33 <b>(-68.84%)</b></td><td>293.40 (-10.47%)</td><td>273.98 (+0.15%)</td><td>273.50 (+0.48%)</td><td>262.00 (+13.13%)</td><td>12.16 <b>(-68.19%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.06 (n/a)</td><td>7.78 (n/a)</td><td>7.71 (n/a)</td><td>6.40 (n/a)</td><td>1.06 (n/a)</td><td>327.70 (n/a)</td><td>273.56 (n/a)</td><td>272.20 (n/a)</td><td>231.60 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.25 (+0.32%)</td><td>7.99 (-2.14%)</td><td>8.37 (+6.03%)</td><td>6.49 (-11.14%)</td><td>1.05 <b>(+34.28%)</b></td><td>323.00 (+12.54%)</td><td>266.36 (+2.97%)</td><td>250.40 (-5.69%)</td><td>226.70 (-0.31%)</td><td>37.25 <b>(+53.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.22 (n/a)</td><td>8.17 (n/a)</td><td>7.90 (n/a)</td><td>7.31 (n/a)</td><td>0.79 (n/a)</td><td>287.00 (n/a)</td><td>258.68 (n/a)</td><td>265.50 (n/a)</td><td>227.40 (n/a)</td><td>24.30 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.20 (+0.33%)</td><td>7.99 (-2.94%)</td><td>7.85 (-1.56%)</td><td>6.31 (-16.77%)</td><td>1.11 <b>(+70.48%)</b></td><td>332.60 <b>(+20.16%)</b></td><td>266.88 (+4.28%)</td><td>267.30 (+1.56%)</td><td>228.00 (-0.31%)</td><td>40.63 <b>(+106.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.17 (n/a)</td><td>8.23 (n/a)</td><td>7.97 (n/a)</td><td>7.58 (n/a)</td><td>0.65 (n/a)</td><td>276.80 (n/a)</td><td>255.92 (n/a)</td><td>263.20 (n/a)</td><td>228.70 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.36 (-6.18%)</td><td>8.17 (-0.60%)</td><td>8.14 (-1.28%)</td><td>8.02 (+7.09%)</td><td>0.13 <b>(-77.03%)</b></td><td>261.60 (-6.60%)</td><td>256.84 (+0.25%)</td><td>257.50 (+1.30%)</td><td>250.80 (+6.59%)</td><td>4.06 <b>(-77.08%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.91 (n/a)</td><td>8.22 (n/a)</td><td>8.25 (n/a)</td><td>7.49 (n/a)</td><td>0.56 (n/a)</td><td>280.10 (n/a)</td><td>256.20 (n/a)</td><td>254.20 (n/a)</td><td>235.30 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.43 (-3.45%)</td><td>8.12 (+1.61%)</td><td>7.87 (-0.50%)</td><td>7.49 (+6.16%)</td><td>0.81 <b>(-24.60%)</b></td><td>280.10 (-5.82%)</td><td>260.08 (-2.14%)</td><td>266.50 (+0.49%)</td><td>222.40 (+3.59%)</td><td>24.01 <b>(-25.49%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>9.77 (n/a)</td><td>7.99 (n/a)</td><td>7.91 (n/a)</td><td>7.05 (n/a)</td><td>1.07 (n/a)</td><td>297.40 (n/a)</td><td>265.78 (n/a)</td><td>265.20 (n/a)</td><td>214.70 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>9.30 (-12.71%)</td><td>8.47 (-7.75%)</td><td>8.40 (-2.18%)</td><td>7.90 (-0.13%)</td><td>0.55 <b>(-57.42%)</b></td><td>265.50 (+0.11%)</td><td>248.50 (+7.08%)</td><td>249.70 (+2.25%)</td><td>225.40 (+14.59%)</td><td>15.78 <b>(-50.38%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>10.66 (n/a)</td><td>9.18 (n/a)</td><td>8.59 (n/a)</td><td>7.91 (n/a)</td><td>1.30 (n/a)</td><td>265.20 (n/a)</td><td>232.06 (n/a)</td><td>244.20 (n/a)</td><td>196.70 (n/a)</td><td>31.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.02 (-3.90%)</td><td>11.15 (-2.50%)</td><td>11.00 (+0.11%)</td><td>10.63 (+0.86%)</td><td>0.52 <b>(-45.29%)</b></td><td>394.70 (-0.83%)</td><td>376.96 (+2.17%)</td><td>381.40 (-0.13%)</td><td>348.80 (+4.06%)</td><td>17.00 <b>(-43.60%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>12.51 (n/a)</td><td>11.43 (n/a)</td><td>10.98 (n/a)</td><td>10.54 (n/a)</td><td>0.96 (n/a)</td><td>398.00 (n/a)</td><td>368.94 (n/a)</td><td>381.90 (n/a)</td><td>335.20 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.32 (-5.45%)</td><td>11.36 (-3.96%)</td><td>11.20 (-9.72%)</td><td>10.68 (+7.22%)</td><td>0.63 <b>(-52.97%)</b></td><td>392.70 (-6.72%)</td><td>369.94 (+3.25%)</td><td>374.40 (+10.77%)</td><td>340.30 (+5.75%)</td><td>19.92 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.03 (n/a)</td><td>11.83 (n/a)</td><td>12.41 (n/a)</td><td>9.96 (n/a)</td><td>1.33 (n/a)</td><td>421.00 (n/a)</td><td>358.30 (n/a)</td><td>338.00 (n/a)</td><td>321.80 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.20 (-0.57%)</td><td>11.50 (+1.95%)</td><td>11.49 (+4.03%)</td><td>10.93 (+5.05%)</td><td>0.46 <b>(-40.01%)</b></td><td>383.70 (-4.81%)</td><td>365.16 (-2.14%)</td><td>365.10 (-3.87%)</td><td>343.80 (+0.59%)</td><td>14.49 <b>(-42.51%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>12.27 (n/a)</td><td>11.28 (n/a)</td><td>11.04 (n/a)</td><td>10.41 (n/a)</td><td>0.77 (n/a)</td><td>403.10 (n/a)</td><td>373.16 (n/a)</td><td>379.80 (n/a)</td><td>341.80 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.86 (-8.10%)</td><td>12.20 (-3.11%)</td><td>12.69 (+4.04%)</td><td>10.69 (-7.84%)</td><td>0.93 (-1.95%)</td><td>392.40 (+8.52%)</td><td>345.58 (+3.28%)</td><td>330.50 (-3.87%)</td><td>326.20 (+8.81%)</td><td>28.35 (+15.91%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>13.99 (n/a)</td><td>12.59 (n/a)</td><td>12.20 (n/a)</td><td>11.60 (n/a)</td><td>0.95 (n/a)</td><td>361.60 (n/a)</td><td>334.62 (n/a)</td><td>343.80 (n/a)</td><td>299.80 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.52 (+0.58%)</td><td>12.54 (-0.65%)</td><td>12.03 (-10.17%)</td><td>11.53 (+12.16%)</td><td>1.27 <b>(-26.24%)</b></td><td>363.80 (-10.86%)</td><td>337.12 (-0.18%)</td><td>348.70 (+11.30%)</td><td>288.80 (-0.59%)</td><td>32.05 <b>(-34.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.44 (n/a)</td><td>12.62 (n/a)</td><td>13.39 (n/a)</td><td>10.28 (n/a)</td><td>1.72 (n/a)</td><td>408.10 (n/a)</td><td>337.72 (n/a)</td><td>313.30 (n/a)</td><td>290.50 (n/a)</td><td>48.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.85 (+3.08%)</td><td>13.41 (-0.54%)</td><td>14.09 (+2.36%)</td><td>11.72 (-5.34%)</td><td>1.35 <b>(+70.37%)</b></td><td>357.90 (+5.64%)</td><td>315.40 (+1.11%)</td><td>297.60 (-2.30%)</td><td>282.50 (-2.99%)</td><td>32.88 <b>(+75.25%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>14.40 (n/a)</td><td>13.48 (n/a)</td><td>13.77 (n/a)</td><td>12.38 (n/a)</td><td>0.79 (n/a)</td><td>338.80 (n/a)</td><td>311.94 (n/a)</td><td>304.60 (n/a)</td><td>291.20 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>14.19 (-11.68%)</td><td>12.90 (-9.55%)</td><td>12.71 (-11.83%)</td><td>12.27 (-0.94%)</td><td>0.79 <b>(-52.69%)</b></td><td>341.80 (+0.97%)</td><td>326.02 (+9.65%)</td><td>330.10 (+13.40%)</td><td>295.60 (+13.26%)</td><td>19.07 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>16.07 (n/a)</td><td>14.27 (n/a)</td><td>14.41 (n/a)</td><td>12.39 (n/a)</td><td>1.67 (n/a)</td><td>338.50 (n/a)</td><td>297.32 (n/a)</td><td>291.10 (n/a)</td><td>261.00 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>12.78 (-16.79%)</td><td>11.67 (-13.11%)</td><td>12.20 (-5.50%)</td><td>10.01 (-18.34%)</td><td>1.18 (-8.41%)</td><td>419.00 <b>(+22.44%)</b></td><td>362.66 (+15.27%)</td><td>343.90 (+5.82%)</td><td>328.20 <b>(+20.18%)</b></td><td>38.69 <b>(+34.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>15.36 (n/a)</td><td>13.43 (n/a)</td><td>12.91 (n/a)</td><td>12.26 (n/a)</td><td>1.29 (n/a)</td><td>342.20 (n/a)</td><td>314.62 (n/a)</td><td>325.00 (n/a)</td><td>273.10 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.41 (+1.77%)</td><td>2.75 (+2.51%)</td><td>2.87 (+5.26%)</td><td>1.95 <b>(+29.29%)</b></td><td>0.54 <b>(-25.58%)</b></td><td>269.10 <b>(-22.65%)</b></td><td>197.48 (-6.88%)</td><td>182.70 (-4.99%)</td><td>153.90 (-1.72%)</td><td>44.06 <b>(-43.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.35 (n/a)</td><td>2.68 (n/a)</td><td>2.73 (n/a)</td><td>1.51 (n/a)</td><td>0.73 (n/a)</td><td>347.90 (n/a)</td><td>212.06 (n/a)</td><td>192.30 (n/a)</td><td>156.60 (n/a)</td><td>78.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>5.27 (-15.72%)</td><td>4.93 (-5.62%)</td><td>4.85 (-8.80%)</td><td>4.62 <b>(+31.25%)</b></td><td>0.26 <b>(-75.05%)</b></td><td>227.10 <b>(-23.82%)</b></td><td>212.94 (+2.04%)</td><td>216.30 (+9.63%)</td><td>199.10 (+18.65%)</td><td>11.15 <b>(-78.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>6.25 (n/a)</td><td>5.23 (n/a)</td><td>5.32 (n/a)</td><td>3.52 (n/a)</td><td>1.04 (n/a)</td><td>298.10 (n/a)</td><td>208.68 (n/a)</td><td>197.30 (n/a)</td><td>167.80 (n/a)</td><td>51.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>8.14 (-2.16%)</td><td>7.67 (+12.78%)</td><td>7.70 (+13.15%)</td><td>7.06 <b>(+36.54%)</b></td><td>0.40 <b>(-65.13%)</b></td><td>297.20 <b>(-26.76%)</b></td><td>274.14 (-13.27%)</td><td>272.30 (-11.62%)</td><td>257.60 (+2.22%)</td><td>14.75 <b>(-74.16%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>8.32 (n/a)</td><td>6.80 (n/a)</td><td>6.81 (n/a)</td><td>5.17 (n/a)</td><td>1.15 (n/a)</td><td>405.80 (n/a)</td><td>316.10 (n/a)</td><td>308.10 (n/a)</td><td>252.00 (n/a)</td><td>57.06 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>3.63 (-2.55%)</td><td>2.87 (-12.11%)</td><td>2.74 (-17.98%)</td><td>2.19 (-14.14%)</td><td>0.56 <b>(+26.90%)</b></td><td>239.50 (+16.43%)</td><td>188.26 (+15.36%)</td><td>191.70 <b>(+21.95%)</b></td><td>144.30 (+2.63%)</td><td>36.60 <b>(+46.18%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>3.73 (n/a)</td><td>3.27 (n/a)</td><td>3.34 (n/a)</td><td>2.55 (n/a)</td><td>0.44 (n/a)</td><td>205.70 (n/a)</td><td>163.20 (n/a)</td><td>157.20 (n/a)</td><td>140.60 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.29 (+9.94%)</td><td>0.20 (-8.32%)</td><td>0.19 (-13.89%)</td><td>0.09 <b>(-46.84%)</b></td><td>0.07 <b>(+86.20%)</b></td><td>347.70 <b>(+88.05%)</b></td><td>186.98 <b>(+23.14%)</b></td><td>169.50 (+16.18%)</td><td>113.10 (-9.01%)</td><td>93.35 <b>(+236.28%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.90 (n/a)</td><td>151.84 (n/a)</td><td>145.90 (n/a)</td><td>124.30 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.21 (+5.31%)</td><td>0.19 (+10.49%)</td><td>0.19 (+12.43%)</td><td>0.15 (+0.20%)</td><td>0.02 <b>(+29.75%)</b></td><td>212.40 (-0.19%)</td><td>173.20 (-9.05%)</td><td>168.80 (-11.06%)</td><td>155.00 (-5.02%)</td><td>22.95 <b>(+26.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>190.44 (n/a)</td><td>189.80 (n/a)</td><td>163.20 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.36 (-18.83%)</td><td>0.32 (-12.45%)</td><td>0.32 (-15.65%)</td><td>0.29 (+2.08%)</td><td>0.02 <b>(-63.28%)</b></td><td>223.50 (-2.06%)</td><td>202.64 (+11.83%)</td><td>204.60 (+18.54%)</td><td>183.00 <b>(+23.23%)</b></td><td>14.66 <b>(-55.64%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>228.20 (n/a)</td><td>181.20 (n/a)</td><td>172.60 (n/a)</td><td>148.50 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.43 (+8.66%)</td><td>0.38 (+10.29%)</td><td>0.37 (+0.94%)</td><td>0.34 <b>(+24.92%)</b></td><td>0.03 <b>(-39.47%)</b></td><td>194.10 (-19.93%)</td><td>174.58 (-10.66%)</td><td>175.00 (-0.91%)</td><td>153.80 (-7.96%)</td><td>14.42 <b>(-55.57%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>242.40 (n/a)</td><td>195.42 (n/a)</td><td>176.60 (n/a)</td><td>167.10 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.54 (+7.25%)</td><td>0.41 (-3.54%)</td><td>0.39 (-7.10%)</td><td>0.33 (-11.06%)</td><td>0.08 <b>(+56.70%)</b></td><td>200.10 (+12.42%)</td><td>164.32 (+5.39%)</td><td>166.70 (+7.62%)</td><td>121.70 (-6.74%)</td><td>28.89 <b>(+61.39%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>178.00 (n/a)</td><td>155.92 (n/a)</td><td>154.90 (n/a)</td><td>130.50 (n/a)</td><td>17.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.98 (-5.44%)</td><td>0.80 (+0.47%)</td><td>0.74 (-4.46%)</td><td>0.60 (-12.06%)</td><td>0.17 (+18.76%)</td><td>217.30 (+13.71%)</td><td>168.96 (+0.93%)</td><td>176.90 (+4.67%)</td><td>133.20 (+5.80%)</td><td>35.27 <b>(+41.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.04 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.14 (n/a)</td><td>191.10 (n/a)</td><td>167.40 (n/a)</td><td>169.00 (n/a)</td><td>125.90 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.04 (-2.76%)</td><td>0.78 (-12.92%)</td><td>0.76 (-12.41%)</td><td>0.60 (-16.32%)</td><td>0.17 (+11.50%)</td><td>219.70 (+19.53%)</td><td>173.60 (+16.23%)</td><td>171.50 (+14.18%)</td><td>126.00 (+2.86%)</td><td>35.28 <b>(+38.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>1.07 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.71 (n/a)</td><td>0.15 (n/a)</td><td>183.80 (n/a)</td><td>149.36 (n/a)</td><td>150.20 (n/a)</td><td>122.50 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.95 (+6.82%)</td><td>0.79 (-4.97%)</td><td>0.80 (-6.33%)</td><td>0.60 (-19.30%)</td><td>0.13 <b>(+128.68%)</b></td><td>216.80 <b>(+23.96%)</b></td><td>169.68 (+7.28%)</td><td>163.00 (+6.75%)</td><td>137.80 (-6.39%)</td><td>30.02 <b>(+168.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.89 (n/a)</td><td>0.83 (n/a)</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.06 (n/a)</td><td>174.90 (n/a)</td><td>158.16 (n/a)</td><td>152.70 (n/a)</td><td>147.20 (n/a)</td><td>11.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>1.11 (+17.11%)</td><td>0.74 (-11.06%)</td><td>0.78 (-5.46%)</td><td>0.40 <b>(-47.48%)</b></td><td>0.26 <b>(+272.62%)</b></td><td>325.40 <b>(+90.40%)</b></td><td>198.16 <b>(+25.21%)</b></td><td>168.40 (+5.71%)</td><td>118.20 (-14.60%)</td><td>79.24 <b>(+529.49%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.77 (n/a)</td><td>0.07 (n/a)</td><td>170.90 (n/a)</td><td>158.26 (n/a)</td><td>159.30 (n/a)</td><td>138.40 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:36:21</td><td>0.12 (+5.62%)</td><td>0.10 (+5.29%)</td><td>0.09 (+1.49%)</td><td>0.09 (+12.73%)</td><td>0.01 (-3.38%)</td><td>184.80 (-11.28%)</td><td>169.92 (-5.35%)</td><td>180.10 (-1.42%)</td><td>135.40 (-5.31%)</td><td>20.90 (-18.43%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:19:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>179.52 (n/a)</td><td>182.70 (n/a)</td><td>143.00 (n/a)</td><td>25.62 (n/a)</td>
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
