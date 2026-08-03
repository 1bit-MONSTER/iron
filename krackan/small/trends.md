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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (+3.34%)</td><td>0.07 (+2.74%)</td><td>0.07 (+3.07%)</td><td>0.05 (-5.10%)</td><td>0.01 <b>(+30.50%)</b></td><td>224.70 (+5.34%)</td><td>183.24 (-2.16%)</td><td>177.20 (-2.96%)</td><td>165.80 (-3.21%)</td><td>23.76 <b>(+36.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>187.28 (n/a)</td><td>182.60 (n/a)</td><td>171.30 (n/a)</td><td>17.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 <b>(-20.54%)</b></td><td>0.06 (-13.64%)</td><td>0.06 (-7.67%)</td><td>0.06 (-17.55%)</td><td>0.01 <b>(-31.02%)</b></td><td>221.90 <b>(+21.26%)</b></td><td>192.48 (+15.45%)</td><td>190.00 (+8.32%)</td><td>173.70 <b>(+25.87%)</b></td><td>19.31 (+5.71%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>166.72 (n/a)</td><td>175.40 (n/a)</td><td>138.00 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.09 (+5.42%)</td><td>0.07 (+1.24%)</td><td>0.07 (+7.33%)</td><td>0.05 (-3.87%)</td><td>0.01 (+14.70%)</td><td>236.40 (+4.05%)</td><td>183.46 (-0.54%)</td><td>178.50 (-6.84%)</td><td>142.30 (-5.13%)</td><td>35.14 (+15.45%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>184.46 (n/a)</td><td>191.60 (n/a)</td><td>150.00 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.08 (+8.82%)</td><td>0.06 (+5.14%)</td><td>0.06 (+1.67%)</td><td>0.06 (+11.77%)</td><td>0.01 (+6.49%)</td><td>220.00 (-10.53%)</td><td>197.30 (-4.99%)</td><td>199.80 (-1.62%)</td><td>162.40 (-8.14%)</td><td>21.75 (-14.64%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>245.90 (n/a)</td><td>207.66 (n/a)</td><td>203.10 (n/a)</td><td>176.80 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (-9.08%)</td><td>0.03 (-7.80%)</td><td>0.03 (-15.05%)</td><td>0.03 (+12.11%)</td><td>0.00 <b>(-54.62%)</b></td><td>188.60 (-10.79%)</td><td>173.52 (+6.77%)</td><td>178.00 (+17.65%)</td><td>160.10 (+9.96%)</td><td>12.10 <b>(-56.51%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>162.52 (n/a)</td><td>151.30 (n/a)</td><td>145.60 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 <b>(-21.26%)</b></td><td>0.03 <b>(-23.96%)</b></td><td>0.03 <b>(-25.39%)</b></td><td>0.03 (-18.92%)</td><td>0.01 <b>(-20.62%)</b></td><td>199.70 <b>(+23.35%)</b></td><td>175.34 <b>(+31.44%)</b></td><td>183.40 <b>(+33.97%)</b></td><td>127.50 <b>(+26.99%)</b></td><td>28.58 <b>(+23.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>161.90 (n/a)</td><td>133.40 (n/a)</td><td>136.90 (n/a)</td><td>100.40 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 <b>(-20.24%)</b></td><td>0.03 (-1.52%)</td><td>0.03 (+11.26%)</td><td>0.03 (+4.07%)</td><td>0.00 <b>(-56.49%)</b></td><td>192.10 (-3.90%)</td><td>174.12 (-0.80%)</td><td>172.10 (-10.08%)</td><td>158.30 <b>(+25.44%)</b></td><td>16.34 <b>(-48.16%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>175.52 (n/a)</td><td>191.40 (n/a)</td><td>126.20 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (-14.45%)</td><td>0.03 (+4.19%)</td><td>0.03 (+15.77%)</td><td>0.03 (+13.45%)</td><td>0.00 <b>(-67.98%)</b></td><td>180.60 (-11.86%)</td><td>171.62 (-6.12%)</td><td>174.30 (-13.63%)</td><td>160.90 (+16.85%)</td><td>9.72 <b>(-67.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>182.80 (n/a)</td><td>201.80 (n/a)</td><td>137.70 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (+2.87%)</td><td>0.04 (+18.03%)</td><td>0.04 <b>(+27.71%)</b></td><td>0.03 (+14.53%)</td><td>0.00 <b>(-34.88%)</b></td><td>169.80 (-12.70%)</td><td>148.24 (-16.26%)</td><td>147.00 <b>(-21.73%)</b></td><td>131.20 (-2.81%)</td><td>13.89 <b>(-43.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.50 (n/a)</td><td>177.02 (n/a)</td><td>187.80 (n/a)</td><td>135.00 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (-1.16%)</td><td>0.03 (-4.70%)</td><td>0.02 (-9.24%)</td><td>0.02 <b>(-20.74%)</b></td><td>0.01 <b>(+72.74%)</b></td><td>257.20 <b>(+26.14%)</b></td><td>203.00 (+7.15%)</td><td>211.80 (+10.14%)</td><td>161.10 (+1.13%)</td><td>38.71 <b>(+119.58%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.90 (n/a)</td><td>189.46 (n/a)</td><td>192.30 (n/a)</td><td>159.30 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (-4.06%)</td><td>0.03 (-3.77%)</td><td>0.03 (-3.78%)</td><td>0.03 (+8.04%)</td><td>0.00 <b>(-24.56%)</b></td><td>209.40 (-7.43%)</td><td>188.68 (+3.10%)</td><td>187.90 (+3.93%)</td><td>158.60 (+4.20%)</td><td>19.78 <b>(-28.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.20 (n/a)</td><td>183.00 (n/a)</td><td>180.80 (n/a)</td><td>152.20 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.03 (-10.62%)</td><td>0.02 (-0.58%)</td><td>0.02 (-1.38%)</td><td>0.02 (+9.39%)</td><td>0.00 <b>(-59.88%)</b></td><td>233.20 (-8.58%)</td><td>220.14 (-0.34%)</td><td>221.90 (+1.42%)</td><td>205.70 (+11.85%)</td><td>10.61 <b>(-58.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.10 (n/a)</td><td>220.90 (n/a)</td><td>218.80 (n/a)</td><td>183.90 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>167.90 (n/a)</td><td>141.90 (n/a)</td><td>138.40 (n/a)</td><td>106.60 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>177.90 (n/a)</td><td>173.50 (n/a)</td><td>155.30 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.50 (n/a)</td><td>170.48 (n/a)</td><td>176.30 (n/a)</td><td>110.30 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>179.88 (n/a)</td><td>183.70 (n/a)</td><td>139.40 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>163.76 (n/a)</td><td>159.90 (n/a)</td><td>146.10 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>166.16 (n/a)</td><td>147.30 (n/a)</td><td>136.50 (n/a)</td><td>39.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>166.04 (n/a)</td><td>172.00 (n/a)</td><td>132.00 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>343.00 (n/a)</td><td>231.22 (n/a)</td><td>217.30 (n/a)</td><td>118.50 (n/a)</td><td>103.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>152.40 (n/a)</td><td>157.00 (n/a)</td><td>125.40 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>166.46 (n/a)</td><td>174.60 (n/a)</td><td>130.10 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.90 (n/a)</td><td>151.46 (n/a)</td><td>153.40 (n/a)</td><td>126.50 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.30 (n/a)</td><td>167.56 (n/a)</td><td>165.40 (n/a)</td><td>151.80 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>163.90 (n/a)</td><td>148.90 (n/a)</td><td>148.80 (n/a)</td><td>135.90 (n/a)</td><td>10.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>181.20 (n/a)</td><td>170.70 (n/a)</td><td>147.60 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.60 (n/a)</td><td>179.78 (n/a)</td><td>161.10 (n/a)</td><td>151.60 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>342.10 (n/a)</td><td>234.24 (n/a)</td><td>212.20 (n/a)</td><td>176.50 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>4.49 (+0.27%)</td><td>3.91 (-1.61%)</td><td>4.14 (+3.13%)</td><td>3.24 (-4.27%)</td><td>0.53 <b>(+27.14%)</b></td><td>2903.30 (+4.47%)</td><td>2439.84 (+2.27%)</td><td>2269.50 (-3.03%)</td><td>2095.20 (-0.27%)</td><td>343.62 <b>(+32.62%)</b></td><td>1765.61 (+0.27%)</td><td>1539.52 (-1.61%)</td><td>1630.02 (+3.13%)</td><td>1274.21 (-4.27%)</td><td>207.28 <b>(+27.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>4.48 (n/a)</td><td>3.98 (n/a)</td><td>4.02 (n/a)</td><td>3.38 (n/a)</td><td>0.41 (n/a)</td><td>2779.20 (n/a)</td><td>2385.64 (n/a)</td><td>2340.50 (n/a)</td><td>2100.90 (n/a)</td><td>259.11 (n/a)</td><td>1760.88 (n/a)</td><td>1564.79 (n/a)</td><td>1580.56 (n/a)</td><td>1331.09 (n/a)</td><td>163.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.14 (-2.46%)</td><td>0.94 (+3.66%)</td><td>0.98 (+5.96%)</td><td>0.67 (-1.29%)</td><td>0.17 (-2.28%)</td><td>332.20 (+1.31%)</td><td>241.66 (-3.41%)</td><td>226.80 (-5.62%)</td><td>194.00 (+2.54%)</td><td>52.65 (+5.48%)</td><td>48.64 (-2.46%)</td><td>40.32 (+3.66%)</td><td>41.61 (+5.96%)</td><td>28.41 (-1.29%)</td><td>7.34 (-2.28%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.17 (n/a)</td><td>0.91 (n/a)</td><td>0.92 (n/a)</td><td>0.67 (n/a)</td><td>0.18 (n/a)</td><td>327.90 (n/a)</td><td>250.20 (n/a)</td><td>240.30 (n/a)</td><td>189.20 (n/a)</td><td>49.92 (n/a)</td><td>49.87 (n/a)</td><td>38.89 (n/a)</td><td>39.27 (n/a)</td><td>28.78 (n/a)</td><td>7.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.26 (+1.80%)</td><td>1.01 (-1.23%)</td><td>1.07 (-4.54%)</td><td>0.60 (-3.55%)</td><td>0.26 (+1.19%)</td><td>365.70 (+3.69%)</td><td>235.04 (+1.66%)</td><td>207.10 (+4.75%)</td><td>175.20 (-1.79%)</td><td>77.52 (+5.80%)</td><td>53.86 (+1.80%)</td><td>43.05 (-1.23%)</td><td>45.57 (-4.54%)</td><td>25.81 (-3.55%)</td><td>11.21 (+1.19%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.24 (n/a)</td><td>1.02 (n/a)</td><td>1.12 (n/a)</td><td>0.63 (n/a)</td><td>0.26 (n/a)</td><td>352.70 (n/a)</td><td>231.20 (n/a)</td><td>197.70 (n/a)</td><td>178.40 (n/a)</td><td>73.26 (n/a)</td><td>52.90 (n/a)</td><td>43.59 (n/a)</td><td>47.74 (n/a)</td><td>26.76 (n/a)</td><td>11.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.52 (-0.00%)</td><td>0.52 (+0.04%)</td><td>0.52 (+0.02%)</td><td>0.52 (+0.11%)</td><td>0.00 <b>(-67.40%)</b></td><td>48654.40 (-0.11%)</td><td>48643.34 (-0.04%)</td><td>48642.70 (-0.02%)</td><td>48631.20 (+0.00%)</td><td>10.59 <b>(-67.49%)</b></td><td>353.27 (-0.00%)</td><td>353.18 (+0.04%)</td><td>353.19 (+0.02%)</td><td>353.10 (+0.11%)</td><td>0.08 <b>(-67.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48708.10 (n/a)</td><td>48660.46 (n/a)</td><td>48652.40 (n/a)</td><td>48628.80 (n/a)</td><td>32.56 (n/a)</td><td>353.29 (n/a)</td><td>353.06 (n/a)</td><td>353.11 (n/a)</td><td>352.71 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.89 (-1.40%)</td><td>0.88 (-0.85%)</td><td>0.89 (-0.39%)</td><td>0.87 (-0.82%)</td><td>0.01 <b>(-27.09%)</b></td><td>28778.00 (+0.83%)</td><td>28457.10 (+0.85%)</td><td>28378.30 (+0.39%)</td><td>28345.10 (+1.42%)</td><td>181.39 <b>(-25.30%)</b></td><td>606.10 (-1.40%)</td><td>603.73 (-0.85%)</td><td>605.39 (-0.39%)</td><td>596.98 (-0.82%)</td><td>3.82 <b>(-27.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28541.20 (n/a)</td><td>28216.58 (n/a)</td><td>28268.60 (n/a)</td><td>27947.70 (n/a)</td><td>242.83 (n/a)</td><td>614.71 (n/a)</td><td>608.89 (n/a)</td><td>607.74 (n/a)</td><td>601.93 (n/a)</td><td>5.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.22 (-3.70%)</td><td>3.19 (-2.22%)</td><td>3.20 (-2.78%)</td><td>3.14 (-0.52%)</td><td>0.04 <b>(-53.34%)</b></td><td>8024.00 (+0.52%)</td><td>7888.04 (+2.23%)</td><td>7856.00 (+2.86%)</td><td>7813.00 (+3.85%)</td><td>89.36 <b>(-51.41%)</b></td><td>2198.88 (-3.70%)</td><td>2178.18 (-2.22%)</td><td>2186.85 (-2.78%)</td><td>2141.05 (-0.52%)</td><td>24.51 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.34 (n/a)</td><td>3.26 (n/a)</td><td>3.29 (n/a)</td><td>3.15 (n/a)</td><td>0.08 (n/a)</td><td>7982.20 (n/a)</td><td>7715.78 (n/a)</td><td>7637.80 (n/a)</td><td>7523.60 (n/a)</td><td>183.90 (n/a)</td><td>2283.46 (n/a)</td><td>2227.60 (n/a)</td><td>2249.32 (n/a)</td><td>2152.28 (n/a)</td><td>52.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.68 (-6.23%)</td><td>3.42 (-3.81%)</td><td>3.55 (-2.98%)</td><td>3.06 (+0.92%)</td><td>0.30 (-9.70%)</td><td>2633.20 (-0.91%)</td><td>2368.76 (+3.84%)</td><td>2270.50 (+3.07%)</td><td>2187.70 (+6.64%)</td><td>212.46 (-6.67%)</td><td>966.28 (-6.23%)</td><td>898.03 (-3.81%)</td><td>931.03 (-2.98%)</td><td>802.80 (+0.92%)</td><td>78.25 (-9.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.93 (n/a)</td><td>3.56 (n/a)</td><td>3.66 (n/a)</td><td>3.03 (n/a)</td><td>0.33 (n/a)</td><td>2657.50 (n/a)</td><td>2281.20 (n/a)</td><td>2202.80 (n/a)</td><td>2051.50 (n/a)</td><td>227.65 (n/a)</td><td>1030.43 (n/a)</td><td>933.56 (n/a)</td><td>959.64 (n/a)</td><td>795.46 (n/a)</td><td>86.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.53 (+17.62%)</td><td>0.41 <b>(+20.18%)</b></td><td>0.35 (+9.62%)</td><td>0.35 <b>(+20.82%)</b></td><td>0.09 <b>(+38.89%)</b></td><td>3602.40 (-17.23%)</td><td>3129.02 (-15.95%)</td><td>3533.30 (-8.78%)</td><td>2371.20 (-14.98%)</td><td>618.71 (+1.16%)</td><td>28.30 (+17.62%)</td><td>22.20 <b>(+20.18%)</b></td><td>18.99 (+9.62%)</td><td>18.63 <b>(+20.82%)</b></td><td>4.77 <b>(+38.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>4352.30 (n/a)</td><td>3722.90 (n/a)</td><td>3873.20 (n/a)</td><td>2789.00 (n/a)</td><td>611.60 (n/a)</td><td>24.06 (n/a)</td><td>18.47 (n/a)</td><td>17.33 (n/a)</td><td>15.42 (n/a)</td><td>3.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>6.42 (+17.62%)</td><td>5.52 <b>(+36.84%)</b></td><td>4.98 <b>(+42.27%)</b></td><td>4.92 <b>(+55.53%)</b></td><td>0.78 <b>(-21.26%)</b></td><td>1351.50 <b>(-35.70%)</b></td><td>1222.82 <b>(-29.02%)</b></td><td>1334.90 <b>(-29.71%)</b></td><td>1035.80 (-14.98%)</td><td>164.69 <b>(-57.00%)</b></td><td>1984.19 (+17.62%)</td><td>1706.77 <b>(+36.84%)</b></td><td>1539.58 <b>(+42.27%)</b></td><td>1520.74 <b>(+55.53%)</b></td><td>241.79 <b>(-21.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>5.46 (n/a)</td><td>4.04 (n/a)</td><td>3.50 (n/a)</td><td>3.16 (n/a)</td><td>0.99 (n/a)</td><td>2101.90 (n/a)</td><td>1722.70 (n/a)</td><td>1899.20 (n/a)</td><td>1218.30 (n/a)</td><td>382.96 (n/a)</td><td>1686.98 (n/a)</td><td>1247.29 (n/a)</td><td>1082.13 (n/a)</td><td>977.81 (n/a)</td><td>307.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>13.51 (n/a)</td><td>12.13 (n/a)</td><td>11.76 (n/a)</td><td>10.96 (n/a)</td><td>1.21 (n/a)</td><td>13.50 (n/a)</td><td>12.12 (n/a)</td><td>11.75 (n/a)</td><td>10.95 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>25.13 (+2.02%)</td><td>24.21 (+0.02%)</td><td>23.94 (-0.91%)</td><td>23.12 (-2.22%)</td><td>0.88 <b>(+122.46%)</b></td><td>25.11 (+2.02%)</td><td>24.19 (+0.02%)</td><td>23.92 (-0.91%)</td><td>23.10 (-2.22%)</td><td>0.88 <b>(+122.46%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>24.63 (n/a)</td><td>24.20 (n/a)</td><td>24.16 (n/a)</td><td>23.64 (n/a)</td><td>0.40 (n/a)</td><td>24.61 (n/a)</td><td>24.19 (n/a)</td><td>24.14 (n/a)</td><td>23.63 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>40.13 (-1.64%)</td><td>38.14 (-3.75%)</td><td>38.98 (-2.04%)</td><td>34.65 (-7.55%)</td><td>2.22 <b>(+74.14%)</b></td><td>40.10 (-1.64%)</td><td>38.12 (-3.75%)</td><td>38.95 (-2.04%)</td><td>34.63 (-7.55%)</td><td>2.21 <b>(+74.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>40.79 (n/a)</td><td>39.63 (n/a)</td><td>39.79 (n/a)</td><td>37.48 (n/a)</td><td>1.27 (n/a)</td><td>40.77 (n/a)</td><td>39.61 (n/a)</td><td>39.76 (n/a)</td><td>37.46 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>45.56 (+4.55%)</td><td>42.16 (-1.08%)</td><td>42.18 (-1.37%)</td><td>38.61 (-7.49%)</td><td>2.54 <b>(+207.22%)</b></td><td>45.53 (+4.55%)</td><td>42.14 (-1.08%)</td><td>42.15 (-1.37%)</td><td>38.59 (-7.49%)</td><td>2.54 <b>(+207.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>43.58 (n/a)</td><td>42.62 (n/a)</td><td>42.76 (n/a)</td><td>41.74 (n/a)</td><td>0.83 (n/a)</td><td>43.55 (n/a)</td><td>42.60 (n/a)</td><td>42.74 (n/a)</td><td>41.71 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>13.51 (n/a)</td><td>12.63 (n/a)</td><td>13.22 (n/a)</td><td>10.42 (n/a)</td><td>1.28 (n/a)</td><td>13.50 (n/a)</td><td>12.62 (n/a)</td><td>13.21 (n/a)</td><td>10.41 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>24.61 (-1.30%)</td><td>23.61 (-1.48%)</td><td>23.56 (-1.20%)</td><td>22.43 (-2.78%)</td><td>0.89 <b>(+30.78%)</b></td><td>24.60 (-1.30%)</td><td>23.60 (-1.48%)</td><td>23.55 (-1.20%)</td><td>22.42 (-2.78%)</td><td>0.88 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>24.94 (n/a)</td><td>23.97 (n/a)</td><td>23.85 (n/a)</td><td>23.07 (n/a)</td><td>0.68 (n/a)</td><td>24.92 (n/a)</td><td>23.95 (n/a)</td><td>23.83 (n/a)</td><td>23.06 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>41.41 (-4.23%)</td><td>39.09 (-1.50%)</td><td>39.41 (+1.12%)</td><td>36.87 (-3.44%)</td><td>1.69 (-16.70%)</td><td>41.38 (-4.23%)</td><td>39.07 (-1.50%)</td><td>39.39 (+1.12%)</td><td>36.85 (-3.44%)</td><td>1.69 (-16.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>43.23 (n/a)</td><td>39.68 (n/a)</td><td>38.98 (n/a)</td><td>38.19 (n/a)</td><td>2.03 (n/a)</td><td>43.21 (n/a)</td><td>39.66 (n/a)</td><td>38.95 (n/a)</td><td>38.16 (n/a)</td><td>2.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>45.04 (+1.60%)</td><td>43.46 (+2.60%)</td><td>43.29 (+1.84%)</td><td>42.03 (+4.15%)</td><td>1.14 <b>(-39.28%)</b></td><td>45.01 (+1.60%)</td><td>43.44 (+2.60%)</td><td>43.26 (+1.84%)</td><td>42.01 (+4.15%)</td><td>1.14 <b>(-39.28%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>44.33 (n/a)</td><td>42.36 (n/a)</td><td>42.51 (n/a)</td><td>40.36 (n/a)</td><td>1.88 (n/a)</td><td>44.30 (n/a)</td><td>42.34 (n/a)</td><td>42.48 (n/a)</td><td>40.33 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>9.14 (-7.75%)</td><td>8.83 (+0.37%)</td><td>8.69 (-1.06%)</td><td>8.59 (+4.91%)</td><td>0.25 <b>(-63.37%)</b></td><td>9.12 (-7.75%)</td><td>8.81 (+0.37%)</td><td>8.67 (-1.06%)</td><td>8.57 (+4.91%)</td><td>0.25 <b>(-63.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>9.90 (n/a)</td><td>8.80 (n/a)</td><td>8.78 (n/a)</td><td>8.19 (n/a)</td><td>0.69 (n/a)</td><td>9.88 (n/a)</td><td>8.78 (n/a)</td><td>8.76 (n/a)</td><td>8.17 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.80 (-12.74%)</td><td>0.78 (-4.27%)</td><td>0.77 (+0.26%)</td><td>0.75 (+5.75%)</td><td>0.02 <b>(-74.18%)</b></td><td>0.79 (-12.74%)</td><td>0.76 (-4.27%)</td><td>0.76 (+0.26%)</td><td>0.74 (+5.75%)</td><td>0.02 <b>(-74.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.92 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.71 (n/a)</td><td>0.09 (n/a)</td><td>0.90 (n/a)</td><td>0.80 (n/a)</td><td>0.76 (n/a)</td><td>0.70 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.21 (-4.28%)</td><td>1.09 (+1.15%)</td><td>1.08 (+10.76%)</td><td>0.99 (+5.17%)</td><td>0.09 <b>(-45.13%)</b></td><td>1.19 (-4.28%)</td><td>1.07 (+1.15%)</td><td>1.07 (+10.76%)</td><td>0.98 (+5.17%)</td><td>0.09 <b>(-45.13%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>1.26 (n/a)</td><td>1.07 (n/a)</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.16 (n/a)</td><td>1.25 (n/a)</td><td>1.06 (n/a)</td><td>0.96 (n/a)</td><td>0.93 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>16.33 (+0.70%)</td><td>15.45 (+4.31%)</td><td>15.57 (+6.50%)</td><td>14.47 (+5.92%)</td><td>0.69 <b>(-27.48%)</b></td><td>16.14 (+0.70%)</td><td>15.28 (+4.31%)</td><td>15.39 (+6.50%)</td><td>14.31 (+5.92%)</td><td>0.68 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>16.22 (n/a)</td><td>14.82 (n/a)</td><td>14.62 (n/a)</td><td>13.66 (n/a)</td><td>0.95 (n/a)</td><td>16.03 (n/a)</td><td>14.64 (n/a)</td><td>14.45 (n/a)</td><td>13.51 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>12.06 (+1.58%)</td><td>11.90 (+3.86%)</td><td>12.04 (+2.82%)</td><td>11.53 (+11.80%)</td><td>0.23 <b>(-64.72%)</b></td><td>11.85 (+1.58%)</td><td>11.69 (+3.86%)</td><td>11.83 (+2.82%)</td><td>11.33 (+11.80%)</td><td>0.23 <b>(-64.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>11.88 (n/a)</td><td>11.46 (n/a)</td><td>11.71 (n/a)</td><td>10.31 (n/a)</td><td>0.65 (n/a)</td><td>11.67 (n/a)</td><td>11.26 (n/a)</td><td>11.50 (n/a)</td><td>10.13 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>8.85 (+5.33%)</td><td>8.19 (+12.30%)</td><td>8.25 (+12.43%)</td><td>7.30 <b>(+20.75%)</b></td><td>0.62 <b>(-37.16%)</b></td><td>8.69 (+5.33%)</td><td>8.05 (+12.30%)</td><td>8.11 (+12.43%)</td><td>7.17 <b>(+20.75%)</b></td><td>0.61 <b>(-37.16%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>8.40 (n/a)</td><td>7.30 (n/a)</td><td>7.34 (n/a)</td><td>6.04 (n/a)</td><td>0.98 (n/a)</td><td>8.25 (n/a)</td><td>7.17 (n/a)</td><td>7.21 (n/a)</td><td>5.94 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>6.55 (-3.64%)</td><td>6.15 (+12.09%)</td><td>6.20 (+16.06%)</td><td>5.56 (+17.00%)</td><td>0.42 <b>(-49.11%)</b></td><td>6.45 (-3.64%)</td><td>6.05 (+12.09%)</td><td>6.10 (+16.06%)</td><td>5.47 (+17.00%)</td><td>0.42 <b>(-49.11%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>6.80 (n/a)</td><td>5.49 (n/a)</td><td>5.34 (n/a)</td><td>4.75 (n/a)</td><td>0.83 (n/a)</td><td>6.69 (n/a)</td><td>5.40 (n/a)</td><td>5.25 (n/a)</td><td>4.68 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>13.59 (n/a)</td><td>13.38 (n/a)</td><td>13.33 (n/a)</td><td>13.29 (n/a)</td><td>0.13 (n/a)</td><td>13.58 (n/a)</td><td>13.37 (n/a)</td><td>13.32 (n/a)</td><td>13.28 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>13.39 (n/a)</td><td>12.90 (n/a)</td><td>13.23 (n/a)</td><td>11.64 (n/a)</td><td>0.73 (n/a)</td><td>13.38 (n/a)</td><td>12.89 (n/a)</td><td>13.22 (n/a)</td><td>11.63 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.90 (n/a)</td><td>158.60 (n/a)</td><td>160.50 (n/a)</td><td>136.10 (n/a)</td><td>13.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>151.80 (n/a)</td><td>147.50 (n/a)</td><td>129.10 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>166.54 (n/a)</td><td>160.20 (n/a)</td><td>128.30 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>151.00 (n/a)</td><td>145.30 (n/a)</td><td>128.00 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>177.88 (n/a)</td><td>184.00 (n/a)</td><td>146.20 (n/a)</td><td>31.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>180.44 (n/a)</td><td>197.00 (n/a)</td><td>130.30 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>168.12 (n/a)</td><td>171.60 (n/a)</td><td>142.90 (n/a)</td><td>16.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.30 (n/a)</td><td>210.22 (n/a)</td><td>212.30 (n/a)</td><td>181.30 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-16.90%)</td><td>0.05 <b>(-22.28%)</b></td><td>0.04 <b>(-30.61%)</b></td><td>0.04 (-17.22%)</td><td>0.01 (+8.84%)</td><td>201.80 <b>(+20.77%)</b></td><td>182.96 <b>(+29.36%)</b></td><td>197.70 <b>(+44.10%)</b></td><td>155.70 <b>(+20.42%)</b></td><td>22.80 <b>(+54.56%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.10 (n/a)</td><td>141.44 (n/a)</td><td>137.20 (n/a)</td><td>129.30 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-14.45%)</td><td>0.05 (+14.55%)</td><td>0.05 <b>(+30.91%)</b></td><td>0.04 <b>(+82.37%)</b></td><td>0.01 <b>(-56.58%)</b></td><td>207.80 <b>(-45.17%)</b></td><td>165.12 <b>(-23.26%)</b></td><td>152.20 <b>(-23.59%)</b></td><td>143.50 (+16.86%)</td><td>27.32 <b>(-72.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>379.00 (n/a)</td><td>215.16 (n/a)</td><td>199.20 (n/a)</td><td>122.80 (n/a)</td><td>100.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 <b>(-20.77%)</b></td><td>0.04 (-11.48%)</td><td>0.04 (-8.52%)</td><td>0.04 (+9.40%)</td><td>0.01 <b>(-51.25%)</b></td><td>228.50 (-8.56%)</td><td>207.48 (+9.60%)</td><td>218.00 (+9.33%)</td><td>172.40 <b>(+26.21%)</b></td><td>24.96 <b>(-42.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>189.30 (n/a)</td><td>199.40 (n/a)</td><td>136.60 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-6.69%)</td><td>0.04 (+1.47%)</td><td>0.05 (+7.43%)</td><td>0.02 (-2.30%)</td><td>0.01 (-0.19%)</td><td>359.20 (+2.34%)</td><td>213.28 (-0.92%)</td><td>179.10 (-6.91%)</td><td>165.20 (+7.20%)</td><td>82.49 (+5.69%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.00 (n/a)</td><td>215.26 (n/a)</td><td>192.40 (n/a)</td><td>154.10 (n/a)</td><td>78.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-4.22%)</td><td>0.05 (-1.88%)</td><td>0.05 (+5.47%)</td><td>0.04 (-8.12%)</td><td>0.01 (+9.84%)</td><td>201.80 (+8.85%)</td><td>168.14 (+2.27%)</td><td>160.90 (-5.24%)</td><td>145.40 (+4.38%)</td><td>21.89 <b>(+27.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>164.40 (n/a)</td><td>169.80 (n/a)</td><td>139.30 (n/a)</td><td>17.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 <b>(+38.02%)</b></td><td>0.05 (+10.25%)</td><td>0.05 (+16.90%)</td><td>0.04 (-12.37%)</td><td>0.01 <b>(+592.53%)</b></td><td>229.90 (+14.09%)</td><td>180.36 (-5.15%)</td><td>161.10 (-14.45%)</td><td>132.10 <b>(-27.54%)</b></td><td>43.30 <b>(+494.03%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>190.16 (n/a)</td><td>188.30 (n/a)</td><td>182.30 (n/a)</td><td>7.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-8.61%)</td><td>0.04 (+2.01%)</td><td>0.04 (-7.05%)</td><td>0.04 <b>(+61.77%)</b></td><td>0.00 <b>(-73.85%)</b></td><td>209.70 <b>(-38.20%)</b></td><td>199.80 (-7.66%)</td><td>202.60 (+7.59%)</td><td>180.70 (+9.45%)</td><td>11.51 <b>(-83.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>339.30 (n/a)</td><td>216.38 (n/a)</td><td>188.30 (n/a)</td><td>165.10 (n/a)</td><td>69.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 <b>(+51.22%)</b></td><td>0.05 (+13.55%)</td><td>0.04 (+4.36%)</td><td>0.04 (+2.04%)</td><td>0.01 <b>(+241.11%)</b></td><td>232.60 (-2.02%)</td><td>187.36 (-8.77%)</td><td>190.10 (-4.18%)</td><td>125.80 <b>(-33.89%)</b></td><td>38.77 <b>(+107.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.40 (n/a)</td><td>205.36 (n/a)</td><td>198.40 (n/a)</td><td>190.30 (n/a)</td><td>18.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (+0.98%)</td><td>0.04 (-5.48%)</td><td>0.04 (-3.34%)</td><td>0.03 (-8.30%)</td><td>0.01 <b>(+43.72%)</b></td><td>241.00 (+9.05%)</td><td>203.16 (+7.33%)</td><td>200.60 (+3.46%)</td><td>159.60 (-0.99%)</td><td>35.91 <b>(+59.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>189.28 (n/a)</td><td>193.90 (n/a)</td><td>161.20 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (-10.76%)</td><td>0.03 (-8.95%)</td><td>0.03 (-11.94%)</td><td>0.03 (-1.11%)</td><td>0.00 <b>(-23.96%)</b></td><td>321.00 (+1.10%)</td><td>246.98 (+8.60%)</td><td>237.60 (+13.58%)</td><td>217.60 (+12.05%)</td><td>42.64 (-15.96%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.50 (n/a)</td><td>227.42 (n/a)</td><td>209.20 (n/a)</td><td>194.20 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-8.35%)</td><td>0.05 (-0.73%)</td><td>0.05 (+10.96%)</td><td>0.04 (+8.25%)</td><td>0.00 <b>(-39.00%)</b></td><td>189.90 (-7.64%)</td><td>170.06 (-0.60%)</td><td>162.00 (-9.85%)</td><td>152.20 (+9.10%)</td><td>17.91 <b>(-35.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>171.08 (n/a)</td><td>179.70 (n/a)</td><td>139.50 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-13.90%)</td><td>0.04 (-1.18%)</td><td>0.04 (-4.76%)</td><td>0.03 (+1.47%)</td><td>0.01 <b>(-37.28%)</b></td><td>248.90 (-1.43%)</td><td>201.40 (-1.78%)</td><td>206.40 (+4.98%)</td><td>155.60 (+16.12%)</td><td>34.41 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>205.04 (n/a)</td><td>196.60 (n/a)</td><td>134.00 (n/a)</td><td>49.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 <b>(+27.34%)</b></td><td>0.05 (+18.99%)</td><td>0.05 (+16.83%)</td><td>0.04 (+9.15%)</td><td>0.01 <b>(+72.26%)</b></td><td>228.90 (-8.40%)</td><td>170.26 (-14.15%)</td><td>162.70 (-14.41%)</td><td>127.00 <b>(-21.51%)</b></td><td>39.64 <b>(+22.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>198.32 (n/a)</td><td>190.10 (n/a)</td><td>161.80 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-3.59%)</td><td>0.05 (-5.10%)</td><td>0.05 (-9.79%)</td><td>0.04 (-8.50%)</td><td>0.01 (+15.71%)</td><td>198.80 (+9.29%)</td><td>166.12 (+6.24%)</td><td>174.00 (+10.90%)</td><td>132.90 (+3.75%)</td><td>28.59 <b>(+28.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.90 (n/a)</td><td>156.36 (n/a)</td><td>156.90 (n/a)</td><td>128.10 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-10.60%)</td><td>0.05 (-2.05%)</td><td>0.05 (+0.55%)</td><td>0.04 (+7.29%)</td><td>0.01 <b>(-36.72%)</b></td><td>183.90 (-6.79%)</td><td>161.82 (+0.40%)</td><td>165.10 (-0.54%)</td><td>133.80 (+11.87%)</td><td>19.68 <b>(-33.42%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>161.18 (n/a)</td><td>166.00 (n/a)</td><td>119.60 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (+18.05%)</td><td>0.04 (-7.72%)</td><td>0.04 (-8.45%)</td><td>0.03 <b>(-32.84%)</b></td><td>0.01 <b>(+205.70%)</b></td><td>306.60 <b>(+48.91%)</b></td><td>217.36 (+17.50%)</td><td>199.30 (+9.27%)</td><td>138.80 (-15.26%)</td><td>71.83 <b>(+291.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.90 (n/a)</td><td>184.98 (n/a)</td><td>182.40 (n/a)</td><td>163.80 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (+15.39%)</td><td>0.04 (-2.55%)</td><td>0.04 (-6.23%)</td><td>0.03 (-14.27%)</td><td>0.01 <b>(+163.73%)</b></td><td>244.90 (+16.62%)</td><td>197.34 (+5.34%)</td><td>196.70 (+6.67%)</td><td>148.70 (-13.29%)</td><td>37.74 <b>(+162.82%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>187.34 (n/a)</td><td>184.40 (n/a)</td><td>171.50 (n/a)</td><td>14.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-4.87%)</td><td>0.04 (-9.68%)</td><td>0.04 (+0.58%)</td><td>0.02 <b>(-27.28%)</b></td><td>0.01 <b>(+77.11%)</b></td><td>330.60 <b>(+37.52%)</b></td><td>228.96 (+15.80%)</td><td>189.10 (-0.58%)</td><td>180.30 (+5.13%)</td><td>66.40 <b>(+145.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>197.72 (n/a)</td><td>190.20 (n/a)</td><td>171.50 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.21 (-0.60%)</td><td>0.21 (-0.18%)</td><td>0.21 (-0.08%)</td><td>0.21 (-0.03%)</td><td>0.00 <b>(-49.55%)</b></td><td>40908.50 (+0.03%)</td><td>40840.72 (+0.18%)</td><td>40872.90 (+0.08%)</td><td>40660.30 (+0.60%)</td><td>102.10 <b>(-49.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40898.10 (n/a)</td><td>40766.32 (n/a)</td><td>40842.20 (n/a)</td><td>40417.80 (n/a)</td><td>201.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 <b>(+33.69%)</b></td><td>0.05 (+10.57%)</td><td>0.04 (+0.44%)</td><td>0.04 (+9.33%)</td><td>0.01 <b>(+98.41%)</b></td><td>202.20 (-8.55%)</td><td>173.66 (-7.86%)</td><td>184.60 (-0.43%)</td><td>124.30 <b>(-25.21%)</b></td><td>30.69 <b>(+34.19%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>188.48 (n/a)</td><td>185.40 (n/a)</td><td>166.20 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 <b>(-27.91%)</b></td><td>0.06 (-7.51%)</td><td>0.07 (+0.41%)</td><td>0.06 (-7.47%)</td><td>0.00 <b>(-65.89%)</b></td><td>217.80 (+8.09%)</td><td>190.84 (+5.94%)</td><td>185.10 (-0.38%)</td><td>181.70 <b>(+38.70%)</b></td><td>15.14 <b>(-47.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>180.14 (n/a)</td><td>185.80 (n/a)</td><td>131.00 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (+19.37%)</td><td>0.04 (-2.17%)</td><td>0.04 (-6.52%)</td><td>0.02 <b>(-35.00%)</b></td><td>0.01 <b>(+169.26%)</b></td><td>368.00 <b>(+53.85%)</b></td><td>223.42 (+11.03%)</td><td>211.40 (+6.98%)</td><td>148.90 (-16.21%)</td><td>85.27 <b>(+259.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.20 (n/a)</td><td>201.22 (n/a)</td><td>197.60 (n/a)</td><td>177.70 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.07 (-8.00%)</td><td>0.06 (-5.09%)</td><td>0.06 (+6.10%)</td><td>0.04 (-3.08%)</td><td>0.01 (-13.71%)</td><td>238.50 (+3.16%)</td><td>188.86 (+4.81%)</td><td>179.80 (-5.77%)</td><td>145.50 (+8.66%)</td><td>37.73 (-0.86%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>180.20 (n/a)</td><td>190.80 (n/a)</td><td>133.90 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-7.83%)</td><td>0.05 (+0.33%)</td><td>0.05 (+5.23%)</td><td>0.04 (+3.22%)</td><td>0.00 <b>(-42.83%)</b></td><td>205.50 (-3.11%)</td><td>180.50 (-1.77%)</td><td>180.10 (-5.01%)</td><td>161.60 (+8.46%)</td><td>17.75 <b>(-40.70%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>183.76 (n/a)</td><td>189.60 (n/a)</td><td>149.00 (n/a)</td><td>29.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-6.65%)</td><td>0.05 (-10.03%)</td><td>0.05 (-10.21%)</td><td>0.04 (-15.91%)</td><td>0.01 (+10.29%)</td><td>230.80 (+18.91%)</td><td>191.06 (+11.86%)</td><td>190.40 (+11.41%)</td><td>160.00 (+7.17%)</td><td>28.63 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>170.80 (n/a)</td><td>170.90 (n/a)</td><td>149.30 (n/a)</td><td>20.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 <b>(-22.38%)</b></td><td>0.05 (+2.86%)</td><td>0.04 (+13.37%)</td><td>0.04 (+14.27%)</td><td>0.00 <b>(-73.32%)</b></td><td>193.70 (-12.47%)</td><td>182.04 (-6.27%)</td><td>186.90 (-11.80%)</td><td>166.10 <b>(+28.86%)</b></td><td>11.66 <b>(-69.09%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>194.22 (n/a)</td><td>211.90 (n/a)</td><td>128.90 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (-8.03%)</td><td>0.05 (+9.39%)</td><td>0.05 <b>(+20.71%)</b></td><td>0.05 <b>(+21.19%)</b></td><td>0.00 <b>(-58.84%)</b></td><td>194.90 (-17.49%)</td><td>181.50 (-10.93%)</td><td>180.20 (-17.15%)</td><td>161.80 (+8.74%)</td><td>13.82 <b>(-63.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>203.78 (n/a)</td><td>217.50 (n/a)</td><td>148.80 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (-7.39%)</td><td>0.04 (-8.09%)</td><td>0.04 (-13.38%)</td><td>0.03 (-4.27%)</td><td>0.01 (+2.75%)</td><td>236.70 (+4.46%)</td><td>203.64 (+9.31%)</td><td>214.50 (+15.45%)</td><td>158.80 (+8.03%)</td><td>35.48 (+17.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>186.30 (n/a)</td><td>185.80 (n/a)</td><td>147.00 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.06 (+16.92%)</td><td>0.05 (+13.48%)</td><td>0.05 (+2.97%)</td><td>0.04 <b>(+42.12%)</b></td><td>0.01 (-6.85%)</td><td>221.60 <b>(-29.63%)</b></td><td>192.00 (-13.59%)</td><td>201.80 (-2.84%)</td><td>149.60 (-14.47%)</td><td>29.60 <b>(-45.95%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.90 (n/a)</td><td>222.20 (n/a)</td><td>207.70 (n/a)</td><td>174.90 (n/a)</td><td>54.76 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (+1.94%)</td><td>0.04 (-7.86%)</td><td>0.04 (-4.43%)</td><td>0.03 <b>(-32.41%)</b></td><td>0.01 <b>(+105.00%)</b></td><td>316.30 <b>(+47.94%)</b></td><td>215.44 (+13.15%)</td><td>191.60 (+4.64%)</td><td>164.40 (-1.91%)</td><td>59.45 <b>(+206.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.80 (n/a)</td><td>190.40 (n/a)</td><td>183.10 (n/a)</td><td>167.60 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (+6.65%)</td><td>0.04 (+8.23%)</td><td>0.04 (+5.33%)</td><td>0.03 (+5.40%)</td><td>0.01 (-7.44%)</td><td>288.00 (-5.11%)</td><td>215.12 (-8.37%)</td><td>196.60 (-5.07%)</td><td>176.10 (-6.23%)</td><td>43.94 (-15.87%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.50 (n/a)</td><td>234.76 (n/a)</td><td>207.10 (n/a)</td><td>187.80 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 <b>(-21.79%)</b></td><td>0.04 (-6.93%)</td><td>0.04 (-5.03%)</td><td>0.03 <b>(+28.83%)</b></td><td>0.01 <b>(-51.79%)</b></td><td>254.50 <b>(-22.38%)</b></td><td>214.98 (+1.42%)</td><td>203.40 (+5.33%)</td><td>185.70 <b>(+27.89%)</b></td><td>32.61 <b>(-53.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.90 (n/a)</td><td>211.96 (n/a)</td><td>193.10 (n/a)</td><td>145.20 (n/a)</td><td>70.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.05 (+11.72%)</td><td>0.04 <b>(+20.32%)</b></td><td>0.04 (+7.46%)</td><td>0.04 <b>(+67.73%)</b></td><td>0.00 <b>(-75.25%)</b></td><td>209.30 <b>(-40.39%)</b></td><td>198.90 (-19.80%)</td><td>201.20 (-6.94%)</td><td>189.70 (-10.48%)</td><td>7.78 <b>(-86.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.10 (n/a)</td><td>248.02 (n/a)</td><td>216.20 (n/a)</td><td>211.90 (n/a)</td><td>59.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.04 (+10.47%)</td><td>0.04 (+1.23%)</td><td>0.04 (+1.69%)</td><td>0.03 (-11.30%)</td><td>0.00 <b>(+395.67%)</b></td><td>258.10 (+12.76%)</td><td>222.14 (-0.39%)</td><td>220.00 (-1.70%)</td><td>195.80 (-9.44%)</td><td>23.47 <b>(+409.73%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.90 (n/a)</td><td>223.00 (n/a)</td><td>223.80 (n/a)</td><td>216.20 (n/a)</td><td>4.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.76 <b>(+20.77%)</b></td><td>0.60 (+12.41%)</td><td>0.59 (+10.40%)</td><td>0.39 (-11.93%)</td><td>0.15 <b>(+89.70%)</b></td><td>249.90 (+13.54%)</td><td>172.00 (-7.61%)</td><td>168.00 (-9.43%)</td><td>129.10 (-17.24%)</td><td>48.08 <b>(+79.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>220.10 (n/a)</td><td>186.16 (n/a)</td><td>185.50 (n/a)</td><td>156.00 (n/a)</td><td>26.85 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.73 (+9.40%)</td><td>0.57 (+5.76%)</td><td>0.58 (+5.60%)</td><td>0.39 (-12.22%)</td><td>0.13 <b>(+57.47%)</b></td><td>250.20 (+13.88%)</td><td>180.12 (-2.88%)</td><td>170.90 (-5.32%)</td><td>135.50 (-8.63%)</td><td>44.41 <b>(+67.57%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.66 (n/a)</td><td>0.54 (n/a)</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>219.70 (n/a)</td><td>185.46 (n/a)</td><td>180.50 (n/a)</td><td>148.30 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.78 (-5.97%)</td><td>0.54 (-8.84%)</td><td>0.51 (-4.83%)</td><td>0.41 (-14.37%)</td><td>0.15 (+4.97%)</td><td>238.90 (+16.82%)</td><td>191.68 (+11.21%)</td><td>191.60 (+5.10%)</td><td>125.60 (+6.35%)</td><td>43.42 <b>(+33.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.83 (n/a)</td><td>0.59 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>204.50 (n/a)</td><td>172.36 (n/a)</td><td>182.30 (n/a)</td><td>118.10 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.77 (+10.53%)</td><td>0.60 (+12.13%)</td><td>0.61 <b>(+25.46%)</b></td><td>0.47 <b>(+31.60%)</b></td><td>0.11 <b>(-23.54%)</b></td><td>209.30 <b>(-24.00%)</b></td><td>169.52 (-13.96%)</td><td>162.20 <b>(-20.29%)</b></td><td>128.40 (-9.51%)</td><td>30.54 <b>(-44.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.69 (n/a)</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.15 (n/a)</td><td>275.40 (n/a)</td><td>197.02 (n/a)</td><td>203.50 (n/a)</td><td>141.90 (n/a)</td><td>55.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.59 <b>(+34.56%)</b></td><td>0.51 <b>(+47.15%)</b></td><td>0.53 <b>(+62.00%)</b></td><td>0.40 <b>(+30.55%)</b></td><td>0.07 <b>(+35.96%)</b></td><td>183.30 <b>(-23.40%)</b></td><td>146.96 <b>(-31.94%)</b></td><td>139.70 <b>(-38.27%)</b></td><td>124.20 <b>(-25.67%)</b></td><td>23.11 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>239.30 (n/a)</td><td>215.94 (n/a)</td><td>226.30 (n/a)</td><td>167.10 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.63 (+12.47%)</td><td>0.50 (+14.18%)</td><td>0.43 (+8.13%)</td><td>0.42 (+5.96%)</td><td>0.10 <b>(+33.56%)</b></td><td>175.10 (-5.61%)</td><td>153.02 (-11.54%)</td><td>170.90 (-7.52%)</td><td>116.10 (-11.10%)</td><td>27.46 (+15.20%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>185.50 (n/a)</td><td>172.98 (n/a)</td><td>184.80 (n/a)</td><td>130.60 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.48 (-11.87%)</td><td>0.41 (-11.93%)</td><td>0.40 (-9.47%)</td><td>0.35 (-10.42%)</td><td>0.05 (-15.40%)</td><td>212.10 (+11.63%)</td><td>182.68 (+13.41%)</td><td>182.30 (+10.48%)</td><td>153.80 (+13.42%)</td><td>24.19 (+8.78%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>190.00 (n/a)</td><td>161.08 (n/a)</td><td>165.00 (n/a)</td><td>135.60 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.55 (+6.26%)</td><td>0.44 (+10.06%)</td><td>0.41 (+11.46%)</td><td>0.34 (-3.57%)</td><td>0.10 <b>(+40.69%)</b></td><td>216.30 (+3.69%)</td><td>175.80 (-7.39%)</td><td>181.00 (-10.31%)</td><td>133.40 (-5.92%)</td><td>38.40 <b>(+38.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>208.60 (n/a)</td><td>189.82 (n/a)</td><td>201.80 (n/a)</td><td>141.80 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>1.04 <b>(+24.30%)</b></td><td>0.79 (+9.46%)</td><td>0.78 (+11.51%)</td><td>0.65 (-1.66%)</td><td>0.15 <b>(+103.92%)</b></td><td>202.50 (+1.71%)</td><td>170.58 (-6.89%)</td><td>168.50 (-10.32%)</td><td>126.00 (-19.54%)</td><td>29.71 <b>(+63.68%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.84 (n/a)</td><td>0.72 (n/a)</td><td>0.70 (n/a)</td><td>0.66 (n/a)</td><td>0.08 (n/a)</td><td>199.10 (n/a)</td><td>183.20 (n/a)</td><td>187.90 (n/a)</td><td>156.60 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.98 (+11.95%)</td><td>0.79 (+3.21%)</td><td>0.76 (+3.91%)</td><td>0.65 (-10.49%)</td><td>0.12 <b>(+87.00%)</b></td><td>203.10 (+11.72%)</td><td>169.88 (-1.87%)</td><td>171.60 (-3.76%)</td><td>133.50 (-10.70%)</td><td>24.67 <b>(+85.28%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.07 (n/a)</td><td>181.80 (n/a)</td><td>173.12 (n/a)</td><td>178.30 (n/a)</td><td>149.50 (n/a)</td><td>13.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.77 (-15.75%)</td><td>0.61 (-17.16%)</td><td>0.65 (-12.86%)</td><td>0.37 <b>(-38.53%)</b></td><td>0.15 (+19.09%)</td><td>351.30 <b>(+62.64%)</b></td><td>227.14 <b>(+25.55%)</b></td><td>200.20 (+14.79%)</td><td>171.30 (+18.71%)</td><td>71.60 <b>(+138.03%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.91 (n/a)</td><td>0.74 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.12 (n/a)</td><td>216.00 (n/a)</td><td>180.92 (n/a)</td><td>174.40 (n/a)</td><td>144.30 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.00 (+2.33%)</td><td>0.00 (+3.83%)</td><td>0.00 (+2.33%)</td><td>0.00 (+13.51%)</td><td>0.00 <b>(-66.67%)</b></td><td>967.19 (-11.82%)</td><td>943.19 (-3.36%)</td><td>940.74 (-0.66%)</td><td>924.24 (-1.92%)</td><td>16.26 <b>(-75.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1096.81 (n/a)</td><td>976.00 (n/a)</td><td>947.00 (n/a)</td><td>942.33 (n/a)</td><td>67.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.01 (-1.22%)</td><td>0.01 (+1.26%)</td><td>0.01 (+0.00%)</td><td>0.01 (+9.59%)</td><td>0.00 <b>(-85.52%)</b></td><td>1025.59 (-8.01%)</td><td>1016.55 (-1.19%)</td><td>1013.35 (+0.28%)</td><td>1007.22 (+1.19%)</td><td>7.94 <b>(-83.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1114.90 (n/a)</td><td>1028.83 (n/a)</td><td>1010.57 (n/a)</td><td>995.35 (n/a)</td><td>49.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.97 (-0.28%)</td><td>0.96 (+2.14%)</td><td>0.97 (+2.91%)</td><td>0.96 (+2.89%)</td><td>0.01 <b>(-66.02%)</b></td><td>2192.96 (-2.81%)</td><td>2176.57 (-2.12%)</td><td>2170.60 (-2.82%)</td><td>2161.57 (+0.27%)</td><td>13.05 <b>(-66.70%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2256.37 (n/a)</td><td>2223.61 (n/a)</td><td>2233.70 (n/a)</td><td>2155.66 (n/a)</td><td>39.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.44 (-3.70%)</td><td>0.43 (-2.82%)</td><td>0.43 (-2.12%)</td><td>0.43 (-2.80%)</td><td>0.00 <b>(-31.75%)</b></td><td>1219.59 (+2.88%)</td><td>1205.76 (+2.89%)</td><td>1207.37 (+2.15%)</td><td>1185.61 (+3.85%)</td><td>13.43 <b>(-27.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.01 (n/a)</td><td>1185.47 (n/a)</td><td>1171.91 (n/a)</td><td>1181.98 (n/a)</td><td>1141.65 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.38 (+0.16%)</td><td>0.37 (-0.13%)</td><td>0.37 (+0.41%)</td><td>0.36 (-1.37%)</td><td>0.01 <b>(+35.84%)</b></td><td>1452.04 (+1.38%)</td><td>1413.30 (+0.13%)</td><td>1411.56 (-0.42%)</td><td>1377.40 (-0.16%)</td><td>27.48 <b>(+37.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1432.28 (n/a)</td><td>1411.41 (n/a)</td><td>1417.51 (n/a)</td><td>1379.55 (n/a)</td><td>19.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>0.38 (+3.50%)</td><td>0.37 (+2.13%)</td><td>0.36 (+2.07%)</td><td>0.36 (+0.03%)</td><td>0.01 <b>(+131.23%)</b></td><td>1475.86 (-0.04%)</td><td>1431.88 (-2.06%)</td><td>1436.53 (-2.03%)</td><td>1394.77 (-3.39%)</td><td>30.26 <b>(+124.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1476.40 (n/a)</td><td>1462.02 (n/a)</td><td>1466.24 (n/a)</td><td>1443.67 (n/a)</td><td>13.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>2.40 <b>(-30.08%)</b></td><td>2.20 <b>(-27.46%)</b></td><td>2.15 <b>(-30.92%)</b></td><td>2.07 (-19.90%)</td><td>0.14 <b>(-60.87%)</b></td><td>253.60 <b>(+24.86%)</b></td><td>239.40 <b>(+36.78%)</b></td><td>243.70 <b>(+44.71%)</b></td><td>218.20 <b>(+42.99%)</b></td><td>14.28 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.44 (n/a)</td><td>3.03 (n/a)</td><td>3.11 (n/a)</td><td>2.58 (n/a)</td><td>0.35 (n/a)</td><td>203.10 (n/a)</td><td>175.02 (n/a)</td><td>168.40 (n/a)</td><td>152.60 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>5.24 (-6.46%)</td><td>4.65 (-0.67%)</td><td>4.82 (+7.43%)</td><td>4.04 (-7.92%)</td><td>0.56 (+9.05%)</td><td>259.50 (+8.58%)</td><td>228.04 (+1.02%)</td><td>217.30 (-6.94%)</td><td>200.00 (+6.89%)</td><td>28.32 <b>(+30.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>5.61 (n/a)</td><td>4.69 (n/a)</td><td>4.49 (n/a)</td><td>4.39 (n/a)</td><td>0.52 (n/a)</td><td>239.00 (n/a)</td><td>225.74 (n/a)</td><td>233.50 (n/a)</td><td>187.10 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:39:45</td><td>3.12 (-19.64%)</td><td>2.61 (-15.17%)</td><td>2.66 (-9.72%)</td><td>2.10 <b>(-22.87%)</b></td><td>0.38 (-18.77%)</td><td>249.70 <b>(+29.65%)</b></td><td>204.46 (+18.05%)</td><td>196.90 (+10.80%)</td><td>168.30 <b>(+24.48%)</b></td><td>30.86 <b>(+33.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:42:07</td><td>3.88 (n/a)</td><td>3.08 (n/a)</td><td>2.95 (n/a)</td><td>2.72 (n/a)</td><td>0.47 (n/a)</td><td>192.60 (n/a)</td><td>173.20 (n/a)</td><td>177.70 (n/a)</td><td>135.20 (n/a)</td><td>23.12 (n/a)</td>
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
