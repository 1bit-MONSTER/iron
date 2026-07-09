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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (+12.74%)</td><td>0.07 (+6.70%)</td><td>0.07 (+7.67%)</td><td>0.06 (+7.67%)</td><td>0.01 <b>(+29.00%)</b></td><td>193.10 (-7.16%)</td><td>177.56 (-5.95%)</td><td>184.00 (-7.12%)</td><td>139.90 (-11.34%)</td><td>21.47 (+4.27%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>188.80 (n/a)</td><td>198.10 (n/a)</td><td>157.80 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (+3.84%)</td><td>0.08 (+12.08%)</td><td>0.07 (+15.27%)</td><td>0.07 (+16.56%)</td><td>0.01 <b>(-22.30%)</b></td><td>182.60 (-14.19%)</td><td>165.36 (-11.86%)</td><td>166.50 (-13.28%)</td><td>134.50 (-3.72%)</td><td>19.21 <b>(-36.18%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>187.60 (n/a)</td><td>192.00 (n/a)</td><td>139.70 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (-6.49%)</td><td>0.07 (+3.61%)</td><td>0.07 (+11.38%)</td><td>0.06 (-2.35%)</td><td>0.01 (-14.49%)</td><td>218.20 (+2.44%)</td><td>184.78 (-3.63%)</td><td>177.50 (-10.22%)</td><td>172.30 (+6.89%)</td><td>18.94 (-3.22%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>191.74 (n/a)</td><td>197.70 (n/a)</td><td>161.20 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (-0.08%)</td><td>0.06 (-8.68%)</td><td>0.06 (-8.34%)</td><td>0.04 <b>(-29.43%)</b></td><td>0.01 <b>(+40.77%)</b></td><td>339.00 <b>(+41.66%)</b></td><td>233.36 (+12.96%)</td><td>220.60 (+9.10%)</td><td>172.70 (+0.06%)</td><td>62.55 <b>(+105.74%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>206.58 (n/a)</td><td>202.20 (n/a)</td><td>172.60 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (-1.40%)</td><td>0.03 (-16.78%)</td><td>0.03 <b>(-21.83%)</b></td><td>0.03 <b>(-21.93%)</b></td><td>0.01 <b>(+121.15%)</b></td><td>195.90 <b>(+28.12%)</b></td><td>170.62 <b>(+22.24%)</b></td><td>176.60 <b>(+27.88%)</b></td><td>129.80 (+1.41%)</td><td>25.43 <b>(+179.98%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>152.90 (n/a)</td><td>139.58 (n/a)</td><td>138.10 (n/a)</td><td>128.00 (n/a)</td><td>9.08 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (-8.86%)</td><td>0.03 (-18.90%)</td><td>0.03 <b>(-21.78%)</b></td><td>0.02 <b>(-24.29%)</b></td><td>0.01 <b>(+37.80%)</b></td><td>214.10 <b>(+32.08%)</b></td><td>178.96 <b>(+25.73%)</b></td><td>179.70 <b>(+27.81%)</b></td><td>129.80 (+9.72%)</td><td>33.18 <b>(+99.47%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.10 (n/a)</td><td>142.34 (n/a)</td><td>140.60 (n/a)</td><td>118.30 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (-14.37%)</td><td>0.03 <b>(-20.02%)</b></td><td>0.03 (-19.73%)</td><td>0.02 <b>(-40.19%)</b></td><td>0.01 <b>(+25.28%)</b></td><td>339.70 <b>(+67.18%)</b></td><td>204.10 <b>(+33.43%)</b></td><td>183.60 <b>(+24.56%)</b></td><td>134.70 (+16.83%)</td><td>79.97 <b>(+152.68%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>152.96 (n/a)</td><td>147.40 (n/a)</td><td>115.30 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (+3.37%)</td><td>0.03 (-3.88%)</td><td>0.03 (-8.10%)</td><td>0.02 (-11.19%)</td><td>0.01 <b>(+33.10%)</b></td><td>224.30 (+12.60%)</td><td>176.26 (+5.42%)</td><td>177.90 (+8.81%)</td><td>133.50 (-3.26%)</td><td>32.84 <b>(+44.12%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.20 (n/a)</td><td>167.20 (n/a)</td><td>163.50 (n/a)</td><td>138.00 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (-8.77%)</td><td>0.03 (-12.41%)</td><td>0.04 (-0.77%)</td><td>0.03 <b>(-27.91%)</b></td><td>0.01 <b>(+112.81%)</b></td><td>201.00 <b>(+38.72%)</b></td><td>159.82 (+17.79%)</td><td>139.50 (+0.79%)</td><td>129.30 (+9.67%)</td><td>34.97 <b>(+232.99%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>144.90 (n/a)</td><td>135.68 (n/a)</td><td>138.40 (n/a)</td><td>117.90 (n/a)</td><td>10.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.03 (-12.93%)</td><td>0.03 <b>(-21.56%)</b></td><td>0.03 <b>(-23.48%)</b></td><td>0.02 (-19.50%)</td><td>0.00 (+9.48%)</td><td>240.20 <b>(+24.20%)</b></td><td>204.66 <b>(+28.51%)</b></td><td>205.50 <b>(+30.64%)</b></td><td>157.10 (+14.84%)</td><td>31.58 <b>(+50.70%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>159.26 (n/a)</td><td>157.30 (n/a)</td><td>136.80 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (-17.48%)</td><td>0.03 (-13.38%)</td><td>0.03 (-16.93%)</td><td>0.02 (-14.66%)</td><td>0.00 <b>(-33.48%)</b></td><td>222.80 (+17.20%)</td><td>182.02 (+14.32%)</td><td>179.30 <b>(+20.42%)</b></td><td>149.70 <b>(+21.21%)</b></td><td>26.30 (-7.53%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>159.22 (n/a)</td><td>148.90 (n/a)</td><td>123.50 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.03 (-11.50%)</td><td>0.02 (-13.14%)</td><td>0.02 (-12.62%)</td><td>0.02 (-13.15%)</td><td>0.00 (+5.49%)</td><td>238.90 (+15.13%)</td><td>215.56 (+15.40%)</td><td>214.40 (+14.47%)</td><td>187.80 (+13.00%)</td><td>20.23 <b>(+37.88%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.50 (n/a)</td><td>186.80 (n/a)</td><td>187.30 (n/a)</td><td>166.20 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>187.30 (n/a)</td><td>175.00 (n/a)</td><td>159.30 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>170.78 (n/a)</td><td>186.20 (n/a)</td><td>143.00 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>176.94 (n/a)</td><td>184.50 (n/a)</td><td>125.70 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>255.80 (n/a)</td><td>216.04 (n/a)</td><td>211.40 (n/a)</td><td>167.00 (n/a)</td><td>34.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>171.68 (n/a)</td><td>161.50 (n/a)</td><td>147.80 (n/a)</td><td>24.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>290.80 (n/a)</td><td>230.22 (n/a)</td><td>216.70 (n/a)</td><td>179.80 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>175.50 (n/a)</td><td>178.20 (n/a)</td><td>139.40 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>267.50 (n/a)</td><td>217.76 (n/a)</td><td>230.00 (n/a)</td><td>168.40 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>162.56 (n/a)</td><td>171.80 (n/a)</td><td>112.80 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>167.08 (n/a)</td><td>164.00 (n/a)</td><td>141.50 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.00 (n/a)</td><td>162.20 (n/a)</td><td>166.20 (n/a)</td><td>144.40 (n/a)</td><td>12.76 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>156.14 (n/a)</td><td>160.10 (n/a)</td><td>130.10 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.90 (n/a)</td><td>149.10 (n/a)</td><td>148.10 (n/a)</td><td>133.90 (n/a)</td><td>11.84 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>177.38 (n/a)</td><td>174.70 (n/a)</td><td>145.80 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>184.60 (n/a)</td><td>181.50 (n/a)</td><td>167.50 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>200.18 (n/a)</td><td>209.00 (n/a)</td><td>175.20 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.49 (-1.66%)</td><td>4.16 (+4.73%)</td><td>4.10 (-0.30%)</td><td>3.88 <b>(+21.13%)</b></td><td>0.22 <b>(-56.99%)</b></td><td>2421.90 (-17.44%)</td><td>2264.96 (-5.70%)</td><td>2291.90 (+0.30%)</td><td>2092.70 (+1.68%)</td><td>120.03 <b>(-64.52%)</b></td><td>1767.72 (-1.66%)</td><td>1637.02 (+4.73%)</td><td>1614.12 (-0.30%)</td><td>1527.45 <b>(+21.13%)</b></td><td>87.95 <b>(-56.99%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>4.57 (n/a)</td><td>3.97 (n/a)</td><td>4.12 (n/a)</td><td>3.21 (n/a)</td><td>0.52 (n/a)</td><td>2933.60 (n/a)</td><td>2401.82 (n/a)</td><td>2285.00 (n/a)</td><td>2058.10 (n/a)</td><td>338.28 (n/a)</td><td>1797.51 (n/a)</td><td>1563.15 (n/a)</td><td>1619.01 (n/a)</td><td>1261.03 (n/a)</td><td>204.48 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.13 (-9.29%)</td><td>0.81 (-10.85%)</td><td>0.67 <b>(-20.88%)</b></td><td>0.60 (-11.60%)</td><td>0.26 (+7.60%)</td><td>366.50 (+13.12%)</td><td>293.04 (+14.76%)</td><td>329.80 <b>(+26.41%)</b></td><td>194.90 (+10.24%)</td><td>83.90 <b>(+33.85%)</b></td><td>48.41 (-9.29%)</td><td>34.71 (-10.85%)</td><td>28.62 <b>(-20.88%)</b></td><td>25.75 (-11.60%)</td><td>11.00 (+7.60%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>1.25 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.68 (n/a)</td><td>0.24 (n/a)</td><td>324.00 (n/a)</td><td>255.36 (n/a)</td><td>260.90 (n/a)</td><td>176.80 (n/a)</td><td>62.68 (n/a)</td><td>53.37 (n/a)</td><td>38.94 (n/a)</td><td>36.17 (n/a)</td><td>29.13 (n/a)</td><td>10.22 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.13 (-11.43%)</td><td>0.89 (-5.99%)</td><td>0.91 (-8.25%)</td><td>0.57 (-10.05%)</td><td>0.22 <b>(-23.59%)</b></td><td>386.80 (+11.18%)</td><td>261.80 (+4.13%)</td><td>242.20 (+9.00%)</td><td>196.10 (+12.90%)</td><td>75.94 (-4.72%)</td><td>48.12 (-11.43%)</td><td>38.16 (-5.99%)</td><td>38.97 (-8.25%)</td><td>24.40 (-10.05%)</td><td>9.30 <b>(-23.59%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>1.27 (n/a)</td><td>0.95 (n/a)</td><td>1.00 (n/a)</td><td>0.64 (n/a)</td><td>0.29 (n/a)</td><td>347.90 (n/a)</td><td>251.42 (n/a)</td><td>222.20 (n/a)</td><td>173.70 (n/a)</td><td>79.70 (n/a)</td><td>54.33 (n/a)</td><td>40.59 (n/a)</td><td>42.47 (n/a)</td><td>27.12 (n/a)</td><td>12.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.52 (-0.11%)</td><td>0.52 (-0.25%)</td><td>0.52 (-0.26%)</td><td>0.51 (-0.13%)</td><td>0.00 (+8.08%)</td><td>48892.60 (+0.13%)</td><td>48787.46 (+0.25%)</td><td>48757.60 (+0.26%)</td><td>48673.40 (+0.11%)</td><td>99.46 (+8.40%)</td><td>352.96 (-0.11%)</td><td>352.14 (-0.25%)</td><td>352.35 (-0.26%)</td><td>351.38 (-0.13%)</td><td>0.72 (+8.08%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48831.30 (n/a)</td><td>48667.38 (n/a)</td><td>48629.40 (n/a)</td><td>48619.00 (n/a)</td><td>91.75 (n/a)</td><td>353.36 (n/a)</td><td>353.01 (n/a)</td><td>353.28 (n/a)</td><td>351.82 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.88 (-1.07%)</td><td>0.88 (-0.09%)</td><td>0.88 (+0.48%)</td><td>0.87 (+0.23%)</td><td>0.00 <b>(-70.94%)</b></td><td>28819.90 (-0.23%)</td><td>28699.84 (+0.08%)</td><td>28666.20 (-0.48%)</td><td>28631.40 (+1.09%)</td><td>75.24 <b>(-70.71%)</b></td><td>600.04 (-1.07%)</td><td>598.61 (-0.09%)</td><td>599.31 (+0.48%)</td><td>596.11 (+0.23%)</td><td>1.57 <b>(-70.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28886.70 (n/a)</td><td>28675.96 (n/a)</td><td>28805.00 (n/a)</td><td>28323.90 (n/a)</td><td>256.89 (n/a)</td><td>606.55 (n/a)</td><td>599.14 (n/a)</td><td>596.42 (n/a)</td><td>594.73 (n/a)</td><td>5.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>3.29 (+1.12%)</td><td>3.21 (+1.82%)</td><td>3.19 (+1.49%)</td><td>3.18 (+3.34%)</td><td>0.05 <b>(-28.86%)</b></td><td>7911.60 (-3.23%)</td><td>7835.22 (-1.80%)</td><td>7890.80 (-1.47%)</td><td>7647.30 (-1.11%)</td><td>108.82 <b>(-31.84%)</b></td><td>2246.52 (+1.12%)</td><td>2192.99 (+1.82%)</td><td>2177.21 (+1.49%)</td><td>2171.47 (+3.34%)</td><td>30.95 <b>(-28.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.25 (n/a)</td><td>3.16 (n/a)</td><td>3.14 (n/a)</td><td>3.08 (n/a)</td><td>0.06 (n/a)</td><td>8175.60 (n/a)</td><td>7978.94 (n/a)</td><td>8008.70 (n/a)</td><td>7733.30 (n/a)</td><td>159.65 (n/a)</td><td>2221.54 (n/a)</td><td>2153.85 (n/a)</td><td>2145.15 (n/a)</td><td>2101.37 (n/a)</td><td>43.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.12 (+6.57%)</td><td>3.47 (+9.10%)</td><td>3.48 (+13.46%)</td><td>2.95 (+6.35%)</td><td>0.49 (+17.49%)</td><td>2730.90 (-5.97%)</td><td>2356.86 (-8.04%)</td><td>2318.50 (-11.86%)</td><td>1954.70 (-6.16%)</td><td>327.04 (+7.15%)</td><td>1081.47 (+6.57%)</td><td>911.08 (+9.10%)</td><td>911.77 (+13.46%)</td><td>774.07 (+6.35%)</td><td>127.99 (+17.49%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.87 (n/a)</td><td>3.18 (n/a)</td><td>3.06 (n/a)</td><td>2.78 (n/a)</td><td>0.42 (n/a)</td><td>2904.30 (n/a)</td><td>2563.00 (n/a)</td><td>2630.60 (n/a)</td><td>2083.10 (n/a)</td><td>305.21 (n/a)</td><td>1014.82 (n/a)</td><td>835.12 (n/a)</td><td>803.58 (n/a)</td><td>727.87 (n/a)</td><td>108.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.34 <b>(-32.13%)</b></td><td>0.31 (-15.25%)</td><td>0.31 (-5.17%)</td><td>0.27 (-10.94%)</td><td>0.03 <b>(-64.76%)</b></td><td>4696.40 (+12.28%)</td><td>4066.64 (+14.99%)</td><td>3968.20 (+5.45%)</td><td>3635.10 <b>(+47.33%)</b></td><td>398.40 <b>(-38.47%)</b></td><td>18.46 <b>(-32.13%)</b></td><td>16.62 (-15.25%)</td><td>16.91 (-5.17%)</td><td>14.29 (-10.94%)</td><td>1.55 <b>(-64.76%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>4182.80 (n/a)</td><td>3536.54 (n/a)</td><td>3763.20 (n/a)</td><td>2467.30 (n/a)</td><td>647.45 (n/a)</td><td>27.20 (n/a)</td><td>19.61 (n/a)</td><td>17.83 (n/a)</td><td>16.04 (n/a)</td><td>4.39 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.79 <b>(-25.60%)</b></td><td>4.22 (-8.40%)</td><td>4.58 (-4.49%)</td><td>3.45 (+3.62%)</td><td>0.64 <b>(-50.91%)</b></td><td>1928.20 (-3.49%)</td><td>1607.70 (+4.50%)</td><td>1452.90 (+4.70%)</td><td>1387.80 <b>(+34.42%)</b></td><td>257.09 <b>(-39.57%)</b></td><td>1480.95 <b>(-25.60%)</b></td><td>1303.54 (-8.40%)</td><td>1414.57 (-4.49%)</td><td>1065.85 (+3.62%)</td><td>197.03 <b>(-50.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>6.44 (n/a)</td><td>4.61 (n/a)</td><td>4.79 (n/a)</td><td>3.33 (n/a)</td><td>1.30 (n/a)</td><td>1998.00 (n/a)</td><td>1538.52 (n/a)</td><td>1387.70 (n/a)</td><td>1032.40 (n/a)</td><td>425.43 (n/a)</td><td>1990.63 (n/a)</td><td>1423.10 (n/a)</td><td>1481.04 (n/a)</td><td>1028.63 (n/a)</td><td>401.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.26 (+5.80%)</td><td>0.22 (+11.18%)</td><td>0.23 <b>(+31.87%)</b></td><td>0.14 (-2.44%)</td><td>0.04 (+1.93%)</td><td>0.26 (+5.80%)</td><td>0.21 (+11.18%)</td><td>0.22 <b>(+31.87%)</b></td><td>0.14 (-2.44%)</td><td>0.04 (+1.93%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>13.45 (+0.33%)</td><td>12.57 (-1.56%)</td><td>13.03 (+1.09%)</td><td>10.90 (-8.01%)</td><td>1.03 <b>(+62.35%)</b></td><td>13.44 (+0.33%)</td><td>12.56 (-1.56%)</td><td>13.03 (+1.09%)</td><td>10.90 (-8.01%)</td><td>1.03 <b>(+62.35%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>13.41 (n/a)</td><td>12.77 (n/a)</td><td>12.89 (n/a)</td><td>11.85 (n/a)</td><td>0.64 (n/a)</td><td>13.40 (n/a)</td><td>12.76 (n/a)</td><td>12.89 (n/a)</td><td>11.85 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>24.80 (+1.25%)</td><td>23.49 (+0.77%)</td><td>24.12 (+0.46%)</td><td>20.43 (-1.67%)</td><td>1.74 (+15.27%)</td><td>24.78 (+1.25%)</td><td>23.48 (+0.77%)</td><td>24.10 (+0.46%)</td><td>20.42 (-1.67%)</td><td>1.74 (+15.27%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>24.49 (n/a)</td><td>23.31 (n/a)</td><td>24.00 (n/a)</td><td>20.78 (n/a)</td><td>1.51 (n/a)</td><td>24.47 (n/a)</td><td>23.30 (n/a)</td><td>23.99 (n/a)</td><td>20.76 (n/a)</td><td>1.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>40.87 (+1.28%)</td><td>39.39 (+0.29%)</td><td>39.38 (+1.01%)</td><td>37.87 (-1.64%)</td><td>1.07 <b>(+44.94%)</b></td><td>40.84 (+1.28%)</td><td>39.36 (+0.29%)</td><td>39.36 (+1.01%)</td><td>37.84 (-1.64%)</td><td>1.07 <b>(+44.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>40.35 (n/a)</td><td>39.27 (n/a)</td><td>38.99 (n/a)</td><td>38.50 (n/a)</td><td>0.74 (n/a)</td><td>40.32 (n/a)</td><td>39.25 (n/a)</td><td>38.97 (n/a)</td><td>38.47 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>44.93 (+3.21%)</td><td>43.01 (+1.78%)</td><td>42.52 (-0.81%)</td><td>41.93 (+5.35%)</td><td>1.16 <b>(-21.45%)</b></td><td>44.90 (+3.21%)</td><td>42.99 (+1.78%)</td><td>42.49 (-0.81%)</td><td>41.91 (+5.35%)</td><td>1.16 <b>(-21.45%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>43.53 (n/a)</td><td>42.26 (n/a)</td><td>42.87 (n/a)</td><td>39.80 (n/a)</td><td>1.47 (n/a)</td><td>43.50 (n/a)</td><td>42.24 (n/a)</td><td>42.84 (n/a)</td><td>39.78 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>13.33 (+0.68%)</td><td>12.67 (-1.13%)</td><td>13.21 (+0.37%)</td><td>11.20 (-6.98%)</td><td>0.90 <b>(+63.89%)</b></td><td>13.32 (+0.68%)</td><td>12.67 (-1.13%)</td><td>13.21 (+0.37%)</td><td>11.19 (-6.98%)</td><td>0.90 <b>(+63.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>13.24 (n/a)</td><td>12.82 (n/a)</td><td>13.17 (n/a)</td><td>12.04 (n/a)</td><td>0.55 (n/a)</td><td>13.23 (n/a)</td><td>12.81 (n/a)</td><td>13.16 (n/a)</td><td>12.03 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>24.95 (-0.62%)</td><td>24.33 (+5.16%)</td><td>24.17 (+0.03%)</td><td>23.99 <b>(+34.09%)</b></td><td>0.37 <b>(-87.40%)</b></td><td>24.93 (-0.62%)</td><td>24.31 (+5.16%)</td><td>24.15 (+0.03%)</td><td>23.98 <b>(+34.09%)</b></td><td>0.37 <b>(-87.40%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>25.10 (n/a)</td><td>23.13 (n/a)</td><td>24.16 (n/a)</td><td>17.89 (n/a)</td><td>2.96 (n/a)</td><td>25.09 (n/a)</td><td>23.12 (n/a)</td><td>24.15 (n/a)</td><td>17.88 (n/a)</td><td>2.96 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>41.01 (-0.38%)</td><td>39.70 (+0.02%)</td><td>40.60 (+1.71%)</td><td>37.30 (-3.23%)</td><td>1.63 <b>(+44.89%)</b></td><td>40.99 (-0.38%)</td><td>39.68 (+0.02%)</td><td>40.58 (+1.71%)</td><td>37.28 (-3.23%)</td><td>1.63 <b>(+44.89%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>41.17 (n/a)</td><td>39.69 (n/a)</td><td>39.92 (n/a)</td><td>38.55 (n/a)</td><td>1.12 (n/a)</td><td>41.15 (n/a)</td><td>39.67 (n/a)</td><td>39.89 (n/a)</td><td>38.53 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>44.68 (-2.38%)</td><td>42.66 (-0.33%)</td><td>42.30 (-1.60%)</td><td>41.13 (+2.35%)</td><td>1.45 <b>(-31.19%)</b></td><td>44.65 (-2.38%)</td><td>42.63 (-0.33%)</td><td>42.28 (-1.60%)</td><td>41.10 (+2.35%)</td><td>1.45 <b>(-31.19%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>45.77 (n/a)</td><td>42.80 (n/a)</td><td>42.99 (n/a)</td><td>40.18 (n/a)</td><td>2.11 (n/a)</td><td>45.74 (n/a)</td><td>42.78 (n/a)</td><td>42.96 (n/a)</td><td>40.16 (n/a)</td><td>2.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.70 (n/a)</td><td>172.04 (n/a)</td><td>173.40 (n/a)</td><td>146.20 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.40 (n/a)</td><td>194.44 (n/a)</td><td>197.10 (n/a)</td><td>130.20 (n/a)</td><td>66.27 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.20 (n/a)</td><td>155.40 (n/a)</td><td>153.70 (n/a)</td><td>128.40 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>175.08 (n/a)</td><td>175.50 (n/a)</td><td>156.10 (n/a)</td><td>14.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>171.76 (n/a)</td><td>178.30 (n/a)</td><td>114.20 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>156.00 (n/a)</td><td>158.50 (n/a)</td><td>136.40 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>172.30 (n/a)</td><td>173.30 (n/a)</td><td>147.90 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>197.92 (n/a)</td><td>180.30 (n/a)</td><td>171.80 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (+1.26%)</td><td>0.06 (+3.99%)</td><td>0.05 (-2.41%)</td><td>0.05 <b>(+28.95%)</b></td><td>0.01 (-19.69%)</td><td>176.50 <b>(-22.49%)</b></td><td>149.04 (-5.99%)</td><td>152.80 (+2.48%)</td><td>119.30 (-1.24%)</td><td>23.51 <b>(-41.92%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>158.54 (n/a)</td><td>149.10 (n/a)</td><td>120.80 (n/a)</td><td>40.48 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 <b>(+23.86%)</b></td><td>0.04 (+4.70%)</td><td>0.04 (-3.72%)</td><td>0.04 (+15.70%)</td><td>0.01 <b>(+44.15%)</b></td><td>220.50 (-13.60%)</td><td>199.38 (-3.59%)</td><td>212.20 (+3.87%)</td><td>138.50 (-19.29%)</td><td>34.53 (+0.05%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.20 (n/a)</td><td>206.80 (n/a)</td><td>204.30 (n/a)</td><td>171.60 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (-6.89%)</td><td>0.05 (-3.65%)</td><td>0.05 (+6.25%)</td><td>0.04 <b>(-22.36%)</b></td><td>0.01 <b>(+32.17%)</b></td><td>233.60 <b>(+28.78%)</b></td><td>165.20 (+6.07%)</td><td>150.70 (-5.87%)</td><td>136.50 (+7.40%)</td><td>39.09 <b>(+92.56%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>155.74 (n/a)</td><td>160.10 (n/a)</td><td>127.10 (n/a)</td><td>20.30 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 <b>(-33.10%)</b></td><td>0.04 <b>(-34.24%)</b></td><td>0.04 <b>(-33.86%)</b></td><td>0.02 <b>(-49.52%)</b></td><td>0.01 (-7.84%)</td><td>349.00 <b>(+98.07%)</b></td><td>219.00 <b>(+58.86%)</b></td><td>200.80 <b>(+51.20%)</b></td><td>160.60 <b>(+49.53%)</b></td><td>74.97 <b>(+185.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>137.86 (n/a)</td><td>132.80 (n/a)</td><td>107.40 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-15.68%)</td><td>0.05 (-10.69%)</td><td>0.05 (-10.51%)</td><td>0.04 (-4.98%)</td><td>0.01 <b>(-32.90%)</b></td><td>187.80 (+5.21%)</td><td>167.92 (+11.18%)</td><td>169.30 (+11.75%)</td><td>149.00 (+18.54%)</td><td>17.49 (-16.68%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>151.04 (n/a)</td><td>151.50 (n/a)</td><td>125.70 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (-0.07%)</td><td>0.05 (+6.47%)</td><td>0.06 (+19.11%)</td><td>0.05 <b>(+22.64%)</b></td><td>0.01 <b>(-37.82%)</b></td><td>171.70 (-18.43%)</td><td>151.02 (-8.41%)</td><td>144.30 (-16.06%)</td><td>127.80 (+0.08%)</td><td>19.38 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>164.88 (n/a)</td><td>171.90 (n/a)</td><td>127.70 (n/a)</td><td>35.65 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-9.03%)</td><td>0.05 (-1.81%)</td><td>0.05 (+4.28%)</td><td>0.04 (-7.62%)</td><td>0.01 <b>(-22.05%)</b></td><td>207.90 (+8.22%)</td><td>175.92 (+1.48%)</td><td>172.30 (-4.12%)</td><td>152.00 (+9.91%)</td><td>20.26 (-4.39%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>173.36 (n/a)</td><td>179.70 (n/a)</td><td>138.30 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-8.35%)</td><td>0.05 (-3.14%)</td><td>0.05 (+0.38%)</td><td>0.04 (+0.38%)</td><td>0.01 (-7.96%)</td><td>194.70 (-0.36%)</td><td>168.70 (+3.14%)</td><td>160.50 (-0.37%)</td><td>151.00 (+9.10%)</td><td>20.28 (-1.53%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>163.56 (n/a)</td><td>161.10 (n/a)</td><td>138.40 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.21 (+0.02%)</td><td>0.20 (+0.01%)</td><td>0.20 (-0.07%)</td><td>0.20 (+0.07%)</td><td>0.00 (-18.47%)</td><td>40961.20 (-0.07%)</td><td>40924.92 (-0.01%)</td><td>40941.50 (+0.07%)</td><td>40859.60 (-0.02%)</td><td>41.66 (-18.49%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40988.20 (n/a)</td><td>40927.74 (n/a)</td><td>40913.30 (n/a)</td><td>40866.90 (n/a)</td><td>51.11 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (-4.97%)</td><td>0.05 (-2.26%)</td><td>0.05 (-2.93%)</td><td>0.04 (+5.25%)</td><td>0.01 <b>(-27.32%)</b></td><td>205.10 (-4.96%)</td><td>159.30 (+0.34%)</td><td>156.60 (+3.03%)</td><td>129.80 (+5.27%)</td><td>28.86 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>158.76 (n/a)</td><td>152.00 (n/a)</td><td>123.30 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.08 (-17.50%)</td><td>0.07 (-16.65%)</td><td>0.07 (-18.77%)</td><td>0.06 (-15.53%)</td><td>0.01 <b>(-21.38%)</b></td><td>207.00 (+18.42%)</td><td>174.74 (+19.83%)</td><td>174.10 <b>(+23.13%)</b></td><td>151.40 <b>(+21.22%)</b></td><td>20.61 (+12.45%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>145.82 (n/a)</td><td>141.40 (n/a)</td><td>124.90 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (-9.98%)</td><td>0.05 (-5.54%)</td><td>0.05 (-18.08%)</td><td>0.04 <b>(+55.20%)</b></td><td>0.01 <b>(-59.66%)</b></td><td>193.00 <b>(-35.58%)</b></td><td>171.02 (-2.80%)</td><td>177.60 <b>(+22.06%)</b></td><td>143.10 (+11.02%)</td><td>20.18 <b>(-71.75%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.60 (n/a)</td><td>175.94 (n/a)</td><td>145.50 (n/a)</td><td>128.90 (n/a)</td><td>71.43 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (-16.53%)</td><td>0.06 (-14.29%)</td><td>0.06 (-17.28%)</td><td>0.05 <b>(-22.78%)</b></td><td>0.01 (-18.17%)</td><td>219.10 <b>(+29.49%)</b></td><td>167.90 (+16.74%)</td><td>160.10 <b>(+20.92%)</b></td><td>144.40 (+19.73%)</td><td>29.72 <b>(+26.43%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>169.20 (n/a)</td><td>143.82 (n/a)</td><td>132.40 (n/a)</td><td>120.60 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (-14.11%)</td><td>0.05 (-6.97%)</td><td>0.05 (-5.48%)</td><td>0.05 (+7.08%)</td><td>0.01 <b>(-38.79%)</b></td><td>180.30 (-6.63%)</td><td>154.84 (+5.48%)</td><td>158.80 (+5.80%)</td><td>134.80 (+16.41%)</td><td>19.65 <b>(-34.93%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>146.80 (n/a)</td><td>150.10 (n/a)</td><td>115.80 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (-18.29%)</td><td>0.05 (-19.41%)</td><td>0.05 (-10.23%)</td><td>0.04 <b>(-21.63%)</b></td><td>0.01 (-14.28%)</td><td>271.90 <b>(+27.59%)</b></td><td>204.38 <b>(+24.94%)</b></td><td>190.80 (+11.38%)</td><td>150.30 <b>(+22.39%)</b></td><td>49.60 <b>(+37.83%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>163.58 (n/a)</td><td>171.30 (n/a)</td><td>122.80 (n/a)</td><td>35.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 <b>(-28.89%)</b></td><td>0.04 (-15.73%)</td><td>0.04 (-4.92%)</td><td>0.04 (-7.78%)</td><td>0.00 <b>(-64.10%)</b></td><td>220.80 (+8.45%)</td><td>194.82 (+15.61%)</td><td>187.50 (+5.16%)</td><td>178.40 <b>(+40.69%)</b></td><td>18.02 <b>(-45.22%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>168.52 (n/a)</td><td>178.30 (n/a)</td><td>126.80 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (+6.81%)</td><td>0.05 (+3.95%)</td><td>0.05 (+0.10%)</td><td>0.04 (+14.35%)</td><td>0.01 (-8.77%)</td><td>222.40 (-12.54%)</td><td>175.88 (-4.80%)</td><td>170.20 (-0.12%)</td><td>146.50 (-6.39%)</td><td>30.09 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>254.30 (n/a)</td><td>184.74 (n/a)</td><td>170.40 (n/a)</td><td>156.50 (n/a)</td><td>40.55 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 <b>(-31.46%)</b></td><td>0.05 (-11.50%)</td><td>0.04 (+0.59%)</td><td>0.04 <b>(+25.33%)</b></td><td>0.00 <b>(-86.68%)</b></td><td>192.20 <b>(-20.22%)</b></td><td>182.12 (+4.69%)</td><td>184.00 (-0.59%)</td><td>169.70 <b>(+45.92%)</b></td><td>8.46 <b>(-83.93%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>240.90 (n/a)</td><td>173.96 (n/a)</td><td>185.10 (n/a)</td><td>116.30 (n/a)</td><td>52.63 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (+1.84%)</td><td>0.06 (-1.15%)</td><td>0.05 (-10.29%)</td><td>0.04 (-3.76%)</td><td>0.01 (-2.23%)</td><td>211.70 (+3.93%)</td><td>168.94 (+1.00%)</td><td>169.90 (+11.48%)</td><td>130.80 (-1.80%)</td><td>29.52 (-3.20%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>167.26 (n/a)</td><td>152.40 (n/a)</td><td>133.20 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (+5.25%)</td><td>0.04 (+1.83%)</td><td>0.04 (-0.93%)</td><td>0.04 (-3.80%)</td><td>0.01 <b>(+38.91%)</b></td><td>231.90 (+3.94%)</td><td>188.90 (-0.19%)</td><td>189.60 (+0.90%)</td><td>143.10 (-4.98%)</td><td>38.17 <b>(+39.23%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>189.26 (n/a)</td><td>187.90 (n/a)</td><td>150.60 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-8.16%)</td><td>0.04 (-9.19%)</td><td>0.04 (-16.20%)</td><td>0.03 (+15.97%)</td><td>0.01 <b>(-26.45%)</b></td><td>267.10 (-13.76%)</td><td>219.00 (+6.96%)</td><td>228.10 (+19.36%)</td><td>172.00 (+8.86%)</td><td>41.66 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.70 (n/a)</td><td>204.74 (n/a)</td><td>191.10 (n/a)</td><td>158.00 (n/a)</td><td>61.94 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-2.24%)</td><td>0.04 (-6.03%)</td><td>0.04 (-12.83%)</td><td>0.04 (-8.41%)</td><td>0.01 (+8.51%)</td><td>228.30 (+9.18%)</td><td>189.12 (+6.84%)</td><td>193.60 (+14.69%)</td><td>158.90 (+2.25%)</td><td>28.28 <b>(+20.00%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>177.02 (n/a)</td><td>168.80 (n/a)</td><td>155.40 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (-11.67%)</td><td>0.04 (-8.79%)</td><td>0.04 <b>(-20.08%)</b></td><td>0.04 (+2.46%)</td><td>0.01 <b>(-42.72%)</b></td><td>226.50 (-2.37%)</td><td>204.14 (+7.46%)</td><td>215.40 <b>(+25.09%)</b></td><td>173.80 (+13.22%)</td><td>23.42 <b>(-38.60%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>189.96 (n/a)</td><td>172.20 (n/a)</td><td>153.50 (n/a)</td><td>38.14 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (+17.43%)</td><td>0.04 (+10.95%)</td><td>0.04 (+1.22%)</td><td>0.03 <b>(+27.56%)</b></td><td>0.01 (-13.54%)</td><td>263.70 <b>(-21.61%)</b></td><td>212.66 (-12.86%)</td><td>206.60 (-1.24%)</td><td>153.80 (-14.84%)</td><td>41.38 <b>(-43.03%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>336.40 (n/a)</td><td>244.04 (n/a)</td><td>209.20 (n/a)</td><td>180.60 (n/a)</td><td>72.64 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.70 (+18.95%)</td><td>0.56 (+2.89%)</td><td>0.53 (-7.10%)</td><td>0.43 (-9.29%)</td><td>0.10 <b>(+86.53%)</b></td><td>231.20 (+10.20%)</td><td>181.32 (-1.02%)</td><td>184.30 (+7.65%)</td><td>139.70 (-15.94%)</td><td>33.57 <b>(+73.08%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.59 (n/a)</td><td>0.54 (n/a)</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>209.80 (n/a)</td><td>183.18 (n/a)</td><td>171.20 (n/a)</td><td>166.20 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.71 (+7.22%)</td><td>0.64 (+4.17%)</td><td>0.62 (+1.69%)</td><td>0.60 (+7.71%)</td><td>0.05 (-0.33%)</td><td>162.50 (-7.14%)</td><td>154.46 (-4.04%)</td><td>158.60 (-1.61%)</td><td>137.80 (-6.77%)</td><td>10.45 (-12.86%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.05 (n/a)</td><td>175.00 (n/a)</td><td>160.96 (n/a)</td><td>161.20 (n/a)</td><td>147.80 (n/a)</td><td>11.99 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.64 (+1.29%)</td><td>0.61 (+5.50%)</td><td>0.61 (+7.44%)</td><td>0.55 (+8.88%)</td><td>0.03 <b>(-29.61%)</b></td><td>177.50 (-8.13%)</td><td>162.20 (-5.48%)</td><td>161.00 (-6.94%)</td><td>153.30 (-1.29%)</td><td>9.19 <b>(-35.65%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.05 (n/a)</td><td>193.20 (n/a)</td><td>171.60 (n/a)</td><td>173.00 (n/a)</td><td>155.30 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.67 (-0.81%)</td><td>0.58 (-1.55%)</td><td>0.56 (-2.59%)</td><td>0.54 (+1.94%)</td><td>0.05 (-3.81%)</td><td>182.10 (-1.94%)</td><td>170.82 (+1.50%)</td><td>176.20 (+2.62%)</td><td>146.30 (+0.83%)</td><td>14.64 (-4.79%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.68 (n/a)</td><td>0.59 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.06 (n/a)</td><td>185.70 (n/a)</td><td>168.30 (n/a)</td><td>171.70 (n/a)</td><td>145.10 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.53 <b>(+20.10%)</b></td><td>0.44 (+8.16%)</td><td>0.41 (+3.42%)</td><td>0.41 (+8.13%)</td><td>0.05 <b>(+78.86%)</b></td><td>181.30 (-7.50%)</td><td>168.88 (-7.00%)</td><td>178.10 (-3.31%)</td><td>140.10 (-16.71%)</td><td>17.53 <b>(+39.30%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.03 (n/a)</td><td>196.00 (n/a)</td><td>181.60 (n/a)</td><td>184.20 (n/a)</td><td>168.20 (n/a)</td><td>12.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.51 (+16.53%)</td><td>0.44 (+6.48%)</td><td>0.44 (+6.14%)</td><td>0.36 (-2.26%)</td><td>0.06 <b>(+124.30%)</b></td><td>202.20 (+2.33%)</td><td>170.72 (-5.12%)</td><td>168.30 (-5.77%)</td><td>144.70 (-14.18%)</td><td>21.99 <b>(+96.71%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.02 (n/a)</td><td>197.60 (n/a)</td><td>179.94 (n/a)</td><td>178.60 (n/a)</td><td>168.60 (n/a)</td><td>11.18 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.59 (+9.48%)</td><td>0.38 (-15.02%)</td><td>0.37 (-14.51%)</td><td>0.20 <b>(-41.58%)</b></td><td>0.14 <b>(+63.47%)</b></td><td>367.90 <b>(+71.12%)</b></td><td>219.50 <b>(+28.88%)</b></td><td>200.50 (+16.98%)</td><td>124.30 (-8.67%)</td><td>90.62 <b>(+169.87%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>215.00 (n/a)</td><td>170.32 (n/a)</td><td>171.40 (n/a)</td><td>136.10 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.42 (+5.38%)</td><td>0.40 (+2.82%)</td><td>0.41 (+5.11%)</td><td>0.35 (-2.46%)</td><td>0.03 <b>(+72.01%)</b></td><td>210.50 (+2.53%)</td><td>186.92 (-2.45%)</td><td>180.70 (-4.89%)</td><td>174.10 (-5.07%)</td><td>14.39 <b>(+68.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.02 (n/a)</td><td>205.30 (n/a)</td><td>191.62 (n/a)</td><td>190.00 (n/a)</td><td>183.40 (n/a)</td><td>8.57 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.01 (+4.12%)</td><td>0.79 (-6.74%)</td><td>0.76 (-14.02%)</td><td>0.71 (+3.74%)</td><td>0.13 (+14.86%)</td><td>185.70 (-3.63%)</td><td>169.28 (+7.53%)</td><td>173.20 (+16.32%)</td><td>130.20 (-3.91%)</td><td>22.83 (+3.19%)</td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.97 (n/a)</td><td>0.84 (n/a)</td><td>0.88 (n/a)</td><td>0.68 (n/a)</td><td>0.11 (n/a)</td><td>192.70 (n/a)</td><td>157.42 (n/a)</td><td>148.90 (n/a)</td><td>135.50 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.96 <b>(+20.84%)</b></td><td>0.69 (-3.85%)</td><td>0.66 (-8.45%)</td><td>0.57 (-14.24%)</td><td>0.15 <b>(+227.96%)</b></td><td>231.70 (+16.61%)</td><td>195.54 (+7.18%)</td><td>199.30 (+9.21%)</td><td>137.10 (-17.26%)</td><td>36.54 <b>(+209.16%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.72 (n/a)</td><td>0.66 (n/a)</td><td>0.05 (n/a)</td><td>198.70 (n/a)</td><td>182.44 (n/a)</td><td>182.50 (n/a)</td><td>165.70 (n/a)</td><td>11.82 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.83 (+3.95%)</td><td>0.66 (-5.30%)</td><td>0.73 (+7.13%)</td><td>0.35 <b>(-46.77%)</b></td><td>0.19 <b>(+251.92%)</b></td><td>372.30 <b>(+87.84%)</b></td><td>217.66 (+15.96%)</td><td>180.70 (-6.66%)</td><td>158.70 (-3.82%)</td><td>89.21 <b>(+550.01%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.06 (n/a)</td><td>198.20 (n/a)</td><td>187.70 (n/a)</td><td>193.60 (n/a)</td><td>165.00 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.00 <b>(+258.33%)</b></td><td>0.00 <b>(+278.18%)</b></td><td>0.00 <b>(+281.82%)</b></td><td>0.00 <b>(+300.00%)</b></td><td>0.00 (+14.02%)</td><td>1034.03 <b>(-74.29%)</b></td><td>988.07 <b>(-73.77%)</b></td><td>969.71 <b>(-75.12%)</b></td><td>960.13 <b>(-72.14%)</b></td><td>31.34 <b>(-88.91%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4021.43 (n/a)</td><td>3766.95 (n/a)</td><td>3897.55 (n/a)</td><td>3446.55 (n/a)</td><td>282.44 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.01 <b>(+260.87%)</b></td><td>0.01 <b>(+289.22%)</b></td><td>0.01 <b>(+263.64%)</b></td><td>0.01 <b>(+341.18%)</b></td><td>0.00 (+12.87%)</td><td>1093.23 <b>(-77.13%)</b></td><td>1033.26 <b>(-74.63%)</b></td><td>1021.84 <b>(-73.06%)</b></td><td>990.94 <b>(-72.46%)</b></td><td>39.57 <b>(-92.55%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4780.52 (n/a)</td><td>4072.29 (n/a)</td><td>3793.67 (n/a)</td><td>3598.51 (n/a)</td><td>531.34 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.95 <b>(+245.42%)</b></td><td>0.95 <b>(+439.82%)</b></td><td>0.95 <b>(+535.64%)</b></td><td>0.94 <b>(+558.57%)</b></td><td>0.01 <b>(-90.85%)</b></td><td>2228.51 <b>(-84.82%)</b></td><td>2214.97 <b>(-82.57%)</b></td><td>2214.31 <b>(-84.27%)</b></td><td>2199.00 <b>(-71.05%)</b></td><td>12.17 <b>(-99.58%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>14677.80 (n/a)</td><td>12711.00 (n/a)</td><td>14077.07 (n/a)</td><td>7595.45 (n/a)</td><td>2925.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>3.15 (-13.38%)</td><td>2.73 (-14.10%)</td><td>2.59 (-18.07%)</td><td>2.27 <b>(-21.44%)</b></td><td>0.37 <b>(+26.72%)</b></td><td>231.00 <b>(+27.34%)</b></td><td>194.78 (+17.42%)</td><td>202.50 <b>(+22.06%)</b></td><td>166.20 (+15.42%)</td><td>26.82 <b>(+82.94%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.64 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>2.89 (n/a)</td><td>0.30 (n/a)</td><td>181.40 (n/a)</td><td>165.88 (n/a)</td><td>165.90 (n/a)</td><td>144.00 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.70 (-12.13%)</td><td>4.51 (-4.36%)</td><td>4.52 (-1.71%)</td><td>4.22 (+2.86%)</td><td>0.20 <b>(-59.25%)</b></td><td>248.30 (-2.78%)</td><td>232.70 (+3.85%)</td><td>232.10 (+1.75%)</td><td>223.30 (+13.81%)</td><td>10.36 <b>(-54.90%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>5.34 (n/a)</td><td>4.72 (n/a)</td><td>4.60 (n/a)</td><td>4.11 (n/a)</td><td>0.48 (n/a)</td><td>255.40 (n/a)</td><td>224.08 (n/a)</td><td>228.10 (n/a)</td><td>196.20 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>2.65 <b>(-23.20%)</b></td><td>2.45 (-15.53%)</td><td>2.54 (-16.80%)</td><td>2.04 (-7.15%)</td><td>0.25 <b>(-46.92%)</b></td><td>256.50 (+7.73%)</td><td>216.04 (+16.78%)</td><td>206.60 <b>(+20.19%)</b></td><td>197.90 <b>(+30.28%)</b></td><td>24.06 <b>(-26.80%)</b></td>
</tr>
<tr>
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.45 (n/a)</td><td>2.90 (n/a)</td><td>3.05 (n/a)</td><td>2.20 (n/a)</td><td>0.47 (n/a)</td><td>238.10 (n/a)</td><td>185.00 (n/a)</td><td>171.90 (n/a)</td><td>151.90 (n/a)</td><td>32.87 (n/a)</td>
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
