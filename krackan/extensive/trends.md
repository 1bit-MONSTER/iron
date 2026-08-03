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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 <b>(-33.08%)</b></td><td>0.03 <b>(-20.83%)</b></td><td>0.03 (-17.42%)</td><td>0.02 (-4.93%)</td><td>0.01 <b>(-52.07%)</b></td><td>251.40 (+5.19%)</td><td>198.44 <b>(+21.36%)</b></td><td>189.90 <b>(+21.11%)</b></td><td>160.30 <b>(+49.39%)</b></td><td>35.70 <b>(-24.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>163.52 (n/a)</td><td>156.80 (n/a)</td><td>107.30 (n/a)</td><td>47.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (+9.29%)</td><td>0.04 (+5.45%)</td><td>0.04 (+9.83%)</td><td>0.03 (+7.38%)</td><td>0.01 (+16.37%)</td><td>189.50 (-6.88%)</td><td>169.72 (-4.97%)</td><td>170.40 (-8.97%)</td><td>133.20 (-8.52%)</td><td>22.83 (-0.30%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.50 (n/a)</td><td>178.60 (n/a)</td><td>187.20 (n/a)</td><td>145.60 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+5.93%)</td><td>0.04 (-1.16%)</td><td>0.04 (+6.52%)</td><td>0.03 <b>(-21.02%)</b></td><td>0.01 <b>(+74.09%)</b></td><td>242.60 <b>(+26.62%)</b></td><td>180.78 (+4.27%)</td><td>173.20 (-6.12%)</td><td>139.90 (-5.60%)</td><td>42.65 <b>(+104.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>173.38 (n/a)</td><td>184.50 (n/a)</td><td>148.20 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (+17.94%)</td><td>0.04 (-9.93%)</td><td>0.03 (-19.99%)</td><td>0.02 <b>(-27.02%)</b></td><td>0.01 <b>(+161.21%)</b></td><td>246.90 <b>(+37.01%)</b></td><td>183.46 (+16.84%)</td><td>191.30 <b>(+25.03%)</b></td><td>117.00 (-15.22%)</td><td>46.88 <b>(+190.95%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.20 (n/a)</td><td>157.02 (n/a)</td><td>153.00 (n/a)</td><td>138.00 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(-32.93%)</b></td><td>0.03 (-7.42%)</td><td>0.03 (-1.24%)</td><td>0.02 <b>(+29.41%)</b></td><td>0.00 <b>(-69.20%)</b></td><td>246.90 <b>(-22.72%)</b></td><td>205.96 (-0.11%)</td><td>193.10 (+1.21%)</td><td>186.30 <b>(+49.16%)</b></td><td>24.91 <b>(-64.73%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>319.50 (n/a)</td><td>206.18 (n/a)</td><td>190.80 (n/a)</td><td>124.90 (n/a)</td><td>70.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-8.57%)</td><td>0.03 (-7.68%)</td><td>0.03 (-11.45%)</td><td>0.02 <b>(+25.61%)</b></td><td>0.00 <b>(-41.49%)</b></td><td>284.30 <b>(-20.39%)</b></td><td>230.70 (+3.19%)</td><td>212.90 (+12.94%)</td><td>192.60 (+9.37%)</td><td>38.50 <b>(-49.62%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>357.10 (n/a)</td><td>223.56 (n/a)</td><td>188.50 (n/a)</td><td>176.10 (n/a)</td><td>76.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-11.13%)</td><td>0.03 (+1.86%)</td><td>0.03 (+1.19%)</td><td>0.03 (+13.84%)</td><td>0.00 <b>(-37.30%)</b></td><td>209.00 (-12.15%)</td><td>181.16 (-4.04%)</td><td>176.90 (-1.23%)</td><td>155.40 (+12.53%)</td><td>24.70 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>188.78 (n/a)</td><td>179.10 (n/a)</td><td>138.10 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-12.76%)</td><td>0.03 (-17.21%)</td><td>0.03 <b>(-22.19%)</b></td><td>0.02 <b>(-20.18%)</b></td><td>0.00 (-1.27%)</td><td>266.30 <b>(+25.32%)</b></td><td>218.54 <b>(+21.45%)</b></td><td>217.40 <b>(+28.56%)</b></td><td>177.70 (+14.57%)</td><td>34.36 <b>(+40.75%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>179.94 (n/a)</td><td>169.10 (n/a)</td><td>155.10 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (+16.07%)</td><td>0.09 (+18.16%)</td><td>0.10 <b>(+30.64%)</b></td><td>0.07 <b>(+36.08%)</b></td><td>0.02 (+9.18%)</td><td>186.40 <b>(-26.53%)</b></td><td>147.30 (-16.27%)</td><td>126.90 <b>(-23.46%)</b></td><td>122.40 (-13.80%)</td><td>31.33 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>253.70 (n/a)</td><td>175.92 (n/a)</td><td>165.80 (n/a)</td><td>142.00 (n/a)</td><td>45.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (+5.57%)</td><td>0.07 (-3.13%)</td><td>0.06 (-5.06%)</td><td>0.05 (-7.94%)</td><td>0.02 <b>(+28.06%)</b></td><td>246.40 (+8.59%)</td><td>195.54 (+5.22%)</td><td>195.80 (+5.33%)</td><td>135.10 (-5.33%)</td><td>45.85 <b>(+32.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>185.84 (n/a)</td><td>185.90 (n/a)</td><td>142.70 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (-11.22%)</td><td>0.07 (-1.79%)</td><td>0.07 (-0.38%)</td><td>0.06 (+9.76%)</td><td>0.01 <b>(-25.52%)</b></td><td>220.10 (-8.90%)</td><td>186.92 (+0.27%)</td><td>187.40 (+0.37%)</td><td>155.00 (+12.65%)</td><td>30.26 <b>(-23.76%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.60 (n/a)</td><td>186.42 (n/a)</td><td>186.70 (n/a)</td><td>137.60 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (-3.05%)</td><td>0.07 (+10.02%)</td><td>0.07 (+12.63%)</td><td>0.05 (+7.25%)</td><td>0.01 <b>(-22.53%)</b></td><td>231.60 (-6.76%)</td><td>184.54 (-10.17%)</td><td>182.30 (-11.20%)</td><td>152.00 (+3.19%)</td><td>29.30 <b>(-21.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>248.40 (n/a)</td><td>205.44 (n/a)</td><td>205.30 (n/a)</td><td>147.30 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (-5.61%)</td><td>0.07 (+3.66%)</td><td>0.07 (+3.90%)</td><td>0.06 (+8.79%)</td><td>0.01 <b>(-31.42%)</b></td><td>213.30 (-8.10%)</td><td>183.80 (-4.81%)</td><td>180.00 (-3.74%)</td><td>156.80 (+5.95%)</td><td>22.05 <b>(-33.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>193.08 (n/a)</td><td>187.00 (n/a)</td><td>148.00 (n/a)</td><td>33.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (-3.98%)</td><td>0.06 (-11.54%)</td><td>0.05 (-18.37%)</td><td>0.04 (-15.34%)</td><td>0.02 (+6.02%)</td><td>295.10 (+18.13%)</td><td>215.78 (+15.43%)</td><td>239.40 <b>(+22.52%)</b></td><td>138.70 (+4.13%)</td><td>63.84 <b>(+31.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>249.80 (n/a)</td><td>186.94 (n/a)</td><td>195.40 (n/a)</td><td>133.20 (n/a)</td><td>48.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (-5.41%)</td><td>0.06 (-1.26%)</td><td>0.06 (+6.69%)</td><td>0.04 (-17.34%)</td><td>0.01 <b>(+21.46%)</b></td><td>303.30 <b>(+20.98%)</b></td><td>208.00 (+3.40%)</td><td>191.30 (-6.27%)</td><td>170.70 (+5.70%)</td><td>54.29 <b>(+61.24%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>250.70 (n/a)</td><td>201.16 (n/a)</td><td>204.10 (n/a)</td><td>161.50 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (+1.13%)</td><td>0.07 (+7.55%)</td><td>0.08 (+16.03%)</td><td>0.06 (+4.70%)</td><td>0.01 (-16.83%)</td><td>211.80 (-4.47%)</td><td>170.16 (-7.94%)</td><td>163.70 (-13.80%)</td><td>141.90 (-1.11%)</td><td>27.37 <b>(-21.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>184.84 (n/a)</td><td>189.90 (n/a)</td><td>143.50 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (-6.31%)</td><td>0.15 (+2.16%)</td><td>0.16 (+5.51%)</td><td>0.13 (+8.92%)</td><td>0.02 <b>(-30.84%)</b></td><td>187.90 (-8.21%)</td><td>162.12 (-3.19%)</td><td>157.70 (-5.17%)</td><td>145.80 (+6.73%)</td><td>18.26 <b>(-32.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>167.46 (n/a)</td><td>166.30 (n/a)</td><td>136.60 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (-18.35%)</td><td>0.14 (-8.80%)</td><td>0.15 (+1.49%)</td><td>0.12 (+15.23%)</td><td>0.02 <b>(-52.26%)</b></td><td>207.80 (-13.20%)</td><td>178.12 (+5.70%)</td><td>163.90 (-1.50%)</td><td>159.00 <b>(+22.50%)</b></td><td>22.76 <b>(-48.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>239.40 (n/a)</td><td>168.52 (n/a)</td><td>166.40 (n/a)</td><td>129.80 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 <b>(+22.23%)</b></td><td>0.16 <b>(+24.12%)</b></td><td>0.17 <b>(+27.53%)</b></td><td>0.13 (+13.01%)</td><td>0.02 <b>(+32.58%)</b></td><td>188.40 (-11.51%)</td><td>153.20 (-19.19%)</td><td>147.60 <b>(-21.57%)</b></td><td>138.70 (-18.17%)</td><td>20.02 (-0.87%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>189.58 (n/a)</td><td>188.20 (n/a)</td><td>169.50 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (-16.46%)</td><td>0.13 (-5.42%)</td><td>0.13 (-5.33%)</td><td>0.11 (-0.09%)</td><td>0.02 <b>(-34.62%)</b></td><td>213.80 (+0.09%)</td><td>186.96 (+4.33%)</td><td>188.50 (+5.66%)</td><td>156.20 (+19.69%)</td><td>25.58 (-19.42%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.60 (n/a)</td><td>179.20 (n/a)</td><td>178.40 (n/a)</td><td>130.50 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (-11.83%)</td><td>0.14 (+6.47%)</td><td>0.14 (+18.99%)</td><td>0.13 <b>(+21.31%)</b></td><td>0.01 <b>(-62.25%)</b></td><td>186.90 (-17.59%)</td><td>170.92 (-9.03%)</td><td>170.80 (-15.99%)</td><td>157.40 (+13.40%)</td><td>13.43 <b>(-65.02%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.80 (n/a)</td><td>187.88 (n/a)</td><td>203.30 (n/a)</td><td>138.80 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (+3.06%)</td><td>0.15 (+19.20%)</td><td>0.14 (+12.17%)</td><td>0.13 <b>(+93.68%)</b></td><td>0.02 <b>(-44.82%)</b></td><td>190.30 <b>(-48.37%)</b></td><td>166.04 <b>(-23.29%)</b></td><td>175.20 (-10.84%)</td><td>138.30 (-2.95%)</td><td>23.43 <b>(-73.80%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>368.60 (n/a)</td><td>216.46 (n/a)</td><td>196.50 (n/a)</td><td>142.50 (n/a)</td><td>89.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (-14.34%)</td><td>0.13 (-4.59%)</td><td>0.12 (-12.85%)</td><td>0.11 (+7.35%)</td><td>0.02 <b>(-41.40%)</b></td><td>215.50 (-6.83%)</td><td>194.64 (+2.78%)</td><td>208.10 (+14.72%)</td><td>163.50 (+16.70%)</td><td>23.05 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.30 (n/a)</td><td>189.38 (n/a)</td><td>181.40 (n/a)</td><td>140.10 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (+15.66%)</td><td>0.13 (+11.52%)</td><td>0.13 (+4.68%)</td><td>0.11 <b>(+55.15%)</b></td><td>0.02 <b>(-32.96%)</b></td><td>218.50 <b>(-35.55%)</b></td><td>187.28 (-14.25%)</td><td>190.60 (-4.46%)</td><td>150.90 (-13.57%)</td><td>24.30 <b>(-64.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>339.00 (n/a)</td><td>218.40 (n/a)</td><td>199.50 (n/a)</td><td>174.60 (n/a)</td><td>68.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 <b>(-22.74%)</b></td><td>0.26 <b>(-28.75%)</b></td><td>0.28 <b>(-22.02%)</b></td><td>0.17 <b>(-47.84%)</b></td><td>0.07 <b>(+33.76%)</b></td><td>297.20 <b>(+91.74%)</b></td><td>200.28 <b>(+47.37%)</b></td><td>176.60 <b>(+28.25%)</b></td><td>141.90 <b>(+29.47%)</b></td><td>60.21 <b>(+244.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>155.00 (n/a)</td><td>135.90 (n/a)</td><td>137.70 (n/a)</td><td>109.60 (n/a)</td><td>17.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 (-18.34%)</td><td>0.26 (-19.98%)</td><td>0.25 (-19.43%)</td><td>0.20 <b>(-28.04%)</b></td><td>0.06 (-5.50%)</td><td>244.60 <b>(+38.98%)</b></td><td>195.64 <b>(+26.53%)</b></td><td>193.60 <b>(+24.10%)</b></td><td>139.50 <b>(+22.48%)</b></td><td>40.28 <b>(+61.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>176.00 (n/a)</td><td>154.62 (n/a)</td><td>156.00 (n/a)</td><td>113.90 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 <b>(-28.07%)</b></td><td>0.27 <b>(-20.60%)</b></td><td>0.27 (-17.98%)</td><td>0.24 (-6.16%)</td><td>0.03 <b>(-58.80%)</b></td><td>204.90 (+6.55%)</td><td>185.56 <b>(+22.72%)</b></td><td>182.90 <b>(+21.93%)</b></td><td>156.60 <b>(+39.08%)</b></td><td>19.06 <b>(-39.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>192.30 (n/a)</td><td>151.20 (n/a)</td><td>150.00 (n/a)</td><td>112.60 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 (-12.68%)</td><td>0.27 (-18.42%)</td><td>0.27 (-11.74%)</td><td>0.20 <b>(-26.06%)</b></td><td>0.06 <b>(+29.91%)</b></td><td>240.40 <b>(+35.28%)</b></td><td>192.36 <b>(+25.59%)</b></td><td>180.40 (+13.32%)</td><td>143.30 (+14.55%)</td><td>42.01 <b>(+109.93%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>177.70 (n/a)</td><td>153.16 (n/a)</td><td>159.20 (n/a)</td><td>125.10 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (-15.53%)</td><td>0.26 (-9.62%)</td><td>0.27 (-10.99%)</td><td>0.23 (+17.63%)</td><td>0.02 <b>(-57.62%)</b></td><td>215.20 (-15.01%)</td><td>193.72 (+7.40%)</td><td>185.10 (+12.39%)</td><td>175.20 (+18.38%)</td><td>17.76 <b>(-58.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>253.20 (n/a)</td><td>180.38 (n/a)</td><td>164.70 (n/a)</td><td>148.00 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.35 (+5.09%)</td><td>0.30 (-0.63%)</td><td>0.29 (+2.12%)</td><td>0.25 (-8.79%)</td><td>0.04 <b>(+39.73%)</b></td><td>195.00 (+9.67%)</td><td>167.90 (+1.23%)</td><td>168.40 (-2.09%)</td><td>139.20 (-4.85%)</td><td>20.00 <b>(+43.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>177.80 (n/a)</td><td>165.86 (n/a)</td><td>172.00 (n/a)</td><td>146.30 (n/a)</td><td>13.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 <b>(-20.29%)</b></td><td>0.23 (-8.63%)</td><td>0.23 (-1.33%)</td><td>0.20 (-0.81%)</td><td>0.02 <b>(-60.76%)</b></td><td>247.30 (+0.82%)</td><td>212.70 (+5.81%)</td><td>213.10 (+1.38%)</td><td>186.60 <b>(+25.40%)</b></td><td>22.22 <b>(-50.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>245.30 (n/a)</td><td>201.02 (n/a)</td><td>210.20 (n/a)</td><td>148.80 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (+0.17%)</td><td>0.25 (+0.86%)</td><td>0.23 (+3.20%)</td><td>0.20 (+0.79%)</td><td>0.05 (-11.33%)</td><td>245.90 (-0.77%)</td><td>203.38 (-1.74%)</td><td>209.90 (-3.14%)</td><td>152.20 (-0.20%)</td><td>36.40 (-14.50%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>247.80 (n/a)</td><td>206.98 (n/a)</td><td>216.70 (n/a)</td><td>152.50 (n/a)</td><td>42.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-16.97%)</td><td>0.02 (-19.01%)</td><td>0.02 <b>(-22.86%)</b></td><td>0.01 (-9.36%)</td><td>0.00 <b>(-27.54%)</b></td><td>206.70 (+10.30%)</td><td>164.92 <b>(+22.11%)</b></td><td>165.90 <b>(+29.71%)</b></td><td>130.40 <b>(+20.41%)</b></td><td>28.06 (-7.86%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>135.06 (n/a)</td><td>127.90 (n/a)</td><td>108.30 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 <b>(-27.80%)</b></td><td>0.02 (-9.06%)</td><td>0.02 (-6.50%)</td><td>0.01 (+7.21%)</td><td>0.00 <b>(-78.46%)</b></td><td>177.80 (-6.72%)</td><td>162.90 (+5.75%)</td><td>161.40 (+6.96%)</td><td>155.10 <b>(+38.48%)</b></td><td>9.29 <b>(-72.91%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>154.04 (n/a)</td><td>150.90 (n/a)</td><td>112.00 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 <b>(-25.34%)</b></td><td>0.02 (-18.83%)</td><td>0.02 (-10.16%)</td><td>0.01 (-12.99%)</td><td>0.00 <b>(-44.54%)</b></td><td>201.40 (+14.95%)</td><td>169.06 <b>(+21.28%)</b></td><td>159.70 (+11.29%)</td><td>144.50 <b>(+33.92%)</b></td><td>23.60 (-12.72%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>175.20 (n/a)</td><td>139.40 (n/a)</td><td>143.50 (n/a)</td><td>107.90 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (+8.28%)</td><td>0.02 (-1.51%)</td><td>0.02 (+5.56%)</td><td>0.01 <b>(-24.37%)</b></td><td>0.00 <b>(+105.00%)</b></td><td>240.20 <b>(+32.20%)</b></td><td>175.78 (+4.18%)</td><td>167.10 (-5.27%)</td><td>140.20 (-7.64%)</td><td>37.97 <b>(+161.88%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>181.70 (n/a)</td><td>168.72 (n/a)</td><td>176.40 (n/a)</td><td>151.80 (n/a)</td><td>14.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-7.88%)</td><td>0.02 (-1.18%)</td><td>0.02 (-0.17%)</td><td>0.02 (+5.20%)</td><td>0.00 <b>(-50.28%)</b></td><td>171.50 (-4.93%)</td><td>161.96 (+0.33%)</td><td>163.30 (+0.12%)</td><td>146.30 (+8.53%)</td><td>9.42 <b>(-49.51%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>180.40 (n/a)</td><td>161.42 (n/a)</td><td>163.10 (n/a)</td><td>134.80 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-2.50%)</td><td>0.02 (+7.48%)</td><td>0.01 (+11.07%)</td><td>0.01 (+12.50%)</td><td>0.00 <b>(-39.16%)</b></td><td>192.40 (-11.09%)</td><td>175.14 (-7.76%)</td><td>175.70 (-9.94%)</td><td>156.40 (+2.56%)</td><td>13.29 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>189.88 (n/a)</td><td>195.10 (n/a)</td><td>152.50 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-13.05%)</td><td>0.02 (-12.65%)</td><td>0.02 (-12.11%)</td><td>0.01 (-11.20%)</td><td>0.00 (-13.23%)</td><td>192.20 (+12.60%)</td><td>175.64 (+14.48%)</td><td>172.40 (+13.80%)</td><td>162.40 (+15.01%)</td><td>13.46 (+12.39%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.70 (n/a)</td><td>153.42 (n/a)</td><td>151.50 (n/a)</td><td>141.20 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.01 (-2.47%)</td><td>0.01 (-18.56%)</td><td>0.01 (-18.61%)</td><td>0.01 <b>(-42.46%)</b></td><td>0.00 <b>(+203.32%)</b></td><td>370.70 <b>(+73.79%)</b></td><td>251.50 <b>(+31.81%)</b></td><td>233.40 <b>(+22.84%)</b></td><td>175.20 (+2.58%)</td><td>80.26 <b>(+431.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>190.80 (n/a)</td><td>190.00 (n/a)</td><td>170.80 (n/a)</td><td>15.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-11.68%)</td><td>0.03 (-13.40%)</td><td>0.03 (-12.05%)</td><td>0.02 <b>(-45.08%)</b></td><td>0.01 <b>(+31.34%)</b></td><td>345.90 <b>(+82.15%)</b></td><td>190.66 <b>(+25.06%)</b></td><td>153.80 (+13.76%)</td><td>141.50 (+13.20%)</td><td>87.16 <b>(+180.84%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>152.46 (n/a)</td><td>135.20 (n/a)</td><td>125.00 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-6.39%)</td><td>0.03 (-6.35%)</td><td>0.04 (-0.93%)</td><td>0.03 (-9.71%)</td><td>0.00 <b>(+35.06%)</b></td><td>177.30 (+10.74%)</td><td>158.24 (+7.28%)</td><td>147.90 (+0.89%)</td><td>144.40 (+6.80%)</td><td>17.00 <b>(+60.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.10 (n/a)</td><td>147.50 (n/a)</td><td>146.60 (n/a)</td><td>135.20 (n/a)</td><td>10.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-0.45%)</td><td>0.03 (-3.97%)</td><td>0.03 (-3.80%)</td><td>0.03 (-10.98%)</td><td>0.01 <b>(+34.55%)</b></td><td>199.10 (+12.30%)</td><td>162.70 (+5.35%)</td><td>158.40 (+4.01%)</td><td>129.50 (+0.47%)</td><td>27.09 <b>(+53.87%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>154.44 (n/a)</td><td>152.30 (n/a)</td><td>128.90 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+3.95%)</td><td>0.03 (+16.48%)</td><td>0.04 (+5.15%)</td><td>0.03 <b>(+120.98%)</b></td><td>0.00 <b>(-59.02%)</b></td><td>185.10 <b>(-54.74%)</b></td><td>154.06 <b>(-25.84%)</b></td><td>149.90 (-4.89%)</td><td>131.20 (-3.81%)</td><td>19.54 <b>(-82.88%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>409.00 (n/a)</td><td>207.74 (n/a)</td><td>157.60 (n/a)</td><td>136.40 (n/a)</td><td>114.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-8.77%)</td><td>0.03 (-15.75%)</td><td>0.03 (-18.20%)</td><td>0.02 <b>(-27.35%)</b></td><td>0.01 <b>(+31.99%)</b></td><td>232.20 <b>(+37.64%)</b></td><td>178.76 <b>(+21.08%)</b></td><td>178.70 <b>(+22.23%)</b></td><td>140.50 (+9.59%)</td><td>36.81 <b>(+96.88%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>168.70 (n/a)</td><td>147.64 (n/a)</td><td>146.20 (n/a)</td><td>128.20 (n/a)</td><td>18.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+17.34%)</td><td>0.03 <b>(+26.32%)</b></td><td>0.03 <b>(+28.51%)</b></td><td>0.03 <b>(+49.85%)</b></td><td>0.00 <b>(-36.78%)</b></td><td>188.90 <b>(-33.27%)</b></td><td>163.04 <b>(-22.84%)</b></td><td>158.60 <b>(-22.18%)</b></td><td>146.50 (-14.78%)</td><td>16.70 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>283.10 (n/a)</td><td>211.30 (n/a)</td><td>203.80 (n/a)</td><td>171.90 (n/a)</td><td>45.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+16.50%)</td><td>0.03 (+6.27%)</td><td>0.03 (+15.32%)</td><td>0.02 <b>(-26.47%)</b></td><td>0.01 <b>(+153.61%)</b></td><td>283.90 <b>(+36.03%)</b></td><td>186.44 (-0.78%)</td><td>168.70 (-13.26%)</td><td>139.60 (-14.15%)</td><td>57.37 <b>(+208.30%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>187.90 (n/a)</td><td>194.50 (n/a)</td><td>162.60 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-1.27%)</td><td>0.03 (+0.92%)</td><td>0.03 (+2.90%)</td><td>0.02 (-8.71%)</td><td>0.00 <b>(+43.72%)</b></td><td>230.30 (+9.56%)</td><td>190.72 (-0.29%)</td><td>186.20 (-2.82%)</td><td>172.60 (+1.29%)</td><td>23.34 <b>(+62.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>191.28 (n/a)</td><td>191.60 (n/a)</td><td>170.40 (n/a)</td><td>14.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (-1.13%)</td><td>0.06 (-3.58%)</td><td>0.07 (-0.11%)</td><td>0.05 (-17.72%)</td><td>0.01 <b>(+114.96%)</b></td><td>202.30 <b>(+21.50%)</b></td><td>164.68 (+4.81%)</td><td>154.10 (+0.13%)</td><td>148.80 (+1.16%)</td><td>22.12 <b>(+163.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>166.50 (n/a)</td><td>157.12 (n/a)</td><td>153.90 (n/a)</td><td>147.10 (n/a)</td><td>8.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (+7.43%)</td><td>0.06 (+11.66%)</td><td>0.06 (+3.79%)</td><td>0.06 <b>(+52.43%)</b></td><td>0.01 <b>(-34.94%)</b></td><td>178.00 <b>(-34.39%)</b></td><td>164.12 (-13.78%)</td><td>168.80 (-3.65%)</td><td>130.20 (-6.87%)</td><td>19.59 <b>(-61.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>271.30 (n/a)</td><td>190.34 (n/a)</td><td>175.20 (n/a)</td><td>139.80 (n/a)</td><td>51.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (+18.71%)</td><td>0.07 (-1.53%)</td><td>0.07 (-2.46%)</td><td>0.05 <b>(-24.37%)</b></td><td>0.02 <b>(+197.41%)</b></td><td>232.90 <b>(+32.25%)</b></td><td>166.70 (+6.78%)</td><td>152.00 (+2.49%)</td><td>122.80 (-15.72%)</td><td>45.64 <b>(+234.33%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>176.10 (n/a)</td><td>156.12 (n/a)</td><td>148.30 (n/a)</td><td>145.70 (n/a)</td><td>13.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (-0.30%)</td><td>0.06 (-4.11%)</td><td>0.06 (+2.98%)</td><td>0.05 (-14.43%)</td><td>0.01 (+18.72%)</td><td>228.00 (+16.86%)</td><td>175.90 (+5.32%)</td><td>166.50 (-2.92%)</td><td>145.80 (+0.34%)</td><td>31.66 <b>(+46.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>167.02 (n/a)</td><td>171.50 (n/a)</td><td>145.30 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 <b>(+29.48%)</b></td><td>0.07 (+9.65%)</td><td>0.06 (-2.76%)</td><td>0.04 (-7.90%)</td><td>0.02 <b>(+108.98%)</b></td><td>234.80 (+8.55%)</td><td>169.08 (-4.95%)</td><td>173.30 (+2.79%)</td><td>118.30 <b>(-22.78%)</b></td><td>45.77 <b>(+73.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>177.88 (n/a)</td><td>168.60 (n/a)</td><td>153.20 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (+13.78%)</td><td>0.06 (+1.51%)</td><td>0.07 (+7.72%)</td><td>0.04 (-16.32%)</td><td>0.01 <b>(+150.80%)</b></td><td>235.70 (+19.46%)</td><td>175.92 (+1.46%)</td><td>160.20 (-7.13%)</td><td>139.00 (-12.14%)</td><td>38.65 <b>(+162.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>197.30 (n/a)</td><td>173.38 (n/a)</td><td>172.50 (n/a)</td><td>158.20 (n/a)</td><td>14.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (+14.77%)</td><td>0.07 <b>(+24.51%)</b></td><td>0.07 <b>(+24.84%)</b></td><td>0.06 <b>(+23.31%)</b></td><td>0.01 (-1.15%)</td><td>183.30 (-18.89%)</td><td>146.34 <b>(-20.56%)</b></td><td>141.80 (-19.89%)</td><td>116.30 (-12.88%)</td><td>25.89 <b>(-30.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>184.22 (n/a)</td><td>177.00 (n/a)</td><td>133.50 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 <b>(+22.66%)</b></td><td>0.05 (+4.05%)</td><td>0.05 (+3.08%)</td><td>0.03 (-14.78%)</td><td>0.01 <b>(+167.78%)</b></td><td>305.40 (+17.33%)</td><td>226.12 (-0.88%)</td><td>219.50 (-3.00%)</td><td>169.90 (-18.47%)</td><td>50.00 <b>(+156.81%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>260.30 (n/a)</td><td>228.12 (n/a)</td><td>226.30 (n/a)</td><td>208.40 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 <b>(+30.31%)</b></td><td>0.14 (+17.84%)</td><td>0.14 (+15.07%)</td><td>0.13 (+9.46%)</td><td>0.02 <b>(+126.37%)</b></td><td>167.10 (-8.69%)</td><td>146.68 (-14.55%)</td><td>145.20 (-13.11%)</td><td>125.00 <b>(-23.27%)</b></td><td>15.94 <b>(+58.07%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>171.66 (n/a)</td><td>167.10 (n/a)</td><td>162.90 (n/a)</td><td>10.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (-13.30%)</td><td>0.14 (+14.22%)</td><td>0.15 <b>(+34.69%)</b></td><td>0.12 <b>(+32.57%)</b></td><td>0.02 <b>(-50.05%)</b></td><td>175.70 <b>(-24.59%)</b></td><td>151.28 (-16.61%)</td><td>143.00 <b>(-25.75%)</b></td><td>132.50 (+15.32%)</td><td>20.69 <b>(-55.84%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>233.00 (n/a)</td><td>181.42 (n/a)</td><td>192.60 (n/a)</td><td>114.90 (n/a)</td><td>46.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 <b>(+29.55%)</b></td><td>0.14 (+19.57%)</td><td>0.15 <b>(+24.06%)</b></td><td>0.11 (+2.57%)</td><td>0.02 <b>(+173.25%)</b></td><td>189.20 (-2.52%)</td><td>148.14 (-14.93%)</td><td>137.40 (-19.37%)</td><td>124.70 <b>(-22.79%)</b></td><td>25.22 <b>(+106.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>174.14 (n/a)</td><td>170.40 (n/a)</td><td>161.50 (n/a)</td><td>12.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 <b>(-24.41%)</b></td><td>0.12 (-8.48%)</td><td>0.12 (+2.71%)</td><td>0.11 (+2.85%)</td><td>0.02 <b>(-56.28%)</b></td><td>197.30 (-2.81%)</td><td>173.06 (+4.53%)</td><td>174.00 (-2.63%)</td><td>140.80 <b>(+32.33%)</b></td><td>22.90 <b>(-44.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>203.00 (n/a)</td><td>165.56 (n/a)</td><td>178.70 (n/a)</td><td>106.40 (n/a)</td><td>41.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (+12.24%)</td><td>0.12 (-0.85%)</td><td>0.12 (-3.59%)</td><td>0.10 (+0.78%)</td><td>0.02 <b>(+39.71%)</b></td><td>202.20 (-0.79%)</td><td>174.22 (+1.37%)</td><td>171.50 (+3.69%)</td><td>142.60 (-10.93%)</td><td>21.72 <b>(+20.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>171.86 (n/a)</td><td>165.40 (n/a)</td><td>160.10 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (+1.41%)</td><td>0.12 (+2.62%)</td><td>0.12 (-3.16%)</td><td>0.09 (-2.99%)</td><td>0.02 (+2.30%)</td><td>236.00 (+3.10%)</td><td>180.32 (-2.42%)</td><td>178.90 (+3.23%)</td><td>142.30 (-1.39%)</td><td>35.77 (+3.24%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>228.90 (n/a)</td><td>184.80 (n/a)</td><td>173.30 (n/a)</td><td>144.30 (n/a)</td><td>34.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (-2.56%)</td><td>0.11 (-7.27%)</td><td>0.11 (-12.18%)</td><td>0.10 (-6.17%)</td><td>0.02 <b>(+33.48%)</b></td><td>216.10 (+6.56%)</td><td>188.42 (+8.90%)</td><td>198.70 (+13.87%)</td><td>155.90 (+2.63%)</td><td>29.26 <b>(+45.29%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>173.02 (n/a)</td><td>174.50 (n/a)</td><td>151.90 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (+7.22%)</td><td>0.11 (-1.13%)</td><td>0.10 (-6.46%)</td><td>0.09 (+9.31%)</td><td>0.01 (-0.57%)</td><td>229.50 (-8.49%)</td><td>201.20 (+0.86%)</td><td>201.00 (+6.91%)</td><td>162.60 (-6.71%)</td><td>26.42 (-15.58%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>199.48 (n/a)</td><td>188.00 (n/a)</td><td>174.30 (n/a)</td><td>31.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>181.40 (n/a)</td><td>198.30 (n/a)</td><td>134.00 (n/a)</td><td>38.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>153.66 (n/a)</td><td>135.60 (n/a)</td><td>120.30 (n/a)</td><td>46.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>186.24 (n/a)</td><td>195.10 (n/a)</td><td>125.80 (n/a)</td><td>40.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.00 (n/a)</td><td>200.58 (n/a)</td><td>212.50 (n/a)</td><td>164.30 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>173.72 (n/a)</td><td>162.90 (n/a)</td><td>156.70 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>367.60 (n/a)</td><td>217.04 (n/a)</td><td>217.70 (n/a)</td><td>124.60 (n/a)</td><td>93.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>172.74 (n/a)</td><td>166.70 (n/a)</td><td>134.40 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>231.20 (n/a)</td><td>205.32 (n/a)</td><td>226.20 (n/a)</td><td>123.40 (n/a)</td><td>46.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>223.40 (n/a)</td><td>177.44 (n/a)</td><td>180.20 (n/a)</td><td>126.00 (n/a)</td><td>44.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>237.80 (n/a)</td><td>186.34 (n/a)</td><td>175.00 (n/a)</td><td>155.00 (n/a)</td><td>33.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>192.94 (n/a)</td><td>194.30 (n/a)</td><td>182.50 (n/a)</td><td>7.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>186.90 (n/a)</td><td>183.20 (n/a)</td><td>160.70 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.33 (+16.15%)</td><td>0.27 (+8.65%)</td><td>0.27 (+13.92%)</td><td>0.22 (-4.83%)</td><td>0.04 <b>(+84.17%)</b></td><td>220.00 (+5.06%)</td><td>183.56 (-6.95%)</td><td>180.70 (-12.20%)</td><td>149.50 (-13.88%)</td><td>26.04 <b>(+64.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>209.40 (n/a)</td><td>197.28 (n/a)</td><td>205.80 (n/a)</td><td>173.60 (n/a)</td><td>15.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>242.40 (n/a)</td><td>181.36 (n/a)</td><td>180.00 (n/a)</td><td>132.20 (n/a)</td><td>47.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>186.10 (n/a)</td><td>146.42 (n/a)</td><td>132.90 (n/a)</td><td>111.40 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>227.20 (n/a)</td><td>177.78 (n/a)</td><td>175.30 (n/a)</td><td>145.30 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>156.40 (n/a)</td><td>152.60 (n/a)</td><td>127.50 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.20 (n/a)</td><td>171.56 (n/a)</td><td>174.40 (n/a)</td><td>149.70 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>171.18 (n/a)</td><td>167.60 (n/a)</td><td>120.40 (n/a)</td><td>34.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>201.50 (n/a)</td><td>201.80 (n/a)</td><td>159.20 (n/a)</td><td>37.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>291.60 (n/a)</td><td>219.98 (n/a)</td><td>221.90 (n/a)</td><td>173.80 (n/a)</td><td>48.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>186.42 (n/a)</td><td>185.10 (n/a)</td><td>175.30 (n/a)</td><td>9.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>204.90 (n/a)</td><td>194.58 (n/a)</td><td>201.10 (n/a)</td><td>178.00 (n/a)</td><td>12.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>267.20 (n/a)</td><td>200.94 (n/a)</td><td>184.80 (n/a)</td><td>164.30 (n/a)</td><td>39.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>235.30 (n/a)</td><td>177.94 (n/a)</td><td>188.80 (n/a)</td><td>131.80 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.50 (n/a)</td><td>168.56 (n/a)</td><td>162.40 (n/a)</td><td>135.70 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>215.20 (n/a)</td><td>177.16 (n/a)</td><td>178.30 (n/a)</td><td>112.60 (n/a)</td><td>40.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>246.80 (n/a)</td><td>206.88 (n/a)</td><td>200.90 (n/a)</td><td>177.30 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>206.10 (n/a)</td><td>175.48 (n/a)</td><td>173.20 (n/a)</td><td>147.90 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>221.90 (n/a)</td><td>187.20 (n/a)</td><td>187.30 (n/a)</td><td>155.90 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>308.90 (n/a)</td><td>209.50 (n/a)</td><td>196.90 (n/a)</td><td>152.30 (n/a)</td><td>58.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>185.02 (n/a)</td><td>172.00 (n/a)</td><td>158.10 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.40 (n/a)</td><td>154.40 (n/a)</td><td>155.00 (n/a)</td><td>136.80 (n/a)</td><td>14.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>170.96 (n/a)</td><td>156.50 (n/a)</td><td>145.50 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>158.16 (n/a)</td><td>158.50 (n/a)</td><td>126.50 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.80 (n/a)</td><td>191.42 (n/a)</td><td>174.70 (n/a)</td><td>171.20 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>186.00 (n/a)</td><td>198.20 (n/a)</td><td>152.70 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>179.78 (n/a)</td><td>169.40 (n/a)</td><td>154.80 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.80 (n/a)</td><td>205.80 (n/a)</td><td>206.80 (n/a)</td><td>163.00 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>178.96 (n/a)</td><td>178.90 (n/a)</td><td>153.50 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>184.68 (n/a)</td><td>185.40 (n/a)</td><td>157.90 (n/a)</td><td>18.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>163.74 (n/a)</td><td>165.40 (n/a)</td><td>127.80 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>173.34 (n/a)</td><td>156.30 (n/a)</td><td>135.40 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>175.76 (n/a)</td><td>175.50 (n/a)</td><td>148.90 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.80 (n/a)</td><td>171.32 (n/a)</td><td>170.10 (n/a)</td><td>153.50 (n/a)</td><td>15.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>179.48 (n/a)</td><td>176.90 (n/a)</td><td>145.00 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.90 (n/a)</td><td>194.94 (n/a)</td><td>192.50 (n/a)</td><td>166.80 (n/a)</td><td>19.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>232.20 (n/a)</td><td>178.82 (n/a)</td><td>175.20 (n/a)</td><td>128.80 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>162.48 (n/a)</td><td>156.00 (n/a)</td><td>144.60 (n/a)</td><td>15.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.50 (n/a)</td><td>173.84 (n/a)</td><td>162.30 (n/a)</td><td>126.20 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>170.98 (n/a)</td><td>168.20 (n/a)</td><td>142.30 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.30 (n/a)</td><td>163.42 (n/a)</td><td>163.60 (n/a)</td><td>149.80 (n/a)</td><td>10.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>182.72 (n/a)</td><td>184.70 (n/a)</td><td>149.50 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.60 (n/a)</td><td>177.94 (n/a)</td><td>166.80 (n/a)</td><td>152.60 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.80 (n/a)</td><td>224.52 (n/a)</td><td>194.20 (n/a)</td><td>184.50 (n/a)</td><td>48.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>174.68 (n/a)</td><td>170.00 (n/a)</td><td>155.00 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>272.80 (n/a)</td><td>180.18 (n/a)</td><td>163.90 (n/a)</td><td>127.30 (n/a)</td><td>54.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>187.10 (n/a)</td><td>152.54 (n/a)</td><td>146.90 (n/a)</td><td>129.30 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.20 (n/a)</td><td>154.28 (n/a)</td><td>140.40 (n/a)</td><td>129.00 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.00 (n/a)</td><td>154.30 (n/a)</td><td>147.50 (n/a)</td><td>138.90 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>162.32 (n/a)</td><td>153.00 (n/a)</td><td>139.50 (n/a)</td><td>20.74 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.50 (n/a)</td><td>167.20 (n/a)</td><td>173.80 (n/a)</td><td>120.70 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.20 (n/a)</td><td>192.50 (n/a)</td><td>206.30 (n/a)</td><td>166.40 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.87 (-0.46%)</td><td>4.39 (+1.21%)</td><td>4.42 (+6.58%)</td><td>3.58 (-7.40%)</td><td>0.51 (+11.84%)</td><td>2627.10 (+7.99%)</td><td>2166.46 (-0.88%)</td><td>2126.30 (-6.18%)</td><td>1932.20 (+0.46%)</td><td>278.12 <b>(+23.57%)</b></td><td>1914.63 (-0.46%)</td><td>1728.17 (+1.21%)</td><td>1739.79 (+6.58%)</td><td>1408.15 (-7.40%)</td><td>201.35 (+11.84%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>4.89 (n/a)</td><td>4.34 (n/a)</td><td>4.15 (n/a)</td><td>3.87 (n/a)</td><td>0.46 (n/a)</td><td>2432.70 (n/a)</td><td>2185.60 (n/a)</td><td>2266.30 (n/a)</td><td>1923.30 (n/a)</td><td>225.08 (n/a)</td><td>1923.50 (n/a)</td><td>1707.44 (n/a)</td><td>1632.33 (n/a)</td><td>1520.72 (n/a)</td><td>180.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.52 <b>(+21.77%)</b></td><td>0.96 (-4.84%)</td><td>0.93 (-1.75%)</td><td>0.69 (-8.22%)</td><td>0.33 <b>(+50.78%)</b></td><td>321.90 (+8.93%)</td><td>249.14 (+9.47%)</td><td>239.00 (+1.79%)</td><td>145.70 (-17.92%)</td><td>71.04 <b>(+41.37%)</b></td><td>64.75 <b>(+21.77%)</b></td><td>41.03 (-4.84%)</td><td>39.48 (-1.75%)</td><td>29.31 (-8.22%)</td><td>14.27 <b>(+50.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.25 (n/a)</td><td>1.01 (n/a)</td><td>0.94 (n/a)</td><td>0.75 (n/a)</td><td>0.22 (n/a)</td><td>295.50 (n/a)</td><td>227.58 (n/a)</td><td>234.80 (n/a)</td><td>177.50 (n/a)</td><td>50.25 (n/a)</td><td>53.17 (n/a)</td><td>43.12 (n/a)</td><td>40.19 (n/a)</td><td>31.94 (n/a)</td><td>9.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.15 (-3.04%)</td><td>1.01 (-3.81%)</td><td>0.98 (-9.93%)</td><td>0.88 (+8.93%)</td><td>0.12 (-16.38%)</td><td>251.80 (-8.20%)</td><td>221.78 (+3.30%)</td><td>226.40 (+11.03%)</td><td>192.20 (+3.17%)</td><td>26.42 <b>(-23.91%)</b></td><td>49.10 (-3.04%)</td><td>43.05 (-3.81%)</td><td>41.68 (-9.93%)</td><td>37.48 (+8.93%)</td><td>5.21 (-16.38%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.19 (n/a)</td><td>1.05 (n/a)</td><td>1.08 (n/a)</td><td>0.81 (n/a)</td><td>0.15 (n/a)</td><td>274.30 (n/a)</td><td>214.70 (n/a)</td><td>203.90 (n/a)</td><td>186.30 (n/a)</td><td>34.72 (n/a)</td><td>50.64 (n/a)</td><td>44.75 (n/a)</td><td>46.27 (n/a)</td><td>34.41 (n/a)</td><td>6.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.52 (+0.88%)</td><td>0.52 (+0.34%)</td><td>0.52 (+0.03%)</td><td>0.52 (+0.42%)</td><td>0.00 <b>(+105.22%)</b></td><td>48627.70 (-0.42%)</td><td>48532.84 (-0.34%)</td><td>48622.10 (-0.03%)</td><td>48201.40 (-0.87%)</td><td>186.00 <b>(+102.59%)</b></td><td>356.42 (+0.88%)</td><td>353.99 (+0.34%)</td><td>353.33 (+0.03%)</td><td>353.29 (+0.42%)</td><td>1.36 <b>(+105.23%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48831.50 (n/a)</td><td>48696.16 (n/a)</td><td>48637.30 (n/a)</td><td>48624.30 (n/a)</td><td>91.81 (n/a)</td><td>353.32 (n/a)</td><td>352.80 (n/a)</td><td>353.22 (n/a)</td><td>351.82 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (+0.63%)</td><td>0.21 (+0.76%)</td><td>0.22 (+0.45%)</td><td>0.21 (+0.96%)</td><td>0.00 (-13.95%)</td><td>118897.80 (-0.95%)</td><td>117093.26 (-0.76%)</td><td>116821.20 (-0.45%)</td><td>116025.00 (-0.62%)</td><td>1141.20 (-15.28%)</td><td>148.07 (+0.63%)</td><td>146.73 (+0.76%)</td><td>147.06 (+0.45%)</td><td>144.49 (+0.96%)</td><td>1.42 (-13.95%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120041.00 (n/a)</td><td>117990.78 (n/a)</td><td>117344.40 (n/a)</td><td>116751.60 (n/a)</td><td>1347.01 (n/a)</td><td>147.15 (n/a)</td><td>145.62 (n/a)</td><td>146.41 (n/a)</td><td>143.12 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.89 (-0.42%)</td><td>0.88 (-0.35%)</td><td>0.88 (-0.64%)</td><td>0.87 (-0.28%)</td><td>0.01 (-15.17%)</td><td>28805.30 (+0.28%)</td><td>28559.28 (+0.35%)</td><td>28568.30 (+0.64%)</td><td>28359.40 (+0.42%)</td><td>167.10 (-14.58%)</td><td>605.79 (-0.42%)</td><td>601.57 (-0.35%)</td><td>601.36 (-0.64%)</td><td>596.41 (-0.28%)</td><td>3.51 (-15.17%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28723.50 (n/a)</td><td>28459.94 (n/a)</td><td>28385.90 (n/a)</td><td>28240.50 (n/a)</td><td>195.62 (n/a)</td><td>608.34 (n/a)</td><td>603.67 (n/a)</td><td>605.22 (n/a)</td><td>598.11 (n/a)</td><td>4.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.52 (-3.16%)</td><td>3.40 (+0.07%)</td><td>3.41 (+1.44%)</td><td>3.24 (-2.21%)</td><td>0.11 (-18.06%)</td><td>7778.40 (+2.26%)</td><td>7399.88 (-0.10%)</td><td>7370.90 (-1.42%)</td><td>7146.40 (+3.27%)</td><td>243.50 (-12.77%)</td><td>2403.98 (-3.16%)</td><td>2323.61 (+0.07%)</td><td>2330.77 (+1.44%)</td><td>2208.66 (-2.21%)</td><td>75.08 (-18.06%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.64 (n/a)</td><td>3.40 (n/a)</td><td>3.37 (n/a)</td><td>3.31 (n/a)</td><td>0.13 (n/a)</td><td>7606.70 (n/a)</td><td>7407.40 (n/a)</td><td>7477.20 (n/a)</td><td>6920.30 (n/a)</td><td>279.15 (n/a)</td><td>2482.53 (n/a)</td><td>2322.04 (n/a)</td><td>2297.63 (n/a)</td><td>2258.52 (n/a)</td><td>91.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.15 (-0.62%)</td><td>2.97 (-3.05%)</td><td>2.89 (-7.97%)</td><td>2.84 (-0.05%)</td><td>0.15 (+13.47%)</td><td>8858.90 (+0.05%)</td><td>8483.78 (+3.20%)</td><td>8701.30 (+8.66%)</td><td>7987.30 (+0.62%)</td><td>434.73 (+13.86%)</td><td>2150.90 (-0.62%)</td><td>2029.36 (-3.05%)</td><td>1974.40 (-7.97%)</td><td>1939.27 (-0.05%)</td><td>105.75 (+13.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.17 (n/a)</td><td>3.07 (n/a)</td><td>3.14 (n/a)</td><td>2.84 (n/a)</td><td>0.14 (n/a)</td><td>8854.70 (n/a)</td><td>8220.94 (n/a)</td><td>8007.80 (n/a)</td><td>7937.90 (n/a)</td><td>381.82 (n/a)</td><td>2164.30 (n/a)</td><td>2093.24 (n/a)</td><td>2145.40 (n/a)</td><td>1940.19 (n/a)</td><td>93.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.34 (+0.71%)</td><td>3.20 (-0.26%)</td><td>3.19 (+0.31%)</td><td>3.08 (-0.26%)</td><td>0.09 (-5.42%)</td><td>8158.40 (+0.26%)</td><td>7866.92 (+0.25%)</td><td>7883.00 (-0.31%)</td><td>7544.80 (-0.71%)</td><td>223.19 (-5.44%)</td><td>2277.04 (+0.71%)</td><td>2185.23 (-0.26%)</td><td>2179.36 (+0.31%)</td><td>2105.80 (-0.26%)</td><td>62.40 (-5.42%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.31 (n/a)</td><td>3.21 (n/a)</td><td>3.18 (n/a)</td><td>3.09 (n/a)</td><td>0.10 (n/a)</td><td>8137.40 (n/a)</td><td>7847.12 (n/a)</td><td>7907.30 (n/a)</td><td>7598.40 (n/a)</td><td>236.02 (n/a)</td><td>2260.98 (n/a)</td><td>2190.90 (n/a)</td><td>2172.66 (n/a)</td><td>2111.21 (n/a)</td><td>65.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.78 (-0.35%)</td><td>0.78 (-0.08%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.01%)</td><td>0.00 <b>(-70.91%)</b></td><td>96566.20 (+0.01%)</td><td>96478.00 (+0.08%)</td><td>96465.70 (+0.02%)</td><td>96433.50 (+0.35%)</td><td>51.22 <b>(-70.79%)</b></td><td>712.61 (-0.35%)</td><td>712.28 (-0.08%)</td><td>712.37 (-0.02%)</td><td>711.63 (-0.01%)</td><td>0.38 <b>(-70.91%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96552.40 (n/a)</td><td>96396.62 (n/a)</td><td>96442.90 (n/a)</td><td>96096.90 (n/a)</td><td>175.32 (n/a)</td><td>715.11 (n/a)</td><td>712.88 (n/a)</td><td>712.54 (n/a)</td><td>711.73 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.73 (-0.02%)</td><td>0.73 (-0.06%)</td><td>0.73 (-0.05%)</td><td>0.73 (-0.15%)</td><td>0.00 <b>(+281.23%)</b></td><td>103812.10 (+0.15%)</td><td>103685.86 (+0.06%)</td><td>103665.50 (+0.05%)</td><td>103625.90 (+0.02%)</td><td>75.52 <b>(+281.97%)</b></td><td>663.15 (-0.02%)</td><td>662.77 (-0.06%)</td><td>662.90 (-0.05%)</td><td>661.96 (-0.15%)</td><td>0.48 <b>(+281.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103652.50 (n/a)</td><td>103619.86 (n/a)</td><td>103613.60 (n/a)</td><td>103600.60 (n/a)</td><td>19.77 (n/a)</td><td>663.31 (n/a)</td><td>663.19 (n/a)</td><td>663.23 (n/a)</td><td>662.98 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.70 (+0.02%)</td><td>0.69 (-0.02%)</td><td>0.70 (+0.04%)</td><td>0.69 (-0.14%)</td><td>0.00 <b>(+32.18%)</b></td><td>109134.30 (+0.14%)</td><td>108719.56 (+0.02%)</td><td>108526.00 (-0.04%)</td><td>108480.90 (-0.02%)</td><td>305.65 <b>(+32.29%)</b></td><td>633.47 (+0.02%)</td><td>632.08 (-0.02%)</td><td>633.21 (+0.04%)</td><td>629.68 (-0.14%)</td><td>1.77 <b>(+32.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108985.20 (n/a)</td><td>108700.28 (n/a)</td><td>108569.90 (n/a)</td><td>108501.90 (n/a)</td><td>231.05 (n/a)</td><td>633.35 (n/a)</td><td>632.19 (n/a)</td><td>632.95 (n/a)</td><td>630.54 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.04 (-5.52%)</td><td>6.77 (-3.39%)</td><td>6.99 (-2.24%)</td><td>6.34 (-1.64%)</td><td>0.35 <b>(-24.64%)</b></td><td>1405.40 (+1.66%)</td><td>1320.12 (+3.37%)</td><td>1275.80 (+2.29%)</td><td>1266.80 (+5.85%)</td><td>68.96 (-19.19%)</td><td>423.80 (-5.52%)</td><td>407.55 (-3.39%)</td><td>420.81 (-2.24%)</td><td>381.99 (-1.64%)</td><td>20.87 <b>(-24.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.45 (n/a)</td><td>7.00 (n/a)</td><td>7.15 (n/a)</td><td>6.45 (n/a)</td><td>0.46 (n/a)</td><td>1382.40 (n/a)</td><td>1277.12 (n/a)</td><td>1247.20 (n/a)</td><td>1196.80 (n/a)</td><td>85.34 (n/a)</td><td>448.57 (n/a)</td><td>421.85 (n/a)</td><td>430.47 (n/a)</td><td>388.37 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.96 (+3.17%)</td><td>6.69 (+13.54%)</td><td>6.77 (+4.41%)</td><td>6.18 <b>(+28.10%)</b></td><td>0.30 <b>(-68.37%)</b></td><td>1442.80 <b>(-21.93%)</b></td><td>1334.68 (-13.69%)</td><td>1316.10 (-4.22%)</td><td>1280.40 (-3.07%)</td><td>62.53 <b>(-76.12%)</b></td><td>419.30 (+3.17%)</td><td>402.92 (+13.54%)</td><td>407.93 (+4.41%)</td><td>372.11 <b>(+28.10%)</b></td><td>17.96 <b>(-68.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.75 (n/a)</td><td>5.89 (n/a)</td><td>6.49 (n/a)</td><td>4.82 (n/a)</td><td>0.94 (n/a)</td><td>1848.20 (n/a)</td><td>1546.32 (n/a)</td><td>1374.10 (n/a)</td><td>1321.00 (n/a)</td><td>261.83 (n/a)</td><td>406.41 (n/a)</td><td>354.88 (n/a)</td><td>390.72 (n/a)</td><td>290.48 (n/a)</td><td>56.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.96 (-1.71%)</td><td>6.55 (+0.73%)</td><td>6.46 (-1.14%)</td><td>6.32 (+9.93%)</td><td>0.26 <b>(-47.27%)</b></td><td>1410.50 (-9.04%)</td><td>1363.16 (-1.07%)</td><td>1379.30 (+1.16%)</td><td>1281.10 (+1.74%)</td><td>52.59 <b>(-51.73%)</b></td><td>419.08 (-1.71%)</td><td>394.33 (+0.73%)</td><td>389.25 (-1.14%)</td><td>380.62 (+9.93%)</td><td>15.64 <b>(-47.27%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.08 (n/a)</td><td>6.50 (n/a)</td><td>6.54 (n/a)</td><td>5.75 (n/a)</td><td>0.49 (n/a)</td><td>1550.60 (n/a)</td><td>1377.96 (n/a)</td><td>1363.50 (n/a)</td><td>1259.20 (n/a)</td><td>108.93 (n/a)</td><td>426.35 (n/a)</td><td>391.49 (n/a)</td><td>393.75 (n/a)</td><td>346.23 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.32 (+3.91%)</td><td>7.94 (+4.60%)</td><td>7.93 (+6.09%)</td><td>7.57 (+5.66%)</td><td>0.27 <b>(-23.07%)</b></td><td>4604.10 (-5.36%)</td><td>4392.42 (-4.47%)</td><td>4398.80 (-5.74%)</td><td>4188.70 (-3.77%)</td><td>147.44 <b>(-29.53%)</b></td><td>512.68 (+3.91%)</td><td>489.35 (+4.60%)</td><td>488.20 (+6.09%)</td><td>466.43 (+5.66%)</td><td>16.41 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.01 (n/a)</td><td>7.60 (n/a)</td><td>7.47 (n/a)</td><td>7.17 (n/a)</td><td>0.35 (n/a)</td><td>4864.70 (n/a)</td><td>4597.88 (n/a)</td><td>4666.70 (n/a)</td><td>4352.70 (n/a)</td><td>209.23 (n/a)</td><td>493.37 (n/a)</td><td>467.84 (n/a)</td><td>460.17 (n/a)</td><td>441.44 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.84 (-1.78%)</td><td>7.51 (-0.03%)</td><td>7.56 (-0.10%)</td><td>7.04 (+3.10%)</td><td>0.29 <b>(-30.67%)</b></td><td>4954.00 (-3.01%)</td><td>4649.70 (-0.11%)</td><td>4614.70 (+0.10%)</td><td>4446.20 (+1.81%)</td><td>185.96 <b>(-31.86%)</b></td><td>482.99 (-1.78%)</td><td>462.43 (-0.03%)</td><td>465.36 (-0.10%)</td><td>433.48 (+3.10%)</td><td>17.98 <b>(-30.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.98 (n/a)</td><td>7.51 (n/a)</td><td>7.56 (n/a)</td><td>6.83 (n/a)</td><td>0.42 (n/a)</td><td>5107.70 (n/a)</td><td>4654.78 (n/a)</td><td>4610.00 (n/a)</td><td>4367.10 (n/a)</td><td>272.91 (n/a)</td><td>491.74 (n/a)</td><td>462.57 (n/a)</td><td>465.83 (n/a)</td><td>420.44 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.49 (+0.15%)</td><td>7.21 (-1.27%)</td><td>7.31 (-1.51%)</td><td>6.63 (-2.97%)</td><td>0.33 <b>(+23.42%)</b></td><td>5257.90 (+3.06%)</td><td>4846.84 (+1.36%)</td><td>4766.70 (+1.53%)</td><td>4652.30 (-0.15%)</td><td>236.49 <b>(+28.06%)</b></td><td>461.60 (+0.15%)</td><td>443.87 (-1.27%)</td><td>450.52 (-1.51%)</td><td>408.43 (-2.97%)</td><td>20.53 <b>(+23.42%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.48 (n/a)</td><td>7.30 (n/a)</td><td>7.43 (n/a)</td><td>6.83 (n/a)</td><td>0.27 (n/a)</td><td>5101.70 (n/a)</td><td>4781.98 (n/a)</td><td>4694.70 (n/a)</td><td>4659.20 (n/a)</td><td>184.67 (n/a)</td><td>460.92 (n/a)</td><td>449.59 (n/a)</td><td>457.43 (n/a)</td><td>420.93 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.79 (+0.38%)</td><td>0.79 (+0.07%)</td><td>0.79 (-0.13%)</td><td>0.79 (+0.03%)</td><td>0.00 <b>(+116.25%)</b></td><td>95924.50 (-0.03%)</td><td>95739.62 (-0.07%)</td><td>95859.70 (+0.13%)</td><td>95360.30 (-0.38%)</td><td>229.32 <b>(+115.33%)</b></td><td>720.63 (+0.38%)</td><td>717.78 (+0.07%)</td><td>716.88 (-0.13%)</td><td>716.39 (+0.03%)</td><td>1.72 <b>(+116.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95956.50 (n/a)</td><td>95808.52 (n/a)</td><td>95737.30 (n/a)</td><td>95726.80 (n/a)</td><td>106.50 (n/a)</td><td>717.87 (n/a)</td><td>717.26 (n/a)</td><td>717.79 (n/a)</td><td>716.15 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.73 (+0.02%)</td><td>0.73 (+0.07%)</td><td>0.73 (+0.04%)</td><td>0.73 (+0.26%)</td><td>0.00 <b>(-84.49%)</b></td><td>102934.40 (-0.26%)</td><td>102911.24 (-0.07%)</td><td>102900.60 (-0.04%)</td><td>102892.10 (-0.02%)</td><td>19.46 <b>(-84.52%)</b></td><td>667.88 (+0.02%)</td><td>667.75 (+0.07%)</td><td>667.82 (+0.04%)</td><td>667.60 (+0.26%)</td><td>0.13 <b>(-84.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103206.50 (n/a)</td><td>102983.98 (n/a)</td><td>102943.80 (n/a)</td><td>102907.60 (n/a)</td><td>125.70 (n/a)</td><td>667.78 (n/a)</td><td>667.28 (n/a)</td><td>667.54 (n/a)</td><td>665.84 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.70 (+0.07%)</td><td>0.70 (+0.22%)</td><td>0.70 (+0.28%)</td><td>0.70 (+0.17%)</td><td>0.00 (-12.75%)</td><td>108009.10 (-0.16%)</td><td>107656.36 (-0.22%)</td><td>107615.70 (-0.28%)</td><td>107363.90 (-0.07%)</td><td>243.16 (-12.90%)</td><td>640.06 (+0.07%)</td><td>638.33 (+0.22%)</td><td>638.56 (+0.28%)</td><td>636.24 (+0.17%)</td><td>1.44 (-12.75%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108187.50 (n/a)</td><td>107888.88 (n/a)</td><td>107917.10 (n/a)</td><td>107436.60 (n/a)</td><td>279.16 (n/a)</td><td>639.63 (n/a)</td><td>636.95 (n/a)</td><td>636.78 (n/a)</td><td>635.19 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.17 (-1.56%)</td><td>3.67 (-1.84%)</td><td>3.63 (-0.88%)</td><td>3.01 (-12.76%)</td><td>0.43 <b>(+39.55%)</b></td><td>2682.10 (+14.62%)</td><td>2223.84 (+2.56%)</td><td>2218.40 (+0.89%)</td><td>1933.90 (+1.58%)</td><td>282.50 <b>(+66.19%)</b></td><td>1093.10 (-1.56%)</td><td>962.03 (-1.84%)</td><td>952.91 (-0.88%)</td><td>788.15 (-12.76%)</td><td>113.32 <b>(+39.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>4.23 (n/a)</td><td>3.74 (n/a)</td><td>3.67 (n/a)</td><td>3.44 (n/a)</td><td>0.31 (n/a)</td><td>2340.00 (n/a)</td><td>2168.26 (n/a)</td><td>2198.90 (n/a)</td><td>1903.80 (n/a)</td><td>169.99 (n/a)</td><td>1110.39 (n/a)</td><td>980.03 (n/a)</td><td>961.35 (n/a)</td><td>903.39 (n/a)</td><td>81.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 <b>(-31.34%)</b></td><td>0.31 (-12.22%)</td><td>0.31 (-6.51%)</td><td>0.28 (+0.76%)</td><td>0.03 <b>(-68.77%)</b></td><td>4438.30 (-0.75%)</td><td>4023.94 (+10.40%)</td><td>3999.10 (+6.96%)</td><td>3637.70 <b>(+45.65%)</b></td><td>339.48 <b>(-52.44%)</b></td><td>18.45 <b>(-31.34%)</b></td><td>16.77 (-12.22%)</td><td>16.78 (-6.51%)</td><td>15.12 (+0.76%)</td><td>1.41 <b>(-68.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>4471.80 (n/a)</td><td>3644.96 (n/a)</td><td>3738.80 (n/a)</td><td>2497.50 (n/a)</td><td>713.75 (n/a)</td><td>26.87 (n/a)</td><td>19.11 (n/a)</td><td>17.95 (n/a)</td><td>15.01 (n/a)</td><td>4.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>6.57 (+2.00%)</td><td>5.02 (+2.29%)</td><td>4.82 (+1.07%)</td><td>3.97 (+5.73%)</td><td>0.95 (-1.61%)</td><td>1674.10 (-5.41%)</td><td>1360.36 (-2.54%)</td><td>1380.20 (-1.05%)</td><td>1012.90 (-1.96%)</td><td>236.12 (-9.69%)</td><td>2028.98 (+2.00%)</td><td>1550.94 (+2.29%)</td><td>1489.11 (+1.07%)</td><td>1227.67 (+5.73%)</td><td>293.78 (-1.61%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.44 (n/a)</td><td>4.91 (n/a)</td><td>4.77 (n/a)</td><td>3.76 (n/a)</td><td>0.97 (n/a)</td><td>1769.90 (n/a)</td><td>1395.84 (n/a)</td><td>1394.90 (n/a)</td><td>1033.20 (n/a)</td><td>261.46 (n/a)</td><td>1989.16 (n/a)</td><td>1516.21 (n/a)</td><td>1473.41 (n/a)</td><td>1161.18 (n/a)</td><td>298.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.48 (n/a)</td><td>13.21 (n/a)</td><td>13.38 (n/a)</td><td>12.82 (n/a)</td><td>0.29 (n/a)</td><td>13.47 (n/a)</td><td>13.20 (n/a)</td><td>13.37 (n/a)</td><td>12.82 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>24.87 (+0.80%)</td><td>24.25 (+1.66%)</td><td>24.61 (+2.07%)</td><td>23.28 (+3.66%)</td><td>0.66 <b>(-22.17%)</b></td><td>24.86 (+0.80%)</td><td>24.24 (+1.66%)</td><td>24.59 (+2.07%)</td><td>23.26 (+3.66%)</td><td>0.66 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>24.68 (n/a)</td><td>23.86 (n/a)</td><td>24.11 (n/a)</td><td>22.45 (n/a)</td><td>0.85 (n/a)</td><td>24.66 (n/a)</td><td>23.84 (n/a)</td><td>24.09 (n/a)</td><td>22.44 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>43.41 (+5.37%)</td><td>41.40 (+3.83%)</td><td>41.81 (+4.49%)</td><td>39.16 (+1.57%)</td><td>1.90 <b>(+91.79%)</b></td><td>43.38 (+5.37%)</td><td>41.38 (+3.83%)</td><td>41.78 (+4.49%)</td><td>39.13 (+1.57%)</td><td>1.90 <b>(+91.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>41.20 (n/a)</td><td>39.87 (n/a)</td><td>40.01 (n/a)</td><td>38.55 (n/a)</td><td>0.99 (n/a)</td><td>41.17 (n/a)</td><td>39.85 (n/a)</td><td>39.99 (n/a)</td><td>38.53 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>45.46 (+2.81%)</td><td>43.45 (+2.57%)</td><td>42.88 (+2.41%)</td><td>41.84 (+4.71%)</td><td>1.73 (-0.95%)</td><td>45.43 (+2.81%)</td><td>43.42 (+2.57%)</td><td>42.86 (+2.41%)</td><td>41.82 (+4.71%)</td><td>1.73 (-0.95%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>44.21 (n/a)</td><td>42.36 (n/a)</td><td>41.87 (n/a)</td><td>39.96 (n/a)</td><td>1.75 (n/a)</td><td>44.19 (n/a)</td><td>42.33 (n/a)</td><td>41.85 (n/a)</td><td>39.94 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.39 (n/a)</td><td>12.77 (n/a)</td><td>13.15 (n/a)</td><td>11.08 (n/a)</td><td>0.97 (n/a)</td><td>13.39 (n/a)</td><td>12.77 (n/a)</td><td>13.14 (n/a)</td><td>11.07 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>25.13 (+0.47%)</td><td>24.41 (+3.94%)</td><td>24.21 (+0.76%)</td><td>23.83 (+18.78%)</td><td>0.51 <b>(-74.25%)</b></td><td>25.11 (+0.47%)</td><td>24.40 (+3.94%)</td><td>24.20 (+0.76%)</td><td>23.81 (+18.78%)</td><td>0.51 <b>(-74.25%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>25.01 (n/a)</td><td>23.49 (n/a)</td><td>24.03 (n/a)</td><td>20.06 (n/a)</td><td>1.96 (n/a)</td><td>24.99 (n/a)</td><td>23.48 (n/a)</td><td>24.02 (n/a)</td><td>20.05 (n/a)</td><td>1.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>42.81 (+8.67%)</td><td>40.10 (+12.99%)</td><td>39.89 (+4.99%)</td><td>38.50 <b>(+27.20%)</b></td><td>1.65 <b>(-64.63%)</b></td><td>42.79 (+8.67%)</td><td>40.07 (+12.99%)</td><td>39.87 (+4.99%)</td><td>38.48 <b>(+27.20%)</b></td><td>1.65 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>39.39 (n/a)</td><td>35.49 (n/a)</td><td>38.00 (n/a)</td><td>30.27 (n/a)</td><td>4.66 (n/a)</td><td>39.37 (n/a)</td><td>35.46 (n/a)</td><td>37.97 (n/a)</td><td>30.25 (n/a)</td><td>4.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>45.60 (+2.97%)</td><td>44.63 (+4.92%)</td><td>44.94 (+4.88%)</td><td>42.48 (+5.76%)</td><td>1.28 <b>(-23.79%)</b></td><td>45.57 (+2.97%)</td><td>44.61 (+4.92%)</td><td>44.92 (+4.88%)</td><td>42.45 (+5.76%)</td><td>1.28 <b>(-23.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>44.29 (n/a)</td><td>42.54 (n/a)</td><td>42.85 (n/a)</td><td>40.17 (n/a)</td><td>1.68 (n/a)</td><td>44.26 (n/a)</td><td>42.52 (n/a)</td><td>42.83 (n/a)</td><td>40.14 (n/a)</td><td>1.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.45 (+12.47%)</td><td>8.76 (-4.34%)</td><td>8.34 (-9.19%)</td><td>7.54 (-15.58%)</td><td>1.17 <b>(+660.98%)</b></td><td>10.43 (+12.47%)</td><td>8.74 (-4.34%)</td><td>8.32 (-9.19%)</td><td>7.53 (-15.58%)</td><td>1.17 <b>(+660.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.29 (n/a)</td><td>9.15 (n/a)</td><td>9.18 (n/a)</td><td>8.93 (n/a)</td><td>0.15 (n/a)</td><td>9.27 (n/a)</td><td>9.14 (n/a)</td><td>9.16 (n/a)</td><td>8.91 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.87 (-4.07%)</td><td>0.79 (-4.88%)</td><td>0.78 (-3.43%)</td><td>0.73 (-7.23%)</td><td>0.06 (+16.37%)</td><td>0.86 (-4.07%)</td><td>0.77 (-4.88%)</td><td>0.77 (-3.43%)</td><td>0.72 (-7.23%)</td><td>0.06 (+16.37%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td><td>0.89 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.29 (+0.96%)</td><td>1.13 (+3.59%)</td><td>1.22 (+12.52%)</td><td>0.87 (-3.10%)</td><td>0.18 (+8.96%)</td><td>1.27 (+0.96%)</td><td>1.12 (+3.59%)</td><td>1.21 (+12.52%)</td><td>0.86 (-3.10%)</td><td>0.18 (+8.96%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.28 (n/a)</td><td>1.09 (n/a)</td><td>1.08 (n/a)</td><td>0.90 (n/a)</td><td>0.17 (n/a)</td><td>1.26 (n/a)</td><td>1.08 (n/a)</td><td>1.07 (n/a)</td><td>0.89 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>15.89 (-1.23%)</td><td>15.04 (+1.66%)</td><td>14.96 (-3.44%)</td><td>14.47 (+17.41%)</td><td>0.59 <b>(-61.69%)</b></td><td>15.70 (-1.23%)</td><td>14.87 (+1.66%)</td><td>14.78 (-3.44%)</td><td>14.30 (+17.41%)</td><td>0.59 <b>(-61.69%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>16.08 (n/a)</td><td>14.79 (n/a)</td><td>15.49 (n/a)</td><td>12.32 (n/a)</td><td>1.55 (n/a)</td><td>15.90 (n/a)</td><td>14.62 (n/a)</td><td>15.31 (n/a)</td><td>12.18 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.02 (+1.02%)</td><td>10.76 (-5.64%)</td><td>11.82 (+1.60%)</td><td>7.75 <b>(-24.09%)</b></td><td>1.83 <b>(+164.21%)</b></td><td>11.81 (+1.02%)</td><td>10.57 (-5.64%)</td><td>11.61 (+1.60%)</td><td>7.62 <b>(-24.09%)</b></td><td>1.80 <b>(+164.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>11.90 (n/a)</td><td>11.40 (n/a)</td><td>11.63 (n/a)</td><td>10.21 (n/a)</td><td>0.69 (n/a)</td><td>11.69 (n/a)</td><td>11.20 (n/a)</td><td>11.43 (n/a)</td><td>10.04 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.91 <b>(+24.37%)</b></td><td>8.18 (+1.42%)</td><td>7.44 (-7.35%)</td><td>7.23 (+2.83%)</td><td>1.55 <b>(+110.89%)</b></td><td>10.72 <b>(+24.37%)</b></td><td>8.03 (+1.42%)</td><td>7.31 (-7.35%)</td><td>7.10 (+2.83%)</td><td>1.52 <b>(+110.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.77 (n/a)</td><td>8.06 (n/a)</td><td>8.03 (n/a)</td><td>7.03 (n/a)</td><td>0.73 (n/a)</td><td>8.62 (n/a)</td><td>7.92 (n/a)</td><td>7.89 (n/a)</td><td>6.90 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>7.20 (+11.94%)</td><td>6.02 (+4.78%)</td><td>5.95 (+3.64%)</td><td>4.91 (-5.29%)</td><td>0.84 <b>(+83.88%)</b></td><td>7.08 (+11.94%)</td><td>5.93 (+4.78%)</td><td>5.86 (+3.64%)</td><td>4.83 (-5.29%)</td><td>0.82 <b>(+83.88%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.43 (n/a)</td><td>5.75 (n/a)</td><td>5.74 (n/a)</td><td>5.18 (n/a)</td><td>0.46 (n/a)</td><td>6.33 (n/a)</td><td>5.66 (n/a)</td><td>5.65 (n/a)</td><td>5.10 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.14 (n/a)</td><td>12.22 (n/a)</td><td>12.31 (n/a)</td><td>11.08 (n/a)</td><td>0.75 (n/a)</td><td>13.13 (n/a)</td><td>12.21 (n/a)</td><td>12.30 (n/a)</td><td>11.07 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.47 (n/a)</td><td>12.96 (n/a)</td><td>13.19 (n/a)</td><td>12.24 (n/a)</td><td>0.49 (n/a)</td><td>13.46 (n/a)</td><td>12.95 (n/a)</td><td>13.18 (n/a)</td><td>12.23 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>166.86 (n/a)</td><td>162.50 (n/a)</td><td>130.60 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>337.20 (n/a)</td><td>187.86 (n/a)</td><td>173.80 (n/a)</td><td>125.90 (n/a)</td><td>86.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>158.98 (n/a)</td><td>159.20 (n/a)</td><td>102.90 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>179.22 (n/a)</td><td>194.20 (n/a)</td><td>115.40 (n/a)</td><td>47.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>174.36 (n/a)</td><td>168.80 (n/a)</td><td>148.30 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>181.56 (n/a)</td><td>182.30 (n/a)</td><td>170.40 (n/a)</td><td>11.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>184.64 (n/a)</td><td>188.80 (n/a)</td><td>153.20 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>328.60 (n/a)</td><td>246.14 (n/a)</td><td>233.70 (n/a)</td><td>197.30 (n/a)</td><td>49.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>186.04 (n/a)</td><td>192.30 (n/a)</td><td>146.50 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>189.24 (n/a)</td><td>190.60 (n/a)</td><td>160.30 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>175.56 (n/a)</td><td>175.40 (n/a)</td><td>126.40 (n/a)</td><td>36.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>163.44 (n/a)</td><td>167.70 (n/a)</td><td>124.40 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>160.20 (n/a)</td><td>165.50 (n/a)</td><td>132.70 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>217.52 (n/a)</td><td>219.90 (n/a)</td><td>168.40 (n/a)</td><td>31.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>183.12 (n/a)</td><td>195.10 (n/a)</td><td>132.60 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>370.80 (n/a)</td><td>247.64 (n/a)</td><td>225.80 (n/a)</td><td>202.30 (n/a)</td><td>69.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.90 (n/a)</td><td>155.52 (n/a)</td><td>160.10 (n/a)</td><td>136.20 (n/a)</td><td>14.18 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>160.18 (n/a)</td><td>162.00 (n/a)</td><td>144.00 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.10 (n/a)</td><td>173.70 (n/a)</td><td>171.50 (n/a)</td><td>127.50 (n/a)</td><td>39.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>169.96 (n/a)</td><td>172.80 (n/a)</td><td>138.00 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>174.36 (n/a)</td><td>169.70 (n/a)</td><td>128.50 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>263.00 (n/a)</td><td>189.72 (n/a)</td><td>171.00 (n/a)</td><td>169.50 (n/a)</td><td>41.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>194.90 (n/a)</td><td>194.90 (n/a)</td><td>164.70 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>208.34 (n/a)</td><td>205.20 (n/a)</td><td>177.50 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.40 (n/a)</td><td>178.88 (n/a)</td><td>165.90 (n/a)</td><td>151.00 (n/a)</td><td>32.35 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>196.60 (n/a)</td><td>196.00 (n/a)</td><td>168.20 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>308.90 (n/a)</td><td>178.82 (n/a)</td><td>141.50 (n/a)</td><td>131.10 (n/a)</td><td>75.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>176.80 (n/a)</td><td>157.12 (n/a)</td><td>165.30 (n/a)</td><td>129.10 (n/a)</td><td>19.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>234.10 (n/a)</td><td>192.12 (n/a)</td><td>192.10 (n/a)</td><td>129.10 (n/a)</td><td>41.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>246.00 (n/a)</td><td>179.48 (n/a)</td><td>179.00 (n/a)</td><td>133.70 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.60 (n/a)</td><td>182.12 (n/a)</td><td>193.60 (n/a)</td><td>138.30 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>202.68 (n/a)</td><td>195.90 (n/a)</td><td>170.20 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-10.88%)</td><td>0.02 (+3.47%)</td><td>0.02 (+2.65%)</td><td>0.02 <b>(+32.40%)</b></td><td>0.00 <b>(-54.24%)</b></td><td>181.00 <b>(-24.49%)</b></td><td>167.94 (-6.48%)</td><td>173.60 (-2.58%)</td><td>142.70 (+12.19%)</td><td>15.58 <b>(-61.13%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>179.58 (n/a)</td><td>178.20 (n/a)</td><td>127.20 (n/a)</td><td>40.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-5.37%)</td><td>0.03 (+2.73%)</td><td>0.03 (+7.95%)</td><td>0.02 <b>(+21.19%)</b></td><td>0.00 <b>(-47.75%)</b></td><td>183.40 (-17.46%)</td><td>158.68 (-4.94%)</td><td>152.20 (-7.42%)</td><td>142.10 (+5.73%)</td><td>16.02 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>166.92 (n/a)</td><td>164.40 (n/a)</td><td>134.40 (n/a)</td><td>34.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-5.95%)</td><td>0.03 (+4.49%)</td><td>0.03 (+0.94%)</td><td>0.02 (+19.20%)</td><td>0.00 <b>(-43.09%)</b></td><td>175.40 (-16.12%)</td><td>155.18 (-7.18%)</td><td>163.60 (-0.91%)</td><td>132.90 (+6.32%)</td><td>18.94 <b>(-50.42%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>167.18 (n/a)</td><td>165.10 (n/a)</td><td>125.00 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(-22.31%)</b></td><td>0.02 (-10.06%)</td><td>0.03 (-0.03%)</td><td>0.02 (-6.16%)</td><td>0.00 <b>(-39.30%)</b></td><td>210.40 (+6.59%)</td><td>174.74 (+9.69%)</td><td>160.60 (+0.06%)</td><td>157.00 <b>(+28.69%)</b></td><td>23.92 (-17.59%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>159.30 (n/a)</td><td>160.50 (n/a)</td><td>122.00 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-4.51%)</td><td>0.02 (-8.20%)</td><td>0.02 (-8.84%)</td><td>0.02 (+1.21%)</td><td>0.00 (-15.03%)</td><td>231.60 (-1.15%)</td><td>193.76 (+8.27%)</td><td>187.70 (+9.70%)</td><td>157.70 (+4.71%)</td><td>28.94 (-12.89%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>178.96 (n/a)</td><td>171.10 (n/a)</td><td>150.60 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-18.00%)</td><td>0.02 (-14.59%)</td><td>0.02 (-6.15%)</td><td>0.01 <b>(-34.88%)</b></td><td>0.00 (+7.20%)</td><td>337.00 <b>(+53.60%)</b></td><td>227.14 <b>(+20.56%)</b></td><td>215.30 (+6.53%)</td><td>172.60 <b>(+21.98%)</b></td><td>65.18 <b>(+107.62%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>188.40 (n/a)</td><td>202.10 (n/a)</td><td>141.50 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 <b>(-32.27%)</b></td><td>0.02 (-18.42%)</td><td>0.02 (-10.40%)</td><td>0.02 (-13.44%)</td><td>0.00 <b>(-61.54%)</b></td><td>233.10 (+15.57%)</td><td>207.62 <b>(+20.15%)</b></td><td>200.40 (+11.58%)</td><td>186.40 <b>(+47.70%)</b></td><td>19.85 <b>(-32.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>172.80 (n/a)</td><td>179.60 (n/a)</td><td>126.20 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-3.99%)</td><td>0.02 <b>(-22.71%)</b></td><td>0.02 (-13.56%)</td><td>0.01 <b>(-42.51%)</b></td><td>0.00 <b>(+187.82%)</b></td><td>381.80 <b>(+73.94%)</b></td><td>272.88 <b>(+39.31%)</b></td><td>227.60 (+15.65%)</td><td>182.70 (+4.16%)</td><td>87.21 <b>(+442.07%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>195.88 (n/a)</td><td>196.80 (n/a)</td><td>175.40 (n/a)</td><td>16.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (-4.38%)</td><td>0.04 (+0.65%)</td><td>0.05 (+8.55%)</td><td>0.04 (-3.19%)</td><td>0.00 <b>(-22.91%)</b></td><td>219.10 (+3.30%)</td><td>184.00 (-1.13%)</td><td>174.30 (-7.88%)</td><td>168.40 (+4.60%)</td><td>20.81 (-14.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>186.10 (n/a)</td><td>189.20 (n/a)</td><td>161.00 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+33.18%)</b></td><td>0.05 (+6.19%)</td><td>0.05 (+2.12%)</td><td>0.04 (-9.28%)</td><td>0.01 <b>(+259.12%)</b></td><td>206.50 (+10.25%)</td><td>168.02 (-3.21%)</td><td>172.70 (-2.10%)</td><td>121.30 <b>(-24.94%)</b></td><td>30.90 <b>(+190.73%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>173.60 (n/a)</td><td>176.40 (n/a)</td><td>161.60 (n/a)</td><td>10.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+40.02%)</b></td><td>0.05 (+16.87%)</td><td>0.05 (+7.82%)</td><td>0.05 (+7.83%)</td><td>0.01 <b>(+175.58%)</b></td><td>179.50 (-7.28%)</td><td>155.96 (-13.26%)</td><td>160.40 (-7.28%)</td><td>120.70 <b>(-28.58%)</b></td><td>21.53 <b>(+74.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>179.80 (n/a)</td><td>173.00 (n/a)</td><td>169.00 (n/a)</td><td>12.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (+1.78%)</td><td>0.05 (+1.76%)</td><td>0.05 (-0.41%)</td><td>0.05 (+10.39%)</td><td>0.01 (-8.51%)</td><td>172.10 (-9.42%)</td><td>162.76 (-1.99%)</td><td>168.90 (+0.42%)</td><td>135.60 (-1.74%)</td><td>15.32 (-18.20%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>166.06 (n/a)</td><td>168.20 (n/a)</td><td>138.00 (n/a)</td><td>18.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 <b>(-23.19%)</b></td><td>0.04 <b>(-20.21%)</b></td><td>0.04 (-11.32%)</td><td>0.03 <b>(-41.89%)</b></td><td>0.01 (+5.78%)</td><td>307.80 <b>(+72.15%)</b></td><td>202.30 <b>(+29.51%)</b></td><td>185.50 (+12.77%)</td><td>159.70 <b>(+30.15%)</b></td><td>60.06 <b>(+146.86%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>156.20 (n/a)</td><td>164.50 (n/a)</td><td>122.70 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (-7.34%)</td><td>0.05 (-3.31%)</td><td>0.04 (-4.48%)</td><td>0.04 (+2.96%)</td><td>0.00 <b>(-26.79%)</b></td><td>194.20 (-2.85%)</td><td>178.98 (+2.91%)</td><td>182.40 (+4.65%)</td><td>153.60 (+7.94%)</td><td>16.07 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>173.92 (n/a)</td><td>174.30 (n/a)</td><td>142.30 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 <b>(+21.42%)</b></td><td>0.05 (+19.72%)</td><td>0.05 <b>(+24.37%)</b></td><td>0.04 (+15.96%)</td><td>0.01 <b>(+24.46%)</b></td><td>203.30 (-13.75%)</td><td>167.98 (-16.34%)</td><td>154.10 (-19.57%)</td><td>143.50 (-17.67%)</td><td>25.50 (-10.80%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>200.78 (n/a)</td><td>191.60 (n/a)</td><td>174.30 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+29.95%)</b></td><td>0.05 (+12.93%)</td><td>0.05 (+16.80%)</td><td>0.03 (+1.46%)</td><td>0.01 <b>(+74.48%)</b></td><td>236.20 (-1.42%)</td><td>175.42 (-8.82%)</td><td>157.20 (-14.38%)</td><td>124.00 <b>(-23.03%)</b></td><td>44.85 <b>(+35.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>192.38 (n/a)</td><td>183.60 (n/a)</td><td>161.10 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+32.02%)</b></td><td>0.05 (+7.02%)</td><td>0.05 (+6.44%)</td><td>0.04 (-2.44%)</td><td>0.01 <b>(+148.82%)</b></td><td>220.50 (+2.51%)</td><td>174.20 (-3.10%)</td><td>163.10 (-6.05%)</td><td>121.70 <b>(-24.27%)</b></td><td>40.70 <b>(+94.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>179.78 (n/a)</td><td>173.60 (n/a)</td><td>160.70 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 <b>(+32.99%)</b></td><td>0.04 (+2.19%)</td><td>0.04 (-1.07%)</td><td>0.02 <b>(-40.80%)</b></td><td>0.01 <b>(+478.78%)</b></td><td>385.20 <b>(+68.95%)</b></td><td>231.04 (+8.46%)</td><td>219.80 (+1.06%)</td><td>148.00 <b>(-24.83%)</b></td><td>92.49 <b>(+661.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.00 (n/a)</td><td>213.02 (n/a)</td><td>217.50 (n/a)</td><td>196.90 (n/a)</td><td>12.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (+12.14%)</td><td>0.10 (+1.33%)</td><td>0.10 (+1.52%)</td><td>0.08 (-2.29%)</td><td>0.02 <b>(+45.48%)</b></td><td>204.40 (+2.35%)</td><td>168.62 (+0.43%)</td><td>169.80 (-1.45%)</td><td>127.60 (-10.83%)</td><td>34.22 <b>(+39.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>167.90 (n/a)</td><td>172.30 (n/a)</td><td>143.10 (n/a)</td><td>24.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-16.46%)</td><td>0.09 (-4.65%)</td><td>0.09 (-3.56%)</td><td>0.08 (+0.40%)</td><td>0.01 <b>(-34.08%)</b></td><td>209.80 (-0.43%)</td><td>177.46 (+3.50%)</td><td>176.60 (+3.70%)</td><td>151.20 (+19.71%)</td><td>24.50 <b>(-20.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>171.46 (n/a)</td><td>170.30 (n/a)</td><td>126.30 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (+6.68%)</td><td>0.11 (+5.09%)</td><td>0.10 (+12.12%)</td><td>0.08 (-3.25%)</td><td>0.03 (+15.64%)</td><td>205.70 (+3.37%)</td><td>163.18 (-3.75%)</td><td>165.10 (-10.80%)</td><td>106.70 (-6.24%)</td><td>37.97 (+13.05%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>169.54 (n/a)</td><td>185.10 (n/a)</td><td>113.80 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (+6.29%)</td><td>0.09 (+1.30%)</td><td>0.09 (-1.53%)</td><td>0.07 (-5.03%)</td><td>0.01 (+11.00%)</td><td>221.00 (+5.29%)</td><td>178.36 (-0.97%)</td><td>173.40 (+1.58%)</td><td>150.00 (-5.90%)</td><td>26.40 (+12.76%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>180.10 (n/a)</td><td>170.70 (n/a)</td><td>159.40 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 <b>(+25.68%)</b></td><td>0.11 <b>(+21.62%)</b></td><td>0.12 <b>(+28.09%)</b></td><td>0.07 (-0.07%)</td><td>0.02 <b>(+49.35%)</b></td><td>224.90 (+0.04%)</td><td>157.44 (-16.25%)</td><td>141.00 <b>(-21.97%)</b></td><td>123.60 <b>(-20.46%)</b></td><td>39.81 <b>(+22.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>187.98 (n/a)</td><td>180.70 (n/a)</td><td>155.40 (n/a)</td><td>32.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 <b>(+21.56%)</b></td><td>0.09 (+11.91%)</td><td>0.09 (+15.33%)</td><td>0.07 (+12.47%)</td><td>0.02 <b>(+28.42%)</b></td><td>222.50 (-11.07%)</td><td>183.48 (-10.14%)</td><td>186.80 (-13.28%)</td><td>130.20 (-17.70%)</td><td>35.33 (-6.54%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>250.20 (n/a)</td><td>204.18 (n/a)</td><td>215.40 (n/a)</td><td>158.20 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (+14.61%)</td><td>0.10 (+11.73%)</td><td>0.09 (+12.56%)</td><td>0.08 (+16.07%)</td><td>0.01 (+4.48%)</td><td>198.90 (-13.82%)</td><td>174.80 (-10.84%)</td><td>175.30 (-11.15%)</td><td>137.90 (-12.78%)</td><td>24.42 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>196.06 (n/a)</td><td>197.30 (n/a)</td><td>158.10 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 (-9.27%)</td><td>0.07 (-12.11%)</td><td>0.07 (-2.08%)</td><td>0.04 <b>(-36.56%)</b></td><td>0.02 <b>(+86.92%)</b></td><td>383.20 <b>(+57.63%)</b></td><td>254.38 (+19.24%)</td><td>219.50 (+2.14%)</td><td>199.60 (+10.22%)</td><td>75.58 <b>(+234.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>213.34 (n/a)</td><td>214.90 (n/a)</td><td>181.10 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (-7.19%)</td><td>0.17 (-0.97%)</td><td>0.17 (+1.39%)</td><td>0.14 (+0.45%)</td><td>0.02 <b>(-32.13%)</b></td><td>233.80 (-0.43%)</td><td>196.30 (-0.11%)</td><td>187.80 (-1.37%)</td><td>174.20 (+7.80%)</td><td>23.78 <b>(-27.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>234.80 (n/a)</td><td>196.52 (n/a)</td><td>190.40 (n/a)</td><td>161.60 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 <b>(+58.96%)</b></td><td>0.21 <b>(+32.32%)</b></td><td>0.22 <b>(+31.89%)</b></td><td>0.15 (+8.63%)</td><td>0.06 <b>(+208.46%)</b></td><td>220.80 (-7.96%)</td><td>167.54 (-19.98%)</td><td>151.90 <b>(-24.20%)</b></td><td>115.80 <b>(-37.10%)</b></td><td>49.59 <b>(+86.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>209.38 (n/a)</td><td>200.40 (n/a)</td><td>184.10 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (+9.62%)</td><td>0.18 (+13.03%)</td><td>0.19 (+15.67%)</td><td>0.15 <b>(+30.68%)</b></td><td>0.03 (-1.38%)</td><td>225.40 <b>(-23.46%)</b></td><td>185.96 (-12.53%)</td><td>174.00 (-13.56%)</td><td>153.30 (-8.75%)</td><td>31.83 <b>(-33.51%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>294.50 (n/a)</td><td>212.60 (n/a)</td><td>201.30 (n/a)</td><td>168.00 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (-7.50%)</td><td>0.17 (-1.25%)</td><td>0.18 (+4.42%)</td><td>0.13 (-16.70%)</td><td>0.03 (+10.00%)</td><td>259.40 <b>(+20.04%)</b></td><td>193.66 (+2.38%)</td><td>186.40 (-4.21%)</td><td>159.10 (+8.08%)</td><td>39.06 <b>(+50.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.10 (n/a)</td><td>189.16 (n/a)</td><td>194.60 (n/a)</td><td>147.20 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (+10.02%)</td><td>0.17 (+4.00%)</td><td>0.16 (+0.61%)</td><td>0.13 (-3.44%)</td><td>0.03 <b>(+60.77%)</b></td><td>249.00 (+3.58%)</td><td>202.08 (-2.37%)</td><td>200.80 (-0.59%)</td><td>161.80 (-9.10%)</td><td>36.51 <b>(+49.59%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>240.40 (n/a)</td><td>206.98 (n/a)</td><td>202.00 (n/a)</td><td>178.00 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (+3.62%)</td><td>0.16 (+7.11%)</td><td>0.17 (+7.10%)</td><td>0.13 <b>(+41.09%)</b></td><td>0.03 <b>(-24.15%)</b></td><td>254.00 <b>(-29.13%)</b></td><td>206.50 (-10.08%)</td><td>188.40 (-6.64%)</td><td>170.50 (-3.45%)</td><td>36.24 <b>(-50.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>358.40 (n/a)</td><td>229.64 (n/a)</td><td>201.80 (n/a)</td><td>176.60 (n/a)</td><td>73.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (+4.51%)</td><td>0.15 (-1.52%)</td><td>0.14 (-3.71%)</td><td>0.14 (-2.23%)</td><td>0.02 <b>(+45.00%)</b></td><td>238.00 (+2.28%)</td><td>224.12 (+1.97%)</td><td>231.30 (+3.86%)</td><td>186.80 (-4.30%)</td><td>21.38 <b>(+40.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>219.78 (n/a)</td><td>222.70 (n/a)</td><td>195.20 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-15.26%)</td><td>0.03 (-12.06%)</td><td>0.03 (-11.55%)</td><td>0.02 (-12.93%)</td><td>0.00 (-19.46%)</td><td>187.30 (+14.84%)</td><td>162.68 (+13.62%)</td><td>155.60 (+13.08%)</td><td>152.30 (+17.97%)</td><td>14.54 (+8.79%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>163.10 (n/a)</td><td>143.18 (n/a)</td><td>137.60 (n/a)</td><td>129.10 (n/a)</td><td>13.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-2.55%)</td><td>0.02 (-11.37%)</td><td>0.02 (-12.66%)</td><td>0.02 (-19.44%)</td><td>0.01 <b>(+27.11%)</b></td><td>238.30 <b>(+24.18%)</b></td><td>173.16 (+15.87%)</td><td>166.80 (+14.48%)</td><td>120.80 (+2.63%)</td><td>45.00 <b>(+61.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>149.44 (n/a)</td><td>145.70 (n/a)</td><td>117.70 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (+5.61%)</td><td>0.02 (+10.53%)</td><td>0.02 (+8.04%)</td><td>0.02 <b>(+46.21%)</b></td><td>0.00 <b>(-42.51%)</b></td><td>230.30 <b>(-31.60%)</b></td><td>201.84 (-12.80%)</td><td>206.40 (-7.44%)</td><td>170.60 (-5.33%)</td><td>21.99 <b>(-64.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>336.70 (n/a)</td><td>231.46 (n/a)</td><td>223.00 (n/a)</td><td>180.20 (n/a)</td><td>61.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-8.12%)</td><td>0.02 (-14.98%)</td><td>0.02 (-15.26%)</td><td>0.01 (-13.56%)</td><td>0.00 (+15.70%)</td><td>274.90 (+15.70%)</td><td>223.56 (+19.74%)</td><td>216.80 (+18.02%)</td><td>158.00 (+8.89%)</td><td>49.57 <b>(+49.06%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.60 (n/a)</td><td>186.70 (n/a)</td><td>183.70 (n/a)</td><td>145.10 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 <b>(+35.93%)</b></td><td>0.03 <b>(+20.48%)</b></td><td>0.03 (+14.69%)</td><td>0.02 <b>(+46.36%)</b></td><td>0.01 <b>(+22.17%)</b></td><td>167.80 <b>(-31.65%)</b></td><td>139.16 (-18.01%)</td><td>139.30 (-12.83%)</td><td>98.00 <b>(-26.43%)</b></td><td>27.43 <b>(-39.58%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>169.72 (n/a)</td><td>159.80 (n/a)</td><td>133.20 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+19.70%)</td><td>0.03 (+6.37%)</td><td>0.03 (+3.27%)</td><td>0.02 (+5.04%)</td><td>0.01 <b>(+25.35%)</b></td><td>179.10 (-4.78%)</td><td>148.98 (-5.47%)</td><td>146.00 (-3.18%)</td><td>109.80 (-16.50%)</td><td>27.49 (-0.35%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>157.60 (n/a)</td><td>150.80 (n/a)</td><td>131.50 (n/a)</td><td>27.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-4.36%)</td><td>0.02 (-13.90%)</td><td>0.02 (-10.62%)</td><td>0.02 <b>(-20.16%)</b></td><td>0.00 <b>(+32.59%)</b></td><td>243.40 <b>(+25.27%)</b></td><td>191.70 (+18.49%)</td><td>180.50 (+11.90%)</td><td>146.90 (+4.56%)</td><td>40.35 <b>(+79.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>161.78 (n/a)</td><td>161.30 (n/a)</td><td>140.50 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-15.79%)</td><td>0.02 (-2.29%)</td><td>0.02 (+2.40%)</td><td>0.02 (+17.11%)</td><td>0.00 <b>(-56.33%)</b></td><td>189.00 (-14.60%)</td><td>174.40 (-1.56%)</td><td>183.80 (-2.34%)</td><td>145.50 (+18.68%)</td><td>18.32 <b>(-55.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>177.16 (n/a)</td><td>188.20 (n/a)</td><td>122.60 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+8.64%)</td><td>0.02 (-1.99%)</td><td>0.02 (-19.70%)</td><td>0.02 (+5.86%)</td><td>0.01 (+7.88%)</td><td>207.70 (-5.55%)</td><td>173.22 (+2.05%)</td><td>194.70 <b>(+24.57%)</b></td><td>118.10 (-7.95%)</td><td>38.56 (-6.79%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>169.74 (n/a)</td><td>156.30 (n/a)</td><td>128.30 (n/a)</td><td>41.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+11.36%)</td><td>0.03 (+6.35%)</td><td>0.02 (-1.86%)</td><td>0.02 (+4.30%)</td><td>0.01 <b>(+38.70%)</b></td><td>200.40 (-4.11%)</td><td>167.66 (-4.39%)</td><td>183.80 (+1.88%)</td><td>117.60 (-10.23%)</td><td>34.97 <b>(+24.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>175.36 (n/a)</td><td>180.40 (n/a)</td><td>131.00 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(+24.42%)</b></td><td>0.02 (+1.76%)</td><td>0.02 (-3.59%)</td><td>0.02 (+10.33%)</td><td>0.01 <b>(+42.23%)</b></td><td>214.10 (-9.39%)</td><td>173.76 (-0.77%)</td><td>174.30 (+3.69%)</td><td>120.40 (-19.63%)</td><td>34.39 (-2.53%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>175.10 (n/a)</td><td>168.10 (n/a)</td><td>149.80 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-6.50%)</td><td>0.03 <b>(+28.82%)</b></td><td>0.03 <b>(+45.52%)</b></td><td>0.02 <b>(+61.76%)</b></td><td>0.01 <b>(-27.66%)</b></td><td>212.20 <b>(-38.17%)</b></td><td>149.46 <b>(-28.34%)</b></td><td>128.30 <b>(-31.32%)</b></td><td>120.60 (+6.91%)</td><td>39.52 <b>(-53.46%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>343.20 (n/a)</td><td>208.56 (n/a)</td><td>186.80 (n/a)</td><td>112.80 (n/a)</td><td>84.92 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(+41.02%)</b></td><td>0.03 <b>(+44.24%)</b></td><td>0.03 <b>(+44.92%)</b></td><td>0.02 (+10.81%)</td><td>0.01 <b>(+69.17%)</b></td><td>257.50 (-9.78%)</td><td>165.48 <b>(-28.81%)</b></td><td>145.20 <b>(-31.02%)</b></td><td>131.50 <b>(-29.07%)</b></td><td>51.93 (+10.23%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>285.40 (n/a)</td><td>232.46 (n/a)</td><td>210.50 (n/a)</td><td>185.40 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-2.51%)</td><td>0.02 (-0.71%)</td><td>0.03 (+3.65%)</td><td>0.02 (-13.28%)</td><td>0.00 <b>(+24.28%)</b></td><td>218.80 (+15.34%)</td><td>170.94 (+1.71%)</td><td>159.30 (-3.51%)</td><td>143.90 (+2.57%)</td><td>29.77 <b>(+47.38%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.70 (n/a)</td><td>168.06 (n/a)</td><td>165.10 (n/a)</td><td>140.30 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-2.12%)</td><td>0.02 (-7.94%)</td><td>0.02 (-10.75%)</td><td>0.02 (-12.39%)</td><td>0.00 <b>(+23.85%)</b></td><td>250.90 (+14.15%)</td><td>191.10 (+9.90%)</td><td>188.30 (+12.02%)</td><td>158.00 (+2.13%)</td><td>37.42 <b>(+41.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.80 (n/a)</td><td>173.88 (n/a)</td><td>168.10 (n/a)</td><td>154.70 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-7.31%)</td><td>0.02 <b>(-20.28%)</b></td><td>0.02 <b>(-24.91%)</b></td><td>0.02 <b>(-20.60%)</b></td><td>0.01 <b>(+20.76%)</b></td><td>211.00 <b>(+25.97%)</b></td><td>179.30 <b>(+27.33%)</b></td><td>182.70 <b>(+33.16%)</b></td><td>128.10 (+7.83%)</td><td>32.65 <b>(+61.69%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.50 (n/a)</td><td>140.82 (n/a)</td><td>137.20 (n/a)</td><td>118.80 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+3.15%)</td><td>0.05 (-8.83%)</td><td>0.05 (-8.11%)</td><td>0.03 <b>(-32.06%)</b></td><td>0.02 <b>(+181.73%)</b></td><td>236.90 <b>(+47.14%)</b></td><td>174.34 (+17.69%)</td><td>161.50 (+8.83%)</td><td>123.10 (-3.07%)</td><td>54.28 <b>(+299.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>161.00 (n/a)</td><td>148.14 (n/a)</td><td>148.40 (n/a)</td><td>127.00 (n/a)</td><td>13.59 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (-11.34%)</td><td>0.05 (-3.75%)</td><td>0.05 (-10.96%)</td><td>0.04 <b>(+22.25%)</b></td><td>0.01 <b>(-54.97%)</b></td><td>188.70 (-18.21%)</td><td>170.78 (-0.91%)</td><td>180.70 (+12.31%)</td><td>144.10 (+12.75%)</td><td>20.00 <b>(-57.62%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>172.34 (n/a)</td><td>160.90 (n/a)</td><td>127.80 (n/a)</td><td>47.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 <b>(-36.48%)</b></td><td>0.04 (-0.97%)</td><td>0.04 (+12.07%)</td><td>0.04 <b>(+70.38%)</b></td><td>0.00 <b>(-79.92%)</b></td><td>222.40 <b>(-41.30%)</b></td><td>190.56 (-12.62%)</td><td>186.70 (-10.76%)</td><td>177.80 <b>(+57.48%)</b></td><td>18.27 <b>(-81.50%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>378.90 (n/a)</td><td>218.08 (n/a)</td><td>209.20 (n/a)</td><td>112.90 (n/a)</td><td>98.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 <b>(-30.64%)</b></td><td>0.04 (-4.10%)</td><td>0.04 (+11.58%)</td><td>0.04 <b>(+22.76%)</b></td><td>0.00 <b>(-68.11%)</b></td><td>232.90 (-18.54%)</td><td>191.74 (-3.52%)</td><td>185.50 (-10.39%)</td><td>173.10 <b>(+44.13%)</b></td><td>24.48 <b>(-61.69%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>285.90 (n/a)</td><td>198.74 (n/a)</td><td>207.00 (n/a)</td><td>120.10 (n/a)</td><td>63.91 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 <b>(-20.52%)</b></td><td>0.05 (-9.48%)</td><td>0.05 (-5.65%)</td><td>0.04 (-9.54%)</td><td>0.01 <b>(-40.57%)</b></td><td>222.80 (+10.57%)</td><td>182.86 (+8.81%)</td><td>178.70 (+5.99%)</td><td>151.00 <b>(+25.83%)</b></td><td>26.41 (-14.43%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>168.06 (n/a)</td><td>168.60 (n/a)</td><td>120.00 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 <b>(-37.17%)</b></td><td>0.04 <b>(-24.58%)</b></td><td>0.04 <b>(-27.33%)</b></td><td>0.03 (+0.16%)</td><td>0.00 <b>(-70.58%)</b></td><td>238.80 (-0.17%)</td><td>207.12 <b>(+25.51%)</b></td><td>199.40 <b>(+37.61%)</b></td><td>186.50 <b>(+59.13%)</b></td><td>22.41 <b>(-54.19%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>165.02 (n/a)</td><td>144.90 (n/a)</td><td>117.20 (n/a)</td><td>48.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (-18.77%)</td><td>0.05 (-8.18%)</td><td>0.05 (-4.13%)</td><td>0.05 (-3.83%)</td><td>0.00 <b>(-51.09%)</b></td><td>179.50 (+4.00%)</td><td>156.56 (+7.39%)</td><td>150.10 (+4.31%)</td><td>144.40 <b>(+23.10%)</b></td><td>14.30 <b>(-37.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.60 (n/a)</td><td>145.78 (n/a)</td><td>143.90 (n/a)</td><td>117.30 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+4.73%)</td><td>0.05 (-13.84%)</td><td>0.05 <b>(-22.85%)</b></td><td>0.04 (-19.33%)</td><td>0.01 <b>(+84.24%)</b></td><td>211.40 <b>(+23.99%)</b></td><td>173.88 (+19.69%)</td><td>181.70 <b>(+29.60%)</b></td><td>121.00 (-4.57%)</td><td>37.01 <b>(+117.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.50 (n/a)</td><td>145.28 (n/a)</td><td>140.20 (n/a)</td><td>126.80 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+15.98%)</td><td>0.06 (+16.97%)</td><td>0.06 (+10.30%)</td><td>0.04 (+6.62%)</td><td>0.01 <b>(+30.94%)</b></td><td>190.40 (-6.21%)</td><td>143.44 (-13.76%)</td><td>144.90 (-9.38%)</td><td>112.40 (-13.74%)</td><td>29.73 (+6.64%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>166.32 (n/a)</td><td>159.90 (n/a)</td><td>130.30 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (-3.51%)</td><td>0.05 (-7.28%)</td><td>0.05 (-9.86%)</td><td>0.04 (-0.16%)</td><td>0.01 (-4.54%)</td><td>184.50 (+0.16%)</td><td>164.26 (+7.78%)</td><td>172.70 (+10.99%)</td><td>129.00 (+3.61%)</td><td>23.45 (+0.52%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>152.40 (n/a)</td><td>155.60 (n/a)</td><td>124.50 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+30.55%)</b></td><td>0.05 (+13.05%)</td><td>0.05 (+4.74%)</td><td>0.03 (-11.31%)</td><td>0.02 <b>(+188.06%)</b></td><td>245.40 (+12.72%)</td><td>171.36 (-4.47%)</td><td>164.90 (-4.52%)</td><td>116.50 <b>(-23.41%)</b></td><td>57.45 <b>(+133.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>179.38 (n/a)</td><td>172.70 (n/a)</td><td>152.10 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+4.87%)</td><td>0.05 (-14.03%)</td><td>0.05 (-19.01%)</td><td>0.03 <b>(-30.23%)</b></td><td>0.02 <b>(+81.46%)</b></td><td>261.40 <b>(+43.31%)</b></td><td>170.60 <b>(+25.90%)</b></td><td>158.90 <b>(+23.47%)</b></td><td>111.10 (-4.64%)</td><td>63.29 <b>(+134.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>135.50 (n/a)</td><td>128.70 (n/a)</td><td>116.50 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (+9.63%)</td><td>0.05 (+9.91%)</td><td>0.04 (-2.29%)</td><td>0.04 <b>(+56.06%)</b></td><td>0.01 <b>(-28.97%)</b></td><td>198.40 <b>(-35.94%)</b></td><td>175.98 (-12.93%)</td><td>186.30 (+2.36%)</td><td>139.20 (-8.78%)</td><td>25.98 <b>(-59.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.70 (n/a)</td><td>202.12 (n/a)</td><td>182.00 (n/a)</td><td>152.60 (n/a)</td><td>63.37 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+10.86%)</td><td>0.05 (+9.14%)</td><td>0.05 (+13.59%)</td><td>0.04 (+10.23%)</td><td>0.01 <b>(+21.92%)</b></td><td>182.50 (-9.29%)</td><td>154.88 (-7.98%)</td><td>153.30 (-12.00%)</td><td>122.10 (-9.76%)</td><td>25.04 (+1.86%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>168.32 (n/a)</td><td>174.20 (n/a)</td><td>135.30 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+14.53%)</td><td>0.05 (+5.63%)</td><td>0.05 (+14.54%)</td><td>0.04 (-3.49%)</td><td>0.01 <b>(+68.69%)</b></td><td>185.60 (+3.63%)</td><td>159.46 (-4.09%)</td><td>154.00 (-12.70%)</td><td>125.00 (-12.71%)</td><td>25.31 <b>(+54.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>166.26 (n/a)</td><td>176.40 (n/a)</td><td>143.20 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+4.11%)</td><td>0.06 (+13.44%)</td><td>0.05 (+14.21%)</td><td>0.05 <b>(+33.67%)</b></td><td>0.01 (-19.89%)</td><td>175.70 <b>(-25.17%)</b></td><td>151.48 (-13.86%)</td><td>153.00 (-12.42%)</td><td>119.60 (-3.94%)</td><td>24.48 <b>(-41.06%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>175.86 (n/a)</td><td>174.70 (n/a)</td><td>124.50 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 <b>(+26.67%)</b></td><td>0.11 <b>(+21.76%)</b></td><td>0.12 <b>(+28.89%)</b></td><td>0.07 (+6.80%)</td><td>0.03 <b>(+52.52%)</b></td><td>227.80 (-6.37%)</td><td>151.52 (-15.98%)</td><td>133.10 <b>(-22.39%)</b></td><td>116.90 <b>(-21.07%)</b></td><td>43.96 (+16.60%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.30 (n/a)</td><td>180.34 (n/a)</td><td>171.50 (n/a)</td><td>148.10 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (-7.72%)</td><td>0.10 (-1.15%)</td><td>0.11 (+11.83%)</td><td>0.08 (-8.17%)</td><td>0.02 (-1.94%)</td><td>209.50 (+8.89%)</td><td>165.36 (+1.66%)</td><td>153.10 (-10.57%)</td><td>129.00 (+8.40%)</td><td>34.39 (+19.18%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>162.66 (n/a)</td><td>171.20 (n/a)</td><td>119.00 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (-5.78%)</td><td>0.09 (-1.25%)</td><td>0.09 (+8.81%)</td><td>0.08 (+2.05%)</td><td>0.01 <b>(-36.69%)</b></td><td>217.40 (-2.03%)</td><td>194.46 (+0.09%)</td><td>190.10 (-8.08%)</td><td>171.10 (+6.14%)</td><td>20.56 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>194.28 (n/a)</td><td>206.80 (n/a)</td><td>161.20 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (-10.93%)</td><td>0.09 (+14.14%)</td><td>0.09 <b>(+21.75%)</b></td><td>0.08 <b>(+67.09%)</b></td><td>0.01 <b>(-57.88%)</b></td><td>215.10 <b>(-40.15%)</b></td><td>190.28 (-18.96%)</td><td>188.30 (-17.84%)</td><td>163.60 (+12.29%)</td><td>22.91 <b>(-71.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>359.40 (n/a)</td><td>234.80 (n/a)</td><td>229.20 (n/a)</td><td>145.70 (n/a)</td><td>80.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (-4.46%)</td><td>0.10 (+5.91%)</td><td>0.11 (+0.22%)</td><td>0.08 (+14.60%)</td><td>0.01 <b>(-40.95%)</b></td><td>206.10 (-12.71%)</td><td>161.74 (-9.16%)</td><td>152.20 (-0.20%)</td><td>138.30 (+4.61%)</td><td>26.24 <b>(-46.10%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.10 (n/a)</td><td>178.04 (n/a)</td><td>152.50 (n/a)</td><td>132.20 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 <b>(+51.99%)</b></td><td>0.12 <b>(+41.80%)</b></td><td>0.11 <b>(+33.77%)</b></td><td>0.08 <b>(+32.55%)</b></td><td>0.03 <b>(+120.82%)</b></td><td>198.80 <b>(-24.55%)</b></td><td>146.92 <b>(-27.34%)</b></td><td>143.80 <b>(-25.22%)</b></td><td>109.00 <b>(-34.22%)</b></td><td>38.26 (+3.37%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>263.50 (n/a)</td><td>202.20 (n/a)</td><td>192.30 (n/a)</td><td>165.70 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 <b>(+24.34%)</b></td><td>0.12 <b>(+21.63%)</b></td><td>0.11 (+2.83%)</td><td>0.09 <b>(+25.60%)</b></td><td>0.03 <b>(+22.47%)</b></td><td>188.70 <b>(-20.38%)</b></td><td>145.54 (-18.09%)</td><td>152.40 (-2.74%)</td><td>106.50 (-19.56%)</td><td>33.82 <b>(-24.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>237.00 (n/a)</td><td>177.68 (n/a)</td><td>156.70 (n/a)</td><td>132.40 (n/a)</td><td>44.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (-9.74%)</td><td>0.11 (+11.94%)</td><td>0.11 <b>(+23.33%)</b></td><td>0.10 <b>(+71.93%)</b></td><td>0.01 <b>(-79.94%)</b></td><td>159.70 <b>(-41.84%)</b></td><td>147.62 (-17.53%)</td><td>148.20 (-18.93%)</td><td>137.70 (+10.78%)</td><td>8.07 <b>(-86.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>274.60 (n/a)</td><td>179.00 (n/a)</td><td>182.80 (n/a)</td><td>124.30 (n/a)</td><td>60.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (+16.35%)</td><td>0.12 (+16.18%)</td><td>0.11 (+9.17%)</td><td>0.09 (+14.71%)</td><td>0.03 <b>(+42.43%)</b></td><td>186.80 (-12.83%)</td><td>146.30 (-12.61%)</td><td>143.80 (-8.41%)</td><td>111.00 (-14.09%)</td><td>35.36 (+3.80%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>167.42 (n/a)</td><td>157.00 (n/a)</td><td>129.20 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 <b>(+33.59%)</b></td><td>0.11 <b>(+30.20%)</b></td><td>0.11 <b>(+31.72%)</b></td><td>0.08 <b>(+26.87%)</b></td><td>0.02 <b>(+46.00%)</b></td><td>196.80 <b>(-21.19%)</b></td><td>156.68 <b>(-22.63%)</b></td><td>152.50 <b>(-24.09%)</b></td><td>112.50 <b>(-25.15%)</b></td><td>32.04 (-13.26%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.70 (n/a)</td><td>202.50 (n/a)</td><td>200.90 (n/a)</td><td>150.30 (n/a)</td><td>36.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (+12.31%)</td><td>0.09 (+0.77%)</td><td>0.08 (-4.63%)</td><td>0.07 (-3.77%)</td><td>0.02 <b>(+88.73%)</b></td><td>229.90 (+3.93%)</td><td>190.34 (+0.83%)</td><td>194.30 (+4.86%)</td><td>152.30 (-10.99%)</td><td>32.24 <b>(+69.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>188.78 (n/a)</td><td>185.30 (n/a)</td><td>171.10 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 <b>(+32.60%)</b></td><td>0.10 (+12.16%)</td><td>0.09 (+1.83%)</td><td>0.08 (+4.66%)</td><td>0.02 <b>(+153.47%)</b></td><td>209.60 (-4.47%)</td><td>169.94 (-8.47%)</td><td>176.90 (-1.83%)</td><td>129.70 <b>(-24.59%)</b></td><td>34.21 <b>(+77.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.40 (n/a)</td><td>185.66 (n/a)</td><td>180.20 (n/a)</td><td>172.00 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (-6.20%)</td><td>0.08 (-7.91%)</td><td>0.08 (-1.84%)</td><td>0.06 <b>(-28.67%)</b></td><td>0.02 <b>(+31.48%)</b></td><td>294.00 <b>(+40.20%)</b></td><td>213.92 (+11.25%)</td><td>204.40 (+1.89%)</td><td>159.90 (+6.60%)</td><td>49.60 <b>(+106.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>192.28 (n/a)</td><td>200.60 (n/a)</td><td>150.00 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (+10.65%)</td><td>0.09 (+8.66%)</td><td>0.08 (+5.47%)</td><td>0.07 (+5.55%)</td><td>0.01 (+6.26%)</td><td>227.10 (-5.26%)</td><td>190.56 (-8.00%)</td><td>194.80 (-5.21%)</td><td>162.00 (-9.60%)</td><td>25.68 (-8.68%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>207.14 (n/a)</td><td>205.50 (n/a)</td><td>179.20 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 <b>(-27.09%)</b></td><td>0.08 (-9.01%)</td><td>0.08 (+0.13%)</td><td>0.06 (-12.42%)</td><td>0.01 <b>(-45.96%)</b></td><td>264.80 (+14.19%)</td><td>202.02 (+7.13%)</td><td>199.40 (-0.10%)</td><td>165.10 <b>(+37.13%)</b></td><td>38.18 (-9.27%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>231.90 (n/a)</td><td>188.58 (n/a)</td><td>199.60 (n/a)</td><td>120.40 (n/a)</td><td>42.09 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (+6.32%)</td><td>0.10 (+7.57%)</td><td>0.11 (+13.73%)</td><td>0.09 (+4.09%)</td><td>0.01 (+7.52%)</td><td>187.10 (-3.95%)</td><td>160.80 (-6.99%)</td><td>154.00 (-12.10%)</td><td>133.50 (-5.99%)</td><td>22.36 (-2.95%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>172.88 (n/a)</td><td>175.20 (n/a)</td><td>142.00 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (+11.92%)</td><td>0.18 (+9.54%)</td><td>0.18 (+10.72%)</td><td>0.15 (+3.64%)</td><td>0.03 <b>(+28.49%)</b></td><td>215.20 (-3.50%)</td><td>180.38 (-8.28%)</td><td>178.80 (-9.65%)</td><td>149.50 (-10.64%)</td><td>25.13 (+10.68%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>196.66 (n/a)</td><td>197.90 (n/a)</td><td>167.30 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (+1.83%)</td><td>0.21 (+8.09%)</td><td>0.21 (+8.22%)</td><td>0.18 (+9.75%)</td><td>0.03 (-13.94%)</td><td>182.80 (-8.87%)</td><td>155.88 (-8.36%)</td><td>156.20 (-7.57%)</td><td>123.40 (-1.83%)</td><td>23.17 <b>(-23.52%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.60 (n/a)</td><td>170.10 (n/a)</td><td>169.00 (n/a)</td><td>125.70 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (-4.01%)</td><td>0.16 (-3.28%)</td><td>0.16 (-3.13%)</td><td>0.12 (+4.53%)</td><td>0.04 (+0.78%)</td><td>282.40 (-4.34%)</td><td>217.34 (+3.41%)</td><td>201.40 (+3.23%)</td><td>164.60 (+4.18%)</td><td>50.46 (-1.91%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>295.20 (n/a)</td><td>210.18 (n/a)</td><td>195.10 (n/a)</td><td>158.00 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (+5.87%)</td><td>0.16 (-10.68%)</td><td>0.15 (-13.72%)</td><td>0.12 <b>(-22.05%)</b></td><td>0.04 <b>(+66.87%)</b></td><td>264.90 <b>(+28.28%)</b></td><td>208.34 (+14.99%)</td><td>218.00 (+15.90%)</td><td>147.30 (-5.58%)</td><td>43.77 <b>(+101.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.50 (n/a)</td><td>181.18 (n/a)</td><td>188.10 (n/a)</td><td>156.00 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 <b>(+37.54%)</b></td><td>0.18 (+8.28%)</td><td>0.16 (-8.84%)</td><td>0.12 <b>(+26.75%)</b></td><td>0.07 <b>(+36.99%)</b></td><td>271.70 <b>(-21.09%)</b></td><td>199.24 (-7.39%)</td><td>200.60 (+9.68%)</td><td>109.50 <b>(-27.29%)</b></td><td>61.28 <b>(-23.76%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>344.30 (n/a)</td><td>215.14 (n/a)</td><td>182.90 (n/a)</td><td>150.60 (n/a)</td><td>80.39 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (-6.40%)</td><td>0.20 (+0.60%)</td><td>0.20 (+4.47%)</td><td>0.18 (+1.33%)</td><td>0.02 <b>(-32.43%)</b></td><td>179.60 (-1.32%)</td><td>162.00 (-1.28%)</td><td>165.80 (-4.27%)</td><td>143.80 (+6.84%)</td><td>14.22 <b>(-29.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.00 (n/a)</td><td>164.10 (n/a)</td><td>173.20 (n/a)</td><td>134.60 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 (+11.67%)</td><td>0.20 (+2.38%)</td><td>0.19 (-9.31%)</td><td>0.17 <b>(+20.55%)</b></td><td>0.05 (-0.68%)</td><td>197.80 (-17.03%)</td><td>167.82 (-3.80%)</td><td>174.00 (+10.27%)</td><td>114.80 (-10.45%)</td><td>31.64 <b>(-30.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.40 (n/a)</td><td>174.44 (n/a)</td><td>157.80 (n/a)</td><td>128.20 (n/a)</td><td>45.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (+18.09%)</td><td>0.19 (+12.14%)</td><td>0.18 (+4.53%)</td><td>0.16 (+12.75%)</td><td>0.04 <b>(+20.74%)</b></td><td>211.10 (-11.34%)</td><td>176.58 (-10.76%)</td><td>181.90 (-4.36%)</td><td>126.60 (-15.32%)</td><td>31.56 (-14.32%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.10 (n/a)</td><td>197.86 (n/a)</td><td>190.20 (n/a)</td><td>149.50 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (+11.38%)</td><td>0.19 (-2.02%)</td><td>0.19 (-3.79%)</td><td>0.14 (-2.18%)</td><td>0.04 <b>(+47.38%)</b></td><td>228.60 (+2.24%)</td><td>181.64 (+3.87%)</td><td>174.00 (+3.94%)</td><td>131.90 (-10.21%)</td><td>38.05 <b>(+31.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.60 (n/a)</td><td>174.88 (n/a)</td><td>167.40 (n/a)</td><td>146.90 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (+17.78%)</td><td>0.21 (+16.26%)</td><td>0.23 (+17.15%)</td><td>0.18 (+13.75%)</td><td>0.03 <b>(+30.09%)</b></td><td>179.00 (-12.08%)</td><td>155.16 (-13.75%)</td><td>144.90 (-14.66%)</td><td>132.10 (-15.10%)</td><td>20.65 (-2.84%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>179.90 (n/a)</td><td>169.80 (n/a)</td><td>155.60 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (-8.87%)</td><td>0.21 (+7.85%)</td><td>0.22 (+16.50%)</td><td>0.20 <b>(+26.97%)</b></td><td>0.01 <b>(-69.30%)</b></td><td>162.60 <b>(-21.26%)</b></td><td>153.72 (-9.18%)</td><td>149.70 (-14.16%)</td><td>146.60 (+9.73%)</td><td>7.52 <b>(-73.15%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>206.50 (n/a)</td><td>169.26 (n/a)</td><td>174.40 (n/a)</td><td>133.60 (n/a)</td><td>28.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (+13.83%)</td><td>0.19 (+5.62%)</td><td>0.15 (-11.65%)</td><td>0.15 (+7.83%)</td><td>0.05 <b>(+66.85%)</b></td><td>213.90 (-7.24%)</td><td>183.46 (-2.92%)</td><td>211.40 (+13.17%)</td><td>133.90 (-12.14%)</td><td>40.67 <b>(+39.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>188.98 (n/a)</td><td>186.80 (n/a)</td><td>152.40 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (-1.27%)</td><td>0.17 (+2.17%)</td><td>0.18 (+0.74%)</td><td>0.13 (-8.53%)</td><td>0.03 (-2.46%)</td><td>260.60 (+9.31%)</td><td>195.62 (-1.99%)</td><td>181.70 (-0.71%)</td><td>170.70 (+1.25%)</td><td>36.85 (+9.47%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.40 (n/a)</td><td>199.60 (n/a)</td><td>183.00 (n/a)</td><td>168.60 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (+5.51%)</td><td>0.19 (+6.23%)</td><td>0.18 (-0.97%)</td><td>0.17 (+16.52%)</td><td>0.03 <b>(-28.65%)</b></td><td>196.50 (-14.19%)</td><td>170.94 (-7.86%)</td><td>178.20 (+0.96%)</td><td>140.20 (-5.27%)</td><td>22.83 <b>(-42.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>229.00 (n/a)</td><td>185.52 (n/a)</td><td>176.50 (n/a)</td><td>148.00 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (-6.80%)</td><td>0.18 (-8.94%)</td><td>0.17 (-14.94%)</td><td>0.14 (-11.45%)</td><td>0.03 (-17.46%)</td><td>238.40 (+12.93%)</td><td>189.00 (+9.20%)</td><td>188.10 (+17.56%)</td><td>149.60 (+7.24%)</td><td>32.40 (-1.75%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.10 (n/a)</td><td>173.08 (n/a)</td><td>160.00 (n/a)</td><td>139.50 (n/a)</td><td>32.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (-11.28%)</td><td>0.19 (-4.15%)</td><td>0.18 (-0.24%)</td><td>0.16 (-3.55%)</td><td>0.02 <b>(-21.71%)</b></td><td>207.40 (+3.65%)</td><td>175.68 (+3.78%)</td><td>177.20 (+0.23%)</td><td>149.50 (+12.66%)</td><td>23.11 (-7.45%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>200.10 (n/a)</td><td>169.28 (n/a)</td><td>176.80 (n/a)</td><td>132.70 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (-0.98%)</td><td>0.21 (-0.25%)</td><td>0.21 (-0.07%)</td><td>0.21 (+0.06%)</td><td>0.00 <b>(-84.07%)</b></td><td>40887.80 (-0.06%)</td><td>40846.44 (+0.25%)</td><td>40838.80 (+0.07%)</td><td>40814.70 (+0.99%)</td><td>32.03 <b>(-83.92%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40911.30 (n/a)</td><td>40743.20 (n/a)</td><td>40811.50 (n/a)</td><td>40414.30 (n/a)</td><td>199.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (-0.69%)</td><td>0.21 (-0.03%)</td><td>0.21 (+0.08%)</td><td>0.21 (+0.48%)</td><td>0.00 <b>(-72.26%)</b></td><td>40913.40 (-0.48%)</td><td>40851.44 (+0.02%)</td><td>40861.10 (-0.08%)</td><td>40764.60 (+0.69%)</td><td>63.69 <b>(-72.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>41109.30 (n/a)</td><td>40841.70 (n/a)</td><td>40895.60 (n/a)</td><td>40483.50 (n/a)</td><td>228.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (-0.22%)</td><td>0.13 (-0.03%)</td><td>0.13 (+0.04%)</td><td>0.13 (+0.01%)</td><td>0.00 <b>(-68.62%)</b></td><td>321884.10 (-0.01%)</td><td>321705.54 (+0.03%)</td><td>321704.70 (-0.04%)</td><td>321514.10 (+0.22%)</td><td>144.98 <b>(-68.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321901.20 (n/a)</td><td>321619.66 (n/a)</td><td>321843.90 (n/a)</td><td>320812.60 (n/a)</td><td>460.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+17.59%)</td><td>0.03 (+17.22%)</td><td>0.03 <b>(+21.38%)</b></td><td>0.02 (+16.82%)</td><td>0.00 <b>(+36.28%)</b></td><td>185.40 (-14.40%)</td><td>157.54 (-14.18%)</td><td>154.30 (-17.62%)</td><td>131.60 (-14.99%)</td><td>26.47 (+1.18%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.60 (n/a)</td><td>183.56 (n/a)</td><td>187.30 (n/a)</td><td>154.80 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (-15.21%)</td><td>0.04 (-13.27%)</td><td>0.04 (-7.38%)</td><td>0.02 <b>(-30.43%)</b></td><td>0.01 (+3.82%)</td><td>278.90 <b>(+43.76%)</b></td><td>179.48 (+19.03%)</td><td>159.60 (+7.98%)</td><td>129.20 (+17.99%)</td><td>57.90 <b>(+88.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>150.78 (n/a)</td><td>147.80 (n/a)</td><td>109.50 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+14.59%)</td><td>0.02 (-14.35%)</td><td>0.02 (-18.64%)</td><td>0.02 <b>(-33.40%)</b></td><td>0.01 <b>(+286.76%)</b></td><td>248.70 <b>(+50.09%)</b></td><td>191.74 <b>(+23.24%)</b></td><td>192.00 <b>(+22.92%)</b></td><td>126.40 (-12.71%)</td><td>48.53 <b>(+404.30%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.70 (n/a)</td><td>155.58 (n/a)</td><td>156.20 (n/a)</td><td>144.80 (n/a)</td><td>9.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (-10.89%)</td><td>0.03 (-6.47%)</td><td>0.03 (-10.76%)</td><td>0.03 (-5.84%)</td><td>0.00 <b>(-28.54%)</b></td><td>190.60 (+6.18%)</td><td>160.78 (+5.78%)</td><td>163.60 (+12.05%)</td><td>133.30 (+12.21%)</td><td>21.97 (-18.42%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>152.00 (n/a)</td><td>146.00 (n/a)</td><td>118.80 (n/a)</td><td>26.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(+24.29%)</b></td><td>0.02 (-0.42%)</td><td>0.02 (+2.09%)</td><td>0.01 <b>(-32.77%)</b></td><td>0.01 <b>(+184.84%)</b></td><td>301.90 <b>(+48.72%)</b></td><td>191.56 (+7.80%)</td><td>176.80 (-2.05%)</td><td>128.00 (-19.55%)</td><td>65.90 <b>(+262.11%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>177.70 (n/a)</td><td>180.50 (n/a)</td><td>159.10 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+11.04%)</td><td>0.04 (+2.78%)</td><td>0.04 (+5.89%)</td><td>0.03 (-4.71%)</td><td>0.01 <b>(+86.33%)</b></td><td>185.60 (+4.98%)</td><td>149.26 (-0.36%)</td><td>136.30 (-5.61%)</td><td>120.70 (-9.93%)</td><td>31.33 <b>(+78.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>176.80 (n/a)</td><td>149.80 (n/a)</td><td>144.40 (n/a)</td><td>134.00 (n/a)</td><td>17.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-15.34%)</td><td>0.02 (-17.93%)</td><td>0.02 (-18.68%)</td><td>0.02 (-12.74%)</td><td>0.00 <b>(-27.15%)</b></td><td>209.60 (+14.60%)</td><td>181.52 <b>(+21.19%)</b></td><td>189.60 <b>(+22.96%)</b></td><td>148.00 (+18.12%)</td><td>24.19 (+0.51%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>149.78 (n/a)</td><td>154.20 (n/a)</td><td>125.30 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+11.09%)</td><td>0.03 (+2.84%)</td><td>0.03 (-5.42%)</td><td>0.02 (+10.89%)</td><td>0.01 (+1.37%)</td><td>235.00 (-9.82%)</td><td>169.02 (-3.57%)</td><td>160.70 (+5.72%)</td><td>127.70 (-10.01%)</td><td>40.66 (-17.43%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.60 (n/a)</td><td>175.28 (n/a)</td><td>152.00 (n/a)</td><td>141.90 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-0.41%)</td><td>0.02 (-9.20%)</td><td>0.02 (-6.82%)</td><td>0.02 (-12.47%)</td><td>0.01 <b>(+22.35%)</b></td><td>211.20 (+14.29%)</td><td>179.00 (+12.10%)</td><td>182.00 (+7.31%)</td><td>117.50 (+0.34%)</td><td>36.76 <b>(+38.99%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>159.68 (n/a)</td><td>169.60 (n/a)</td><td>117.10 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.04 (+12.36%)</td><td>0.03 (+13.57%)</td><td>0.03 (+18.52%)</td><td>0.02 (-1.90%)</td><td>0.01 <b>(+34.11%)</b></td><td>208.10 (+1.91%)</td><td>160.84 (-10.98%)</td><td>159.60 (-15.60%)</td><td>127.00 (-11.00%)</td><td>31.53 <b>(+20.46%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.20 (n/a)</td><td>180.68 (n/a)</td><td>189.10 (n/a)</td><td>142.70 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (-13.36%)</td><td>0.02 (-3.48%)</td><td>0.02 (+5.23%)</td><td>0.02 (+0.16%)</td><td>0.00 <b>(-32.83%)</b></td><td>203.10 (-0.20%)</td><td>181.90 (+2.78%)</td><td>173.20 (-4.94%)</td><td>162.10 (+15.37%)</td><td>19.66 <b>(-20.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.50 (n/a)</td><td>176.98 (n/a)</td><td>182.20 (n/a)</td><td>140.50 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+16.84%)</td><td>0.03 <b>(+28.73%)</b></td><td>0.03 <b>(+32.64%)</b></td><td>0.02 <b>(+46.32%)</b></td><td>0.00 <b>(-21.91%)</b></td><td>185.70 <b>(-31.68%)</b></td><td>160.80 <b>(-23.98%)</b></td><td>161.00 <b>(-24.63%)</b></td><td>134.50 (-14.44%)</td><td>19.74 <b>(-54.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>271.80 (n/a)</td><td>211.52 (n/a)</td><td>213.60 (n/a)</td><td>157.20 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 <b>(+42.87%)</b></td><td>0.02 (+3.51%)</td><td>0.02 (-12.43%)</td><td>0.02 (-0.58%)</td><td>0.01 <b>(+156.83%)</b></td><td>239.50 (+0.59%)</td><td>194.80 (+0.85%)</td><td>208.10 (+14.15%)</td><td>121.30 <b>(-30.01%)</b></td><td>45.16 <b>(+70.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>193.16 (n/a)</td><td>182.30 (n/a)</td><td>173.30 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.03 (+0.44%)</td><td>0.02 (+6.72%)</td><td>0.02 (+3.70%)</td><td>0.02 <b>(+20.46%)</b></td><td>0.00 <b>(-42.94%)</b></td><td>187.50 (-16.96%)</td><td>178.80 (-7.14%)</td><td>183.20 (-3.58%)</td><td>159.50 (-0.44%)</td><td>11.12 <b>(-53.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.80 (n/a)</td><td>192.54 (n/a)</td><td>190.00 (n/a)</td><td>160.20 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.02 (-0.85%)</td><td>0.02 (-14.83%)</td><td>0.02 (-11.24%)</td><td>0.01 <b>(-39.44%)</b></td><td>0.00 <b>(+134.85%)</b></td><td>362.70 <b>(+65.16%)</b></td><td>236.84 <b>(+24.21%)</b></td><td>212.90 (+12.65%)</td><td>176.00 (+0.86%)</td><td>74.24 <b>(+306.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>190.68 (n/a)</td><td>189.00 (n/a)</td><td>174.50 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+2.04%)</td><td>0.05 (-11.27%)</td><td>0.04 <b>(-21.94%)</b></td><td>0.04 <b>(-21.17%)</b></td><td>0.01 <b>(+105.66%)</b></td><td>216.50 <b>(+26.83%)</b></td><td>174.38 (+17.30%)</td><td>186.30 <b>(+28.13%)</b></td><td>124.30 (-1.97%)</td><td>41.39 <b>(+155.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.70 (n/a)</td><td>148.66 (n/a)</td><td>145.40 (n/a)</td><td>126.80 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (+9.97%)</td><td>0.09 (+14.54%)</td><td>0.08 (+10.19%)</td><td>0.07 (+18.14%)</td><td>0.02 (+17.70%)</td><td>183.00 (-15.36%)</td><td>149.20 (-12.29%)</td><td>153.80 (-9.26%)</td><td>108.50 (-9.05%)</td><td>32.86 (-5.31%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.20 (n/a)</td><td>170.10 (n/a)</td><td>169.50 (n/a)</td><td>119.30 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+18.07%)</td><td>0.05 (-7.10%)</td><td>0.05 (-10.49%)</td><td>0.03 <b>(-34.70%)</b></td><td>0.02 <b>(+185.36%)</b></td><td>281.60 <b>(+53.13%)</b></td><td>187.34 (+16.10%)</td><td>178.20 (+11.72%)</td><td>119.10 (-15.35%)</td><td>62.15 <b>(+271.91%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>161.36 (n/a)</td><td>159.50 (n/a)</td><td>140.70 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.08 <b>(+40.81%)</b></td><td>0.06 (+8.81%)</td><td>0.05 (+1.87%)</td><td>0.04 (-16.48%)</td><td>0.02 <b>(+294.63%)</b></td><td>241.30 (+19.69%)</td><td>183.38 (-3.24%)</td><td>194.10 (-1.82%)</td><td>123.00 <b>(-28.98%)</b></td><td>46.29 <b>(+231.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>201.60 (n/a)</td><td>189.52 (n/a)</td><td>197.70 (n/a)</td><td>173.20 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (-3.41%)</td><td>0.05 (-11.26%)</td><td>0.04 (-14.13%)</td><td>0.03 <b>(-30.66%)</b></td><td>0.02 <b>(+78.36%)</b></td><td>295.30 <b>(+44.19%)</b></td><td>202.04 <b>(+22.15%)</b></td><td>191.90 (+16.44%)</td><td>132.60 (+3.59%)</td><td>72.48 <b>(+156.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>165.40 (n/a)</td><td>164.80 (n/a)</td><td>128.00 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+9.85%)</td><td>0.06 <b>(+28.63%)</b></td><td>0.06 <b>(+42.88%)</b></td><td>0.06 <b>(+49.24%)</b></td><td>0.00 <b>(-72.11%)</b></td><td>166.60 <b>(-32.98%)</b></td><td>159.24 <b>(-24.39%)</b></td><td>162.30 <b>(-30.01%)</b></td><td>151.70 (-9.00%)</td><td>6.72 <b>(-82.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>248.60 (n/a)</td><td>210.62 (n/a)</td><td>231.90 (n/a)</td><td>166.70 (n/a)</td><td>38.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 <b>(+37.52%)</b></td><td>0.06 (+16.20%)</td><td>0.05 (-2.15%)</td><td>0.04 (+13.24%)</td><td>0.01 <b>(+112.97%)</b></td><td>188.90 (-11.69%)</td><td>149.20 (-11.48%)</td><td>159.80 (+2.17%)</td><td>110.90 <b>(-27.28%)</b></td><td>34.07 <b>(+31.36%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>168.54 (n/a)</td><td>156.40 (n/a)</td><td>152.50 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (+8.28%)</td><td>0.05 (+1.16%)</td><td>0.05 (-7.41%)</td><td>0.04 (-2.24%)</td><td>0.01 <b>(+33.86%)</b></td><td>209.90 (+2.29%)</td><td>177.18 (-0.43%)</td><td>183.50 (+8.00%)</td><td>143.20 (-7.61%)</td><td>26.13 <b>(+24.11%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>177.94 (n/a)</td><td>169.90 (n/a)</td><td>155.00 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (+12.99%)</td><td>0.06 (+18.84%)</td><td>0.06 (+1.92%)</td><td>0.05 <b>(+37.72%)</b></td><td>0.01 <b>(-37.31%)</b></td><td>156.80 <b>(-27.41%)</b></td><td>138.30 (-18.10%)</td><td>142.00 (-1.87%)</td><td>121.80 (-11.48%)</td><td>14.65 <b>(-60.40%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>168.86 (n/a)</td><td>144.70 (n/a)</td><td>137.60 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.07 (-9.08%)</td><td>0.06 (+8.48%)</td><td>0.06 (+16.71%)</td><td>0.05 (+7.64%)</td><td>0.01 <b>(-35.72%)</b></td><td>197.70 (-7.10%)</td><td>161.28 (-9.63%)</td><td>151.90 (-14.33%)</td><td>137.60 (+9.99%)</td><td>23.33 <b>(-32.80%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>178.46 (n/a)</td><td>177.30 (n/a)</td><td>125.10 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (-2.56%)</td><td>0.05 (+2.61%)</td><td>0.05 (+15.25%)</td><td>0.03 (-14.43%)</td><td>0.01 (+3.21%)</td><td>246.70 (+16.86%)</td><td>171.94 (-1.56%)</td><td>156.40 (-13.21%)</td><td>141.10 (+2.62%)</td><td>42.41 <b>(+31.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>174.66 (n/a)</td><td>180.20 (n/a)</td><td>137.50 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (-11.81%)</td><td>0.05 (-1.40%)</td><td>0.05 (+5.01%)</td><td>0.04 (-3.11%)</td><td>0.01 (-19.12%)</td><td>221.30 (+3.22%)</td><td>188.06 (+0.85%)</td><td>181.80 (-4.77%)</td><td>161.00 (+13.38%)</td><td>28.27 (-6.68%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>186.48 (n/a)</td><td>190.90 (n/a)</td><td>142.00 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 (+15.04%)</td><td>0.05 (+15.40%)</td><td>0.05 (+7.88%)</td><td>0.03 <b>(+29.43%)</b></td><td>0.01 (-6.29%)</td><td>240.30 <b>(-22.76%)</b></td><td>176.74 (-15.04%)</td><td>165.20 (-7.30%)</td><td>151.10 (-13.11%)</td><td>36.75 <b>(-37.16%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.10 (n/a)</td><td>208.02 (n/a)</td><td>178.20 (n/a)</td><td>173.90 (n/a)</td><td>58.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.06 (+11.98%)</td><td>0.05 (+9.86%)</td><td>0.05 (+14.12%)</td><td>0.04 (-7.47%)</td><td>0.01 <b>(+58.33%)</b></td><td>229.40 (+8.05%)</td><td>177.36 (-7.51%)</td><td>175.10 (-12.36%)</td><td>141.60 (-10.66%)</td><td>33.70 <b>(+54.18%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>191.76 (n/a)</td><td>199.80 (n/a)</td><td>158.50 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.05 <b>(+24.43%)</b></td><td>0.04 <b>(+26.45%)</b></td><td>0.05 <b>(+33.72%)</b></td><td>0.03 <b>(+25.93%)</b></td><td>0.01 <b>(+23.76%)</b></td><td>243.50 <b>(-20.58%)</b></td><td>192.26 <b>(-20.94%)</b></td><td>177.70 <b>(-25.21%)</b></td><td>173.20 (-19.63%)</td><td>29.39 <b>(-20.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>306.60 (n/a)</td><td>243.18 (n/a)</td><td>237.60 (n/a)</td><td>215.50 (n/a)</td><td>37.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-6.25%)</td><td>0.10 (+8.14%)</td><td>0.11 <b>(+23.46%)</b></td><td>0.08 (+11.44%)</td><td>0.01 <b>(-31.56%)</b></td><td>205.30 (-10.23%)</td><td>168.28 (-9.14%)</td><td>156.00 (-19.00%)</td><td>150.00 (+6.61%)</td><td>23.83 <b>(-34.35%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>228.70 (n/a)</td><td>185.20 (n/a)</td><td>192.60 (n/a)</td><td>140.70 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (+14.30%)</td><td>0.17 <b>(+22.68%)</b></td><td>0.17 <b>(+27.42%)</b></td><td>0.13 (+1.66%)</td><td>0.02 <b>(+53.46%)</b></td><td>189.90 (-1.66%)</td><td>149.08 (-17.73%)</td><td>146.10 <b>(-21.54%)</b></td><td>131.00 (-12.49%)</td><td>24.09 <b>(+34.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.10 (n/a)</td><td>181.20 (n/a)</td><td>186.20 (n/a)</td><td>149.70 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-14.18%)</td><td>0.09 (-8.17%)</td><td>0.09 (+6.51%)</td><td>0.07 (-11.90%)</td><td>0.02 <b>(-25.19%)</b></td><td>224.10 (+13.53%)</td><td>181.28 (+7.84%)</td><td>177.30 (-6.14%)</td><td>150.10 (+16.54%)</td><td>32.84 (-3.02%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.40 (n/a)</td><td>168.10 (n/a)</td><td>188.90 (n/a)</td><td>128.80 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (+11.39%)</td><td>0.13 (+12.09%)</td><td>0.12 (+10.72%)</td><td>0.11 <b>(+51.65%)</b></td><td>0.02 <b>(-32.31%)</b></td><td>180.90 <b>(-34.05%)</b></td><td>162.76 (-14.20%)</td><td>165.20 (-9.68%)</td><td>128.20 (-10.22%)</td><td>20.74 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>274.30 (n/a)</td><td>189.70 (n/a)</td><td>182.90 (n/a)</td><td>142.80 (n/a)</td><td>52.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (+3.46%)</td><td>0.10 (+1.65%)</td><td>0.10 (-0.09%)</td><td>0.08 (+11.66%)</td><td>0.02 (-4.62%)</td><td>199.80 (-10.44%)</td><td>163.48 (-2.33%)</td><td>163.30 (+0.06%)</td><td>126.10 (-3.37%)</td><td>32.22 (-15.34%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.10 (n/a)</td><td>167.38 (n/a)</td><td>163.20 (n/a)</td><td>130.50 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 <b>(+23.82%)</b></td><td>0.13 <b>(+24.45%)</b></td><td>0.13 (+14.79%)</td><td>0.10 <b>(+82.51%)</b></td><td>0.02 (-18.61%)</td><td>201.60 <b>(-45.22%)</b></td><td>158.74 <b>(-24.91%)</b></td><td>155.10 (-12.87%)</td><td>128.50 (-19.28%)</td><td>29.61 <b>(-66.30%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>368.00 (n/a)</td><td>211.40 (n/a)</td><td>178.00 (n/a)</td><td>159.20 (n/a)</td><td>87.89 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-16.46%)</td><td>0.10 (+3.27%)</td><td>0.10 (+8.46%)</td><td>0.09 (+16.91%)</td><td>0.01 <b>(-64.16%)</b></td><td>183.10 (-14.48%)</td><td>170.16 (-6.33%)</td><td>171.20 (-7.76%)</td><td>148.40 (+19.68%)</td><td>13.25 <b>(-63.22%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.10 (n/a)</td><td>181.66 (n/a)</td><td>185.60 (n/a)</td><td>124.00 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 <b>(+68.72%)</b></td><td>0.12 <b>(+36.30%)</b></td><td>0.11 <b>(+32.04%)</b></td><td>0.10 (+19.06%)</td><td>0.02 <b>(+507.97%)</b></td><td>190.70 (-16.03%)</td><td>162.92 <b>(-24.98%)</b></td><td>162.10 <b>(-24.25%)</b></td><td>123.60 <b>(-40.72%)</b></td><td>26.56 <b>(+200.63%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>217.18 (n/a)</td><td>214.00 (n/a)</td><td>208.50 (n/a)</td><td>8.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 <b>(+21.60%)</b></td><td>0.09 (-9.34%)</td><td>0.08 (-18.11%)</td><td>0.04 <b>(-51.01%)</b></td><td>0.04 <b>(+205.39%)</b></td><td>404.60 <b>(+104.14%)</b></td><td>219.64 <b>(+28.16%)</b></td><td>199.90 <b>(+22.11%)</b></td><td>123.00 (-17.73%)</td><td>110.13 <b>(+427.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>171.38 (n/a)</td><td>163.70 (n/a)</td><td>149.50 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (+1.14%)</td><td>0.10 (-3.49%)</td><td>0.10 (-4.15%)</td><td>0.07 (-5.97%)</td><td>0.02 (+8.58%)</td><td>263.90 (+6.33%)</td><td>193.32 (+4.43%)</td><td>187.00 (+4.29%)</td><td>135.20 (-1.17%)</td><td>46.48 (+13.06%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.20 (n/a)</td><td>185.12 (n/a)</td><td>179.30 (n/a)</td><td>136.80 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (+16.90%)</td><td>0.09 (-3.20%)</td><td>0.09 (-10.20%)</td><td>0.07 (-15.97%)</td><td>0.02 <b>(+119.20%)</b></td><td>233.60 (+19.00%)</td><td>181.26 (+6.60%)</td><td>185.90 (+11.38%)</td><td>130.80 (-14.45%)</td><td>39.46 <b>(+121.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>170.04 (n/a)</td><td>166.90 (n/a)</td><td>152.90 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 <b>(+25.25%)</b></td><td>0.09 (+7.71%)</td><td>0.08 (-5.69%)</td><td>0.06 (-15.02%)</td><td>0.02 <b>(+184.22%)</b></td><td>293.60 (+17.68%)</td><td>209.62 (-2.81%)</td><td>216.30 (+6.03%)</td><td>157.30 <b>(-20.15%)</b></td><td>55.65 <b>(+156.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>215.68 (n/a)</td><td>204.00 (n/a)</td><td>197.00 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 (+12.53%)</td><td>0.10 (+5.61%)</td><td>0.10 (+8.95%)</td><td>0.08 (-4.80%)</td><td>0.01 <b>(+57.23%)</b></td><td>204.50 (+5.03%)</td><td>162.00 (-4.35%)</td><td>156.60 (-8.26%)</td><td>135.80 (-11.13%)</td><td>25.43 <b>(+52.14%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>169.36 (n/a)</td><td>170.70 (n/a)</td><td>152.80 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (-1.66%)</td><td>0.10 (+16.20%)</td><td>0.10 (+15.70%)</td><td>0.09 <b>(+40.09%)</b></td><td>0.02 <b>(-34.93%)</b></td><td>199.10 <b>(-28.64%)</b></td><td>171.72 (-17.80%)</td><td>173.60 (-13.55%)</td><td>131.10 (+1.71%)</td><td>27.35 <b>(-51.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>279.00 (n/a)</td><td>208.90 (n/a)</td><td>200.80 (n/a)</td><td>128.90 (n/a)</td><td>56.73 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.10 (+3.06%)</td><td>0.08 (+6.03%)</td><td>0.09 (+11.27%)</td><td>0.07 (+6.86%)</td><td>0.01 (+16.28%)</td><td>237.80 (-6.41%)</td><td>198.54 (-5.39%)</td><td>180.60 (-10.15%)</td><td>171.90 (-2.94%)</td><td>30.23 (+4.51%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>209.84 (n/a)</td><td>201.00 (n/a)</td><td>177.10 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (-0.71%)</td><td>0.20 (+2.46%)</td><td>0.21 (+6.70%)</td><td>0.16 (-5.78%)</td><td>0.03 (+1.82%)</td><td>208.20 (+6.12%)</td><td>163.76 (-2.15%)</td><td>159.80 (-6.28%)</td><td>129.90 (+0.70%)</td><td>28.59 (+12.04%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.20 (n/a)</td><td>167.36 (n/a)</td><td>170.50 (n/a)</td><td>129.00 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (+2.87%)</td><td>0.24 <b>(+20.84%)</b></td><td>0.24 <b>(+31.02%)</b></td><td>0.20 <b>(+35.11%)</b></td><td>0.02 <b>(-52.59%)</b></td><td>160.40 <b>(-26.01%)</b></td><td>139.42 <b>(-20.19%)</b></td><td>139.40 <b>(-23.66%)</b></td><td>123.70 (-2.75%)</td><td>13.51 <b>(-65.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.80 (n/a)</td><td>174.70 (n/a)</td><td>182.60 (n/a)</td><td>127.20 (n/a)</td><td>39.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 <b>(+34.97%)</b></td><td>0.24 (+15.34%)</td><td>0.24 (+16.29%)</td><td>0.19 (+0.41%)</td><td>0.05 <b>(+194.78%)</b></td><td>210.90 (-0.42%)</td><td>173.70 (-11.21%)</td><td>173.00 (-14.02%)</td><td>130.70 <b>(-25.91%)</b></td><td>31.57 <b>(+118.11%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>195.64 (n/a)</td><td>201.20 (n/a)</td><td>176.40 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (-0.49%)</td><td>0.21 (+8.18%)</td><td>0.21 (+2.44%)</td><td>0.17 <b>(+54.47%)</b></td><td>0.04 <b>(-39.37%)</b></td><td>194.20 <b>(-35.25%)</b></td><td>162.72 (-13.95%)</td><td>153.60 (-2.35%)</td><td>132.30 (+0.53%)</td><td>29.47 <b>(-58.64%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>299.90 (n/a)</td><td>189.10 (n/a)</td><td>157.30 (n/a)</td><td>131.60 (n/a)</td><td>71.26 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (-0.63%)</td><td>0.24 (+1.31%)</td><td>0.24 (+6.69%)</td><td>0.20 (-5.24%)</td><td>0.04 (+10.11%)</td><td>205.50 (+5.55%)</td><td>175.24 (-0.79%)</td><td>171.20 (-6.24%)</td><td>138.80 (+0.65%)</td><td>27.46 <b>(+21.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>194.70 (n/a)</td><td>176.64 (n/a)</td><td>182.60 (n/a)</td><td>137.90 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 (-11.37%)</td><td>0.19 (-8.47%)</td><td>0.18 (-14.80%)</td><td>0.17 (+4.30%)</td><td>0.02 <b>(-51.27%)</b></td><td>190.10 (-4.09%)</td><td>173.40 (+7.01%)</td><td>179.30 (+17.42%)</td><td>148.50 (+12.84%)</td><td>15.83 <b>(-48.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.20 (n/a)</td><td>162.04 (n/a)</td><td>152.70 (n/a)</td><td>131.60 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 (+17.04%)</td><td>0.21 (+9.64%)</td><td>0.21 (+12.04%)</td><td>0.16 (-6.63%)</td><td>0.04 <b>(+64.16%)</b></td><td>236.70 (+7.10%)</td><td>179.10 (-6.99%)</td><td>179.00 (-10.72%)</td><td>134.70 (-14.53%)</td><td>37.06 <b>(+53.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>221.00 (n/a)</td><td>192.56 (n/a)</td><td>200.50 (n/a)</td><td>157.60 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.25 (+1.83%)</td><td>0.20 (-4.70%)</td><td>0.20 (+5.08%)</td><td>0.16 (-10.69%)</td><td>0.03 (-1.24%)</td><td>199.00 (+11.99%)</td><td>166.02 (+5.02%)</td><td>164.40 (-4.86%)</td><td>130.10 (-1.81%)</td><td>24.66 (+7.79%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.70 (n/a)</td><td>158.08 (n/a)</td><td>172.80 (n/a)</td><td>132.50 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (-2.19%)</td><td>0.19 (-12.45%)</td><td>0.17 <b>(-22.37%)</b></td><td>0.15 (-12.51%)</td><td>0.04 <b>(+36.20%)</b></td><td>239.30 (+14.28%)</td><td>204.58 (+15.95%)</td><td>215.50 <b>(+28.81%)</b></td><td>155.20 (+2.24%)</td><td>36.55 <b>(+59.42%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>209.40 (n/a)</td><td>176.44 (n/a)</td><td>167.30 (n/a)</td><td>151.80 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (-11.32%)</td><td>0.18 (-9.72%)</td><td>0.19 (-6.75%)</td><td>0.16 (-14.50%)</td><td>0.02 (+11.20%)</td><td>206.30 (+16.95%)</td><td>179.16 (+11.07%)</td><td>175.50 (+7.21%)</td><td>163.30 (+12.78%)</td><td>17.44 <b>(+47.05%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>161.30 (n/a)</td><td>163.70 (n/a)</td><td>144.80 (n/a)</td><td>11.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (-6.75%)</td><td>0.19 (-3.21%)</td><td>0.18 (+1.72%)</td><td>0.15 (-5.86%)</td><td>0.03 (-13.05%)</td><td>227.30 (+6.21%)</td><td>191.14 (+2.94%)</td><td>191.60 (-1.69%)</td><td>162.30 (+7.20%)</td><td>29.09 (-3.13%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>214.00 (n/a)</td><td>185.68 (n/a)</td><td>194.90 (n/a)</td><td>151.40 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (-19.84%)</td><td>0.17 (-3.62%)</td><td>0.17 (-1.00%)</td><td>0.16 <b>(+24.94%)</b></td><td>0.02 <b>(-67.78%)</b></td><td>209.00 (-19.95%)</td><td>189.68 (-1.07%)</td><td>193.70 (+0.99%)</td><td>166.30 <b>(+24.76%)</b></td><td>15.78 <b>(-67.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>261.10 (n/a)</td><td>191.74 (n/a)</td><td>191.80 (n/a)</td><td>133.30 (n/a)</td><td>49.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 <b>(+27.54%)</b></td><td>0.18 (+5.69%)</td><td>0.17 (-0.45%)</td><td>0.16 (+0.47%)</td><td>0.03 <b>(+239.47%)</b></td><td>221.20 (-0.45%)</td><td>196.66 (-4.09%)</td><td>202.30 (+0.45%)</td><td>155.60 <b>(-21.61%)</b></td><td>25.62 <b>(+159.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>205.04 (n/a)</td><td>201.40 (n/a)</td><td>198.50 (n/a)</td><td>9.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 (+18.64%)</td><td>0.15 (+12.07%)</td><td>0.17 (+15.96%)</td><td>0.09 (-9.06%)</td><td>0.04 <b>(+41.26%)</b></td><td>385.20 (+9.96%)</td><td>234.06 (-7.21%)</td><td>194.50 (-13.75%)</td><td>171.80 (-15.70%)</td><td>86.62 <b>(+40.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>350.30 (n/a)</td><td>252.26 (n/a)</td><td>225.50 (n/a)</td><td>203.80 (n/a)</td><td>61.87 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (-1.73%)</td><td>0.12 (+0.05%)</td><td>0.12 (-2.97%)</td><td>0.10 (+14.26%)</td><td>0.02 <b>(-27.58%)</b></td><td>200.50 (-12.48%)</td><td>170.66 (-1.82%)</td><td>174.00 (+3.02%)</td><td>138.10 (+1.77%)</td><td>23.37 <b>(-36.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>229.10 (n/a)</td><td>173.82 (n/a)</td><td>168.90 (n/a)</td><td>135.70 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (-0.43%)</td><td>0.11 (-2.05%)</td><td>0.10 (-10.37%)</td><td>0.09 (-8.61%)</td><td>0.02 (+19.49%)</td><td>237.20 (+9.41%)</td><td>187.56 (+3.34%)</td><td>197.50 (+11.58%)</td><td>140.50 (+0.43%)</td><td>38.39 <b>(+29.69%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>181.50 (n/a)</td><td>177.00 (n/a)</td><td>139.90 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.16 (-1.85%)</td><td>0.13 (-1.08%)</td><td>0.13 (-3.06%)</td><td>0.09 (-7.66%)</td><td>0.03 (+4.38%)</td><td>234.80 (+8.30%)</td><td>169.82 (+1.81%)</td><td>159.90 (+3.16%)</td><td>128.70 (+1.90%)</td><td>45.10 (+11.15%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.80 (n/a)</td><td>166.80 (n/a)</td><td>155.00 (n/a)</td><td>126.30 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (+10.82%)</td><td>0.13 (+15.02%)</td><td>0.12 (+18.64%)</td><td>0.12 <b>(+23.20%)</b></td><td>0.02 (-1.70%)</td><td>177.30 (-18.82%)</td><td>160.32 (-13.73%)</td><td>165.00 (-15.69%)</td><td>118.80 (-9.73%)</td><td>24.08 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>185.84 (n/a)</td><td>195.70 (n/a)</td><td>131.60 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (+19.21%)</td><td>0.13 <b>(+20.12%)</b></td><td>0.11 (-11.32%)</td><td>0.10 <b>(+57.93%)</b></td><td>0.03 (-0.15%)</td><td>201.40 <b>(-36.67%)</b></td><td>169.02 <b>(-20.03%)</b></td><td>192.10 (+12.73%)</td><td>123.60 (-16.09%)</td><td>39.46 <b>(-46.87%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>318.00 (n/a)</td><td>211.36 (n/a)</td><td>170.40 (n/a)</td><td>147.30 (n/a)</td><td>74.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (+10.92%)</td><td>0.12 (+8.77%)</td><td>0.11 (+10.22%)</td><td>0.06 <b>(-36.39%)</b></td><td>0.04 <b>(+90.64%)</b></td><td>355.00 <b>(+57.22%)</b></td><td>197.38 (+2.98%)</td><td>178.70 (-9.29%)</td><td>123.40 (-9.86%)</td><td>94.03 <b>(+175.71%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>191.66 (n/a)</td><td>197.00 (n/a)</td><td>136.90 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 <b>(+24.48%)</b></td><td>0.11 (-5.65%)</td><td>0.12 (-0.87%)</td><td>0.06 <b>(-35.71%)</b></td><td>0.04 <b>(+136.25%)</b></td><td>316.90 <b>(+55.57%)</b></td><td>205.22 (+16.73%)</td><td>174.20 (+0.87%)</td><td>120.00 (-19.68%)</td><td>78.28 <b>(+200.38%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>203.70 (n/a)</td><td>175.80 (n/a)</td><td>172.70 (n/a)</td><td>149.40 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 <b>(+28.46%)</b></td><td>0.11 (+1.14%)</td><td>0.10 (-10.70%)</td><td>0.09 (-9.82%)</td><td>0.03 <b>(+142.61%)</b></td><td>227.80 (+10.91%)</td><td>189.12 (+3.40%)</td><td>205.10 (+11.95%)</td><td>119.20 <b>(-22.19%)</b></td><td>44.62 <b>(+105.94%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>182.90 (n/a)</td><td>183.20 (n/a)</td><td>153.20 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 <b>(+24.40%)</b></td><td>0.16 (+15.32%)</td><td>0.16 <b>(+20.80%)</b></td><td>0.12 (+9.55%)</td><td>0.03 <b>(+79.04%)</b></td><td>201.00 (-8.72%)</td><td>164.02 (-11.42%)</td><td>155.50 (-17.20%)</td><td>121.10 (-19.64%)</td><td>34.44 <b>(+37.17%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.20 (n/a)</td><td>185.16 (n/a)</td><td>187.80 (n/a)</td><td>150.70 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 (-0.41%)</td><td>0.15 <b>(+26.78%)</b></td><td>0.17 <b>(+42.01%)</b></td><td>0.11 <b>(+62.11%)</b></td><td>0.03 <b>(-20.59%)</b></td><td>231.60 <b>(-38.31%)</b></td><td>172.32 <b>(-25.83%)</b></td><td>147.10 <b>(-29.58%)</b></td><td>137.30 (+0.37%)</td><td>42.08 <b>(-52.31%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>375.40 (n/a)</td><td>232.34 (n/a)</td><td>208.90 (n/a)</td><td>136.80 (n/a)</td><td>88.23 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 <b>(+60.84%)</b></td><td>0.15 <b>(+35.48%)</b></td><td>0.14 <b>(+22.38%)</b></td><td>0.10 <b>(+22.68%)</b></td><td>0.03 <b>(+115.01%)</b></td><td>247.00 (-18.48%)</td><td>175.22 <b>(-24.14%)</b></td><td>174.40 (-18.28%)</td><td>127.00 <b>(-37.81%)</b></td><td>45.17 (+9.26%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>303.00 (n/a)</td><td>230.98 (n/a)</td><td>213.40 (n/a)</td><td>204.20 (n/a)</td><td>41.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.17 (+8.37%)</td><td>0.15 (+10.65%)</td><td>0.16 (+17.86%)</td><td>0.11 (+0.81%)</td><td>0.03 <b>(+44.58%)</b></td><td>227.30 (-0.83%)</td><td>170.78 (-8.44%)</td><td>156.50 (-15.18%)</td><td>144.80 (-7.71%)</td><td>34.47 <b>(+29.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>186.52 (n/a)</td><td>184.50 (n/a)</td><td>156.90 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.19 <b>(+22.27%)</b></td><td>0.15 (+11.41%)</td><td>0.14 (-3.81%)</td><td>0.12 (+2.05%)</td><td>0.03 <b>(+101.42%)</b></td><td>198.50 (-2.02%)</td><td>164.86 (-8.02%)</td><td>179.80 (+3.99%)</td><td>128.20 (-18.24%)</td><td>33.84 <b>(+53.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>179.24 (n/a)</td><td>172.90 (n/a)</td><td>156.80 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 <b>(+24.70%)</b></td><td>0.16 <b>(+21.22%)</b></td><td>0.14 (+1.83%)</td><td>0.13 <b>(+32.69%)</b></td><td>0.04 <b>(+56.78%)</b></td><td>194.80 <b>(-24.64%)</b></td><td>157.52 (-16.41%)</td><td>172.70 (-1.76%)</td><td>118.20 (-19.81%)</td><td>36.60 (-12.49%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>258.50 (n/a)</td><td>188.44 (n/a)</td><td>175.80 (n/a)</td><td>147.40 (n/a)</td><td>41.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 (+7.63%)</td><td>0.14 (-2.58%)</td><td>0.14 (+0.42%)</td><td>0.12 (+3.75%)</td><td>0.03 (+2.30%)</td><td>212.10 (-3.59%)</td><td>177.68 (+2.40%)</td><td>177.50 (-0.39%)</td><td>124.20 (-7.11%)</td><td>33.32 (-9.07%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>220.00 (n/a)</td><td>173.52 (n/a)</td><td>178.20 (n/a)</td><td>133.70 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.15 (-11.55%)</td><td>0.13 (-4.59%)</td><td>0.11 (-9.90%)</td><td>0.10 (+4.64%)</td><td>0.03 <b>(-25.20%)</b></td><td>245.70 (-4.43%)</td><td>202.58 (+2.49%)</td><td>220.00 (+11.00%)</td><td>159.20 (+13.07%)</td><td>39.86 <b>(-21.82%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>257.10 (n/a)</td><td>197.66 (n/a)</td><td>198.20 (n/a)</td><td>140.80 (n/a)</td><td>50.99 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.12 <b>(-28.45%)</b></td><td>0.10 (-3.33%)</td><td>0.11 (+6.36%)</td><td>0.09 <b>(+88.35%)</b></td><td>0.01 <b>(-73.89%)</b></td><td>214.70 <b>(-46.92%)</b></td><td>180.68 (-12.96%)</td><td>173.20 (-6.02%)</td><td>157.90 <b>(+39.73%)</b></td><td>21.24 <b>(-81.49%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>404.50 (n/a)</td><td>207.58 (n/a)</td><td>184.30 (n/a)</td><td>113.00 (n/a)</td><td>114.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (+7.02%)</td><td>0.10 (+0.15%)</td><td>0.10 (+4.12%)</td><td>0.08 (-7.22%)</td><td>0.02 <b>(+22.92%)</b></td><td>241.20 (+7.77%)</td><td>193.60 (+0.95%)</td><td>191.00 (-3.97%)</td><td>136.20 (-6.58%)</td><td>38.32 (+19.87%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.80 (n/a)</td><td>191.78 (n/a)</td><td>198.90 (n/a)</td><td>145.80 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 (-6.10%)</td><td>0.11 (+4.43%)</td><td>0.11 (+5.47%)</td><td>0.10 (+19.50%)</td><td>0.01 <b>(-35.94%)</b></td><td>187.10 (-16.29%)</td><td>166.42 (-6.23%)</td><td>168.80 (-5.17%)</td><td>144.40 (+6.49%)</td><td>20.73 <b>(-42.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>223.50 (n/a)</td><td>177.48 (n/a)</td><td>178.00 (n/a)</td><td>135.60 (n/a)</td><td>36.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (-0.26%)</td><td>0.11 (+1.32%)</td><td>0.10 (-2.08%)</td><td>0.09 (+18.13%)</td><td>0.02 (-14.89%)</td><td>205.70 (-15.35%)</td><td>175.92 (-2.73%)</td><td>188.40 (+2.11%)</td><td>136.40 (+0.29%)</td><td>29.59 <b>(-27.83%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>180.86 (n/a)</td><td>184.50 (n/a)</td><td>136.00 (n/a)</td><td>41.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-6.19%)</td><td>0.10 (-4.42%)</td><td>0.10 (+2.96%)</td><td>0.07 <b>(-24.20%)</b></td><td>0.02 <b>(+54.15%)</b></td><td>258.80 <b>(+31.91%)</b></td><td>194.06 (+6.52%)</td><td>185.00 (-2.89%)</td><td>164.80 (+6.60%)</td><td>37.62 <b>(+124.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>182.18 (n/a)</td><td>190.50 (n/a)</td><td>154.60 (n/a)</td><td>16.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.13 <b>(+26.62%)</b></td><td>0.11 (+17.43%)</td><td>0.11 <b>(+20.77%)</b></td><td>0.09 (+1.71%)</td><td>0.01 <b>(+150.29%)</b></td><td>203.60 (-1.69%)</td><td>167.66 (-13.81%)</td><td>165.40 (-17.22%)</td><td>142.50 <b>(-21.01%)</b></td><td>23.61 <b>(+96.32%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>194.52 (n/a)</td><td>199.80 (n/a)</td><td>180.40 (n/a)</td><td>12.03 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.11 (-13.31%)</td><td>0.09 (-4.51%)</td><td>0.09 (-4.00%)</td><td>0.08 (+5.10%)</td><td>0.01 <b>(-41.52%)</b></td><td>221.20 (-4.82%)</td><td>197.84 (+3.15%)</td><td>207.00 (+4.18%)</td><td>168.90 (+15.37%)</td><td>21.15 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>232.40 (n/a)</td><td>191.80 (n/a)</td><td>198.70 (n/a)</td><td>146.40 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 (+11.83%)</td><td>0.10 (+6.84%)</td><td>0.10 (-4.25%)</td><td>0.08 <b>(+45.61%)</b></td><td>0.03 (-8.30%)</td><td>237.90 <b>(-31.32%)</b></td><td>186.44 (-10.61%)</td><td>181.70 (+4.49%)</td><td>127.30 (-10.60%)</td><td>44.31 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>346.40 (n/a)</td><td>208.58 (n/a)</td><td>173.90 (n/a)</td><td>142.40 (n/a)</td><td>81.47 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.67 (+2.66%)</td><td>0.52 (-2.61%)</td><td>0.50 (-4.28%)</td><td>0.45 (-3.02%)</td><td>0.09 <b>(+27.30%)</b></td><td>219.70 (+3.10%)</td><td>192.52 (+3.49%)</td><td>198.20 (+4.48%)</td><td>147.50 (-2.58%)</td><td>28.69 <b>(+29.53%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.07 (n/a)</td><td>213.10 (n/a)</td><td>186.02 (n/a)</td><td>189.70 (n/a)</td><td>151.40 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.66 (-2.47%)</td><td>0.54 (-4.86%)</td><td>0.53 (-1.16%)</td><td>0.43 (-7.40%)</td><td>0.10 (-1.19%)</td><td>227.40 (+7.98%)</td><td>187.08 (+5.37%)</td><td>184.20 (+1.15%)</td><td>149.00 (+2.48%)</td><td>34.94 (+12.22%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.68 (n/a)</td><td>0.57 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.10 (n/a)</td><td>210.60 (n/a)</td><td>177.54 (n/a)</td><td>182.10 (n/a)</td><td>145.40 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.79 <b>(+30.19%)</b></td><td>0.65 (+19.21%)</td><td>0.61 (+10.53%)</td><td>0.51 (+8.11%)</td><td>0.13 <b>(+112.45%)</b></td><td>192.20 (-7.51%)</td><td>157.24 (-14.33%)</td><td>160.70 (-9.52%)</td><td>125.20 <b>(-23.19%)</b></td><td>30.60 <b>(+46.54%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.60 (n/a)</td><td>0.54 (n/a)</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.06 (n/a)</td><td>207.80 (n/a)</td><td>183.54 (n/a)</td><td>177.60 (n/a)</td><td>163.00 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.61 (+3.10%)</td><td>0.54 (+4.15%)</td><td>0.55 (+0.64%)</td><td>0.43 (+12.99%)</td><td>0.08 (-9.99%)</td><td>228.40 (-11.47%)</td><td>185.26 (-4.74%)</td><td>177.60 (-0.62%)</td><td>159.90 (-3.03%)</td><td>28.10 <b>(-24.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>258.00 (n/a)</td><td>194.48 (n/a)</td><td>178.70 (n/a)</td><td>164.90 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.42 (-14.73%)</td><td>0.41 (+0.57%)</td><td>0.42 (-2.05%)</td><td>0.39 <b>(+31.90%)</b></td><td>0.01 <b>(-83.87%)</b></td><td>187.20 <b>(-24.18%)</b></td><td>179.02 (-3.40%)</td><td>177.00 (+2.08%)</td><td>174.40 (+17.28%)</td><td>5.29 <b>(-86.00%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>246.90 (n/a)</td><td>185.32 (n/a)</td><td>173.40 (n/a)</td><td>148.70 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.56 (+3.71%)</td><td>0.47 (+12.45%)</td><td>0.48 (+15.85%)</td><td>0.36 (+4.34%)</td><td>0.08 (+0.21%)</td><td>204.90 (-4.16%)</td><td>160.78 (-11.15%)</td><td>154.80 (-13.71%)</td><td>130.80 (-3.61%)</td><td>28.11 (-3.56%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>213.80 (n/a)</td><td>180.96 (n/a)</td><td>179.40 (n/a)</td><td>135.70 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.67 <b>(+68.60%)</b></td><td>0.48 <b>(+36.91%)</b></td><td>0.43 (+16.14%)</td><td>0.36 <b>(+31.77%)</b></td><td>0.13 <b>(+179.43%)</b></td><td>202.50 <b>(-24.10%)</b></td><td>161.56 <b>(-24.01%)</b></td><td>169.60 (-13.91%)</td><td>110.80 <b>(-40.72%)</b></td><td>40.61 <b>(+25.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>266.80 (n/a)</td><td>212.62 (n/a)</td><td>197.00 (n/a)</td><td>186.90 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.54 (+16.91%)</td><td>0.44 (+11.08%)</td><td>0.44 <b>(+20.96%)</b></td><td>0.32 (-4.18%)</td><td>0.08 <b>(+44.75%)</b></td><td>227.60 (+4.36%)</td><td>173.54 (-8.80%)</td><td>166.30 (-17.35%)</td><td>136.30 (-14.49%)</td><td>33.70 <b>(+33.65%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>218.10 (n/a)</td><td>190.28 (n/a)</td><td>201.20 (n/a)</td><td>159.40 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (-12.21%)</td><td>0.20 (-8.53%)</td><td>0.19 (-10.86%)</td><td>0.17 (-9.17%)</td><td>0.02 <b>(-29.59%)</b></td><td>219.20 (+10.10%)</td><td>190.24 (+8.65%)</td><td>189.90 (+12.17%)</td><td>161.30 (+13.91%)</td><td>20.76 (-14.02%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>199.10 (n/a)</td><td>175.10 (n/a)</td><td>169.30 (n/a)</td><td>141.60 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 (+13.59%)</td><td>0.22 (+3.02%)</td><td>0.21 (+7.05%)</td><td>0.17 (+2.66%)</td><td>0.05 (+9.75%)</td><td>217.50 (-2.60%)</td><td>174.60 (-2.89%)</td><td>178.10 (-6.61%)</td><td>123.60 (-11.97%)</td><td>33.57 (-6.39%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>179.80 (n/a)</td><td>190.70 (n/a)</td><td>140.40 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 <b>(+45.25%)</b></td><td>0.23 <b>(+20.87%)</b></td><td>0.22 (+13.25%)</td><td>0.16 (-10.94%)</td><td>0.06 <b>(+593.41%)</b></td><td>235.70 (+12.29%)</td><td>169.74 (-12.96%)</td><td>170.20 (-11.68%)</td><td>128.40 <b>(-31.15%)</b></td><td>44.47 <b>(+406.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>195.02 (n/a)</td><td>192.70 (n/a)</td><td>186.50 (n/a)</td><td>8.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (-16.85%)</td><td>0.16 (-19.23%)</td><td>0.14 <b>(-21.47%)</b></td><td>0.09 <b>(-41.34%)</b></td><td>0.07 <b>(+34.51%)</b></td><td>392.40 <b>(+70.46%)</b></td><td>268.52 <b>(+38.30%)</b></td><td>254.90 <b>(+27.32%)</b></td><td>154.40 <b>(+20.25%)</b></td><td>112.98 <b>(+189.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>230.20 (n/a)</td><td>194.16 (n/a)</td><td>200.20 (n/a)</td><td>128.40 (n/a)</td><td>39.00 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (+4.34%)</td><td>0.22 (-8.37%)</td><td>0.21 (-16.95%)</td><td>0.15 (-11.14%)</td><td>0.05 <b>(+35.37%)</b></td><td>238.30 (+12.56%)</td><td>176.72 (+11.38%)</td><td>177.20 <b>(+20.38%)</b></td><td>130.40 (-4.12%)</td><td>42.12 <b>(+39.45%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>211.70 (n/a)</td><td>158.66 (n/a)</td><td>147.20 (n/a)</td><td>136.00 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.30 <b>(+34.09%)</b></td><td>0.22 (+10.71%)</td><td>0.21 (+3.39%)</td><td>0.15 (-13.46%)</td><td>0.06 <b>(+164.98%)</b></td><td>247.20 (+15.57%)</td><td>176.56 (-5.50%)</td><td>177.10 (-3.28%)</td><td>121.70 <b>(-25.43%)</b></td><td>46.74 <b>(+128.03%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>213.90 (n/a)</td><td>186.84 (n/a)</td><td>183.10 (n/a)</td><td>163.20 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 <b>(-25.86%)</b></td><td>0.18 (-18.65%)</td><td>0.17 (-10.72%)</td><td>0.15 (-11.47%)</td><td>0.03 <b>(-48.54%)</b></td><td>249.30 (+12.96%)</td><td>212.00 <b>(+20.06%)</b></td><td>213.60 (+12.01%)</td><td>171.20 <b>(+34.80%)</b></td><td>29.69 <b>(-21.01%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>220.70 (n/a)</td><td>176.58 (n/a)</td><td>190.70 (n/a)</td><td>127.00 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.20 <b>(-32.57%)</b></td><td>0.17 (-17.83%)</td><td>0.17 (-19.04%)</td><td>0.15 (+4.49%)</td><td>0.02 <b>(-69.69%)</b></td><td>246.70 (-4.31%)</td><td>217.82 (+13.71%)</td><td>212.50 <b>(+23.47%)</b></td><td>184.80 <b>(+48.31%)</b></td><td>24.20 <b>(-59.05%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>257.80 (n/a)</td><td>191.56 (n/a)</td><td>172.10 (n/a)</td><td>124.60 (n/a)</td><td>59.11 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.34 <b>(+20.21%)</b></td><td>0.26 <b>(+20.23%)</b></td><td>0.23 (+6.34%)</td><td>0.19 <b>(+49.09%)</b></td><td>0.07 (+19.32%)</td><td>219.20 <b>(-32.95%)</b></td><td>170.16 (-18.22%)</td><td>174.70 (-5.97%)</td><td>120.20 (-16.82%)</td><td>45.01 <b>(-36.61%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>326.90 (n/a)</td><td>208.06 (n/a)</td><td>185.80 (n/a)</td><td>144.50 (n/a)</td><td>71.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.31 (+3.04%)</td><td>0.26 (+12.89%)</td><td>0.28 (+19.86%)</td><td>0.19 (+4.88%)</td><td>0.05 (+18.64%)</td><td>213.60 (-4.64%)</td><td>164.66 (-10.67%)</td><td>147.10 (-16.61%)</td><td>133.20 (-2.99%)</td><td>36.90 (+8.36%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>224.00 (n/a)</td><td>184.32 (n/a)</td><td>176.40 (n/a)</td><td>137.30 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.33 (-6.16%)</td><td>0.26 (+11.90%)</td><td>0.23 (+11.74%)</td><td>0.21 (+9.71%)</td><td>0.06 (-14.53%)</td><td>191.30 (-8.86%)</td><td>162.30 (-11.79%)</td><td>178.90 (-10.51%)</td><td>123.10 (+6.58%)</td><td>33.31 (-14.08%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>209.90 (n/a)</td><td>184.00 (n/a)</td><td>199.90 (n/a)</td><td>115.50 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.32 (+19.89%)</td><td>0.24 (+9.13%)</td><td>0.22 (-1.53%)</td><td>0.17 (+3.65%)</td><td>0.06 <b>(+49.99%)</b></td><td>235.50 (-3.52%)</td><td>178.70 (-6.72%)</td><td>185.10 (+1.59%)</td><td>126.60 (-16.60%)</td><td>40.21 (+17.70%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>244.10 (n/a)</td><td>191.58 (n/a)</td><td>182.20 (n/a)</td><td>151.80 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (+6.65%)</td><td>0.23 (+4.11%)</td><td>0.25 (+10.61%)</td><td>0.20 (+2.49%)</td><td>0.03 <b>(+42.73%)</b></td><td>202.90 (-2.41%)</td><td>177.34 (-3.42%)</td><td>166.10 (-9.63%)</td><td>155.60 (-6.21%)</td><td>21.49 <b>(+32.48%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>183.62 (n/a)</td><td>183.80 (n/a)</td><td>165.90 (n/a)</td><td>16.22 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (+9.00%)</td><td>0.23 <b>(+20.80%)</b></td><td>0.25 <b>(+30.33%)</b></td><td>0.18 <b>(+29.19%)</b></td><td>0.03 (-3.47%)</td><td>224.80 <b>(-22.59%)</b></td><td>180.82 (-18.09%)</td><td>164.10 <b>(-23.28%)</b></td><td>158.50 (-8.22%)</td><td>29.60 <b>(-33.66%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>290.40 (n/a)</td><td>220.76 (n/a)</td><td>213.90 (n/a)</td><td>172.70 (n/a)</td><td>44.62 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 (-17.72%)</td><td>0.22 (-14.60%)</td><td>0.21 <b>(-21.73%)</b></td><td>0.19 <b>(+49.82%)</b></td><td>0.03 <b>(-64.57%)</b></td><td>214.90 <b>(-33.26%)</b></td><td>191.42 (+5.87%)</td><td>193.60 <b>(+27.70%)</b></td><td>156.70 <b>(+21.57%)</b></td><td>22.11 <b>(-72.58%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>322.00 (n/a)</td><td>180.80 (n/a)</td><td>151.60 (n/a)</td><td>128.90 (n/a)</td><td>80.65 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (-12.61%)</td><td>0.20 <b>(-20.98%)</b></td><td>0.21 (-19.43%)</td><td>0.13 <b>(-36.46%)</b></td><td>0.05 (+18.64%)</td><td>313.90 <b>(+57.34%)</b></td><td>216.04 <b>(+31.19%)</b></td><td>199.20 <b>(+24.11%)</b></td><td>147.10 (+14.39%)</td><td>62.00 <b>(+115.90%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>199.50 (n/a)</td><td>164.68 (n/a)</td><td>160.50 (n/a)</td><td>128.60 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.21 (-15.69%)</td><td>0.18 (-16.21%)</td><td>0.17 (-15.53%)</td><td>0.12 <b>(-33.72%)</b></td><td>0.04 <b>(+25.54%)</b></td><td>297.30 <b>(+50.84%)</b></td><td>207.70 <b>(+22.77%)</b></td><td>201.80 (+18.36%)</td><td>166.40 (+18.60%)</td><td>53.49 <b>(+123.78%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>197.10 (n/a)</td><td>169.18 (n/a)</td><td>170.50 (n/a)</td><td>140.30 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.23 (-4.10%)</td><td>0.20 (+10.68%)</td><td>0.20 (+14.59%)</td><td>0.18 (+13.73%)</td><td>0.02 <b>(-40.65%)</b></td><td>193.30 (-12.10%)</td><td>173.00 (-10.96%)</td><td>172.30 (-12.76%)</td><td>152.80 (+4.23%)</td><td>16.27 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>219.90 (n/a)</td><td>194.30 (n/a)</td><td>197.50 (n/a)</td><td>146.60 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.29 <b>(+21.09%)</b></td><td>0.25 <b>(+20.57%)</b></td><td>0.27 <b>(+40.25%)</b></td><td>0.18 (+7.48%)</td><td>0.05 <b>(+60.10%)</b></td><td>192.50 (-6.96%)</td><td>147.54 (-15.48%)</td><td>130.20 <b>(-28.70%)</b></td><td>119.70 (-17.45%)</td><td>33.45 <b>(+24.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>206.90 (n/a)</td><td>174.56 (n/a)</td><td>182.60 (n/a)</td><td>145.00 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.27 <b>(+23.47%)</b></td><td>0.21 (+6.99%)</td><td>0.20 (-0.18%)</td><td>0.18 (+1.78%)</td><td>0.04 <b>(+106.53%)</b></td><td>197.80 (-1.74%)</td><td>169.18 (-4.89%)</td><td>171.60 (+0.18%)</td><td>127.80 (-18.96%)</td><td>28.22 <b>(+63.30%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>201.30 (n/a)</td><td>177.88 (n/a)</td><td>171.30 (n/a)</td><td>157.70 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.26 <b>(+22.20%)</b></td><td>0.21 (+16.50%)</td><td>0.19 (+5.19%)</td><td>0.17 (+18.82%)</td><td>0.04 <b>(+45.39%)</b></td><td>201.10 (-15.82%)</td><td>168.16 (-13.52%)</td><td>180.00 (-4.96%)</td><td>134.50 (-18.19%)</td><td>28.88 (-2.08%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>238.90 (n/a)</td><td>194.46 (n/a)</td><td>189.40 (n/a)</td><td>164.40 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.24 (+7.22%)</td><td>0.19 (-6.76%)</td><td>0.21 (+4.10%)</td><td>0.10 <b>(-43.59%)</b></td><td>0.06 <b>(+182.08%)</b></td><td>362.00 <b>(+77.28%)</b></td><td>209.96 (+19.20%)</td><td>162.40 (-3.91%)</td><td>146.30 (-6.76%)</td><td>90.78 <b>(+363.79%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>176.14 (n/a)</td><td>169.00 (n/a)</td><td>156.90 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (+18.94%)</td><td>0.20 (+14.12%)</td><td>0.20 (+14.61%)</td><td>0.14 <b>(+32.25%)</b></td><td>0.05 (+12.44%)</td><td>250.50 <b>(-24.37%)</b></td><td>188.30 (-13.52%)</td><td>176.20 (-12.73%)</td><td>126.50 (-15.89%)</td><td>50.69 <b>(-28.28%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>331.20 (n/a)</td><td>217.74 (n/a)</td><td>201.90 (n/a)</td><td>150.40 (n/a)</td><td>70.67 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.18 <b>(-21.18%)</b></td><td>0.17 (-5.60%)</td><td>0.16 (-2.93%)</td><td>0.16 (+11.63%)</td><td>0.01 <b>(-75.40%)</b></td><td>216.10 (-10.41%)</td><td>209.04 (+3.71%)</td><td>214.20 (+3.03%)</td><td>194.60 <b>(+26.86%)</b></td><td>9.37 <b>(-71.26%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.20 (n/a)</td><td>201.56 (n/a)</td><td>207.90 (n/a)</td><td>153.40 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.81 (-11.13%)</td><td>0.70 (-2.72%)</td><td>0.65 (-8.46%)</td><td>0.62 (+3.88%)</td><td>0.08 <b>(-36.34%)</b></td><td>210.60 (-3.70%)</td><td>190.26 (+1.48%)</td><td>200.40 (+9.27%)</td><td>162.30 (+12.55%)</td><td>20.85 <b>(-32.04%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.91 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.60 (n/a)</td><td>0.13 (n/a)</td><td>218.70 (n/a)</td><td>187.48 (n/a)</td><td>183.40 (n/a)</td><td>144.20 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.92 (-19.45%)</td><td>0.77 (-1.18%)</td><td>0.72 (-6.76%)</td><td>0.59 (+15.20%)</td><td>0.14 <b>(-44.62%)</b></td><td>221.00 (-13.20%)</td><td>175.10 (-4.01%)</td><td>181.50 (+7.27%)</td><td>142.60 <b>(+24.22%)</b></td><td>32.10 <b>(-42.76%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.14 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.51 (n/a)</td><td>0.25 (n/a)</td><td>254.60 (n/a)</td><td>182.42 (n/a)</td><td>169.20 (n/a)</td><td>114.80 (n/a)</td><td>56.08 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.94 (-9.53%)</td><td>0.75 (-2.37%)</td><td>0.71 (+7.24%)</td><td>0.63 (+3.52%)</td><td>0.12 <b>(-39.42%)</b></td><td>206.60 (-3.41%)</td><td>177.46 (-0.57%)</td><td>184.70 (-6.72%)</td><td>139.50 (+10.54%)</td><td>25.93 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.04 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.61 (n/a)</td><td>0.20 (n/a)</td><td>213.90 (n/a)</td><td>178.48 (n/a)</td><td>198.00 (n/a)</td><td>126.20 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.00 (+2.33%)</td><td>0.00 (+1.42%)</td><td>0.00 (+4.76%)</td><td>0.00 (-4.76%)</td><td>0.00 <b>(+216.23%)</b></td><td>1017.55 (+3.41%)</td><td>956.02 (-1.67%)</td><td>937.90 (-3.80%)</td><td>935.89 (-2.47%)</td><td>34.97 <b>(+189.67%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>983.98 (n/a)</td><td>972.27 (n/a)</td><td>974.97 (n/a)</td><td>959.59 (n/a)</td><td>12.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.01 (-2.35%)</td><td>0.01 (-0.73%)</td><td>0.01 (-3.57%)</td><td>0.01 (+3.85%)</td><td>0.00 <b>(-61.98%)</b></td><td>1013.16 (-2.96%)</td><td>999.40 (+0.49%)</td><td>1005.68 (+2.54%)</td><td>985.16 (+2.70%)</td><td>12.61 <b>(-62.89%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1044.06 (n/a)</td><td>994.57 (n/a)</td><td>980.77 (n/a)</td><td>959.25 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.97 (+3.65%)</td><td>0.96 (+2.96%)</td><td>0.96 (+3.08%)</td><td>0.95 (+2.41%)</td><td>0.01 <b>(+98.35%)</b></td><td>2214.31 (-2.35%)</td><td>2189.61 (-2.86%)</td><td>2190.41 (-2.99%)</td><td>2159.10 (-3.52%)</td><td>22.77 <b>(+86.44%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.92 (n/a)</td><td>0.01 (n/a)</td><td>2267.71 (n/a)</td><td>2254.15 (n/a)</td><td>2257.93 (n/a)</td><td>2237.80 (n/a)</td><td>12.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.44 (-1.28%)</td><td>0.43 (-0.91%)</td><td>0.44 (+0.05%)</td><td>0.42 (-2.10%)</td><td>0.01 <b>(+25.82%)</b></td><td>1234.28 (+2.15%)</td><td>1206.77 (+0.92%)</td><td>1199.35 (-0.07%)</td><td>1194.63 (+1.31%)</td><td>16.10 <b>(+30.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.00 (n/a)</td><td>1208.31 (n/a)</td><td>1195.78 (n/a)</td><td>1200.15 (n/a)</td><td>1179.22 (n/a)</td><td>12.34 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.38 (+0.97%)</td><td>0.37 (+0.47%)</td><td>0.37 (+1.04%)</td><td>0.36 (-0.63%)</td><td>0.01 <b>(+66.68%)</b></td><td>1449.74 (+0.61%)</td><td>1420.83 (-0.47%)</td><td>1415.03 (-1.02%)</td><td>1397.40 (-0.95%)</td><td>20.71 <b>(+65.39%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1440.88 (n/a)</td><td>1427.48 (n/a)</td><td>1429.66 (n/a)</td><td>1410.77 (n/a)</td><td>12.52 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.38 (+3.70%)</td><td>0.38 (+4.67%)</td><td>0.37 (+4.16%)</td><td>0.37 (+5.12%)</td><td>0.00 <b>(-25.42%)</b></td><td>1409.64 (-4.89%)</td><td>1395.23 (-4.48%)</td><td>1405.29 (-4.00%)</td><td>1374.71 (-3.55%)</td><td>16.08 <b>(-32.29%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.01 (n/a)</td><td>1482.07 (n/a)</td><td>1460.73 (n/a)</td><td>1463.88 (n/a)</td><td>1425.32 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.79 <b>(-22.64%)</b></td><td>4.16 (-16.28%)</td><td>4.26 (-17.51%)</td><td>2.80 <b>(-32.32%)</b></td><td>0.81 (-3.18%)</td><td>374.40 <b>(+47.75%)</b></td><td>261.78 <b>(+21.49%)</b></td><td>246.30 <b>(+21.21%)</b></td><td>218.90 <b>(+29.30%)</b></td><td>64.62 <b>(+83.55%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>6.19 (n/a)</td><td>4.97 (n/a)</td><td>5.16 (n/a)</td><td>4.14 (n/a)</td><td>0.84 (n/a)</td><td>253.40 (n/a)</td><td>215.48 (n/a)</td><td>203.20 (n/a)</td><td>169.30 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.71 (-13.42%)</td><td>4.26 (-10.68%)</td><td>4.39 (-13.13%)</td><td>3.66 (-8.56%)</td><td>0.41 <b>(-38.82%)</b></td><td>286.60 (+9.35%)</td><td>248.22 (+10.97%)</td><td>238.90 (+15.13%)</td><td>222.40 (+15.47%)</td><td>25.15 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.44 (n/a)</td><td>4.77 (n/a)</td><td>5.05 (n/a)</td><td>4.00 (n/a)</td><td>0.67 (n/a)</td><td>262.10 (n/a)</td><td>223.68 (n/a)</td><td>207.50 (n/a)</td><td>192.60 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>4.76 (-14.91%)</td><td>4.41 (-12.12%)</td><td>4.50 (-11.40%)</td><td>3.99 (-11.63%)</td><td>0.37 <b>(-22.49%)</b></td><td>262.90 (+13.17%)</td><td>239.24 (+13.60%)</td><td>232.80 (+12.85%)</td><td>220.50 (+17.54%)</td><td>20.65 (+1.58%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.59 (n/a)</td><td>5.02 (n/a)</td><td>5.08 (n/a)</td><td>4.51 (n/a)</td><td>0.48 (n/a)</td><td>232.30 (n/a)</td><td>210.60 (n/a)</td><td>206.30 (n/a)</td><td>187.60 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>5.66 (+10.51%)</td><td>5.19 (+13.82%)</td><td>5.46 <b>(+23.78%)</b></td><td>4.55 (+7.16%)</td><td>0.54 <b>(+47.71%)</b></td><td>230.70 (-6.67%)</td><td>204.08 (-11.77%)</td><td>192.10 (-19.22%)</td><td>185.40 (-9.52%)</td><td>22.19 <b>(+24.58%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.12 (n/a)</td><td>4.56 (n/a)</td><td>4.41 (n/a)</td><td>4.24 (n/a)</td><td>0.37 (n/a)</td><td>247.20 (n/a)</td><td>231.30 (n/a)</td><td>237.80 (n/a)</td><td>204.90 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.60 (+7.29%)</td><td>7.76 (+9.54%)</td><td>7.54 (+3.48%)</td><td>7.01 (+17.65%)</td><td>0.61 <b>(-23.26%)</b></td><td>299.20 (-15.00%)</td><td>271.62 (-9.23%)</td><td>278.00 (-3.37%)</td><td>243.80 (-6.80%)</td><td>21.07 <b>(-39.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.02 (n/a)</td><td>7.08 (n/a)</td><td>7.29 (n/a)</td><td>5.96 (n/a)</td><td>0.79 (n/a)</td><td>352.00 (n/a)</td><td>299.24 (n/a)</td><td>287.70 (n/a)</td><td>261.60 (n/a)</td><td>35.10 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.44 (+1.40%)</td><td>7.36 (-3.03%)</td><td>7.46 (-5.00%)</td><td>5.74 (-10.04%)</td><td>1.00 <b>(+37.00%)</b></td><td>365.30 (+11.17%)</td><td>289.96 (+4.03%)</td><td>281.30 (+5.28%)</td><td>248.50 (-1.39%)</td><td>44.67 <b>(+51.41%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.32 (n/a)</td><td>7.59 (n/a)</td><td>7.85 (n/a)</td><td>6.38 (n/a)</td><td>0.73 (n/a)</td><td>328.60 (n/a)</td><td>278.74 (n/a)</td><td>267.20 (n/a)</td><td>252.00 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.29 (-10.71%)</td><td>7.70 (-3.82%)</td><td>7.57 (-3.20%)</td><td>6.81 (-3.39%)</td><td>0.61 <b>(-33.22%)</b></td><td>307.90 (+3.50%)</td><td>273.86 (+3.47%)</td><td>277.10 (+3.32%)</td><td>252.90 (+12.00%)</td><td>22.53 <b>(-23.47%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.29 (n/a)</td><td>8.00 (n/a)</td><td>7.82 (n/a)</td><td>7.05 (n/a)</td><td>0.92 (n/a)</td><td>297.50 (n/a)</td><td>264.68 (n/a)</td><td>268.20 (n/a)</td><td>225.80 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>10.51 (+6.93%)</td><td>8.56 (-1.44%)</td><td>8.53 (+2.17%)</td><td>7.02 (-11.09%)</td><td>1.28 <b>(+51.27%)</b></td><td>298.90 (+12.50%)</td><td>249.42 (+2.47%)</td><td>246.00 (-2.11%)</td><td>199.50 (-6.51%)</td><td>36.21 <b>(+57.75%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.83 (n/a)</td><td>8.68 (n/a)</td><td>8.35 (n/a)</td><td>7.89 (n/a)</td><td>0.85 (n/a)</td><td>265.70 (n/a)</td><td>243.40 (n/a)</td><td>251.30 (n/a)</td><td>213.40 (n/a)</td><td>22.95 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.97 (+0.06%)</td><td>8.04 (-3.78%)</td><td>7.74 (-7.44%)</td><td>7.52 (-1.90%)</td><td>0.61 (+5.75%)</td><td>278.90 (+1.94%)</td><td>262.08 (+3.99%)</td><td>270.80 (+8.02%)</td><td>233.90 (-0.04%)</td><td>19.13 (+8.46%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>8.96 (n/a)</td><td>8.35 (n/a)</td><td>8.37 (n/a)</td><td>7.67 (n/a)</td><td>0.58 (n/a)</td><td>273.60 (n/a)</td><td>252.02 (n/a)</td><td>250.70 (n/a)</td><td>234.00 (n/a)</td><td>17.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>9.39 (-0.94%)</td><td>8.30 (-2.01%)</td><td>8.23 (-5.54%)</td><td>7.42 (-0.83%)</td><td>0.72 (-9.36%)</td><td>282.60 (+0.82%)</td><td>254.20 (+1.92%)</td><td>254.70 (+5.86%)</td><td>223.40 (+0.95%)</td><td>21.63 (-9.08%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>9.48 (n/a)</td><td>8.47 (n/a)</td><td>8.72 (n/a)</td><td>7.48 (n/a)</td><td>0.80 (n/a)</td><td>280.30 (n/a)</td><td>249.42 (n/a)</td><td>240.60 (n/a)</td><td>221.30 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.09 (-2.35%)</td><td>11.28 (-2.39%)</td><td>11.24 (+1.11%)</td><td>10.63 (-3.02%)</td><td>0.57 (-17.14%)</td><td>394.70 (+3.11%)</td><td>372.74 (+2.37%)</td><td>373.30 (-1.09%)</td><td>346.90 (+2.39%)</td><td>18.69 (-12.35%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.38 (n/a)</td><td>11.55 (n/a)</td><td>11.11 (n/a)</td><td>10.96 (n/a)</td><td>0.69 (n/a)</td><td>382.80 (n/a)</td><td>364.10 (n/a)</td><td>377.40 (n/a)</td><td>338.80 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>12.89 (+5.84%)</td><td>11.44 (-1.65%)</td><td>10.95 (-7.17%)</td><td>10.67 (+0.51%)</td><td>0.94 <b>(+46.45%)</b></td><td>392.90 (-0.51%)</td><td>368.64 (+1.94%)</td><td>382.90 (+7.71%)</td><td>325.40 (-5.54%)</td><td>28.91 <b>(+38.57%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.18 (n/a)</td><td>11.63 (n/a)</td><td>11.80 (n/a)</td><td>10.62 (n/a)</td><td>0.64 (n/a)</td><td>394.90 (n/a)</td><td>361.64 (n/a)</td><td>355.50 (n/a)</td><td>344.50 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>11.80 (-8.13%)</td><td>11.24 (+3.61%)</td><td>10.93 (-0.26%)</td><td>10.83 <b>(+26.02%)</b></td><td>0.49 <b>(-69.54%)</b></td><td>387.10 <b>(-20.64%)</b></td><td>373.70 (-5.12%)</td><td>383.60 (+0.26%)</td><td>355.60 (+8.85%)</td><td>16.03 <b>(-73.99%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>12.84 (n/a)</td><td>10.85 (n/a)</td><td>10.96 (n/a)</td><td>8.60 (n/a)</td><td>1.61 (n/a)</td><td>487.80 (n/a)</td><td>393.86 (n/a)</td><td>382.60 (n/a)</td><td>326.70 (n/a)</td><td>61.64 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.27 (-3.45%)</td><td>12.96 (-2.41%)</td><td>13.59 (+6.19%)</td><td>10.94 (-10.56%)</td><td>1.46 <b>(+40.44%)</b></td><td>383.30 (+11.81%)</td><td>327.08 (+3.08%)</td><td>308.70 (-5.83%)</td><td>293.80 (+3.56%)</td><td>39.00 <b>(+62.21%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.78 (n/a)</td><td>13.28 (n/a)</td><td>12.79 (n/a)</td><td>12.24 (n/a)</td><td>1.04 (n/a)</td><td>342.80 (n/a)</td><td>317.30 (n/a)</td><td>327.80 (n/a)</td><td>283.70 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.67 (-2.46%)</td><td>13.23 (-1.38%)</td><td>12.89 (-5.96%)</td><td>12.70 (+6.01%)</td><td>0.83 <b>(-30.01%)</b></td><td>330.40 (-5.65%)</td><td>318.06 (+1.06%)</td><td>325.40 (+6.31%)</td><td>285.90 (+2.51%)</td><td>18.64 <b>(-32.72%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>15.04 (n/a)</td><td>13.41 (n/a)</td><td>13.70 (n/a)</td><td>11.98 (n/a)</td><td>1.19 (n/a)</td><td>350.20 (n/a)</td><td>314.72 (n/a)</td><td>306.10 (n/a)</td><td>278.90 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.44 (-0.33%)</td><td>13.19 (+3.51%)</td><td>13.18 (+5.95%)</td><td>11.92 (+0.28%)</td><td>0.98 (-2.51%)</td><td>351.80 (-0.26%)</td><td>319.44 (-3.41%)</td><td>318.20 (-5.61%)</td><td>290.40 (+0.31%)</td><td>23.94 (-0.30%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.49 (n/a)</td><td>12.74 (n/a)</td><td>12.44 (n/a)</td><td>11.89 (n/a)</td><td>1.01 (n/a)</td><td>352.70 (n/a)</td><td>330.72 (n/a)</td><td>337.10 (n/a)</td><td>289.50 (n/a)</td><td>24.01 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>14.98 (+9.09%)</td><td>13.20 (+14.00%)</td><td>13.10 (+9.47%)</td><td>11.07 <b>(+27.97%)</b></td><td>1.75 (-7.80%)</td><td>378.70 <b>(-21.87%)</b></td><td>322.32 (-13.15%)</td><td>320.10 (-8.65%)</td><td>280.00 (-8.35%)</td><td>43.37 <b>(-36.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>13.73 (n/a)</td><td>11.58 (n/a)</td><td>11.97 (n/a)</td><td>8.65 (n/a)</td><td>1.90 (n/a)</td><td>484.70 (n/a)</td><td>371.14 (n/a)</td><td>350.40 (n/a)</td><td>305.50 (n/a)</td><td>68.80 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>13.62 (-2.97%)</td><td>11.87 (+0.02%)</td><td>12.90 (+3.94%)</td><td>8.65 (-9.39%)</td><td>2.02 (+2.02%)</td><td>484.60 (+10.36%)</td><td>363.08 (+0.40%)</td><td>325.00 (-3.79%)</td><td>308.00 (+3.08%)</td><td>72.61 (+15.93%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>14.03 (n/a)</td><td>11.87 (n/a)</td><td>12.42 (n/a)</td><td>9.55 (n/a)</td><td>1.98 (n/a)</td><td>439.10 (n/a)</td><td>361.64 (n/a)</td><td>337.80 (n/a)</td><td>298.80 (n/a)</td><td>62.63 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.33 (-2.97%)</td><td>2.52 (-11.90%)</td><td>2.38 (-14.23%)</td><td>2.09 (-19.06%)</td><td>0.52 <b>(+52.27%)</b></td><td>250.70 <b>(+23.56%)</b></td><td>214.18 (+15.82%)</td><td>220.50 (+16.60%)</td><td>157.30 (+3.08%)</td><td>39.43 <b>(+98.95%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.44 (n/a)</td><td>2.86 (n/a)</td><td>2.77 (n/a)</td><td>2.58 (n/a)</td><td>0.34 (n/a)</td><td>202.90 (n/a)</td><td>184.92 (n/a)</td><td>189.10 (n/a)</td><td>152.60 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>5.53 (-5.20%)</td><td>4.84 (+0.09%)</td><td>4.96 (+6.26%)</td><td>3.80 (-3.09%)</td><td>0.67 (-7.88%)</td><td>275.60 (+3.18%)</td><td>220.42 (-0.20%)</td><td>211.50 (-5.87%)</td><td>189.70 (+5.45%)</td><td>33.69 (+2.20%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>5.83 (n/a)</td><td>4.83 (n/a)</td><td>4.67 (n/a)</td><td>3.93 (n/a)</td><td>0.72 (n/a)</td><td>267.10 (n/a)</td><td>220.86 (n/a)</td><td>224.70 (n/a)</td><td>179.90 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>8.67 (+11.87%)</td><td>7.71 (+8.38%)</td><td>7.77 (+4.32%)</td><td>6.48 (+10.32%)</td><td>0.83 (+6.50%)</td><td>323.60 (-9.36%)</td><td>274.80 (-7.81%)</td><td>270.00 (-4.15%)</td><td>241.90 (-10.61%)</td><td>31.12 (-13.05%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>7.75 (n/a)</td><td>7.11 (n/a)</td><td>7.45 (n/a)</td><td>5.87 (n/a)</td><td>0.78 (n/a)</td><td>357.00 (n/a)</td><td>298.08 (n/a)</td><td>281.70 (n/a)</td><td>270.60 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>3.39 (+5.30%)</td><td>2.85 (-1.88%)</td><td>2.79 (-10.55%)</td><td>2.51 (+1.99%)</td><td>0.34 (-12.29%)</td><td>208.90 (-1.97%)</td><td>186.10 (+1.47%)</td><td>187.70 (+11.79%)</td><td>154.60 (-5.04%)</td><td>20.28 (-19.87%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>3.22 (n/a)</td><td>2.90 (n/a)</td><td>3.12 (n/a)</td><td>2.46 (n/a)</td><td>0.38 (n/a)</td><td>213.10 (n/a)</td><td>183.40 (n/a)</td><td>167.90 (n/a)</td><td>162.80 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.28 (+8.03%)</td><td>0.20 (+1.27%)</td><td>0.19 (-3.15%)</td><td>0.15 (+13.00%)</td><td>0.05 (+4.89%)</td><td>220.90 (-11.53%)</td><td>173.46 (-1.97%)</td><td>170.90 (+3.26%)</td><td>116.90 (-7.44%)</td><td>37.77 (-18.80%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>249.70 (n/a)</td><td>176.94 (n/a)</td><td>165.50 (n/a)</td><td>126.30 (n/a)</td><td>46.51 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.22 <b>(-21.30%)</b></td><td>0.19 (-5.28%)</td><td>0.20 (-1.90%)</td><td>0.17 (+8.56%)</td><td>0.02 <b>(-55.16%)</b></td><td>195.80 (-7.86%)</td><td>173.36 (+1.87%)</td><td>162.40 (+1.88%)</td><td>150.90 <b>(+27.02%)</b></td><td>20.79 <b>(-47.98%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>212.50 (n/a)</td><td>170.18 (n/a)</td><td>159.40 (n/a)</td><td>118.80 (n/a)</td><td>39.97 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.54 (-0.75%)</td><td>0.39 (-6.73%)</td><td>0.34 <b>(-23.87%)</b></td><td>0.31 <b>(+71.31%)</b></td><td>0.10 <b>(-34.27%)</b></td><td>210.90 <b>(-41.63%)</b></td><td>173.60 (-4.87%)</td><td>193.00 <b>(+31.38%)</b></td><td>120.70 (+0.75%)</td><td>37.04 <b>(-63.43%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>361.30 (n/a)</td><td>182.48 (n/a)</td><td>146.90 (n/a)</td><td>119.80 (n/a)</td><td>101.30 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.48 (-3.38%)</td><td>0.42 (+5.83%)</td><td>0.44 (+8.44%)</td><td>0.32 (+11.51%)</td><td>0.06 (-14.43%)</td><td>203.00 (-10.30%)</td><td>159.48 (-6.46%)</td><td>149.70 (-7.82%)</td><td>136.30 (+3.49%)</td><td>27.32 <b>(-22.08%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>226.30 (n/a)</td><td>170.50 (n/a)</td><td>162.40 (n/a)</td><td>131.70 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.46 (-8.64%)</td><td>0.38 (-10.43%)</td><td>0.36 (-14.26%)</td><td>0.33 (-5.97%)</td><td>0.05 (-15.15%)</td><td>200.00 (+6.38%)</td><td>175.20 (+11.34%)</td><td>180.30 (+16.62%)</td><td>143.80 (+9.52%)</td><td>24.14 (-0.46%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>188.00 (n/a)</td><td>157.36 (n/a)</td><td>154.60 (n/a)</td><td>131.30 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.04 (+1.15%)</td><td>0.86 (-7.94%)</td><td>0.86 (-9.96%)</td><td>0.68 (-11.87%)</td><td>0.13 <b>(+27.93%)</b></td><td>191.80 (+13.42%)</td><td>155.96 (+9.48%)</td><td>151.90 (+11.04%)</td><td>126.30 (-1.17%)</td><td>23.72 <b>(+43.34%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.03 (n/a)</td><td>0.93 (n/a)</td><td>0.96 (n/a)</td><td>0.78 (n/a)</td><td>0.10 (n/a)</td><td>169.10 (n/a)</td><td>142.46 (n/a)</td><td>136.80 (n/a)</td><td>127.80 (n/a)</td><td>16.55 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.99 (-9.54%)</td><td>0.68 <b>(-22.02%)</b></td><td>0.62 <b>(-26.92%)</b></td><td>0.55 <b>(-28.09%)</b></td><td>0.18 <b>(+33.23%)</b></td><td>236.60 <b>(+39.09%)</b></td><td>199.72 <b>(+31.67%)</b></td><td>210.20 <b>(+36.85%)</b></td><td>132.50 (+10.60%)</td><td>40.91 <b>(+97.77%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>1.09 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.13 (n/a)</td><td>170.10 (n/a)</td><td>151.68 (n/a)</td><td>153.60 (n/a)</td><td>119.80 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.03 (+14.89%)</td><td>0.75 (-2.76%)</td><td>0.67 (-12.87%)</td><td>0.62 (+5.10%)</td><td>0.17 <b>(+45.94%)</b></td><td>209.80 (-4.85%)</td><td>181.22 (+4.27%)</td><td>196.80 (+14.82%)</td><td>127.70 (-12.95%)</td><td>33.51 (+17.58%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.89 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.59 (n/a)</td><td>0.11 (n/a)</td><td>220.50 (n/a)</td><td>173.80 (n/a)</td><td>171.40 (n/a)</td><td>146.70 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>1.07 (+15.47%)</td><td>0.79 (+2.01%)</td><td>0.73 (-0.47%)</td><td>0.66 (+3.49%)</td><td>0.16 <b>(+33.21%)</b></td><td>199.50 (-3.39%)</td><td>169.92 (-1.15%)</td><td>178.80 (+0.51%)</td><td>122.90 (-13.39%)</td><td>28.58 (+8.78%)</td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>206.50 (n/a)</td><td>171.90 (n/a)</td><td>177.90 (n/a)</td><td>141.90 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>cdc48e9</code> — 2026-08-03 16:53:11</td><td>0.14 <b>(+38.63%)</b></td><td>0.10 <b>(+22.21%)</b></td><td>0.09 (+8.37%)</td><td>0.09 <b>(+20.12%)</b></td><td>0.02 <b>(+112.72%)</b></td><td>190.90 (-16.75%)</td><td>161.54 (-16.37%)</td><td>175.10 (-7.70%)</td><td>116.90 <b>(-27.84%)</b></td><td>31.48 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>8f90c43</code> — 2026-08-01 01:13:30</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>193.16 (n/a)</td><td>189.70 (n/a)</td><td>162.00 (n/a)</td><td>24.60 (n/a)</td>
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
