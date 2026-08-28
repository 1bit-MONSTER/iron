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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.10 (+1.01%)</td><td>0.08 (+16.59%)</td><td>0.09 <b>(+28.26%)</b></td><td>0.06 (+13.62%)</td><td>0.01 (-12.48%)</td><td>198.90 (-11.95%)</td><td>153.74 (-14.99%)</td><td>142.00 <b>(-22.02%)</b></td><td>128.50 (-1.00%)</td><td>27.58 (-19.40%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>180.84 (n/a)</td><td>182.10 (n/a)</td><td>129.80 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.09 <b>(+22.20%)</b></td><td>0.07 (+7.46%)</td><td>0.07 (+3.82%)</td><td>0.06 (+9.56%)</td><td>0.01 <b>(+44.09%)</b></td><td>208.50 (-8.71%)</td><td>173.42 (-6.25%)</td><td>170.50 (-3.67%)</td><td>134.30 (-18.16%)</td><td>27.89 (+6.35%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>184.98 (n/a)</td><td>177.00 (n/a)</td><td>164.10 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.10 (+12.16%)</td><td>0.07 (-3.01%)</td><td>0.07 (+0.01%)</td><td>0.05 (-6.23%)</td><td>0.02 <b>(+44.18%)</b></td><td>252.00 (+6.64%)</td><td>185.70 (+6.56%)</td><td>174.20 (+0.00%)</td><td>123.80 (-10.87%)</td><td>53.14 <b>(+38.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>174.26 (n/a)</td><td>174.20 (n/a)</td><td>138.90 (n/a)</td><td>38.27 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 <b>(-23.02%)</b></td><td>0.07 (-0.34%)</td><td>0.07 (+10.05%)</td><td>0.06 (+15.98%)</td><td>0.00 <b>(-75.88%)</b></td><td>195.60 (-13.76%)</td><td>181.44 (-3.13%)</td><td>182.40 (-9.12%)</td><td>168.10 <b>(+29.91%)</b></td><td>10.39 <b>(-72.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>187.30 (n/a)</td><td>200.70 (n/a)</td><td>129.40 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 <b>(+29.41%)</b></td><td>0.04 (+12.73%)</td><td>0.04 (+8.62%)</td><td>0.03 (+10.25%)</td><td>0.01 <b>(+83.82%)</b></td><td>170.00 (-9.28%)</td><td>148.88 (-10.37%)</td><td>145.70 (-7.96%)</td><td>116.90 <b>(-22.74%)</b></td><td>21.33 <b>(+29.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>166.10 (n/a)</td><td>158.30 (n/a)</td><td>151.30 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 <b>(-31.50%)</b></td><td>0.03 (-3.54%)</td><td>0.03 <b>(+20.02%)</b></td><td>0.02 <b>(-27.62%)</b></td><td>0.01 <b>(-32.69%)</b></td><td>315.30 <b>(+38.17%)</b></td><td>189.48 (+3.70%)</td><td>156.50 (-16.67%)</td><td>151.40 <b>(+46.00%)</b></td><td>70.61 <b>(+47.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>182.72 (n/a)</td><td>187.80 (n/a)</td><td>103.70 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 (-5.95%)</td><td>0.03 (-7.50%)</td><td>0.03 (-13.57%)</td><td>0.02 (+0.36%)</td><td>0.00 (-16.37%)</td><td>219.00 (-0.36%)</td><td>187.92 (+7.55%)</td><td>193.50 (+15.66%)</td><td>156.80 (+6.31%)</td><td>23.08 (-14.58%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.80 (n/a)</td><td>174.72 (n/a)</td><td>167.30 (n/a)</td><td>147.50 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (-19.45%)</td><td>0.03 (+6.72%)</td><td>0.03 <b>(+20.55%)</b></td><td>0.03 (+11.73%)</td><td>0.00 <b>(-60.29%)</b></td><td>192.60 (-10.50%)</td><td>163.48 (-10.78%)</td><td>161.90 (-17.06%)</td><td>138.20 <b>(+24.17%)</b></td><td>19.32 <b>(-54.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>183.24 (n/a)</td><td>195.20 (n/a)</td><td>111.30 (n/a)</td><td>42.86 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 <b>(-22.20%)</b></td><td>0.03 (-17.62%)</td><td>0.03 (-13.97%)</td><td>0.02 (-12.66%)</td><td>0.00 <b>(-30.61%)</b></td><td>235.40 (+14.49%)</td><td>188.24 <b>(+20.30%)</b></td><td>173.10 (+16.25%)</td><td>156.50 <b>(+28.49%)</b></td><td>32.58 (+1.58%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>156.48 (n/a)</td><td>148.90 (n/a)</td><td>121.80 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 <b>(+52.56%)</b></td><td>0.03 <b>(+26.98%)</b></td><td>0.03 <b>(+30.08%)</b></td><td>0.02 (+10.32%)</td><td>0.01 <b>(+96.23%)</b></td><td>229.10 (-9.38%)</td><td>169.38 (-17.88%)</td><td>163.60 <b>(-23.12%)</b></td><td>105.70 <b>(-34.47%)</b></td><td>49.62 <b>(+20.11%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>206.26 (n/a)</td><td>212.80 (n/a)</td><td>161.30 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (-10.61%)</td><td>0.03 (+3.25%)</td><td>0.03 (+3.88%)</td><td>0.03 (+15.13%)</td><td>0.00 <b>(-41.30%)</b></td><td>206.40 (-13.17%)</td><td>175.70 (-5.50%)</td><td>180.20 (-3.74%)</td><td>144.90 (+11.81%)</td><td>22.47 <b>(-41.33%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>185.92 (n/a)</td><td>187.20 (n/a)</td><td>129.60 (n/a)</td><td>38.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.03 <b>(-29.07%)</b></td><td>0.03 (-6.75%)</td><td>0.03 (+8.48%)</td><td>0.02 (+6.10%)</td><td>0.00 <b>(-69.01%)</b></td><td>241.50 (-5.74%)</td><td>208.84 (+2.61%)</td><td>201.90 (-7.81%)</td><td>187.50 <b>(+40.98%)</b></td><td>20.27 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.20 (n/a)</td><td>203.52 (n/a)</td><td>219.00 (n/a)</td><td>133.00 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>192.10 (n/a)</td><td>148.14 (n/a)</td><td>149.70 (n/a)</td><td>112.60 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>160.90 (n/a)</td><td>158.90 (n/a)</td><td>141.70 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>283.00 (n/a)</td><td>202.48 (n/a)</td><td>201.80 (n/a)</td><td>150.80 (n/a)</td><td>50.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>193.48 (n/a)</td><td>203.60 (n/a)</td><td>147.70 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>158.72 (n/a)</td><td>165.10 (n/a)</td><td>119.90 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>199.92 (n/a)</td><td>207.10 (n/a)</td><td>174.00 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>189.84 (n/a)</td><td>208.00 (n/a)</td><td>143.20 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>334.00 (n/a)</td><td>243.98 (n/a)</td><td>221.30 (n/a)</td><td>135.00 (n/a)</td><td>86.90 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.90 (n/a)</td><td>150.34 (n/a)</td><td>128.80 (n/a)</td><td>117.80 (n/a)</td><td>43.09 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.20 (n/a)</td><td>147.64 (n/a)</td><td>151.60 (n/a)</td><td>119.80 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.90 (n/a)</td><td>171.04 (n/a)</td><td>172.20 (n/a)</td><td>145.40 (n/a)</td><td>16.38 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>368.10 (n/a)</td><td>198.92 (n/a)</td><td>171.30 (n/a)</td><td>128.80 (n/a)</td><td>98.50 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.80 (n/a)</td><td>174.36 (n/a)</td><td>181.80 (n/a)</td><td>153.60 (n/a)</td><td>13.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>185.12 (n/a)</td><td>179.90 (n/a)</td><td>122.80 (n/a)</td><td>50.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>176.02 (n/a)</td><td>173.80 (n/a)</td><td>130.40 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.50 (n/a)</td><td>200.40 (n/a)</td><td>218.60 (n/a)</td><td>127.90 (n/a)</td><td>50.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>4.34 (+0.83%)</td><td>4.07 (-3.22%)</td><td>4.15 (-1.11%)</td><td>3.76 (-7.98%)</td><td>0.23 <b>(+171.68%)</b></td><td>2501.50 (+8.67%)</td><td>2315.36 (+3.56%)</td><td>2264.40 (+1.13%)</td><td>2169.00 (-0.82%)</td><td>133.62 <b>(+194.02%)</b></td><td>1705.54 (+0.83%)</td><td>1601.94 (-3.22%)</td><td>1633.69 (-1.11%)</td><td>1478.87 (-7.98%)</td><td>90.78 <b>(+171.69%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>4.30 (n/a)</td><td>4.21 (n/a)</td><td>4.20 (n/a)</td><td>4.09 (n/a)</td><td>0.08 (n/a)</td><td>2301.90 (n/a)</td><td>2235.66 (n/a)</td><td>2239.20 (n/a)</td><td>2187.00 (n/a)</td><td>45.45 (n/a)</td><td>1691.51 (n/a)</td><td>1655.25 (n/a)</td><td>1652.07 (n/a)</td><td>1607.11 (n/a)</td><td>33.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.23 (+3.67%)</td><td>1.05 (+11.26%)</td><td>0.99 (+4.95%)</td><td>0.98 <b>(+34.73%)</b></td><td>0.10 <b>(-37.84%)</b></td><td>225.60 <b>(-25.77%)</b></td><td>212.96 (-11.72%)</td><td>223.10 (-4.70%)</td><td>180.30 (-3.53%)</td><td>18.98 <b>(-55.86%)</b></td><td>52.36 (+3.67%)</td><td>44.64 (+11.26%)</td><td>42.30 (+4.95%)</td><td>41.84 <b>(+34.73%)</b></td><td>4.43 <b>(-37.84%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.18 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.73 (n/a)</td><td>0.17 (n/a)</td><td>303.90 (n/a)</td><td>241.24 (n/a)</td><td>234.10 (n/a)</td><td>186.90 (n/a)</td><td>43.00 (n/a)</td><td>50.50 (n/a)</td><td>40.12 (n/a)</td><td>40.31 (n/a)</td><td>31.05 (n/a)</td><td>7.13 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.21 (-2.27%)</td><td>0.90 (-1.19%)</td><td>0.95 (+8.03%)</td><td>0.67 (-6.08%)</td><td>0.22 (+1.24%)</td><td>328.30 (+6.49%)</td><td>258.26 (+1.73%)</td><td>233.50 (-7.41%)</td><td>182.60 (+2.30%)</td><td>61.39 (+11.24%)</td><td>51.67 (-2.27%)</td><td>38.29 (-1.19%)</td><td>40.42 (+8.03%)</td><td>28.74 (-6.08%)</td><td>9.34 (+1.24%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.24 (n/a)</td><td>0.91 (n/a)</td><td>0.88 (n/a)</td><td>0.72 (n/a)</td><td>0.22 (n/a)</td><td>308.30 (n/a)</td><td>253.88 (n/a)</td><td>252.20 (n/a)</td><td>178.50 (n/a)</td><td>55.19 (n/a)</td><td>52.87 (n/a)</td><td>38.75 (n/a)</td><td>37.42 (n/a)</td><td>30.61 (n/a)</td><td>9.22 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.52 (+0.02%)</td><td>0.52 (+0.02%)</td><td>0.52 (+0.02%)</td><td>0.52 (-0.03%)</td><td>0.00 (+15.18%)</td><td>48649.40 (+0.03%)</td><td>48494.88 (-0.02%)</td><td>48471.10 (-0.02%)</td><td>48433.10 (-0.02%)</td><td>88.95 (+15.19%)</td><td>354.71 (+0.02%)</td><td>354.26 (+0.02%)</td><td>354.44 (+0.02%)</td><td>353.14 (-0.03%)</td><td>0.65 (+15.19%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48633.90 (n/a)</td><td>48502.38 (n/a)</td><td>48483.00 (n/a)</td><td>48444.60 (n/a)</td><td>77.22 (n/a)</td><td>354.63 (n/a)</td><td>354.21 (n/a)</td><td>354.35 (n/a)</td><td>353.25 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.90 (-0.26%)</td><td>0.89 (-0.13%)</td><td>0.89 (-0.08%)</td><td>0.88 (+0.16%)</td><td>0.01 (-17.21%)</td><td>28474.90 (-0.16%)</td><td>28216.96 (+0.13%)</td><td>28232.20 (+0.08%)</td><td>27880.60 (+0.26%)</td><td>213.66 (-17.19%)</td><td>616.19 (-0.26%)</td><td>608.88 (-0.13%)</td><td>608.52 (-0.08%)</td><td>603.33 (+0.16%)</td><td>4.63 (-17.21%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28520.40 (n/a)</td><td>28180.20 (n/a)</td><td>28209.50 (n/a)</td><td>27807.90 (n/a)</td><td>258.02 (n/a)</td><td>617.81 (n/a)</td><td>609.68 (n/a)</td><td>609.01 (n/a)</td><td>602.37 (n/a)</td><td>5.59 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.35 (+1.58%)</td><td>3.28 (+1.19%)</td><td>3.30 (+0.76%)</td><td>3.17 (+0.85%)</td><td>0.07 (+2.76%)</td><td>7948.80 (-0.84%)</td><td>7686.76 (-1.17%)</td><td>7635.30 (-0.75%)</td><td>7516.60 (-1.55%)</td><td>160.62 (+0.72%)</td><td>2285.58 (+1.58%)</td><td>2235.77 (+1.19%)</td><td>2250.06 (+0.76%)</td><td>2161.32 (+0.85%)</td><td>45.99 (+2.76%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.30 (n/a)</td><td>3.24 (n/a)</td><td>3.27 (n/a)</td><td>3.14 (n/a)</td><td>0.07 (n/a)</td><td>8016.50 (n/a)</td><td>7778.14 (n/a)</td><td>7693.20 (n/a)</td><td>7635.10 (n/a)</td><td>159.46 (n/a)</td><td>2250.11 (n/a)</td><td>2209.47 (n/a)</td><td>2233.13 (n/a)</td><td>2143.07 (n/a)</td><td>44.76 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.96 (+7.35%)</td><td>3.61 (+1.02%)</td><td>3.57 (+0.37%)</td><td>3.26 (-3.90%)</td><td>0.25 <b>(+103.08%)</b></td><td>2475.40 (+4.06%)</td><td>2244.72 (-0.71%)</td><td>2258.50 (-0.37%)</td><td>2033.20 (-6.85%)</td><td>158.60 <b>(+97.76%)</b></td><td>1039.73 (+7.35%)</td><td>945.49 (+1.02%)</td><td>935.98 (+0.37%)</td><td>853.97 (-3.90%)</td><td>66.56 <b>(+103.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.69 (n/a)</td><td>3.57 (n/a)</td><td>3.56 (n/a)</td><td>3.39 (n/a)</td><td>0.12 (n/a)</td><td>2378.90 (n/a)</td><td>2260.80 (n/a)</td><td>2266.90 (n/a)</td><td>2182.60 (n/a)</td><td>80.20 (n/a)</td><td>968.53 (n/a)</td><td>935.97 (n/a)</td><td>932.54 (n/a)</td><td>888.60 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.60 (+9.21%)</td><td>0.39 (-2.80%)</td><td>0.36 (+3.61%)</td><td>0.28 (-14.23%)</td><td>0.13 <b>(+32.01%)</b></td><td>4448.60 (+16.59%)</td><td>3459.76 (+5.88%)</td><td>3434.40 (-3.49%)</td><td>2069.80 (-8.43%)</td><td>902.89 <b>(+33.32%)</b></td><td>32.42 (+9.21%)</td><td>20.79 (-2.80%)</td><td>19.54 (+3.61%)</td><td>15.09 (-14.23%)</td><td>6.84 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.55 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>3815.50 (n/a)</td><td>3267.72 (n/a)</td><td>3558.50 (n/a)</td><td>2260.40 (n/a)</td><td>677.23 (n/a)</td><td>29.69 (n/a)</td><td>21.39 (n/a)</td><td>18.86 (n/a)</td><td>17.59 (n/a)</td><td>5.18 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>4.84 (-4.29%)</td><td>4.11 (-9.51%)</td><td>3.72 <b>(-20.61%)</b></td><td>3.62 (+0.98%)</td><td>0.60 (+7.50%)</td><td>1836.00 (-0.98%)</td><td>1646.92 (+10.77%)</td><td>1788.30 <b>(+25.95%)</b></td><td>1374.90 (+4.48%)</td><td>229.18 (+8.29%)</td><td>1494.82 (-4.29%)</td><td>1268.62 (-9.51%)</td><td>1149.28 <b>(-20.61%)</b></td><td>1119.38 (+0.98%)</td><td>186.13 (+7.50%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>5.06 (n/a)</td><td>4.54 (n/a)</td><td>4.69 (n/a)</td><td>3.59 (n/a)</td><td>0.56 (n/a)</td><td>1854.10 (n/a)</td><td>1486.84 (n/a)</td><td>1419.80 (n/a)</td><td>1315.90 (n/a)</td><td>211.63 (n/a)</td><td>1561.88 (n/a)</td><td>1401.93 (n/a)</td><td>1447.57 (n/a)</td><td>1108.48 (n/a)</td><td>173.14 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>13.31 (n/a)</td><td>12.06 (n/a)</td><td>12.11 (n/a)</td><td>11.10 (n/a)</td><td>0.97 (n/a)</td><td>13.30 (n/a)</td><td>12.06 (n/a)</td><td>12.10 (n/a)</td><td>11.09 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>24.64 (+1.48%)</td><td>24.00 (+0.34%)</td><td>23.96 (+0.47%)</td><td>23.69 (-0.15%)</td><td>0.38 <b>(+78.88%)</b></td><td>24.62 (+1.48%)</td><td>23.99 (+0.34%)</td><td>23.94 (+0.47%)</td><td>23.68 (-0.15%)</td><td>0.38 <b>(+78.88%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>24.28 (n/a)</td><td>23.92 (n/a)</td><td>23.84 (n/a)</td><td>23.73 (n/a)</td><td>0.21 (n/a)</td><td>24.26 (n/a)</td><td>23.91 (n/a)</td><td>23.83 (n/a)</td><td>23.72 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>40.59 (-2.33%)</td><td>39.56 (-0.19%)</td><td>39.28 (-2.46%)</td><td>38.81 (+10.13%)</td><td>0.82 <b>(-68.20%)</b></td><td>40.56 (-2.33%)</td><td>39.54 (-0.19%)</td><td>39.26 (-2.46%)</td><td>38.78 (+10.13%)</td><td>0.81 <b>(-68.20%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>41.56 (n/a)</td><td>39.64 (n/a)</td><td>40.27 (n/a)</td><td>35.23 (n/a)</td><td>2.56 (n/a)</td><td>41.53 (n/a)</td><td>39.62 (n/a)</td><td>40.25 (n/a)</td><td>35.21 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>44.01 (+1.63%)</td><td>42.99 (+3.12%)</td><td>42.68 (+1.86%)</td><td>42.41 (+8.98%)</td><td>0.70 <b>(-57.86%)</b></td><td>43.99 (+1.63%)</td><td>42.96 (+3.12%)</td><td>42.65 (+1.86%)</td><td>42.39 (+8.98%)</td><td>0.70 <b>(-57.86%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>43.31 (n/a)</td><td>41.69 (n/a)</td><td>41.90 (n/a)</td><td>38.92 (n/a)</td><td>1.67 (n/a)</td><td>43.28 (n/a)</td><td>41.66 (n/a)</td><td>41.87 (n/a)</td><td>38.89 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>13.33 (n/a)</td><td>12.25 (n/a)</td><td>12.69 (n/a)</td><td>10.77 (n/a)</td><td>1.16 (n/a)</td><td>13.32 (n/a)</td><td>12.24 (n/a)</td><td>12.68 (n/a)</td><td>10.76 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>24.25 (-0.96%)</td><td>24.09 (+0.09%)</td><td>24.18 (-0.57%)</td><td>23.88 (+2.62%)</td><td>0.18 <b>(-65.85%)</b></td><td>24.23 (-0.96%)</td><td>24.08 (+0.09%)</td><td>24.17 (-0.57%)</td><td>23.87 (+2.62%)</td><td>0.18 <b>(-65.85%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>24.48 (n/a)</td><td>24.07 (n/a)</td><td>24.32 (n/a)</td><td>23.27 (n/a)</td><td>0.52 (n/a)</td><td>24.47 (n/a)</td><td>24.06 (n/a)</td><td>24.31 (n/a)</td><td>23.26 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>41.02 (+1.89%)</td><td>39.80 (+2.52%)</td><td>39.64 (+1.17%)</td><td>38.60 (+5.35%)</td><td>0.88 <b>(-42.22%)</b></td><td>40.99 (+1.89%)</td><td>39.78 (+2.52%)</td><td>39.62 (+1.17%)</td><td>38.58 (+5.35%)</td><td>0.88 <b>(-42.22%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>40.26 (n/a)</td><td>38.83 (n/a)</td><td>39.18 (n/a)</td><td>36.64 (n/a)</td><td>1.53 (n/a)</td><td>40.23 (n/a)</td><td>38.80 (n/a)</td><td>39.16 (n/a)</td><td>36.62 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>42.58 (-5.47%)</td><td>41.96 (-2.02%)</td><td>41.94 (-2.87%)</td><td>41.27 (+6.50%)</td><td>0.61 <b>(-74.78%)</b></td><td>42.55 (-5.47%)</td><td>41.94 (-2.02%)</td><td>41.92 (-2.87%)</td><td>41.24 (+6.50%)</td><td>0.61 <b>(-74.78%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>45.04 (n/a)</td><td>42.83 (n/a)</td><td>43.18 (n/a)</td><td>38.75 (n/a)</td><td>2.41 (n/a)</td><td>45.02 (n/a)</td><td>42.80 (n/a)</td><td>43.15 (n/a)</td><td>38.72 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>8.86 (-3.59%)</td><td>8.30 (-5.55%)</td><td>8.40 (-4.34%)</td><td>7.69 (-8.72%)</td><td>0.52 <b>(+59.24%)</b></td><td>8.85 (-3.59%)</td><td>8.28 (-5.55%)</td><td>8.39 (-4.34%)</td><td>7.67 (-8.72%)</td><td>0.52 <b>(+59.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>9.19 (n/a)</td><td>8.79 (n/a)</td><td>8.79 (n/a)</td><td>8.42 (n/a)</td><td>0.33 (n/a)</td><td>9.18 (n/a)</td><td>8.77 (n/a)</td><td>8.77 (n/a)</td><td>8.40 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.96 (+3.40%)</td><td>0.84 (-2.76%)</td><td>0.86 (-0.70%)</td><td>0.67 (-16.78%)</td><td>0.12 <b>(+136.62%)</b></td><td>0.95 (+3.40%)</td><td>0.83 (-2.76%)</td><td>0.85 (-0.70%)</td><td>0.66 (-16.78%)</td><td>0.11 <b>(+136.62%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.93 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.81 (n/a)</td><td>0.05 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.27 (-9.21%)</td><td>1.00 (-18.64%)</td><td>0.97 (-15.55%)</td><td>0.77 <b>(-28.51%)</b></td><td>0.18 <b>(+20.46%)</b></td><td>1.26 (-9.21%)</td><td>0.99 (-18.64%)</td><td>0.96 (-15.55%)</td><td>0.76 <b>(-28.51%)</b></td><td>0.18 <b>(+20.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.40 (n/a)</td><td>1.23 (n/a)</td><td>1.15 (n/a)</td><td>1.07 (n/a)</td><td>0.15 (n/a)</td><td>1.38 (n/a)</td><td>1.21 (n/a)</td><td>1.13 (n/a)</td><td>1.06 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>16.74 (-19.03%)</td><td>16.37 (-5.71%)</td><td>16.53 (-4.71%)</td><td>15.91 (+13.37%)</td><td>0.36 <b>(-84.72%)</b></td><td>16.55 (-19.03%)</td><td>16.18 (-5.71%)</td><td>16.34 (-4.71%)</td><td>15.73 (+13.37%)</td><td>0.35 <b>(-84.72%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>20.68 (n/a)</td><td>17.36 (n/a)</td><td>17.35 (n/a)</td><td>14.04 (n/a)</td><td>2.35 (n/a)</td><td>20.44 (n/a)</td><td>17.16 (n/a)</td><td>17.15 (n/a)</td><td>13.87 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>13.26 (-6.66%)</td><td>12.58 (-6.40%)</td><td>12.85 (-6.18%)</td><td>11.74 (-2.57%)</td><td>0.66 (-19.87%)</td><td>13.03 (-6.66%)</td><td>12.36 (-6.40%)</td><td>12.63 (-6.18%)</td><td>11.53 (-2.57%)</td><td>0.65 (-19.87%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>14.21 (n/a)</td><td>13.44 (n/a)</td><td>13.70 (n/a)</td><td>12.04 (n/a)</td><td>0.82 (n/a)</td><td>13.96 (n/a)</td><td>13.20 (n/a)</td><td>13.46 (n/a)</td><td>11.83 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>8.36 (-0.17%)</td><td>7.01 (-11.54%)</td><td>7.19 (-7.44%)</td><td>5.22 <b>(-32.22%)</b></td><td>1.16 <b>(+283.15%)</b></td><td>8.21 (-0.17%)</td><td>6.89 (-11.54%)</td><td>7.07 (-7.44%)</td><td>5.13 <b>(-32.22%)</b></td><td>1.14 <b>(+283.15%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>8.37 (n/a)</td><td>7.93 (n/a)</td><td>7.77 (n/a)</td><td>7.70 (n/a)</td><td>0.30 (n/a)</td><td>8.23 (n/a)</td><td>7.79 (n/a)</td><td>7.63 (n/a)</td><td>7.56 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>6.86 (+1.59%)</td><td>5.82 (+4.47%)</td><td>6.02 (+9.45%)</td><td>4.31 (-12.75%)</td><td>0.98 <b>(+33.20%)</b></td><td>6.75 (+1.59%)</td><td>5.73 (+4.47%)</td><td>5.93 (+9.45%)</td><td>4.24 (-12.75%)</td><td>0.96 <b>(+33.20%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>6.76 (n/a)</td><td>5.57 (n/a)</td><td>5.50 (n/a)</td><td>4.94 (n/a)</td><td>0.73 (n/a)</td><td>6.65 (n/a)</td><td>5.48 (n/a)</td><td>5.42 (n/a)</td><td>4.86 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>12.72 (n/a)</td><td>12.09 (n/a)</td><td>12.10 (n/a)</td><td>11.06 (n/a)</td><td>0.68 (n/a)</td><td>12.72 (n/a)</td><td>12.09 (n/a)</td><td>12.09 (n/a)</td><td>11.05 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>13.35 (n/a)</td><td>13.05 (n/a)</td><td>13.06 (n/a)</td><td>12.80 (n/a)</td><td>0.23 (n/a)</td><td>13.35 (n/a)</td><td>13.04 (n/a)</td><td>13.05 (n/a)</td><td>12.80 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.60 (n/a)</td><td>177.80 (n/a)</td><td>171.60 (n/a)</td><td>167.40 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>167.60 (n/a)</td><td>174.30 (n/a)</td><td>126.20 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>181.36 (n/a)</td><td>186.30 (n/a)</td><td>121.20 (n/a)</td><td>40.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>181.26 (n/a)</td><td>191.00 (n/a)</td><td>136.70 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.70 (n/a)</td><td>175.66 (n/a)</td><td>177.70 (n/a)</td><td>154.70 (n/a)</td><td>12.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.90 (n/a)</td><td>205.98 (n/a)</td><td>201.20 (n/a)</td><td>176.80 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>233.10 (n/a)</td><td>188.76 (n/a)</td><td>208.20 (n/a)</td><td>114.00 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>281.50 (n/a)</td><td>234.64 (n/a)</td><td>215.70 (n/a)</td><td>206.10 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 <b>(-25.98%)</b></td><td>0.05 (-13.93%)</td><td>0.04 (-12.96%)</td><td>0.04 (-10.80%)</td><td>0.01 <b>(-44.32%)</b></td><td>201.20 (+12.09%)</td><td>176.08 (+13.97%)</td><td>187.00 (+14.86%)</td><td>143.70 <b>(+35.06%)</b></td><td>25.42 (-15.08%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>154.50 (n/a)</td><td>162.80 (n/a)</td><td>106.40 (n/a)</td><td>29.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (-0.71%)</td><td>0.06 (+5.13%)</td><td>0.05 (-2.14%)</td><td>0.04 (+8.31%)</td><td>0.01 (+3.36%)</td><td>182.40 (-7.69%)</td><td>151.10 (-4.92%)</td><td>161.80 (+2.15%)</td><td>121.20 (+0.75%)</td><td>26.36 (-5.16%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>158.92 (n/a)</td><td>158.40 (n/a)</td><td>120.30 (n/a)</td><td>27.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (-7.45%)</td><td>0.05 (-5.16%)</td><td>0.05 (-10.64%)</td><td>0.04 (+3.04%)</td><td>0.01 <b>(-21.73%)</b></td><td>207.40 (-2.95%)</td><td>155.54 (+3.51%)</td><td>153.80 (+11.94%)</td><td>124.10 (+8.01%)</td><td>33.45 (-18.06%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>150.26 (n/a)</td><td>137.40 (n/a)</td><td>114.90 (n/a)</td><td>40.82 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (-10.94%)</td><td>0.05 (-4.54%)</td><td>0.05 (-12.86%)</td><td>0.04 <b>(+78.96%)</b></td><td>0.01 <b>(-61.37%)</b></td><td>192.00 <b>(-44.10%)</b></td><td>175.38 (-6.43%)</td><td>180.80 (+14.79%)</td><td>142.60 (+12.28%)</td><td>20.20 <b>(-77.28%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>343.50 (n/a)</td><td>187.44 (n/a)</td><td>157.50 (n/a)</td><td>127.00 (n/a)</td><td>88.89 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 <b>(-33.59%)</b></td><td>0.04 <b>(-25.15%)</b></td><td>0.04 (-18.65%)</td><td>0.04 (-15.63%)</td><td>0.00 <b>(-72.67%)</b></td><td>203.20 (+18.55%)</td><td>186.18 <b>(+30.14%)</b></td><td>189.90 <b>(+22.91%)</b></td><td>170.70 <b>(+50.53%)</b></td><td>13.46 <b>(-50.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>143.06 (n/a)</td><td>154.50 (n/a)</td><td>113.40 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (-19.77%)</td><td>0.05 <b>(-20.95%)</b></td><td>0.04 <b>(-23.21%)</b></td><td>0.04 <b>(-20.27%)</b></td><td>0.01 (-12.34%)</td><td>204.50 <b>(+25.46%)</b></td><td>182.04 <b>(+27.00%)</b></td><td>192.50 <b>(+30.24%)</b></td><td>139.50 <b>(+24.66%)</b></td><td>27.23 <b>(+41.14%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.00 (n/a)</td><td>143.34 (n/a)</td><td>147.80 (n/a)</td><td>111.90 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (+5.93%)</td><td>0.05 (-10.43%)</td><td>0.04 (-18.18%)</td><td>0.04 (-17.78%)</td><td>0.01 <b>(+82.18%)</b></td><td>216.80 <b>(+21.59%)</b></td><td>183.66 (+14.24%)</td><td>191.30 <b>(+22.24%)</b></td><td>130.20 (-5.58%)</td><td>33.60 <b>(+101.07%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.30 (n/a)</td><td>160.76 (n/a)</td><td>156.50 (n/a)</td><td>137.90 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 <b>(+28.99%)</b></td><td>0.05 (-4.95%)</td><td>0.04 <b>(-20.92%)</b></td><td>0.04 (+9.27%)</td><td>0.01 <b>(+76.02%)</b></td><td>206.40 (-8.47%)</td><td>182.20 (+8.14%)</td><td>197.60 <b>(+26.42%)</b></td><td>112.40 <b>(-22.43%)</b></td><td>39.23 (+18.87%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>168.48 (n/a)</td><td>156.30 (n/a)</td><td>144.90 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 <b>(-38.71%)</b></td><td>0.04 (-15.73%)</td><td>0.04 (-4.50%)</td><td>0.04 (+9.42%)</td><td>0.00 <b>(-79.61%)</b></td><td>223.50 (-8.59%)</td><td>202.36 (+11.88%)</td><td>199.00 (+4.68%)</td><td>185.70 <b>(+63.18%)</b></td><td>15.02 <b>(-68.42%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.50 (n/a)</td><td>180.88 (n/a)</td><td>190.10 (n/a)</td><td>113.80 (n/a)</td><td>47.56 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 <b>(+26.41%)</b></td><td>0.04 (-3.48%)</td><td>0.04 (-10.56%)</td><td>0.03 (-11.40%)</td><td>0.01 <b>(+162.74%)</b></td><td>243.10 (+12.86%)</td><td>206.66 (+8.00%)</td><td>212.40 (+11.85%)</td><td>131.80 <b>(-20.89%)</b></td><td>45.09 <b>(+128.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.40 (n/a)</td><td>191.36 (n/a)</td><td>189.90 (n/a)</td><td>166.60 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (-3.15%)</td><td>0.06 <b>(+32.34%)</b></td><td>0.06 <b>(+50.16%)</b></td><td>0.04 <b>(+42.62%)</b></td><td>0.01 <b>(-39.45%)</b></td><td>184.40 <b>(-29.89%)</b></td><td>138.92 <b>(-28.47%)</b></td><td>128.10 <b>(-33.39%)</b></td><td>121.90 (+3.22%)</td><td>25.72 <b>(-54.45%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>263.00 (n/a)</td><td>194.22 (n/a)</td><td>192.30 (n/a)</td><td>118.10 (n/a)</td><td>56.47 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (+0.62%)</td><td>0.04 (+0.55%)</td><td>0.04 (-0.17%)</td><td>0.03 (+18.95%)</td><td>0.01 <b>(-24.56%)</b></td><td>293.30 (-15.94%)</td><td>220.66 (-3.61%)</td><td>217.80 (+0.18%)</td><td>175.10 (-0.62%)</td><td>45.17 <b>(-36.13%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.90 (n/a)</td><td>228.92 (n/a)</td><td>217.40 (n/a)</td><td>176.20 (n/a)</td><td>70.72 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (-15.55%)</td><td>0.05 (-16.50%)</td><td>0.05 (-11.79%)</td><td>0.03 <b>(-26.21%)</b></td><td>0.01 (+15.03%)</td><td>240.70 <b>(+35.53%)</b></td><td>171.68 <b>(+22.33%)</b></td><td>152.90 (+13.34%)</td><td>136.20 (+18.43%)</td><td>41.96 <b>(+83.49%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>140.34 (n/a)</td><td>134.90 (n/a)</td><td>115.00 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 <b>(+20.80%)</b></td><td>0.05 (+2.95%)</td><td>0.05 (-0.62%)</td><td>0.04 (-18.09%)</td><td>0.01 <b>(+291.99%)</b></td><td>210.30 <b>(+22.13%)</b></td><td>163.52 (-0.34%)</td><td>162.90 (+0.62%)</td><td>127.10 (-17.25%)</td><td>30.83 <b>(+296.53%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>164.08 (n/a)</td><td>161.90 (n/a)</td><td>153.60 (n/a)</td><td>7.78 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (-8.09%)</td><td>0.05 (-0.68%)</td><td>0.05 (+0.10%)</td><td>0.05 (+9.69%)</td><td>0.01 <b>(-41.56%)</b></td><td>172.10 (-8.85%)</td><td>157.16 (-0.72%)</td><td>157.80 (-0.13%)</td><td>134.50 (+8.73%)</td><td>14.42 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>158.30 (n/a)</td><td>158.00 (n/a)</td><td>123.70 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (+5.28%)</td><td>0.05 (+6.09%)</td><td>0.05 (+13.98%)</td><td>0.03 (-2.40%)</td><td>0.01 (+11.94%)</td><td>241.60 (+2.46%)</td><td>177.84 (-4.86%)</td><td>169.80 (-12.25%)</td><td>124.40 (-4.97%)</td><td>43.95 (+11.52%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>186.92 (n/a)</td><td>193.50 (n/a)</td><td>130.90 (n/a)</td><td>39.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 <b>(+31.89%)</b></td><td>0.05 (+18.70%)</td><td>0.05 <b>(+27.50%)</b></td><td>0.03 (-10.80%)</td><td>0.02 <b>(+59.34%)</b></td><td>286.20 (+12.10%)</td><td>179.04 (-11.50%)</td><td>155.80 <b>(-21.59%)</b></td><td>114.60 <b>(-24.16%)</b></td><td>66.23 <b>(+38.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.30 (n/a)</td><td>202.30 (n/a)</td><td>198.70 (n/a)</td><td>151.10 (n/a)</td><td>47.67 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (-13.39%)</td><td>0.05 (-10.23%)</td><td>0.05 (-12.64%)</td><td>0.04 (+10.50%)</td><td>0.01 <b>(-39.77%)</b></td><td>213.70 (-9.53%)</td><td>182.14 (+8.75%)</td><td>181.00 (+14.48%)</td><td>154.70 (+15.45%)</td><td>24.38 <b>(-39.46%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>167.48 (n/a)</td><td>158.10 (n/a)</td><td>134.00 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.18 (-0.82%)</td><td>0.18 (-0.28%)</td><td>0.18 (-0.04%)</td><td>0.18 (-0.50%)</td><td>0.00 <b>(-36.04%)</b></td><td>47651.70 (+0.50%)</td><td>47427.42 (+0.28%)</td><td>47414.70 (+0.04%)</td><td>47289.00 (+0.82%)</td><td>143.35 <b>(-35.17%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47412.60 (n/a)</td><td>47296.94 (n/a)</td><td>47395.60 (n/a)</td><td>46902.30 (n/a)</td><td>221.11 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 <b>(+26.52%)</b></td><td>0.05 (+18.86%)</td><td>0.05 (+15.76%)</td><td>0.05 <b>(+20.95%)</b></td><td>0.01 <b>(+47.05%)</b></td><td>171.00 (-17.31%)</td><td>154.68 (-15.60%)</td><td>154.70 (-13.58%)</td><td>129.90 <b>(-20.99%)</b></td><td>17.01 (-2.99%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.80 (n/a)</td><td>183.28 (n/a)</td><td>179.00 (n/a)</td><td>164.40 (n/a)</td><td>17.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 (+6.74%)</td><td>0.07 (+8.17%)</td><td>0.07 (+9.32%)</td><td>0.06 (+10.79%)</td><td>0.01 (-2.71%)</td><td>210.50 (-9.73%)</td><td>178.06 (-7.79%)</td><td>172.90 (-8.52%)</td><td>154.70 (-6.30%)</td><td>20.55 (-18.03%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>193.10 (n/a)</td><td>189.00 (n/a)</td><td>165.10 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (+14.70%)</td><td>0.05 (+11.15%)</td><td>0.05 <b>(+30.02%)</b></td><td>0.03 (-11.25%)</td><td>0.01 <b>(+54.34%)</b></td><td>250.60 (+12.68%)</td><td>176.98 (-7.65%)</td><td>156.20 <b>(-23.09%)</b></td><td>135.00 (-12.79%)</td><td>45.26 <b>(+56.74%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>191.64 (n/a)</td><td>203.10 (n/a)</td><td>154.80 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (-5.54%)</td><td>0.05 (-12.60%)</td><td>0.06 (-12.17%)</td><td>0.04 (-13.51%)</td><td>0.01 (+8.51%)</td><td>252.20 (+15.58%)</td><td>200.40 (+15.56%)</td><td>184.20 (+13.84%)</td><td>151.70 (+5.86%)</td><td>40.62 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>173.42 (n/a)</td><td>161.80 (n/a)</td><td>143.30 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 <b>(+57.85%)</b></td><td>0.05 <b>(+29.26%)</b></td><td>0.05 (+13.43%)</td><td>0.04 (+15.61%)</td><td>0.01 <b>(+221.33%)</b></td><td>191.70 (-13.49%)</td><td>157.76 <b>(-20.66%)</b></td><td>168.10 (-11.80%)</td><td>116.00 <b>(-36.65%)</b></td><td>29.44 <b>(+73.32%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>198.84 (n/a)</td><td>190.60 (n/a)</td><td>183.10 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (+14.18%)</td><td>0.06 (+12.27%)</td><td>0.06 (+12.69%)</td><td>0.05 (-4.89%)</td><td>0.01 <b>(+84.55%)</b></td><td>218.40 (+5.10%)</td><td>176.84 (-9.66%)</td><td>178.30 (-11.25%)</td><td>145.30 (-12.42%)</td><td>28.99 <b>(+71.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>195.74 (n/a)</td><td>200.90 (n/a)</td><td>165.90 (n/a)</td><td>16.94 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.04 (-7.72%)</td><td>0.04 (+6.53%)</td><td>0.04 (+9.68%)</td><td>0.04 (+13.92%)</td><td>0.00 <b>(-49.24%)</b></td><td>217.00 (-12.22%)</td><td>192.74 (-7.14%)</td><td>187.60 (-8.80%)</td><td>183.30 (+8.40%)</td><td>13.73 <b>(-50.81%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.20 (n/a)</td><td>207.56 (n/a)</td><td>205.70 (n/a)</td><td>169.10 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.08 <b>(+21.80%)</b></td><td>0.06 (+7.91%)</td><td>0.05 (-4.48%)</td><td>0.05 (+6.36%)</td><td>0.01 <b>(+49.08%)</b></td><td>204.20 (-5.99%)</td><td>171.82 (-5.77%)</td><td>185.80 (+4.74%)</td><td>112.80 (-17.90%)</td><td>35.23 (+8.92%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>182.34 (n/a)</td><td>177.40 (n/a)</td><td>137.40 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (+14.24%)</td><td>0.05 (+3.74%)</td><td>0.05 (+6.65%)</td><td>0.04 (+1.33%)</td><td>0.01 <b>(+76.05%)</b></td><td>196.80 (-1.30%)</td><td>173.64 (-2.70%)</td><td>167.50 (-6.22%)</td><td>142.50 (-12.47%)</td><td>23.01 <b>(+56.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.40 (n/a)</td><td>178.46 (n/a)</td><td>178.60 (n/a)</td><td>162.80 (n/a)</td><td>14.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 (+18.55%)</td><td>0.05 (+18.75%)</td><td>0.05 (+16.02%)</td><td>0.04 <b>(+49.62%)</b></td><td>0.01 (-2.68%)</td><td>220.10 <b>(-33.16%)</b></td><td>176.82 (-18.09%)</td><td>169.40 (-13.84%)</td><td>137.10 (-15.63%)</td><td>34.42 <b>(-47.48%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>329.30 (n/a)</td><td>215.88 (n/a)</td><td>196.60 (n/a)</td><td>162.50 (n/a)</td><td>65.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 (-15.68%)</td><td>0.05 (+8.09%)</td><td>0.04 (+12.74%)</td><td>0.04 (+19.71%)</td><td>0.01 <b>(-53.70%)</b></td><td>196.70 (-16.44%)</td><td>176.62 (-10.94%)</td><td>186.20 (-11.29%)</td><td>148.80 (+18.57%)</td><td>20.49 <b>(-51.59%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>198.32 (n/a)</td><td>209.90 (n/a)</td><td>125.50 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.07 <b>(+64.99%)</b></td><td>0.05 <b>(+22.32%)</b></td><td>0.04 (-2.08%)</td><td>0.04 <b>(+58.55%)</b></td><td>0.01 <b>(+76.87%)</b></td><td>223.90 <b>(-36.93%)</b></td><td>193.06 (-17.82%)</td><td>209.90 (+2.09%)</td><td>118.50 <b>(-39.39%)</b></td><td>42.39 <b>(-37.24%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>355.00 (n/a)</td><td>234.92 (n/a)</td><td>205.60 (n/a)</td><td>195.50 (n/a)</td><td>67.54 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.06 <b>(+21.26%)</b></td><td>0.05 (+13.81%)</td><td>0.04 (+1.18%)</td><td>0.04 <b>(+21.30%)</b></td><td>0.01 <b>(+29.28%)</b></td><td>200.80 (-17.57%)</td><td>173.88 (-11.94%)</td><td>185.00 (-1.12%)</td><td>132.80 (-17.52%)</td><td>27.00 (-14.04%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.60 (n/a)</td><td>197.46 (n/a)</td><td>187.10 (n/a)</td><td>161.00 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 (-1.18%)</td><td>0.04 (-13.50%)</td><td>0.04 (-13.01%)</td><td>0.03 <b>(-30.19%)</b></td><td>0.01 <b>(+63.16%)</b></td><td>317.40 <b>(+43.23%)</b></td><td>243.48 (+19.71%)</td><td>247.50 (+14.96%)</td><td>165.90 (+1.22%)</td><td>56.87 <b>(+131.42%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>203.40 (n/a)</td><td>215.30 (n/a)</td><td>163.90 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.05 <b>(+20.46%)</b></td><td>0.04 (+7.33%)</td><td>0.04 (+3.67%)</td><td>0.02 (-17.81%)</td><td>0.01 <b>(+93.06%)</b></td><td>375.90 <b>(+21.65%)</b></td><td>246.04 (-2.67%)</td><td>225.50 (-3.55%)</td><td>181.20 (-16.99%)</td><td>75.26 <b>(+105.56%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>309.00 (n/a)</td><td>252.78 (n/a)</td><td>233.80 (n/a)</td><td>218.30 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.71 (-11.72%)</td><td>0.58 (-15.14%)</td><td>0.57 (-18.08%)</td><td>0.45 (-18.99%)</td><td>0.09 (-0.23%)</td><td>220.50 <b>(+23.46%)</b></td><td>174.50 (+18.56%)</td><td>172.30 <b>(+22.03%)</b></td><td>139.20 (+13.26%)</td><td>29.80 <b>(+39.82%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.80 (n/a)</td><td>0.68 (n/a)</td><td>0.70 (n/a)</td><td>0.55 (n/a)</td><td>0.09 (n/a)</td><td>178.60 (n/a)</td><td>147.18 (n/a)</td><td>141.20 (n/a)</td><td>122.90 (n/a)</td><td>21.31 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.94 (-6.06%)</td><td>0.62 (-9.20%)</td><td>0.56 (-7.43%)</td><td>0.42 <b>(-23.53%)</b></td><td>0.22 <b>(+21.55%)</b></td><td>232.90 <b>(+30.77%)</b></td><td>175.38 (+15.95%)</td><td>175.20 (+8.01%)</td><td>104.60 (+6.41%)</td><td>57.21 <b>(+85.76%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.00 (n/a)</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.55 (n/a)</td><td>0.18 (n/a)</td><td>178.10 (n/a)</td><td>151.26 (n/a)</td><td>162.20 (n/a)</td><td>98.30 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.90 <b>(+31.23%)</b></td><td>0.63 (+16.58%)</td><td>0.65 <b>(+22.91%)</b></td><td>0.45 (+2.71%)</td><td>0.17 <b>(+65.00%)</b></td><td>220.90 (-2.64%)</td><td>165.56 (-11.77%)</td><td>152.00 (-18.63%)</td><td>109.50 <b>(-23.80%)</b></td><td>43.23 <b>(+21.07%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.68 (n/a)</td><td>0.54 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.11 (n/a)</td><td>226.90 (n/a)</td><td>187.64 (n/a)</td><td>186.80 (n/a)</td><td>143.70 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.73 <b>(+25.47%)</b></td><td>0.53 (+5.25%)</td><td>0.45 (-6.82%)</td><td>0.41 (-12.51%)</td><td>0.14 <b>(+190.45%)</b></td><td>240.80 (+14.29%)</td><td>193.74 (-0.83%)</td><td>217.60 (+7.35%)</td><td>134.30 <b>(-20.34%)</b></td><td>45.40 <b>(+164.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.58 (n/a)</td><td>0.51 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>210.70 (n/a)</td><td>195.36 (n/a)</td><td>202.70 (n/a)</td><td>168.60 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.61 <b>(+23.72%)</b></td><td>0.46 (+1.62%)</td><td>0.41 (-10.13%)</td><td>0.34 (-19.84%)</td><td>0.11 <b>(+268.05%)</b></td><td>218.10 <b>(+24.77%)</b></td><td>168.08 (+2.58%)</td><td>181.60 (+11.27%)</td><td>120.80 (-19.20%)</td><td>38.87 <b>(+261.39%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.03 (n/a)</td><td>174.80 (n/a)</td><td>163.86 (n/a)</td><td>163.20 (n/a)</td><td>149.50 (n/a)</td><td>10.75 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.50 (-8.55%)</td><td>0.40 (-7.99%)</td><td>0.38 (-14.12%)</td><td>0.36 <b>(+21.20%)</b></td><td>0.06 <b>(-35.74%)</b></td><td>206.90 (-17.47%)</td><td>189.44 (+5.84%)</td><td>195.90 (+16.40%)</td><td>147.80 (+9.40%)</td><td>24.24 <b>(-44.57%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>250.70 (n/a)</td><td>178.98 (n/a)</td><td>168.30 (n/a)</td><td>135.10 (n/a)</td><td>43.73 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.50 <b>(-24.37%)</b></td><td>0.44 (-1.83%)</td><td>0.43 (+3.61%)</td><td>0.37 <b>(+24.84%)</b></td><td>0.05 <b>(-62.71%)</b></td><td>198.50 (-19.90%)</td><td>170.48 (-3.65%)</td><td>170.80 (-3.50%)</td><td>146.20 <b>(+32.19%)</b></td><td>19.86 <b>(-59.26%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.67 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.14 (n/a)</td><td>247.80 (n/a)</td><td>176.94 (n/a)</td><td>177.00 (n/a)</td><td>110.60 (n/a)</td><td>48.74 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.59 <b>(+29.55%)</b></td><td>0.45 (+9.97%)</td><td>0.38 (-6.86%)</td><td>0.32 (-8.55%)</td><td>0.12 <b>(+219.11%)</b></td><td>230.20 (+9.36%)</td><td>174.98 (-4.47%)</td><td>192.00 (+7.38%)</td><td>125.90 <b>(-22.81%)</b></td><td>45.01 <b>(+154.60%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.45 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>210.50 (n/a)</td><td>183.16 (n/a)</td><td>178.80 (n/a)</td><td>163.10 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.04 (-4.64%)</td><td>0.83 (+1.16%)</td><td>0.78 (-1.79%)</td><td>0.72 (+5.09%)</td><td>0.12 <b>(-23.55%)</b></td><td>181.80 (-4.82%)</td><td>160.60 (-2.26%)</td><td>167.80 (+1.82%)</td><td>126.20 (+4.82%)</td><td>21.04 <b>(-24.80%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.09 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.16 (n/a)</td><td>191.00 (n/a)</td><td>164.32 (n/a)</td><td>164.80 (n/a)</td><td>120.40 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>1.06 (+15.22%)</td><td>0.67 (-13.72%)</td><td>0.58 <b>(-25.71%)</b></td><td>0.32 <b>(-43.72%)</b></td><td>0.28 <b>(+119.17%)</b></td><td>404.40 <b>(+77.68%)</b></td><td>229.04 <b>(+32.16%)</b></td><td>224.10 <b>(+34.59%)</b></td><td>123.50 (-13.15%)</td><td>107.50 <b>(+232.40%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.58 (n/a)</td><td>0.13 (n/a)</td><td>227.60 (n/a)</td><td>173.30 (n/a)</td><td>166.50 (n/a)</td><td>142.20 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.85 (-2.18%)</td><td>0.78 (+3.48%)</td><td>0.80 (+4.44%)</td><td>0.65 (-2.95%)</td><td>0.08 (-0.66%)</td><td>202.50 (+3.05%)</td><td>169.82 (-3.34%)</td><td>164.40 (-4.25%)</td><td>153.30 (+2.20%)</td><td>19.73 (+4.67%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.87 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.67 (n/a)</td><td>0.08 (n/a)</td><td>196.50 (n/a)</td><td>175.68 (n/a)</td><td>171.70 (n/a)</td><td>150.00 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.00 (-2.22%)</td><td>0.00 (+0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 (+9.54%)</td><td>1040.36 (+0.37%)</td><td>973.35 (-0.34%)</td><td>972.15 (-0.15%)</td><td>936.91 (+2.35%)</td><td>41.73 (-3.59%)</td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1036.52 (n/a)</td><td>976.67 (n/a)</td><td>973.59 (n/a)</td><td>915.40 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.01 (+0.00%)</td><td>0.01 (-2.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (-10.81%)</td><td>0.00 <b>(+78.04%)</b></td><td>1236.94 (+11.77%)</td><td>1055.67 (+2.61%)</td><td>1027.40 (+0.19%)</td><td>968.09 (-0.00%)</td><td>104.33 <b>(+102.95%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1106.70 (n/a)</td><td>1028.86 (n/a)</td><td>1025.44 (n/a)</td><td>968.13 (n/a)</td><td>51.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.96 (-4.27%)</td><td>0.95 (-1.85%)</td><td>0.95 (-0.09%)</td><td>0.94 (-0.77%)</td><td>0.01 <b>(-72.51%)</b></td><td>2230.56 (+0.78%)</td><td>2203.80 (+1.84%)</td><td>2200.64 (+0.10%)</td><td>2187.00 (+4.47%)</td><td>16.35 <b>(-71.02%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.03 (n/a)</td><td>2213.34 (n/a)</td><td>2164.03 (n/a)</td><td>2198.47 (n/a)</td><td>2093.50 (n/a)</td><td>56.41 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.41 (+1.19%)</td><td>0.39 (+1.99%)</td><td>0.39 (+0.75%)</td><td>0.38 (+3.70%)</td><td>0.01 (-19.22%)</td><td>1375.92 (-3.57%)</td><td>1340.33 (-1.98%)</td><td>1349.53 (-0.73%)</td><td>1288.52 (-1.18%)</td><td>34.57 <b>(-23.09%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1426.89 (n/a)</td><td>1367.39 (n/a)</td><td>1359.52 (n/a)</td><td>1303.92 (n/a)</td><td>44.95 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.26 (+2.85%)</td><td>0.25 (+0.54%)</td><td>0.25 (-0.12%)</td><td>0.25 (+0.41%)</td><td>0.01 <b>(+69.12%)</b></td><td>2117.18 (-0.42%)</td><td>2066.20 (-0.52%)</td><td>2072.40 (+0.13%)</td><td>1987.16 (-2.79%)</td><td>49.94 <b>(+63.08%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.00 (n/a)</td><td>2126.08 (n/a)</td><td>2076.92 (n/a)</td><td>2069.74 (n/a)</td><td>2044.18 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>0.38 (+2.57%)</td><td>0.37 (+2.53%)</td><td>0.37 (+4.52%)</td><td>0.36 (+0.59%)</td><td>0.01 <b>(+38.46%)</b></td><td>1460.15 (-0.58%)</td><td>1412.30 (-2.45%)</td><td>1398.69 (-4.35%)</td><td>1383.10 (-2.49%)</td><td>33.01 <b>(+33.92%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1468.74 (n/a)</td><td>1447.79 (n/a)</td><td>1462.24 (n/a)</td><td>1418.37 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.41 (+5.44%)</td><td>2.95 (-3.00%)</td><td>2.84 (-11.64%)</td><td>2.69 (+12.55%)</td><td>0.29 <b>(-20.78%)</b></td><td>194.60 (-11.14%)</td><td>178.76 (+2.44%)</td><td>184.90 (+13.23%)</td><td>153.70 (-5.12%)</td><td>16.43 <b>(-34.05%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.24 (n/a)</td><td>3.05 (n/a)</td><td>3.21 (n/a)</td><td>2.39 (n/a)</td><td>0.37 (n/a)</td><td>219.00 (n/a)</td><td>174.50 (n/a)</td><td>163.30 (n/a)</td><td>162.00 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>6.38 (+7.64%)</td><td>5.04 (-6.28%)</td><td>4.71 (-15.23%)</td><td>3.98 (-13.48%)</td><td>0.93 <b>(+78.64%)</b></td><td>263.50 (+15.57%)</td><td>213.58 (+8.68%)</td><td>222.80 (+18.01%)</td><td>164.30 (-7.12%)</td><td>38.06 <b>(+88.31%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>5.93 (n/a)</td><td>5.38 (n/a)</td><td>5.55 (n/a)</td><td>4.60 (n/a)</td><td>0.52 (n/a)</td><td>228.00 (n/a)</td><td>196.52 (n/a)</td><td>188.80 (n/a)</td><td>176.90 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>8982f0c</code> — 2026-08-28 19:39:04</td><td>3.58 (+4.27%)</td><td>3.01 (-1.66%)</td><td>3.21 (+7.71%)</td><td>2.00 <b>(-26.96%)</b></td><td>0.63 <b>(+108.12%)</b></td><td>262.50 <b>(+36.93%)</b></td><td>181.70 (+5.42%)</td><td>163.40 (-7.16%)</td><td>146.50 (-4.12%)</td><td>47.21 <b>(+182.61%)</b></td>
</tr>
<tr>
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.43 (n/a)</td><td>3.07 (n/a)</td><td>2.98 (n/a)</td><td>2.73 (n/a)</td><td>0.30 (n/a)</td><td>191.70 (n/a)</td><td>172.36 (n/a)</td><td>176.00 (n/a)</td><td>152.80 (n/a)</td><td>16.71 (n/a)</td>
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
