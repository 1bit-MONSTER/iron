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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.11 <b>(+30.89%)</b></td><td>0.08 (+13.00%)</td><td>0.07 (-0.60%)</td><td>0.06 <b>(+22.81%)</b></td><td>0.02 <b>(+73.61%)</b></td><td>190.10 (-18.59%)</td><td>167.08 (-9.96%)</td><td>182.90 (+0.61%)</td><td>113.40 <b>(-23.64%)</b></td><td>32.44 (+6.27%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>185.56 (n/a)</td><td>181.80 (n/a)</td><td>148.50 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 <b>(+30.73%)</b></td><td>0.09 <b>(+25.51%)</b></td><td>0.09 <b>(+29.11%)</b></td><td>0.07 (+2.79%)</td><td>0.01 <b>(+179.01%)</b></td><td>184.80 (-2.69%)</td><td>146.52 (-19.13%)</td><td>143.50 <b>(-22.52%)</b></td><td>124.50 <b>(-23.53%)</b></td><td>23.10 <b>(+115.02%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>181.18 (n/a)</td><td>185.20 (n/a)</td><td>162.80 (n/a)</td><td>10.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 <b>(+63.20%)</b></td><td>0.07 <b>(+20.83%)</b></td><td>0.06 (+11.54%)</td><td>0.06 (+1.53%)</td><td>0.02 <b>(+750.46%)</b></td><td>214.30 (-1.52%)</td><td>181.46 (-13.70%)</td><td>190.10 (-10.33%)</td><td>122.40 <b>(-38.74%)</b></td><td>38.24 <b>(+415.26%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>217.60 (n/a)</td><td>210.26 (n/a)</td><td>212.00 (n/a)</td><td>199.80 (n/a)</td><td>7.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 <b>(+36.12%)</b></td><td>0.06 (+1.32%)</td><td>0.06 (-3.15%)</td><td>0.04 <b>(-27.19%)</b></td><td>0.02 <b>(+210.63%)</b></td><td>296.60 <b>(+37.31%)</b></td><td>204.38 (+5.48%)</td><td>201.40 (+3.28%)</td><td>125.70 <b>(-26.53%)</b></td><td>61.28 <b>(+208.53%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>193.76 (n/a)</td><td>195.00 (n/a)</td><td>171.10 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (-7.03%)</td><td>0.03 (-18.45%)</td><td>0.03 (-19.36%)</td><td>0.02 <b>(-24.46%)</b></td><td>0.01 <b>(+24.07%)</b></td><td>228.40 <b>(+32.41%)</b></td><td>186.76 <b>(+25.28%)</b></td><td>189.10 <b>(+24.00%)</b></td><td>132.90 (+7.52%)</td><td>39.76 <b>(+79.50%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>149.08 (n/a)</td><td>152.50 (n/a)</td><td>123.60 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.03 <b>(-38.11%)</b></td><td>0.03 <b>(-22.53%)</b></td><td>0.03 (-12.60%)</td><td>0.03 (-2.21%)</td><td>0.00 <b>(-85.64%)</b></td><td>183.40 (+2.29%)</td><td>172.42 <b>(+22.08%)</b></td><td>170.10 (+14.39%)</td><td>163.20 <b>(+61.58%)</b></td><td>8.83 <b>(-75.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>179.30 (n/a)</td><td>141.24 (n/a)</td><td>148.70 (n/a)</td><td>101.00 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 <b>(+27.88%)</b></td><td>0.03 (+4.48%)</td><td>0.03 (+2.58%)</td><td>0.02 (-16.55%)</td><td>0.01 <b>(+115.15%)</b></td><td>237.40 (+19.84%)</td><td>168.82 (-0.50%)</td><td>163.60 (-2.50%)</td><td>116.50 <b>(-21.76%)</b></td><td>43.42 <b>(+106.47%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.10 (n/a)</td><td>169.66 (n/a)</td><td>167.80 (n/a)</td><td>148.90 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (-4.72%)</td><td>0.03 (-9.04%)</td><td>0.03 (-11.68%)</td><td>0.03 (-14.15%)</td><td>0.00 (+19.51%)</td><td>203.30 (+16.44%)</td><td>169.80 (+10.72%)</td><td>167.00 (+13.22%)</td><td>140.40 (+4.93%)</td><td>24.93 <b>(+44.71%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.60 (n/a)</td><td>153.36 (n/a)</td><td>147.50 (n/a)</td><td>133.80 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (-5.20%)</td><td>0.03 (-0.08%)</td><td>0.04 (+15.91%)</td><td>0.02 (-18.28%)</td><td>0.01 <b>(+36.28%)</b></td><td>213.20 <b>(+22.39%)</b></td><td>163.88 (+2.18%)</td><td>146.80 (-13.70%)</td><td>132.40 (+5.50%)</td><td>35.67 <b>(+78.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.20 (n/a)</td><td>160.38 (n/a)</td><td>170.10 (n/a)</td><td>125.50 (n/a)</td><td>20.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (-5.70%)</td><td>0.03 (+4.64%)</td><td>0.04 <b>(+25.06%)</b></td><td>0.03 (-4.84%)</td><td>0.01 (+13.94%)</td><td>193.40 (+5.11%)</td><td>159.38 (-3.62%)</td><td>138.90 <b>(-20.03%)</b></td><td>135.30 (+6.03%)</td><td>30.09 <b>(+28.42%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>165.36 (n/a)</td><td>173.70 (n/a)</td><td>127.60 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (+14.21%)</td><td>0.03 (-2.93%)</td><td>0.03 (-6.73%)</td><td>0.02 (-12.56%)</td><td>0.01 <b>(+101.52%)</b></td><td>222.90 (+14.37%)</td><td>176.78 (+6.16%)</td><td>177.90 (+7.23%)</td><td>127.10 (-12.47%)</td><td>38.34 <b>(+101.34%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>166.52 (n/a)</td><td>165.90 (n/a)</td><td>145.20 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.03 (-4.51%)</td><td>0.02 (-0.37%)</td><td>0.02 (-2.83%)</td><td>0.02 <b>(+29.51%)</b></td><td>0.00 <b>(-41.91%)</b></td><td>238.10 <b>(-22.77%)</b></td><td>219.28 (-2.20%)</td><td>224.90 (+2.93%)</td><td>182.00 (+4.72%)</td><td>22.96 <b>(-54.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>308.30 (n/a)</td><td>224.22 (n/a)</td><td>218.50 (n/a)</td><td>173.80 (n/a)</td><td>50.69 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>191.62 (n/a)</td><td>212.50 (n/a)</td><td>137.40 (n/a)</td><td>35.29 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>182.60 (n/a)</td><td>183.20 (n/a)</td><td>146.20 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>185.40 (n/a)</td><td>175.70 (n/a)</td><td>160.10 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>362.00 (n/a)</td><td>205.90 (n/a)</td><td>182.00 (n/a)</td><td>105.50 (n/a)</td><td>94.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>157.02 (n/a)</td><td>140.60 (n/a)</td><td>130.20 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>154.14 (n/a)</td><td>168.10 (n/a)</td><td>117.70 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>207.14 (n/a)</td><td>200.30 (n/a)</td><td>175.00 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>297.20 (n/a)</td><td>195.94 (n/a)</td><td>177.60 (n/a)</td><td>158.10 (n/a)</td><td>57.55 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>155.44 (n/a)</td><td>154.80 (n/a)</td><td>128.90 (n/a)</td><td>19.51 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>166.02 (n/a)</td><td>167.60 (n/a)</td><td>111.00 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>172.84 (n/a)</td><td>178.70 (n/a)</td><td>125.00 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>166.44 (n/a)</td><td>179.20 (n/a)</td><td>126.30 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>200.00 (n/a)</td><td>167.24 (n/a)</td><td>183.20 (n/a)</td><td>89.30 (n/a)</td><td>44.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>203.66 (n/a)</td><td>217.50 (n/a)</td><td>162.40 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>180.62 (n/a)</td><td>182.50 (n/a)</td><td>157.20 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>198.78 (n/a)</td><td>204.40 (n/a)</td><td>167.40 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>4.84 (-2.25%)</td><td>4.26 (+9.35%)</td><td>4.17 (+18.98%)</td><td>3.94 (+14.62%)</td><td>0.35 <b>(-47.36%)</b></td><td>2387.20 (-12.76%)</td><td>2218.30 (-9.97%)</td><td>2255.30 (-15.95%)</td><td>1942.90 (+2.30%)</td><td>169.23 <b>(-54.37%)</b></td><td>1904.00 (-2.25%)</td><td>1675.98 (+9.35%)</td><td>1640.30 (+18.98%)</td><td>1549.67 (+14.62%)</td><td>136.74 <b>(-47.36%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>4.95 (n/a)</td><td>3.90 (n/a)</td><td>3.50 (n/a)</td><td>3.44 (n/a)</td><td>0.66 (n/a)</td><td>2736.30 (n/a)</td><td>2463.82 (n/a)</td><td>2683.30 (n/a)</td><td>1899.20 (n/a)</td><td>370.89 (n/a)</td><td>1947.90 (n/a)</td><td>1532.65 (n/a)</td><td>1378.66 (n/a)</td><td>1351.98 (n/a)</td><td>259.78 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.23 (+3.43%)</td><td>0.94 (+9.52%)</td><td>1.01 <b>(+43.65%)</b></td><td>0.62 (-3.14%)</td><td>0.28 (+6.19%)</td><td>357.60 (+3.23%)</td><td>255.28 (-7.85%)</td><td>218.20 <b>(-30.38%)</b></td><td>179.40 (-3.34%)</td><td>82.85 (+7.31%)</td><td>52.60 (+3.43%)</td><td>40.06 (+9.52%)</td><td>43.25 <b>(+43.65%)</b></td><td>26.39 (-3.14%)</td><td>12.00 (+6.19%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.19 (n/a)</td><td>0.86 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.26 (n/a)</td><td>346.40 (n/a)</td><td>277.04 (n/a)</td><td>313.40 (n/a)</td><td>185.60 (n/a)</td><td>77.21 (n/a)</td><td>50.85 (n/a)</td><td>36.58 (n/a)</td><td>30.11 (n/a)</td><td>27.25 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.59 <b>(+24.70%)</b></td><td>1.02 (+6.95%)</td><td>0.96 (-5.89%)</td><td>0.67 (+1.71%)</td><td>0.38 <b>(+37.86%)</b></td><td>329.60 (-1.67%)</td><td>241.60 (-3.57%)</td><td>230.80 (+6.26%)</td><td>139.20 (-19.82%)</td><td>81.94 (+7.10%)</td><td>67.80 <b>(+24.70%)</b></td><td>43.32 (+6.95%)</td><td>40.88 (-5.89%)</td><td>28.64 (+1.71%)</td><td>16.18 <b>(+37.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.27 (n/a)</td><td>0.95 (n/a)</td><td>1.02 (n/a)</td><td>0.66 (n/a)</td><td>0.28 (n/a)</td><td>335.20 (n/a)</td><td>250.54 (n/a)</td><td>217.20 (n/a)</td><td>173.60 (n/a)</td><td>76.50 (n/a)</td><td>54.37 (n/a)</td><td>40.51 (n/a)</td><td>43.44 (n/a)</td><td>28.15 (n/a)</td><td>11.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.52 (-0.22%)</td><td>0.52 (-0.09%)</td><td>0.52 (-0.00%)</td><td>0.52 (-0.22%)</td><td>0.00 (-15.88%)</td><td>48756.80 (+0.22%)</td><td>48607.94 (+0.09%)</td><td>48633.80 (+0.00%)</td><td>48398.00 (+0.22%)</td><td>130.53 (-15.52%)</td><td>354.97 (-0.22%)</td><td>353.44 (-0.09%)</td><td>353.25 (-0.00%)</td><td>352.36 (-0.22%)</td><td>0.95 (-15.88%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48650.60 (n/a)</td><td>48566.26 (n/a)</td><td>48631.40 (n/a)</td><td>48290.40 (n/a)</td><td>154.51 (n/a)</td><td>355.76 (n/a)</td><td>353.74 (n/a)</td><td>353.27 (n/a)</td><td>353.13 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.90 (+0.46%)</td><td>0.89 (+0.13%)</td><td>0.88 (-0.62%)</td><td>0.88 (+0.47%)</td><td>0.01 <b>(-22.88%)</b></td><td>28603.70 (-0.47%)</td><td>28386.06 (-0.13%)</td><td>28466.40 (+0.62%)</td><td>28070.60 (-0.46%)</td><td>204.31 <b>(-23.66%)</b></td><td>612.02 (+0.46%)</td><td>605.25 (+0.13%)</td><td>603.51 (-0.62%)</td><td>600.62 (+0.47%)</td><td>4.38 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28739.40 (n/a)</td><td>28423.34 (n/a)</td><td>28289.80 (n/a)</td><td>28200.10 (n/a)</td><td>267.62 (n/a)</td><td>609.21 (n/a)</td><td>604.47 (n/a)</td><td>607.28 (n/a)</td><td>597.78 (n/a)</td><td>5.67 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.35 (+0.55%)</td><td>3.24 (-0.08%)</td><td>3.20 (-3.03%)</td><td>3.17 (+1.57%)</td><td>0.08 (-14.15%)</td><td>7937.90 (-1.55%)</td><td>7763.48 (+0.06%)</td><td>7864.20 (+3.13%)</td><td>7512.80 (-0.55%)</td><td>191.79 (-15.89%)</td><td>2286.75 (+0.55%)</td><td>2214.00 (-0.08%)</td><td>2184.56 (-3.03%)</td><td>2164.28 (+1.57%)</td><td>55.24 (-14.15%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>3.33 (n/a)</td><td>3.25 (n/a)</td><td>3.30 (n/a)</td><td>3.12 (n/a)</td><td>0.09 (n/a)</td><td>8062.80 (n/a)</td><td>7758.50 (n/a)</td><td>7625.70 (n/a)</td><td>7554.00 (n/a)</td><td>228.02 (n/a)</td><td>2274.28 (n/a)</td><td>2215.85 (n/a)</td><td>2252.90 (n/a)</td><td>2130.76 (n/a)</td><td>64.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>4.12 (+0.51%)</td><td>3.74 (+7.66%)</td><td>3.73 (+15.25%)</td><td>3.12 (+1.20%)</td><td>0.41 (-8.44%)</td><td>2586.00 (-1.18%)</td><td>2178.38 (-7.33%)</td><td>2161.80 (-13.23%)</td><td>1955.00 (-0.51%)</td><td>255.62 (-10.63%)</td><td>1081.28 (+0.51%)</td><td>980.45 (+7.66%)</td><td>977.85 (+15.25%)</td><td>817.44 (+1.20%)</td><td>107.34 (-8.44%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>4.10 (n/a)</td><td>3.47 (n/a)</td><td>3.24 (n/a)</td><td>3.08 (n/a)</td><td>0.45 (n/a)</td><td>2617.00 (n/a)</td><td>2350.70 (n/a)</td><td>2491.50 (n/a)</td><td>1965.10 (n/a)</td><td>286.02 (n/a)</td><td>1075.75 (n/a)</td><td>910.67 (n/a)</td><td>848.45 (n/a)</td><td>807.78 (n/a)</td><td>117.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.37 <b>(-27.92%)</b></td><td>0.32 (-11.26%)</td><td>0.32 (-7.18%)</td><td>0.31 (+10.67%)</td><td>0.03 <b>(-71.14%)</b></td><td>4071.80 (-9.64%)</td><td>3856.08 (+8.57%)</td><td>3924.40 (+7.73%)</td><td>3381.50 <b>(+38.73%)</b></td><td>282.95 <b>(-62.94%)</b></td><td>19.85 <b>(-27.92%)</b></td><td>17.48 (-11.26%)</td><td>17.10 (-7.18%)</td><td>16.48 (+10.67%)</td><td>1.39 <b>(-71.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>4506.10 (n/a)</td><td>3551.74 (n/a)</td><td>3642.70 (n/a)</td><td>2437.50 (n/a)</td><td>763.49 (n/a)</td><td>27.53 (n/a)</td><td>19.70 (n/a)</td><td>18.42 (n/a)</td><td>14.89 (n/a)</td><td>4.80 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.01 (-3.94%)</td><td>4.93 (+7.80%)</td><td>4.83 (+2.97%)</td><td>4.14 <b>(+23.80%)</b></td><td>0.68 <b>(-39.84%)</b></td><td>1606.60 (-19.22%)</td><td>1368.88 (-10.19%)</td><td>1378.50 (-2.89%)</td><td>1105.90 (+4.10%)</td><td>177.42 <b>(-50.58%)</b></td><td>1858.40 (-3.94%)</td><td>1522.85 (+7.80%)</td><td>1490.87 (+2.97%)</td><td>1279.26 <b>(+23.80%)</b></td><td>209.03 <b>(-39.84%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>6.26 (n/a)</td><td>4.57 (n/a)</td><td>4.69 (n/a)</td><td>3.34 (n/a)</td><td>1.12 (n/a)</td><td>1988.90 (n/a)</td><td>1524.12 (n/a)</td><td>1419.50 (n/a)</td><td>1062.30 (n/a)</td><td>359.03 (n/a)</td><td>1934.60 (n/a)</td><td>1412.60 (n/a)</td><td>1447.81 (n/a)</td><td>1033.33 (n/a)</td><td>347.48 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>13.71 (n/a)</td><td>13.23 (n/a)</td><td>13.26 (n/a)</td><td>12.66 (n/a)</td><td>0.38 (n/a)</td><td>13.70 (n/a)</td><td>13.22 (n/a)</td><td>13.26 (n/a)</td><td>12.65 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>25.28 (+1.63%)</td><td>24.30 (+2.08%)</td><td>24.66 (+3.12%)</td><td>22.41 (-2.57%)</td><td>1.12 <b>(+44.94%)</b></td><td>25.27 (+1.63%)</td><td>24.28 (+2.08%)</td><td>24.65 (+3.12%)</td><td>22.40 (-2.57%)</td><td>1.12 <b>(+44.94%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>24.88 (n/a)</td><td>23.80 (n/a)</td><td>23.92 (n/a)</td><td>23.01 (n/a)</td><td>0.77 (n/a)</td><td>24.86 (n/a)</td><td>23.79 (n/a)</td><td>23.90 (n/a)</td><td>22.99 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>42.13 (+1.95%)</td><td>39.10 (+4.62%)</td><td>40.14 (+4.98%)</td><td>33.32 (+8.07%)</td><td>3.37 (-18.06%)</td><td>42.10 (+1.95%)</td><td>39.08 (+4.62%)</td><td>40.11 (+4.98%)</td><td>33.30 (+8.07%)</td><td>3.37 (-18.06%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>41.32 (n/a)</td><td>37.37 (n/a)</td><td>38.24 (n/a)</td><td>30.83 (n/a)</td><td>4.12 (n/a)</td><td>41.30 (n/a)</td><td>37.35 (n/a)</td><td>38.21 (n/a)</td><td>30.81 (n/a)</td><td>4.12 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>46.67 (+7.43%)</td><td>42.93 (+5.22%)</td><td>43.35 (+4.60%)</td><td>37.62 (+4.78%)</td><td>3.31 (+13.12%)</td><td>46.64 (+7.43%)</td><td>42.90 (+5.22%)</td><td>43.32 (+4.60%)</td><td>37.60 (+4.78%)</td><td>3.30 (+13.12%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>43.44 (n/a)</td><td>40.80 (n/a)</td><td>41.44 (n/a)</td><td>35.91 (n/a)</td><td>2.92 (n/a)</td><td>43.42 (n/a)</td><td>40.78 (n/a)</td><td>41.42 (n/a)</td><td>35.88 (n/a)</td><td>2.92 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>13.49 (n/a)</td><td>12.67 (n/a)</td><td>13.26 (n/a)</td><td>11.14 (n/a)</td><td>1.02 (n/a)</td><td>13.48 (n/a)</td><td>12.66 (n/a)</td><td>13.25 (n/a)</td><td>11.13 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>25.17 (+3.85%)</td><td>24.45 (+2.27%)</td><td>24.82 (+2.98%)</td><td>22.54 (-3.53%)</td><td>1.08 <b>(+188.39%)</b></td><td>25.16 (+3.85%)</td><td>24.43 (+2.27%)</td><td>24.81 (+2.98%)</td><td>22.53 (-3.53%)</td><td>1.08 <b>(+188.39%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>24.24 (n/a)</td><td>23.91 (n/a)</td><td>24.10 (n/a)</td><td>23.37 (n/a)</td><td>0.37 (n/a)</td><td>24.22 (n/a)</td><td>23.89 (n/a)</td><td>24.09 (n/a)</td><td>23.35 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>41.76 (+5.59%)</td><td>39.51 (+4.88%)</td><td>40.20 (+4.82%)</td><td>34.07 (+1.26%)</td><td>3.16 <b>(+32.83%)</b></td><td>41.73 (+5.59%)</td><td>39.49 (+4.88%)</td><td>40.17 (+4.82%)</td><td>34.05 (+1.26%)</td><td>3.16 <b>(+32.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>39.55 (n/a)</td><td>37.67 (n/a)</td><td>38.35 (n/a)</td><td>33.65 (n/a)</td><td>2.38 (n/a)</td><td>39.52 (n/a)</td><td>37.65 (n/a)</td><td>38.32 (n/a)</td><td>33.63 (n/a)</td><td>2.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>45.97 (-4.01%)</td><td>40.95 (-2.94%)</td><td>43.57 (+2.85%)</td><td>26.89 <b>(-27.55%)</b></td><td>7.97 <b>(+102.54%)</b></td><td>45.94 (-4.01%)</td><td>40.92 (-2.94%)</td><td>43.54 (+2.85%)</td><td>26.87 <b>(-27.55%)</b></td><td>7.96 <b>(+102.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>47.89 (n/a)</td><td>42.19 (n/a)</td><td>42.36 (n/a)</td><td>37.12 (n/a)</td><td>3.93 (n/a)</td><td>47.86 (n/a)</td><td>42.16 (n/a)</td><td>42.34 (n/a)</td><td>37.09 (n/a)</td><td>3.93 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>9.56 (-1.82%)</td><td>8.74 (-5.70%)</td><td>8.51 (-5.77%)</td><td>8.17 (-8.60%)</td><td>0.58 <b>(+43.72%)</b></td><td>9.54 (-1.82%)</td><td>8.72 (-5.70%)</td><td>8.49 (-5.77%)</td><td>8.15 (-8.60%)</td><td>0.57 <b>(+43.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>9.74 (n/a)</td><td>9.27 (n/a)</td><td>9.03 (n/a)</td><td>8.94 (n/a)</td><td>0.40 (n/a)</td><td>9.72 (n/a)</td><td>9.25 (n/a)</td><td>9.01 (n/a)</td><td>8.92 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.88 (+5.57%)</td><td>0.80 (+3.44%)</td><td>0.79 (+2.56%)</td><td>0.74 (+2.98%)</td><td>0.06 <b>(+31.77%)</b></td><td>0.87 (+5.57%)</td><td>0.79 (+3.44%)</td><td>0.78 (+2.56%)</td><td>0.73 (+2.98%)</td><td>0.06 <b>(+31.77%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.04 (n/a)</td><td>0.82 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>1.29 (+0.38%)</td><td>1.17 (+5.54%)</td><td>1.14 (+0.10%)</td><td>1.08 <b>(+22.38%)</b></td><td>0.09 <b>(-43.77%)</b></td><td>1.28 (+0.38%)</td><td>1.16 (+5.54%)</td><td>1.12 (+0.10%)</td><td>1.07 <b>(+22.38%)</b></td><td>0.09 <b>(-43.77%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>1.29 (n/a)</td><td>1.11 (n/a)</td><td>1.14 (n/a)</td><td>0.88 (n/a)</td><td>0.17 (n/a)</td><td>1.27 (n/a)</td><td>1.10 (n/a)</td><td>1.12 (n/a)</td><td>0.87 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>17.63 (+0.26%)</td><td>15.25 (-4.06%)</td><td>14.67 (-4.42%)</td><td>13.66 (-4.24%)</td><td>1.52 (+12.03%)</td><td>17.43 (+0.26%)</td><td>15.07 (-4.06%)</td><td>14.50 (-4.42%)</td><td>13.50 (-4.24%)</td><td>1.50 (+12.03%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>17.58 (n/a)</td><td>15.90 (n/a)</td><td>15.34 (n/a)</td><td>14.26 (n/a)</td><td>1.35 (n/a)</td><td>17.38 (n/a)</td><td>15.71 (n/a)</td><td>15.17 (n/a)</td><td>14.10 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>12.41 (-3.34%)</td><td>11.86 (-1.75%)</td><td>11.70 (-2.06%)</td><td>11.65 (+0.46%)</td><td>0.32 <b>(-31.63%)</b></td><td>12.19 (-3.34%)</td><td>11.65 (-1.75%)</td><td>11.50 (-2.06%)</td><td>11.45 (+0.46%)</td><td>0.31 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>12.84 (n/a)</td><td>12.07 (n/a)</td><td>11.95 (n/a)</td><td>11.60 (n/a)</td><td>0.46 (n/a)</td><td>12.62 (n/a)</td><td>11.86 (n/a)</td><td>11.74 (n/a)</td><td>11.40 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>8.12 (-0.13%)</td><td>7.30 (-5.93%)</td><td>7.27 (-8.68%)</td><td>6.58 (-9.88%)</td><td>0.64 <b>(+68.04%)</b></td><td>7.98 (-0.13%)</td><td>7.18 (-5.93%)</td><td>7.15 (-8.68%)</td><td>6.47 (-9.88%)</td><td>0.63 <b>(+68.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>8.13 (n/a)</td><td>7.76 (n/a)</td><td>7.96 (n/a)</td><td>7.31 (n/a)</td><td>0.38 (n/a)</td><td>7.99 (n/a)</td><td>7.63 (n/a)</td><td>7.82 (n/a)</td><td>7.18 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.66 (+12.54%)</td><td>6.02 (+3.89%)</td><td>6.00 (+3.79%)</td><td>5.42 (-3.07%)</td><td>0.45 <b>(+241.46%)</b></td><td>6.55 (+12.54%)</td><td>5.92 (+3.89%)</td><td>5.90 (+3.79%)</td><td>5.33 (-3.07%)</td><td>0.44 <b>(+241.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>5.92 (n/a)</td><td>5.79 (n/a)</td><td>5.78 (n/a)</td><td>5.59 (n/a)</td><td>0.13 (n/a)</td><td>5.82 (n/a)</td><td>5.70 (n/a)</td><td>5.69 (n/a)</td><td>5.50 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>13.22 (n/a)</td><td>12.77 (n/a)</td><td>13.05 (n/a)</td><td>12.00 (n/a)</td><td>0.52 (n/a)</td><td>13.21 (n/a)</td><td>12.77 (n/a)</td><td>13.05 (n/a)</td><td>12.00 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>13.52 (n/a)</td><td>12.60 (n/a)</td><td>12.41 (n/a)</td><td>11.71 (n/a)</td><td>0.72 (n/a)</td><td>13.51 (n/a)</td><td>12.59 (n/a)</td><td>12.40 (n/a)</td><td>11.70 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>187.36 (n/a)</td><td>189.10 (n/a)</td><td>148.70 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>178.90 (n/a)</td><td>172.80 (n/a)</td><td>154.70 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>172.80 (n/a)</td><td>193.30 (n/a)</td><td>137.50 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>185.12 (n/a)</td><td>188.70 (n/a)</td><td>152.90 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>171.66 (n/a)</td><td>177.60 (n/a)</td><td>116.10 (n/a)</td><td>36.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.90 (n/a)</td><td>217.50 (n/a)</td><td>204.00 (n/a)</td><td>166.40 (n/a)</td><td>51.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>210.98 (n/a)</td><td>206.20 (n/a)</td><td>157.40 (n/a)</td><td>54.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>252.20 (n/a)</td><td>224.78 (n/a)</td><td>221.00 (n/a)</td><td>211.40 (n/a)</td><td>16.03 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-7.19%)</td><td>0.05 (-5.60%)</td><td>0.04 (-10.94%)</td><td>0.04 (+19.69%)</td><td>0.01 <b>(-25.42%)</b></td><td>207.00 (-16.46%)</td><td>186.02 (+3.44%)</td><td>197.40 (+12.29%)</td><td>135.30 (+7.72%)</td><td>28.84 <b>(-35.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.80 (n/a)</td><td>179.84 (n/a)</td><td>175.80 (n/a)</td><td>125.60 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 <b>(-25.87%)</b></td><td>0.05 (-8.31%)</td><td>0.04 (-2.42%)</td><td>0.04 (-2.66%)</td><td>0.01 <b>(-52.49%)</b></td><td>211.40 (+2.72%)</td><td>182.94 (+6.26%)</td><td>187.30 (+2.46%)</td><td>158.90 <b>(+34.89%)</b></td><td>22.62 <b>(-33.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>172.16 (n/a)</td><td>182.80 (n/a)</td><td>117.80 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+12.54%)</td><td>0.05 (+6.94%)</td><td>0.05 (-0.24%)</td><td>0.04 <b>(+20.21%)</b></td><td>0.01 (-8.30%)</td><td>207.70 (-16.82%)</td><td>176.62 (-7.61%)</td><td>181.00 (+0.22%)</td><td>137.50 (-11.18%)</td><td>26.08 <b>(-33.14%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.70 (n/a)</td><td>191.16 (n/a)</td><td>180.60 (n/a)</td><td>154.80 (n/a)</td><td>39.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-6.49%)</td><td>0.04 (-1.63%)</td><td>0.04 (+3.78%)</td><td>0.03 (-13.43%)</td><td>0.01 (-10.36%)</td><td>322.90 (+15.49%)</td><td>224.38 (+1.77%)</td><td>211.40 (-3.65%)</td><td>172.70 (+6.93%)</td><td>57.58 (+15.82%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.60 (n/a)</td><td>220.48 (n/a)</td><td>219.40 (n/a)</td><td>161.50 (n/a)</td><td>49.71 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-11.08%)</td><td>0.04 (-6.06%)</td><td>0.04 (-12.73%)</td><td>0.04 (+4.59%)</td><td>0.01 <b>(-26.04%)</b></td><td>226.60 (-4.39%)</td><td>194.94 (+5.12%)</td><td>204.10 (+14.60%)</td><td>157.30 (+12.44%)</td><td>28.71 <b>(-21.08%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>185.44 (n/a)</td><td>178.10 (n/a)</td><td>139.90 (n/a)</td><td>36.38 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-4.01%)</td><td>0.04 (-1.18%)</td><td>0.04 (+1.43%)</td><td>0.04 (-1.10%)</td><td>0.01 (-3.48%)</td><td>212.90 (+1.14%)</td><td>186.36 (+1.16%)</td><td>189.60 (-1.40%)</td><td>159.00 (+4.19%)</td><td>24.78 (+1.54%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>184.22 (n/a)</td><td>192.30 (n/a)</td><td>152.60 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-2.04%)</td><td>0.04 (+11.83%)</td><td>0.05 (+12.13%)</td><td>0.04 <b>(+36.43%)</b></td><td>0.01 <b>(-42.16%)</b></td><td>221.90 <b>(-26.72%)</b></td><td>187.70 (-13.50%)</td><td>181.90 (-10.79%)</td><td>164.60 (+2.05%)</td><td>22.84 <b>(-57.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.80 (n/a)</td><td>217.00 (n/a)</td><td>203.90 (n/a)</td><td>161.30 (n/a)</td><td>53.79 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-12.29%)</td><td>0.04 (-2.65%)</td><td>0.04 (-4.81%)</td><td>0.03 <b>(+27.38%)</b></td><td>0.00 <b>(-53.69%)</b></td><td>244.40 <b>(-21.52%)</b></td><td>213.06 (-1.72%)</td><td>215.80 (+5.01%)</td><td>179.80 (+14.01%)</td><td>24.38 <b>(-59.30%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.40 (n/a)</td><td>216.78 (n/a)</td><td>205.50 (n/a)</td><td>157.70 (n/a)</td><td>59.90 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-4.52%)</td><td>0.03 (-15.54%)</td><td>0.04 (-9.94%)</td><td>0.03 <b>(-27.14%)</b></td><td>0.01 <b>(+65.71%)</b></td><td>327.40 <b>(+37.27%)</b></td><td>249.78 <b>(+23.46%)</b></td><td>227.50 (+11.03%)</td><td>175.70 (+4.77%)</td><td>65.68 <b>(+147.87%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>202.32 (n/a)</td><td>204.90 (n/a)</td><td>167.70 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (-19.18%)</td><td>0.03 (-16.25%)</td><td>0.03 (-14.15%)</td><td>0.03 <b>(-27.61%)</b></td><td>0.01 (+7.20%)</td><td>324.50 <b>(+38.14%)</b></td><td>251.22 <b>(+20.67%)</b></td><td>240.20 (+16.49%)</td><td>214.00 <b>(+23.70%)</b></td><td>43.95 <b>(+87.83%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>208.18 (n/a)</td><td>206.20 (n/a)</td><td>173.00 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+3.45%)</td><td>0.05 (-6.72%)</td><td>0.05 (-17.49%)</td><td>0.04 (-12.07%)</td><td>0.01 <b>(+64.95%)</b></td><td>199.90 (+13.71%)</td><td>168.12 (+9.50%)</td><td>173.60 <b>(+21.23%)</b></td><td>134.00 (-3.32%)</td><td>32.89 <b>(+79.36%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>153.54 (n/a)</td><td>143.20 (n/a)</td><td>138.60 (n/a)</td><td>18.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.04 (+9.47%)</td><td>0.04 (+4.62%)</td><td>0.04 (+3.90%)</td><td>0.03 (-1.12%)</td><td>0.00 <b>(+92.77%)</b></td><td>237.70 (+1.11%)</td><td>210.24 (-4.02%)</td><td>211.30 (-3.74%)</td><td>190.40 (-8.64%)</td><td>18.13 <b>(+77.44%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.10 (n/a)</td><td>219.04 (n/a)</td><td>219.50 (n/a)</td><td>208.40 (n/a)</td><td>10.22 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-7.83%)</td><td>0.04 (-12.56%)</td><td>0.04 <b>(-21.79%)</b></td><td>0.03 (-7.22%)</td><td>0.01 (-17.98%)</td><td>251.70 (+7.79%)</td><td>192.10 (+13.61%)</td><td>189.20 <b>(+27.84%)</b></td><td>156.50 (+8.53%)</td><td>36.61 (-2.84%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>169.08 (n/a)</td><td>148.00 (n/a)</td><td>144.20 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-8.91%)</td><td>0.05 (-10.48%)</td><td>0.04 (-17.24%)</td><td>0.04 (-7.64%)</td><td>0.01 (-12.53%)</td><td>204.60 (+8.25%)</td><td>175.76 (+11.38%)</td><td>183.10 <b>(+20.78%)</b></td><td>134.00 (+9.75%)</td><td>26.82 (+0.75%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>157.80 (n/a)</td><td>151.60 (n/a)</td><td>122.10 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-13.48%)</td><td>0.05 (-13.04%)</td><td>0.06 (-5.91%)</td><td>0.04 (-18.11%)</td><td>0.01 (+19.64%)</td><td>194.00 <b>(+22.09%)</b></td><td>163.18 (+16.32%)</td><td>146.40 (+6.24%)</td><td>136.80 (+15.64%)</td><td>27.73 <b>(+72.81%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>158.90 (n/a)</td><td>140.28 (n/a)</td><td>137.80 (n/a)</td><td>118.30 (n/a)</td><td>16.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-8.89%)</td><td>0.05 (-15.16%)</td><td>0.05 (-11.45%)</td><td>0.04 <b>(-22.75%)</b></td><td>0.00 <b>(+43.68%)</b></td><td>209.60 <b>(+29.46%)</b></td><td>181.56 (+18.60%)</td><td>179.40 (+12.97%)</td><td>154.90 (+9.78%)</td><td>19.62 <b>(+104.05%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>161.90 (n/a)</td><td>153.08 (n/a)</td><td>158.80 (n/a)</td><td>141.10 (n/a)</td><td>9.62 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-9.37%)</td><td>0.04 (-10.68%)</td><td>0.04 <b>(-20.22%)</b></td><td>0.04 (-1.31%)</td><td>0.00 <b>(-37.38%)</b></td><td>222.70 (+1.32%)</td><td>195.96 (+10.86%)</td><td>201.50 <b>(+25.39%)</b></td><td>172.70 (+10.35%)</td><td>19.58 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>176.76 (n/a)</td><td>160.70 (n/a)</td><td>156.50 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 <b>(-38.66%)</b></td><td>0.04 (-16.19%)</td><td>0.04 (-18.79%)</td><td>0.04 <b>(+39.99%)</b></td><td>0.00 <b>(-87.56%)</b></td><td>200.80 <b>(-28.57%)</b></td><td>188.92 (+4.96%)</td><td>187.70 <b>(+23.16%)</b></td><td>178.00 <b>(+63.00%)</b></td><td>10.68 <b>(-85.64%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>281.10 (n/a)</td><td>180.00 (n/a)</td><td>152.40 (n/a)</td><td>109.20 (n/a)</td><td>74.34 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.21 (+0.24%)</td><td>0.21 (+0.05%)</td><td>0.21 (+0.03%)</td><td>0.21 (-0.02%)</td><td>0.00 <b>(+141.45%)</b></td><td>40905.80 (+0.02%)</td><td>40836.80 (-0.05%)</td><td>40836.10 (-0.03%)</td><td>40727.10 (-0.24%)</td><td>73.91 <b>(+140.88%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40898.00 (n/a)</td><td>40855.52 (n/a)</td><td>40849.90 (n/a)</td><td>40823.40 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 <b>(+23.10%)</b></td><td>0.05 (+5.97%)</td><td>0.05 (-5.00%)</td><td>0.04 (-5.32%)</td><td>0.01 <b>(+55.95%)</b></td><td>217.20 (+5.59%)</td><td>165.18 (-2.97%)</td><td>176.10 (+5.26%)</td><td>110.80 (-18.77%)</td><td>41.69 <b>(+30.86%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>170.24 (n/a)</td><td>167.30 (n/a)</td><td>136.40 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.11 <b>(+22.40%)</b></td><td>0.08 (+19.01%)</td><td>0.08 (+12.62%)</td><td>0.06 (+8.76%)</td><td>0.02 <b>(+38.18%)</b></td><td>214.70 (-8.05%)</td><td>160.04 (-14.84%)</td><td>163.00 (-11.17%)</td><td>111.20 (-18.36%)</td><td>37.63 (+4.72%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>187.92 (n/a)</td><td>183.50 (n/a)</td><td>136.20 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-16.30%)</td><td>0.05 (-11.66%)</td><td>0.04 (-15.36%)</td><td>0.04 (-8.95%)</td><td>0.01 <b>(-26.39%)</b></td><td>212.30 (+9.83%)</td><td>180.68 (+12.46%)</td><td>188.90 (+18.14%)</td><td>155.30 (+19.46%)</td><td>24.48 (-6.20%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>160.66 (n/a)</td><td>159.90 (n/a)</td><td>130.00 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (+7.38%)</td><td>0.06 (+7.00%)</td><td>0.06 <b>(+23.22%)</b></td><td>0.05 (-0.22%)</td><td>0.01 (+6.53%)</td><td>221.10 (+0.23%)</td><td>175.50 (-6.35%)</td><td>163.80 (-18.83%)</td><td>138.40 (-6.86%)</td><td>33.53 (+1.87%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>187.40 (n/a)</td><td>201.80 (n/a)</td><td>148.60 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (-12.16%)</td><td>0.05 (+1.83%)</td><td>0.05 <b>(+20.19%)</b></td><td>0.04 (-5.51%)</td><td>0.01 <b>(-34.60%)</b></td><td>212.70 (+5.82%)</td><td>168.38 (-3.15%)</td><td>157.10 (-16.79%)</td><td>154.30 (+13.87%)</td><td>25.04 <b>(-21.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>173.86 (n/a)</td><td>188.80 (n/a)</td><td>135.50 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-11.98%)</td><td>0.05 (+5.91%)</td><td>0.06 (+13.61%)</td><td>0.04 (+8.80%)</td><td>0.01 <b>(-44.70%)</b></td><td>242.10 (-8.09%)</td><td>193.84 (-8.16%)</td><td>181.70 (-11.97%)</td><td>178.80 (+13.60%)</td><td>27.08 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>263.40 (n/a)</td><td>211.06 (n/a)</td><td>206.40 (n/a)</td><td>157.40 (n/a)</td><td>47.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-4.88%)</td><td>0.05 (+8.13%)</td><td>0.05 (+5.18%)</td><td>0.04 <b>(+31.48%)</b></td><td>0.01 <b>(-36.75%)</b></td><td>201.70 <b>(-23.94%)</b></td><td>175.02 (-10.32%)</td><td>180.10 (-4.91%)</td><td>146.20 (+5.10%)</td><td>23.62 <b>(-49.89%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.20 (n/a)</td><td>195.16 (n/a)</td><td>189.40 (n/a)</td><td>139.10 (n/a)</td><td>47.14 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+1.99%)</td><td>0.05 (+3.26%)</td><td>0.05 (+5.65%)</td><td>0.04 (+11.29%)</td><td>0.01 (+0.45%)</td><td>218.90 (-10.18%)</td><td>186.30 (-3.39%)</td><td>177.30 (-5.39%)</td><td>159.60 (-1.97%)</td><td>26.87 (-12.88%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>192.84 (n/a)</td><td>187.40 (n/a)</td><td>162.80 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+1.27%)</td><td>0.05 (-0.81%)</td><td>0.04 (-6.80%)</td><td>0.04 (+3.25%)</td><td>0.01 (+1.00%)</td><td>216.00 (-3.14%)</td><td>178.96 (+0.73%)</td><td>183.70 (+7.30%)</td><td>142.10 (-1.25%)</td><td>28.49 (-5.17%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>177.66 (n/a)</td><td>171.20 (n/a)</td><td>143.90 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.07 (-11.61%)</td><td>0.05 (-1.64%)</td><td>0.05 (-7.41%)</td><td>0.04 (+0.74%)</td><td>0.02 (-10.41%)</td><td>231.50 (-0.73%)</td><td>178.58 (+1.24%)</td><td>199.10 (+7.97%)</td><td>124.70 (+13.16%)</td><td>46.08 (+1.70%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>176.40 (n/a)</td><td>184.40 (n/a)</td><td>110.20 (n/a)</td><td>45.31 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+0.85%)</td><td>0.05 (+4.67%)</td><td>0.05 (+14.61%)</td><td>0.04 (+7.37%)</td><td>0.01 (-15.97%)</td><td>199.00 (-6.88%)</td><td>170.92 (-5.07%)</td><td>159.30 (-12.76%)</td><td>148.00 (-0.87%)</td><td>21.92 <b>(-20.49%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>180.04 (n/a)</td><td>182.60 (n/a)</td><td>149.30 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (-10.66%)</td><td>0.05 (-0.57%)</td><td>0.04 (-7.95%)</td><td>0.04 (+5.08%)</td><td>0.01 (-18.62%)</td><td>233.60 (-4.85%)</td><td>194.82 (-0.36%)</td><td>210.10 (+8.63%)</td><td>155.20 (+11.98%)</td><td>33.64 (-12.38%)</td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>195.52 (n/a)</td><td>193.40 (n/a)</td><td>138.60 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.06 (+12.90%)</td><td>0.04 (-0.46%)</td><td>0.04 (-6.57%)</td><td>0.03 (-13.35%)</td><td>0.01 <b>(+81.58%)</b></td><td>252.50 (+15.40%)</td><td>197.18 (+2.93%)</td><td>203.40 (+7.00%)</td><td>147.60 (-11.40%)</td><td>40.75 <b>(+83.63%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>191.56 (n/a)</td><td>190.10 (n/a)</td><td>166.60 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 <b>(-28.35%)</b></td><td>0.05 (-2.48%)</td><td>0.04 (+7.41%)</td><td>0.04 (+3.92%)</td><td>0.01 <b>(-52.19%)</b></td><td>221.70 (-3.78%)</td><td>194.44 (-2.19%)</td><td>208.00 (-6.89%)</td><td>160.50 <b>(+39.57%)</b></td><td>31.38 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>198.80 (n/a)</td><td>223.40 (n/a)</td><td>115.00 (n/a)</td><td>48.32 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.05 (+4.90%)</td><td>0.03 (-10.25%)</td><td>0.03 (-9.11%)</td><td>0.02 <b>(-32.72%)</b></td><td>0.01 <b>(+186.96%)</b></td><td>343.00 <b>(+48.61%)</b></td><td>255.32 (+17.99%)</td><td>239.90 (+10.00%)</td><td>178.80 (-4.69%)</td><td>71.48 <b>(+316.21%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.80 (n/a)</td><td>216.40 (n/a)</td><td>218.10 (n/a)</td><td>187.60 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.71 (+5.10%)</td><td>0.56 (-2.14%)</td><td>0.63 (+5.19%)</td><td>0.29 <b>(-38.76%)</b></td><td>0.18 <b>(+81.10%)</b></td><td>340.90 <b>(+63.27%)</b></td><td>195.06 (+11.71%)</td><td>157.20 (-4.90%)</td><td>138.00 (-4.83%)</td><td>85.07 <b>(+179.27%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.68 (n/a)</td><td>0.58 (n/a)</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.10 (n/a)</td><td>208.80 (n/a)</td><td>174.62 (n/a)</td><td>165.30 (n/a)</td><td>145.00 (n/a)</td><td>30.46 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.62 <b>(-25.28%)</b></td><td>0.56 (-2.14%)</td><td>0.55 (+3.93%)</td><td>0.48 (+10.18%)</td><td>0.05 <b>(-64.64%)</b></td><td>204.40 (-9.28%)</td><td>177.40 (-1.82%)</td><td>178.20 (-3.78%)</td><td>157.40 <b>(+33.84%)</b></td><td>17.92 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.15 (n/a)</td><td>225.30 (n/a)</td><td>180.68 (n/a)</td><td>185.20 (n/a)</td><td>117.60 (n/a)</td><td>39.59 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.70 (-11.48%)</td><td>0.60 (+1.58%)</td><td>0.58 (+0.62%)</td><td>0.50 (+11.36%)</td><td>0.10 <b>(-25.98%)</b></td><td>198.50 (-10.18%)</td><td>168.42 (-3.16%)</td><td>170.60 (-0.58%)</td><td>139.80 (+13.02%)</td><td>27.41 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.79 (n/a)</td><td>0.59 (n/a)</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.13 (n/a)</td><td>221.00 (n/a)</td><td>173.92 (n/a)</td><td>171.60 (n/a)</td><td>123.70 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.69 (+8.55%)</td><td>0.56 (+10.70%)</td><td>0.54 (+11.78%)</td><td>0.49 <b>(+21.19%)</b></td><td>0.08 <b>(-27.75%)</b></td><td>202.00 (-17.48%)</td><td>179.14 (-11.65%)</td><td>182.00 (-10.57%)</td><td>142.80 (-7.87%)</td><td>22.05 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.11 (n/a)</td><td>244.80 (n/a)</td><td>202.76 (n/a)</td><td>203.50 (n/a)</td><td>155.00 (n/a)</td><td>42.21 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.52 (+12.10%)</td><td>0.46 (+11.08%)</td><td>0.50 <b>(+23.77%)</b></td><td>0.32 (-13.20%)</td><td>0.08 <b>(+138.05%)</b></td><td>231.50 (+15.23%)</td><td>167.52 (-7.41%)</td><td>146.70 (-19.22%)</td><td>141.10 (-10.81%)</td><td>37.80 <b>(+149.04%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>200.90 (n/a)</td><td>180.92 (n/a)</td><td>181.60 (n/a)</td><td>158.20 (n/a)</td><td>15.18 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.56 <b>(+34.83%)</b></td><td>0.47 <b>(+22.38%)</b></td><td>0.49 <b>(+23.26%)</b></td><td>0.31 (-8.87%)</td><td>0.10 <b>(+184.52%)</b></td><td>238.30 (+9.71%)</td><td>164.16 (-15.27%)</td><td>149.90 (-18.89%)</td><td>131.00 <b>(-25.82%)</b></td><td>42.52 <b>(+142.70%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.03 (n/a)</td><td>217.20 (n/a)</td><td>193.74 (n/a)</td><td>184.80 (n/a)</td><td>176.60 (n/a)</td><td>17.52 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.51 (+18.96%)</td><td>0.44 (+7.22%)</td><td>0.44 (+5.83%)</td><td>0.39 (+6.33%)</td><td>0.05 <b>(+87.06%)</b></td><td>188.80 (-5.98%)</td><td>169.02 (-6.21%)</td><td>166.90 (-5.49%)</td><td>143.30 (-15.95%)</td><td>17.44 <b>(+45.54%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.03 (n/a)</td><td>200.80 (n/a)</td><td>180.22 (n/a)</td><td>176.60 (n/a)</td><td>170.50 (n/a)</td><td>11.98 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.51 (-11.70%)</td><td>0.41 (+0.01%)</td><td>0.37 (+11.72%)</td><td>0.34 (+4.59%)</td><td>0.08 <b>(-29.46%)</b></td><td>218.50 (-4.38%)</td><td>185.52 (-2.87%)</td><td>199.20 (-10.47%)</td><td>144.90 (+13.20%)</td><td>35.87 <b>(-26.78%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.58 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>228.50 (n/a)</td><td>191.00 (n/a)</td><td>222.50 (n/a)</td><td>128.00 (n/a)</td><td>48.99 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.79 (-1.59%)</td><td>0.75 (+3.45%)</td><td>0.75 (+4.12%)</td><td>0.69 (+6.38%)</td><td>0.04 <b>(-36.72%)</b></td><td>188.80 (-5.98%)</td><td>175.62 (-3.64%)</td><td>174.30 (-3.97%)</td><td>166.20 (+1.65%)</td><td>8.90 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.72 (n/a)</td><td>0.65 (n/a)</td><td>0.06 (n/a)</td><td>200.80 (n/a)</td><td>182.26 (n/a)</td><td>181.50 (n/a)</td><td>163.50 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.89 (+4.95%)</td><td>0.75 (+4.43%)</td><td>0.74 (-7.11%)</td><td>0.68 <b>(+27.86%)</b></td><td>0.08 <b>(-40.98%)</b></td><td>192.40 <b>(-21.82%)</b></td><td>176.08 (-6.65%)</td><td>178.00 (+7.62%)</td><td>147.00 (-4.73%)</td><td>17.67 <b>(-56.41%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.85 (n/a)</td><td>0.72 (n/a)</td><td>0.79 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>246.10 (n/a)</td><td>188.62 (n/a)</td><td>165.40 (n/a)</td><td>154.30 (n/a)</td><td>40.53 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.88 (+4.48%)</td><td>0.72 (-0.30%)</td><td>0.68 (-8.87%)</td><td>0.64 <b>(+42.38%)</b></td><td>0.09 <b>(-39.92%)</b></td><td>203.30 <b>(-29.78%)</b></td><td>184.74 (-3.55%)</td><td>191.90 (+9.72%)</td><td>149.60 (-4.29%)</td><td>21.53 <b>(-61.28%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.84 (n/a)</td><td>0.72 (n/a)</td><td>0.75 (n/a)</td><td>0.45 (n/a)</td><td>0.16 (n/a)</td><td>289.50 (n/a)</td><td>191.54 (n/a)</td><td>174.90 (n/a)</td><td>156.30 (n/a)</td><td>55.60 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.00 (-6.52%)</td><td>0.00 (-5.00%)</td><td>0.00 (-2.27%)</td><td>0.00 (-4.76%)</td><td>0.00 (+3.92%)</td><td>1027.44 (+5.97%)</td><td>982.05 (+5.63%)</td><td>954.62 (+2.60%)</td><td>950.15 (+5.89%)</td><td>40.94 <b>(+36.46%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>969.52 (n/a)</td><td>929.70 (n/a)</td><td>930.40 (n/a)</td><td>897.28 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.01 (+0.00%)</td><td>0.01 (-1.47%)</td><td>0.01 (+1.23%)</td><td>0.01 (-8.75%)</td><td>0.00 <b>(+134.23%)</b></td><td>1122.74 (+9.75%)</td><td>1020.83 (+1.84%)</td><td>1004.23 (-0.74%)</td><td>961.96 (-0.19%)</td><td>60.40 <b>(+160.38%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1022.96 (n/a)</td><td>1002.36 (n/a)</td><td>1011.75 (n/a)</td><td>963.76 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>0.94 (-0.71%)</td><td>0.93 (-1.13%)</td><td>0.93 (-1.05%)</td><td>0.92 (-1.58%)</td><td>0.01 <b>(+65.91%)</b></td><td>2276.66 (+1.61%)</td><td>2253.67 (+1.15%)</td><td>2256.59 (+1.06%)</td><td>2228.69 (+0.71%)</td><td>21.12 <b>(+70.37%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2240.51 (n/a)</td><td>2228.10 (n/a)</td><td>2232.86 (n/a)</td><td>2212.98 (n/a)</td><td>12.40 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.33 (+0.20%)</td><td>3.08 (+11.23%)</td><td>3.05 (+15.63%)</td><td>2.68 (+13.04%)</td><td>0.26 <b>(-35.76%)</b></td><td>195.40 (-11.50%)</td><td>171.22 (-10.98%)</td><td>171.70 (-13.50%)</td><td>157.60 (-0.19%)</td><td>15.03 <b>(-43.10%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>3.32 (n/a)</td><td>2.77 (n/a)</td><td>2.64 (n/a)</td><td>2.37 (n/a)</td><td>0.40 (n/a)</td><td>220.80 (n/a)</td><td>192.34 (n/a)</td><td>198.50 (n/a)</td><td>157.90 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>6.17 (+18.00%)</td><td>4.87 (+2.93%)</td><td>4.56 (-3.03%)</td><td>4.15 (-1.89%)</td><td>0.80 <b>(+76.95%)</b></td><td>252.90 (+1.93%)</td><td>219.36 (-1.68%)</td><td>229.70 (+3.10%)</td><td>169.90 (-15.22%)</td><td>32.01 <b>(+50.72%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>5.23 (n/a)</td><td>4.73 (n/a)</td><td>4.71 (n/a)</td><td>4.23 (n/a)</td><td>0.45 (n/a)</td><td>248.10 (n/a)</td><td>223.10 (n/a)</td><td>222.80 (n/a)</td><td>200.40 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>ece908d</code> — 2026-07-31 18:28:17</td><td>3.13 (+12.06%)</td><td>2.81 (+6.94%)</td><td>2.87 (+7.15%)</td><td>2.44 (+5.01%)</td><td>0.27 <b>(+47.47%)</b></td><td>215.20 (-4.78%)</td><td>187.84 (-6.18%)</td><td>183.00 (-6.68%)</td><td>167.60 (-10.76%)</td><td>18.40 <b>(+23.95%)</b></td>
</tr>
<tr>
<td><code>826c238</code> — 2026-07-28 16:39:37</td><td>2.79 (n/a)</td><td>2.63 (n/a)</td><td>2.67 (n/a)</td><td>2.32 (n/a)</td><td>0.18 (n/a)</td><td>226.00 (n/a)</td><td>200.22 (n/a)</td><td>196.10 (n/a)</td><td>187.80 (n/a)</td><td>14.84 (n/a)</td>
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
