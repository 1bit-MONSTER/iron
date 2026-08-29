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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.10 (+10.50%)</td><td>0.07 (+5.09%)</td><td>0.08 (+10.49%)</td><td>0.05 (+3.63%)</td><td>0.02 <b>(+51.51%)</b></td><td>243.00 (-3.49%)</td><td>178.68 (-1.45%)</td><td>158.70 (-9.47%)</td><td>129.00 (-9.54%)</td><td>54.61 <b>(+29.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>251.80 (n/a)</td><td>181.30 (n/a)</td><td>175.30 (n/a)</td><td>142.60 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.09 (-11.90%)</td><td>0.07 (+8.03%)</td><td>0.08 (+19.65%)</td><td>0.06 (+18.92%)</td><td>0.01 <b>(-38.04%)</b></td><td>197.70 (-15.91%)</td><td>167.88 (-10.24%)</td><td>156.60 (-16.44%)</td><td>137.80 (+13.51%)</td><td>27.20 <b>(-37.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>235.10 (n/a)</td><td>187.04 (n/a)</td><td>187.40 (n/a)</td><td>121.40 (n/a)</td><td>43.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 <b>(-24.72%)</b></td><td>0.06 (+0.96%)</td><td>0.06 (+13.58%)</td><td>0.06 (+14.77%)</td><td>0.00 <b>(-78.37%)</b></td><td>203.80 (-12.87%)</td><td>191.24 (-4.65%)</td><td>189.70 (-11.97%)</td><td>177.00 <b>(+32.88%)</b></td><td>10.29 <b>(-73.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.90 (n/a)</td><td>200.56 (n/a)</td><td>215.50 (n/a)</td><td>133.20 (n/a)</td><td>39.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (-13.17%)</td><td>0.06 (+0.32%)</td><td>0.06 (-0.42%)</td><td>0.05 <b>(+36.58%)</b></td><td>0.01 <b>(-47.38%)</b></td><td>224.80 <b>(-26.80%)</b></td><td>202.12 (-5.45%)</td><td>210.50 (+0.43%)</td><td>155.20 (+15.22%)</td><td>27.01 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>307.10 (n/a)</td><td>213.76 (n/a)</td><td>209.60 (n/a)</td><td>134.70 (n/a)</td><td>62.22 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (+12.80%)</td><td>0.04 (+8.62%)</td><td>0.03 (-10.90%)</td><td>0.03 <b>(+58.62%)</b></td><td>0.01 <b>(-36.83%)</b></td><td>164.90 <b>(-36.94%)</b></td><td>147.60 (-12.88%)</td><td>152.10 (+12.25%)</td><td>115.20 (-11.38%)</td><td>19.97 <b>(-64.46%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.50 (n/a)</td><td>169.42 (n/a)</td><td>135.50 (n/a)</td><td>130.00 (n/a)</td><td>56.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (+16.33%)</td><td>0.03 <b>(+28.74%)</b></td><td>0.03 (+16.41%)</td><td>0.03 <b>(+55.30%)</b></td><td>0.01 (-19.35%)</td><td>189.70 <b>(-35.61%)</b></td><td>155.16 <b>(-26.92%)</b></td><td>165.50 (-14.12%)</td><td>115.70 (-13.98%)</td><td>30.65 <b>(-57.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.60 (n/a)</td><td>212.32 (n/a)</td><td>192.70 (n/a)</td><td>134.50 (n/a)</td><td>72.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (-5.38%)</td><td>0.04 (+4.05%)</td><td>0.04 (+6.51%)</td><td>0.04 <b>(+21.48%)</b></td><td>0.00 <b>(-51.30%)</b></td><td>145.50 (-17.70%)</td><td>134.60 (-5.42%)</td><td>134.70 (-6.13%)</td><td>121.70 (+5.64%)</td><td>9.69 <b>(-57.70%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>142.32 (n/a)</td><td>143.50 (n/a)</td><td>115.20 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (-13.84%)</td><td>0.03 (-10.52%)</td><td>0.04 (-0.84%)</td><td>0.03 (+10.35%)</td><td>0.01 <b>(-42.19%)</b></td><td>193.40 (-9.37%)</td><td>159.92 (+7.50%)</td><td>149.70 (+0.81%)</td><td>126.00 (+16.02%)</td><td>27.64 <b>(-35.65%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>148.76 (n/a)</td><td>148.50 (n/a)</td><td>108.60 (n/a)</td><td>42.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (+13.11%)</td><td>0.04 (+2.43%)</td><td>0.03 (-3.62%)</td><td>0.03 (+6.28%)</td><td>0.01 <b>(+25.49%)</b></td><td>183.60 (-5.89%)</td><td>149.78 (-1.67%)</td><td>154.20 (+3.77%)</td><td>103.90 (-11.65%)</td><td>29.35 (+0.04%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>152.32 (n/a)</td><td>148.60 (n/a)</td><td>117.60 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (-3.20%)</td><td>0.03 (-10.13%)</td><td>0.03 (-17.00%)</td><td>0.03 (-2.89%)</td><td>0.00 (-2.24%)</td><td>196.00 (+3.00%)</td><td>178.58 (+11.24%)</td><td>183.20 <b>(+20.45%)</b></td><td>146.10 (+3.25%)</td><td>18.99 (+0.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>160.54 (n/a)</td><td>152.10 (n/a)</td><td>141.50 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 <b>(+35.99%)</b></td><td>0.03 (+10.72%)</td><td>0.03 (-9.29%)</td><td>0.03 (+10.76%)</td><td>0.01 <b>(+129.60%)</b></td><td>201.30 (-9.69%)</td><td>174.28 (-6.87%)</td><td>197.10 (+10.23%)</td><td>119.40 <b>(-26.48%)</b></td><td>36.90 <b>(+55.52%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.90 (n/a)</td><td>187.14 (n/a)</td><td>178.80 (n/a)</td><td>162.40 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (+5.86%)</td><td>0.03 (+2.62%)</td><td>0.02 (-5.53%)</td><td>0.02 (-4.98%)</td><td>0.00 <b>(+97.02%)</b></td><td>239.10 (+5.24%)</td><td>211.06 (-1.35%)</td><td>228.70 (+5.88%)</td><td>178.10 (-5.52%)</td><td>29.60 <b>(+94.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>213.94 (n/a)</td><td>216.00 (n/a)</td><td>188.50 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>163.50 (n/a)</td><td>149.72 (n/a)</td><td>154.70 (n/a)</td><td>131.20 (n/a)</td><td>12.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>284.10 (n/a)</td><td>197.82 (n/a)</td><td>174.00 (n/a)</td><td>167.30 (n/a)</td><td>49.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>187.00 (n/a)</td><td>189.40 (n/a)</td><td>160.40 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>209.88 (n/a)</td><td>210.50 (n/a)</td><td>183.20 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>166.26 (n/a)</td><td>165.50 (n/a)</td><td>106.30 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>263.80 (n/a)</td><td>187.60 (n/a)</td><td>172.10 (n/a)</td><td>151.20 (n/a)</td><td>44.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>172.60 (n/a)</td><td>165.34 (n/a)</td><td>168.80 (n/a)</td><td>149.30 (n/a)</td><td>9.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>182.04 (n/a)</td><td>177.30 (n/a)</td><td>165.90 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.20 (n/a)</td><td>233.38 (n/a)</td><td>179.40 (n/a)</td><td>152.00 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.40 (n/a)</td><td>176.14 (n/a)</td><td>173.80 (n/a)</td><td>153.40 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>159.36 (n/a)</td><td>157.40 (n/a)</td><td>141.40 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.40 (n/a)</td><td>197.10 (n/a)</td><td>180.60 (n/a)</td><td>150.70 (n/a)</td><td>58.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>180.76 (n/a)</td><td>178.00 (n/a)</td><td>148.40 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.50 (n/a)</td><td>207.90 (n/a)</td><td>215.90 (n/a)</td><td>187.10 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.30 (n/a)</td><td>193.64 (n/a)</td><td>199.30 (n/a)</td><td>179.00 (n/a)</td><td>13.40 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.40 (n/a)</td><td>232.44 (n/a)</td><td>219.00 (n/a)</td><td>193.60 (n/a)</td><td>48.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.33 (+1.66%)</td><td>3.97 (-5.29%)</td><td>4.17 (-0.95%)</td><td>3.51 (-13.41%)</td><td>0.36 <b>(+339.69%)</b></td><td>2680.20 (+15.49%)</td><td>2385.42 (+6.27%)</td><td>2256.70 (+0.96%)</td><td>2172.80 (-1.63%)</td><td>222.94 <b>(+399.84%)</b></td><td>1702.55 (+1.66%)</td><td>1561.37 (-5.29%)</td><td>1639.27 (-0.95%)</td><td>1380.29 (-13.41%)</td><td>141.10 <b>(+339.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>4.26 (n/a)</td><td>4.19 (n/a)</td><td>4.21 (n/a)</td><td>4.05 (n/a)</td><td>0.08 (n/a)</td><td>2320.70 (n/a)</td><td>2244.60 (n/a)</td><td>2235.20 (n/a)</td><td>2208.90 (n/a)</td><td>44.60 (n/a)</td><td>1674.75 (n/a)</td><td>1648.62 (n/a)</td><td>1655.03 (n/a)</td><td>1594.08 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.15 <b>(-27.13%)</b></td><td>0.94 (-19.50%)</td><td>1.05 (+0.38%)</td><td>0.67 <b>(-29.29%)</b></td><td>0.23 (-6.72%)</td><td>332.60 <b>(+41.41%)</b></td><td>249.88 <b>(+27.19%)</b></td><td>210.20 (-0.38%)</td><td>192.90 <b>(+37.30%)</b></td><td>67.92 <b>(+86.75%)</b></td><td>48.93 <b>(-27.13%)</b></td><td>39.92 (-19.50%)</td><td>44.89 (+0.38%)</td><td>28.37 <b>(-29.29%)</b></td><td>9.92 (-6.72%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.57 (n/a)</td><td>1.16 (n/a)</td><td>1.05 (n/a)</td><td>0.94 (n/a)</td><td>0.25 (n/a)</td><td>235.20 (n/a)</td><td>196.46 (n/a)</td><td>211.00 (n/a)</td><td>140.50 (n/a)</td><td>36.37 (n/a)</td><td>67.15 (n/a)</td><td>49.59 (n/a)</td><td>44.72 (n/a)</td><td>40.13 (n/a)</td><td>10.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.35 <b>(+42.19%)</b></td><td>0.98 <b>(+21.43%)</b></td><td>1.05 <b>(+38.05%)</b></td><td>0.69 (+1.45%)</td><td>0.28 <b>(+125.65%)</b></td><td>319.10 (-1.42%)</td><td>242.50 (-13.34%)</td><td>211.00 <b>(-27.54%)</b></td><td>164.10 <b>(-29.66%)</b></td><td>71.69 <b>(+70.17%)</b></td><td>57.52 <b>(+42.19%)</b></td><td>41.73 <b>(+21.43%)</b></td><td>44.73 <b>(+38.05%)</b></td><td>29.58 (+1.45%)</td><td>12.06 <b>(+125.65%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.95 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>323.70 (n/a)</td><td>279.84 (n/a)</td><td>291.20 (n/a)</td><td>233.30 (n/a)</td><td>42.13 (n/a)</td><td>40.45 (n/a)</td><td>34.37 (n/a)</td><td>32.40 (n/a)</td><td>29.16 (n/a)</td><td>5.34 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.52 (+0.06%)</td><td>0.52 (+0.05%)</td><td>0.52 (+0.05%)</td><td>0.52 (+0.00%)</td><td>0.00 <b>(+24.30%)</b></td><td>48627.60 (-0.00%)</td><td>48503.70 (-0.05%)</td><td>48483.60 (-0.05%)</td><td>48440.80 (-0.06%)</td><td>76.34 <b>(+24.22%)</b></td><td>354.66 (+0.06%)</td><td>354.20 (+0.05%)</td><td>354.34 (+0.05%)</td><td>353.29 (+0.00%)</td><td>0.56 <b>(+24.30%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48627.80 (n/a)</td><td>48527.34 (n/a)</td><td>48507.70 (n/a)</td><td>48470.50 (n/a)</td><td>61.45 (n/a)</td><td>354.44 (n/a)</td><td>354.02 (n/a)</td><td>354.17 (n/a)</td><td>353.29 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.90 (-0.68%)</td><td>0.89 (-0.39%)</td><td>0.89 (-0.87%)</td><td>0.88 (+0.30%)</td><td>0.00 <b>(-51.30%)</b></td><td>28467.90 (-0.30%)</td><td>28256.22 (+0.38%)</td><td>28262.40 (+0.88%)</td><td>28094.00 (+0.68%)</td><td>141.19 <b>(-51.06%)</b></td><td>611.51 (-0.68%)</td><td>608.02 (-0.39%)</td><td>607.87 (-0.87%)</td><td>603.48 (+0.30%)</td><td>3.03 <b>(-51.30%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28554.10 (n/a)</td><td>28148.18 (n/a)</td><td>28015.60 (n/a)</td><td>27903.40 (n/a)</td><td>288.52 (n/a)</td><td>615.69 (n/a)</td><td>610.39 (n/a)</td><td>613.22 (n/a)</td><td>601.66 (n/a)</td><td>6.23 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>3.33 (+1.71%)</td><td>3.25 (+2.50%)</td><td>3.24 (+2.46%)</td><td>3.18 (+2.88%)</td><td>0.06 (-10.16%)</td><td>7910.60 (-2.80%)</td><td>7750.22 (-2.45%)</td><td>7755.80 (-2.40%)</td><td>7549.80 (-1.68%)</td><td>146.54 (-13.82%)</td><td>2275.55 (+1.71%)</td><td>2217.34 (+2.50%)</td><td>2215.10 (+2.46%)</td><td>2171.76 (+2.88%)</td><td>42.12 (-10.16%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.28 (n/a)</td><td>3.17 (n/a)</td><td>3.17 (n/a)</td><td>3.09 (n/a)</td><td>0.07 (n/a)</td><td>8138.70 (n/a)</td><td>7944.60 (n/a)</td><td>7946.70 (n/a)</td><td>7679.00 (n/a)</td><td>170.05 (n/a)</td><td>2237.26 (n/a)</td><td>2163.26 (n/a)</td><td>2161.88 (n/a)</td><td>2110.88 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.23 (+2.44%)</td><td>3.64 (+7.71%)</td><td>3.63 (+13.10%)</td><td>3.02 (+1.88%)</td><td>0.43 (-4.05%)</td><td>2665.30 (-1.85%)</td><td>2239.66 (-7.26%)</td><td>2221.30 (-11.59%)</td><td>1904.80 (-2.38%)</td><td>273.25 (-4.88%)</td><td>1109.81 (+2.44%)</td><td>954.77 (+7.71%)</td><td>951.66 (+13.10%)</td><td>793.12 (+1.88%)</td><td>112.56 (-4.05%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>4.13 (n/a)</td><td>3.38 (n/a)</td><td>3.21 (n/a)</td><td>2.97 (n/a)</td><td>0.45 (n/a)</td><td>2715.50 (n/a)</td><td>2415.00 (n/a)</td><td>2512.40 (n/a)</td><td>1951.30 (n/a)</td><td>287.28 (n/a)</td><td>1083.32 (n/a)</td><td>886.45 (n/a)</td><td>841.40 (n/a)</td><td>778.48 (n/a)</td><td>117.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.36 <b>(-22.20%)</b></td><td>0.32 (-9.94%)</td><td>0.32 (-4.44%)</td><td>0.29 (-10.02%)</td><td>0.03 <b>(-50.63%)</b></td><td>4354.30 (+11.14%)</td><td>3881.08 (+9.74%)</td><td>3888.10 (+4.65%)</td><td>3457.50 <b>(+28.53%)</b></td><td>353.37 <b>(-27.76%)</b></td><td>19.41 <b>(-22.20%)</b></td><td>17.41 (-9.94%)</td><td>17.26 (-4.44%)</td><td>15.41 (-10.02%)</td><td>1.58 <b>(-50.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>3918.00 (n/a)</td><td>3536.72 (n/a)</td><td>3715.50 (n/a)</td><td>2690.00 (n/a)</td><td>489.16 (n/a)</td><td>24.95 (n/a)</td><td>19.33 (n/a)</td><td>18.06 (n/a)</td><td>17.13 (n/a)</td><td>3.20 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.97 (-0.98%)</td><td>4.06 (-6.92%)</td><td>3.74 <b>(-21.31%)</b></td><td>3.42 (-1.57%)</td><td>0.72 (+3.99%)</td><td>1942.60 (+1.60%)</td><td>1679.38 (+7.69%)</td><td>1779.80 <b>(+27.07%)</b></td><td>1339.50 (+0.99%)</td><td>280.77 (+6.91%)</td><td>1534.27 (-0.98%)</td><td>1253.27 (-6.92%)</td><td>1154.72 <b>(-21.31%)</b></td><td>1057.98 (-1.57%)</td><td>221.05 (+3.99%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>5.02 (n/a)</td><td>4.36 (n/a)</td><td>4.75 (n/a)</td><td>3.48 (n/a)</td><td>0.69 (n/a)</td><td>1912.10 (n/a)</td><td>1559.52 (n/a)</td><td>1400.60 (n/a)</td><td>1326.40 (n/a)</td><td>262.62 (n/a)</td><td>1549.49 (n/a)</td><td>1346.45 (n/a)</td><td>1467.42 (n/a)</td><td>1074.87 (n/a)</td><td>212.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>13.42 (n/a)</td><td>12.94 (n/a)</td><td>13.19 (n/a)</td><td>12.15 (n/a)</td><td>0.54 (n/a)</td><td>13.41 (n/a)</td><td>12.93 (n/a)</td><td>13.19 (n/a)</td><td>12.14 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>24.57 (+1.19%)</td><td>24.18 (+0.06%)</td><td>24.29 (+0.42%)</td><td>23.50 (-2.16%)</td><td>0.40 <b>(+314.40%)</b></td><td>24.55 (+1.19%)</td><td>24.16 (+0.06%)</td><td>24.27 (+0.42%)</td><td>23.49 (-2.16%)</td><td>0.40 <b>(+314.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>24.28 (n/a)</td><td>24.16 (n/a)</td><td>24.19 (n/a)</td><td>24.02 (n/a)</td><td>0.10 (n/a)</td><td>24.26 (n/a)</td><td>24.15 (n/a)</td><td>24.17 (n/a)</td><td>24.01 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>40.43 (-2.61%)</td><td>39.25 (-4.07%)</td><td>39.46 (-3.36%)</td><td>37.55 (-6.51%)</td><td>1.07 <b>(+98.33%)</b></td><td>40.40 (-2.61%)</td><td>39.23 (-4.07%)</td><td>39.44 (-3.36%)</td><td>37.53 (-6.51%)</td><td>1.07 <b>(+98.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>41.51 (n/a)</td><td>40.91 (n/a)</td><td>40.84 (n/a)</td><td>40.17 (n/a)</td><td>0.54 (n/a)</td><td>41.49 (n/a)</td><td>40.89 (n/a)</td><td>40.81 (n/a)</td><td>40.14 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>43.55 (-4.22%)</td><td>41.94 (+0.45%)</td><td>43.00 (+3.75%)</td><td>39.40 (+2.63%)</td><td>1.82 <b>(-32.80%)</b></td><td>43.52 (-4.22%)</td><td>41.91 (+0.45%)</td><td>42.97 (+3.75%)</td><td>39.38 (+2.63%)</td><td>1.82 <b>(-32.80%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>45.47 (n/a)</td><td>41.75 (n/a)</td><td>41.44 (n/a)</td><td>38.39 (n/a)</td><td>2.70 (n/a)</td><td>45.44 (n/a)</td><td>41.72 (n/a)</td><td>41.42 (n/a)</td><td>38.37 (n/a)</td><td>2.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>13.36 (n/a)</td><td>11.88 (n/a)</td><td>12.12 (n/a)</td><td>10.89 (n/a)</td><td>1.03 (n/a)</td><td>13.35 (n/a)</td><td>11.87 (n/a)</td><td>12.11 (n/a)</td><td>10.88 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>24.71 (-0.25%)</td><td>24.19 (-0.24%)</td><td>24.12 (-0.80%)</td><td>23.69 (+2.46%)</td><td>0.40 <b>(-40.29%)</b></td><td>24.70 (-0.25%)</td><td>24.17 (-0.24%)</td><td>24.11 (-0.80%)</td><td>23.68 (+2.46%)</td><td>0.40 <b>(-40.29%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>24.77 (n/a)</td><td>24.24 (n/a)</td><td>24.31 (n/a)</td><td>23.12 (n/a)</td><td>0.67 (n/a)</td><td>24.76 (n/a)</td><td>24.23 (n/a)</td><td>24.30 (n/a)</td><td>23.11 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>42.51 (+1.91%)</td><td>39.95 (-1.59%)</td><td>39.47 (-4.63%)</td><td>37.82 (-2.75%)</td><td>1.80 <b>(+40.61%)</b></td><td>42.48 (+1.91%)</td><td>39.92 (-1.59%)</td><td>39.45 (-4.63%)</td><td>37.80 (-2.75%)</td><td>1.80 <b>(+40.61%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>41.71 (n/a)</td><td>40.59 (n/a)</td><td>41.39 (n/a)</td><td>38.89 (n/a)</td><td>1.28 (n/a)</td><td>41.68 (n/a)</td><td>40.57 (n/a)</td><td>41.36 (n/a)</td><td>38.86 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>45.42 (+3.94%)</td><td>39.36 (-0.58%)</td><td>40.36 (-6.98%)</td><td>29.95 <b>(+21.05%)</b></td><td>5.94 <b>(-28.50%)</b></td><td>45.39 (+3.94%)</td><td>39.34 (-0.58%)</td><td>40.34 (-6.98%)</td><td>29.93 <b>(+21.05%)</b></td><td>5.94 <b>(-28.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>43.70 (n/a)</td><td>39.59 (n/a)</td><td>43.39 (n/a)</td><td>24.74 (n/a)</td><td>8.31 (n/a)</td><td>43.67 (n/a)</td><td>39.57 (n/a)</td><td>43.36 (n/a)</td><td>24.73 (n/a)</td><td>8.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>9.32 (-3.24%)</td><td>8.94 (+0.19%)</td><td>9.00 (+3.74%)</td><td>8.40 (-0.06%)</td><td>0.34 <b>(-32.86%)</b></td><td>9.30 (-3.24%)</td><td>8.92 (+0.19%)</td><td>8.98 (+3.74%)</td><td>8.38 (-0.06%)</td><td>0.34 <b>(-32.86%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>9.63 (n/a)</td><td>8.92 (n/a)</td><td>8.67 (n/a)</td><td>8.40 (n/a)</td><td>0.51 (n/a)</td><td>9.62 (n/a)</td><td>8.90 (n/a)</td><td>8.65 (n/a)</td><td>8.39 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.01 (-4.85%)</td><td>0.93 (-0.54%)</td><td>0.94 (+3.62%)</td><td>0.80 (-1.37%)</td><td>0.09 (-17.30%)</td><td>1.00 (-4.85%)</td><td>0.91 (-0.54%)</td><td>0.93 (+3.62%)</td><td>0.79 (-1.37%)</td><td>0.09 (-17.30%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.07 (n/a)</td><td>0.93 (n/a)</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.11 (n/a)</td><td>1.05 (n/a)</td><td>0.92 (n/a)</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.42 (+3.39%)</td><td>1.20 (+7.21%)</td><td>1.10 (-0.81%)</td><td>1.06 (+15.85%)</td><td>0.17 (+2.05%)</td><td>1.41 (+3.39%)</td><td>1.18 (+7.21%)</td><td>1.09 (-0.81%)</td><td>1.04 (+15.85%)</td><td>0.17 (+2.05%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.38 (n/a)</td><td>1.12 (n/a)</td><td>1.11 (n/a)</td><td>0.91 (n/a)</td><td>0.17 (n/a)</td><td>1.36 (n/a)</td><td>1.10 (n/a)</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>17.66 (+4.95%)</td><td>15.47 (+0.21%)</td><td>16.31 (+4.21%)</td><td>13.11 (+0.83%)</td><td>2.15 <b>(+48.50%)</b></td><td>17.45 (+4.95%)</td><td>15.30 (+0.21%)</td><td>16.12 (+4.21%)</td><td>12.95 (+0.83%)</td><td>2.13 <b>(+48.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>16.83 (n/a)</td><td>15.44 (n/a)</td><td>15.65 (n/a)</td><td>13.00 (n/a)</td><td>1.45 (n/a)</td><td>16.63 (n/a)</td><td>15.26 (n/a)</td><td>15.47 (n/a)</td><td>12.85 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>14.37 (+3.85%)</td><td>13.77 (+5.76%)</td><td>13.63 (+3.76%)</td><td>13.46 (+17.93%)</td><td>0.36 <b>(-63.42%)</b></td><td>14.12 (+3.85%)</td><td>13.53 (+5.76%)</td><td>13.39 (+3.76%)</td><td>13.23 (+17.93%)</td><td>0.35 <b>(-63.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>13.84 (n/a)</td><td>13.02 (n/a)</td><td>13.13 (n/a)</td><td>11.42 (n/a)</td><td>0.98 (n/a)</td><td>13.60 (n/a)</td><td>12.79 (n/a)</td><td>12.90 (n/a)</td><td>11.22 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>7.98 (-0.16%)</td><td>7.06 (-0.55%)</td><td>7.45 (+5.27%)</td><td>5.19 (-18.32%)</td><td>1.11 <b>(+86.87%)</b></td><td>7.84 (-0.16%)</td><td>6.94 (-0.55%)</td><td>7.32 (+5.27%)</td><td>5.10 (-18.32%)</td><td>1.09 <b>(+86.87%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>8.00 (n/a)</td><td>7.10 (n/a)</td><td>7.08 (n/a)</td><td>6.35 (n/a)</td><td>0.60 (n/a)</td><td>7.86 (n/a)</td><td>6.98 (n/a)</td><td>6.95 (n/a)</td><td>6.24 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>6.11 (-1.57%)</td><td>5.74 (+7.42%)</td><td>5.67 (+4.08%)</td><td>5.54 (+19.40%)</td><td>0.23 <b>(-65.63%)</b></td><td>6.02 (-1.57%)</td><td>5.65 (+7.42%)</td><td>5.58 (+4.08%)</td><td>5.45 (+19.40%)</td><td>0.22 <b>(-65.63%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>6.21 (n/a)</td><td>5.34 (n/a)</td><td>5.45 (n/a)</td><td>4.64 (n/a)</td><td>0.66 (n/a)</td><td>6.11 (n/a)</td><td>5.26 (n/a)</td><td>5.36 (n/a)</td><td>4.57 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>13.57 (n/a)</td><td>13.31 (n/a)</td><td>13.35 (n/a)</td><td>12.88 (n/a)</td><td>0.26 (n/a)</td><td>13.57 (n/a)</td><td>13.31 (n/a)</td><td>13.35 (n/a)</td><td>12.87 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>13.40 (n/a)</td><td>12.31 (n/a)</td><td>13.23 (n/a)</td><td>10.59 (n/a)</td><td>1.35 (n/a)</td><td>13.39 (n/a)</td><td>12.31 (n/a)</td><td>13.22 (n/a)</td><td>10.58 (n/a)</td><td>1.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>170.24 (n/a)</td><td>168.40 (n/a)</td><td>145.70 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>166.86 (n/a)</td><td>171.50 (n/a)</td><td>114.20 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>181.90 (n/a)</td><td>183.00 (n/a)</td><td>167.80 (n/a)</td><td>10.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.10 (n/a)</td><td>192.66 (n/a)</td><td>195.50 (n/a)</td><td>149.00 (n/a)</td><td>49.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>177.32 (n/a)</td><td>172.20 (n/a)</td><td>136.40 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>169.88 (n/a)</td><td>165.90 (n/a)</td><td>146.80 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>178.36 (n/a)</td><td>181.10 (n/a)</td><td>142.10 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.30 (n/a)</td><td>227.04 (n/a)</td><td>207.40 (n/a)</td><td>174.20 (n/a)</td><td>61.46 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-26.11%)</b></td><td>0.05 <b>(-22.01%)</b></td><td>0.05 <b>(-27.14%)</b></td><td>0.04 (-5.29%)</td><td>0.00 <b>(-65.81%)</b></td><td>190.50 (+5.60%)</td><td>174.86 <b>(+24.99%)</b></td><td>176.40 <b>(+37.17%)</b></td><td>156.70 <b>(+35.32%)</b></td><td>14.18 <b>(-50.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>139.90 (n/a)</td><td>128.60 (n/a)</td><td>115.80 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-23.77%)</b></td><td>0.05 (-11.86%)</td><td>0.05 (-6.55%)</td><td>0.04 (-11.48%)</td><td>0.01 <b>(-38.15%)</b></td><td>229.00 (+12.97%)</td><td>184.54 (+12.26%)</td><td>177.40 (+7.06%)</td><td>160.60 <b>(+31.21%)</b></td><td>27.23 (-5.21%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>164.38 (n/a)</td><td>165.70 (n/a)</td><td>122.40 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (+2.11%)</td><td>0.05 (-2.88%)</td><td>0.05 (+0.28%)</td><td>0.04 (-9.27%)</td><td>0.01 <b>(+49.53%)</b></td><td>204.90 (+10.22%)</td><td>177.74 (+3.95%)</td><td>177.40 (-0.28%)</td><td>144.40 (-2.10%)</td><td>24.95 <b>(+64.42%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>170.98 (n/a)</td><td>177.90 (n/a)</td><td>147.50 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-23.77%)</b></td><td>0.05 (-9.19%)</td><td>0.05 (-1.55%)</td><td>0.04 (+13.32%)</td><td>0.01 <b>(-57.90%)</b></td><td>205.20 (-11.78%)</td><td>180.34 (+5.78%)</td><td>177.50 (+1.54%)</td><td>153.50 <b>(+31.20%)</b></td><td>21.14 <b>(-50.51%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>170.48 (n/a)</td><td>174.80 (n/a)</td><td>117.00 (n/a)</td><td>42.71 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-27.12%)</b></td><td>0.04 <b>(-28.62%)</b></td><td>0.04 <b>(-28.26%)</b></td><td>0.04 <b>(-21.74%)</b></td><td>0.01 <b>(-42.38%)</b></td><td>230.10 <b>(+27.76%)</b></td><td>197.52 <b>(+38.73%)</b></td><td>203.50 <b>(+39.38%)</b></td><td>162.20 <b>(+37.23%)</b></td><td>25.73 (+2.25%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>142.38 (n/a)</td><td>146.00 (n/a)</td><td>118.20 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-30.91%)</b></td><td>0.04 <b>(-25.87%)</b></td><td>0.04 <b>(-25.01%)</b></td><td>0.04 (-1.72%)</td><td>0.01 <b>(-61.49%)</b></td><td>231.20 (+1.76%)</td><td>193.12 <b>(+29.13%)</b></td><td>187.20 <b>(+33.33%)</b></td><td>171.80 <b>(+44.73%)</b></td><td>24.71 <b>(-44.82%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>149.56 (n/a)</td><td>140.40 (n/a)</td><td>118.70 (n/a)</td><td>44.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-0.54%)</td><td>0.04 (-11.84%)</td><td>0.04 (-16.52%)</td><td>0.04 (-6.50%)</td><td>0.01 (+13.07%)</td><td>231.10 (+6.94%)</td><td>197.54 (+14.09%)</td><td>205.00 (+19.74%)</td><td>147.40 (+0.55%)</td><td>31.92 (+17.89%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>173.14 (n/a)</td><td>171.20 (n/a)</td><td>146.60 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (-11.70%)</td><td>0.04 <b>(-21.36%)</b></td><td>0.04 <b>(-22.63%)</b></td><td>0.03 <b>(-34.21%)</b></td><td>0.01 <b>(+40.06%)</b></td><td>316.10 <b>(+51.97%)</b></td><td>230.62 <b>(+30.65%)</b></td><td>222.40 <b>(+29.23%)</b></td><td>172.30 (+13.21%)</td><td>53.15 <b>(+145.66%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>176.52 (n/a)</td><td>172.10 (n/a)</td><td>152.20 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-4.25%)</td><td>0.05 (-1.65%)</td><td>0.05 (+14.90%)</td><td>0.02 <b>(-37.79%)</b></td><td>0.01 <b>(+69.72%)</b></td><td>336.80 <b>(+60.76%)</b></td><td>202.34 (+10.51%)</td><td>165.50 (-12.99%)</td><td>141.40 (+4.43%)</td><td>82.00 <b>(+193.41%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>183.10 (n/a)</td><td>190.20 (n/a)</td><td>135.40 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (+2.69%)</td><td>0.04 (+0.96%)</td><td>0.04 (-8.35%)</td><td>0.03 <b>(+25.42%)</b></td><td>0.00 <b>(-34.21%)</b></td><td>264.90 <b>(-20.28%)</b></td><td>223.32 (-3.43%)</td><td>226.80 (+9.14%)</td><td>190.50 (-2.66%)</td><td>28.06 <b>(-50.69%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.30 (n/a)</td><td>231.26 (n/a)</td><td>207.80 (n/a)</td><td>195.70 (n/a)</td><td>56.89 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-28.04%)</b></td><td>0.04 (-14.01%)</td><td>0.04 (-19.05%)</td><td>0.04 <b>(+91.18%)</b></td><td>0.00 <b>(-84.30%)</b></td><td>206.10 <b>(-47.70%)</b></td><td>197.94 (-1.41%)</td><td>205.00 <b>(+23.57%)</b></td><td>177.00 <b>(+38.93%)</b></td><td>12.39 <b>(-88.83%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>394.10 (n/a)</td><td>200.78 (n/a)</td><td>165.90 (n/a)</td><td>127.40 (n/a)</td><td>110.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (-4.59%)</td><td>0.04 (-14.82%)</td><td>0.04 (-19.84%)</td><td>0.03 <b>(-22.78%)</b></td><td>0.01 <b>(+254.94%)</b></td><td>243.80 <b>(+29.47%)</b></td><td>214.26 (+18.86%)</td><td>220.70 <b>(+24.76%)</b></td><td>183.60 (+4.79%)</td><td>27.13 <b>(+376.43%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.30 (n/a)</td><td>180.26 (n/a)</td><td>176.90 (n/a)</td><td>175.20 (n/a)</td><td>5.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-6.72%)</td><td>0.05 (-3.80%)</td><td>0.05 (+1.87%)</td><td>0.04 (-18.85%)</td><td>0.01 (+5.56%)</td><td>230.80 <b>(+23.22%)</b></td><td>177.78 (+4.87%)</td><td>172.10 (-1.83%)</td><td>139.60 (+7.22%)</td><td>33.07 <b>(+46.31%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>169.52 (n/a)</td><td>175.30 (n/a)</td><td>130.20 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-3.80%)</td><td>0.05 (-19.31%)</td><td>0.05 (-18.83%)</td><td>0.03 <b>(-43.93%)</b></td><td>0.01 <b>(+214.59%)</b></td><td>286.10 <b>(+78.37%)</b></td><td>195.00 <b>(+34.54%)</b></td><td>176.90 <b>(+23.19%)</b></td><td>134.00 (+3.96%)</td><td>65.88 <b>(+472.13%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>160.40 (n/a)</td><td>144.94 (n/a)</td><td>143.60 (n/a)</td><td>128.90 (n/a)</td><td>11.51 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-11.74%)</td><td>0.05 (+2.64%)</td><td>0.05 (+2.15%)</td><td>0.04 <b>(+38.27%)</b></td><td>0.01 <b>(-55.07%)</b></td><td>201.10 <b>(-27.66%)</b></td><td>170.66 (-7.38%)</td><td>168.80 (-2.14%)</td><td>147.10 (+13.33%)</td><td>19.60 <b>(-64.66%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.00 (n/a)</td><td>184.26 (n/a)</td><td>172.50 (n/a)</td><td>129.80 (n/a)</td><td>55.47 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-13.26%)</td><td>0.05 (-1.12%)</td><td>0.05 (-5.48%)</td><td>0.04 <b>(+61.67%)</b></td><td>0.01 <b>(-63.11%)</b></td><td>191.80 <b>(-38.15%)</b></td><td>174.60 (-6.71%)</td><td>179.10 (+5.79%)</td><td>148.30 (+15.32%)</td><td>17.72 <b>(-75.19%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.10 (n/a)</td><td>187.16 (n/a)</td><td>169.30 (n/a)</td><td>128.60 (n/a)</td><td>71.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-24.30%)</b></td><td>0.04 (-18.13%)</td><td>0.04 (-9.98%)</td><td>0.03 (-16.37%)</td><td>0.01 <b>(-39.86%)</b></td><td>244.90 (+19.58%)</td><td>200.34 <b>(+20.54%)</b></td><td>192.40 (+11.09%)</td><td>163.70 <b>(+32.12%)</b></td><td>30.93 (-3.37%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>166.20 (n/a)</td><td>173.20 (n/a)</td><td>123.90 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 <b>(-20.67%)</b></td><td>0.04 (-18.03%)</td><td>0.04 (-14.90%)</td><td>0.04 <b>(-21.42%)</b></td><td>0.00 <b>(-21.78%)</b></td><td>220.50 <b>(+27.24%)</b></td><td>198.36 <b>(+21.99%)</b></td><td>199.90 (+17.52%)</td><td>176.10 <b>(+26.06%)</b></td><td>17.40 <b>(+25.62%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.30 (n/a)</td><td>162.60 (n/a)</td><td>170.10 (n/a)</td><td>139.70 (n/a)</td><td>13.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.18 (-0.02%)</td><td>0.18 (+0.01%)</td><td>0.18 (+0.08%)</td><td>0.18 (+0.06%)</td><td>0.00 (-8.57%)</td><td>47391.30 (-0.06%)</td><td>47287.48 (-0.01%)</td><td>47356.10 (-0.08%)</td><td>46967.50 (+0.02%)</td><td>179.57 (-8.65%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47421.80 (n/a)</td><td>47294.36 (n/a)</td><td>47393.80 (n/a)</td><td>46957.40 (n/a)</td><td>196.56 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (+1.70%)</td><td>0.06 (+8.08%)</td><td>0.06 (+10.51%)</td><td>0.05 (+11.28%)</td><td>0.01 <b>(-23.01%)</b></td><td>163.90 (-10.14%)</td><td>133.70 (-8.36%)</td><td>129.70 (-9.49%)</td><td>121.90 (-1.69%)</td><td>17.28 <b>(-29.32%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>145.90 (n/a)</td><td>143.30 (n/a)</td><td>124.00 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.10 (-4.76%)</td><td>0.08 (+6.59%)</td><td>0.09 (+14.00%)</td><td>0.05 (-2.05%)</td><td>0.02 (-16.74%)</td><td>224.50 (+2.09%)</td><td>152.68 (-7.81%)</td><td>140.30 (-12.26%)</td><td>118.40 (+4.96%)</td><td>42.75 (-10.86%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>165.62 (n/a)</td><td>159.90 (n/a)</td><td>112.80 (n/a)</td><td>47.95 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (+0.58%)</td><td>0.06 (+15.20%)</td><td>0.06 (+4.63%)</td><td>0.05 <b>(+45.21%)</b></td><td>0.01 <b>(-43.48%)</b></td><td>175.20 <b>(-31.13%)</b></td><td>144.04 (-17.94%)</td><td>144.90 (-4.42%)</td><td>117.70 (-0.59%)</td><td>20.70 <b>(-61.92%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>175.54 (n/a)</td><td>151.60 (n/a)</td><td>118.40 (n/a)</td><td>54.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (+2.46%)</td><td>0.07 (+9.05%)</td><td>0.06 (-5.57%)</td><td>0.06 <b>(+98.98%)</b></td><td>0.01 <b>(-47.96%)</b></td><td>176.80 <b>(-49.73%)</b></td><td>153.12 (-18.11%)</td><td>158.60 (+5.87%)</td><td>128.90 (-2.42%)</td><td>22.19 <b>(-76.11%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>351.70 (n/a)</td><td>186.98 (n/a)</td><td>149.80 (n/a)</td><td>132.10 (n/a)</td><td>92.88 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (+5.85%)</td><td>0.05 (+0.16%)</td><td>0.05 (-11.70%)</td><td>0.05 (+16.00%)</td><td>0.01 (-3.81%)</td><td>180.70 (-13.79%)</td><td>155.56 (-1.06%)</td><td>163.60 (+13.30%)</td><td>115.80 (-5.55%)</td><td>24.93 <b>(-25.13%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>157.22 (n/a)</td><td>144.40 (n/a)</td><td>122.60 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.08 (-8.39%)</td><td>0.07 <b>(+20.71%)</b></td><td>0.07 (+15.62%)</td><td>0.06 <b>(+58.92%)</b></td><td>0.01 <b>(-70.39%)</b></td><td>168.20 <b>(-37.10%)</b></td><td>148.76 <b>(-23.53%)</b></td><td>146.70 (-13.50%)</td><td>134.40 (+9.18%)</td><td>12.25 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>267.40 (n/a)</td><td>194.54 (n/a)</td><td>169.60 (n/a)</td><td>123.10 (n/a)</td><td>62.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 <b>(+20.05%)</b></td><td>0.05 (+10.94%)</td><td>0.05 <b>(+21.71%)</b></td><td>0.04 (-7.80%)</td><td>0.01 <b>(+61.83%)</b></td><td>207.50 (+8.47%)</td><td>160.36 (-8.46%)</td><td>154.40 (-17.83%)</td><td>124.90 (-16.73%)</td><td>30.34 <b>(+46.89%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>175.18 (n/a)</td><td>187.90 (n/a)</td><td>150.00 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 <b>(-24.20%)</b></td><td>0.06 (+4.11%)</td><td>0.06 (+16.11%)</td><td>0.05 <b>(+43.67%)</b></td><td>0.01 <b>(-67.08%)</b></td><td>170.60 <b>(-30.40%)</b></td><td>149.26 (-12.12%)</td><td>155.70 (-13.88%)</td><td>126.60 <b>(+31.87%)</b></td><td>17.29 <b>(-69.09%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>245.10 (n/a)</td><td>169.84 (n/a)</td><td>180.80 (n/a)</td><td>96.00 (n/a)</td><td>55.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-19.78%)</td><td>0.05 (+19.51%)</td><td>0.05 <b>(+26.81%)</b></td><td>0.05 <b>(+134.60%)</b></td><td>0.00 <b>(-89.78%)</b></td><td>159.10 <b>(-57.38%)</b></td><td>150.46 <b>(-27.36%)</b></td><td>149.40 <b>(-21.16%)</b></td><td>146.20 <b>(+24.64%)</b></td><td>5.05 <b>(-94.84%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>373.30 (n/a)</td><td>207.12 (n/a)</td><td>189.50 (n/a)</td><td>117.30 (n/a)</td><td>97.78 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (-14.00%)</td><td>0.06 (-14.00%)</td><td>0.05 (-18.61%)</td><td>0.04 (-8.93%)</td><td>0.01 (-16.91%)</td><td>211.20 (+9.77%)</td><td>170.88 (+15.85%)</td><td>170.90 <b>(+22.86%)</b></td><td>142.50 (+16.23%)</td><td>28.73 (+2.76%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>147.50 (n/a)</td><td>139.10 (n/a)</td><td>122.60 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.07 (+11.18%)</td><td>0.06 (+11.74%)</td><td>0.06 (+9.31%)</td><td>0.05 <b>(+39.15%)</b></td><td>0.01 <b>(-23.88%)</b></td><td>166.80 <b>(-28.17%)</b></td><td>150.04 (-12.39%)</td><td>148.20 (-8.52%)</td><td>122.40 (-10.07%)</td><td>18.31 <b>(-51.26%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>171.26 (n/a)</td><td>162.00 (n/a)</td><td>136.10 (n/a)</td><td>37.57 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 <b>(-21.70%)</b></td><td>0.05 (-5.88%)</td><td>0.05 (-1.56%)</td><td>0.05 (+1.27%)</td><td>0.00 <b>(-61.65%)</b></td><td>191.00 (-1.24%)</td><td>170.34 (+4.09%)</td><td>164.90 (+1.60%)</td><td>156.10 <b>(+27.74%)</b></td><td>13.58 <b>(-50.78%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>163.64 (n/a)</td><td>162.30 (n/a)</td><td>122.20 (n/a)</td><td>27.59 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (+4.62%)</td><td>0.05 (+4.40%)</td><td>0.06 (+10.55%)</td><td>0.04 (+0.54%)</td><td>0.01 (+15.54%)</td><td>192.00 (-0.52%)</td><td>153.68 (-3.70%)</td><td>143.80 (-9.50%)</td><td>129.10 (-4.37%)</td><td>27.41 (+11.01%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>159.58 (n/a)</td><td>158.90 (n/a)</td><td>135.00 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.06 (+9.64%)</td><td>0.05 (+7.83%)</td><td>0.05 (+4.94%)</td><td>0.04 (-2.82%)</td><td>0.01 <b>(+43.68%)</b></td><td>220.60 (+2.89%)</td><td>177.70 (-6.43%)</td><td>172.60 (-4.69%)</td><td>152.10 (-8.76%)</td><td>28.08 <b>(+31.05%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>189.92 (n/a)</td><td>181.10 (n/a)</td><td>166.70 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.05 (-9.54%)</td><td>0.04 (-9.32%)</td><td>0.04 (-13.54%)</td><td>0.03 (-16.06%)</td><td>0.01 (+10.16%)</td><td>260.80 (+19.14%)</td><td>205.48 (+11.18%)</td><td>202.90 (+15.68%)</td><td>171.30 (+10.52%)</td><td>35.70 <b>(+43.38%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>184.82 (n/a)</td><td>175.40 (n/a)</td><td>155.00 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.73 (-2.66%)</td><td>0.55 (-9.20%)</td><td>0.54 (-18.23%)</td><td>0.45 (+10.07%)</td><td>0.11 (-14.04%)</td><td>218.60 (-9.14%)</td><td>183.46 (+8.61%)</td><td>182.00 <b>(+22.31%)</b></td><td>135.50 (+2.73%)</td><td>33.62 <b>(-21.71%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.66 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>240.60 (n/a)</td><td>168.92 (n/a)</td><td>148.80 (n/a)</td><td>131.90 (n/a)</td><td>42.94 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.69 (-6.24%)</td><td>0.54 (-19.64%)</td><td>0.52 <b>(-27.68%)</b></td><td>0.45 <b>(-25.10%)</b></td><td>0.09 <b>(+29.58%)</b></td><td>220.90 <b>(+33.56%)</b></td><td>184.66 <b>(+25.93%)</b></td><td>188.00 <b>(+38.24%)</b></td><td>142.20 (+6.68%)</td><td>28.63 <b>(+79.91%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.07 (n/a)</td><td>165.40 (n/a)</td><td>146.64 (n/a)</td><td>136.00 (n/a)</td><td>133.30 (n/a)</td><td>15.92 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.62 (-11.44%)</td><td>0.55 (-11.93%)</td><td>0.55 (-9.96%)</td><td>0.47 (-17.93%)</td><td>0.06 (+9.55%)</td><td>207.90 <b>(+21.79%)</b></td><td>180.24 (+13.95%)</td><td>180.00 (+11.04%)</td><td>158.30 (+12.91%)</td><td>19.62 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.70 (n/a)</td><td>0.63 (n/a)</td><td>0.61 (n/a)</td><td>0.58 (n/a)</td><td>0.05 (n/a)</td><td>170.70 (n/a)</td><td>158.18 (n/a)</td><td>162.10 (n/a)</td><td>140.20 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.57 (-6.55%)</td><td>0.44 (-3.57%)</td><td>0.41 (-11.38%)</td><td>0.28 (-16.60%)</td><td>0.12 (+11.65%)</td><td>346.30 (+19.91%)</td><td>235.24 (+5.93%)</td><td>238.50 (+12.82%)</td><td>173.60 (+6.96%)</td><td>69.76 <b>(+38.66%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.61 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>288.80 (n/a)</td><td>222.08 (n/a)</td><td>211.40 (n/a)</td><td>162.30 (n/a)</td><td>50.31 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.46 (-6.26%)</td><td>0.41 (-12.19%)</td><td>0.40 (-14.09%)</td><td>0.34 <b>(-20.06%)</b></td><td>0.05 <b>(+106.87%)</b></td><td>214.00 <b>(+25.07%)</b></td><td>181.54 (+14.99%)</td><td>182.20 (+16.42%)</td><td>159.40 (+6.62%)</td><td>22.68 <b>(+170.59%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.43 (n/a)</td><td>0.02 (n/a)</td><td>171.10 (n/a)</td><td>157.88 (n/a)</td><td>156.50 (n/a)</td><td>149.50 (n/a)</td><td>8.38 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.60 (+1.39%)</td><td>0.47 (-0.32%)</td><td>0.44 (-10.43%)</td><td>0.40 (+3.26%)</td><td>0.08 (-3.20%)</td><td>182.40 (-3.13%)</td><td>159.24 (+0.03%)</td><td>167.00 (+11.63%)</td><td>122.90 (-1.36%)</td><td>23.92 (-10.43%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>188.30 (n/a)</td><td>159.20 (n/a)</td><td>149.60 (n/a)</td><td>124.60 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.51 <b>(-33.02%)</b></td><td>0.39 <b>(-20.82%)</b></td><td>0.41 (-14.30%)</td><td>0.26 <b>(-23.10%)</b></td><td>0.10 <b>(-38.58%)</b></td><td>286.50 <b>(+30.05%)</b></td><td>198.12 <b>(+24.38%)</b></td><td>181.50 (+16.65%)</td><td>144.70 <b>(+49.33%)</b></td><td>56.04 <b>(+25.01%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.76 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.16 (n/a)</td><td>220.30 (n/a)</td><td>159.28 (n/a)</td><td>155.60 (n/a)</td><td>96.90 (n/a)</td><td>44.83 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.48 (-3.05%)</td><td>0.37 (-13.86%)</td><td>0.37 (-12.10%)</td><td>0.30 (-12.96%)</td><td>0.07 <b>(+28.30%)</b></td><td>246.10 (+14.89%)</td><td>206.06 (+17.80%)</td><td>196.70 (+13.77%)</td><td>152.30 (+3.11%)</td><td>38.39 <b>(+52.88%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>214.20 (n/a)</td><td>174.92 (n/a)</td><td>172.90 (n/a)</td><td>147.70 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.82 <b>(-21.05%)</b></td><td>0.67 (-15.94%)</td><td>0.71 (-3.87%)</td><td>0.46 <b>(-29.53%)</b></td><td>0.14 (-7.45%)</td><td>282.50 <b>(+41.89%)</b></td><td>203.84 <b>(+20.72%)</b></td><td>185.20 (+4.04%)</td><td>160.40 <b>(+26.70%)</b></td><td>49.56 <b>(+68.02%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.03 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.66 (n/a)</td><td>0.15 (n/a)</td><td>199.10 (n/a)</td><td>168.86 (n/a)</td><td>178.00 (n/a)</td><td>126.60 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.98 (-16.05%)</td><td>0.67 <b>(-20.01%)</b></td><td>0.70 (-15.94%)</td><td>0.37 <b>(-32.25%)</b></td><td>0.23 (-2.92%)</td><td>350.20 <b>(+47.58%)</b></td><td>216.84 <b>(+30.38%)</b></td><td>186.00 (+19.00%)</td><td>133.80 (+19.15%)</td><td>85.02 <b>(+73.55%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>1.17 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.55 (n/a)</td><td>0.24 (n/a)</td><td>237.30 (n/a)</td><td>166.32 (n/a)</td><td>156.30 (n/a)</td><td>112.30 (n/a)</td><td>48.99 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.89 (-6.80%)</td><td>0.73 (-6.24%)</td><td>0.74 (+1.91%)</td><td>0.60 (-13.84%)</td><td>0.12 (+11.23%)</td><td>218.40 (+16.05%)</td><td>182.72 (+7.52%)</td><td>176.10 (-1.89%)</td><td>146.80 (+7.31%)</td><td>31.13 <b>(+39.65%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.96 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.70 (n/a)</td><td>0.11 (n/a)</td><td>188.20 (n/a)</td><td>169.94 (n/a)</td><td>179.50 (n/a)</td><td>136.80 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>183.70 (n/a)</td><td>204.50 (n/a)</td><td>114.70 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.00 (n/a)</td><td>184.18 (n/a)</td><td>174.60 (n/a)</td><td>107.60 (n/a)</td><td>59.85 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>170.32 (n/a)</td><td>177.20 (n/a)</td><td>121.50 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.82 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>248.90 (n/a)</td><td>177.52 (n/a)</td><td>161.40 (n/a)</td><td>152.90 (n/a)</td><td>40.37 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.09 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.78 (n/a)</td><td>0.13 (n/a)</td><td>168.50 (n/a)</td><td>137.64 (n/a)</td><td>136.60 (n/a)</td><td>120.70 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.05 (n/a)</td><td>0.80 (n/a)</td><td>0.83 (n/a)</td><td>0.57 (n/a)</td><td>0.18 (n/a)</td><td>233.00 (n/a)</td><td>172.08 (n/a)</td><td>158.30 (n/a)</td><td>126.20 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.20 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.76 (n/a)</td><td>0.19 (n/a)</td><td>173.30 (n/a)</td><td>153.90 (n/a)</td><td>164.30 (n/a)</td><td>109.80 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>1.12 (n/a)</td><td>0.93 (n/a)</td><td>1.01 (n/a)</td><td>0.74 (n/a)</td><td>0.17 (n/a)</td><td>179.10 (n/a)</td><td>146.80 (n/a)</td><td>130.30 (n/a)</td><td>118.30 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.50 (n/a)</td><td>155.66 (n/a)</td><td>165.10 (n/a)</td><td>119.90 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.80 (n/a)</td><td>165.14 (n/a)</td><td>169.30 (n/a)</td><td>124.90 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.00 (+4.65%)</td><td>0.00 (+3.83%)</td><td>0.00 (+4.76%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>983.35 (-3.54%)</td><td>942.25 (-3.94%)</td><td>933.12 (-4.40%)</td><td>901.27 (-6.12%)</td><td>34.38 <b>(+47.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1019.42 (n/a)</td><td>980.92 (n/a)</td><td>976.11 (n/a)</td><td>960.03 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.01 (-1.18%)</td><td>0.01 (-1.25%)</td><td>0.01 (-1.25%)</td><td>0.01 (+0.00%)</td><td>0.00 (-10.13%)</td><td>1092.01 (-0.08%)</td><td>1036.47 (+1.26%)</td><td>1037.39 (+1.11%)</td><td>970.26 (+1.02%)</td><td>43.59 (-9.04%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1092.88 (n/a)</td><td>1023.59 (n/a)</td><td>1025.99 (n/a)</td><td>960.47 (n/a)</td><td>47.93 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.98 (+0.35%)</td><td>0.96 (+0.92%)</td><td>0.96 (+1.58%)</td><td>0.94 (+0.08%)</td><td>0.01 (-2.83%)</td><td>2219.24 (-0.08%)</td><td>2176.91 (-0.91%)</td><td>2173.66 (-1.55%)</td><td>2143.18 (-0.35%)</td><td>27.21 (-2.83%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2221.10 (n/a)</td><td>2196.89 (n/a)</td><td>2207.94 (n/a)</td><td>2150.73 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.40 (-1.67%)</td><td>0.39 (-0.34%)</td><td>0.39 (-0.03%)</td><td>0.38 (-0.73%)</td><td>0.01 <b>(-25.33%)</b></td><td>1375.17 (+0.74%)</td><td>1345.35 (+0.33%)</td><td>1345.14 (+0.03%)</td><td>1325.32 (+1.69%)</td><td>20.21 <b>(-23.68%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1365.09 (n/a)</td><td>1340.95 (n/a)</td><td>1344.76 (n/a)</td><td>1303.28 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.26 (-1.88%)</td><td>0.25 (-0.63%)</td><td>0.25 (+0.04%)</td><td>0.24 (-0.41%)</td><td>0.01 (-7.65%)</td><td>2180.90 (+0.40%)</td><td>2112.50 (+0.63%)</td><td>2090.43 (-0.04%)</td><td>2052.10 (+1.91%)</td><td>59.81 (-5.58%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2172.23 (n/a)</td><td>2099.35 (n/a)</td><td>2091.35 (n/a)</td><td>2013.67 (n/a)</td><td>63.35 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>0.38 (+2.87%)</td><td>0.37 (+1.61%)</td><td>0.36 (+1.31%)</td><td>0.36 (+1.69%)</td><td>0.01 <b>(+35.14%)</b></td><td>1452.66 (-1.66%)</td><td>1428.87 (-1.56%)</td><td>1440.23 (-1.31%)</td><td>1366.55 (-2.78%)</td><td>35.24 <b>(+29.00%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.01 (n/a)</td><td>1477.20 (n/a)</td><td>1451.54 (n/a)</td><td>1459.38 (n/a)</td><td>1405.68 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>3.61 (+6.86%)</td><td>2.88 (-10.74%)</td><td>2.78 (-13.96%)</td><td>2.47 (-19.91%)</td><td>0.43 <b>(+316.73%)</b></td><td>212.10 <b>(+24.84%)</b></td><td>184.76 (+13.71%)</td><td>188.40 (+16.22%)</td><td>145.40 (-6.37%)</td><td>24.27 <b>(+368.54%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.37 (n/a)</td><td>3.23 (n/a)</td><td>3.23 (n/a)</td><td>3.09 (n/a)</td><td>0.10 (n/a)</td><td>169.90 (n/a)</td><td>162.48 (n/a)</td><td>162.10 (n/a)</td><td>155.30 (n/a)</td><td>5.18 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.93 (-19.80%)</td><td>4.62 (-17.05%)</td><td>4.67 (-16.32%)</td><td>4.31 (-12.44%)</td><td>0.25 <b>(-43.51%)</b></td><td>243.00 (+14.19%)</td><td>227.56 <b>(+20.21%)</b></td><td>224.40 (+19.55%)</td><td>212.80 <b>(+24.66%)</b></td><td>12.56 (-19.71%)</td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>6.14 (n/a)</td><td>5.57 (n/a)</td><td>5.59 (n/a)</td><td>4.93 (n/a)</td><td>0.45 (n/a)</td><td>212.80 (n/a)</td><td>189.30 (n/a)</td><td>187.70 (n/a)</td><td>170.70 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>a15c8cd</code> — 2026-08-29 04:15:06</td><td>4.70 <b>(+37.16%)</b></td><td>3.31 (+5.06%)</td><td>2.74 (-14.99%)</td><td>2.27 <b>(-21.26%)</b></td><td>1.04 <b>(+318.96%)</b></td><td>231.10 <b>(+26.98%)</b></td><td>170.66 (+2.08%)</td><td>191.10 (+17.67%)</td><td>111.60 <b>(-27.11%)</b></td><td>49.76 <b>(+272.58%)</b></td>
</tr>
<tr>
<td><code>3ad2eb2</code> — 2026-08-29 00:09:23</td><td>3.42 (n/a)</td><td>3.15 (n/a)</td><td>3.23 (n/a)</td><td>2.88 (n/a)</td><td>0.25 (n/a)</td><td>182.00 (n/a)</td><td>167.18 (n/a)</td><td>162.40 (n/a)</td><td>153.10 (n/a)</td><td>13.35 (n/a)</td>
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
