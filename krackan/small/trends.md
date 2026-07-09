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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 <b>(+22.74%)</b></td><td>0.07 (+11.53%)</td><td>0.06 (+2.19%)</td><td>0.06 (+13.84%)</td><td>0.01 <b>(+61.47%)</b></td><td>208.00 (-12.13%)</td><td>188.80 (-9.90%)</td><td>198.10 (-2.12%)</td><td>157.80 (-18.49%)</td><td>20.59 (+15.28%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>236.70 (n/a)</td><td>209.54 (n/a)</td><td>202.40 (n/a)</td><td>193.60 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.09 <b>(+22.71%)</b></td><td>0.07 (+5.90%)</td><td>0.06 (-0.39%)</td><td>0.06 (-0.25%)</td><td>0.01 <b>(+118.35%)</b></td><td>212.80 (+0.24%)</td><td>187.60 (-3.88%)</td><td>192.00 (+0.42%)</td><td>139.70 (-18.49%)</td><td>30.10 <b>(+75.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>195.18 (n/a)</td><td>191.20 (n/a)</td><td>171.40 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (+19.28%)</td><td>0.06 <b>(+26.53%)</b></td><td>0.06 (+16.43%)</td><td>0.06 <b>(+51.46%)</b></td><td>0.01 <b>(-40.14%)</b></td><td>213.00 <b>(-33.97%)</b></td><td>191.74 <b>(-23.85%)</b></td><td>197.70 (-14.12%)</td><td>161.20 (-16.13%)</td><td>19.57 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>322.60 (n/a)</td><td>251.78 (n/a)</td><td>230.20 (n/a)</td><td>192.20 (n/a)</td><td>61.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (+0.67%)</td><td>0.06 (+1.18%)</td><td>0.06 (+1.95%)</td><td>0.05 (-5.13%)</td><td>0.01 <b>(+33.03%)</b></td><td>239.30 (+5.42%)</td><td>206.58 (-0.35%)</td><td>202.20 (-1.89%)</td><td>172.60 (-0.63%)</td><td>30.40 <b>(+41.80%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>207.30 (n/a)</td><td>206.10 (n/a)</td><td>173.70 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (-1.49%)</td><td>0.04 (+19.70%)</td><td>0.04 <b>(+34.77%)</b></td><td>0.03 <b>(+31.03%)</b></td><td>0.00 <b>(-63.63%)</b></td><td>152.90 <b>(-23.70%)</b></td><td>139.58 (-18.86%)</td><td>138.10 <b>(-25.79%)</b></td><td>128.00 (+1.51%)</td><td>9.08 <b>(-72.12%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>172.02 (n/a)</td><td>186.10 (n/a)</td><td>126.10 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (+18.88%)</td><td>0.04 <b>(+23.02%)</b></td><td>0.04 <b>(+25.45%)</b></td><td>0.03 <b>(+26.66%)</b></td><td>0.00 (-3.68%)</td><td>162.10 <b>(-21.04%)</b></td><td>142.34 (-19.29%)</td><td>140.60 <b>(-20.25%)</b></td><td>118.30 (-15.86%)</td><td>16.63 <b>(-36.84%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>176.36 (n/a)</td><td>176.30 (n/a)</td><td>140.60 (n/a)</td><td>26.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 <b>(+20.45%)</b></td><td>0.04 (+6.90%)</td><td>0.04 (+7.82%)</td><td>0.03 (-9.01%)</td><td>0.01 <b>(+99.39%)</b></td><td>203.20 (+9.90%)</td><td>152.96 (-4.24%)</td><td>147.40 (-7.24%)</td><td>115.30 (-16.99%)</td><td>31.65 <b>(+84.21%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>159.74 (n/a)</td><td>158.90 (n/a)</td><td>138.90 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (+2.18%)</td><td>0.03 (-0.96%)</td><td>0.03 (-2.82%)</td><td>0.03 (-3.61%)</td><td>0.00 (-5.26%)</td><td>199.20 (+3.75%)</td><td>167.20 (+0.78%)</td><td>163.50 (+2.89%)</td><td>138.00 (-2.13%)</td><td>22.79 (-5.69%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.00 (n/a)</td><td>165.90 (n/a)</td><td>158.90 (n/a)</td><td>141.00 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 (+11.90%)</td><td>0.04 <b>(+25.75%)</b></td><td>0.04 <b>(+22.11%)</b></td><td>0.04 <b>(+49.80%)</b></td><td>0.00 <b>(-44.61%)</b></td><td>144.90 <b>(-33.23%)</b></td><td>135.68 <b>(-22.27%)</b></td><td>138.40 (-18.11%)</td><td>117.90 (-10.68%)</td><td>10.50 <b>(-67.26%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>174.56 (n/a)</td><td>169.00 (n/a)</td><td>132.00 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 <b>(+30.12%)</b></td><td>0.03 <b>(+27.19%)</b></td><td>0.03 <b>(+30.81%)</b></td><td>0.03 (+12.95%)</td><td>0.00 <b>(+75.15%)</b></td><td>193.40 (-11.45%)</td><td>159.26 <b>(-20.84%)</b></td><td>157.30 <b>(-23.53%)</b></td><td>136.80 <b>(-23.15%)</b></td><td>20.95 <b>(+21.32%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>201.18 (n/a)</td><td>205.70 (n/a)</td><td>178.00 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.04 <b>(+58.54%)</b></td><td>0.03 <b>(+36.04%)</b></td><td>0.04 <b>(+43.36%)</b></td><td>0.03 <b>(+25.38%)</b></td><td>0.01 <b>(+225.19%)</b></td><td>190.10 <b>(-20.26%)</b></td><td>159.22 <b>(-24.91%)</b></td><td>148.90 <b>(-30.26%)</b></td><td>123.50 <b>(-36.93%)</b></td><td>28.44 <b>(+68.77%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>212.04 (n/a)</td><td>213.50 (n/a)</td><td>195.80 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.03 (+5.16%)</td><td>0.03 (+17.03%)</td><td>0.03 <b>(+22.21%)</b></td><td>0.03 <b>(+50.55%)</b></td><td>0.00 <b>(-58.42%)</b></td><td>207.50 <b>(-33.56%)</b></td><td>186.80 (-17.78%)</td><td>187.30 (-18.17%)</td><td>166.20 (-4.92%)</td><td>14.67 <b>(-73.34%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>312.30 (n/a)</td><td>227.20 (n/a)</td><td>228.90 (n/a)</td><td>174.80 (n/a)</td><td>55.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>168.50 (n/a)</td><td>138.06 (n/a)</td><td>137.50 (n/a)</td><td>111.80 (n/a)</td><td>24.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>167.50 (n/a)</td><td>145.84 (n/a)</td><td>151.80 (n/a)</td><td>115.70 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>170.60 (n/a)</td><td>154.94 (n/a)</td><td>161.10 (n/a)</td><td>133.10 (n/a)</td><td>15.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>154.86 (n/a)</td><td>148.70 (n/a)</td><td>124.90 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>201.84 (n/a)</td><td>207.80 (n/a)</td><td>178.80 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>184.78 (n/a)</td><td>183.80 (n/a)</td><td>141.00 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>204.34 (n/a)</td><td>199.80 (n/a)</td><td>189.70 (n/a)</td><td>13.18 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>322.00 (n/a)</td><td>222.30 (n/a)</td><td>211.60 (n/a)</td><td>173.00 (n/a)</td><td>58.71 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>146.00 (n/a)</td><td>129.90 (n/a)</td><td>107.10 (n/a)</td><td>46.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.70 (n/a)</td><td>212.50 (n/a)</td><td>192.60 (n/a)</td><td>157.20 (n/a)</td><td>76.96 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.50 (n/a)</td><td>186.18 (n/a)</td><td>162.70 (n/a)</td><td>141.70 (n/a)</td><td>57.92 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>168.54 (n/a)</td><td>162.70 (n/a)</td><td>138.80 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>186.60 (n/a)</td><td>188.10 (n/a)</td><td>169.60 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.50 (n/a)</td><td>211.48 (n/a)</td><td>184.70 (n/a)</td><td>133.70 (n/a)</td><td>88.93 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>187.32 (n/a)</td><td>188.10 (n/a)</td><td>154.40 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.20 (n/a)</td><td>231.12 (n/a)</td><td>225.30 (n/a)</td><td>177.90 (n/a)</td><td>45.48 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>4.57 (-4.86%)</td><td>3.97 (-0.23%)</td><td>4.12 (+1.34%)</td><td>3.21 (-6.67%)</td><td>0.52 (-5.53%)</td><td>2933.60 (+7.15%)</td><td>2401.82 (+0.24%)</td><td>2285.00 (-1.32%)</td><td>2058.10 (+5.11%)</td><td>338.28 (+6.49%)</td><td>1797.51 (-4.86%)</td><td>1563.15 (-0.23%)</td><td>1619.01 (+1.34%)</td><td>1261.03 (-6.67%)</td><td>204.48 (-5.53%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>4.80 (n/a)</td><td>3.98 (n/a)</td><td>4.06 (n/a)</td><td>3.43 (n/a)</td><td>0.55 (n/a)</td><td>2737.90 (n/a)</td><td>2396.10 (n/a)</td><td>2315.50 (n/a)</td><td>1958.10 (n/a)</td><td>317.65 (n/a)</td><td>1889.27 (n/a)</td><td>1566.75 (n/a)</td><td>1597.63 (n/a)</td><td>1351.20 (n/a)</td><td>216.45 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>1.25 (-0.27%)</td><td>0.91 (+2.96%)</td><td>0.85 <b>(+20.68%)</b></td><td>0.68 <b>(+22.62%)</b></td><td>0.24 <b>(-28.45%)</b></td><td>324.00 (-18.45%)</td><td>255.36 (-8.38%)</td><td>260.90 (-17.15%)</td><td>176.80 (+0.23%)</td><td>62.68 <b>(-35.96%)</b></td><td>53.37 (-0.27%)</td><td>38.94 (+2.96%)</td><td>36.17 <b>(+20.68%)</b></td><td>29.13 <b>(+22.62%)</b></td><td>10.22 <b>(-28.45%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>1.25 (n/a)</td><td>0.89 (n/a)</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.33 (n/a)</td><td>397.30 (n/a)</td><td>278.72 (n/a)</td><td>314.90 (n/a)</td><td>176.40 (n/a)</td><td>97.87 (n/a)</td><td>53.51 (n/a)</td><td>37.82 (n/a)</td><td>29.97 (n/a)</td><td>23.76 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>1.27 (+18.92%)</td><td>0.95 (-7.88%)</td><td>1.00 (-4.14%)</td><td>0.64 <b>(-35.51%)</b></td><td>0.29 <b>(+772.06%)</b></td><td>347.90 <b>(+55.04%)</b></td><td>251.42 (+17.30%)</td><td>222.20 (+4.32%)</td><td>173.70 (-15.92%)</td><td>79.70 <b>(+1060.76%)</b></td><td>54.33 (+18.92%)</td><td>40.59 (-7.88%)</td><td>42.47 (-4.14%)</td><td>27.12 <b>(-35.51%)</b></td><td>12.18 <b>(+772.06%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>1.07 (n/a)</td><td>1.03 (n/a)</td><td>1.04 (n/a)</td><td>0.99 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>214.34 (n/a)</td><td>213.00 (n/a)</td><td>206.60 (n/a)</td><td>6.87 (n/a)</td><td>45.69 (n/a)</td><td>44.07 (n/a)</td><td>44.31 (n/a)</td><td>42.06 (n/a)</td><td>1.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.52 (-0.07%)</td><td>0.52 (+0.12%)</td><td>0.52 (+0.04%)</td><td>0.52 (+0.44%)</td><td>0.00 <b>(-49.96%)</b></td><td>48831.30 (-0.44%)</td><td>48667.38 (-0.12%)</td><td>48629.40 (-0.04%)</td><td>48619.00 (+0.07%)</td><td>91.75 <b>(-50.18%)</b></td><td>353.36 (-0.07%)</td><td>353.01 (+0.12%)</td><td>353.28 (+0.04%)</td><td>351.82 (+0.44%)</td><td>0.66 <b>(-49.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>49047.20 (n/a)</td><td>48726.04 (n/a)</td><td>48651.10 (n/a)</td><td>48583.30 (n/a)</td><td>184.16 (n/a)</td><td>353.62 (n/a)</td><td>352.58 (n/a)</td><td>353.12 (n/a)</td><td>350.27 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.89 (-0.05%)</td><td>0.88 (-0.31%)</td><td>0.87 (-0.54%)</td><td>0.87 (-0.61%)</td><td>0.01 <b>(+56.76%)</b></td><td>28886.70 (+0.61%)</td><td>28675.96 (+0.32%)</td><td>28805.00 (+0.54%)</td><td>28323.90 (+0.05%)</td><td>256.89 <b>(+58.06%)</b></td><td>606.55 (-0.05%)</td><td>599.14 (-0.31%)</td><td>596.42 (-0.54%)</td><td>594.73 (-0.61%)</td><td>5.39 <b>(+56.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28711.90 (n/a)</td><td>28584.60 (n/a)</td><td>28650.10 (n/a)</td><td>28309.30 (n/a)</td><td>162.53 (n/a)</td><td>606.86 (n/a)</td><td>601.03 (n/a)</td><td>599.64 (n/a)</td><td>598.35 (n/a)</td><td>3.44 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.25 (-2.79%)</td><td>3.16 (-3.28%)</td><td>3.14 (-4.24%)</td><td>3.08 (-2.80%)</td><td>0.06 <b>(-23.57%)</b></td><td>8175.60 (+2.88%)</td><td>7978.94 (+3.37%)</td><td>8008.70 (+4.43%)</td><td>7733.30 (+2.87%)</td><td>159.65 (-19.44%)</td><td>2221.54 (-2.79%)</td><td>2153.85 (-3.28%)</td><td>2145.15 (-4.24%)</td><td>2101.37 (-2.80%)</td><td>43.50 <b>(-23.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.35 (n/a)</td><td>3.26 (n/a)</td><td>3.28 (n/a)</td><td>3.17 (n/a)</td><td>0.08 (n/a)</td><td>7946.50 (n/a)</td><td>7718.80 (n/a)</td><td>7669.10 (n/a)</td><td>7517.40 (n/a)</td><td>198.18 (n/a)</td><td>2285.34 (n/a)</td><td>2226.89 (n/a)</td><td>2240.14 (n/a)</td><td>2161.95 (n/a)</td><td>56.91 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.87 (-8.50%)</td><td>3.18 (-19.44%)</td><td>3.06 <b>(-22.21%)</b></td><td>2.78 <b>(-21.57%)</b></td><td>0.42 <b>(+44.52%)</b></td><td>2904.30 <b>(+27.50%)</b></td><td>2563.00 <b>(+25.15%)</b></td><td>2630.60 <b>(+28.55%)</b></td><td>2083.10 (+9.30%)</td><td>305.21 <b>(+98.85%)</b></td><td>1014.82 (-8.50%)</td><td>835.12 (-19.44%)</td><td>803.58 <b>(-22.21%)</b></td><td>727.87 <b>(-21.57%)</b></td><td>108.94 <b>(+44.52%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>4.23 (n/a)</td><td>3.95 (n/a)</td><td>3.94 (n/a)</td><td>3.54 (n/a)</td><td>0.29 (n/a)</td><td>2277.80 (n/a)</td><td>2048.02 (n/a)</td><td>2046.30 (n/a)</td><td>1905.90 (n/a)</td><td>153.49 (n/a)</td><td>1109.14 (n/a)</td><td>1036.69 (n/a)</td><td>1033.05 (n/a)</td><td>928.04 (n/a)</td><td>75.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.50 <b>(+40.96%)</b></td><td>0.36 (+7.00%)</td><td>0.33 (-3.39%)</td><td>0.30 (-8.65%)</td><td>0.08 <b>(+552.72%)</b></td><td>4182.80 (+9.46%)</td><td>3536.54 (-3.50%)</td><td>3763.20 (+3.51%)</td><td>2467.30 <b>(-29.06%)</b></td><td>647.45 <b>(+385.57%)</b></td><td>27.20 <b>(+40.96%)</b></td><td>19.61 (+7.00%)</td><td>17.83 (-3.39%)</td><td>16.04 (-8.65%)</td><td>4.39 <b>(+552.72%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.01 (n/a)</td><td>3821.20 (n/a)</td><td>3664.98 (n/a)</td><td>3635.60 (n/a)</td><td>3477.80 (n/a)</td><td>133.34 (n/a)</td><td>19.30 (n/a)</td><td>18.33 (n/a)</td><td>18.46 (n/a)</td><td>17.56 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>6.44 (+1.36%)</td><td>4.61 (+8.34%)</td><td>4.79 <b>(+42.45%)</b></td><td>3.33 (+3.80%)</td><td>1.30 (-6.71%)</td><td>1998.00 (-3.66%)</td><td>1538.52 (-8.75%)</td><td>1387.70 <b>(-29.80%)</b></td><td>1032.40 (-1.35%)</td><td>425.43 (-9.03%)</td><td>1990.63 (+1.36%)</td><td>1423.10 (+8.34%)</td><td>1481.04 <b>(+42.45%)</b></td><td>1028.63 (+3.80%)</td><td>401.41 (-6.71%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>6.36 (n/a)</td><td>4.25 (n/a)</td><td>3.37 (n/a)</td><td>3.21 (n/a)</td><td>1.39 (n/a)</td><td>2073.80 (n/a)</td><td>1686.02 (n/a)</td><td>1976.80 (n/a)</td><td>1046.50 (n/a)</td><td>467.65 (n/a)</td><td>1963.86 (n/a)</td><td>1313.54 (n/a)</td><td>1039.67 (n/a)</td><td>991.01 (n/a)</td><td>430.28 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.25 (+15.52%)</td><td>0.19 (-4.02%)</td><td>0.17 (-15.58%)</td><td>0.15 <b>(-21.94%)</b></td><td>0.04 <b>(+337.33%)</b></td><td>0.24 (+15.52%)</td><td>0.19 (-4.02%)</td><td>0.17 (-15.58%)</td><td>0.15 <b>(-21.94%)</b></td><td>0.04 <b>(+337.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>13.41 (+0.77%)</td><td>12.77 (+2.40%)</td><td>12.89 (+4.81%)</td><td>11.85 (-2.32%)</td><td>0.64 <b>(+34.72%)</b></td><td>13.40 (+0.77%)</td><td>12.76 (+2.40%)</td><td>12.89 (+4.81%)</td><td>11.85 (-2.32%)</td><td>0.64 <b>(+34.72%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>13.30 (n/a)</td><td>12.47 (n/a)</td><td>12.30 (n/a)</td><td>12.13 (n/a)</td><td>0.47 (n/a)</td><td>13.29 (n/a)</td><td>12.46 (n/a)</td><td>12.29 (n/a)</td><td>12.13 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>24.49 (-3.40%)</td><td>23.31 (+1.92%)</td><td>24.00 (-0.40%)</td><td>20.78 <b>(+26.46%)</b></td><td>1.51 <b>(-58.49%)</b></td><td>24.47 (-3.40%)</td><td>23.30 (+1.92%)</td><td>23.99 (-0.40%)</td><td>20.76 <b>(+26.46%)</b></td><td>1.51 <b>(-58.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>25.35 (n/a)</td><td>22.87 (n/a)</td><td>24.10 (n/a)</td><td>16.43 (n/a)</td><td>3.64 (n/a)</td><td>25.33 (n/a)</td><td>22.86 (n/a)</td><td>24.09 (n/a)</td><td>16.42 (n/a)</td><td>3.64 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>40.35 (-2.56%)</td><td>39.27 (-4.11%)</td><td>38.99 (-4.85%)</td><td>38.50 (-4.70%)</td><td>0.74 <b>(+83.42%)</b></td><td>40.32 (-2.56%)</td><td>39.25 (-4.11%)</td><td>38.97 (-4.85%)</td><td>38.47 (-4.70%)</td><td>0.74 <b>(+83.42%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>41.41 (n/a)</td><td>40.96 (n/a)</td><td>40.98 (n/a)</td><td>40.40 (n/a)</td><td>0.40 (n/a)</td><td>41.38 (n/a)</td><td>40.93 (n/a)</td><td>40.95 (n/a)</td><td>40.37 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>43.53 (-6.97%)</td><td>42.26 (-0.27%)</td><td>42.87 (+1.73%)</td><td>39.80 (+2.70%)</td><td>1.47 <b>(-49.08%)</b></td><td>43.50 (-6.97%)</td><td>42.24 (-0.27%)</td><td>42.84 (+1.73%)</td><td>39.78 (+2.70%)</td><td>1.47 <b>(-49.08%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>46.79 (n/a)</td><td>42.37 (n/a)</td><td>42.14 (n/a)</td><td>38.75 (n/a)</td><td>2.89 (n/a)</td><td>46.76 (n/a)</td><td>42.35 (n/a)</td><td>42.11 (n/a)</td><td>38.73 (n/a)</td><td>2.89 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>13.24 (+0.04%)</td><td>12.82 (+5.45%)</td><td>13.17 (+7.98%)</td><td>12.04 (+13.74%)</td><td>0.55 <b>(-43.79%)</b></td><td>13.23 (+0.04%)</td><td>12.81 (+5.45%)</td><td>13.16 (+7.98%)</td><td>12.03 (+13.74%)</td><td>0.55 <b>(-43.79%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>13.23 (n/a)</td><td>12.16 (n/a)</td><td>12.19 (n/a)</td><td>10.58 (n/a)</td><td>0.98 (n/a)</td><td>13.22 (n/a)</td><td>12.15 (n/a)</td><td>12.18 (n/a)</td><td>10.58 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>25.10 (-0.30%)</td><td>23.13 (-0.13%)</td><td>24.16 (+5.96%)</td><td>17.89 (-18.25%)</td><td>2.96 <b>(+136.34%)</b></td><td>25.09 (-0.30%)</td><td>23.12 (-0.13%)</td><td>24.15 (+5.96%)</td><td>17.88 (-18.25%)</td><td>2.96 <b>(+136.33%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>25.18 (n/a)</td><td>23.16 (n/a)</td><td>22.80 (n/a)</td><td>21.89 (n/a)</td><td>1.25 (n/a)</td><td>25.16 (n/a)</td><td>23.15 (n/a)</td><td>22.79 (n/a)</td><td>21.87 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>41.17 (-0.94%)</td><td>39.69 (+8.04%)</td><td>39.92 (+0.39%)</td><td>38.55 <b>(+31.11%)</b></td><td>1.12 <b>(-78.88%)</b></td><td>41.15 (-0.94%)</td><td>39.67 (+8.04%)</td><td>39.89 (+0.39%)</td><td>38.53 <b>(+31.11%)</b></td><td>1.12 <b>(-78.88%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>41.56 (n/a)</td><td>36.74 (n/a)</td><td>39.76 (n/a)</td><td>29.40 (n/a)</td><td>5.32 (n/a)</td><td>41.54 (n/a)</td><td>36.72 (n/a)</td><td>39.74 (n/a)</td><td>29.39 (n/a)</td><td>5.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>45.77 (+4.44%)</td><td>42.80 (-0.06%)</td><td>42.99 (-0.97%)</td><td>40.18 (-0.69%)</td><td>2.11 <b>(+53.91%)</b></td><td>45.74 (+4.44%)</td><td>42.78 (-0.06%)</td><td>42.96 (-0.97%)</td><td>40.16 (-0.69%)</td><td>2.11 <b>(+53.91%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>43.83 (n/a)</td><td>42.83 (n/a)</td><td>43.41 (n/a)</td><td>40.46 (n/a)</td><td>1.37 (n/a)</td><td>43.80 (n/a)</td><td>42.80 (n/a)</td><td>43.39 (n/a)</td><td>40.44 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>182.66 (n/a)</td><td>185.00 (n/a)</td><td>132.70 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>165.42 (n/a)</td><td>160.60 (n/a)</td><td>125.00 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.50 (n/a)</td><td>187.60 (n/a)</td><td>172.00 (n/a)</td><td>127.50 (n/a)</td><td>58.15 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>171.94 (n/a)</td><td>172.70 (n/a)</td><td>141.90 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>172.12 (n/a)</td><td>171.50 (n/a)</td><td>135.90 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.10 (n/a)</td><td>179.14 (n/a)</td><td>168.50 (n/a)</td><td>139.80 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.40 (n/a)</td><td>231.54 (n/a)</td><td>194.70 (n/a)</td><td>160.50 (n/a)</td><td>72.70 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>203.68 (n/a)</td><td>207.00 (n/a)</td><td>175.10 (n/a)</td><td>17.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 (+12.36%)</td><td>0.05 (+8.35%)</td><td>0.05 (+14.73%)</td><td>0.04 (-6.29%)</td><td>0.01 (+12.44%)</td><td>227.70 (+6.75%)</td><td>158.54 (-6.82%)</td><td>149.10 (-12.86%)</td><td>120.80 (-11.05%)</td><td>40.48 (+16.70%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>170.14 (n/a)</td><td>171.10 (n/a)</td><td>135.80 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (+15.66%)</td><td>0.04 (+7.23%)</td><td>0.04 (+6.30%)</td><td>0.03 (-6.81%)</td><td>0.01 <b>(+163.87%)</b></td><td>255.20 (+7.32%)</td><td>206.80 (-5.02%)</td><td>204.30 (-5.94%)</td><td>171.60 (-13.51%)</td><td>34.51 <b>(+141.57%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.80 (n/a)</td><td>217.74 (n/a)</td><td>217.20 (n/a)</td><td>198.40 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 <b>(+29.70%)</b></td><td>0.05 <b>(+30.69%)</b></td><td>0.05 <b>(+22.12%)</b></td><td>0.05 <b>(+92.03%)</b></td><td>0.01 <b>(-29.66%)</b></td><td>181.40 <b>(-47.92%)</b></td><td>155.74 <b>(-27.84%)</b></td><td>160.10 (-18.15%)</td><td>127.10 <b>(-22.92%)</b></td><td>20.30 <b>(-73.13%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.30 (n/a)</td><td>215.84 (n/a)</td><td>195.60 (n/a)</td><td>164.90 (n/a)</td><td>75.55 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 <b>(+25.59%)</b></td><td>0.06 <b>(+24.12%)</b></td><td>0.06 <b>(+35.84%)</b></td><td>0.05 (+14.14%)</td><td>0.01 <b>(+26.19%)</b></td><td>176.20 (-12.38%)</td><td>137.86 (-19.20%)</td><td>132.80 <b>(-26.39%)</b></td><td>107.40 <b>(-20.39%)</b></td><td>26.23 (-10.78%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>170.62 (n/a)</td><td>180.40 (n/a)</td><td>134.90 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 <b>(+41.36%)</b></td><td>0.06 <b>(+33.34%)</b></td><td>0.05 <b>(+20.29%)</b></td><td>0.05 <b>(+42.74%)</b></td><td>0.01 <b>(+27.69%)</b></td><td>178.50 <b>(-29.95%)</b></td><td>151.04 <b>(-25.26%)</b></td><td>151.50 (-16.85%)</td><td>125.70 <b>(-29.22%)</b></td><td>20.99 <b>(-36.44%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.80 (n/a)</td><td>202.08 (n/a)</td><td>182.20 (n/a)</td><td>177.60 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 <b>(+42.49%)</b></td><td>0.05 <b>(+27.23%)</b></td><td>0.05 (+19.80%)</td><td>0.04 (+12.39%)</td><td>0.01 <b>(+166.70%)</b></td><td>210.50 (-11.03%)</td><td>164.88 (-19.07%)</td><td>171.90 (-16.55%)</td><td>127.70 <b>(-29.84%)</b></td><td>35.65 <b>(+61.60%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.60 (n/a)</td><td>203.74 (n/a)</td><td>206.00 (n/a)</td><td>182.00 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 <b>(+22.79%)</b></td><td>0.05 (+11.00%)</td><td>0.05 (+8.48%)</td><td>0.04 (+10.35%)</td><td>0.01 <b>(+83.15%)</b></td><td>192.10 (-9.39%)</td><td>173.36 (-9.18%)</td><td>179.70 (-7.80%)</td><td>138.30 (-18.55%)</td><td>21.19 <b>(+33.29%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.00 (n/a)</td><td>190.88 (n/a)</td><td>194.90 (n/a)</td><td>169.80 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 <b>(+31.60%)</b></td><td>0.05 <b>(+24.57%)</b></td><td>0.05 <b>(+22.42%)</b></td><td>0.04 <b>(+20.95%)</b></td><td>0.01 <b>(+36.96%)</b></td><td>195.40 (-17.34%)</td><td>163.56 (-19.56%)</td><td>161.10 (-18.31%)</td><td>138.40 <b>(-24.00%)</b></td><td>20.59 (-12.26%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.40 (n/a)</td><td>203.34 (n/a)</td><td>197.20 (n/a)</td><td>182.10 (n/a)</td><td>23.47 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 <b>(+25.74%)</b></td><td>0.05 (+14.95%)</td><td>0.05 (+18.86%)</td><td>0.04 (-14.55%)</td><td>0.01 <b>(+252.68%)</b></td><td>215.80 (+17.03%)</td><td>158.76 (-9.49%)</td><td>152.00 (-15.88%)</td><td>123.30 <b>(-20.50%)</b></td><td>38.41 <b>(+224.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>175.40 (n/a)</td><td>180.70 (n/a)</td><td>155.10 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.10 (+14.47%)</td><td>0.09 <b>(+34.92%)</b></td><td>0.09 <b>(+54.47%)</b></td><td>0.07 <b>(+38.57%)</b></td><td>0.01 <b>(-32.43%)</b></td><td>174.80 <b>(-27.83%)</b></td><td>145.82 <b>(-27.99%)</b></td><td>141.40 <b>(-35.26%)</b></td><td>124.90 (-12.66%)</td><td>18.33 <b>(-57.21%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.20 (n/a)</td><td>202.50 (n/a)</td><td>218.40 (n/a)</td><td>143.00 (n/a)</td><td>42.84 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (+1.48%)</td><td>0.05 (+0.91%)</td><td>0.06 (+7.83%)</td><td>0.03 <b>(-30.90%)</b></td><td>0.01 <b>(+57.08%)</b></td><td>299.60 <b>(+44.73%)</b></td><td>175.94 (+6.10%)</td><td>145.50 (-7.27%)</td><td>128.90 (-1.45%)</td><td>71.43 <b>(+125.37%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>165.82 (n/a)</td><td>156.90 (n/a)</td><td>130.80 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 <b>(+45.70%)</b></td><td>0.07 <b>(+40.31%)</b></td><td>0.08 <b>(+48.23%)</b></td><td>0.06 <b>(+30.41%)</b></td><td>0.01 <b>(+159.95%)</b></td><td>169.20 <b>(-23.30%)</b></td><td>143.82 <b>(-27.64%)</b></td><td>132.40 <b>(-32.55%)</b></td><td>120.60 <b>(-31.36%)</b></td><td>23.50 <b>(+41.82%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>220.60 (n/a)</td><td>198.76 (n/a)</td><td>196.30 (n/a)</td><td>175.70 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 <b>(+32.50%)</b></td><td>0.06 <b>(+32.05%)</b></td><td>0.05 (+17.40%)</td><td>0.04 <b>(+25.95%)</b></td><td>0.01 <b>(+36.77%)</b></td><td>193.10 <b>(-20.60%)</b></td><td>146.80 <b>(-24.07%)</b></td><td>150.10 (-14.81%)</td><td>115.80 <b>(-24.51%)</b></td><td>30.20 (-19.69%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.20 (n/a)</td><td>193.34 (n/a)</td><td>176.20 (n/a)</td><td>153.40 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.08 <b>(+35.72%)</b></td><td>0.07 (+15.17%)</td><td>0.06 (+1.54%)</td><td>0.05 (-0.75%)</td><td>0.01 <b>(+154.46%)</b></td><td>213.10 (+0.76%)</td><td>163.58 (-10.48%)</td><td>171.30 (-1.55%)</td><td>122.80 <b>(-26.33%)</b></td><td>35.99 <b>(+86.53%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>182.74 (n/a)</td><td>174.00 (n/a)</td><td>166.70 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (+19.30%)</td><td>0.05 (+11.69%)</td><td>0.05 (-1.36%)</td><td>0.04 (+13.25%)</td><td>0.01 (+18.96%)</td><td>203.60 (-11.71%)</td><td>168.52 (-10.41%)</td><td>178.30 (+1.36%)</td><td>126.80 (-16.19%)</td><td>32.89 (-13.64%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>188.10 (n/a)</td><td>175.90 (n/a)</td><td>151.30 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (+9.58%)</td><td>0.05 (+9.63%)</td><td>0.05 (+9.96%)</td><td>0.04 (+7.21%)</td><td>0.01 <b>(+21.48%)</b></td><td>254.30 (-6.75%)</td><td>184.74 (-8.26%)</td><td>170.40 (-9.02%)</td><td>156.50 (-8.75%)</td><td>40.55 (+0.09%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.70 (n/a)</td><td>201.38 (n/a)</td><td>187.30 (n/a)</td><td>171.50 (n/a)</td><td>40.52 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 <b>(+40.17%)</b></td><td>0.05 (+14.41%)</td><td>0.04 (-5.12%)</td><td>0.03 (-12.60%)</td><td>0.02 <b>(+206.81%)</b></td><td>240.90 (+14.39%)</td><td>173.96 (-6.57%)</td><td>185.10 (+5.41%)</td><td>116.30 <b>(-28.69%)</b></td><td>52.63 <b>(+134.76%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>186.20 (n/a)</td><td>175.60 (n/a)</td><td>163.10 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.07 <b>(+24.90%)</b></td><td>0.06 (+13.69%)</td><td>0.06 <b>(+22.56%)</b></td><td>0.05 (+4.40%)</td><td>0.01 <b>(+80.44%)</b></td><td>203.70 (-4.23%)</td><td>167.26 (-10.61%)</td><td>152.40 (-18.42%)</td><td>133.20 (-19.90%)</td><td>30.49 <b>(+44.47%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>187.12 (n/a)</td><td>186.80 (n/a)</td><td>166.30 (n/a)</td><td>21.11 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (-6.55%)</td><td>0.04 (-5.18%)</td><td>0.04 (+1.07%)</td><td>0.04 (-10.15%)</td><td>0.01 (-7.47%)</td><td>223.10 (+11.33%)</td><td>189.26 (+5.47%)</td><td>187.90 (-1.05%)</td><td>150.60 (+7.04%)</td><td>27.42 (+8.96%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>179.44 (n/a)</td><td>189.90 (n/a)</td><td>140.70 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 <b>(+35.82%)</b></td><td>0.05 <b>(+21.14%)</b></td><td>0.05 <b>(+22.63%)</b></td><td>0.03 (-16.74%)</td><td>0.01 <b>(+347.26%)</b></td><td>309.70 <b>(+20.09%)</b></td><td>204.74 (-12.71%)</td><td>191.10 (-18.47%)</td><td>158.00 <b>(-26.37%)</b></td><td>61.94 <b>(+296.71%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>257.90 (n/a)</td><td>234.56 (n/a)</td><td>234.40 (n/a)</td><td>214.60 (n/a)</td><td>15.61 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 <b>(+20.69%)</b></td><td>0.05 (+19.93%)</td><td>0.05 <b>(+26.71%)</b></td><td>0.04 (+13.06%)</td><td>0.01 <b>(+59.99%)</b></td><td>209.10 (-11.55%)</td><td>177.02 (-16.07%)</td><td>168.80 <b>(-21.05%)</b></td><td>155.40 (-17.12%)</td><td>23.57 (+17.36%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.40 (n/a)</td><td>210.92 (n/a)</td><td>213.80 (n/a)</td><td>187.50 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.06 (+0.54%)</td><td>0.05 (+9.55%)</td><td>0.05 <b>(+24.81%)</b></td><td>0.04 (-1.42%)</td><td>0.01 <b>(+20.87%)</b></td><td>232.00 (+1.40%)</td><td>189.96 (-7.71%)</td><td>172.20 (-19.87%)</td><td>153.50 (-0.58%)</td><td>38.14 <b>(+29.96%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>205.82 (n/a)</td><td>214.90 (n/a)</td><td>154.40 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.05 (+18.15%)</td><td>0.04 (+7.75%)</td><td>0.04 (+10.43%)</td><td>0.02 (+5.81%)</td><td>0.01 <b>(+63.92%)</b></td><td>336.40 (-5.51%)</td><td>244.04 (-4.00%)</td><td>209.20 (-9.44%)</td><td>180.60 (-15.37%)</td><td>72.64 <b>(+25.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>356.00 (n/a)</td><td>254.22 (n/a)</td><td>231.00 (n/a)</td><td>213.40 (n/a)</td><td>57.78 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.59 (-8.66%)</td><td>0.54 (-7.12%)</td><td>0.57 (-6.47%)</td><td>0.47 (-6.93%)</td><td>0.05 <b>(-21.42%)</b></td><td>209.80 (+7.48%)</td><td>183.18 (+7.31%)</td><td>171.20 (+6.87%)</td><td>166.20 (+9.49%)</td><td>19.40 (-8.31%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.65 (n/a)</td><td>0.58 (n/a)</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.07 (n/a)</td><td>195.20 (n/a)</td><td>170.70 (n/a)</td><td>160.20 (n/a)</td><td>151.80 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.67 (+0.70%)</td><td>0.61 (+7.18%)</td><td>0.61 (+4.16%)</td><td>0.56 <b>(+22.38%)</b></td><td>0.05 <b>(-38.30%)</b></td><td>175.00 (-18.30%)</td><td>160.96 (-7.65%)</td><td>161.20 (-3.99%)</td><td>147.80 (-0.67%)</td><td>11.99 <b>(-51.21%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.46 (n/a)</td><td>0.07 (n/a)</td><td>214.20 (n/a)</td><td>174.30 (n/a)</td><td>167.90 (n/a)</td><td>148.80 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.63 (-8.98%)</td><td>0.58 (+0.00%)</td><td>0.57 (-0.65%)</td><td>0.51 (+8.58%)</td><td>0.05 <b>(-55.96%)</b></td><td>193.20 (-7.91%)</td><td>171.60 (-2.20%)</td><td>173.00 (+0.64%)</td><td>155.30 (+9.91%)</td><td>14.28 <b>(-55.89%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.70 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.11 (n/a)</td><td>209.80 (n/a)</td><td>175.46 (n/a)</td><td>171.90 (n/a)</td><td>141.30 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.68 <b>(+39.85%)</b></td><td>0.59 <b>(+32.06%)</b></td><td>0.57 <b>(+26.65%)</b></td><td>0.53 <b>(+42.09%)</b></td><td>0.06 <b>(+23.13%)</b></td><td>185.70 <b>(-29.61%)</b></td><td>168.30 <b>(-24.44%)</b></td><td>171.70 <b>(-21.02%)</b></td><td>145.10 <b>(-28.49%)</b></td><td>15.37 <b>(-38.49%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>263.80 (n/a)</td><td>222.74 (n/a)</td><td>217.40 (n/a)</td><td>202.90 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.44 (-13.95%)</td><td>0.41 (-5.79%)</td><td>0.40 (-7.58%)</td><td>0.38 (+4.93%)</td><td>0.03 <b>(-50.02%)</b></td><td>196.00 (-4.72%)</td><td>181.60 (+5.07%)</td><td>184.20 (+8.23%)</td><td>168.20 (+16.16%)</td><td>12.58 <b>(-45.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>205.70 (n/a)</td><td>172.84 (n/a)</td><td>170.20 (n/a)</td><td>144.80 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.44 (-5.08%)</td><td>0.41 (+4.10%)</td><td>0.41 (+3.88%)</td><td>0.37 <b>(+21.98%)</b></td><td>0.02 <b>(-56.60%)</b></td><td>197.60 (-18.04%)</td><td>179.94 (-5.42%)</td><td>178.60 (-3.72%)</td><td>168.60 (+5.31%)</td><td>11.18 <b>(-63.39%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>241.10 (n/a)</td><td>190.26 (n/a)</td><td>185.50 (n/a)</td><td>160.10 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.54 <b>(+20.64%)</b></td><td>0.45 (+8.46%)</td><td>0.43 (+5.48%)</td><td>0.34 (-8.94%)</td><td>0.09 <b>(+226.23%)</b></td><td>215.00 (+9.86%)</td><td>170.32 (-5.21%)</td><td>171.40 (-5.20%)</td><td>136.10 (-17.11%)</td><td>33.58 <b>(+189.88%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.45 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.03 (n/a)</td><td>195.70 (n/a)</td><td>179.68 (n/a)</td><td>180.80 (n/a)</td><td>164.20 (n/a)</td><td>11.58 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.40 (-7.71%)</td><td>0.39 (+11.40%)</td><td>0.39 (+15.78%)</td><td>0.36 <b>(+24.77%)</b></td><td>0.02 <b>(-69.49%)</b></td><td>205.30 (-19.87%)</td><td>191.62 (-11.72%)</td><td>190.00 (-13.60%)</td><td>183.40 (+8.33%)</td><td>8.57 <b>(-72.69%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>256.20 (n/a)</td><td>217.06 (n/a)</td><td>219.90 (n/a)</td><td>169.30 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.97 (+11.83%)</td><td>0.84 <b>(+23.28%)</b></td><td>0.88 (+13.53%)</td><td>0.68 <b>(+36.46%)</b></td><td>0.11 <b>(-36.13%)</b></td><td>192.70 <b>(-26.70%)</b></td><td>157.42 <b>(-22.10%)</b></td><td>148.90 (-11.89%)</td><td>135.50 (-10.62%)</td><td>22.12 <b>(-59.28%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.86 (n/a)</td><td>0.69 (n/a)</td><td>0.78 (n/a)</td><td>0.50 (n/a)</td><td>0.17 (n/a)</td><td>262.90 (n/a)</td><td>202.08 (n/a)</td><td>169.00 (n/a)</td><td>151.60 (n/a)</td><td>54.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.79 (-15.29%)</td><td>0.72 (-1.48%)</td><td>0.72 (+4.59%)</td><td>0.66 (+9.11%)</td><td>0.05 <b>(-62.21%)</b></td><td>198.70 (-8.35%)</td><td>182.44 (-0.30%)</td><td>182.50 (-4.40%)</td><td>165.70 (+18.02%)</td><td>11.82 <b>(-58.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.93 (n/a)</td><td>0.73 (n/a)</td><td>0.69 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>216.80 (n/a)</td><td>182.98 (n/a)</td><td>190.90 (n/a)</td><td>140.40 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.79 (-6.47%)</td><td>0.70 (-2.46%)</td><td>0.68 (-10.10%)</td><td>0.66 (+18.23%)</td><td>0.06 <b>(-48.78%)</b></td><td>198.20 (-15.41%)</td><td>187.70 (+1.01%)</td><td>193.60 (+11.26%)</td><td>165.00 (+6.93%)</td><td>13.72 <b>(-54.72%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.85 (n/a)</td><td>0.72 (n/a)</td><td>0.75 (n/a)</td><td>0.56 (n/a)</td><td>0.11 (n/a)</td><td>234.30 (n/a)</td><td>185.82 (n/a)</td><td>174.00 (n/a)</td><td>154.30 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.00 (+0.00%)</td><td>0.00 (+3.77%)</td><td>0.00 (+0.00%)</td><td>0.00 (+11.11%)</td><td>0.00 <b>(-34.06%)</b></td><td>4021.43 (-9.66%)</td><td>3766.95 (-4.08%)</td><td>3897.55 (+1.39%)</td><td>3446.55 (-0.74%)</td><td>282.44 <b>(-39.73%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4451.35 (n/a)</td><td>3927.18 (n/a)</td><td>3844.19 (n/a)</td><td>3472.28 (n/a)</td><td>468.63 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.00 (+9.52%)</td><td>0.00 (+9.68%)</td><td>0.00 <b>(+22.22%)</b></td><td>0.00 (-5.56%)</td><td>0.00 <b>(+101.38%)</b></td><td>4780.52 (+4.44%)</td><td>4072.29 (-7.78%)</td><td>3793.67 (-16.37%)</td><td>3598.51 (-8.86%)</td><td>531.34 <b>(+101.27%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4577.20 (n/a)</td><td>4415.88 (n/a)</td><td>4536.16 (n/a)</td><td>3948.49 (n/a)</td><td>263.99 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>0.28 (+0.15%)</td><td>0.18 (-16.53%)</td><td>0.15 (-18.53%)</td><td>0.14 (-8.57%)</td><td>0.06 (-6.36%)</td><td>14677.80 (+9.38%)</td><td>12711.00 (+19.50%)</td><td>14077.07 <b>(+22.79%)</b></td><td>7595.45 (-0.16%)</td><td>2925.98 (+2.35%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>13419.47 (n/a)</td><td>10637.06 (n/a)</td><td>11464.28 (n/a)</td><td>7607.60 (n/a)</td><td>2858.67 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.64 (-0.15%)</td><td>3.18 (+11.82%)</td><td>3.16 (+17.58%)</td><td>2.89 (+14.75%)</td><td>0.30 <b>(-35.01%)</b></td><td>181.40 (-12.87%)</td><td>165.88 (-11.53%)</td><td>165.90 (-14.97%)</td><td>144.00 (+0.14%)</td><td>14.66 <b>(-41.53%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.65 (n/a)</td><td>2.84 (n/a)</td><td>2.69 (n/a)</td><td>2.52 (n/a)</td><td>0.45 (n/a)</td><td>208.20 (n/a)</td><td>187.50 (n/a)</td><td>195.10 (n/a)</td><td>143.80 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>5.34 (-3.88%)</td><td>4.72 (+5.49%)</td><td>4.60 (+9.38%)</td><td>4.11 (+4.77%)</td><td>0.48 <b>(-28.17%)</b></td><td>255.40 (-4.56%)</td><td>224.08 (-5.96%)</td><td>228.10 (-8.58%)</td><td>196.20 (+4.03%)</td><td>22.98 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>5.56 (n/a)</td><td>4.47 (n/a)</td><td>4.20 (n/a)</td><td>3.92 (n/a)</td><td>0.67 (n/a)</td><td>267.60 (n/a)</td><td>238.28 (n/a)</td><td>249.50 (n/a)</td><td>188.60 (n/a)</td><td>32.23 (n/a)</td>
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
<td><code>f2ce7b0</code> — 2026-07-09 19:02:34</td><td>3.45 (+4.15%)</td><td>2.90 (+2.15%)</td><td>3.05 (+1.77%)</td><td>2.20 (-5.31%)</td><td>0.47 (+8.25%)</td><td>238.10 (+5.59%)</td><td>185.00 (-1.76%)</td><td>171.90 (-1.77%)</td><td>151.90 (-3.98%)</td><td>32.87 (+10.77%)</td>
</tr>
<tr>
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.31 (n/a)</td><td>2.84 (n/a)</td><td>3.00 (n/a)</td><td>2.33 (n/a)</td><td>0.43 (n/a)</td><td>225.50 (n/a)</td><td>188.32 (n/a)</td><td>175.00 (n/a)</td><td>158.20 (n/a)</td><td>29.67 (n/a)</td>
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
