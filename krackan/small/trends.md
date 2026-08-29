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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (+13.92%)</td><td>0.07 (+8.72%)</td><td>0.07 (+5.13%)</td><td>0.05 (-9.51%)</td><td>0.01 <b>(+35.64%)</b></td><td>251.80 (+10.54%)</td><td>181.30 (-6.52%)</td><td>175.30 (-4.88%)</td><td>142.60 (-12.19%)</td><td>42.25 <b>(+32.39%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>193.94 (n/a)</td><td>184.30 (n/a)</td><td>162.40 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 <b>(+27.95%)</b></td><td>0.07 (-2.30%)</td><td>0.07 (-9.92%)</td><td>0.05 (-15.96%)</td><td>0.02 <b>(+197.72%)</b></td><td>235.10 (+18.98%)</td><td>187.04 (+7.05%)</td><td>187.40 (+11.02%)</td><td>121.40 <b>(-21.83%)</b></td><td>43.19 <b>(+167.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>174.72 (n/a)</td><td>168.80 (n/a)</td><td>155.30 (n/a)</td><td>16.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (-7.50%)</td><td>0.06 (-13.83%)</td><td>0.06 <b>(-20.23%)</b></td><td>0.05 (-13.19%)</td><td>0.02 (+7.33%)</td><td>233.90 (+15.22%)</td><td>200.56 (+17.47%)</td><td>215.50 <b>(+25.36%)</b></td><td>133.20 (+8.03%)</td><td>39.44 <b>(+33.42%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>170.74 (n/a)</td><td>171.90 (n/a)</td><td>123.30 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (+18.94%)</td><td>0.06 (+0.30%)</td><td>0.06 (+3.70%)</td><td>0.04 <b>(-26.54%)</b></td><td>0.02 <b>(+102.95%)</b></td><td>307.10 <b>(+36.13%)</b></td><td>213.76 (+5.22%)</td><td>209.60 (-3.54%)</td><td>134.70 (-15.97%)</td><td>62.22 <b>(+130.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>203.16 (n/a)</td><td>217.30 (n/a)</td><td>160.30 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (+18.52%)</td><td>0.03 (+5.08%)</td><td>0.04 (+19.11%)</td><td>0.02 <b>(-23.41%)</b></td><td>0.01 <b>(+173.79%)</b></td><td>261.50 <b>(+30.55%)</b></td><td>169.42 (+1.32%)</td><td>135.50 (-16.05%)</td><td>130.00 (-15.58%)</td><td>56.18 <b>(+193.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>167.22 (n/a)</td><td>161.40 (n/a)</td><td>154.00 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (+16.48%)</td><td>0.03 (-1.70%)</td><td>0.03 (-4.58%)</td><td>0.02 (-17.74%)</td><td>0.01 <b>(+107.03%)</b></td><td>294.60 <b>(+21.58%)</b></td><td>212.32 (+9.49%)</td><td>192.70 (+4.84%)</td><td>134.50 (-14.17%)</td><td>72.44 <b>(+123.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>193.92 (n/a)</td><td>183.80 (n/a)</td><td>156.70 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 <b>(+27.53%)</b></td><td>0.04 <b>(+28.02%)</b></td><td>0.04 <b>(+22.99%)</b></td><td>0.03 <b>(+49.21%)</b></td><td>0.01 (-5.09%)</td><td>176.80 <b>(-32.98%)</b></td><td>142.32 <b>(-23.61%)</b></td><td>143.50 (-18.70%)</td><td>115.20 <b>(-21.58%)</b></td><td>22.90 <b>(-50.75%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.80 (n/a)</td><td>186.30 (n/a)</td><td>176.50 (n/a)</td><td>146.90 (n/a)</td><td>46.50 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (+19.00%)</td><td>0.04 (+19.91%)</td><td>0.04 <b>(+21.11%)</b></td><td>0.02 (-1.92%)</td><td>0.01 <b>(+66.59%)</b></td><td>213.40 (+1.96%)</td><td>148.76 (-13.62%)</td><td>148.50 (-17.41%)</td><td>108.60 (-15.94%)</td><td>42.95 <b>(+39.31%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>172.22 (n/a)</td><td>179.80 (n/a)</td><td>129.20 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (+17.74%)</td><td>0.04 (+14.26%)</td><td>0.04 (+17.34%)</td><td>0.03 (+11.33%)</td><td>0.01 <b>(+27.79%)</b></td><td>195.10 (-10.17%)</td><td>152.32 (-11.97%)</td><td>148.60 (-14.79%)</td><td>117.60 (-15.03%)</td><td>29.34 (-2.10%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>173.04 (n/a)</td><td>174.40 (n/a)</td><td>138.40 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (-17.44%)</td><td>0.03 (+11.07%)</td><td>0.03 <b>(+30.95%)</b></td><td>0.03 (+11.73%)</td><td>0.00 <b>(-57.13%)</b></td><td>190.30 (-10.53%)</td><td>160.54 (-13.37%)</td><td>152.10 <b>(-23.61%)</b></td><td>141.50 <b>(+21.15%)</b></td><td>18.96 <b>(-51.09%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>185.32 (n/a)</td><td>199.10 (n/a)</td><td>116.80 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.03 (-15.61%)</td><td>0.03 (-0.63%)</td><td>0.03 (+8.28%)</td><td>0.02 (-2.33%)</td><td>0.00 <b>(-40.93%)</b></td><td>222.90 (+2.39%)</td><td>187.14 (-0.95%)</td><td>178.80 (-7.64%)</td><td>162.40 (+18.45%)</td><td>23.73 <b>(-27.13%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>188.94 (n/a)</td><td>193.60 (n/a)</td><td>137.10 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.03 (+15.19%)</td><td>0.02 (+7.59%)</td><td>0.02 (+2.91%)</td><td>0.02 (+11.28%)</td><td>0.00 <b>(+26.37%)</b></td><td>227.20 (-10.16%)</td><td>213.94 (-6.98%)</td><td>216.00 (-2.83%)</td><td>188.50 (-13.17%)</td><td>15.24 (-2.22%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.90 (n/a)</td><td>230.00 (n/a)</td><td>222.30 (n/a)</td><td>217.10 (n/a)</td><td>15.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>149.40 (n/a)</td><td>153.50 (n/a)</td><td>125.20 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>151.12 (n/a)</td><td>143.40 (n/a)</td><td>132.80 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>148.32 (n/a)</td><td>148.30 (n/a)</td><td>121.90 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>276.00 (n/a)</td><td>191.06 (n/a)</td><td>173.60 (n/a)</td><td>137.30 (n/a)</td><td>56.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>168.90 (n/a)</td><td>173.10 (n/a)</td><td>120.80 (n/a)</td><td>35.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>217.18 (n/a)</td><td>204.20 (n/a)</td><td>178.60 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.30 (n/a)</td><td>188.10 (n/a)</td><td>192.80 (n/a)</td><td>125.00 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>229.00 (n/a)</td><td>194.26 (n/a)</td><td>201.30 (n/a)</td><td>132.00 (n/a)</td><td>37.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>165.84 (n/a)</td><td>161.40 (n/a)</td><td>143.70 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>161.52 (n/a)</td><td>155.70 (n/a)</td><td>135.70 (n/a)</td><td>29.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>169.94 (n/a)</td><td>153.60 (n/a)</td><td>136.60 (n/a)</td><td>47.95 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>159.62 (n/a)</td><td>140.90 (n/a)</td><td>135.40 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>150.58 (n/a)</td><td>138.90 (n/a)</td><td>124.40 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>161.66 (n/a)</td><td>171.10 (n/a)</td><td>134.10 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>171.04 (n/a)</td><td>159.60 (n/a)</td><td>150.30 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>202.34 (n/a)</td><td>200.90 (n/a)</td><td>191.30 (n/a)</td><td>10.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>4.26 (-4.65%)</td><td>4.19 (+9.57%)</td><td>4.21 (+18.84%)</td><td>4.05 <b>(+20.19%)</b></td><td>0.08 <b>(-83.20%)</b></td><td>2320.70 (-16.80%)</td><td>2244.60 (-9.83%)</td><td>2235.20 (-15.85%)</td><td>2208.90 (+4.87%)</td><td>44.60 <b>(-85.23%)</b></td><td>1674.75 (-4.65%)</td><td>1648.62 (+9.57%)</td><td>1655.03 (+18.84%)</td><td>1594.08 <b>(+20.19%)</b></td><td>32.09 <b>(-83.20%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.46 (n/a)</td><td>3.82 (n/a)</td><td>3.54 (n/a)</td><td>3.37 (n/a)</td><td>0.49 (n/a)</td><td>2789.30 (n/a)</td><td>2489.34 (n/a)</td><td>2656.30 (n/a)</td><td>2106.30 (n/a)</td><td>302.03 (n/a)</td><td>1756.36 (n/a)</td><td>1504.61 (n/a)</td><td>1392.69 (n/a)</td><td>1326.28 (n/a)</td><td>191.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.57 <b>(+58.80%)</b></td><td>1.16 <b>(+27.65%)</b></td><td>1.05 (+11.68%)</td><td>0.94 <b>(+31.98%)</b></td><td>0.25 <b>(+117.01%)</b></td><td>235.20 <b>(-24.23%)</b></td><td>196.46 <b>(-20.33%)</b></td><td>211.00 (-10.48%)</td><td>140.50 <b>(-37.05%)</b></td><td>36.37 (-0.20%)</td><td>67.15 <b>(+58.80%)</b></td><td>49.59 <b>(+27.65%)</b></td><td>44.72 (+11.68%)</td><td>40.13 <b>(+31.98%)</b></td><td>10.64 <b>(+117.01%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.99 (n/a)</td><td>0.91 (n/a)</td><td>0.94 (n/a)</td><td>0.71 (n/a)</td><td>0.11 (n/a)</td><td>310.40 (n/a)</td><td>246.58 (n/a)</td><td>235.70 (n/a)</td><td>223.20 (n/a)</td><td>36.44 (n/a)</td><td>42.28 (n/a)</td><td>38.85 (n/a)</td><td>40.04 (n/a)</td><td>30.40 (n/a)</td><td>4.90 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.95 <b>(-26.41%)</b></td><td>0.81 (-12.80%)</td><td>0.76 <b>(-22.48%)</b></td><td>0.68 (+17.12%)</td><td>0.13 <b>(-58.33%)</b></td><td>323.70 (-14.61%)</td><td>279.84 (+6.49%)</td><td>291.20 <b>(+28.96%)</b></td><td>233.30 <b>(+35.88%)</b></td><td>42.13 <b>(-53.69%)</b></td><td>40.45 <b>(-26.41%)</b></td><td>34.37 (-12.80%)</td><td>32.40 <b>(-22.48%)</b></td><td>29.16 (+17.12%)</td><td>5.34 <b>(-58.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>1.29 (n/a)</td><td>0.92 (n/a)</td><td>0.98 (n/a)</td><td>0.58 (n/a)</td><td>0.30 (n/a)</td><td>379.10 (n/a)</td><td>262.78 (n/a)</td><td>225.80 (n/a)</td><td>171.70 (n/a)</td><td>90.97 (n/a)</td><td>54.96 (n/a)</td><td>39.41 (n/a)</td><td>41.80 (n/a)</td><td>24.89 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.52 (-1.02%)</td><td>0.52 (-0.29%)</td><td>0.52 (-0.09%)</td><td>0.52 (-0.03%)</td><td>0.00 <b>(-74.79%)</b></td><td>48627.80 (+0.03%)</td><td>48527.34 (+0.29%)</td><td>48507.70 (+0.09%)</td><td>48470.50 (+1.03%)</td><td>61.45 <b>(-74.49%)</b></td><td>354.44 (-1.02%)</td><td>354.02 (-0.29%)</td><td>354.17 (-0.09%)</td><td>353.29 (-0.03%)</td><td>0.45 <b>(-74.79%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48612.40 (n/a)</td><td>48385.52 (n/a)</td><td>48462.30 (n/a)</td><td>47975.60 (n/a)</td><td>240.93 (n/a)</td><td>358.10 (n/a)</td><td>355.07 (n/a)</td><td>354.50 (n/a)</td><td>353.40 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.90 (-0.04%)</td><td>0.89 (-0.17%)</td><td>0.90 (+0.36%)</td><td>0.88 (-0.98%)</td><td>0.01 <b>(+97.06%)</b></td><td>28554.10 (+0.99%)</td><td>28148.18 (+0.17%)</td><td>28015.60 (-0.36%)</td><td>27903.40 (+0.04%)</td><td>288.52 <b>(+99.03%)</b></td><td>615.69 (-0.04%)</td><td>610.39 (-0.17%)</td><td>613.22 (+0.36%)</td><td>601.66 (-0.98%)</td><td>6.23 <b>(+97.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28274.70 (n/a)</td><td>28099.30 (n/a)</td><td>28116.10 (n/a)</td><td>27892.80 (n/a)</td><td>144.96 (n/a)</td><td>615.93 (n/a)</td><td>611.41 (n/a)</td><td>611.03 (n/a)</td><td>607.60 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.28 (-5.40%)</td><td>3.17 (-3.25%)</td><td>3.17 (-2.73%)</td><td>3.09 (-2.64%)</td><td>0.07 <b>(-41.22%)</b></td><td>8138.70 (+2.71%)</td><td>7944.60 (+3.29%)</td><td>7946.70 (+2.81%)</td><td>7679.00 (+5.71%)</td><td>170.05 <b>(-36.34%)</b></td><td>2237.26 (-5.40%)</td><td>2163.26 (-3.25%)</td><td>2161.88 (-2.73%)</td><td>2110.88 (-2.64%)</td><td>46.88 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>3.46 (n/a)</td><td>3.28 (n/a)</td><td>3.26 (n/a)</td><td>3.18 (n/a)</td><td>0.12 (n/a)</td><td>7923.70 (n/a)</td><td>7691.58 (n/a)</td><td>7729.70 (n/a)</td><td>7264.20 (n/a)</td><td>267.12 (n/a)</td><td>2365.00 (n/a)</td><td>2235.81 (n/a)</td><td>2222.59 (n/a)</td><td>2168.16 (n/a)</td><td>79.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>4.13 (-1.51%)</td><td>3.38 (-5.86%)</td><td>3.21 (-10.76%)</td><td>2.97 (-0.39%)</td><td>0.45 (+3.04%)</td><td>2715.50 (+0.40%)</td><td>2415.00 (+6.29%)</td><td>2512.40 (+12.06%)</td><td>1951.30 (+1.53%)</td><td>287.28 (+1.76%)</td><td>1083.32 (-1.51%)</td><td>886.45 (-5.86%)</td><td>841.40 (-10.76%)</td><td>778.48 (-0.39%)</td><td>117.31 (+3.04%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.19 (n/a)</td><td>3.59 (n/a)</td><td>3.60 (n/a)</td><td>2.98 (n/a)</td><td>0.43 (n/a)</td><td>2704.80 (n/a)</td><td>2272.14 (n/a)</td><td>2242.00 (n/a)</td><td>1921.90 (n/a)</td><td>282.31 (n/a)</td><td>1099.91 (n/a)</td><td>941.59 (n/a)</td><td>942.87 (n/a)</td><td>781.55 (n/a)</td><td>113.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.46 <b>(-21.37%)</b></td><td>0.36 (-4.80%)</td><td>0.34 (+2.18%)</td><td>0.32 (+2.87%)</td><td>0.06 <b>(-50.08%)</b></td><td>3918.00 (-2.79%)</td><td>3536.72 (+0.97%)</td><td>3715.50 (-2.13%)</td><td>2690.00 <b>(+27.17%)</b></td><td>489.16 <b>(-37.53%)</b></td><td>24.95 <b>(-21.37%)</b></td><td>19.33 (-4.80%)</td><td>18.06 (+2.18%)</td><td>17.13 (+2.87%)</td><td>3.20 <b>(-50.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.59 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.12 (n/a)</td><td>4030.30 (n/a)</td><td>3502.74 (n/a)</td><td>3796.30 (n/a)</td><td>2115.20 (n/a)</td><td>783.00 (n/a)</td><td>31.73 (n/a)</td><td>20.30 (n/a)</td><td>17.68 (n/a)</td><td>16.65 (n/a)</td><td>6.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>5.02 (+3.70%)</td><td>4.36 (-0.97%)</td><td>4.75 (+1.65%)</td><td>3.48 (-2.37%)</td><td>0.69 <b>(+28.28%)</b></td><td>1912.10 (+2.43%)</td><td>1559.52 (+1.82%)</td><td>1400.60 (-1.62%)</td><td>1326.40 (-3.56%)</td><td>262.62 <b>(+27.10%)</b></td><td>1549.49 (+3.70%)</td><td>1346.45 (-0.97%)</td><td>1467.42 (+1.65%)</td><td>1074.87 (-2.37%)</td><td>212.57 <b>(+28.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.84 (n/a)</td><td>4.40 (n/a)</td><td>4.67 (n/a)</td><td>3.56 (n/a)</td><td>0.54 (n/a)</td><td>1866.70 (n/a)</td><td>1531.66 (n/a)</td><td>1423.70 (n/a)</td><td>1375.40 (n/a)</td><td>206.62 (n/a)</td><td>1494.28 (n/a)</td><td>1359.65 (n/a)</td><td>1443.61 (n/a)</td><td>1100.98 (n/a)</td><td>165.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.39 (n/a)</td><td>12.64 (n/a)</td><td>13.12 (n/a)</td><td>11.13 (n/a)</td><td>0.98 (n/a)</td><td>13.39 (n/a)</td><td>12.63 (n/a)</td><td>13.11 (n/a)</td><td>11.13 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>24.28 (-0.77%)</td><td>24.16 (+2.31%)</td><td>24.19 (+1.09%)</td><td>24.02 (+10.14%)</td><td>0.10 <b>(-90.83%)</b></td><td>24.26 (-0.77%)</td><td>24.15 (+2.31%)</td><td>24.17 (+1.09%)</td><td>24.01 (+10.14%)</td><td>0.10 <b>(-90.83%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>24.46 (n/a)</td><td>23.61 (n/a)</td><td>23.93 (n/a)</td><td>21.81 (n/a)</td><td>1.05 (n/a)</td><td>24.45 (n/a)</td><td>23.60 (n/a)</td><td>23.91 (n/a)</td><td>21.80 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>41.51 (+0.42%)</td><td>40.91 (+1.62%)</td><td>40.84 (+1.27%)</td><td>40.17 (+4.21%)</td><td>0.54 <b>(-53.19%)</b></td><td>41.49 (+0.42%)</td><td>40.89 (+1.62%)</td><td>40.81 (+1.27%)</td><td>40.14 (+4.21%)</td><td>0.54 <b>(-53.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>41.34 (n/a)</td><td>40.26 (n/a)</td><td>40.32 (n/a)</td><td>38.55 (n/a)</td><td>1.15 (n/a)</td><td>41.31 (n/a)</td><td>40.24 (n/a)</td><td>40.30 (n/a)</td><td>38.52 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>45.47 (-3.42%)</td><td>41.75 (+1.04%)</td><td>41.44 (+0.13%)</td><td>38.39 (+16.33%)</td><td>2.70 <b>(-51.96%)</b></td><td>45.44 (-3.42%)</td><td>41.72 (+1.04%)</td><td>41.42 (+0.13%)</td><td>38.37 (+16.33%)</td><td>2.70 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>47.08 (n/a)</td><td>41.32 (n/a)</td><td>41.39 (n/a)</td><td>33.00 (n/a)</td><td>5.63 (n/a)</td><td>47.05 (n/a)</td><td>41.30 (n/a)</td><td>41.37 (n/a)</td><td>32.98 (n/a)</td><td>5.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.43 (n/a)</td><td>12.35 (n/a)</td><td>12.76 (n/a)</td><td>11.20 (n/a)</td><td>0.98 (n/a)</td><td>13.42 (n/a)</td><td>12.34 (n/a)</td><td>12.75 (n/a)</td><td>11.20 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>24.77 (+1.32%)</td><td>24.24 (+2.02%)</td><td>24.31 (+1.66%)</td><td>23.12 (+0.77%)</td><td>0.67 <b>(+20.40%)</b></td><td>24.76 (+1.32%)</td><td>24.23 (+2.02%)</td><td>24.30 (+1.66%)</td><td>23.11 (+0.77%)</td><td>0.67 <b>(+20.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>24.45 (n/a)</td><td>23.77 (n/a)</td><td>23.92 (n/a)</td><td>22.95 (n/a)</td><td>0.55 (n/a)</td><td>24.44 (n/a)</td><td>23.75 (n/a)</td><td>23.90 (n/a)</td><td>22.93 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>41.71 (+0.13%)</td><td>40.59 (-0.07%)</td><td>41.39 (+1.38%)</td><td>38.89 (-0.77%)</td><td>1.28 (+17.07%)</td><td>41.68 (+0.13%)</td><td>40.57 (-0.07%)</td><td>41.36 (+1.38%)</td><td>38.86 (-0.77%)</td><td>1.28 (+17.07%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>41.65 (n/a)</td><td>40.62 (n/a)</td><td>40.83 (n/a)</td><td>39.19 (n/a)</td><td>1.09 (n/a)</td><td>41.63 (n/a)</td><td>40.60 (n/a)</td><td>40.80 (n/a)</td><td>39.17 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>43.70 (-1.68%)</td><td>39.59 (-8.35%)</td><td>43.39 (-0.30%)</td><td>24.74 <b>(-40.47%)</b></td><td>8.31 <b>(+527.21%)</b></td><td>43.67 (-1.68%)</td><td>39.57 (-8.35%)</td><td>43.36 (-0.30%)</td><td>24.73 <b>(-40.47%)</b></td><td>8.31 <b>(+527.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>44.44 (n/a)</td><td>43.20 (n/a)</td><td>43.52 (n/a)</td><td>41.57 (n/a)</td><td>1.33 (n/a)</td><td>44.42 (n/a)</td><td>43.17 (n/a)</td><td>43.49 (n/a)</td><td>41.54 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>9.63 (+2.51%)</td><td>8.92 (-0.14%)</td><td>8.67 (-2.54%)</td><td>8.40 (+2.46%)</td><td>0.51 (+6.46%)</td><td>9.62 (+2.51%)</td><td>8.90 (-0.14%)</td><td>8.65 (-2.54%)</td><td>8.39 (+2.46%)</td><td>0.51 (+6.46%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>9.40 (n/a)</td><td>8.93 (n/a)</td><td>8.90 (n/a)</td><td>8.20 (n/a)</td><td>0.48 (n/a)</td><td>9.38 (n/a)</td><td>8.92 (n/a)</td><td>8.88 (n/a)</td><td>8.18 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.07 (+7.24%)</td><td>0.93 (+2.72%)</td><td>0.91 (-4.27%)</td><td>0.81 (+8.44%)</td><td>0.11 (+0.64%)</td><td>1.05 (+7.24%)</td><td>0.92 (+2.72%)</td><td>0.89 (-4.27%)</td><td>0.80 (+8.44%)</td><td>0.10 (+0.64%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.99 (n/a)</td><td>0.91 (n/a)</td><td>0.95 (n/a)</td><td>0.75 (n/a)</td><td>0.10 (n/a)</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.93 (n/a)</td><td>0.74 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.38 (+11.19%)</td><td>1.12 (+1.27%)</td><td>1.11 (-3.88%)</td><td>0.91 (+6.72%)</td><td>0.17 (+12.31%)</td><td>1.36 (+11.19%)</td><td>1.10 (+1.27%)</td><td>1.10 (-3.88%)</td><td>0.90 (+6.72%)</td><td>0.17 (+12.31%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>1.24 (n/a)</td><td>1.10 (n/a)</td><td>1.15 (n/a)</td><td>0.85 (n/a)</td><td>0.15 (n/a)</td><td>1.22 (n/a)</td><td>1.09 (n/a)</td><td>1.14 (n/a)</td><td>0.84 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>16.83 (-5.47%)</td><td>15.44 (-7.11%)</td><td>15.65 (-8.53%)</td><td>13.00 (-12.97%)</td><td>1.45 (+19.02%)</td><td>16.63 (-5.47%)</td><td>15.26 (-7.11%)</td><td>15.47 (-8.53%)</td><td>12.85 (-12.97%)</td><td>1.43 (+19.02%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>17.80 (n/a)</td><td>16.62 (n/a)</td><td>17.11 (n/a)</td><td>14.94 (n/a)</td><td>1.22 (n/a)</td><td>17.59 (n/a)</td><td>16.43 (n/a)</td><td>16.91 (n/a)</td><td>14.76 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.84 (-5.18%)</td><td>13.02 (-6.77%)</td><td>13.13 (-7.04%)</td><td>11.42 (-12.99%)</td><td>0.98 <b>(+65.32%)</b></td><td>13.60 (-5.18%)</td><td>12.79 (-6.77%)</td><td>12.90 (-7.04%)</td><td>11.22 (-12.99%)</td><td>0.96 <b>(+65.33%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>14.60 (n/a)</td><td>13.96 (n/a)</td><td>14.13 (n/a)</td><td>13.12 (n/a)</td><td>0.59 (n/a)</td><td>14.34 (n/a)</td><td>13.72 (n/a)</td><td>13.88 (n/a)</td><td>12.89 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>8.00 <b>(-24.86%)</b></td><td>7.10 (-9.75%)</td><td>7.08 (-0.11%)</td><td>6.35 (-3.60%)</td><td>0.60 <b>(-63.85%)</b></td><td>7.86 <b>(-24.86%)</b></td><td>6.98 (-9.75%)</td><td>6.95 (-0.11%)</td><td>6.24 (-3.60%)</td><td>0.59 <b>(-63.85%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>10.64 (n/a)</td><td>7.87 (n/a)</td><td>7.08 (n/a)</td><td>6.59 (n/a)</td><td>1.65 (n/a)</td><td>10.46 (n/a)</td><td>7.73 (n/a)</td><td>6.96 (n/a)</td><td>6.47 (n/a)</td><td>1.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>6.21 (-1.17%)</td><td>5.34 (-9.72%)</td><td>5.45 (-12.56%)</td><td>4.64 (-5.00%)</td><td>0.66 (+11.85%)</td><td>6.11 (-1.17%)</td><td>5.26 (-9.72%)</td><td>5.36 (-12.56%)</td><td>4.57 (-5.00%)</td><td>0.65 (+11.85%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>6.28 (n/a)</td><td>5.92 (n/a)</td><td>6.23 (n/a)</td><td>4.88 (n/a)</td><td>0.59 (n/a)</td><td>6.18 (n/a)</td><td>5.82 (n/a)</td><td>6.13 (n/a)</td><td>4.81 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.43 (n/a)</td><td>12.96 (n/a)</td><td>13.36 (n/a)</td><td>12.13 (n/a)</td><td>0.62 (n/a)</td><td>13.43 (n/a)</td><td>12.95 (n/a)</td><td>13.35 (n/a)</td><td>12.12 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.44 (n/a)</td><td>12.94 (n/a)</td><td>13.30 (n/a)</td><td>12.22 (n/a)</td><td>0.62 (n/a)</td><td>13.43 (n/a)</td><td>12.93 (n/a)</td><td>13.29 (n/a)</td><td>12.21 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.50 (n/a)</td><td>169.36 (n/a)</td><td>172.60 (n/a)</td><td>156.40 (n/a)</td><td>7.81 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>162.50 (n/a)</td><td>148.46 (n/a)</td><td>155.60 (n/a)</td><td>123.40 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>172.20 (n/a)</td><td>158.40 (n/a)</td><td>147.20 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>155.80 (n/a)</td><td>147.60 (n/a)</td><td>109.50 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>179.68 (n/a)</td><td>171.70 (n/a)</td><td>131.80 (n/a)</td><td>39.18 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>247.90 (n/a)</td><td>166.80 (n/a)</td><td>146.90 (n/a)</td><td>114.80 (n/a)</td><td>59.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>339.00 (n/a)</td><td>229.62 (n/a)</td><td>250.20 (n/a)</td><td>131.10 (n/a)</td><td>80.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>352.90 (n/a)</td><td>258.62 (n/a)</td><td>242.60 (n/a)</td><td>184.50 (n/a)</td><td>65.00 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+39.74%)</b></td><td>0.06 <b>(+33.38%)</b></td><td>0.06 <b>(+36.54%)</b></td><td>0.05 (+18.12%)</td><td>0.01 <b>(+142.07%)</b></td><td>180.40 (-15.34%)</td><td>139.90 <b>(-23.36%)</b></td><td>128.60 <b>(-26.72%)</b></td><td>115.80 <b>(-28.43%)</b></td><td>28.42 <b>(+42.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>182.54 (n/a)</td><td>175.50 (n/a)</td><td>161.80 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (+8.92%)</td><td>0.05 (+4.93%)</td><td>0.05 (+4.39%)</td><td>0.04 (+0.48%)</td><td>0.01 <b>(+24.12%)</b></td><td>202.70 (-0.49%)</td><td>164.38 (-3.98%)</td><td>165.70 (-4.22%)</td><td>122.40 (-8.18%)</td><td>28.73 (+13.08%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>171.20 (n/a)</td><td>173.00 (n/a)</td><td>133.30 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (-18.73%)</td><td>0.05 (-2.82%)</td><td>0.05 (-3.38%)</td><td>0.04 (+11.09%)</td><td>0.00 <b>(-60.39%)</b></td><td>185.90 (-9.98%)</td><td>170.98 (-0.27%)</td><td>177.90 (+3.49%)</td><td>147.50 <b>(+23.02%)</b></td><td>15.18 <b>(-56.53%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>171.44 (n/a)</td><td>171.90 (n/a)</td><td>119.90 (n/a)</td><td>34.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+33.11%)</b></td><td>0.05 (+8.27%)</td><td>0.05 (+3.24%)</td><td>0.04 (-14.95%)</td><td>0.01 <b>(+163.44%)</b></td><td>232.60 (+17.59%)</td><td>170.48 (-3.61%)</td><td>174.80 (-3.10%)</td><td>117.00 <b>(-24.86%)</b></td><td>42.71 <b>(+132.62%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.80 (n/a)</td><td>176.86 (n/a)</td><td>180.40 (n/a)</td><td>155.70 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+46.86%)</b></td><td>0.06 <b>(+31.88%)</b></td><td>0.06 <b>(+23.62%)</b></td><td>0.05 (+9.45%)</td><td>0.01 <b>(+312.40%)</b></td><td>180.10 (-8.63%)</td><td>142.38 <b>(-22.54%)</b></td><td>146.00 (-19.11%)</td><td>118.20 <b>(-31.95%)</b></td><td>25.16 <b>(+151.36%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.10 (n/a)</td><td>183.80 (n/a)</td><td>180.50 (n/a)</td><td>173.70 (n/a)</td><td>10.01 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+22.39%)</b></td><td>0.06 <b>(+31.16%)</b></td><td>0.06 <b>(+39.59%)</b></td><td>0.04 (-2.50%)</td><td>0.01 <b>(+63.61%)</b></td><td>227.20 (+2.57%)</td><td>149.56 <b>(-21.38%)</b></td><td>140.40 <b>(-28.37%)</b></td><td>118.70 (-18.25%)</td><td>44.78 <b>(+37.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>190.22 (n/a)</td><td>196.00 (n/a)</td><td>145.20 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 <b>(-26.52%)</b></td><td>0.05 (-4.46%)</td><td>0.05 (+1.19%)</td><td>0.04 (-4.16%)</td><td>0.01 <b>(-52.75%)</b></td><td>216.10 (+4.35%)</td><td>173.14 (+1.06%)</td><td>171.20 (-1.15%)</td><td>146.60 <b>(+35.99%)</b></td><td>27.08 <b>(-29.54%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>171.32 (n/a)</td><td>173.20 (n/a)</td><td>107.80 (n/a)</td><td>38.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 <b>(-27.12%)</b></td><td>0.05 (-1.83%)</td><td>0.05 (+13.68%)</td><td>0.04 (-0.68%)</td><td>0.01 <b>(-61.82%)</b></td><td>208.00 (+0.73%)</td><td>176.52 (-2.42%)</td><td>172.10 (-12.01%)</td><td>152.20 <b>(+37.24%)</b></td><td>21.64 <b>(-45.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>180.90 (n/a)</td><td>195.60 (n/a)</td><td>110.90 (n/a)</td><td>39.48 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 <b>(+36.33%)</b></td><td>0.05 (+15.86%)</td><td>0.04 (+8.69%)</td><td>0.04 (+15.03%)</td><td>0.01 <b>(+118.94%)</b></td><td>209.50 (-13.07%)</td><td>183.10 (-12.39%)</td><td>190.20 (-7.98%)</td><td>135.40 <b>(-26.61%)</b></td><td>27.95 <b>(+32.82%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>241.00 (n/a)</td><td>209.00 (n/a)</td><td>206.70 (n/a)</td><td>184.50 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (+8.45%)</td><td>0.04 (-0.12%)</td><td>0.04 (+8.33%)</td><td>0.02 <b>(-30.18%)</b></td><td>0.01 <b>(+439.59%)</b></td><td>332.30 <b>(+43.23%)</b></td><td>231.26 (+3.85%)</td><td>207.80 (-7.73%)</td><td>195.70 (-7.78%)</td><td>56.89 <b>(+640.71%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.00 (n/a)</td><td>222.68 (n/a)</td><td>225.20 (n/a)</td><td>212.20 (n/a)</td><td>7.68 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (+13.52%)</td><td>0.05 (-6.72%)</td><td>0.05 (-5.85%)</td><td>0.02 <b>(-53.34%)</b></td><td>0.02 <b>(+245.81%)</b></td><td>394.10 <b>(+114.30%)</b></td><td>200.78 <b>(+25.83%)</b></td><td>165.90 (+6.21%)</td><td>127.40 (-11.89%)</td><td>110.92 <b>(+573.32%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>159.56 (n/a)</td><td>156.20 (n/a)</td><td>144.60 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (-9.51%)</td><td>0.05 (+12.45%)</td><td>0.05 (+18.21%)</td><td>0.04 <b>(+30.58%)</b></td><td>0.00 <b>(-79.31%)</b></td><td>188.30 <b>(-23.42%)</b></td><td>180.26 (-12.83%)</td><td>176.90 (-15.40%)</td><td>175.20 (+10.54%)</td><td>5.69 <b>(-82.03%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.90 (n/a)</td><td>206.78 (n/a)</td><td>209.10 (n/a)</td><td>158.50 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (+7.84%)</td><td>0.05 (+3.27%)</td><td>0.05 (-3.93%)</td><td>0.04 <b>(+21.21%)</b></td><td>0.01 (-1.76%)</td><td>187.30 (-17.49%)</td><td>169.52 (-3.81%)</td><td>175.30 (+4.10%)</td><td>130.20 (-7.26%)</td><td>22.60 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>176.24 (n/a)</td><td>168.40 (n/a)</td><td>140.40 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (+4.40%)</td><td>0.06 (+12.63%)</td><td>0.06 <b>(+21.78%)</b></td><td>0.05 <b>(+20.79%)</b></td><td>0.00 <b>(-43.74%)</b></td><td>160.40 (-17.19%)</td><td>144.94 (-12.53%)</td><td>143.60 (-17.90%)</td><td>128.90 (-4.16%)</td><td>11.51 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>165.70 (n/a)</td><td>174.90 (n/a)</td><td>134.50 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (-7.66%)</td><td>0.05 (-5.78%)</td><td>0.05 (+5.02%)</td><td>0.03 (-1.92%)</td><td>0.01 <b>(-21.87%)</b></td><td>278.00 (+1.94%)</td><td>184.26 (+3.74%)</td><td>172.50 (-4.75%)</td><td>129.80 (+8.26%)</td><td>55.47 (-8.03%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>272.70 (n/a)</td><td>177.62 (n/a)</td><td>181.10 (n/a)</td><td>119.90 (n/a)</td><td>60.31 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 <b>(+24.96%)</b></td><td>0.05 (+11.77%)</td><td>0.05 (+7.93%)</td><td>0.03 (-18.01%)</td><td>0.01 <b>(+96.36%)</b></td><td>310.10 <b>(+21.94%)</b></td><td>187.16 (-4.50%)</td><td>169.30 (-7.33%)</td><td>128.60 (-19.98%)</td><td>71.44 <b>(+98.27%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.30 (n/a)</td><td>195.98 (n/a)</td><td>182.70 (n/a)</td><td>160.70 (n/a)</td><td>36.03 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (+13.51%)</td><td>0.05 (+13.36%)</td><td>0.05 (+8.91%)</td><td>0.04 (+8.26%)</td><td>0.01 (+18.11%)</td><td>204.80 (-7.62%)</td><td>166.20 (-11.52%)</td><td>173.20 (-8.17%)</td><td>123.90 (-11.88%)</td><td>32.01 (-6.66%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>187.84 (n/a)</td><td>188.60 (n/a)</td><td>140.60 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (+13.43%)</td><td>0.05 (+17.02%)</td><td>0.05 (+14.68%)</td><td>0.05 <b>(+21.38%)</b></td><td>0.00 (-3.25%)</td><td>173.30 (-17.59%)</td><td>162.60 (-14.78%)</td><td>170.10 (-12.81%)</td><td>139.70 (-11.86%)</td><td>13.85 <b>(-28.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.30 (n/a)</td><td>190.80 (n/a)</td><td>195.10 (n/a)</td><td>158.50 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.18 (+0.87%)</td><td>0.18 (+0.23%)</td><td>0.18 (+0.00%)</td><td>0.18 (+0.09%)</td><td>0.00 <b>(+445.38%)</b></td><td>47421.80 (-0.09%)</td><td>47294.36 (-0.23%)</td><td>47393.80 (-0.00%)</td><td>46957.40 (-0.87%)</td><td>196.56 <b>(+440.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47464.00 (n/a)</td><td>47402.48 (n/a)</td><td>47394.60 (n/a)</td><td>47368.10 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (+9.46%)</td><td>0.06 <b>(+22.57%)</b></td><td>0.06 <b>(+28.41%)</b></td><td>0.04 <b>(+23.61%)</b></td><td>0.01 (-8.18%)</td><td>182.40 (-19.08%)</td><td>145.90 (-19.47%)</td><td>143.30 <b>(-22.12%)</b></td><td>124.00 (-8.62%)</td><td>24.44 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>181.18 (n/a)</td><td>184.00 (n/a)</td><td>135.70 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.11 <b>(+53.90%)</b></td><td>0.08 <b>(+27.81%)</b></td><td>0.08 <b>(+30.29%)</b></td><td>0.06 (+4.46%)</td><td>0.02 <b>(+210.23%)</b></td><td>219.90 (-4.27%)</td><td>165.62 (-17.11%)</td><td>159.90 <b>(-23.27%)</b></td><td>112.80 <b>(-35.02%)</b></td><td>47.95 <b>(+100.94%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>199.80 (n/a)</td><td>208.40 (n/a)</td><td>173.60 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+24.83%)</b></td><td>0.05 (+5.67%)</td><td>0.05 <b>(+21.07%)</b></td><td>0.03 <b>(-20.34%)</b></td><td>0.01 <b>(+104.43%)</b></td><td>254.40 <b>(+25.51%)</b></td><td>175.54 (-0.01%)</td><td>151.60 (-17.38%)</td><td>118.40 (-19.89%)</td><td>54.35 <b>(+114.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>175.56 (n/a)</td><td>183.50 (n/a)</td><td>147.80 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 (-5.59%)</td><td>0.06 (-2.72%)</td><td>0.07 (+5.74%)</td><td>0.03 <b>(-44.18%)</b></td><td>0.02 <b>(+69.29%)</b></td><td>351.70 <b>(+79.16%)</b></td><td>186.98 (+14.35%)</td><td>149.80 (-5.43%)</td><td>132.10 (+5.93%)</td><td>92.88 <b>(+239.86%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>163.52 (n/a)</td><td>158.40 (n/a)</td><td>124.70 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (+8.12%)</td><td>0.05 (+7.43%)</td><td>0.06 (+18.29%)</td><td>0.04 (-4.67%)</td><td>0.01 <b>(+28.76%)</b></td><td>209.60 (+4.90%)</td><td>157.22 (-5.73%)</td><td>144.40 (-15.51%)</td><td>122.60 (-7.54%)</td><td>33.29 <b>(+28.68%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>166.78 (n/a)</td><td>170.90 (n/a)</td><td>132.60 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 (+13.09%)</td><td>0.06 (-7.88%)</td><td>0.06 (-1.01%)</td><td>0.04 <b>(-26.97%)</b></td><td>0.02 <b>(+136.55%)</b></td><td>267.40 <b>(+36.92%)</b></td><td>194.54 (+16.74%)</td><td>169.60 (+1.01%)</td><td>123.10 (-11.57%)</td><td>62.78 <b>(+202.46%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>166.64 (n/a)</td><td>167.90 (n/a)</td><td>139.20 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (+2.32%)</td><td>0.05 (+3.09%)</td><td>0.04 (-7.05%)</td><td>0.04 <b>(+21.41%)</b></td><td>0.01 (-18.69%)</td><td>191.30 (-17.65%)</td><td>175.18 (-3.97%)</td><td>187.90 (+7.56%)</td><td>150.00 (-2.28%)</td><td>20.66 <b>(-34.28%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>182.42 (n/a)</td><td>174.70 (n/a)</td><td>153.50 (n/a)</td><td>31.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 <b>(+40.09%)</b></td><td>0.06 (+10.17%)</td><td>0.05 (-1.10%)</td><td>0.04 <b>(-20.72%)</b></td><td>0.02 <b>(+165.48%)</b></td><td>245.10 <b>(+26.15%)</b></td><td>169.84 (-1.42%)</td><td>180.80 (+1.12%)</td><td>96.00 <b>(-28.57%)</b></td><td>55.94 <b>(+134.22%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>172.28 (n/a)</td><td>178.80 (n/a)</td><td>134.40 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+23.48%)</b></td><td>0.05 (-6.30%)</td><td>0.04 (-9.14%)</td><td>0.02 <b>(-45.23%)</b></td><td>0.02 <b>(+175.45%)</b></td><td>373.30 <b>(+82.63%)</b></td><td>207.12 <b>(+21.36%)</b></td><td>189.50 (+10.05%)</td><td>117.30 (-18.99%)</td><td>97.78 <b>(+331.32%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>170.66 (n/a)</td><td>172.20 (n/a)</td><td>144.80 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 <b>(+39.66%)</b></td><td>0.06 <b>(+43.99%)</b></td><td>0.07 <b>(+45.74%)</b></td><td>0.05 <b>(+39.76%)</b></td><td>0.01 <b>(+54.70%)</b></td><td>192.40 <b>(-28.45%)</b></td><td>147.50 <b>(-30.23%)</b></td><td>139.10 <b>(-31.38%)</b></td><td>122.60 <b>(-28.39%)</b></td><td>27.96 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.90 (n/a)</td><td>211.42 (n/a)</td><td>202.70 (n/a)</td><td>171.20 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 <b>(+24.47%)</b></td><td>0.05 <b>(+22.29%)</b></td><td>0.05 (+17.64%)</td><td>0.04 <b>(+26.64%)</b></td><td>0.01 <b>(+24.16%)</b></td><td>232.20 <b>(-21.02%)</b></td><td>171.26 (-18.35%)</td><td>162.00 (-14.96%)</td><td>136.10 (-19.66%)</td><td>37.57 <b>(-23.19%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.00 (n/a)</td><td>209.76 (n/a)</td><td>190.50 (n/a)</td><td>169.40 (n/a)</td><td>48.91 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 <b>(+44.49%)</b></td><td>0.05 <b>(+39.69%)</b></td><td>0.05 <b>(+38.43%)</b></td><td>0.04 <b>(+80.73%)</b></td><td>0.01 (+11.84%)</td><td>193.40 <b>(-44.68%)</b></td><td>163.64 <b>(-30.45%)</b></td><td>162.30 <b>(-27.77%)</b></td><td>122.20 <b>(-30.80%)</b></td><td>27.59 <b>(-59.14%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>349.60 (n/a)</td><td>235.30 (n/a)</td><td>224.70 (n/a)</td><td>176.60 (n/a)</td><td>67.53 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (+5.38%)</td><td>0.05 (+13.76%)</td><td>0.05 (+16.05%)</td><td>0.04 <b>(+25.94%)</b></td><td>0.01 (-13.43%)</td><td>193.00 <b>(-20.61%)</b></td><td>159.58 (-13.38%)</td><td>158.90 (-13.88%)</td><td>135.00 (-5.13%)</td><td>24.69 <b>(-36.21%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>184.24 (n/a)</td><td>184.50 (n/a)</td><td>142.30 (n/a)</td><td>38.71 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (+15.05%)</td><td>0.05 (+9.45%)</td><td>0.05 (+12.56%)</td><td>0.04 (+2.36%)</td><td>0.01 <b>(+101.47%)</b></td><td>214.40 (-2.28%)</td><td>189.92 (-7.99%)</td><td>181.10 (-11.18%)</td><td>166.70 (-13.09%)</td><td>21.43 <b>(+72.42%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>206.42 (n/a)</td><td>203.90 (n/a)</td><td>191.80 (n/a)</td><td>12.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 <b>(+28.17%)</b></td><td>0.04 <b>(+27.81%)</b></td><td>0.05 <b>(+26.49%)</b></td><td>0.04 <b>(+58.58%)</b></td><td>0.01 (-13.07%)</td><td>218.90 <b>(-36.93%)</b></td><td>184.82 <b>(-23.68%)</b></td><td>175.40 <b>(-20.96%)</b></td><td>155.00 <b>(-21.95%)</b></td><td>24.90 <b>(-58.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>347.10 (n/a)</td><td>242.16 (n/a)</td><td>221.90 (n/a)</td><td>198.60 (n/a)</td><td>60.07 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.75 (-6.91%)</td><td>0.61 (+7.60%)</td><td>0.66 <b>(+24.05%)</b></td><td>0.41 (+5.76%)</td><td>0.13 <b>(-25.58%)</b></td><td>240.60 (-5.42%)</td><td>168.92 (-9.84%)</td><td>148.80 (-19.39%)</td><td>131.90 (+7.41%)</td><td>42.94 <b>(-22.51%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.80 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.17 (n/a)</td><td>254.40 (n/a)</td><td>187.36 (n/a)</td><td>184.60 (n/a)</td><td>122.80 (n/a)</td><td>55.41 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.74 (-12.96%)</td><td>0.68 (+12.87%)</td><td>0.72 <b>(+36.43%)</b></td><td>0.59 (+17.30%)</td><td>0.07 <b>(-50.09%)</b></td><td>165.40 (-14.74%)</td><td>146.64 (-13.73%)</td><td>136.00 <b>(-26.68%)</b></td><td>133.30 (+14.91%)</td><td>15.92 <b>(-49.75%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.85 (n/a)</td><td>0.60 (n/a)</td><td>0.53 (n/a)</td><td>0.51 (n/a)</td><td>0.14 (n/a)</td><td>194.00 (n/a)</td><td>169.98 (n/a)</td><td>185.50 (n/a)</td><td>116.00 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.70 (-12.13%)</td><td>0.63 (+15.71%)</td><td>0.61 <b>(+28.31%)</b></td><td>0.58 <b>(+38.87%)</b></td><td>0.05 <b>(-65.60%)</b></td><td>170.70 <b>(-27.97%)</b></td><td>158.18 (-17.79%)</td><td>162.10 <b>(-22.07%)</b></td><td>140.20 (+13.80%)</td><td>13.14 <b>(-71.26%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.80 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.16 (n/a)</td><td>237.00 (n/a)</td><td>192.40 (n/a)</td><td>208.00 (n/a)</td><td>123.20 (n/a)</td><td>45.72 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.61 (-14.64%)</td><td>0.46 (-5.81%)</td><td>0.47 (+3.35%)</td><td>0.34 (-11.27%)</td><td>0.10 (-17.36%)</td><td>288.80 (+12.68%)</td><td>222.08 (+6.01%)</td><td>211.40 (-3.21%)</td><td>162.30 (+17.18%)</td><td>50.31 (+16.40%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.71 (n/a)</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.13 (n/a)</td><td>256.30 (n/a)</td><td>209.48 (n/a)</td><td>218.40 (n/a)</td><td>138.50 (n/a)</td><td>43.22 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.49 (+0.01%)</td><td>0.47 (+14.56%)</td><td>0.47 (+16.65%)</td><td>0.43 <b>(+46.21%)</b></td><td>0.02 <b>(-68.25%)</b></td><td>171.10 <b>(-31.59%)</b></td><td>157.88 (-15.20%)</td><td>156.50 (-14.29%)</td><td>149.50 (+0.00%)</td><td>8.38 <b>(-78.55%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>250.10 (n/a)</td><td>186.18 (n/a)</td><td>182.60 (n/a)</td><td>149.50 (n/a)</td><td>39.08 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.59 <b>(+33.68%)</b></td><td>0.47 <b>(+25.64%)</b></td><td>0.49 <b>(+33.36%)</b></td><td>0.39 <b>(+33.87%)</b></td><td>0.08 <b>(+31.15%)</b></td><td>188.30 <b>(-25.31%)</b></td><td>159.20 <b>(-20.39%)</b></td><td>149.60 <b>(-25.01%)</b></td><td>124.60 <b>(-25.17%)</b></td><td>26.70 <b>(-23.59%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>252.10 (n/a)</td><td>199.98 (n/a)</td><td>199.50 (n/a)</td><td>166.50 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.76 <b>(+29.00%)</b></td><td>0.50 (+17.13%)</td><td>0.47 <b>(+20.29%)</b></td><td>0.33 (+9.04%)</td><td>0.16 <b>(+37.02%)</b></td><td>220.30 (-8.32%)</td><td>159.28 (-13.38%)</td><td>155.60 (-16.84%)</td><td>96.90 <b>(-22.48%)</b></td><td>44.83 (-5.85%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.12 (n/a)</td><td>240.30 (n/a)</td><td>183.88 (n/a)</td><td>187.10 (n/a)</td><td>125.00 (n/a)</td><td>47.62 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.50 (-4.10%)</td><td>0.43 (+7.35%)</td><td>0.43 (+2.68%)</td><td>0.34 (+13.10%)</td><td>0.06 <b>(-31.59%)</b></td><td>214.20 (-11.56%)</td><td>174.92 (-8.69%)</td><td>172.90 (-2.65%)</td><td>147.70 (+4.31%)</td><td>25.11 <b>(-37.00%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>242.20 (n/a)</td><td>191.56 (n/a)</td><td>177.60 (n/a)</td><td>141.60 (n/a)</td><td>39.86 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.03 <b>(+36.37%)</b></td><td>0.80 <b>(+21.82%)</b></td><td>0.74 (+14.17%)</td><td>0.66 (+19.17%)</td><td>0.15 <b>(+107.83%)</b></td><td>199.10 (-16.10%)</td><td>168.86 (-16.54%)</td><td>178.00 (-12.44%)</td><td>126.60 <b>(-26.69%)</b></td><td>29.50 <b>(+26.78%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.07 (n/a)</td><td>237.30 (n/a)</td><td>202.32 (n/a)</td><td>203.30 (n/a)</td><td>172.70 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.17 <b>(+59.04%)</b></td><td>0.84 <b>(+23.77%)</b></td><td>0.84 <b>(+21.22%)</b></td><td>0.55 (-12.43%)</td><td>0.24 <b>(+502.14%)</b></td><td>237.30 (+14.20%)</td><td>166.32 (-13.82%)</td><td>156.30 (-17.52%)</td><td>112.30 <b>(-37.16%)</b></td><td>48.99 <b>(+333.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.73 (n/a)</td><td>0.68 (n/a)</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.04 (n/a)</td><td>207.80 (n/a)</td><td>193.00 (n/a)</td><td>189.50 (n/a)</td><td>178.70 (n/a)</td><td>11.29 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.96 (-1.02%)</td><td>0.78 (+8.84%)</td><td>0.73 (+9.87%)</td><td>0.70 (+18.10%)</td><td>0.11 <b>(-28.66%)</b></td><td>188.20 (-15.30%)</td><td>169.94 (-9.84%)</td><td>179.50 (-8.98%)</td><td>136.80 (+1.03%)</td><td>22.29 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.97 (n/a)</td><td>0.72 (n/a)</td><td>0.66 (n/a)</td><td>0.59 (n/a)</td><td>0.16 (n/a)</td><td>222.20 (n/a)</td><td>188.48 (n/a)</td><td>197.20 (n/a)</td><td>135.40 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-15.98%)</td><td>1019.42 (-1.01%)</td><td>980.92 (-0.02%)</td><td>976.11 (-0.72%)</td><td>960.03 (+0.81%)</td><td>23.39 <b>(-26.38%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1029.85 (n/a)</td><td>981.13 (n/a)</td><td>983.16 (n/a)</td><td>952.29 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.01 (+6.25%)</td><td>0.01 (+3.09%)</td><td>0.01 (+2.56%)</td><td>0.01 (+2.74%)</td><td>0.00 <b>(+33.45%)</b></td><td>1092.88 (-2.23%)</td><td>1023.59 (-3.02%)</td><td>1025.99 (-2.00%)</td><td>960.47 (-6.13%)</td><td>47.93 <b>(+30.06%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1117.85 (n/a)</td><td>1055.45 (n/a)</td><td>1046.90 (n/a)</td><td>1023.17 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.98 (+0.24%)</td><td>0.95 (-0.19%)</td><td>0.95 (-0.90%)</td><td>0.94 (+0.41%)</td><td>0.01 (-4.71%)</td><td>2221.10 (-0.41%)</td><td>2196.89 (+0.19%)</td><td>2207.94 (+0.90%)</td><td>2150.73 (-0.23%)</td><td>28.00 (-5.42%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2230.19 (n/a)</td><td>2192.65 (n/a)</td><td>2188.24 (n/a)</td><td>2155.77 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.40 (+2.47%)</td><td>0.39 (+2.63%)</td><td>0.39 (+2.71%)</td><td>0.38 (+2.67%)</td><td>0.01 (+12.38%)</td><td>1365.09 (-2.60%)</td><td>1340.95 (-2.55%)</td><td>1344.76 (-2.62%)</td><td>1303.28 (-2.42%)</td><td>26.48 (+7.81%)</td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1401.49 (n/a)</td><td>1376.11 (n/a)</td><td>1380.99 (n/a)</td><td>1335.55 (n/a)</td><td>24.56 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.26 (+2.76%)</td><td>0.25 (+0.00%)</td><td>0.25 (+0.48%)</td><td>0.24 (-1.71%)</td><td>0.01 <b>(+118.94%)</b></td><td>2172.23 (+1.76%)</td><td>2099.35 (+0.05%)</td><td>2091.35 (-0.49%)</td><td>2013.67 (-2.66%)</td><td>63.35 <b>(+117.29%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.00 (n/a)</td><td>2134.63 (n/a)</td><td>2098.25 (n/a)</td><td>2101.74 (n/a)</td><td>2068.61 (n/a)</td><td>29.16 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.37 (+2.14%)</td><td>0.36 (-0.13%)</td><td>0.36 (-0.58%)</td><td>0.35 (-1.25%)</td><td>0.01 <b>(+177.86%)</b></td><td>1477.20 (+1.27%)</td><td>1451.54 (+0.16%)</td><td>1459.38 (+0.59%)</td><td>1405.68 (-2.10%)</td><td>27.32 <b>(+176.43%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1458.69 (n/a)</td><td>1449.16 (n/a)</td><td>1450.78 (n/a)</td><td>1435.80 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.37 (-3.27%)</td><td>3.23 <b>(+23.18%)</b></td><td>3.23 <b>(+21.68%)</b></td><td>3.09 <b>(+67.94%)</b></td><td>0.10 <b>(-83.50%)</b></td><td>169.90 <b>(-40.45%)</b></td><td>162.48 <b>(-22.44%)</b></td><td>162.10 (-17.84%)</td><td>155.30 (+3.33%)</td><td>5.18 <b>(-89.88%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>3.49 (n/a)</td><td>2.62 (n/a)</td><td>2.66 (n/a)</td><td>1.84 (n/a)</td><td>0.62 (n/a)</td><td>285.30 (n/a)</td><td>209.48 (n/a)</td><td>197.30 (n/a)</td><td>150.30 (n/a)</td><td>51.19 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>6.14 (+9.58%)</td><td>5.57 <b>(+21.39%)</b></td><td>5.59 <b>(+22.30%)</b></td><td>4.93 <b>(+29.72%)</b></td><td>0.45 <b>(-31.96%)</b></td><td>212.80 <b>(-22.90%)</b></td><td>189.30 (-18.49%)</td><td>187.70 (-18.25%)</td><td>170.70 (-8.72%)</td><td>15.65 <b>(-51.40%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>5.61 (n/a)</td><td>4.59 (n/a)</td><td>4.57 (n/a)</td><td>3.80 (n/a)</td><td>0.66 (n/a)</td><td>276.00 (n/a)</td><td>232.24 (n/a)</td><td>229.60 (n/a)</td><td>187.00 (n/a)</td><td>32.20 (n/a)</td>
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
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.42 <b>(-21.01%)</b></td><td>3.15 (-0.80%)</td><td>3.23 (+5.42%)</td><td>2.88 <b>(+22.24%)</b></td><td>0.25 <b>(-67.30%)</b></td><td>182.00 (-18.20%)</td><td>167.18 (-2.95%)</td><td>162.40 (-5.20%)</td><td>153.10 <b>(+26.63%)</b></td><td>13.35 <b>(-65.44%)</b></td>
</tr>
<tr>
<td><code>480e1e0</code> — 2026-08-28 22:00:11</td><td>4.34 (n/a)</td><td>3.18 (n/a)</td><td>3.06 (n/a)</td><td>2.36 (n/a)</td><td>0.76 (n/a)</td><td>222.50 (n/a)</td><td>172.26 (n/a)</td><td>171.30 (n/a)</td><td>120.90 (n/a)</td><td>38.64 (n/a)</td>
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
