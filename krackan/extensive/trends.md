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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (+14.86%)</td><td>0.04 (-1.90%)</td><td>0.03 (-15.18%)</td><td>0.03 (+7.30%)</td><td>0.01 <b>(+51.69%)</b></td><td>194.30 (-6.81%)</td><td>171.04 (+3.71%)</td><td>189.20 (+17.88%)</td><td>115.80 (-12.93%)</td><td>33.13 <b>(+20.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>164.92 (n/a)</td><td>160.50 (n/a)</td><td>133.00 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 <b>(-31.40%)</b></td><td>0.04 (-11.75%)</td><td>0.04 (+4.24%)</td><td>0.03 (-0.94%)</td><td>0.01 <b>(-54.75%)</b></td><td>200.20 (+0.96%)</td><td>168.00 (+6.69%)</td><td>172.90 (-4.05%)</td><td>126.80 <b>(+45.75%)</b></td><td>30.79 <b>(-31.17%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>157.46 (n/a)</td><td>180.20 (n/a)</td><td>87.00 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-1.85%)</td><td>0.04 (+6.55%)</td><td>0.04 (+18.72%)</td><td>0.03 (+4.94%)</td><td>0.01 (-14.21%)</td><td>204.60 (-4.70%)</td><td>163.98 (-6.88%)</td><td>155.50 (-15.76%)</td><td>130.20 (+1.88%)</td><td>27.81 (-13.77%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>176.10 (n/a)</td><td>184.60 (n/a)</td><td>127.80 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (-8.79%)</td><td>0.04 (-3.69%)</td><td>0.03 (-2.10%)</td><td>0.03 (+7.96%)</td><td>0.00 <b>(-39.38%)</b></td><td>204.70 (-7.38%)</td><td>176.62 (+2.07%)</td><td>178.40 (+2.12%)</td><td>151.80 (+9.60%)</td><td>20.25 <b>(-37.97%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>173.04 (n/a)</td><td>174.70 (n/a)</td><td>138.50 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-14.40%)</td><td>0.03 (-14.92%)</td><td>0.03 (-14.77%)</td><td>0.02 (-19.20%)</td><td>0.00 (-2.68%)</td><td>255.80 <b>(+23.75%)</b></td><td>213.68 (+18.07%)</td><td>202.20 (+17.35%)</td><td>181.70 (+16.77%)</td><td>33.06 <b>(+37.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>180.98 (n/a)</td><td>172.30 (n/a)</td><td>155.60 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (-4.04%)</td><td>0.03 (-3.85%)</td><td>0.03 (+14.54%)</td><td>0.02 <b>(-22.59%)</b></td><td>0.01 (+18.70%)</td><td>277.50 <b>(+29.19%)</b></td><td>197.70 (+6.44%)</td><td>176.20 (-12.69%)</td><td>146.00 (+4.21%)</td><td>51.60 <b>(+62.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>185.74 (n/a)</td><td>201.80 (n/a)</td><td>140.10 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (+18.93%)</td><td>0.03 (+4.28%)</td><td>0.03 (-0.69%)</td><td>0.02 (-13.41%)</td><td>0.01 <b>(+73.32%)</b></td><td>256.10 (+15.46%)</td><td>190.00 (-1.80%)</td><td>189.40 (+0.69%)</td><td>142.80 (-15.90%)</td><td>41.96 <b>(+70.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>193.48 (n/a)</td><td>188.10 (n/a)</td><td>169.80 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-9.65%)</td><td>0.03 (-6.74%)</td><td>0.03 (-4.42%)</td><td>0.03 (+0.08%)</td><td>0.00 <b>(-51.07%)</b></td><td>225.00 (-0.09%)</td><td>213.44 (+6.34%)</td><td>216.00 (+4.65%)</td><td>192.40 (+10.64%)</td><td>12.61 <b>(-46.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>225.20 (n/a)</td><td>200.72 (n/a)</td><td>206.40 (n/a)</td><td>173.90 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 <b>(+20.97%)</b></td><td>0.07 (+18.91%)</td><td>0.08 <b>(+30.43%)</b></td><td>0.05 (+0.49%)</td><td>0.01 <b>(+46.45%)</b></td><td>236.80 (-0.50%)</td><td>176.04 (-14.76%)</td><td>156.90 <b>(-23.31%)</b></td><td>145.60 (-17.32%)</td><td>37.29 <b>(+21.59%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>206.52 (n/a)</td><td>204.60 (n/a)</td><td>176.10 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (+5.54%)</td><td>0.08 (+11.90%)</td><td>0.08 (+11.08%)</td><td>0.06 (+15.02%)</td><td>0.01 (-17.65%)</td><td>197.90 (-13.09%)</td><td>162.74 (-11.77%)</td><td>159.90 (-9.97%)</td><td>135.00 (-5.26%)</td><td>23.49 <b>(-32.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>184.44 (n/a)</td><td>177.60 (n/a)</td><td>142.50 (n/a)</td><td>34.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (-1.27%)</td><td>0.07 (-4.95%)</td><td>0.06 (-2.75%)</td><td>0.06 (-11.16%)</td><td>0.01 <b>(+29.81%)</b></td><td>219.90 (+12.54%)</td><td>187.58 (+6.25%)</td><td>192.10 (+2.84%)</td><td>153.30 (+1.32%)</td><td>29.81 <b>(+47.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>176.54 (n/a)</td><td>186.80 (n/a)</td><td>151.30 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (+0.68%)</td><td>0.07 (+2.87%)</td><td>0.07 (-1.12%)</td><td>0.07 (+15.31%)</td><td>0.01 (-19.29%)</td><td>186.80 (-13.32%)</td><td>175.08 (-3.74%)</td><td>184.20 (+1.15%)</td><td>139.00 (-0.64%)</td><td>20.27 <b>(-31.07%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>181.88 (n/a)</td><td>182.10 (n/a)</td><td>139.90 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (-15.73%)</td><td>0.07 (-8.56%)</td><td>0.06 (-7.93%)</td><td>0.06 (-14.46%)</td><td>0.01 (-15.61%)</td><td>214.80 (+16.87%)</td><td>186.48 (+9.35%)</td><td>194.90 (+8.64%)</td><td>155.20 (+18.65%)</td><td>26.27 (+17.73%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.80 (n/a)</td><td>170.54 (n/a)</td><td>179.40 (n/a)</td><td>130.80 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (+6.40%)</td><td>0.07 (+12.81%)</td><td>0.07 (+11.09%)</td><td>0.06 (+17.07%)</td><td>0.01 (+1.23%)</td><td>194.00 (-14.61%)</td><td>172.54 (-11.56%)</td><td>169.50 (-9.98%)</td><td>153.50 (-6.00%)</td><td>19.74 (-19.25%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>195.10 (n/a)</td><td>188.30 (n/a)</td><td>163.30 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 <b>(+29.83%)</b></td><td>0.07 (+3.67%)</td><td>0.06 (-10.65%)</td><td>0.05 (+15.99%)</td><td>0.02 <b>(+43.53%)</b></td><td>269.70 (-13.81%)</td><td>198.26 (-2.42%)</td><td>202.20 (+11.96%)</td><td>120.90 <b>(-22.94%)</b></td><td>53.78 (-13.98%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>312.90 (n/a)</td><td>203.18 (n/a)</td><td>180.60 (n/a)</td><td>156.90 (n/a)</td><td>62.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (+19.16%)</td><td>0.06 (-1.47%)</td><td>0.06 (+2.23%)</td><td>0.04 <b>(-33.95%)</b></td><td>0.01 <b>(+493.98%)</b></td><td>312.60 <b>(+51.38%)</b></td><td>210.92 (+7.16%)</td><td>195.40 (-2.15%)</td><td>158.20 (-16.07%)</td><td>60.85 <b>(+680.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>196.82 (n/a)</td><td>199.70 (n/a)</td><td>188.50 (n/a)</td><td>7.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (-4.02%)</td><td>0.14 (-4.05%)</td><td>0.15 (+8.12%)</td><td>0.10 <b>(-23.14%)</b></td><td>0.02 <b>(+68.48%)</b></td><td>244.40 <b>(+30.14%)</b></td><td>186.76 (+6.39%)</td><td>167.20 (-7.52%)</td><td>154.80 (+4.17%)</td><td>36.72 <b>(+133.46%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>175.54 (n/a)</td><td>180.80 (n/a)</td><td>148.60 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 <b>(+36.11%)</b></td><td>0.14 (+8.42%)</td><td>0.14 (+3.87%)</td><td>0.12 (+0.22%)</td><td>0.03 <b>(+167.95%)</b></td><td>210.10 (-0.19%)</td><td>178.04 (-5.04%)</td><td>179.70 (-3.75%)</td><td>125.00 <b>(-26.56%)</b></td><td>35.17 <b>(+100.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>187.48 (n/a)</td><td>186.70 (n/a)</td><td>170.20 (n/a)</td><td>17.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 <b>(+21.52%)</b></td><td>0.14 (+13.48%)</td><td>0.13 (+6.31%)</td><td>0.12 <b>(+34.92%)</b></td><td>0.02 (+9.10%)</td><td>201.80 <b>(-25.86%)</b></td><td>177.54 (-12.66%)</td><td>184.40 (-5.92%)</td><td>134.10 (-17.73%)</td><td>25.49 <b>(-38.14%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>272.20 (n/a)</td><td>203.28 (n/a)</td><td>196.00 (n/a)</td><td>163.00 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 <b>(+25.98%)</b></td><td>0.14 (-4.28%)</td><td>0.14 (-2.08%)</td><td>0.08 <b>(-39.69%)</b></td><td>0.05 <b>(+520.04%)</b></td><td>292.50 <b>(+65.82%)</b></td><td>191.56 (+14.87%)</td><td>171.70 (+2.08%)</td><td>125.30 <b>(-20.60%)</b></td><td>68.98 <b>(+718.53%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>166.76 (n/a)</td><td>168.20 (n/a)</td><td>157.80 (n/a)</td><td>8.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (-3.49%)</td><td>0.15 (+4.32%)</td><td>0.16 (+12.06%)</td><td>0.11 (-15.61%)</td><td>0.02 <b>(+36.68%)</b></td><td>232.30 (+18.52%)</td><td>170.32 (-2.66%)</td><td>158.40 (-10.76%)</td><td>150.40 (+3.58%)</td><td>34.93 <b>(+70.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.00 (n/a)</td><td>174.98 (n/a)</td><td>177.50 (n/a)</td><td>145.20 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 <b>(+20.28%)</b></td><td>0.14 <b>(+21.23%)</b></td><td>0.14 (+12.29%)</td><td>0.11 <b>(+54.08%)</b></td><td>0.02 <b>(-28.60%)</b></td><td>220.70 <b>(-35.09%)</b></td><td>184.14 <b>(-20.24%)</b></td><td>179.40 (-10.92%)</td><td>155.50 (-16.89%)</td><td>23.63 <b>(-62.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>340.00 (n/a)</td><td>230.86 (n/a)</td><td>201.40 (n/a)</td><td>187.10 (n/a)</td><td>62.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (+16.75%)</td><td>0.14 (+2.64%)</td><td>0.14 (-0.72%)</td><td>0.08 (-16.10%)</td><td>0.04 <b>(+69.00%)</b></td><td>301.70 (+19.20%)</td><td>192.74 (+2.38%)</td><td>178.70 (+0.68%)</td><td>137.70 (-14.31%)</td><td>65.76 <b>(+72.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>253.10 (n/a)</td><td>188.26 (n/a)</td><td>177.50 (n/a)</td><td>160.70 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 <b>(-20.75%)</b></td><td>0.11 (-11.25%)</td><td>0.11 (-10.73%)</td><td>0.08 (-4.28%)</td><td>0.02 <b>(-20.85%)</b></td><td>324.40 (+4.48%)</td><td>239.60 (+11.49%)</td><td>223.00 (+12.06%)</td><td>189.30 <b>(+26.20%)</b></td><td>58.19 (-1.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>310.50 (n/a)</td><td>214.90 (n/a)</td><td>199.00 (n/a)</td><td>150.00 (n/a)</td><td>59.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.38 <b>(+31.90%)</b></td><td>0.32 <b>(+32.15%)</b></td><td>0.31 (+18.25%)</td><td>0.27 <b>(+85.73%)</b></td><td>0.04 <b>(-27.62%)</b></td><td>182.40 <b>(-46.15%)</b></td><td>155.58 <b>(-27.87%)</b></td><td>159.00 (-15.47%)</td><td>130.90 <b>(-24.16%)</b></td><td>19.45 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>338.70 (n/a)</td><td>215.68 (n/a)</td><td>188.10 (n/a)</td><td>172.60 (n/a)</td><td>69.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.43 <b>(+24.69%)</b></td><td>0.32 <b>(+22.11%)</b></td><td>0.31 (+14.02%)</td><td>0.25 <b>(+63.64%)</b></td><td>0.07 (+1.70%)</td><td>195.00 <b>(-38.89%)</b></td><td>158.86 <b>(-21.04%)</b></td><td>158.90 (-12.31%)</td><td>115.10 (-19.85%)</td><td>31.77 <b>(-53.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>319.10 (n/a)</td><td>201.20 (n/a)</td><td>181.20 (n/a)</td><td>143.60 (n/a)</td><td>68.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.29 (+4.96%)</td><td>0.27 (+7.72%)</td><td>0.27 (+4.11%)</td><td>0.25 (+19.69%)</td><td>0.02 <b>(-34.37%)</b></td><td>199.30 (-16.47%)</td><td>181.12 (-7.89%)</td><td>181.40 (-3.97%)</td><td>167.30 (-4.73%)</td><td>12.82 <b>(-48.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>238.60 (n/a)</td><td>196.64 (n/a)</td><td>188.90 (n/a)</td><td>175.60 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 <b>(+28.96%)</b></td><td>0.32 (+18.20%)</td><td>0.31 (+14.23%)</td><td>0.27 <b>(+21.50%)</b></td><td>0.04 <b>(+44.39%)</b></td><td>179.40 (-17.71%)</td><td>156.46 (-15.22%)</td><td>157.30 (-12.47%)</td><td>132.40 <b>(-22.48%)</b></td><td>17.33 (-9.75%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>218.00 (n/a)</td><td>184.54 (n/a)</td><td>179.70 (n/a)</td><td>170.80 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 (+12.15%)</td><td>0.29 (+12.56%)</td><td>0.32 (+19.70%)</td><td>0.21 (+13.76%)</td><td>0.06 <b>(+33.32%)</b></td><td>232.00 (-12.09%)</td><td>176.00 (-10.21%)</td><td>156.00 (-16.44%)</td><td>137.90 (-10.86%)</td><td>40.93 (+1.11%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>263.90 (n/a)</td><td>196.02 (n/a)</td><td>186.70 (n/a)</td><td>154.70 (n/a)</td><td>40.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 <b>(+20.55%)</b></td><td>0.29 (+5.10%)</td><td>0.29 (+2.10%)</td><td>0.24 (-5.18%)</td><td>0.05 <b>(+98.97%)</b></td><td>208.60 (+5.46%)</td><td>174.30 (-3.58%)</td><td>169.10 (-2.03%)</td><td>137.50 (-17.07%)</td><td>26.24 <b>(+70.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>197.80 (n/a)</td><td>180.78 (n/a)</td><td>172.60 (n/a)</td><td>165.80 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.34 (+9.09%)</td><td>0.27 (+1.09%)</td><td>0.24 (-18.45%)</td><td>0.23 <b>(+34.23%)</b></td><td>0.04 <b>(-26.16%)</b></td><td>212.00 <b>(-25.51%)</b></td><td>188.08 (-4.14%)</td><td>200.70 <b>(+22.60%)</b></td><td>144.40 (-8.32%)</td><td>27.12 <b>(-49.80%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>284.60 (n/a)</td><td>196.20 (n/a)</td><td>163.70 (n/a)</td><td>157.50 (n/a)</td><td>54.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.29 (-6.44%)</td><td>0.27 (+8.49%)</td><td>0.27 (+8.23%)</td><td>0.26 <b>(+64.85%)</b></td><td>0.01 <b>(-81.00%)</b></td><td>188.90 <b>(-39.34%)</b></td><td>179.38 (-13.06%)</td><td>179.90 (-7.60%)</td><td>167.90 (+6.87%)</td><td>7.56 <b>(-87.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>311.40 (n/a)</td><td>206.32 (n/a)</td><td>194.70 (n/a)</td><td>157.10 (n/a)</td><td>62.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (+14.48%)</td><td>0.02 (-2.65%)</td><td>0.02 (-15.53%)</td><td>0.01 (-2.80%)</td><td>0.00 <b>(+26.20%)</b></td><td>185.80 (+2.94%)</td><td>155.16 (+3.62%)</td><td>157.80 (+18.38%)</td><td>107.20 (-12.63%)</td><td>29.76 (+5.53%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>180.50 (n/a)</td><td>149.74 (n/a)</td><td>133.30 (n/a)</td><td>122.70 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (+6.78%)</td><td>0.02 (+3.10%)</td><td>0.02 (-4.51%)</td><td>0.01 (+11.73%)</td><td>0.00 (-13.32%)</td><td>188.70 (-10.53%)</td><td>166.84 (-3.87%)</td><td>172.60 (+4.67%)</td><td>133.30 (-6.32%)</td><td>20.54 <b>(-30.15%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>173.56 (n/a)</td><td>164.90 (n/a)</td><td>142.30 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-19.14%)</td><td>0.01 (-13.56%)</td><td>0.02 (-16.45%)</td><td>0.01 (-10.07%)</td><td>0.00 <b>(-30.48%)</b></td><td>216.70 (+11.24%)</td><td>179.36 (+14.30%)</td><td>167.90 (+19.67%)</td><td>148.80 <b>(+23.69%)</b></td><td>31.00 (-6.96%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>156.92 (n/a)</td><td>140.30 (n/a)</td><td>120.30 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-17.06%)</td><td>0.01 (-7.96%)</td><td>0.01 (-8.90%)</td><td>0.01 (-2.99%)</td><td>0.00 <b>(-41.44%)</b></td><td>221.20 (+3.08%)</td><td>186.36 (+7.21%)</td><td>177.10 (+9.73%)</td><td>167.60 <b>(+20.58%)</b></td><td>21.61 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>173.82 (n/a)</td><td>161.40 (n/a)</td><td>139.00 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (+8.65%)</td><td>0.01 (-11.72%)</td><td>0.01 (-18.35%)</td><td>0.01 (-14.23%)</td><td>0.00 <b>(+57.73%)</b></td><td>234.20 (+16.58%)</td><td>192.42 (+17.42%)</td><td>209.30 <b>(+22.47%)</b></td><td>117.00 (-7.95%)</td><td>44.79 <b>(+61.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>163.88 (n/a)</td><td>170.90 (n/a)</td><td>127.10 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (+10.17%)</td><td>0.02 (+11.56%)</td><td>0.01 (+9.31%)</td><td>0.01 <b>(+29.37%)</b></td><td>0.00 <b>(-22.76%)</b></td><td>187.20 <b>(-22.68%)</b></td><td>166.36 (-12.18%)</td><td>175.70 (-8.49%)</td><td>131.80 (-9.23%)</td><td>21.61 <b>(-45.85%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>242.10 (n/a)</td><td>189.44 (n/a)</td><td>192.00 (n/a)</td><td>145.20 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-7.30%)</td><td>0.01 (-4.89%)</td><td>0.01 (-3.36%)</td><td>0.01 (-6.45%)</td><td>0.00 (-2.18%)</td><td>224.90 (+6.89%)</td><td>186.04 (+5.24%)</td><td>176.10 (+3.47%)</td><td>170.50 (+7.84%)</td><td>22.32 (+11.97%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>176.78 (n/a)</td><td>170.20 (n/a)</td><td>158.10 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.01 (-7.48%)</td><td>0.01 (-5.75%)</td><td>0.01 (-6.50%)</td><td>0.01 (-2.61%)</td><td>0.00 (-15.06%)</td><td>233.30 (+2.68%)</td><td>219.86 (+6.04%)</td><td>220.40 (+6.94%)</td><td>206.70 (+8.11%)</td><td>12.01 (-6.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>207.34 (n/a)</td><td>206.10 (n/a)</td><td>191.20 (n/a)</td><td>12.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-19.73%)</td><td>0.03 (-11.35%)</td><td>0.03 (-12.37%)</td><td>0.02 (+6.59%)</td><td>0.00 <b>(-52.49%)</b></td><td>211.00 (-6.18%)</td><td>179.58 (+9.23%)</td><td>176.70 (+14.07%)</td><td>157.50 <b>(+24.51%)</b></td><td>22.15 <b>(-44.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>164.40 (n/a)</td><td>154.90 (n/a)</td><td>126.50 (n/a)</td><td>40.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-16.52%)</td><td>0.03 (-17.82%)</td><td>0.03 (-3.04%)</td><td>0.01 <b>(-47.29%)</b></td><td>0.01 <b>(+73.72%)</b></td><td>370.30 <b>(+89.70%)</b></td><td>216.70 <b>(+33.67%)</b></td><td>164.40 (+3.14%)</td><td>155.00 (+19.78%)</td><td>91.98 <b>(+290.64%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>162.12 (n/a)</td><td>159.40 (n/a)</td><td>129.40 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+16.35%)</td><td>0.03 (+18.27%)</td><td>0.03 (+19.64%)</td><td>0.02 <b>(+59.57%)</b></td><td>0.00 (-16.02%)</td><td>228.10 <b>(-37.34%)</b></td><td>183.84 (-18.90%)</td><td>164.70 (-16.44%)</td><td>157.40 (-14.04%)</td><td>33.08 <b>(-57.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>364.00 (n/a)</td><td>226.68 (n/a)</td><td>197.10 (n/a)</td><td>183.10 (n/a)</td><td>77.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-1.59%)</td><td>0.03 (+7.75%)</td><td>0.03 (+17.40%)</td><td>0.02 (-3.75%)</td><td>0.00 (+7.86%)</td><td>221.70 (+3.89%)</td><td>179.42 (-6.92%)</td><td>168.00 (-14.81%)</td><td>160.50 (+1.58%)</td><td>24.65 (+19.50%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>192.76 (n/a)</td><td>197.20 (n/a)</td><td>158.00 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+7.81%)</td><td>0.03 (+5.24%)</td><td>0.03 (+0.44%)</td><td>0.03 (+19.04%)</td><td>0.00 (-7.68%)</td><td>194.70 (-16.01%)</td><td>180.96 (-5.42%)</td><td>191.60 (-0.42%)</td><td>151.10 (-7.19%)</td><td>18.93 <b>(-28.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.80 (n/a)</td><td>191.32 (n/a)</td><td>192.40 (n/a)</td><td>162.80 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+5.08%)</td><td>0.03 (+6.69%)</td><td>0.03 (+3.22%)</td><td>0.02 (+12.48%)</td><td>0.00 <b>(-20.58%)</b></td><td>214.10 (-11.09%)</td><td>200.90 (-6.47%)</td><td>204.70 (-3.12%)</td><td>185.00 (-4.79%)</td><td>11.17 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.80 (n/a)</td><td>214.80 (n/a)</td><td>211.30 (n/a)</td><td>194.30 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-13.66%)</td><td>0.03 (-8.00%)</td><td>0.03 (-15.09%)</td><td>0.02 (+11.66%)</td><td>0.00 <b>(-49.83%)</b></td><td>222.10 (-10.44%)</td><td>197.26 (+5.87%)</td><td>204.20 (+17.83%)</td><td>167.40 (+15.85%)</td><td>20.83 <b>(-49.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>186.32 (n/a)</td><td>173.30 (n/a)</td><td>144.50 (n/a)</td><td>40.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-10.53%)</td><td>0.02 (-14.44%)</td><td>0.02 (-10.68%)</td><td>0.02 <b>(-35.55%)</b></td><td>0.00 <b>(+135.20%)</b></td><td>342.80 <b>(+55.11%)</b></td><td>249.08 <b>(+20.00%)</b></td><td>233.00 (+11.91%)</td><td>210.20 (+11.75%)</td><td>53.22 <b>(+328.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.00 (n/a)</td><td>207.56 (n/a)</td><td>208.20 (n/a)</td><td>188.10 (n/a)</td><td>12.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (+9.87%)</td><td>0.07 (+17.90%)</td><td>0.08 <b>(+40.84%)</b></td><td>0.05 (-5.34%)</td><td>0.01 <b>(+68.04%)</b></td><td>205.00 (+5.62%)</td><td>153.82 (-13.18%)</td><td>131.10 <b>(-29.02%)</b></td><td>127.50 (-8.99%)</td><td>35.08 <b>(+59.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>177.18 (n/a)</td><td>184.70 (n/a)</td><td>140.10 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (+18.04%)</td><td>0.06 (+12.50%)</td><td>0.06 (+3.46%)</td><td>0.06 <b>(+25.63%)</b></td><td>0.01 (+3.88%)</td><td>180.20 <b>(-20.41%)</b></td><td>166.18 (-11.38%)</td><td>172.20 (-3.31%)</td><td>144.10 (-15.33%)</td><td>15.93 <b>(-30.17%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>187.52 (n/a)</td><td>178.10 (n/a)</td><td>170.20 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (+7.38%)</td><td>0.06 (+1.82%)</td><td>0.06 (+0.10%)</td><td>0.05 (-2.37%)</td><td>0.01 <b>(+94.27%)</b></td><td>193.80 (+2.43%)</td><td>173.66 (-1.00%)</td><td>174.10 (-0.06%)</td><td>149.10 (-6.87%)</td><td>19.86 <b>(+88.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>175.42 (n/a)</td><td>174.20 (n/a)</td><td>160.10 (n/a)</td><td>10.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 <b>(-36.86%)</b></td><td>0.05 <b>(-23.48%)</b></td><td>0.06 (-16.80%)</td><td>0.05 (+3.22%)</td><td>0.00 <b>(-79.58%)</b></td><td>223.40 (-3.12%)</td><td>199.96 <b>(+23.20%)</b></td><td>190.60 <b>(+20.18%)</b></td><td>188.50 <b>(+58.40%)</b></td><td>15.21 <b>(-67.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>162.30 (n/a)</td><td>158.60 (n/a)</td><td>119.00 (n/a)</td><td>46.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (-15.37%)</td><td>0.06 (-3.21%)</td><td>0.05 (-4.03%)</td><td>0.05 (-2.01%)</td><td>0.01 <b>(-35.20%)</b></td><td>211.20 (+2.08%)</td><td>179.52 (+1.33%)</td><td>191.50 (+4.19%)</td><td>139.80 (+18.17%)</td><td>27.99 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>177.16 (n/a)</td><td>183.80 (n/a)</td><td>118.30 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+3.73%)</td><td>0.06 (+0.71%)</td><td>0.05 (-2.75%)</td><td>0.05 (+1.37%)</td><td>0.01 (+11.75%)</td><td>216.50 (-1.37%)</td><td>190.22 (-0.60%)</td><td>194.10 (+2.81%)</td><td>167.80 (-3.62%)</td><td>19.28 (+5.70%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>191.36 (n/a)</td><td>188.80 (n/a)</td><td>174.10 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 <b>(+37.86%)</b></td><td>0.06 (+16.12%)</td><td>0.06 (+8.38%)</td><td>0.05 (+15.87%)</td><td>0.01 <b>(+96.45%)</b></td><td>214.90 (-13.69%)</td><td>177.58 (-12.02%)</td><td>184.20 (-7.72%)</td><td>120.20 <b>(-27.50%)</b></td><td>34.94 (+15.52%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>249.00 (n/a)</td><td>201.84 (n/a)</td><td>199.60 (n/a)</td><td>165.80 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 <b>(+47.66%)</b></td><td>0.06 <b>(+27.69%)</b></td><td>0.06 (+19.25%)</td><td>0.05 <b>(+54.19%)</b></td><td>0.01 <b>(+41.47%)</b></td><td>229.10 <b>(-35.15%)</b></td><td>192.28 <b>(-22.17%)</b></td><td>186.50 (-16.18%)</td><td>139.00 <b>(-32.29%)</b></td><td>35.79 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>353.30 (n/a)</td><td>247.06 (n/a)</td><td>222.50 (n/a)</td><td>205.30 (n/a)</td><td>60.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (+2.99%)</td><td>0.10 (-10.45%)</td><td>0.10 (-19.95%)</td><td>0.09 (-9.04%)</td><td>0.02 <b>(+31.67%)</b></td><td>243.80 (+9.97%)</td><td>210.52 (+12.92%)</td><td>217.30 <b>(+24.96%)</b></td><td>161.70 (-2.94%)</td><td>34.77 <b>(+43.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>186.44 (n/a)</td><td>173.90 (n/a)</td><td>166.60 (n/a)</td><td>24.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 <b>(+27.72%)</b></td><td>0.13 (+5.98%)</td><td>0.11 (+0.21%)</td><td>0.10 (-9.11%)</td><td>0.04 <b>(+107.13%)</b></td><td>208.60 (+10.02%)</td><td>168.24 (-0.95%)</td><td>183.80 (-0.22%)</td><td>103.20 <b>(-21.70%)</b></td><td>43.75 <b>(+77.50%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.60 (n/a)</td><td>169.86 (n/a)</td><td>184.20 (n/a)</td><td>131.80 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (+17.88%)</td><td>0.13 (+14.52%)</td><td>0.13 (+9.49%)</td><td>0.11 (+17.86%)</td><td>0.02 <b>(+20.96%)</b></td><td>197.30 (-15.14%)</td><td>159.82 (-12.56%)</td><td>156.10 (-8.66%)</td><td>126.70 (-15.14%)</td><td>28.93 (-13.41%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.50 (n/a)</td><td>182.78 (n/a)</td><td>170.90 (n/a)</td><td>149.30 (n/a)</td><td>33.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 <b>(+32.01%)</b></td><td>0.14 <b>(+24.62%)</b></td><td>0.14 <b>(+20.61%)</b></td><td>0.10 (+16.60%)</td><td>0.04 <b>(+86.39%)</b></td><td>205.30 (-14.24%)</td><td>157.50 (-17.36%)</td><td>151.10 (-17.07%)</td><td>113.20 <b>(-24.23%)</b></td><td>40.24 <b>(+22.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>239.40 (n/a)</td><td>190.58 (n/a)</td><td>182.20 (n/a)</td><td>149.40 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-12.22%)</td><td>0.10 (-12.52%)</td><td>0.10 (-18.26%)</td><td>0.09 (-11.65%)</td><td>0.01 <b>(-29.02%)</b></td><td>229.30 (+13.18%)</td><td>205.50 (+13.90%)</td><td>208.80 <b>(+22.32%)</b></td><td>181.30 (+13.88%)</td><td>17.76 (-10.68%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>180.42 (n/a)</td><td>170.70 (n/a)</td><td>159.20 (n/a)</td><td>19.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (+16.87%)</td><td>0.13 (+13.22%)</td><td>0.13 (+15.82%)</td><td>0.09 (-6.06%)</td><td>0.04 <b>(+63.93%)</b></td><td>221.30 (+6.45%)</td><td>166.60 (-8.62%)</td><td>158.50 (-13.62%)</td><td>116.50 (-14.40%)</td><td>44.23 <b>(+52.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>182.32 (n/a)</td><td>183.50 (n/a)</td><td>136.10 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 <b>(+47.84%)</b></td><td>0.14 <b>(+40.48%)</b></td><td>0.14 <b>(+33.75%)</b></td><td>0.10 <b>(+32.00%)</b></td><td>0.02 <b>(+52.75%)</b></td><td>200.90 <b>(-24.25%)</b></td><td>156.44 <b>(-28.53%)</b></td><td>150.20 <b>(-25.24%)</b></td><td>130.60 <b>(-32.37%)</b></td><td>26.79 (-18.32%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>265.20 (n/a)</td><td>218.90 (n/a)</td><td>200.90 (n/a)</td><td>193.10 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 <b>(+20.35%)</b></td><td>0.10 <b>(+22.44%)</b></td><td>0.09 (+16.29%)</td><td>0.08 <b>(+30.94%)</b></td><td>0.02 (+2.15%)</td><td>251.60 <b>(-23.62%)</b></td><td>214.44 (-19.15%)</td><td>223.00 (-14.00%)</td><td>173.60 (-16.90%)</td><td>33.33 <b>(-35.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>329.40 (n/a)</td><td>265.24 (n/a)</td><td>259.30 (n/a)</td><td>208.90 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>172.32 (n/a)</td><td>175.30 (n/a)</td><td>146.40 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>158.76 (n/a)</td><td>163.90 (n/a)</td><td>112.40 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.90 (n/a)</td><td>171.78 (n/a)</td><td>182.60 (n/a)</td><td>146.10 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>322.60 (n/a)</td><td>227.48 (n/a)</td><td>190.90 (n/a)</td><td>155.80 (n/a)</td><td>76.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>169.46 (n/a)</td><td>166.30 (n/a)</td><td>132.30 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>181.26 (n/a)</td><td>178.80 (n/a)</td><td>138.20 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>162.10 (n/a)</td><td>167.80 (n/a)</td><td>136.10 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>191.72 (n/a)</td><td>193.10 (n/a)</td><td>174.00 (n/a)</td><td>12.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>236.60 (n/a)</td><td>187.50 (n/a)</td><td>174.90 (n/a)</td><td>156.90 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>174.32 (n/a)</td><td>181.20 (n/a)</td><td>136.00 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>224.20 (n/a)</td><td>186.34 (n/a)</td><td>187.50 (n/a)</td><td>159.40 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>329.40 (n/a)</td><td>236.38 (n/a)</td><td>218.90 (n/a)</td><td>183.30 (n/a)</td><td>56.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (+2.28%)</td><td>0.29 (+16.37%)</td><td>0.27 (+12.14%)</td><td>0.23 <b>(+62.23%)</b></td><td>0.05 <b>(-34.98%)</b></td><td>210.80 <b>(-38.36%)</b></td><td>175.86 (-19.60%)</td><td>180.90 (-10.84%)</td><td>132.50 (-2.21%)</td><td>28.63 <b>(-62.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>342.00 (n/a)</td><td>218.72 (n/a)</td><td>202.90 (n/a)</td><td>135.50 (n/a)</td><td>76.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>209.70 (n/a)</td><td>171.76 (n/a)</td><td>182.40 (n/a)</td><td>128.00 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>251.60 (n/a)</td><td>196.26 (n/a)</td><td>191.70 (n/a)</td><td>168.90 (n/a)</td><td>33.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>233.90 (n/a)</td><td>204.62 (n/a)</td><td>217.00 (n/a)</td><td>158.70 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>169.14 (n/a)</td><td>162.40 (n/a)</td><td>156.50 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>179.46 (n/a)</td><td>182.50 (n/a)</td><td>103.10 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>340.50 (n/a)</td><td>211.82 (n/a)</td><td>174.80 (n/a)</td><td>168.70 (n/a)</td><td>72.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>193.80 (n/a)</td><td>209.40 (n/a)</td><td>125.50 (n/a)</td><td>40.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>184.14 (n/a)</td><td>180.00 (n/a)</td><td>148.00 (n/a)</td><td>26.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>171.12 (n/a)</td><td>191.50 (n/a)</td><td>118.40 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>295.90 (n/a)</td><td>195.82 (n/a)</td><td>171.90 (n/a)</td><td>167.80 (n/a)</td><td>56.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>178.42 (n/a)</td><td>170.30 (n/a)</td><td>149.60 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.10 (n/a)</td><td>154.44 (n/a)</td><td>143.20 (n/a)</td><td>138.80 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>186.36 (n/a)</td><td>188.80 (n/a)</td><td>169.10 (n/a)</td><td>13.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>228.60 (n/a)</td><td>203.20 (n/a)</td><td>205.50 (n/a)</td><td>168.60 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.70 (n/a)</td><td>201.78 (n/a)</td><td>213.90 (n/a)</td><td>129.00 (n/a)</td><td>44.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>260.90 (n/a)</td><td>184.68 (n/a)</td><td>188.90 (n/a)</td><td>130.60 (n/a)</td><td>53.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>206.20 (n/a)</td><td>186.32 (n/a)</td><td>198.60 (n/a)</td><td>140.40 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>246.10 (n/a)</td><td>223.84 (n/a)</td><td>224.30 (n/a)</td><td>201.80 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>168.30 (n/a)</td><td>163.20 (n/a)</td><td>135.10 (n/a)</td><td>31.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>172.00 (n/a)</td><td>177.10 (n/a)</td><td>161.60 (n/a)</td><td>8.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>168.28 (n/a)</td><td>176.80 (n/a)</td><td>125.80 (n/a)</td><td>40.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.70 (n/a)</td><td>184.04 (n/a)</td><td>188.50 (n/a)</td><td>142.80 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>185.88 (n/a)</td><td>177.60 (n/a)</td><td>165.10 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>269.30 (n/a)</td><td>212.56 (n/a)</td><td>203.90 (n/a)</td><td>171.10 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.00 (n/a)</td><td>201.94 (n/a)</td><td>203.30 (n/a)</td><td>172.00 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>277.80 (n/a)</td><td>226.48 (n/a)</td><td>219.50 (n/a)</td><td>191.20 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.20 (n/a)</td><td>181.04 (n/a)</td><td>161.20 (n/a)</td><td>126.80 (n/a)</td><td>48.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>162.10 (n/a)</td><td>145.40 (n/a)</td><td>138.30 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>176.60 (n/a)</td><td>166.90 (n/a)</td><td>134.60 (n/a)</td><td>32.59 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>149.14 (n/a)</td><td>144.80 (n/a)</td><td>126.80 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>177.08 (n/a)</td><td>166.00 (n/a)</td><td>154.60 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>193.40 (n/a)</td><td>186.50 (n/a)</td><td>149.70 (n/a)</td><td>32.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.10 (n/a)</td><td>184.78 (n/a)</td><td>175.60 (n/a)</td><td>174.20 (n/a)</td><td>14.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>204.40 (n/a)</td><td>195.40 (n/a)</td><td>173.50 (n/a)</td><td>26.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>207.00 (n/a)</td><td>188.24 (n/a)</td><td>185.10 (n/a)</td><td>178.90 (n/a)</td><td>11.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>187.20 (n/a)</td><td>188.50 (n/a)</td><td>161.20 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.10 (n/a)</td><td>175.48 (n/a)</td><td>182.60 (n/a)</td><td>127.10 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>291.50 (n/a)</td><td>214.56 (n/a)</td><td>209.90 (n/a)</td><td>166.50 (n/a)</td><td>47.64 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>237.50 (n/a)</td><td>184.12 (n/a)</td><td>181.70 (n/a)</td><td>135.10 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>186.22 (n/a)</td><td>199.00 (n/a)</td><td>145.50 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>214.20 (n/a)</td><td>203.38 (n/a)</td><td>205.70 (n/a)</td><td>193.20 (n/a)</td><td>8.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>205.60 (n/a)</td><td>193.80 (n/a)</td><td>188.30 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.40 (n/a)</td><td>181.54 (n/a)</td><td>185.30 (n/a)</td><td>155.60 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.10 (n/a)</td><td>197.54 (n/a)</td><td>202.40 (n/a)</td><td>170.20 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.80 (n/a)</td><td>177.94 (n/a)</td><td>196.50 (n/a)</td><td>140.00 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.10 (n/a)</td><td>176.66 (n/a)</td><td>183.30 (n/a)</td><td>133.60 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>244.40 (n/a)</td><td>195.50 (n/a)</td><td>194.60 (n/a)</td><td>121.90 (n/a)</td><td>48.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.40 (n/a)</td><td>198.24 (n/a)</td><td>193.90 (n/a)</td><td>159.40 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>246.40 (n/a)</td><td>213.64 (n/a)</td><td>202.80 (n/a)</td><td>175.60 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>235.10 (n/a)</td><td>202.02 (n/a)</td><td>199.50 (n/a)</td><td>171.30 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>4.78 (-0.43%)</td><td>4.06 (-4.15%)</td><td>3.86 (-6.15%)</td><td>3.45 (-14.22%)</td><td>0.66 <b>(+107.71%)</b></td><td>2724.10 (+16.57%)</td><td>2365.26 (+6.09%)</td><td>2434.90 (+6.56%)</td><td>1968.10 (+0.43%)</td><td>375.41 <b>(+144.39%)</b></td><td>1879.67 (-0.43%)</td><td>1597.09 (-4.15%)</td><td>1519.34 (-6.15%)</td><td>1358.01 (-14.22%)</td><td>260.74 <b>(+107.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>4.80 (n/a)</td><td>4.24 (n/a)</td><td>4.12 (n/a)</td><td>4.02 (n/a)</td><td>0.32 (n/a)</td><td>2336.80 (n/a)</td><td>2229.52 (n/a)</td><td>2285.10 (n/a)</td><td>1959.60 (n/a)</td><td>153.61 (n/a)</td><td>1887.83 (n/a)</td><td>1666.20 (n/a)</td><td>1618.93 (n/a)</td><td>1583.06 (n/a)</td><td>125.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.23 (+0.08%)</td><td>0.97 (+1.46%)</td><td>0.99 (+6.38%)</td><td>0.61 (-6.49%)</td><td>0.24 (+13.49%)</td><td>363.00 (+6.95%)</td><td>241.78 (+0.15%)</td><td>224.20 (-6.04%)</td><td>179.20 (-0.11%)</td><td>72.74 <b>(+20.94%)</b></td><td>52.65 (+0.08%)</td><td>41.46 (+1.46%)</td><td>42.08 (+6.38%)</td><td>26.00 (-6.49%)</td><td>10.31 (+13.49%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.23 (n/a)</td><td>0.96 (n/a)</td><td>0.93 (n/a)</td><td>0.65 (n/a)</td><td>0.21 (n/a)</td><td>339.40 (n/a)</td><td>241.42 (n/a)</td><td>238.60 (n/a)</td><td>179.40 (n/a)</td><td>60.14 (n/a)</td><td>52.61 (n/a)</td><td>40.86 (n/a)</td><td>39.56 (n/a)</td><td>27.81 (n/a)</td><td>9.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.15 (+4.21%)</td><td>0.89 (-10.45%)</td><td>0.87 (-18.57%)</td><td>0.61 (-6.64%)</td><td>0.24 <b>(+26.08%)</b></td><td>364.10 (+7.12%)</td><td>265.32 (+14.08%)</td><td>255.70 <b>(+22.81%)</b></td><td>193.00 (-4.03%)</td><td>74.27 <b>(+23.53%)</b></td><td>48.91 (+4.21%)</td><td>37.85 (-10.45%)</td><td>36.91 (-18.57%)</td><td>25.92 (-6.64%)</td><td>10.28 <b>(+26.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>1.06 (n/a)</td><td>0.65 (n/a)</td><td>0.19 (n/a)</td><td>339.90 (n/a)</td><td>232.58 (n/a)</td><td>208.20 (n/a)</td><td>201.10 (n/a)</td><td>60.13 (n/a)</td><td>46.93 (n/a)</td><td>42.26 (n/a)</td><td>45.32 (n/a)</td><td>27.76 (n/a)</td><td>8.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.52 (-0.05%)</td><td>0.52 (-0.01%)</td><td>0.52 (+0.00%)</td><td>0.51 (+0.09%)</td><td>0.00 (-13.12%)</td><td>48873.60 (-0.09%)</td><td>48713.34 (+0.01%)</td><td>48649.50 (-0.00%)</td><td>48620.60 (+0.05%)</td><td>114.98 (-13.19%)</td><td>353.35 (-0.05%)</td><td>352.67 (-0.01%)</td><td>353.14 (+0.00%)</td><td>351.52 (+0.09%)</td><td>0.83 (-13.12%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48920.00 (n/a)</td><td>48709.80 (n/a)</td><td>48651.10 (n/a)</td><td>48595.90 (n/a)</td><td>132.46 (n/a)</td><td>353.53 (n/a)</td><td>352.70 (n/a)</td><td>353.12 (n/a)</td><td>351.18 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (+0.10%)</td><td>0.21 (-0.08%)</td><td>0.21 (-0.03%)</td><td>0.21 (-0.32%)</td><td>0.00 <b>(+32.30%)</b></td><td>118892.30 (+0.32%)</td><td>117858.10 (+0.08%)</td><td>117617.10 (+0.03%)</td><td>116996.20 (-0.10%)</td><td>711.58 <b>(+32.62%)</b></td><td>146.84 (+0.10%)</td><td>145.77 (-0.08%)</td><td>146.07 (-0.03%)</td><td>144.50 (-0.32%)</td><td>0.88 <b>(+32.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118512.10 (n/a)</td><td>117764.04 (n/a)</td><td>117586.10 (n/a)</td><td>117110.20 (n/a)</td><td>536.56 (n/a)</td><td>146.70 (n/a)</td><td>145.89 (n/a)</td><td>146.10 (n/a)</td><td>144.96 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.90 (+0.56%)</td><td>0.89 (+0.32%)</td><td>0.89 (-0.11%)</td><td>0.88 (+0.82%)</td><td>0.01 (-12.98%)</td><td>28566.40 (-0.82%)</td><td>28354.80 (-0.32%)</td><td>28422.50 (+0.11%)</td><td>28059.30 (-0.56%)</td><td>208.02 (-14.15%)</td><td>612.27 (+0.56%)</td><td>605.92 (+0.32%)</td><td>604.45 (-0.11%)</td><td>601.40 (+0.82%)</td><td>4.46 (-12.98%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28801.80 (n/a)</td><td>28445.98 (n/a)</td><td>28392.50 (n/a)</td><td>28216.50 (n/a)</td><td>242.32 (n/a)</td><td>608.86 (n/a)</td><td>603.98 (n/a)</td><td>605.09 (n/a)</td><td>596.49 (n/a)</td><td>5.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.62 (-0.05%)</td><td>3.47 (-1.39%)</td><td>3.49 (-1.27%)</td><td>3.31 (-1.02%)</td><td>0.14 <b>(+29.91%)</b></td><td>7599.90 (+1.03%)</td><td>7252.64 (+1.47%)</td><td>7202.70 (+1.28%)</td><td>6943.00 (+0.05%)</td><td>302.64 <b>(+31.06%)</b></td><td>2474.42 (-0.05%)</td><td>2372.06 (-1.39%)</td><td>2385.20 (-1.27%)</td><td>2260.53 (-1.02%)</td><td>98.49 <b>(+29.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.63 (n/a)</td><td>3.52 (n/a)</td><td>3.54 (n/a)</td><td>3.35 (n/a)</td><td>0.11 (n/a)</td><td>7522.60 (n/a)</td><td>7147.38 (n/a)</td><td>7111.50 (n/a)</td><td>6939.60 (n/a)</td><td>230.91 (n/a)</td><td>2475.64 (n/a)</td><td>2405.62 (n/a)</td><td>2415.79 (n/a)</td><td>2283.77 (n/a)</td><td>75.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.26 (+3.19%)</td><td>2.99 (+3.81%)</td><td>2.91 (+3.05%)</td><td>2.79 (+2.55%)</td><td>0.19 (+17.92%)</td><td>9004.30 (-2.49%)</td><td>8442.80 (-3.59%)</td><td>8637.00 (-2.96%)</td><td>7724.10 (-3.09%)</td><td>532.42 (+12.63%)</td><td>2224.19 (+3.19%)</td><td>2041.49 (+3.81%)</td><td>1989.09 (+3.05%)</td><td>1907.95 (+2.55%)</td><td>131.78 (+17.92%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.16 (n/a)</td><td>2.88 (n/a)</td><td>2.83 (n/a)</td><td>2.73 (n/a)</td><td>0.16 (n/a)</td><td>9233.90 (n/a)</td><td>8757.44 (n/a)</td><td>8900.20 (n/a)</td><td>7970.10 (n/a)</td><td>472.73 (n/a)</td><td>2155.53 (n/a)</td><td>1966.56 (n/a)</td><td>1930.27 (n/a)</td><td>1860.53 (n/a)</td><td>111.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.32 (-0.09%)</td><td>3.19 (-1.52%)</td><td>3.16 (-3.79%)</td><td>3.15 (+0.11%)</td><td>0.07 (-17.34%)</td><td>7993.30 (-0.11%)</td><td>7891.94 (+1.52%)</td><td>7963.30 (+3.94%)</td><td>7587.50 (+0.08%)</td><td>170.95 (-17.88%)</td><td>2264.23 (-0.09%)</td><td>2177.73 (-1.52%)</td><td>2157.37 (-3.79%)</td><td>2149.30 (+0.11%)</td><td>48.55 (-17.34%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.32 (n/a)</td><td>3.24 (n/a)</td><td>3.28 (n/a)</td><td>3.14 (n/a)</td><td>0.09 (n/a)</td><td>8001.90 (n/a)</td><td>7773.72 (n/a)</td><td>7661.80 (n/a)</td><td>7581.10 (n/a)</td><td>208.18 (n/a)</td><td>2266.16 (n/a)</td><td>2211.26 (n/a)</td><td>2242.28 (n/a)</td><td>2146.97 (n/a)</td><td>58.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.79 (-0.11%)</td><td>0.78 (-0.08%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.11%)</td><td>0.00 (-0.33%)</td><td>96611.50 (+0.12%)</td><td>96453.88 (+0.08%)</td><td>96456.60 (+0.02%)</td><td>96158.20 (+0.11%)</td><td>180.67 (-0.10%)</td><td>714.65 (-0.11%)</td><td>712.46 (-0.08%)</td><td>712.44 (-0.02%)</td><td>711.30 (-0.11%)</td><td>1.34 (-0.33%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96500.40 (n/a)</td><td>96373.40 (n/a)</td><td>96433.70 (n/a)</td><td>96054.40 (n/a)</td><td>180.84 (n/a)</td><td>715.42 (n/a)</td><td>713.06 (n/a)</td><td>712.61 (n/a)</td><td>712.12 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.73 (+0.03%)</td><td>0.73 (+0.14%)</td><td>0.73 (+0.17%)</td><td>0.73 (+0.18%)</td><td>0.00 <b>(-67.43%)</b></td><td>103713.20 (-0.18%)</td><td>103654.48 (-0.14%)</td><td>103649.50 (-0.17%)</td><td>103617.70 (-0.03%)</td><td>35.38 <b>(-67.49%)</b></td><td>663.20 (+0.03%)</td><td>662.97 (+0.14%)</td><td>663.00 (+0.17%)</td><td>662.59 (+0.18%)</td><td>0.23 <b>(-67.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103905.00 (n/a)</td><td>103803.30 (n/a)</td><td>103824.30 (n/a)</td><td>103652.50 (n/a)</td><td>108.84 (n/a)</td><td>662.98 (n/a)</td><td>662.02 (n/a)</td><td>661.88 (n/a)</td><td>661.37 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.70 (+0.16%)</td><td>0.69 (+0.23%)</td><td>0.69 (+0.20%)</td><td>0.69 (+0.22%)</td><td>0.00 (-7.37%)</td><td>108949.70 (-0.22%)</td><td>108732.18 (-0.23%)</td><td>108825.20 (-0.20%)</td><td>108444.90 (-0.16%)</td><td>219.28 (-7.72%)</td><td>633.68 (+0.16%)</td><td>632.01 (+0.23%)</td><td>631.47 (+0.20%)</td><td>630.75 (+0.22%)</td><td>1.28 (-7.37%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109189.20 (n/a)</td><td>108981.00 (n/a)</td><td>109042.80 (n/a)</td><td>108616.30 (n/a)</td><td>237.63 (n/a)</td><td>632.68 (n/a)</td><td>630.57 (n/a)</td><td>630.21 (n/a)</td><td>629.36 (n/a)</td><td>1.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.48 (-2.08%)</td><td>6.56 (-9.87%)</td><td>6.60 (-12.17%)</td><td>5.09 <b>(-25.42%)</b></td><td>0.93 <b>(+142.42%)</b></td><td>1752.50 <b>(+34.08%)</b></td><td>1383.12 (+12.74%)</td><td>1350.50 (+13.85%)</td><td>1191.60 (+2.12%)</td><td>221.57 <b>(+235.82%)</b></td><td>450.53 (-2.08%)</td><td>395.31 (-9.87%)</td><td>397.53 (-12.17%)</td><td>306.34 <b>(-25.42%)</b></td><td>56.15 <b>(+142.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.64 (n/a)</td><td>7.28 (n/a)</td><td>7.51 (n/a)</td><td>6.82 (n/a)</td><td>0.38 (n/a)</td><td>1307.10 (n/a)</td><td>1226.82 (n/a)</td><td>1186.20 (n/a)</td><td>1166.90 (n/a)</td><td>65.98 (n/a)</td><td>460.09 (n/a)</td><td>438.62 (n/a)</td><td>452.61 (n/a)</td><td>410.73 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.97 (+2.29%)</td><td>6.45 (+0.67%)</td><td>6.71 (+6.16%)</td><td>5.32 (-13.23%)</td><td>0.68 <b>(+127.95%)</b></td><td>1676.40 (+15.25%)</td><td>1395.14 (+0.16%)</td><td>1328.40 (-5.80%)</td><td>1278.50 (-2.24%)</td><td>164.41 <b>(+158.33%)</b></td><td>419.94 (+2.29%)</td><td>388.66 (+0.67%)</td><td>404.14 (+6.16%)</td><td>320.26 (-13.23%)</td><td>40.85 <b>(+127.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.82 (n/a)</td><td>6.41 (n/a)</td><td>6.32 (n/a)</td><td>6.13 (n/a)</td><td>0.30 (n/a)</td><td>1454.60 (n/a)</td><td>1392.98 (n/a)</td><td>1410.20 (n/a)</td><td>1307.80 (n/a)</td><td>63.64 (n/a)</td><td>410.52 (n/a)</td><td>386.06 (n/a)</td><td>380.70 (n/a)</td><td>369.09 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.95 (-1.73%)</td><td>6.38 (-0.53%)</td><td>6.24 (-6.00%)</td><td>6.04 (+17.26%)</td><td>0.38 <b>(-47.91%)</b></td><td>1474.80 (-14.72%)</td><td>1401.38 (-0.40%)</td><td>1428.80 (+6.39%)</td><td>1281.90 (+1.75%)</td><td>81.14 <b>(-56.03%)</b></td><td>418.81 (-1.73%)</td><td>384.16 (-0.53%)</td><td>375.76 (-6.00%)</td><td>364.02 (+17.26%)</td><td>22.99 <b>(-47.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.07 (n/a)</td><td>6.41 (n/a)</td><td>6.64 (n/a)</td><td>5.15 (n/a)</td><td>0.73 (n/a)</td><td>1729.40 (n/a)</td><td>1406.96 (n/a)</td><td>1343.00 (n/a)</td><td>1259.80 (n/a)</td><td>184.53 (n/a)</td><td>426.16 (n/a)</td><td>386.20 (n/a)</td><td>399.74 (n/a)</td><td>310.43 (n/a)</td><td>44.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.98 (-0.41%)</td><td>7.91 (+4.30%)</td><td>7.95 (+6.73%)</td><td>7.77 (+8.74%)</td><td>0.09 <b>(-77.66%)</b></td><td>4485.30 (-8.04%)</td><td>4409.80 (-4.32%)</td><td>4388.30 (-6.30%)</td><td>4369.20 (+0.41%)</td><td>49.49 <b>(-79.18%)</b></td><td>491.50 (-0.41%)</td><td>487.03 (+4.30%)</td><td>489.37 (+6.73%)</td><td>478.79 (+8.74%)</td><td>5.42 <b>(-77.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>8.01 (n/a)</td><td>7.58 (n/a)</td><td>7.44 (n/a)</td><td>7.15 (n/a)</td><td>0.39 (n/a)</td><td>4877.50 (n/a)</td><td>4608.74 (n/a)</td><td>4683.40 (n/a)</td><td>4351.50 (n/a)</td><td>237.73 (n/a)</td><td>493.51 (n/a)</td><td>466.96 (n/a)</td><td>458.53 (n/a)</td><td>440.29 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.94 (+2.61%)</td><td>7.44 (-0.26%)</td><td>7.56 (+0.67%)</td><td>6.94 (-0.78%)</td><td>0.38 <b>(+38.80%)</b></td><td>5023.20 (+0.79%)</td><td>4695.84 (+0.37%)</td><td>4612.10 (-0.66%)</td><td>4392.60 (-2.54%)</td><td>243.72 <b>(+35.48%)</b></td><td>488.89 (+2.61%)</td><td>458.30 (-0.26%)</td><td>465.62 (+0.67%)</td><td>427.51 (-0.78%)</td><td>23.65 <b>(+38.80%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.74 (n/a)</td><td>7.46 (n/a)</td><td>7.51 (n/a)</td><td>7.00 (n/a)</td><td>0.28 (n/a)</td><td>4984.00 (n/a)</td><td>4678.76 (n/a)</td><td>4642.90 (n/a)</td><td>4507.10 (n/a)</td><td>179.90 (n/a)</td><td>476.47 (n/a)</td><td>459.51 (n/a)</td><td>462.53 (n/a)</td><td>430.88 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.36 (-4.38%)</td><td>7.13 (-3.15%)</td><td>7.27 (-0.16%)</td><td>6.81 (-5.16%)</td><td>0.26 <b>(+27.02%)</b></td><td>5119.30 (+5.44%)</td><td>4893.38 (+3.30%)</td><td>4795.90 (+0.16%)</td><td>4739.70 (+4.58%)</td><td>177.61 <b>(+40.48%)</b></td><td>453.09 (-4.38%)</td><td>439.31 (-3.15%)</td><td>447.77 (-0.16%)</td><td>419.49 (-5.16%)</td><td>15.73 <b>(+27.02%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.69 (n/a)</td><td>7.36 (n/a)</td><td>7.28 (n/a)</td><td>7.18 (n/a)</td><td>0.20 (n/a)</td><td>4855.00 (n/a)</td><td>4736.86 (n/a)</td><td>4788.30 (n/a)</td><td>4532.10 (n/a)</td><td>126.43 (n/a)</td><td>473.84 (n/a)</td><td>453.62 (n/a)</td><td>448.48 (n/a)</td><td>442.32 (n/a)</td><td>12.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.79 (-0.03%)</td><td>0.79 (-0.04%)</td><td>0.79 (-0.03%)</td><td>0.79 (-0.03%)</td><td>0.00 (+4.90%)</td><td>95893.90 (+0.03%)</td><td>95793.72 (+0.04%)</td><td>95771.80 (+0.03%)</td><td>95724.70 (+0.03%)</td><td>69.24 (+4.94%)</td><td>717.89 (-0.03%)</td><td>717.37 (-0.04%)</td><td>717.53 (-0.03%)</td><td>716.62 (-0.03%)</td><td>0.52 (+4.90%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95868.50 (n/a)</td><td>95756.80 (n/a)</td><td>95741.60 (n/a)</td><td>95692.40 (n/a)</td><td>65.98 (n/a)</td><td>718.13 (n/a)</td><td>717.65 (n/a)</td><td>717.76 (n/a)</td><td>716.81 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.73 (+0.02%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.03%)</td><td>0.73 (+0.09%)</td><td>0.00 <b>(-47.20%)</b></td><td>102954.10 (-0.09%)</td><td>102924.34 (-0.03%)</td><td>102919.80 (-0.03%)</td><td>102895.70 (-0.02%)</td><td>27.47 <b>(-47.30%)</b></td><td>667.86 (+0.02%)</td><td>667.67 (+0.03%)</td><td>667.70 (+0.03%)</td><td>667.48 (+0.09%)</td><td>0.18 <b>(-47.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103051.20 (n/a)</td><td>102960.16 (n/a)</td><td>102946.00 (n/a)</td><td>102918.70 (n/a)</td><td>52.12 (n/a)</td><td>667.71 (n/a)</td><td>667.44 (n/a)</td><td>667.53 (n/a)</td><td>666.85 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.70 (-0.02%)</td><td>0.70 (+0.01%)</td><td>0.70 (-0.04%)</td><td>0.70 (-0.05%)</td><td>0.00 (+8.17%)</td><td>108001.90 (+0.05%)</td><td>107787.92 (-0.01%)</td><td>107868.50 (+0.04%)</td><td>107533.40 (+0.02%)</td><td>193.73 (+8.23%)</td><td>639.05 (-0.02%)</td><td>637.55 (+0.01%)</td><td>637.07 (-0.04%)</td><td>636.28 (-0.05%)</td><td>1.15 (+8.17%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107950.60 (n/a)</td><td>107799.20 (n/a)</td><td>107830.20 (n/a)</td><td>107508.30 (n/a)</td><td>178.99 (n/a)</td><td>639.20 (n/a)</td><td>637.48 (n/a)</td><td>637.29 (n/a)</td><td>636.58 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>4.10 (-0.44%)</td><td>3.44 (-7.75%)</td><td>3.57 (-1.53%)</td><td>2.88 (-17.35%)</td><td>0.53 <b>(+119.12%)</b></td><td>2796.10 <b>(+20.99%)</b></td><td>2390.90 (+10.15%)</td><td>2258.50 (+1.55%)</td><td>1967.80 (+0.44%)</td><td>372.24 <b>(+177.20%)</b></td><td>1074.23 (-0.44%)</td><td>901.35 (-7.75%)</td><td>935.99 (-1.53%)</td><td>756.03 (-17.35%)</td><td>138.60 <b>(+119.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>4.11 (n/a)</td><td>3.73 (n/a)</td><td>3.62 (n/a)</td><td>3.49 (n/a)</td><td>0.24 (n/a)</td><td>2311.00 (n/a)</td><td>2170.50 (n/a)</td><td>2224.00 (n/a)</td><td>1959.10 (n/a)</td><td>134.28 (n/a)</td><td>1079.03 (n/a)</td><td>977.06 (n/a)</td><td>950.52 (n/a)</td><td>914.72 (n/a)</td><td>63.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.44 (+13.74%)</td><td>0.34 (+3.73%)</td><td>0.32 (+0.81%)</td><td>0.28 (-1.81%)</td><td>0.06 <b>(+72.39%)</b></td><td>4398.70 (+1.85%)</td><td>3809.78 (-2.05%)</td><td>3891.40 (-0.80%)</td><td>2851.10 (-12.08%)</td><td>638.33 <b>(+58.11%)</b></td><td>23.54 (+13.74%)</td><td>18.07 (+3.73%)</td><td>17.25 (+0.81%)</td><td>15.26 (-1.81%)</td><td>3.40 <b>(+72.39%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>4319.00 (n/a)</td><td>3889.50 (n/a)</td><td>3922.90 (n/a)</td><td>3242.80 (n/a)</td><td>403.72 (n/a)</td><td>20.69 (n/a)</td><td>17.42 (n/a)</td><td>17.11 (n/a)</td><td>15.54 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.25 (-1.28%)</td><td>5.14 (+16.50%)</td><td>4.81 <b>(+21.58%)</b></td><td>4.76 <b>(+45.89%)</b></td><td>0.64 <b>(-47.63%)</b></td><td>1398.60 <b>(-31.45%)</b></td><td>1309.38 (-17.79%)</td><td>1384.00 (-17.75%)</td><td>1065.00 (+1.29%)</td><td>142.25 <b>(-63.14%)</b></td><td>1929.76 (-1.28%)</td><td>1586.72 (+16.50%)</td><td>1485.02 <b>(+21.58%)</b></td><td>1469.49 <b>(+45.89%)</b></td><td>196.94 <b>(-47.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.33 (n/a)</td><td>4.41 (n/a)</td><td>3.95 (n/a)</td><td>3.26 (n/a)</td><td>1.22 (n/a)</td><td>2040.30 (n/a)</td><td>1592.74 (n/a)</td><td>1682.60 (n/a)</td><td>1051.40 (n/a)</td><td>385.91 (n/a)</td><td>1954.74 (n/a)</td><td>1361.93 (n/a)</td><td>1221.46 (n/a)</td><td>1007.29 (n/a)</td><td>376.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>13.52 (n/a)</td><td>12.89 (n/a)</td><td>13.17 (n/a)</td><td>12.00 (n/a)</td><td>0.60 (n/a)</td><td>13.51 (n/a)</td><td>12.89 (n/a)</td><td>13.17 (n/a)</td><td>11.99 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>24.95 (-0.04%)</td><td>24.13 (-0.17%)</td><td>23.93 (-1.37%)</td><td>23.56 (+2.99%)</td><td>0.55 <b>(-33.52%)</b></td><td>24.94 (-0.04%)</td><td>24.12 (-0.17%)</td><td>23.92 (-1.37%)</td><td>23.54 (+2.99%)</td><td>0.55 <b>(-33.52%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>24.96 (n/a)</td><td>24.17 (n/a)</td><td>24.27 (n/a)</td><td>22.87 (n/a)</td><td>0.82 (n/a)</td><td>24.95 (n/a)</td><td>24.16 (n/a)</td><td>24.25 (n/a)</td><td>22.86 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>42.56 (+1.30%)</td><td>39.82 (+0.47%)</td><td>39.08 (-0.67%)</td><td>38.47 (+0.81%)</td><td>1.62 (+13.16%)</td><td>42.53 (+1.30%)</td><td>39.79 (+0.47%)</td><td>39.06 (-0.67%)</td><td>38.45 (+0.81%)</td><td>1.62 (+13.16%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>42.01 (n/a)</td><td>39.63 (n/a)</td><td>39.35 (n/a)</td><td>38.16 (n/a)</td><td>1.43 (n/a)</td><td>41.98 (n/a)</td><td>39.61 (n/a)</td><td>39.32 (n/a)</td><td>38.14 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>43.61 (-1.76%)</td><td>41.40 (-2.29%)</td><td>41.27 (-2.76%)</td><td>38.94 (-2.09%)</td><td>1.82 (+6.40%)</td><td>43.58 (-1.76%)</td><td>41.37 (-2.29%)</td><td>41.25 (-2.76%)</td><td>38.91 (-2.09%)</td><td>1.82 (+6.40%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>44.39 (n/a)</td><td>42.37 (n/a)</td><td>42.45 (n/a)</td><td>39.77 (n/a)</td><td>1.71 (n/a)</td><td>44.36 (n/a)</td><td>42.34 (n/a)</td><td>42.42 (n/a)</td><td>39.74 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.72 (n/a)</td><td>12.08 (n/a)</td><td>12.15 (n/a)</td><td>11.36 (n/a)</td><td>0.54 (n/a)</td><td>12.72 (n/a)</td><td>12.07 (n/a)</td><td>12.15 (n/a)</td><td>11.35 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>24.40 (-2.27%)</td><td>23.83 (+0.79%)</td><td>23.97 (+0.22%)</td><td>22.49 (+3.29%)</td><td>0.77 <b>(-44.47%)</b></td><td>24.38 (-2.27%)</td><td>23.81 (+0.79%)</td><td>23.95 (+0.22%)</td><td>22.48 (+3.29%)</td><td>0.77 <b>(-44.47%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>24.96 (n/a)</td><td>23.64 (n/a)</td><td>23.91 (n/a)</td><td>21.77 (n/a)</td><td>1.40 (n/a)</td><td>24.95 (n/a)</td><td>23.63 (n/a)</td><td>23.90 (n/a)</td><td>21.76 (n/a)</td><td>1.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>40.58 (-0.18%)</td><td>39.61 (+1.97%)</td><td>39.67 (+3.85%)</td><td>38.76 (+2.29%)</td><td>0.76 <b>(-36.17%)</b></td><td>40.56 (-0.18%)</td><td>39.59 (+1.97%)</td><td>39.65 (+3.85%)</td><td>38.74 (+2.29%)</td><td>0.76 <b>(-36.17%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>40.65 (n/a)</td><td>38.85 (n/a)</td><td>38.20 (n/a)</td><td>37.89 (n/a)</td><td>1.19 (n/a)</td><td>40.63 (n/a)</td><td>38.82 (n/a)</td><td>38.18 (n/a)</td><td>37.87 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>44.19 (-1.56%)</td><td>43.20 (+4.77%)</td><td>43.16 (+4.92%)</td><td>42.14 (+10.91%)</td><td>0.90 <b>(-67.56%)</b></td><td>44.16 (-1.56%)</td><td>43.17 (+4.77%)</td><td>43.13 (+4.92%)</td><td>42.12 (+10.91%)</td><td>0.90 <b>(-67.56%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>44.89 (n/a)</td><td>41.23 (n/a)</td><td>41.13 (n/a)</td><td>38.00 (n/a)</td><td>2.77 (n/a)</td><td>44.86 (n/a)</td><td>41.21 (n/a)</td><td>41.11 (n/a)</td><td>37.98 (n/a)</td><td>2.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.17 (-3.67%)</td><td>8.45 (-7.47%)</td><td>8.44 (-6.63%)</td><td>7.57 (-14.12%)</td><td>0.58 <b>(+86.66%)</b></td><td>9.16 (-3.67%)</td><td>8.43 (-7.47%)</td><td>8.43 (-6.63%)</td><td>7.55 (-14.12%)</td><td>0.58 <b>(+86.66%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.52 (n/a)</td><td>9.13 (n/a)</td><td>9.04 (n/a)</td><td>8.81 (n/a)</td><td>0.31 (n/a)</td><td>9.50 (n/a)</td><td>9.12 (n/a)</td><td>9.02 (n/a)</td><td>8.79 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.98 (+3.01%)</td><td>0.82 (-9.23%)</td><td>0.81 (-14.44%)</td><td>0.74 (-6.55%)</td><td>0.10 <b>(+43.10%)</b></td><td>0.97 (+3.01%)</td><td>0.81 (-9.23%)</td><td>0.79 (-14.44%)</td><td>0.73 (-6.55%)</td><td>0.10 <b>(+43.10%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.96 (n/a)</td><td>0.90 (n/a)</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.07 (n/a)</td><td>0.94 (n/a)</td><td>0.89 (n/a)</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.16 (+0.85%)</td><td>1.05 (-1.46%)</td><td>1.01 (-2.79%)</td><td>0.98 (-2.22%)</td><td>0.07 (+19.21%)</td><td>1.14 (+0.85%)</td><td>1.04 (-1.46%)</td><td>1.00 (-2.79%)</td><td>0.97 (-2.22%)</td><td>0.07 (+19.21%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.15 (n/a)</td><td>1.06 (n/a)</td><td>1.04 (n/a)</td><td>1.01 (n/a)</td><td>0.06 (n/a)</td><td>1.13 (n/a)</td><td>1.05 (n/a)</td><td>1.03 (n/a)</td><td>0.99 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>16.37 (+6.70%)</td><td>15.32 (+2.55%)</td><td>15.34 (+2.51%)</td><td>14.35 (+0.10%)</td><td>0.85 <b>(+126.11%)</b></td><td>16.18 (+6.70%)</td><td>15.15 (+2.55%)</td><td>15.16 (+2.51%)</td><td>14.19 (+0.10%)</td><td>0.84 <b>(+126.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>15.34 (n/a)</td><td>14.94 (n/a)</td><td>14.96 (n/a)</td><td>14.34 (n/a)</td><td>0.38 (n/a)</td><td>15.17 (n/a)</td><td>14.77 (n/a)</td><td>14.79 (n/a)</td><td>14.17 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.13 (+2.54%)</td><td>11.71 (+9.42%)</td><td>11.76 (+1.12%)</td><td>10.97 <b>(+60.38%)</b></td><td>0.48 <b>(-77.81%)</b></td><td>11.91 (+2.54%)</td><td>11.50 (+9.42%)</td><td>11.55 (+1.12%)</td><td>10.78 <b>(+60.38%)</b></td><td>0.47 <b>(-77.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.83 (n/a)</td><td>10.70 (n/a)</td><td>11.63 (n/a)</td><td>6.84 (n/a)</td><td>2.16 (n/a)</td><td>11.62 (n/a)</td><td>10.51 (n/a)</td><td>11.42 (n/a)</td><td>6.72 (n/a)</td><td>2.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.19 (-14.28%)</td><td>7.12 (-2.44%)</td><td>7.21 (-1.21%)</td><td>6.01 <b>(+20.53%)</b></td><td>0.83 <b>(-52.43%)</b></td><td>8.04 (-14.28%)</td><td>7.00 (-2.44%)</td><td>7.09 (-1.21%)</td><td>5.91 <b>(+20.53%)</b></td><td>0.81 <b>(-52.43%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.55 (n/a)</td><td>7.30 (n/a)</td><td>7.30 (n/a)</td><td>4.99 (n/a)</td><td>1.73 (n/a)</td><td>9.38 (n/a)</td><td>7.17 (n/a)</td><td>7.17 (n/a)</td><td>4.90 (n/a)</td><td>1.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>6.29 (-7.87%)</td><td>5.78 (+3.48%)</td><td>6.07 (+7.12%)</td><td>4.65 (+0.03%)</td><td>0.69 (-16.81%)</td><td>6.19 (-7.87%)</td><td>5.69 (+3.48%)</td><td>5.97 (+7.12%)</td><td>4.58 (+0.03%)</td><td>0.68 (-16.81%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.83 (n/a)</td><td>5.58 (n/a)</td><td>5.67 (n/a)</td><td>4.65 (n/a)</td><td>0.83 (n/a)</td><td>6.72 (n/a)</td><td>5.49 (n/a)</td><td>5.58 (n/a)</td><td>4.58 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>13.23 (n/a)</td><td>12.59 (n/a)</td><td>12.81 (n/a)</td><td>11.67 (n/a)</td><td>0.62 (n/a)</td><td>13.22 (n/a)</td><td>12.58 (n/a)</td><td>12.81 (n/a)</td><td>11.67 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>13.35 (n/a)</td><td>12.46 (n/a)</td><td>12.20 (n/a)</td><td>11.87 (n/a)</td><td>0.62 (n/a)</td><td>13.34 (n/a)</td><td>12.45 (n/a)</td><td>12.19 (n/a)</td><td>11.86 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>174.06 (n/a)</td><td>174.00 (n/a)</td><td>127.10 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.80 (n/a)</td><td>187.26 (n/a)</td><td>196.20 (n/a)</td><td>147.60 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>185.48 (n/a)</td><td>191.30 (n/a)</td><td>127.30 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.80 (n/a)</td><td>190.78 (n/a)</td><td>193.30 (n/a)</td><td>161.70 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>180.96 (n/a)</td><td>186.00 (n/a)</td><td>153.50 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.60 (n/a)</td><td>196.28 (n/a)</td><td>202.70 (n/a)</td><td>164.00 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>266.90 (n/a)</td><td>230.34 (n/a)</td><td>213.50 (n/a)</td><td>204.30 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>285.60 (n/a)</td><td>230.16 (n/a)</td><td>219.90 (n/a)</td><td>194.40 (n/a)</td><td>34.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>187.56 (n/a)</td><td>197.80 (n/a)</td><td>137.40 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>387.00 (n/a)</td><td>227.54 (n/a)</td><td>180.30 (n/a)</td><td>158.00 (n/a)</td><td>93.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>188.22 (n/a)</td><td>197.10 (n/a)</td><td>145.20 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>169.58 (n/a)</td><td>168.20 (n/a)</td><td>150.00 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>182.50 (n/a)</td><td>203.90 (n/a)</td><td>134.20 (n/a)</td><td>40.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>169.18 (n/a)</td><td>164.90 (n/a)</td><td>132.60 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.60 (n/a)</td><td>216.06 (n/a)</td><td>214.20 (n/a)</td><td>138.80 (n/a)</td><td>57.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>285.90 (n/a)</td><td>242.00 (n/a)</td><td>223.60 (n/a)</td><td>195.80 (n/a)</td><td>39.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.40 (n/a)</td><td>153.46 (n/a)</td><td>162.20 (n/a)</td><td>122.00 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.00 (n/a)</td><td>174.06 (n/a)</td><td>175.10 (n/a)</td><td>136.40 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>160.02 (n/a)</td><td>160.70 (n/a)</td><td>136.60 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.50 (n/a)</td><td>179.28 (n/a)</td><td>179.40 (n/a)</td><td>147.80 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>173.58 (n/a)</td><td>180.50 (n/a)</td><td>149.70 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>187.34 (n/a)</td><td>187.90 (n/a)</td><td>157.20 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.60 (n/a)</td><td>192.84 (n/a)</td><td>212.60 (n/a)</td><td>146.90 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>209.06 (n/a)</td><td>207.20 (n/a)</td><td>172.80 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>197.12 (n/a)</td><td>194.70 (n/a)</td><td>186.00 (n/a)</td><td>10.64 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.70 (n/a)</td><td>173.86 (n/a)</td><td>166.10 (n/a)</td><td>147.00 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>192.18 (n/a)</td><td>191.00 (n/a)</td><td>181.40 (n/a)</td><td>7.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>188.62 (n/a)</td><td>193.80 (n/a)</td><td>163.30 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.70 (n/a)</td><td>178.54 (n/a)</td><td>184.10 (n/a)</td><td>141.60 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>281.60 (n/a)</td><td>214.18 (n/a)</td><td>205.00 (n/a)</td><td>171.50 (n/a)</td><td>42.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>188.26 (n/a)</td><td>189.10 (n/a)</td><td>175.70 (n/a)</td><td>7.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>261.90 (n/a)</td><td>229.00 (n/a)</td><td>239.10 (n/a)</td><td>187.10 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 <b>(-25.63%)</b></td><td>0.03 (-5.97%)</td><td>0.03 <b>(+20.50%)</b></td><td>0.02 (+9.95%)</td><td>0.00 <b>(-60.19%)</b></td><td>207.00 (-9.05%)</td><td>166.52 (-0.79%)</td><td>158.50 (-17.02%)</td><td>138.40 <b>(+34.50%)</b></td><td>26.04 <b>(-49.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>167.84 (n/a)</td><td>191.00 (n/a)</td><td>102.90 (n/a)</td><td>51.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-17.37%)</td><td>0.03 (+4.40%)</td><td>0.03 (+14.52%)</td><td>0.02 (+16.17%)</td><td>0.00 <b>(-73.03%)</b></td><td>174.50 (-13.91%)</td><td>159.12 (-7.42%)</td><td>158.60 (-12.71%)</td><td>149.30 <b>(+20.99%)</b></td><td>9.62 <b>(-72.34%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>171.88 (n/a)</td><td>181.70 (n/a)</td><td>123.40 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (+18.94%)</td><td>0.03 (-10.30%)</td><td>0.03 (+0.16%)</td><td>0.01 <b>(-47.39%)</b></td><td>0.01 <b>(+126.04%)</b></td><td>333.80 <b>(+90.09%)</b></td><td>187.68 <b>(+27.90%)</b></td><td>145.80 (-0.14%)</td><td>103.50 (-15.92%)</td><td>90.43 <b>(+282.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.60 (n/a)</td><td>146.74 (n/a)</td><td>146.00 (n/a)</td><td>123.10 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-2.15%)</td><td>0.02 (-13.32%)</td><td>0.02 (-12.45%)</td><td>0.01 <b>(-28.94%)</b></td><td>0.01 <b>(+44.16%)</b></td><td>306.90 <b>(+40.72%)</b></td><td>204.56 (+19.74%)</td><td>188.40 (+14.18%)</td><td>148.60 (+2.20%)</td><td>59.87 <b>(+113.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>170.84 (n/a)</td><td>165.00 (n/a)</td><td>145.40 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 <b>(-26.59%)</b></td><td>0.02 (-19.83%)</td><td>0.02 (-14.11%)</td><td>0.01 <b>(-35.82%)</b></td><td>0.01 (-14.54%)</td><td>370.40 <b>(+55.83%)</b></td><td>227.56 <b>(+28.16%)</b></td><td>192.50 (+16.45%)</td><td>174.80 <b>(+36.24%)</b></td><td>82.09 <b>(+82.59%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>177.56 (n/a)</td><td>165.30 (n/a)</td><td>128.30 (n/a)</td><td>44.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+14.42%)</td><td>0.03 (+10.34%)</td><td>0.03 (+10.06%)</td><td>0.02 (+5.72%)</td><td>0.01 <b>(+33.70%)</b></td><td>204.20 (-5.38%)</td><td>160.14 (-8.27%)</td><td>163.30 (-9.13%)</td><td>121.10 (-12.56%)</td><td>34.26 (+10.40%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>174.58 (n/a)</td><td>179.70 (n/a)</td><td>138.50 (n/a)</td><td>31.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 <b>(-20.76%)</b></td><td>0.02 (-12.00%)</td><td>0.02 (-5.68%)</td><td>0.02 (-11.67%)</td><td>0.00 <b>(-49.19%)</b></td><td>220.30 (+13.21%)</td><td>203.34 (+12.88%)</td><td>198.00 (+6.00%)</td><td>185.00 <b>(+26.19%)</b></td><td>14.40 <b>(-25.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>180.14 (n/a)</td><td>186.80 (n/a)</td><td>146.60 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-3.60%)</td><td>0.02 (+1.12%)</td><td>0.02 (+9.13%)</td><td>0.02 (-3.89%)</td><td>0.00 (-13.46%)</td><td>224.20 (+4.04%)</td><td>188.52 (-1.40%)</td><td>186.60 (-8.39%)</td><td>166.00 (+3.75%)</td><td>23.81 (-7.23%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>191.20 (n/a)</td><td>203.70 (n/a)</td><td>160.00 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-10.26%)</td><td>0.05 (-9.41%)</td><td>0.05 (-7.75%)</td><td>0.04 (-2.64%)</td><td>0.01 <b>(-31.79%)</b></td><td>192.50 (+2.72%)</td><td>173.20 (+9.10%)</td><td>178.80 (+8.36%)</td><td>138.40 (+11.43%)</td><td>20.42 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>158.76 (n/a)</td><td>165.00 (n/a)</td><td>124.20 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 <b>(-20.08%)</b></td><td>0.04 (-19.68%)</td><td>0.05 (-16.95%)</td><td>0.03 <b>(-22.03%)</b></td><td>0.01 <b>(-23.31%)</b></td><td>235.40 <b>(+28.21%)</b></td><td>189.34 <b>(+24.32%)</b></td><td>175.40 <b>(+20.47%)</b></td><td>154.90 <b>(+25.12%)</b></td><td>32.16 <b>(+22.54%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>152.30 (n/a)</td><td>145.60 (n/a)</td><td>123.80 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-17.43%)</td><td>0.04 (-19.18%)</td><td>0.04 <b>(-24.15%)</b></td><td>0.03 (-1.73%)</td><td>0.01 <b>(-29.65%)</b></td><td>250.10 (+1.75%)</td><td>211.72 <b>(+21.52%)</b></td><td>231.60 <b>(+31.89%)</b></td><td>159.30 <b>(+21.05%)</b></td><td>39.16 (-13.00%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.80 (n/a)</td><td>174.22 (n/a)</td><td>175.60 (n/a)</td><td>131.60 (n/a)</td><td>45.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-12.07%)</td><td>0.05 (+9.79%)</td><td>0.05 (+13.81%)</td><td>0.05 <b>(+34.04%)</b></td><td>0.01 <b>(-61.38%)</b></td><td>171.50 <b>(-25.40%)</b></td><td>158.26 (-13.23%)</td><td>165.30 (-12.12%)</td><td>141.10 (+13.79%)</td><td>14.73 <b>(-67.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>182.38 (n/a)</td><td>188.10 (n/a)</td><td>124.00 (n/a)</td><td>45.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (-0.26%)</td><td>0.05 (+0.11%)</td><td>0.05 (+9.90%)</td><td>0.04 (+5.67%)</td><td>0.01 <b>(-27.67%)</b></td><td>194.40 (-5.40%)</td><td>161.28 (-2.34%)</td><td>164.00 (-9.04%)</td><td>123.10 (+0.24%)</td><td>25.94 <b>(-30.93%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>165.14 (n/a)</td><td>180.30 (n/a)</td><td>122.80 (n/a)</td><td>37.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+4.05%)</td><td>0.05 (+0.21%)</td><td>0.05 (-4.49%)</td><td>0.04 <b>(+22.85%)</b></td><td>0.01 <b>(-33.94%)</b></td><td>188.80 (-18.59%)</td><td>170.06 (-1.96%)</td><td>173.90 (+4.70%)</td><td>142.10 (-3.92%)</td><td>17.12 <b>(-50.10%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>173.46 (n/a)</td><td>166.10 (n/a)</td><td>147.90 (n/a)</td><td>34.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-0.71%)</td><td>0.05 (-3.45%)</td><td>0.05 (+1.22%)</td><td>0.04 (-11.77%)</td><td>0.01 (+15.99%)</td><td>210.20 (+13.38%)</td><td>173.42 (+4.08%)</td><td>168.70 (-1.17%)</td><td>148.90 (+0.74%)</td><td>23.17 <b>(+36.18%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>166.62 (n/a)</td><td>170.70 (n/a)</td><td>147.80 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-15.81%)</td><td>0.04 (-10.74%)</td><td>0.04 (-7.80%)</td><td>0.04 (-9.26%)</td><td>0.00 <b>(-36.21%)</b></td><td>223.20 (+10.22%)</td><td>192.26 (+11.02%)</td><td>183.10 (+8.47%)</td><td>172.50 (+18.72%)</td><td>22.22 (-17.70%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>173.18 (n/a)</td><td>168.80 (n/a)</td><td>145.30 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-8.67%)</td><td>0.04 (+0.46%)</td><td>0.05 (+10.13%)</td><td>0.03 (-15.71%)</td><td>0.01 (+1.89%)</td><td>250.20 (+18.63%)</td><td>193.36 (+0.11%)</td><td>181.30 (-9.17%)</td><td>167.60 (+9.47%)</td><td>32.55 <b>(+40.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>193.14 (n/a)</td><td>199.60 (n/a)</td><td>153.10 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (-4.09%)</td><td>0.04 (-6.93%)</td><td>0.04 (-8.35%)</td><td>0.03 (-4.92%)</td><td>0.00 (-5.03%)</td><td>236.30 (+5.21%)</td><td>216.50 (+7.45%)</td><td>216.50 (+9.12%)</td><td>197.70 (+4.27%)</td><td>14.20 (+3.20%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>201.48 (n/a)</td><td>198.40 (n/a)</td><td>189.60 (n/a)</td><td>13.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-9.77%)</td><td>0.09 (-5.75%)</td><td>0.09 (+2.19%)</td><td>0.08 (+0.54%)</td><td>0.01 <b>(-30.24%)</b></td><td>204.70 (-0.53%)</td><td>178.96 (+4.84%)</td><td>178.10 (-2.14%)</td><td>148.20 (+10.85%)</td><td>23.96 <b>(-20.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>170.70 (n/a)</td><td>182.00 (n/a)</td><td>133.70 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-5.79%)</td><td>0.10 (+4.91%)</td><td>0.09 (+1.93%)</td><td>0.09 <b>(+21.57%)</b></td><td>0.01 <b>(-46.94%)</b></td><td>184.90 (-17.75%)</td><td>166.44 (-7.21%)</td><td>173.40 (-1.87%)</td><td>143.90 (+6.12%)</td><td>17.21 <b>(-54.15%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>179.38 (n/a)</td><td>176.70 (n/a)</td><td>135.60 (n/a)</td><td>37.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (+7.07%)</td><td>0.11 (+8.53%)</td><td>0.10 (+4.45%)</td><td>0.09 (+5.97%)</td><td>0.02 (+14.08%)</td><td>190.40 (-5.60%)</td><td>159.06 (-7.62%)</td><td>167.40 (-4.29%)</td><td>126.80 (-6.63%)</td><td>25.07 (+0.93%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>172.18 (n/a)</td><td>174.90 (n/a)</td><td>135.80 (n/a)</td><td>24.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+9.17%)</td><td>0.10 (+8.28%)</td><td>0.10 (+11.88%)</td><td>0.08 (+3.73%)</td><td>0.02 <b>(+46.85%)</b></td><td>208.40 (-3.56%)</td><td>171.16 (-6.30%)</td><td>161.60 (-10.62%)</td><td>135.60 (-8.44%)</td><td>33.03 <b>(+34.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>182.66 (n/a)</td><td>180.80 (n/a)</td><td>148.10 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 <b>(-27.62%)</b></td><td>0.09 <b>(-20.64%)</b></td><td>0.09 <b>(-24.46%)</b></td><td>0.07 (-10.04%)</td><td>0.01 <b>(-55.61%)</b></td><td>233.00 (+11.16%)</td><td>194.32 <b>(+23.03%)</b></td><td>190.90 <b>(+32.39%)</b></td><td>171.00 <b>(+38.13%)</b></td><td>23.46 <b>(-31.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.60 (n/a)</td><td>157.94 (n/a)</td><td>144.20 (n/a)</td><td>123.80 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (-14.54%)</td><td>0.08 (-17.05%)</td><td>0.08 (-11.69%)</td><td>0.05 <b>(-42.10%)</b></td><td>0.02 <b>(+50.73%)</b></td><td>347.40 <b>(+72.66%)</b></td><td>223.46 <b>(+26.08%)</b></td><td>197.70 (+13.23%)</td><td>180.20 (+17.01%)</td><td>69.66 <b>(+217.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>177.24 (n/a)</td><td>174.60 (n/a)</td><td>154.00 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (-11.17%)</td><td>0.09 (+2.82%)</td><td>0.09 (+10.39%)</td><td>0.08 (+11.30%)</td><td>0.00 <b>(-65.82%)</b></td><td>193.70 (-10.16%)</td><td>184.00 (-3.88%)</td><td>180.90 (-9.41%)</td><td>173.60 (+12.58%)</td><td>8.36 <b>(-64.54%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>191.42 (n/a)</td><td>199.70 (n/a)</td><td>154.20 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (-10.94%)</td><td>0.08 (+1.90%)</td><td>0.08 (+8.60%)</td><td>0.08 (+11.21%)</td><td>0.00 <b>(-71.56%)</b></td><td>207.80 (-10.08%)</td><td>201.18 (-3.27%)</td><td>204.00 (-7.90%)</td><td>188.00 (+12.31%)</td><td>7.89 <b>(-71.77%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>207.98 (n/a)</td><td>221.50 (n/a)</td><td>167.40 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (+1.77%)</td><td>0.20 (+6.80%)</td><td>0.19 (-3.31%)</td><td>0.18 (+19.58%)</td><td>0.02 <b>(-41.68%)</b></td><td>178.90 (-16.36%)</td><td>164.60 (-7.62%)</td><td>169.10 (+3.43%)</td><td>150.20 (-1.77%)</td><td>13.12 <b>(-52.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.90 (n/a)</td><td>178.18 (n/a)</td><td>163.50 (n/a)</td><td>152.90 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 <b>(-28.46%)</b></td><td>0.18 (-8.36%)</td><td>0.19 (+2.29%)</td><td>0.17 (-1.57%)</td><td>0.01 <b>(-70.11%)</b></td><td>198.00 (+1.59%)</td><td>183.16 (+6.62%)</td><td>176.20 (-2.22%)</td><td>172.70 <b>(+39.72%)</b></td><td>12.33 <b>(-56.21%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.90 (n/a)</td><td>171.78 (n/a)</td><td>180.20 (n/a)</td><td>123.60 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (-6.13%)</td><td>0.18 (-3.53%)</td><td>0.19 (-3.53%)</td><td>0.14 (-8.32%)</td><td>0.03 (-18.21%)</td><td>227.50 (+9.06%)</td><td>181.16 (+3.17%)</td><td>173.40 (+3.71%)</td><td>155.40 (+6.51%)</td><td>27.85 (-4.34%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.60 (n/a)</td><td>175.60 (n/a)</td><td>167.20 (n/a)</td><td>145.90 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (-19.01%)</td><td>0.19 (-8.71%)</td><td>0.18 (-11.19%)</td><td>0.16 (+4.48%)</td><td>0.03 <b>(-35.45%)</b></td><td>206.40 (-4.31%)</td><td>172.26 (+7.37%)</td><td>180.90 (+12.57%)</td><td>143.10 <b>(+23.47%)</b></td><td>26.66 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>215.70 (n/a)</td><td>160.44 (n/a)</td><td>160.70 (n/a)</td><td>115.90 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (-19.18%)</td><td>0.15 (-18.84%)</td><td>0.15 (-13.97%)</td><td>0.10 <b>(-29.23%)</b></td><td>0.03 (-18.41%)</td><td>330.00 <b>(+41.27%)</b></td><td>234.64 <b>(+24.00%)</b></td><td>217.50 (+16.25%)</td><td>181.40 <b>(+23.74%)</b></td><td>58.01 <b>(+45.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>233.60 (n/a)</td><td>189.22 (n/a)</td><td>187.10 (n/a)</td><td>146.60 (n/a)</td><td>39.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (+3.36%)</td><td>0.18 (-7.89%)</td><td>0.18 (-11.12%)</td><td>0.15 (-15.58%)</td><td>0.03 <b>(+73.68%)</b></td><td>224.20 (+18.44%)</td><td>187.64 (+10.77%)</td><td>185.30 (+12.51%)</td><td>148.10 (-3.27%)</td><td>35.01 <b>(+102.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>189.30 (n/a)</td><td>169.40 (n/a)</td><td>164.70 (n/a)</td><td>153.10 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (-2.58%)</td><td>0.15 (-7.03%)</td><td>0.15 (-9.51%)</td><td>0.13 (-5.58%)</td><td>0.02 (+7.78%)</td><td>253.90 (+5.92%)</td><td>217.78 (+7.80%)</td><td>214.30 (+10.52%)</td><td>184.80 (+2.61%)</td><td>26.10 (+15.18%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>239.70 (n/a)</td><td>202.02 (n/a)</td><td>193.90 (n/a)</td><td>180.10 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-19.55%)</td><td>0.02 <b>(-21.02%)</b></td><td>0.02 (-17.45%)</td><td>0.01 <b>(-48.20%)</b></td><td>0.01 <b>(+57.55%)</b></td><td>340.30 <b>(+93.02%)</b></td><td>209.96 <b>(+34.52%)</b></td><td>182.40 <b>(+21.12%)</b></td><td>163.30 <b>(+24.28%)</b></td><td>74.23 <b>(+278.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.30 (n/a)</td><td>156.08 (n/a)</td><td>150.60 (n/a)</td><td>131.40 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-10.28%)</td><td>0.02 (-17.77%)</td><td>0.02 (-18.65%)</td><td>0.02 (-19.82%)</td><td>0.00 (+11.32%)</td><td>221.40 <b>(+24.73%)</b></td><td>181.46 <b>(+23.04%)</b></td><td>171.50 <b>(+22.94%)</b></td><td>137.80 (+11.49%)</td><td>33.20 <b>(+54.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.50 (n/a)</td><td>147.48 (n/a)</td><td>139.50 (n/a)</td><td>123.60 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-1.85%)</td><td>0.02 (-9.05%)</td><td>0.02 (-9.82%)</td><td>0.01 <b>(-26.59%)</b></td><td>0.00 <b>(+86.05%)</b></td><td>308.80 <b>(+36.22%)</b></td><td>223.98 (+12.70%)</td><td>209.40 (+10.91%)</td><td>186.40 (+1.91%)</td><td>48.71 <b>(+168.10%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>198.74 (n/a)</td><td>188.80 (n/a)</td><td>182.90 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+10.16%)</td><td>0.02 (+2.44%)</td><td>0.02 (+2.20%)</td><td>0.02 (-5.70%)</td><td>0.00 <b>(+64.82%)</b></td><td>215.50 (+6.05%)</td><td>177.34 (-1.26%)</td><td>177.30 (-2.15%)</td><td>141.80 (-9.22%)</td><td>27.04 <b>(+58.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.20 (n/a)</td><td>179.60 (n/a)</td><td>181.20 (n/a)</td><td>156.20 (n/a)</td><td>17.03 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (+7.34%)</td><td>0.03 (-2.95%)</td><td>0.03 (-4.43%)</td><td>0.02 (-3.01%)</td><td>0.01 <b>(+40.92%)</b></td><td>201.50 (+3.12%)</td><td>163.32 (+5.56%)</td><td>159.70 (+4.58%)</td><td>110.10 (-6.85%)</td><td>38.43 <b>(+39.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>154.72 (n/a)</td><td>152.70 (n/a)</td><td>118.20 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+14.85%)</td><td>0.02 (+2.20%)</td><td>0.02 (+5.04%)</td><td>0.02 (-3.76%)</td><td>0.00 <b>(+46.91%)</b></td><td>233.30 (+3.92%)</td><td>176.98 (-0.71%)</td><td>165.30 (-4.84%)</td><td>136.60 (-12.94%)</td><td>35.97 <b>(+32.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>178.24 (n/a)</td><td>173.70 (n/a)</td><td>156.90 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+9.11%)</td><td>0.02 (+13.86%)</td><td>0.02 (+14.62%)</td><td>0.02 (-4.73%)</td><td>0.00 <b>(+35.38%)</b></td><td>241.50 (+4.95%)</td><td>178.62 (-11.09%)</td><td>171.30 (-12.74%)</td><td>149.90 (-8.32%)</td><td>36.46 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.10 (n/a)</td><td>200.90 (n/a)</td><td>196.30 (n/a)</td><td>163.50 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-7.87%)</td><td>0.02 (-0.73%)</td><td>0.02 (-6.31%)</td><td>0.02 (+9.49%)</td><td>0.00 <b>(-43.96%)</b></td><td>205.70 (-8.66%)</td><td>173.54 (-1.97%)</td><td>175.00 (+6.77%)</td><td>148.90 (+8.53%)</td><td>21.83 <b>(-45.20%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>177.02 (n/a)</td><td>163.90 (n/a)</td><td>137.20 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-1.44%)</td><td>0.02 (+1.84%)</td><td>0.02 (+18.69%)</td><td>0.01 <b>(-21.48%)</b></td><td>0.01 (+15.81%)</td><td>279.60 <b>(+27.32%)</b></td><td>184.32 (+1.39%)</td><td>165.10 (-15.77%)</td><td>125.40 (+1.46%)</td><td>61.20 <b>(+50.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>181.80 (n/a)</td><td>196.00 (n/a)</td><td>123.60 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-9.99%)</td><td>0.02 (+1.10%)</td><td>0.02 (+7.72%)</td><td>0.02 (-3.73%)</td><td>0.00 (-19.47%)</td><td>238.80 (+3.87%)</td><td>174.02 (-1.92%)</td><td>169.30 (-7.13%)</td><td>135.90 (+11.12%)</td><td>38.83 (-1.34%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>177.42 (n/a)</td><td>182.30 (n/a)</td><td>122.30 (n/a)</td><td>39.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+7.52%)</td><td>0.03 (+19.21%)</td><td>0.03 <b>(+36.66%)</b></td><td>0.02 (-7.65%)</td><td>0.01 <b>(+36.54%)</b></td><td>248.90 (+8.31%)</td><td>169.48 (-14.29%)</td><td>148.30 <b>(-26.84%)</b></td><td>139.90 (-6.98%)</td><td>45.99 <b>(+36.83%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>197.74 (n/a)</td><td>202.70 (n/a)</td><td>150.40 (n/a)</td><td>33.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-0.57%)</td><td>0.02 (+8.54%)</td><td>0.02 <b>(+29.21%)</b></td><td>0.02 (+17.38%)</td><td>0.00 <b>(-31.94%)</b></td><td>218.60 (-14.81%)</td><td>184.40 (-10.62%)</td><td>173.80 <b>(-22.62%)</b></td><td>148.10 (+0.54%)</td><td>30.18 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.60 (n/a)</td><td>206.30 (n/a)</td><td>224.60 (n/a)</td><td>147.30 (n/a)</td><td>49.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-0.51%)</td><td>0.02 (+0.25%)</td><td>0.02 (-9.24%)</td><td>0.02 (+2.56%)</td><td>0.00 (-12.32%)</td><td>221.90 (-2.50%)</td><td>191.28 (-0.87%)</td><td>201.50 (+10.17%)</td><td>153.20 (+0.52%)</td><td>26.38 (-17.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>192.96 (n/a)</td><td>182.90 (n/a)</td><td>152.40 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 <b>(+28.84%)</b></td><td>0.02 (+9.61%)</td><td>0.02 (+1.29%)</td><td>0.02 (+14.40%)</td><td>0.01 <b>(+67.00%)</b></td><td>226.30 (-12.59%)</td><td>186.28 (-7.06%)</td><td>187.10 (-1.27%)</td><td>126.80 <b>(-22.35%)</b></td><td>39.07 (+8.90%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.90 (n/a)</td><td>200.42 (n/a)</td><td>189.50 (n/a)</td><td>163.30 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+19.65%)</td><td>0.02 (+4.69%)</td><td>0.02 (-4.43%)</td><td>0.02 (+3.45%)</td><td>0.00 <b>(+56.60%)</b></td><td>231.70 (-3.34%)</td><td>191.90 (-3.14%)</td><td>204.20 (+4.61%)</td><td>139.90 (-16.43%)</td><td>34.57 <b>(+23.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.70 (n/a)</td><td>198.12 (n/a)</td><td>195.20 (n/a)</td><td>167.40 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 <b>(+26.33%)</b></td><td>0.02 (-3.75%)</td><td>0.02 (-4.29%)</td><td>0.02 <b>(-25.43%)</b></td><td>0.01 <b>(+239.89%)</b></td><td>258.10 <b>(+34.08%)</b></td><td>193.28 (+10.45%)</td><td>187.10 (+4.47%)</td><td>121.40 <b>(-20.86%)</b></td><td>52.59 <b>(+260.26%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.50 (n/a)</td><td>175.00 (n/a)</td><td>179.10 (n/a)</td><td>153.40 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (+13.98%)</td><td>0.05 (+6.31%)</td><td>0.05 (+11.90%)</td><td>0.04 (-6.58%)</td><td>0.01 <b>(+63.94%)</b></td><td>187.80 (+7.01%)</td><td>154.90 (-4.70%)</td><td>155.10 (-10.66%)</td><td>124.60 (-12.25%)</td><td>25.65 <b>(+52.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.50 (n/a)</td><td>162.54 (n/a)</td><td>173.60 (n/a)</td><td>142.00 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (+17.80%)</td><td>0.05 (+6.59%)</td><td>0.05 (-2.52%)</td><td>0.04 (-6.59%)</td><td>0.01 <b>(+94.00%)</b></td><td>212.20 (+7.06%)</td><td>161.22 (-3.28%)</td><td>171.10 (+2.58%)</td><td>117.30 (-15.06%)</td><td>37.27 <b>(+73.49%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>166.68 (n/a)</td><td>166.80 (n/a)</td><td>138.10 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (-13.15%)</td><td>0.04 (-9.81%)</td><td>0.04 (-16.14%)</td><td>0.04 (+0.22%)</td><td>0.00 <b>(-58.61%)</b></td><td>224.70 (-0.22%)</td><td>212.46 (+10.11%)</td><td>215.80 (+19.29%)</td><td>202.30 (+15.14%)</td><td>9.87 <b>(-52.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.20 (n/a)</td><td>192.96 (n/a)</td><td>180.90 (n/a)</td><td>175.70 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-6.33%)</td><td>0.04 (-11.60%)</td><td>0.04 (-13.71%)</td><td>0.03 <b>(-28.08%)</b></td><td>0.01 <b>(+38.12%)</b></td><td>299.70 <b>(+39.07%)</b></td><td>210.44 (+16.51%)</td><td>208.60 (+15.89%)</td><td>161.60 (+6.74%)</td><td>54.15 <b>(+109.40%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>180.62 (n/a)</td><td>180.00 (n/a)</td><td>151.40 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-16.94%)</td><td>0.05 (-4.22%)</td><td>0.05 (+5.58%)</td><td>0.05 (+9.70%)</td><td>0.00 <b>(-66.74%)</b></td><td>176.60 (-8.83%)</td><td>153.42 (+0.08%)</td><td>150.00 (-5.30%)</td><td>138.40 <b>(+20.45%)</b></td><td>14.11 <b>(-61.71%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>153.30 (n/a)</td><td>158.40 (n/a)</td><td>114.90 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (-7.17%)</td><td>0.05 (+0.15%)</td><td>0.06 (+10.78%)</td><td>0.05 (+2.33%)</td><td>0.01 <b>(-26.74%)</b></td><td>176.60 (-2.27%)</td><td>152.82 (-1.36%)</td><td>145.80 (-9.78%)</td><td>124.50 (+7.70%)</td><td>21.34 <b>(-22.43%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>154.92 (n/a)</td><td>161.60 (n/a)</td><td>115.60 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-4.48%)</td><td>0.05 (-6.42%)</td><td>0.05 (-14.39%)</td><td>0.04 (+0.24%)</td><td>0.01 (+3.90%)</td><td>208.70 (-0.24%)</td><td>165.44 (+7.16%)</td><td>169.80 (+16.86%)</td><td>128.40 (+4.65%)</td><td>35.34 (+3.65%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>154.38 (n/a)</td><td>145.30 (n/a)</td><td>122.70 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-11.67%)</td><td>0.04 (-10.76%)</td><td>0.04 <b>(-22.17%)</b></td><td>0.04 (-10.25%)</td><td>0.01 (+7.21%)</td><td>212.60 (+11.43%)</td><td>187.56 (+12.78%)</td><td>205.70 <b>(+28.48%)</b></td><td>153.80 (+13.17%)</td><td>30.56 <b>(+31.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>166.30 (n/a)</td><td>160.10 (n/a)</td><td>135.90 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-7.78%)</td><td>0.05 (+5.96%)</td><td>0.05 (+7.76%)</td><td>0.04 <b>(+24.18%)</b></td><td>0.00 <b>(-51.01%)</b></td><td>185.00 (-19.50%)</td><td>167.94 (-7.60%)</td><td>160.70 (-7.16%)</td><td>154.50 (+8.42%)</td><td>14.37 <b>(-57.37%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>181.76 (n/a)</td><td>173.10 (n/a)</td><td>142.50 (n/a)</td><td>33.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+4.70%)</td><td>0.05 (+10.48%)</td><td>0.05 (+18.86%)</td><td>0.05 (+16.66%)</td><td>0.01 <b>(-26.65%)</b></td><td>181.70 (-14.29%)</td><td>166.70 (-10.50%)</td><td>170.90 (-15.85%)</td><td>139.80 (-4.44%)</td><td>16.85 <b>(-40.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>186.26 (n/a)</td><td>203.10 (n/a)</td><td>146.30 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 <b>(+29.29%)</b></td><td>0.05 (+9.94%)</td><td>0.05 (+0.18%)</td><td>0.05 (+16.69%)</td><td>0.01 <b>(+76.71%)</b></td><td>180.40 (-14.34%)</td><td>166.08 (-8.14%)</td><td>173.80 (-0.23%)</td><td>124.80 <b>(-22.63%)</b></td><td>23.30 (+14.94%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>180.80 (n/a)</td><td>174.20 (n/a)</td><td>161.30 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-6.08%)</td><td>0.05 (-1.86%)</td><td>0.04 (-2.61%)</td><td>0.04 (+6.31%)</td><td>0.01 <b>(-21.90%)</b></td><td>216.00 (-5.92%)</td><td>179.68 (+0.66%)</td><td>183.20 (+2.69%)</td><td>140.80 (+6.51%)</td><td>27.33 <b>(-22.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>178.50 (n/a)</td><td>178.40 (n/a)</td><td>132.20 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+11.33%)</td><td>0.05 (+7.43%)</td><td>0.04 (+8.88%)</td><td>0.04 (+10.34%)</td><td>0.01 (+3.40%)</td><td>206.80 (-9.34%)</td><td>178.10 (-7.33%)</td><td>187.20 (-8.15%)</td><td>131.50 (-10.18%)</td><td>29.96 (-17.12%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>192.18 (n/a)</td><td>203.80 (n/a)</td><td>146.40 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (+5.69%)</td><td>0.05 (+12.90%)</td><td>0.05 (+6.62%)</td><td>0.04 <b>(+45.70%)</b></td><td>0.00 <b>(-45.38%)</b></td><td>187.90 <b>(-31.37%)</b></td><td>174.64 (-13.53%)</td><td>176.70 (-6.21%)</td><td>153.80 (-5.35%)</td><td>14.44 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>273.80 (n/a)</td><td>201.96 (n/a)</td><td>188.40 (n/a)</td><td>162.50 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+7.05%)</td><td>0.05 (-0.13%)</td><td>0.05 (-4.66%)</td><td>0.04 (+17.65%)</td><td>0.01 (-16.25%)</td><td>222.50 (-15.01%)</td><td>178.30 (-2.50%)</td><td>178.60 (+4.87%)</td><td>127.20 (-6.61%)</td><td>35.20 <b>(-33.19%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.80 (n/a)</td><td>182.88 (n/a)</td><td>170.30 (n/a)</td><td>136.20 (n/a)</td><td>52.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-9.31%)</td><td>0.04 (-9.26%)</td><td>0.04 (-10.19%)</td><td>0.04 (-9.24%)</td><td>0.01 (+4.98%)</td><td>214.90 (+10.15%)</td><td>186.26 (+10.46%)</td><td>189.80 (+11.32%)</td><td>164.50 (+10.25%)</td><td>21.54 <b>(+23.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>168.62 (n/a)</td><td>170.50 (n/a)</td><td>149.20 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+5.01%)</td><td>0.10 (+0.83%)</td><td>0.10 (-10.72%)</td><td>0.08 (+14.02%)</td><td>0.01 (-18.21%)</td><td>193.50 (-12.28%)</td><td>164.94 (-1.86%)</td><td>169.50 (+12.03%)</td><td>139.90 (-4.77%)</td><td>21.23 <b>(-32.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>168.06 (n/a)</td><td>151.30 (n/a)</td><td>146.90 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-7.36%)</td><td>0.10 (-13.07%)</td><td>0.10 (-17.10%)</td><td>0.07 (-6.36%)</td><td>0.02 <b>(-21.09%)</b></td><td>222.60 (+6.81%)</td><td>175.68 (+13.81%)</td><td>167.80 <b>(+20.63%)</b></td><td>134.00 (+7.98%)</td><td>34.16 (-6.56%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>154.36 (n/a)</td><td>139.10 (n/a)</td><td>124.10 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (+0.59%)</td><td>0.08 (+5.74%)</td><td>0.08 (+0.18%)</td><td>0.07 <b>(+24.58%)</b></td><td>0.01 <b>(-38.71%)</b></td><td>232.50 (-19.72%)</td><td>210.94 (-6.86%)</td><td>214.60 (-0.19%)</td><td>187.30 (-0.58%)</td><td>18.89 <b>(-52.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>289.60 (n/a)</td><td>226.48 (n/a)</td><td>215.00 (n/a)</td><td>188.40 (n/a)</td><td>39.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 (+6.26%)</td><td>0.08 (+9.07%)</td><td>0.08 (+11.13%)</td><td>0.07 (+15.82%)</td><td>0.01 <b>(-37.28%)</b></td><td>230.80 (-13.66%)</td><td>206.14 (-9.59%)</td><td>206.60 (-10.02%)</td><td>178.80 (-5.89%)</td><td>18.45 <b>(-49.13%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>267.30 (n/a)</td><td>228.00 (n/a)</td><td>229.60 (n/a)</td><td>190.00 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 <b>(-20.41%)</b></td><td>0.10 (-5.98%)</td><td>0.10 (+5.93%)</td><td>0.09 (+13.22%)</td><td>0.01 <b>(-61.33%)</b></td><td>178.70 (-11.67%)</td><td>166.56 (+1.91%)</td><td>171.00 (-5.63%)</td><td>138.60 <b>(+25.66%)</b></td><td>16.40 <b>(-57.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>202.30 (n/a)</td><td>163.44 (n/a)</td><td>181.20 (n/a)</td><td>110.30 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+0.51%)</td><td>0.09 (-12.11%)</td><td>0.09 (-13.31%)</td><td>0.07 <b>(-27.76%)</b></td><td>0.02 <b>(+85.99%)</b></td><td>246.10 <b>(+38.41%)</b></td><td>181.22 (+17.17%)</td><td>174.10 (+15.37%)</td><td>137.20 (-0.51%)</td><td>40.89 <b>(+159.82%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>154.66 (n/a)</td><td>150.90 (n/a)</td><td>137.90 (n/a)</td><td>15.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 <b>(-22.37%)</b></td><td>0.10 (+15.16%)</td><td>0.10 (+15.26%)</td><td>0.09 <b>(+77.25%)</b></td><td>0.01 <b>(-76.94%)</b></td><td>191.40 <b>(-43.59%)</b></td><td>167.54 <b>(-23.80%)</b></td><td>164.90 (-13.26%)</td><td>152.80 <b>(+28.84%)</b></td><td>14.72 <b>(-83.43%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>339.30 (n/a)</td><td>219.88 (n/a)</td><td>190.10 (n/a)</td><td>118.60 (n/a)</td><td>88.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 <b>(-20.42%)</b></td><td>0.10 (-19.42%)</td><td>0.11 (-4.74%)</td><td>0.04 <b>(-53.96%)</b></td><td>0.03 <b>(+47.34%)</b></td><td>377.90 <b>(+117.18%)</b></td><td>197.66 <b>(+39.26%)</b></td><td>151.70 (+4.98%)</td><td>137.00 <b>(+25.69%)</b></td><td>101.57 <b>(+333.34%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>174.00 (n/a)</td><td>141.94 (n/a)</td><td>144.50 (n/a)</td><td>109.00 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+6.26%)</td><td>0.10 (-2.79%)</td><td>0.09 (-12.96%)</td><td>0.09 (-1.52%)</td><td>0.01 <b>(+47.17%)</b></td><td>189.10 (+1.56%)</td><td>168.44 (+3.76%)</td><td>182.60 (+14.92%)</td><td>139.00 (-5.89%)</td><td>23.28 <b>(+42.64%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>162.34 (n/a)</td><td>158.90 (n/a)</td><td>147.70 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (-14.78%)</td><td>0.09 (+4.31%)</td><td>0.09 (+13.59%)</td><td>0.08 (+18.00%)</td><td>0.01 <b>(-50.20%)</b></td><td>203.00 (-15.24%)</td><td>178.76 (-6.63%)</td><td>173.30 (-11.99%)</td><td>157.00 (+17.34%)</td><td>19.71 <b>(-48.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.50 (n/a)</td><td>191.46 (n/a)</td><td>196.90 (n/a)</td><td>133.80 (n/a)</td><td>37.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (-17.84%)</td><td>0.09 (-9.91%)</td><td>0.09 (-8.97%)</td><td>0.08 (-4.97%)</td><td>0.01 <b>(-52.79%)</b></td><td>207.50 (+5.22%)</td><td>180.20 (+9.33%)</td><td>177.50 (+9.84%)</td><td>163.50 <b>(+21.74%)</b></td><td>16.45 <b>(-38.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.20 (n/a)</td><td>164.82 (n/a)</td><td>161.60 (n/a)</td><td>134.30 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 <b>(+37.78%)</b></td><td>0.10 (+4.94%)</td><td>0.09 (-5.70%)</td><td>0.07 (-3.48%)</td><td>0.03 <b>(+153.06%)</b></td><td>218.50 (+3.60%)</td><td>170.96 (-0.36%)</td><td>176.30 (+6.01%)</td><td>107.30 <b>(-27.40%)</b></td><td>41.44 <b>(+77.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>171.58 (n/a)</td><td>166.30 (n/a)</td><td>147.80 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (-0.26%)</td><td>0.09 (-5.61%)</td><td>0.09 (-12.67%)</td><td>0.08 (+7.38%)</td><td>0.01 (-16.22%)</td><td>212.90 (-6.91%)</td><td>188.74 (+5.32%)</td><td>189.40 (+14.51%)</td><td>163.80 (+0.24%)</td><td>21.61 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>179.20 (n/a)</td><td>165.40 (n/a)</td><td>163.40 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-17.94%)</td><td>0.09 (-10.94%)</td><td>0.09 (-7.89%)</td><td>0.08 (-5.46%)</td><td>0.01 <b>(-42.70%)</b></td><td>194.10 (+5.78%)</td><td>178.34 (+11.12%)</td><td>179.80 (+8.51%)</td><td>151.30 <b>(+21.82%)</b></td><td>17.05 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.50 (n/a)</td><td>160.50 (n/a)</td><td>165.70 (n/a)</td><td>124.20 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 <b>(-35.19%)</b></td><td>0.08 (-19.46%)</td><td>0.08 (-8.24%)</td><td>0.06 <b>(-26.60%)</b></td><td>0.01 <b>(-49.09%)</b></td><td>262.30 <b>(+36.19%)</b></td><td>206.82 <b>(+22.64%)</b></td><td>196.70 (+8.98%)</td><td>185.60 <b>(+54.28%)</b></td><td>31.91 (+11.28%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.60 (n/a)</td><td>168.64 (n/a)</td><td>180.50 (n/a)</td><td>120.30 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-18.65%)</td><td>0.08 <b>(-26.68%)</b></td><td>0.08 <b>(-22.72%)</b></td><td>0.05 <b>(-44.35%)</b></td><td>0.02 <b>(+52.81%)</b></td><td>299.10 <b>(+79.64%)</b></td><td>213.42 <b>(+44.34%)</b></td><td>197.90 <b>(+29.43%)</b></td><td>146.70 <b>(+22.86%)</b></td><td>64.22 <b>(+240.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>166.50 (n/a)</td><td>147.86 (n/a)</td><td>152.90 (n/a)</td><td>119.40 (n/a)</td><td>18.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 <b>(-29.63%)</b></td><td>0.17 <b>(-22.83%)</b></td><td>0.17 <b>(-21.92%)</b></td><td>0.15 (-16.31%)</td><td>0.01 <b>(-60.49%)</b></td><td>219.60 (+19.48%)</td><td>193.32 <b>(+27.71%)</b></td><td>189.60 <b>(+28.02%)</b></td><td>176.70 <b>(+42.16%)</b></td><td>16.23 <b>(-32.13%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>151.38 (n/a)</td><td>148.10 (n/a)</td><td>124.30 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 <b>(-22.67%)</b></td><td>0.18 (-15.31%)</td><td>0.17 (-13.00%)</td><td>0.15 (-14.39%)</td><td>0.02 <b>(-49.00%)</b></td><td>217.30 (+16.83%)</td><td>186.44 (+16.44%)</td><td>188.20 (+14.97%)</td><td>164.90 <b>(+29.33%)</b></td><td>20.20 <b>(-23.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.00 (n/a)</td><td>160.12 (n/a)</td><td>163.70 (n/a)</td><td>127.50 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (-4.02%)</td><td>0.14 (-19.11%)</td><td>0.14 <b>(-20.15%)</b></td><td>0.09 <b>(-40.90%)</b></td><td>0.03 <b>(+152.33%)</b></td><td>352.70 <b>(+69.24%)</b></td><td>246.14 <b>(+28.71%)</b></td><td>231.50 <b>(+25.20%)</b></td><td>185.40 (+4.22%)</td><td>62.82 <b>(+365.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>191.24 (n/a)</td><td>184.90 (n/a)</td><td>177.90 (n/a)</td><td>13.49 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (+2.99%)</td><td>0.16 (-5.66%)</td><td>0.14 (-14.67%)</td><td>0.14 (-9.45%)</td><td>0.03 <b>(+52.20%)</b></td><td>241.40 (+10.48%)</td><td>210.34 (+7.70%)</td><td>230.90 (+17.21%)</td><td>159.10 (-2.93%)</td><td>36.15 <b>(+64.98%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.50 (n/a)</td><td>195.30 (n/a)</td><td>197.00 (n/a)</td><td>163.90 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (-11.46%)</td><td>0.20 (-5.31%)</td><td>0.20 (+4.69%)</td><td>0.16 (-3.67%)</td><td>0.03 <b>(-29.85%)</b></td><td>198.80 (+3.81%)</td><td>167.18 (+3.92%)</td><td>163.90 (-4.49%)</td><td>130.70 (+12.96%)</td><td>26.88 (-18.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>191.50 (n/a)</td><td>160.88 (n/a)</td><td>171.60 (n/a)</td><td>115.70 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 <b>(-22.55%)</b></td><td>0.16 <b>(-25.91%)</b></td><td>0.16 <b>(-28.75%)</b></td><td>0.13 (-19.19%)</td><td>0.03 <b>(-29.57%)</b></td><td>256.40 <b>(+23.75%)</b></td><td>211.08 <b>(+33.85%)</b></td><td>207.90 <b>(+40.38%)</b></td><td>154.50 <b>(+29.18%)</b></td><td>39.67 (+11.19%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.20 (n/a)</td><td>157.70 (n/a)</td><td>148.10 (n/a)</td><td>119.60 (n/a)</td><td>35.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (-17.93%)</td><td>0.18 (-9.53%)</td><td>0.18 (-1.39%)</td><td>0.16 (-2.29%)</td><td>0.02 <b>(-56.78%)</b></td><td>201.00 (+2.34%)</td><td>180.86 (+7.98%)</td><td>186.10 (+1.42%)</td><td>158.00 <b>(+21.82%)</b></td><td>16.82 <b>(-46.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.40 (n/a)</td><td>167.50 (n/a)</td><td>183.50 (n/a)</td><td>129.70 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (-4.55%)</td><td>0.20 (-4.25%)</td><td>0.19 (-15.99%)</td><td>0.15 (-6.68%)</td><td>0.05 (+11.64%)</td><td>214.10 (+7.16%)</td><td>168.28 (+5.44%)</td><td>176.50 (+19.02%)</td><td>129.30 (+4.78%)</td><td>36.77 (+18.46%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.80 (n/a)</td><td>159.60 (n/a)</td><td>148.30 (n/a)</td><td>123.40 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (-9.30%)</td><td>0.19 (-10.98%)</td><td>0.18 (-5.16%)</td><td>0.15 (-11.97%)</td><td>0.04 (-12.48%)</td><td>214.50 (+13.61%)</td><td>180.20 (+12.05%)</td><td>183.90 (+5.39%)</td><td>129.40 (+10.22%)</td><td>32.00 (+5.82%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.80 (n/a)</td><td>160.82 (n/a)</td><td>174.50 (n/a)</td><td>117.40 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 (-5.57%)</td><td>0.16 <b>(-21.61%)</b></td><td>0.17 (-19.75%)</td><td>0.09 <b>(-45.78%)</b></td><td>0.05 <b>(+80.72%)</b></td><td>356.50 <b>(+84.43%)</b></td><td>217.08 <b>(+36.87%)</b></td><td>190.10 <b>(+24.57%)</b></td><td>149.20 (+5.89%)</td><td>80.36 <b>(+278.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.30 (n/a)</td><td>158.60 (n/a)</td><td>152.60 (n/a)</td><td>140.90 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (-9.85%)</td><td>0.18 (-8.54%)</td><td>0.19 (-0.53%)</td><td>0.15 (-13.07%)</td><td>0.02 (+7.45%)</td><td>215.00 (+15.03%)</td><td>184.10 (+9.66%)</td><td>172.20 (+0.58%)</td><td>168.10 (+10.96%)</td><td>20.08 <b>(+37.97%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>167.88 (n/a)</td><td>171.20 (n/a)</td><td>151.50 (n/a)</td><td>14.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (-4.31%)</td><td>0.18 (-5.98%)</td><td>0.18 (-7.13%)</td><td>0.15 (+0.76%)</td><td>0.02 (+0.51%)</td><td>216.60 (-0.73%)</td><td>189.32 (+6.43%)</td><td>185.00 (+7.68%)</td><td>163.10 (+4.48%)</td><td>25.09 (+3.50%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>177.88 (n/a)</td><td>171.80 (n/a)</td><td>156.10 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (+4.19%)</td><td>0.18 (+8.13%)</td><td>0.19 (+13.00%)</td><td>0.15 (+12.59%)</td><td>0.03 (-7.68%)</td><td>220.10 (-11.18%)</td><td>181.42 (-8.10%)</td><td>169.10 (-11.47%)</td><td>157.90 (-4.01%)</td><td>27.56 <b>(-20.97%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.80 (n/a)</td><td>197.40 (n/a)</td><td>191.00 (n/a)</td><td>164.50 (n/a)</td><td>34.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.27 <b>(+22.46%)</b></td><td>0.20 (+11.37%)</td><td>0.18 (-0.41%)</td><td>0.16 <b>(+20.74%)</b></td><td>0.04 <b>(+49.22%)</b></td><td>201.20 (-17.17%)</td><td>173.00 (-9.11%)</td><td>186.50 (+0.43%)</td><td>121.90 (-18.35%)</td><td>33.82 (+0.76%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>242.90 (n/a)</td><td>190.34 (n/a)</td><td>185.70 (n/a)</td><td>149.30 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (-7.17%)</td><td>0.17 (-8.83%)</td><td>0.16 (-9.63%)</td><td>0.15 (-8.48%)</td><td>0.02 (-1.71%)</td><td>214.00 (+9.24%)</td><td>199.72 (+9.76%)</td><td>205.10 (+10.63%)</td><td>169.30 (+7.70%)</td><td>17.45 (+14.29%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.90 (n/a)</td><td>181.96 (n/a)</td><td>185.40 (n/a)</td><td>157.20 (n/a)</td><td>15.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (+12.68%)</td><td>0.17 (-6.46%)</td><td>0.17 (-10.22%)</td><td>0.09 <b>(-42.31%)</b></td><td>0.06 <b>(+128.22%)</b></td><td>383.80 <b>(+73.35%)</b></td><td>218.68 (+18.37%)</td><td>191.80 (+11.38%)</td><td>140.90 (-11.27%)</td><td>96.22 <b>(+268.74%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>184.74 (n/a)</td><td>172.20 (n/a)</td><td>158.80 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (+0.82%)</td><td>0.21 (+0.15%)</td><td>0.21 (+0.00%)</td><td>0.21 (+0.01%)</td><td>0.00 <b>(+209.44%)</b></td><td>40880.60 (-0.01%)</td><td>40745.90 (-0.15%)</td><td>40829.40 (-0.00%)</td><td>40393.50 (-0.81%)</td><td>201.55 <b>(+206.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40884.20 (n/a)</td><td>40806.58 (n/a)</td><td>40830.30 (n/a)</td><td>40723.20 (n/a)</td><td>65.73 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (+0.14%)</td><td>0.21 (+0.10%)</td><td>0.21 (+0.10%)</td><td>0.21 (+0.04%)</td><td>0.00 <b>(+68.90%)</b></td><td>40917.50 (-0.04%)</td><td>40853.86 (-0.10%)</td><td>40846.20 (-0.10%)</td><td>40798.40 (-0.14%)</td><td>52.58 <b>(+68.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40933.10 (n/a)</td><td>40894.88 (n/a)</td><td>40886.00 (n/a)</td><td>40857.00 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (-0.04%)</td><td>0.13 (-0.03%)</td><td>0.13 (-0.04%)</td><td>0.13 (-0.02%)</td><td>0.00 (-11.68%)</td><td>321912.20 (+0.02%)</td><td>321770.64 (+0.03%)</td><td>321760.20 (+0.04%)</td><td>321628.00 (+0.04%)</td><td>117.20 (-11.74%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321847.40 (n/a)</td><td>321661.14 (n/a)</td><td>321640.00 (n/a)</td><td>321487.60 (n/a)</td><td>132.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 (+4.08%)</td><td>0.03 (+11.21%)</td><td>0.03 <b>(+29.63%)</b></td><td>0.02 (+6.92%)</td><td>0.01 (-1.00%)</td><td>218.10 (-6.48%)</td><td>152.12 (-10.75%)</td><td>126.80 <b>(-22.87%)</b></td><td>113.50 (-3.90%)</td><td>44.72 (-10.32%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>170.44 (n/a)</td><td>164.40 (n/a)</td><td>118.10 (n/a)</td><td>49.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 <b>(-22.85%)</b></td><td>0.03 (-18.24%)</td><td>0.03 (-19.01%)</td><td>0.02 <b>(-24.54%)</b></td><td>0.00 <b>(-21.96%)</b></td><td>277.50 <b>(+32.52%)</b></td><td>206.46 <b>(+22.51%)</b></td><td>193.60 <b>(+23.47%)</b></td><td>177.80 <b>(+29.59%)</b></td><td>40.61 <b>(+36.58%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>168.52 (n/a)</td><td>156.80 (n/a)</td><td>137.20 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+8.47%)</td><td>0.03 (-7.18%)</td><td>0.02 (-14.69%)</td><td>0.02 (-19.17%)</td><td>0.00 <b>(+143.91%)</b></td><td>199.10 <b>(+23.74%)</b></td><td>163.12 (+10.20%)</td><td>171.50 (+17.22%)</td><td>124.30 (-7.79%)</td><td>28.87 <b>(+173.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.90 (n/a)</td><td>148.02 (n/a)</td><td>146.30 (n/a)</td><td>134.80 (n/a)</td><td>10.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+10.58%)</td><td>0.03 (+8.19%)</td><td>0.03 (+9.88%)</td><td>0.02 (+4.33%)</td><td>0.00 <b>(+29.18%)</b></td><td>207.10 (-4.16%)</td><td>177.08 (-7.34%)</td><td>174.10 (-8.99%)</td><td>159.00 (-9.56%)</td><td>18.45 (+13.82%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.10 (n/a)</td><td>191.10 (n/a)</td><td>191.30 (n/a)</td><td>175.80 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-10.70%)</td><td>0.02 (-16.99%)</td><td>0.02 (-16.90%)</td><td>0.02 <b>(-24.80%)</b></td><td>0.00 <b>(+20.37%)</b></td><td>258.00 <b>(+32.99%)</b></td><td>194.14 <b>(+22.59%)</b></td><td>185.80 <b>(+20.34%)</b></td><td>146.80 (+11.98%)</td><td>40.72 <b>(+79.65%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>158.36 (n/a)</td><td>154.40 (n/a)</td><td>131.10 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 <b>(-21.21%)</b></td><td>0.03 (-16.25%)</td><td>0.03 (-14.57%)</td><td>0.03 (+1.81%)</td><td>0.00 <b>(-57.05%)</b></td><td>190.00 (-1.76%)</td><td>175.20 (+16.77%)</td><td>180.20 (+17.09%)</td><td>150.00 <b>(+26.90%)</b></td><td>15.62 <b>(-46.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>150.04 (n/a)</td><td>153.90 (n/a)</td><td>118.20 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-5.62%)</td><td>0.02 (-14.81%)</td><td>0.03 (-9.60%)</td><td>0.02 <b>(-25.73%)</b></td><td>0.00 <b>(+84.51%)</b></td><td>200.00 <b>(+34.59%)</b></td><td>167.70 (+19.36%)</td><td>161.80 (+10.59%)</td><td>132.40 (+6.00%)</td><td>26.80 <b>(+163.89%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>148.60 (n/a)</td><td>140.50 (n/a)</td><td>146.30 (n/a)</td><td>124.90 (n/a)</td><td>10.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-0.63%)</td><td>0.03 (-5.73%)</td><td>0.03 (-1.00%)</td><td>0.02 (-16.61%)</td><td>0.00 <b>(+51.78%)</b></td><td>244.10 (+19.95%)</td><td>184.90 (+8.20%)</td><td>171.70 (+1.00%)</td><td>150.80 (+0.67%)</td><td>38.33 <b>(+82.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.50 (n/a)</td><td>170.88 (n/a)</td><td>170.00 (n/a)</td><td>149.80 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+10.65%)</td><td>0.03 (-9.17%)</td><td>0.02 (-16.49%)</td><td>0.02 <b>(-24.28%)</b></td><td>0.00 <b>(+328.40%)</b></td><td>203.60 <b>(+32.12%)</b></td><td>168.24 (+13.20%)</td><td>180.10 (+19.75%)</td><td>125.30 (-9.66%)</td><td>30.75 <b>(+408.63%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>154.10 (n/a)</td><td>148.62 (n/a)</td><td>150.40 (n/a)</td><td>138.70 (n/a)</td><td>6.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 <b>(+28.14%)</b></td><td>0.03 (+6.80%)</td><td>0.03 (+1.56%)</td><td>0.02 (+3.39%)</td><td>0.00 <b>(+167.63%)</b></td><td>187.90 (-3.24%)</td><td>167.70 (-4.83%)</td><td>172.00 (-1.49%)</td><td>126.40 <b>(-21.98%)</b></td><td>24.13 <b>(+96.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>176.22 (n/a)</td><td>174.60 (n/a)</td><td>162.00 (n/a)</td><td>12.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (-5.25%)</td><td>0.02 (-10.76%)</td><td>0.02 (-16.20%)</td><td>0.02 (-5.63%)</td><td>0.00 (-3.43%)</td><td>230.90 (+5.92%)</td><td>187.86 (+12.03%)</td><td>190.20 (+19.32%)</td><td>145.30 (+5.52%)</td><td>30.90 (+3.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>167.68 (n/a)</td><td>159.40 (n/a)</td><td>137.70 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+4.76%)</td><td>0.02 (-5.18%)</td><td>0.02 (-5.80%)</td><td>0.01 <b>(-32.10%)</b></td><td>0.01 <b>(+132.05%)</b></td><td>308.90 <b>(+47.24%)</b></td><td>209.84 (+10.57%)</td><td>198.60 (+6.20%)</td><td>163.00 (-4.57%)</td><td>59.88 <b>(+220.82%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>189.78 (n/a)</td><td>187.00 (n/a)</td><td>170.80 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (-14.30%)</td><td>0.02 (-18.76%)</td><td>0.02 (-13.86%)</td><td>0.01 <b>(-25.22%)</b></td><td>0.00 (-0.26%)</td><td>275.10 <b>(+33.74%)</b></td><td>219.36 <b>(+24.47%)</b></td><td>199.40 (+16.13%)</td><td>171.40 (+16.68%)</td><td>43.56 <b>(+56.33%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>176.24 (n/a)</td><td>171.70 (n/a)</td><td>146.90 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.03 (+11.78%)</td><td>0.02 (+8.50%)</td><td>0.02 (+6.45%)</td><td>0.02 (-4.18%)</td><td>0.00 <b>(+25.05%)</b></td><td>254.40 (+4.35%)</td><td>195.24 (-7.13%)</td><td>186.50 (-6.05%)</td><td>157.70 (-10.50%)</td><td>36.39 (+15.81%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.80 (n/a)</td><td>210.24 (n/a)</td><td>198.50 (n/a)</td><td>176.20 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.02 (+0.62%)</td><td>0.02 (-5.30%)</td><td>0.02 (-7.96%)</td><td>0.02 (-8.08%)</td><td>0.00 <b>(+30.59%)</b></td><td>253.30 (+8.76%)</td><td>214.02 (+6.33%)</td><td>210.70 (+8.66%)</td><td>178.70 (-0.61%)</td><td>29.46 <b>(+40.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>201.28 (n/a)</td><td>193.90 (n/a)</td><td>179.80 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-18.12%)</td><td>0.05 (-11.30%)</td><td>0.05 (-9.35%)</td><td>0.04 (-7.37%)</td><td>0.00 <b>(-45.76%)</b></td><td>196.60 (+7.96%)</td><td>172.38 (+11.80%)</td><td>169.90 (+10.25%)</td><td>157.40 <b>(+22.11%)</b></td><td>14.64 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>154.18 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (-3.74%)</td><td>0.08 (+3.46%)</td><td>0.07 (-4.32%)</td><td>0.06 <b>(+62.08%)</b></td><td>0.01 <b>(-38.99%)</b></td><td>198.50 <b>(-38.30%)</b></td><td>166.46 (-11.10%)</td><td>167.70 (+4.49%)</td><td>129.10 (+3.86%)</td><td>30.63 <b>(-61.46%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>321.70 (n/a)</td><td>187.24 (n/a)</td><td>160.50 (n/a)</td><td>124.30 (n/a)</td><td>79.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-0.78%)</td><td>0.05 (-7.94%)</td><td>0.04 (-13.98%)</td><td>0.04 <b>(-22.35%)</b></td><td>0.01 <b>(+51.70%)</b></td><td>231.40 <b>(+28.77%)</b></td><td>178.02 (+11.50%)</td><td>184.10 (+16.30%)</td><td>129.60 (+0.78%)</td><td>39.03 <b>(+96.90%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>159.66 (n/a)</td><td>158.30 (n/a)</td><td>128.60 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 <b>(+22.40%)</b></td><td>0.07 (+5.79%)</td><td>0.07 (+11.49%)</td><td>0.05 (+1.26%)</td><td>0.01 <b>(+60.59%)</b></td><td>193.40 (-1.23%)</td><td>160.62 (-3.62%)</td><td>152.60 (-10.34%)</td><td>115.60 (-18.30%)</td><td>32.79 <b>(+36.75%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>166.66 (n/a)</td><td>170.20 (n/a)</td><td>141.50 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-8.24%)</td><td>0.05 (-16.04%)</td><td>0.05 (-18.83%)</td><td>0.04 (-19.12%)</td><td>0.01 <b>(+53.40%)</b></td><td>190.60 <b>(+23.61%)</b></td><td>171.48 <b>(+20.19%)</b></td><td>180.70 <b>(+23.26%)</b></td><td>139.20 (+9.01%)</td><td>20.91 <b>(+106.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>154.20 (n/a)</td><td>142.68 (n/a)</td><td>146.60 (n/a)</td><td>127.70 (n/a)</td><td>10.11 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.07 (+1.55%)</td><td>0.06 (-0.62%)</td><td>0.06 (+2.09%)</td><td>0.05 (+3.62%)</td><td>0.01 (-4.16%)</td><td>188.10 (-3.49%)</td><td>173.12 (+0.49%)</td><td>173.40 (-2.09%)</td><td>145.60 (-1.56%)</td><td>17.11 (-8.57%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>172.28 (n/a)</td><td>177.10 (n/a)</td><td>147.90 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+5.62%)</td><td>0.05 (-3.42%)</td><td>0.05 (-10.98%)</td><td>0.04 (+0.15%)</td><td>0.01 (+6.15%)</td><td>205.30 (-0.15%)</td><td>167.98 (+3.74%)</td><td>162.10 (+12.34%)</td><td>131.60 (-5.32%)</td><td>29.50 (+2.25%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>161.92 (n/a)</td><td>144.30 (n/a)</td><td>139.00 (n/a)</td><td>28.85 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-16.38%)</td><td>0.05 (-4.15%)</td><td>0.05 (-9.24%)</td><td>0.05 <b>(+38.07%)</b></td><td>0.01 <b>(-64.26%)</b></td><td>197.90 <b>(-27.56%)</b></td><td>178.68 (-3.21%)</td><td>182.70 (+10.19%)</td><td>147.70 (+19.60%)</td><td>18.56 <b>(-69.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>273.20 (n/a)</td><td>184.60 (n/a)</td><td>165.80 (n/a)</td><td>123.50 (n/a)</td><td>61.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (-19.89%)</td><td>0.05 (-9.75%)</td><td>0.05 (+0.64%)</td><td>0.04 (-6.06%)</td><td>0.01 <b>(-41.01%)</b></td><td>212.70 (+6.46%)</td><td>183.86 (+8.72%)</td><td>180.20 (-0.61%)</td><td>144.90 <b>(+24.81%)</b></td><td>26.14 (-19.61%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>169.12 (n/a)</td><td>181.30 (n/a)</td><td>116.10 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 (+6.15%)</td><td>0.05 (-8.15%)</td><td>0.04 (-16.71%)</td><td>0.04 (-17.16%)</td><td>0.01 <b>(+91.17%)</b></td><td>248.20 <b>(+20.72%)</b></td><td>204.44 (+12.06%)</td><td>217.50 <b>(+20.03%)</b></td><td>145.40 (-5.77%)</td><td>42.04 <b>(+117.93%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>182.44 (n/a)</td><td>181.20 (n/a)</td><td>154.30 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.06 <b>(+20.48%)</b></td><td>0.05 (+16.77%)</td><td>0.05 (+8.26%)</td><td>0.03 <b>(+28.04%)</b></td><td>0.01 (+4.68%)</td><td>239.10 <b>(-21.89%)</b></td><td>178.40 (-15.62%)</td><td>173.60 (-7.61%)</td><td>133.50 (-17.03%)</td><td>38.42 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.10 (n/a)</td><td>211.42 (n/a)</td><td>187.90 (n/a)</td><td>160.90 (n/a)</td><td>57.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (-11.20%)</td><td>0.04 (-11.67%)</td><td>0.04 (-6.49%)</td><td>0.04 (-17.50%)</td><td>0.00 (+1.95%)</td><td>242.00 <b>(+21.18%)</b></td><td>211.56 (+13.49%)</td><td>209.10 (+6.96%)</td><td>189.40 (+12.67%)</td><td>22.19 <b>(+37.94%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.70 (n/a)</td><td>186.42 (n/a)</td><td>195.50 (n/a)</td><td>168.10 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 <b>(-22.45%)</b></td><td>0.04 (-7.26%)</td><td>0.04 (+1.30%)</td><td>0.02 (-13.92%)</td><td>0.01 <b>(-25.67%)</b></td><td>331.50 (+16.19%)</td><td>216.90 (+7.24%)</td><td>191.40 (-1.29%)</td><td>172.50 <b>(+28.92%)</b></td><td>64.81 (+18.11%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>285.30 (n/a)</td><td>202.26 (n/a)</td><td>193.90 (n/a)</td><td>133.80 (n/a)</td><td>54.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.05 (+5.78%)</td><td>0.04 (+0.66%)</td><td>0.05 (+7.08%)</td><td>0.03 (-16.55%)</td><td>0.01 <b>(+106.05%)</b></td><td>271.10 (+19.85%)</td><td>209.96 (+1.22%)</td><td>191.30 (-6.64%)</td><td>175.30 (-5.45%)</td><td>38.21 <b>(+135.98%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.20 (n/a)</td><td>207.42 (n/a)</td><td>204.90 (n/a)</td><td>185.40 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.04 <b>(-23.10%)</b></td><td>0.03 <b>(-22.55%)</b></td><td>0.04 (-14.64%)</td><td>0.02 <b>(-35.55%)</b></td><td>0.01 <b>(+34.42%)</b></td><td>332.60 <b>(+55.13%)</b></td><td>244.50 <b>(+32.29%)</b></td><td>215.60 (+17.11%)</td><td>205.80 <b>(+30.09%)</b></td><td>54.07 <b>(+167.77%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>214.40 (n/a)</td><td>184.82 (n/a)</td><td>184.10 (n/a)</td><td>158.20 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 <b>(+28.82%)</b></td><td>0.10 (+13.19%)</td><td>0.09 (+7.39%)</td><td>0.08 (-4.65%)</td><td>0.02 <b>(+195.93%)</b></td><td>215.70 (+4.86%)</td><td>170.52 (-8.52%)</td><td>177.60 (-6.87%)</td><td>127.00 <b>(-22.37%)</b></td><td>37.56 <b>(+138.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>186.40 (n/a)</td><td>190.70 (n/a)</td><td>163.60 (n/a)</td><td>15.76 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 <b>(+28.08%)</b></td><td>0.15 (+4.68%)</td><td>0.14 (+1.33%)</td><td>0.11 (-17.32%)</td><td>0.03 <b>(+264.95%)</b></td><td>230.00 <b>(+20.99%)</b></td><td>173.38 (-1.31%)</td><td>174.00 (-1.30%)</td><td>128.60 <b>(-21.92%)</b></td><td>36.98 <b>(+249.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>175.68 (n/a)</td><td>176.30 (n/a)</td><td>164.70 (n/a)</td><td>10.58 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-19.39%)</td><td>0.09 (-0.95%)</td><td>0.09 (+12.19%)</td><td>0.07 (+4.76%)</td><td>0.02 <b>(-51.23%)</b></td><td>225.50 (-4.53%)</td><td>176.46 (-4.46%)</td><td>174.00 (-10.86%)</td><td>142.30 <b>(+24.06%)</b></td><td>30.65 <b>(-42.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>236.20 (n/a)</td><td>184.70 (n/a)</td><td>195.20 (n/a)</td><td>114.70 (n/a)</td><td>53.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (-6.79%)</td><td>0.10 (-9.10%)</td><td>0.10 (-5.29%)</td><td>0.09 (-10.29%)</td><td>0.02 (+10.22%)</td><td>234.00 (+11.48%)</td><td>205.26 (+10.65%)</td><td>201.20 (+5.56%)</td><td>163.40 (+7.29%)</td><td>29.64 <b>(+36.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>185.50 (n/a)</td><td>190.60 (n/a)</td><td>152.30 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+7.08%)</td><td>0.09 (+7.58%)</td><td>0.09 (+4.49%)</td><td>0.07 <b>(+21.50%)</b></td><td>0.02 (-5.86%)</td><td>242.90 (-17.69%)</td><td>188.76 (-8.50%)</td><td>187.40 (-4.34%)</td><td>140.80 (-6.57%)</td><td>36.97 <b>(-30.76%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>295.10 (n/a)</td><td>206.30 (n/a)</td><td>195.90 (n/a)</td><td>150.70 (n/a)</td><td>53.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-10.97%)</td><td>0.11 (-9.82%)</td><td>0.11 (-10.68%)</td><td>0.10 (-11.82%)</td><td>0.01 (-13.23%)</td><td>214.50 (+13.37%)</td><td>193.84 (+10.87%)</td><td>192.00 (+11.95%)</td><td>180.30 (+12.34%)</td><td>12.57 (+11.27%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>174.84 (n/a)</td><td>171.50 (n/a)</td><td>160.50 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 <b>(+21.68%)</b></td><td>0.11 <b>(+20.72%)</b></td><td>0.11 <b>(+34.32%)</b></td><td>0.07 (-10.96%)</td><td>0.02 <b>(+72.76%)</b></td><td>220.80 (+12.31%)</td><td>154.84 (-14.82%)</td><td>144.90 <b>(-25.58%)</b></td><td>116.50 (-17.84%)</td><td>39.05 <b>(+68.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>181.78 (n/a)</td><td>194.70 (n/a)</td><td>141.80 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (+0.90%)</td><td>0.11 (+8.14%)</td><td>0.11 <b>(+25.47%)</b></td><td>0.10 (+12.96%)</td><td>0.01 <b>(-35.34%)</b></td><td>188.00 (-11.45%)</td><td>168.88 (-8.77%)</td><td>161.70 <b>(-20.31%)</b></td><td>150.70 (-0.86%)</td><td>17.57 <b>(-41.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>185.12 (n/a)</td><td>202.90 (n/a)</td><td>152.00 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (+1.77%)</td><td>0.10 (-2.76%)</td><td>0.10 (-7.15%)</td><td>0.08 (+4.34%)</td><td>0.01 (-10.75%)</td><td>192.90 (-4.17%)</td><td>172.54 (+2.56%)</td><td>168.40 (+7.74%)</td><td>148.00 (-1.73%)</td><td>18.29 (-14.87%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>168.24 (n/a)</td><td>156.30 (n/a)</td><td>150.60 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-18.98%)</td><td>0.11 (-14.00%)</td><td>0.11 (-9.73%)</td><td>0.09 (+16.02%)</td><td>0.01 <b>(-55.67%)</b></td><td>198.40 (-13.78%)</td><td>174.66 (+11.80%)</td><td>165.40 (+10.78%)</td><td>152.20 <b>(+23.44%)</b></td><td>20.54 <b>(-52.60%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>230.10 (n/a)</td><td>156.22 (n/a)</td><td>149.30 (n/a)</td><td>123.30 (n/a)</td><td>43.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-0.66%)</td><td>0.09 (+6.62%)</td><td>0.09 (+16.50%)</td><td>0.07 (+13.14%)</td><td>0.02 (-18.78%)</td><td>251.70 (-11.62%)</td><td>192.98 (-8.24%)</td><td>175.20 (-14.16%)</td><td>150.40 (+0.60%)</td><td>40.65 <b>(-26.47%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.80 (n/a)</td><td>210.30 (n/a)</td><td>204.10 (n/a)</td><td>149.50 (n/a)</td><td>55.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.09 <b>(-21.49%)</b></td><td>0.09 (-13.56%)</td><td>0.08 (-14.90%)</td><td>0.08 (-9.53%)</td><td>0.01 <b>(-54.31%)</b></td><td>212.50 (+10.56%)</td><td>200.74 (+14.98%)</td><td>205.80 (+17.53%)</td><td>186.80 <b>(+27.33%)</b></td><td>11.37 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>174.58 (n/a)</td><td>175.10 (n/a)</td><td>146.70 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-4.51%)</td><td>0.09 (-6.18%)</td><td>0.09 (-6.29%)</td><td>0.08 (-10.05%)</td><td>0.01 <b>(+24.05%)</b></td><td>211.70 (+11.13%)</td><td>184.64 (+7.16%)</td><td>183.30 (+6.69%)</td><td>155.50 (+4.71%)</td><td>22.66 <b>(+46.84%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>172.30 (n/a)</td><td>171.80 (n/a)</td><td>148.50 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 (-1.53%)</td><td>0.08 (-4.38%)</td><td>0.08 (-10.22%)</td><td>0.08 (+3.80%)</td><td>0.01 <b>(-23.53%)</b></td><td>230.20 (-3.68%)</td><td>208.58 (+3.85%)</td><td>210.70 (+11.36%)</td><td>174.80 (+1.57%)</td><td>20.86 <b>(-27.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>200.84 (n/a)</td><td>189.20 (n/a)</td><td>172.10 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (+12.30%)</td><td>0.08 (-0.41%)</td><td>0.08 (-3.00%)</td><td>0.06 (-10.94%)</td><td>0.02 <b>(+99.15%)</b></td><td>254.90 (+12.29%)</td><td>209.28 (+2.95%)</td><td>212.70 (+3.10%)</td><td>155.20 (-10.96%)</td><td>41.32 <b>(+101.16%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>203.28 (n/a)</td><td>206.30 (n/a)</td><td>174.30 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 (-5.50%)</td><td>0.18 (+2.58%)</td><td>0.17 (-0.50%)</td><td>0.15 (+4.32%)</td><td>0.02 (-19.17%)</td><td>221.30 (-4.16%)</td><td>189.28 (-3.18%)</td><td>191.80 (+0.52%)</td><td>162.30 (+5.80%)</td><td>24.39 (-19.04%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.90 (n/a)</td><td>195.50 (n/a)</td><td>190.80 (n/a)</td><td>153.40 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (+7.00%)</td><td>0.17 (+4.38%)</td><td>0.17 (+4.95%)</td><td>0.13 (+9.57%)</td><td>0.03 (+4.54%)</td><td>246.80 (-8.76%)</td><td>193.38 (-4.43%)</td><td>191.70 (-4.72%)</td><td>153.90 (-6.50%)</td><td>36.46 (-12.26%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>270.50 (n/a)</td><td>202.34 (n/a)</td><td>201.20 (n/a)</td><td>164.60 (n/a)</td><td>41.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (-5.82%)</td><td>0.22 (-6.84%)</td><td>0.21 (+1.95%)</td><td>0.18 (-3.63%)</td><td>0.05 <b>(-25.74%)</b></td><td>232.90 (+3.74%)</td><td>191.82 (+4.95%)</td><td>198.60 (-1.93%)</td><td>136.40 (+6.15%)</td><td>34.83 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>224.50 (n/a)</td><td>182.78 (n/a)</td><td>202.50 (n/a)</td><td>128.50 (n/a)</td><td>44.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 <b>(-35.93%)</b></td><td>0.16 <b>(-25.86%)</b></td><td>0.16 <b>(-23.87%)</b></td><td>0.13 (-19.71%)</td><td>0.02 <b>(-61.95%)</b></td><td>247.40 <b>(+24.57%)</b></td><td>208.48 <b>(+31.92%)</b></td><td>204.80 <b>(+31.37%)</b></td><td>184.20 <b>(+56.10%)</b></td><td>23.44 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.60 (n/a)</td><td>158.04 (n/a)</td><td>155.90 (n/a)</td><td>118.00 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 <b>(-25.15%)</b></td><td>0.20 (-7.38%)</td><td>0.19 (-3.37%)</td><td>0.18 (+9.71%)</td><td>0.02 <b>(-66.34%)</b></td><td>224.50 (-8.85%)</td><td>206.20 (+4.37%)</td><td>214.20 (+3.48%)</td><td>184.10 <b>(+33.60%)</b></td><td>17.21 <b>(-58.35%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>246.30 (n/a)</td><td>197.56 (n/a)</td><td>207.00 (n/a)</td><td>137.80 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (-0.11%)</td><td>0.18 (-12.21%)</td><td>0.16 (-19.68%)</td><td>0.15 (-9.06%)</td><td>0.03 <b>(+26.33%)</b></td><td>215.50 (+9.95%)</td><td>187.74 (+14.90%)</td><td>198.80 <b>(+24.48%)</b></td><td>141.30 (+0.14%)</td><td>28.41 <b>(+34.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.00 (n/a)</td><td>163.40 (n/a)</td><td>159.70 (n/a)</td><td>141.10 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (-10.81%)</td><td>0.18 (-6.65%)</td><td>0.20 (+11.04%)</td><td>0.15 (-9.45%)</td><td>0.03 (-15.21%)</td><td>248.90 (+10.43%)</td><td>206.08 (+6.89%)</td><td>184.20 (-9.93%)</td><td>173.90 (+12.12%)</td><td>35.68 (+7.65%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>225.40 (n/a)</td><td>192.80 (n/a)</td><td>204.50 (n/a)</td><td>155.10 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (-14.47%)</td><td>0.18 (-0.07%)</td><td>0.18 (+3.53%)</td><td>0.16 (+15.36%)</td><td>0.01 <b>(-60.03%)</b></td><td>211.20 (-13.30%)</td><td>187.68 (-2.71%)</td><td>184.50 (-3.40%)</td><td>170.10 (+16.91%)</td><td>15.97 <b>(-59.34%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.60 (n/a)</td><td>192.90 (n/a)</td><td>191.00 (n/a)</td><td>145.50 (n/a)</td><td>39.29 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (-14.66%)</td><td>0.20 (-8.37%)</td><td>0.19 (-0.81%)</td><td>0.15 (-16.51%)</td><td>0.03 (-19.14%)</td><td>240.80 (+19.80%)</td><td>192.46 (+8.81%)</td><td>194.10 (+0.83%)</td><td>153.30 (+17.11%)</td><td>34.29 (+11.02%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>201.00 (n/a)</td><td>176.88 (n/a)</td><td>192.50 (n/a)</td><td>130.90 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 <b>(-29.06%)</b></td><td>0.18 (-13.98%)</td><td>0.19 (+6.40%)</td><td>0.13 (-19.74%)</td><td>0.03 <b>(-34.25%)</b></td><td>242.90 <b>(+24.63%)</b></td><td>191.82 (+15.29%)</td><td>169.30 (-6.05%)</td><td>159.80 <b>(+40.92%)</b></td><td>38.16 (+17.82%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>194.90 (n/a)</td><td>166.38 (n/a)</td><td>180.20 (n/a)</td><td>113.40 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (-16.08%)</td><td>0.17 (+0.88%)</td><td>0.17 (+11.70%)</td><td>0.15 (+6.10%)</td><td>0.01 <b>(-57.67%)</b></td><td>232.00 (-5.77%)</td><td>205.38 (-2.74%)</td><td>200.40 (-10.50%)</td><td>186.70 (+19.14%)</td><td>16.76 <b>(-50.39%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>246.20 (n/a)</td><td>211.16 (n/a)</td><td>223.90 (n/a)</td><td>156.70 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 <b>(-32.70%)</b></td><td>0.16 <b>(-21.41%)</b></td><td>0.16 (-18.66%)</td><td>0.15 (-0.21%)</td><td>0.01 <b>(-80.23%)</b></td><td>212.30 (+0.24%)</td><td>203.78 <b>(+23.74%)</b></td><td>207.60 <b>(+22.91%)</b></td><td>188.20 <b>(+48.54%)</b></td><td>9.38 <b>(-70.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.80 (n/a)</td><td>164.68 (n/a)</td><td>168.90 (n/a)</td><td>126.70 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (-2.91%)</td><td>0.18 (-5.44%)</td><td>0.16 (-9.29%)</td><td>0.16 (-2.50%)</td><td>0.02 (+2.17%)</td><td>222.00 (+2.54%)</td><td>201.14 (+5.90%)</td><td>212.90 (+10.25%)</td><td>165.40 (+2.99%)</td><td>24.07 (+8.74%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>189.94 (n/a)</td><td>193.10 (n/a)</td><td>160.60 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.16 (-19.91%)</td><td>0.15 (-13.26%)</td><td>0.15 (-6.74%)</td><td>0.13 (-14.42%)</td><td>0.01 <b>(-34.83%)</b></td><td>258.70 (+16.85%)</td><td>225.10 (+14.85%)</td><td>217.30 (+7.26%)</td><td>203.30 <b>(+24.88%)</b></td><td>21.40 (-2.57%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>196.00 (n/a)</td><td>202.60 (n/a)</td><td>162.80 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (-10.76%)</td><td>0.12 (-1.14%)</td><td>0.12 (+4.12%)</td><td>0.11 (+17.43%)</td><td>0.01 <b>(-52.03%)</b></td><td>193.50 (-14.83%)</td><td>173.08 (-1.23%)</td><td>170.90 (-3.93%)</td><td>151.40 (+12.07%)</td><td>15.99 <b>(-54.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>175.24 (n/a)</td><td>177.90 (n/a)</td><td>135.10 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (+17.25%)</td><td>0.11 (-4.01%)</td><td>0.10 (-15.40%)</td><td>0.06 <b>(-42.71%)</b></td><td>0.04 <b>(+237.52%)</b></td><td>363.30 <b>(+74.58%)</b></td><td>215.50 (+17.30%)</td><td>211.20 (+18.19%)</td><td>136.60 (-14.68%)</td><td>91.95 <b>(+378.53%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>183.72 (n/a)</td><td>178.70 (n/a)</td><td>160.10 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (-11.16%)</td><td>0.12 (-6.91%)</td><td>0.12 (-6.72%)</td><td>0.09 (-4.43%)</td><td>0.02 (-15.55%)</td><td>221.90 (+4.62%)</td><td>175.80 (+6.96%)</td><td>172.30 (+7.22%)</td><td>143.60 (+12.54%)</td><td>30.77 (-1.46%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>212.10 (n/a)</td><td>164.36 (n/a)</td><td>160.70 (n/a)</td><td>127.60 (n/a)</td><td>31.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.14 (-10.67%)</td><td>0.12 (-9.07%)</td><td>0.12 (-10.15%)</td><td>0.11 (+6.27%)</td><td>0.01 <b>(-45.57%)</b></td><td>183.40 (-5.90%)</td><td>169.30 (+8.39%)</td><td>175.00 (+11.32%)</td><td>144.90 (+11.89%)</td><td>14.89 <b>(-42.85%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>156.20 (n/a)</td><td>157.20 (n/a)</td><td>129.50 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (-9.99%)</td><td>0.12 (-2.15%)</td><td>0.12 (-2.84%)</td><td>0.11 (+8.90%)</td><td>0.01 <b>(-38.01%)</b></td><td>184.10 (-8.18%)</td><td>171.38 (+0.80%)</td><td>177.50 (+2.90%)</td><td>141.00 (+11.11%)</td><td>17.27 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>170.02 (n/a)</td><td>172.50 (n/a)</td><td>126.90 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (+5.48%)</td><td>0.11 (+6.18%)</td><td>0.11 (+1.42%)</td><td>0.10 (+14.36%)</td><td>0.01 (-9.61%)</td><td>201.30 (-12.52%)</td><td>181.54 (-6.27%)</td><td>190.70 (-1.40%)</td><td>153.30 (-5.19%)</td><td>20.26 <b>(-24.78%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>193.68 (n/a)</td><td>193.40 (n/a)</td><td>161.70 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.15 (+8.77%)</td><td>0.11 (-3.50%)</td><td>0.11 (+3.55%)</td><td>0.06 <b>(-33.90%)</b></td><td>0.03 <b>(+90.92%)</b></td><td>336.60 <b>(+51.28%)</b></td><td>210.54 (+10.64%)</td><td>189.00 (-3.47%)</td><td>139.70 (-8.03%)</td><td>74.28 <b>(+186.16%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>190.30 (n/a)</td><td>195.80 (n/a)</td><td>151.90 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-15.33%)</td><td>0.10 (-14.48%)</td><td>0.09 (-17.81%)</td><td>0.08 (-9.63%)</td><td>0.01 <b>(-20.54%)</b></td><td>245.90 (+10.67%)</td><td>215.30 (+16.64%)</td><td>217.90 <b>(+21.66%)</b></td><td>183.60 (+18.07%)</td><td>25.50 (+2.68%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>184.58 (n/a)</td><td>179.10 (n/a)</td><td>155.50 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (-1.77%)</td><td>0.15 (-3.46%)</td><td>0.15 (-9.29%)</td><td>0.13 (+5.39%)</td><td>0.02 <b>(-21.27%)</b></td><td>196.30 (-5.12%)</td><td>169.00 (+2.75%)</td><td>168.00 (+10.24%)</td><td>140.80 (+1.81%)</td><td>19.81 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>164.48 (n/a)</td><td>152.40 (n/a)</td><td>138.30 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.18 (-12.52%)</td><td>0.16 (+6.74%)</td><td>0.16 (+18.41%)</td><td>0.13 <b>(+90.12%)</b></td><td>0.02 <b>(-67.85%)</b></td><td>189.20 <b>(-47.40%)</b></td><td>158.72 (-18.71%)</td><td>150.50 (-15.54%)</td><td>140.30 (+14.25%)</td><td>19.33 <b>(-80.09%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>359.70 (n/a)</td><td>195.24 (n/a)</td><td>178.20 (n/a)</td><td>122.80 (n/a)</td><td>97.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.19 (+14.84%)</td><td>0.16 (+10.27%)</td><td>0.17 (+10.83%)</td><td>0.14 (+16.49%)</td><td>0.02 <b>(+31.94%)</b></td><td>175.30 (-14.15%)</td><td>152.68 (-8.99%)</td><td>144.90 (-9.78%)</td><td>132.40 (-12.95%)</td><td>20.97 (-0.95%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>167.76 (n/a)</td><td>160.60 (n/a)</td><td>152.10 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (-15.01%)</td><td>0.14 (-7.32%)</td><td>0.15 (-5.89%)</td><td>0.12 (-6.86%)</td><td>0.02 <b>(-29.78%)</b></td><td>209.10 (+7.40%)</td><td>172.74 (+6.83%)</td><td>166.10 (+6.27%)</td><td>144.60 (+17.66%)</td><td>25.50 (-11.60%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.70 (n/a)</td><td>161.70 (n/a)</td><td>156.30 (n/a)</td><td>122.90 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (+9.88%)</td><td>0.14 (+18.94%)</td><td>0.15 (+17.01%)</td><td>0.11 <b>(+56.93%)</b></td><td>0.03 <b>(-22.07%)</b></td><td>232.40 <b>(-36.28%)</b></td><td>175.22 <b>(-20.47%)</b></td><td>168.20 (-14.53%)</td><td>142.10 (-8.97%)</td><td>35.73 <b>(-57.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>364.70 (n/a)</td><td>220.32 (n/a)</td><td>196.80 (n/a)</td><td>156.10 (n/a)</td><td>83.18 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.22 <b>(+36.74%)</b></td><td>0.16 (+19.53%)</td><td>0.15 (+13.05%)</td><td>0.14 (+17.24%)</td><td>0.03 <b>(+107.36%)</b></td><td>176.10 (-14.68%)</td><td>155.74 (-14.93%)</td><td>162.60 (-11.53%)</td><td>113.00 <b>(-26.86%)</b></td><td>25.92 <b>(+28.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>206.40 (n/a)</td><td>183.08 (n/a)</td><td>183.80 (n/a)</td><td>154.50 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 <b>(-32.97%)</b></td><td>0.11 <b>(-28.29%)</b></td><td>0.11 <b>(-21.82%)</b></td><td>0.10 <b>(-21.62%)</b></td><td>0.01 <b>(-62.10%)</b></td><td>250.10 <b>(+27.54%)</b></td><td>222.18 <b>(+36.24%)</b></td><td>228.00 <b>(+27.95%)</b></td><td>187.70 <b>(+49.21%)</b></td><td>22.81 <b>(-27.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>163.08 (n/a)</td><td>178.20 (n/a)</td><td>125.80 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.17 (-6.35%)</td><td>0.13 (-15.21%)</td><td>0.12 <b>(-20.50%)</b></td><td>0.10 (-15.46%)</td><td>0.03 (-1.60%)</td><td>250.00 (+18.32%)</td><td>202.82 (+18.62%)</td><td>210.40 <b>(+25.76%)</b></td><td>144.00 (+6.75%)</td><td>40.79 <b>(+22.24%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.30 (n/a)</td><td>170.98 (n/a)</td><td>167.30 (n/a)</td><td>134.90 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-13.21%)</td><td>0.10 (-11.78%)</td><td>0.10 (-8.40%)</td><td>0.08 (-15.93%)</td><td>0.02 (-7.22%)</td><td>242.70 (+18.97%)</td><td>187.92 (+13.85%)</td><td>177.60 (+9.23%)</td><td>150.80 (+15.29%)</td><td>33.92 <b>(+30.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>165.06 (n/a)</td><td>162.60 (n/a)</td><td>130.80 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.13 (+8.77%)</td><td>0.11 (+9.62%)</td><td>0.10 (+12.61%)</td><td>0.10 (+7.74%)</td><td>0.01 (+7.13%)</td><td>191.20 (-7.14%)</td><td>174.50 (-8.78%)</td><td>177.30 (-11.17%)</td><td>144.00 (-8.10%)</td><td>18.32 (-8.66%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>191.30 (n/a)</td><td>199.60 (n/a)</td><td>156.70 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 <b>(-25.27%)</b></td><td>0.10 (-13.64%)</td><td>0.10 (-10.25%)</td><td>0.09 (-0.76%)</td><td>0.01 <b>(-65.71%)</b></td><td>211.50 (+0.76%)</td><td>185.86 (+12.47%)</td><td>185.40 (+11.42%)</td><td>169.40 <b>(+33.81%)</b></td><td>16.13 <b>(-52.86%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>165.26 (n/a)</td><td>166.40 (n/a)</td><td>126.60 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 <b>(-22.55%)</b></td><td>0.10 <b>(-20.95%)</b></td><td>0.10 <b>(-25.22%)</b></td><td>0.08 (-7.85%)</td><td>0.01 <b>(-50.69%)</b></td><td>231.00 (+8.50%)</td><td>195.26 <b>(+23.69%)</b></td><td>188.60 <b>(+33.76%)</b></td><td>169.70 <b>(+29.05%)</b></td><td>24.65 <b>(-29.49%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>157.86 (n/a)</td><td>141.00 (n/a)</td><td>131.50 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-19.74%)</td><td>0.10 (-1.80%)</td><td>0.11 (+5.70%)</td><td>0.09 (+8.89%)</td><td>0.01 <b>(-55.38%)</b></td><td>212.30 (-8.17%)</td><td>178.42 (-2.94%)</td><td>174.20 (-5.43%)</td><td>150.60 <b>(+24.57%)</b></td><td>23.93 <b>(-50.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>231.20 (n/a)</td><td>183.82 (n/a)</td><td>184.20 (n/a)</td><td>120.90 (n/a)</td><td>48.50 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.12 (-11.04%)</td><td>0.10 (-9.74%)</td><td>0.11 (+2.77%)</td><td>0.09 (-17.13%)</td><td>0.02 (-11.90%)</td><td>216.40 <b>(+20.69%)</b></td><td>179.44 (+10.86%)</td><td>170.20 (-2.69%)</td><td>147.90 (+12.39%)</td><td>26.53 (+18.47%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>179.30 (n/a)</td><td>161.86 (n/a)</td><td>174.90 (n/a)</td><td>131.60 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-2.76%)</td><td>0.09 (+0.85%)</td><td>0.09 (+1.17%)</td><td>0.08 (+1.78%)</td><td>0.01 (-15.34%)</td><td>225.70 (-1.78%)</td><td>201.82 (-1.30%)</td><td>205.20 (-1.16%)</td><td>164.70 (+2.87%)</td><td>23.73 (-14.89%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>204.48 (n/a)</td><td>207.60 (n/a)</td><td>160.10 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.10 <b>(-23.65%)</b></td><td>0.09 (-19.79%)</td><td>0.08 (-18.06%)</td><td>0.08 (-11.11%)</td><td>0.01 <b>(-56.14%)</b></td><td>232.10 (+12.45%)</td><td>216.38 <b>(+23.27%)</b></td><td>219.80 <b>(+22.04%)</b></td><td>190.50 <b>(+31.02%)</b></td><td>15.52 <b>(-36.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.40 (n/a)</td><td>175.54 (n/a)</td><td>180.10 (n/a)</td><td>145.40 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.68 (-10.79%)</td><td>0.56 (-2.86%)</td><td>0.55 (-3.11%)</td><td>0.47 (-0.86%)</td><td>0.09 <b>(-22.43%)</b></td><td>207.30 (+0.88%)</td><td>177.78 (+2.20%)</td><td>178.70 (+3.24%)</td><td>144.50 (+12.10%)</td><td>26.05 (-9.59%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.76 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.11 (n/a)</td><td>205.50 (n/a)</td><td>173.96 (n/a)</td><td>173.10 (n/a)</td><td>128.90 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.80 (+19.27%)</td><td>0.61 (+4.28%)</td><td>0.67 (+18.75%)</td><td>0.41 <b>(-22.02%)</b></td><td>0.17 <b>(+214.45%)</b></td><td>240.10 <b>(+28.26%)</b></td><td>173.84 (+2.10%)</td><td>146.50 (-15.80%)</td><td>123.00 (-16.16%)</td><td>52.43 <b>(+254.72%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.05 (n/a)</td><td>187.20 (n/a)</td><td>170.26 (n/a)</td><td>174.00 (n/a)</td><td>146.70 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.71 (-7.66%)</td><td>0.60 (+5.93%)</td><td>0.56 (-2.47%)</td><td>0.54 <b>(+37.22%)</b></td><td>0.07 <b>(-48.43%)</b></td><td>180.50 <b>(-27.10%)</b></td><td>165.84 (-9.09%)</td><td>177.10 (+2.55%)</td><td>138.50 (+8.29%)</td><td>18.39 <b>(-59.07%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.77 (n/a)</td><td>0.57 (n/a)</td><td>0.57 (n/a)</td><td>0.40 (n/a)</td><td>0.14 (n/a)</td><td>247.60 (n/a)</td><td>182.42 (n/a)</td><td>172.70 (n/a)</td><td>127.90 (n/a)</td><td>44.92 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.57 (-13.98%)</td><td>0.50 (-8.06%)</td><td>0.48 (-10.15%)</td><td>0.47 (+1.80%)</td><td>0.04 <b>(-54.12%)</b></td><td>207.00 (-1.76%)</td><td>196.64 (+7.28%)</td><td>203.50 (+11.26%)</td><td>173.30 (+16.23%)</td><td>13.82 <b>(-48.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.66 (n/a)</td><td>0.55 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>210.70 (n/a)</td><td>183.30 (n/a)</td><td>182.90 (n/a)</td><td>149.10 (n/a)</td><td>27.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.56 (+0.95%)</td><td>0.44 (-1.16%)</td><td>0.44 (+5.29%)</td><td>0.31 <b>(-22.92%)</b></td><td>0.10 <b>(+62.99%)</b></td><td>237.00 <b>(+29.79%)</b></td><td>174.54 (+4.43%)</td><td>166.90 (-5.06%)</td><td>131.90 (-0.90%)</td><td>42.58 <b>(+110.82%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.55 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>182.60 (n/a)</td><td>167.14 (n/a)</td><td>175.80 (n/a)</td><td>133.10 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.53 (-4.29%)</td><td>0.43 (-4.93%)</td><td>0.50 (+16.20%)</td><td>0.30 <b>(-28.73%)</b></td><td>0.11 <b>(+103.35%)</b></td><td>246.00 <b>(+40.33%)</b></td><td>179.42 (+10.17%)</td><td>146.30 (-13.94%)</td><td>140.20 (+4.47%)</td><td>49.37 <b>(+198.48%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.05 (n/a)</td><td>175.30 (n/a)</td><td>162.86 (n/a)</td><td>170.00 (n/a)</td><td>134.20 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.44 <b>(-24.69%)</b></td><td>0.41 (-9.51%)</td><td>0.44 (+7.42%)</td><td>0.33 (+1.94%)</td><td>0.05 <b>(-58.27%)</b></td><td>225.90 (-1.91%)</td><td>180.30 (+6.08%)</td><td>168.30 (-6.91%)</td><td>167.10 <b>(+32.83%)</b></td><td>25.55 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.59 (n/a)</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>230.30 (n/a)</td><td>169.96 (n/a)</td><td>180.80 (n/a)</td><td>125.80 (n/a)</td><td>44.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 <b>(-20.27%)</b></td><td>0.32 (-12.11%)</td><td>0.34 (-4.83%)</td><td>0.24 <b>(-25.89%)</b></td><td>0.05 (-9.81%)</td><td>307.50 <b>(+34.93%)</b></td><td>232.86 (+14.63%)</td><td>218.60 (+5.05%)</td><td>197.40 <b>(+25.41%)</b></td><td>43.64 <b>(+62.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.47 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>227.90 (n/a)</td><td>203.14 (n/a)</td><td>208.10 (n/a)</td><td>157.40 (n/a)</td><td>26.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.26 (-7.07%)</td><td>0.20 (-12.45%)</td><td>0.21 (-18.51%)</td><td>0.12 <b>(-28.03%)</b></td><td>0.05 (-0.62%)</td><td>298.70 <b>(+38.93%)</b></td><td>195.70 (+16.53%)</td><td>178.90 <b>(+22.70%)</b></td><td>140.60 (+7.66%)</td><td>61.05 <b>(+51.02%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>215.00 (n/a)</td><td>167.94 (n/a)</td><td>145.80 (n/a)</td><td>130.60 (n/a)</td><td>40.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (+1.72%)</td><td>0.22 (+16.96%)</td><td>0.24 (+10.89%)</td><td>0.19 <b>(+72.55%)</b></td><td>0.03 <b>(-46.44%)</b></td><td>194.10 <b>(-42.06%)</b></td><td>166.98 <b>(-21.06%)</b></td><td>156.20 (-9.82%)</td><td>145.40 (-1.69%)</td><td>24.92 <b>(-68.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>335.00 (n/a)</td><td>211.52 (n/a)</td><td>173.20 (n/a)</td><td>147.90 (n/a)</td><td>79.55 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (+16.68%)</td><td>0.24 (+13.98%)</td><td>0.22 (+4.80%)</td><td>0.17 (+8.75%)</td><td>0.05 (+17.62%)</td><td>214.00 (-8.04%)</td><td>161.36 (-12.07%)</td><td>167.20 (-4.57%)</td><td>121.20 (-14.29%)</td><td>36.69 (-9.31%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>232.70 (n/a)</td><td>183.50 (n/a)</td><td>175.20 (n/a)</td><td>141.40 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.26 (-1.56%)</td><td>0.23 (+9.29%)</td><td>0.25 (+12.90%)</td><td>0.18 (+12.87%)</td><td>0.03 (-18.33%)</td><td>208.10 (-11.41%)</td><td>160.48 (-9.63%)</td><td>147.70 (-11.45%)</td><td>141.10 (+1.58%)</td><td>27.43 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>234.90 (n/a)</td><td>177.58 (n/a)</td><td>166.80 (n/a)</td><td>138.90 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.32 <b>(+42.61%)</b></td><td>0.22 (+15.49%)</td><td>0.20 (+1.79%)</td><td>0.17 (+4.02%)</td><td>0.06 <b>(+122.04%)</b></td><td>220.10 (-3.84%)</td><td>175.58 (-10.64%)</td><td>183.10 (-1.77%)</td><td>114.50 <b>(-29.88%)</b></td><td>38.44 <b>(+39.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>228.90 (n/a)</td><td>196.48 (n/a)</td><td>186.40 (n/a)</td><td>163.30 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (-18.16%)</td><td>0.20 (-1.22%)</td><td>0.21 (+11.27%)</td><td>0.17 (-2.15%)</td><td>0.04 <b>(-33.36%)</b></td><td>222.90 (+2.20%)</td><td>184.82 (-0.38%)</td><td>173.60 (-10.14%)</td><td>150.40 <b>(+22.28%)</b></td><td>32.54 (-10.75%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>218.10 (n/a)</td><td>185.52 (n/a)</td><td>193.20 (n/a)</td><td>123.00 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.23 (-16.40%)</td><td>0.19 (+0.27%)</td><td>0.20 (+11.68%)</td><td>0.15 (+8.86%)</td><td>0.03 <b>(-46.38%)</b></td><td>244.60 (-8.15%)</td><td>196.36 (-3.92%)</td><td>187.90 (-10.44%)</td><td>160.00 (+19.67%)</td><td>30.93 <b>(-39.23%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>266.30 (n/a)</td><td>204.38 (n/a)</td><td>209.80 (n/a)</td><td>133.70 (n/a)</td><td>50.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (+10.95%)</td><td>0.21 (+13.46%)</td><td>0.21 (+9.44%)</td><td>0.15 <b>(+21.14%)</b></td><td>0.04 (-2.31%)</td><td>240.60 (-17.46%)</td><td>182.30 (-12.84%)</td><td>175.80 (-8.63%)</td><td>147.00 (-9.87%)</td><td>35.50 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>291.50 (n/a)</td><td>209.16 (n/a)</td><td>192.40 (n/a)</td><td>163.10 (n/a)</td><td>49.34 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.28 (+16.16%)</td><td>0.23 <b>(+29.00%)</b></td><td>0.24 <b>(+33.49%)</b></td><td>0.19 <b>(+45.33%)</b></td><td>0.03 (-19.08%)</td><td>216.10 <b>(-31.18%)</b></td><td>177.06 <b>(-24.24%)</b></td><td>171.90 <b>(-25.10%)</b></td><td>146.60 (-13.87%)</td><td>25.12 <b>(-51.85%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>314.00 (n/a)</td><td>233.72 (n/a)</td><td>229.50 (n/a)</td><td>170.20 (n/a)</td><td>52.17 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 <b>(-25.71%)</b></td><td>0.21 (-18.85%)</td><td>0.22 (-16.12%)</td><td>0.19 (-5.17%)</td><td>0.02 <b>(-52.39%)</b></td><td>217.40 (+5.48%)</td><td>193.16 <b>(+21.30%)</b></td><td>183.20 (+19.19%)</td><td>174.10 <b>(+34.65%)</b></td><td>18.97 <b>(-33.68%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>206.10 (n/a)</td><td>159.24 (n/a)</td><td>153.70 (n/a)</td><td>129.30 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.33 (+8.50%)</td><td>0.26 (+12.95%)</td><td>0.25 <b>(+20.62%)</b></td><td>0.20 (-0.20%)</td><td>0.05 (+10.66%)</td><td>209.70 (+0.19%)</td><td>162.16 (-11.22%)</td><td>167.10 (-17.07%)</td><td>122.30 (-7.84%)</td><td>33.85 (-0.89%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>209.30 (n/a)</td><td>182.66 (n/a)</td><td>201.50 (n/a)</td><td>132.70 (n/a)</td><td>34.15 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (+2.51%)</td><td>0.21 (-4.28%)</td><td>0.19 (-14.72%)</td><td>0.17 (+4.90%)</td><td>0.05 (+5.37%)</td><td>247.10 (-4.67%)</td><td>200.60 (+4.61%)</td><td>217.10 (+17.29%)</td><td>137.10 (-2.49%)</td><td>45.25 (-2.55%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>259.20 (n/a)</td><td>191.76 (n/a)</td><td>185.10 (n/a)</td><td>140.60 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 <b>(-20.39%)</b></td><td>0.22 (-9.43%)</td><td>0.23 (+0.33%)</td><td>0.19 (+2.68%)</td><td>0.02 <b>(-63.62%)</b></td><td>214.70 (-2.63%)</td><td>183.66 (+6.69%)</td><td>178.60 (-0.33%)</td><td>166.00 <b>(+25.57%)</b></td><td>18.34 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>220.50 (n/a)</td><td>172.14 (n/a)</td><td>179.20 (n/a)</td><td>132.20 (n/a)</td><td>38.57 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (-14.21%)</td><td>0.22 (-7.17%)</td><td>0.23 (+0.36%)</td><td>0.20 (-2.79%)</td><td>0.02 <b>(-46.86%)</b></td><td>203.40 (+2.88%)</td><td>185.42 (+6.78%)</td><td>179.80 (-0.39%)</td><td>171.80 (+16.55%)</td><td>14.13 <b>(-35.57%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>197.70 (n/a)</td><td>173.64 (n/a)</td><td>180.50 (n/a)</td><td>147.40 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (+16.43%)</td><td>0.23 (+9.02%)</td><td>0.22 (+5.97%)</td><td>0.18 (+5.40%)</td><td>0.05 (+16.30%)</td><td>224.40 (-5.12%)</td><td>183.74 (-8.17%)</td><td>189.90 (-5.66%)</td><td>134.90 (-14.08%)</td><td>32.71 (-9.67%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>236.50 (n/a)</td><td>200.08 (n/a)</td><td>201.30 (n/a)</td><td>157.00 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.30 (-15.77%)</td><td>0.24 (-5.78%)</td><td>0.24 (-6.17%)</td><td>0.19 <b>(+49.14%)</b></td><td>0.04 <b>(-52.92%)</b></td><td>219.10 <b>(-32.94%)</b></td><td>174.74 (-4.56%)</td><td>171.00 (+6.54%)</td><td>135.10 (+18.72%)</td><td>30.03 <b>(-64.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>326.70 (n/a)</td><td>183.08 (n/a)</td><td>160.50 (n/a)</td><td>113.80 (n/a)</td><td>84.26 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (-8.80%)</td><td>0.18 <b>(-20.29%)</b></td><td>0.18 <b>(-26.09%)</b></td><td>0.10 <b>(-43.91%)</b></td><td>0.06 <b>(+58.53%)</b></td><td>356.60 <b>(+78.30%)</b></td><td>209.60 <b>(+36.41%)</b></td><td>197.40 <b>(+35.30%)</b></td><td>142.30 (+9.63%)</td><td>86.74 <b>(+208.88%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>200.00 (n/a)</td><td>153.66 (n/a)</td><td>145.90 (n/a)</td><td>129.80 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (+0.66%)</td><td>0.19 (-3.28%)</td><td>0.18 (-8.59%)</td><td>0.16 (-8.67%)</td><td>0.03 <b>(+25.89%)</b></td><td>220.50 (+9.48%)</td><td>185.36 (+4.44%)</td><td>196.60 (+9.40%)</td><td>140.60 (-0.64%)</td><td>30.48 <b>(+38.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>177.48 (n/a)</td><td>179.70 (n/a)</td><td>141.50 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (-18.95%)</td><td>0.20 (-8.37%)</td><td>0.21 (-5.04%)</td><td>0.16 (-2.30%)</td><td>0.03 <b>(-39.18%)</b></td><td>220.30 (+2.37%)</td><td>175.28 (+7.00%)</td><td>166.40 (+5.32%)</td><td>146.10 <b>(+23.40%)</b></td><td>28.10 <b>(-21.51%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>215.20 (n/a)</td><td>163.82 (n/a)</td><td>158.00 (n/a)</td><td>118.40 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.20 <b>(-21.08%)</b></td><td>0.17 (-19.78%)</td><td>0.16 (-19.02%)</td><td>0.14 (-9.75%)</td><td>0.02 <b>(-40.86%)</b></td><td>242.90 (+10.81%)</td><td>212.30 <b>(+23.23%)</b></td><td>213.00 <b>(+23.48%)</b></td><td>176.20 <b>(+26.76%)</b></td><td>23.89 (-19.66%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>219.20 (n/a)</td><td>172.28 (n/a)</td><td>172.50 (n/a)</td><td>139.00 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 <b>(-25.64%)</b></td><td>0.18 <b>(-21.81%)</b></td><td>0.19 (-18.31%)</td><td>0.14 (-11.38%)</td><td>0.03 <b>(-44.56%)</b></td><td>245.90 (+12.85%)</td><td>194.92 <b>(+25.27%)</b></td><td>185.70 <b>(+22.41%)</b></td><td>165.20 <b>(+34.53%)</b></td><td>31.43 (-16.05%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>217.90 (n/a)</td><td>155.60 (n/a)</td><td>151.70 (n/a)</td><td>122.80 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 <b>(-29.36%)</b></td><td>0.19 (-1.84%)</td><td>0.19 (+17.44%)</td><td>0.17 (+11.98%)</td><td>0.02 <b>(-72.92%)</b></td><td>205.30 (-10.70%)</td><td>186.40 (-3.76%)</td><td>186.20 (-14.86%)</td><td>169.20 <b>(+41.59%)</b></td><td>16.07 <b>(-66.44%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>229.90 (n/a)</td><td>193.68 (n/a)</td><td>218.70 (n/a)</td><td>119.50 (n/a)</td><td>47.87 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 <b>(-28.42%)</b></td><td>0.16 <b>(-31.33%)</b></td><td>0.15 <b>(-30.65%)</b></td><td>0.12 <b>(-36.78%)</b></td><td>0.03 (-16.97%)</td><td>282.30 <b>(+58.15%)</b></td><td>226.02 <b>(+47.00%)</b></td><td>231.10 <b>(+44.17%)</b></td><td>167.40 <b>(+39.73%)</b></td><td>41.11 <b>(+82.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>178.50 (n/a)</td><td>153.76 (n/a)</td><td>160.30 (n/a)</td><td>119.80 (n/a)</td><td>22.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.25 (+4.61%)</td><td>0.19 (-2.46%)</td><td>0.20 (-10.41%)</td><td>0.13 <b>(+27.57%)</b></td><td>0.04 <b>(-24.13%)</b></td><td>264.20 <b>(-21.63%)</b></td><td>186.86 (-3.07%)</td><td>178.30 (+11.65%)</td><td>137.50 (-4.38%)</td><td>46.63 <b>(-42.96%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>337.10 (n/a)</td><td>192.78 (n/a)</td><td>159.70 (n/a)</td><td>143.80 (n/a)</td><td>81.75 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.02 (+13.26%)</td><td>0.80 (-3.04%)</td><td>0.79 (-7.47%)</td><td>0.63 (-9.45%)</td><td>0.14 <b>(+70.67%)</b></td><td>208.60 (+10.43%)</td><td>169.00 (+4.77%)</td><td>165.20 (+8.12%)</td><td>128.70 (-11.67%)</td><td>29.04 <b>(+63.73%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.90 (n/a)</td><td>0.82 (n/a)</td><td>0.86 (n/a)</td><td>0.69 (n/a)</td><td>0.08 (n/a)</td><td>188.90 (n/a)</td><td>161.30 (n/a)</td><td>152.80 (n/a)</td><td>145.70 (n/a)</td><td>17.74 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.77 <b>(-21.92%)</b></td><td>0.65 <b>(-22.93%)</b></td><td>0.63 <b>(-27.81%)</b></td><td>0.55 (-11.48%)</td><td>0.08 <b>(-41.08%)</b></td><td>239.70 (+12.96%)</td><td>205.50 <b>(+28.09%)</b></td><td>209.20 <b>(+38.54%)</b></td><td>170.40 <b>(+28.02%)</b></td><td>24.94 (-18.32%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.99 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.62 (n/a)</td><td>0.14 (n/a)</td><td>212.20 (n/a)</td><td>160.44 (n/a)</td><td>151.00 (n/a)</td><td>133.10 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.86 (-10.78%)</td><td>0.68 (-18.69%)</td><td>0.72 (-11.45%)</td><td>0.54 <b>(-23.89%)</b></td><td>0.13 (+18.98%)</td><td>242.30 <b>(+31.40%)</b></td><td>198.38 <b>(+25.08%)</b></td><td>182.60 (+12.93%)</td><td>152.20 (+12.08%)</td><td>39.12 <b>(+85.00%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.97 (n/a)</td><td>0.84 (n/a)</td><td>0.81 (n/a)</td><td>0.71 (n/a)</td><td>0.11 (n/a)</td><td>184.40 (n/a)</td><td>158.60 (n/a)</td><td>161.70 (n/a)</td><td>135.80 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.00 (-2.22%)</td><td>0.00 (+1.41%)</td><td>0.00 (+0.00%)</td><td>0.00 (+7.50%)</td><td>0.00 <b>(-75.38%)</b></td><td>957.84 (-6.50%)</td><td>953.73 (-0.94%)</td><td>956.58 (+0.27%)</td><td>940.95 (+2.44%)</td><td>7.17 <b>(-81.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1024.39 (n/a)</td><td>962.74 (n/a)</td><td>954.02 (n/a)</td><td>918.52 (n/a)</td><td>39.72 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.01 (-2.35%)</td><td>0.01 (-1.23%)</td><td>0.01 (+0.00%)</td><td>0.01 (-2.63%)</td><td>0.00 (+1.93%)</td><td>1100.64 (+2.28%)</td><td>1017.29 (+0.96%)</td><td>1001.21 (+0.26%)</td><td>983.56 (+2.46%)</td><td>47.44 (+5.96%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1076.09 (n/a)</td><td>1007.62 (n/a)</td><td>998.63 (n/a)</td><td>959.98 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.94 (-1.79%)</td><td>0.93 (-0.89%)</td><td>0.94 (-0.64%)</td><td>0.91 (-0.04%)</td><td>0.01 <b>(-28.72%)</b></td><td>2295.97 (+0.05%)</td><td>2253.66 (+0.89%)</td><td>2237.45 (+0.64%)</td><td>2232.42 (+1.82%)</td><td>27.85 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.91 (n/a)</td><td>0.02 (n/a)</td><td>2294.87 (n/a)</td><td>2233.82 (n/a)</td><td>2223.22 (n/a)</td><td>2192.48 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.01 (n/a)</td><td>1199.06 (n/a)</td><td>1173.15 (n/a)</td><td>1169.90 (n/a)</td><td>1162.41 (n/a)</td><td>15.05 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1442.89 (n/a)</td><td>1422.72 (n/a)</td><td>1431.10 (n/a)</td><td>1398.44 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.00 (n/a)</td><td>1490.13 (n/a)</td><td>1473.01 (n/a)</td><td>1471.24 (n/a)</td><td>1461.47 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.42 (-13.31%)</td><td>4.83 (-3.40%)</td><td>4.78 (+5.98%)</td><td>4.32 (+8.26%)</td><td>0.53 <b>(-49.17%)</b></td><td>242.70 (-7.65%)</td><td>218.98 (+1.12%)</td><td>219.50 (-5.63%)</td><td>193.60 (+15.38%)</td><td>23.63 <b>(-44.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.25 (n/a)</td><td>5.00 (n/a)</td><td>4.51 (n/a)</td><td>3.99 (n/a)</td><td>1.03 (n/a)</td><td>262.80 (n/a)</td><td>216.56 (n/a)</td><td>232.60 (n/a)</td><td>167.80 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.40 (-6.89%)</td><td>4.82 (+2.96%)</td><td>4.88 (+11.06%)</td><td>4.06 (+2.36%)</td><td>0.54 <b>(-33.48%)</b></td><td>258.10 (-2.31%)</td><td>219.82 (-4.04%)</td><td>214.90 (-9.93%)</td><td>194.30 (+7.41%)</td><td>25.69 <b>(-31.22%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.80 (n/a)</td><td>4.68 (n/a)</td><td>4.39 (n/a)</td><td>3.97 (n/a)</td><td>0.81 (n/a)</td><td>264.20 (n/a)</td><td>229.08 (n/a)</td><td>238.60 (n/a)</td><td>180.90 (n/a)</td><td>37.35 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.42 (-3.71%)</td><td>4.54 (-4.67%)</td><td>4.85 (+6.86%)</td><td>3.04 <b>(-31.42%)</b></td><td>0.91 <b>(+84.26%)</b></td><td>344.70 <b>(+45.81%)</b></td><td>240.34 (+8.41%)</td><td>216.40 (-6.44%)</td><td>193.50 (+3.86%)</td><td>60.35 <b>(+193.87%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.63 (n/a)</td><td>4.77 (n/a)</td><td>4.53 (n/a)</td><td>4.43 (n/a)</td><td>0.49 (n/a)</td><td>236.40 (n/a)</td><td>221.70 (n/a)</td><td>231.30 (n/a)</td><td>186.30 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.07 (-16.32%)</td><td>4.67 (+3.59%)</td><td>4.59 (-1.41%)</td><td>4.40 <b>(+49.25%)</b></td><td>0.26 <b>(-80.70%)</b></td><td>238.40 <b>(-33.01%)</b></td><td>225.06 (-10.31%)</td><td>228.70 (+1.46%)</td><td>206.60 (+19.49%)</td><td>11.99 <b>(-84.75%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.06 (n/a)</td><td>4.51 (n/a)</td><td>4.65 (n/a)</td><td>2.95 (n/a)</td><td>1.33 (n/a)</td><td>355.90 (n/a)</td><td>250.92 (n/a)</td><td>225.40 (n/a)</td><td>172.90 (n/a)</td><td>78.65 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.24 (+0.03%)</td><td>7.88 (-1.02%)</td><td>7.98 (-4.95%)</td><td>6.30 (+10.47%)</td><td>1.09 <b>(-23.10%)</b></td><td>332.90 (-9.46%)</td><td>270.42 (-0.35%)</td><td>262.70 (+5.21%)</td><td>227.00 (+0.00%)</td><td>39.84 <b>(-30.42%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.24 (n/a)</td><td>7.96 (n/a)</td><td>8.40 (n/a)</td><td>5.70 (n/a)</td><td>1.42 (n/a)</td><td>367.70 (n/a)</td><td>271.38 (n/a)</td><td>249.70 (n/a)</td><td>227.00 (n/a)</td><td>57.25 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>7.62 <b>(-23.68%)</b></td><td>7.08 (-15.84%)</td><td>7.15 (-9.90%)</td><td>6.38 (-7.45%)</td><td>0.46 <b>(-66.55%)</b></td><td>328.60 (+8.06%)</td><td>297.22 (+16.74%)</td><td>293.30 (+10.97%)</td><td>275.30 <b>(+31.03%)</b></td><td>20.01 <b>(-51.07%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.98 (n/a)</td><td>8.41 (n/a)</td><td>7.94 (n/a)</td><td>6.90 (n/a)</td><td>1.38 (n/a)</td><td>304.10 (n/a)</td><td>254.60 (n/a)</td><td>264.30 (n/a)</td><td>210.10 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.55 (-8.05%)</td><td>7.64 (-6.15%)</td><td>7.48 (-9.65%)</td><td>7.08 (-0.74%)</td><td>0.55 <b>(-37.97%)</b></td><td>296.40 (+0.75%)</td><td>275.50 (+5.97%)</td><td>280.30 (+10.70%)</td><td>245.30 (+8.73%)</td><td>18.71 <b>(-33.55%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.30 (n/a)</td><td>8.14 (n/a)</td><td>8.28 (n/a)</td><td>7.13 (n/a)</td><td>0.88 (n/a)</td><td>294.20 (n/a)</td><td>259.98 (n/a)</td><td>253.20 (n/a)</td><td>225.60 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.60 (-10.35%)</td><td>7.83 (-6.48%)</td><td>8.60 (+12.60%)</td><td>4.97 <b>(-33.57%)</b></td><td>1.80 <b>(+32.14%)</b></td><td>422.20 <b>(+50.52%)</b></td><td>282.88 (+10.81%)</td><td>243.80 (-11.22%)</td><td>218.50 (+11.54%)</td><td>81.96 <b>(+130.05%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>10.70 (n/a)</td><td>8.37 (n/a)</td><td>7.64 (n/a)</td><td>7.48 (n/a)</td><td>1.36 (n/a)</td><td>280.50 (n/a)</td><td>255.28 (n/a)</td><td>274.60 (n/a)</td><td>195.90 (n/a)</td><td>35.63 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>9.35 (-8.35%)</td><td>8.49 (+0.17%)</td><td>8.22 (+0.90%)</td><td>7.80 (+1.75%)</td><td>0.77 <b>(-22.97%)</b></td><td>268.80 (-1.72%)</td><td>248.48 (-0.51%)</td><td>255.10 (-0.89%)</td><td>224.20 (+9.10%)</td><td>22.05 (-15.73%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>10.20 (n/a)</td><td>8.48 (n/a)</td><td>8.15 (n/a)</td><td>7.67 (n/a)</td><td>1.00 (n/a)</td><td>273.50 (n/a)</td><td>249.76 (n/a)</td><td>257.40 (n/a)</td><td>205.50 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>10.19 (+6.90%)</td><td>8.05 (-1.33%)</td><td>7.59 (-11.37%)</td><td>6.63 (+2.79%)</td><td>1.33 (-1.33%)</td><td>316.20 (-2.71%)</td><td>265.88 (+1.03%)</td><td>276.40 (+12.82%)</td><td>205.70 (-6.46%)</td><td>40.51 (-12.06%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.54 (n/a)</td><td>8.16 (n/a)</td><td>8.56 (n/a)</td><td>6.45 (n/a)</td><td>1.35 (n/a)</td><td>325.00 (n/a)</td><td>263.18 (n/a)</td><td>245.00 (n/a)</td><td>219.90 (n/a)</td><td>46.07 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.32 (+4.64%)</td><td>11.35 (+3.51%)</td><td>11.66 (+7.29%)</td><td>9.78 (-5.73%)</td><td>1.07 <b>(+110.00%)</b></td><td>428.80 (+6.06%)</td><td>372.42 (-2.82%)</td><td>359.80 (-6.79%)</td><td>340.40 (-4.41%)</td><td>37.09 <b>(+112.92%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.78 (n/a)</td><td>10.96 (n/a)</td><td>10.87 (n/a)</td><td>10.38 (n/a)</td><td>0.51 (n/a)</td><td>404.30 (n/a)</td><td>383.22 (n/a)</td><td>386.00 (n/a)</td><td>356.10 (n/a)</td><td>17.42 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.45 (-2.76%)</td><td>11.17 (-4.02%)</td><td>11.18 (-1.31%)</td><td>10.22 (-4.60%)</td><td>0.83 (-16.32%)</td><td>410.40 (+4.83%)</td><td>377.24 (+4.04%)</td><td>375.20 (+1.35%)</td><td>336.90 (+2.84%)</td><td>27.22 (-10.35%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.80 (n/a)</td><td>11.63 (n/a)</td><td>11.33 (n/a)</td><td>10.71 (n/a)</td><td>0.99 (n/a)</td><td>391.50 (n/a)</td><td>362.58 (n/a)</td><td>370.20 (n/a)</td><td>327.60 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>11.94 (+0.48%)</td><td>11.18 (+4.22%)</td><td>11.24 (+3.33%)</td><td>10.68 (+9.82%)</td><td>0.52 <b>(-40.08%)</b></td><td>392.80 (-8.93%)</td><td>375.70 (-4.38%)</td><td>373.10 (-3.24%)</td><td>351.40 (-0.48%)</td><td>17.17 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.88 (n/a)</td><td>10.73 (n/a)</td><td>10.88 (n/a)</td><td>9.72 (n/a)</td><td>0.87 (n/a)</td><td>431.30 (n/a)</td><td>392.92 (n/a)</td><td>385.60 (n/a)</td><td>353.10 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.67 (-8.97%)</td><td>11.57 (-9.49%)</td><td>12.14 (-4.78%)</td><td>9.82 (-12.75%)</td><td>1.22 (+11.91%)</td><td>427.30 (+14.62%)</td><td>365.98 (+10.86%)</td><td>345.60 (+5.01%)</td><td>330.90 (+9.82%)</td><td>40.98 <b>(+41.36%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.92 (n/a)</td><td>12.78 (n/a)</td><td>12.75 (n/a)</td><td>11.25 (n/a)</td><td>1.09 (n/a)</td><td>372.80 (n/a)</td><td>330.12 (n/a)</td><td>329.10 (n/a)</td><td>301.30 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.84 (+0.91%)</td><td>12.04 (-3.29%)</td><td>12.16 (-2.26%)</td><td>10.41 (-13.65%)</td><td>0.99 <b>(+274.45%)</b></td><td>402.80 (+15.81%)</td><td>350.42 (+3.98%)</td><td>345.00 (+2.31%)</td><td>326.70 (-0.88%)</td><td>31.07 <b>(+331.67%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.73 (n/a)</td><td>12.45 (n/a)</td><td>12.44 (n/a)</td><td>12.06 (n/a)</td><td>0.26 (n/a)</td><td>347.80 (n/a)</td><td>337.02 (n/a)</td><td>337.20 (n/a)</td><td>329.60 (n/a)</td><td>7.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>13.97 (+8.44%)</td><td>12.16 (+3.17%)</td><td>12.43 (+5.80%)</td><td>10.11 (-5.85%)</td><td>1.46 <b>(+70.49%)</b></td><td>414.80 (+6.22%)</td><td>349.08 (-2.32%)</td><td>337.50 (-5.49%)</td><td>300.20 (-7.77%)</td><td>43.60 <b>(+68.61%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.89 (n/a)</td><td>11.79 (n/a)</td><td>11.75 (n/a)</td><td>10.74 (n/a)</td><td>0.85 (n/a)</td><td>390.50 (n/a)</td><td>357.36 (n/a)</td><td>357.10 (n/a)</td><td>325.50 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.46 (-8.46%)</td><td>11.77 (-3.54%)</td><td>11.99 (+0.12%)</td><td>10.57 (+0.12%)</td><td>0.78 <b>(-41.60%)</b></td><td>396.80 (-0.10%)</td><td>357.66 (+3.05%)</td><td>349.80 (-0.11%)</td><td>336.80 (+9.24%)</td><td>24.92 <b>(-35.12%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.61 (n/a)</td><td>12.20 (n/a)</td><td>11.98 (n/a)</td><td>10.56 (n/a)</td><td>1.34 (n/a)</td><td>397.20 (n/a)</td><td>347.08 (n/a)</td><td>350.20 (n/a)</td><td>308.30 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>12.72 (-2.17%)</td><td>11.06 (-2.99%)</td><td>10.83 (-14.61%)</td><td>9.86 (+8.34%)</td><td>1.15 <b>(-43.07%)</b></td><td>425.30 (-7.68%)</td><td>382.44 (+1.16%)</td><td>387.40 (+17.11%)</td><td>329.60 (+2.20%)</td><td>38.51 <b>(-46.29%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.01 (n/a)</td><td>11.40 (n/a)</td><td>12.68 (n/a)</td><td>9.10 (n/a)</td><td>2.02 (n/a)</td><td>460.70 (n/a)</td><td>378.06 (n/a)</td><td>330.80 (n/a)</td><td>322.50 (n/a)</td><td>71.69 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.05 (-12.11%)</td><td>2.57 (-9.72%)</td><td>2.59 (-3.08%)</td><td>2.04 <b>(-20.21%)</b></td><td>0.37 (-1.39%)</td><td>257.10 <b>(+25.35%)</b></td><td>207.22 (+11.34%)</td><td>202.10 (+3.16%)</td><td>171.70 (+13.78%)</td><td>31.56 <b>(+44.38%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.47 (n/a)</td><td>2.85 (n/a)</td><td>2.68 (n/a)</td><td>2.56 (n/a)</td><td>0.37 (n/a)</td><td>205.10 (n/a)</td><td>186.12 (n/a)</td><td>195.90 (n/a)</td><td>150.90 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>5.70 (+5.58%)</td><td>4.75 (+1.20%)</td><td>4.72 (+2.47%)</td><td>3.76 (-14.14%)</td><td>0.77 <b>(+88.97%)</b></td><td>279.00 (+16.44%)</td><td>225.58 (+0.43%)</td><td>222.30 (-2.41%)</td><td>184.00 (-5.25%)</td><td>37.68 <b>(+110.46%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.40 (n/a)</td><td>4.69 (n/a)</td><td>4.60 (n/a)</td><td>4.38 (n/a)</td><td>0.41 (n/a)</td><td>239.60 (n/a)</td><td>224.62 (n/a)</td><td>227.80 (n/a)</td><td>194.20 (n/a)</td><td>17.90 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>8.64 (+8.48%)</td><td>7.51 (+1.46%)</td><td>7.81 (+4.60%)</td><td>5.68 (-15.47%)</td><td>1.17 <b>(+151.15%)</b></td><td>369.20 (+18.30%)</td><td>285.54 (+0.45%)</td><td>268.60 (-4.38%)</td><td>242.80 (-7.82%)</td><td>50.75 <b>(+175.81%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.96 (n/a)</td><td>7.40 (n/a)</td><td>7.47 (n/a)</td><td>6.72 (n/a)</td><td>0.47 (n/a)</td><td>312.10 (n/a)</td><td>284.26 (n/a)</td><td>280.90 (n/a)</td><td>263.40 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>3.78 (+9.01%)</td><td>2.85 (-0.94%)</td><td>2.57 (-6.24%)</td><td>2.12 (-6.91%)</td><td>0.75 <b>(+60.38%)</b></td><td>247.20 (+7.43%)</td><td>194.22 (+4.25%)</td><td>203.90 (+6.64%)</td><td>138.70 (-8.27%)</td><td>48.55 <b>(+57.41%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.47 (n/a)</td><td>2.88 (n/a)</td><td>2.74 (n/a)</td><td>2.28 (n/a)</td><td>0.47 (n/a)</td><td>230.10 (n/a)</td><td>186.30 (n/a)</td><td>191.20 (n/a)</td><td>151.20 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.24 (+1.86%)</td><td>0.20 (-0.27%)</td><td>0.19 (-0.55%)</td><td>0.16 (-3.95%)</td><td>0.03 (-3.12%)</td><td>202.20 (+4.12%)</td><td>170.72 (+0.12%)</td><td>173.90 (+0.52%)</td><td>136.40 (-1.87%)</td><td>23.59 (-4.32%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.20 (n/a)</td><td>170.52 (n/a)</td><td>173.00 (n/a)</td><td>139.00 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.21 (-13.79%)</td><td>0.19 (-10.96%)</td><td>0.20 (-13.66%)</td><td>0.15 (-12.45%)</td><td>0.02 <b>(-32.64%)</b></td><td>219.10 (+14.23%)</td><td>176.10 (+11.22%)</td><td>163.30 (+15.82%)</td><td>156.50 (+16.01%)</td><td>25.64 (-10.27%)</td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>191.80 (n/a)</td><td>158.34 (n/a)</td><td>141.00 (n/a)</td><td>134.90 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.51 <b>(+29.92%)</b></td><td>0.39 (+9.36%)</td><td>0.36 (+4.64%)</td><td>0.31 (-4.34%)</td><td>0.08 <b>(+191.01%)</b></td><td>209.00 (+4.55%)</td><td>173.86 (-5.99%)</td><td>183.40 (-4.43%)</td><td>129.50 <b>(-23.05%)</b></td><td>33.59 <b>(+136.79%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.03 (n/a)</td><td>199.90 (n/a)</td><td>184.94 (n/a)</td><td>191.90 (n/a)</td><td>168.30 (n/a)</td><td>14.19 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.42 (-8.04%)</td><td>0.33 (-7.81%)</td><td>0.34 (+0.67%)</td><td>0.19 <b>(-30.12%)</b></td><td>0.08 <b>(+21.49%)</b></td><td>339.80 <b>(+43.07%)</b></td><td>213.72 (+12.97%)</td><td>192.70 (-0.67%)</td><td>156.00 (+8.79%)</td><td>72.14 <b>(+104.95%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>237.50 (n/a)</td><td>189.18 (n/a)</td><td>194.00 (n/a)</td><td>143.40 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.43 (-18.49%)</td><td>0.35 (-19.46%)</td><td>0.36 <b>(-21.16%)</b></td><td>0.26 (-18.27%)</td><td>0.08 (+2.21%)</td><td>249.50 <b>(+22.36%)</b></td><td>196.28 <b>(+26.29%)</b></td><td>181.60 <b>(+26.82%)</b></td><td>152.20 <b>(+22.74%)</b></td><td>48.23 <b>(+52.30%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>203.90 (n/a)</td><td>155.42 (n/a)</td><td>143.20 (n/a)</td><td>124.00 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.82 (-7.80%)</td><td>0.72 (+5.86%)</td><td>0.70 (+4.37%)</td><td>0.67 <b>(+29.37%)</b></td><td>0.06 <b>(-54.67%)</b></td><td>196.70 <b>(-22.71%)</b></td><td>183.08 (-7.90%)</td><td>187.40 (-4.19%)</td><td>159.00 (+8.46%)</td><td>14.51 <b>(-62.08%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.89 (n/a)</td><td>0.68 (n/a)</td><td>0.67 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>254.50 (n/a)</td><td>198.78 (n/a)</td><td>195.60 (n/a)</td><td>146.60 (n/a)</td><td>38.27 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.72 <b>(-29.21%)</b></td><td>0.65 (-19.29%)</td><td>0.66 <b>(-20.49%)</b></td><td>0.58 (+10.32%)</td><td>0.05 <b>(-70.82%)</b></td><td>225.40 (-9.37%)</td><td>201.90 (+18.35%)</td><td>198.00 <b>(+25.79%)</b></td><td>182.40 <b>(+41.29%)</b></td><td>17.20 <b>(-63.50%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.01 (n/a)</td><td>0.81 (n/a)</td><td>0.83 (n/a)</td><td>0.53 (n/a)</td><td>0.19 (n/a)</td><td>248.70 (n/a)</td><td>170.60 (n/a)</td><td>157.40 (n/a)</td><td>129.10 (n/a)</td><td>47.12 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.03 (-7.68%)</td><td>0.68 (-19.96%)</td><td>0.61 <b>(-25.40%)</b></td><td>0.54 (-17.07%)</td><td>0.20 <b>(+21.05%)</b></td><td>242.20 <b>(+20.56%)</b></td><td>203.04 <b>(+28.34%)</b></td><td>216.00 <b>(+34.08%)</b></td><td>127.50 (+8.33%)</td><td>47.56 <b>(+59.31%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.11 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.65 (n/a)</td><td>0.17 (n/a)</td><td>200.90 (n/a)</td><td>158.20 (n/a)</td><td>161.10 (n/a)</td><td>117.70 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>1.02 (+7.57%)</td><td>0.72 (+1.03%)</td><td>0.65 (-11.43%)</td><td>0.59 <b>(+21.05%)</b></td><td>0.17 (+2.93%)</td><td>222.60 (-17.40%)</td><td>188.28 (-2.03%)</td><td>200.80 (+12.94%)</td><td>128.40 (-7.02%)</td><td>35.83 <b>(-26.07%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.95 (n/a)</td><td>0.71 (n/a)</td><td>0.74 (n/a)</td><td>0.49 (n/a)</td><td>0.17 (n/a)</td><td>269.50 (n/a)</td><td>192.18 (n/a)</td><td>177.80 (n/a)</td><td>138.10 (n/a)</td><td>48.47 (n/a)</td>
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
<td><code>65c00d6</code> — 2026-08-01 00:10:25</td><td>0.11 (-8.69%)</td><td>0.09 (-14.26%)</td><td>0.09 (-7.44%)</td><td>0.05 <b>(-39.73%)</b></td><td>0.02 <b>(+82.45%)</b></td><td>302.70 <b>(+65.95%)</b></td><td>202.24 <b>(+22.73%)</b></td><td>186.40 (+8.06%)</td><td>153.80 (+9.47%)</td><td>61.16 <b>(+228.17%)</b></td>
</tr>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>164.78 (n/a)</td><td>172.50 (n/a)</td><td>140.50 (n/a)</td><td>18.64 (n/a)</td>
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
