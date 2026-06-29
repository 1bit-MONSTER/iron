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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (+7.06%)</td><td>0.07 (-16.15%)</td><td>0.07 (-5.77%)</td><td>0.03 <b>(-53.41%)</b></td><td>0.03 <b>(+172.93%)</b></td><td>378.50 <b>(+114.69%)</b></td><td>216.20 <b>(+38.22%)</b></td><td>173.40 (+6.12%)</td><td>120.80 (-6.65%)</td><td>103.24 <b>(+467.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>156.42 (n/a)</td><td>163.40 (n/a)</td><td>129.40 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.11 <b>(+40.53%)</b></td><td>0.08 (+13.24%)</td><td>0.07 (+1.36%)</td><td>0.06 (+15.16%)</td><td>0.02 <b>(+109.51%)</b></td><td>201.40 (-13.15%)</td><td>166.84 (-9.42%)</td><td>175.50 (-1.35%)</td><td>110.00 <b>(-28.85%)</b></td><td>34.07 (+19.01%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>184.20 (n/a)</td><td>177.90 (n/a)</td><td>154.60 (n/a)</td><td>28.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (+10.20%)</td><td>0.07 (+6.25%)</td><td>0.07 <b>(+22.59%)</b></td><td>0.04 <b>(-34.80%)</b></td><td>0.03 <b>(+60.78%)</b></td><td>330.00 <b>(+53.42%)</b></td><td>190.80 (+2.75%)</td><td>167.70 (-18.43%)</td><td>119.10 (-9.29%)</td><td>83.99 <b>(+123.19%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>185.70 (n/a)</td><td>205.60 (n/a)</td><td>131.30 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (-7.84%)</td><td>0.06 (+3.99%)</td><td>0.06 (+10.35%)</td><td>0.04 (-10.08%)</td><td>0.01 (-8.95%)</td><td>322.80 (+11.20%)</td><td>218.80 (-3.82%)</td><td>210.10 (-9.36%)</td><td>173.40 (+8.51%)</td><td>60.99 (+10.51%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>290.30 (n/a)</td><td>227.48 (n/a)</td><td>231.80 (n/a)</td><td>159.80 (n/a)</td><td>55.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (-4.25%)</td><td>0.03 (-3.64%)</td><td>0.03 (+3.53%)</td><td>0.03 (-1.97%)</td><td>0.00 <b>(-21.27%)</b></td><td>192.20 (+2.02%)</td><td>166.78 (+3.09%)</td><td>161.30 (-3.41%)</td><td>139.90 (+4.48%)</td><td>22.46 (-13.42%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>161.78 (n/a)</td><td>167.00 (n/a)</td><td>133.90 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 <b>(+44.31%)</b></td><td>0.04 <b>(+51.71%)</b></td><td>0.04 <b>(+44.41%)</b></td><td>0.03 <b>(+66.20%)</b></td><td>0.01 <b>(+25.92%)</b></td><td>151.70 <b>(-39.83%)</b></td><td>135.46 <b>(-34.50%)</b></td><td>144.20 <b>(-30.77%)</b></td><td>114.50 <b>(-30.69%)</b></td><td>16.49 <b>(-47.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.10 (n/a)</td><td>206.80 (n/a)</td><td>208.30 (n/a)</td><td>165.20 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (-12.56%)</td><td>0.03 (-4.14%)</td><td>0.03 (+1.94%)</td><td>0.03 (-7.50%)</td><td>0.00 <b>(-23.02%)</b></td><td>208.90 (+8.07%)</td><td>173.38 (+3.92%)</td><td>166.20 (-1.89%)</td><td>154.70 (+14.34%)</td><td>21.55 (-3.08%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>166.84 (n/a)</td><td>169.40 (n/a)</td><td>135.30 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 <b>(+23.52%)</b></td><td>0.04 <b>(+40.11%)</b></td><td>0.04 <b>(+45.00%)</b></td><td>0.03 <b>(+51.02%)</b></td><td>0.00 <b>(-20.20%)</b></td><td>166.50 <b>(-33.77%)</b></td><td>142.44 <b>(-30.22%)</b></td><td>141.20 <b>(-31.05%)</b></td><td>125.90 (-19.04%)</td><td>17.33 <b>(-58.12%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.40 (n/a)</td><td>204.12 (n/a)</td><td>204.80 (n/a)</td><td>155.50 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 <b>(+26.85%)</b></td><td>0.04 <b>(+28.38%)</b></td><td>0.04 <b>(+33.73%)</b></td><td>0.03 <b>(+30.20%)</b></td><td>0.01 (+6.52%)</td><td>190.00 <b>(-23.20%)</b></td><td>150.76 <b>(-22.91%)</b></td><td>149.00 <b>(-25.20%)</b></td><td>117.90 <b>(-21.14%)</b></td><td>26.30 <b>(-34.46%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.40 (n/a)</td><td>195.56 (n/a)</td><td>199.20 (n/a)</td><td>149.50 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 <b>(+23.85%)</b></td><td>0.03 (+10.32%)</td><td>0.03 (-1.55%)</td><td>0.03 (+18.17%)</td><td>0.01 <b>(+31.65%)</b></td><td>200.80 (-15.38%)</td><td>167.68 (-8.83%)</td><td>177.90 (+1.60%)</td><td>118.30 (-19.25%)</td><td>33.63 (-10.11%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>183.92 (n/a)</td><td>175.10 (n/a)</td><td>146.50 (n/a)</td><td>37.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (-6.18%)</td><td>0.03 (-3.18%)</td><td>0.03 (-7.42%)</td><td>0.02 (+17.50%)</td><td>0.01 <b>(-25.18%)</b></td><td>220.70 (-14.89%)</td><td>187.00 (+0.85%)</td><td>188.80 (+8.01%)</td><td>150.20 (+6.60%)</td><td>34.01 <b>(-30.43%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.30 (n/a)</td><td>185.42 (n/a)</td><td>174.80 (n/a)</td><td>140.90 (n/a)</td><td>48.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (-15.62%)</td><td>0.03 (+0.28%)</td><td>0.03 (+6.71%)</td><td>0.02 <b>(+37.80%)</b></td><td>0.00 <b>(-56.09%)</b></td><td>222.80 <b>(-27.40%)</b></td><td>197.06 (-5.70%)</td><td>191.20 (-6.27%)</td><td>164.50 (+18.52%)</td><td>23.76 <b>(-62.14%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>306.90 (n/a)</td><td>208.98 (n/a)</td><td>204.00 (n/a)</td><td>138.80 (n/a)</td><td>62.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>147.16 (n/a)</td><td>139.80 (n/a)</td><td>116.60 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>187.82 (n/a)</td><td>184.80 (n/a)</td><td>150.40 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>188.68 (n/a)</td><td>193.70 (n/a)</td><td>137.80 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>188.88 (n/a)</td><td>207.20 (n/a)</td><td>151.40 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>160.56 (n/a)</td><td>170.40 (n/a)</td><td>131.50 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>169.82 (n/a)</td><td>168.70 (n/a)</td><td>118.70 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>225.30 (n/a)</td><td>166.32 (n/a)</td><td>155.30 (n/a)</td><td>117.80 (n/a)</td><td>43.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>289.10 (n/a)</td><td>202.40 (n/a)</td><td>187.00 (n/a)</td><td>159.40 (n/a)</td><td>50.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>159.70 (n/a)</td><td>145.30 (n/a)</td><td>150.80 (n/a)</td><td>114.10 (n/a)</td><td>18.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>155.80 (n/a)</td><td>145.78 (n/a)</td><td>153.80 (n/a)</td><td>121.90 (n/a)</td><td>14.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>165.82 (n/a)</td><td>163.60 (n/a)</td><td>127.50 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>163.88 (n/a)</td><td>166.50 (n/a)</td><td>140.20 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>148.20 (n/a)</td><td>135.46 (n/a)</td><td>140.70 (n/a)</td><td>113.60 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.30 (n/a)</td><td>171.02 (n/a)</td><td>179.10 (n/a)</td><td>147.60 (n/a)</td><td>16.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>159.12 (n/a)</td><td>156.40 (n/a)</td><td>138.00 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>210.98 (n/a)</td><td>222.00 (n/a)</td><td>172.00 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.35 (-11.78%)</td><td>4.03 (-8.71%)</td><td>4.03 (-4.11%)</td><td>3.65 (-8.96%)</td><td>0.25 <b>(-40.07%)</b></td><td>2577.60 (+9.84%)</td><td>2342.44 (+9.12%)</td><td>2336.40 (+4.29%)</td><td>2159.60 (+13.36%)</td><td>151.02 <b>(-24.33%)</b></td><td>1712.99 (-11.78%)</td><td>1584.41 (-8.71%)</td><td>1583.36 (-4.11%)</td><td>1435.20 (-8.96%)</td><td>99.61 <b>(-40.07%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>4.94 (n/a)</td><td>4.41 (n/a)</td><td>4.20 (n/a)</td><td>4.01 (n/a)</td><td>0.42 (n/a)</td><td>2346.60 (n/a)</td><td>2146.64 (n/a)</td><td>2240.30 (n/a)</td><td>1905.10 (n/a)</td><td>199.58 (n/a)</td><td>1941.82 (n/a)</td><td>1735.67 (n/a)</td><td>1651.26 (n/a)</td><td>1576.47 (n/a)</td><td>166.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>1.02 <b>(-24.51%)</b></td><td>0.96 (-16.28%)</td><td>0.96 <b>(-25.81%)</b></td><td>0.91 <b>(+34.58%)</b></td><td>0.04 <b>(-84.95%)</b></td><td>242.60 <b>(-25.67%)</b></td><td>231.22 (+11.62%)</td><td>229.40 <b>(+34.78%)</b></td><td>216.90 <b>(+32.42%)</b></td><td>10.41 <b>(-85.02%)</b></td><td>43.50 <b>(-24.51%)</b></td><td>40.88 (-16.28%)</td><td>41.13 <b>(-25.81%)</b></td><td>38.91 <b>(+34.58%)</b></td><td>1.86 <b>(-84.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.35 (n/a)</td><td>1.14 (n/a)</td><td>1.30 (n/a)</td><td>0.68 (n/a)</td><td>0.29 (n/a)</td><td>326.40 (n/a)</td><td>207.14 (n/a)</td><td>170.20 (n/a)</td><td>163.80 (n/a)</td><td>69.49 (n/a)</td><td>57.63 (n/a)</td><td>48.83 (n/a)</td><td>55.44 (n/a)</td><td>28.91 (n/a)</td><td>12.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>1.15 (-12.62%)</td><td>0.90 (-16.32%)</td><td>0.85 <b>(-29.39%)</b></td><td>0.64 (-1.39%)</td><td>0.20 <b>(-31.38%)</b></td><td>343.80 (+1.42%)</td><td>256.80 (+15.73%)</td><td>260.60 <b>(+41.63%)</b></td><td>192.90 (+14.48%)</td><td>59.25 (-19.15%)</td><td>48.93 (-12.62%)</td><td>38.30 (-16.32%)</td><td>36.22 <b>(-29.39%)</b></td><td>27.45 (-1.39%)</td><td>8.53 <b>(-31.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.31 (n/a)</td><td>1.07 (n/a)</td><td>1.20 (n/a)</td><td>0.65 (n/a)</td><td>0.29 (n/a)</td><td>339.00 (n/a)</td><td>221.90 (n/a)</td><td>184.00 (n/a)</td><td>168.50 (n/a)</td><td>73.29 (n/a)</td><td>56.00 (n/a)</td><td>45.76 (n/a)</td><td>51.29 (n/a)</td><td>27.83 (n/a)</td><td>12.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (-0.85%)</td><td>0.52 (-0.23%)</td><td>0.52 (-0.10%)</td><td>0.52 (-0.06%)</td><td>0.00 <b>(-84.33%)</b></td><td>48698.80 (+0.06%)</td><td>48651.26 (+0.23%)</td><td>48644.30 (+0.10%)</td><td>48625.70 (+0.86%)</td><td>29.38 <b>(-84.18%)</b></td><td>353.31 (-0.85%)</td><td>353.12 (-0.23%)</td><td>353.17 (-0.10%)</td><td>352.78 (-0.06%)</td><td>0.21 <b>(-84.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48668.40 (n/a)</td><td>48539.04 (n/a)</td><td>48595.00 (n/a)</td><td>48211.30 (n/a)</td><td>185.70 (n/a)</td><td>356.35 (n/a)</td><td>353.94 (n/a)</td><td>353.53 (n/a)</td><td>353.00 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.89 (+0.60%)</td><td>0.88 (+0.29%)</td><td>0.88 (+0.39%)</td><td>0.87 (+0.28%)</td><td>0.01 (+17.19%)</td><td>28783.60 (-0.28%)</td><td>28574.08 (-0.29%)</td><td>28568.40 (-0.38%)</td><td>28342.90 (-0.59%)</td><td>165.78 (+16.22%)</td><td>606.14 (+0.60%)</td><td>601.26 (+0.29%)</td><td>601.36 (+0.39%)</td><td>596.86 (+0.28%)</td><td>3.49 (+17.19%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.00 (n/a)</td><td>28863.80 (n/a)</td><td>28656.32 (n/a)</td><td>28678.50 (n/a)</td><td>28511.80 (n/a)</td><td>142.64 (n/a)</td><td>602.55 (n/a)</td><td>599.53 (n/a)</td><td>599.05 (n/a)</td><td>595.20 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>3.45 (+0.37%)</td><td>3.27 (-0.12%)</td><td>3.25 (-1.93%)</td><td>3.19 (+1.67%)</td><td>0.10 (-18.29%)</td><td>7880.60 (-1.65%)</td><td>7693.12 (+0.08%)</td><td>7749.80 (+1.97%)</td><td>7302.80 (-0.37%)</td><td>225.78 <b>(-20.86%)</b></td><td>2352.51 (+0.37%)</td><td>2234.74 (-0.12%)</td><td>2216.80 (-1.93%)</td><td>2180.03 (+1.67%)</td><td>67.84 (-18.29%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.43 (n/a)</td><td>3.28 (n/a)</td><td>3.31 (n/a)</td><td>3.14 (n/a)</td><td>0.12 (n/a)</td><td>8012.50 (n/a)</td><td>7687.26 (n/a)</td><td>7600.00 (n/a)</td><td>7330.00 (n/a)</td><td>285.31 (n/a)</td><td>2343.79 (n/a)</td><td>2237.32 (n/a)</td><td>2260.51 (n/a)</td><td>2144.14 (n/a)</td><td>83.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.25 (+10.32%)</td><td>3.43 (+1.13%)</td><td>3.29 (-0.92%)</td><td>2.75 (-5.72%)</td><td>0.62 <b>(+67.36%)</b></td><td>2928.00 (+6.07%)</td><td>2412.46 (+0.49%)</td><td>2451.90 (+0.93%)</td><td>1897.40 (-9.35%)</td><td>426.57 <b>(+61.12%)</b></td><td>1114.14 (+10.32%)</td><td>899.19 (+1.13%)</td><td>862.16 (-0.92%)</td><td>721.97 (-5.72%)</td><td>163.11 <b>(+67.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.85 (n/a)</td><td>3.39 (n/a)</td><td>3.32 (n/a)</td><td>2.92 (n/a)</td><td>0.37 (n/a)</td><td>2760.40 (n/a)</td><td>2400.60 (n/a)</td><td>2429.40 (n/a)</td><td>2093.20 (n/a)</td><td>264.75 (n/a)</td><td>1009.89 (n/a)</td><td>889.15 (n/a)</td><td>870.16 (n/a)</td><td>765.79 (n/a)</td><td>97.46 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (+12.14%)</td><td>0.34 (-9.45%)</td><td>0.31 (-9.74%)</td><td>0.26 <b>(-20.59%)</b></td><td>0.11 <b>(+69.51%)</b></td><td>4846.70 <b>(+25.93%)</b></td><td>3875.42 (+15.07%)</td><td>4024.20 (+10.79%)</td><td>2398.40 (-10.83%)</td><td>957.27 <b>(+84.97%)</b></td><td>27.98 (+12.14%)</td><td>18.42 (-9.45%)</td><td>16.68 (-9.74%)</td><td>13.85 <b>(-20.59%)</b></td><td>5.67 <b>(+69.51%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>3848.80 (n/a)</td><td>3367.78 (n/a)</td><td>3632.40 (n/a)</td><td>2689.60 (n/a)</td><td>517.52 (n/a)</td><td>24.95 (n/a)</td><td>20.34 (n/a)</td><td>18.48 (n/a)</td><td>17.44 (n/a)</td><td>3.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.96 <b>(-22.71%)</b></td><td>4.49 (-10.62%)</td><td>4.66 (-1.19%)</td><td>3.52 (-11.28%)</td><td>0.56 <b>(-38.96%)</b></td><td>1892.00 (+12.71%)</td><td>1503.56 (+10.69%)</td><td>1426.90 (+1.21%)</td><td>1340.90 <b>(+29.38%)</b></td><td>220.47 (-6.99%)</td><td>1532.72 <b>(-22.71%)</b></td><td>1387.16 (-10.62%)</td><td>1440.38 (-1.19%)</td><td>1086.24 (-11.28%)</td><td>173.12 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>6.42 (n/a)</td><td>5.02 (n/a)</td><td>4.72 (n/a)</td><td>3.96 (n/a)</td><td>0.92 (n/a)</td><td>1678.60 (n/a)</td><td>1358.40 (n/a)</td><td>1409.90 (n/a)</td><td>1036.40 (n/a)</td><td>237.03 (n/a)</td><td>1982.97 (n/a)</td><td>1552.03 (n/a)</td><td>1457.75 (n/a)</td><td>1224.38 (n/a)</td><td>283.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.20 <b>(-23.48%)</b></td><td>0.18 <b>(-23.54%)</b></td><td>0.19 (-13.19%)</td><td>0.12 <b>(-36.66%)</b></td><td>0.03 (+9.95%)</td><td>0.20 <b>(-23.48%)</b></td><td>0.17 <b>(-23.54%)</b></td><td>0.19 (-13.19%)</td><td>0.12 <b>(-36.66%)</b></td><td>0.03 (+9.95%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>13.26 (+0.37%)</td><td>12.51 (-0.01%)</td><td>12.54 (-3.62%)</td><td>11.91 (+9.34%)</td><td>0.53 <b>(-44.60%)</b></td><td>13.25 (+0.37%)</td><td>12.50 (-0.01%)</td><td>12.53 (-3.62%)</td><td>11.90 (+9.34%)</td><td>0.53 <b>(-44.60%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>13.21 (n/a)</td><td>12.51 (n/a)</td><td>13.01 (n/a)</td><td>10.89 (n/a)</td><td>0.96 (n/a)</td><td>13.21 (n/a)</td><td>12.51 (n/a)</td><td>13.00 (n/a)</td><td>10.89 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>24.01 (-4.73%)</td><td>23.56 (-3.79%)</td><td>23.86 (-3.29%)</td><td>22.30 (-5.18%)</td><td>0.71 (+8.40%)</td><td>24.00 (-4.73%)</td><td>23.55 (-3.79%)</td><td>23.85 (-3.29%)</td><td>22.29 (-5.18%)</td><td>0.71 (+8.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>25.21 (n/a)</td><td>24.49 (n/a)</td><td>24.67 (n/a)</td><td>23.52 (n/a)</td><td>0.65 (n/a)</td><td>25.19 (n/a)</td><td>24.47 (n/a)</td><td>24.66 (n/a)</td><td>23.50 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>39.63 (-7.49%)</td><td>37.41 (-6.75%)</td><td>39.38 (-1.66%)</td><td>30.65 (-16.21%)</td><td>3.85 <b>(+59.77%)</b></td><td>39.61 (-7.49%)</td><td>37.39 (-6.75%)</td><td>39.35 (-1.66%)</td><td>30.63 (-16.21%)</td><td>3.84 <b>(+59.77%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>42.84 (n/a)</td><td>40.12 (n/a)</td><td>40.04 (n/a)</td><td>36.58 (n/a)</td><td>2.41 (n/a)</td><td>42.82 (n/a)</td><td>40.10 (n/a)</td><td>40.02 (n/a)</td><td>36.56 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>44.67 (-1.78%)</td><td>42.57 (-0.98%)</td><td>43.32 (+2.95%)</td><td>39.02 (-2.62%)</td><td>2.21 (-5.63%)</td><td>44.64 (-1.78%)</td><td>42.55 (-0.98%)</td><td>43.29 (+2.95%)</td><td>39.00 (-2.62%)</td><td>2.21 (-5.63%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>45.48 (n/a)</td><td>42.99 (n/a)</td><td>42.07 (n/a)</td><td>40.07 (n/a)</td><td>2.34 (n/a)</td><td>45.45 (n/a)</td><td>42.97 (n/a)</td><td>42.05 (n/a)</td><td>40.05 (n/a)</td><td>2.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>13.21 (-1.88%)</td><td>12.46 (-0.76%)</td><td>12.36 (-4.47%)</td><td>11.97 (+11.79%)</td><td>0.46 <b>(-58.46%)</b></td><td>13.20 (-1.88%)</td><td>12.45 (-0.76%)</td><td>12.35 (-4.47%)</td><td>11.96 (+11.79%)</td><td>0.46 <b>(-58.46%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>13.46 (n/a)</td><td>12.55 (n/a)</td><td>12.94 (n/a)</td><td>10.71 (n/a)</td><td>1.10 (n/a)</td><td>13.46 (n/a)</td><td>12.54 (n/a)</td><td>12.93 (n/a)</td><td>10.70 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>24.33 (-2.22%)</td><td>23.69 (-2.51%)</td><td>23.86 (-3.15%)</td><td>22.48 (-2.93%)</td><td>0.71 (+2.25%)</td><td>24.32 (-2.22%)</td><td>23.67 (-2.51%)</td><td>23.84 (-3.15%)</td><td>22.46 (-2.93%)</td><td>0.71 (+2.25%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>24.88 (n/a)</td><td>24.30 (n/a)</td><td>24.64 (n/a)</td><td>23.16 (n/a)</td><td>0.69 (n/a)</td><td>24.87 (n/a)</td><td>24.28 (n/a)</td><td>24.62 (n/a)</td><td>23.14 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>40.80 (-4.13%)</td><td>35.21 (-12.84%)</td><td>37.70 (-4.65%)</td><td>24.68 <b>(-35.81%)</b></td><td>6.59 <b>(+266.21%)</b></td><td>40.77 (-4.13%)</td><td>35.18 (-12.84%)</td><td>37.67 (-4.65%)</td><td>24.67 <b>(-35.81%)</b></td><td>6.58 <b>(+266.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>42.56 (n/a)</td><td>40.39 (n/a)</td><td>39.53 (n/a)</td><td>38.45 (n/a)</td><td>1.80 (n/a)</td><td>42.53 (n/a)</td><td>40.37 (n/a)</td><td>39.51 (n/a)</td><td>38.43 (n/a)</td><td>1.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>45.51 (+0.50%)</td><td>42.04 (-4.91%)</td><td>42.21 (-5.78%)</td><td>38.89 (-8.99%)</td><td>2.55 <b>(+134.47%)</b></td><td>45.48 (+0.50%)</td><td>42.02 (-4.91%)</td><td>42.18 (-5.78%)</td><td>38.86 (-8.99%)</td><td>2.54 <b>(+134.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>45.29 (n/a)</td><td>44.22 (n/a)</td><td>44.80 (n/a)</td><td>42.73 (n/a)</td><td>1.09 (n/a)</td><td>45.26 (n/a)</td><td>44.19 (n/a)</td><td>44.77 (n/a)</td><td>42.70 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>193.56 (n/a)</td><td>220.70 (n/a)</td><td>132.50 (n/a)</td><td>45.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>361.00 (n/a)</td><td>248.62 (n/a)</td><td>195.40 (n/a)</td><td>154.70 (n/a)</td><td>103.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>168.42 (n/a)</td><td>173.40 (n/a)</td><td>144.90 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>267.60 (n/a)</td><td>172.78 (n/a)</td><td>162.60 (n/a)</td><td>107.80 (n/a)</td><td>58.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>153.90 (n/a)</td><td>151.80 (n/a)</td><td>129.30 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>271.20 (n/a)</td><td>181.54 (n/a)</td><td>183.50 (n/a)</td><td>112.50 (n/a)</td><td>57.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.50 (n/a)</td><td>188.24 (n/a)</td><td>169.80 (n/a)</td><td>134.90 (n/a)</td><td>74.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>261.30 (n/a)</td><td>219.66 (n/a)</td><td>212.90 (n/a)</td><td>195.00 (n/a)</td><td>24.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (+6.51%)</td><td>0.05 (-0.18%)</td><td>0.05 (-9.52%)</td><td>0.04 (-2.32%)</td><td>0.01 <b>(+29.68%)</b></td><td>194.90 (+2.36%)</td><td>162.32 (+1.37%)</td><td>170.60 (+10.56%)</td><td>121.20 (-6.12%)</td><td>30.98 <b>(+23.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>160.12 (n/a)</td><td>154.30 (n/a)</td><td>129.10 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (-4.45%)</td><td>0.04 (-6.81%)</td><td>0.03 (-15.10%)</td><td>0.02 (+11.06%)</td><td>0.01 (-0.22%)</td><td>340.70 (-9.94%)</td><td>245.58 (+6.35%)</td><td>247.50 (+17.80%)</td><td>158.60 (+4.62%)</td><td>75.27 (-12.61%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>378.30 (n/a)</td><td>230.92 (n/a)</td><td>210.10 (n/a)</td><td>151.60 (n/a)</td><td>86.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 <b>(-22.60%)</b></td><td>0.05 (-14.08%)</td><td>0.05 (-11.13%)</td><td>0.04 (-13.01%)</td><td>0.01 <b>(-43.30%)</b></td><td>217.30 (+14.91%)</td><td>175.48 (+14.66%)</td><td>172.60 (+12.52%)</td><td>154.40 <b>(+29.21%)</b></td><td>24.89 (-14.26%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>153.04 (n/a)</td><td>153.40 (n/a)</td><td>119.50 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (-16.77%)</td><td>0.06 (-3.37%)</td><td>0.06 (+7.65%)</td><td>0.05 (+9.36%)</td><td>0.01 <b>(-51.03%)</b></td><td>175.90 (-8.58%)</td><td>149.50 (+0.44%)</td><td>146.40 (-7.11%)</td><td>129.00 <b>(+20.11%)</b></td><td>18.08 <b>(-45.17%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>148.84 (n/a)</td><td>157.60 (n/a)</td><td>107.40 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (+10.32%)</td><td>0.05 (+18.76%)</td><td>0.05 (+18.24%)</td><td>0.04 <b>(+53.54%)</b></td><td>0.01 <b>(-37.26%)</b></td><td>182.70 <b>(-34.87%)</b></td><td>158.30 (-18.50%)</td><td>153.90 (-15.39%)</td><td>141.50 (-9.35%)</td><td>17.68 <b>(-64.53%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.50 (n/a)</td><td>194.24 (n/a)</td><td>181.90 (n/a)</td><td>156.10 (n/a)</td><td>49.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (-14.57%)</td><td>0.05 (+4.93%)</td><td>0.05 (+11.81%)</td><td>0.05 <b>(+23.48%)</b></td><td>0.00 <b>(-61.30%)</b></td><td>177.10 (-19.02%)</td><td>157.68 (-7.88%)</td><td>160.20 (-10.55%)</td><td>143.50 (+17.05%)</td><td>13.60 <b>(-63.11%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>171.16 (n/a)</td><td>179.10 (n/a)</td><td>122.60 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (+0.22%)</td><td>0.05 (+1.57%)</td><td>0.05 (+4.03%)</td><td>0.05 (+4.27%)</td><td>0.00 (-17.08%)</td><td>174.40 (-4.07%)</td><td>164.34 (-1.72%)</td><td>164.40 (-3.92%)</td><td>148.70 (-0.20%)</td><td>10.68 (-19.89%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.80 (n/a)</td><td>167.22 (n/a)</td><td>171.10 (n/a)</td><td>149.00 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (-3.03%)</td><td>0.05 (-5.71%)</td><td>0.05 (+2.01%)</td><td>0.03 (-16.08%)</td><td>0.01 (+18.74%)</td><td>241.20 (+19.11%)</td><td>177.40 (+7.49%)</td><td>163.60 (-1.98%)</td><td>145.20 (+3.12%)</td><td>37.58 <b>(+52.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>165.04 (n/a)</td><td>166.90 (n/a)</td><td>140.80 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (-14.51%)</td><td>0.05 (-4.50%)</td><td>0.05 (-5.62%)</td><td>0.04 (+17.20%)</td><td>0.00 <b>(-60.89%)</b></td><td>197.90 (-14.70%)</td><td>177.86 (+2.12%)</td><td>174.40 (+5.95%)</td><td>162.00 (+16.97%)</td><td>13.53 <b>(-61.83%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>174.16 (n/a)</td><td>164.60 (n/a)</td><td>138.50 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 <b>(+28.98%)</b></td><td>0.09 (+19.98%)</td><td>0.09 (+16.78%)</td><td>0.07 (+15.37%)</td><td>0.01 <b>(+60.53%)</b></td><td>169.70 (-13.29%)</td><td>142.12 (-16.22%)</td><td>141.00 (-14.39%)</td><td>121.80 <b>(-22.47%)</b></td><td>17.56 (+9.57%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>169.64 (n/a)</td><td>164.70 (n/a)</td><td>157.10 (n/a)</td><td>16.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (+16.85%)</td><td>0.06 (+8.84%)</td><td>0.05 (+3.72%)</td><td>0.05 (+6.47%)</td><td>0.01 <b>(+75.76%)</b></td><td>167.00 (-6.07%)</td><td>147.64 (-7.42%)</td><td>156.60 (-3.63%)</td><td>123.80 (-14.38%)</td><td>18.28 <b>(+40.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.80 (n/a)</td><td>159.48 (n/a)</td><td>162.50 (n/a)</td><td>144.60 (n/a)</td><td>12.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (-8.52%)</td><td>0.06 (+11.53%)</td><td>0.06 (+10.40%)</td><td>0.05 <b>(+96.07%)</b></td><td>0.01 <b>(-68.88%)</b></td><td>193.50 <b>(-49.00%)</b></td><td>173.96 (-19.98%)</td><td>178.10 (-9.41%)</td><td>152.10 (+9.27%)</td><td>15.98 <b>(-83.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>379.40 (n/a)</td><td>217.40 (n/a)</td><td>196.60 (n/a)</td><td>139.20 (n/a)</td><td>95.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 <b>(+26.30%)</b></td><td>0.05 (+12.42%)</td><td>0.04 (-1.29%)</td><td>0.04 <b>(+24.54%)</b></td><td>0.01 <b>(+43.86%)</b></td><td>209.00 (-19.71%)</td><td>175.44 (-10.33%)</td><td>182.20 (+1.28%)</td><td>127.70 <b>(-20.83%)</b></td><td>35.11 (-9.45%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.30 (n/a)</td><td>195.64 (n/a)</td><td>179.90 (n/a)</td><td>161.30 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (-0.83%)</td><td>0.07 (+3.66%)</td><td>0.07 (+13.42%)</td><td>0.05 (+5.37%)</td><td>0.01 (-0.78%)</td><td>204.60 (-5.10%)</td><td>160.16 (-3.69%)</td><td>147.50 (-11.84%)</td><td>133.00 (+0.83%)</td><td>30.56 (-5.62%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>166.30 (n/a)</td><td>167.30 (n/a)</td><td>131.90 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 <b>(-24.26%)</b></td><td>0.05 (-8.17%)</td><td>0.05 (-3.85%)</td><td>0.04 (-4.41%)</td><td>0.01 <b>(-40.94%)</b></td><td>208.10 (+4.63%)</td><td>172.08 (+6.30%)</td><td>178.10 (+3.97%)</td><td>136.70 <b>(+31.95%)</b></td><td>30.14 (-14.55%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>161.88 (n/a)</td><td>171.30 (n/a)</td><td>103.60 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (+0.03%)</td><td>0.06 (+18.57%)</td><td>0.06 (+18.04%)</td><td>0.06 <b>(+48.95%)</b></td><td>0.01 <b>(-40.58%)</b></td><td>163.60 <b>(-32.87%)</b></td><td>145.24 (-19.63%)</td><td>144.00 (-15.29%)</td><td>114.60 (+0.00%)</td><td>19.54 <b>(-59.77%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>243.70 (n/a)</td><td>180.72 (n/a)</td><td>170.00 (n/a)</td><td>114.60 (n/a)</td><td>48.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (-16.74%)</td><td>0.05 (-1.20%)</td><td>0.04 (-4.25%)</td><td>0.03 <b>(+49.19%)</b></td><td>0.01 <b>(-45.19%)</b></td><td>246.50 <b>(-32.98%)</b></td><td>185.50 (-9.28%)</td><td>182.40 (+4.41%)</td><td>135.40 <b>(+20.14%)</b></td><td>40.68 <b>(-58.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>367.80 (n/a)</td><td>204.48 (n/a)</td><td>174.70 (n/a)</td><td>112.70 (n/a)</td><td>96.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (-1.81%)</td><td>0.05 (-13.34%)</td><td>0.05 (-7.38%)</td><td>0.03 <b>(-39.77%)</b></td><td>0.01 <b>(+209.60%)</b></td><td>288.90 <b>(+66.03%)</b></td><td>196.30 <b>(+20.53%)</b></td><td>178.30 (+8.00%)</td><td>153.60 (+1.86%)</td><td>53.08 <b>(+455.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.00 (n/a)</td><td>162.86 (n/a)</td><td>165.10 (n/a)</td><td>150.80 (n/a)</td><td>9.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 <b>(-21.61%)</b></td><td>0.05 (-1.08%)</td><td>0.05 (+5.87%)</td><td>0.04 <b>(+28.51%)</b></td><td>0.01 <b>(-53.02%)</b></td><td>226.40 <b>(-22.17%)</b></td><td>184.56 (-4.50%)</td><td>170.20 (-5.55%)</td><td>161.60 <b>(+27.55%)</b></td><td>27.81 <b>(-54.62%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.90 (n/a)</td><td>193.26 (n/a)</td><td>180.20 (n/a)</td><td>126.70 (n/a)</td><td>61.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (-9.58%)</td><td>0.04 (+0.75%)</td><td>0.04 (+10.40%)</td><td>0.04 (+2.25%)</td><td>0.01 <b>(-40.90%)</b></td><td>224.50 (-2.22%)</td><td>195.96 (-2.47%)</td><td>197.10 (-9.42%)</td><td>166.00 (+10.59%)</td><td>22.01 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>200.92 (n/a)</td><td>217.60 (n/a)</td><td>150.10 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (-17.52%)</td><td>0.04 (-13.56%)</td><td>0.05 (-14.10%)</td><td>0.04 (+19.45%)</td><td>0.01 <b>(-52.58%)</b></td><td>208.30 (-16.31%)</td><td>186.90 (+11.28%)</td><td>181.20 (+16.38%)</td><td>156.30 <b>(+21.26%)</b></td><td>21.89 <b>(-53.39%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>167.96 (n/a)</td><td>155.70 (n/a)</td><td>128.90 (n/a)</td><td>46.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 <b>(+41.72%)</b></td><td>0.05 (+14.71%)</td><td>0.04 (+2.53%)</td><td>0.04 (+4.99%)</td><td>0.01 <b>(+216.24%)</b></td><td>222.70 (-4.79%)</td><td>191.98 (-10.66%)</td><td>205.20 (-2.43%)</td><td>136.90 <b>(-29.47%)</b></td><td>33.23 <b>(+103.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.90 (n/a)</td><td>214.88 (n/a)</td><td>210.30 (n/a)</td><td>194.10 (n/a)</td><td>16.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (-10.57%)</td><td>0.03 <b>(-23.29%)</b></td><td>0.03 <b>(-24.34%)</b></td><td>0.02 <b>(-23.16%)</b></td><td>0.01 <b>(+20.81%)</b></td><td>397.50 <b>(+30.16%)</b></td><td>300.50 <b>(+35.94%)</b></td><td>286.50 <b>(+32.21%)</b></td><td>188.20 (+11.82%)</td><td>91.11 <b>(+77.89%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>305.40 (n/a)</td><td>221.06 (n/a)</td><td>216.70 (n/a)</td><td>168.30 (n/a)</td><td>51.22 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.79 (+5.48%)</td><td>0.57 (-0.75%)</td><td>0.58 <b>(+21.56%)</b></td><td>0.44 (-5.04%)</td><td>0.14 (-9.06%)</td><td>225.00 (+5.29%)</td><td>179.08 (-0.17%)</td><td>169.80 (-17.73%)</td><td>124.70 (-5.24%)</td><td>39.63 (-8.08%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.75 (n/a)</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.15 (n/a)</td><td>213.70 (n/a)</td><td>179.38 (n/a)</td><td>206.40 (n/a)</td><td>131.60 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.82 (+17.70%)</td><td>0.67 <b>(+39.76%)</b></td><td>0.66 <b>(+59.29%)</b></td><td>0.58 <b>(+62.56%)</b></td><td>0.09 <b>(-39.40%)</b></td><td>169.20 <b>(-38.50%)</b></td><td>147.96 <b>(-32.39%)</b></td><td>148.60 <b>(-37.19%)</b></td><td>119.60 (-15.06%)</td><td>18.27 <b>(-69.66%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.70 (n/a)</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.15 (n/a)</td><td>275.10 (n/a)</td><td>218.84 (n/a)</td><td>236.60 (n/a)</td><td>140.80 (n/a)</td><td>60.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.59 (+0.78%)</td><td>0.50 (-4.59%)</td><td>0.50 (-9.74%)</td><td>0.39 (-8.63%)</td><td>0.07 (+11.33%)</td><td>250.00 (+9.46%)</td><td>199.14 (+5.33%)</td><td>197.30 (+10.78%)</td><td>167.40 (-0.77%)</td><td>31.56 <b>(+23.84%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.58 (n/a)</td><td>0.53 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>228.40 (n/a)</td><td>189.06 (n/a)</td><td>178.10 (n/a)</td><td>168.70 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.61 (-0.11%)</td><td>0.51 (+1.59%)</td><td>0.50 (-1.66%)</td><td>0.43 (+8.76%)</td><td>0.06 <b>(-35.20%)</b></td><td>226.30 (-8.05%)</td><td>193.34 (-3.44%)</td><td>195.20 (+1.67%)</td><td>162.00 (+0.12%)</td><td>23.68 <b>(-40.39%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.61 (n/a)</td><td>0.51 (n/a)</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.10 (n/a)</td><td>246.10 (n/a)</td><td>200.22 (n/a)</td><td>192.00 (n/a)</td><td>161.80 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.67 <b>(+41.65%)</b></td><td>0.45 (+2.92%)</td><td>0.46 (+5.49%)</td><td>0.30 <b>(-28.67%)</b></td><td>0.14 <b>(+525.39%)</b></td><td>249.40 <b>(+40.19%)</b></td><td>175.06 (+4.44%)</td><td>159.80 (-5.22%)</td><td>109.90 <b>(-29.42%)</b></td><td>52.38 <b>(+518.59%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>167.62 (n/a)</td><td>168.60 (n/a)</td><td>155.70 (n/a)</td><td>8.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (+6.39%)</td><td>0.39 (-8.05%)</td><td>0.37 (-12.57%)</td><td>0.28 (-18.21%)</td><td>0.10 <b>(+65.30%)</b></td><td>266.60 <b>(+22.24%)</b></td><td>197.30 (+12.87%)</td><td>200.30 (+14.39%)</td><td>141.50 (-6.04%)</td><td>51.56 <b>(+87.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>218.10 (n/a)</td><td>174.80 (n/a)</td><td>175.10 (n/a)</td><td>150.60 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.49 (+2.64%)</td><td>0.42 (+1.77%)</td><td>0.42 (+4.05%)</td><td>0.33 (-1.99%)</td><td>0.06 (+18.78%)</td><td>220.80 (+2.03%)</td><td>179.20 (-1.22%)</td><td>174.90 (-3.90%)</td><td>150.60 (-2.59%)</td><td>27.96 (+17.93%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>216.40 (n/a)</td><td>181.42 (n/a)</td><td>182.00 (n/a)</td><td>154.60 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.61 (+15.74%)</td><td>0.44 (+10.88%)</td><td>0.43 (+16.37%)</td><td>0.32 <b>(+26.39%)</b></td><td>0.11 (-7.19%)</td><td>227.80 <b>(-20.88%)</b></td><td>176.58 (-12.45%)</td><td>172.50 (-14.09%)</td><td>120.20 (-13.59%)</td><td>39.69 <b>(-35.79%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>287.90 (n/a)</td><td>201.70 (n/a)</td><td>200.80 (n/a)</td><td>139.10 (n/a)</td><td>61.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.89 (-4.73%)</td><td>0.71 (+0.66%)</td><td>0.67 (-5.97%)</td><td>0.62 (+10.98%)</td><td>0.11 <b>(-25.33%)</b></td><td>211.60 (-9.92%)</td><td>186.42 (-2.00%)</td><td>194.50 (+6.40%)</td><td>147.90 (+4.97%)</td><td>24.75 <b>(-29.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.93 (n/a)</td><td>0.71 (n/a)</td><td>0.72 (n/a)</td><td>0.56 (n/a)</td><td>0.14 (n/a)</td><td>234.90 (n/a)</td><td>190.22 (n/a)</td><td>182.80 (n/a)</td><td>140.90 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.95 <b>(+21.48%)</b></td><td>0.71 (+2.35%)</td><td>0.66 (-1.15%)</td><td>0.57 (-5.22%)</td><td>0.14 <b>(+96.28%)</b></td><td>229.00 (+5.53%)</td><td>190.86 (-0.36%)</td><td>197.70 (+1.13%)</td><td>137.80 (-17.68%)</td><td>33.43 <b>(+65.32%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.67 (n/a)</td><td>0.60 (n/a)</td><td>0.07 (n/a)</td><td>217.00 (n/a)</td><td>191.54 (n/a)</td><td>195.50 (n/a)</td><td>167.40 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.79 <b>(-23.14%)</b></td><td>0.69 (-11.35%)</td><td>0.70 (-2.54%)</td><td>0.54 (-2.81%)</td><td>0.09 <b>(-51.33%)</b></td><td>243.20 (+2.92%)</td><td>193.12 (+9.27%)</td><td>186.30 (+2.59%)</td><td>165.30 <b>(+30.06%)</b></td><td>29.49 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>1.03 (n/a)</td><td>0.78 (n/a)</td><td>0.72 (n/a)</td><td>0.55 (n/a)</td><td>0.19 (n/a)</td><td>236.30 (n/a)</td><td>176.74 (n/a)</td><td>181.60 (n/a)</td><td>127.10 (n/a)</td><td>43.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.00 (-8.33%)</td><td>0.00 (-3.85%)</td><td>0.00 (-9.09%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-25.46%)</b></td><td>4616.74 (+3.15%)</td><td>4157.53 (+4.09%)</td><td>4169.13 (+9.09%)</td><td>3765.84 (+7.06%)</td><td>364.88 (-11.07%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4475.59 (n/a)</td><td>3994.10 (n/a)</td><td>3821.83 (n/a)</td><td>3517.56 (n/a)</td><td>410.30 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.00 (+0.00%)</td><td>0.00 (-2.06%)</td><td>0.00 (+0.00%)</td><td>0.00 (-11.76%)</td><td>0.00 (+17.71%)</td><td>5550.60 (+16.31%)</td><td>4432.38 (+4.62%)</td><td>4539.79 (+0.65%)</td><td>3567.47 (+0.95%)</td><td>785.64 <b>(+32.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4772.10 (n/a)</td><td>4236.73 (n/a)</td><td>4510.67 (n/a)</td><td>3533.78 (n/a)</td><td>592.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.28 (+0.87%)</td><td>0.25 <b>(+36.72%)</b></td><td>0.27 <b>(+81.02%)</b></td><td>0.17 <b>(+23.57%)</b></td><td>0.05 (-18.61%)</td><td>12461.92 (-19.06%)</td><td>8720.16 <b>(-28.92%)</b></td><td>7661.84 <b>(-44.77%)</b></td><td>7552.69 (-0.86%)</td><td>2112.03 <b>(-32.91%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>15396.52 (n/a)</td><td>12268.40 (n/a)</td><td>13872.79 (n/a)</td><td>7618.14 (n/a)</td><td>3148.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>2.93 (-5.46%)</td><td>2.42 (-11.08%)</td><td>2.45 (-10.54%)</td><td>1.85 (-15.12%)</td><td>0.41 (+5.26%)</td><td>283.20 (+17.80%)</td><td>221.78 (+13.26%)</td><td>213.70 (+11.83%)</td><td>178.90 (+5.80%)</td><td>39.73 <b>(+34.48%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.10 (n/a)</td><td>2.72 (n/a)</td><td>2.74 (n/a)</td><td>2.18 (n/a)</td><td>0.39 (n/a)</td><td>240.40 (n/a)</td><td>195.82 (n/a)</td><td>191.10 (n/a)</td><td>169.10 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>5.87 (+6.51%)</td><td>4.52 (-11.62%)</td><td>4.65 (-12.55%)</td><td>3.43 <b>(-20.05%)</b></td><td>1.02 <b>(+113.42%)</b></td><td>305.60 <b>(+25.09%)</b></td><td>241.74 (+17.01%)</td><td>225.60 (+14.34%)</td><td>178.70 (-6.10%)</td><td>54.79 <b>(+153.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>5.51 (n/a)</td><td>5.12 (n/a)</td><td>5.32 (n/a)</td><td>4.29 (n/a)</td><td>0.48 (n/a)</td><td>244.30 (n/a)</td><td>206.60 (n/a)</td><td>197.30 (n/a)</td><td>190.30 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>3.17 (-7.78%)</td><td>2.72 (-5.07%)</td><td>2.74 (-3.85%)</td><td>2.16 (-5.45%)</td><td>0.46 (-2.92%)</td><td>242.30 (+5.76%)</td><td>197.36 (+5.48%)</td><td>191.00 (+3.97%)</td><td>165.60 (+8.45%)</td><td>34.11 (+9.23%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>3.43 (n/a)</td><td>2.86 (n/a)</td><td>2.85 (n/a)</td><td>2.29 (n/a)</td><td>0.47 (n/a)</td><td>229.10 (n/a)</td><td>187.10 (n/a)</td><td>183.70 (n/a)</td><td>152.70 (n/a)</td><td>31.23 (n/a)</td>
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
