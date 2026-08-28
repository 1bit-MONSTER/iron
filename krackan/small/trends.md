# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 <b>(-20.88%)</b></td><td>0.06 <b>(-20.87%)</b></td><td>0.07 <b>(-22.95%)</b></td><td>0.05 (-12.72%)</td><td>0.01 <b>(-20.13%)</b></td><td>227.80 (+14.53%)</td><td>193.94 <b>(+26.15%)</b></td><td>184.30 <b>(+29.79%)</b></td><td>162.40 <b>(+26.38%)</b></td><td>31.91 (+15.72%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>153.74 (n/a)</td><td>142.00 (n/a)</td><td>128.50 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (-13.51%)</td><td>0.07 (-2.24%)</td><td>0.07 (+0.99%)</td><td>0.06 (+5.50%)</td><td>0.01 <b>(-47.82%)</b></td><td>197.60 (-5.23%)</td><td>174.72 (+0.75%)</td><td>168.80 (-1.00%)</td><td>155.30 (+15.64%)</td><td>16.15 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>173.42 (n/a)</td><td>170.50 (n/a)</td><td>134.30 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.10 (+0.47%)</td><td>0.07 (+4.60%)</td><td>0.07 (+1.36%)</td><td>0.06 <b>(+24.10%)</b></td><td>0.02 <b>(-26.54%)</b></td><td>203.00 (-19.44%)</td><td>170.74 (-8.06%)</td><td>171.90 (-1.32%)</td><td>123.30 (-0.40%)</td><td>29.56 <b>(-44.37%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>252.00 (n/a)</td><td>185.70 (n/a)</td><td>174.20 (n/a)</td><td>123.80 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (+4.92%)</td><td>0.06 (-9.48%)</td><td>0.06 (-16.09%)</td><td>0.05 (-13.31%)</td><td>0.01 <b>(+137.86%)</b></td><td>225.60 (+15.34%)</td><td>203.16 (+11.97%)</td><td>217.30 (+19.13%)</td><td>160.30 (-4.64%)</td><td>26.99 <b>(+159.73%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>195.60 (n/a)</td><td>181.44 (n/a)</td><td>182.40 (n/a)</td><td>168.10 (n/a)</td><td>10.39 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.03 <b>(-24.10%)</b></td><td>0.03 (-11.74%)</td><td>0.03 (-9.72%)</td><td>0.03 (-15.13%)</td><td>0.00 <b>(-42.63%)</b></td><td>200.30 (+17.82%)</td><td>167.22 (+12.32%)</td><td>161.40 (+10.78%)</td><td>154.00 <b>(+31.74%)</b></td><td>19.12 (-10.36%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>170.00 (n/a)</td><td>148.88 (n/a)</td><td>145.70 (n/a)</td><td>116.90 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.03 (-3.40%)</td><td>0.03 (-7.63%)</td><td>0.03 (-14.86%)</td><td>0.02 <b>(+30.12%)</b></td><td>0.00 <b>(-41.17%)</b></td><td>242.30 <b>(-23.15%)</b></td><td>193.92 (+2.34%)</td><td>183.80 (+17.44%)</td><td>156.70 (+3.50%)</td><td>32.44 <b>(-54.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>315.30 (n/a)</td><td>189.48 (n/a)</td><td>156.50 (n/a)</td><td>151.40 (n/a)</td><td>70.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (+6.75%)</td><td>0.03 (+3.96%)</td><td>0.03 (+9.66%)</td><td>0.02 (-17.00%)</td><td>0.01 <b>(+74.39%)</b></td><td>263.80 <b>(+20.46%)</b></td><td>186.30 (-0.86%)</td><td>176.50 (-8.79%)</td><td>146.90 (-6.31%)</td><td>46.50 <b>(+101.50%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.00 (n/a)</td><td>187.92 (n/a)</td><td>193.50 (n/a)</td><td>156.80 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (+6.98%)</td><td>0.03 (-3.45%)</td><td>0.03 (-9.94%)</td><td>0.03 (-7.96%)</td><td>0.01 <b>(+59.84%)</b></td><td>209.30 (+8.67%)</td><td>172.22 (+5.35%)</td><td>179.80 (+11.06%)</td><td>129.20 (-6.51%)</td><td>30.83 <b>(+59.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.60 (n/a)</td><td>163.48 (n/a)</td><td>161.90 (n/a)</td><td>138.20 (n/a)</td><td>19.32 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (+13.07%)</td><td>0.03 (+8.87%)</td><td>0.03 (-0.75%)</td><td>0.02 (+8.39%)</td><td>0.01 (+13.51%)</td><td>217.20 (-7.73%)</td><td>173.04 (-8.07%)</td><td>174.40 (+0.75%)</td><td>138.40 (-11.57%)</td><td>29.97 (-8.01%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.40 (n/a)</td><td>188.24 (n/a)</td><td>173.10 (n/a)</td><td>156.50 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (-9.45%)</td><td>0.03 (-10.97%)</td><td>0.03 (-17.85%)</td><td>0.02 (+7.75%)</td><td>0.01 (-19.94%)</td><td>212.70 (-7.16%)</td><td>185.32 (+9.41%)</td><td>199.10 <b>(+21.70%)</b></td><td>116.80 (+10.50%)</td><td>38.76 <b>(-21.89%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>169.38 (n/a)</td><td>163.60 (n/a)</td><td>105.70 (n/a)</td><td>49.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (+5.73%)</td><td>0.03 (-5.64%)</td><td>0.03 (-6.96%)</td><td>0.02 (-5.19%)</td><td>0.01 <b>(+45.48%)</b></td><td>217.70 (+5.47%)</td><td>188.94 (+7.54%)</td><td>193.60 (+7.44%)</td><td>137.10 (-5.38%)</td><td>32.56 <b>(+44.92%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>175.70 (n/a)</td><td>180.20 (n/a)</td><td>144.90 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.02 (-13.64%)</td><td>0.02 (-9.53%)</td><td>0.02 (-9.18%)</td><td>0.02 (-4.49%)</td><td>0.00 <b>(-35.53%)</b></td><td>252.90 (+4.72%)</td><td>230.00 (+10.13%)</td><td>222.30 (+10.10%)</td><td>217.10 (+15.79%)</td><td>15.58 <b>(-23.13%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.50 (n/a)</td><td>208.84 (n/a)</td><td>201.90 (n/a)</td><td>187.50 (n/a)</td><td>20.27 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>170.68 (n/a)</td><td>180.10 (n/a)</td><td>142.50 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>172.72 (n/a)</td><td>165.20 (n/a)</td><td>156.10 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>166.36 (n/a)</td><td>157.50 (n/a)</td><td>133.20 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>194.52 (n/a)</td><td>178.70 (n/a)</td><td>149.60 (n/a)</td><td>37.23 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>154.82 (n/a)</td><td>156.60 (n/a)</td><td>134.50 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>174.00 (n/a)</td><td>159.64 (n/a)</td><td>159.90 (n/a)</td><td>145.70 (n/a)</td><td>10.04 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.20 (n/a)</td><td>180.32 (n/a)</td><td>176.80 (n/a)</td><td>138.90 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>310.50 (n/a)</td><td>215.90 (n/a)</td><td>195.00 (n/a)</td><td>179.30 (n/a)</td><td>54.23 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>146.22 (n/a)</td><td>131.50 (n/a)</td><td>124.20 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>155.80 (n/a)</td><td>150.60 (n/a)</td><td>137.80 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>161.14 (n/a)</td><td>146.70 (n/a)</td><td>135.40 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>331.90 (n/a)</td><td>189.76 (n/a)</td><td>162.50 (n/a)</td><td>137.70 (n/a)</td><td>80.15 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.60 (n/a)</td><td>175.16 (n/a)</td><td>177.20 (n/a)</td><td>164.40 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>194.40 (n/a)</td><td>204.60 (n/a)</td><td>154.10 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>169.40 (n/a)</td><td>175.60 (n/a)</td><td>129.30 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>184.60 (n/a)</td><td>185.10 (n/a)</td><td>153.70 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.46 (+2.98%)</td><td>3.82 (-6.08%)</td><td>3.54 (-14.75%)</td><td>3.37 (-10.32%)</td><td>0.49 <b>(+110.44%)</b></td><td>2789.30 (+11.51%)</td><td>2489.34 (+7.51%)</td><td>2656.30 (+17.31%)</td><td>2106.30 (-2.89%)</td><td>302.03 <b>(+126.04%)</b></td><td>1756.36 (+2.98%)</td><td>1504.61 (-6.08%)</td><td>1392.69 (-14.75%)</td><td>1326.28 (-10.32%)</td><td>191.03 <b>(+110.44%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>4.34 (n/a)</td><td>4.07 (n/a)</td><td>4.15 (n/a)</td><td>3.76 (n/a)</td><td>0.23 (n/a)</td><td>2501.50 (n/a)</td><td>2315.36 (n/a)</td><td>2264.40 (n/a)</td><td>2169.00 (n/a)</td><td>133.62 (n/a)</td><td>1705.54 (n/a)</td><td>1601.94 (n/a)</td><td>1633.69 (n/a)</td><td>1478.87 (n/a)</td><td>90.78 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.99 (-19.24%)</td><td>0.91 (-12.96%)</td><td>0.94 (-5.34%)</td><td>0.71 <b>(-27.34%)</b></td><td>0.11 (+10.56%)</td><td>310.40 <b>(+37.59%)</b></td><td>246.58 (+15.79%)</td><td>235.70 (+5.65%)</td><td>223.20 <b>(+23.79%)</b></td><td>36.44 <b>(+92.02%)</b></td><td>42.28 (-19.24%)</td><td>38.85 (-12.96%)</td><td>40.04 (-5.34%)</td><td>30.40 <b>(-27.34%)</b></td><td>4.90 (+10.56%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.23 (n/a)</td><td>1.05 (n/a)</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td><td>0.10 (n/a)</td><td>225.60 (n/a)</td><td>212.96 (n/a)</td><td>223.10 (n/a)</td><td>180.30 (n/a)</td><td>18.98 (n/a)</td><td>52.36 (n/a)</td><td>44.64 (n/a)</td><td>42.30 (n/a)</td><td>41.84 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>1.29 (+6.37%)</td><td>0.92 (+2.92%)</td><td>0.98 (+3.40%)</td><td>0.58 (-13.39%)</td><td>0.30 <b>(+37.36%)</b></td><td>379.10 (+15.47%)</td><td>262.78 (+1.75%)</td><td>225.80 (-3.30%)</td><td>171.70 (-5.97%)</td><td>90.97 <b>(+48.19%)</b></td><td>54.96 (+6.37%)</td><td>39.41 (+2.92%)</td><td>41.80 (+3.40%)</td><td>24.89 (-13.39%)</td><td>12.82 <b>(+37.36%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.21 (n/a)</td><td>0.90 (n/a)</td><td>0.95 (n/a)</td><td>0.67 (n/a)</td><td>0.22 (n/a)</td><td>328.30 (n/a)</td><td>258.26 (n/a)</td><td>233.50 (n/a)</td><td>182.60 (n/a)</td><td>61.39 (n/a)</td><td>51.67 (n/a)</td><td>38.29 (n/a)</td><td>40.42 (n/a)</td><td>28.74 (n/a)</td><td>9.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.52 (+0.95%)</td><td>0.52 (+0.23%)</td><td>0.52 (+0.02%)</td><td>0.52 (+0.08%)</td><td>0.00 <b>(+174.00%)</b></td><td>48612.40 (-0.08%)</td><td>48385.52 (-0.23%)</td><td>48462.30 (-0.02%)</td><td>47975.60 (-0.94%)</td><td>240.93 <b>(+170.86%)</b></td><td>358.10 (+0.95%)</td><td>355.07 (+0.23%)</td><td>354.50 (+0.02%)</td><td>353.40 (+0.08%)</td><td>1.78 <b>(+174.00%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48649.40 (n/a)</td><td>48494.88 (n/a)</td><td>48471.10 (n/a)</td><td>48433.10 (n/a)</td><td>88.95 (n/a)</td><td>354.71 (n/a)</td><td>354.26 (n/a)</td><td>354.44 (n/a)</td><td>353.14 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.90 (-0.04%)</td><td>0.90 (+0.42%)</td><td>0.90 (+0.41%)</td><td>0.89 (+0.71%)</td><td>0.00 <b>(-31.76%)</b></td><td>28274.70 (-0.70%)</td><td>28099.30 (-0.42%)</td><td>28116.10 (-0.41%)</td><td>27892.80 (+0.04%)</td><td>144.96 <b>(-32.15%)</b></td><td>615.93 (-0.04%)</td><td>611.41 (+0.42%)</td><td>611.03 (+0.41%)</td><td>607.60 (+0.71%)</td><td>3.16 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28474.90 (n/a)</td><td>28216.96 (n/a)</td><td>28232.20 (n/a)</td><td>27880.60 (n/a)</td><td>213.66 (n/a)</td><td>616.19 (n/a)</td><td>608.88 (n/a)</td><td>608.52 (n/a)</td><td>603.33 (n/a)</td><td>4.63 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>3.46 (+3.48%)</td><td>3.28 (+0.00%)</td><td>3.26 (-1.22%)</td><td>3.18 (+0.32%)</td><td>0.12 <b>(+73.44%)</b></td><td>7923.70 (-0.32%)</td><td>7691.58 (+0.06%)</td><td>7729.70 (+1.24%)</td><td>7264.20 (-3.36%)</td><td>267.12 <b>(+66.31%)</b></td><td>2365.00 (+3.48%)</td><td>2235.81 (+0.00%)</td><td>2222.59 (-1.22%)</td><td>2168.16 (+0.32%)</td><td>79.77 <b>(+73.44%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.35 (n/a)</td><td>3.28 (n/a)</td><td>3.30 (n/a)</td><td>3.17 (n/a)</td><td>0.07 (n/a)</td><td>7948.80 (n/a)</td><td>7686.76 (n/a)</td><td>7635.30 (n/a)</td><td>7516.60 (n/a)</td><td>160.62 (n/a)</td><td>2285.58 (n/a)</td><td>2235.77 (n/a)</td><td>2250.06 (n/a)</td><td>2161.32 (n/a)</td><td>45.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.19 (+5.79%)</td><td>3.59 (-0.41%)</td><td>3.60 (+0.74%)</td><td>2.98 (-8.48%)</td><td>0.43 <b>(+71.05%)</b></td><td>2704.80 (+9.27%)</td><td>2272.14 (+1.22%)</td><td>2242.00 (-0.73%)</td><td>1921.90 (-5.47%)</td><td>282.31 <b>(+78.00%)</b></td><td>1099.91 (+5.79%)</td><td>941.59 (-0.41%)</td><td>942.87 (+0.74%)</td><td>781.55 (-8.48%)</td><td>113.85 <b>(+71.05%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.96 (n/a)</td><td>3.61 (n/a)</td><td>3.57 (n/a)</td><td>3.26 (n/a)</td><td>0.25 (n/a)</td><td>2475.40 (n/a)</td><td>2244.72 (n/a)</td><td>2258.50 (n/a)</td><td>2033.20 (n/a)</td><td>158.60 (n/a)</td><td>1039.73 (n/a)</td><td>945.49 (n/a)</td><td>935.98 (n/a)</td><td>853.97 (n/a)</td><td>66.56 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.59 (-2.15%)</td><td>0.38 (-2.34%)</td><td>0.33 (-9.53%)</td><td>0.31 (+10.38%)</td><td>0.12 (-6.33%)</td><td>4030.30 (-9.40%)</td><td>3502.74 (+1.24%)</td><td>3796.30 (+10.54%)</td><td>2115.20 (+2.19%)</td><td>783.00 (-13.28%)</td><td>31.73 (-2.15%)</td><td>20.30 (-2.34%)</td><td>17.68 (-9.53%)</td><td>16.65 (+10.38%)</td><td>6.40 (-6.33%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.60 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>4448.60 (n/a)</td><td>3459.76 (n/a)</td><td>3434.40 (n/a)</td><td>2069.80 (n/a)</td><td>902.89 (n/a)</td><td>32.42 (n/a)</td><td>20.79 (n/a)</td><td>19.54 (n/a)</td><td>15.09 (n/a)</td><td>6.84 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.84 (-0.04%)</td><td>4.40 (+7.18%)</td><td>4.67 <b>(+25.61%)</b></td><td>3.56 (-1.64%)</td><td>0.54 (-10.97%)</td><td>1866.70 (+1.67%)</td><td>1531.66 (-7.00%)</td><td>1423.70 <b>(-20.39%)</b></td><td>1375.40 (+0.04%)</td><td>206.62 (-9.84%)</td><td>1494.28 (-0.04%)</td><td>1359.65 (+7.18%)</td><td>1443.61 <b>(+25.61%)</b></td><td>1100.98 (-1.64%)</td><td>165.71 (-10.97%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>4.84 (n/a)</td><td>4.11 (n/a)</td><td>3.72 (n/a)</td><td>3.62 (n/a)</td><td>0.60 (n/a)</td><td>1836.00 (n/a)</td><td>1646.92 (n/a)</td><td>1788.30 (n/a)</td><td>1374.90 (n/a)</td><td>229.18 (n/a)</td><td>1494.82 (n/a)</td><td>1268.62 (n/a)</td><td>1149.28 (n/a)</td><td>1119.38 (n/a)</td><td>186.13 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>13.69 (n/a)</td><td>12.88 (n/a)</td><td>13.07 (n/a)</td><td>11.97 (n/a)</td><td>0.64 (n/a)</td><td>13.69 (n/a)</td><td>12.87 (n/a)</td><td>13.06 (n/a)</td><td>11.96 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>24.46 (-0.70%)</td><td>23.61 (-1.60%)</td><td>23.93 (-0.13%)</td><td>21.81 (-7.95%)</td><td>1.05 <b>(+174.25%)</b></td><td>24.45 (-0.70%)</td><td>23.60 (-1.60%)</td><td>23.91 (-0.13%)</td><td>21.80 (-7.95%)</td><td>1.05 <b>(+174.26%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>24.64 (n/a)</td><td>24.00 (n/a)</td><td>23.96 (n/a)</td><td>23.69 (n/a)</td><td>0.38 (n/a)</td><td>24.62 (n/a)</td><td>23.99 (n/a)</td><td>23.94 (n/a)</td><td>23.68 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>41.34 (+1.85%)</td><td>40.26 (+1.76%)</td><td>40.32 (+2.65%)</td><td>38.55 (-0.67%)</td><td>1.15 <b>(+40.89%)</b></td><td>41.31 (+1.85%)</td><td>40.24 (+1.76%)</td><td>40.30 (+2.65%)</td><td>38.52 (-0.67%)</td><td>1.15 <b>(+40.89%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>40.59 (n/a)</td><td>39.56 (n/a)</td><td>39.28 (n/a)</td><td>38.81 (n/a)</td><td>0.82 (n/a)</td><td>40.56 (n/a)</td><td>39.54 (n/a)</td><td>39.26 (n/a)</td><td>38.78 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>47.08 (+6.96%)</td><td>41.32 (-3.87%)</td><td>41.39 (-3.01%)</td><td>33.00 <b>(-22.19%)</b></td><td>5.63 <b>(+699.54%)</b></td><td>47.05 (+6.96%)</td><td>41.30 (-3.87%)</td><td>41.37 (-3.01%)</td><td>32.98 <b>(-22.19%)</b></td><td>5.62 <b>(+699.54%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>44.01 (n/a)</td><td>42.99 (n/a)</td><td>42.68 (n/a)</td><td>42.41 (n/a)</td><td>0.70 (n/a)</td><td>43.99 (n/a)</td><td>42.96 (n/a)</td><td>42.65 (n/a)</td><td>42.39 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>13.46 (n/a)</td><td>12.31 (n/a)</td><td>12.77 (n/a)</td><td>10.06 (n/a)</td><td>1.34 (n/a)</td><td>13.46 (n/a)</td><td>12.30 (n/a)</td><td>12.76 (n/a)</td><td>10.06 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>24.45 (+0.83%)</td><td>23.77 (-1.36%)</td><td>23.92 (-1.11%)</td><td>22.95 (-3.91%)</td><td>0.55 <b>(+210.60%)</b></td><td>24.44 (+0.83%)</td><td>23.75 (-1.36%)</td><td>23.90 (-1.11%)</td><td>22.93 (-3.91%)</td><td>0.55 <b>(+210.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>24.25 (n/a)</td><td>24.09 (n/a)</td><td>24.18 (n/a)</td><td>23.88 (n/a)</td><td>0.18 (n/a)</td><td>24.23 (n/a)</td><td>24.08 (n/a)</td><td>24.17 (n/a)</td><td>23.87 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>41.65 (+1.55%)</td><td>40.62 (+2.06%)</td><td>40.83 (+2.98%)</td><td>39.19 (+1.52%)</td><td>1.09 <b>(+23.98%)</b></td><td>41.63 (+1.55%)</td><td>40.60 (+2.06%)</td><td>40.80 (+2.98%)</td><td>39.17 (+1.52%)</td><td>1.09 <b>(+23.98%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>41.02 (n/a)</td><td>39.80 (n/a)</td><td>39.64 (n/a)</td><td>38.60 (n/a)</td><td>0.88 (n/a)</td><td>40.99 (n/a)</td><td>39.78 (n/a)</td><td>39.62 (n/a)</td><td>38.58 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>44.44 (+4.38%)</td><td>43.20 (+2.94%)</td><td>43.52 (+3.77%)</td><td>41.57 (+0.73%)</td><td>1.33 <b>(+118.00%)</b></td><td>44.42 (+4.38%)</td><td>43.17 (+2.94%)</td><td>43.49 (+3.77%)</td><td>41.54 (+0.73%)</td><td>1.32 <b>(+118.00%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>42.58 (n/a)</td><td>41.96 (n/a)</td><td>41.94 (n/a)</td><td>41.27 (n/a)</td><td>0.61 (n/a)</td><td>42.55 (n/a)</td><td>41.94 (n/a)</td><td>41.92 (n/a)</td><td>41.24 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>9.40 (+6.02%)</td><td>8.93 (+7.65%)</td><td>8.90 (+5.87%)</td><td>8.20 (+6.71%)</td><td>0.48 (-8.47%)</td><td>9.38 (+6.02%)</td><td>8.92 (+7.65%)</td><td>8.88 (+5.87%)</td><td>8.18 (+6.71%)</td><td>0.47 (-8.47%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>8.86 (n/a)</td><td>8.30 (n/a)</td><td>8.40 (n/a)</td><td>7.69 (n/a)</td><td>0.52 (n/a)</td><td>8.85 (n/a)</td><td>8.28 (n/a)</td><td>8.39 (n/a)</td><td>7.67 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.99 (+3.32%)</td><td>0.91 (+7.85%)</td><td>0.95 (+10.47%)</td><td>0.75 (+11.92%)</td><td>0.10 (-10.40%)</td><td>0.98 (+3.32%)</td><td>0.89 (+7.85%)</td><td>0.93 (+10.47%)</td><td>0.74 (+11.92%)</td><td>0.10 (-10.40%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.96 (n/a)</td><td>0.84 (n/a)</td><td>0.86 (n/a)</td><td>0.67 (n/a)</td><td>0.12 (n/a)</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.66 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>1.24 (-2.44%)</td><td>1.10 (+10.40%)</td><td>1.15 (+19.21%)</td><td>0.85 (+11.55%)</td><td>0.15 (-18.30%)</td><td>1.22 (-2.44%)</td><td>1.09 (+10.40%)</td><td>1.14 (+19.21%)</td><td>0.84 (+11.55%)</td><td>0.15 (-18.30%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.27 (n/a)</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.77 (n/a)</td><td>0.18 (n/a)</td><td>1.26 (n/a)</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.76 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>17.80 (+6.33%)</td><td>16.62 (+1.57%)</td><td>17.11 (+3.51%)</td><td>14.94 (-6.14%)</td><td>1.22 <b>(+239.31%)</b></td><td>17.59 (+6.33%)</td><td>16.43 (+1.57%)</td><td>16.91 (+3.51%)</td><td>14.76 (-6.14%)</td><td>1.20 <b>(+239.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>16.74 (n/a)</td><td>16.37 (n/a)</td><td>16.53 (n/a)</td><td>15.91 (n/a)</td><td>0.36 (n/a)</td><td>16.55 (n/a)</td><td>16.18 (n/a)</td><td>16.34 (n/a)</td><td>15.73 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>14.60 (+10.06%)</td><td>13.96 (+11.00%)</td><td>14.13 (+9.92%)</td><td>13.12 (+11.82%)</td><td>0.59 (-10.09%)</td><td>14.34 (+10.06%)</td><td>13.72 (+11.00%)</td><td>13.88 (+9.92%)</td><td>12.89 (+11.82%)</td><td>0.58 (-10.09%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>13.26 (n/a)</td><td>12.58 (n/a)</td><td>12.85 (n/a)</td><td>11.74 (n/a)</td><td>0.66 (n/a)</td><td>13.03 (n/a)</td><td>12.36 (n/a)</td><td>12.63 (n/a)</td><td>11.53 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>10.64 <b>(+27.33%)</b></td><td>7.87 (+12.20%)</td><td>7.08 (-1.49%)</td><td>6.59 <b>(+26.28%)</b></td><td>1.65 <b>(+42.42%)</b></td><td>10.46 <b>(+27.33%)</b></td><td>7.73 (+12.20%)</td><td>6.96 (-1.49%)</td><td>6.47 <b>(+26.28%)</b></td><td>1.62 <b>(+42.42%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>8.36 (n/a)</td><td>7.01 (n/a)</td><td>7.19 (n/a)</td><td>5.22 (n/a)</td><td>1.16 (n/a)</td><td>8.21 (n/a)</td><td>6.89 (n/a)</td><td>7.07 (n/a)</td><td>5.13 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>6.28 (-8.43%)</td><td>5.92 (+1.64%)</td><td>6.23 (+3.43%)</td><td>4.88 (+13.37%)</td><td>0.59 <b>(-39.31%)</b></td><td>6.18 (-8.43%)</td><td>5.82 (+1.64%)</td><td>6.13 (+3.43%)</td><td>4.81 (+13.37%)</td><td>0.58 <b>(-39.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>6.86 (n/a)</td><td>5.82 (n/a)</td><td>6.02 (n/a)</td><td>4.31 (n/a)</td><td>0.98 (n/a)</td><td>6.75 (n/a)</td><td>5.73 (n/a)</td><td>5.93 (n/a)</td><td>4.24 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>13.23 (n/a)</td><td>12.47 (n/a)</td><td>12.57 (n/a)</td><td>11.64 (n/a)</td><td>0.73 (n/a)</td><td>13.22 (n/a)</td><td>12.46 (n/a)</td><td>12.56 (n/a)</td><td>11.63 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>13.17 (n/a)</td><td>12.65 (n/a)</td><td>12.67 (n/a)</td><td>12.09 (n/a)</td><td>0.39 (n/a)</td><td>13.17 (n/a)</td><td>12.64 (n/a)</td><td>12.67 (n/a)</td><td>12.09 (n/a)</td><td>0.39 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>159.88 (n/a)</td><td>158.60 (n/a)</td><td>115.50 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>151.64 (n/a)</td><td>148.50 (n/a)</td><td>119.00 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>168.62 (n/a)</td><td>168.00 (n/a)</td><td>137.00 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>197.30 (n/a)</td><td>194.70 (n/a)</td><td>164.10 (n/a)</td><td>29.81 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>189.46 (n/a)</td><td>189.90 (n/a)</td><td>134.10 (n/a)</td><td>40.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>193.26 (n/a)</td><td>199.50 (n/a)</td><td>156.00 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.60 (n/a)</td><td>215.34 (n/a)</td><td>203.20 (n/a)</td><td>140.90 (n/a)</td><td>76.28 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.20 (n/a)</td><td>231.34 (n/a)</td><td>206.40 (n/a)</td><td>189.20 (n/a)</td><td>54.64 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-11.20%)</td><td>0.05 (-4.38%)</td><td>0.05 (+6.53%)</td><td>0.04 (-5.59%)</td><td>0.00 <b>(-34.99%)</b></td><td>213.10 (+5.91%)</td><td>182.54 (+3.67%)</td><td>175.50 (-6.15%)</td><td>161.80 (+12.60%)</td><td>19.93 <b>(-21.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>176.08 (n/a)</td><td>187.00 (n/a)</td><td>143.70 (n/a)</td><td>25.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-9.09%)</td><td>0.05 (-12.29%)</td><td>0.05 (-6.47%)</td><td>0.04 (-10.45%)</td><td>0.01 <b>(-21.88%)</b></td><td>203.70 (+11.68%)</td><td>171.20 (+13.30%)</td><td>173.00 (+6.92%)</td><td>133.30 (+9.98%)</td><td>25.41 (-3.62%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>151.10 (n/a)</td><td>161.80 (n/a)</td><td>121.20 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (+3.57%)</td><td>0.05 (-8.91%)</td><td>0.05 (-10.56%)</td><td>0.04 (+0.43%)</td><td>0.01 (+7.21%)</td><td>206.50 (-0.43%)</td><td>171.44 (+10.22%)</td><td>171.90 (+11.77%)</td><td>119.90 (-3.38%)</td><td>34.91 (+4.38%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>155.54 (n/a)</td><td>153.80 (n/a)</td><td>124.10 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-8.46%)</td><td>0.05 (-1.17%)</td><td>0.05 (+0.17%)</td><td>0.04 (-2.95%)</td><td>0.00 (-19.02%)</td><td>197.80 (+3.02%)</td><td>176.86 (+0.84%)</td><td>180.40 (-0.22%)</td><td>155.70 (+9.19%)</td><td>18.36 (-9.10%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>175.38 (n/a)</td><td>180.80 (n/a)</td><td>142.60 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-1.70%)</td><td>0.04 (+1.11%)</td><td>0.05 (+5.21%)</td><td>0.04 (+3.08%)</td><td>0.00 <b>(-25.29%)</b></td><td>197.10 (-3.00%)</td><td>183.80 (-1.28%)</td><td>180.50 (-4.95%)</td><td>173.70 (+1.76%)</td><td>10.01 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>203.20 (n/a)</td><td>186.18 (n/a)</td><td>189.90 (n/a)</td><td>170.70 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-3.98%)</td><td>0.04 (-3.85%)</td><td>0.04 (-1.80%)</td><td>0.04 (-7.70%)</td><td>0.01 (+4.58%)</td><td>221.50 (+8.31%)</td><td>190.22 (+4.49%)</td><td>196.00 (+1.82%)</td><td>145.20 (+4.09%)</td><td>32.49 (+19.32%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>182.04 (n/a)</td><td>192.50 (n/a)</td><td>139.50 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 <b>(+20.83%)</b></td><td>0.05 (+9.51%)</td><td>0.05 (+10.46%)</td><td>0.04 (+4.71%)</td><td>0.01 <b>(+47.13%)</b></td><td>207.10 (-4.47%)</td><td>171.32 (-6.72%)</td><td>173.20 (-9.46%)</td><td>107.80 (-17.20%)</td><td>38.43 (+14.37%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>183.66 (n/a)</td><td>191.30 (n/a)</td><td>130.20 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (+1.33%)</td><td>0.05 (+0.87%)</td><td>0.04 (+1.01%)</td><td>0.04 (-0.09%)</td><td>0.01 (+2.30%)</td><td>206.50 (+0.05%)</td><td>180.90 (-0.71%)</td><td>195.60 (-1.01%)</td><td>110.90 (-1.33%)</td><td>39.48 (+0.63%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>182.20 (n/a)</td><td>197.60 (n/a)</td><td>112.40 (n/a)</td><td>39.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (+0.64%)</td><td>0.04 (-2.84%)</td><td>0.04 (-3.73%)</td><td>0.03 (-7.29%)</td><td>0.00 <b>(+30.19%)</b></td><td>241.00 (+7.83%)</td><td>209.00 (+3.28%)</td><td>206.70 (+3.87%)</td><td>184.50 (-0.65%)</td><td>21.04 <b>(+40.12%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.50 (n/a)</td><td>202.36 (n/a)</td><td>199.00 (n/a)</td><td>185.70 (n/a)</td><td>15.02 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 <b>(-37.91%)</b></td><td>0.04 (-11.65%)</td><td>0.04 (-5.68%)</td><td>0.04 (+4.78%)</td><td>0.00 <b>(-89.13%)</b></td><td>232.00 (-4.57%)</td><td>222.68 (+7.75%)</td><td>225.20 (+6.03%)</td><td>212.20 <b>(+61.00%)</b></td><td>7.68 <b>(-82.97%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>206.66 (n/a)</td><td>212.40 (n/a)</td><td>131.80 (n/a)</td><td>45.09 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-15.69%)</td><td>0.05 (-14.16%)</td><td>0.05 (-18.02%)</td><td>0.04 (+0.31%)</td><td>0.01 <b>(-43.74%)</b></td><td>183.90 (-0.27%)</td><td>159.56 (+14.86%)</td><td>156.20 <b>(+21.94%)</b></td><td>144.60 (+18.62%)</td><td>16.47 <b>(-35.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>138.92 (n/a)</td><td>128.10 (n/a)</td><td>121.90 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (+10.45%)</td><td>0.04 (+5.68%)</td><td>0.04 (+4.14%)</td><td>0.03 (+19.30%)</td><td>0.01 (-3.63%)</td><td>245.90 (-16.16%)</td><td>206.78 (-6.29%)</td><td>209.10 (-3.99%)</td><td>158.50 (-9.48%)</td><td>31.69 <b>(-29.84%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.30 (n/a)</td><td>220.66 (n/a)</td><td>217.80 (n/a)</td><td>175.10 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-2.98%)</td><td>0.05 (-4.22%)</td><td>0.05 (-9.20%)</td><td>0.04 (+6.05%)</td><td>0.01 <b>(-22.76%)</b></td><td>227.00 (-5.69%)</td><td>176.24 (+2.66%)</td><td>168.40 (+10.14%)</td><td>140.40 (+3.08%)</td><td>31.59 <b>(-24.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>171.68 (n/a)</td><td>152.90 (n/a)</td><td>136.20 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-5.50%)</td><td>0.05 (-2.04%)</td><td>0.05 (-6.83%)</td><td>0.04 (+8.53%)</td><td>0.01 (-13.19%)</td><td>193.70 (-7.89%)</td><td>165.70 (+1.33%)</td><td>174.90 (+7.37%)</td><td>134.50 (+5.82%)</td><td>25.63 (-16.86%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>163.52 (n/a)</td><td>162.90 (n/a)</td><td>127.10 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (+12.25%)</td><td>0.05 (-4.48%)</td><td>0.05 (-12.87%)</td><td>0.03 <b>(-36.89%)</b></td><td>0.02 <b>(+197.34%)</b></td><td>272.70 <b>(+58.45%)</b></td><td>177.62 (+13.02%)</td><td>181.10 (+14.77%)</td><td>119.90 (-10.86%)</td><td>60.31 <b>(+318.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>157.16 (n/a)</td><td>157.80 (n/a)</td><td>134.50 (n/a)</td><td>14.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 <b>(-22.62%)</b></td><td>0.04 (-11.45%)</td><td>0.04 (-7.11%)</td><td>0.03 (-4.98%)</td><td>0.01 <b>(-40.95%)</b></td><td>254.30 (+5.26%)</td><td>195.98 (+10.20%)</td><td>182.70 (+7.60%)</td><td>160.70 <b>(+29.18%)</b></td><td>36.03 (-18.02%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.60 (n/a)</td><td>177.84 (n/a)</td><td>169.80 (n/a)</td><td>124.40 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-18.50%)</td><td>0.04 (-10.76%)</td><td>0.04 (-17.39%)</td><td>0.04 <b>(+29.07%)</b></td><td>0.01 <b>(-44.82%)</b></td><td>221.70 <b>(-22.54%)</b></td><td>187.84 (+4.92%)</td><td>188.60 <b>(+21.05%)</b></td><td>140.60 <b>(+22.69%)</b></td><td>34.29 <b>(-48.23%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>286.20 (n/a)</td><td>179.04 (n/a)</td><td>155.80 (n/a)</td><td>114.60 (n/a)</td><td>66.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-2.41%)</td><td>0.04 (-5.04%)</td><td>0.04 (-7.24%)</td><td>0.04 (+1.61%)</td><td>0.00 (-19.84%)</td><td>210.30 (-1.59%)</td><td>190.80 (+4.75%)</td><td>195.10 (+7.79%)</td><td>158.50 (+2.46%)</td><td>19.26 <b>(-21.01%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>182.14 (n/a)</td><td>181.00 (n/a)</td><td>154.70 (n/a)</td><td>24.38 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.18 (-0.17%)</td><td>0.18 (+0.05%)</td><td>0.18 (+0.04%)</td><td>0.18 (+0.40%)</td><td>0.00 <b>(-74.55%)</b></td><td>47464.00 (-0.39%)</td><td>47402.48 (-0.05%)</td><td>47394.60 (-0.04%)</td><td>47368.10 (+0.17%)</td><td>36.40 <b>(-74.61%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47651.70 (n/a)</td><td>47427.42 (n/a)</td><td>47414.70 (n/a)</td><td>47289.00 (n/a)</td><td>143.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-4.25%)</td><td>0.05 (-12.54%)</td><td>0.04 (-15.94%)</td><td>0.04 <b>(-24.16%)</b></td><td>0.01 <b>(+58.91%)</b></td><td>225.40 <b>(+31.81%)</b></td><td>181.18 (+17.13%)</td><td>184.00 (+18.94%)</td><td>135.70 (+4.46%)</td><td>36.73 <b>(+115.85%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>154.68 (n/a)</td><td>154.70 (n/a)</td><td>129.90 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (-10.89%)</td><td>0.06 (-10.75%)</td><td>0.06 (-17.05%)</td><td>0.05 (-8.37%)</td><td>0.01 (-1.73%)</td><td>229.70 (+9.12%)</td><td>199.80 (+12.21%)</td><td>208.40 <b>(+20.53%)</b></td><td>173.60 (+12.22%)</td><td>23.86 (+16.15%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>178.06 (n/a)</td><td>172.90 (n/a)</td><td>154.70 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-8.64%)</td><td>0.05 (-1.97%)</td><td>0.04 (-14.89%)</td><td>0.04 <b>(+23.62%)</b></td><td>0.01 <b>(-33.51%)</b></td><td>202.70 (-19.11%)</td><td>175.56 (-0.80%)</td><td>183.50 (+17.48%)</td><td>147.80 (+9.48%)</td><td>25.37 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>176.98 (n/a)</td><td>156.20 (n/a)</td><td>135.00 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 <b>(+21.64%)</b></td><td>0.06 <b>(+21.47%)</b></td><td>0.06 (+16.34%)</td><td>0.05 <b>(+28.49%)</b></td><td>0.01 (+7.60%)</td><td>196.30 <b>(-22.16%)</b></td><td>163.52 (-18.40%)</td><td>158.40 (-14.01%)</td><td>124.70 (-17.80%)</td><td>27.33 <b>(-32.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>200.40 (n/a)</td><td>184.20 (n/a)</td><td>151.70 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-12.49%)</td><td>0.05 (-6.43%)</td><td>0.05 (-1.64%)</td><td>0.04 (-4.10%)</td><td>0.01 <b>(-26.64%)</b></td><td>199.80 (+4.23%)</td><td>166.78 (+5.72%)</td><td>170.90 (+1.67%)</td><td>132.60 (+14.31%)</td><td>25.87 (-12.13%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>157.76 (n/a)</td><td>168.10 (n/a)</td><td>116.00 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (+4.39%)</td><td>0.06 (+5.25%)</td><td>0.06 (+6.22%)</td><td>0.05 (+11.88%)</td><td>0.01 (-16.87%)</td><td>195.30 (-10.58%)</td><td>166.64 (-5.77%)</td><td>167.90 (-5.83%)</td><td>139.20 (-4.20%)</td><td>20.76 <b>(-28.39%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>176.84 (n/a)</td><td>178.30 (n/a)</td><td>145.30 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (+19.43%)</td><td>0.05 (+7.58%)</td><td>0.05 (+7.39%)</td><td>0.04 (-6.56%)</td><td>0.01 <b>(+156.97%)</b></td><td>232.30 (+7.05%)</td><td>182.42 (-5.35%)</td><td>174.70 (-6.88%)</td><td>153.50 (-16.26%)</td><td>31.43 <b>(+128.90%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>192.74 (n/a)</td><td>187.60 (n/a)</td><td>183.30 (n/a)</td><td>13.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (-16.13%)</td><td>0.05 (-2.88%)</td><td>0.05 (+3.91%)</td><td>0.05 (+5.06%)</td><td>0.01 <b>(-42.23%)</b></td><td>194.30 (-4.85%)</td><td>172.28 (+0.27%)</td><td>178.80 (-3.77%)</td><td>134.40 (+19.15%)</td><td>23.89 <b>(-32.20%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>171.82 (n/a)</td><td>185.80 (n/a)</td><td>112.80 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-1.61%)</td><td>0.05 (+1.63%)</td><td>0.05 (-2.73%)</td><td>0.04 (-3.72%)</td><td>0.01 (-4.66%)</td><td>204.40 (+3.86%)</td><td>170.66 (-1.72%)</td><td>172.20 (+2.81%)</td><td>144.80 (+1.61%)</td><td>22.67 (-1.47%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>173.64 (n/a)</td><td>167.50 (n/a)</td><td>142.50 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-19.91%)</td><td>0.04 (-17.11%)</td><td>0.05 (-16.41%)</td><td>0.03 (-18.12%)</td><td>0.01 <b>(-32.56%)</b></td><td>268.90 <b>(+22.17%)</b></td><td>211.42 (+19.57%)</td><td>202.70 (+19.66%)</td><td>171.20 <b>(+24.87%)</b></td><td>35.76 (+3.89%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>176.82 (n/a)</td><td>169.40 (n/a)</td><td>137.10 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-12.14%)</td><td>0.04 (-13.73%)</td><td>0.04 (-2.27%)</td><td>0.03 <b>(-33.10%)</b></td><td>0.01 <b>(+34.39%)</b></td><td>294.00 <b>(+49.47%)</b></td><td>209.76 (+18.76%)</td><td>190.50 (+2.31%)</td><td>169.40 (+13.84%)</td><td>48.91 <b>(+138.71%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>176.62 (n/a)</td><td>186.20 (n/a)</td><td>148.80 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 <b>(-32.90%)</b></td><td>0.04 (-18.00%)</td><td>0.04 (-6.57%)</td><td>0.02 <b>(-35.95%)</b></td><td>0.01 <b>(-36.76%)</b></td><td>349.60 <b>(+56.14%)</b></td><td>235.30 <b>(+21.88%)</b></td><td>224.70 (+7.05%)</td><td>176.60 <b>(+49.03%)</b></td><td>67.53 <b>(+59.31%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>193.06 (n/a)</td><td>209.90 (n/a)</td><td>118.50 (n/a)</td><td>42.39 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (-6.69%)</td><td>0.05 (-4.51%)</td><td>0.04 (+0.28%)</td><td>0.03 (-17.39%)</td><td>0.01 (+8.98%)</td><td>243.10 <b>(+21.07%)</b></td><td>184.24 (+5.96%)</td><td>184.50 (-0.27%)</td><td>142.30 (+7.15%)</td><td>38.71 <b>(+43.38%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>173.88 (n/a)</td><td>185.00 (n/a)</td><td>132.80 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (-13.54%)</td><td>0.04 (+12.76%)</td><td>0.04 <b>(+21.37%)</b></td><td>0.04 <b>(+44.66%)</b></td><td>0.00 <b>(-73.46%)</b></td><td>219.40 <b>(-30.88%)</b></td><td>206.42 (-15.22%)</td><td>203.90 (-17.62%)</td><td>191.80 (+15.61%)</td><td>12.43 <b>(-78.15%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.40 (n/a)</td><td>243.48 (n/a)</td><td>247.50 (n/a)</td><td>165.90 (n/a)</td><td>56.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (-8.76%)</td><td>0.04 (-0.43%)</td><td>0.04 (+1.64%)</td><td>0.02 (+8.29%)</td><td>0.01 (-19.36%)</td><td>347.10 (-7.66%)</td><td>242.16 (-1.58%)</td><td>221.90 (-1.60%)</td><td>198.60 (+9.60%)</td><td>60.07 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>375.90 (n/a)</td><td>246.04 (n/a)</td><td>225.50 (n/a)</td><td>181.20 (n/a)</td><td>75.26 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.80 (+13.39%)</td><td>0.56 (-1.93%)</td><td>0.53 (-6.65%)</td><td>0.39 (-13.34%)</td><td>0.17 <b>(+83.53%)</b></td><td>254.40 (+15.37%)</td><td>187.36 (+7.37%)</td><td>184.60 (+7.14%)</td><td>122.80 (-11.78%)</td><td>55.41 <b>(+85.94%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.71 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.09 (n/a)</td><td>220.50 (n/a)</td><td>174.50 (n/a)</td><td>172.30 (n/a)</td><td>139.20 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.85 (-9.81%)</td><td>0.60 (-2.84%)</td><td>0.53 (-5.55%)</td><td>0.51 <b>(+20.03%)</b></td><td>0.14 <b>(-35.88%)</b></td><td>194.00 (-16.70%)</td><td>169.98 (-3.08%)</td><td>185.50 (+5.88%)</td><td>116.00 (+10.90%)</td><td>31.67 <b>(-44.64%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.94 (n/a)</td><td>0.62 (n/a)</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>232.90 (n/a)</td><td>175.38 (n/a)</td><td>175.20 (n/a)</td><td>104.60 (n/a)</td><td>57.21 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.80 (-11.08%)</td><td>0.54 (-14.17%)</td><td>0.47 <b>(-26.90%)</b></td><td>0.41 (-6.79%)</td><td>0.16 (-10.74%)</td><td>237.00 (+7.29%)</td><td>192.40 (+16.21%)</td><td>208.00 <b>(+36.84%)</b></td><td>123.20 (+12.51%)</td><td>45.72 (+5.76%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.90 (n/a)</td><td>0.63 (n/a)</td><td>0.65 (n/a)</td><td>0.45 (n/a)</td><td>0.17 (n/a)</td><td>220.90 (n/a)</td><td>165.56 (n/a)</td><td>152.00 (n/a)</td><td>109.50 (n/a)</td><td>43.23 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.71 (-3.01%)</td><td>0.49 (-8.11%)</td><td>0.45 (-0.39%)</td><td>0.38 (-6.02%)</td><td>0.13 (-8.65%)</td><td>256.30 (+6.44%)</td><td>209.48 (+8.12%)</td><td>218.40 (+0.37%)</td><td>138.50 (+3.13%)</td><td>43.22 (-4.79%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.73 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.41 (n/a)</td><td>0.14 (n/a)</td><td>240.80 (n/a)</td><td>193.74 (n/a)</td><td>217.60 (n/a)</td><td>134.30 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.49 (-19.16%)</td><td>0.41 (-10.96%)</td><td>0.40 (-0.54%)</td><td>0.29 (-12.80%)</td><td>0.08 <b>(-31.54%)</b></td><td>250.10 (+14.67%)</td><td>186.18 (+10.77%)</td><td>182.60 (+0.55%)</td><td>149.50 <b>(+23.76%)</b></td><td>39.08 (+0.54%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.61 (n/a)</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>218.10 (n/a)</td><td>168.08 (n/a)</td><td>181.60 (n/a)</td><td>120.80 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.44 (-11.27%)</td><td>0.38 (-4.55%)</td><td>0.37 (-1.78%)</td><td>0.29 (-17.95%)</td><td>0.06 (+5.34%)</td><td>252.10 <b>(+21.85%)</b></td><td>199.98 (+5.56%)</td><td>199.50 (+1.84%)</td><td>166.50 (+12.65%)</td><td>34.94 <b>(+44.17%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>206.90 (n/a)</td><td>189.44 (n/a)</td><td>195.90 (n/a)</td><td>147.80 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.59 (+16.98%)</td><td>0.42 (-2.82%)</td><td>0.39 (-8.73%)</td><td>0.31 (-17.39%)</td><td>0.12 <b>(+131.88%)</b></td><td>240.30 <b>(+21.06%)</b></td><td>183.88 (+7.86%)</td><td>187.10 (+9.54%)</td><td>125.00 (-14.50%)</td><td>47.62 <b>(+139.80%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>198.50 (n/a)</td><td>170.48 (n/a)</td><td>170.80 (n/a)</td><td>146.20 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.52 (-11.07%)</td><td>0.40 (-10.55%)</td><td>0.42 (+8.12%)</td><td>0.30 (-4.97%)</td><td>0.08 <b>(-29.38%)</b></td><td>242.20 (+5.21%)</td><td>191.56 (+9.48%)</td><td>177.60 (-7.50%)</td><td>141.60 (+12.47%)</td><td>39.86 (-11.43%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>230.20 (n/a)</td><td>174.98 (n/a)</td><td>192.00 (n/a)</td><td>125.90 (n/a)</td><td>45.01 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.76 <b>(-26.90%)</b></td><td>0.65 <b>(-21.03%)</b></td><td>0.64 (-17.46%)</td><td>0.55 <b>(-23.39%)</b></td><td>0.07 <b>(-39.94%)</b></td><td>237.30 <b>(+30.53%)</b></td><td>202.32 <b>(+25.98%)</b></td><td>203.30 <b>(+21.16%)</b></td><td>172.70 <b>(+36.85%)</b></td><td>23.27 (+10.61%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.04 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.72 (n/a)</td><td>0.12 (n/a)</td><td>181.80 (n/a)</td><td>160.60 (n/a)</td><td>167.80 (n/a)</td><td>126.20 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.73 <b>(-30.90%)</b></td><td>0.68 (+1.85%)</td><td>0.69 (+18.24%)</td><td>0.63 <b>(+94.65%)</b></td><td>0.04 <b>(-85.68%)</b></td><td>207.80 <b>(-48.62%)</b></td><td>193.00 (-15.74%)</td><td>189.50 (-15.44%)</td><td>178.70 <b>(+44.70%)</b></td><td>11.29 <b>(-89.50%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.06 (n/a)</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>404.40 (n/a)</td><td>229.04 (n/a)</td><td>224.10 (n/a)</td><td>123.50 (n/a)</td><td>107.50 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.97 (+13.22%)</td><td>0.72 (-7.69%)</td><td>0.66 (-16.65%)</td><td>0.59 (-8.90%)</td><td>0.16 <b>(+90.57%)</b></td><td>222.20 (+9.73%)</td><td>188.48 (+10.99%)</td><td>197.20 (+19.95%)</td><td>135.40 (-11.68%)</td><td>36.43 <b>(+84.59%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.80 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>202.50 (n/a)</td><td>169.82 (n/a)</td><td>164.40 (n/a)</td><td>153.30 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.00 (-2.27%)</td><td>0.00 (-0.95%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.56%)</td><td>0.00 <b>(-36.38%)</b></td><td>1029.85 (-1.01%)</td><td>981.13 (+0.80%)</td><td>983.16 (+1.13%)</td><td>952.29 (+1.64%)</td><td>31.77 <b>(-23.87%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1040.36 (n/a)</td><td>973.35 (n/a)</td><td>972.15 (n/a)</td><td>936.91 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.01 (-5.88%)</td><td>0.01 (-1.02%)</td><td>0.01 (-2.50%)</td><td>0.01 (+10.61%)</td><td>0.00 <b>(-62.64%)</b></td><td>1117.85 (-9.63%)</td><td>1055.45 (-0.02%)</td><td>1046.90 (+1.90%)</td><td>1023.17 (+5.69%)</td><td>36.85 <b>(-64.68%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1236.94 (n/a)</td><td>1055.67 (n/a)</td><td>1027.40 (n/a)</td><td>968.09 (n/a)</td><td>104.33 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.97 (+1.45%)</td><td>0.96 (+0.52%)</td><td>0.96 (+0.57%)</td><td>0.94 (+0.01%)</td><td>0.01 <b>(+84.11%)</b></td><td>2230.19 (-0.02%)</td><td>2192.65 (-0.51%)</td><td>2188.24 (-0.56%)</td><td>2155.77 (-1.43%)</td><td>29.60 <b>(+81.09%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2230.56 (n/a)</td><td>2203.80 (n/a)</td><td>2200.64 (n/a)</td><td>2187.00 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.39 (-3.51%)</td><td>0.38 (-2.62%)</td><td>0.38 (-2.29%)</td><td>0.37 (-1.81%)</td><td>0.01 <b>(-32.51%)</b></td><td>1401.49 (+1.86%)</td><td>1376.11 (+2.67%)</td><td>1380.99 (+2.33%)</td><td>1335.55 (+3.65%)</td><td>24.56 <b>(-28.96%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1375.92 (n/a)</td><td>1340.33 (n/a)</td><td>1349.53 (n/a)</td><td>1288.52 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.25 (-3.94%)</td><td>0.25 (-1.54%)</td><td>0.25 (-1.38%)</td><td>0.25 (-0.81%)</td><td>0.00 <b>(-44.45%)</b></td><td>2134.63 (+0.82%)</td><td>2098.25 (+1.55%)</td><td>2101.74 (+1.42%)</td><td>2068.61 (+4.10%)</td><td>29.16 <b>(-41.62%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2117.18 (n/a)</td><td>2066.20 (n/a)</td><td>2072.40 (n/a)</td><td>1987.16 (n/a)</td><td>49.94 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.37 (-3.67%)</td><td>0.36 (-2.58%)</td><td>0.36 (-3.58%)</td><td>0.36 (+0.08%)</td><td>0.00 <b>(-70.89%)</b></td><td>1458.69 (-0.10%)</td><td>1449.16 (+2.61%)</td><td>1450.78 (+3.72%)</td><td>1435.80 (+3.81%)</td><td>9.88 <b>(-70.06%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1460.15 (n/a)</td><td>1412.30 (n/a)</td><td>1398.69 (n/a)</td><td>1383.10 (n/a)</td><td>33.01 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>3.49 (+2.26%)</td><td>2.62 (-11.27%)</td><td>2.66 (-6.31%)</td><td>1.84 <b>(-31.79%)</b></td><td>0.62 <b>(+114.22%)</b></td><td>285.30 <b>(+46.61%)</b></td><td>209.48 (+17.19%)</td><td>197.30 (+6.71%)</td><td>150.30 (-2.21%)</td><td>51.19 <b>(+211.56%)</b></td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.41 (n/a)</td><td>2.95 (n/a)</td><td>2.84 (n/a)</td><td>2.69 (n/a)</td><td>0.29 (n/a)</td><td>194.60 (n/a)</td><td>178.76 (n/a)</td><td>184.90 (n/a)</td><td>153.70 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>5.61 (-12.14%)</td><td>4.59 (-8.99%)</td><td>4.57 (-2.98%)</td><td>3.80 (-4.52%)</td><td>0.66 <b>(-29.14%)</b></td><td>276.00 (+4.74%)</td><td>232.24 (+8.74%)</td><td>229.60 (+3.05%)</td><td>187.00 (+13.82%)</td><td>32.20 (-15.41%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>6.38 (n/a)</td><td>5.04 (n/a)</td><td>4.71 (n/a)</td><td>3.98 (n/a)</td><td>0.93 (n/a)</td><td>263.50 (n/a)</td><td>213.58 (n/a)</td><td>222.80 (n/a)</td><td>164.30 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.72 <b>(+20.32%)</b></td><td>3.12 (+16.02%)</td><td>3.04 (+6.32%)</td><td>2.73 <b>(+32.06%)</b></td><td>0.43 (+8.15%)</td><td>192.20 <b>(-24.30%)</b></td><td>170.32 (-14.26%)</td><td>172.50 (-5.94%)</td><td>141.00 (-16.86%)</td><td>22.57 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (n/a)</td><td>2.69 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.40 (n/a)</td><td>253.90 (n/a)</td><td>198.64 (n/a)</td><td>183.40 (n/a)</td><td>169.60 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.34 <b>(+21.15%)</b></td><td>3.18 (+5.40%)</td><td>3.06 (-4.60%)</td><td>2.36 (+18.00%)</td><td>0.76 <b>(+20.85%)</b></td><td>222.50 (-15.24%)</td><td>172.26 (-5.20%)</td><td>171.30 (+4.83%)</td><td>120.90 (-17.47%)</td><td>38.64 (-18.15%)</td>
</tr>
<tr>
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.58 (n/a)</td><td>3.01 (n/a)</td><td>3.21 (n/a)</td><td>2.00 (n/a)</td><td>0.63 (n/a)</td><td>262.50 (n/a)</td><td>181.70 (n/a)</td><td>163.40 (n/a)</td><td>146.50 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.36 (+7.95%)</td><td>3.26 (+13.04%)</td><td>3.33 <b>(+22.37%)</b></td><td>2.38 (+18.97%)</td><td>0.79 (-14.92%)</td><td>220.70 (-15.96%)</td><td>168.40 (-14.68%)</td><td>157.40 (-18.28%)</td><td>120.30 (-7.39%)</td><td>40.78 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (n/a)</td><td>2.89 (n/a)</td><td>2.72 (n/a)</td><td>2.00 (n/a)</td><td>0.93 (n/a)</td><td>262.60 (n/a)</td><td>197.38 (n/a)</td><td>192.60 (n/a)</td><td>129.90 (n/a)</td><td>62.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>
