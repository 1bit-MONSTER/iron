# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+2.10%)</td><td>0.03 (+7.00%)</td><td>0.03 (+6.40%)</td><td>0.03 (+17.78%)</td><td>0.00 (-8.93%)</td><td>213.50 (-15.08%)</td><td>184.08 (-7.24%)</td><td>178.40 (-6.06%)</td><td>157.00 (-2.06%)</td><td>27.12 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.40 (n/a)</td><td>198.44 (n/a)</td><td>189.90 (n/a)</td><td>160.30 (n/a)</td><td>35.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 <b>(-22.83%)</b></td><td>0.03 (-9.71%)</td><td>0.03 (-8.30%)</td><td>0.03 (-8.02%)</td><td>0.00 <b>(-59.85%)</b></td><td>206.00 (+8.71%)</td><td>185.62 (+9.37%)</td><td>185.90 (+9.10%)</td><td>172.60 <b>(+29.58%)</b></td><td>12.99 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>169.72 (n/a)</td><td>170.40 (n/a)</td><td>133.20 (n/a)</td><td>22.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-10.24%)</td><td>0.03 (-5.02%)</td><td>0.03 (-12.12%)</td><td>0.03 (+15.12%)</td><td>0.00 <b>(-41.05%)</b></td><td>210.70 (-13.15%)</td><td>185.12 (+2.40%)</td><td>197.10 (+13.80%)</td><td>155.80 (+11.37%)</td><td>24.45 <b>(-42.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.60 (n/a)</td><td>180.78 (n/a)</td><td>173.20 (n/a)</td><td>139.90 (n/a)</td><td>42.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-11.96%)</td><td>0.04 (-1.49%)</td><td>0.03 (+3.33%)</td><td>0.03 (+17.57%)</td><td>0.01 <b>(-35.66%)</b></td><td>210.00 (-14.95%)</td><td>179.98 (-1.90%)</td><td>185.10 (-3.24%)</td><td>132.90 (+13.59%)</td><td>29.43 <b>(-37.23%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>183.46 (n/a)</td><td>191.30 (n/a)</td><td>117.00 (n/a)</td><td>46.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 <b>(+43.66%)</b></td><td>0.03 (+11.92%)</td><td>0.03 (+1.23%)</td><td>0.02 (-7.51%)</td><td>0.01 <b>(+173.52%)</b></td><td>266.90 (+8.10%)</td><td>192.62 (-6.48%)</td><td>190.80 (-1.19%)</td><td>129.70 <b>(-30.38%)</b></td><td>50.68 <b>(+103.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.90 (n/a)</td><td>205.96 (n/a)</td><td>193.10 (n/a)</td><td>186.30 (n/a)</td><td>24.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+17.28%)</td><td>0.04 <b>(+29.95%)</b></td><td>0.04 <b>(+21.29%)</b></td><td>0.03 <b>(+56.22%)</b></td><td>0.00 <b>(-68.45%)</b></td><td>182.00 <b>(-35.98%)</b></td><td>174.00 <b>(-24.58%)</b></td><td>175.50 (-17.57%)</td><td>164.20 (-14.75%)</td><td>6.57 <b>(-82.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>284.30 (n/a)</td><td>230.70 (n/a)</td><td>212.90 (n/a)</td><td>192.60 (n/a)</td><td>38.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-4.71%)</td><td>0.03 (-8.37%)</td><td>0.03 (-13.84%)</td><td>0.03 (+0.21%)</td><td>0.00 <b>(-24.54%)</b></td><td>208.50 (-0.24%)</td><td>196.56 (+8.50%)</td><td>205.40 (+16.11%)</td><td>163.10 (+4.95%)</td><td>19.26 <b>(-22.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>181.16 (n/a)</td><td>176.90 (n/a)</td><td>155.40 (n/a)</td><td>24.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+16.94%)</td><td>0.03 (+15.92%)</td><td>0.03 (+5.79%)</td><td>0.03 <b>(+22.06%)</b></td><td>0.01 <b>(+27.26%)</b></td><td>218.10 (-18.10%)</td><td>189.00 (-13.52%)</td><td>205.50 (-5.47%)</td><td>152.00 (-14.46%)</td><td>30.44 (-11.42%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>266.30 (n/a)</td><td>218.54 (n/a)</td><td>217.40 (n/a)</td><td>177.70 (n/a)</td><td>34.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (+3.87%)</td><td>0.08 (-6.49%)</td><td>0.08 (-12.92%)</td><td>0.06 (-9.52%)</td><td>0.02 (+5.91%)</td><td>206.00 (+10.52%)</td><td>158.64 (+7.70%)</td><td>145.70 (+14.81%)</td><td>117.80 (-3.76%)</td><td>36.22 (+15.60%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>147.30 (n/a)</td><td>126.90 (n/a)</td><td>122.40 (n/a)</td><td>31.33 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 <b>(+22.90%)</b></td><td>0.08 <b>(+27.17%)</b></td><td>0.08 <b>(+24.98%)</b></td><td>0.06 (+15.75%)</td><td>0.02 <b>(+26.74%)</b></td><td>212.90 (-13.60%)</td><td>154.52 <b>(-20.98%)</b></td><td>156.70 (-19.97%)</td><td>110.00 (-18.58%)</td><td>40.02 (-12.72%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>246.40 (n/a)</td><td>195.54 (n/a)</td><td>195.80 (n/a)</td><td>135.10 (n/a)</td><td>45.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 <b>(+20.61%)</b></td><td>0.08 (+12.06%)</td><td>0.07 (+7.60%)</td><td>0.06 (+10.33%)</td><td>0.01 <b>(+23.48%)</b></td><td>199.50 (-9.36%)</td><td>167.28 (-10.51%)</td><td>174.20 (-7.04%)</td><td>128.50 (-17.10%)</td><td>28.02 (-7.38%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>186.92 (n/a)</td><td>187.40 (n/a)</td><td>155.00 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (+3.46%)</td><td>0.07 (+3.48%)</td><td>0.07 (+7.51%)</td><td>0.05 (+3.33%)</td><td>0.01 <b>(+25.36%)</b></td><td>224.10 (-3.24%)</td><td>179.82 (-2.56%)</td><td>169.50 (-7.02%)</td><td>146.90 (-3.36%)</td><td>33.63 (+14.80%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>184.54 (n/a)</td><td>182.30 (n/a)</td><td>152.00 (n/a)</td><td>29.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (+12.17%)</td><td>0.08 (+13.57%)</td><td>0.08 (+12.58%)</td><td>0.06 (+0.30%)</td><td>0.01 <b>(+53.40%)</b></td><td>212.70 (-0.28%)</td><td>163.78 (-10.89%)</td><td>159.80 (-11.22%)</td><td>139.70 (-10.91%)</td><td>29.84 <b>(+35.35%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>183.80 (n/a)</td><td>180.00 (n/a)</td><td>156.80 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 <b>(+20.80%)</b></td><td>0.08 <b>(+25.61%)</b></td><td>0.07 <b>(+45.21%)</b></td><td>0.05 <b>(+22.48%)</b></td><td>0.02 (+3.28%)</td><td>240.90 (-18.37%)</td><td>168.40 <b>(-21.96%)</b></td><td>164.90 <b>(-31.12%)</b></td><td>114.80 (-17.23%)</td><td>46.19 <b>(-27.65%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>295.10 (n/a)</td><td>215.78 (n/a)</td><td>239.40 (n/a)</td><td>138.70 (n/a)</td><td>63.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 <b>(+47.90%)</b></td><td>0.07 (+13.33%)</td><td>0.07 (+2.28%)</td><td>0.04 (+1.42%)</td><td>0.02 <b>(+95.17%)</b></td><td>299.00 (-1.42%)</td><td>193.76 (-6.85%)</td><td>187.00 (-2.25%)</td><td>115.40 <b>(-32.40%)</b></td><td>68.24 <b>(+25.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>303.30 (n/a)</td><td>208.00 (n/a)</td><td>191.30 (n/a)</td><td>170.70 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-14.61%)</td><td>0.07 (-6.67%)</td><td>0.07 (-4.36%)</td><td>0.06 (-0.47%)</td><td>0.01 <b>(-40.96%)</b></td><td>212.70 (+0.42%)</td><td>180.22 (+5.91%)</td><td>171.10 (+4.52%)</td><td>166.20 (+17.12%)</td><td>19.03 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>170.16 (n/a)</td><td>163.70 (n/a)</td><td>141.90 (n/a)</td><td>27.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (+2.79%)</td><td>0.14 (-10.88%)</td><td>0.12 (-19.85%)</td><td>0.12 (-7.05%)</td><td>0.02 <b>(+32.14%)</b></td><td>202.20 (+7.61%)</td><td>183.42 (+13.14%)</td><td>196.70 <b>(+24.73%)</b></td><td>141.90 (-2.67%)</td><td>25.61 <b>(+40.27%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>187.90 (n/a)</td><td>162.12 (n/a)</td><td>157.70 (n/a)</td><td>145.80 (n/a)</td><td>18.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (+17.74%)</td><td>0.14 (-2.39%)</td><td>0.13 (-14.58%)</td><td>0.12 (+0.87%)</td><td>0.03 <b>(+53.07%)</b></td><td>206.00 (-0.87%)</td><td>184.58 (+3.63%)</td><td>191.90 (+17.08%)</td><td>135.00 (-15.09%)</td><td>28.79 <b>(+26.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>178.12 (n/a)</td><td>163.90 (n/a)</td><td>159.00 (n/a)</td><td>22.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (+19.43%)</td><td>0.16 (-0.15%)</td><td>0.16 (-3.33%)</td><td>0.12 (-10.51%)</td><td>0.04 <b>(+93.44%)</b></td><td>210.60 (+11.78%)</td><td>157.72 (+2.95%)</td><td>152.60 (+3.39%)</td><td>116.10 (-16.29%)</td><td>35.62 <b>(+77.95%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.40 (n/a)</td><td>153.20 (n/a)</td><td>147.60 (n/a)</td><td>138.70 (n/a)</td><td>20.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 <b>(+22.25%)</b></td><td>0.16 <b>(+20.19%)</b></td><td>0.16 <b>(+22.02%)</b></td><td>0.14 (+19.65%)</td><td>0.02 (+15.02%)</td><td>178.70 (-16.42%)</td><td>155.30 (-16.93%)</td><td>154.40 (-18.09%)</td><td>127.80 (-18.18%)</td><td>19.94 <b>(-22.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>186.96 (n/a)</td><td>188.50 (n/a)</td><td>156.20 (n/a)</td><td>25.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (+14.59%)</td><td>0.14 (-0.49%)</td><td>0.16 (+13.74%)</td><td>0.09 <b>(-31.45%)</b></td><td>0.04 <b>(+230.55%)</b></td><td>272.70 <b>(+45.91%)</b></td><td>182.66 (+6.87%)</td><td>150.20 (-12.06%)</td><td>137.40 (-12.71%)</td><td>56.94 <b>(+323.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>170.92 (n/a)</td><td>170.80 (n/a)</td><td>157.40 (n/a)</td><td>13.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 <b>(+26.55%)</b></td><td>0.17 (+10.25%)</td><td>0.15 (+7.24%)</td><td>0.14 (+10.01%)</td><td>0.03 <b>(+56.70%)</b></td><td>173.00 (-9.09%)</td><td>152.48 (-8.17%)</td><td>163.30 (-6.79%)</td><td>109.20 <b>(-21.04%)</b></td><td>26.57 (+13.40%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>166.04 (n/a)</td><td>175.20 (n/a)</td><td>138.30 (n/a)</td><td>23.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (+13.26%)</td><td>0.13 (+2.40%)</td><td>0.12 (+0.62%)</td><td>0.11 (-5.05%)</td><td>0.03 <b>(+70.65%)</b></td><td>227.00 (+5.34%)</td><td>194.02 (-0.32%)</td><td>206.80 (-0.62%)</td><td>144.40 (-11.68%)</td><td>37.13 <b>(+61.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.50 (n/a)</td><td>194.64 (n/a)</td><td>208.10 (n/a)</td><td>163.50 (n/a)</td><td>23.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (-3.33%)</td><td>0.12 (-12.28%)</td><td>0.12 (-7.09%)</td><td>0.07 <b>(-40.05%)</b></td><td>0.03 <b>(+82.17%)</b></td><td>364.50 <b>(+66.82%)</b></td><td>228.54 <b>(+22.03%)</b></td><td>205.10 (+7.61%)</td><td>156.10 (+3.45%)</td><td>81.14 <b>(+233.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.50 (n/a)</td><td>187.28 (n/a)</td><td>190.60 (n/a)</td><td>150.90 (n/a)</td><td>24.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (+2.26%)</td><td>0.31 <b>(+20.11%)</b></td><td>0.32 (+14.40%)</td><td>0.25 <b>(+49.76%)</b></td><td>0.04 <b>(-34.89%)</b></td><td>198.40 <b>(-33.24%)</b></td><td>159.34 <b>(-20.44%)</b></td><td>154.40 (-12.57%)</td><td>138.80 (-2.18%)</td><td>24.60 <b>(-59.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>297.20 (n/a)</td><td>200.28 (n/a)</td><td>176.60 (n/a)</td><td>141.90 (n/a)</td><td>60.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (+0.53%)</td><td>0.30 (+15.31%)</td><td>0.30 (+16.60%)</td><td>0.24 (+16.97%)</td><td>0.05 (-10.70%)</td><td>209.10 (-14.51%)</td><td>167.62 (-14.32%)</td><td>166.00 (-14.26%)</td><td>138.70 (-0.57%)</td><td>30.04 <b>(-25.42%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>244.60 (n/a)</td><td>195.64 (n/a)</td><td>193.60 (n/a)</td><td>139.50 (n/a)</td><td>40.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.32 (+1.67%)</td><td>0.30 (+13.46%)</td><td>0.32 (+17.54%)</td><td>0.25 (+5.47%)</td><td>0.03 (-3.49%)</td><td>194.30 (-5.17%)</td><td>163.36 (-11.96%)</td><td>155.60 (-14.93%)</td><td>154.00 (-1.66%)</td><td>17.35 (-8.98%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>204.90 (n/a)</td><td>185.56 (n/a)</td><td>182.90 (n/a)</td><td>156.60 (n/a)</td><td>19.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (-8.34%)</td><td>0.29 (+9.76%)</td><td>0.31 (+13.69%)</td><td>0.26 <b>(+27.51%)</b></td><td>0.03 <b>(-53.04%)</b></td><td>188.50 <b>(-21.59%)</b></td><td>169.86 (-11.70%)</td><td>158.70 (-12.03%)</td><td>156.40 (+9.14%)</td><td>16.41 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>240.40 (n/a)</td><td>192.36 (n/a)</td><td>180.40 (n/a)</td><td>143.30 (n/a)</td><td>42.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.37 <b>(+31.85%)</b></td><td>0.30 (+15.80%)</td><td>0.30 (+12.51%)</td><td>0.22 (-2.29%)</td><td>0.05 <b>(+136.02%)</b></td><td>220.30 (+2.37%)</td><td>170.86 (-11.80%)</td><td>164.50 (-11.13%)</td><td>132.90 <b>(-24.14%)</b></td><td>32.54 <b>(+83.23%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>193.72 (n/a)</td><td>185.10 (n/a)</td><td>175.20 (n/a)</td><td>17.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (-11.54%)</td><td>0.25 (-17.29%)</td><td>0.27 (-8.65%)</td><td>0.12 <b>(-52.64%)</b></td><td>0.08 <b>(+111.00%)</b></td><td>411.60 <b>(+111.08%)</b></td><td>226.64 <b>(+34.99%)</b></td><td>184.30 (+9.44%)</td><td>157.30 (+13.00%)</td><td>105.78 <b>(+428.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>195.00 (n/a)</td><td>167.90 (n/a)</td><td>168.40 (n/a)</td><td>139.20 (n/a)</td><td>20.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.45 <b>(+72.54%)</b></td><td>0.29 <b>(+23.97%)</b></td><td>0.27 (+16.07%)</td><td>0.16 (-18.70%)</td><td>0.11 <b>(+366.70%)</b></td><td>304.20 <b>(+23.01%)</b></td><td>190.98 (-10.21%)</td><td>183.60 (-13.84%)</td><td>108.20 <b>(-42.02%)</b></td><td>73.27 <b>(+229.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>247.30 (n/a)</td><td>212.70 (n/a)</td><td>213.10 (n/a)</td><td>186.60 (n/a)</td><td>22.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.35 (+8.73%)</td><td>0.25 (-1.25%)</td><td>0.23 (+0.10%)</td><td>0.16 <b>(-21.39%)</b></td><td>0.07 <b>(+51.95%)</b></td><td>312.80 <b>(+27.21%)</b></td><td>215.40 (+5.91%)</td><td>209.70 (-0.10%)</td><td>140.00 (-8.02%)</td><td>65.44 <b>(+79.78%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>245.90 (n/a)</td><td>203.38 (n/a)</td><td>209.90 (n/a)</td><td>152.20 (n/a)</td><td>36.40 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+18.10%)</td><td>0.02 (+16.39%)</td><td>0.02 (+11.70%)</td><td>0.01 (+6.38%)</td><td>0.00 <b>(+49.67%)</b></td><td>194.30 (-6.00%)</td><td>144.12 (-12.61%)</td><td>148.50 (-10.49%)</td><td>110.50 (-15.26%)</td><td>32.96 (+17.48%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>164.92 (n/a)</td><td>165.90 (n/a)</td><td>130.40 (n/a)</td><td>28.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 <b>(+25.22%)</b></td><td>0.02 (+5.89%)</td><td>0.02 (+0.26%)</td><td>0.01 (-1.86%)</td><td>0.00 <b>(+182.13%)</b></td><td>181.10 (+1.86%)</td><td>155.86 (-4.32%)</td><td>161.00 (-0.25%)</td><td>123.90 <b>(-20.12%)</b></td><td>20.77 <b>(+123.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>177.80 (n/a)</td><td>162.90 (n/a)</td><td>161.40 (n/a)</td><td>155.10 (n/a)</td><td>9.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 <b>(+23.64%)</b></td><td>0.02 (+11.27%)</td><td>0.02 (-0.29%)</td><td>0.01 (+4.85%)</td><td>0.00 <b>(+95.91%)</b></td><td>192.10 (-4.62%)</td><td>156.36 (-7.51%)</td><td>160.20 (+0.31%)</td><td>116.80 (-19.17%)</td><td>35.60 <b>(+50.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.40 (n/a)</td><td>169.06 (n/a)</td><td>159.70 (n/a)</td><td>144.50 (n/a)</td><td>23.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+3.13%)</td><td>0.02 (+1.75%)</td><td>0.02 (+6.23%)</td><td>0.01 (-12.23%)</td><td>0.00 <b>(+28.17%)</b></td><td>273.70 (+13.95%)</td><td>177.36 (+0.90%)</td><td>157.30 (-5.86%)</td><td>135.90 (-3.07%)</td><td>54.92 <b>(+44.64%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>240.20 (n/a)</td><td>175.78 (n/a)</td><td>167.10 (n/a)</td><td>140.20 (n/a)</td><td>37.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+19.21%)</td><td>0.02 (-0.62%)</td><td>0.02 (-2.62%)</td><td>0.01 <b>(-28.85%)</b></td><td>0.00 <b>(+386.18%)</b></td><td>241.00 <b>(+40.52%)</b></td><td>175.14 (+8.14%)</td><td>167.70 (+2.69%)</td><td>122.80 (-16.06%)</td><td>53.30 <b>(+465.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.50 (n/a)</td><td>161.96 (n/a)</td><td>163.30 (n/a)</td><td>146.30 (n/a)</td><td>9.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+8.24%)</td><td>0.01 (-4.10%)</td><td>0.01 (-1.96%)</td><td>0.01 (-14.34%)</td><td>0.00 <b>(+117.54%)</b></td><td>224.50 (+16.68%)</td><td>186.12 (+6.27%)</td><td>179.20 (+1.99%)</td><td>144.50 (-7.61%)</td><td>31.44 <b>(+136.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>175.14 (n/a)</td><td>175.70 (n/a)</td><td>156.40 (n/a)</td><td>13.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+3.72%)</td><td>0.01 (-7.32%)</td><td>0.01 (-8.78%)</td><td>0.01 <b>(-28.27%)</b></td><td>0.00 <b>(+156.75%)</b></td><td>267.90 <b>(+39.39%)</b></td><td>196.16 (+11.68%)</td><td>189.00 (+9.63%)</td><td>156.60 (-3.57%)</td><td>45.64 <b>(+239.09%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>175.64 (n/a)</td><td>172.40 (n/a)</td><td>162.40 (n/a)</td><td>13.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+8.99%)</td><td>0.01 <b>(+20.88%)</b></td><td>0.01 <b>(+22.52%)</b></td><td>0.01 <b>(+54.14%)</b></td><td>0.00 <b>(-23.69%)</b></td><td>240.50 <b>(-35.12%)</b></td><td>198.34 <b>(-21.14%)</b></td><td>190.50 (-18.38%)</td><td>160.70 (-8.28%)</td><td>37.24 <b>(-53.61%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>370.70 (n/a)</td><td>251.50 (n/a)</td><td>233.40 (n/a)</td><td>175.20 (n/a)</td><td>80.26 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+10.55%)</td><td>0.03 (+2.73%)</td><td>0.03 (-11.88%)</td><td>0.03 <b>(+65.33%)</b></td><td>0.01 <b>(-34.22%)</b></td><td>209.20 <b>(-39.52%)</b></td><td>170.32 (-10.67%)</td><td>174.50 (+13.46%)</td><td>128.00 (-9.54%)</td><td>29.26 <b>(-66.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.90 (n/a)</td><td>190.66 (n/a)</td><td>153.80 (n/a)</td><td>141.50 (n/a)</td><td>87.16 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+14.20%)</td><td>0.03 (-1.54%)</td><td>0.03 (-13.33%)</td><td>0.03 (-0.57%)</td><td>0.00 <b>(+43.99%)</b></td><td>178.30 (+0.56%)</td><td>161.86 (+2.29%)</td><td>170.70 (+15.42%)</td><td>126.50 (-12.40%)</td><td>21.18 <b>(+24.61%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>158.24 (n/a)</td><td>147.90 (n/a)</td><td>144.40 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-12.70%)</td><td>0.03 (-4.98%)</td><td>0.03 (-6.75%)</td><td>0.03 (+6.28%)</td><td>0.00 <b>(-50.81%)</b></td><td>187.40 (-5.88%)</td><td>168.44 (+3.53%)</td><td>169.80 (+7.20%)</td><td>148.30 (+14.52%)</td><td>14.25 <b>(-47.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>162.70 (n/a)</td><td>158.40 (n/a)</td><td>129.50 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-4.37%)</td><td>0.03 (-11.32%)</td><td>0.03 (-13.34%)</td><td>0.03 (-8.09%)</td><td>0.00 (+19.23%)</td><td>201.40 (+8.81%)</td><td>175.02 (+13.61%)</td><td>173.00 (+15.41%)</td><td>137.20 (+4.57%)</td><td>26.40 <b>(+35.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>154.06 (n/a)</td><td>149.90 (n/a)</td><td>131.20 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+10.61%)</td><td>0.03 (+1.29%)</td><td>0.03 (+3.25%)</td><td>0.02 (+6.66%)</td><td>0.01 (+7.44%)</td><td>217.70 (-6.24%)</td><td>176.24 (-1.41%)</td><td>173.10 (-3.13%)</td><td>127.00 (-9.61%)</td><td>33.04 (-10.23%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>178.76 (n/a)</td><td>178.70 (n/a)</td><td>140.50 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+8.24%)</td><td>0.03 (-2.55%)</td><td>0.03 (-12.12%)</td><td>0.03 (-8.67%)</td><td>0.01 <b>(+77.22%)</b></td><td>206.80 (+9.48%)</td><td>170.06 (+4.31%)</td><td>180.50 (+13.81%)</td><td>135.30 (-7.65%)</td><td>29.26 <b>(+75.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.90 (n/a)</td><td>163.04 (n/a)</td><td>158.60 (n/a)</td><td>146.50 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-4.05%)</td><td>0.03 (-4.88%)</td><td>0.03 (-16.71%)</td><td>0.03 <b>(+38.46%)</b></td><td>0.00 <b>(-39.04%)</b></td><td>205.00 <b>(-27.79%)</b></td><td>187.58 (+0.61%)</td><td>202.50 <b>(+20.04%)</b></td><td>145.50 (+4.23%)</td><td>25.42 <b>(-55.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>283.90 (n/a)</td><td>186.44 (n/a)</td><td>168.70 (n/a)</td><td>139.60 (n/a)</td><td>57.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 <b>(+26.69%)</b></td><td>0.03 (-2.48%)</td><td>0.02 (-12.58%)</td><td>0.02 (-3.20%)</td><td>0.01 <b>(+116.30%)</b></td><td>237.90 (+3.30%)</td><td>201.04 (+5.41%)</td><td>212.90 (+14.34%)</td><td>136.20 <b>(-21.09%)</b></td><td>39.31 <b>(+68.44%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.30 (n/a)</td><td>190.72 (n/a)</td><td>186.20 (n/a)</td><td>172.60 (n/a)</td><td>23.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 <b>(+22.44%)</b></td><td>0.07 (+2.54%)</td><td>0.06 (-7.65%)</td><td>0.04 <b>(-24.12%)</b></td><td>0.02 <b>(+155.08%)</b></td><td>266.60 <b>(+31.78%)</b></td><td>171.98 (+4.43%)</td><td>166.80 (+8.24%)</td><td>121.50 (-18.35%)</td><td>58.81 <b>(+165.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>164.68 (n/a)</td><td>154.10 (n/a)</td><td>148.80 (n/a)</td><td>22.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (-5.62%)</td><td>0.06 (-10.82%)</td><td>0.06 (-3.82%)</td><td>0.04 <b>(-24.64%)</b></td><td>0.01 <b>(+45.96%)</b></td><td>236.20 <b>(+32.70%)</b></td><td>189.20 (+15.28%)</td><td>175.50 (+3.97%)</td><td>137.90 (+5.91%)</td><td>42.39 <b>(+116.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>164.12 (n/a)</td><td>168.80 (n/a)</td><td>130.20 (n/a)</td><td>19.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-13.17%)</td><td>0.06 (-3.38%)</td><td>0.07 (+0.90%)</td><td>0.05 (+10.76%)</td><td>0.01 <b>(-33.19%)</b></td><td>210.20 (-9.75%)</td><td>167.52 (+0.49%)</td><td>150.70 (-0.86%)</td><td>141.40 (+15.15%)</td><td>31.36 <b>(-31.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>166.70 (n/a)</td><td>152.00 (n/a)</td><td>122.80 (n/a)</td><td>45.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (+15.38%)</td><td>0.06 (-0.97%)</td><td>0.06 (-12.61%)</td><td>0.05 (-1.34%)</td><td>0.01 <b>(+46.44%)</b></td><td>231.10 (+1.36%)</td><td>180.76 (+2.76%)</td><td>190.60 (+14.47%)</td><td>126.30 (-13.37%)</td><td>38.89 <b>(+22.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>175.90 (n/a)</td><td>166.50 (n/a)</td><td>145.80 (n/a)</td><td>31.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (-9.03%)</td><td>0.07 (-0.89%)</td><td>0.06 (+0.45%)</td><td>0.06 <b>(+31.65%)</b></td><td>0.01 <b>(-48.82%)</b></td><td>178.40 <b>(-24.02%)</b></td><td>163.12 (-3.52%)</td><td>172.60 (-0.40%)</td><td>130.00 (+9.89%)</td><td>19.60 <b>(-57.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>234.80 (n/a)</td><td>169.08 (n/a)</td><td>173.30 (n/a)</td><td>118.30 (n/a)</td><td>45.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-5.31%)</td><td>0.06 (-0.42%)</td><td>0.06 (-12.54%)</td><td>0.05 <b>(+20.95%)</b></td><td>0.01 <b>(-36.82%)</b></td><td>194.90 (-17.31%)</td><td>172.66 (-1.85%)</td><td>183.10 (+14.29%)</td><td>146.80 (+5.61%)</td><td>20.87 <b>(-45.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>175.92 (n/a)</td><td>160.20 (n/a)</td><td>139.00 (n/a)</td><td>38.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (-5.36%)</td><td>0.06 (-14.88%)</td><td>0.06 (-15.99%)</td><td>0.04 <b>(-29.81%)</b></td><td>0.02 <b>(+29.56%)</b></td><td>261.10 <b>(+42.44%)</b></td><td>178.22 <b>(+21.78%)</b></td><td>168.80 (+19.04%)</td><td>122.90 (+5.67%)</td><td>51.49 <b>(+98.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>146.34 (n/a)</td><td>141.80 (n/a)</td><td>116.30 (n/a)</td><td>25.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-17.08%)</td><td>0.04 (-8.65%)</td><td>0.04 (-7.96%)</td><td>0.04 (+10.13%)</td><td>0.01 <b>(-45.72%)</b></td><td>277.30 (-9.20%)</td><td>241.54 (+6.82%)</td><td>238.50 (+8.66%)</td><td>204.90 <b>(+20.60%)</b></td><td>29.32 <b>(-41.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>305.40 (n/a)</td><td>226.12 (n/a)</td><td>219.50 (n/a)</td><td>169.90 (n/a)</td><td>50.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (-10.19%)</td><td>0.11 <b>(-21.98%)</b></td><td>0.11 <b>(-26.10%)</b></td><td>0.09 <b>(-28.13%)</b></td><td>0.02 <b>(+42.53%)</b></td><td>232.60 <b>(+39.20%)</b></td><td>191.68 <b>(+30.68%)</b></td><td>196.50 <b>(+35.33%)</b></td><td>139.20 (+11.36%)</td><td>34.15 <b>(+114.25%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>167.10 (n/a)</td><td>146.68 (n/a)</td><td>145.20 (n/a)</td><td>125.00 (n/a)</td><td>15.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (+7.15%)</td><td>0.12 (-12.69%)</td><td>0.13 (-9.21%)</td><td>0.06 <b>(-46.39%)</b></td><td>0.04 <b>(+118.14%)</b></td><td>327.80 <b>(+86.57%)</b></td><td>191.50 <b>(+26.59%)</b></td><td>157.50 (+10.14%)</td><td>123.70 (-6.64%)</td><td>81.48 <b>(+293.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>175.70 (n/a)</td><td>151.28 (n/a)</td><td>143.00 (n/a)</td><td>132.50 (n/a)</td><td>20.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 <b>(-25.13%)</b></td><td>0.11 <b>(-23.16%)</b></td><td>0.12 <b>(-24.58%)</b></td><td>0.08 <b>(-29.24%)</b></td><td>0.02 (-11.33%)</td><td>267.50 <b>(+41.38%)</b></td><td>194.68 <b>(+31.42%)</b></td><td>182.10 <b>(+32.53%)</b></td><td>166.50 <b>(+33.52%)</b></td><td>42.00 <b>(+66.54%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>148.14 (n/a)</td><td>137.40 (n/a)</td><td>124.70 (n/a)</td><td>25.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-4.84%)</td><td>0.12 (+0.92%)</td><td>0.12 (+3.52%)</td><td>0.10 (-8.10%)</td><td>0.02 (-3.16%)</td><td>214.70 (+8.82%)</td><td>171.70 (-0.79%)</td><td>168.00 (-3.45%)</td><td>147.90 (+5.04%)</td><td>25.79 (+12.60%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>197.30 (n/a)</td><td>173.06 (n/a)</td><td>174.00 (n/a)</td><td>140.80 (n/a)</td><td>22.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-4.01%)</td><td>0.11 (-6.82%)</td><td>0.11 (-10.43%)</td><td>0.08 <b>(-20.16%)</b></td><td>0.02 <b>(+37.82%)</b></td><td>253.30 <b>(+25.27%)</b></td><td>190.66 (+9.44%)</td><td>191.50 (+11.66%)</td><td>148.60 (+4.21%)</td><td>39.91 <b>(+83.72%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>174.22 (n/a)</td><td>171.50 (n/a)</td><td>142.60 (n/a)</td><td>21.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (-1.40%)</td><td>0.11 (-5.72%)</td><td>0.10 (-14.31%)</td><td>0.09 (+3.43%)</td><td>0.02 (+8.53%)</td><td>228.20 (-3.31%)</td><td>192.16 (+6.57%)</td><td>208.80 (+16.71%)</td><td>144.30 (+1.41%)</td><td>37.86 (+5.83%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>180.32 (n/a)</td><td>178.90 (n/a)</td><td>142.30 (n/a)</td><td>35.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (+14.60%)</td><td>0.12 (+9.85%)</td><td>0.13 <b>(+21.31%)</b></td><td>0.08 (-16.52%)</td><td>0.03 <b>(+45.81%)</b></td><td>258.90 (+19.81%)</td><td>176.16 (-6.51%)</td><td>163.80 (-17.56%)</td><td>136.00 (-12.76%)</td><td>47.72 <b>(+63.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>216.10 (n/a)</td><td>188.42 (n/a)</td><td>198.70 (n/a)</td><td>155.90 (n/a)</td><td>29.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-5.30%)</td><td>0.10 (-10.12%)</td><td>0.09 (-14.01%)</td><td>0.08 (-11.49%)</td><td>0.02 (+11.16%)</td><td>259.20 (+12.94%)</td><td>225.36 (+12.01%)</td><td>233.80 (+16.32%)</td><td>171.70 (+5.60%)</td><td>34.66 <b>(+31.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>201.20 (n/a)</td><td>201.00 (n/a)</td><td>162.60 (n/a)</td><td>26.42 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>145.30 (n/a)</td><td>144.50 (n/a)</td><td>118.00 (n/a)</td><td>26.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>169.02 (n/a)</td><td>165.40 (n/a)</td><td>130.30 (n/a)</td><td>34.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>178.30 (n/a)</td><td>165.60 (n/a)</td><td>147.70 (n/a)</td><td>35.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>303.60 (n/a)</td><td>198.78 (n/a)</td><td>166.80 (n/a)</td><td>132.50 (n/a)</td><td>68.15 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>159.90 (n/a)</td><td>162.60 (n/a)</td><td>122.10 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>165.04 (n/a)</td><td>130.60 (n/a)</td><td>117.60 (n/a)</td><td>56.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>169.62 (n/a)</td><td>159.80 (n/a)</td><td>117.90 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>300.00 (n/a)</td><td>207.80 (n/a)</td><td>159.50 (n/a)</td><td>148.20 (n/a)</td><td>72.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.10 (n/a)</td><td>162.60 (n/a)</td><td>152.60 (n/a)</td><td>125.90 (n/a)</td><td>40.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>229.70 (n/a)</td><td>173.74 (n/a)</td><td>175.90 (n/a)</td><td>125.80 (n/a)</td><td>44.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>193.10 (n/a)</td><td>157.56 (n/a)</td><td>154.70 (n/a)</td><td>123.30 (n/a)</td><td>26.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>166.36 (n/a)</td><td>160.90 (n/a)</td><td>139.40 (n/a)</td><td>22.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.38 (+14.78%)</td><td>0.31 (+13.10%)</td><td>0.30 (+9.29%)</td><td>0.28 <b>(+23.54%)</b></td><td>0.04 (+2.44%)</td><td>178.10 (-19.05%)</td><td>161.56 (-11.99%)</td><td>165.30 (-8.52%)</td><td>130.20 (-12.91%)</td><td>18.35 <b>(-29.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>220.00 (n/a)</td><td>183.56 (n/a)</td><td>180.70 (n/a)</td><td>149.50 (n/a)</td><td>26.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>178.30 (n/a)</td><td>161.32 (n/a)</td><td>162.60 (n/a)</td><td>136.30 (n/a)</td><td>17.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>218.30 (n/a)</td><td>150.46 (n/a)</td><td>131.50 (n/a)</td><td>127.40 (n/a)</td><td>38.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>282.00 (n/a)</td><td>191.48 (n/a)</td><td>158.40 (n/a)</td><td>128.80 (n/a)</td><td>67.58 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>157.64 (n/a)</td><td>151.20 (n/a)</td><td>117.30 (n/a)</td><td>42.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>152.38 (n/a)</td><td>143.30 (n/a)</td><td>101.50 (n/a)</td><td>43.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>170.50 (n/a)</td><td>177.70 (n/a)</td><td>105.80 (n/a)</td><td>42.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>199.70 (n/a)</td><td>193.90 (n/a)</td><td>170.60 (n/a)</td><td>26.04 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>176.66 (n/a)</td><td>173.70 (n/a)</td><td>169.00 (n/a)</td><td>8.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.10 (n/a)</td><td>198.00 (n/a)</td><td>182.40 (n/a)</td><td>147.90 (n/a)</td><td>56.21 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>197.40 (n/a)</td><td>161.42 (n/a)</td><td>167.10 (n/a)</td><td>111.70 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>159.58 (n/a)</td><td>151.70 (n/a)</td><td>147.20 (n/a)</td><td>14.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>166.10 (n/a)</td><td>143.14 (n/a)</td><td>146.00 (n/a)</td><td>118.50 (n/a)</td><td>19.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>186.80 (n/a)</td><td>156.92 (n/a)</td><td>148.80 (n/a)</td><td>130.50 (n/a)</td><td>25.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.20 (n/a)</td><td>140.32 (n/a)</td><td>132.80 (n/a)</td><td>112.40 (n/a)</td><td>26.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.20 (n/a)</td><td>159.06 (n/a)</td><td>159.60 (n/a)</td><td>124.50 (n/a)</td><td>24.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>178.80 (n/a)</td><td>148.00 (n/a)</td><td>155.20 (n/a)</td><td>104.30 (n/a)</td><td>29.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>276.50 (n/a)</td><td>209.74 (n/a)</td><td>216.60 (n/a)</td><td>154.70 (n/a)</td><td>52.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>224.20 (n/a)</td><td>159.84 (n/a)</td><td>149.40 (n/a)</td><td>125.30 (n/a)</td><td>37.54 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>161.00 (n/a)</td><td>150.40 (n/a)</td><td>117.90 (n/a)</td><td>36.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>157.34 (n/a)</td><td>161.40 (n/a)</td><td>126.60 (n/a)</td><td>30.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.50 (n/a)</td><td>148.84 (n/a)</td><td>144.20 (n/a)</td><td>128.60 (n/a)</td><td>23.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.50 (n/a)</td><td>155.82 (n/a)</td><td>156.50 (n/a)</td><td>141.00 (n/a)</td><td>8.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.10 (n/a)</td><td>174.76 (n/a)</td><td>167.40 (n/a)</td><td>151.80 (n/a)</td><td>25.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>281.40 (n/a)</td><td>199.40 (n/a)</td><td>197.50 (n/a)</td><td>144.50 (n/a)</td><td>51.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.70 (n/a)</td><td>176.36 (n/a)</td><td>168.70 (n/a)</td><td>149.50 (n/a)</td><td>27.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.40 (n/a)</td><td>217.60 (n/a)</td><td>220.70 (n/a)</td><td>177.60 (n/a)</td><td>33.56 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.80 (n/a)</td><td>189.40 (n/a)</td><td>174.80 (n/a)</td><td>137.00 (n/a)</td><td>47.50 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>340.10 (n/a)</td><td>185.54 (n/a)</td><td>156.40 (n/a)</td><td>131.90 (n/a)</td><td>87.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.80 (n/a)</td><td>178.54 (n/a)</td><td>154.80 (n/a)</td><td>131.60 (n/a)</td><td>59.91 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>192.58 (n/a)</td><td>171.60 (n/a)</td><td>163.30 (n/a)</td><td>35.45 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>180.24 (n/a)</td><td>161.30 (n/a)</td><td>144.00 (n/a)</td><td>36.24 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>196.34 (n/a)</td><td>223.50 (n/a)</td><td>122.60 (n/a)</td><td>50.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>196.04 (n/a)</td><td>191.00 (n/a)</td><td>160.40 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>356.20 (n/a)</td><td>213.86 (n/a)</td><td>182.70 (n/a)</td><td>169.90 (n/a)</td><td>79.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>156.02 (n/a)</td><td>162.00 (n/a)</td><td>135.90 (n/a)</td><td>18.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>347.80 (n/a)</td><td>204.04 (n/a)</td><td>185.10 (n/a)</td><td>136.40 (n/a)</td><td>83.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>257.00 (n/a)</td><td>185.06 (n/a)</td><td>171.90 (n/a)</td><td>158.60 (n/a)</td><td>40.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.10 (n/a)</td><td>173.66 (n/a)</td><td>143.80 (n/a)</td><td>135.50 (n/a)</td><td>45.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>270.70 (n/a)</td><td>195.12 (n/a)</td><td>177.80 (n/a)</td><td>141.60 (n/a)</td><td>52.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>171.18 (n/a)</td><td>165.20 (n/a)</td><td>142.90 (n/a)</td><td>25.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>178.54 (n/a)</td><td>171.70 (n/a)</td><td>149.60 (n/a)</td><td>27.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>213.24 (n/a)</td><td>220.10 (n/a)</td><td>180.00 (n/a)</td><td>31.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.30 (n/a)</td><td>157.78 (n/a)</td><td>159.70 (n/a)</td><td>128.10 (n/a)</td><td>28.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>369.20 (n/a)</td><td>204.64 (n/a)</td><td>172.30 (n/a)</td><td>132.20 (n/a)</td><td>93.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>313.40 (n/a)</td><td>200.18 (n/a)</td><td>164.00 (n/a)</td><td>138.80 (n/a)</td><td>75.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.20 (n/a)</td><td>188.12 (n/a)</td><td>192.30 (n/a)</td><td>161.80 (n/a)</td><td>23.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.00 (n/a)</td><td>164.16 (n/a)</td><td>146.60 (n/a)</td><td>140.60 (n/a)</td><td>38.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>184.28 (n/a)</td><td>186.70 (n/a)</td><td>168.00 (n/a)</td><td>14.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>186.00 (n/a)</td><td>189.00 (n/a)</td><td>149.40 (n/a)</td><td>23.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>287.10 (n/a)</td><td>214.26 (n/a)</td><td>208.00 (n/a)</td><td>135.40 (n/a)</td><td>60.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>4.40 (-9.63%)</td><td>4.19 (-4.53%)</td><td>4.18 (-5.46%)</td><td>3.91 (+9.23%)</td><td>0.20 <b>(-60.93%)</b></td><td>2405.10 (-8.45%)</td><td>2246.40 (+3.69%)</td><td>2249.20 (+5.78%)</td><td>2138.20 (+10.66%)</td><td>108.85 <b>(-60.86%)</b></td><td>1730.16 (-9.63%)</td><td>1649.85 (-4.53%)</td><td>1644.75 (-5.46%)</td><td>1538.12 (+9.23%)</td><td>78.67 <b>(-60.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.87 (n/a)</td><td>4.39 (n/a)</td><td>4.42 (n/a)</td><td>3.58 (n/a)</td><td>0.51 (n/a)</td><td>2627.10 (n/a)</td><td>2166.46 (n/a)</td><td>2126.30 (n/a)</td><td>1932.20 (n/a)</td><td>278.12 (n/a)</td><td>1914.63 (n/a)</td><td>1728.17 (n/a)</td><td>1739.79 (n/a)</td><td>1408.15 (n/a)</td><td>201.35 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.08 <b>(-28.89%)</b></td><td>0.86 (-10.56%)</td><td>0.88 (-4.52%)</td><td>0.65 (-6.02%)</td><td>0.21 <b>(-37.93%)</b></td><td>342.60 (+6.43%)</td><td>270.12 (+8.42%)</td><td>250.30 (+4.73%)</td><td>205.00 <b>(+40.70%)</b></td><td>67.49 (-4.99%)</td><td>46.04 <b>(-28.89%)</b></td><td>36.70 (-10.56%)</td><td>37.70 (-4.52%)</td><td>27.55 (-6.02%)</td><td>8.86 <b>(-37.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.52 (n/a)</td><td>0.96 (n/a)</td><td>0.93 (n/a)</td><td>0.69 (n/a)</td><td>0.33 (n/a)</td><td>321.90 (n/a)</td><td>249.14 (n/a)</td><td>239.00 (n/a)</td><td>145.70 (n/a)</td><td>71.04 (n/a)</td><td>64.75 (n/a)</td><td>41.03 (n/a)</td><td>39.48 (n/a)</td><td>29.31 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.20 (+4.30%)</td><td>1.04 (+2.76%)</td><td>1.18 <b>(+21.25%)</b></td><td>0.64 <b>(-27.30%)</b></td><td>0.24 <b>(+99.16%)</b></td><td>346.40 <b>(+37.57%)</b></td><td>226.32 (+2.05%)</td><td>186.80 (-17.49%)</td><td>184.30 (-4.11%)</td><td>69.72 <b>(+163.92%)</b></td><td>51.22 (+4.30%)</td><td>44.24 (+2.76%)</td><td>50.53 <b>(+21.25%)</b></td><td>27.25 <b>(-27.30%)</b></td><td>10.38 <b>(+99.16%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.15 (n/a)</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.88 (n/a)</td><td>0.12 (n/a)</td><td>251.80 (n/a)</td><td>221.78 (n/a)</td><td>226.40 (n/a)</td><td>192.20 (n/a)</td><td>26.42 (n/a)</td><td>49.10 (n/a)</td><td>43.05 (n/a)</td><td>41.68 (n/a)</td><td>37.48 (n/a)</td><td>5.21 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.52 (-0.80%)</td><td>0.52 (-0.30%)</td><td>0.52 (-0.11%)</td><td>0.52 (-0.31%)</td><td>0.00 <b>(-59.07%)</b></td><td>48777.20 (+0.31%)</td><td>48679.30 (+0.30%)</td><td>48673.80 (+0.11%)</td><td>48590.90 (+0.81%)</td><td>76.99 <b>(-58.61%)</b></td><td>353.56 (-0.80%)</td><td>352.92 (-0.30%)</td><td>352.96 (-0.11%)</td><td>352.21 (-0.31%)</td><td>0.56 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48627.70 (n/a)</td><td>48532.84 (n/a)</td><td>48622.10 (n/a)</td><td>48201.40 (n/a)</td><td>186.00 (n/a)</td><td>356.42 (n/a)</td><td>353.99 (n/a)</td><td>353.33 (n/a)</td><td>353.29 (n/a)</td><td>1.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (-1.09%)</td><td>0.21 (-1.44%)</td><td>0.21 (-2.01%)</td><td>0.21 (-0.77%)</td><td>0.00 (-5.07%)</td><td>119817.20 (+0.77%)</td><td>118806.74 (+1.46%)</td><td>119218.40 (+2.05%)</td><td>117305.40 (+1.10%)</td><td>1103.65 (-3.29%)</td><td>146.45 (-1.09%)</td><td>144.61 (-1.44%)</td><td>144.10 (-2.01%)</td><td>143.38 (-0.77%)</td><td>1.35 (-5.07%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118897.80 (n/a)</td><td>117093.26 (n/a)</td><td>116821.20 (n/a)</td><td>116025.00 (n/a)</td><td>1141.20 (n/a)</td><td>148.07 (n/a)</td><td>146.73 (n/a)</td><td>147.06 (n/a)</td><td>144.49 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.92 (+3.36%)</td><td>0.89 (+1.43%)</td><td>0.89 (+0.70%)</td><td>0.88 (+1.30%)</td><td>0.01 <b>(+163.40%)</b></td><td>28437.00 (-1.28%)</td><td>28160.18 (-1.40%)</td><td>28369.60 (-0.70%)</td><td>27438.60 (-3.25%)</td><td>419.95 <b>(+151.32%)</b></td><td>626.12 (+3.36%)</td><td>610.19 (+1.43%)</td><td>605.57 (+0.70%)</td><td>604.14 (+1.30%)</td><td>9.25 <b>(+163.40%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28805.30 (n/a)</td><td>28559.28 (n/a)</td><td>28568.30 (n/a)</td><td>28359.40 (n/a)</td><td>167.10 (n/a)</td><td>605.79 (n/a)</td><td>601.57 (n/a)</td><td>601.36 (n/a)</td><td>596.41 (n/a)</td><td>3.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.52 (-0.09%)</td><td>3.45 (+1.30%)</td><td>3.52 (+2.98%)</td><td>3.34 (+3.13%)</td><td>0.09 (-13.64%)</td><td>7542.70 (-3.03%)</td><td>7303.44 (-1.30%)</td><td>7157.50 (-2.90%)</td><td>7152.70 (+0.09%)</td><td>203.26 (-16.53%)</td><td>2401.89 (-0.09%)</td><td>2353.75 (+1.30%)</td><td>2400.26 (+2.98%)</td><td>2277.69 (+3.13%)</td><td>64.83 (-13.64%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.52 (n/a)</td><td>3.40 (n/a)</td><td>3.41 (n/a)</td><td>3.24 (n/a)</td><td>0.11 (n/a)</td><td>7778.40 (n/a)</td><td>7399.88 (n/a)</td><td>7370.90 (n/a)</td><td>7146.40 (n/a)</td><td>243.50 (n/a)</td><td>2403.98 (n/a)</td><td>2323.61 (n/a)</td><td>2330.77 (n/a)</td><td>2208.66 (n/a)</td><td>75.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>2.88 (-8.66%)</td><td>2.79 (-6.27%)</td><td>2.81 (-2.86%)</td><td>2.68 (-5.73%)</td><td>0.08 <b>(-49.90%)</b></td><td>9397.60 (+6.08%)</td><td>9037.78 (+6.53%)</td><td>8957.60 (+2.95%)</td><td>8744.50 (+9.48%)</td><td>253.88 <b>(-41.60%)</b></td><td>1964.65 (-8.66%)</td><td>1902.09 (-6.27%)</td><td>1917.91 (-2.86%)</td><td>1828.11 (-5.73%)</td><td>52.98 <b>(-49.90%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.15 (n/a)</td><td>2.97 (n/a)</td><td>2.89 (n/a)</td><td>2.84 (n/a)</td><td>0.15 (n/a)</td><td>8858.90 (n/a)</td><td>8483.78 (n/a)</td><td>8701.30 (n/a)</td><td>7987.30 (n/a)</td><td>434.73 (n/a)</td><td>2150.90 (n/a)</td><td>2029.36 (n/a)</td><td>1974.40 (n/a)</td><td>1939.27 (n/a)</td><td>105.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.32 (-0.35%)</td><td>3.19 (-0.28%)</td><td>3.18 (-0.44%)</td><td>3.01 (-2.38%)</td><td>0.13 <b>(+40.67%)</b></td><td>8357.20 (+2.44%)</td><td>7894.52 (+0.35%)</td><td>7917.70 (+0.44%)</td><td>7571.40 (+0.35%)</td><td>321.84 <b>(+44.20%)</b></td><td>2269.06 (-0.35%)</td><td>2179.04 (-0.28%)</td><td>2169.81 (-0.44%)</td><td>2055.69 (-2.38%)</td><td>87.77 <b>(+40.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.34 (n/a)</td><td>3.20 (n/a)</td><td>3.19 (n/a)</td><td>3.08 (n/a)</td><td>0.09 (n/a)</td><td>8158.40 (n/a)</td><td>7866.92 (n/a)</td><td>7883.00 (n/a)</td><td>7544.80 (n/a)</td><td>223.19 (n/a)</td><td>2277.04 (n/a)</td><td>2185.23 (n/a)</td><td>2179.36 (n/a)</td><td>2105.80 (n/a)</td><td>62.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.78 (+0.02%)</td><td>0.78 (+0.01%)</td><td>0.78 (-0.01%)</td><td>0.78 (+0.05%)</td><td>0.00 (-19.46%)</td><td>96514.30 (-0.05%)</td><td>96472.96 (-0.01%)</td><td>96473.80 (+0.01%)</td><td>96417.10 (-0.02%)</td><td>41.22 (-19.52%)</td><td>712.73 (+0.02%)</td><td>712.32 (+0.01%)</td><td>712.31 (-0.01%)</td><td>712.01 (+0.05%)</td><td>0.30 (-19.46%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96566.20 (n/a)</td><td>96478.00 (n/a)</td><td>96465.70 (n/a)</td><td>96433.50 (n/a)</td><td>51.22 (n/a)</td><td>712.61 (n/a)</td><td>712.28 (n/a)</td><td>712.37 (n/a)</td><td>711.63 (n/a)</td><td>0.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (+0.03%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.05%)</td><td>0.00 <b>(+37.70%)</b></td><td>103859.20 (+0.05%)</td><td>103694.06 (+0.01%)</td><td>103651.30 (-0.01%)</td><td>103598.40 (-0.03%)</td><td>104.06 <b>(+37.79%)</b></td><td>663.33 (+0.03%)</td><td>662.71 (-0.01%)</td><td>662.99 (+0.01%)</td><td>661.66 (-0.05%)</td><td>0.66 <b>(+37.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103812.10 (n/a)</td><td>103685.86 (n/a)</td><td>103665.50 (n/a)</td><td>103625.90 (n/a)</td><td>75.52 (n/a)</td><td>663.15 (n/a)</td><td>662.77 (n/a)</td><td>662.90 (n/a)</td><td>661.96 (n/a)</td><td>0.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.70 (+0.06%)</td><td>0.69 (-0.02%)</td><td>0.69 (-0.11%)</td><td>0.69 (-0.09%)</td><td>0.00 (+12.26%)</td><td>109231.30 (+0.09%)</td><td>108740.02 (+0.02%)</td><td>108644.80 (+0.11%)</td><td>108420.10 (-0.06%)</td><td>343.26 (+12.31%)</td><td>633.83 (+0.06%)</td><td>631.97 (-0.02%)</td><td>632.52 (-0.11%)</td><td>629.12 (-0.09%)</td><td>1.99 (+12.26%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109134.30 (n/a)</td><td>108719.56 (n/a)</td><td>108526.00 (n/a)</td><td>108480.90 (n/a)</td><td>305.65 (n/a)</td><td>633.47 (n/a)</td><td>632.08 (n/a)</td><td>633.21 (n/a)</td><td>629.68 (n/a)</td><td>1.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.45 (+5.91%)</td><td>6.51 (-3.81%)</td><td>7.11 (+1.78%)</td><td>5.07 <b>(-20.07%)</b></td><td>1.11 <b>(+220.26%)</b></td><td>1758.30 <b>(+25.11%)</b></td><td>1404.62 (+6.40%)</td><td>1253.40 (-1.76%)</td><td>1196.10 (-5.58%)</td><td>258.51 <b>(+274.85%)</b></td><td>448.87 (+5.91%)</td><td>392.04 (-3.81%)</td><td>428.32 (+1.78%)</td><td>305.34 <b>(-20.07%)</b></td><td>66.84 <b>(+220.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.04 (n/a)</td><td>6.77 (n/a)</td><td>6.99 (n/a)</td><td>6.34 (n/a)</td><td>0.35 (n/a)</td><td>1405.40 (n/a)</td><td>1320.12 (n/a)</td><td>1275.80 (n/a)</td><td>1266.80 (n/a)</td><td>68.96 (n/a)</td><td>423.80 (n/a)</td><td>407.55 (n/a)</td><td>420.81 (n/a)</td><td>381.99 (n/a)</td><td>20.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>6.97 (+0.16%)</td><td>6.72 (+0.41%)</td><td>6.69 (-1.17%)</td><td>6.39 (+3.40%)</td><td>0.22 <b>(-26.50%)</b></td><td>1395.30 (-3.29%)</td><td>1328.12 (-0.49%)</td><td>1331.70 (+1.19%)</td><td>1278.40 (-0.16%)</td><td>43.95 <b>(-29.72%)</b></td><td>419.97 (+0.16%)</td><td>404.59 (+0.41%)</td><td>403.16 (-1.17%)</td><td>384.76 (+3.40%)</td><td>13.20 <b>(-26.50%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.96 (n/a)</td><td>6.69 (n/a)</td><td>6.77 (n/a)</td><td>6.18 (n/a)</td><td>0.30 (n/a)</td><td>1442.80 (n/a)</td><td>1334.68 (n/a)</td><td>1316.10 (n/a)</td><td>1280.40 (n/a)</td><td>62.53 (n/a)</td><td>419.30 (n/a)</td><td>402.92 (n/a)</td><td>407.93 (n/a)</td><td>372.11 (n/a)</td><td>17.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.09 (+1.91%)</td><td>6.57 (+0.29%)</td><td>6.60 (+2.09%)</td><td>6.11 (-3.37%)</td><td>0.44 <b>(+71.38%)</b></td><td>1459.70 (+3.49%)</td><td>1362.48 (-0.05%)</td><td>1351.00 (-2.05%)</td><td>1257.10 (-1.87%)</td><td>92.46 <b>(+75.83%)</b></td><td>427.08 (+1.91%)</td><td>395.50 (+0.29%)</td><td>397.37 (+2.09%)</td><td>367.80 (-3.37%)</td><td>26.80 <b>(+71.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.96 (n/a)</td><td>6.55 (n/a)</td><td>6.46 (n/a)</td><td>6.32 (n/a)</td><td>0.26 (n/a)</td><td>1410.50 (n/a)</td><td>1363.16 (n/a)</td><td>1379.30 (n/a)</td><td>1281.10 (n/a)</td><td>52.59 (n/a)</td><td>419.08 (n/a)</td><td>394.33 (n/a)</td><td>389.25 (n/a)</td><td>380.62 (n/a)</td><td>15.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.01 (-3.77%)</td><td>7.55 (-4.95%)</td><td>7.43 (-6.27%)</td><td>7.16 (-5.41%)</td><td>0.39 <b>(+45.55%)</b></td><td>4867.30 (+5.72%)</td><td>4626.64 (+5.33%)</td><td>4692.90 (+6.69%)</td><td>4352.70 (+3.92%)</td><td>235.01 <b>(+59.39%)</b></td><td>493.37 (-3.77%)</td><td>465.13 (-4.95%)</td><td>457.60 (-6.27%)</td><td>441.21 (-5.41%)</td><td>23.89 <b>(+45.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.32 (n/a)</td><td>7.94 (n/a)</td><td>7.93 (n/a)</td><td>7.57 (n/a)</td><td>0.27 (n/a)</td><td>4604.10 (n/a)</td><td>4392.42 (n/a)</td><td>4398.80 (n/a)</td><td>4188.70 (n/a)</td><td>147.44 (n/a)</td><td>512.68 (n/a)</td><td>489.35 (n/a)</td><td>488.20 (n/a)</td><td>466.43 (n/a)</td><td>16.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.59 (-3.25%)</td><td>7.28 (-3.10%)</td><td>7.43 (-1.68%)</td><td>6.76 (-3.89%)</td><td>0.37 <b>(+25.43%)</b></td><td>5154.60 (+4.05%)</td><td>4802.32 (+3.28%)</td><td>4693.50 (+1.71%)</td><td>4595.40 (+3.36%)</td><td>247.63 <b>(+33.16%)</b></td><td>467.31 (-3.25%)</td><td>448.11 (-3.10%)</td><td>457.55 (-1.68%)</td><td>416.62 (-3.89%)</td><td>22.56 <b>(+25.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.84 (n/a)</td><td>7.51 (n/a)</td><td>7.56 (n/a)</td><td>7.04 (n/a)</td><td>0.29 (n/a)</td><td>4954.00 (n/a)</td><td>4649.70 (n/a)</td><td>4614.70 (n/a)</td><td>4446.20 (n/a)</td><td>185.96 (n/a)</td><td>482.99 (n/a)</td><td>462.43 (n/a)</td><td>465.36 (n/a)</td><td>433.48 (n/a)</td><td>17.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.59 (+1.33%)</td><td>7.08 (-1.82%)</td><td>7.13 (-2.59%)</td><td>6.73 (+1.57%)</td><td>0.36 (+7.05%)</td><td>5176.80 (-1.54%)</td><td>4937.62 (+1.87%)</td><td>4893.30 (+2.66%)</td><td>4591.20 (-1.31%)</td><td>245.19 (+3.68%)</td><td>467.73 (+1.33%)</td><td>435.80 (-1.82%)</td><td>438.87 (-2.59%)</td><td>414.83 (+1.57%)</td><td>21.98 (+7.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.49 (n/a)</td><td>7.21 (n/a)</td><td>7.31 (n/a)</td><td>6.63 (n/a)</td><td>0.33 (n/a)</td><td>5257.90 (n/a)</td><td>4846.84 (n/a)</td><td>4766.70 (n/a)</td><td>4652.30 (n/a)</td><td>236.49 (n/a)</td><td>461.60 (n/a)</td><td>443.87 (n/a)</td><td>450.52 (n/a)</td><td>408.43 (n/a)</td><td>20.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.79 (-0.25%)</td><td>0.79 (-0.02%)</td><td>0.79 (+0.09%)</td><td>0.79 (+0.05%)</td><td>0.00 <b>(-55.58%)</b></td><td>95878.20 (-0.05%)</td><td>95755.36 (+0.02%)</td><td>95769.20 (-0.09%)</td><td>95599.20 (+0.25%)</td><td>102.09 <b>(-55.48%)</b></td><td>718.83 (-0.25%)</td><td>717.66 (-0.02%)</td><td>717.55 (+0.09%)</td><td>716.74 (+0.05%)</td><td>0.77 <b>(-55.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95924.50 (n/a)</td><td>95739.62 (n/a)</td><td>95859.70 (n/a)</td><td>95360.30 (n/a)</td><td>229.32 (n/a)</td><td>720.63 (n/a)</td><td>717.78 (n/a)</td><td>716.88 (n/a)</td><td>716.39 (n/a)</td><td>1.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (-0.02%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.01%)</td><td>0.73 (+0.00%)</td><td>0.00 <b>(-35.28%)</b></td><td>102934.00 (-0.00%)</td><td>102919.40 (+0.01%)</td><td>102913.20 (+0.01%)</td><td>102908.30 (+0.02%)</td><td>12.57 <b>(-35.44%)</b></td><td>667.77 (-0.02%)</td><td>667.70 (-0.01%)</td><td>667.74 (-0.01%)</td><td>667.61 (+0.00%)</td><td>0.08 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102934.40 (n/a)</td><td>102911.24 (n/a)</td><td>102900.60 (n/a)</td><td>102892.10 (n/a)</td><td>19.46 (n/a)</td><td>667.88 (n/a)</td><td>667.75 (n/a)</td><td>667.82 (n/a)</td><td>667.60 (n/a)</td><td>0.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.70 (-0.25%)</td><td>0.70 (-0.20%)</td><td>0.70 (-0.25%)</td><td>0.70 (-0.20%)</td><td>0.00 (-5.78%)</td><td>108227.80 (+0.20%)</td><td>107871.82 (+0.20%)</td><td>107890.80 (+0.26%)</td><td>107630.80 (+0.25%)</td><td>230.13 (-5.36%)</td><td>638.47 (-0.25%)</td><td>637.05 (-0.20%)</td><td>636.94 (-0.25%)</td><td>634.95 (-0.20%)</td><td>1.36 (-5.79%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108009.10 (n/a)</td><td>107656.36 (n/a)</td><td>107615.70 (n/a)</td><td>107363.90 (n/a)</td><td>243.16 (n/a)</td><td>640.06 (n/a)</td><td>638.33 (n/a)</td><td>638.56 (n/a)</td><td>636.24 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.72 (-10.72%)</td><td>3.53 (-3.83%)</td><td>3.66 (+0.83%)</td><td>2.95 (-1.90%)</td><td>0.33 <b>(-24.10%)</b></td><td>2734.00 (+1.94%)</td><td>2302.98 (+3.56%)</td><td>2200.20 (-0.82%)</td><td>2166.10 (+12.01%)</td><td>242.93 (-14.01%)</td><td>975.92 (-10.72%)</td><td>925.17 (-3.83%)</td><td>960.78 (+0.83%)</td><td>773.20 (-1.90%)</td><td>86.01 <b>(-24.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.17 (n/a)</td><td>3.67 (n/a)</td><td>3.63 (n/a)</td><td>3.01 (n/a)</td><td>0.43 (n/a)</td><td>2682.10 (n/a)</td><td>2223.84 (n/a)</td><td>2218.40 (n/a)</td><td>1933.90 (n/a)</td><td>282.50 (n/a)</td><td>1093.10 (n/a)</td><td>962.03 (n/a)</td><td>952.91 (n/a)</td><td>788.15 (n/a)</td><td>113.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.51 <b>(+48.25%)</b></td><td>0.34 (+9.58%)</td><td>0.31 (+0.37%)</td><td>0.27 (-2.61%)</td><td>0.10 <b>(+263.68%)</b></td><td>4557.20 (+2.68%)</td><td>3832.96 (-4.75%)</td><td>3984.30 (-0.37%)</td><td>2453.80 <b>(-32.55%)</b></td><td>820.96 <b>(+141.83%)</b></td><td>27.35 <b>(+48.25%)</b></td><td>18.38 (+9.58%)</td><td>16.84 (+0.37%)</td><td>14.73 (-2.61%)</td><td>5.13 <b>(+263.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>4438.30 (n/a)</td><td>4023.94 (n/a)</td><td>3999.10 (n/a)</td><td>3637.70 (n/a)</td><td>339.48 (n/a)</td><td>18.45 (n/a)</td><td>16.77 (n/a)</td><td>16.78 (n/a)</td><td>15.12 (n/a)</td><td>1.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.05 <b>(-23.17%)</b></td><td>3.98 <b>(-20.67%)</b></td><td>3.94 (-18.27%)</td><td>3.30 (-17.00%)</td><td>0.67 <b>(-29.27%)</b></td><td>2016.90 <b>(+20.48%)</b></td><td>1706.06 <b>(+25.41%)</b></td><td>1688.80 <b>(+22.36%)</b></td><td>1318.40 <b>(+30.16%)</b></td><td>266.40 (+12.82%)</td><td>1558.89 <b>(-23.17%)</b></td><td>1230.39 <b>(-20.67%)</b></td><td>1216.99 (-18.27%)</td><td>1019.02 (-17.00%)</td><td>207.80 <b>(-29.27%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.57 (n/a)</td><td>5.02 (n/a)</td><td>4.82 (n/a)</td><td>3.97 (n/a)</td><td>0.95 (n/a)</td><td>1674.10 (n/a)</td><td>1360.36 (n/a)</td><td>1380.20 (n/a)</td><td>1012.90 (n/a)</td><td>236.12 (n/a)</td><td>2028.98 (n/a)</td><td>1550.94 (n/a)</td><td>1489.11 (n/a)</td><td>1227.67 (n/a)</td><td>293.78 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.31 (n/a)</td><td>12.89 (n/a)</td><td>13.16 (n/a)</td><td>12.07 (n/a)</td><td>0.52 (n/a)</td><td>13.31 (n/a)</td><td>12.88 (n/a)</td><td>13.15 (n/a)</td><td>12.06 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>24.80 (-0.30%)</td><td>24.13 (-0.50%)</td><td>24.18 (-1.73%)</td><td>23.44 (+0.69%)</td><td>0.50 <b>(-24.14%)</b></td><td>24.78 (-0.30%)</td><td>24.11 (-0.50%)</td><td>24.17 (-1.73%)</td><td>23.42 (+0.69%)</td><td>0.50 <b>(-24.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>24.87 (n/a)</td><td>24.25 (n/a)</td><td>24.61 (n/a)</td><td>23.28 (n/a)</td><td>0.66 (n/a)</td><td>24.86 (n/a)</td><td>24.24 (n/a)</td><td>24.59 (n/a)</td><td>23.26 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>41.26 (-4.96%)</td><td>39.42 (-4.79%)</td><td>39.36 (-5.85%)</td><td>38.03 (-2.87%)</td><td>1.17 <b>(-38.51%)</b></td><td>41.23 (-4.96%)</td><td>39.39 (-4.79%)</td><td>39.34 (-5.85%)</td><td>38.01 (-2.87%)</td><td>1.17 <b>(-38.51%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>43.41 (n/a)</td><td>41.40 (n/a)</td><td>41.81 (n/a)</td><td>39.16 (n/a)</td><td>1.90 (n/a)</td><td>43.38 (n/a)</td><td>41.38 (n/a)</td><td>41.78 (n/a)</td><td>39.13 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>45.06 (-0.87%)</td><td>43.32 (-0.29%)</td><td>43.47 (+1.37%)</td><td>42.09 (+0.59%)</td><td>1.19 <b>(-31.34%)</b></td><td>45.04 (-0.87%)</td><td>43.29 (-0.29%)</td><td>43.45 (+1.37%)</td><td>42.07 (+0.59%)</td><td>1.19 <b>(-31.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>45.46 (n/a)</td><td>43.45 (n/a)</td><td>42.88 (n/a)</td><td>41.84 (n/a)</td><td>1.73 (n/a)</td><td>45.43 (n/a)</td><td>43.42 (n/a)</td><td>42.86 (n/a)</td><td>41.82 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.36 (n/a)</td><td>13.24 (n/a)</td><td>13.27 (n/a)</td><td>13.02 (n/a)</td><td>0.13 (n/a)</td><td>13.35 (n/a)</td><td>13.23 (n/a)</td><td>13.26 (n/a)</td><td>13.02 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>24.41 (-2.84%)</td><td>24.00 (-1.70%)</td><td>23.90 (-1.30%)</td><td>23.84 (+0.05%)</td><td>0.23 <b>(-53.72%)</b></td><td>24.40 (-2.84%)</td><td>23.99 (-1.70%)</td><td>23.88 (-1.30%)</td><td>23.83 (+0.05%)</td><td>0.23 <b>(-53.72%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>25.13 (n/a)</td><td>24.41 (n/a)</td><td>24.21 (n/a)</td><td>23.83 (n/a)</td><td>0.51 (n/a)</td><td>25.11 (n/a)</td><td>24.40 (n/a)</td><td>24.20 (n/a)</td><td>23.81 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>41.19 (-3.79%)</td><td>36.69 (-8.50%)</td><td>39.16 (-1.84%)</td><td>24.46 <b>(-36.49%)</b></td><td>6.89 <b>(+318.45%)</b></td><td>41.16 (-3.79%)</td><td>36.66 (-8.50%)</td><td>39.14 (-1.84%)</td><td>24.44 <b>(-36.49%)</b></td><td>6.89 <b>(+318.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>42.81 (n/a)</td><td>40.10 (n/a)</td><td>39.89 (n/a)</td><td>38.50 (n/a)</td><td>1.65 (n/a)</td><td>42.79 (n/a)</td><td>40.07 (n/a)</td><td>39.87 (n/a)</td><td>38.48 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>42.99 (-5.72%)</td><td>42.64 (-4.47%)</td><td>42.55 (-5.33%)</td><td>42.43 (-0.12%)</td><td>0.24 <b>(-81.41%)</b></td><td>42.97 (-5.72%)</td><td>42.61 (-4.47%)</td><td>42.52 (-5.33%)</td><td>42.41 (-0.12%)</td><td>0.24 <b>(-81.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>45.60 (n/a)</td><td>44.63 (n/a)</td><td>44.94 (n/a)</td><td>42.48 (n/a)</td><td>1.28 (n/a)</td><td>45.57 (n/a)</td><td>44.61 (n/a)</td><td>44.92 (n/a)</td><td>42.45 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.13 (-12.63%)</td><td>8.68 (-0.84%)</td><td>8.63 (+3.57%)</td><td>8.41 (+11.60%)</td><td>0.27 <b>(-77.00%)</b></td><td>9.11 (-12.63%)</td><td>8.67 (-0.84%)</td><td>8.62 (+3.57%)</td><td>8.40 (+11.60%)</td><td>0.27 <b>(-77.00%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.45 (n/a)</td><td>8.76 (n/a)</td><td>8.34 (n/a)</td><td>7.54 (n/a)</td><td>1.17 (n/a)</td><td>10.43 (n/a)</td><td>8.74 (n/a)</td><td>8.32 (n/a)</td><td>7.53 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.91 (+4.76%)</td><td>0.78 (-0.22%)</td><td>0.75 (-4.02%)</td><td>0.69 (-5.46%)</td><td>0.09 <b>(+53.70%)</b></td><td>0.90 (+4.76%)</td><td>0.77 (-0.22%)</td><td>0.74 (-4.02%)</td><td>0.68 (-5.46%)</td><td>0.09 <b>(+53.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.87 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.06 (n/a)</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.17 (-8.96%)</td><td>1.03 (-8.87%)</td><td>1.11 (-8.72%)</td><td>0.86 (-1.58%)</td><td>0.15 (-19.94%)</td><td>1.16 (-8.96%)</td><td>1.02 (-8.87%)</td><td>1.10 (-8.72%)</td><td>0.85 (-1.58%)</td><td>0.14 (-19.94%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.29 (n/a)</td><td>1.13 (n/a)</td><td>1.22 (n/a)</td><td>0.87 (n/a)</td><td>0.18 (n/a)</td><td>1.27 (n/a)</td><td>1.12 (n/a)</td><td>1.21 (n/a)</td><td>0.86 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>15.80 (-0.53%)</td><td>14.82 (-1.48%)</td><td>14.67 (-1.94%)</td><td>13.80 (-4.63%)</td><td>0.78 <b>(+30.70%)</b></td><td>15.62 (-0.53%)</td><td>14.64 (-1.48%)</td><td>14.50 (-1.94%)</td><td>13.64 (-4.63%)</td><td>0.77 <b>(+30.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>15.89 (n/a)</td><td>15.04 (n/a)</td><td>14.96 (n/a)</td><td>14.47 (n/a)</td><td>0.59 (n/a)</td><td>15.70 (n/a)</td><td>14.87 (n/a)</td><td>14.78 (n/a)</td><td>14.30 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.12 (+0.84%)</td><td>10.89 (+1.20%)</td><td>11.76 (-0.50%)</td><td>6.95 (-10.38%)</td><td>2.21 <b>(+20.86%)</b></td><td>11.91 (+0.84%)</td><td>10.70 (+1.20%)</td><td>11.55 (-0.50%)</td><td>6.83 (-10.38%)</td><td>2.18 <b>(+20.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.02 (n/a)</td><td>10.76 (n/a)</td><td>11.82 (n/a)</td><td>7.75 (n/a)</td><td>1.83 (n/a)</td><td>11.81 (n/a)</td><td>10.57 (n/a)</td><td>11.61 (n/a)</td><td>7.62 (n/a)</td><td>1.80 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.91 <b>(-27.46%)</b></td><td>7.42 (-9.21%)</td><td>7.81 (+4.96%)</td><td>6.08 (-15.91%)</td><td>0.77 <b>(-50.19%)</b></td><td>7.78 <b>(-27.46%)</b></td><td>7.29 (-9.21%)</td><td>7.67 (+4.96%)</td><td>5.97 (-15.91%)</td><td>0.76 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.91 (n/a)</td><td>8.18 (n/a)</td><td>7.44 (n/a)</td><td>7.23 (n/a)</td><td>1.55 (n/a)</td><td>10.72 (n/a)</td><td>8.03 (n/a)</td><td>7.31 (n/a)</td><td>7.10 (n/a)</td><td>1.52 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>6.77 (-6.00%)</td><td>6.19 (+2.69%)</td><td>6.14 (+3.20%)</td><td>5.50 (+12.12%)</td><td>0.53 <b>(-36.99%)</b></td><td>6.66 (-6.00%)</td><td>6.09 (+2.69%)</td><td>6.05 (+3.20%)</td><td>5.42 (+12.12%)</td><td>0.52 <b>(-36.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.20 (n/a)</td><td>6.02 (n/a)</td><td>5.95 (n/a)</td><td>4.91 (n/a)</td><td>0.84 (n/a)</td><td>7.08 (n/a)</td><td>5.93 (n/a)</td><td>5.86 (n/a)</td><td>4.83 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.21 (n/a)</td><td>12.83 (n/a)</td><td>12.99 (n/a)</td><td>12.24 (n/a)</td><td>0.43 (n/a)</td><td>13.20 (n/a)</td><td>12.82 (n/a)</td><td>12.99 (n/a)</td><td>12.23 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.25 (n/a)</td><td>12.28 (n/a)</td><td>12.55 (n/a)</td><td>10.37 (n/a)</td><td>1.15 (n/a)</td><td>13.24 (n/a)</td><td>12.27 (n/a)</td><td>12.54 (n/a)</td><td>10.36 (n/a)</td><td>1.15 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.70 (n/a)</td><td>148.32 (n/a)</td><td>148.00 (n/a)</td><td>132.70 (n/a)</td><td>10.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>150.48 (n/a)</td><td>170.50 (n/a)</td><td>109.50 (n/a)</td><td>30.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>146.06 (n/a)</td><td>151.10 (n/a)</td><td>105.60 (n/a)</td><td>24.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>146.96 (n/a)</td><td>130.60 (n/a)</td><td>118.20 (n/a)</td><td>30.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.80 (n/a)</td><td>149.34 (n/a)</td><td>149.10 (n/a)</td><td>129.70 (n/a)</td><td>18.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>172.78 (n/a)</td><td>180.10 (n/a)</td><td>126.50 (n/a)</td><td>27.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.10 (n/a)</td><td>175.74 (n/a)</td><td>174.40 (n/a)</td><td>144.00 (n/a)</td><td>28.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>191.56 (n/a)</td><td>186.30 (n/a)</td><td>149.60 (n/a)</td><td>30.27 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>161.14 (n/a)</td><td>171.90 (n/a)</td><td>126.90 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>161.42 (n/a)</td><td>159.90 (n/a)</td><td>129.60 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>167.84 (n/a)</td><td>165.80 (n/a)</td><td>147.00 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>171.14 (n/a)</td><td>165.60 (n/a)</td><td>151.60 (n/a)</td><td>15.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>153.88 (n/a)</td><td>145.60 (n/a)</td><td>134.50 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>192.38 (n/a)</td><td>191.70 (n/a)</td><td>168.90 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>184.46 (n/a)</td><td>179.20 (n/a)</td><td>157.80 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.50 (n/a)</td><td>254.18 (n/a)</td><td>254.00 (n/a)</td><td>204.10 (n/a)</td><td>47.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>180.90 (n/a)</td><td>184.90 (n/a)</td><td>124.90 (n/a)</td><td>39.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>194.42 (n/a)</td><td>184.00 (n/a)</td><td>163.20 (n/a)</td><td>31.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>184.22 (n/a)</td><td>186.30 (n/a)</td><td>130.50 (n/a)</td><td>36.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>158.02 (n/a)</td><td>147.10 (n/a)</td><td>142.70 (n/a)</td><td>20.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>159.12 (n/a)</td><td>161.80 (n/a)</td><td>124.10 (n/a)</td><td>31.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>177.02 (n/a)</td><td>173.40 (n/a)</td><td>163.20 (n/a)</td><td>11.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>178.62 (n/a)</td><td>165.60 (n/a)</td><td>162.50 (n/a)</td><td>26.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>209.64 (n/a)</td><td>206.40 (n/a)</td><td>185.50 (n/a)</td><td>19.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>218.60 (n/a)</td><td>164.74 (n/a)</td><td>152.00 (n/a)</td><td>146.10 (n/a)</td><td>30.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>189.50 (n/a)</td><td>164.62 (n/a)</td><td>151.20 (n/a)</td><td>144.10 (n/a)</td><td>22.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.30 (n/a)</td><td>169.60 (n/a)</td><td>164.60 (n/a)</td><td>143.30 (n/a)</td><td>25.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>277.30 (n/a)</td><td>202.48 (n/a)</td><td>194.10 (n/a)</td><td>141.10 (n/a)</td><td>50.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>165.10 (n/a)</td><td>150.88 (n/a)</td><td>152.60 (n/a)</td><td>134.30 (n/a)</td><td>11.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.10 (n/a)</td><td>170.62 (n/a)</td><td>158.80 (n/a)</td><td>152.70 (n/a)</td><td>29.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>156.50 (n/a)</td><td>151.60 (n/a)</td><td>130.10 (n/a)</td><td>22.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.80 (n/a)</td><td>179.12 (n/a)</td><td>174.80 (n/a)</td><td>139.10 (n/a)</td><td>27.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+19.08%)</td><td>0.03 (+4.10%)</td><td>0.03 (+6.21%)</td><td>0.02 (-14.03%)</td><td>0.01 <b>(+118.22%)</b></td><td>210.60 (+16.35%)</td><td>165.60 (-1.39%)</td><td>163.50 (-5.82%)</td><td>119.90 (-15.98%)</td><td>32.77 <b>(+110.37%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.00 (n/a)</td><td>167.94 (n/a)</td><td>173.60 (n/a)</td><td>142.70 (n/a)</td><td>15.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+8.85%)</td><td>0.02 (-8.58%)</td><td>0.02 <b>(-23.80%)</b></td><td>0.02 (-10.63%)</td><td>0.01 <b>(+102.92%)</b></td><td>205.20 (+11.89%)</td><td>177.94 (+12.14%)</td><td>199.80 <b>(+31.27%)</b></td><td>130.50 (-8.16%)</td><td>33.76 <b>(+110.79%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>158.68 (n/a)</td><td>152.20 (n/a)</td><td>142.10 (n/a)</td><td>16.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-12.81%)</td><td>0.02 (-9.89%)</td><td>0.02 (-0.57%)</td><td>0.02 (-10.44%)</td><td>0.00 <b>(-28.26%)</b></td><td>195.90 (+11.69%)</td><td>171.52 (+10.53%)</td><td>164.50 (+0.55%)</td><td>152.40 (+14.67%)</td><td>17.76 (-6.22%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.40 (n/a)</td><td>155.18 (n/a)</td><td>163.60 (n/a)</td><td>132.90 (n/a)</td><td>18.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+17.62%)</td><td>0.02 (-0.66%)</td><td>0.02 (-10.90%)</td><td>0.02 (-7.14%)</td><td>0.00 <b>(+50.37%)</b></td><td>226.50 (+7.65%)</td><td>178.44 (+2.12%)</td><td>180.20 (+12.20%)</td><td>133.50 (-14.97%)</td><td>33.10 <b>(+38.33%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>174.74 (n/a)</td><td>160.60 (n/a)</td><td>157.00 (n/a)</td><td>23.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+8.64%)</td><td>0.02 (+7.17%)</td><td>0.02 (-1.07%)</td><td>0.02 (+16.15%)</td><td>0.00 (-3.54%)</td><td>199.30 (-13.95%)</td><td>179.88 (-7.16%)</td><td>189.70 (+1.07%)</td><td>145.10 (-7.99%)</td><td>21.77 <b>(-24.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.60 (n/a)</td><td>193.76 (n/a)</td><td>187.70 (n/a)</td><td>157.70 (n/a)</td><td>28.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+13.35%)</td><td>0.02 <b>(+20.99%)</b></td><td>0.02 <b>(+23.25%)</b></td><td>0.02 <b>(+61.66%)</b></td><td>0.00 <b>(-39.73%)</b></td><td>208.40 <b>(-38.16%)</b></td><td>179.72 <b>(-20.88%)</b></td><td>174.70 (-18.86%)</td><td>152.20 (-11.82%)</td><td>20.93 <b>(-67.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>337.00 (n/a)</td><td>227.14 (n/a)</td><td>215.30 (n/a)</td><td>172.60 (n/a)</td><td>65.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 <b>(+33.02%)</b></td><td>0.02 (+13.65%)</td><td>0.02 (+4.51%)</td><td>0.02 (+5.35%)</td><td>0.00 <b>(+115.28%)</b></td><td>221.20 (-5.11%)</td><td>185.48 (-10.66%)</td><td>191.80 (-4.29%)</td><td>140.10 <b>(-24.84%)</b></td><td>29.36 <b>(+47.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>207.62 (n/a)</td><td>200.40 (n/a)</td><td>186.40 (n/a)</td><td>19.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (-7.18%)</td><td>0.02 (+18.85%)</td><td>0.02 (+8.47%)</td><td>0.02 <b>(+58.49%)</b></td><td>0.00 <b>(-68.07%)</b></td><td>240.90 <b>(-36.90%)</b></td><td>213.26 <b>(-21.85%)</b></td><td>209.80 (-7.82%)</td><td>196.80 (+7.72%)</td><td>18.10 <b>(-79.25%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>381.80 (n/a)</td><td>272.88 (n/a)</td><td>227.60 (n/a)</td><td>182.70 (n/a)</td><td>87.21 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+52.75%)</b></td><td>0.05 (+14.79%)</td><td>0.05 (+2.34%)</td><td>0.04 (+5.22%)</td><td>0.01 <b>(+189.60%)</b></td><td>208.20 (-4.97%)</td><td>165.94 (-9.82%)</td><td>170.30 (-2.29%)</td><td>110.20 <b>(-34.56%)</b></td><td>35.28 <b>(+69.48%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>184.00 (n/a)</td><td>174.30 (n/a)</td><td>168.40 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 <b>(-23.85%)</b></td><td>0.05 (-6.85%)</td><td>0.05 (+0.13%)</td><td>0.04 (-0.77%)</td><td>0.00 <b>(-57.10%)</b></td><td>208.10 (+0.77%)</td><td>176.40 (+4.99%)</td><td>172.50 (-0.12%)</td><td>159.40 <b>(+31.41%)</b></td><td>18.54 <b>(-39.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>168.02 (n/a)</td><td>172.70 (n/a)</td><td>121.30 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (+0.82%)</td><td>0.05 (-8.37%)</td><td>0.05 (-10.12%)</td><td>0.04 (-16.09%)</td><td>0.01 <b>(+34.96%)</b></td><td>214.00 (+19.22%)</td><td>173.50 (+11.25%)</td><td>178.50 (+11.28%)</td><td>119.70 (-0.83%)</td><td>33.93 <b>(+57.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>155.96 (n/a)</td><td>160.40 (n/a)</td><td>120.70 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (+4.78%)</td><td>0.05 (-2.55%)</td><td>0.05 (-3.68%)</td><td>0.04 <b>(-25.74%)</b></td><td>0.01 <b>(+101.11%)</b></td><td>231.70 <b>(+34.63%)</b></td><td>172.54 (+6.01%)</td><td>175.30 (+3.79%)</td><td>129.40 (-4.57%)</td><td>39.77 <b>(+159.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>162.76 (n/a)</td><td>168.90 (n/a)</td><td>135.60 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+35.77%)</b></td><td>0.05 (+19.33%)</td><td>0.04 (+0.70%)</td><td>0.04 <b>(+59.86%)</b></td><td>0.01 <b>(+20.21%)</b></td><td>192.50 <b>(-37.46%)</b></td><td>166.30 (-17.80%)</td><td>184.20 (-0.70%)</td><td>117.60 <b>(-26.36%)</b></td><td>31.83 <b>(-47.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.80 (n/a)</td><td>202.30 (n/a)</td><td>185.50 (n/a)</td><td>159.70 (n/a)</td><td>60.06 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (+17.75%)</td><td>0.05 (+3.14%)</td><td>0.05 (+9.32%)</td><td>0.03 <b>(-25.78%)</b></td><td>0.01 <b>(+163.87%)</b></td><td>261.60 <b>(+34.71%)</b></td><td>181.94 (+1.65%)</td><td>166.90 (-8.50%)</td><td>130.50 (-15.04%)</td><td>50.00 <b>(+211.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>178.98 (n/a)</td><td>182.40 (n/a)</td><td>153.60 (n/a)</td><td>16.07 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-2.35%)</td><td>0.04 (-10.17%)</td><td>0.04 <b>(-21.59%)</b></td><td>0.04 (-3.33%)</td><td>0.01 (-2.50%)</td><td>210.30 (+3.44%)</td><td>187.00 (+11.32%)</td><td>196.50 <b>(+27.51%)</b></td><td>147.00 (+2.44%)</td><td>26.17 (+2.61%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>167.98 (n/a)</td><td>154.10 (n/a)</td><td>143.50 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-11.00%)</td><td>0.05 (+4.40%)</td><td>0.06 (+5.97%)</td><td>0.04 (+19.86%)</td><td>0.01 <b>(-33.01%)</b></td><td>197.00 (-16.60%)</td><td>163.10 (-7.02%)</td><td>148.30 (-5.66%)</td><td>139.30 (+12.34%)</td><td>27.72 <b>(-38.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>175.42 (n/a)</td><td>157.20 (n/a)</td><td>124.00 (n/a)</td><td>44.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-8.76%)</td><td>0.05 (+1.29%)</td><td>0.05 (-2.62%)</td><td>0.04 (+14.72%)</td><td>0.01 <b>(-38.50%)</b></td><td>192.20 (-12.83%)</td><td>166.98 (-4.14%)</td><td>167.50 (+2.70%)</td><td>133.40 (+9.61%)</td><td>23.35 <b>(-42.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>174.20 (n/a)</td><td>163.10 (n/a)</td><td>121.70 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-17.86%)</td><td>0.04 (+3.38%)</td><td>0.04 (+5.57%)</td><td>0.04 <b>(+69.92%)</b></td><td>0.00 <b>(-71.37%)</b></td><td>226.70 <b>(-41.15%)</b></td><td>202.42 (-12.39%)</td><td>208.20 (-5.28%)</td><td>180.20 <b>(+21.76%)</b></td><td>18.33 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>385.20 (n/a)</td><td>231.04 (n/a)</td><td>219.80 (n/a)</td><td>148.00 (n/a)</td><td>92.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (-1.77%)</td><td>0.11 (+10.78%)</td><td>0.12 <b>(+20.09%)</b></td><td>0.09 (+17.97%)</td><td>0.01 <b>(-34.28%)</b></td><td>173.20 (-15.26%)</td><td>148.94 (-11.67%)</td><td>141.40 (-16.73%)</td><td>129.90 (+1.80%)</td><td>19.19 <b>(-43.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>168.62 (n/a)</td><td>169.80 (n/a)</td><td>127.60 (n/a)</td><td>34.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (+6.51%)</td><td>0.09 (-4.94%)</td><td>0.11 (+15.15%)</td><td>0.05 <b>(-31.56%)</b></td><td>0.03 <b>(+146.56%)</b></td><td>306.60 <b>(+46.14%)</b></td><td>207.58 (+16.97%)</td><td>153.30 (-13.19%)</td><td>142.00 (-6.08%)</td><td>83.91 <b>(+242.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>177.46 (n/a)</td><td>176.60 (n/a)</td><td>151.20 (n/a)</td><td>24.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 <b>(-20.62%)</b></td><td>0.09 (-14.07%)</td><td>0.08 (-15.24%)</td><td>0.08 (-3.56%)</td><td>0.02 <b>(-38.30%)</b></td><td>213.30 (+3.69%)</td><td>185.12 (+13.45%)</td><td>194.80 (+17.99%)</td><td>134.40 <b>(+25.96%)</b></td><td>30.15 <b>(-20.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>205.70 (n/a)</td><td>163.18 (n/a)</td><td>165.10 (n/a)</td><td>106.70 (n/a)</td><td>37.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-3.29%)</td><td>0.09 (-1.39%)</td><td>0.09 (-5.66%)</td><td>0.08 (+9.77%)</td><td>0.01 <b>(-20.79%)</b></td><td>201.30 (-8.91%)</td><td>179.64 (+0.72%)</td><td>183.80 (+6.00%)</td><td>155.10 (+3.40%)</td><td>19.25 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>178.36 (n/a)</td><td>173.40 (n/a)</td><td>150.00 (n/a)</td><td>26.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-8.44%)</td><td>0.09 (-16.76%)</td><td>0.09 <b>(-24.20%)</b></td><td>0.07 (-3.50%)</td><td>0.02 (-14.77%)</td><td>233.10 (+3.65%)</td><td>187.40 (+19.03%)</td><td>186.10 <b>(+31.99%)</b></td><td>135.00 (+9.22%)</td><td>36.24 (-8.97%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.90 (n/a)</td><td>157.44 (n/a)</td><td>141.00 (n/a)</td><td>123.60 (n/a)</td><td>39.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (-17.75%)</td><td>0.09 (-3.50%)</td><td>0.09 (+6.67%)</td><td>0.07 (-1.66%)</td><td>0.01 <b>(-38.94%)</b></td><td>226.20 (+1.66%)</td><td>186.76 (+1.79%)</td><td>175.10 (-6.26%)</td><td>158.20 <b>(+21.51%)</b></td><td>27.43 <b>(-22.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>183.48 (n/a)</td><td>186.80 (n/a)</td><td>130.20 (n/a)</td><td>35.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-4.41%)</td><td>0.10 (+3.36%)</td><td>0.09 (+1.00%)</td><td>0.09 (+8.26%)</td><td>0.01 <b>(-28.36%)</b></td><td>183.70 (-7.64%)</td><td>167.70 (-4.06%)</td><td>173.60 (-0.97%)</td><td>144.30 (+4.64%)</td><td>16.99 <b>(-30.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>174.80 (n/a)</td><td>175.30 (n/a)</td><td>137.90 (n/a)</td><td>24.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (+10.86%)</td><td>0.08 (+11.83%)</td><td>0.08 (+8.73%)</td><td>0.05 (+19.26%)</td><td>0.02 (+3.85%)</td><td>321.30 (-16.15%)</td><td>224.98 (-11.56%)</td><td>201.80 (-8.06%)</td><td>180.00 (-9.82%)</td><td>58.35 <b>(-22.80%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>383.20 (n/a)</td><td>254.38 (n/a)</td><td>219.50 (n/a)</td><td>199.60 (n/a)</td><td>75.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 <b>(+51.85%)</b></td><td>0.24 <b>(+40.52%)</b></td><td>0.24 <b>(+34.77%)</b></td><td>0.19 <b>(+38.97%)</b></td><td>0.03 <b>(+74.52%)</b></td><td>168.20 <b>(-28.06%)</b></td><td>140.32 <b>(-28.52%)</b></td><td>139.40 <b>(-25.77%)</b></td><td>114.70 <b>(-34.16%)</b></td><td>19.48 (-18.07%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>196.30 (n/a)</td><td>187.80 (n/a)</td><td>174.20 (n/a)</td><td>23.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (-12.38%)</td><td>0.18 (-16.20%)</td><td>0.18 (-18.77%)</td><td>0.10 <b>(-30.69%)</b></td><td>0.05 (-14.41%)</td><td>318.60 <b>(+44.29%)</b></td><td>202.08 <b>(+20.62%)</b></td><td>187.00 <b>(+23.11%)</b></td><td>132.20 (+14.16%)</td><td>69.58 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>220.80 (n/a)</td><td>167.54 (n/a)</td><td>151.90 (n/a)</td><td>115.80 (n/a)</td><td>49.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (+2.81%)</td><td>0.19 (+5.52%)</td><td>0.19 (+0.90%)</td><td>0.17 (+16.55%)</td><td>0.02 <b>(-33.08%)</b></td><td>193.40 (-14.20%)</td><td>173.74 (-6.57%)</td><td>172.50 (-0.86%)</td><td>149.10 (-2.74%)</td><td>17.59 <b>(-44.76%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.40 (n/a)</td><td>185.96 (n/a)</td><td>174.00 (n/a)</td><td>153.30 (n/a)</td><td>31.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 <b>(+29.51%)</b></td><td>0.18 (+6.13%)</td><td>0.18 (-0.43%)</td><td>0.14 (+7.27%)</td><td>0.05 <b>(+66.07%)</b></td><td>241.80 (-6.78%)</td><td>186.78 (-3.55%)</td><td>187.20 (+0.43%)</td><td>122.90 <b>(-22.75%)</b></td><td>44.11 (+12.95%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.40 (n/a)</td><td>193.66 (n/a)</td><td>186.40 (n/a)</td><td>159.10 (n/a)</td><td>39.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (+11.27%)</td><td>0.17 (+3.34%)</td><td>0.15 (-10.31%)</td><td>0.14 (+5.09%)</td><td>0.04 <b>(+33.44%)</b></td><td>236.90 (-4.86%)</td><td>198.26 (-1.89%)</td><td>223.90 (+11.50%)</td><td>145.40 (-10.14%)</td><td>42.10 (+15.33%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>249.00 (n/a)</td><td>202.08 (n/a)</td><td>200.80 (n/a)</td><td>161.80 (n/a)</td><td>36.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (+3.49%)</td><td>0.17 (+5.02%)</td><td>0.17 (-1.96%)</td><td>0.15 <b>(+20.10%)</b></td><td>0.02 <b>(-34.65%)</b></td><td>211.50 (-16.73%)</td><td>193.60 (-6.25%)</td><td>192.20 (+2.02%)</td><td>164.70 (-3.40%)</td><td>18.86 <b>(-47.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>254.00 (n/a)</td><td>206.50 (n/a)</td><td>188.40 (n/a)</td><td>170.50 (n/a)</td><td>36.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (-9.05%)</td><td>0.14 (-6.24%)</td><td>0.15 (+4.40%)</td><td>0.10 <b>(-25.77%)</b></td><td>0.02 <b>(+40.07%)</b></td><td>320.60 <b>(+34.71%)</b></td><td>242.98 (+8.42%)</td><td>221.60 (-4.19%)</td><td>205.40 (+9.96%)</td><td>45.89 <b>(+114.65%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>238.00 (n/a)</td><td>224.12 (n/a)</td><td>231.30 (n/a)</td><td>186.80 (n/a)</td><td>21.38 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+2.57%)</td><td>0.02 (-10.58%)</td><td>0.02 (-9.10%)</td><td>0.02 <b>(-28.66%)</b></td><td>0.00 <b>(+126.97%)</b></td><td>262.60 <b>(+40.20%)</b></td><td>188.38 (+15.80%)</td><td>171.10 (+9.96%)</td><td>148.50 (-2.50%)</td><td>45.68 <b>(+214.14%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>162.68 (n/a)</td><td>155.60 (n/a)</td><td>152.30 (n/a)</td><td>14.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-16.40%)</td><td>0.02 (-3.92%)</td><td>0.02 (-7.53%)</td><td>0.02 (+18.25%)</td><td>0.00 <b>(-42.49%)</b></td><td>201.50 (-15.44%)</td><td>174.02 (+0.50%)</td><td>180.40 (+8.15%)</td><td>144.50 (+19.62%)</td><td>25.82 <b>(-42.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>173.16 (n/a)</td><td>166.80 (n/a)</td><td>120.80 (n/a)</td><td>45.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (-4.94%)</td><td>0.02 (-7.05%)</td><td>0.02 (-3.10%)</td><td>0.01 <b>(-30.42%)</b></td><td>0.00 <b>(+76.41%)</b></td><td>330.90 <b>(+43.68%)</b></td><td>225.38 (+11.66%)</td><td>213.10 (+3.25%)</td><td>179.40 (+5.16%)</td><td>61.09 <b>(+177.78%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.30 (n/a)</td><td>201.84 (n/a)</td><td>206.40 (n/a)</td><td>170.60 (n/a)</td><td>21.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+1.72%)</td><td>0.02 (+12.38%)</td><td>0.02 (+14.79%)</td><td>0.02 <b>(+24.60%)</b></td><td>0.00 <b>(-30.58%)</b></td><td>220.60 (-19.75%)</td><td>193.74 (-13.34%)</td><td>188.80 (-12.92%)</td><td>155.30 (-1.71%)</td><td>26.65 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.90 (n/a)</td><td>223.56 (n/a)</td><td>216.80 (n/a)</td><td>158.00 (n/a)</td><td>49.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-14.66%)</td><td>0.03 (-13.24%)</td><td>0.02 (-15.64%)</td><td>0.02 (-9.20%)</td><td>0.01 (-19.02%)</td><td>184.80 (+10.13%)</td><td>159.60 (+14.69%)</td><td>165.10 (+18.52%)</td><td>114.80 (+17.14%)</td><td>29.07 (+6.00%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>139.16 (n/a)</td><td>139.30 (n/a)</td><td>98.00 (n/a)</td><td>27.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-17.13%)</td><td>0.02 (-13.05%)</td><td>0.02 (-16.20%)</td><td>0.02 <b>(-20.12%)</b></td><td>0.01 (+5.22%)</td><td>224.20 <b>(+25.18%)</b></td><td>174.48 (+17.12%)</td><td>174.30 (+19.38%)</td><td>132.60 <b>(+20.77%)</b></td><td>42.15 <b>(+53.31%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>148.98 (n/a)</td><td>146.00 (n/a)</td><td>109.80 (n/a)</td><td>27.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+10.30%)</td><td>0.02 (+3.46%)</td><td>0.02 (-1.25%)</td><td>0.02 (+1.05%)</td><td>0.01 (+14.51%)</td><td>240.80 (-1.07%)</td><td>186.18 (-2.88%)</td><td>182.80 (+1.27%)</td><td>133.20 (-9.33%)</td><td>40.67 (+0.77%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.40 (n/a)</td><td>191.70 (n/a)</td><td>180.50 (n/a)</td><td>146.90 (n/a)</td><td>40.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (-16.24%)</td><td>0.02 (-16.82%)</td><td>0.02 (-2.07%)</td><td>0.01 <b>(-48.35%)</b></td><td>0.01 <b>(+83.81%)</b></td><td>365.90 <b>(+93.60%)</b></td><td>223.84 <b>(+28.35%)</b></td><td>187.70 (+2.12%)</td><td>173.80 (+19.45%)</td><td>80.57 <b>(+339.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>174.40 (n/a)</td><td>183.80 (n/a)</td><td>145.50 (n/a)</td><td>18.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 <b>(-20.62%)</b></td><td>0.02 (-5.52%)</td><td>0.02 (+16.38%)</td><td>0.02 (-15.15%)</td><td>0.00 <b>(-35.67%)</b></td><td>244.80 (+17.86%)</td><td>180.26 (+4.06%)</td><td>167.30 (-14.07%)</td><td>148.80 <b>(+25.99%)</b></td><td>37.77 (-2.06%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>173.22 (n/a)</td><td>194.70 (n/a)</td><td>118.10 (n/a)</td><td>38.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-7.22%)</td><td>0.03 (-0.50%)</td><td>0.02 (+10.60%)</td><td>0.02 (-5.66%)</td><td>0.01 (-17.00%)</td><td>212.40 (+5.99%)</td><td>167.04 (-0.37%)</td><td>166.20 (-9.58%)</td><td>126.80 (+7.82%)</td><td>32.95 (-5.80%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>167.66 (n/a)</td><td>183.80 (n/a)</td><td>117.60 (n/a)</td><td>34.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-19.56%)</td><td>0.02 (-8.54%)</td><td>0.02 (-5.08%)</td><td>0.02 (-0.83%)</td><td>0.00 <b>(-45.05%)</b></td><td>215.90 (+0.84%)</td><td>185.80 (+6.93%)</td><td>183.70 (+5.39%)</td><td>149.70 <b>(+24.34%)</b></td><td>24.19 <b>(-29.66%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>173.76 (n/a)</td><td>174.30 (n/a)</td><td>120.40 (n/a)</td><td>34.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 <b>(-30.90%)</b></td><td>0.02 <b>(-28.89%)</b></td><td>0.02 <b>(-38.29%)</b></td><td>0.02 (-4.29%)</td><td>0.00 <b>(-70.66%)</b></td><td>221.70 (+4.48%)</td><td>201.62 <b>(+34.90%)</b></td><td>208.00 <b>(+62.12%)</b></td><td>174.60 <b>(+44.78%)</b></td><td>17.68 <b>(-55.25%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>149.46 (n/a)</td><td>128.30 (n/a)</td><td>120.60 (n/a)</td><td>39.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-16.06%)</td><td>0.02 (-17.91%)</td><td>0.02 <b>(-28.37%)</b></td><td>0.02 (+14.35%)</td><td>0.00 <b>(-43.49%)</b></td><td>225.20 (-12.54%)</td><td>193.76 (+17.09%)</td><td>202.80 <b>(+39.67%)</b></td><td>156.60 (+19.09%)</td><td>28.89 <b>(-44.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.50 (n/a)</td><td>165.48 (n/a)</td><td>145.20 (n/a)</td><td>131.50 (n/a)</td><td>51.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+13.28%)</td><td>0.02 (+0.37%)</td><td>0.02 (-9.19%)</td><td>0.02 (+8.04%)</td><td>0.01 <b>(+32.67%)</b></td><td>202.50 (-7.45%)</td><td>171.96 (+0.60%)</td><td>175.40 (+10.11%)</td><td>127.10 (-11.67%)</td><td>32.54 (+9.31%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>170.94 (n/a)</td><td>159.30 (n/a)</td><td>143.90 (n/a)</td><td>29.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 <b>(+27.70%)</b></td><td>0.02 (+8.64%)</td><td>0.02 (+1.62%)</td><td>0.02 <b>(+25.43%)</b></td><td>0.01 <b>(+33.62%)</b></td><td>200.10 <b>(-20.25%)</b></td><td>176.36 (-7.71%)</td><td>185.30 (-1.59%)</td><td>123.70 <b>(-21.71%)</b></td><td>30.51 (-18.47%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>250.90 (n/a)</td><td>191.10 (n/a)</td><td>188.30 (n/a)</td><td>158.00 (n/a)</td><td>37.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 <b>(-22.99%)</b></td><td>0.02 (-9.90%)</td><td>0.02 (-7.93%)</td><td>0.02 (-4.71%)</td><td>0.00 <b>(-52.50%)</b></td><td>221.40 (+4.93%)</td><td>194.82 (+8.66%)</td><td>198.40 (+8.59%)</td><td>166.40 <b>(+29.90%)</b></td><td>21.32 <b>(-34.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>179.30 (n/a)</td><td>182.70 (n/a)</td><td>128.10 (n/a)</td><td>32.65 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-0.85%)</td><td>0.05 (-2.20%)</td><td>0.05 (-9.25%)</td><td>0.04 <b>(+27.02%)</b></td><td>0.01 <b>(-39.83%)</b></td><td>186.50 <b>(-21.27%)</b></td><td>168.78 (-3.19%)</td><td>178.00 (+10.22%)</td><td>124.20 (+0.89%)</td><td>25.59 <b>(-52.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>174.34 (n/a)</td><td>161.50 (n/a)</td><td>123.10 (n/a)</td><td>54.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+22.11%)</b></td><td>0.06 (+17.98%)</td><td>0.06 <b>(+29.81%)</b></td><td>0.05 (+9.56%)</td><td>0.01 <b>(+54.07%)</b></td><td>172.20 (-8.74%)</td><td>146.10 (-14.45%)</td><td>139.20 <b>(-22.97%)</b></td><td>118.00 (-18.11%)</td><td>23.54 (+17.70%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>170.78 (n/a)</td><td>180.70 (n/a)</td><td>144.10 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (+0.66%)</td><td>0.04 (-12.39%)</td><td>0.04 (-11.38%)</td><td>0.03 <b>(-29.22%)</b></td><td>0.01 <b>(+134.76%)</b></td><td>314.10 <b>(+41.23%)</b></td><td>226.66 (+18.94%)</td><td>210.70 (+12.85%)</td><td>176.60 (-0.67%)</td><td>58.00 <b>(+217.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.40 (n/a)</td><td>190.56 (n/a)</td><td>186.70 (n/a)</td><td>177.80 (n/a)</td><td>18.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-0.96%)</td><td>0.04 (-13.15%)</td><td>0.04 (-14.84%)</td><td>0.03 (-19.33%)</td><td>0.01 <b>(+37.03%)</b></td><td>288.70 <b>(+23.96%)</b></td><td>224.22 (+16.94%)</td><td>217.90 (+17.47%)</td><td>174.80 (+0.98%)</td><td>42.22 <b>(+72.47%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>191.74 (n/a)</td><td>185.50 (n/a)</td><td>173.10 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+25.68%)</b></td><td>0.06 <b>(+22.13%)</b></td><td>0.06 <b>(+20.62%)</b></td><td>0.04 (+14.51%)</td><td>0.01 <b>(+76.34%)</b></td><td>194.60 (-12.66%)</td><td>152.44 (-16.64%)</td><td>148.20 (-17.07%)</td><td>120.10 <b>(-20.46%)</b></td><td>31.71 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>182.86 (n/a)</td><td>178.70 (n/a)</td><td>151.00 (n/a)</td><td>26.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+53.84%)</b></td><td>0.06 <b>(+51.40%)</b></td><td>0.06 <b>(+52.20%)</b></td><td>0.05 <b>(+33.52%)</b></td><td>0.01 <b>(+107.90%)</b></td><td>178.80 <b>(-25.13%)</b></td><td>138.24 <b>(-33.26%)</b></td><td>131.00 <b>(-34.30%)</b></td><td>121.30 <b>(-34.96%)</b></td><td>23.31 (+4.02%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.80 (n/a)</td><td>207.12 (n/a)</td><td>199.40 (n/a)</td><td>186.50 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+21.55%)</b></td><td>0.05 (-1.57%)</td><td>0.05 (-10.55%)</td><td>0.04 (-4.42%)</td><td>0.01 <b>(+127.92%)</b></td><td>187.80 (+4.62%)</td><td>162.40 (+3.73%)</td><td>167.80 (+11.79%)</td><td>118.80 (-17.73%)</td><td>27.66 <b>(+93.47%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.50 (n/a)</td><td>156.56 (n/a)</td><td>150.10 (n/a)</td><td>144.40 (n/a)</td><td>14.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-1.23%)</td><td>0.06 (+15.32%)</td><td>0.06 <b>(+28.66%)</b></td><td>0.05 <b>(+23.65%)</b></td><td>0.01 <b>(-29.07%)</b></td><td>171.00 (-19.11%)</td><td>147.26 (-15.31%)</td><td>141.20 <b>(-22.29%)</b></td><td>122.50 (+1.24%)</td><td>22.10 <b>(-40.30%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>173.88 (n/a)</td><td>181.70 (n/a)</td><td>121.00 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-6.70%)</td><td>0.06 (-3.23%)</td><td>0.06 (-0.10%)</td><td>0.05 (+10.82%)</td><td>0.01 <b>(-35.05%)</b></td><td>171.80 (-9.77%)</td><td>145.48 (+1.42%)</td><td>145.10 (+0.14%)</td><td>120.40 (+7.12%)</td><td>18.43 <b>(-38.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>143.44 (n/a)</td><td>144.90 (n/a)</td><td>112.40 (n/a)</td><td>29.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-3.73%)</td><td>0.06 (+10.58%)</td><td>0.06 <b>(+26.20%)</b></td><td>0.05 (+1.44%)</td><td>0.01 (-15.45%)</td><td>181.80 (-1.46%)</td><td>147.80 (-10.02%)</td><td>136.80 <b>(-20.79%)</b></td><td>134.00 (+3.88%)</td><td>20.18 (-13.94%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>164.26 (n/a)</td><td>172.70 (n/a)</td><td>129.00 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-19.41%)</td><td>0.05 (+0.93%)</td><td>0.06 (+11.50%)</td><td>0.04 <b>(+33.88%)</b></td><td>0.01 <b>(-70.25%)</b></td><td>183.30 <b>(-25.31%)</b></td><td>156.26 (-8.81%)</td><td>147.90 (-10.31%)</td><td>144.50 <b>(+24.03%)</b></td><td>16.54 <b>(-71.21%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>245.40 (n/a)</td><td>171.36 (n/a)</td><td>164.90 (n/a)</td><td>116.50 (n/a)</td><td>57.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (+8.43%)</td><td>0.06 (+9.91%)</td><td>0.06 (+13.46%)</td><td>0.04 <b>(+32.63%)</b></td><td>0.02 (-17.23%)</td><td>197.10 <b>(-24.60%)</b></td><td>147.48 (-13.55%)</td><td>140.00 (-11.89%)</td><td>102.40 (-7.83%)</td><td>38.14 <b>(-39.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>261.40 (n/a)</td><td>170.60 (n/a)</td><td>158.90 (n/a)</td><td>111.10 (n/a)</td><td>63.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-10.07%)</td><td>0.05 (-3.87%)</td><td>0.05 (+5.39%)</td><td>0.04 (-8.72%)</td><td>0.01 <b>(-24.85%)</b></td><td>217.40 (+9.58%)</td><td>181.98 (+3.41%)</td><td>176.80 (-5.10%)</td><td>154.80 (+11.21%)</td><td>23.68 (-8.85%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>175.98 (n/a)</td><td>186.30 (n/a)</td><td>139.20 (n/a)</td><td>25.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-18.53%)</td><td>0.05 (-12.77%)</td><td>0.05 (-7.38%)</td><td>0.04 (-17.55%)</td><td>0.01 (-11.77%)</td><td>221.30 <b>(+21.26%)</b></td><td>178.06 (+14.97%)</td><td>165.50 (+7.96%)</td><td>149.90 <b>(+22.77%)</b></td><td>32.07 <b>(+28.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>154.88 (n/a)</td><td>153.30 (n/a)</td><td>122.10 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 <b>(-20.64%)</b></td><td>0.04 <b>(-21.46%)</b></td><td>0.05 (-14.66%)</td><td>0.02 <b>(-46.50%)</b></td><td>0.01 <b>(+24.29%)</b></td><td>346.90 <b>(+86.91%)</b></td><td>214.58 <b>(+34.57%)</b></td><td>180.50 (+17.21%)</td><td>157.50 <b>(+26.00%)</b></td><td>76.34 <b>(+201.57%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.60 (n/a)</td><td>159.46 (n/a)</td><td>154.00 (n/a)</td><td>125.00 (n/a)</td><td>25.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-11.78%)</td><td>0.04 <b>(-20.00%)</b></td><td>0.04 <b>(-23.61%)</b></td><td>0.04 (-19.10%)</td><td>0.01 (+0.04%)</td><td>217.20 <b>(+23.62%)</b></td><td>190.80 <b>(+25.96%)</b></td><td>200.30 <b>(+30.92%)</b></td><td>135.60 (+13.38%)</td><td>33.06 <b>(+35.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>151.48 (n/a)</td><td>153.00 (n/a)</td><td>119.60 (n/a)</td><td>24.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-0.13%)</td><td>0.11 (-6.28%)</td><td>0.10 (-15.73%)</td><td>0.08 (+5.66%)</td><td>0.03 (+6.51%)</td><td>215.60 (-5.36%)</td><td>161.76 (+6.76%)</td><td>157.90 (+18.63%)</td><td>117.00 (+0.09%)</td><td>41.75 (-5.03%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>227.80 (n/a)</td><td>151.52 (n/a)</td><td>133.10 (n/a)</td><td>116.90 (n/a)</td><td>43.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (+2.13%)</td><td>0.10 (-5.45%)</td><td>0.10 (-9.60%)</td><td>0.07 (-14.56%)</td><td>0.02 (+9.37%)</td><td>245.20 (+17.04%)</td><td>176.84 (+6.94%)</td><td>169.30 (+10.58%)</td><td>126.30 (-2.09%)</td><td>43.12 <b>(+25.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.50 (n/a)</td><td>165.36 (n/a)</td><td>153.10 (n/a)</td><td>129.00 (n/a)</td><td>34.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.08 (-13.38%)</td><td>0.07 (-17.17%)</td><td>0.07 <b>(-21.14%)</b></td><td>0.06 (-16.61%)</td><td>0.01 (-9.64%)</td><td>260.70 (+19.92%)</td><td>234.98 <b>(+20.84%)</b></td><td>241.00 <b>(+26.78%)</b></td><td>197.60 (+15.49%)</td><td>25.27 <b>(+22.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>194.46 (n/a)</td><td>190.10 (n/a)</td><td>171.10 (n/a)</td><td>20.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (+8.52%)</td><td>0.09 (+0.40%)</td><td>0.09 (-1.58%)</td><td>0.07 (-7.70%)</td><td>0.01 <b>(+35.45%)</b></td><td>233.00 (+8.32%)</td><td>191.24 (+0.50%)</td><td>191.30 (+1.59%)</td><td>150.70 (-7.89%)</td><td>30.42 <b>(+32.76%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>190.28 (n/a)</td><td>188.30 (n/a)</td><td>163.60 (n/a)</td><td>22.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-3.32%)</td><td>0.10 (-7.41%)</td><td>0.09 (-19.02%)</td><td>0.08 (+1.24%)</td><td>0.02 (+6.36%)</td><td>203.50 (-1.26%)</td><td>175.02 (+8.21%)</td><td>187.90 <b>(+23.46%)</b></td><td>143.10 (+3.47%)</td><td>27.23 (+3.77%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>161.74 (n/a)</td><td>152.20 (n/a)</td><td>138.30 (n/a)</td><td>26.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-8.85%)</td><td>0.12 (-2.04%)</td><td>0.12 (+3.54%)</td><td>0.10 (+15.32%)</td><td>0.02 <b>(-36.66%)</b></td><td>172.40 (-13.28%)</td><td>145.34 (-1.08%)</td><td>138.90 (-3.41%)</td><td>119.60 (+9.72%)</td><td>24.23 <b>(-36.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>198.80 (n/a)</td><td>146.92 (n/a)</td><td>143.80 (n/a)</td><td>109.00 (n/a)</td><td>38.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-10.41%)</td><td>0.09 (-19.43%)</td><td>0.09 (-15.12%)</td><td>0.07 <b>(-22.13%)</b></td><td>0.03 (+3.15%)</td><td>242.30 <b>(+28.40%)</b></td><td>185.32 <b>(+27.33%)</b></td><td>179.50 (+17.78%)</td><td>118.80 (+11.55%)</td><td>52.84 <b>(+56.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>188.70 (n/a)</td><td>145.54 (n/a)</td><td>152.40 (n/a)</td><td>106.50 (n/a)</td><td>33.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (+7.14%)</td><td>0.09 (-15.57%)</td><td>0.09 <b>(-21.14%)</b></td><td>0.07 <b>(-35.78%)</b></td><td>0.02 <b>(+286.30%)</b></td><td>248.70 <b>(+55.73%)</b></td><td>183.08 <b>(+24.02%)</b></td><td>187.90 <b>(+26.79%)</b></td><td>128.50 (-6.68%)</td><td>44.96 <b>(+457.20%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>159.70 (n/a)</td><td>147.62 (n/a)</td><td>148.20 (n/a)</td><td>137.70 (n/a)</td><td>8.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-4.32%)</td><td>0.11 (-9.89%)</td><td>0.12 (+5.52%)</td><td>0.06 <b>(-30.67%)</b></td><td>0.03 (+12.97%)</td><td>269.50 <b>(+44.27%)</b></td><td>169.62 (+15.94%)</td><td>136.30 (-5.22%)</td><td>116.00 (+4.50%)</td><td>62.44 <b>(+76.57%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>186.80 (n/a)</td><td>146.30 (n/a)</td><td>143.80 (n/a)</td><td>111.00 (n/a)</td><td>35.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-16.13%)</td><td>0.09 (-13.10%)</td><td>0.10 (-10.31%)</td><td>0.08 (-7.94%)</td><td>0.02 <b>(-22.41%)</b></td><td>213.80 (+8.64%)</td><td>179.10 (+14.31%)</td><td>170.10 (+11.54%)</td><td>134.10 (+19.20%)</td><td>33.26 (+3.81%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>156.68 (n/a)</td><td>152.50 (n/a)</td><td>112.50 (n/a)</td><td>32.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 <b>(+26.48%)</b></td><td>0.10 (+10.27%)</td><td>0.09 (+7.78%)</td><td>0.08 (+6.21%)</td><td>0.02 <b>(+56.35%)</b></td><td>216.40 (-5.87%)</td><td>175.76 (-7.66%)</td><td>180.30 (-7.21%)</td><td>120.40 <b>(-20.95%)</b></td><td>37.18 (+15.34%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.90 (n/a)</td><td>190.34 (n/a)</td><td>194.30 (n/a)</td><td>152.30 (n/a)</td><td>32.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (+5.12%)</td><td>0.10 (+3.67%)</td><td>0.11 (+16.34%)</td><td>0.08 (+7.13%)</td><td>0.02 (-3.18%)</td><td>195.70 (-6.63%)</td><td>163.22 (-3.95%)</td><td>152.10 (-14.02%)</td><td>123.40 (-4.86%)</td><td>30.77 (-10.05%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.60 (n/a)</td><td>169.94 (n/a)</td><td>176.90 (n/a)</td><td>129.70 (n/a)</td><td>34.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (+13.98%)</td><td>0.10 <b>(+22.66%)</b></td><td>0.10 <b>(+29.04%)</b></td><td>0.07 <b>(+31.80%)</b></td><td>0.02 (+16.54%)</td><td>223.10 <b>(-24.12%)</b></td><td>173.70 (-18.80%)</td><td>158.40 <b>(-22.50%)</b></td><td>140.30 (-12.26%)</td><td>37.24 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>294.00 (n/a)</td><td>213.92 (n/a)</td><td>204.40 (n/a)</td><td>159.90 (n/a)</td><td>49.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (+19.83%)</td><td>0.10 (+18.65%)</td><td>0.10 (+13.58%)</td><td>0.09 <b>(+24.23%)</b></td><td>0.01 <b>(+24.33%)</b></td><td>182.80 (-19.51%)</td><td>160.68 (-15.68%)</td><td>171.50 (-11.96%)</td><td>135.20 (-16.54%)</td><td>21.36 (-16.84%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>190.56 (n/a)</td><td>194.80 (n/a)</td><td>162.00 (n/a)</td><td>25.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 <b>(+25.49%)</b></td><td>0.09 (+11.90%)</td><td>0.09 (+6.44%)</td><td>0.06 (-7.78%)</td><td>0.03 <b>(+92.51%)</b></td><td>287.10 (+8.42%)</td><td>189.82 (-6.04%)</td><td>187.30 (-6.07%)</td><td>131.60 <b>(-20.29%)</b></td><td>61.56 <b>(+61.21%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>264.80 (n/a)</td><td>202.02 (n/a)</td><td>199.40 (n/a)</td><td>165.10 (n/a)</td><td>38.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.10 (-14.45%)</td><td>0.10 (-6.95%)</td><td>0.09 (-11.07%)</td><td>0.09 (-1.13%)</td><td>0.01 <b>(-45.97%)</b></td><td>189.30 (+1.18%)</td><td>171.06 (+6.38%)</td><td>173.20 (+12.47%)</td><td>156.10 (+16.93%)</td><td>13.91 <b>(-37.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>160.80 (n/a)</td><td>154.00 (n/a)</td><td>133.50 (n/a)</td><td>22.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+16.37%)</td><td>0.21 (+11.83%)</td><td>0.19 (+4.35%)</td><td>0.16 (+6.09%)</td><td>0.04 <b>(+48.08%)</b></td><td>202.80 (-5.76%)</td><td>163.12 (-9.57%)</td><td>171.30 (-4.19%)</td><td>128.50 (-14.05%)</td><td>29.63 (+17.94%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.20 (n/a)</td><td>180.38 (n/a)</td><td>178.80 (n/a)</td><td>149.50 (n/a)</td><td>25.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-8.48%)</td><td>0.21 (-0.58%)</td><td>0.21 (-1.39%)</td><td>0.19 (+6.55%)</td><td>0.02 <b>(-31.32%)</b></td><td>171.50 (-6.18%)</td><td>155.30 (-0.37%)</td><td>158.40 (+1.41%)</td><td>134.80 (+9.24%)</td><td>16.47 <b>(-28.92%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.80 (n/a)</td><td>155.88 (n/a)</td><td>156.20 (n/a)</td><td>123.40 (n/a)</td><td>23.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (-16.17%)</td><td>0.15 (-5.86%)</td><td>0.15 (-10.25%)</td><td>0.14 (+18.18%)</td><td>0.01 <b>(-65.18%)</b></td><td>239.00 (-15.37%)</td><td>222.52 (+2.38%)</td><td>224.40 (+11.42%)</td><td>196.30 (+19.26%)</td><td>17.62 <b>(-65.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>282.40 (n/a)</td><td>217.34 (n/a)</td><td>201.40 (n/a)</td><td>164.60 (n/a)</td><td>50.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (+2.79%)</td><td>0.18 (+7.57%)</td><td>0.17 (+13.48%)</td><td>0.15 (+18.57%)</td><td>0.03 (-15.64%)</td><td>223.40 (-15.67%)</td><td>190.62 (-8.51%)</td><td>192.10 (-11.88%)</td><td>143.30 (-2.72%)</td><td>30.19 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>264.90 (n/a)</td><td>208.34 (n/a)</td><td>218.00 (n/a)</td><td>147.30 (n/a)</td><td>43.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (-5.92%)</td><td>0.22 <b>(+24.04%)</b></td><td>0.24 <b>(+48.26%)</b></td><td>0.16 <b>(+36.00%)</b></td><td>0.05 <b>(-28.04%)</b></td><td>199.80 <b>(-26.46%)</b></td><td>152.40 <b>(-23.51%)</b></td><td>135.30 <b>(-32.55%)</b></td><td>116.40 (+6.30%)</td><td>36.45 <b>(-40.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>271.70 (n/a)</td><td>199.24 (n/a)</td><td>200.60 (n/a)</td><td>109.50 (n/a)</td><td>61.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 <b>(+23.41%)</b></td><td>0.20 (+0.47%)</td><td>0.20 (-0.99%)</td><td>0.12 <b>(-32.10%)</b></td><td>0.06 <b>(+228.76%)</b></td><td>264.60 <b>(+47.33%)</b></td><td>173.08 (+6.84%)</td><td>167.40 (+0.97%)</td><td>116.50 (-18.98%)</td><td>56.97 <b>(+300.74%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>162.00 (n/a)</td><td>165.80 (n/a)</td><td>143.80 (n/a)</td><td>14.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (-10.70%)</td><td>0.19 (-8.10%)</td><td>0.17 (-9.41%)</td><td>0.14 (-17.17%)</td><td>0.05 (+0.35%)</td><td>238.80 <b>(+20.73%)</b></td><td>185.20 (+10.36%)</td><td>192.10 (+10.40%)</td><td>128.50 (+11.93%)</td><td>44.49 <b>(+40.63%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>197.80 (n/a)</td><td>167.82 (n/a)</td><td>174.00 (n/a)</td><td>114.80 (n/a)</td><td>31.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (-3.37%)</td><td>0.20 (+4.26%)</td><td>0.18 (-1.67%)</td><td>0.16 (+0.37%)</td><td>0.04 (+10.17%)</td><td>210.30 (-0.38%)</td><td>170.68 (-3.34%)</td><td>185.00 (+1.70%)</td><td>131.00 (+3.48%)</td><td>35.84 (+13.58%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>176.58 (n/a)</td><td>181.90 (n/a)</td><td>126.60 (n/a)</td><td>31.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (-12.56%)</td><td>0.18 (-5.08%)</td><td>0.17 (-11.81%)</td><td>0.15 (+5.98%)</td><td>0.03 <b>(-37.51%)</b></td><td>215.70 (-5.64%)</td><td>187.34 (+3.14%)</td><td>197.30 (+13.39%)</td><td>150.90 (+14.40%)</td><td>25.18 <b>(-33.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>228.60 (n/a)</td><td>181.64 (n/a)</td><td>174.00 (n/a)</td><td>131.90 (n/a)</td><td>38.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (-9.04%)</td><td>0.19 (-11.04%)</td><td>0.17 <b>(-23.26%)</b></td><td>0.17 (-7.57%)</td><td>0.03 (-3.35%)</td><td>193.60 (+8.16%)</td><td>174.66 (+12.57%)</td><td>188.90 <b>(+30.37%)</b></td><td>145.20 (+9.92%)</td><td>23.44 (+13.47%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>179.00 (n/a)</td><td>155.16 (n/a)</td><td>144.90 (n/a)</td><td>132.10 (n/a)</td><td>20.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 <b>(+23.86%)</b></td><td>0.18 (-15.71%)</td><td>0.17 <b>(-23.48%)</b></td><td>0.11 <b>(-45.54%)</b></td><td>0.06 <b>(+514.78%)</b></td><td>298.60 <b>(+83.64%)</b></td><td>200.22 <b>(+30.25%)</b></td><td>195.70 <b>(+30.73%)</b></td><td>118.30 (-19.30%)</td><td>67.70 <b>(+799.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>162.60 (n/a)</td><td>153.72 (n/a)</td><td>149.70 (n/a)</td><td>146.60 (n/a)</td><td>7.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+5.81%)</td><td>0.18 (-1.12%)</td><td>0.17 (+10.92%)</td><td>0.14 (-11.63%)</td><td>0.05 (+5.78%)</td><td>242.00 (+13.14%)</td><td>186.56 (+1.69%)</td><td>190.60 (-9.84%)</td><td>126.50 (-5.53%)</td><td>44.28 (+8.88%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.90 (n/a)</td><td>183.46 (n/a)</td><td>211.40 (n/a)</td><td>133.90 (n/a)</td><td>40.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (+15.48%)</td><td>0.18 (+7.39%)</td><td>0.20 (+8.54%)</td><td>0.11 (-13.09%)</td><td>0.04 <b>(+66.10%)</b></td><td>299.90 (+15.08%)</td><td>189.72 (-3.02%)</td><td>167.40 (-7.87%)</td><td>147.80 (-13.42%)</td><td>62.40 <b>(+69.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>260.60 (n/a)</td><td>195.62 (n/a)</td><td>181.70 (n/a)</td><td>170.70 (n/a)</td><td>36.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 <b>(+22.38%)</b></td><td>0.21 (+6.48%)</td><td>0.19 (+1.09%)</td><td>0.16 (-5.45%)</td><td>0.05 <b>(+91.67%)</b></td><td>207.80 (+5.75%)</td><td>165.68 (-3.08%)</td><td>176.30 (-1.07%)</td><td>114.60 (-18.26%)</td><td>37.73 <b>(+65.23%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.50 (n/a)</td><td>170.94 (n/a)</td><td>178.20 (n/a)</td><td>140.20 (n/a)</td><td>22.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+17.57%)</td><td>0.17 (-3.09%)</td><td>0.15 (-15.53%)</td><td>0.13 (-3.40%)</td><td>0.05 <b>(+71.29%)</b></td><td>246.80 (+3.52%)</td><td>201.64 (+6.69%)</td><td>222.70 (+18.39%)</td><td>127.30 (-14.91%)</td><td>47.21 <b>(+45.72%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.40 (n/a)</td><td>189.00 (n/a)</td><td>188.10 (n/a)</td><td>149.60 (n/a)</td><td>32.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (+8.11%)</td><td>0.19 (-1.24%)</td><td>0.19 (+2.43%)</td><td>0.14 (-8.44%)</td><td>0.03 <b>(+41.02%)</b></td><td>226.50 (+9.21%)</td><td>180.34 (+2.65%)</td><td>173.00 (-2.37%)</td><td>138.30 (-7.49%)</td><td>33.20 <b>(+43.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>175.68 (n/a)</td><td>177.20 (n/a)</td><td>149.50 (n/a)</td><td>23.11 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (-13.70%)</td><td>0.18 (-13.85%)</td><td>0.18 (-13.87%)</td><td>0.18 (-13.99%)</td><td>0.00 <b>(+121.83%)</b></td><td>47538.60 (+16.27%)</td><td>47411.48 (+16.07%)</td><td>47417.00 (+16.11%)</td><td>47294.30 (+15.88%)</td><td>95.71 <b>(+198.78%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40887.80 (n/a)</td><td>40846.44 (n/a)</td><td>40838.80 (n/a)</td><td>40814.70 (n/a)</td><td>32.03 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (-13.94%)</td><td>0.18 (-13.83%)</td><td>0.18 (-13.82%)</td><td>0.18 (-13.76%)</td><td>0.00 <b>(-67.95%)</b></td><td>47440.60 (+15.95%)</td><td>47409.20 (+16.05%)</td><td>47413.40 (+16.04%)</td><td>47369.00 (+16.20%)</td><td>27.49 <b>(-56.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40913.40 (n/a)</td><td>40851.44 (n/a)</td><td>40861.10 (n/a)</td><td>40764.60 (n/a)</td><td>63.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-14.17%)</td><td>0.11 (-14.15%)</td><td>0.11 (-14.15%)</td><td>0.11 (-14.15%)</td><td>0.00 <b>(-32.44%)</b></td><td>374919.50 (+16.48%)</td><td>374743.28 (+16.49%)</td><td>374708.80 (+16.48%)</td><td>374591.70 (+16.51%)</td><td>132.90 (-8.33%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321884.10 (n/a)</td><td>321705.54 (n/a)</td><td>321704.70 (n/a)</td><td>321514.10 (n/a)</td><td>144.98 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+0.98%)</td><td>0.02 (-9.08%)</td><td>0.03 (-1.27%)</td><td>0.01 <b>(-45.16%)</b></td><td>0.01 <b>(+77.36%)</b></td><td>338.10 <b>(+82.36%)</b></td><td>191.08 <b>(+21.29%)</b></td><td>156.30 (+1.30%)</td><td>130.30 (-0.99%)</td><td>85.97 <b>(+224.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>157.54 (n/a)</td><td>154.30 (n/a)</td><td>131.60 (n/a)</td><td>26.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (+10.87%)</td><td>0.04 (+3.76%)</td><td>0.04 (-4.74%)</td><td>0.03 <b>(+25.94%)</b></td><td>0.01 (-0.09%)</td><td>221.50 <b>(-20.58%)</b></td><td>169.20 (-5.73%)</td><td>167.50 (+4.95%)</td><td>116.50 (-9.83%)</td><td>38.30 <b>(-33.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>278.90 (n/a)</td><td>179.48 (n/a)</td><td>159.60 (n/a)</td><td>129.20 (n/a)</td><td>57.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+4.30%)</td><td>0.03 <b>(+23.31%)</b></td><td>0.03 (+17.96%)</td><td>0.02 <b>(+42.22%)</b></td><td>0.00 <b>(-23.48%)</b></td><td>174.90 <b>(-29.67%)</b></td><td>150.30 <b>(-21.61%)</b></td><td>162.70 (-15.26%)</td><td>121.20 (-4.11%)</td><td>24.74 <b>(-49.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.70 (n/a)</td><td>191.74 (n/a)</td><td>192.00 (n/a)</td><td>126.40 (n/a)</td><td>48.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-0.66%)</td><td>0.03 (+6.24%)</td><td>0.04 (+12.26%)</td><td>0.03 (+1.47%)</td><td>0.00 (-2.99%)</td><td>187.90 (-1.42%)</td><td>151.26 (-5.92%)</td><td>145.80 (-10.88%)</td><td>134.20 (+0.68%)</td><td>21.57 (-1.81%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>160.78 (n/a)</td><td>163.60 (n/a)</td><td>133.30 (n/a)</td><td>21.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (+11.04%)</td><td>0.03 <b>(+30.86%)</b></td><td>0.03 <b>(+30.21%)</b></td><td>0.02 <b>(+77.52%)</b></td><td>0.00 <b>(-36.65%)</b></td><td>170.10 <b>(-43.66%)</b></td><td>137.52 <b>(-28.21%)</b></td><td>135.80 <b>(-23.19%)</b></td><td>115.30 (-9.92%)</td><td>20.53 <b>(-68.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>301.90 (n/a)</td><td>191.56 (n/a)</td><td>176.80 (n/a)</td><td>128.00 (n/a)</td><td>65.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-3.25%)</td><td>0.03 (-14.20%)</td><td>0.03 (-19.59%)</td><td>0.02 <b>(-39.78%)</b></td><td>0.01 <b>(+37.62%)</b></td><td>308.20 <b>(+66.06%)</b></td><td>186.34 <b>(+24.84%)</b></td><td>169.60 <b>(+24.43%)</b></td><td>124.80 (+3.40%)</td><td>73.65 <b>(+135.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.60 (n/a)</td><td>149.26 (n/a)</td><td>136.30 (n/a)</td><td>120.70 (n/a)</td><td>31.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+15.80%)</td><td>0.03 <b>(+23.29%)</b></td><td>0.03 <b>(+28.25%)</b></td><td>0.02 <b>(+23.27%)</b></td><td>0.00 (-2.59%)</td><td>170.00 (-18.89%)</td><td>146.50 (-19.29%)</td><td>147.80 <b>(-22.05%)</b></td><td>127.80 (-13.65%)</td><td>16.56 <b>(-31.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.60 (n/a)</td><td>181.52 (n/a)</td><td>189.60 (n/a)</td><td>148.00 (n/a)</td><td>24.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-14.77%)</td><td>0.03 (-9.21%)</td><td>0.03 (-12.02%)</td><td>0.02 (+11.53%)</td><td>0.00 <b>(-44.68%)</b></td><td>210.70 (-10.34%)</td><td>181.00 (+7.09%)</td><td>182.60 (+13.63%)</td><td>149.80 (+17.31%)</td><td>22.93 <b>(-43.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>169.02 (n/a)</td><td>160.70 (n/a)</td><td>127.70 (n/a)</td><td>40.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-5.23%)</td><td>0.03 (+17.69%)</td><td>0.03 <b>(+37.08%)</b></td><td>0.02 (+16.97%)</td><td>0.00 <b>(-22.79%)</b></td><td>180.50 (-14.54%)</td><td>149.32 (-16.58%)</td><td>132.80 <b>(-27.03%)</b></td><td>124.00 (+5.53%)</td><td>27.12 <b>(-26.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>179.00 (n/a)</td><td>182.00 (n/a)</td><td>117.50 (n/a)</td><td>36.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 <b>(+20.02%)</b></td><td>0.03 (+4.30%)</td><td>0.03 (+4.83%)</td><td>0.02 (-12.58%)</td><td>0.01 <b>(+66.51%)</b></td><td>238.10 (+14.42%)</td><td>161.38 (+0.34%)</td><td>152.20 (-4.64%)</td><td>105.80 (-16.69%)</td><td>50.54 <b>(+60.30%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>160.84 (n/a)</td><td>159.60 (n/a)</td><td>127.00 (n/a)</td><td>31.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 <b>(+24.38%)</b></td><td>0.02 (+4.68%)</td><td>0.02 (-6.14%)</td><td>0.02 (-1.20%)</td><td>0.00 <b>(+85.86%)</b></td><td>205.60 (+1.23%)</td><td>176.38 (-3.03%)</td><td>184.50 (+6.52%)</td><td>130.40 (-19.56%)</td><td>28.05 <b>(+42.71%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>181.90 (n/a)</td><td>173.20 (n/a)</td><td>162.10 (n/a)</td><td>19.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (+7.19%)</td><td>0.03 (-6.45%)</td><td>0.02 (-12.15%)</td><td>0.02 (-16.47%)</td><td>0.01 <b>(+66.16%)</b></td><td>222.30 (+19.71%)</td><td>176.12 (+9.53%)</td><td>183.30 (+13.85%)</td><td>125.50 (-6.69%)</td><td>35.92 <b>(+81.97%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>160.80 (n/a)</td><td>161.00 (n/a)</td><td>134.50 (n/a)</td><td>19.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.03 (-13.64%)</td><td>0.02 (+6.22%)</td><td>0.02 <b>(+23.77%)</b></td><td>0.02 (-9.61%)</td><td>0.01 (-13.30%)</td><td>265.00 (+10.65%)</td><td>183.30 (-5.90%)</td><td>168.10 (-19.22%)</td><td>140.50 (+15.83%)</td><td>51.62 (+14.32%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>194.80 (n/a)</td><td>208.10 (n/a)</td><td>121.30 (n/a)</td><td>45.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 <b>(+48.89%)</b></td><td>0.02 (-2.25%)</td><td>0.02 (-10.58%)</td><td>0.01 <b>(-35.84%)</b></td><td>0.01 <b>(+497.26%)</b></td><td>292.20 <b>(+55.84%)</b></td><td>202.68 (+13.36%)</td><td>204.90 (+11.84%)</td><td>107.10 <b>(-32.85%)</b></td><td>65.69 <b>(+490.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.50 (n/a)</td><td>178.80 (n/a)</td><td>183.20 (n/a)</td><td>159.50 (n/a)</td><td>11.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.02 (+2.31%)</td><td>0.02 (-0.72%)</td><td>0.02 (-8.78%)</td><td>0.01 (+9.33%)</td><td>0.00 (-7.31%)</td><td>331.70 (-8.55%)</td><td>234.90 (-0.82%)</td><td>233.40 (+9.63%)</td><td>172.00 (-2.27%)</td><td>60.44 (-18.58%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>362.70 (n/a)</td><td>236.84 (n/a)</td><td>212.90 (n/a)</td><td>176.00 (n/a)</td><td>74.24 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-8.48%)</td><td>0.04 (-12.80%)</td><td>0.04 (-14.84%)</td><td>0.04 (-6.10%)</td><td>0.01 (-15.82%)</td><td>230.60 (+6.51%)</td><td>198.36 (+13.75%)</td><td>218.70 (+17.39%)</td><td>135.80 (+9.25%)</td><td>41.22 (-0.43%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>174.38 (n/a)</td><td>186.30 (n/a)</td><td>124.30 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 <b>(-20.88%)</b></td><td>0.07 (-17.31%)</td><td>0.07 (-6.74%)</td><td>0.05 <b>(-30.49%)</b></td><td>0.02 <b>(-20.30%)</b></td><td>263.20 <b>(+43.83%)</b></td><td>181.68 <b>(+21.77%)</b></td><td>164.90 (+7.22%)</td><td>137.10 <b>(+26.36%)</b></td><td>48.80 <b>(+48.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>149.20 (n/a)</td><td>153.80 (n/a)</td><td>108.50 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-11.43%)</td><td>0.05 (+4.64%)</td><td>0.05 (+11.54%)</td><td>0.04 <b>(+43.19%)</b></td><td>0.01 <b>(-45.91%)</b></td><td>196.70 <b>(-30.15%)</b></td><td>168.14 (-10.25%)</td><td>159.80 (-10.33%)</td><td>134.50 (+12.93%)</td><td>27.28 <b>(-56.11%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>281.60 (n/a)</td><td>187.34 (n/a)</td><td>178.20 (n/a)</td><td>119.10 (n/a)</td><td>62.15 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (-12.06%)</td><td>0.06 (-4.19%)</td><td>0.06 (+8.61%)</td><td>0.04 (-1.03%)</td><td>0.01 <b>(-28.12%)</b></td><td>243.90 (+1.08%)</td><td>187.30 (+2.14%)</td><td>178.70 (-7.93%)</td><td>139.80 (+13.66%)</td><td>39.08 (-15.57%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>241.30 (n/a)</td><td>183.38 (n/a)</td><td>194.10 (n/a)</td><td>123.00 (n/a)</td><td>46.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-8.86%)</td><td>0.05 (+17.12%)</td><td>0.05 <b>(+25.65%)</b></td><td>0.05 <b>(+72.52%)</b></td><td>0.00 <b>(-78.47%)</b></td><td>171.20 <b>(-42.03%)</b></td><td>155.92 <b>(-22.83%)</b></td><td>152.70 <b>(-20.43%)</b></td><td>145.40 (+9.65%)</td><td>10.38 <b>(-85.67%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>295.30 (n/a)</td><td>202.04 (n/a)</td><td>191.90 (n/a)</td><td>132.60 (n/a)</td><td>72.48 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 <b>(+30.25%)</b></td><td>0.06 (-2.41%)</td><td>0.06 (-5.24%)</td><td>0.05 <b>(-23.54%)</b></td><td>0.02 <b>(+463.51%)</b></td><td>217.90 <b>(+30.79%)</b></td><td>170.10 (+6.82%)</td><td>171.30 (+5.55%)</td><td>116.50 <b>(-23.20%)</b></td><td>37.27 <b>(+454.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>166.60 (n/a)</td><td>159.24 (n/a)</td><td>162.30 (n/a)</td><td>151.70 (n/a)</td><td>6.72 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 <b>(-24.47%)</b></td><td>0.05 (-16.26%)</td><td>0.05 (-5.99%)</td><td>0.04 (-10.54%)</td><td>0.01 <b>(-46.75%)</b></td><td>211.20 (+11.81%)</td><td>173.74 (+16.45%)</td><td>170.00 (+6.38%)</td><td>146.80 <b>(+32.37%)</b></td><td>27.32 (-19.80%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>149.20 (n/a)</td><td>159.80 (n/a)</td><td>110.90 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 <b>(-23.89%)</b></td><td>0.04 (-15.06%)</td><td>0.05 (-6.94%)</td><td>0.04 (-7.07%)</td><td>0.00 <b>(-55.95%)</b></td><td>225.80 (+7.58%)</td><td>205.86 (+16.19%)</td><td>197.10 (+7.41%)</td><td>188.10 <b>(+31.35%)</b></td><td>16.60 <b>(-36.48%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>177.18 (n/a)</td><td>183.50 (n/a)</td><td>143.20 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-14.73%)</td><td>0.05 (-8.49%)</td><td>0.06 (-3.19%)</td><td>0.05 (-4.75%)</td><td>0.00 <b>(-53.73%)</b></td><td>164.60 (+4.97%)</td><td>150.12 (+8.55%)</td><td>146.70 (+3.31%)</td><td>142.80 (+17.24%)</td><td>8.54 <b>(-41.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>156.80 (n/a)</td><td>138.30 (n/a)</td><td>142.00 (n/a)</td><td>121.80 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 (+9.19%)</td><td>0.05 (-6.11%)</td><td>0.05 (-16.05%)</td><td>0.04 (-4.32%)</td><td>0.01 <b>(+40.72%)</b></td><td>206.60 (+4.50%)</td><td>173.86 (+7.80%)</td><td>180.90 (+19.09%)</td><td>126.00 (-8.43%)</td><td>29.85 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>161.28 (n/a)</td><td>151.90 (n/a)</td><td>137.60 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-11.55%)</td><td>0.05 (-8.93%)</td><td>0.05 (-9.15%)</td><td>0.04 (+18.24%)</td><td>0.01 <b>(-42.60%)</b></td><td>208.60 (-15.44%)</td><td>183.86 (+6.93%)</td><td>172.10 (+10.04%)</td><td>159.50 (+13.04%)</td><td>22.73 <b>(-46.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>171.94 (n/a)</td><td>156.40 (n/a)</td><td>141.10 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.05 (-6.77%)</td><td>0.04 (-14.73%)</td><td>0.04 (-9.73%)</td><td>0.02 <b>(-40.20%)</b></td><td>0.01 <b>(+45.90%)</b></td><td>370.00 <b>(+67.19%)</b></td><td>232.30 <b>(+23.52%)</b></td><td>201.40 (+10.78%)</td><td>172.70 (+7.27%)</td><td>78.88 <b>(+179.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>188.06 (n/a)</td><td>181.80 (n/a)</td><td>161.00 (n/a)</td><td>28.27 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.07 <b>(+32.82%)</b></td><td>0.05 (+12.26%)</td><td>0.05 (+3.88%)</td><td>0.04 <b>(+27.20%)</b></td><td>0.01 <b>(+41.91%)</b></td><td>188.90 <b>(-21.39%)</b></td><td>158.24 (-10.47%)</td><td>159.10 (-3.69%)</td><td>113.80 <b>(-24.69%)</b></td><td>30.47 (-17.08%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>176.74 (n/a)</td><td>165.20 (n/a)</td><td>151.10 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.06 (-8.66%)</td><td>0.05 (-2.72%)</td><td>0.05 (-0.23%)</td><td>0.04 (+9.35%)</td><td>0.01 <b>(-32.15%)</b></td><td>209.80 (-8.54%)</td><td>179.70 (+1.32%)</td><td>175.50 (+0.23%)</td><td>155.00 (+9.46%)</td><td>22.76 <b>(-32.46%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>177.36 (n/a)</td><td>175.10 (n/a)</td><td>141.60 (n/a)</td><td>33.70 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.04 (-12.87%)</td><td>0.04 (-15.57%)</td><td>0.04 (-19.60%)</td><td>0.03 (-5.67%)</td><td>0.00 <b>(-36.89%)</b></td><td>258.10 (+6.00%)</td><td>225.84 (+17.47%)</td><td>221.00 <b>(+24.37%)</b></td><td>198.80 (+14.78%)</td><td>22.37 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.50 (n/a)</td><td>192.26 (n/a)</td><td>177.70 (n/a)</td><td>173.20 (n/a)</td><td>29.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (+4.44%)</td><td>0.09 (-5.64%)</td><td>0.09 (-14.72%)</td><td>0.08 (-0.32%)</td><td>0.01 (+1.18%)</td><td>205.90 (+0.29%)</td><td>178.28 (+5.94%)</td><td>183.00 (+17.31%)</td><td>143.70 (-4.20%)</td><td>22.91 (-3.86%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>168.28 (n/a)</td><td>156.00 (n/a)</td><td>150.00 (n/a)</td><td>23.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (+10.91%)</td><td>0.17 (+3.22%)</td><td>0.18 (+4.49%)</td><td>0.12 (-5.68%)</td><td>0.03 <b>(+36.30%)</b></td><td>201.40 (+6.06%)</td><td>146.60 (-1.66%)</td><td>139.90 (-4.24%)</td><td>118.10 (-9.85%)</td><td>32.34 <b>(+34.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.90 (n/a)</td><td>149.08 (n/a)</td><td>146.10 (n/a)</td><td>131.00 (n/a)</td><td>24.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-2.92%)</td><td>0.09 (+1.98%)</td><td>0.09 (+0.06%)</td><td>0.09 (+18.17%)</td><td>0.01 <b>(-52.92%)</b></td><td>189.60 (-15.39%)</td><td>174.12 (-3.95%)</td><td>177.20 (-0.06%)</td><td>154.60 (+3.00%)</td><td>13.77 <b>(-58.07%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>181.28 (n/a)</td><td>177.30 (n/a)</td><td>150.10 (n/a)</td><td>32.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (+7.60%)</td><td>0.14 (+8.43%)</td><td>0.14 (+15.88%)</td><td>0.09 (-16.43%)</td><td>0.03 <b>(+85.46%)</b></td><td>216.40 (+19.62%)</td><td>156.24 (-4.01%)</td><td>142.50 (-13.74%)</td><td>119.10 (-7.10%)</td><td>42.43 <b>(+104.57%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>180.90 (n/a)</td><td>162.76 (n/a)</td><td>165.20 (n/a)</td><td>128.20 (n/a)</td><td>20.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-10.60%)</td><td>0.10 (-5.06%)</td><td>0.09 (-8.17%)</td><td>0.08 (+0.55%)</td><td>0.02 <b>(-20.34%)</b></td><td>198.70 (-0.55%)</td><td>170.54 (+4.32%)</td><td>177.90 (+8.94%)</td><td>141.10 (+11.90%)</td><td>27.77 (-13.83%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>163.48 (n/a)</td><td>163.30 (n/a)</td><td>126.10 (n/a)</td><td>32.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (+2.50%)</td><td>0.13 (-5.22%)</td><td>0.13 (-3.93%)</td><td>0.10 (-2.66%)</td><td>0.03 (+9.69%)</td><td>207.10 (+2.73%)</td><td>168.50 (+6.15%)</td><td>161.40 (+4.06%)</td><td>125.40 (-2.41%)</td><td>33.32 (+12.53%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>201.60 (n/a)</td><td>158.74 (n/a)</td><td>155.10 (n/a)</td><td>128.50 (n/a)</td><td>29.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (+3.84%)</td><td>0.09 (-7.03%)</td><td>0.08 (-15.83%)</td><td>0.07 <b>(-20.82%)</b></td><td>0.02 <b>(+139.73%)</b></td><td>231.30 <b>(+26.32%)</b></td><td>188.66 (+10.87%)</td><td>203.40 (+18.81%)</td><td>142.90 (-3.71%)</td><td>38.47 <b>(+190.41%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>170.16 (n/a)</td><td>171.20 (n/a)</td><td>148.40 (n/a)</td><td>13.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 <b>(-22.42%)</b></td><td>0.10 (-12.27%)</td><td>0.10 (-10.54%)</td><td>0.09 (-6.37%)</td><td>0.01 <b>(-51.56%)</b></td><td>203.70 (+6.82%)</td><td>182.80 (+12.20%)</td><td>181.20 (+11.78%)</td><td>159.30 <b>(+28.88%)</b></td><td>17.85 <b>(-32.79%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>162.92 (n/a)</td><td>162.10 (n/a)</td><td>123.60 (n/a)</td><td>26.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (+3.16%)</td><td>0.12 <b>(+31.21%)</b></td><td>0.13 <b>(+55.77%)</b></td><td>0.08 <b>(+102.16%)</b></td><td>0.02 <b>(-33.89%)</b></td><td>200.20 <b>(-50.52%)</b></td><td>147.82 <b>(-32.70%)</b></td><td>128.30 <b>(-35.82%)</b></td><td>119.20 (-3.09%)</td><td>33.78 <b>(-69.32%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>404.60 (n/a)</td><td>219.64 (n/a)</td><td>199.90 (n/a)</td><td>123.00 (n/a)</td><td>110.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (+12.96%)</td><td>0.11 (+7.35%)</td><td>0.09 (-6.58%)</td><td>0.08 (+17.71%)</td><td>0.03 <b>(+27.24%)</b></td><td>224.20 (-15.04%)</td><td>182.16 (-5.77%)</td><td>200.20 (+7.06%)</td><td>119.70 (-11.46%)</td><td>44.94 (-3.32%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>263.90 (n/a)</td><td>193.32 (n/a)</td><td>187.00 (n/a)</td><td>135.20 (n/a)</td><td>46.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (+0.40%)</td><td>0.10 (+4.87%)</td><td>0.08 (-5.29%)</td><td>0.08 (+13.08%)</td><td>0.02 (+13.16%)</td><td>206.60 (-11.56%)</td><td>173.82 (-4.10%)</td><td>196.30 (+5.59%)</td><td>130.30 (-0.38%)</td><td>39.28 (-0.45%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.60 (n/a)</td><td>181.26 (n/a)</td><td>185.90 (n/a)</td><td>130.80 (n/a)</td><td>39.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 <b>(+37.78%)</b></td><td>0.10 (+15.03%)</td><td>0.09 (+14.95%)</td><td>0.07 (+16.47%)</td><td>0.03 <b>(+50.86%)</b></td><td>252.10 (-14.13%)</td><td>186.40 (-11.08%)</td><td>188.20 (-12.99%)</td><td>114.10 <b>(-27.46%)</b></td><td>53.78 (-3.36%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>293.60 (n/a)</td><td>209.62 (n/a)</td><td>216.30 (n/a)</td><td>157.30 (n/a)</td><td>55.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 (-12.62%)</td><td>0.09 (-8.18%)</td><td>0.10 (-6.05%)</td><td>0.08 (-5.37%)</td><td>0.01 (-19.57%)</td><td>216.10 (+5.67%)</td><td>175.72 (+8.47%)</td><td>166.70 (+6.45%)</td><td>155.40 (+14.43%)</td><td>24.28 (-4.50%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>162.00 (n/a)</td><td>156.60 (n/a)</td><td>135.80 (n/a)</td><td>25.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-7.18%)</td><td>0.09 (-11.82%)</td><td>0.08 (-17.33%)</td><td>0.08 (-10.80%)</td><td>0.02 (+2.18%)</td><td>223.30 (+12.15%)</td><td>195.80 (+14.02%)</td><td>209.90 <b>(+20.91%)</b></td><td>141.30 (+7.78%)</td><td>33.24 <b>(+21.54%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>171.72 (n/a)</td><td>173.60 (n/a)</td><td>131.10 (n/a)</td><td>27.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.09 (-1.38%)</td><td>0.08 (-10.70%)</td><td>0.07 (-17.96%)</td><td>0.06 (-10.37%)</td><td>0.01 (+3.36%)</td><td>265.30 (+11.56%)</td><td>223.10 (+12.37%)</td><td>220.20 <b>(+21.93%)</b></td><td>174.30 (+1.40%)</td><td>35.20 (+16.47%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>198.54 (n/a)</td><td>180.60 (n/a)</td><td>171.90 (n/a)</td><td>30.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-6.54%)</td><td>0.19 (-6.30%)</td><td>0.19 (-7.76%)</td><td>0.15 (-2.07%)</td><td>0.03 (-6.56%)</td><td>212.60 (+2.11%)</td><td>174.58 (+6.61%)</td><td>173.30 (+8.45%)</td><td>139.00 (+7.01%)</td><td>28.81 (+0.75%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.20 (n/a)</td><td>163.76 (n/a)</td><td>159.80 (n/a)</td><td>129.90 (n/a)</td><td>28.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (+0.80%)</td><td>0.22 (-6.04%)</td><td>0.23 (-0.45%)</td><td>0.18 (-10.11%)</td><td>0.04 <b>(+65.84%)</b></td><td>178.50 (+11.28%)</td><td>150.66 (+8.06%)</td><td>140.00 (+0.43%)</td><td>122.70 (-0.81%)</td><td>25.44 <b>(+88.36%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>160.40 (n/a)</td><td>139.42 (n/a)</td><td>139.40 (n/a)</td><td>123.70 (n/a)</td><td>13.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (-1.18%)</td><td>0.27 (+9.42%)</td><td>0.26 (+11.44%)</td><td>0.19 (-3.07%)</td><td>0.05 (+2.89%)</td><td>217.60 (+3.18%)</td><td>159.28 (-8.30%)</td><td>155.20 (-10.29%)</td><td>132.30 (+1.22%)</td><td>34.41 (+8.97%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>210.90 (n/a)</td><td>173.70 (n/a)</td><td>173.00 (n/a)</td><td>130.70 (n/a)</td><td>31.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+3.95%)</td><td>0.20 (-5.12%)</td><td>0.21 (-2.76%)</td><td>0.15 (-13.58%)</td><td>0.04 <b>(+21.38%)</b></td><td>224.70 (+15.71%)</td><td>174.14 (+7.02%)</td><td>157.90 (+2.80%)</td><td>127.30 (-3.78%)</td><td>39.39 <b>(+33.66%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.20 (n/a)</td><td>162.72 (n/a)</td><td>153.60 (n/a)</td><td>132.30 (n/a)</td><td>29.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.33 (+12.55%)</td><td>0.22 (-6.07%)</td><td>0.22 (-7.76%)</td><td>0.14 <b>(-28.31%)</b></td><td>0.07 <b>(+82.77%)</b></td><td>286.60 <b>(+39.46%)</b></td><td>197.66 (+12.79%)</td><td>185.60 (+8.41%)</td><td>123.30 (-11.17%)</td><td>61.18 <b>(+122.83%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>205.50 (n/a)</td><td>175.24 (n/a)</td><td>171.20 (n/a)</td><td>138.80 (n/a)</td><td>27.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (-0.23%)</td><td>0.18 (-5.24%)</td><td>0.19 (+5.56%)</td><td>0.14 <b>(-21.29%)</b></td><td>0.04 <b>(+101.80%)</b></td><td>241.50 <b>(+27.04%)</b></td><td>188.58 (+8.75%)</td><td>169.80 (-5.30%)</td><td>148.90 (+0.27%)</td><td>41.66 <b>(+163.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>173.40 (n/a)</td><td>179.30 (n/a)</td><td>148.50 (n/a)</td><td>15.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-12.34%)</td><td>0.20 (-4.03%)</td><td>0.22 (+9.18%)</td><td>0.16 (+0.11%)</td><td>0.04 (-11.11%)</td><td>236.40 (-0.13%)</td><td>186.04 (+3.87%)</td><td>163.90 (-8.44%)</td><td>153.60 (+14.03%)</td><td>37.14 (+0.21%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>236.70 (n/a)</td><td>179.10 (n/a)</td><td>179.00 (n/a)</td><td>134.70 (n/a)</td><td>37.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (+12.20%)</td><td>0.21 (+3.42%)</td><td>0.21 (+5.43%)</td><td>0.15 (-11.74%)</td><td>0.05 <b>(+61.39%)</b></td><td>225.50 (+13.32%)</td><td>165.48 (-0.33%)</td><td>155.90 (-5.17%)</td><td>116.00 (-10.84%)</td><td>41.14 <b>(+66.79%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>166.02 (n/a)</td><td>164.40 (n/a)</td><td>130.10 (n/a)</td><td>24.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+8.45%)</td><td>0.21 (+12.83%)</td><td>0.20 (+17.77%)</td><td>0.16 (+6.30%)</td><td>0.04 (+7.25%)</td><td>225.10 (-5.93%)</td><td>181.20 (-11.43%)</td><td>183.00 (-15.08%)</td><td>143.10 (-7.80%)</td><td>33.29 (-8.92%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>239.30 (n/a)</td><td>204.58 (n/a)</td><td>215.50 (n/a)</td><td>155.20 (n/a)</td><td>36.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 <b>(+24.39%)</b></td><td>0.20 (+7.85%)</td><td>0.19 (+1.68%)</td><td>0.13 (-18.63%)</td><td>0.05 <b>(+186.76%)</b></td><td>253.60 <b>(+22.93%)</b></td><td>174.36 (-2.68%)</td><td>172.60 (-1.65%)</td><td>131.20 (-19.66%)</td><td>49.09 <b>(+181.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.30 (n/a)</td><td>179.16 (n/a)</td><td>175.50 (n/a)</td><td>163.30 (n/a)</td><td>17.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (-0.43%)</td><td>0.18 (-0.97%)</td><td>0.17 (-6.43%)</td><td>0.16 (+3.46%)</td><td>0.03 (-4.51%)</td><td>219.70 (-3.34%)</td><td>192.64 (+0.78%)</td><td>204.80 (+6.89%)</td><td>163.00 (+0.43%)</td><td>27.08 (-6.92%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>227.30 (n/a)</td><td>191.14 (n/a)</td><td>191.60 (n/a)</td><td>162.30 (n/a)</td><td>29.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 <b>(+22.61%)</b></td><td>0.19 (+9.79%)</td><td>0.21 <b>(+23.60%)</b></td><td>0.13 (-19.18%)</td><td>0.05 <b>(+228.00%)</b></td><td>258.60 <b>(+23.73%)</b></td><td>182.60 (-3.73%)</td><td>156.80 (-19.05%)</td><td>135.60 (-18.46%)</td><td>52.83 <b>(+234.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>189.68 (n/a)</td><td>193.70 (n/a)</td><td>166.30 (n/a)</td><td>15.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 (+17.06%)</td><td>0.20 (+12.03%)</td><td>0.18 (+5.61%)</td><td>0.17 (+5.01%)</td><td>0.04 <b>(+46.80%)</b></td><td>210.60 (-4.79%)</td><td>177.56 (-9.71%)</td><td>191.60 (-5.29%)</td><td>133.00 (-14.52%)</td><td>30.63 (+19.54%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>221.20 (n/a)</td><td>196.66 (n/a)</td><td>202.30 (n/a)</td><td>155.60 (n/a)</td><td>25.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (+3.43%)</td><td>0.17 (+10.91%)</td><td>0.16 (-5.26%)</td><td>0.14 <b>(+64.25%)</b></td><td>0.02 <b>(-43.26%)</b></td><td>234.50 <b>(-39.12%)</b></td><td>197.54 (-15.60%)</td><td>205.20 (+5.50%)</td><td>166.10 (-3.32%)</td><td>27.09 <b>(-68.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>385.20 (n/a)</td><td>234.06 (n/a)</td><td>194.50 (n/a)</td><td>171.80 (n/a)</td><td>86.62 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (-0.30%)</td><td>0.11 (-7.20%)</td><td>0.11 (-8.65%)</td><td>0.09 (-12.82%)</td><td>0.02 <b>(+42.55%)</b></td><td>230.00 (+14.71%)</td><td>187.88 (+10.09%)</td><td>190.50 (+9.48%)</td><td>138.50 (+0.29%)</td><td>39.22 <b>(+67.82%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>170.66 (n/a)</td><td>174.00 (n/a)</td><td>138.10 (n/a)</td><td>23.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 (+2.63%)</td><td>0.12 (+5.99%)</td><td>0.11 (+7.47%)</td><td>0.09 (+8.99%)</td><td>0.02 (+3.13%)</td><td>217.60 (-8.26%)</td><td>176.70 (-5.79%)</td><td>183.80 (-6.94%)</td><td>136.90 (-2.56%)</td><td>35.23 (-8.23%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>237.20 (n/a)</td><td>187.56 (n/a)</td><td>197.50 (n/a)</td><td>140.50 (n/a)</td><td>38.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-12.26%)</td><td>0.12 (-2.40%)</td><td>0.13 (-1.31%)</td><td>0.11 <b>(+21.56%)</b></td><td>0.01 <b>(-53.64%)</b></td><td>193.10 (-17.76%)</td><td>166.82 (-1.77%)</td><td>162.00 (+1.31%)</td><td>146.60 (+13.91%)</td><td>20.10 <b>(-55.43%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>234.80 (n/a)</td><td>169.82 (n/a)</td><td>159.90 (n/a)</td><td>128.70 (n/a)</td><td>45.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (+4.27%)</td><td>0.14 (+3.64%)</td><td>0.13 (+8.30%)</td><td>0.10 (-16.77%)</td><td>0.03 <b>(+26.74%)</b></td><td>213.00 <b>(+20.14%)</b></td><td>157.52 (-1.75%)</td><td>152.30 (-7.70%)</td><td>113.90 (-4.12%)</td><td>36.03 <b>(+49.60%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.30 (n/a)</td><td>160.32 (n/a)</td><td>165.00 (n/a)</td><td>118.80 (n/a)</td><td>24.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 <b>(-21.28%)</b></td><td>0.12 (-9.12%)</td><td>0.12 (+13.81%)</td><td>0.09 (-8.29%)</td><td>0.02 <b>(-51.08%)</b></td><td>219.60 (+9.04%)</td><td>180.04 (+6.52%)</td><td>168.80 (-12.13%)</td><td>157.00 <b>(+27.02%)</b></td><td>26.56 <b>(-32.71%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>169.02 (n/a)</td><td>192.10 (n/a)</td><td>123.60 (n/a)</td><td>39.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.18 (+7.16%)</td><td>0.13 (+6.94%)</td><td>0.12 (+3.07%)</td><td>0.10 <b>(+73.82%)</b></td><td>0.03 <b>(-32.74%)</b></td><td>204.20 <b>(-42.48%)</b></td><td>165.92 (-15.94%)</td><td>173.40 (-2.97%)</td><td>115.20 (-6.65%)</td><td>33.04 <b>(-64.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>355.00 (n/a)</td><td>197.38 (n/a)</td><td>178.70 (n/a)</td><td>123.40 (n/a)</td><td>94.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 <b>(-34.52%)</b></td><td>0.10 (-8.62%)</td><td>0.10 (-15.47%)</td><td>0.09 <b>(+42.72%)</b></td><td>0.01 <b>(-80.87%)</b></td><td>222.00 <b>(-29.95%)</b></td><td>201.30 (-1.91%)</td><td>206.10 (+18.31%)</td><td>183.30 <b>(+52.75%)</b></td><td>15.55 <b>(-80.13%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>316.90 (n/a)</td><td>205.22 (n/a)</td><td>174.20 (n/a)</td><td>120.00 (n/a)</td><td>78.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (-19.76%)</td><td>0.11 (-1.05%)</td><td>0.11 (+14.84%)</td><td>0.08 (-8.50%)</td><td>0.02 <b>(-33.04%)</b></td><td>248.90 (+9.26%)</td><td>187.06 (-1.09%)</td><td>178.60 (-12.92%)</td><td>148.60 <b>(+24.66%)</b></td><td>40.74 (-8.69%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>227.80 (n/a)</td><td>189.12 (n/a)</td><td>205.10 (n/a)</td><td>119.20 (n/a)</td><td>44.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (-3.24%)</td><td>0.14 (-12.97%)</td><td>0.14 (-13.32%)</td><td>0.07 <b>(-39.54%)</b></td><td>0.04 <b>(+29.75%)</b></td><td>332.50 <b>(+65.42%)</b></td><td>200.70 <b>(+22.36%)</b></td><td>179.40 (+15.37%)</td><td>125.20 (+3.39%)</td><td>77.95 <b>(+126.34%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.00 (n/a)</td><td>164.02 (n/a)</td><td>155.50 (n/a)</td><td>121.10 (n/a)</td><td>34.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (-6.29%)</td><td>0.15 (-0.95%)</td><td>0.15 (-8.78%)</td><td>0.11 (+6.94%)</td><td>0.02 <b>(-32.65%)</b></td><td>216.50 (-6.52%)</td><td>169.92 (-1.39%)</td><td>161.30 (+9.65%)</td><td>146.50 (+6.70%)</td><td>28.55 <b>(-32.15%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.60 (n/a)</td><td>172.32 (n/a)</td><td>147.10 (n/a)</td><td>137.30 (n/a)</td><td>42.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 (+6.59%)</td><td>0.15 (+0.38%)</td><td>0.15 (+7.09%)</td><td>0.07 <b>(-31.92%)</b></td><td>0.05 <b>(+55.25%)</b></td><td>362.80 <b>(+46.88%)</b></td><td>193.74 (+10.57%)</td><td>162.80 (-6.65%)</td><td>119.10 (-6.22%)</td><td>98.63 <b>(+118.37%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>247.00 (n/a)</td><td>175.22 (n/a)</td><td>174.40 (n/a)</td><td>127.00 (n/a)</td><td>45.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.21 <b>(+21.36%)</b></td><td>0.14 (-3.94%)</td><td>0.13 (-15.75%)</td><td>0.10 (-7.59%)</td><td>0.04 <b>(+63.13%)</b></td><td>246.00 (+8.23%)</td><td>184.42 (+7.99%)</td><td>185.80 (+18.72%)</td><td>119.30 (-17.61%)</td><td>50.12 <b>(+45.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>227.30 (n/a)</td><td>170.78 (n/a)</td><td>156.50 (n/a)</td><td>144.80 (n/a)</td><td>34.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (+3.89%)</td><td>0.15 (-2.39%)</td><td>0.15 (+6.62%)</td><td>0.12 (-6.12%)</td><td>0.03 (-8.31%)</td><td>211.50 (+6.55%)</td><td>168.10 (+1.97%)</td><td>168.60 (-6.23%)</td><td>123.40 (-3.74%)</td><td>32.38 (-4.32%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.50 (n/a)</td><td>164.86 (n/a)</td><td>179.80 (n/a)</td><td>128.20 (n/a)</td><td>33.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (-7.99%)</td><td>0.16 (-1.25%)</td><td>0.17 <b>(+21.06%)</b></td><td>0.10 <b>(-20.23%)</b></td><td>0.04 (-10.56%)</td><td>244.20 <b>(+25.36%)</b></td><td>160.68 (+2.01%)</td><td>142.60 (-17.43%)</td><td>128.50 (+8.71%)</td><td>47.85 <b>(+30.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>194.80 (n/a)</td><td>157.52 (n/a)</td><td>172.70 (n/a)</td><td>118.20 (n/a)</td><td>36.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.17 (-16.42%)</td><td>0.13 (-9.39%)</td><td>0.12 (-14.04%)</td><td>0.10 (-15.32%)</td><td>0.03 (-17.41%)</td><td>250.40 (+18.06%)</td><td>195.96 (+10.29%)</td><td>206.50 (+16.34%)</td><td>148.60 (+19.65%)</td><td>39.66 (+19.02%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.10 (n/a)</td><td>177.68 (n/a)</td><td>177.50 (n/a)</td><td>124.20 (n/a)</td><td>33.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.16 (+1.10%)</td><td>0.13 (+6.54%)</td><td>0.15 <b>(+32.91%)</b></td><td>0.10 (-1.18%)</td><td>0.03 (+5.55%)</td><td>248.60 (+1.18%)</td><td>190.98 (-5.73%)</td><td>165.50 <b>(-24.77%)</b></td><td>157.50 (-1.07%)</td><td>42.84 (+7.47%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>202.58 (n/a)</td><td>220.00 (n/a)</td><td>159.20 (n/a)</td><td>39.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (+4.09%)</td><td>0.10 (-5.30%)</td><td>0.10 (-8.19%)</td><td>0.07 <b>(-22.71%)</b></td><td>0.02 <b>(+90.60%)</b></td><td>277.80 <b>(+29.39%)</b></td><td>197.54 (+9.33%)</td><td>188.70 (+8.95%)</td><td>151.70 (-3.93%)</td><td>49.89 <b>(+134.91%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>180.68 (n/a)</td><td>173.20 (n/a)</td><td>157.90 (n/a)</td><td>21.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.13 (-4.98%)</td><td>0.11 (+10.79%)</td><td>0.12 <b>(+25.81%)</b></td><td>0.08 (+5.85%)</td><td>0.02 (-5.87%)</td><td>227.90 (-5.51%)</td><td>174.24 (-10.00%)</td><td>151.80 <b>(-20.52%)</b></td><td>143.40 (+5.29%)</td><td>36.79 (-3.98%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.20 (n/a)</td><td>193.60 (n/a)</td><td>191.00 (n/a)</td><td>136.20 (n/a)</td><td>38.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (+12.59%)</td><td>0.12 (+6.79%)</td><td>0.13 (+15.69%)</td><td>0.09 (-4.80%)</td><td>0.02 <b>(+53.80%)</b></td><td>196.50 (+5.02%)</td><td>158.24 (-4.92%)</td><td>145.90 (-13.57%)</td><td>128.30 (-11.15%)</td><td>30.16 <b>(+45.51%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>166.42 (n/a)</td><td>168.80 (n/a)</td><td>144.40 (n/a)</td><td>20.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (+6.67%)</td><td>0.13 (+17.31%)</td><td>0.13 <b>(+30.27%)</b></td><td>0.11 (+18.34%)</td><td>0.01 <b>(-29.91%)</b></td><td>173.80 (-15.51%)</td><td>147.74 (-16.02%)</td><td>144.60 <b>(-23.25%)</b></td><td>127.90 (-6.23%)</td><td>16.63 <b>(-43.79%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>175.92 (n/a)</td><td>188.40 (n/a)</td><td>136.40 (n/a)</td><td>29.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (+5.89%)</td><td>0.10 (+1.55%)</td><td>0.10 (-1.61%)</td><td>0.08 (+19.22%)</td><td>0.01 (-13.36%)</td><td>217.10 (-16.11%)</td><td>189.08 (-2.57%)</td><td>188.00 (+1.62%)</td><td>155.60 (-5.58%)</td><td>25.40 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>258.80 (n/a)</td><td>194.06 (n/a)</td><td>185.00 (n/a)</td><td>164.80 (n/a)</td><td>37.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.14 (+5.42%)</td><td>0.11 (-0.80%)</td><td>0.11 (-3.01%)</td><td>0.08 (-13.71%)</td><td>0.02 <b>(+64.73%)</b></td><td>235.90 (+15.86%)</td><td>173.74 (+3.63%)</td><td>170.50 (+3.08%)</td><td>135.20 (-5.12%)</td><td>41.42 <b>(+75.40%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>167.66 (n/a)</td><td>165.40 (n/a)</td><td>142.50 (n/a)</td><td>23.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.15 <b>(+39.05%)</b></td><td>0.11 (+17.85%)</td><td>0.10 (+14.20%)</td><td>0.09 (+2.18%)</td><td>0.03 <b>(+154.22%)</b></td><td>216.40 (-2.17%)</td><td>173.42 (-12.34%)</td><td>181.30 (-12.42%)</td><td>121.50 <b>(-28.06%)</b></td><td>37.67 <b>(+78.17%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>197.84 (n/a)</td><td>207.00 (n/a)</td><td>168.90 (n/a)</td><td>21.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.12 (-15.76%)</td><td>0.10 (-7.27%)</td><td>0.09 (-13.16%)</td><td>0.08 (+5.34%)</td><td>0.02 <b>(-38.41%)</b></td><td>225.80 (-5.09%)</td><td>195.52 (+4.87%)</td><td>209.20 (+15.13%)</td><td>151.20 (+18.77%)</td><td>30.31 <b>(-31.60%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>237.90 (n/a)</td><td>186.44 (n/a)</td><td>181.70 (n/a)</td><td>127.30 (n/a)</td><td>44.31 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.78 (+16.83%)</td><td>0.59 (+12.64%)</td><td>0.53 (+6.97%)</td><td>0.45 (+0.01%)</td><td>0.13 <b>(+48.02%)</b></td><td>219.70 (+0.00%)</td><td>173.84 (-9.70%)</td><td>185.30 (-6.51%)</td><td>126.20 (-14.44%)</td><td>36.20 <b>(+26.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.67 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.09 (n/a)</td><td>219.70 (n/a)</td><td>192.52 (n/a)</td><td>198.20 (n/a)</td><td>147.50 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.77 (+16.66%)</td><td>0.52 (-3.98%)</td><td>0.50 (-6.91%)</td><td>0.39 (-10.53%)</td><td>0.15 <b>(+47.69%)</b></td><td>254.20 (+11.79%)</td><td>200.20 (+7.01%)</td><td>197.90 (+7.44%)</td><td>127.80 (-14.23%)</td><td>47.73 <b>(+36.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.66 (n/a)</td><td>0.54 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.10 (n/a)</td><td>227.40 (n/a)</td><td>187.08 (n/a)</td><td>184.20 (n/a)</td><td>149.00 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.73 (-6.93%)</td><td>0.61 (-5.66%)</td><td>0.58 (-4.80%)</td><td>0.44 (-14.47%)</td><td>0.12 (-5.12%)</td><td>224.70 (+16.91%)</td><td>167.32 (+6.41%)</td><td>168.80 (+5.04%)</td><td>134.50 (+7.43%)</td><td>36.60 (+19.63%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.79 (n/a)</td><td>0.65 (n/a)</td><td>0.61 (n/a)</td><td>0.51 (n/a)</td><td>0.13 (n/a)</td><td>192.20 (n/a)</td><td>157.24 (n/a)</td><td>160.70 (n/a)</td><td>125.20 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.62 (+0.20%)</td><td>0.52 (-4.55%)</td><td>0.52 (-5.70%)</td><td>0.42 (-2.02%)</td><td>0.08 (-0.72%)</td><td>233.10 (+2.06%)</td><td>194.12 (+4.78%)</td><td>188.30 (+6.02%)</td><td>159.60 (-0.19%)</td><td>28.68 (+2.07%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>228.40 (n/a)</td><td>185.26 (n/a)</td><td>177.60 (n/a)</td><td>159.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.56 <b>(+32.45%)</b></td><td>0.46 (+11.66%)</td><td>0.42 (+1.48%)</td><td>0.41 (+3.36%)</td><td>0.06 <b>(+437.98%)</b></td><td>181.10 (-3.26%)</td><td>162.54 (-9.21%)</td><td>174.50 (-1.41%)</td><td>131.60 <b>(-24.54%)</b></td><td>20.86 <b>(+293.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>179.02 (n/a)</td><td>177.00 (n/a)</td><td>174.40 (n/a)</td><td>5.29 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.52 (-7.68%)</td><td>0.43 (-7.34%)</td><td>0.44 (-7.75%)</td><td>0.35 (-2.57%)</td><td>0.06 <b>(-20.75%)</b></td><td>210.30 (+2.64%)</td><td>172.32 (+7.18%)</td><td>167.80 (+8.40%)</td><td>141.70 (+8.33%)</td><td>24.62 (-12.41%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.56 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>204.90 (n/a)</td><td>160.78 (n/a)</td><td>154.80 (n/a)</td><td>130.80 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.47 <b>(-29.81%)</b></td><td>0.39 (-19.22%)</td><td>0.40 (-7.61%)</td><td>0.30 (-18.79%)</td><td>0.08 <b>(-42.69%)</b></td><td>249.30 <b>(+23.11%)</b></td><td>195.26 <b>(+20.86%)</b></td><td>183.60 (+8.25%)</td><td>157.90 <b>(+42.51%)</b></td><td>39.82 (-1.94%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.67 (n/a)</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.36 (n/a)</td><td>0.13 (n/a)</td><td>202.50 (n/a)</td><td>161.56 (n/a)</td><td>169.60 (n/a)</td><td>110.80 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.41 <b>(-23.58%)</b></td><td>0.38 (-12.31%)</td><td>0.39 (-11.87%)</td><td>0.33 (+2.80%)</td><td>0.03 <b>(-56.69%)</b></td><td>221.40 (-2.72%)</td><td>193.74 (+11.64%)</td><td>188.70 (+13.47%)</td><td>178.40 <b>(+30.89%)</b></td><td>18.05 <b>(-46.45%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>227.60 (n/a)</td><td>173.54 (n/a)</td><td>166.30 (n/a)</td><td>136.30 (n/a)</td><td>33.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (+5.02%)</td><td>0.20 (+2.40%)</td><td>0.22 (+15.78%)</td><td>0.11 <b>(-35.92%)</b></td><td>0.05 <b>(+146.85%)</b></td><td>342.10 <b>(+56.07%)</b></td><td>200.92 (+5.61%)</td><td>164.00 (-13.64%)</td><td>153.60 (-4.77%)</td><td>79.70 <b>(+283.86%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>219.20 (n/a)</td><td>190.24 (n/a)</td><td>189.90 (n/a)</td><td>161.30 (n/a)</td><td>20.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (-4.17%)</td><td>0.22 (+0.70%)</td><td>0.23 (+12.93%)</td><td>0.10 <b>(-41.11%)</b></td><td>0.07 <b>(+49.46%)</b></td><td>369.40 <b>(+69.84%)</b></td><td>193.02 (+10.55%)</td><td>157.70 (-11.45%)</td><td>129.00 (+4.37%)</td><td>99.62 <b>(+196.73%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>217.50 (n/a)</td><td>174.60 (n/a)</td><td>178.10 (n/a)</td><td>123.60 (n/a)</td><td>33.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 <b>(-21.77%)</b></td><td>0.20 (-13.08%)</td><td>0.20 (-8.20%)</td><td>0.17 (+9.17%)</td><td>0.02 <b>(-57.50%)</b></td><td>215.90 (-8.40%)</td><td>187.58 (+10.51%)</td><td>185.40 (+8.93%)</td><td>164.20 <b>(+27.88%)</b></td><td>22.88 <b>(-48.54%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>235.70 (n/a)</td><td>169.74 (n/a)</td><td>170.20 (n/a)</td><td>128.40 (n/a)</td><td>44.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (+18.26%)</td><td>0.22 <b>(+36.26%)</b></td><td>0.21 <b>(+47.37%)</b></td><td>0.18 <b>(+92.59%)</b></td><td>0.04 <b>(-42.64%)</b></td><td>203.70 <b>(-48.09%)</b></td><td>173.16 <b>(-35.51%)</b></td><td>173.00 <b>(-32.13%)</b></td><td>130.50 (-15.48%)</td><td>27.89 <b>(-75.31%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>392.40 (n/a)</td><td>268.52 (n/a)</td><td>254.90 (n/a)</td><td>154.40 (n/a)</td><td>112.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (-19.67%)</td><td>0.21 (-3.36%)</td><td>0.22 (+4.18%)</td><td>0.19 <b>(+20.10%)</b></td><td>0.02 <b>(-65.36%)</b></td><td>198.40 (-16.74%)</td><td>175.94 (-0.44%)</td><td>170.10 (-4.01%)</td><td>162.30 <b>(+24.46%)</b></td><td>15.19 <b>(-63.93%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>238.30 (n/a)</td><td>176.72 (n/a)</td><td>177.20 (n/a)</td><td>130.40 (n/a)</td><td>42.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (-5.36%)</td><td>0.22 (+1.95%)</td><td>0.22 (+5.19%)</td><td>0.18 <b>(+20.44%)</b></td><td>0.05 (-16.55%)</td><td>205.30 (-16.95%)</td><td>169.92 (-3.76%)</td><td>168.40 (-4.91%)</td><td>128.60 (+5.67%)</td><td>35.24 <b>(-24.60%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>247.20 (n/a)</td><td>176.56 (n/a)</td><td>177.10 (n/a)</td><td>121.70 (n/a)</td><td>46.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.19 (-9.90%)</td><td>0.19 (+5.23%)</td><td>0.19 (+7.75%)</td><td>0.18 <b>(+20.43%)</b></td><td>0.01 <b>(-75.85%)</b></td><td>207.00 (-16.97%)</td><td>198.42 (-6.41%)</td><td>198.30 (-7.16%)</td><td>190.10 (+11.04%)</td><td>6.63 <b>(-77.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>249.30 (n/a)</td><td>212.00 (n/a)</td><td>213.60 (n/a)</td><td>171.20 (n/a)</td><td>29.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (+8.47%)</td><td>0.19 (+9.27%)</td><td>0.18 (+2.40%)</td><td>0.17 (+12.11%)</td><td>0.02 (-1.00%)</td><td>220.00 (-10.82%)</td><td>198.88 (-8.70%)</td><td>207.50 (-2.35%)</td><td>170.30 (-7.85%)</td><td>19.48 (-19.50%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>246.70 (n/a)</td><td>217.82 (n/a)</td><td>212.50 (n/a)</td><td>184.80 (n/a)</td><td>24.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 <b>(-21.46%)</b></td><td>0.23 (-8.13%)</td><td>0.23 (-0.12%)</td><td>0.19 (+1.48%)</td><td>0.03 <b>(-57.19%)</b></td><td>216.00 (-1.46%)</td><td>177.00 (+4.02%)</td><td>174.90 (+0.11%)</td><td>153.10 <b>(+27.37%)</b></td><td>24.50 <b>(-45.56%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>219.20 (n/a)</td><td>170.16 (n/a)</td><td>174.70 (n/a)</td><td>120.20 (n/a)</td><td>45.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.31 (+0.41%)</td><td>0.26 (-0.65%)</td><td>0.25 (-8.69%)</td><td>0.23 (+19.16%)</td><td>0.03 <b>(-41.09%)</b></td><td>179.20 (-16.10%)</td><td>161.36 (-2.00%)</td><td>161.10 (+9.52%)</td><td>132.70 (-0.38%)</td><td>18.16 <b>(-50.77%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>213.60 (n/a)</td><td>164.66 (n/a)</td><td>147.10 (n/a)</td><td>133.20 (n/a)</td><td>36.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (-13.52%)</td><td>0.24 (-8.99%)</td><td>0.25 (+7.56%)</td><td>0.19 (-11.06%)</td><td>0.04 <b>(-36.44%)</b></td><td>215.10 (+12.44%)</td><td>175.26 (+7.99%)</td><td>166.30 (-7.04%)</td><td>142.30 (+15.60%)</td><td>27.72 (-16.78%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>191.30 (n/a)</td><td>162.30 (n/a)</td><td>178.90 (n/a)</td><td>123.10 (n/a)</td><td>33.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.30 (-5.75%)</td><td>0.24 (-0.29%)</td><td>0.21 (-4.42%)</td><td>0.19 (+10.64%)</td><td>0.05 (-13.85%)</td><td>212.80 (-9.64%)</td><td>177.20 (-0.84%)</td><td>193.60 (+4.59%)</td><td>134.40 (+6.16%)</td><td>33.29 (-17.21%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>235.50 (n/a)</td><td>178.70 (n/a)</td><td>185.10 (n/a)</td><td>126.60 (n/a)</td><td>40.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.28 (+5.60%)</td><td>0.23 (-1.04%)</td><td>0.22 (-10.73%)</td><td>0.20 (+1.18%)</td><td>0.03 (+10.80%)</td><td>200.50 (-1.18%)</td><td>179.46 (+1.20%)</td><td>186.10 (+12.04%)</td><td>147.30 (-5.33%)</td><td>21.99 (+2.32%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>202.90 (n/a)</td><td>177.34 (n/a)</td><td>166.10 (n/a)</td><td>155.60 (n/a)</td><td>21.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-6.00%)</td><td>0.22 (-6.58%)</td><td>0.22 (-13.09%)</td><td>0.18 (+0.33%)</td><td>0.02 <b>(-33.53%)</b></td><td>224.00 (-0.36%)</td><td>191.54 (+5.93%)</td><td>188.80 (+15.05%)</td><td>168.60 (+6.37%)</td><td>21.36 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>224.80 (n/a)</td><td>180.82 (n/a)</td><td>164.10 (n/a)</td><td>158.50 (n/a)</td><td>29.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (-11.15%)</td><td>0.19 (-11.92%)</td><td>0.21 (-1.74%)</td><td>0.12 <b>(-35.02%)</b></td><td>0.04 <b>(+56.42%)</b></td><td>330.80 <b>(+53.93%)</b></td><td>225.88 (+18.00%)</td><td>197.10 (+1.81%)</td><td>176.40 (+12.57%)</td><td>62.41 <b>(+182.23%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>214.90 (n/a)</td><td>191.42 (n/a)</td><td>193.60 (n/a)</td><td>156.70 (n/a)</td><td>22.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-14.80%)</td><td>0.20 (-2.60%)</td><td>0.19 (-9.21%)</td><td>0.17 <b>(+33.98%)</b></td><td>0.02 <b>(-54.50%)</b></td><td>234.30 <b>(-25.36%)</b></td><td>211.02 (-2.32%)</td><td>219.40 (+10.14%)</td><td>172.70 (+17.40%)</td><td>23.82 <b>(-61.58%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>313.90 (n/a)</td><td>216.04 (n/a)</td><td>199.20 (n/a)</td><td>147.10 (n/a)</td><td>62.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.26 <b>(+25.20%)</b></td><td>0.20 (+12.35%)</td><td>0.19 (+9.99%)</td><td>0.12 (-0.81%)</td><td>0.06 <b>(+46.05%)</b></td><td>299.80 (+0.84%)</td><td>190.92 (-8.08%)</td><td>183.50 (-9.07%)</td><td>132.90 <b>(-20.13%)</b></td><td>65.09 <b>(+21.70%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>297.30 (n/a)</td><td>207.70 (n/a)</td><td>201.80 (n/a)</td><td>166.40 (n/a)</td><td>53.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (-3.41%)</td><td>0.19 (-7.35%)</td><td>0.20 (-2.46%)</td><td>0.16 (-11.40%)</td><td>0.03 <b>(+37.36%)</b></td><td>218.20 (+12.88%)</td><td>188.42 (+8.91%)</td><td>176.70 (+2.55%)</td><td>158.20 (+3.53%)</td><td>26.86 <b>(+65.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>193.30 (n/a)</td><td>173.00 (n/a)</td><td>172.30 (n/a)</td><td>152.80 (n/a)</td><td>16.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.24 (-17.41%)</td><td>0.19 <b>(-20.60%)</b></td><td>0.19 <b>(-29.05%)</b></td><td>0.16 (-11.28%)</td><td>0.03 <b>(-41.45%)</b></td><td>217.00 (+12.73%)</td><td>182.10 <b>(+23.42%)</b></td><td>183.50 <b>(+40.94%)</b></td><td>145.00 <b>(+21.14%)</b></td><td>26.81 (-19.85%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>192.50 (n/a)</td><td>147.54 (n/a)</td><td>130.20 (n/a)</td><td>119.70 (n/a)</td><td>33.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 (+0.81%)</td><td>0.22 (+2.71%)</td><td>0.21 (+4.48%)</td><td>0.18 (+0.35%)</td><td>0.04 (+8.84%)</td><td>197.10 (-0.35%)</td><td>165.56 (-2.14%)</td><td>164.30 (-4.25%)</td><td>126.70 (-0.86%)</td><td>31.23 (+10.65%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>197.80 (n/a)</td><td>169.18 (n/a)</td><td>171.60 (n/a)</td><td>127.80 (n/a)</td><td>28.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.29 (+12.06%)</td><td>0.20 (-5.14%)</td><td>0.19 (-1.19%)</td><td>0.09 <b>(-48.42%)</b></td><td>0.08 <b>(+105.40%)</b></td><td>389.80 <b>(+93.83%)</b></td><td>204.48 <b>(+21.60%)</b></td><td>182.20 (+1.22%)</td><td>120.00 (-10.78%)</td><td>108.31 <b>(+275.04%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.10 (n/a)</td><td>168.16 (n/a)</td><td>180.00 (n/a)</td><td>134.50 (n/a)</td><td>28.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.25 (+6.51%)</td><td>0.21 (+12.07%)</td><td>0.20 (-4.71%)</td><td>0.17 <b>(+72.69%)</b></td><td>0.04 <b>(-28.96%)</b></td><td>209.60 <b>(-42.10%)</b></td><td>172.68 (-17.76%)</td><td>170.40 (+4.93%)</td><td>137.40 (-6.08%)</td><td>35.14 <b>(-61.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>362.00 (n/a)</td><td>209.96 (n/a)</td><td>162.40 (n/a)</td><td>146.30 (n/a)</td><td>90.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.22 (-18.75%)</td><td>0.18 (-7.66%)</td><td>0.17 (-12.59%)</td><td>0.14 (+1.87%)</td><td>0.03 <b>(-38.10%)</b></td><td>245.90 (-1.84%)</td><td>197.36 (+4.81%)</td><td>201.60 (+14.42%)</td><td>155.60 <b>(+23.00%)</b></td><td>36.65 <b>(-27.68%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>250.50 (n/a)</td><td>188.30 (n/a)</td><td>176.20 (n/a)</td><td>126.50 (n/a)</td><td>50.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (+10.05%)</td><td>0.18 (+6.00%)</td><td>0.19 (+14.24%)</td><td>0.15 (-4.35%)</td><td>0.02 <b>(+171.54%)</b></td><td>225.90 (+4.53%)</td><td>199.18 (-4.72%)</td><td>187.50 (-12.46%)</td><td>176.90 (-9.10%)</td><td>24.37 <b>(+160.10%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>209.04 (n/a)</td><td>214.20 (n/a)</td><td>194.60 (n/a)</td><td>9.37 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.01 <b>(+25.32%)</b></td><td>0.76 (+9.81%)</td><td>0.69 (+5.08%)</td><td>0.59 (-4.77%)</td><td>0.17 <b>(+110.77%)</b></td><td>221.10 (+4.99%)</td><td>177.88 (-6.51%)</td><td>190.70 (-4.84%)</td><td>129.50 <b>(-20.21%)</b></td><td>36.33 <b>(+74.22%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.81 (n/a)</td><td>0.70 (n/a)</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>210.60 (n/a)</td><td>190.26 (n/a)</td><td>200.40 (n/a)</td><td>162.30 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.89 (-3.38%)</td><td>0.83 (+8.61%)</td><td>0.86 (+18.72%)</td><td>0.70 (+17.60%)</td><td>0.08 <b>(-42.56%)</b></td><td>187.90 (-14.98%)</td><td>158.30 (-9.59%)</td><td>152.90 (-15.76%)</td><td>147.60 (+3.51%)</td><td>16.84 <b>(-47.53%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.92 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.14 (n/a)</td><td>221.00 (n/a)</td><td>175.10 (n/a)</td><td>181.50 (n/a)</td><td>142.60 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.04 (+10.35%)</td><td>0.78 (+3.24%)</td><td>0.66 (-6.64%)</td><td>0.63 (-1.22%)</td><td>0.19 <b>(+60.51%)</b></td><td>209.20 (+1.26%)</td><td>176.48 (-0.55%)</td><td>197.80 (+7.09%)</td><td>126.40 (-9.39%)</td><td>39.51 <b>(+52.38%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.94 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>206.60 (n/a)</td><td>177.46 (n/a)</td><td>184.70 (n/a)</td><td>139.50 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.00 (+0.00%)</td><td>0.00 (-1.40%)</td><td>0.00 (-2.27%)</td><td>0.00 (-2.50%)</td><td>0.00 (+19.72%)</td><td>1055.53 (+3.73%)</td><td>969.43 (+1.40%)</td><td>948.29 (+1.11%)</td><td>936.36 (+0.05%)</td><td>49.83 <b>(+42.52%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1017.55 (n/a)</td><td>956.02 (n/a)</td><td>937.90 (n/a)</td><td>935.89 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.01 (+1.20%)</td><td>0.01 (+0.98%)</td><td>0.01 (+1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>1009.78 (-0.33%)</td><td>990.69 (-0.87%)</td><td>994.41 (-1.12%)</td><td>975.27 (-1.00%)</td><td>13.99 (+10.95%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1013.16 (n/a)</td><td>999.40 (n/a)</td><td>1005.68 (n/a)</td><td>985.16 (n/a)</td><td>12.61 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>1.00 (+3.18%)</td><td>0.97 (+0.92%)</td><td>0.96 (+0.25%)</td><td>0.95 (+0.29%)</td><td>0.02 <b>(+104.80%)</b></td><td>2208.09 (-0.28%)</td><td>2170.08 (-0.89%)</td><td>2184.93 (-0.25%)</td><td>2092.51 (-3.08%)</td><td>44.84 <b>(+96.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2214.31 (n/a)</td><td>2189.61 (n/a)</td><td>2190.41 (n/a)</td><td>2159.10 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.40 (-8.36%)</td><td>0.40 (-7.94%)</td><td>0.40 (-8.65%)</td><td>0.40 (-6.17%)</td><td>0.00 <b>(-73.81%)</b></td><td>1315.19 (+6.56%)</td><td>1310.68 (+8.61%)</td><td>1312.97 (+9.47%)</td><td>1303.62 (+9.12%)</td><td>4.82 <b>(-70.08%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.01 (n/a)</td><td>1234.28 (n/a)</td><td>1206.77 (n/a)</td><td>1199.35 (n/a)</td><td>1194.63 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.27 <b>(-28.81%)</b></td><td>0.26 <b>(-29.56%)</b></td><td>0.26 <b>(-30.72%)</b></td><td>0.25 <b>(-29.56%)</b></td><td>0.01 (+11.02%)</td><td>2058.68 <b>(+42.00%)</b></td><td>2018.00 <b>(+42.03%)</b></td><td>2042.70 <b>(+44.36%)</b></td><td>1963.09 <b>(+40.48%)</b></td><td>45.95 <b>(+121.87%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1449.74 (n/a)</td><td>1420.83 (n/a)</td><td>1415.03 (n/a)</td><td>1397.40 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.38 (-1.13%)</td><td>0.37 (-1.42%)</td><td>0.37 (-1.05%)</td><td>0.36 (-2.37%)</td><td>0.01 <b>(+22.63%)</b></td><td>1443.73 (+2.42%)</td><td>1415.38 (+1.44%)</td><td>1420.24 (+1.06%)</td><td>1390.38 (+1.14%)</td><td>20.42 <b>(+26.94%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.00 (n/a)</td><td>1409.64 (n/a)</td><td>1395.23 (n/a)</td><td>1405.29 (n/a)</td><td>1374.71 (n/a)</td><td>16.08 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.45 (+13.82%)</td><td>4.77 (+14.43%)</td><td>4.54 (+6.57%)</td><td>4.24 <b>(+51.25%)</b></td><td>0.58 <b>(-28.69%)</b></td><td>247.50 <b>(-33.89%)</b></td><td>222.58 (-14.97%)</td><td>231.20 (-6.13%)</td><td>192.30 (-12.15%)</td><td>26.24 <b>(-59.39%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.79 (n/a)</td><td>4.16 (n/a)</td><td>4.26 (n/a)</td><td>2.80 (n/a)</td><td>0.81 (n/a)</td><td>374.40 (n/a)</td><td>261.78 (n/a)</td><td>246.30 (n/a)</td><td>218.90 (n/a)</td><td>64.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.07 (-3.32%)</td><td>5.04 (-2.53%)</td><td>4.57 (-8.79%)</td><td>4.45 (+13.74%)</td><td>0.75 <b>(-29.32%)</b></td><td>235.70 (-12.09%)</td><td>211.54 (+0.78%)</td><td>229.30 (+9.66%)</td><td>172.70 (+3.41%)</td><td>29.42 <b>(-32.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (n/a)</td><td>5.17 (n/a)</td><td>5.01 (n/a)</td><td>3.91 (n/a)</td><td>1.06 (n/a)</td><td>268.10 (n/a)</td><td>209.90 (n/a)</td><td>209.10 (n/a)</td><td>167.00 (n/a)</td><td>43.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.47 (+16.11%)</td><td>4.72 (+10.96%)</td><td>4.85 (+10.62%)</td><td>4.19 (+14.41%)</td><td>0.53 <b>(+29.65%)</b></td><td>250.50 (-12.60%)</td><td>224.20 (-9.68%)</td><td>216.00 (-9.59%)</td><td>191.60 (-13.85%)</td><td>24.77 (-1.48%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.71 (n/a)</td><td>4.26 (n/a)</td><td>4.39 (n/a)</td><td>3.66 (n/a)</td><td>0.41 (n/a)</td><td>286.60 (n/a)</td><td>248.22 (n/a)</td><td>238.90 (n/a)</td><td>222.40 (n/a)</td><td>25.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.90 (-8.30%)</td><td>5.29 (-9.69%)</td><td>5.33 (-9.44%)</td><td>4.32 (-17.92%)</td><td>0.63 <b>(+48.72%)</b></td><td>242.80 <b>(+21.89%)</b></td><td>200.84 (+11.65%)</td><td>196.70 (+10.44%)</td><td>177.70 (+9.09%)</td><td>25.91 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.44 (n/a)</td><td>5.85 (n/a)</td><td>5.89 (n/a)</td><td>5.26 (n/a)</td><td>0.42 (n/a)</td><td>199.20 (n/a)</td><td>179.88 (n/a)</td><td>178.10 (n/a)</td><td>162.90 (n/a)</td><td>13.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.08 (+6.91%)</td><td>4.70 (+6.66%)</td><td>4.99 (+10.71%)</td><td>4.14 (+3.74%)</td><td>0.46 <b>(+24.37%)</b></td><td>253.40 (-3.61%)</td><td>224.82 (-6.03%)</td><td>210.30 (-9.66%)</td><td>206.20 (-6.49%)</td><td>23.07 (+11.72%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.76 (n/a)</td><td>4.41 (n/a)</td><td>4.50 (n/a)</td><td>3.99 (n/a)</td><td>0.37 (n/a)</td><td>262.90 (n/a)</td><td>239.24 (n/a)</td><td>232.80 (n/a)</td><td>220.50 (n/a)</td><td>20.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.74 (-0.12%)</td><td>4.61 (-7.02%)</td><td>4.54 (-11.57%)</td><td>3.96 (+14.09%)</td><td>0.71 <b>(-20.62%)</b></td><td>264.80 (-12.35%)</td><td>231.30 (+5.98%)</td><td>230.90 (+13.13%)</td><td>182.80 (+0.11%)</td><td>32.62 <b>(-32.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>5.74 (n/a)</td><td>4.96 (n/a)</td><td>5.14 (n/a)</td><td>3.47 (n/a)</td><td>0.89 (n/a)</td><td>302.10 (n/a)</td><td>218.24 (n/a)</td><td>204.10 (n/a)</td><td>182.60 (n/a)</td><td>48.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.04 (-10.89%)</td><td>4.64 (-10.55%)</td><td>4.66 (-14.65%)</td><td>4.29 (-5.66%)</td><td>0.28 <b>(-49.06%)</b></td><td>244.50 (+5.98%)</td><td>226.70 (+11.08%)</td><td>225.10 (+17.18%)</td><td>208.00 (+12.19%)</td><td>13.43 <b>(-39.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>5.66 (n/a)</td><td>5.19 (n/a)</td><td>5.46 (n/a)</td><td>4.55 (n/a)</td><td>0.54 (n/a)</td><td>230.70 (n/a)</td><td>204.08 (n/a)</td><td>192.10 (n/a)</td><td>185.40 (n/a)</td><td>22.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.46 (-11.94%)</td><td>4.86 (-6.49%)</td><td>5.12 (-1.20%)</td><td>3.86 (-5.40%)</td><td>0.62 (-18.01%)</td><td>271.90 (+5.67%)</td><td>219.16 (+6.57%)</td><td>204.90 (+1.24%)</td><td>192.00 (+13.54%)</td><td>31.52 (-1.78%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.20 (n/a)</td><td>5.19 (n/a)</td><td>5.18 (n/a)</td><td>4.08 (n/a)</td><td>0.76 (n/a)</td><td>257.30 (n/a)</td><td>205.64 (n/a)</td><td>202.40 (n/a)</td><td>169.10 (n/a)</td><td>32.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.03 (-6.60%)</td><td>7.55 (-2.70%)</td><td>7.63 (+1.17%)</td><td>7.02 (+0.13%)</td><td>0.37 <b>(-38.80%)</b></td><td>298.80 (-0.13%)</td><td>278.34 (+2.47%)</td><td>274.80 (-1.15%)</td><td>261.00 (+7.05%)</td><td>13.90 <b>(-34.02%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.60 (n/a)</td><td>7.76 (n/a)</td><td>7.54 (n/a)</td><td>7.01 (n/a)</td><td>0.61 (n/a)</td><td>299.20 (n/a)</td><td>271.62 (n/a)</td><td>278.00 (n/a)</td><td>243.80 (n/a)</td><td>21.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.30 (+1.85%)</td><td>7.79 (-9.28%)</td><td>7.97 (-7.36%)</td><td>6.48 <b>(-21.46%)</b></td><td>1.12 <b>(+212.94%)</b></td><td>323.40 <b>(+27.32%)</b></td><td>273.58 (+11.90%)</td><td>263.30 (+7.95%)</td><td>225.40 (-1.83%)</td><td>39.14 <b>(+294.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.14 (n/a)</td><td>8.59 (n/a)</td><td>8.60 (n/a)</td><td>8.26 (n/a)</td><td>0.36 (n/a)</td><td>254.00 (n/a)</td><td>244.48 (n/a)</td><td>243.90 (n/a)</td><td>229.60 (n/a)</td><td>9.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.95 (-5.82%)</td><td>7.52 (+2.19%)</td><td>7.36 (-1.23%)</td><td>7.24 <b>(+26.05%)</b></td><td>0.33 <b>(-67.47%)</b></td><td>289.80 <b>(-20.67%)</b></td><td>279.42 (-3.63%)</td><td>284.80 (+1.24%)</td><td>263.90 (+6.20%)</td><td>11.93 <b>(-73.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.44 (n/a)</td><td>7.36 (n/a)</td><td>7.46 (n/a)</td><td>5.74 (n/a)</td><td>1.00 (n/a)</td><td>365.30 (n/a)</td><td>289.96 (n/a)</td><td>281.30 (n/a)</td><td>248.50 (n/a)</td><td>44.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.96 (-14.23%)</td><td>7.45 (-7.69%)</td><td>7.63 (-3.08%)</td><td>6.68 (-7.17%)</td><td>0.49 <b>(-39.44%)</b></td><td>313.90 (+7.72%)</td><td>282.30 (+7.89%)</td><td>274.80 (+3.15%)</td><td>263.60 (+16.59%)</td><td>19.35 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.28 (n/a)</td><td>8.08 (n/a)</td><td>7.87 (n/a)</td><td>7.20 (n/a)</td><td>0.80 (n/a)</td><td>291.40 (n/a)</td><td>261.66 (n/a)</td><td>266.40 (n/a)</td><td>226.10 (n/a)</td><td>25.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.56 (+3.19%)</td><td>7.35 (-4.53%)</td><td>7.18 (-5.19%)</td><td>5.97 (-12.32%)</td><td>0.98 <b>(+59.08%)</b></td><td>351.20 (+14.06%)</td><td>289.58 (+5.74%)</td><td>292.20 (+5.45%)</td><td>245.10 (-3.08%)</td><td>40.22 <b>(+78.55%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.29 (n/a)</td><td>7.70 (n/a)</td><td>7.57 (n/a)</td><td>6.81 (n/a)</td><td>0.61 (n/a)</td><td>307.90 (n/a)</td><td>273.86 (n/a)</td><td>277.10 (n/a)</td><td>252.90 (n/a)</td><td>22.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.32 (+4.81%)</td><td>7.98 (-5.16%)</td><td>7.86 (-6.29%)</td><td>6.85 (-14.35%)</td><td>0.92 <b>(+134.01%)</b></td><td>306.10 (+16.74%)</td><td>265.38 (+6.35%)</td><td>266.90 (+6.72%)</td><td>225.00 (-4.62%)</td><td>30.03 <b>(+159.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.89 (n/a)</td><td>8.42 (n/a)</td><td>8.39 (n/a)</td><td>8.00 (n/a)</td><td>0.39 (n/a)</td><td>262.20 (n/a)</td><td>249.54 (n/a)</td><td>250.10 (n/a)</td><td>235.90 (n/a)</td><td>11.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>8.69 (-17.32%)</td><td>7.94 (-7.15%)</td><td>7.70 (-9.69%)</td><td>7.52 (+7.12%)</td><td>0.52 <b>(-59.15%)</b></td><td>279.00 (-6.66%)</td><td>264.88 (+6.20%)</td><td>272.40 (+10.73%)</td><td>241.30 <b>(+20.95%)</b></td><td>16.95 <b>(-53.19%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.51 (n/a)</td><td>8.56 (n/a)</td><td>8.53 (n/a)</td><td>7.02 (n/a)</td><td>1.28 (n/a)</td><td>298.90 (n/a)</td><td>249.42 (n/a)</td><td>246.00 (n/a)</td><td>199.50 (n/a)</td><td>36.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.58 (-10.71%)</td><td>7.74 (-6.57%)</td><td>7.96 (-3.41%)</td><td>7.02 (+0.70%)</td><td>0.68 <b>(-29.18%)</b></td><td>298.80 (-0.70%)</td><td>272.60 (+6.53%)</td><td>263.40 (+3.50%)</td><td>244.40 (+11.96%)</td><td>24.05 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.61 (n/a)</td><td>8.28 (n/a)</td><td>8.24 (n/a)</td><td>6.97 (n/a)</td><td>0.96 (n/a)</td><td>300.90 (n/a)</td><td>255.90 (n/a)</td><td>254.50 (n/a)</td><td>218.30 (n/a)</td><td>30.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.09 (+1.32%)</td><td>8.18 (+1.82%)</td><td>8.36 (+8.01%)</td><td>7.19 (-4.43%)</td><td>0.90 <b>(+46.94%)</b></td><td>291.80 (+4.63%)</td><td>258.80 (-1.25%)</td><td>250.70 (-7.42%)</td><td>230.80 (-1.33%)</td><td>29.09 <b>(+52.06%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.97 (n/a)</td><td>8.04 (n/a)</td><td>7.74 (n/a)</td><td>7.52 (n/a)</td><td>0.61 (n/a)</td><td>278.90 (n/a)</td><td>262.08 (n/a)</td><td>270.80 (n/a)</td><td>233.90 (n/a)</td><td>19.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.12 (-7.72%)</td><td>7.78 (-14.12%)</td><td>8.18 (-8.20%)</td><td>5.47 <b>(-36.73%)</b></td><td>1.37 <b>(+184.57%)</b></td><td>383.20 <b>(+58.02%)</b></td><td>278.10 (+19.85%)</td><td>256.50 (+8.96%)</td><td>230.00 (+8.39%)</td><td>60.38 <b>(+413.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.88 (n/a)</td><td>9.06 (n/a)</td><td>8.91 (n/a)</td><td>8.65 (n/a)</td><td>0.48 (n/a)</td><td>242.50 (n/a)</td><td>232.04 (n/a)</td><td>235.40 (n/a)</td><td>212.20 (n/a)</td><td>11.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>9.42 (+0.29%)</td><td>8.65 (+4.29%)</td><td>8.68 (+5.43%)</td><td>8.06 (+8.63%)</td><td>0.52 <b>(-27.57%)</b></td><td>260.20 (-7.93%)</td><td>243.04 (-4.39%)</td><td>241.60 (-5.14%)</td><td>222.70 (-0.31%)</td><td>14.50 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>9.39 (n/a)</td><td>8.30 (n/a)</td><td>8.23 (n/a)</td><td>7.42 (n/a)</td><td>0.72 (n/a)</td><td>282.60 (n/a)</td><td>254.20 (n/a)</td><td>254.70 (n/a)</td><td>223.40 (n/a)</td><td>21.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.39 (-14.41%)</td><td>7.08 <b>(-20.79%)</b></td><td>7.49 (-17.64%)</td><td>5.61 <b>(-31.28%)</b></td><td>1.27 <b>(+93.89%)</b></td><td>373.50 <b>(+45.50%)</b></td><td>304.60 <b>(+29.18%)</b></td><td>280.10 <b>(+21.41%)</b></td><td>250.10 (+16.87%)</td><td>57.28 <b>(+231.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.80 (n/a)</td><td>8.93 (n/a)</td><td>9.09 (n/a)</td><td>8.17 (n/a)</td><td>0.65 (n/a)</td><td>256.70 (n/a)</td><td>235.80 (n/a)</td><td>230.70 (n/a)</td><td>214.00 (n/a)</td><td>17.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>11.43 (-5.44%)</td><td>10.58 (-6.19%)</td><td>10.51 (-6.47%)</td><td>9.66 (-9.12%)</td><td>0.71 <b>(+24.52%)</b></td><td>434.40 (+10.06%)</td><td>397.98 (+6.77%)</td><td>399.10 (+6.91%)</td><td>366.90 (+5.77%)</td><td>27.03 <b>(+44.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.09 (n/a)</td><td>11.28 (n/a)</td><td>11.24 (n/a)</td><td>10.63 (n/a)</td><td>0.57 (n/a)</td><td>394.70 (n/a)</td><td>372.74 (n/a)</td><td>373.30 (n/a)</td><td>346.90 (n/a)</td><td>18.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.79 (+4.79%)</td><td>10.71 (-4.69%)</td><td>10.59 (-5.22%)</td><td>8.04 <b>(-21.86%)</b></td><td>1.77 <b>(+114.98%)</b></td><td>521.90 <b>(+27.98%)</b></td><td>401.16 (+7.05%)</td><td>396.00 (+5.52%)</td><td>328.10 (-4.57%)</td><td>73.89 <b>(+168.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.20 (n/a)</td><td>11.24 (n/a)</td><td>11.18 (n/a)</td><td>10.28 (n/a)</td><td>0.83 (n/a)</td><td>407.80 (n/a)</td><td>374.74 (n/a)</td><td>375.30 (n/a)</td><td>343.80 (n/a)</td><td>27.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.25 (-4.92%)</td><td>11.65 (+1.83%)</td><td>11.87 (+8.40%)</td><td>10.77 (+0.93%)</td><td>0.65 <b>(-30.64%)</b></td><td>389.30 (-0.92%)</td><td>361.12 (-2.04%)</td><td>353.30 (-7.73%)</td><td>342.30 (+5.19%)</td><td>20.73 <b>(-28.28%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.89 (n/a)</td><td>11.44 (n/a)</td><td>10.95 (n/a)</td><td>10.67 (n/a)</td><td>0.94 (n/a)</td><td>392.90 (n/a)</td><td>368.64 (n/a)</td><td>382.90 (n/a)</td><td>325.40 (n/a)</td><td>28.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.22 (-7.10%)</td><td>11.22 (-5.79%)</td><td>11.11 (-10.84%)</td><td>10.08 (-0.84%)</td><td>0.82 <b>(-31.08%)</b></td><td>416.30 (+0.85%)</td><td>375.54 (+5.70%)</td><td>377.40 (+12.15%)</td><td>343.30 (+7.65%)</td><td>28.08 <b>(-25.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.15 (n/a)</td><td>11.91 (n/a)</td><td>12.47 (n/a)</td><td>10.16 (n/a)</td><td>1.20 (n/a)</td><td>412.80 (n/a)</td><td>355.28 (n/a)</td><td>336.50 (n/a)</td><td>318.90 (n/a)</td><td>37.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>11.47 (-2.80%)</td><td>11.01 (-2.07%)</td><td>10.98 (+0.42%)</td><td>10.26 (-5.26%)</td><td>0.48 (-1.27%)</td><td>408.60 (+5.55%)</td><td>381.64 (+2.12%)</td><td>382.00 (-0.42%)</td><td>365.80 (+2.87%)</td><td>17.21 (+7.38%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>11.80 (n/a)</td><td>11.24 (n/a)</td><td>10.93 (n/a)</td><td>10.83 (n/a)</td><td>0.49 (n/a)</td><td>387.10 (n/a)</td><td>373.70 (n/a)</td><td>383.60 (n/a)</td><td>355.60 (n/a)</td><td>16.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.69 (+1.23%)</td><td>10.74 (-9.37%)</td><td>11.05 (-5.08%)</td><td>8.04 <b>(-29.12%)</b></td><td>1.68 <b>(+237.04%)</b></td><td>521.70 <b>(+41.08%)</b></td><td>399.42 (+12.70%)</td><td>379.40 (+5.33%)</td><td>330.50 (-1.23%)</td><td>71.97 <b>(+389.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.54 (n/a)</td><td>11.85 (n/a)</td><td>11.65 (n/a)</td><td>11.34 (n/a)</td><td>0.50 (n/a)</td><td>369.80 (n/a)</td><td>354.42 (n/a)</td><td>360.20 (n/a)</td><td>334.60 (n/a)</td><td>14.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.27 (-0.05%)</td><td>12.85 (-0.85%)</td><td>12.88 (-5.19%)</td><td>11.44 (+4.53%)</td><td>1.19 (-18.92%)</td><td>366.70 (-4.33%)</td><td>328.60 (+0.46%)</td><td>325.60 (+5.47%)</td><td>294.00 (+0.07%)</td><td>30.50 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.27 (n/a)</td><td>12.96 (n/a)</td><td>13.59 (n/a)</td><td>10.94 (n/a)</td><td>1.46 (n/a)</td><td>383.30 (n/a)</td><td>327.08 (n/a)</td><td>308.70 (n/a)</td><td>293.80 (n/a)</td><td>39.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.14 (-1.28%)</td><td>12.97 (-3.81%)</td><td>12.38 (-4.30%)</td><td>12.00 (+1.39%)</td><td>1.32 (-15.31%)</td><td>349.60 (-1.38%)</td><td>325.76 (+3.66%)</td><td>338.70 (+4.50%)</td><td>277.00 (+1.32%)</td><td>30.47 (-14.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>15.34 (n/a)</td><td>13.49 (n/a)</td><td>12.94 (n/a)</td><td>11.83 (n/a)</td><td>1.56 (n/a)</td><td>354.50 (n/a)</td><td>314.26 (n/a)</td><td>324.10 (n/a)</td><td>273.40 (n/a)</td><td>35.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>12.50 (-14.77%)</td><td>11.88 (-10.15%)</td><td>12.12 (-5.97%)</td><td>10.81 (-14.83%)</td><td>0.65 <b>(-21.13%)</b></td><td>387.90 (+17.40%)</td><td>353.88 (+11.26%)</td><td>346.10 (+6.36%)</td><td>335.50 (+17.35%)</td><td>20.48 (+9.85%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.67 (n/a)</td><td>13.23 (n/a)</td><td>12.89 (n/a)</td><td>12.70 (n/a)</td><td>0.83 (n/a)</td><td>330.40 (n/a)</td><td>318.06 (n/a)</td><td>325.40 (n/a)</td><td>285.90 (n/a)</td><td>18.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.09 (-5.90%)</td><td>12.36 (-7.75%)</td><td>12.58 (-6.85%)</td><td>10.90 (-11.37%)</td><td>1.20 (+4.75%)</td><td>384.90 (+12.81%)</td><td>341.76 (+8.56%)</td><td>333.40 (+7.34%)</td><td>297.60 (+6.25%)</td><td>32.68 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.98 (n/a)</td><td>13.40 (n/a)</td><td>13.50 (n/a)</td><td>12.29 (n/a)</td><td>1.14 (n/a)</td><td>341.20 (n/a)</td><td>314.80 (n/a)</td><td>310.60 (n/a)</td><td>280.10 (n/a)</td><td>26.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.57 (+0.89%)</td><td>12.87 (-2.39%)</td><td>13.26 (+0.58%)</td><td>11.33 (-4.96%)</td><td>1.36 <b>(+39.02%)</b></td><td>370.10 (+5.20%)</td><td>328.76 (+2.92%)</td><td>316.30 (-0.60%)</td><td>287.90 (-0.86%)</td><td>35.15 <b>(+46.85%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.44 (n/a)</td><td>13.19 (n/a)</td><td>13.18 (n/a)</td><td>11.92 (n/a)</td><td>0.98 (n/a)</td><td>351.80 (n/a)</td><td>319.44 (n/a)</td><td>318.20 (n/a)</td><td>290.40 (n/a)</td><td>23.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.26 (+5.74%)</td><td>12.48 (-0.64%)</td><td>12.66 (-2.21%)</td><td>9.12 (-14.69%)</td><td>2.19 <b>(+40.34%)</b></td><td>459.80 (+17.24%)</td><td>345.66 (+2.18%)</td><td>331.40 (+2.25%)</td><td>274.90 (-5.44%)</td><td>68.46 <b>(+59.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.43 (n/a)</td><td>12.56 (n/a)</td><td>12.94 (n/a)</td><td>10.69 (n/a)</td><td>1.56 (n/a)</td><td>392.20 (n/a)</td><td>338.28 (n/a)</td><td>324.10 (n/a)</td><td>290.70 (n/a)</td><td>42.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>14.34 (-4.28%)</td><td>13.02 (-1.36%)</td><td>13.12 (+0.09%)</td><td>11.92 (+7.65%)</td><td>0.89 <b>(-48.91%)</b></td><td>351.80 (-7.10%)</td><td>323.28 (+0.30%)</td><td>319.80 (-0.09%)</td><td>292.50 (+4.46%)</td><td>21.90 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.98 (n/a)</td><td>13.20 (n/a)</td><td>13.10 (n/a)</td><td>11.07 (n/a)</td><td>1.75 (n/a)</td><td>378.70 (n/a)</td><td>322.32 (n/a)</td><td>320.10 (n/a)</td><td>280.00 (n/a)</td><td>43.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.75 (+5.58%)</td><td>13.18 (-1.29%)</td><td>13.02 (-2.55%)</td><td>10.68 (-16.09%)</td><td>1.64 <b>(+245.21%)</b></td><td>392.80 (+19.17%)</td><td>322.62 (+2.58%)</td><td>322.20 (+2.61%)</td><td>284.40 (-5.26%)</td><td>43.64 <b>(+287.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.97 (n/a)</td><td>13.35 (n/a)</td><td>13.36 (n/a)</td><td>12.73 (n/a)</td><td>0.48 (n/a)</td><td>329.60 (n/a)</td><td>314.50 (n/a)</td><td>314.00 (n/a)</td><td>300.20 (n/a)</td><td>11.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>13.95 (+2.45%)</td><td>12.48 (+5.07%)</td><td>12.55 (-2.76%)</td><td>10.81 <b>(+24.90%)</b></td><td>1.31 <b>(-35.12%)</b></td><td>388.00 (-19.93%)</td><td>339.24 (-6.57%)</td><td>334.20 (+2.83%)</td><td>300.60 (-2.40%)</td><td>36.30 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.62 (n/a)</td><td>11.87 (n/a)</td><td>12.90 (n/a)</td><td>8.65 (n/a)</td><td>2.02 (n/a)</td><td>484.60 (n/a)</td><td>363.08 (n/a)</td><td>325.00 (n/a)</td><td>308.00 (n/a)</td><td>72.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>17.73 (-7.59%)</td><td>12.82 (-9.96%)</td><td>12.67 (-8.75%)</td><td>9.51 (+2.33%)</td><td>3.37 (-11.44%)</td><td>440.80 (-2.28%)</td><td>345.08 (+10.11%)</td><td>330.90 (+9.57%)</td><td>236.50 (+8.19%)</td><td>86.11 (-4.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>19.19 (n/a)</td><td>14.23 (n/a)</td><td>13.89 (n/a)</td><td>9.30 (n/a)</td><td>3.81 (n/a)</td><td>451.10 (n/a)</td><td>313.40 (n/a)</td><td>302.00 (n/a)</td><td>218.60 (n/a)</td><td>89.93 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>2.71 (-18.72%)</td><td>2.53 (+0.19%)</td><td>2.63 (+10.47%)</td><td>2.21 (+5.56%)</td><td>0.22 <b>(-57.30%)</b></td><td>237.50 (-5.27%)</td><td>208.72 (-2.55%)</td><td>199.60 (-9.48%)</td><td>193.50 <b>(+23.01%)</b></td><td>19.21 <b>(-51.29%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.33 (n/a)</td><td>2.52 (n/a)</td><td>2.38 (n/a)</td><td>2.09 (n/a)</td><td>0.52 (n/a)</td><td>250.70 (n/a)</td><td>214.18 (n/a)</td><td>220.50 (n/a)</td><td>157.30 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>5.42 (-1.88%)</td><td>4.79 (-1.03%)</td><td>4.72 (-4.78%)</td><td>4.21 (+10.56%)</td><td>0.44 <b>(-33.46%)</b></td><td>249.30 (-9.54%)</td><td>220.48 (+0.03%)</td><td>222.10 (+5.01%)</td><td>193.30 (+1.90%)</td><td>20.34 <b>(-39.62%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>5.53 (n/a)</td><td>4.84 (n/a)</td><td>4.96 (n/a)</td><td>3.80 (n/a)</td><td>0.67 (n/a)</td><td>275.60 (n/a)</td><td>220.42 (n/a)</td><td>211.50 (n/a)</td><td>189.70 (n/a)</td><td>33.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>7.87 (-9.24%)</td><td>7.21 (-6.48%)</td><td>7.07 (-9.00%)</td><td>6.89 (+6.29%)</td><td>0.38 <b>(-53.48%)</b></td><td>304.50 (-5.90%)</td><td>291.62 (+6.12%)</td><td>296.70 (+9.89%)</td><td>266.50 (+10.17%)</td><td>14.72 <b>(-52.71%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.67 (n/a)</td><td>7.71 (n/a)</td><td>7.77 (n/a)</td><td>6.48 (n/a)</td><td>0.83 (n/a)</td><td>323.60 (n/a)</td><td>274.80 (n/a)</td><td>270.00 (n/a)</td><td>241.90 (n/a)</td><td>31.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.42 (+7.36%)</td><td>2.69 (-1.00%)</td><td>2.67 (-10.43%)</td><td>2.19 <b>(+46.58%)</b></td><td>0.45 <b>(-34.58%)</b></td><td>239.90 <b>(-31.79%)</b></td><td>199.02 (-4.85%)</td><td>196.70 (+11.63%)</td><td>153.50 (-6.86%)</td><td>31.19 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.18 (n/a)</td><td>2.72 (n/a)</td><td>2.98 (n/a)</td><td>1.49 (n/a)</td><td>0.69 (n/a)</td><td>351.70 (n/a)</td><td>209.16 (n/a)</td><td>176.20 (n/a)</td><td>164.80 (n/a)</td><td>79.85 (n/a)</td>
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
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>3.68 (+8.49%)</td><td>3.15 (+10.50%)</td><td>3.11 (+11.37%)</td><td>2.74 (+9.17%)</td><td>0.34 (+1.14%)</td><td>191.40 (-8.38%)</td><td>168.18 (-9.63%)</td><td>168.50 (-10.23%)</td><td>142.50 (-7.83%)</td><td>17.39 (-14.25%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.39 (n/a)</td><td>2.85 (n/a)</td><td>2.79 (n/a)</td><td>2.51 (n/a)</td><td>0.34 (n/a)</td><td>208.90 (n/a)</td><td>186.10 (n/a)</td><td>187.70 (n/a)</td><td>154.60 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.35 (+11.05%)</td><td>2.64 (-8.02%)</td><td>2.64 (-12.30%)</td><td>2.18 (-9.18%)</td><td>0.45 <b>(+68.04%)</b></td><td>240.20 (+10.13%)</td><td>202.52 (+10.20%)</td><td>198.70 (+14.06%)</td><td>156.50 (-9.95%)</td><td>31.72 <b>(+64.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.02 (n/a)</td><td>2.87 (n/a)</td><td>3.01 (n/a)</td><td>2.40 (n/a)</td><td>0.27 (n/a)</td><td>218.10 (n/a)</td><td>183.78 (n/a)</td><td>174.20 (n/a)</td><td>173.80 (n/a)</td><td>19.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.23 (-17.91%)</td><td>0.18 (-6.29%)</td><td>0.17 (-8.88%)</td><td>0.15 (+3.41%)</td><td>0.03 <b>(-35.28%)</b></td><td>213.70 (-3.26%)</td><td>181.30 (+4.52%)</td><td>187.50 (+9.71%)</td><td>142.40 <b>(+21.81%)</b></td><td>29.93 <b>(-20.75%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>220.90 (n/a)</td><td>173.46 (n/a)</td><td>170.90 (n/a)</td><td>116.90 (n/a)</td><td>37.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-2.71%)</td><td>0.22 (-4.17%)</td><td>0.21 (-2.48%)</td><td>0.13 (-19.03%)</td><td>0.07 (+16.95%)</td><td>252.00 <b>(+23.47%)</b></td><td>166.80 (+8.26%)</td><td>153.70 (+2.60%)</td><td>108.40 (+2.75%)</td><td>57.68 <b>(+48.01%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>154.08 (n/a)</td><td>149.80 (n/a)</td><td>105.50 (n/a)</td><td>38.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.20 (-5.60%)</td><td>0.16 (-15.62%)</td><td>0.16 <b>(-20.72%)</b></td><td>0.13 <b>(-21.83%)</b></td><td>0.03 <b>(+21.61%)</b></td><td>250.40 <b>(+27.89%)</b></td><td>207.50 (+19.69%)</td><td>204.90 <b>(+26.17%)</b></td><td>159.90 (+5.96%)</td><td>32.65 <b>(+56.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>173.36 (n/a)</td><td>162.40 (n/a)</td><td>150.90 (n/a)</td><td>20.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+10.75%)</td><td>0.24 (+16.62%)</td><td>0.25 <b>(+23.01%)</b></td><td>0.17 (+5.41%)</td><td>0.05 <b>(+22.12%)</b></td><td>197.30 (-5.14%)</td><td>142.28 (-13.43%)</td><td>128.60 (-18.71%)</td><td>110.80 (-9.70%)</td><td>34.24 (+6.74%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>164.36 (n/a)</td><td>158.20 (n/a)</td><td>122.70 (n/a)</td><td>32.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.56 (+2.43%)</td><td>0.39 (-0.13%)</td><td>0.36 (+6.93%)</td><td>0.31 (-0.94%)</td><td>0.10 (-0.57%)</td><td>212.90 (+0.95%)</td><td>173.34 (-0.15%)</td><td>180.50 (-6.48%)</td><td>117.90 (-2.32%)</td><td>34.83 (-5.98%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>210.90 (n/a)</td><td>173.60 (n/a)</td><td>193.00 (n/a)</td><td>120.70 (n/a)</td><td>37.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+7.51%)</td><td>0.41 (-6.98%)</td><td>0.38 (-15.71%)</td><td>0.35 (+10.51%)</td><td>0.09 (+10.99%)</td><td>187.30 (-9.52%)</td><td>165.30 (+7.53%)</td><td>172.10 (+18.61%)</td><td>115.70 (-6.99%)</td><td>29.42 (-9.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>207.00 (n/a)</td><td>153.72 (n/a)</td><td>145.10 (n/a)</td><td>124.40 (n/a)</td><td>32.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.39 (-19.84%)</td><td>0.32 <b>(-24.16%)</b></td><td>0.30 <b>(-32.26%)</b></td><td>0.27 (-15.47%)</td><td>0.05 (-19.04%)</td><td>240.10 (+18.28%)</td><td>210.22 <b>(+31.82%)</b></td><td>221.00 <b>(+47.63%)</b></td><td>170.10 <b>(+24.80%)</b></td><td>32.86 <b>(+20.26%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>203.00 (n/a)</td><td>159.48 (n/a)</td><td>149.70 (n/a)</td><td>136.30 (n/a)</td><td>27.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+14.09%)</td><td>0.41 (+4.91%)</td><td>0.40 (+8.52%)</td><td>0.34 <b>(+22.63%)</b></td><td>0.09 (+0.96%)</td><td>191.20 (-18.43%)</td><td>164.24 (-5.77%)</td><td>165.90 (-7.83%)</td><td>115.60 (-12.36%)</td><td>29.39 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>234.40 (n/a)</td><td>174.30 (n/a)</td><td>180.00 (n/a)</td><td>131.90 (n/a)</td><td>41.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.43 (-4.91%)</td><td>0.33 (-12.27%)</td><td>0.35 (-2.85%)</td><td>0.20 <b>(-38.11%)</b></td><td>0.08 <b>(+54.91%)</b></td><td>323.10 <b>(+61.55%)</b></td><td>209.76 (+19.73%)</td><td>185.60 (+2.94%)</td><td>151.20 (+5.15%)</td><td>66.63 <b>(+175.99%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>200.00 (n/a)</td><td>175.20 (n/a)</td><td>180.30 (n/a)</td><td>143.80 (n/a)</td><td>24.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.44 (-8.43%)</td><td>0.35 (-17.74%)</td><td>0.36 (-14.25%)</td><td>0.28 <b>(-25.93%)</b></td><td>0.06 <b>(+56.54%)</b></td><td>233.40 <b>(+34.99%)</b></td><td>189.10 <b>(+23.55%)</b></td><td>180.30 (+16.62%)</td><td>149.30 (+9.22%)</td><td>31.69 <b>(+131.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.04 (n/a)</td><td>172.90 (n/a)</td><td>153.06 (n/a)</td><td>154.60 (n/a)</td><td>136.70 (n/a)</td><td>13.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.97 (-6.86%)</td><td>0.80 (-6.08%)</td><td>0.78 (-9.35%)</td><td>0.69 (+0.39%)</td><td>0.10 (-19.52%)</td><td>191.10 (-0.36%)</td><td>165.12 (+5.87%)</td><td>167.60 (+10.34%)</td><td>135.60 (+7.36%)</td><td>19.99 (-15.72%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.04 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>191.80 (n/a)</td><td>155.96 (n/a)</td><td>151.90 (n/a)</td><td>126.30 (n/a)</td><td>23.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.12 (+10.46%)</td><td>0.82 (-2.73%)</td><td>0.75 (-11.80%)</td><td>0.51 (-17.11%)</td><td>0.25 <b>(+58.42%)</b></td><td>259.40 <b>(+20.65%)</b></td><td>173.04 (+8.00%)</td><td>174.80 (+13.43%)</td><td>116.70 (-9.46%)</td><td>56.79 <b>(+67.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.61 (n/a)</td><td>0.16 (n/a)</td><td>215.00 (n/a)</td><td>160.22 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>33.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.86 (-12.63%)</td><td>0.70 (+2.12%)</td><td>0.68 (+9.54%)</td><td>0.53 (-4.84%)</td><td>0.12 <b>(-30.45%)</b></td><td>248.60 (+5.07%)</td><td>192.34 (-3.70%)</td><td>191.90 (-8.71%)</td><td>151.60 (+14.42%)</td><td>35.80 (-12.49%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.99 (n/a)</td><td>0.68 (n/a)</td><td>0.62 (n/a)</td><td>0.55 (n/a)</td><td>0.18 (n/a)</td><td>236.60 (n/a)</td><td>199.72 (n/a)</td><td>210.20 (n/a)</td><td>132.50 (n/a)</td><td>40.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.08 (+11.42%)</td><td>0.84 (+10.19%)</td><td>0.71 (-5.09%)</td><td>0.68 (+8.35%)</td><td>0.20 <b>(+53.95%)</b></td><td>193.90 (-7.71%)</td><td>162.64 (-7.35%)</td><td>185.40 (+5.34%)</td><td>121.80 (-10.24%)</td><td>35.51 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>210.10 (n/a)</td><td>175.54 (n/a)</td><td>176.00 (n/a)</td><td>135.70 (n/a)</td><td>27.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.72 <b>(-29.42%)</b></td><td>0.64 (-13.80%)</td><td>0.64 (-4.65%)</td><td>0.56 (-9.92%)</td><td>0.06 <b>(-64.46%)</b></td><td>233.00 (+11.06%)</td><td>204.78 (+13.00%)</td><td>206.40 (+4.88%)</td><td>180.90 <b>(+41.66%)</b></td><td>19.02 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.03 (n/a)</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.62 (n/a)</td><td>0.17 (n/a)</td><td>209.80 (n/a)</td><td>181.22 (n/a)</td><td>196.80 (n/a)</td><td>127.70 (n/a)</td><td>33.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.91 (-7.72%)</td><td>0.75 (-7.56%)</td><td>0.74 (-7.43%)</td><td>0.61 (-12.47%)</td><td>0.15 <b>(+21.75%)</b></td><td>216.40 (+14.26%)</td><td>179.28 (+9.66%)</td><td>177.30 (+8.04%)</td><td>144.10 (+8.35%)</td><td>34.73 <b>(+49.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.99 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>189.40 (n/a)</td><td>163.48 (n/a)</td><td>164.10 (n/a)</td><td>133.00 (n/a)</td><td>23.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.79 <b>(-26.03%)</b></td><td>0.66 (-16.43%)</td><td>0.66 (-10.33%)</td><td>0.54 (-17.10%)</td><td>0.10 <b>(-39.46%)</b></td><td>240.70 <b>(+20.65%)</b></td><td>201.28 (+18.46%)</td><td>199.40 (+11.52%)</td><td>166.10 <b>(+35.15%)</b></td><td>29.41 (+2.93%)</td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.07 (n/a)</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.66 (n/a)</td><td>0.16 (n/a)</td><td>199.50 (n/a)</td><td>169.92 (n/a)</td><td>178.80 (n/a)</td><td>122.90 (n/a)</td><td>28.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 <b>(-30.80%)</b></td><td>0.68 <b>(-25.14%)</b></td><td>0.68 <b>(-20.51%)</b></td><td>0.48 <b>(-24.02%)</b></td><td>0.14 <b>(-45.20%)</b></td><td>271.50 <b>(+31.60%)</b></td><td>199.46 <b>(+30.35%)</b></td><td>193.20 <b>(+25.78%)</b></td><td>149.90 <b>(+44.55%)</b></td><td>44.25 (+7.66%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.26 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.25 (n/a)</td><td>206.30 (n/a)</td><td>153.02 (n/a)</td><td>153.60 (n/a)</td><td>103.70 (n/a)</td><td>41.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ee933b1</code> — 2026-08-24 22:01:42</td><td>0.11 <b>(-20.42%)</b></td><td>0.09 (-10.65%)</td><td>0.10 (+2.10%)</td><td>0.07 <b>(-22.33%)</b></td><td>0.02 <b>(-28.03%)</b></td><td>245.80 <b>(+28.76%)</b></td><td>180.00 (+11.43%)</td><td>171.50 (-2.06%)</td><td>146.90 <b>(+25.66%)</b></td><td>38.15 <b>(+21.18%)</b></td>
</tr>
<tr>
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>161.54 (n/a)</td><td>175.10 (n/a)</td><td>116.90 (n/a)</td><td>31.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+5.28%)</td><td>0.10 (-6.35%)</td><td>0.10 (-9.66%)</td><td>0.07 (-18.86%)</td><td>0.02 <b>(+61.29%)</b></td><td>226.90 <b>(+23.25%)</b></td><td>174.48 (+9.64%)</td><td>170.10 (+10.67%)</td><td>128.50 (-5.03%)</td><td>38.92 <b>(+86.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>159.14 (n/a)</td><td>153.70 (n/a)</td><td>135.30 (n/a)</td><td>20.83 (n/a)</td>
</tr>
</tbody>
</table>


</details>
