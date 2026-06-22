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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 <b>(+25.71%)</b></td><td>0.09 <b>(+20.06%)</b></td><td>0.09 <b>(+20.21%)</b></td><td>0.07 (+16.47%)</td><td>0.01 <b>(+40.13%)</b></td><td>171.00 (-14.11%)</td><td>144.24 (-16.38%)</td><td>139.10 (-16.86%)</td><td>118.80 <b>(-20.48%)</b></td><td>20.37 (-4.10%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>172.50 (n/a)</td><td>167.30 (n/a)</td><td>149.40 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (-9.04%)</td><td>0.08 (+8.62%)</td><td>0.08 <b>(+21.19%)</b></td><td>0.06 (+14.76%)</td><td>0.01 <b>(-36.99%)</b></td><td>208.40 (-12.88%)</td><td>165.20 (-10.61%)</td><td>157.20 (-17.48%)</td><td>141.60 (+9.94%)</td><td>26.89 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>239.20 (n/a)</td><td>184.80 (n/a)</td><td>190.50 (n/a)</td><td>128.80 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 <b>(+56.98%)</b></td><td>0.08 <b>(+24.53%)</b></td><td>0.07 (+17.47%)</td><td>0.05 (+14.29%)</td><td>0.02 <b>(+168.13%)</b></td><td>230.20 (-12.50%)</td><td>173.58 (-15.97%)</td><td>166.00 (-14.87%)</td><td>117.50 <b>(-36.31%)</b></td><td>47.20 <b>(+47.79%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>263.10 (n/a)</td><td>206.56 (n/a)</td><td>195.00 (n/a)</td><td>184.50 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (+3.16%)</td><td>0.06 (-15.01%)</td><td>0.05 (-19.13%)</td><td>0.04 <b>(-24.65%)</b></td><td>0.01 <b>(+72.17%)</b></td><td>293.70 <b>(+32.72%)</b></td><td>223.06 <b>(+21.74%)</b></td><td>225.40 <b>(+23.71%)</b></td><td>149.90 (-3.10%)</td><td>51.74 <b>(+112.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>183.22 (n/a)</td><td>182.20 (n/a)</td><td>154.70 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (+4.04%)</td><td>0.03 (-2.51%)</td><td>0.03 (-12.37%)</td><td>0.03 (-0.96%)</td><td>0.01 (+3.12%)</td><td>196.00 (+0.93%)</td><td>167.52 (+2.48%)</td><td>172.60 (+14.08%)</td><td>125.40 (-3.83%)</td><td>26.23 (-6.75%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>163.46 (n/a)</td><td>151.30 (n/a)</td><td>130.40 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 <b>(+27.43%)</b></td><td>0.04 (+14.11%)</td><td>0.03 (+4.75%)</td><td>0.02 (-17.62%)</td><td>0.01 <b>(+137.34%)</b></td><td>233.80 <b>(+21.39%)</b></td><td>159.08 (-6.61%)</td><td>168.90 (-4.52%)</td><td>110.50 <b>(-21.52%)</b></td><td>51.06 <b>(+109.72%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.60 (n/a)</td><td>170.34 (n/a)</td><td>176.90 (n/a)</td><td>140.80 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (-2.29%)</td><td>0.04 (+5.73%)</td><td>0.03 (+0.11%)</td><td>0.03 (+5.36%)</td><td>0.01 (-7.77%)</td><td>184.80 (-5.08%)</td><td>152.10 (-6.10%)</td><td>162.30 (-0.06%)</td><td>118.90 (+2.32%)</td><td>28.47 (-14.04%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>161.98 (n/a)</td><td>162.40 (n/a)</td><td>116.20 (n/a)</td><td>33.12 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (+10.23%)</td><td>0.03 (+7.89%)</td><td>0.03 (+9.08%)</td><td>0.02 (-7.60%)</td><td>0.01 <b>(+50.08%)</b></td><td>227.50 (+8.23%)</td><td>176.84 (-5.90%)</td><td>177.40 (-8.32%)</td><td>138.90 (-9.27%)</td><td>33.75 <b>(+48.48%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>187.92 (n/a)</td><td>193.50 (n/a)</td><td>153.10 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 <b>(+22.72%)</b></td><td>0.04 <b>(+27.03%)</b></td><td>0.04 <b>(+33.87%)</b></td><td>0.03 <b>(+29.62%)</b></td><td>0.01 (+5.78%)</td><td>174.80 <b>(-22.86%)</b></td><td>143.24 <b>(-21.85%)</b></td><td>133.20 <b>(-25.29%)</b></td><td>119.70 (-18.52%)</td><td>21.99 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>183.28 (n/a)</td><td>178.30 (n/a)</td><td>146.90 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.03 (-2.83%)</td><td>0.03 (+10.70%)</td><td>0.03 <b>(+26.87%)</b></td><td>0.02 (-2.19%)</td><td>0.00 (+3.46%)</td><td>212.40 (+2.21%)</td><td>173.12 (-9.48%)</td><td>158.90 <b>(-21.18%)</b></td><td>150.30 (+2.87%)</td><td>28.03 (+9.09%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>191.24 (n/a)</td><td>201.60 (n/a)</td><td>146.10 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (+14.78%)</td><td>0.03 (-2.74%)</td><td>0.03 (-17.33%)</td><td>0.02 (-7.54%)</td><td>0.01 <b>(+58.55%)</b></td><td>222.30 (+8.12%)</td><td>184.88 (+5.67%)</td><td>195.40 <b>(+20.99%)</b></td><td>123.60 (-12.90%)</td><td>42.28 <b>(+46.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>174.96 (n/a)</td><td>161.50 (n/a)</td><td>141.90 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.03 (+2.46%)</td><td>0.03 (+1.77%)</td><td>0.03 (+3.30%)</td><td>0.02 (-10.05%)</td><td>0.00 <b>(+54.94%)</b></td><td>259.40 (+11.14%)</td><td>209.18 (-0.76%)</td><td>206.60 (-3.23%)</td><td>179.00 (-2.40%)</td><td>31.06 <b>(+72.10%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.40 (n/a)</td><td>210.78 (n/a)</td><td>213.50 (n/a)</td><td>183.40 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>163.70 (n/a)</td><td>154.30 (n/a)</td><td>133.70 (n/a)</td><td>40.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.80 (n/a)</td><td>147.40 (n/a)</td><td>152.90 (n/a)</td><td>115.00 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>161.84 (n/a)</td><td>156.80 (n/a)</td><td>136.50 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>194.70 (n/a)</td><td>186.20 (n/a)</td><td>163.80 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>173.90 (n/a)</td><td>176.10 (n/a)</td><td>144.10 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>241.20 (n/a)</td><td>173.24 (n/a)</td><td>176.90 (n/a)</td><td>110.40 (n/a)</td><td>47.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>181.26 (n/a)</td><td>180.80 (n/a)</td><td>143.40 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>315.80 (n/a)</td><td>228.98 (n/a)</td><td>222.60 (n/a)</td><td>141.80 (n/a)</td><td>78.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>179.32 (n/a)</td><td>195.90 (n/a)</td><td>112.50 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.20 (n/a)</td><td>183.18 (n/a)</td><td>176.10 (n/a)</td><td>154.50 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>178.30 (n/a)</td><td>173.10 (n/a)</td><td>161.70 (n/a)</td><td>16.80 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>159.06 (n/a)</td><td>154.20 (n/a)</td><td>130.50 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>171.48 (n/a)</td><td>175.10 (n/a)</td><td>142.30 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.70 (n/a)</td><td>227.94 (n/a)</td><td>211.90 (n/a)</td><td>178.50 (n/a)</td><td>57.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.20 (n/a)</td><td>194.26 (n/a)</td><td>188.70 (n/a)</td><td>170.40 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>211.38 (n/a)</td><td>213.70 (n/a)</td><td>195.60 (n/a)</td><td>15.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.99 (-2.80%)</td><td>4.24 (-8.61%)</td><td>4.04 (-11.92%)</td><td>3.96 (-4.91%)</td><td>0.43 (+4.85%)</td><td>2371.90 (+5.16%)</td><td>2232.02 (+9.54%)</td><td>2326.50 (+13.54%)</td><td>1884.20 (+2.88%)</td><td>200.51 (+12.65%)</td><td>1963.40 (-2.80%)</td><td>1669.47 (-8.61%)</td><td>1590.09 (-11.92%)</td><td>1559.66 (-4.91%)</td><td>167.85 (+4.85%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>5.13 (n/a)</td><td>4.64 (n/a)</td><td>4.59 (n/a)</td><td>4.17 (n/a)</td><td>0.41 (n/a)</td><td>2255.50 (n/a)</td><td>2037.64 (n/a)</td><td>2049.10 (n/a)</td><td>1831.50 (n/a)</td><td>177.99 (n/a)</td><td>2019.91 (n/a)</td><td>1826.68 (n/a)</td><td>1805.34 (n/a)</td><td>1640.13 (n/a)</td><td>160.08 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.55 <b>(+25.34%)</b></td><td>0.93 (-17.07%)</td><td>0.77 <b>(-33.36%)</b></td><td>0.64 <b>(-26.69%)</b></td><td>0.38 <b>(+161.38%)</b></td><td>343.50 <b>(+36.42%)</b></td><td>264.76 <b>(+32.13%)</b></td><td>287.10 <b>(+50.00%)</b></td><td>142.30 <b>(-20.19%)</b></td><td>84.51 <b>(+182.59%)</b></td><td>66.33 <b>(+25.34%)</b></td><td>39.67 (-17.07%)</td><td>32.87 <b>(-33.36%)</b></td><td>27.47 <b>(-26.69%)</b></td><td>16.19 <b>(+161.38%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>1.24 (n/a)</td><td>1.12 (n/a)</td><td>1.16 (n/a)</td><td>0.88 (n/a)</td><td>0.15 (n/a)</td><td>251.80 (n/a)</td><td>200.38 (n/a)</td><td>191.40 (n/a)</td><td>178.30 (n/a)</td><td>29.91 (n/a)</td><td>52.92 (n/a)</td><td>47.83 (n/a)</td><td>49.32 (n/a)</td><td>37.47 (n/a)</td><td>6.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.99 <b>(-30.92%)</b></td><td>0.83 <b>(-30.69%)</b></td><td>0.87 <b>(-29.85%)</b></td><td>0.66 (-19.69%)</td><td>0.13 <b>(-48.59%)</b></td><td>333.80 <b>(+24.51%)</b></td><td>270.16 <b>(+41.36%)</b></td><td>253.10 <b>(+42.59%)</b></td><td>223.40 <b>(+44.78%)</b></td><td>43.20 (-6.83%)</td><td>42.24 <b>(-30.92%)</b></td><td>35.62 <b>(-30.69%)</b></td><td>37.28 <b>(-29.85%)</b></td><td>28.27 (-19.69%)</td><td>5.41 <b>(-48.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>1.43 (n/a)</td><td>1.20 (n/a)</td><td>1.25 (n/a)</td><td>0.82 (n/a)</td><td>0.25 (n/a)</td><td>268.10 (n/a)</td><td>191.12 (n/a)</td><td>177.50 (n/a)</td><td>154.30 (n/a)</td><td>46.37 (n/a)</td><td>61.16 (n/a)</td><td>51.39 (n/a)</td><td>53.15 (n/a)</td><td>35.20 (n/a)</td><td>10.52 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.52 (+1.01%)</td><td>0.52 (+0.49%)</td><td>0.52 (+0.37%)</td><td>0.52 (+0.38%)</td><td>0.00 <b>(+421.45%)</b></td><td>48670.60 (-0.38%)</td><td>48570.74 (-0.49%)</td><td>48627.00 (-0.37%)</td><td>48274.70 (-1.00%)</td><td>166.79 <b>(+413.80%)</b></td><td>355.88 (+1.01%)</td><td>353.71 (+0.49%)</td><td>353.30 (+0.37%)</td><td>352.98 (+0.38%)</td><td>1.22 <b>(+421.49%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48854.90 (n/a)</td><td>48807.76 (n/a)</td><td>48807.50 (n/a)</td><td>48763.20 (n/a)</td><td>32.46 (n/a)</td><td>352.31 (n/a)</td><td>351.99 (n/a)</td><td>351.99 (n/a)</td><td>351.65 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.89 (-0.63%)</td><td>0.88 (+0.09%)</td><td>0.88 (-0.18%)</td><td>0.87 (+0.29%)</td><td>0.01 <b>(-32.10%)</b></td><td>28932.90 (-0.29%)</td><td>28586.36 (-0.10%)</td><td>28600.70 (+0.18%)</td><td>28274.00 (+0.63%)</td><td>244.64 <b>(-31.87%)</b></td><td>607.62 (-0.63%)</td><td>601.02 (+0.09%)</td><td>600.68 (-0.18%)</td><td>593.78 (+0.29%)</td><td>5.14 <b>(-32.09%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>29017.60 (n/a)</td><td>28613.74 (n/a)</td><td>28550.40 (n/a)</td><td>28096.10 (n/a)</td><td>359.06 (n/a)</td><td>611.47 (n/a)</td><td>600.48 (n/a)</td><td>601.74 (n/a)</td><td>592.05 (n/a)</td><td>7.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.27 (-2.67%)</td><td>3.16 (-2.38%)</td><td>3.16 (-0.77%)</td><td>3.08 (-2.72%)</td><td>0.07 <b>(-24.31%)</b></td><td>8158.20 (+2.80%)</td><td>7954.42 (+2.41%)</td><td>7966.10 (+0.77%)</td><td>7689.80 (+2.74%)</td><td>169.99 <b>(-20.53%)</b></td><td>2234.13 (-2.67%)</td><td>2160.59 (-2.38%)</td><td>2156.62 (-0.77%)</td><td>2105.84 (-2.72%)</td><td>46.71 <b>(-24.31%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>3.36 (n/a)</td><td>3.24 (n/a)</td><td>3.18 (n/a)</td><td>3.17 (n/a)</td><td>0.09 (n/a)</td><td>7936.30 (n/a)</td><td>7767.18 (n/a)</td><td>7905.10 (n/a)</td><td>7484.70 (n/a)</td><td>213.91 (n/a)</td><td>2295.35 (n/a)</td><td>2213.21 (n/a)</td><td>2173.25 (n/a)</td><td>2164.71 (n/a)</td><td>61.71 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.35 (+1.76%)</td><td>3.79 (-7.03%)</td><td>3.70 (-11.79%)</td><td>3.18 (-11.18%)</td><td>0.47 <b>(+62.98%)</b></td><td>2538.80 (+12.59%)</td><td>2151.30 (+8.45%)</td><td>2177.10 (+13.37%)</td><td>1854.30 (-1.73%)</td><td>272.71 <b>(+77.20%)</b></td><td>1140.03 (+1.76%)</td><td>995.10 (-7.03%)</td><td>970.97 (-11.79%)</td><td>832.66 (-11.18%)</td><td>123.51 <b>(+62.98%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>4.27 (n/a)</td><td>4.08 (n/a)</td><td>4.20 (n/a)</td><td>3.57 (n/a)</td><td>0.29 (n/a)</td><td>2255.00 (n/a)</td><td>1983.64 (n/a)</td><td>1920.40 (n/a)</td><td>1887.00 (n/a)</td><td>153.89 (n/a)</td><td>1120.28 (n/a)</td><td>1070.40 (n/a)</td><td>1100.77 (n/a)</td><td>937.46 (n/a)</td><td>75.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.36 <b>(-31.23%)</b></td><td>0.32 (-12.08%)</td><td>0.33 (-2.51%)</td><td>0.27 (-9.52%)</td><td>0.03 <b>(-64.03%)</b></td><td>4573.70 (+10.52%)</td><td>3972.46 (+10.36%)</td><td>3824.60 (+2.57%)</td><td>3505.50 <b>(+45.42%)</b></td><td>416.07 <b>(-39.98%)</b></td><td>19.14 <b>(-31.23%)</b></td><td>17.04 (-12.08%)</td><td>17.55 (-2.51%)</td><td>14.67 (-9.52%)</td><td>1.73 <b>(-64.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.52 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>4138.30 (n/a)</td><td>3599.66 (n/a)</td><td>3728.60 (n/a)</td><td>2410.60 (n/a)</td><td>693.24 (n/a)</td><td>27.84 (n/a)</td><td>19.38 (n/a)</td><td>18.00 (n/a)</td><td>16.22 (n/a)</td><td>4.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>6.57 (-0.02%)</td><td>4.58 (-9.64%)</td><td>4.48 (-8.74%)</td><td>3.58 (-4.84%)</td><td>1.21 (+17.47%)</td><td>1857.80 (+5.08%)</td><td>1523.60 (+12.31%)</td><td>1484.60 (+9.58%)</td><td>1012.60 (+0.02%)</td><td>341.54 <b>(+23.63%)</b></td><td>2029.68 (-0.02%)</td><td>1414.56 (-9.64%)</td><td>1384.37 (-8.74%)</td><td>1106.25 (-4.84%)</td><td>372.43 (+17.47%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>6.57 (n/a)</td><td>5.07 (n/a)</td><td>4.91 (n/a)</td><td>3.76 (n/a)</td><td>1.03 (n/a)</td><td>1768.00 (n/a)</td><td>1356.64 (n/a)</td><td>1354.80 (n/a)</td><td>1012.40 (n/a)</td><td>276.26 (n/a)</td><td>2030.00 (n/a)</td><td>1565.55 (n/a)</td><td>1517.00 (n/a)</td><td>1162.48 (n/a)</td><td>317.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.21 (-4.69%)</td><td>0.19 (-0.22%)</td><td>0.20 (+0.58%)</td><td>0.15 (+9.71%)</td><td>0.02 <b>(-28.34%)</b></td><td>0.21 (-4.69%)</td><td>0.19 (-0.22%)</td><td>0.20 (+0.58%)</td><td>0.15 (+9.71%)</td><td>0.02 <b>(-28.34%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>13.40 (+2.07%)</td><td>13.23 (+3.95%)</td><td>13.22 (+3.70%)</td><td>13.06 (+7.13%)</td><td>0.14 <b>(-60.55%)</b></td><td>13.39 (+2.07%)</td><td>13.22 (+3.95%)</td><td>13.21 (+3.70%)</td><td>13.05 (+7.13%)</td><td>0.14 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>13.13 (n/a)</td><td>12.73 (n/a)</td><td>12.75 (n/a)</td><td>12.19 (n/a)</td><td>0.35 (n/a)</td><td>13.12 (n/a)</td><td>12.72 (n/a)</td><td>12.74 (n/a)</td><td>12.18 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>25.34 (-0.25%)</td><td>24.94 (+2.17%)</td><td>25.00 (+2.15%)</td><td>24.45 (+4.23%)</td><td>0.37 <b>(-47.65%)</b></td><td>25.33 (-0.25%)</td><td>24.92 (+2.17%)</td><td>24.98 (+2.15%)</td><td>24.43 (+4.23%)</td><td>0.37 <b>(-47.65%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>25.41 (n/a)</td><td>24.41 (n/a)</td><td>24.47 (n/a)</td><td>23.46 (n/a)</td><td>0.70 (n/a)</td><td>25.39 (n/a)</td><td>24.39 (n/a)</td><td>24.46 (n/a)</td><td>23.44 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>44.73 (+10.22%)</td><td>41.67 (+5.09%)</td><td>41.73 (+5.49%)</td><td>38.99 (+1.05%)</td><td>2.06 <b>(+165.79%)</b></td><td>44.70 (+10.22%)</td><td>41.65 (+5.09%)</td><td>41.71 (+5.49%)</td><td>38.96 (+1.05%)</td><td>2.06 <b>(+165.79%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>40.58 (n/a)</td><td>39.65 (n/a)</td><td>39.56 (n/a)</td><td>38.58 (n/a)</td><td>0.77 (n/a)</td><td>40.56 (n/a)</td><td>39.63 (n/a)</td><td>39.54 (n/a)</td><td>38.56 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>44.41 (+0.08%)</td><td>42.73 (-1.74%)</td><td>42.73 (-1.69%)</td><td>40.44 (-5.35%)</td><td>1.49 <b>(+154.05%)</b></td><td>44.38 (+0.08%)</td><td>42.70 (-1.74%)</td><td>42.71 (-1.69%)</td><td>40.41 (-5.35%)</td><td>1.49 <b>(+154.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>44.37 (n/a)</td><td>43.48 (n/a)</td><td>43.47 (n/a)</td><td>42.72 (n/a)</td><td>0.59 (n/a)</td><td>44.34 (n/a)</td><td>43.46 (n/a)</td><td>43.44 (n/a)</td><td>42.70 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>13.29 (-1.03%)</td><td>13.01 (+2.86%)</td><td>13.24 (+0.70%)</td><td>12.15 (+12.54%)</td><td>0.48 <b>(-54.81%)</b></td><td>13.28 (-1.03%)</td><td>13.00 (+2.86%)</td><td>13.23 (+0.70%)</td><td>12.14 (+12.54%)</td><td>0.48 <b>(-54.81%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>13.43 (n/a)</td><td>12.65 (n/a)</td><td>13.15 (n/a)</td><td>10.80 (n/a)</td><td>1.07 (n/a)</td><td>13.42 (n/a)</td><td>12.64 (n/a)</td><td>13.14 (n/a)</td><td>10.79 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>24.73 (+1.16%)</td><td>24.37 (+1.87%)</td><td>24.32 (+0.90%)</td><td>24.16 (+5.57%)</td><td>0.23 <b>(-64.23%)</b></td><td>24.71 (+1.16%)</td><td>24.35 (+1.87%)</td><td>24.30 (+0.90%)</td><td>24.15 (+5.57%)</td><td>0.23 <b>(-64.23%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>24.44 (n/a)</td><td>23.92 (n/a)</td><td>24.10 (n/a)</td><td>22.89 (n/a)</td><td>0.64 (n/a)</td><td>24.43 (n/a)</td><td>23.90 (n/a)</td><td>24.09 (n/a)</td><td>22.87 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>42.49 (+3.43%)</td><td>40.41 (+2.03%)</td><td>39.80 (-0.70%)</td><td>38.87 (+3.58%)</td><td>1.42 (-9.95%)</td><td>42.47 (+3.43%)</td><td>40.39 (+2.03%)</td><td>39.77 (-0.70%)</td><td>38.85 (+3.58%)</td><td>1.42 (-9.95%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>41.09 (n/a)</td><td>39.61 (n/a)</td><td>40.08 (n/a)</td><td>37.53 (n/a)</td><td>1.57 (n/a)</td><td>41.06 (n/a)</td><td>39.59 (n/a)</td><td>40.05 (n/a)</td><td>37.51 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>43.81 (-5.00%)</td><td>41.94 (+0.05%)</td><td>43.68 (+6.43%)</td><td>37.77 (-2.99%)</td><td>2.67 (-3.21%)</td><td>43.78 (-5.00%)</td><td>41.91 (+0.05%)</td><td>43.65 (+6.43%)</td><td>37.75 (-2.99%)</td><td>2.67 (-3.21%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>46.11 (n/a)</td><td>41.92 (n/a)</td><td>41.04 (n/a)</td><td>38.93 (n/a)</td><td>2.76 (n/a)</td><td>46.08 (n/a)</td><td>41.89 (n/a)</td><td>41.01 (n/a)</td><td>38.91 (n/a)</td><td>2.76 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>255.10 (n/a)</td><td>195.74 (n/a)</td><td>209.00 (n/a)</td><td>106.30 (n/a)</td><td>55.10 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>143.14 (n/a)</td><td>134.70 (n/a)</td><td>109.10 (n/a)</td><td>35.25 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>144.78 (n/a)</td><td>134.30 (n/a)</td><td>106.20 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>158.18 (n/a)</td><td>149.60 (n/a)</td><td>134.10 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>168.10 (n/a)</td><td>158.90 (n/a)</td><td>135.00 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.40 (n/a)</td><td>186.42 (n/a)</td><td>178.20 (n/a)</td><td>152.50 (n/a)</td><td>41.27 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>180.90 (n/a)</td><td>168.30 (n/a)</td><td>168.30 (n/a)</td><td>154.80 (n/a)</td><td>9.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.30 (n/a)</td><td>242.60 (n/a)</td><td>213.10 (n/a)</td><td>186.20 (n/a)</td><td>63.32 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 <b>(+39.70%)</b></td><td>0.05 <b>(+26.97%)</b></td><td>0.05 (+19.46%)</td><td>0.04 <b>(+75.00%)</b></td><td>0.01 (+8.17%)</td><td>198.10 <b>(-42.84%)</b></td><td>162.30 <b>(-24.40%)</b></td><td>164.60 (-16.28%)</td><td>114.10 <b>(-28.46%)</b></td><td>31.98 <b>(-58.04%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.60 (n/a)</td><td>214.68 (n/a)</td><td>196.60 (n/a)</td><td>159.50 (n/a)</td><td>76.20 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 (+9.25%)</td><td>0.03 (-15.21%)</td><td>0.03 <b>(-27.38%)</b></td><td>0.03 (+9.34%)</td><td>0.01 (+16.25%)</td><td>319.60 (-8.53%)</td><td>274.78 (+18.45%)</td><td>305.00 <b>(+37.70%)</b></td><td>165.30 (-8.47%)</td><td>63.06 (-7.85%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>349.40 (n/a)</td><td>231.98 (n/a)</td><td>221.50 (n/a)</td><td>180.60 (n/a)</td><td>68.43 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-3.37%)</td><td>0.05 (-0.51%)</td><td>0.05 (+4.93%)</td><td>0.04 (-5.93%)</td><td>0.01 (+1.87%)</td><td>187.80 (+6.28%)</td><td>158.76 (+0.67%)</td><td>156.00 (-4.70%)</td><td>135.80 (+3.51%)</td><td>19.52 (+14.55%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.70 (n/a)</td><td>157.70 (n/a)</td><td>163.70 (n/a)</td><td>131.20 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (+16.68%)</td><td>0.06 (+12.41%)</td><td>0.05 (+6.06%)</td><td>0.05 (+6.62%)</td><td>0.01 <b>(+57.87%)</b></td><td>180.30 (-6.24%)</td><td>149.70 (-9.78%)</td><td>157.60 (-5.69%)</td><td>116.30 (-14.30%)</td><td>27.56 <b>(+26.16%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>165.92 (n/a)</td><td>167.10 (n/a)</td><td>135.70 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (+10.55%)</td><td>0.05 (+2.29%)</td><td>0.05 (-1.40%)</td><td>0.04 (+2.22%)</td><td>0.01 <b>(+32.83%)</b></td><td>187.00 (-2.15%)</td><td>161.66 (-1.04%)</td><td>168.70 (+1.38%)</td><td>110.50 (-9.57%)</td><td>29.64 (+16.77%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>163.36 (n/a)</td><td>166.40 (n/a)</td><td>122.20 (n/a)</td><td>25.39 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (+13.69%)</td><td>0.05 (+12.56%)</td><td>0.04 (+3.42%)</td><td>0.03 (-10.66%)</td><td>0.01 <b>(+68.28%)</b></td><td>234.90 (+11.91%)</td><td>173.32 (-7.29%)</td><td>188.30 (-3.29%)</td><td>118.80 (-12.00%)</td><td>48.92 <b>(+64.72%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>186.94 (n/a)</td><td>194.70 (n/a)</td><td>135.00 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-15.16%)</td><td>0.04 (-2.90%)</td><td>0.04 (+16.13%)</td><td>0.04 (+19.96%)</td><td>0.01 <b>(-42.72%)</b></td><td>232.70 (-16.65%)</td><td>197.10 (-2.86%)</td><td>193.80 (-13.90%)</td><td>142.00 (+17.84%)</td><td>35.38 <b>(-43.36%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>279.20 (n/a)</td><td>202.90 (n/a)</td><td>225.10 (n/a)</td><td>120.50 (n/a)</td><td>62.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (+7.20%)</td><td>0.05 (+12.21%)</td><td>0.05 (+7.40%)</td><td>0.04 (+13.19%)</td><td>0.01 (+17.22%)</td><td>209.60 (-11.64%)</td><td>168.02 (-10.62%)</td><td>175.70 (-6.89%)</td><td>134.50 (-6.73%)</td><td>31.97 (-6.49%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>187.98 (n/a)</td><td>188.70 (n/a)</td><td>144.20 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.21 (-1.34%)</td><td>0.21 (-0.84%)</td><td>0.21 (-0.65%)</td><td>0.21 (-0.68%)</td><td>0.00 <b>(-76.97%)</b></td><td>40882.90 (+0.68%)</td><td>40842.88 (+0.84%)</td><td>40843.80 (+0.66%)</td><td>40791.90 (+1.35%)</td><td>34.87 <b>(-76.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40604.80 (n/a)</td><td>40502.20 (n/a)</td><td>40576.30 (n/a)</td><td>40247.10 (n/a)</td><td>148.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (-4.40%)</td><td>0.05 (-12.68%)</td><td>0.05 (-19.64%)</td><td>0.04 (-17.29%)</td><td>0.01 (+10.52%)</td><td>222.90 <b>(+20.88%)</b></td><td>174.88 (+15.95%)</td><td>171.40 <b>(+24.38%)</b></td><td>125.60 (+4.58%)</td><td>37.70 <b>(+36.13%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>150.82 (n/a)</td><td>137.80 (n/a)</td><td>120.10 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.10 (+13.92%)</td><td>0.08 (+10.86%)</td><td>0.08 (+5.68%)</td><td>0.07 <b>(+34.88%)</b></td><td>0.01 (-17.05%)</td><td>174.30 <b>(-25.86%)</b></td><td>150.70 (-11.44%)</td><td>152.20 (-5.35%)</td><td>122.40 (-12.20%)</td><td>19.14 <b>(-49.03%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>170.16 (n/a)</td><td>160.80 (n/a)</td><td>139.40 (n/a)</td><td>37.56 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.08 (-0.03%)</td><td>0.06 (-6.14%)</td><td>0.06 (+3.33%)</td><td>0.04 (-11.57%)</td><td>0.01 <b>(+28.33%)</b></td><td>187.60 (+13.08%)</td><td>142.14 (+9.00%)</td><td>126.20 (-3.22%)</td><td>108.90 (+0.00%)</td><td>35.64 <b>(+50.75%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.90 (n/a)</td><td>130.40 (n/a)</td><td>130.40 (n/a)</td><td>108.90 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (-1.79%)</td><td>0.06 (-14.25%)</td><td>0.06 (-14.68%)</td><td>0.04 <b>(-38.55%)</b></td><td>0.01 <b>(+140.22%)</b></td><td>286.80 <b>(+62.77%)</b></td><td>195.00 <b>(+22.13%)</b></td><td>184.30 (+17.16%)</td><td>144.70 (+1.83%)</td><td>54.29 <b>(+316.66%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>159.66 (n/a)</td><td>157.30 (n/a)</td><td>142.10 (n/a)</td><td>13.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-9.16%)</td><td>0.05 (-6.57%)</td><td>0.05 (-5.94%)</td><td>0.04 (-15.27%)</td><td>0.01 (+5.32%)</td><td>203.40 (+18.05%)</td><td>159.68 (+8.01%)</td><td>161.50 (+6.32%)</td><td>126.50 (+10.10%)</td><td>32.68 <b>(+30.59%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.30 (n/a)</td><td>147.84 (n/a)</td><td>151.90 (n/a)</td><td>114.90 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.09 (+14.50%)</td><td>0.06 (+2.75%)</td><td>0.06 (+18.27%)</td><td>0.04 <b>(-23.97%)</b></td><td>0.02 <b>(+50.15%)</b></td><td>290.50 <b>(+31.51%)</b></td><td>190.66 (+2.36%)</td><td>174.10 (-15.44%)</td><td>119.20 (-12.67%)</td><td>64.15 <b>(+74.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>186.26 (n/a)</td><td>205.90 (n/a)</td><td>136.50 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (-7.62%)</td><td>0.05 (+2.03%)</td><td>0.05 (+7.74%)</td><td>0.04 <b>(+23.06%)</b></td><td>0.01 <b>(-37.78%)</b></td><td>217.90 (-18.75%)</td><td>163.86 (-8.50%)</td><td>166.90 (-7.17%)</td><td>119.40 (+8.25%)</td><td>36.56 <b>(-43.69%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>268.20 (n/a)</td><td>179.08 (n/a)</td><td>179.80 (n/a)</td><td>110.30 (n/a)</td><td>64.93 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-10.07%)</td><td>0.06 <b>(+23.66%)</b></td><td>0.06 <b>(+38.00%)</b></td><td>0.05 <b>(+69.04%)</b></td><td>0.00 <b>(-71.79%)</b></td><td>184.10 <b>(-40.82%)</b></td><td>162.56 <b>(-25.41%)</b></td><td>157.80 <b>(-27.55%)</b></td><td>150.20 (+11.26%)</td><td>13.14 <b>(-81.05%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>311.10 (n/a)</td><td>217.94 (n/a)</td><td>217.80 (n/a)</td><td>135.00 (n/a)</td><td>69.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (+11.82%)</td><td>0.05 (+10.31%)</td><td>0.05 (+10.06%)</td><td>0.04 (+7.10%)</td><td>0.01 (-4.62%)</td><td>212.40 (-6.60%)</td><td>156.58 (-10.11%)</td><td>153.30 (-9.18%)</td><td>120.70 (-10.53%)</td><td>33.98 (-15.83%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>174.20 (n/a)</td><td>168.80 (n/a)</td><td>134.90 (n/a)</td><td>40.37 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.07 (+8.06%)</td><td>0.06 (+17.29%)</td><td>0.05 (+7.87%)</td><td>0.05 <b>(+70.69%)</b></td><td>0.01 <b>(-37.26%)</b></td><td>190.50 <b>(-41.40%)</b></td><td>167.38 <b>(-21.30%)</b></td><td>173.90 (-7.30%)</td><td>124.10 (-7.46%)</td><td>25.30 <b>(-67.60%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>325.10 (n/a)</td><td>212.68 (n/a)</td><td>187.60 (n/a)</td><td>134.10 (n/a)</td><td>78.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 <b>(-35.21%)</b></td><td>0.04 (-14.64%)</td><td>0.05 (-11.87%)</td><td>0.04 (+7.64%)</td><td>0.00 <b>(-82.18%)</b></td><td>195.60 (-7.12%)</td><td>185.08 (+12.69%)</td><td>180.10 (+13.48%)</td><td>177.50 <b>(+54.35%)</b></td><td>9.21 <b>(-74.15%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>164.24 (n/a)</td><td>158.70 (n/a)</td><td>115.00 (n/a)</td><td>35.64 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-4.69%)</td><td>0.04 (-4.37%)</td><td>0.04 (+2.18%)</td><td>0.03 (+9.64%)</td><td>0.01 (-10.93%)</td><td>291.30 (-8.77%)</td><td>224.02 (+3.10%)</td><td>209.80 (-2.10%)</td><td>154.10 (+4.97%)</td><td>56.38 (-13.64%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.30 (n/a)</td><td>217.28 (n/a)</td><td>214.30 (n/a)</td><td>146.80 (n/a)</td><td>65.29 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (+18.79%)</td><td>0.05 (+19.55%)</td><td>0.05 (+7.68%)</td><td>0.05 <b>(+68.12%)</b></td><td>0.01 <b>(-38.69%)</b></td><td>175.90 <b>(-40.51%)</b></td><td>161.40 (-19.36%)</td><td>164.30 (-7.12%)</td><td>137.80 (-15.77%)</td><td>16.00 <b>(-70.46%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.70 (n/a)</td><td>200.14 (n/a)</td><td>176.90 (n/a)</td><td>163.60 (n/a)</td><td>54.15 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.06 (-9.43%)</td><td>0.05 (-5.49%)</td><td>0.05 (-1.83%)</td><td>0.04 (-6.64%)</td><td>0.01 (-4.40%)</td><td>220.50 (+7.14%)</td><td>183.86 (+5.96%)</td><td>184.10 (+1.88%)</td><td>155.50 (+10.44%)</td><td>28.03 (+11.73%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>173.52 (n/a)</td><td>180.70 (n/a)</td><td>140.80 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.05 <b>(+23.38%)</b></td><td>0.04 <b>(+20.34%)</b></td><td>0.04 (+10.86%)</td><td>0.03 <b>(+27.54%)</b></td><td>0.01 (-10.79%)</td><td>289.10 <b>(-21.59%)</b></td><td>216.22 (-19.62%)</td><td>215.20 (-9.77%)</td><td>160.70 (-18.96%)</td><td>46.82 <b>(-41.92%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.70 (n/a)</td><td>269.00 (n/a)</td><td>238.50 (n/a)</td><td>198.30 (n/a)</td><td>80.61 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.70 (-14.87%)</td><td>0.55 (-13.78%)</td><td>0.52 <b>(-26.55%)</b></td><td>0.44 <b>(+43.19%)</b></td><td>0.11 <b>(-43.56%)</b></td><td>223.70 <b>(-30.16%)</b></td><td>183.34 (+5.68%)</td><td>189.40 <b>(+36.16%)</b></td><td>140.80 (+17.43%)</td><td>36.26 <b>(-56.50%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.82 (n/a)</td><td>0.64 (n/a)</td><td>0.71 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>320.30 (n/a)</td><td>173.48 (n/a)</td><td>139.10 (n/a)</td><td>119.90 (n/a)</td><td>83.35 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.64 <b>(-27.32%)</b></td><td>0.54 (-19.74%)</td><td>0.56 (-17.53%)</td><td>0.44 (-7.09%)</td><td>0.08 <b>(-45.08%)</b></td><td>221.10 (+7.64%)</td><td>185.40 <b>(+22.02%)</b></td><td>175.20 <b>(+21.25%)</b></td><td>153.70 <b>(+37.60%)</b></td><td>27.88 (-18.71%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.88 (n/a)</td><td>0.67 (n/a)</td><td>0.68 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>205.40 (n/a)</td><td>151.94 (n/a)</td><td>144.50 (n/a)</td><td>111.70 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.62 (-11.72%)</td><td>0.52 (-17.95%)</td><td>0.50 <b>(-23.07%)</b></td><td>0.44 (-6.54%)</td><td>0.07 <b>(-26.12%)</b></td><td>222.20 (+7.03%)</td><td>191.72 <b>(+20.99%)</b></td><td>195.30 <b>(+30.03%)</b></td><td>159.80 (+13.25%)</td><td>24.25 (-12.71%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.70 (n/a)</td><td>0.63 (n/a)</td><td>0.65 (n/a)</td><td>0.47 (n/a)</td><td>0.09 (n/a)</td><td>207.60 (n/a)</td><td>158.46 (n/a)</td><td>150.20 (n/a)</td><td>141.10 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.58 <b>(-24.50%)</b></td><td>0.49 (-18.08%)</td><td>0.47 (-13.81%)</td><td>0.43 (-18.45%)</td><td>0.06 <b>(-40.44%)</b></td><td>231.20 <b>(+22.59%)</b></td><td>203.18 <b>(+21.03%)</b></td><td>211.00 (+16.06%)</td><td>170.90 <b>(+32.38%)</b></td><td>23.79 (-3.58%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.76 (n/a)</td><td>0.60 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.10 (n/a)</td><td>188.60 (n/a)</td><td>167.88 (n/a)</td><td>181.80 (n/a)</td><td>129.10 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.61 (+1.86%)</td><td>0.51 (-9.01%)</td><td>0.50 (-13.45%)</td><td>0.37 <b>(-22.13%)</b></td><td>0.10 <b>(+96.51%)</b></td><td>197.80 <b>(+28.44%)</b></td><td>150.10 (+12.67%)</td><td>148.50 (+15.56%)</td><td>120.70 (-1.79%)</td><td>30.91 <b>(+144.23%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.05 (n/a)</td><td>154.00 (n/a)</td><td>133.22 (n/a)</td><td>128.50 (n/a)</td><td>122.90 (n/a)</td><td>12.66 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.57 (+8.27%)</td><td>0.47 (+4.65%)</td><td>0.44 (-10.18%)</td><td>0.39 <b>(+42.02%)</b></td><td>0.09 (-18.90%)</td><td>191.20 <b>(-29.60%)</b></td><td>159.60 (-7.84%)</td><td>168.70 (+11.35%)</td><td>128.40 (-7.63%)</td><td>28.04 <b>(-49.86%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>271.60 (n/a)</td><td>173.18 (n/a)</td><td>151.50 (n/a)</td><td>139.00 (n/a)</td><td>55.91 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.52 (-15.60%)</td><td>0.43 (-11.33%)</td><td>0.42 (-9.82%)</td><td>0.36 (-12.79%)</td><td>0.07 (-9.60%)</td><td>204.20 (+14.65%)</td><td>173.70 (+13.07%)</td><td>175.70 (+10.92%)</td><td>141.30 (+18.44%)</td><td>27.56 <b>(+26.48%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.08 (n/a)</td><td>178.10 (n/a)</td><td>153.62 (n/a)</td><td>158.40 (n/a)</td><td>119.30 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.45 (-11.66%)</td><td>0.39 (-11.81%)</td><td>0.35 <b>(-26.44%)</b></td><td>0.34 <b>(+24.97%)</b></td><td>0.06 <b>(-42.76%)</b></td><td>219.40 (-19.96%)</td><td>194.00 (+8.96%)</td><td>208.10 <b>(+35.92%)</b></td><td>163.40 (+13.24%)</td><td>27.02 <b>(-50.39%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>274.10 (n/a)</td><td>178.04 (n/a)</td><td>153.10 (n/a)</td><td>144.30 (n/a)</td><td>54.46 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.94 (-12.82%)</td><td>0.81 (-15.78%)</td><td>0.83 (-17.62%)</td><td>0.68 (-19.92%)</td><td>0.11 (+11.86%)</td><td>192.30 <b>(+24.87%)</b></td><td>163.58 (+19.56%)</td><td>157.70 <b>(+21.40%)</b></td><td>139.70 (+14.70%)</td><td>22.87 <b>(+58.71%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>1.08 (n/a)</td><td>0.97 (n/a)</td><td>1.01 (n/a)</td><td>0.85 (n/a)</td><td>0.10 (n/a)</td><td>154.00 (n/a)</td><td>136.82 (n/a)</td><td>129.90 (n/a)</td><td>121.80 (n/a)</td><td>14.41 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.12 (-0.71%)</td><td>0.78 (-17.88%)</td><td>0.67 <b>(-29.26%)</b></td><td>0.63 (-18.54%)</td><td>0.20 <b>(+43.33%)</b></td><td>207.50 <b>(+22.78%)</b></td><td>175.56 <b>(+24.94%)</b></td><td>194.60 <b>(+41.32%)</b></td><td>117.30 (+0.69%)</td><td>36.50 <b>(+74.17%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>1.12 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.78 (n/a)</td><td>0.14 (n/a)</td><td>169.00 (n/a)</td><td>140.52 (n/a)</td><td>137.70 (n/a)</td><td>116.50 (n/a)</td><td>20.96 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>1.16 (+1.56%)</td><td>0.85 (-15.78%)</td><td>0.84 (-17.13%)</td><td>0.60 <b>(-29.69%)</b></td><td>0.22 <b>(+110.29%)</b></td><td>217.60 <b>(+42.22%)</b></td><td>163.42 <b>(+24.09%)</b></td><td>155.40 <b>(+20.75%)</b></td><td>112.90 (-1.57%)</td><td>41.45 <b>(+194.54%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>1.14 (n/a)</td><td>1.00 (n/a)</td><td>1.02 (n/a)</td><td>0.86 (n/a)</td><td>0.10 (n/a)</td><td>153.00 (n/a)</td><td>131.70 (n/a)</td><td>128.70 (n/a)</td><td>114.70 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.00 (-8.33%)</td><td>0.00 (-14.81%)</td><td>0.00 (-18.18%)</td><td>0.00 (-11.11%)</td><td>0.00 (-15.98%)</td><td>5168.09 (+13.76%)</td><td>4431.69 (+12.79%)</td><td>4492.92 (+16.65%)</td><td>3576.64 (+2.63%)</td><td>573.28 <b>(+22.81%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4543.17 (n/a)</td><td>3929.28 (n/a)</td><td>3851.61 (n/a)</td><td>3484.84 (n/a)</td><td>466.81 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.00 (-4.35%)</td><td>0.00 (-5.66%)</td><td>0.00 (-9.09%)</td><td>0.00 (+0.00%)</td><td>0.00 (-17.80%)</td><td>4552.05 (+1.22%)</td><td>4150.54 (+6.78%)</td><td>4122.63 (+9.19%)</td><td>3806.88 (+6.17%)</td><td>311.43 (-14.19%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4497.33 (n/a)</td><td>3887.13 (n/a)</td><td>3775.82 (n/a)</td><td>3585.56 (n/a)</td><td>362.95 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>0.27 (-0.36%)</td><td>0.24 (+6.83%)</td><td>0.25 (-3.52%)</td><td>0.19 <b>(+25.13%)</b></td><td>0.03 <b>(-45.56%)</b></td><td>11055.95 <b>(-20.08%)</b></td><td>8841.86 (-10.46%)</td><td>8494.64 (+3.66%)</td><td>7636.48 (+0.34%)</td><td>1298.01 <b>(-54.06%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>13833.24 (n/a)</td><td>9874.95 (n/a)</td><td>8194.32 (n/a)</td><td>7610.28 (n/a)</td><td>2825.75 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (-11.56%)</td><td>2.69 (-4.25%)</td><td>2.86 (+8.05%)</td><td>2.07 (-8.43%)</td><td>0.40 (-19.42%)</td><td>253.90 (+9.20%)</td><td>198.64 (+4.00%)</td><td>183.40 (-7.47%)</td><td>169.60 (+13.07%)</td><td>33.34 (+2.59%)</td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>3.50 (n/a)</td><td>2.81 (n/a)</td><td>2.65 (n/a)</td><td>2.26 (n/a)</td><td>0.49 (n/a)</td><td>232.50 (n/a)</td><td>191.00 (n/a)</td><td>198.20 (n/a)</td><td>150.00 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (+2.23%)</td><td>2.89 (-19.61%)</td><td>2.72 <b>(-29.77%)</b></td><td>2.00 <b>(-30.01%)</b></td><td>0.93 <b>(+99.22%)</b></td><td>262.60 <b>(+42.87%)</b></td><td>197.38 <b>(+33.17%)</b></td><td>192.60 <b>(+42.35%)</b></td><td>129.90 (-2.18%)</td><td>62.14 <b>(+186.82%)</b></td>
</tr>
<tr>
<td><code>5503a95</code> — 2026-05-12 00:06:19</td><td>3.95 (n/a)</td><td>3.59 (n/a)</td><td>3.88 (n/a)</td><td>2.85 (n/a)</td><td>0.47 (n/a)</td><td>183.80 (n/a)</td><td>148.22 (n/a)</td><td>135.30 (n/a)</td><td>132.80 (n/a)</td><td>21.66 (n/a)</td>
</tr>
</tbody>
</table>


</details>
