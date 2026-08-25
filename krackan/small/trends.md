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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (-11.80%)</td><td>0.07 (-7.39%)</td><td>0.07 (+2.60%)</td><td>0.05 (-13.67%)</td><td>0.01 <b>(-20.15%)</b></td><td>225.90 (+15.79%)</td><td>180.84 (+7.16%)</td><td>182.10 (-2.57%)</td><td>129.80 (+13.36%)</td><td>34.21 (+2.09%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>168.76 (n/a)</td><td>186.90 (n/a)</td><td>114.50 (n/a)</td><td>33.51 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 <b>(-38.64%)</b></td><td>0.07 (-16.87%)</td><td>0.07 (-3.81%)</td><td>0.05 (-16.83%)</td><td>0.01 <b>(-63.75%)</b></td><td>228.40 <b>(+20.21%)</b></td><td>184.98 (+15.76%)</td><td>177.00 (+4.00%)</td><td>164.10 <b>(+62.96%)</b></td><td>26.22 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.00 (n/a)</td><td>159.80 (n/a)</td><td>170.20 (n/a)</td><td>100.70 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (+0.55%)</td><td>0.07 (+10.63%)</td><td>0.07 (+13.94%)</td><td>0.05 (+0.97%)</td><td>0.01 (+1.03%)</td><td>236.30 (-0.96%)</td><td>174.26 (-9.53%)</td><td>174.20 (-12.24%)</td><td>138.90 (-0.57%)</td><td>38.27 (+1.81%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>192.62 (n/a)</td><td>198.50 (n/a)</td><td>139.70 (n/a)</td><td>37.59 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (-1.00%)</td><td>0.07 (-3.93%)</td><td>0.06 (-11.43%)</td><td>0.05 (-4.59%)</td><td>0.02 (+7.77%)</td><td>226.80 (+4.81%)</td><td>187.30 (+4.84%)</td><td>200.70 (+12.94%)</td><td>129.40 (+1.01%)</td><td>37.31 (+14.53%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>178.66 (n/a)</td><td>177.70 (n/a)</td><td>128.10 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.03 (-10.28%)</td><td>0.03 (+0.81%)</td><td>0.03 (+5.82%)</td><td>0.03 (+10.42%)</td><td>0.00 <b>(-40.40%)</b></td><td>187.40 (-9.47%)</td><td>166.10 (-2.12%)</td><td>158.30 (-5.49%)</td><td>151.30 (+11.50%)</td><td>16.47 <b>(-40.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>169.70 (n/a)</td><td>167.50 (n/a)</td><td>135.70 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(+27.53%)</b></td><td>0.03 (-9.61%)</td><td>0.03 <b>(-24.74%)</b></td><td>0.02 (-8.25%)</td><td>0.01 <b>(+86.75%)</b></td><td>228.20 (+8.98%)</td><td>182.72 (+16.17%)</td><td>187.80 <b>(+32.81%)</b></td><td>103.70 <b>(-21.62%)</b></td><td>48.03 <b>(+50.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>157.28 (n/a)</td><td>141.40 (n/a)</td><td>132.30 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (+4.93%)</td><td>0.03 (-5.04%)</td><td>0.03 (-5.03%)</td><td>0.02 (-13.14%)</td><td>0.00 <b>(+59.88%)</b></td><td>219.80 (+15.14%)</td><td>174.72 (+6.50%)</td><td>167.30 (+5.29%)</td><td>147.50 (-4.65%)</td><td>27.02 <b>(+78.50%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>164.06 (n/a)</td><td>158.90 (n/a)</td><td>154.70 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(+44.46%)</b></td><td>0.03 (+3.83%)</td><td>0.03 (-10.63%)</td><td>0.02 (-4.52%)</td><td>0.01 <b>(+198.37%)</b></td><td>215.20 (+4.72%)</td><td>183.24 (+1.26%)</td><td>195.20 (+11.86%)</td><td>111.30 <b>(-30.78%)</b></td><td>42.86 <b>(+111.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.50 (n/a)</td><td>180.96 (n/a)</td><td>174.50 (n/a)</td><td>160.80 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 <b>(+22.48%)</b></td><td>0.03 (+10.60%)</td><td>0.04 (+12.64%)</td><td>0.03 (-6.01%)</td><td>0.01 <b>(+120.49%)</b></td><td>205.60 (+6.36%)</td><td>156.48 (-7.40%)</td><td>148.90 (-11.21%)</td><td>121.80 (-18.36%)</td><td>32.07 <b>(+93.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>168.98 (n/a)</td><td>167.70 (n/a)</td><td>149.20 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.03 (-5.58%)</td><td>0.03 (-6.18%)</td><td>0.02 (-9.06%)</td><td>0.02 (-6.70%)</td><td>0.01 <b>(+20.61%)</b></td><td>252.80 (+7.21%)</td><td>206.26 (+7.97%)</td><td>212.80 (+9.97%)</td><td>161.30 (+5.91%)</td><td>41.31 <b>(+34.32%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.80 (n/a)</td><td>191.04 (n/a)</td><td>193.50 (n/a)</td><td>152.30 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 <b>(+24.60%)</b></td><td>0.03 (+1.27%)</td><td>0.03 (-2.46%)</td><td>0.02 (-16.62%)</td><td>0.01 <b>(+190.58%)</b></td><td>237.70 (+19.99%)</td><td>185.92 (+2.05%)</td><td>187.20 (+2.52%)</td><td>129.60 (-19.70%)</td><td>38.29 <b>(+170.95%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.10 (n/a)</td><td>182.18 (n/a)</td><td>182.60 (n/a)</td><td>161.40 (n/a)</td><td>14.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 <b>(+24.53%)</b></td><td>0.03 (+2.41%)</td><td>0.02 (-3.52%)</td><td>0.02 (-11.52%)</td><td>0.01 <b>(+99.63%)</b></td><td>256.20 (+13.01%)</td><td>203.52 (+1.24%)</td><td>219.00 (+3.64%)</td><td>133.00 (-19.69%)</td><td>47.08 <b>(+75.16%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>201.02 (n/a)</td><td>211.30 (n/a)</td><td>165.60 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>183.08 (n/a)</td><td>185.10 (n/a)</td><td>154.30 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>174.50 (n/a)</td><td>167.40 (n/a)</td><td>161.60 (n/a)</td><td>13.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>235.40 (n/a)</td><td>181.02 (n/a)</td><td>179.80 (n/a)</td><td>133.10 (n/a)</td><td>39.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>193.14 (n/a)</td><td>191.50 (n/a)</td><td>168.90 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>185.72 (n/a)</td><td>192.30 (n/a)</td><td>138.70 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>185.98 (n/a)</td><td>190.10 (n/a)</td><td>161.20 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>190.28 (n/a)</td><td>196.00 (n/a)</td><td>151.30 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>320.20 (n/a)</td><td>233.80 (n/a)</td><td>223.10 (n/a)</td><td>193.60 (n/a)</td><td>50.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>185.30 (n/a)</td><td>195.00 (n/a)</td><td>155.60 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>185.12 (n/a)</td><td>178.00 (n/a)</td><td>167.80 (n/a)</td><td>16.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>194.24 (n/a)</td><td>174.30 (n/a)</td><td>166.10 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>188.30 (n/a)</td><td>197.80 (n/a)</td><td>143.00 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>184.34 (n/a)</td><td>175.70 (n/a)</td><td>169.80 (n/a)</td><td>17.09 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>181.76 (n/a)</td><td>188.40 (n/a)</td><td>138.10 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>192.78 (n/a)</td><td>195.20 (n/a)</td><td>152.90 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>322.40 (n/a)</td><td>235.60 (n/a)</td><td>220.50 (n/a)</td><td>170.40 (n/a)</td><td>58.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>4.30 (-1.52%)</td><td>4.21 (+8.82%)</td><td>4.20 (+11.60%)</td><td>4.09 (+16.04%)</td><td>0.08 <b>(-77.34%)</b></td><td>2301.90 (-13.83%)</td><td>2235.66 (-8.74%)</td><td>2239.20 (-10.40%)</td><td>2187.00 (+1.54%)</td><td>45.45 <b>(-80.33%)</b></td><td>1691.51 (-1.52%)</td><td>1655.25 (+8.82%)</td><td>1652.07 (+11.60%)</td><td>1607.11 (+16.04%)</td><td>33.41 <b>(-77.34%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.37 (n/a)</td><td>3.87 (n/a)</td><td>3.76 (n/a)</td><td>3.52 (n/a)</td><td>0.37 (n/a)</td><td>2671.20 (n/a)</td><td>2449.88 (n/a)</td><td>2499.00 (n/a)</td><td>2153.90 (n/a)</td><td>231.06 (n/a)</td><td>1717.55 (n/a)</td><td>1521.14 (n/a)</td><td>1480.33 (n/a)</td><td>1384.92 (n/a)</td><td>147.43 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.18 (+13.82%)</td><td>0.94 (-2.82%)</td><td>0.94 (-2.66%)</td><td>0.73 (-17.64%)</td><td>0.17 <b>(+143.28%)</b></td><td>303.90 <b>(+21.41%)</b></td><td>241.24 (+5.10%)</td><td>234.10 (+2.72%)</td><td>186.90 (-12.13%)</td><td>43.00 <b>(+161.16%)</b></td><td>50.50 (+13.82%)</td><td>40.12 (-2.82%)</td><td>40.31 (-2.66%)</td><td>31.05 (-17.64%)</td><td>7.13 <b>(+143.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.04 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.88 (n/a)</td><td>0.07 (n/a)</td><td>250.30 (n/a)</td><td>229.54 (n/a)</td><td>227.90 (n/a)</td><td>212.70 (n/a)</td><td>16.46 (n/a)</td><td>44.37 (n/a)</td><td>41.28 (n/a)</td><td>41.41 (n/a)</td><td>37.71 (n/a)</td><td>2.93 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.24 (+6.37%)</td><td>0.91 (+2.91%)</td><td>0.88 (-5.24%)</td><td>0.72 (+10.49%)</td><td>0.22 (-3.59%)</td><td>308.30 (-9.51%)</td><td>253.88 (-4.01%)</td><td>252.20 (+5.52%)</td><td>178.50 (-6.00%)</td><td>55.19 (-19.80%)</td><td>52.87 (+6.37%)</td><td>38.75 (+2.91%)</td><td>37.42 (-5.24%)</td><td>30.61 (+10.49%)</td><td>9.22 (-3.59%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.16 (n/a)</td><td>0.88 (n/a)</td><td>0.93 (n/a)</td><td>0.65 (n/a)</td><td>0.22 (n/a)</td><td>340.70 (n/a)</td><td>264.48 (n/a)</td><td>239.00 (n/a)</td><td>189.90 (n/a)</td><td>68.81 (n/a)</td><td>49.70 (n/a)</td><td>37.66 (n/a)</td><td>39.49 (n/a)</td><td>27.70 (n/a)</td><td>9.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.52 (+0.37%)</td><td>0.52 (+0.36%)</td><td>0.52 (+0.34%)</td><td>0.52 (+0.36%)</td><td>0.00 (+4.06%)</td><td>48633.90 (-0.36%)</td><td>48502.38 (-0.36%)</td><td>48483.00 (-0.34%)</td><td>48444.60 (-0.37%)</td><td>77.22 (+3.27%)</td><td>354.63 (+0.37%)</td><td>354.21 (+0.36%)</td><td>354.35 (+0.34%)</td><td>353.25 (+0.36%)</td><td>0.56 (+4.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48808.00 (n/a)</td><td>48676.00 (n/a)</td><td>48648.30 (n/a)</td><td>48622.50 (n/a)</td><td>74.78 (n/a)</td><td>353.33 (n/a)</td><td>352.94 (n/a)</td><td>353.14 (n/a)</td><td>351.99 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.90 (+1.07%)</td><td>0.89 (+0.79%)</td><td>0.89 (+0.87%)</td><td>0.88 (+0.52%)</td><td>0.01 (+12.45%)</td><td>28520.40 (-0.51%)</td><td>28180.20 (-0.78%)</td><td>28209.50 (-0.86%)</td><td>27807.90 (-1.06%)</td><td>258.02 (+10.67%)</td><td>617.81 (+1.07%)</td><td>609.68 (+0.79%)</td><td>609.01 (+0.87%)</td><td>602.37 (+0.52%)</td><td>5.59 (+12.45%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28667.40 (n/a)</td><td>28401.98 (n/a)</td><td>28455.40 (n/a)</td><td>28106.10 (n/a)</td><td>233.14 (n/a)</td><td>611.25 (n/a)</td><td>604.92 (n/a)</td><td>603.75 (n/a)</td><td>599.28 (n/a)</td><td>4.97 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.30 (-0.91%)</td><td>3.24 (+0.65%)</td><td>3.27 (+3.35%)</td><td>3.14 (+0.88%)</td><td>0.07 <b>(-31.91%)</b></td><td>8016.50 (-0.87%)</td><td>7778.14 (-0.68%)</td><td>7693.20 (-3.24%)</td><td>7635.10 (+0.92%)</td><td>159.46 <b>(-31.54%)</b></td><td>2250.11 (-0.91%)</td><td>2209.47 (+0.65%)</td><td>2233.13 (+3.35%)</td><td>2143.07 (+0.88%)</td><td>44.76 <b>(-31.91%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>3.33 (n/a)</td><td>3.22 (n/a)</td><td>3.17 (n/a)</td><td>3.11 (n/a)</td><td>0.10 (n/a)</td><td>8086.90 (n/a)</td><td>7831.54 (n/a)</td><td>7951.10 (n/a)</td><td>7565.50 (n/a)</td><td>232.94 (n/a)</td><td>2270.83 (n/a)</td><td>2195.25 (n/a)</td><td>2160.70 (n/a)</td><td>2124.40 (n/a)</td><td>65.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.69 (-13.47%)</td><td>3.57 (-3.81%)</td><td>3.56 (-4.19%)</td><td>3.39 (+16.07%)</td><td>0.12 <b>(-76.10%)</b></td><td>2378.90 (-13.85%)</td><td>2260.80 (+2.27%)</td><td>2266.90 (+4.37%)</td><td>2182.60 (+15.56%)</td><td>80.20 <b>(-76.51%)</b></td><td>968.53 (-13.47%)</td><td>935.97 (-3.81%)</td><td>932.54 (-4.19%)</td><td>888.60 (+16.07%)</td><td>32.78 <b>(-76.10%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.27 (n/a)</td><td>3.71 (n/a)</td><td>3.71 (n/a)</td><td>2.92 (n/a)</td><td>0.52 (n/a)</td><td>2761.30 (n/a)</td><td>2210.72 (n/a)</td><td>2171.90 (n/a)</td><td>1888.70 (n/a)</td><td>341.39 (n/a)</td><td>1119.25 (n/a)</td><td>973.05 (n/a)</td><td>973.32 (n/a)</td><td>765.57 (n/a)</td><td>137.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.55 (+9.09%)</td><td>0.40 (+14.10%)</td><td>0.35 (+7.85%)</td><td>0.33 (+18.20%)</td><td>0.10 (+6.33%)</td><td>3815.50 (-15.40%)</td><td>3267.72 (-12.57%)</td><td>3558.50 (-7.28%)</td><td>2260.40 (-8.33%)</td><td>677.23 (-11.80%)</td><td>29.69 (+9.09%)</td><td>21.39 (+14.10%)</td><td>18.86 (+7.85%)</td><td>17.59 (+18.20%)</td><td>5.18 (+6.33%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>4509.80 (n/a)</td><td>3737.72 (n/a)</td><td>3837.90 (n/a)</td><td>2465.80 (n/a)</td><td>767.80 (n/a)</td><td>27.22 (n/a)</td><td>18.75 (n/a)</td><td>17.49 (n/a)</td><td>14.88 (n/a)</td><td>4.87 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>5.06 (+3.40%)</td><td>4.54 (-3.43%)</td><td>4.69 (-1.31%)</td><td>3.59 <b>(-20.06%)</b></td><td>0.56 <b>(+263.07%)</b></td><td>1854.10 <b>(+25.09%)</b></td><td>1486.84 (+4.94%)</td><td>1419.80 (+1.33%)</td><td>1315.90 (-3.29%)</td><td>211.63 <b>(+351.38%)</b></td><td>1561.88 (+3.40%)</td><td>1401.93 (-3.43%)</td><td>1447.57 (-1.31%)</td><td>1108.48 <b>(-20.06%)</b></td><td>173.14 <b>(+263.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.89 (n/a)</td><td>4.70 (n/a)</td><td>4.75 (n/a)</td><td>4.49 (n/a)</td><td>0.15 (n/a)</td><td>1482.20 (n/a)</td><td>1416.90 (n/a)</td><td>1401.20 (n/a)</td><td>1360.60 (n/a)</td><td>46.89 (n/a)</td><td>1510.52 (n/a)</td><td>1451.77 (n/a)</td><td>1466.77 (n/a)</td><td>1386.60 (n/a)</td><td>47.69 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>13.56 (n/a)</td><td>12.96 (n/a)</td><td>13.33 (n/a)</td><td>12.20 (n/a)</td><td>0.70 (n/a)</td><td>13.56 (n/a)</td><td>12.95 (n/a)</td><td>13.32 (n/a)</td><td>12.19 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>24.28 (-3.82%)</td><td>23.92 (-3.26%)</td><td>23.84 (-3.44%)</td><td>23.73 (-1.80%)</td><td>0.21 <b>(-46.62%)</b></td><td>24.26 (-3.82%)</td><td>23.91 (-3.26%)</td><td>23.83 (-3.44%)</td><td>23.72 (-1.80%)</td><td>0.21 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>25.24 (n/a)</td><td>24.73 (n/a)</td><td>24.69 (n/a)</td><td>24.17 (n/a)</td><td>0.40 (n/a)</td><td>25.23 (n/a)</td><td>24.71 (n/a)</td><td>24.68 (n/a)</td><td>24.15 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>41.56 (+0.76%)</td><td>39.64 (-0.36%)</td><td>40.27 (+0.79%)</td><td>35.23 (-8.64%)</td><td>2.56 <b>(+136.16%)</b></td><td>41.53 (+0.76%)</td><td>39.62 (-0.36%)</td><td>40.25 (+0.79%)</td><td>35.21 (-8.64%)</td><td>2.56 <b>(+136.16%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>41.24 (n/a)</td><td>39.78 (n/a)</td><td>39.96 (n/a)</td><td>38.57 (n/a)</td><td>1.09 (n/a)</td><td>41.22 (n/a)</td><td>39.76 (n/a)</td><td>39.93 (n/a)</td><td>38.55 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>43.31 (-5.32%)</td><td>41.69 (-5.16%)</td><td>41.90 (-3.12%)</td><td>38.92 (-8.95%)</td><td>1.67 <b>(+31.63%)</b></td><td>43.28 (-5.32%)</td><td>41.66 (-5.16%)</td><td>41.87 (-3.12%)</td><td>38.89 (-8.95%)</td><td>1.67 <b>(+31.63%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>45.74 (n/a)</td><td>43.95 (n/a)</td><td>43.25 (n/a)</td><td>42.74 (n/a)</td><td>1.27 (n/a)</td><td>45.71 (n/a)</td><td>43.92 (n/a)</td><td>43.22 (n/a)</td><td>42.72 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>13.34 (n/a)</td><td>12.71 (n/a)</td><td>13.13 (n/a)</td><td>11.32 (n/a)</td><td>0.85 (n/a)</td><td>13.33 (n/a)</td><td>12.71 (n/a)</td><td>13.13 (n/a)</td><td>11.31 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>24.48 (-2.91%)</td><td>24.07 (-3.03%)</td><td>24.32 (-2.45%)</td><td>23.27 (-4.12%)</td><td>0.52 <b>(+31.53%)</b></td><td>24.47 (-2.91%)</td><td>24.06 (-3.03%)</td><td>24.31 (-2.45%)</td><td>23.26 (-4.12%)</td><td>0.52 <b>(+31.53%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>25.22 (n/a)</td><td>24.82 (n/a)</td><td>24.93 (n/a)</td><td>24.27 (n/a)</td><td>0.40 (n/a)</td><td>25.20 (n/a)</td><td>24.81 (n/a)</td><td>24.92 (n/a)</td><td>24.26 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>40.26 (-0.63%)</td><td>38.83 (-1.19%)</td><td>39.18 (-0.97%)</td><td>36.64 (-0.09%)</td><td>1.53 (-2.06%)</td><td>40.23 (-0.63%)</td><td>38.80 (-1.19%)</td><td>39.16 (-0.97%)</td><td>36.62 (-0.09%)</td><td>1.53 (-2.06%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>40.51 (n/a)</td><td>39.29 (n/a)</td><td>39.57 (n/a)</td><td>36.67 (n/a)</td><td>1.56 (n/a)</td><td>40.49 (n/a)</td><td>39.27 (n/a)</td><td>39.55 (n/a)</td><td>36.65 (n/a)</td><td>1.56 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>45.04 (+0.36%)</td><td>42.83 (+0.29%)</td><td>43.18 (+2.18%)</td><td>38.75 (-1.54%)</td><td>2.41 (+4.76%)</td><td>45.02 (+0.36%)</td><td>42.80 (+0.29%)</td><td>43.15 (+2.18%)</td><td>38.72 (-1.54%)</td><td>2.41 (+4.76%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>44.88 (n/a)</td><td>42.71 (n/a)</td><td>42.26 (n/a)</td><td>39.35 (n/a)</td><td>2.30 (n/a)</td><td>44.85 (n/a)</td><td>42.68 (n/a)</td><td>42.23 (n/a)</td><td>39.33 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>9.19 (-6.54%)</td><td>8.79 (-3.45%)</td><td>8.79 (-3.10%)</td><td>8.42 (-0.69%)</td><td>0.33 <b>(-37.87%)</b></td><td>9.18 (-6.54%)</td><td>8.77 (-3.45%)</td><td>8.77 (-3.10%)</td><td>8.40 (-0.69%)</td><td>0.33 <b>(-37.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>9.84 (n/a)</td><td>9.10 (n/a)</td><td>9.07 (n/a)</td><td>8.48 (n/a)</td><td>0.52 (n/a)</td><td>9.82 (n/a)</td><td>9.08 (n/a)</td><td>9.05 (n/a)</td><td>8.46 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.93 (+5.12%)</td><td>0.87 (+4.13%)</td><td>0.87 (+4.77%)</td><td>0.81 (+3.31%)</td><td>0.05 (+5.89%)</td><td>0.91 (+5.12%)</td><td>0.85 (+4.13%)</td><td>0.85 (+4.77%)</td><td>0.79 (+3.31%)</td><td>0.05 (+5.89%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.88 (n/a)</td><td>0.83 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.05 (n/a)</td><td>0.87 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.40 (+6.70%)</td><td>1.23 (-2.29%)</td><td>1.15 (-11.15%)</td><td>1.07 (-6.72%)</td><td>0.15 <b>(+130.24%)</b></td><td>1.38 (+6.70%)</td><td>1.21 (-2.29%)</td><td>1.13 (-11.15%)</td><td>1.06 (-6.72%)</td><td>0.15 <b>(+130.24%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.31 (n/a)</td><td>1.26 (n/a)</td><td>1.29 (n/a)</td><td>1.15 (n/a)</td><td>0.07 (n/a)</td><td>1.30 (n/a)</td><td>1.24 (n/a)</td><td>1.27 (n/a)</td><td>1.14 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>20.68 <b>(+25.59%)</b></td><td>17.36 (+14.24%)</td><td>17.35 (+14.41%)</td><td>14.04 (-3.49%)</td><td>2.35 <b>(+199.47%)</b></td><td>20.44 <b>(+25.59%)</b></td><td>17.16 (+14.24%)</td><td>17.15 (+14.41%)</td><td>13.87 (-3.49%)</td><td>2.32 <b>(+199.47%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>16.46 (n/a)</td><td>15.19 (n/a)</td><td>15.16 (n/a)</td><td>14.54 (n/a)</td><td>0.78 (n/a)</td><td>16.27 (n/a)</td><td>15.02 (n/a)</td><td>14.99 (n/a)</td><td>14.37 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>14.21 (+15.80%)</td><td>13.44 (+13.05%)</td><td>13.70 (+17.20%)</td><td>12.04 (+3.68%)</td><td>0.82 <b>(+157.13%)</b></td><td>13.96 (+15.80%)</td><td>13.20 (+13.05%)</td><td>13.46 (+17.20%)</td><td>11.83 (+3.68%)</td><td>0.81 <b>(+157.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>12.27 (n/a)</td><td>11.89 (n/a)</td><td>11.69 (n/a)</td><td>11.62 (n/a)</td><td>0.32 (n/a)</td><td>12.06 (n/a)</td><td>11.68 (n/a)</td><td>11.49 (n/a)</td><td>11.41 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>8.37 (-16.97%)</td><td>7.93 (-8.82%)</td><td>7.77 (-9.41%)</td><td>7.70 (-0.28%)</td><td>0.30 <b>(-65.64%)</b></td><td>8.23 (-16.97%)</td><td>7.79 (-8.82%)</td><td>7.63 (-9.41%)</td><td>7.56 (-0.28%)</td><td>0.30 <b>(-65.64%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>10.08 (n/a)</td><td>8.70 (n/a)</td><td>8.58 (n/a)</td><td>7.72 (n/a)</td><td>0.88 (n/a)</td><td>9.91 (n/a)</td><td>8.55 (n/a)</td><td>8.43 (n/a)</td><td>7.58 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>6.76 (-4.11%)</td><td>5.57 (-16.31%)</td><td>5.50 (-16.76%)</td><td>4.94 (-19.66%)</td><td>0.73 <b>(+110.17%)</b></td><td>6.65 (-4.11%)</td><td>5.48 (-16.31%)</td><td>5.42 (-16.76%)</td><td>4.86 (-19.66%)</td><td>0.72 <b>(+110.17%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>7.05 (n/a)</td><td>6.66 (n/a)</td><td>6.61 (n/a)</td><td>6.15 (n/a)</td><td>0.35 (n/a)</td><td>6.93 (n/a)</td><td>6.55 (n/a)</td><td>6.51 (n/a)</td><td>6.05 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>13.23 (n/a)</td><td>12.23 (n/a)</td><td>12.30 (n/a)</td><td>11.07 (n/a)</td><td>0.77 (n/a)</td><td>13.22 (n/a)</td><td>12.23 (n/a)</td><td>12.29 (n/a)</td><td>11.07 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>13.14 (n/a)</td><td>12.72 (n/a)</td><td>13.06 (n/a)</td><td>11.75 (n/a)</td><td>0.60 (n/a)</td><td>13.13 (n/a)</td><td>12.71 (n/a)</td><td>13.05 (n/a)</td><td>11.74 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>178.48 (n/a)</td><td>173.60 (n/a)</td><td>138.00 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>189.40 (n/a)</td><td>198.00 (n/a)</td><td>141.70 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>174.48 (n/a)</td><td>178.10 (n/a)</td><td>146.00 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.60 (n/a)</td><td>157.80 (n/a)</td><td>153.20 (n/a)</td><td>143.60 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>167.82 (n/a)</td><td>170.80 (n/a)</td><td>131.10 (n/a)</td><td>31.81 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.50 (n/a)</td><td>208.64 (n/a)</td><td>203.50 (n/a)</td><td>148.10 (n/a)</td><td>53.26 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.80 (n/a)</td><td>199.80 (n/a)</td><td>187.70 (n/a)</td><td>164.70 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>276.00 (n/a)</td><td>227.76 (n/a)</td><td>224.40 (n/a)</td><td>197.90 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.08 (+10.94%)</td><td>0.06 (-5.27%)</td><td>0.05 (-12.38%)</td><td>0.05 (-4.99%)</td><td>0.01 <b>(+38.92%)</b></td><td>179.50 (+5.28%)</td><td>154.50 (+7.31%)</td><td>162.80 (+14.17%)</td><td>106.40 (-9.83%)</td><td>29.94 <b>(+30.11%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.50 (n/a)</td><td>143.98 (n/a)</td><td>142.60 (n/a)</td><td>118.00 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (+2.20%)</td><td>0.05 (-7.96%)</td><td>0.05 (-16.59%)</td><td>0.04 (-10.52%)</td><td>0.01 (+0.76%)</td><td>197.60 (+11.76%)</td><td>158.92 (+8.82%)</td><td>158.40 (+19.91%)</td><td>120.30 (-2.20%)</td><td>27.80 (+7.54%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>146.04 (n/a)</td><td>132.10 (n/a)</td><td>123.00 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (+10.35%)</td><td>0.06 (+4.97%)</td><td>0.06 (+10.52%)</td><td>0.04 <b>(-20.51%)</b></td><td>0.01 <b>(+113.03%)</b></td><td>213.70 <b>(+25.78%)</b></td><td>150.26 (-0.66%)</td><td>137.40 (-9.55%)</td><td>114.90 (-9.38%)</td><td>40.82 <b>(+140.78%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>151.26 (n/a)</td><td>151.90 (n/a)</td><td>126.80 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (+9.03%)</td><td>0.05 (-4.36%)</td><td>0.05 (-7.51%)</td><td>0.02 <b>(-39.21%)</b></td><td>0.02 <b>(+84.76%)</b></td><td>343.50 <b>(+64.43%)</b></td><td>187.44 (+15.60%)</td><td>157.50 (+8.10%)</td><td>127.00 (-8.24%)</td><td>88.89 <b>(+197.26%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>162.14 (n/a)</td><td>145.70 (n/a)</td><td>138.40 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 <b>(+20.61%)</b></td><td>0.06 (+11.21%)</td><td>0.05 (-3.81%)</td><td>0.05 (+7.42%)</td><td>0.01 <b>(+67.49%)</b></td><td>171.40 (-6.95%)</td><td>143.06 (-8.65%)</td><td>154.50 (+3.97%)</td><td>113.40 (-17.04%)</td><td>26.99 <b>(+25.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>156.60 (n/a)</td><td>148.60 (n/a)</td><td>136.70 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 <b>(+26.62%)</b></td><td>0.06 <b>(+20.01%)</b></td><td>0.06 (+17.60%)</td><td>0.05 <b>(+23.82%)</b></td><td>0.01 <b>(+27.46%)</b></td><td>163.00 (-19.27%)</td><td>143.34 (-16.66%)</td><td>147.80 (-14.96%)</td><td>111.90 <b>(-21.03%)</b></td><td>19.29 <b>(-20.69%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>172.00 (n/a)</td><td>173.80 (n/a)</td><td>141.70 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (-7.55%)</td><td>0.05 (-6.57%)</td><td>0.05 (-5.49%)</td><td>0.05 (+5.21%)</td><td>0.01 <b>(-31.87%)</b></td><td>178.30 (-4.96%)</td><td>160.76 (+6.03%)</td><td>156.50 (+5.81%)</td><td>137.90 (+8.16%)</td><td>16.71 <b>(-29.20%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>151.62 (n/a)</td><td>147.90 (n/a)</td><td>127.50 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (+7.11%)</td><td>0.05 (+7.09%)</td><td>0.05 (+13.30%)</td><td>0.04 (+0.44%)</td><td>0.01 <b>(+23.86%)</b></td><td>225.50 (-0.44%)</td><td>168.48 (-5.88%)</td><td>156.30 (-11.69%)</td><td>144.90 (-6.64%)</td><td>33.00 (+16.14%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>179.00 (n/a)</td><td>177.00 (n/a)</td><td>155.20 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (-1.06%)</td><td>0.05 (-2.42%)</td><td>0.04 (-13.06%)</td><td>0.03 (+9.35%)</td><td>0.01 (-5.96%)</td><td>244.50 (-8.56%)</td><td>180.88 (+0.89%)</td><td>190.10 (+15.00%)</td><td>113.80 (+1.07%)</td><td>47.56 (-16.72%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>267.40 (n/a)</td><td>179.28 (n/a)</td><td>165.30 (n/a)</td><td>112.60 (n/a)</td><td>57.10 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (+16.08%)</td><td>0.04 (+15.57%)</td><td>0.04 (+11.15%)</td><td>0.04 <b>(+52.33%)</b></td><td>0.00 <b>(-37.45%)</b></td><td>215.40 <b>(-34.35%)</b></td><td>191.36 (-16.03%)</td><td>189.90 (-10.04%)</td><td>166.60 (-13.81%)</td><td>19.70 <b>(-65.30%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.10 (n/a)</td><td>227.90 (n/a)</td><td>211.10 (n/a)</td><td>193.30 (n/a)</td><td>56.77 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 <b>(+25.46%)</b></td><td>0.05 (-7.32%)</td><td>0.04 (-11.74%)</td><td>0.03 <b>(-29.12%)</b></td><td>0.02 <b>(+187.70%)</b></td><td>263.00 <b>(+41.09%)</b></td><td>194.22 (+15.52%)</td><td>192.30 (+13.25%)</td><td>118.10 <b>(-20.31%)</b></td><td>56.47 <b>(+220.81%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>168.12 (n/a)</td><td>169.80 (n/a)</td><td>148.20 (n/a)</td><td>17.60 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (-9.24%)</td><td>0.04 (-11.19%)</td><td>0.04 (-4.38%)</td><td>0.02 <b>(-39.36%)</b></td><td>0.01 <b>(+71.07%)</b></td><td>348.90 <b>(+64.89%)</b></td><td>228.92 (+18.32%)</td><td>217.40 (+4.57%)</td><td>176.20 (+10.19%)</td><td>70.72 <b>(+207.61%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>193.48 (n/a)</td><td>207.90 (n/a)</td><td>159.90 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (+19.81%)</td><td>0.06 (+15.71%)</td><td>0.06 <b>(+20.56%)</b></td><td>0.05 (+5.54%)</td><td>0.01 <b>(+56.07%)</b></td><td>177.60 (-5.28%)</td><td>140.34 (-12.76%)</td><td>134.90 (-17.04%)</td><td>115.00 (-16.55%)</td><td>22.87 <b>(+26.13%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>160.86 (n/a)</td><td>162.60 (n/a)</td><td>137.80 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(-23.52%)</b></td><td>0.05 (-5.32%)</td><td>0.05 (+7.34%)</td><td>0.05 (+9.48%)</td><td>0.00 <b>(-77.58%)</b></td><td>172.20 (-8.65%)</td><td>164.08 (+2.77%)</td><td>161.90 (-6.85%)</td><td>153.60 <b>(+30.72%)</b></td><td>7.78 <b>(-72.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>159.66 (n/a)</td><td>173.80 (n/a)</td><td>117.50 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 <b>(+30.55%)</b></td><td>0.05 (+13.92%)</td><td>0.05 (+12.00%)</td><td>0.04 (+0.94%)</td><td>0.01 <b>(+194.53%)</b></td><td>188.80 (-0.94%)</td><td>158.30 (-10.64%)</td><td>158.00 (-10.68%)</td><td>123.70 <b>(-23.36%)</b></td><td>24.95 <b>(+121.75%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>177.14 (n/a)</td><td>176.90 (n/a)</td><td>161.40 (n/a)</td><td>11.25 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (+13.53%)</td><td>0.05 (-5.61%)</td><td>0.04 (-15.18%)</td><td>0.03 (-9.00%)</td><td>0.01 <b>(+51.60%)</b></td><td>235.80 (+9.88%)</td><td>186.92 (+8.18%)</td><td>193.50 (+17.92%)</td><td>130.90 (-11.97%)</td><td>39.41 <b>(+44.38%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>172.78 (n/a)</td><td>164.10 (n/a)</td><td>148.70 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (+3.25%)</td><td>0.04 (-6.64%)</td><td>0.04 (-6.92%)</td><td>0.03 (-7.13%)</td><td>0.01 <b>(+35.33%)</b></td><td>255.30 (+7.68%)</td><td>202.30 (+9.51%)</td><td>198.70 (+7.46%)</td><td>151.10 (-3.14%)</td><td>47.67 <b>(+44.21%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>184.74 (n/a)</td><td>184.90 (n/a)</td><td>156.00 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (+10.51%)</td><td>0.05 (+2.08%)</td><td>0.05 (+2.62%)</td><td>0.03 (-13.69%)</td><td>0.01 <b>(+75.48%)</b></td><td>236.20 (+15.90%)</td><td>167.48 (+0.59%)</td><td>158.10 (-2.53%)</td><td>134.00 (-9.46%)</td><td>40.28 <b>(+85.59%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>166.50 (n/a)</td><td>162.20 (n/a)</td><td>148.00 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.18 (+0.29%)</td><td>0.18 (+0.08%)</td><td>0.18 (-0.04%)</td><td>0.18 (+0.19%)</td><td>0.00 <b>(+27.12%)</b></td><td>47412.60 (-0.19%)</td><td>47296.94 (-0.08%)</td><td>47395.60 (+0.04%)</td><td>46902.30 (-0.29%)</td><td>221.11 <b>(+26.58%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47502.00 (n/a)</td><td>47333.36 (n/a)</td><td>47376.40 (n/a)</td><td>47039.70 (n/a)</td><td>174.68 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (-6.76%)</td><td>0.05 (-5.65%)</td><td>0.05 (+0.94%)</td><td>0.04 (-5.84%)</td><td>0.00 (-18.15%)</td><td>206.80 (+6.21%)</td><td>183.28 (+5.80%)</td><td>179.00 (-0.94%)</td><td>164.40 (+7.31%)</td><td>17.54 (-4.69%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>173.24 (n/a)</td><td>180.70 (n/a)</td><td>153.20 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (-19.56%)</td><td>0.06 (-14.25%)</td><td>0.07 (-13.91%)</td><td>0.05 (-5.40%)</td><td>0.01 <b>(-41.48%)</b></td><td>233.20 (+5.71%)</td><td>193.10 (+14.87%)</td><td>189.00 (+16.16%)</td><td>165.10 <b>(+24.32%)</b></td><td>25.06 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>168.10 (n/a)</td><td>162.70 (n/a)</td><td>132.80 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(-22.53%)</b></td><td>0.04 (-18.03%)</td><td>0.04 <b>(-25.41%)</b></td><td>0.04 (-4.28%)</td><td>0.01 <b>(-35.89%)</b></td><td>222.40 (+4.46%)</td><td>191.64 <b>(+20.15%)</b></td><td>203.10 <b>(+34.06%)</b></td><td>154.80 <b>(+29.11%)</b></td><td>28.88 (-15.45%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>159.50 (n/a)</td><td>151.50 (n/a)</td><td>119.90 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (-14.55%)</td><td>0.06 (-3.66%)</td><td>0.06 (+4.21%)</td><td>0.05 (+6.13%)</td><td>0.01 <b>(-34.99%)</b></td><td>218.20 (-5.75%)</td><td>173.42 (+1.31%)</td><td>161.80 (-4.03%)</td><td>143.30 (+17.08%)</td><td>30.30 <b>(-27.70%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>171.18 (n/a)</td><td>168.60 (n/a)</td><td>122.40 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 <b>(-22.14%)</b></td><td>0.04 (-13.89%)</td><td>0.04 (-15.94%)</td><td>0.04 <b>(+33.02%)</b></td><td>0.00 <b>(-70.72%)</b></td><td>221.60 <b>(-24.83%)</b></td><td>198.84 (+8.97%)</td><td>190.60 (+18.98%)</td><td>183.10 <b>(+28.40%)</b></td><td>16.99 <b>(-73.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.80 (n/a)</td><td>182.48 (n/a)</td><td>160.20 (n/a)</td><td>142.60 (n/a)</td><td>63.28 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 <b>(-38.15%)</b></td><td>0.05 <b>(-24.17%)</b></td><td>0.05 (-15.49%)</td><td>0.05 (+11.98%)</td><td>0.01 <b>(-77.69%)</b></td><td>207.80 (-10.70%)</td><td>195.74 <b>(+21.73%)</b></td><td>200.90 (+18.32%)</td><td>165.90 <b>(+61.70%)</b></td><td>16.94 <b>(-67.41%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>160.80 (n/a)</td><td>169.80 (n/a)</td><td>102.60 (n/a)</td><td>51.99 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(-23.24%)</b></td><td>0.04 <b>(-21.37%)</b></td><td>0.04 (-19.88%)</td><td>0.03 <b>(-20.60%)</b></td><td>0.01 <b>(-34.55%)</b></td><td>247.20 <b>(+25.93%)</b></td><td>207.56 <b>(+26.38%)</b></td><td>205.70 <b>(+24.82%)</b></td><td>169.10 <b>(+30.28%)</b></td><td>27.91 (+6.83%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>164.24 (n/a)</td><td>164.80 (n/a)</td><td>129.80 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (+14.35%)</td><td>0.05 (+3.03%)</td><td>0.05 (+4.81%)</td><td>0.04 (-4.63%)</td><td>0.01 <b>(+85.00%)</b></td><td>217.20 (+4.88%)</td><td>182.34 (-1.13%)</td><td>177.40 (-4.62%)</td><td>137.40 (-12.54%)</td><td>32.34 <b>(+73.23%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>184.42 (n/a)</td><td>186.00 (n/a)</td><td>157.10 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 <b>(-20.65%)</b></td><td>0.05 (-5.39%)</td><td>0.05 (-5.90%)</td><td>0.04 (+6.17%)</td><td>0.00 <b>(-64.39%)</b></td><td>199.40 (-5.81%)</td><td>178.46 (+2.49%)</td><td>178.60 (+6.25%)</td><td>162.80 <b>(+26.01%)</b></td><td>14.71 <b>(-59.43%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>174.12 (n/a)</td><td>168.10 (n/a)</td><td>129.20 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.06 (-18.35%)</td><td>0.05 <b>(-23.68%)</b></td><td>0.05 <b>(-20.47%)</b></td><td>0.03 <b>(-46.92%)</b></td><td>0.01 <b>(+62.92%)</b></td><td>329.30 <b>(+88.39%)</b></td><td>215.88 <b>(+37.56%)</b></td><td>196.60 <b>(+25.78%)</b></td><td>162.50 <b>(+22.46%)</b></td><td>65.54 <b>(+297.97%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>156.94 (n/a)</td><td>156.30 (n/a)</td><td>132.70 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.07 (-2.63%)</td><td>0.04 (-12.57%)</td><td>0.04 <b>(-24.25%)</b></td><td>0.03 (-2.41%)</td><td>0.01 (+0.26%)</td><td>235.40 (+2.44%)</td><td>198.32 (+14.36%)</td><td>209.90 <b>(+32.01%)</b></td><td>125.50 (+2.70%)</td><td>42.33 (-1.66%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>173.42 (n/a)</td><td>159.00 (n/a)</td><td>122.20 (n/a)</td><td>43.04 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (-9.85%)</td><td>0.04 (-15.08%)</td><td>0.04 (-7.32%)</td><td>0.02 <b>(-37.41%)</b></td><td>0.01 <b>(+97.26%)</b></td><td>355.00 <b>(+59.77%)</b></td><td>234.92 <b>(+22.87%)</b></td><td>205.60 (+7.93%)</td><td>195.50 (+10.89%)</td><td>67.54 <b>(+261.01%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>191.20 (n/a)</td><td>190.50 (n/a)</td><td>176.30 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (-8.03%)</td><td>0.04 (-4.93%)</td><td>0.04 (-7.33%)</td><td>0.03 (+9.26%)</td><td>0.01 <b>(-31.25%)</b></td><td>243.60 (-8.46%)</td><td>197.46 (+2.94%)</td><td>187.10 (+7.90%)</td><td>161.00 (+8.71%)</td><td>31.41 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.10 (n/a)</td><td>191.82 (n/a)</td><td>173.40 (n/a)</td><td>148.10 (n/a)</td><td>46.39 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.05 (+2.40%)</td><td>0.04 (-11.36%)</td><td>0.04 (-19.57%)</td><td>0.04 (-7.20%)</td><td>0.01 <b>(+48.46%)</b></td><td>221.60 (+7.78%)</td><td>203.40 (+13.67%)</td><td>215.30 <b>(+24.38%)</b></td><td>163.90 (-2.32%)</td><td>24.57 <b>(+56.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>178.94 (n/a)</td><td>173.10 (n/a)</td><td>167.80 (n/a)</td><td>15.71 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.04 (-12.64%)</td><td>0.03 (-10.94%)</td><td>0.04 (-6.57%)</td><td>0.03 (-17.32%)</td><td>0.00 (-8.95%)</td><td>309.00 <b>(+20.94%)</b></td><td>252.78 (+12.48%)</td><td>233.80 (+7.05%)</td><td>218.30 (+14.47%)</td><td>36.61 <b>(+23.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>255.50 (n/a)</td><td>224.74 (n/a)</td><td>218.40 (n/a)</td><td>190.70 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.80 <b>(+24.27%)</b></td><td>0.68 <b>(+28.31%)</b></td><td>0.70 <b>(+31.66%)</b></td><td>0.55 <b>(+34.10%)</b></td><td>0.09 (-4.93%)</td><td>178.60 <b>(-25.43%)</b></td><td>147.18 <b>(-23.08%)</b></td><td>141.20 <b>(-24.05%)</b></td><td>122.90 (-19.52%)</td><td>21.31 <b>(-42.15%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.64 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.10 (n/a)</td><td>239.50 (n/a)</td><td>191.34 (n/a)</td><td>185.90 (n/a)</td><td>152.70 (n/a)</td><td>36.84 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.00 <b>(+34.81%)</b></td><td>0.68 (+9.69%)</td><td>0.61 (+0.62%)</td><td>0.55 (+19.56%)</td><td>0.18 <b>(+62.67%)</b></td><td>178.10 (-16.38%)</td><td>151.26 (-7.37%)</td><td>162.20 (-0.61%)</td><td>98.30 <b>(-25.81%)</b></td><td>30.80 (-3.51%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.11 (n/a)</td><td>213.00 (n/a)</td><td>163.30 (n/a)</td><td>163.20 (n/a)</td><td>132.50 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.68 (+11.85%)</td><td>0.54 (+9.37%)</td><td>0.53 (+5.05%)</td><td>0.43 <b>(+22.14%)</b></td><td>0.11 (-8.90%)</td><td>226.90 (-18.12%)</td><td>187.64 (-10.14%)</td><td>186.80 (-4.84%)</td><td>143.70 (-10.63%)</td><td>35.71 <b>(-30.82%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>277.10 (n/a)</td><td>208.82 (n/a)</td><td>196.30 (n/a)</td><td>160.80 (n/a)</td><td>51.62 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.58 (-11.27%)</td><td>0.51 (-4.23%)</td><td>0.48 (-17.83%)</td><td>0.47 <b>(+42.69%)</b></td><td>0.05 <b>(-64.06%)</b></td><td>210.70 <b>(-29.93%)</b></td><td>195.36 (-1.37%)</td><td>202.70 <b>(+21.67%)</b></td><td>168.60 (+12.70%)</td><td>17.17 <b>(-72.22%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.59 (n/a)</td><td>0.33 (n/a)</td><td>0.13 (n/a)</td><td>300.70 (n/a)</td><td>198.08 (n/a)</td><td>166.60 (n/a)</td><td>149.60 (n/a)</td><td>61.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.49 (-10.63%)</td><td>0.45 (+1.75%)</td><td>0.45 (+9.25%)</td><td>0.42 <b>(+24.26%)</b></td><td>0.03 <b>(-65.87%)</b></td><td>174.80 (-19.56%)</td><td>163.86 (-4.45%)</td><td>163.20 (-8.47%)</td><td>149.50 (+11.90%)</td><td>10.75 <b>(-68.37%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>217.30 (n/a)</td><td>171.50 (n/a)</td><td>178.30 (n/a)</td><td>133.60 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.55 (-2.52%)</td><td>0.43 (-13.02%)</td><td>0.44 (-10.31%)</td><td>0.29 <b>(-31.79%)</b></td><td>0.09 <b>(+90.40%)</b></td><td>250.70 <b>(+46.61%)</b></td><td>178.98 (+18.99%)</td><td>168.30 (+11.53%)</td><td>135.10 (+2.58%)</td><td>43.73 <b>(+195.42%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.56 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.05 (n/a)</td><td>171.00 (n/a)</td><td>150.42 (n/a)</td><td>150.90 (n/a)</td><td>131.70 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.67 (+14.23%)</td><td>0.45 (+3.78%)</td><td>0.42 (+14.01%)</td><td>0.30 (-2.63%)</td><td>0.14 (+13.25%)</td><td>247.80 (+2.69%)</td><td>176.94 (-2.98%)</td><td>177.00 (-12.29%)</td><td>110.60 (-12.43%)</td><td>48.74 (+1.60%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.12 (n/a)</td><td>241.30 (n/a)</td><td>182.38 (n/a)</td><td>201.80 (n/a)</td><td>126.30 (n/a)</td><td>47.98 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.45 (-11.52%)</td><td>0.41 (-2.15%)</td><td>0.41 (-1.58%)</td><td>0.35 <b>(+30.63%)</b></td><td>0.04 <b>(-60.18%)</b></td><td>210.50 <b>(-23.45%)</b></td><td>183.16 (-2.19%)</td><td>178.80 (+1.59%)</td><td>163.10 (+13.03%)</td><td>17.68 <b>(-66.02%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>275.00 (n/a)</td><td>187.26 (n/a)</td><td>176.00 (n/a)</td><td>144.30 (n/a)</td><td>52.02 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.09 (+6.76%)</td><td>0.82 (-7.37%)</td><td>0.80 (-10.64%)</td><td>0.69 (-9.90%)</td><td>0.16 <b>(+55.30%)</b></td><td>191.00 (+10.98%)</td><td>164.32 (+9.68%)</td><td>164.80 (+11.96%)</td><td>120.40 (-6.30%)</td><td>27.97 <b>(+58.87%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.76 (n/a)</td><td>0.10 (n/a)</td><td>172.10 (n/a)</td><td>149.82 (n/a)</td><td>147.20 (n/a)</td><td>128.50 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.92 (-10.62%)</td><td>0.78 (-17.50%)</td><td>0.79 (-15.38%)</td><td>0.58 <b>(-32.69%)</b></td><td>0.13 <b>(+96.80%)</b></td><td>227.60 <b>(+48.56%)</b></td><td>173.30 <b>(+23.75%)</b></td><td>166.50 (+18.17%)</td><td>142.20 (+11.88%)</td><td>32.34 <b>(+238.52%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.86 (n/a)</td><td>0.06 (n/a)</td><td>153.20 (n/a)</td><td>140.04 (n/a)</td><td>140.90 (n/a)</td><td>127.10 (n/a)</td><td>9.55 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.87 (-6.81%)</td><td>0.75 (-12.27%)</td><td>0.76 (-16.02%)</td><td>0.67 (-6.88%)</td><td>0.08 (-10.29%)</td><td>196.50 (+7.38%)</td><td>175.68 (+13.89%)</td><td>171.70 (+19.07%)</td><td>150.00 (+7.30%)</td><td>18.85 (+4.36%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.94 (n/a)</td><td>0.86 (n/a)</td><td>0.91 (n/a)</td><td>0.72 (n/a)</td><td>0.09 (n/a)</td><td>183.00 (n/a)</td><td>154.26 (n/a)</td><td>144.20 (n/a)</td><td>139.80 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.00 (+4.65%)</td><td>0.00 (-1.41%)</td><td>0.00 (-2.33%)</td><td>0.00 (-4.76%)</td><td>0.00 <b>(+241.57%)</b></td><td>1036.52 (+5.96%)</td><td>976.67 (+1.89%)</td><td>973.59 (+2.18%)</td><td>915.40 (-3.22%)</td><td>43.29 <b>(+193.25%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>978.24 (n/a)</td><td>958.55 (n/a)</td><td>952.80 (n/a)</td><td>945.83 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.01 (+3.66%)</td><td>0.01 (-0.25%)</td><td>0.01 (+0.00%)</td><td>0.01 (-5.13%)</td><td>0.00 <b>(+127.07%)</b></td><td>1106.70 (+5.88%)</td><td>1028.86 (+1.02%)</td><td>1025.44 (+0.58%)</td><td>968.13 (-2.63%)</td><td>51.41 <b>(+142.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1045.21 (n/a)</td><td>1018.48 (n/a)</td><td>1019.57 (n/a)</td><td>994.24 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>1.00 (+3.59%)</td><td>0.97 (+1.37%)</td><td>0.95 (-0.16%)</td><td>0.95 (-0.16%)</td><td>0.03 <b>(+248.46%)</b></td><td>2213.34 (+0.16%)</td><td>2164.03 (-1.31%)</td><td>2198.47 (+0.15%)</td><td>2093.50 (-3.47%)</td><td>56.41 <b>(+237.83%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2209.86 (n/a)</td><td>2192.65 (n/a)</td><td>2195.13 (n/a)</td><td>2168.81 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.40 (+0.90%)</td><td>0.38 (-1.54%)</td><td>0.39 (-1.10%)</td><td>0.37 (-3.70%)</td><td>0.01 <b>(+87.27%)</b></td><td>1426.89 (+3.83%)</td><td>1367.39 (+1.62%)</td><td>1359.52 (+1.10%)</td><td>1303.92 (-0.90%)</td><td>44.95 <b>(+92.33%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1374.32 (n/a)</td><td>1345.59 (n/a)</td><td>1344.77 (n/a)</td><td>1315.76 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.26 (-3.50%)</td><td>0.25 (-1.14%)</td><td>0.25 (+0.08%)</td><td>0.25 (-0.96%)</td><td>0.00 <b>(-42.16%)</b></td><td>2126.08 (+0.96%)</td><td>2076.92 (+1.12%)</td><td>2069.74 (-0.09%)</td><td>2044.18 (+3.63%)</td><td>30.63 <b>(-39.07%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2105.81 (n/a)</td><td>2054.01 (n/a)</td><td>2071.67 (n/a)</td><td>1972.63 (n/a)</td><td>50.27 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>0.37 (-1.02%)</td><td>0.36 (-2.04%)</td><td>0.36 (-3.39%)</td><td>0.36 (-2.30%)</td><td>0.01 <b>(+80.32%)</b></td><td>1468.74 (+2.37%)</td><td>1447.79 (+2.10%)</td><td>1462.24 (+3.54%)</td><td>1418.37 (+1.02%)</td><td>24.65 <b>(+87.35%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.00 (n/a)</td><td>1434.79 (n/a)</td><td>1418.00 (n/a)</td><td>1412.31 (n/a)</td><td>1404.09 (n/a)</td><td>13.16 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.24 (+8.69%)</td><td>3.05 <b>(+32.35%)</b></td><td>3.21 <b>(+41.52%)</b></td><td>2.39 <b>(+47.75%)</b></td><td>0.37 <b>(-29.25%)</b></td><td>219.00 <b>(-32.32%)</b></td><td>174.50 <b>(-26.61%)</b></td><td>163.30 <b>(-29.37%)</b></td><td>162.00 (-8.01%)</td><td>24.91 <b>(-55.92%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>2.98 (n/a)</td><td>2.30 (n/a)</td><td>2.27 (n/a)</td><td>1.62 (n/a)</td><td>0.52 (n/a)</td><td>323.60 (n/a)</td><td>237.76 (n/a)</td><td>231.20 (n/a)</td><td>176.10 (n/a)</td><td>56.52 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>5.93 <b>(+27.27%)</b></td><td>5.38 <b>(+21.97%)</b></td><td>5.55 <b>(+21.83%)</b></td><td>4.60 (+17.38%)</td><td>0.52 <b>(+70.27%)</b></td><td>228.00 (-14.80%)</td><td>196.52 (-17.69%)</td><td>188.80 (-17.95%)</td><td>176.90 <b>(-21.41%)</b></td><td>20.21 (+14.68%)</td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>4.66 (n/a)</td><td>4.41 (n/a)</td><td>4.56 (n/a)</td><td>3.92 (n/a)</td><td>0.31 (n/a)</td><td>267.60 (n/a)</td><td>238.76 (n/a)</td><td>230.10 (n/a)</td><td>225.10 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>aab8083</code> — 2026-08-25 22:38:08</td><td>3.43 <b>(+21.01%)</b></td><td>3.07 <b>(+22.41%)</b></td><td>2.98 (+14.93%)</td><td>2.73 <b>(+52.20%)</b></td><td>0.30 <b>(-26.56%)</b></td><td>191.70 <b>(-34.30%)</b></td><td>172.36 (-19.86%)</td><td>176.00 (-13.00%)</td><td>152.80 (-17.36%)</td><td>16.71 <b>(-61.72%)</b></td>
</tr>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:28:31</td><td>2.84 (n/a)</td><td>2.50 (n/a)</td><td>2.59 (n/a)</td><td>1.80 (n/a)</td><td>0.41 (n/a)</td><td>291.80 (n/a)</td><td>215.08 (n/a)</td><td>202.30 (n/a)</td><td>184.90 (n/a)</td><td>43.64 (n/a)</td>
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
