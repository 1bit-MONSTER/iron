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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (+3.09%)</td><td>0.08 (+12.06%)</td><td>0.08 (+14.78%)</td><td>0.07 (+7.03%)</td><td>0.01 (-11.68%)</td><td>180.50 (-6.53%)</td><td>157.86 (-11.09%)</td><td>160.30 (-12.88%)</td><td>135.70 (-3.00%)</td><td>17.51 (-18.45%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>177.56 (n/a)</td><td>184.00 (n/a)</td><td>139.90 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 <b>(-21.19%)</b></td><td>0.06 (-14.40%)</td><td>0.07 (-10.33%)</td><td>0.05 (-19.49%)</td><td>0.01 (-17.33%)</td><td>226.80 <b>(+24.21%)</b></td><td>193.38 (+16.94%)</td><td>185.70 (+11.53%)</td><td>170.70 <b>(+26.91%)</b></td><td>24.95 <b>(+29.88%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>165.36 (n/a)</td><td>166.50 (n/a)</td><td>134.50 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.10 <b>(+44.65%)</b></td><td>0.07 (+10.87%)</td><td>0.07 (+6.81%)</td><td>0.05 (-10.70%)</td><td>0.02 <b>(+216.44%)</b></td><td>244.30 (+11.96%)</td><td>174.60 (-5.51%)</td><td>166.20 (-6.37%)</td><td>119.10 <b>(-30.88%)</b></td><td>45.86 <b>(+142.10%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>184.78 (n/a)</td><td>177.50 (n/a)</td><td>172.30 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 <b>(+22.77%)</b></td><td>0.06 (+13.91%)</td><td>0.06 (+12.15%)</td><td>0.05 <b>(+27.41%)</b></td><td>0.02 <b>(+21.47%)</b></td><td>266.10 <b>(-21.50%)</b></td><td>203.70 (-12.71%)</td><td>196.70 (-10.83%)</td><td>140.70 (-18.53%)</td><td>45.32 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>339.00 (n/a)</td><td>233.36 (n/a)</td><td>220.60 (n/a)</td><td>172.70 (n/a)</td><td>62.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (+13.96%)</td><td>0.04 (+18.83%)</td><td>0.04 <b>(+29.35%)</b></td><td>0.03 (+13.86%)</td><td>0.01 (+16.61%)</td><td>172.00 (-12.20%)</td><td>143.84 (-15.70%)</td><td>136.60 <b>(-22.65%)</b></td><td>113.90 (-12.25%)</td><td>23.74 (-6.66%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>170.62 (n/a)</td><td>176.60 (n/a)</td><td>129.80 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 <b>(+37.92%)</b></td><td>0.04 <b>(+27.30%)</b></td><td>0.03 (+16.82%)</td><td>0.03 <b>(+31.77%)</b></td><td>0.01 <b>(+56.45%)</b></td><td>162.40 <b>(-24.15%)</b></td><td>142.02 <b>(-20.64%)</b></td><td>153.80 (-14.41%)</td><td>94.10 <b>(-27.50%)</b></td><td>28.23 (-14.92%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>178.96 (n/a)</td><td>179.70 (n/a)</td><td>129.80 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (+14.51%)</td><td>0.04 <b>(+32.13%)</b></td><td>0.03 <b>(+21.88%)</b></td><td>0.03 <b>(+110.34%)</b></td><td>0.01 <b>(-33.67%)</b></td><td>161.50 <b>(-52.46%)</b></td><td>142.72 <b>(-30.07%)</b></td><td>150.60 (-17.97%)</td><td>117.60 (-12.69%)</td><td>21.10 <b>(-73.62%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>339.70 (n/a)</td><td>204.10 (n/a)</td><td>183.60 (n/a)</td><td>134.70 (n/a)</td><td>79.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (+4.04%)</td><td>0.03 (+0.55%)</td><td>0.03 (-1.17%)</td><td>0.03 (+9.80%)</td><td>0.01 (+2.56%)</td><td>204.30 (-8.92%)</td><td>174.86 (-0.79%)</td><td>180.10 (+1.24%)</td><td>128.30 (-3.90%)</td><td>28.68 (-12.66%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>176.26 (n/a)</td><td>177.90 (n/a)</td><td>133.50 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (-8.38%)</td><td>0.03 (-14.61%)</td><td>0.03 <b>(-21.14%)</b></td><td>0.02 (-15.44%)</td><td>0.01 (-18.17%)</td><td>237.70 (+18.26%)</td><td>186.10 (+16.44%)</td><td>176.90 <b>(+26.81%)</b></td><td>141.10 (+9.13%)</td><td>36.54 (+4.47%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>159.82 (n/a)</td><td>139.50 (n/a)</td><td>129.30 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.03 (-11.83%)</td><td>0.03 (+5.29%)</td><td>0.03 (+9.36%)</td><td>0.03 (+18.45%)</td><td>0.00 <b>(-63.54%)</b></td><td>202.80 (-15.57%)</td><td>190.88 (-6.73%)</td><td>187.90 (-8.56%)</td><td>178.20 (+13.43%)</td><td>11.32 <b>(-64.14%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.20 (n/a)</td><td>204.66 (n/a)</td><td>205.50 (n/a)</td><td>157.10 (n/a)</td><td>31.58 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 <b>(+31.09%)</b></td><td>0.03 (+6.67%)</td><td>0.03 (-1.91%)</td><td>0.03 (+10.20%)</td><td>0.01 <b>(+104.57%)</b></td><td>202.20 (-9.25%)</td><td>175.62 (-3.52%)</td><td>182.80 (+1.95%)</td><td>114.20 <b>(-23.71%)</b></td><td>36.12 <b>(+37.35%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>182.02 (n/a)</td><td>179.30 (n/a)</td><td>149.70 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.02 (-13.50%)</td><td>0.02 (-5.86%)</td><td>0.02 (-4.21%)</td><td>0.02 (-1.72%)</td><td>0.00 <b>(-56.99%)</b></td><td>243.10 (+1.76%)</td><td>227.68 (+5.62%)</td><td>223.80 (+4.38%)</td><td>217.10 (+15.60%)</td><td>10.26 <b>(-49.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.90 (n/a)</td><td>215.56 (n/a)</td><td>214.40 (n/a)</td><td>187.80 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>181.28 (n/a)</td><td>166.10 (n/a)</td><td>145.10 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>167.14 (n/a)</td><td>155.10 (n/a)</td><td>128.10 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>193.82 (n/a)</td><td>183.80 (n/a)</td><td>174.20 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>162.96 (n/a)</td><td>161.70 (n/a)</td><td>134.20 (n/a)</td><td>20.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>168.28 (n/a)</td><td>155.70 (n/a)</td><td>143.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>190.70 (n/a)</td><td>182.00 (n/a)</td><td>187.10 (n/a)</td><td>169.70 (n/a)</td><td>10.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>223.20 (n/a)</td><td>183.88 (n/a)</td><td>187.60 (n/a)</td><td>120.80 (n/a)</td><td>41.22 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>189.46 (n/a)</td><td>187.30 (n/a)</td><td>163.40 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>155.46 (n/a)</td><td>156.10 (n/a)</td><td>128.90 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>164.26 (n/a)</td><td>166.90 (n/a)</td><td>122.00 (n/a)</td><td>35.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>166.38 (n/a)</td><td>168.80 (n/a)</td><td>139.80 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>174.36 (n/a)</td><td>164.20 (n/a)</td><td>129.30 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.40 (n/a)</td><td>149.66 (n/a)</td><td>152.00 (n/a)</td><td>133.50 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.70 (n/a)</td><td>162.56 (n/a)</td><td>174.00 (n/a)</td><td>118.30 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>176.82 (n/a)</td><td>185.50 (n/a)</td><td>147.40 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.30 (n/a)</td><td>224.76 (n/a)</td><td>232.50 (n/a)</td><td>167.40 (n/a)</td><td>55.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>4.13 (-8.16%)</td><td>4.07 (-2.16%)</td><td>4.08 (-0.47%)</td><td>3.96 (+1.86%)</td><td>0.07 <b>(-69.27%)</b></td><td>2377.60 (-1.83%)</td><td>2310.12 (+1.99%)</td><td>2302.60 (+0.47%)</td><td>2278.70 (+8.89%)</td><td>39.66 <b>(-66.96%)</b></td><td>1623.43 (-8.16%)</td><td>1601.73 (-2.16%)</td><td>1606.61 (-0.47%)</td><td>1555.90 (+1.86%)</td><td>27.02 <b>(-69.27%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.49 (n/a)</td><td>4.16 (n/a)</td><td>4.10 (n/a)</td><td>3.88 (n/a)</td><td>0.22 (n/a)</td><td>2421.90 (n/a)</td><td>2264.96 (n/a)</td><td>2291.90 (n/a)</td><td>2092.70 (n/a)</td><td>120.03 (n/a)</td><td>1767.72 (n/a)</td><td>1637.02 (n/a)</td><td>1614.12 (n/a)</td><td>1527.45 (n/a)</td><td>87.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>1.34 (+18.52%)</td><td>0.95 (+16.54%)</td><td>0.99 <b>(+48.15%)</b></td><td>0.68 (+12.84%)</td><td>0.27 (+3.56%)</td><td>324.80 (-11.38%)</td><td>247.96 (-15.38%)</td><td>222.60 <b>(-32.50%)</b></td><td>164.50 (-15.60%)</td><td>66.55 <b>(-20.68%)</b></td><td>57.38 (+18.52%)</td><td>40.46 (+16.54%)</td><td>42.39 <b>(+48.15%)</b></td><td>29.06 (+12.84%)</td><td>11.39 (+3.56%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.13 (n/a)</td><td>0.81 (n/a)</td><td>0.67 (n/a)</td><td>0.60 (n/a)</td><td>0.26 (n/a)</td><td>366.50 (n/a)</td><td>293.04 (n/a)</td><td>329.80 (n/a)</td><td>194.90 (n/a)</td><td>83.90 (n/a)</td><td>48.41 (n/a)</td><td>34.71 (n/a)</td><td>28.62 (n/a)</td><td>25.75 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>1.37 <b>(+21.05%)</b></td><td>1.07 (+19.76%)</td><td>1.19 <b>(+30.76%)</b></td><td>0.61 (+5.98%)</td><td>0.29 <b>(+35.12%)</b></td><td>365.00 (-5.64%)</td><td>224.18 (-14.37%)</td><td>185.20 <b>(-23.53%)</b></td><td>162.00 (-17.39%)</td><td>82.13 (+8.16%)</td><td>58.25 <b>(+21.05%)</b></td><td>45.71 (+19.76%)</td><td>50.96 <b>(+30.76%)</b></td><td>25.86 (+5.98%)</td><td>12.57 <b>(+35.12%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.13 (n/a)</td><td>0.89 (n/a)</td><td>0.91 (n/a)</td><td>0.57 (n/a)</td><td>0.22 (n/a)</td><td>386.80 (n/a)</td><td>261.80 (n/a)</td><td>242.20 (n/a)</td><td>196.10 (n/a)</td><td>75.94 (n/a)</td><td>48.12 (n/a)</td><td>38.16 (n/a)</td><td>38.97 (n/a)</td><td>24.40 (n/a)</td><td>9.30 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 (+0.12%)</td><td>0.52 (+0.32%)</td><td>0.52 (+0.28%)</td><td>0.52 (+0.50%)</td><td>0.00 <b>(-82.96%)</b></td><td>48648.30 (-0.50%)</td><td>48629.88 (-0.32%)</td><td>48619.90 (-0.28%)</td><td>48613.70 (-0.12%)</td><td>16.82 <b>(-83.09%)</b></td><td>353.40 (+0.12%)</td><td>353.28 (+0.32%)</td><td>353.35 (+0.28%)</td><td>353.14 (+0.50%)</td><td>0.12 <b>(-82.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48892.60 (n/a)</td><td>48787.46 (n/a)</td><td>48757.60 (n/a)</td><td>48673.40 (n/a)</td><td>99.46 (n/a)</td><td>352.96 (n/a)</td><td>352.14 (n/a)</td><td>352.35 (n/a)</td><td>351.38 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.89 (+1.31%)</td><td>0.88 (+0.56%)</td><td>0.88 (+0.24%)</td><td>0.87 (+0.06%)</td><td>0.01 <b>(+184.02%)</b></td><td>28803.80 (-0.06%)</td><td>28539.90 (-0.56%)</td><td>28597.40 (-0.24%)</td><td>28260.10 (-1.30%)</td><td>210.60 <b>(+179.92%)</b></td><td>607.92 (+1.31%)</td><td>601.99 (+0.56%)</td><td>600.75 (+0.24%)</td><td>596.44 (+0.06%)</td><td>4.45 <b>(+184.03%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.00 (n/a)</td><td>28819.90 (n/a)</td><td>28699.84 (n/a)</td><td>28666.20 (n/a)</td><td>28631.40 (n/a)</td><td>75.24 (n/a)</td><td>600.04 (n/a)</td><td>598.61 (n/a)</td><td>599.31 (n/a)</td><td>596.11 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.32 (+0.99%)</td><td>3.22 (+0.33%)</td><td>3.19 (+0.09%)</td><td>3.11 (-2.26%)</td><td>0.09 <b>(+105.20%)</b></td><td>8094.50 (+2.31%)</td><td>7813.80 (-0.27%)</td><td>7883.70 (-0.09%)</td><td>7572.10 (-0.98%)</td><td>225.26 <b>(+107.00%)</b></td><td>2268.84 (+0.99%)</td><td>2200.13 (+0.33%)</td><td>2179.17 (+0.09%)</td><td>2122.40 (-2.26%)</td><td>63.50 <b>(+105.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>3.29 (n/a)</td><td>3.21 (n/a)</td><td>3.19 (n/a)</td><td>3.18 (n/a)</td><td>0.05 (n/a)</td><td>7911.60 (n/a)</td><td>7835.22 (n/a)</td><td>7890.80 (n/a)</td><td>7647.30 (n/a)</td><td>108.82 (n/a)</td><td>2246.52 (n/a)</td><td>2192.99 (n/a)</td><td>2177.21 (n/a)</td><td>2171.47 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.93 (-4.77%)</td><td>3.44 (-0.93%)</td><td>3.55 (+2.09%)</td><td>3.03 (+2.55%)</td><td>0.38 <b>(-21.15%)</b></td><td>2663.00 (-2.49%)</td><td>2365.70 (+0.38%)</td><td>2271.00 (-2.05%)</td><td>2052.50 (+5.00%)</td><td>266.26 (-18.59%)</td><td>1029.92 (-4.77%)</td><td>902.64 (-0.93%)</td><td>930.82 (+2.09%)</td><td>793.82 (+2.55%)</td><td>100.92 <b>(-21.15%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.12 (n/a)</td><td>3.47 (n/a)</td><td>3.48 (n/a)</td><td>2.95 (n/a)</td><td>0.49 (n/a)</td><td>2730.90 (n/a)</td><td>2356.86 (n/a)</td><td>2318.50 (n/a)</td><td>1954.70 (n/a)</td><td>327.04 (n/a)</td><td>1081.47 (n/a)</td><td>911.08 (n/a)</td><td>911.77 (n/a)</td><td>774.07 (n/a)</td><td>127.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 <b>(+50.92%)</b></td><td>0.41 <b>(+32.10%)</b></td><td>0.37 (+16.84%)</td><td>0.32 <b>(+21.85%)</b></td><td>0.09 <b>(+224.94%)</b></td><td>3854.10 (-17.94%)</td><td>3181.74 <b>(-21.76%)</b></td><td>3396.30 (-14.41%)</td><td>2408.60 <b>(-33.74%)</b></td><td>687.47 <b>(+72.56%)</b></td><td>27.86 <b>(+50.92%)</b></td><td>21.96 <b>(+32.10%)</b></td><td>19.76 (+16.84%)</td><td>17.41 <b>(+21.85%)</b></td><td>5.03 <b>(+224.94%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>4696.40 (n/a)</td><td>4066.64 (n/a)</td><td>3968.20 (n/a)</td><td>3635.10 (n/a)</td><td>398.40 (n/a)</td><td>18.46 (n/a)</td><td>16.62 (n/a)</td><td>16.91 (n/a)</td><td>14.29 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>6.10 <b>(+27.26%)</b></td><td>4.58 (+8.47%)</td><td>4.84 (+5.81%)</td><td>3.32 (-3.75%)</td><td>1.11 <b>(+73.86%)</b></td><td>2003.30 (+3.89%)</td><td>1524.52 (-5.17%)</td><td>1373.10 (-5.49%)</td><td>1090.50 <b>(-21.42%)</b></td><td>372.16 <b>(+44.76%)</b></td><td>1884.65 <b>(+27.26%)</b></td><td>1414.00 (+8.47%)</td><td>1496.77 (+5.81%)</td><td>1025.91 (-3.75%)</td><td>342.56 <b>(+73.86%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.79 (n/a)</td><td>4.22 (n/a)</td><td>4.58 (n/a)</td><td>3.45 (n/a)</td><td>0.64 (n/a)</td><td>1928.20 (n/a)</td><td>1607.70 (n/a)</td><td>1452.90 (n/a)</td><td>1387.80 (n/a)</td><td>257.09 (n/a)</td><td>1480.95 (n/a)</td><td>1303.54 (n/a)</td><td>1414.57 (n/a)</td><td>1065.85 (n/a)</td><td>197.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.23 (-10.03%)</td><td>0.21 (-4.78%)</td><td>0.20 (-12.99%)</td><td>0.20 <b>(+35.32%)</b></td><td>0.02 <b>(-62.55%)</b></td><td>0.23 (-10.03%)</td><td>0.20 (-4.78%)</td><td>0.19 (-12.99%)</td><td>0.19 <b>(+35.32%)</b></td><td>0.02 <b>(-62.55%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>13.32 (-0.98%)</td><td>12.79 (+1.70%)</td><td>13.26 (+1.70%)</td><td>10.86 (-0.36%)</td><td>1.08 (+4.22%)</td><td>13.31 (-0.98%)</td><td>12.78 (+1.70%)</td><td>13.25 (+1.70%)</td><td>10.86 (-0.36%)</td><td>1.07 (+4.22%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>13.45 (n/a)</td><td>12.57 (n/a)</td><td>13.03 (n/a)</td><td>10.90 (n/a)</td><td>1.03 (n/a)</td><td>13.44 (n/a)</td><td>12.56 (n/a)</td><td>13.03 (n/a)</td><td>10.90 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>25.35 (+2.23%)</td><td>24.68 (+5.05%)</td><td>24.54 (+1.75%)</td><td>24.22 (+18.55%)</td><td>0.49 <b>(-71.96%)</b></td><td>25.33 (+2.23%)</td><td>24.66 (+5.05%)</td><td>24.52 (+1.75%)</td><td>24.20 (+18.55%)</td><td>0.49 <b>(-71.96%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>24.80 (n/a)</td><td>23.49 (n/a)</td><td>24.12 (n/a)</td><td>20.43 (n/a)</td><td>1.74 (n/a)</td><td>24.78 (n/a)</td><td>23.48 (n/a)</td><td>24.10 (n/a)</td><td>20.42 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>44.44 (+8.76%)</td><td>41.00 (+4.10%)</td><td>41.27 (+4.78%)</td><td>36.98 (-2.34%)</td><td>2.77 <b>(+159.26%)</b></td><td>44.42 (+8.76%)</td><td>40.98 (+4.10%)</td><td>41.24 (+4.78%)</td><td>36.96 (-2.34%)</td><td>2.77 <b>(+159.26%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>40.87 (n/a)</td><td>39.39 (n/a)</td><td>39.38 (n/a)</td><td>37.87 (n/a)</td><td>1.07 (n/a)</td><td>40.84 (n/a)</td><td>39.36 (n/a)</td><td>39.36 (n/a)</td><td>37.84 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>45.57 (+1.43%)</td><td>43.49 (+1.11%)</td><td>42.87 (+0.84%)</td><td>42.67 (+1.76%)</td><td>1.23 (+6.38%)</td><td>45.54 (+1.43%)</td><td>43.46 (+1.11%)</td><td>42.85 (+0.84%)</td><td>42.64 (+1.76%)</td><td>1.23 (+6.38%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>44.93 (n/a)</td><td>43.01 (n/a)</td><td>42.52 (n/a)</td><td>41.93 (n/a)</td><td>1.16 (n/a)</td><td>44.90 (n/a)</td><td>42.99 (n/a)</td><td>42.49 (n/a)</td><td>41.91 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>13.30 (-0.21%)</td><td>12.73 (+0.40%)</td><td>13.22 (+0.05%)</td><td>11.88 (+6.09%)</td><td>0.72 <b>(-20.42%)</b></td><td>13.29 (-0.21%)</td><td>12.72 (+0.40%)</td><td>13.21 (+0.05%)</td><td>11.87 (+6.09%)</td><td>0.72 <b>(-20.42%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>13.33 (n/a)</td><td>12.67 (n/a)</td><td>13.21 (n/a)</td><td>11.20 (n/a)</td><td>0.90 (n/a)</td><td>13.32 (n/a)</td><td>12.67 (n/a)</td><td>13.21 (n/a)</td><td>11.19 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>25.17 (+0.90%)</td><td>24.77 (+1.82%)</td><td>24.77 (+2.50%)</td><td>24.21 (+0.91%)</td><td>0.38 (+1.89%)</td><td>25.16 (+0.90%)</td><td>24.75 (+1.82%)</td><td>24.76 (+2.50%)</td><td>24.20 (+0.91%)</td><td>0.38 (+1.89%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>24.95 (n/a)</td><td>24.33 (n/a)</td><td>24.17 (n/a)</td><td>23.99 (n/a)</td><td>0.37 (n/a)</td><td>24.93 (n/a)</td><td>24.31 (n/a)</td><td>24.15 (n/a)</td><td>23.98 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>41.39 (+0.91%)</td><td>39.88 (+0.44%)</td><td>39.82 (-1.92%)</td><td>38.22 (+2.46%)</td><td>1.38 (-15.33%)</td><td>41.36 (+0.91%)</td><td>39.85 (+0.44%)</td><td>39.79 (-1.92%)</td><td>38.20 (+2.46%)</td><td>1.38 (-15.33%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>41.01 (n/a)</td><td>39.70 (n/a)</td><td>40.60 (n/a)</td><td>37.30 (n/a)</td><td>1.63 (n/a)</td><td>40.99 (n/a)</td><td>39.68 (n/a)</td><td>40.58 (n/a)</td><td>37.28 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>42.64 (-4.56%)</td><td>42.22 (-1.03%)</td><td>42.39 (+0.22%)</td><td>41.43 (+0.74%)</td><td>0.47 <b>(-67.74%)</b></td><td>42.62 (-4.56%)</td><td>42.19 (-1.03%)</td><td>42.37 (+0.22%)</td><td>41.41 (+0.74%)</td><td>0.47 <b>(-67.74%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>44.68 (n/a)</td><td>42.66 (n/a)</td><td>42.30 (n/a)</td><td>41.13 (n/a)</td><td>1.45 (n/a)</td><td>44.65 (n/a)</td><td>42.63 (n/a)</td><td>42.28 (n/a)</td><td>41.10 (n/a)</td><td>1.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>398.00 (n/a)</td><td>195.76 (n/a)</td><td>156.60 (n/a)</td><td>124.00 (n/a)</td><td>114.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>154.64 (n/a)</td><td>167.90 (n/a)</td><td>114.10 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>168.28 (n/a)</td><td>161.90 (n/a)</td><td>134.70 (n/a)</td><td>24.89 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.50 (n/a)</td><td>155.18 (n/a)</td><td>159.90 (n/a)</td><td>126.40 (n/a)</td><td>16.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>173.34 (n/a)</td><td>180.20 (n/a)</td><td>130.70 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.80 (n/a)</td><td>202.80 (n/a)</td><td>185.50 (n/a)</td><td>171.40 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.60 (n/a)</td><td>186.72 (n/a)</td><td>184.20 (n/a)</td><td>175.00 (n/a)</td><td>14.14 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>208.40 (n/a)</td><td>207.60 (n/a)</td><td>201.00 (n/a)</td><td>7.29 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>384.60 (n/a)</td><td>216.56 (n/a)</td><td>188.90 (n/a)</td><td>143.50 (n/a)</td><td>96.03 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>170.14 (n/a)</td><td>171.70 (n/a)</td><td>143.50 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>183.10 (n/a)</td><td>184.10 (n/a)</td><td>120.20 (n/a)</td><td>43.79 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.20 (n/a)</td><td>175.92 (n/a)</td><td>168.20 (n/a)</td><td>129.90 (n/a)</td><td>42.76 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>159.76 (n/a)</td><td>160.80 (n/a)</td><td>131.10 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>172.38 (n/a)</td><td>172.10 (n/a)</td><td>147.80 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>179.72 (n/a)</td><td>182.90 (n/a)</td><td>146.90 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>187.36 (n/a)</td><td>190.40 (n/a)</td><td>166.10 (n/a)</td><td>13.25 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>192.98 (n/a)</td><td>193.80 (n/a)</td><td>115.20 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>205.98 (n/a)</td><td>206.30 (n/a)</td><td>169.30 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (-5.63%)</td><td>0.05 (-8.75%)</td><td>0.05 (-4.45%)</td><td>0.04 (-15.52%)</td><td>0.01 (+5.46%)</td><td>209.00 (+18.41%)</td><td>164.68 (+10.49%)</td><td>159.90 (+4.65%)</td><td>126.50 (+6.04%)</td><td>31.33 <b>(+33.24%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>149.04 (n/a)</td><td>152.80 (n/a)</td><td>119.30 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 <b>(-20.11%)</b></td><td>0.04 (+0.65%)</td><td>0.04 (+8.75%)</td><td>0.04 (+7.85%)</td><td>0.00 <b>(-70.69%)</b></td><td>204.50 (-7.26%)</td><td>192.64 (-3.38%)</td><td>195.10 (-8.06%)</td><td>173.40 <b>(+25.20%)</b></td><td>11.83 <b>(-65.75%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>199.38 (n/a)</td><td>212.20 (n/a)</td><td>138.50 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (-1.08%)</td><td>0.05 (-3.45%)</td><td>0.05 (-8.04%)</td><td>0.04 (+17.78%)</td><td>0.01 <b>(-27.01%)</b></td><td>198.30 (-15.11%)</td><td>167.72 (+1.53%)</td><td>163.90 (+8.76%)</td><td>138.00 (+1.10%)</td><td>23.58 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>165.20 (n/a)</td><td>150.70 (n/a)</td><td>136.50 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 <b>(+36.69%)</b></td><td>0.05 <b>(+30.67%)</b></td><td>0.05 (+19.54%)</td><td>0.05 <b>(+95.83%)</b></td><td>0.01 (-6.27%)</td><td>178.20 <b>(-48.94%)</b></td><td>159.54 <b>(-27.15%)</b></td><td>168.00 (-16.33%)</td><td>117.50 <b>(-26.84%)</b></td><td>24.08 <b>(-67.87%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>349.00 (n/a)</td><td>219.00 (n/a)</td><td>200.80 (n/a)</td><td>160.60 (n/a)</td><td>74.97 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (+6.00%)</td><td>0.05 (-3.63%)</td><td>0.05 (+4.60%)</td><td>0.02 <b>(-51.53%)</b></td><td>0.02 <b>(+194.20%)</b></td><td>387.60 <b>(+106.39%)</b></td><td>199.52 (+18.82%)</td><td>161.80 (-4.43%)</td><td>140.60 (-5.64%)</td><td>105.69 <b>(+504.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>167.92 (n/a)</td><td>169.30 (n/a)</td><td>149.00 (n/a)</td><td>17.49 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (-2.32%)</td><td>0.05 (-1.85%)</td><td>0.05 (-9.86%)</td><td>0.05 (+4.98%)</td><td>0.01 <b>(-26.50%)</b></td><td>163.50 (-4.78%)</td><td>152.86 (+1.22%)</td><td>160.10 (+10.95%)</td><td>130.80 (+2.35%)</td><td>13.44 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>151.02 (n/a)</td><td>144.30 (n/a)</td><td>127.80 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (+12.41%)</td><td>0.05 (+2.22%)</td><td>0.05 (-2.77%)</td><td>0.04 (-4.00%)</td><td>0.01 <b>(+84.80%)</b></td><td>216.60 (+4.18%)</td><td>175.80 (-0.07%)</td><td>177.20 (+2.84%)</td><td>135.20 (-11.05%)</td><td>34.20 <b>(+68.78%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>175.92 (n/a)</td><td>172.30 (n/a)</td><td>152.00 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (+12.07%)</td><td>0.05 (-7.63%)</td><td>0.04 (-14.53%)</td><td>0.03 <b>(-30.17%)</b></td><td>0.01 <b>(+117.41%)</b></td><td>278.80 <b>(+43.19%)</b></td><td>192.62 (+14.18%)</td><td>187.80 (+17.01%)</td><td>134.80 (-10.73%)</td><td>56.50 <b>(+178.64%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>168.70 (n/a)</td><td>160.50 (n/a)</td><td>151.00 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (+3.20%)</td><td>0.05 (-11.66%)</td><td>0.04 (-18.23%)</td><td>0.04 (-7.19%)</td><td>0.01 <b>(+26.58%)</b></td><td>220.90 (+7.70%)</td><td>182.94 (+14.84%)</td><td>191.50 <b>(+22.29%)</b></td><td>125.80 (-3.08%)</td><td>36.66 <b>(+27.03%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>159.30 (n/a)</td><td>156.60 (n/a)</td><td>129.80 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.09 (+7.96%)</td><td>0.07 (+1.14%)</td><td>0.07 (-1.52%)</td><td>0.06 (-2.66%)</td><td>0.01 <b>(+36.12%)</b></td><td>212.60 (+2.71%)</td><td>174.12 (-0.35%)</td><td>176.80 (+1.55%)</td><td>140.30 (-7.33%)</td><td>26.34 <b>(+27.80%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>174.74 (n/a)</td><td>174.10 (n/a)</td><td>151.40 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (+14.01%)</td><td>0.05 (+2.32%)</td><td>0.04 (-5.69%)</td><td>0.04 (-14.18%)</td><td>0.01 <b>(+112.72%)</b></td><td>224.90 (+16.53%)</td><td>173.94 (+1.71%)</td><td>188.30 (+6.02%)</td><td>125.60 (-12.23%)</td><td>42.65 <b>(+111.34%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>171.02 (n/a)</td><td>177.60 (n/a)</td><td>143.10 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 <b>(-20.16%)</b></td><td>0.05 (-19.44%)</td><td>0.05 <b>(-21.48%)</b></td><td>0.04 (-9.72%)</td><td>0.01 <b>(-36.13%)</b></td><td>242.70 (+10.77%)</td><td>206.40 <b>(+22.93%)</b></td><td>203.90 <b>(+27.36%)</b></td><td>180.90 <b>(+25.28%)</b></td><td>25.41 (-14.48%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>167.90 (n/a)</td><td>160.10 (n/a)</td><td>144.40 (n/a)</td><td>29.72 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (+18.44%)</td><td>0.05 (+0.83%)</td><td>0.05 (-1.55%)</td><td>0.04 (-3.30%)</td><td>0.01 <b>(+60.15%)</b></td><td>186.50 (+3.44%)</td><td>155.98 (+0.74%)</td><td>161.30 (+1.57%)</td><td>113.80 (-15.58%)</td><td>27.57 <b>(+40.29%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>154.84 (n/a)</td><td>158.80 (n/a)</td><td>134.80 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (-0.16%)</td><td>0.06 (+11.20%)</td><td>0.07 <b>(+21.37%)</b></td><td>0.03 <b>(-23.72%)</b></td><td>0.02 <b>(+35.25%)</b></td><td>356.40 <b>(+31.08%)</b></td><td>195.96 (-4.12%)</td><td>157.20 (-17.61%)</td><td>150.50 (+0.13%)</td><td>89.79 <b>(+81.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>271.90 (n/a)</td><td>204.38 (n/a)</td><td>190.80 (n/a)</td><td>150.30 (n/a)</td><td>49.60 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 <b>(+31.72%)</b></td><td>0.05 (+11.65%)</td><td>0.05 (+5.44%)</td><td>0.04 (+0.68%)</td><td>0.01 <b>(+136.12%)</b></td><td>219.30 (-0.68%)</td><td>178.06 (-8.60%)</td><td>177.80 (-5.17%)</td><td>135.40 <b>(-24.10%)</b></td><td>31.96 <b>(+77.41%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.80 (n/a)</td><td>194.82 (n/a)</td><td>187.50 (n/a)</td><td>178.40 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.07 (+16.19%)</td><td>0.05 (-1.88%)</td><td>0.05 (-8.75%)</td><td>0.04 (-3.03%)</td><td>0.01 <b>(+45.74%)</b></td><td>229.30 (+3.10%)</td><td>182.32 (+3.66%)</td><td>186.50 (+9.58%)</td><td>126.10 (-13.92%)</td><td>37.38 <b>(+24.22%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>175.88 (n/a)</td><td>170.20 (n/a)</td><td>146.50 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 <b>(+28.94%)</b></td><td>0.04 (-1.24%)</td><td>0.04 (-9.58%)</td><td>0.04 (-14.38%)</td><td>0.01 <b>(+393.66%)</b></td><td>224.50 (+16.81%)</td><td>191.12 (+4.94%)</td><td>203.50 (+10.60%)</td><td>131.60 <b>(-22.45%)</b></td><td>37.51 <b>(+343.44%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>182.12 (n/a)</td><td>184.00 (n/a)</td><td>169.70 (n/a)</td><td>8.46 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.06 (-10.30%)</td><td>0.05 (-6.57%)</td><td>0.05 (-4.96%)</td><td>0.04 (+1.76%)</td><td>0.01 <b>(-24.47%)</b></td><td>208.00 (-1.75%)</td><td>179.20 (+6.07%)</td><td>178.80 (+5.24%)</td><td>145.80 (+11.47%)</td><td>24.50 (-16.99%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>168.94 (n/a)</td><td>169.90 (n/a)</td><td>130.80 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (-8.24%)</td><td>0.04 (-2.58%)</td><td>0.04 (+0.03%)</td><td>0.04 (-0.56%)</td><td>0.01 <b>(-25.60%)</b></td><td>233.20 (+0.56%)</td><td>191.30 (+1.27%)</td><td>189.60 (+0.00%)</td><td>155.90 (+8.94%)</td><td>30.82 (-19.26%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>188.90 (n/a)</td><td>189.60 (n/a)</td><td>143.10 (n/a)</td><td>38.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (-9.40%)</td><td>0.04 (+4.54%)</td><td>0.04 (+12.34%)</td><td>0.04 <b>(+20.51%)</b></td><td>0.00 <b>(-67.22%)</b></td><td>221.60 (-17.03%)</td><td>203.88 (-6.90%)</td><td>203.00 (-11.00%)</td><td>189.90 (+10.41%)</td><td>12.72 <b>(-69.47%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>267.10 (n/a)</td><td>219.00 (n/a)</td><td>228.10 (n/a)</td><td>172.00 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (-7.67%)</td><td>0.04 (-0.77%)</td><td>0.04 (+2.82%)</td><td>0.04 (+14.80%)</td><td>0.00 <b>(-61.57%)</b></td><td>198.90 (-12.88%)</td><td>187.74 (-0.73%)</td><td>188.30 (-2.74%)</td><td>172.10 (+8.31%)</td><td>10.43 <b>(-63.11%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>189.12 (n/a)</td><td>193.60 (n/a)</td><td>158.90 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (+5.55%)</td><td>0.05 (+8.87%)</td><td>0.05 <b>(+22.91%)</b></td><td>0.04 (+1.21%)</td><td>0.01 (+15.24%)</td><td>223.80 (-1.19%)</td><td>188.02 (-7.90%)</td><td>175.30 (-18.62%)</td><td>164.70 (-5.24%)</td><td>25.27 (+7.90%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>204.14 (n/a)</td><td>215.40 (n/a)</td><td>173.80 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.05 (-10.53%)</td><td>0.04 (+3.84%)</td><td>0.04 (+1.50%)</td><td>0.03 (+6.34%)</td><td>0.01 <b>(-32.46%)</b></td><td>248.00 (-5.95%)</td><td>201.40 (-5.29%)</td><td>203.60 (-1.45%)</td><td>171.90 (+11.77%)</td><td>29.78 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.70 (n/a)</td><td>212.66 (n/a)</td><td>206.60 (n/a)</td><td>153.80 (n/a)</td><td>41.38 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.73 (+3.51%)</td><td>0.64 (+14.91%)</td><td>0.67 <b>(+25.77%)</b></td><td>0.55 <b>(+29.38%)</b></td><td>0.08 (-18.24%)</td><td>178.70 <b>(-22.71%)</b></td><td>155.80 (-14.07%)</td><td>146.60 <b>(-20.46%)</b></td><td>135.00 (-3.36%)</td><td>20.95 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.10 (n/a)</td><td>231.20 (n/a)</td><td>181.32 (n/a)</td><td>184.30 (n/a)</td><td>139.70 (n/a)</td><td>33.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.66 (-8.12%)</td><td>0.59 (-7.64%)</td><td>0.58 (-6.27%)</td><td>0.50 (-17.07%)</td><td>0.07 <b>(+44.32%)</b></td><td>195.90 <b>(+20.55%)</b></td><td>168.28 (+8.95%)</td><td>169.20 (+6.68%)</td><td>150.00 (+8.85%)</td><td>19.31 <b>(+84.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.60 (n/a)</td><td>0.05 (n/a)</td><td>162.50 (n/a)</td><td>154.46 (n/a)</td><td>158.60 (n/a)</td><td>137.80 (n/a)</td><td>10.45 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.76 (+17.75%)</td><td>0.60 (-1.32%)</td><td>0.56 (-8.76%)</td><td>0.51 (-8.32%)</td><td>0.10 <b>(+196.51%)</b></td><td>193.60 (+9.07%)</td><td>167.16 (+3.06%)</td><td>176.50 (+9.63%)</td><td>130.20 (-15.07%)</td><td>24.62 <b>(+167.85%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.64 (n/a)</td><td>0.61 (n/a)</td><td>0.61 (n/a)</td><td>0.55 (n/a)</td><td>0.03 (n/a)</td><td>177.50 (n/a)</td><td>162.20 (n/a)</td><td>161.00 (n/a)</td><td>153.30 (n/a)</td><td>9.19 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.62 (-8.44%)</td><td>0.53 (-8.46%)</td><td>0.52 (-6.98%)</td><td>0.48 (-10.81%)</td><td>0.05 (-0.29%)</td><td>204.20 (+12.14%)</td><td>186.92 (+9.43%)</td><td>189.50 (+7.55%)</td><td>159.80 (+9.23%)</td><td>18.02 <b>(+23.10%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.05 (n/a)</td><td>182.10 (n/a)</td><td>170.82 (n/a)</td><td>176.20 (n/a)</td><td>146.30 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.48 (-9.28%)</td><td>0.41 (-6.18%)</td><td>0.41 (-0.41%)</td><td>0.37 (-9.72%)</td><td>0.04 (-19.36%)</td><td>200.80 (+10.76%)</td><td>179.62 (+6.36%)</td><td>178.80 (+0.39%)</td><td>154.40 (+10.21%)</td><td>17.09 (-2.52%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.05 (n/a)</td><td>181.30 (n/a)</td><td>168.88 (n/a)</td><td>178.10 (n/a)</td><td>140.10 (n/a)</td><td>17.53 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.52 (+1.16%)</td><td>0.46 (+5.38%)</td><td>0.45 (+2.64%)</td><td>0.44 <b>(+20.38%)</b></td><td>0.03 <b>(-42.79%)</b></td><td>168.00 (-16.91%)</td><td>160.46 (-6.01%)</td><td>164.00 (-2.55%)</td><td>143.00 (-1.17%)</td><td>10.26 <b>(-53.33%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>202.20 (n/a)</td><td>170.72 (n/a)</td><td>168.30 (n/a)</td><td>144.70 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.55 (-7.51%)</td><td>0.45 (+17.38%)</td><td>0.44 (+19.85%)</td><td>0.35 <b>(+72.99%)</b></td><td>0.07 <b>(-49.15%)</b></td><td>212.70 <b>(-42.19%)</b></td><td>169.16 <b>(-22.93%)</b></td><td>167.30 (-16.56%)</td><td>134.40 (+8.13%)</td><td>28.28 <b>(-68.79%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.59 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>367.90 (n/a)</td><td>219.50 (n/a)</td><td>200.50 (n/a)</td><td>124.30 (n/a)</td><td>90.62 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.53 <b>(+24.17%)</b></td><td>0.41 (+3.19%)</td><td>0.41 (-0.17%)</td><td>0.33 (-4.54%)</td><td>0.07 <b>(+154.38%)</b></td><td>220.50 (+4.75%)</td><td>184.58 (-1.25%)</td><td>181.00 (+0.17%)</td><td>140.20 (-19.47%)</td><td>30.16 <b>(+109.51%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>186.92 (n/a)</td><td>180.70 (n/a)</td><td>174.10 (n/a)</td><td>14.39 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.84 (-16.68%)</td><td>0.75 (-5.33%)</td><td>0.75 (-1.17%)</td><td>0.63 (-11.02%)</td><td>0.08 <b>(-35.19%)</b></td><td>208.70 (+12.39%)</td><td>177.50 (+4.86%)</td><td>175.20 (+1.15%)</td><td>156.20 (+19.97%)</td><td>20.33 (-10.94%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>1.01 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.13 (n/a)</td><td>185.70 (n/a)</td><td>169.28 (n/a)</td><td>173.20 (n/a)</td><td>130.20 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.95 (-1.04%)</td><td>0.74 (+6.26%)</td><td>0.70 (+7.19%)</td><td>0.55 (-3.12%)</td><td>0.17 (+9.69%)</td><td>239.20 (+3.24%)</td><td>185.72 (-5.02%)</td><td>186.00 (-6.67%)</td><td>138.60 (+1.09%)</td><td>42.43 (+16.13%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.15 (n/a)</td><td>231.70 (n/a)</td><td>195.54 (n/a)</td><td>199.30 (n/a)</td><td>137.10 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.74 (-10.34%)</td><td>0.63 (-4.50%)</td><td>0.61 (-15.70%)</td><td>0.50 <b>(+42.08%)</b></td><td>0.09 <b>(-51.12%)</b></td><td>262.00 <b>(-29.63%)</b></td><td>210.52 (-3.28%)</td><td>214.30 (+18.59%)</td><td>177.00 (+11.53%)</td><td>33.43 <b>(-62.52%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.83 (n/a)</td><td>0.66 (n/a)</td><td>0.73 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>372.30 (n/a)</td><td>217.66 (n/a)</td><td>180.70 (n/a)</td><td>158.70 (n/a)</td><td>89.21 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.00 (+0.00%)</td><td>0.00 (+0.96%)</td><td>0.00 (+2.38%)</td><td>0.00 (-5.00%)</td><td>0.00 <b>(+96.12%)</b></td><td>1079.03 (+4.35%)</td><td>978.73 (-0.95%)</td><td>952.71 (-1.75%)</td><td>950.43 (-1.01%)</td><td>56.23 <b>(+79.46%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1034.03 (n/a)</td><td>988.07 (n/a)</td><td>969.71 (n/a)</td><td>960.13 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.01 (-1.20%)</td><td>0.01 (+0.50%)</td><td>0.01 (+1.25%)</td><td>0.01 (+2.67%)</td><td>0.00 <b>(-28.91%)</b></td><td>1063.48 (-2.72%)</td><td>1025.53 (-0.75%)</td><td>1013.10 (-0.86%)</td><td>997.32 (+0.64%)</td><td>27.23 <b>(-31.20%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1093.23 (n/a)</td><td>1033.26 (n/a)</td><td>1021.84 (n/a)</td><td>990.94 (n/a)</td><td>39.57 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>0.95 (-0.18%)</td><td>0.95 (+0.34%)</td><td>0.95 (+0.38%)</td><td>0.95 (+0.53%)</td><td>0.00 <b>(-53.23%)</b></td><td>2216.53 (-0.54%)</td><td>2207.36 (-0.34%)</td><td>2205.81 (-0.38%)</td><td>2202.82 (+0.17%)</td><td>5.64 <b>(-53.64%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2228.51 (n/a)</td><td>2214.97 (n/a)</td><td>2214.31 (n/a)</td><td>2199.00 (n/a)</td><td>12.17 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.06 (-2.97%)</td><td>2.77 (+1.48%)</td><td>2.65 (+2.44%)</td><td>2.58 (+13.66%)</td><td>0.22 <b>(-41.69%)</b></td><td>203.20 (-12.03%)</td><td>189.98 (-2.46%)</td><td>197.70 (-2.37%)</td><td>171.30 (+3.07%)</td><td>14.48 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>3.15 (n/a)</td><td>2.73 (n/a)</td><td>2.59 (n/a)</td><td>2.27 (n/a)</td><td>0.37 (n/a)</td><td>231.00 (n/a)</td><td>194.78 (n/a)</td><td>202.50 (n/a)</td><td>166.20 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>6.24 <b>(+32.82%)</b></td><td>4.51 (-0.14%)</td><td>4.30 (-4.79%)</td><td>3.63 (-14.04%)</td><td>1.01 <b>(+414.20%)</b></td><td>288.80 (+16.31%)</td><td>240.64 (+3.41%)</td><td>243.70 (+5.00%)</td><td>168.10 <b>(-24.72%)</b></td><td>45.00 <b>(+334.21%)</b></td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>4.70 (n/a)</td><td>4.51 (n/a)</td><td>4.52 (n/a)</td><td>4.22 (n/a)</td><td>0.20 (n/a)</td><td>248.30 (n/a)</td><td>232.70 (n/a)</td><td>232.10 (n/a)</td><td>223.30 (n/a)</td><td>10.36 (n/a)</td>
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
<td><code>17769b8</code> — 2026-07-09 23:01:35</td><td>3.01 (+13.75%)</td><td>2.55 (+3.94%)</td><td>2.47 (-2.56%)</td><td>2.24 (+9.69%)</td><td>0.29 (+19.37%)</td><td>233.80 (-8.85%)</td><td>208.04 (-3.70%)</td><td>212.10 (+2.66%)</td><td>173.90 (-12.13%)</td><td>22.60 (-6.05%)</td>
</tr>
<tr>
<td><code>c9bc036</code> — 2026-07-09 21:31:18</td><td>2.65 (n/a)</td><td>2.45 (n/a)</td><td>2.54 (n/a)</td><td>2.04 (n/a)</td><td>0.25 (n/a)</td><td>256.50 (n/a)</td><td>216.04 (n/a)</td><td>206.60 (n/a)</td><td>197.90 (n/a)</td><td>24.06 (n/a)</td>
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
