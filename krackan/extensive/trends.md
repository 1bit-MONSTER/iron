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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-12.66%)</td><td>0.03 (-12.80%)</td><td>0.03 (-7.65%)</td><td>0.03 (-17.16%)</td><td>0.01 <b>(-24.47%)</b></td><td>230.50 <b>(+20.68%)</b></td><td>179.90 (+14.22%)</td><td>176.10 (+8.30%)</td><td>147.50 (+14.52%)</td><td>30.68 (+11.00%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>157.50 (n/a)</td><td>162.60 (n/a)</td><td>128.80 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 <b>(-21.10%)</b></td><td>0.03 (-12.51%)</td><td>0.03 (-14.47%)</td><td>0.03 (-1.33%)</td><td>0.00 <b>(-43.71%)</b></td><td>204.70 (+1.34%)</td><td>179.02 (+12.73%)</td><td>178.50 (+16.90%)</td><td>160.00 <b>(+26.68%)</b></td><td>19.36 <b>(-29.88%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>158.80 (n/a)</td><td>152.70 (n/a)</td><td>126.30 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-12.39%)</td><td>0.03 <b>(-22.73%)</b></td><td>0.03 (-11.84%)</td><td>0.02 <b>(-56.51%)</b></td><td>0.01 <b>(+234.83%)</b></td><td>387.40 <b>(+129.91%)</b></td><td>224.82 <b>(+42.17%)</b></td><td>182.50 (+13.42%)</td><td>162.70 (+14.18%)</td><td>92.78 <b>(+830.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>168.50 (n/a)</td><td>158.14 (n/a)</td><td>160.90 (n/a)</td><td>142.50 (n/a)</td><td>9.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 <b>(-23.95%)</b></td><td>0.03 (-0.48%)</td><td>0.03 (+8.75%)</td><td>0.03 (+16.64%)</td><td>0.00 <b>(-70.45%)</b></td><td>201.90 (-14.27%)</td><td>186.36 (-4.21%)</td><td>186.20 (-8.05%)</td><td>165.50 <b>(+31.45%)</b></td><td>15.21 <b>(-66.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>194.56 (n/a)</td><td>202.50 (n/a)</td><td>125.90 (n/a)</td><td>45.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-18.87%)</td><td>0.03 <b>(-21.08%)</b></td><td>0.03 <b>(-24.72%)</b></td><td>0.03 (-16.16%)</td><td>0.01 <b>(-25.66%)</b></td><td>237.90 (+19.31%)</td><td>196.02 <b>(+26.06%)</b></td><td>200.10 <b>(+32.87%)</b></td><td>153.60 <b>(+23.27%)</b></td><td>30.35 (+6.73%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>155.50 (n/a)</td><td>150.60 (n/a)</td><td>124.60 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-10.39%)</td><td>0.04 (+1.79%)</td><td>0.04 (-5.77%)</td><td>0.03 <b>(+27.34%)</b></td><td>0.01 <b>(-41.48%)</b></td><td>210.00 <b>(-21.50%)</b></td><td>170.40 (-6.82%)</td><td>164.10 (+6.14%)</td><td>139.50 (+11.60%)</td><td>29.47 <b>(-49.75%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.50 (n/a)</td><td>182.88 (n/a)</td><td>154.60 (n/a)</td><td>125.00 (n/a)</td><td>58.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-10.51%)</td><td>0.03 (+6.58%)</td><td>0.03 <b>(+29.83%)</b></td><td>0.02 <b>(+36.66%)</b></td><td>0.01 <b>(-48.66%)</b></td><td>250.40 <b>(-26.85%)</b></td><td>194.18 (-13.74%)</td><td>188.60 <b>(-22.99%)</b></td><td>161.30 (+11.70%)</td><td>37.01 <b>(-55.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>342.30 (n/a)</td><td>225.12 (n/a)</td><td>244.90 (n/a)</td><td>144.40 (n/a)</td><td>82.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-9.24%)</td><td>0.03 (-1.10%)</td><td>0.03 (+6.19%)</td><td>0.02 (-0.56%)</td><td>0.01 (-17.98%)</td><td>315.90 (+0.54%)</td><td>220.64 (-0.56%)</td><td>203.10 (-5.84%)</td><td>157.40 (+10.15%)</td><td>61.19 (-7.27%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>314.20 (n/a)</td><td>221.88 (n/a)</td><td>215.70 (n/a)</td><td>142.90 (n/a)</td><td>65.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-3.74%)</td><td>0.07 (+1.18%)</td><td>0.08 (+14.03%)</td><td>0.04 <b>(-31.65%)</b></td><td>0.02 <b>(+31.51%)</b></td><td>318.30 <b>(+46.28%)</b></td><td>188.98 (+4.83%)</td><td>157.40 (-12.26%)</td><td>132.80 (+3.83%)</td><td>75.00 <b>(+110.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.60 (n/a)</td><td>180.28 (n/a)</td><td>179.40 (n/a)</td><td>127.90 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (-11.77%)</td><td>0.07 (-8.81%)</td><td>0.07 (-15.66%)</td><td>0.06 (+2.81%)</td><td>0.01 <b>(-44.92%)</b></td><td>207.60 (-2.72%)</td><td>184.28 (+6.80%)</td><td>184.70 (+18.55%)</td><td>149.60 (+13.33%)</td><td>21.55 <b>(-43.57%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.40 (n/a)</td><td>172.54 (n/a)</td><td>155.80 (n/a)</td><td>132.00 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (-7.21%)</td><td>0.07 (-4.26%)</td><td>0.07 (+2.12%)</td><td>0.05 (-12.86%)</td><td>0.01 (+7.05%)</td><td>247.20 (+14.76%)</td><td>189.46 (+5.36%)</td><td>178.00 (-2.09%)</td><td>151.60 (+7.75%)</td><td>36.54 <b>(+37.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>179.82 (n/a)</td><td>181.80 (n/a)</td><td>140.70 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-1.08%)</td><td>0.07 (-3.12%)</td><td>0.07 (+4.56%)</td><td>0.05 <b>(-26.08%)</b></td><td>0.02 <b>(+45.59%)</b></td><td>257.80 <b>(+35.26%)</b></td><td>179.68 (+7.02%)</td><td>165.80 (-4.33%)</td><td>129.70 (+1.09%)</td><td>49.51 <b>(+110.08%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>167.90 (n/a)</td><td>173.30 (n/a)</td><td>128.30 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (-15.17%)</td><td>0.07 (+8.14%)</td><td>0.06 (+6.47%)</td><td>0.06 <b>(+91.39%)</b></td><td>0.01 <b>(-64.51%)</b></td><td>204.20 <b>(-47.75%)</b></td><td>184.42 (-18.45%)</td><td>193.40 (-6.07%)</td><td>151.90 (+17.84%)</td><td>21.41 <b>(-78.76%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>390.80 (n/a)</td><td>226.14 (n/a)</td><td>205.90 (n/a)</td><td>128.90 (n/a)</td><td>100.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (+18.30%)</td><td>0.06 (-4.06%)</td><td>0.06 (-11.66%)</td><td>0.05 (-17.73%)</td><td>0.02 <b>(+90.86%)</b></td><td>271.80 <b>(+21.56%)</b></td><td>208.28 (+9.12%)</td><td>213.10 (+13.17%)</td><td>125.70 (-15.47%)</td><td>52.45 <b>(+86.40%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>190.88 (n/a)</td><td>188.30 (n/a)</td><td>148.70 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+10.22%)</td><td>0.06 (-1.66%)</td><td>0.06 (+5.74%)</td><td>0.04 <b>(-34.83%)</b></td><td>0.01 <b>(+315.39%)</b></td><td>344.70 <b>(+53.40%)</b></td><td>226.60 (+7.29%)</td><td>199.80 (-5.40%)</td><td>178.10 (-9.27%)</td><td>67.99 <b>(+497.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>211.20 (n/a)</td><td>211.20 (n/a)</td><td>196.30 (n/a)</td><td>11.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (+3.91%)</td><td>0.06 (-15.17%)</td><td>0.06 (-4.84%)</td><td>0.03 <b>(-43.97%)</b></td><td>0.02 <b>(+181.61%)</b></td><td>363.00 <b>(+78.47%)</b></td><td>237.10 <b>(+26.14%)</b></td><td>206.20 (+5.10%)</td><td>162.30 (-3.79%)</td><td>77.32 <b>(+403.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>187.96 (n/a)</td><td>196.20 (n/a)</td><td>168.70 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (+18.30%)</td><td>0.15 (+3.35%)</td><td>0.14 (-1.42%)</td><td>0.11 (-10.79%)</td><td>0.03 <b>(+153.29%)</b></td><td>216.90 (+12.09%)</td><td>169.80 (-0.64%)</td><td>171.60 (+1.42%)</td><td>133.80 (-15.48%)</td><td>34.11 <b>(+136.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>170.90 (n/a)</td><td>169.20 (n/a)</td><td>158.30 (n/a)</td><td>14.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 <b>(-21.96%)</b></td><td>0.12 (-14.16%)</td><td>0.12 (-16.90%)</td><td>0.11 (-7.11%)</td><td>0.01 <b>(-65.99%)</b></td><td>217.60 (+7.67%)</td><td>206.58 (+15.33%)</td><td>205.60 <b>(+20.37%)</b></td><td>196.40 <b>(+28.11%)</b></td><td>10.01 <b>(-54.45%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>179.12 (n/a)</td><td>170.80 (n/a)</td><td>153.30 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (-17.54%)</td><td>0.12 <b>(-22.06%)</b></td><td>0.12 <b>(-22.05%)</b></td><td>0.09 <b>(-27.38%)</b></td><td>0.02 (+6.91%)</td><td>264.10 <b>(+37.70%)</b></td><td>210.76 <b>(+29.67%)</b></td><td>211.50 <b>(+28.34%)</b></td><td>170.30 <b>(+21.30%)</b></td><td>35.84 <b>(+79.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>191.80 (n/a)</td><td>162.54 (n/a)</td><td>164.80 (n/a)</td><td>140.40 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 <b>(+44.35%)</b></td><td>0.15 (+13.16%)</td><td>0.13 (-1.04%)</td><td>0.12 (-2.86%)</td><td>0.04 <b>(+383.94%)</b></td><td>209.00 (+2.96%)</td><td>172.76 (-7.51%)</td><td>187.20 (+1.03%)</td><td>121.40 <b>(-30.71%)</b></td><td>40.22 <b>(+252.83%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>186.78 (n/a)</td><td>185.30 (n/a)</td><td>175.20 (n/a)</td><td>11.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 <b>(-31.25%)</b></td><td>0.13 (-1.06%)</td><td>0.13 (+2.08%)</td><td>0.11 <b>(+79.18%)</b></td><td>0.01 <b>(-85.87%)</b></td><td>214.20 <b>(-44.19%)</b></td><td>196.00 (-10.45%)</td><td>191.00 (-2.05%)</td><td>189.20 <b>(+45.43%)</b></td><td>10.43 <b>(-89.19%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>383.80 (n/a)</td><td>218.86 (n/a)</td><td>195.00 (n/a)</td><td>130.10 (n/a)</td><td>96.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (-4.13%)</td><td>0.13 (+5.07%)</td><td>0.14 (+9.23%)</td><td>0.10 <b>(+20.54%)</b></td><td>0.02 <b>(-30.09%)</b></td><td>240.20 (-17.03%)</td><td>188.58 (-7.68%)</td><td>173.00 (-8.47%)</td><td>157.70 (+4.30%)</td><td>33.79 <b>(-39.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>289.50 (n/a)</td><td>204.26 (n/a)</td><td>189.00 (n/a)</td><td>151.20 (n/a)</td><td>55.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (+9.87%)</td><td>0.11 (-3.32%)</td><td>0.11 (+0.33%)</td><td>0.07 <b>(-35.75%)</b></td><td>0.02 <b>(+351.79%)</b></td><td>357.90 <b>(+55.61%)</b></td><td>237.34 (+8.69%)</td><td>217.30 (-0.32%)</td><td>186.10 (-8.95%)</td><td>68.59 <b>(+576.72%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>230.00 (n/a)</td><td>218.36 (n/a)</td><td>218.00 (n/a)</td><td>204.40 (n/a)</td><td>10.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 <b>(-24.81%)</b></td><td>0.10 <b>(-25.82%)</b></td><td>0.10 (-18.89%)</td><td>0.07 <b>(-27.97%)</b></td><td>0.02 (-18.45%)</td><td>341.70 <b>(+38.85%)</b></td><td>268.46 <b>(+36.29%)</b></td><td>238.70 <b>(+23.30%)</b></td><td>198.20 <b>(+33.02%)</b></td><td>68.26 <b>(+57.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>246.10 (n/a)</td><td>196.98 (n/a)</td><td>193.60 (n/a)</td><td>149.00 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.44 <b>(+32.69%)</b></td><td>0.29 (+8.22%)</td><td>0.25 (-4.33%)</td><td>0.23 (+11.71%)</td><td>0.09 <b>(+87.42%)</b></td><td>216.00 (-10.48%)</td><td>179.64 (-4.62%)</td><td>193.40 (+4.48%)</td><td>111.70 <b>(-24.68%)</b></td><td>42.03 <b>(+22.46%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>241.30 (n/a)</td><td>188.34 (n/a)</td><td>185.10 (n/a)</td><td>148.30 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.36 <b>(+27.49%)</b></td><td>0.32 (+17.81%)</td><td>0.33 <b>(+24.37%)</b></td><td>0.25 (+1.77%)</td><td>0.05 <b>(+208.82%)</b></td><td>196.60 (-1.75%)</td><td>158.08 (-13.48%)</td><td>148.00 (-19.61%)</td><td>134.80 <b>(-21.54%)</b></td><td>27.04 <b>(+135.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>182.70 (n/a)</td><td>184.10 (n/a)</td><td>171.80 (n/a)</td><td>11.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.35 (-7.92%)</td><td>0.30 (+9.12%)</td><td>0.33 <b>(+31.66%)</b></td><td>0.23 (+1.13%)</td><td>0.06 (-4.48%)</td><td>211.00 (-1.12%)</td><td>168.84 (-8.29%)</td><td>149.50 <b>(-24.03%)</b></td><td>140.80 (+8.56%)</td><td>34.23 (+6.17%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>213.40 (n/a)</td><td>184.10 (n/a)</td><td>196.80 (n/a)</td><td>129.70 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.33 (-11.07%)</td><td>0.27 (+10.48%)</td><td>0.26 (+18.66%)</td><td>0.21 (+7.92%)</td><td>0.05 <b>(-30.31%)</b></td><td>231.50 (-7.33%)</td><td>185.26 (-11.66%)</td><td>186.80 (-15.70%)</td><td>148.40 (+12.42%)</td><td>34.28 <b>(-25.33%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>249.80 (n/a)</td><td>209.72 (n/a)</td><td>221.60 (n/a)</td><td>132.00 (n/a)</td><td>45.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.33 (-14.81%)</td><td>0.30 (-14.41%)</td><td>0.28 <b>(-20.96%)</b></td><td>0.27 (-6.48%)</td><td>0.03 <b>(-32.64%)</b></td><td>183.70 (+6.93%)</td><td>167.50 (+16.11%)</td><td>174.30 <b>(+26.49%)</b></td><td>148.20 (+17.34%)</td><td>16.71 (-15.37%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>171.80 (n/a)</td><td>144.26 (n/a)</td><td>137.80 (n/a)</td><td>126.30 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 <b>(+20.18%)</b></td><td>0.28 (-5.12%)</td><td>0.25 (-9.37%)</td><td>0.24 (-9.03%)</td><td>0.06 <b>(+112.29%)</b></td><td>207.60 (+9.96%)</td><td>184.14 (+8.04%)</td><td>196.20 (+10.35%)</td><td>126.70 (-16.81%)</td><td>32.59 <b>(+91.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>188.80 (n/a)</td><td>170.44 (n/a)</td><td>177.80 (n/a)</td><td>152.30 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 <b>(+31.84%)</b></td><td>0.29 <b>(+26.08%)</b></td><td>0.25 (+13.45%)</td><td>0.24 <b>(+52.75%)</b></td><td>0.07 <b>(+26.94%)</b></td><td>209.00 <b>(-34.52%)</b></td><td>176.30 <b>(-21.39%)</b></td><td>198.10 (-11.84%)</td><td>125.30 <b>(-24.15%)</b></td><td>37.58 <b>(-36.70%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>319.20 (n/a)</td><td>224.26 (n/a)</td><td>224.70 (n/a)</td><td>165.20 (n/a)</td><td>59.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (+2.39%)</td><td>0.23 (-1.99%)</td><td>0.24 (-1.14%)</td><td>0.17 (+3.77%)</td><td>0.05 (+2.29%)</td><td>288.30 (-3.61%)</td><td>218.36 (+1.85%)</td><td>209.00 (+1.16%)</td><td>160.80 (-2.37%)</td><td>47.09 (-6.89%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>299.10 (n/a)</td><td>214.40 (n/a)</td><td>206.60 (n/a)</td><td>164.70 (n/a)</td><td>50.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 <b>(-28.44%)</b></td><td>0.01 <b>(-21.87%)</b></td><td>0.01 (-11.01%)</td><td>0.01 (-19.58%)</td><td>0.00 <b>(-50.76%)</b></td><td>240.70 <b>(+24.33%)</b></td><td>197.18 <b>(+25.86%)</b></td><td>185.80 (+12.40%)</td><td>172.50 <b>(+39.68%)</b></td><td>26.70 (-10.54%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>156.66 (n/a)</td><td>165.30 (n/a)</td><td>123.50 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (+1.74%)</td><td>0.02 (-8.21%)</td><td>0.01 <b>(-24.42%)</b></td><td>0.01 (-17.77%)</td><td>0.01 <b>(+44.38%)</b></td><td>237.60 <b>(+21.60%)</b></td><td>180.70 (+14.28%)</td><td>206.30 <b>(+32.33%)</b></td><td>115.60 (-1.78%)</td><td>54.30 <b>(+67.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>158.12 (n/a)</td><td>155.90 (n/a)</td><td>117.70 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-5.90%)</td><td>0.02 (-0.34%)</td><td>0.02 (+3.79%)</td><td>0.01 (+4.06%)</td><td>0.00 (-17.06%)</td><td>182.40 (-3.90%)</td><td>157.10 (-0.53%)</td><td>154.40 (-3.68%)</td><td>119.00 (+6.25%)</td><td>25.90 (-12.03%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>157.94 (n/a)</td><td>160.30 (n/a)</td><td>112.00 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (+1.27%)</td><td>0.02 (-5.55%)</td><td>0.01 (-11.45%)</td><td>0.01 <b>(-20.39%)</b></td><td>0.00 <b>(+70.86%)</b></td><td>232.20 <b>(+25.58%)</b></td><td>176.88 (+9.10%)</td><td>181.00 (+12.91%)</td><td>135.70 (-1.24%)</td><td>40.96 <b>(+100.73%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>162.12 (n/a)</td><td>160.30 (n/a)</td><td>137.40 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-9.91%)</td><td>0.01 (+4.78%)</td><td>0.01 (+0.18%)</td><td>0.01 <b>(+20.52%)</b></td><td>0.00 <b>(-48.09%)</b></td><td>198.70 (-17.04%)</td><td>180.28 (-7.01%)</td><td>188.90 (-0.21%)</td><td>155.20 (+11.02%)</td><td>18.56 <b>(-52.13%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>239.50 (n/a)</td><td>193.88 (n/a)</td><td>189.30 (n/a)</td><td>139.80 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 <b>(-21.95%)</b></td><td>0.01 (-16.52%)</td><td>0.01 (-17.51%)</td><td>0.01 (-9.12%)</td><td>0.00 <b>(-42.20%)</b></td><td>216.40 (+10.02%)</td><td>188.62 (+18.26%)</td><td>186.40 <b>(+21.20%)</b></td><td>156.90 <b>(+28.08%)</b></td><td>22.35 (-18.48%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>196.70 (n/a)</td><td>159.50 (n/a)</td><td>153.80 (n/a)</td><td>122.50 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (+0.13%)</td><td>0.01 (-18.75%)</td><td>0.01 (-19.69%)</td><td>0.01 <b>(-44.99%)</b></td><td>0.00 <b>(+119.63%)</b></td><td>362.10 <b>(+81.78%)</b></td><td>231.16 <b>(+32.97%)</b></td><td>215.90 <b>(+24.51%)</b></td><td>144.80 (-0.14%)</td><td>80.69 <b>(+315.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>199.20 (n/a)</td><td>173.84 (n/a)</td><td>173.40 (n/a)</td><td>145.00 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.01 (+8.06%)</td><td>0.01 (+5.74%)</td><td>0.01 (-1.08%)</td><td>0.01 (+10.78%)</td><td>0.00 <b>(-23.56%)</b></td><td>236.40 (-9.74%)</td><td>212.00 (-5.97%)</td><td>208.60 (+1.07%)</td><td>189.90 (-7.46%)</td><td>17.80 <b>(-34.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>261.90 (n/a)</td><td>225.46 (n/a)</td><td>206.40 (n/a)</td><td>205.20 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+1.39%)</td><td>0.03 (-5.71%)</td><td>0.03 (+2.62%)</td><td>0.02 <b>(-21.37%)</b></td><td>0.01 <b>(+39.95%)</b></td><td>236.80 <b>(+27.18%)</b></td><td>171.36 (+8.62%)</td><td>156.20 (-2.56%)</td><td>134.00 (-1.33%)</td><td>40.55 <b>(+84.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.20 (n/a)</td><td>157.76 (n/a)</td><td>160.30 (n/a)</td><td>135.80 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-5.84%)</td><td>0.03 (-9.65%)</td><td>0.03 (-9.32%)</td><td>0.02 <b>(-36.80%)</b></td><td>0.01 <b>(+70.88%)</b></td><td>288.10 <b>(+58.21%)</b></td><td>182.36 (+17.47%)</td><td>173.20 (+10.25%)</td><td>134.30 (+6.25%)</td><td>62.57 <b>(+189.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.10 (n/a)</td><td>155.24 (n/a)</td><td>157.10 (n/a)</td><td>126.40 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+17.90%)</td><td>0.03 <b>(+22.17%)</b></td><td>0.03 (+9.80%)</td><td>0.03 <b>(+100.62%)</b></td><td>0.00 <b>(-46.30%)</b></td><td>186.30 <b>(-50.15%)</b></td><td>165.86 <b>(-24.79%)</b></td><td>169.50 (-8.92%)</td><td>135.50 (-15.15%)</td><td>19.63 <b>(-77.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>373.70 (n/a)</td><td>220.54 (n/a)</td><td>186.10 (n/a)</td><td>159.70 (n/a)</td><td>88.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-0.64%)</td><td>0.03 (+2.08%)</td><td>0.03 (+4.85%)</td><td>0.02 (+2.59%)</td><td>0.01 (+3.68%)</td><td>211.60 (-2.53%)</td><td>170.76 (-1.82%)</td><td>162.00 (-4.59%)</td><td>134.20 (+0.68%)</td><td>31.42 (+3.57%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>173.92 (n/a)</td><td>169.80 (n/a)</td><td>133.30 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+0.33%)</td><td>0.03 (+1.97%)</td><td>0.03 (-5.80%)</td><td>0.02 (-8.19%)</td><td>0.01 (+17.23%)</td><td>231.80 (+8.93%)</td><td>178.44 (-1.00%)</td><td>184.70 (+6.15%)</td><td>141.10 (-0.35%)</td><td>35.85 <b>(+24.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.80 (n/a)</td><td>180.24 (n/a)</td><td>174.00 (n/a)</td><td>141.60 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-7.62%)</td><td>0.03 (-2.71%)</td><td>0.03 (+8.66%)</td><td>0.02 <b>(-21.06%)</b></td><td>0.01 (+0.75%)</td><td>246.70 <b>(+26.71%)</b></td><td>174.46 (+4.40%)</td><td>156.40 (-7.95%)</td><td>122.80 (+8.19%)</td><td>46.89 <b>(+43.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>167.10 (n/a)</td><td>169.90 (n/a)</td><td>113.50 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 <b>(+32.01%)</b></td><td>0.03 <b>(+21.45%)</b></td><td>0.03 <b>(+22.56%)</b></td><td>0.03 (+15.69%)</td><td>0.01 <b>(+48.73%)</b></td><td>196.50 (-13.55%)</td><td>154.26 (-16.96%)</td><td>155.50 (-18.37%)</td><td>117.40 <b>(-24.26%)</b></td><td>28.55 (-1.39%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.30 (n/a)</td><td>185.76 (n/a)</td><td>190.50 (n/a)</td><td>155.00 (n/a)</td><td>28.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+12.82%)</td><td>0.03 <b>(+20.76%)</b></td><td>0.03 (+12.69%)</td><td>0.03 <b>(+71.23%)</b></td><td>0.00 <b>(-62.48%)</b></td><td>206.50 <b>(-41.60%)</b></td><td>190.46 <b>(-20.58%)</b></td><td>183.80 (-11.25%)</td><td>178.50 (-11.37%)</td><td>12.40 <b>(-80.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>353.60 (n/a)</td><td>239.80 (n/a)</td><td>207.10 (n/a)</td><td>201.40 (n/a)</td><td>64.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (+15.36%)</td><td>0.07 (+5.50%)</td><td>0.07 (-4.94%)</td><td>0.05 (-12.86%)</td><td>0.02 <b>(+79.27%)</b></td><td>232.70 (+14.74%)</td><td>157.52 (-0.44%)</td><td>151.20 (+5.22%)</td><td>112.20 (-13.29%)</td><td>49.91 <b>(+69.65%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>158.22 (n/a)</td><td>143.70 (n/a)</td><td>129.40 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 <b>(+26.27%)</b></td><td>0.07 <b>(+21.06%)</b></td><td>0.07 (+16.72%)</td><td>0.06 <b>(+35.71%)</b></td><td>0.01 (+19.95%)</td><td>175.50 <b>(-26.29%)</b></td><td>150.06 (-17.69%)</td><td>147.60 (-14.34%)</td><td>129.20 <b>(-20.78%)</b></td><td>21.33 <b>(-32.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>182.32 (n/a)</td><td>172.30 (n/a)</td><td>163.10 (n/a)</td><td>31.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (+9.77%)</td><td>0.06 (-6.23%)</td><td>0.07 (-4.77%)</td><td>0.05 (-16.06%)</td><td>0.01 <b>(+72.62%)</b></td><td>230.10 (+19.10%)</td><td>173.82 (+10.05%)</td><td>153.00 (+5.01%)</td><td>128.40 (-8.94%)</td><td>42.31 <b>(+91.88%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>157.94 (n/a)</td><td>145.70 (n/a)</td><td>141.00 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-1.99%)</td><td>0.07 (+10.73%)</td><td>0.06 (+10.94%)</td><td>0.05 <b>(+23.72%)</b></td><td>0.02 (-13.61%)</td><td>202.90 (-19.16%)</td><td>161.42 (-11.90%)</td><td>162.80 (-9.86%)</td><td>118.40 (+1.98%)</td><td>37.44 <b>(-27.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>251.00 (n/a)</td><td>183.22 (n/a)</td><td>180.60 (n/a)</td><td>116.10 (n/a)</td><td>51.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-12.40%)</td><td>0.07 (+4.71%)</td><td>0.06 <b>(+23.14%)</b></td><td>0.05 (+2.22%)</td><td>0.02 <b>(-20.12%)</b></td><td>201.40 (-2.19%)</td><td>163.24 (-6.21%)</td><td>163.50 (-18.82%)</td><td>123.30 (+14.17%)</td><td>37.90 (-12.08%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>205.90 (n/a)</td><td>174.04 (n/a)</td><td>201.40 (n/a)</td><td>108.00 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-0.44%)</td><td>0.06 (+4.73%)</td><td>0.06 (+7.80%)</td><td>0.05 (+3.21%)</td><td>0.01 (-10.12%)</td><td>219.80 (-3.13%)</td><td>169.68 (-5.44%)</td><td>164.20 (-7.23%)</td><td>121.60 (+0.50%)</td><td>35.52 (-12.55%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.90 (n/a)</td><td>179.44 (n/a)</td><td>177.00 (n/a)</td><td>121.00 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+2.96%)</td><td>0.06 (+9.94%)</td><td>0.07 (+9.09%)</td><td>0.05 (+19.06%)</td><td>0.01 (-12.71%)</td><td>231.10 (-15.99%)</td><td>174.34 (-10.50%)</td><td>160.00 (-8.31%)</td><td>146.30 (-2.92%)</td><td>34.28 <b>(-29.76%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>275.10 (n/a)</td><td>194.80 (n/a)</td><td>174.50 (n/a)</td><td>150.70 (n/a)</td><td>48.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+1.04%)</td><td>0.06 (+15.97%)</td><td>0.06 <b>(+38.77%)</b></td><td>0.04 <b>(+29.80%)</b></td><td>0.01 <b>(-25.28%)</b></td><td>241.50 <b>(-22.97%)</b></td><td>186.72 (-17.23%)</td><td>170.30 <b>(-27.93%)</b></td><td>143.20 (-1.04%)</td><td>39.20 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>313.50 (n/a)</td><td>225.60 (n/a)</td><td>236.30 (n/a)</td><td>144.70 (n/a)</td><td>66.68 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 <b>(+31.61%)</b></td><td>0.11 (-10.70%)</td><td>0.10 (-17.73%)</td><td>0.06 <b>(-41.09%)</b></td><td>0.05 <b>(+185.99%)</b></td><td>365.00 <b>(+69.77%)</b></td><td>221.96 <b>(+26.37%)</b></td><td>215.30 <b>(+21.57%)</b></td><td>116.60 <b>(-23.99%)</b></td><td>91.27 <b>(+268.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>175.64 (n/a)</td><td>177.10 (n/a)</td><td>153.40 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (-4.25%)</td><td>0.14 (+6.76%)</td><td>0.14 (+2.91%)</td><td>0.10 (+14.69%)</td><td>0.03 (-15.25%)</td><td>203.10 (-12.83%)</td><td>153.64 (-7.89%)</td><td>154.10 (-2.84%)</td><td>124.20 (+4.46%)</td><td>31.61 <b>(-25.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>233.00 (n/a)</td><td>166.80 (n/a)</td><td>158.60 (n/a)</td><td>118.90 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (+1.54%)</td><td>0.13 (-6.69%)</td><td>0.13 (-9.79%)</td><td>0.08 <b>(-23.45%)</b></td><td>0.03 <b>(+39.17%)</b></td><td>274.20 <b>(+30.63%)</b></td><td>175.68 (+11.32%)</td><td>160.10 (+10.87%)</td><td>132.50 (-1.56%)</td><td>56.53 <b>(+85.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>157.82 (n/a)</td><td>144.40 (n/a)</td><td>134.60 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-1.28%)</td><td>0.12 (-6.63%)</td><td>0.12 (-4.52%)</td><td>0.10 (-16.13%)</td><td>0.02 <b>(+77.64%)</b></td><td>219.60 (+19.22%)</td><td>183.04 (+8.22%)</td><td>178.10 (+4.76%)</td><td>159.70 (+1.27%)</td><td>24.86 <b>(+115.12%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>169.14 (n/a)</td><td>170.00 (n/a)</td><td>157.70 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (-11.92%)</td><td>0.12 (-9.39%)</td><td>0.12 (-12.94%)</td><td>0.11 (+4.39%)</td><td>0.01 <b>(-46.61%)</b></td><td>188.50 (-4.22%)</td><td>169.10 (+8.68%)</td><td>169.80 (+14.88%)</td><td>146.20 (+13.51%)</td><td>15.25 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>155.60 (n/a)</td><td>147.80 (n/a)</td><td>128.80 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 <b>(+33.82%)</b></td><td>0.13 (+19.08%)</td><td>0.13 <b>(+22.13%)</b></td><td>0.10 (+1.21%)</td><td>0.03 <b>(+103.97%)</b></td><td>220.20 (-1.21%)</td><td>168.52 (-13.60%)</td><td>163.40 (-18.14%)</td><td>117.30 <b>(-25.29%)</b></td><td>37.93 <b>(+50.64%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>195.04 (n/a)</td><td>199.60 (n/a)</td><td>157.00 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (+6.98%)</td><td>0.12 (+1.73%)</td><td>0.12 (-2.28%)</td><td>0.10 (-11.50%)</td><td>0.02 <b>(+109.81%)</b></td><td>219.70 (+13.01%)</td><td>179.54 (-0.45%)</td><td>181.50 (+2.37%)</td><td>155.50 (-6.49%)</td><td>26.11 <b>(+116.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>180.36 (n/a)</td><td>177.30 (n/a)</td><td>166.30 (n/a)</td><td>12.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (-4.44%)</td><td>0.11 (-1.43%)</td><td>0.12 <b>(+20.39%)</b></td><td>0.06 <b>(-34.65%)</b></td><td>0.03 <b>(+32.72%)</b></td><td>357.60 <b>(+53.02%)</b></td><td>215.78 (+7.55%)</td><td>180.70 (-16.92%)</td><td>150.30 (+4.67%)</td><td>82.57 <b>(+127.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>233.70 (n/a)</td><td>200.64 (n/a)</td><td>217.50 (n/a)</td><td>143.60 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>176.60 (n/a)</td><td>150.94 (n/a)</td><td>167.20 (n/a)</td><td>118.00 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>178.62 (n/a)</td><td>179.80 (n/a)</td><td>123.90 (n/a)</td><td>43.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>183.12 (n/a)</td><td>166.10 (n/a)</td><td>156.90 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>182.98 (n/a)</td><td>194.10 (n/a)</td><td>139.90 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>171.16 (n/a)</td><td>185.30 (n/a)</td><td>123.60 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>167.82 (n/a)</td><td>160.90 (n/a)</td><td>153.80 (n/a)</td><td>16.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>161.14 (n/a)</td><td>152.90 (n/a)</td><td>124.70 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>290.60 (n/a)</td><td>231.64 (n/a)</td><td>227.40 (n/a)</td><td>177.10 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>207.00 (n/a)</td><td>165.88 (n/a)</td><td>172.30 (n/a)</td><td>124.60 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>234.90 (n/a)</td><td>178.36 (n/a)</td><td>171.50 (n/a)</td><td>137.80 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>171.32 (n/a)</td><td>175.60 (n/a)</td><td>136.70 (n/a)</td><td>29.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>184.88 (n/a)</td><td>185.30 (n/a)</td><td>162.10 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 (+6.08%)</td><td>0.28 (-4.86%)</td><td>0.27 (-6.60%)</td><td>0.23 (-6.95%)</td><td>0.07 <b>(+39.91%)</b></td><td>217.60 (+7.51%)</td><td>181.64 (+7.12%)</td><td>182.80 (+7.09%)</td><td>126.70 (-5.73%)</td><td>37.04 <b>(+43.44%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>202.40 (n/a)</td><td>169.56 (n/a)</td><td>170.70 (n/a)</td><td>134.40 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>220.20 (n/a)</td><td>167.62 (n/a)</td><td>154.90 (n/a)</td><td>132.30 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>173.40 (n/a)</td><td>154.80 (n/a)</td><td>156.80 (n/a)</td><td>130.50 (n/a)</td><td>15.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>229.40 (n/a)</td><td>190.18 (n/a)</td><td>178.00 (n/a)</td><td>169.30 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>162.24 (n/a)</td><td>169.20 (n/a)</td><td>103.90 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>180.12 (n/a)</td><td>175.40 (n/a)</td><td>127.60 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>171.20 (n/a)</td><td>171.10 (n/a)</td><td>141.90 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>218.90 (n/a)</td><td>208.12 (n/a)</td><td>207.00 (n/a)</td><td>196.70 (n/a)</td><td>9.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>157.66 (n/a)</td><td>152.50 (n/a)</td><td>122.40 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.80 (n/a)</td><td>184.32 (n/a)</td><td>178.20 (n/a)</td><td>136.50 (n/a)</td><td>45.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>243.50 (n/a)</td><td>197.12 (n/a)</td><td>182.00 (n/a)</td><td>169.20 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>251.10 (n/a)</td><td>212.86 (n/a)</td><td>218.00 (n/a)</td><td>180.70 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>156.82 (n/a)</td><td>150.20 (n/a)</td><td>123.20 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>179.84 (n/a)</td><td>180.10 (n/a)</td><td>164.60 (n/a)</td><td>11.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>244.20 (n/a)</td><td>193.56 (n/a)</td><td>193.50 (n/a)</td><td>154.30 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>209.14 (n/a)</td><td>217.30 (n/a)</td><td>188.40 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>209.70 (n/a)</td><td>179.56 (n/a)</td><td>170.90 (n/a)</td><td>156.40 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>245.10 (n/a)</td><td>197.56 (n/a)</td><td>206.60 (n/a)</td><td>140.30 (n/a)</td><td>39.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>236.00 (n/a)</td><td>191.58 (n/a)</td><td>178.20 (n/a)</td><td>171.50 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>151.10 (n/a)</td><td>157.50 (n/a)</td><td>91.50 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.30 (n/a)</td><td>173.46 (n/a)</td><td>175.70 (n/a)</td><td>138.30 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>169.68 (n/a)</td><td>165.60 (n/a)</td><td>127.60 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>182.10 (n/a)</td><td>179.30 (n/a)</td><td>162.20 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.80 (n/a)</td><td>197.86 (n/a)</td><td>216.30 (n/a)</td><td>147.40 (n/a)</td><td>46.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>281.10 (n/a)</td><td>200.00 (n/a)</td><td>173.10 (n/a)</td><td>159.90 (n/a)</td><td>51.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.40 (n/a)</td><td>191.58 (n/a)</td><td>208.30 (n/a)</td><td>145.80 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>374.40 (n/a)</td><td>241.92 (n/a)</td><td>231.90 (n/a)</td><td>171.30 (n/a)</td><td>78.65 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>200.02 (n/a)</td><td>197.30 (n/a)</td><td>151.70 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>186.88 (n/a)</td><td>181.70 (n/a)</td><td>146.30 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>185.00 (n/a)</td><td>180.90 (n/a)</td><td>128.50 (n/a)</td><td>41.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>210.40 (n/a)</td><td>205.20 (n/a)</td><td>174.40 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.80 (n/a)</td><td>190.46 (n/a)</td><td>174.10 (n/a)</td><td>150.60 (n/a)</td><td>54.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>183.90 (n/a)</td><td>187.80 (n/a)</td><td>144.90 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>185.08 (n/a)</td><td>194.00 (n/a)</td><td>121.90 (n/a)</td><td>40.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.90 (n/a)</td><td>214.18 (n/a)</td><td>198.90 (n/a)</td><td>166.00 (n/a)</td><td>51.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>166.34 (n/a)</td><td>166.90 (n/a)</td><td>131.30 (n/a)</td><td>34.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>194.82 (n/a)</td><td>182.00 (n/a)</td><td>163.60 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>190.72 (n/a)</td><td>186.00 (n/a)</td><td>161.60 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>178.04 (n/a)</td><td>178.00 (n/a)</td><td>165.60 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>255.50 (n/a)</td><td>183.42 (n/a)</td><td>182.00 (n/a)</td><td>105.50 (n/a)</td><td>56.10 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>182.56 (n/a)</td><td>177.10 (n/a)</td><td>167.50 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>313.40 (n/a)</td><td>208.04 (n/a)</td><td>202.80 (n/a)</td><td>138.40 (n/a)</td><td>66.23 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>334.40 (n/a)</td><td>237.28 (n/a)</td><td>225.80 (n/a)</td><td>175.80 (n/a)</td><td>58.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>214.90 (n/a)</td><td>181.78 (n/a)</td><td>173.70 (n/a)</td><td>144.70 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.80 (n/a)</td><td>161.48 (n/a)</td><td>163.80 (n/a)</td><td>139.40 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.60 (n/a)</td><td>173.10 (n/a)</td><td>177.00 (n/a)</td><td>147.00 (n/a)</td><td>15.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>257.40 (n/a)</td><td>185.86 (n/a)</td><td>178.10 (n/a)</td><td>152.50 (n/a)</td><td>41.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>336.00 (n/a)</td><td>201.96 (n/a)</td><td>165.70 (n/a)</td><td>151.90 (n/a)</td><td>77.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.40 (n/a)</td><td>196.04 (n/a)</td><td>195.90 (n/a)</td><td>147.50 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.00 (n/a)</td><td>204.10 (n/a)</td><td>207.00 (n/a)</td><td>168.20 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>4.82 (+13.92%)</td><td>4.34 (+7.71%)</td><td>4.27 (+3.89%)</td><td>4.06 (+15.01%)</td><td>0.31 (+9.56%)</td><td>2317.40 (-13.05%)</td><td>2177.60 (-7.19%)</td><td>2200.70 (-3.74%)</td><td>1949.30 (-12.22%)</td><td>148.82 (-17.56%)</td><td>1897.78 (+13.92%)</td><td>1705.49 (+7.71%)</td><td>1681.01 (+3.89%)</td><td>1596.34 (+15.01%)</td><td>121.87 (+9.56%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.23 (n/a)</td><td>4.03 (n/a)</td><td>4.11 (n/a)</td><td>3.53 (n/a)</td><td>0.28 (n/a)</td><td>2665.20 (n/a)</td><td>2346.42 (n/a)</td><td>2286.30 (n/a)</td><td>2220.70 (n/a)</td><td>180.52 (n/a)</td><td>1665.86 (n/a)</td><td>1583.44 (n/a)</td><td>1618.09 (n/a)</td><td>1388.01 (n/a)</td><td>111.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.00 (-9.94%)</td><td>0.84 (-0.08%)</td><td>0.96 (+7.98%)</td><td>0.56 (-3.46%)</td><td>0.20 (-16.64%)</td><td>397.20 (+3.60%)</td><td>278.80 (-1.60%)</td><td>229.80 (-7.38%)</td><td>222.10 (+11.05%)</td><td>77.15 (-9.80%)</td><td>42.49 (-9.94%)</td><td>35.71 (-0.08%)</td><td>41.07 (+7.98%)</td><td>23.76 (-3.46%)</td><td>8.48 (-16.64%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.11 (n/a)</td><td>0.84 (n/a)</td><td>0.89 (n/a)</td><td>0.58 (n/a)</td><td>0.24 (n/a)</td><td>383.40 (n/a)</td><td>283.34 (n/a)</td><td>248.10 (n/a)</td><td>200.00 (n/a)</td><td>85.53 (n/a)</td><td>47.18 (n/a)</td><td>35.74 (n/a)</td><td>38.04 (n/a)</td><td>24.61 (n/a)</td><td>10.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.15 (+11.04%)</td><td>0.93 (+3.54%)</td><td>0.93 (-2.77%)</td><td>0.69 <b>(+20.25%)</b></td><td>0.17 (-8.34%)</td><td>321.70 (-16.85%)</td><td>244.12 (-5.20%)</td><td>236.90 (+2.87%)</td><td>192.20 (-9.93%)</td><td>49.04 <b>(-32.70%)</b></td><td>49.09 (+11.04%)</td><td>39.82 (+3.54%)</td><td>39.84 (-2.77%)</td><td>29.33 <b>(+20.25%)</b></td><td>7.37 (-8.34%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td><td>0.96 (n/a)</td><td>0.57 (n/a)</td><td>0.19 (n/a)</td><td>386.90 (n/a)</td><td>257.50 (n/a)</td><td>230.30 (n/a)</td><td>213.40 (n/a)</td><td>72.88 (n/a)</td><td>44.21 (n/a)</td><td>38.46 (n/a)</td><td>40.98 (n/a)</td><td>24.39 (n/a)</td><td>8.04 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.52 (+0.04%)</td><td>0.52 (+0.34%)</td><td>0.52 (+0.02%)</td><td>0.52 (+1.30%)</td><td>0.00 <b>(-87.40%)</b></td><td>48694.20 (-1.28%)</td><td>48632.26 (-0.34%)</td><td>48622.40 (-0.02%)</td><td>48597.60 (-0.04%)</td><td>38.00 <b>(-87.57%)</b></td><td>353.51 (+0.04%)</td><td>353.26 (+0.34%)</td><td>353.33 (+0.02%)</td><td>352.81 (+1.30%)</td><td>0.28 <b>(-87.41%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>49327.70 (n/a)</td><td>48798.02 (n/a)</td><td>48632.10 (n/a)</td><td>48616.00 (n/a)</td><td>305.73 (n/a)</td><td>353.38 (n/a)</td><td>352.07 (n/a)</td><td>353.26 (n/a)</td><td>348.28 (n/a)</td><td>2.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (+0.61%)</td><td>0.21 (+0.48%)</td><td>0.21 (+0.57%)</td><td>0.21 (-0.19%)</td><td>0.00 <b>(+20.78%)</b></td><td>119815.00 (+0.19%)</td><td>117670.22 (-0.47%)</td><td>117574.50 (-0.56%)</td><td>116304.40 (-0.60%)</td><td>1385.89 <b>(+20.40%)</b></td><td>147.71 (+0.61%)</td><td>146.02 (+0.48%)</td><td>146.12 (+0.57%)</td><td>143.39 (-0.19%)</td><td>1.71 <b>(+20.78%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119588.10 (n/a)</td><td>118228.50 (n/a)</td><td>118241.20 (n/a)</td><td>117010.70 (n/a)</td><td>1151.05 (n/a)</td><td>146.82 (n/a)</td><td>145.32 (n/a)</td><td>145.30 (n/a)</td><td>143.66 (n/a)</td><td>1.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.89 (+1.02%)</td><td>0.89 (+0.68%)</td><td>0.89 (+0.98%)</td><td>0.88 (+0.33%)</td><td>0.01 <b>(+66.37%)</b></td><td>28660.20 (-0.32%)</td><td>28394.78 (-0.67%)</td><td>28306.80 (-0.97%)</td><td>28137.80 (-1.01%)</td><td>223.02 <b>(+64.32%)</b></td><td>610.56 (+1.02%)</td><td>605.07 (+0.68%)</td><td>606.92 (+0.98%)</td><td>599.43 (+0.33%)</td><td>4.75 <b>(+66.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28753.60 (n/a)</td><td>28586.58 (n/a)</td><td>28583.40 (n/a)</td><td>28424.70 (n/a)</td><td>135.72 (n/a)</td><td>604.40 (n/a)</td><td>600.99 (n/a)</td><td>601.04 (n/a)</td><td>597.49 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.52 (-0.51%)</td><td>3.47 (+1.37%)</td><td>3.51 (+0.26%)</td><td>3.32 (+2.80%)</td><td>0.08 <b>(-35.80%)</b></td><td>7574.20 (-2.72%)</td><td>7248.82 (-1.42%)</td><td>7172.50 (-0.26%)</td><td>7147.30 (+0.52%)</td><td>182.66 <b>(-36.98%)</b></td><td>2403.69 (-0.51%)</td><td>2371.19 (+1.37%)</td><td>2395.23 (+0.26%)</td><td>2268.22 (+2.80%)</td><td>57.83 <b>(-35.80%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.54 (n/a)</td><td>3.43 (n/a)</td><td>3.50 (n/a)</td><td>3.23 (n/a)</td><td>0.13 (n/a)</td><td>7786.30 (n/a)</td><td>7353.26 (n/a)</td><td>7191.20 (n/a)</td><td>7110.50 (n/a)</td><td>289.84 (n/a)</td><td>2416.12 (n/a)</td><td>2339.20 (n/a)</td><td>2389.00 (n/a)</td><td>2206.42 (n/a)</td><td>90.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.13 (+9.13%)</td><td>2.89 (+4.79%)</td><td>2.88 (+2.39%)</td><td>2.72 (+5.15%)</td><td>0.15 <b>(+34.92%)</b></td><td>9268.90 (-4.90%)</td><td>8712.56 (-4.49%)</td><td>8742.70 (-2.33%)</td><td>8046.90 (-8.36%)</td><td>455.87 (+16.84%)</td><td>2134.97 (+9.13%)</td><td>1976.26 (+4.79%)</td><td>1965.05 (+2.39%)</td><td>1853.50 (+5.15%)</td><td>105.41 <b>(+34.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>2.87 (n/a)</td><td>2.76 (n/a)</td><td>2.81 (n/a)</td><td>2.58 (n/a)</td><td>0.11 (n/a)</td><td>9746.30 (n/a)</td><td>9122.14 (n/a)</td><td>8951.30 (n/a)</td><td>8781.40 (n/a)</td><td>390.15 (n/a)</td><td>1956.39 (n/a)</td><td>1885.99 (n/a)</td><td>1919.26 (n/a)</td><td>1762.70 (n/a)</td><td>78.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.34 (+1.82%)</td><td>3.26 (+1.82%)</td><td>3.26 (+1.51%)</td><td>3.19 (+1.45%)</td><td>0.07 <b>(+20.48%)</b></td><td>7891.30 (-1.43%)</td><td>7726.24 (-1.77%)</td><td>7723.70 (-1.49%)</td><td>7532.10 (-1.79%)</td><td>156.39 (+16.81%)</td><td>2280.88 (+1.82%)</td><td>2224.31 (+1.82%)</td><td>2224.32 (+1.51%)</td><td>2177.05 (+1.45%)</td><td>45.11 <b>(+20.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.28 (n/a)</td><td>3.20 (n/a)</td><td>3.21 (n/a)</td><td>3.14 (n/a)</td><td>0.05 (n/a)</td><td>8006.10 (n/a)</td><td>7865.74 (n/a)</td><td>7840.60 (n/a)</td><td>7669.00 (n/a)</td><td>133.88 (n/a)</td><td>2240.18 (n/a)</td><td>2184.64 (n/a)</td><td>2191.14 (n/a)</td><td>2145.84 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.78 (+0.02%)</td><td>0.78 (+0.03%)</td><td>0.78 (+0.02%)</td><td>0.78 (+0.08%)</td><td>0.00 <b>(-28.23%)</b></td><td>96555.70 (-0.08%)</td><td>96456.16 (-0.03%)</td><td>96441.30 (-0.02%)</td><td>96392.20 (-0.02%)</td><td>60.46 <b>(-28.30%)</b></td><td>712.92 (+0.02%)</td><td>712.44 (+0.03%)</td><td>712.55 (+0.02%)</td><td>711.71 (+0.08%)</td><td>0.45 <b>(-28.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96630.40 (n/a)</td><td>96482.92 (n/a)</td><td>96457.20 (n/a)</td><td>96415.60 (n/a)</td><td>84.32 (n/a)</td><td>712.74 (n/a)</td><td>712.25 (n/a)</td><td>712.43 (n/a)</td><td>711.16 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.73 (-0.01%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.10%)</td><td>0.73 (+0.03%)</td><td>0.00 (-15.24%)</td><td>103904.40 (-0.03%)</td><td>103744.98 (+0.04%)</td><td>103756.00 (+0.10%)</td><td>103614.40 (+0.01%)</td><td>111.96 (-15.29%)</td><td>663.22 (-0.01%)</td><td>662.39 (-0.04%)</td><td>662.32 (-0.10%)</td><td>661.37 (+0.03%)</td><td>0.71 (-15.24%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103933.50 (n/a)</td><td>103703.72 (n/a)</td><td>103655.70 (n/a)</td><td>103601.60 (n/a)</td><td>132.17 (n/a)</td><td>663.31 (n/a)</td><td>662.65 (n/a)</td><td>662.96 (n/a)</td><td>661.19 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.70 (+0.73%)</td><td>0.70 (+0.79%)</td><td>0.70 (+0.81%)</td><td>0.69 (+0.76%)</td><td>0.00 <b>(-24.47%)</b></td><td>108910.50 (-0.75%)</td><td>108587.94 (-0.78%)</td><td>108581.30 (-0.80%)</td><td>108322.10 (-0.72%)</td><td>218.89 <b>(-25.59%)</b></td><td>634.40 (+0.73%)</td><td>632.85 (+0.79%)</td><td>632.88 (+0.81%)</td><td>630.97 (+0.76%)</td><td>1.27 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109733.50 (n/a)</td><td>109442.22 (n/a)</td><td>109457.70 (n/a)</td><td>109107.80 (n/a)</td><td>294.15 (n/a)</td><td>629.83 (n/a)</td><td>627.91 (n/a)</td><td>627.82 (n/a)</td><td>626.24 (n/a)</td><td>1.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.57 (+2.78%)</td><td>6.83 (+0.14%)</td><td>7.21 (+6.68%)</td><td>4.97 <b>(-22.50%)</b></td><td>1.06 <b>(+162.16%)</b></td><td>1794.20 <b>(+29.02%)</b></td><td>1337.56 (+2.02%)</td><td>1236.00 (-6.26%)</td><td>1177.00 (-2.70%)</td><td>257.47 <b>(+236.57%)</b></td><td>456.12 (+2.78%)</td><td>411.17 (+0.14%)</td><td>434.34 (+6.68%)</td><td>299.23 <b>(-22.50%)</b></td><td>63.74 <b>(+162.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.37 (n/a)</td><td>6.82 (n/a)</td><td>6.76 (n/a)</td><td>6.41 (n/a)</td><td>0.40 (n/a)</td><td>1390.60 (n/a)</td><td>1311.08 (n/a)</td><td>1318.60 (n/a)</td><td>1209.70 (n/a)</td><td>76.50 (n/a)</td><td>443.79 (n/a)</td><td>410.62 (n/a)</td><td>407.15 (n/a)</td><td>386.08 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.10 (+2.31%)</td><td>5.98 (-11.89%)</td><td>6.47 (-4.68%)</td><td>4.66 <b>(-30.56%)</b></td><td>1.21 <b>(+1129.14%)</b></td><td>1914.50 <b>(+44.01%)</b></td><td>1542.78 (+17.55%)</td><td>1378.60 (+4.92%)</td><td>1255.10 (-2.25%)</td><td>331.26 <b>(+1655.28%)</b></td><td>427.75 (+2.31%)</td><td>360.48 (-11.89%)</td><td>389.43 (-4.68%)</td><td>280.43 <b>(-30.56%)</b></td><td>72.82 <b>(+1129.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.94 (n/a)</td><td>6.79 (n/a)</td><td>6.78 (n/a)</td><td>6.70 (n/a)</td><td>0.10 (n/a)</td><td>1329.40 (n/a)</td><td>1312.40 (n/a)</td><td>1314.00 (n/a)</td><td>1284.00 (n/a)</td><td>18.87 (n/a)</td><td>418.11 (n/a)</td><td>409.14 (n/a)</td><td>408.57 (n/a)</td><td>403.84 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.03 (+1.12%)</td><td>5.71 (-12.92%)</td><td>5.99 (-8.50%)</td><td>4.53 <b>(-26.25%)</b></td><td>1.07 <b>(+223.69%)</b></td><td>1967.20 <b>(+35.59%)</b></td><td>1607.26 (+17.98%)</td><td>1487.30 (+9.28%)</td><td>1267.70 (-1.10%)</td><td>308.47 <b>(+347.31%)</b></td><td>423.51 (+1.12%)</td><td>343.88 (-12.92%)</td><td>360.96 (-8.50%)</td><td>272.91 <b>(-26.25%)</b></td><td>64.51 <b>(+223.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.95 (n/a)</td><td>6.56 (n/a)</td><td>6.55 (n/a)</td><td>6.14 (n/a)</td><td>0.33 (n/a)</td><td>1450.80 (n/a)</td><td>1362.28 (n/a)</td><td>1361.00 (n/a)</td><td>1281.80 (n/a)</td><td>68.96 (n/a)</td><td>418.84 (n/a)</td><td>394.90 (n/a)</td><td>394.48 (n/a)</td><td>370.04 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.22 (-0.66%)</td><td>7.86 (+1.07%)</td><td>7.98 (+0.39%)</td><td>6.99 (-4.18%)</td><td>0.50 <b>(+24.01%)</b></td><td>4984.70 (+4.37%)</td><td>4450.08 (-0.92%)</td><td>4368.40 (-0.39%)</td><td>4242.70 (+0.66%)</td><td>307.35 <b>(+30.25%)</b></td><td>506.16 (-0.66%)</td><td>484.28 (+1.07%)</td><td>491.60 (+0.39%)</td><td>430.82 (-4.18%)</td><td>31.01 <b>(+24.01%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.27 (n/a)</td><td>7.78 (n/a)</td><td>7.95 (n/a)</td><td>7.30 (n/a)</td><td>0.41 (n/a)</td><td>4776.10 (n/a)</td><td>4491.60 (n/a)</td><td>4385.50 (n/a)</td><td>4214.80 (n/a)</td><td>235.96 (n/a)</td><td>509.51 (n/a)</td><td>479.16 (n/a)</td><td>489.68 (n/a)</td><td>449.63 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.93 (+0.85%)</td><td>7.38 (-3.08%)</td><td>7.13 (-6.37%)</td><td>6.96 (-5.44%)</td><td>0.46 <b>(+163.31%)</b></td><td>5006.70 (+5.75%)</td><td>4736.38 (+3.45%)</td><td>4888.30 (+6.80%)</td><td>4398.90 (-0.85%)</td><td>290.36 <b>(+174.42%)</b></td><td>488.19 (+0.85%)</td><td>454.80 (-3.08%)</td><td>439.31 (-6.37%)</td><td>428.92 (-5.44%)</td><td>28.45 <b>(+163.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.86 (n/a)</td><td>7.62 (n/a)</td><td>7.62 (n/a)</td><td>7.36 (n/a)</td><td>0.18 (n/a)</td><td>4734.40 (n/a)</td><td>4578.24 (n/a)</td><td>4576.90 (n/a)</td><td>4436.50 (n/a)</td><td>105.81 (n/a)</td><td>484.05 (n/a)</td><td>469.26 (n/a)</td><td>469.20 (n/a)</td><td>453.59 (n/a)</td><td>10.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.42 (-3.24%)</td><td>7.15 (-2.86%)</td><td>7.18 (-2.26%)</td><td>6.91 (-3.98%)</td><td>0.23 (+15.55%)</td><td>5048.60 (+4.15%)</td><td>4877.04 (+2.96%)</td><td>4855.50 (+2.31%)</td><td>4697.50 (+3.35%)</td><td>154.26 <b>(+24.58%)</b></td><td>457.16 (-3.24%)</td><td>440.68 (-2.86%)</td><td>442.27 (-2.26%)</td><td>425.36 (-3.98%)</td><td>13.93 (+15.55%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.67 (n/a)</td><td>7.36 (n/a)</td><td>7.35 (n/a)</td><td>7.19 (n/a)</td><td>0.20 (n/a)</td><td>4847.60 (n/a)</td><td>4736.60 (n/a)</td><td>4746.00 (n/a)</td><td>4545.30 (n/a)</td><td>123.83 (n/a)</td><td>472.46 (n/a)</td><td>453.63 (n/a)</td><td>452.48 (n/a)</td><td>443.00 (n/a)</td><td>12.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.79 (+0.02%)</td><td>0.79 (+0.03%)</td><td>0.79 (+0.07%)</td><td>0.79 (+0.04%)</td><td>0.00 (+16.00%)</td><td>95894.70 (-0.04%)</td><td>95773.68 (-0.03%)</td><td>95708.40 (-0.07%)</td><td>95693.60 (-0.02%)</td><td>102.14 (+15.96%)</td><td>718.12 (+0.02%)</td><td>717.52 (+0.03%)</td><td>718.01 (+0.07%)</td><td>716.61 (+0.04%)</td><td>0.76 (+16.00%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95929.40 (n/a)</td><td>95801.40 (n/a)</td><td>95774.50 (n/a)</td><td>95717.20 (n/a)</td><td>88.08 (n/a)</td><td>717.94 (n/a)</td><td>717.31 (n/a)</td><td>717.51 (n/a)</td><td>716.35 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.73 (+0.00%)</td><td>0.73 (-0.02%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.13%)</td><td>0.00 <b>(+223.42%)</b></td><td>103082.20 (+0.13%)</td><td>102940.22 (+0.02%)</td><td>102911.00 (-0.00%)</td><td>102878.60 (-0.00%)</td><td>81.05 <b>(+223.67%)</b></td><td>667.97 (+0.00%)</td><td>667.57 (-0.02%)</td><td>667.76 (+0.00%)</td><td>666.65 (-0.13%)</td><td>0.53 <b>(+223.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102951.40 (n/a)</td><td>102914.54 (n/a)</td><td>102914.50 (n/a)</td><td>102881.00 (n/a)</td><td>25.04 (n/a)</td><td>667.95 (n/a)</td><td>667.73 (n/a)</td><td>667.73 (n/a)</td><td>667.49 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.70 (+0.20%)</td><td>0.70 (+0.09%)</td><td>0.70 (+0.06%)</td><td>0.70 (+0.05%)</td><td>0.00 <b>(+81.26%)</b></td><td>107992.60 (-0.05%)</td><td>107866.86 (-0.09%)</td><td>107878.00 (-0.06%)</td><td>107664.40 (-0.20%)</td><td>122.51 <b>(+80.77%)</b></td><td>638.27 (+0.20%)</td><td>637.08 (+0.09%)</td><td>637.01 (+0.06%)</td><td>636.34 (+0.05%)</td><td>0.72 <b>(+81.25%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108044.10 (n/a)</td><td>107962.18 (n/a)</td><td>107940.30 (n/a)</td><td>107876.80 (n/a)</td><td>67.77 (n/a)</td><td>637.02 (n/a)</td><td>636.51 (n/a)</td><td>636.64 (n/a)</td><td>636.03 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>4.35 (+16.24%)</td><td>3.93 <b>(+23.04%)</b></td><td>3.89 <b>(+25.07%)</b></td><td>3.57 <b>(+22.11%)</b></td><td>0.29 (-10.35%)</td><td>2259.40 (-18.11%)</td><td>2057.52 (-18.98%)</td><td>2070.30 <b>(-20.05%)</b></td><td>1855.00 (-13.97%)</td><td>148.62 <b>(-35.98%)</b></td><td>1139.60 (+16.24%)</td><td>1031.74 <b>(+23.04%)</b></td><td>1021.05 <b>(+25.07%)</b></td><td>935.63 <b>(+22.11%)</b></td><td>75.15 (-10.35%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.74 (n/a)</td><td>3.20 (n/a)</td><td>3.11 (n/a)</td><td>2.92 (n/a)</td><td>0.32 (n/a)</td><td>2759.00 (n/a)</td><td>2539.52 (n/a)</td><td>2589.40 (n/a)</td><td>2156.20 (n/a)</td><td>232.15 (n/a)</td><td>980.40 (n/a)</td><td>838.53 (n/a)</td><td>816.39 (n/a)</td><td>766.19 (n/a)</td><td>83.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.34 (-15.48%)</td><td>0.32 (-10.36%)</td><td>0.32 (-6.51%)</td><td>0.29 (-11.53%)</td><td>0.03 (-17.32%)</td><td>4364.10 (+13.03%)</td><td>3975.80 (+11.51%)</td><td>3849.30 (+6.96%)</td><td>3622.20 (+18.31%)</td><td>358.09 (+12.42%)</td><td>18.53 (-15.48%)</td><td>16.99 (-10.36%)</td><td>17.43 (-6.51%)</td><td>15.38 (-11.53%)</td><td>1.50 (-17.32%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>3860.90 (n/a)</td><td>3565.44 (n/a)</td><td>3598.70 (n/a)</td><td>3061.60 (n/a)</td><td>318.52 (n/a)</td><td>21.92 (n/a)</td><td>18.95 (n/a)</td><td>18.65 (n/a)</td><td>17.38 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.05 (+0.72%)</td><td>4.96 (+7.83%)</td><td>5.07 (+6.74%)</td><td>3.24 (-9.08%)</td><td>1.14 (+11.99%)</td><td>2051.70 (+9.98%)</td><td>1410.16 (-6.14%)</td><td>1313.20 (-6.31%)</td><td>1098.80 (-0.72%)</td><td>387.38 (+18.14%)</td><td>1870.35 (+0.72%)</td><td>1533.62 (+7.83%)</td><td>1565.09 (+6.74%)</td><td>1001.69 (-9.08%)</td><td>352.40 (+11.99%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.01 (n/a)</td><td>4.60 (n/a)</td><td>4.75 (n/a)</td><td>3.57 (n/a)</td><td>1.02 (n/a)</td><td>1865.50 (n/a)</td><td>1502.46 (n/a)</td><td>1401.70 (n/a)</td><td>1106.80 (n/a)</td><td>327.89 (n/a)</td><td>1856.93 (n/a)</td><td>1422.25 (n/a)</td><td>1466.23 (n/a)</td><td>1101.68 (n/a)</td><td>314.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-2.17%)</td><td>0.21 (+6.90%)</td><td>0.23 (+12.61%)</td><td>0.18 <b>(+35.70%)</b></td><td>0.03 <b>(-32.13%)</b></td><td>0.24 (-2.17%)</td><td>0.21 (+6.90%)</td><td>0.22 (+12.61%)</td><td>0.18 <b>(+35.70%)</b></td><td>0.03 <b>(-32.13%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.44 (+0.86%)</td><td>12.66 (+3.05%)</td><td>13.28 (+0.87%)</td><td>11.50 (+11.70%)</td><td>0.99 <b>(-27.48%)</b></td><td>13.43 (+0.86%)</td><td>12.65 (+3.05%)</td><td>13.27 (+0.87%)</td><td>11.49 (+11.70%)</td><td>0.99 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.33 (n/a)</td><td>12.28 (n/a)</td><td>13.17 (n/a)</td><td>10.29 (n/a)</td><td>1.37 (n/a)</td><td>13.32 (n/a)</td><td>12.27 (n/a)</td><td>13.16 (n/a)</td><td>10.28 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>24.77 (-3.59%)</td><td>24.12 (-1.37%)</td><td>24.20 (-1.65%)</td><td>23.37 (+0.36%)</td><td>0.54 <b>(-38.97%)</b></td><td>24.76 (-3.59%)</td><td>24.10 (-1.37%)</td><td>24.19 (-1.65%)</td><td>23.36 (+0.36%)</td><td>0.54 <b>(-38.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>25.69 (n/a)</td><td>24.45 (n/a)</td><td>24.61 (n/a)</td><td>23.28 (n/a)</td><td>0.88 (n/a)</td><td>25.68 (n/a)</td><td>24.44 (n/a)</td><td>24.59 (n/a)</td><td>23.27 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>41.28 (-1.31%)</td><td>39.93 (-1.51%)</td><td>40.09 (-1.42%)</td><td>38.07 (-2.76%)</td><td>1.21 (-0.59%)</td><td>41.25 (-1.31%)</td><td>39.90 (-1.51%)</td><td>40.07 (-1.42%)</td><td>38.05 (-2.76%)</td><td>1.21 (-0.59%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>41.83 (n/a)</td><td>40.54 (n/a)</td><td>40.67 (n/a)</td><td>39.15 (n/a)</td><td>1.22 (n/a)</td><td>41.80 (n/a)</td><td>40.52 (n/a)</td><td>40.65 (n/a)</td><td>39.13 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>45.71 (+4.15%)</td><td>43.52 (+1.81%)</td><td>43.47 (+1.44%)</td><td>40.60 (-0.87%)</td><td>2.19 <b>(+98.99%)</b></td><td>45.68 (+4.15%)</td><td>43.49 (+1.81%)</td><td>43.45 (+1.44%)</td><td>40.58 (-0.87%)</td><td>2.18 <b>(+98.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>43.89 (n/a)</td><td>42.74 (n/a)</td><td>42.85 (n/a)</td><td>40.96 (n/a)</td><td>1.10 (n/a)</td><td>43.86 (n/a)</td><td>42.72 (n/a)</td><td>42.83 (n/a)</td><td>40.93 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.53 (+0.69%)</td><td>12.25 (-2.66%)</td><td>13.42 (+1.09%)</td><td>9.19 (-12.36%)</td><td>1.89 <b>(+50.53%)</b></td><td>13.52 (+0.69%)</td><td>12.24 (-2.66%)</td><td>13.41 (+1.09%)</td><td>9.18 (-12.36%)</td><td>1.89 <b>(+50.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.44 (n/a)</td><td>12.58 (n/a)</td><td>13.27 (n/a)</td><td>10.49 (n/a)</td><td>1.25 (n/a)</td><td>13.43 (n/a)</td><td>12.58 (n/a)</td><td>13.27 (n/a)</td><td>10.48 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>25.16 (-0.49%)</td><td>24.61 (+2.10%)</td><td>24.42 (+2.76%)</td><td>23.92 (+0.86%)</td><td>0.52 <b>(-21.49%)</b></td><td>25.14 (-0.49%)</td><td>24.59 (+2.10%)</td><td>24.41 (+2.76%)</td><td>23.91 (+0.86%)</td><td>0.52 <b>(-21.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>25.28 (n/a)</td><td>24.10 (n/a)</td><td>23.77 (n/a)</td><td>23.72 (n/a)</td><td>0.67 (n/a)</td><td>25.26 (n/a)</td><td>24.09 (n/a)</td><td>23.75 (n/a)</td><td>23.70 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>42.87 (+5.93%)</td><td>39.72 (+0.85%)</td><td>39.22 (+0.03%)</td><td>38.27 (-0.57%)</td><td>1.89 <b>(+120.06%)</b></td><td>42.85 (+5.93%)</td><td>39.70 (+0.85%)</td><td>39.20 (+0.03%)</td><td>38.24 (-0.57%)</td><td>1.89 <b>(+120.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>40.47 (n/a)</td><td>39.39 (n/a)</td><td>39.21 (n/a)</td><td>38.49 (n/a)</td><td>0.86 (n/a)</td><td>40.45 (n/a)</td><td>39.36 (n/a)</td><td>39.19 (n/a)</td><td>38.46 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>47.19 (+9.48%)</td><td>44.27 (+4.35%)</td><td>43.58 (+1.78%)</td><td>42.10 (+1.52%)</td><td>1.97 <b>(+167.62%)</b></td><td>47.16 (+9.48%)</td><td>44.24 (+4.35%)</td><td>43.55 (+1.78%)</td><td>42.07 (+1.52%)</td><td>1.97 <b>(+167.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>43.10 (n/a)</td><td>42.43 (n/a)</td><td>42.82 (n/a)</td><td>41.47 (n/a)</td><td>0.74 (n/a)</td><td>43.08 (n/a)</td><td>42.40 (n/a)</td><td>42.79 (n/a)</td><td>41.44 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.34 (+5.51%)</td><td>8.96 (+7.12%)</td><td>9.05 (+6.76%)</td><td>8.39 (+5.67%)</td><td>0.37 (+1.20%)</td><td>9.32 (+5.51%)</td><td>8.95 (+7.12%)</td><td>9.03 (+6.76%)</td><td>8.38 (+5.67%)</td><td>0.37 (+1.20%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.85 (n/a)</td><td>8.37 (n/a)</td><td>8.47 (n/a)</td><td>7.94 (n/a)</td><td>0.36 (n/a)</td><td>8.83 (n/a)</td><td>8.35 (n/a)</td><td>8.46 (n/a)</td><td>7.93 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.89 (-4.47%)</td><td>0.78 (-4.77%)</td><td>0.74 (-8.43%)</td><td>0.71 (-2.29%)</td><td>0.08 (+5.76%)</td><td>0.87 (-4.47%)</td><td>0.77 (-4.77%)</td><td>0.73 (-8.43%)</td><td>0.70 (-2.29%)</td><td>0.08 (+5.76%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.07 (n/a)</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.12 (-7.45%)</td><td>1.02 (-1.93%)</td><td>1.07 (+6.68%)</td><td>0.91 (+2.41%)</td><td>0.10 <b>(-22.03%)</b></td><td>1.11 (-7.45%)</td><td>1.01 (-1.93%)</td><td>1.06 (+6.68%)</td><td>0.90 (+2.41%)</td><td>0.10 <b>(-22.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.21 (n/a)</td><td>1.04 (n/a)</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.13 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td><td>0.99 (n/a)</td><td>0.88 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>16.50 (+7.91%)</td><td>15.05 (+1.70%)</td><td>14.66 (-2.38%)</td><td>13.63 (-4.14%)</td><td>1.19 <b>(+140.83%)</b></td><td>16.31 (+7.91%)</td><td>14.88 (+1.70%)</td><td>14.49 (-2.38%)</td><td>13.47 (-4.14%)</td><td>1.18 <b>(+140.83%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>15.29 (n/a)</td><td>14.80 (n/a)</td><td>15.02 (n/a)</td><td>14.22 (n/a)</td><td>0.49 (n/a)</td><td>15.12 (n/a)</td><td>14.63 (n/a)</td><td>14.85 (n/a)</td><td>14.06 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>11.88 (+1.93%)</td><td>11.54 (-0.05%)</td><td>11.80 (+2.25%)</td><td>10.49 (-8.33%)</td><td>0.59 <b>(+601.60%)</b></td><td>11.67 (+1.93%)</td><td>11.34 (-0.05%)</td><td>11.60 (+2.25%)</td><td>10.30 (-8.33%)</td><td>0.58 <b>(+601.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>11.66 (n/a)</td><td>11.55 (n/a)</td><td>11.54 (n/a)</td><td>11.44 (n/a)</td><td>0.08 (n/a)</td><td>11.45 (n/a)</td><td>11.35 (n/a)</td><td>11.34 (n/a)</td><td>11.24 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.10 (-1.17%)</td><td>7.54 (+3.06%)</td><td>7.70 (+5.66%)</td><td>6.64 (+2.97%)</td><td>0.57 <b>(-20.28%)</b></td><td>7.96 (-1.17%)</td><td>7.41 (+3.06%)</td><td>7.57 (+5.66%)</td><td>6.52 (+2.97%)</td><td>0.56 <b>(-20.28%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.20 (n/a)</td><td>7.32 (n/a)</td><td>7.29 (n/a)</td><td>6.44 (n/a)</td><td>0.72 (n/a)</td><td>8.06 (n/a)</td><td>7.19 (n/a)</td><td>7.16 (n/a)</td><td>6.33 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.90 (-1.05%)</td><td>5.20 (-2.49%)</td><td>4.99 (-11.41%)</td><td>4.67 (+3.42%)</td><td>0.50 (-16.11%)</td><td>5.81 (-1.05%)</td><td>5.12 (-2.49%)</td><td>4.91 (-11.41%)</td><td>4.59 (+3.42%)</td><td>0.49 (-16.11%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.97 (n/a)</td><td>5.34 (n/a)</td><td>5.63 (n/a)</td><td>4.51 (n/a)</td><td>0.60 (n/a)</td><td>5.87 (n/a)</td><td>5.25 (n/a)</td><td>5.54 (n/a)</td><td>4.44 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.50 (n/a)</td><td>162.22 (n/a)</td><td>149.80 (n/a)</td><td>146.20 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>180.60 (n/a)</td><td>159.70 (n/a)</td><td>165.60 (n/a)</td><td>106.50 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>350.40 (n/a)</td><td>221.48 (n/a)</td><td>203.50 (n/a)</td><td>147.70 (n/a)</td><td>75.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>332.50 (n/a)</td><td>196.72 (n/a)</td><td>163.40 (n/a)</td><td>152.00 (n/a)</td><td>76.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>184.20 (n/a)</td><td>186.40 (n/a)</td><td>147.50 (n/a)</td><td>27.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>179.88 (n/a)</td><td>182.30 (n/a)</td><td>164.40 (n/a)</td><td>10.65 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>274.40 (n/a)</td><td>194.84 (n/a)</td><td>191.30 (n/a)</td><td>152.20 (n/a)</td><td>47.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.60 (n/a)</td><td>219.48 (n/a)</td><td>216.90 (n/a)</td><td>170.20 (n/a)</td><td>41.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>174.86 (n/a)</td><td>177.90 (n/a)</td><td>125.90 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>159.64 (n/a)</td><td>149.80 (n/a)</td><td>133.10 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.20 (n/a)</td><td>153.40 (n/a)</td><td>160.30 (n/a)</td><td>131.20 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>172.40 (n/a)</td><td>177.80 (n/a)</td><td>148.10 (n/a)</td><td>17.78 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>177.64 (n/a)</td><td>174.30 (n/a)</td><td>145.20 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.20 (n/a)</td><td>187.72 (n/a)</td><td>167.10 (n/a)</td><td>130.20 (n/a)</td><td>54.69 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.50 (n/a)</td><td>181.62 (n/a)</td><td>180.90 (n/a)</td><td>130.30 (n/a)</td><td>53.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>187.84 (n/a)</td><td>201.20 (n/a)</td><td>133.80 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>179.92 (n/a)</td><td>191.40 (n/a)</td><td>130.60 (n/a)</td><td>36.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.60 (n/a)</td><td>189.46 (n/a)</td><td>178.90 (n/a)</td><td>135.10 (n/a)</td><td>42.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.90 (n/a)</td><td>187.00 (n/a)</td><td>183.20 (n/a)</td><td>147.80 (n/a)</td><td>38.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>174.20 (n/a)</td><td>171.70 (n/a)</td><td>156.30 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.70 (n/a)</td><td>183.62 (n/a)</td><td>189.80 (n/a)</td><td>137.00 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.90 (n/a)</td><td>193.58 (n/a)</td><td>182.40 (n/a)</td><td>155.90 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>190.96 (n/a)</td><td>183.70 (n/a)</td><td>171.00 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>235.16 (n/a)</td><td>225.50 (n/a)</td><td>191.00 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-10.46%)</td><td>0.17 (-3.60%)</td><td>0.15 (-3.31%)</td><td>0.13 (-11.37%)</td><td>0.03 (-13.58%)</td><td>256.70 (+12.84%)</td><td>204.06 (+3.55%)</td><td>213.80 (+3.38%)</td><td>157.00 (+11.66%)</td><td>38.21 (+9.68%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>227.50 (n/a)</td><td>197.06 (n/a)</td><td>206.80 (n/a)</td><td>140.60 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>187.54 (n/a)</td><td>188.50 (n/a)</td><td>169.10 (n/a)</td><td>10.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>224.80 (n/a)</td><td>188.16 (n/a)</td><td>188.00 (n/a)</td><td>155.60 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>281.40 (n/a)</td><td>212.24 (n/a)</td><td>189.40 (n/a)</td><td>185.90 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.60 (n/a)</td><td>175.40 (n/a)</td><td>182.60 (n/a)</td><td>150.40 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>241.10 (n/a)</td><td>199.70 (n/a)</td><td>197.50 (n/a)</td><td>172.10 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.00 (n/a)</td><td>182.08 (n/a)</td><td>186.50 (n/a)</td><td>152.20 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>332.10 (n/a)</td><td>236.94 (n/a)</td><td>219.00 (n/a)</td><td>191.20 (n/a)</td><td>55.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-5.17%)</td><td>0.02 (-8.07%)</td><td>0.02 (-9.43%)</td><td>0.02 (+7.94%)</td><td>0.00 <b>(-25.08%)</b></td><td>207.80 (-7.36%)</td><td>173.52 (+6.87%)</td><td>175.90 (+10.42%)</td><td>136.30 (+5.41%)</td><td>29.22 <b>(-25.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>162.36 (n/a)</td><td>159.30 (n/a)</td><td>129.30 (n/a)</td><td>38.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-12.60%)</td><td>0.02 (-1.63%)</td><td>0.02 (+1.87%)</td><td>0.02 (+10.39%)</td><td>0.00 <b>(-56.10%)</b></td><td>190.50 (-9.42%)</td><td>171.06 (-0.66%)</td><td>169.30 (-1.80%)</td><td>151.80 (+14.48%)</td><td>14.58 <b>(-54.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.30 (n/a)</td><td>172.20 (n/a)</td><td>172.40 (n/a)</td><td>132.60 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-12.68%)</td><td>0.03 (+9.35%)</td><td>0.03 (+11.51%)</td><td>0.02 <b>(+60.98%)</b></td><td>0.00 <b>(-45.72%)</b></td><td>202.30 <b>(-37.89%)</b></td><td>153.56 (-17.07%)</td><td>143.30 (-10.33%)</td><td>125.80 (+14.47%)</td><td>30.30 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>325.70 (n/a)</td><td>185.16 (n/a)</td><td>159.80 (n/a)</td><td>109.90 (n/a)</td><td>82.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 <b>(+21.77%)</b></td><td>0.03 (+16.42%)</td><td>0.03 (+0.21%)</td><td>0.02 <b>(+91.57%)</b></td><td>0.00 <b>(-31.72%)</b></td><td>187.60 <b>(-47.82%)</b></td><td>162.74 <b>(-21.23%)</b></td><td>161.70 (-0.25%)</td><td>122.20 (-17.88%)</td><td>25.59 <b>(-71.25%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>359.50 (n/a)</td><td>206.60 (n/a)</td><td>162.10 (n/a)</td><td>148.80 (n/a)</td><td>89.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-4.36%)</td><td>0.02 (-4.56%)</td><td>0.02 (-3.73%)</td><td>0.02 (-5.87%)</td><td>0.00 (-0.44%)</td><td>204.10 (+6.25%)</td><td>176.94 (+4.86%)</td><td>170.00 (+3.91%)</td><td>158.80 (+4.54%)</td><td>17.62 (+11.09%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>168.74 (n/a)</td><td>163.60 (n/a)</td><td>151.90 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-15.76%)</td><td>0.02 (-10.16%)</td><td>0.02 (-0.39%)</td><td>0.02 (-19.90%)</td><td>0.00 (-13.55%)</td><td>260.60 <b>(+24.87%)</b></td><td>205.92 (+11.55%)</td><td>198.90 (+0.40%)</td><td>175.00 (+18.64%)</td><td>33.17 <b>(+31.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>184.60 (n/a)</td><td>198.10 (n/a)</td><td>147.50 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-7.69%)</td><td>0.02 (-7.03%)</td><td>0.02 (-10.42%)</td><td>0.02 (-6.93%)</td><td>0.00 (-13.15%)</td><td>215.40 (+7.43%)</td><td>195.04 (+7.42%)</td><td>203.00 (+11.60%)</td><td>170.80 (+8.31%)</td><td>18.62 (-0.84%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.50 (n/a)</td><td>181.56 (n/a)</td><td>181.90 (n/a)</td><td>157.70 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-5.80%)</td><td>0.02 (-4.13%)</td><td>0.02 (-6.31%)</td><td>0.02 (+6.97%)</td><td>0.00 <b>(-27.76%)</b></td><td>242.30 (-6.48%)</td><td>214.10 (+3.36%)</td><td>219.60 (+6.71%)</td><td>185.40 (+6.12%)</td><td>23.24 <b>(-29.13%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.10 (n/a)</td><td>207.14 (n/a)</td><td>205.80 (n/a)</td><td>174.70 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (-9.10%)</td><td>0.05 (-14.57%)</td><td>0.05 <b>(-24.18%)</b></td><td>0.04 <b>(-22.00%)</b></td><td>0.01 <b>(+33.04%)</b></td><td>206.20 <b>(+28.23%)</b></td><td>157.48 <b>(+20.77%)</b></td><td>167.10 <b>(+31.89%)</b></td><td>114.80 (+10.07%)</td><td>39.85 <b>(+78.68%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>160.80 (n/a)</td><td>130.40 (n/a)</td><td>126.70 (n/a)</td><td>104.30 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-23.05%)</b></td><td>0.04 (-18.86%)</td><td>0.05 (-17.57%)</td><td>0.04 <b>(-21.58%)</b></td><td>0.01 <b>(-26.93%)</b></td><td>231.50 <b>(+27.55%)</b></td><td>186.54 <b>(+23.03%)</b></td><td>177.70 <b>(+21.30%)</b></td><td>160.60 <b>(+29.94%)</b></td><td>27.28 <b>(+23.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.50 (n/a)</td><td>151.62 (n/a)</td><td>146.50 (n/a)</td><td>123.60 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-17.16%)</td><td>0.05 (-16.83%)</td><td>0.05 (-19.60%)</td><td>0.04 (-12.70%)</td><td>0.01 <b>(-27.36%)</b></td><td>188.90 (+14.55%)</td><td>163.42 (+19.70%)</td><td>164.60 <b>(+24.32%)</b></td><td>139.20 <b>(+20.73%)</b></td><td>20.00 (-0.02%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.90 (n/a)</td><td>136.52 (n/a)</td><td>132.40 (n/a)</td><td>115.30 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+12.53%)</td><td>0.05 (-5.37%)</td><td>0.05 (-16.60%)</td><td>0.04 (-13.71%)</td><td>0.01 <b>(+62.46%)</b></td><td>207.80 (+15.90%)</td><td>168.26 (+8.48%)</td><td>177.80 (+19.89%)</td><td>111.30 (-11.17%)</td><td>35.59 <b>(+55.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.30 (n/a)</td><td>155.10 (n/a)</td><td>148.30 (n/a)</td><td>125.30 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (+15.23%)</td><td>0.05 (+1.21%)</td><td>0.05 (-6.72%)</td><td>0.04 (-9.49%)</td><td>0.01 <b>(+137.50%)</b></td><td>196.30 (+10.47%)</td><td>165.60 (+1.46%)</td><td>175.80 (+7.20%)</td><td>128.60 (-13.23%)</td><td>32.42 <b>(+126.90%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>163.22 (n/a)</td><td>164.00 (n/a)</td><td>148.20 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+0.02%)</td><td>0.05 (+2.28%)</td><td>0.04 (-1.52%)</td><td>0.04 (-3.44%)</td><td>0.01 (+0.85%)</td><td>230.10 (+3.56%)</td><td>176.94 (-2.06%)</td><td>184.80 (+1.54%)</td><td>123.90 (+0.00%)</td><td>40.23 (+3.30%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>180.66 (n/a)</td><td>182.00 (n/a)</td><td>123.90 (n/a)</td><td>38.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-15.85%)</td><td>0.05 (+0.98%)</td><td>0.05 (+11.14%)</td><td>0.04 <b>(+25.94%)</b></td><td>0.01 <b>(-48.94%)</b></td><td>211.30 <b>(-20.59%)</b></td><td>176.34 (-4.81%)</td><td>163.10 (-10.04%)</td><td>158.60 (+18.80%)</td><td>23.34 <b>(-53.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.10 (n/a)</td><td>185.26 (n/a)</td><td>181.30 (n/a)</td><td>133.50 (n/a)</td><td>50.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-13.95%)</td><td>0.05 (-3.68%)</td><td>0.04 (-5.85%)</td><td>0.04 (+1.83%)</td><td>0.01 <b>(-30.58%)</b></td><td>205.40 (-1.82%)</td><td>179.72 (+2.50%)</td><td>182.80 (+6.22%)</td><td>152.20 (+16.27%)</td><td>24.88 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>175.34 (n/a)</td><td>172.10 (n/a)</td><td>130.90 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-22.14%)</b></td><td>0.04 (-8.75%)</td><td>0.04 (-8.05%)</td><td>0.04 (+15.32%)</td><td>0.01 <b>(-54.75%)</b></td><td>214.20 (-13.28%)</td><td>193.10 (+5.68%)</td><td>202.10 (+8.77%)</td><td>165.00 <b>(+28.40%)</b></td><td>22.58 <b>(-49.19%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>182.72 (n/a)</td><td>185.80 (n/a)</td><td>128.50 (n/a)</td><td>44.44 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (+10.53%)</td><td>0.04 (+5.47%)</td><td>0.04 (-3.85%)</td><td>0.03 <b>(+59.17%)</b></td><td>0.01 <b>(-29.57%)</b></td><td>236.00 <b>(-37.17%)</b></td><td>210.86 (-10.30%)</td><td>219.60 (+4.03%)</td><td>156.40 (-9.54%)</td><td>31.23 <b>(-62.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>375.60 (n/a)</td><td>235.08 (n/a)</td><td>211.10 (n/a)</td><td>172.90 (n/a)</td><td>82.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (+2.58%)</td><td>0.11 (+4.03%)</td><td>0.10 (+1.79%)</td><td>0.09 (+14.72%)</td><td>0.02 (-17.43%)</td><td>173.20 (-12.83%)</td><td>157.30 (-5.01%)</td><td>165.00 (-1.79%)</td><td>122.30 (-2.47%)</td><td>20.43 <b>(-31.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>165.60 (n/a)</td><td>168.00 (n/a)</td><td>125.40 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (+6.56%)</td><td>0.11 (+4.70%)</td><td>0.10 (+9.28%)</td><td>0.09 (+10.54%)</td><td>0.02 (-1.10%)</td><td>176.70 (-9.52%)</td><td>157.98 (-4.87%)</td><td>162.10 (-8.47%)</td><td>120.50 (-6.15%)</td><td>21.82 (-17.75%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>166.06 (n/a)</td><td>177.10 (n/a)</td><td>128.40 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-1.61%)</td><td>0.10 (-8.58%)</td><td>0.10 (-6.82%)</td><td>0.08 (-16.06%)</td><td>0.02 (+14.08%)</td><td>206.60 (+19.15%)</td><td>164.64 (+10.27%)</td><td>161.10 (+7.33%)</td><td>129.30 (+1.65%)</td><td>27.72 <b>(+39.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>173.40 (n/a)</td><td>149.30 (n/a)</td><td>150.10 (n/a)</td><td>127.20 (n/a)</td><td>19.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-18.88%)</td><td>0.09 (-5.82%)</td><td>0.09 (-2.50%)</td><td>0.08 (+16.56%)</td><td>0.01 <b>(-64.99%)</b></td><td>203.00 (-14.20%)</td><td>179.90 (-0.10%)</td><td>187.80 (+2.57%)</td><td>154.40 <b>(+23.32%)</b></td><td>19.34 <b>(-62.68%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>236.60 (n/a)</td><td>180.08 (n/a)</td><td>183.10 (n/a)</td><td>125.20 (n/a)</td><td>51.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-4.44%)</td><td>0.10 (+3.95%)</td><td>0.12 (+8.17%)</td><td>0.07 (+2.62%)</td><td>0.03 (-4.81%)</td><td>234.00 (-2.58%)</td><td>169.40 (-4.42%)</td><td>141.10 (-7.54%)</td><td>130.60 (+4.65%)</td><td>46.66 (-6.95%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.20 (n/a)</td><td>177.24 (n/a)</td><td>152.60 (n/a)</td><td>124.80 (n/a)</td><td>50.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-14.56%)</td><td>0.09 (-7.32%)</td><td>0.09 (-11.64%)</td><td>0.07 (+9.49%)</td><td>0.01 <b>(-39.35%)</b></td><td>219.00 (-8.67%)</td><td>177.50 (+5.25%)</td><td>177.00 (+13.17%)</td><td>153.80 (+17.05%)</td><td>25.79 <b>(-38.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.80 (n/a)</td><td>168.64 (n/a)</td><td>156.40 (n/a)</td><td>131.40 (n/a)</td><td>41.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (-4.67%)</td><td>0.08 (-5.65%)</td><td>0.08 (-12.63%)</td><td>0.08 (+14.84%)</td><td>0.01 <b>(-37.69%)</b></td><td>216.10 (-12.93%)</td><td>197.72 (+3.74%)</td><td>200.00 (+14.42%)</td><td>160.10 (+4.85%)</td><td>22.36 <b>(-44.01%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.20 (n/a)</td><td>190.60 (n/a)</td><td>174.80 (n/a)</td><td>152.70 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-10.57%)</td><td>0.08 (-17.29%)</td><td>0.07 <b>(-22.92%)</b></td><td>0.07 (-3.74%)</td><td>0.01 <b>(-27.76%)</b></td><td>232.80 (+3.88%)</td><td>214.76 <b>(+20.15%)</b></td><td>220.50 <b>(+29.71%)</b></td><td>179.10 (+11.80%)</td><td>20.68 <b>(-20.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>178.74 (n/a)</td><td>170.00 (n/a)</td><td>160.20 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (-13.46%)</td><td>0.18 (-12.17%)</td><td>0.18 (-19.33%)</td><td>0.15 (-6.58%)</td><td>0.02 <b>(-40.12%)</b></td><td>219.70 (+7.01%)</td><td>187.30 (+12.52%)</td><td>183.40 <b>(+24.00%)</b></td><td>166.60 (+15.53%)</td><td>21.14 <b>(-24.90%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.30 (n/a)</td><td>166.46 (n/a)</td><td>147.90 (n/a)</td><td>144.20 (n/a)</td><td>28.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 <b>(+20.22%)</b></td><td>0.23 (+8.31%)</td><td>0.22 (+8.87%)</td><td>0.18 (-7.21%)</td><td>0.05 <b>(+85.81%)</b></td><td>185.80 (+7.77%)</td><td>146.92 (-5.65%)</td><td>146.80 (-8.14%)</td><td>106.20 (-16.84%)</td><td>28.51 <b>(+65.67%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>172.40 (n/a)</td><td>155.72 (n/a)</td><td>159.80 (n/a)</td><td>127.70 (n/a)</td><td>17.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (+0.53%)</td><td>0.20 (+12.82%)</td><td>0.18 (+13.97%)</td><td>0.17 <b>(+74.91%)</b></td><td>0.04 <b>(-35.54%)</b></td><td>198.00 <b>(-42.82%)</b></td><td>170.24 (-19.09%)</td><td>186.10 (-12.26%)</td><td>123.70 (-0.48%)</td><td>32.15 <b>(-62.73%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>346.30 (n/a)</td><td>210.40 (n/a)</td><td>212.10 (n/a)</td><td>124.30 (n/a)</td><td>86.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (-4.32%)</td><td>0.20 (-1.83%)</td><td>0.20 (+0.92%)</td><td>0.18 (-1.53%)</td><td>0.02 (-19.41%)</td><td>183.50 (+1.55%)</td><td>165.08 (+1.51%)</td><td>162.80 (-0.91%)</td><td>143.40 (+4.52%)</td><td>15.65 (-15.28%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>180.70 (n/a)</td><td>162.62 (n/a)</td><td>164.30 (n/a)</td><td>137.20 (n/a)</td><td>18.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 <b>(-26.68%)</b></td><td>0.14 <b>(-26.10%)</b></td><td>0.14 <b>(-35.00%)</b></td><td>0.13 (-17.18%)</td><td>0.02 <b>(-53.99%)</b></td><td>251.30 <b>(+20.70%)</b></td><td>231.24 <b>(+33.19%)</b></td><td>241.70 <b>(+53.85%)</b></td><td>200.10 <b>(+36.40%)</b></td><td>23.21 <b>(-24.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.20 (n/a)</td><td>173.62 (n/a)</td><td>157.10 (n/a)</td><td>146.70 (n/a)</td><td>30.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (-9.36%)</td><td>0.17 (-9.15%)</td><td>0.17 <b>(-20.30%)</b></td><td>0.15 <b>(+21.89%)</b></td><td>0.02 <b>(-54.81%)</b></td><td>212.40 (-17.96%)</td><td>191.96 (+6.23%)</td><td>197.20 <b>(+25.53%)</b></td><td>163.90 (+10.37%)</td><td>18.96 <b>(-59.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>258.90 (n/a)</td><td>180.70 (n/a)</td><td>157.10 (n/a)</td><td>148.50 (n/a)</td><td>46.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (-13.83%)</td><td>0.13 (-19.74%)</td><td>0.14 (-13.00%)</td><td>0.10 <b>(-36.00%)</b></td><td>0.03 <b>(+122.22%)</b></td><td>336.80 <b>(+56.29%)</b></td><td>262.80 <b>(+29.10%)</b></td><td>240.00 (+14.94%)</td><td>207.80 (+16.02%)</td><td>59.95 <b>(+306.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>203.56 (n/a)</td><td>208.80 (n/a)</td><td>179.10 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-16.74%)</td><td>0.02 (-9.90%)</td><td>0.02 <b>(-21.05%)</b></td><td>0.02 (+6.96%)</td><td>0.00 <b>(-39.49%)</b></td><td>218.80 (-6.50%)</td><td>182.16 (+7.56%)</td><td>189.20 <b>(+26.64%)</b></td><td>146.20 <b>(+20.13%)</b></td><td>29.58 <b>(-34.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>169.36 (n/a)</td><td>149.40 (n/a)</td><td>121.70 (n/a)</td><td>44.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+0.48%)</td><td>0.02 (-5.98%)</td><td>0.02 <b>(-20.20%)</b></td><td>0.02 (-4.14%)</td><td>0.01 <b>(+45.19%)</b></td><td>207.40 (+4.33%)</td><td>171.62 (+8.57%)</td><td>189.20 <b>(+25.30%)</b></td><td>130.50 (-0.53%)</td><td>36.54 <b>(+44.33%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>158.08 (n/a)</td><td>151.00 (n/a)</td><td>131.20 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-1.88%)</td><td>0.02 (-3.71%)</td><td>0.02 (-9.82%)</td><td>0.02 (+5.24%)</td><td>0.00 (-7.09%)</td><td>253.70 (-4.98%)</td><td>209.52 (+3.32%)</td><td>217.50 (+10.91%)</td><td>167.00 (+1.89%)</td><td>35.95 (-11.67%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>267.00 (n/a)</td><td>202.78 (n/a)</td><td>196.10 (n/a)</td><td>163.90 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-19.63%)</td><td>0.02 (-4.85%)</td><td>0.02 (-9.23%)</td><td>0.02 <b>(+27.35%)</b></td><td>0.00 <b>(-68.64%)</b></td><td>223.50 <b>(-21.47%)</b></td><td>199.36 (+0.17%)</td><td>194.20 (+10.15%)</td><td>182.50 <b>(+24.40%)</b></td><td>16.40 <b>(-69.87%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>284.60 (n/a)</td><td>199.02 (n/a)</td><td>176.30 (n/a)</td><td>146.70 (n/a)</td><td>54.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-7.98%)</td><td>0.03 (-11.00%)</td><td>0.03 (-9.49%)</td><td>0.02 (-16.77%)</td><td>0.00 (+14.50%)</td><td>200.40 <b>(+20.14%)</b></td><td>158.30 (+13.56%)</td><td>153.90 (+10.48%)</td><td>126.90 (+8.65%)</td><td>29.04 <b>(+49.97%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.80 (n/a)</td><td>139.40 (n/a)</td><td>139.30 (n/a)</td><td>116.80 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+12.22%)</td><td>0.03 <b>(+20.63%)</b></td><td>0.03 <b>(+40.76%)</b></td><td>0.02 (+7.08%)</td><td>0.00 (+7.20%)</td><td>189.90 (-6.59%)</td><td>148.46 (-17.28%)</td><td>142.70 <b>(-28.97%)</b></td><td>120.30 (-10.89%)</td><td>27.79 (-13.09%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.30 (n/a)</td><td>179.48 (n/a)</td><td>200.90 (n/a)</td><td>135.00 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-17.88%)</td><td>0.03 (-2.53%)</td><td>0.03 (+5.79%)</td><td>0.02 (+16.21%)</td><td>0.00 <b>(-53.30%)</b></td><td>185.40 (-13.93%)</td><td>153.80 (-3.10%)</td><td>141.50 (-5.48%)</td><td>134.30 <b>(+21.76%)</b></td><td>23.37 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>158.72 (n/a)</td><td>149.70 (n/a)</td><td>110.30 (n/a)</td><td>48.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+17.80%)</td><td>0.03 (+11.31%)</td><td>0.03 (+11.36%)</td><td>0.02 (+12.64%)</td><td>0.01 <b>(+42.82%)</b></td><td>189.20 (-11.22%)</td><td>146.20 (-9.07%)</td><td>133.90 (-10.19%)</td><td>113.80 (-15.14%)</td><td>32.03 (+4.78%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>160.78 (n/a)</td><td>149.10 (n/a)</td><td>134.10 (n/a)</td><td>30.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-1.62%)</td><td>0.03 (+10.88%)</td><td>0.02 <b>(+22.13%)</b></td><td>0.02 <b>(+34.70%)</b></td><td>0.00 <b>(-43.30%)</b></td><td>178.00 <b>(-25.74%)</b></td><td>165.78 (-14.33%)</td><td>175.00 (-18.11%)</td><td>127.50 (+1.67%)</td><td>21.56 <b>(-58.79%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>193.52 (n/a)</td><td>213.70 (n/a)</td><td>125.40 (n/a)</td><td>52.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-11.30%)</td><td>0.02 (-7.00%)</td><td>0.02 (-2.66%)</td><td>0.02 (+7.36%)</td><td>0.00 <b>(-49.05%)</b></td><td>189.20 (-6.84%)</td><td>168.96 (+3.62%)</td><td>171.40 (+2.70%)</td><td>134.50 (+12.74%)</td><td>20.72 <b>(-48.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>163.06 (n/a)</td><td>166.90 (n/a)</td><td>119.30 (n/a)</td><td>39.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-9.02%)</td><td>0.02 (-8.92%)</td><td>0.03 (+3.05%)</td><td>0.01 <b>(-28.18%)</b></td><td>0.01 <b>(+42.69%)</b></td><td>300.50 <b>(+39.25%)</b></td><td>195.88 (+15.81%)</td><td>156.20 (-2.98%)</td><td>143.30 (+9.89%)</td><td>67.13 <b>(+114.96%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>169.14 (n/a)</td><td>161.00 (n/a)</td><td>130.40 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-9.31%)</td><td>0.03 (+10.05%)</td><td>0.03 <b>(+26.54%)</b></td><td>0.02 <b>(+40.00%)</b></td><td>0.00 <b>(-51.88%)</b></td><td>184.40 <b>(-28.58%)</b></td><td>151.68 (-15.99%)</td><td>145.30 <b>(-20.99%)</b></td><td>124.50 (+10.27%)</td><td>23.86 <b>(-60.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.20 (n/a)</td><td>180.56 (n/a)</td><td>183.90 (n/a)</td><td>112.90 (n/a)</td><td>61.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-0.08%)</td><td>0.02 (+3.13%)</td><td>0.02 (-1.30%)</td><td>0.02 (+7.17%)</td><td>0.01 (-3.43%)</td><td>219.80 (-6.71%)</td><td>187.42 (-3.42%)</td><td>204.10 (+1.34%)</td><td>130.20 (+0.08%)</td><td>38.39 (-6.79%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>194.06 (n/a)</td><td>201.40 (n/a)</td><td>130.10 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+17.68%)</td><td>0.03 (+10.48%)</td><td>0.03 (-0.12%)</td><td>0.02 <b>(+24.32%)</b></td><td>0.01 <b>(+20.32%)</b></td><td>189.80 (-19.54%)</td><td>154.22 (-9.66%)</td><td>160.90 (+0.12%)</td><td>115.10 (-15.06%)</td><td>29.60 <b>(-22.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.90 (n/a)</td><td>170.72 (n/a)</td><td>160.70 (n/a)</td><td>135.50 (n/a)</td><td>38.10 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+17.78%)</td><td>0.02 (-3.36%)</td><td>0.02 <b>(-25.03%)</b></td><td>0.02 (-2.58%)</td><td>0.01 <b>(+67.55%)</b></td><td>223.30 (+2.62%)</td><td>190.68 (+6.93%)</td><td>219.40 <b>(+33.37%)</b></td><td>122.00 (-15.04%)</td><td>45.08 <b>(+46.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.60 (n/a)</td><td>178.32 (n/a)</td><td>164.50 (n/a)</td><td>143.60 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+0.92%)</td><td>0.02 (+0.20%)</td><td>0.02 (-10.24%)</td><td>0.02 (-13.98%)</td><td>0.01 <b>(+28.36%)</b></td><td>236.80 (+16.25%)</td><td>172.42 (+1.64%)</td><td>174.20 (+11.38%)</td><td>134.80 (-0.96%)</td><td>41.13 <b>(+41.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.70 (n/a)</td><td>169.64 (n/a)</td><td>156.40 (n/a)</td><td>136.10 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-1.99%)</td><td>0.05 (-1.08%)</td><td>0.06 (+3.38%)</td><td>0.05 (+6.65%)</td><td>0.01 <b>(-26.79%)</b></td><td>174.70 (-6.28%)</td><td>152.46 (-0.04%)</td><td>148.70 (-3.32%)</td><td>126.60 (+2.01%)</td><td>18.35 <b>(-29.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>152.52 (n/a)</td><td>153.80 (n/a)</td><td>124.10 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (-14.69%)</td><td>0.05 (-18.96%)</td><td>0.05 (-18.86%)</td><td>0.04 <b>(-31.62%)</b></td><td>0.01 <b>(+21.58%)</b></td><td>212.00 <b>(+46.31%)</b></td><td>161.02 <b>(+25.64%)</b></td><td>155.80 <b>(+23.26%)</b></td><td>124.20 (+17.28%)</td><td>31.83 <b>(+114.64%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>144.90 (n/a)</td><td>128.16 (n/a)</td><td>126.40 (n/a)</td><td>105.90 (n/a)</td><td>14.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 <b>(-22.76%)</b></td><td>0.04 <b>(-21.39%)</b></td><td>0.04 <b>(-21.89%)</b></td><td>0.03 <b>(-27.18%)</b></td><td>0.00 (-4.39%)</td><td>299.40 <b>(+37.34%)</b></td><td>237.42 <b>(+28.04%)</b></td><td>231.70 <b>(+28.01%)</b></td><td>208.30 <b>(+29.46%)</b></td><td>36.81 <b>(+70.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>185.42 (n/a)</td><td>181.00 (n/a)</td><td>160.90 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+9.77%)</td><td>0.04 (-7.23%)</td><td>0.04 (-11.97%)</td><td>0.03 <b>(-35.82%)</b></td><td>0.01 <b>(+92.95%)</b></td><td>304.90 <b>(+55.80%)</b></td><td>205.64 (+15.66%)</td><td>214.40 (+13.62%)</td><td>124.00 (-8.89%)</td><td>67.27 <b>(+173.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>177.80 (n/a)</td><td>188.70 (n/a)</td><td>136.10 (n/a)</td><td>24.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (-0.15%)</td><td>0.05 (-18.36%)</td><td>0.05 <b>(-25.41%)</b></td><td>0.03 <b>(-40.98%)</b></td><td>0.02 <b>(+63.84%)</b></td><td>289.40 <b>(+69.44%)</b></td><td>177.74 <b>(+33.08%)</b></td><td>173.20 <b>(+34.06%)</b></td><td>104.30 (+0.19%)</td><td>68.83 <b>(+181.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>133.56 (n/a)</td><td>129.20 (n/a)</td><td>104.10 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+8.12%)</td><td>0.05 (-7.75%)</td><td>0.04 <b>(-25.77%)</b></td><td>0.04 (-13.20%)</td><td>0.02 <b>(+83.40%)</b></td><td>227.20 (+15.21%)</td><td>177.46 (+14.43%)</td><td>201.10 <b>(+34.70%)</b></td><td>114.80 (-7.49%)</td><td>50.94 <b>(+91.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>155.08 (n/a)</td><td>149.30 (n/a)</td><td>124.10 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-22.61%)</b></td><td>0.04 <b>(-27.25%)</b></td><td>0.04 <b>(-26.93%)</b></td><td>0.03 <b>(-43.05%)</b></td><td>0.01 <b>(+34.26%)</b></td><td>310.90 <b>(+75.55%)</b></td><td>213.94 <b>(+44.13%)</b></td><td>205.10 <b>(+36.82%)</b></td><td>153.90 <b>(+29.22%)</b></td><td>62.94 <b>(+205.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.10 (n/a)</td><td>148.44 (n/a)</td><td>149.90 (n/a)</td><td>119.10 (n/a)</td><td>20.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (+3.74%)</td><td>0.05 (+6.87%)</td><td>0.05 (-4.26%)</td><td>0.04 <b>(+76.05%)</b></td><td>0.01 <b>(-38.54%)</b></td><td>209.00 <b>(-43.21%)</b></td><td>157.94 (-16.48%)</td><td>154.60 (+4.39%)</td><td>127.20 (-3.64%)</td><td>31.87 <b>(-68.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>368.00 (n/a)</td><td>189.10 (n/a)</td><td>148.10 (n/a)</td><td>132.00 (n/a)</td><td>100.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-19.39%)</td><td>0.04 (-10.71%)</td><td>0.04 (-13.29%)</td><td>0.04 (+10.14%)</td><td>0.00 <b>(-63.79%)</b></td><td>205.40 (-9.24%)</td><td>190.96 (+8.77%)</td><td>192.00 (+15.38%)</td><td>166.70 <b>(+24.03%)</b></td><td>14.67 <b>(-60.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>175.56 (n/a)</td><td>166.40 (n/a)</td><td>134.40 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+12.33%)</td><td>0.06 (-1.07%)</td><td>0.05 (-7.49%)</td><td>0.04 (-17.28%)</td><td>0.01 <b>(+85.30%)</b></td><td>203.40 <b>(+20.86%)</b></td><td>156.12 (+4.98%)</td><td>164.30 (+8.09%)</td><td>110.90 (-11.00%)</td><td>39.07 <b>(+93.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.30 (n/a)</td><td>148.72 (n/a)</td><td>152.00 (n/a)</td><td>124.60 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (+9.56%)</td><td>0.05 (-6.92%)</td><td>0.05 (-13.97%)</td><td>0.04 (-2.36%)</td><td>0.01 <b>(+41.70%)</b></td><td>190.60 (+2.42%)</td><td>168.38 (+9.24%)</td><td>176.80 (+16.24%)</td><td>113.50 (-8.76%)</td><td>31.79 <b>(+29.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.10 (n/a)</td><td>154.14 (n/a)</td><td>152.10 (n/a)</td><td>124.40 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-5.47%)</td><td>0.05 (-10.55%)</td><td>0.05 (-14.30%)</td><td>0.04 (-9.79%)</td><td>0.01 (+10.50%)</td><td>188.90 (+10.86%)</td><td>172.56 (+12.11%)</td><td>175.80 (+16.66%)</td><td>141.00 (+5.78%)</td><td>18.61 <b>(+26.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>153.92 (n/a)</td><td>150.70 (n/a)</td><td>133.30 (n/a)</td><td>14.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (+16.16%)</td><td>0.05 (+11.99%)</td><td>0.05 (+17.25%)</td><td>0.04 (+11.79%)</td><td>0.01 (+12.70%)</td><td>205.40 (-10.54%)</td><td>169.80 (-10.70%)</td><td>172.40 (-14.74%)</td><td>132.80 (-13.88%)</td><td>29.27 (-10.73%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>190.14 (n/a)</td><td>202.20 (n/a)</td><td>154.20 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 <b>(+21.25%)</b></td><td>0.05 <b>(+22.61%)</b></td><td>0.05 (+18.70%)</td><td>0.05 <b>(+47.69%)</b></td><td>0.01 (-18.27%)</td><td>167.90 <b>(-32.33%)</b></td><td>152.22 <b>(-20.38%)</b></td><td>158.40 (-15.74%)</td><td>120.10 (-17.51%)</td><td>18.95 <b>(-54.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.10 (n/a)</td><td>191.18 (n/a)</td><td>188.00 (n/a)</td><td>145.60 (n/a)</td><td>42.06 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-3.52%)</td><td>0.04 (-8.37%)</td><td>0.04 (-12.51%)</td><td>0.04 (-5.24%)</td><td>0.01 (+10.37%)</td><td>212.20 (+5.52%)</td><td>186.44 (+9.43%)</td><td>185.60 (+14.36%)</td><td>161.60 (+3.66%)</td><td>21.72 (+19.38%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>170.38 (n/a)</td><td>162.30 (n/a)</td><td>155.90 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-25.40%)</b></td><td>0.05 (-17.88%)</td><td>0.05 (-13.09%)</td><td>0.04 (-7.92%)</td><td>0.00 <b>(-61.37%)</b></td><td>195.10 (+8.57%)</td><td>176.62 (+19.43%)</td><td>170.60 (+15.04%)</td><td>163.20 <b>(+33.99%)</b></td><td>14.93 <b>(-42.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>147.88 (n/a)</td><td>148.30 (n/a)</td><td>121.80 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 <b>(-32.17%)</b></td><td>0.09 <b>(-32.12%)</b></td><td>0.09 <b>(-35.77%)</b></td><td>0.08 <b>(-26.71%)</b></td><td>0.01 <b>(-45.17%)</b></td><td>210.60 <b>(+36.40%)</b></td><td>188.96 <b>(+46.69%)</b></td><td>189.60 <b>(+55.67%)</b></td><td>171.10 <b>(+47.50%)</b></td><td>16.98 (+8.30%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>154.40 (n/a)</td><td>128.82 (n/a)</td><td>121.80 (n/a)</td><td>116.00 (n/a)</td><td>15.68 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-10.18%)</td><td>0.10 (-13.86%)</td><td>0.11 (-4.63%)</td><td>0.06 <b>(-38.85%)</b></td><td>0.02 <b>(+36.70%)</b></td><td>266.80 <b>(+63.48%)</b></td><td>172.16 <b>(+21.32%)</b></td><td>150.00 (+4.82%)</td><td>128.50 (+11.26%)</td><td>54.69 <b>(+159.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>163.20 (n/a)</td><td>141.90 (n/a)</td><td>143.10 (n/a)</td><td>115.50 (n/a)</td><td>21.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (+8.88%)</td><td>0.08 (+8.95%)</td><td>0.08 (+13.88%)</td><td>0.07 (+8.31%)</td><td>0.01 (+12.35%)</td><td>236.60 (-7.69%)</td><td>198.80 (-8.13%)</td><td>194.20 (-12.17%)</td><td>169.00 (-8.20%)</td><td>27.22 (-3.93%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.30 (n/a)</td><td>216.40 (n/a)</td><td>221.10 (n/a)</td><td>184.10 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (-0.04%)</td><td>0.09 (-1.70%)</td><td>0.09 (-0.49%)</td><td>0.07 (-7.51%)</td><td>0.01 <b>(+44.52%)</b></td><td>224.00 (+8.11%)</td><td>185.54 (+2.43%)</td><td>176.00 (+0.46%)</td><td>165.90 (+0.06%)</td><td>24.20 <b>(+53.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>181.14 (n/a)</td><td>175.20 (n/a)</td><td>165.80 (n/a)</td><td>15.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (-19.60%)</td><td>0.10 (-3.46%)</td><td>0.10 (+0.27%)</td><td>0.08 (-3.47%)</td><td>0.01 <b>(-44.83%)</b></td><td>193.60 (+3.58%)</td><td>159.98 (+1.51%)</td><td>160.90 (-0.25%)</td><td>138.00 <b>(+24.32%)</b></td><td>21.62 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>157.60 (n/a)</td><td>161.30 (n/a)</td><td>111.00 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 <b>(-33.72%)</b></td><td>0.08 <b>(-26.88%)</b></td><td>0.09 <b>(-22.02%)</b></td><td>0.07 <b>(-33.92%)</b></td><td>0.01 <b>(-34.65%)</b></td><td>244.70 <b>(+51.33%)</b></td><td>199.66 <b>(+36.79%)</b></td><td>192.30 <b>(+28.20%)</b></td><td>177.90 <b>(+50.89%)</b></td><td>26.22 <b>(+56.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>161.70 (n/a)</td><td>145.96 (n/a)</td><td>150.00 (n/a)</td><td>117.90 (n/a)</td><td>16.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (+7.49%)</td><td>0.10 (+2.62%)</td><td>0.09 (+3.84%)</td><td>0.08 (-8.47%)</td><td>0.01 <b>(+48.92%)</b></td><td>213.80 (+9.25%)</td><td>173.32 (-1.63%)</td><td>174.50 (-3.70%)</td><td>146.50 (-6.98%)</td><td>26.01 <b>(+54.35%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>176.20 (n/a)</td><td>181.20 (n/a)</td><td>157.50 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-18.83%)</td><td>0.10 (-12.46%)</td><td>0.10 <b>(-24.38%)</b></td><td>0.09 (+12.66%)</td><td>0.01 <b>(-66.11%)</b></td><td>192.20 (-11.27%)</td><td>173.34 (+7.38%)</td><td>172.20 <b>(+32.26%)</b></td><td>149.10 <b>(+23.22%)</b></td><td>18.20 <b>(-63.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.60 (n/a)</td><td>161.42 (n/a)</td><td>130.20 (n/a)</td><td>121.00 (n/a)</td><td>49.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 <b>(+20.74%)</b></td><td>0.09 (-8.25%)</td><td>0.08 (-14.89%)</td><td>0.05 <b>(-35.51%)</b></td><td>0.03 <b>(+153.11%)</b></td><td>312.20 <b>(+55.09%)</b></td><td>196.82 (+18.74%)</td><td>192.80 (+17.49%)</td><td>116.70 (-17.18%)</td><td>71.65 <b>(+224.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>165.76 (n/a)</td><td>164.10 (n/a)</td><td>140.90 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (+16.90%)</td><td>0.10 (+17.78%)</td><td>0.11 <b>(+24.26%)</b></td><td>0.08 (+4.94%)</td><td>0.02 <b>(+68.00%)</b></td><td>217.30 (-4.69%)</td><td>165.50 (-14.06%)</td><td>151.70 (-19.52%)</td><td>146.60 (-14.47%)</td><td>29.80 <b>(+36.65%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>192.58 (n/a)</td><td>188.50 (n/a)</td><td>171.40 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 <b>(+28.61%)</b></td><td>0.11 <b>(+26.19%)</b></td><td>0.12 <b>(+45.36%)</b></td><td>0.06 <b>(-21.28%)</b></td><td>0.03 <b>(+142.25%)</b></td><td>260.10 <b>(+27.06%)</b></td><td>157.40 (-14.71%)</td><td>135.50 <b>(-31.22%)</b></td><td>113.90 <b>(-22.25%)</b></td><td>60.12 <b>(+142.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>184.54 (n/a)</td><td>197.00 (n/a)</td><td>146.50 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (+9.67%)</td><td>0.11 (+5.83%)</td><td>0.11 (+9.83%)</td><td>0.08 (-1.62%)</td><td>0.03 <b>(+61.53%)</b></td><td>212.30 (+1.63%)</td><td>162.12 (-2.77%)</td><td>149.70 (-8.94%)</td><td>123.50 (-8.79%)</td><td>40.81 <b>(+47.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.90 (n/a)</td><td>166.74 (n/a)</td><td>164.40 (n/a)</td><td>135.40 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (+4.62%)</td><td>0.09 (+4.22%)</td><td>0.09 (+7.91%)</td><td>0.07 (+0.30%)</td><td>0.01 (+2.41%)</td><td>221.30 (-0.32%)</td><td>188.20 (-4.11%)</td><td>187.20 (-7.33%)</td><td>147.60 (-4.40%)</td><td>26.78 (-5.37%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>196.26 (n/a)</td><td>202.00 (n/a)</td><td>154.40 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (+1.60%)</td><td>0.10 (-1.49%)</td><td>0.09 (-4.83%)</td><td>0.08 (+6.50%)</td><td>0.01 (-2.58%)</td><td>198.30 (-6.11%)</td><td>172.72 (+1.28%)</td><td>182.40 (+5.07%)</td><td>140.70 (-1.61%)</td><td>23.83 (-10.30%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>170.54 (n/a)</td><td>173.60 (n/a)</td><td>143.00 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-6.09%)</td><td>0.09 (-12.02%)</td><td>0.08 (-13.06%)</td><td>0.07 (-12.76%)</td><td>0.02 (+19.06%)</td><td>231.70 (+14.65%)</td><td>194.62 (+14.98%)</td><td>199.40 (+15.06%)</td><td>148.70 (+6.44%)</td><td>34.71 <b>(+47.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>169.26 (n/a)</td><td>173.30 (n/a)</td><td>139.70 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-14.26%)</td><td>0.10 (-5.41%)</td><td>0.10 (-0.56%)</td><td>0.08 (-6.37%)</td><td>0.01 (-12.52%)</td><td>201.90 (+6.77%)</td><td>173.58 (+5.67%)</td><td>163.10 (+0.55%)</td><td>152.20 (+16.63%)</td><td>24.50 (+10.94%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>164.26 (n/a)</td><td>162.20 (n/a)</td><td>130.50 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (+7.59%)</td><td>0.21 (+14.52%)</td><td>0.22 <b>(+36.39%)</b></td><td>0.15 (-0.23%)</td><td>0.04 (+2.60%)</td><td>213.60 (+0.23%)</td><td>159.18 (-12.72%)</td><td>148.30 <b>(-26.69%)</b></td><td>121.10 (-6.99%)</td><td>34.32 (-3.11%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.10 (n/a)</td><td>182.38 (n/a)</td><td>202.30 (n/a)</td><td>130.20 (n/a)</td><td>35.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (+2.95%)</td><td>0.21 (+1.01%)</td><td>0.21 (-3.96%)</td><td>0.18 (+5.58%)</td><td>0.04 <b>(+23.54%)</b></td><td>187.20 (-5.26%)</td><td>157.56 (-0.23%)</td><td>159.00 (+4.13%)</td><td>127.20 (-2.90%)</td><td>28.93 (+12.40%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.60 (n/a)</td><td>157.92 (n/a)</td><td>152.70 (n/a)</td><td>131.00 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (+18.24%)</td><td>0.17 (+7.74%)</td><td>0.18 (+10.61%)</td><td>0.14 (-6.51%)</td><td>0.02 <b>(+136.12%)</b></td><td>236.80 (+6.96%)</td><td>192.22 (-6.01%)</td><td>181.10 (-9.59%)</td><td>163.30 (-15.43%)</td><td>27.94 <b>(+118.40%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>204.52 (n/a)</td><td>200.30 (n/a)</td><td>193.10 (n/a)</td><td>12.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (+1.82%)</td><td>0.18 (+6.42%)</td><td>0.18 (+6.68%)</td><td>0.16 <b>(+23.63%)</b></td><td>0.01 <b>(-50.05%)</b></td><td>201.70 (-19.09%)</td><td>183.84 (-7.38%)</td><td>180.60 (-6.23%)</td><td>168.90 (-1.75%)</td><td>12.60 <b>(-60.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>249.30 (n/a)</td><td>198.48 (n/a)</td><td>192.60 (n/a)</td><td>171.90 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (-14.48%)</td><td>0.20 (-15.60%)</td><td>0.21 (-12.03%)</td><td>0.14 (-16.97%)</td><td>0.06 (+1.34%)</td><td>241.90 <b>(+20.47%)</b></td><td>172.18 <b>(+21.03%)</b></td><td>156.90 (+13.70%)</td><td>124.40 (+16.92%)</td><td>52.77 <b>(+40.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>200.80 (n/a)</td><td>142.26 (n/a)</td><td>138.00 (n/a)</td><td>106.40 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-12.19%)</td><td>0.21 (-3.45%)</td><td>0.20 (+2.63%)</td><td>0.19 <b>(+35.54%)</b></td><td>0.03 <b>(-53.05%)</b></td><td>174.90 <b>(-26.20%)</b></td><td>156.52 (-3.26%)</td><td>164.90 (-2.54%)</td><td>122.70 (+13.82%)</td><td>22.05 <b>(-58.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>237.00 (n/a)</td><td>161.80 (n/a)</td><td>169.20 (n/a)</td><td>107.80 (n/a)</td><td>52.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (-0.98%)</td><td>0.21 (+4.28%)</td><td>0.19 (-12.72%)</td><td>0.16 <b>(+41.67%)</b></td><td>0.04 <b>(-31.32%)</b></td><td>201.80 <b>(-29.42%)</b></td><td>164.68 (-9.75%)</td><td>169.20 (+14.56%)</td><td>125.30 (+0.97%)</td><td>32.24 <b>(-51.78%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>285.90 (n/a)</td><td>182.48 (n/a)</td><td>147.70 (n/a)</td><td>124.10 (n/a)</td><td>66.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (-4.68%)</td><td>0.19 (-0.26%)</td><td>0.19 (-1.45%)</td><td>0.16 (+8.96%)</td><td>0.03 <b>(-31.32%)</b></td><td>210.50 (-8.20%)</td><td>178.60 (-2.20%)</td><td>172.50 (+1.47%)</td><td>145.90 (+4.89%)</td><td>28.91 <b>(-34.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>229.30 (n/a)</td><td>182.62 (n/a)</td><td>170.00 (n/a)</td><td>139.10 (n/a)</td><td>44.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 <b>(+24.05%)</b></td><td>0.24 <b>(+22.79%)</b></td><td>0.26 <b>(+30.35%)</b></td><td>0.18 (+12.00%)</td><td>0.04 <b>(+66.58%)</b></td><td>186.90 (-10.70%)</td><td>140.86 (-17.60%)</td><td>127.40 <b>(-23.25%)</b></td><td>124.80 (-19.38%)</td><td>26.47 (+19.03%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>170.94 (n/a)</td><td>166.00 (n/a)</td><td>154.80 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-15.58%)</td><td>0.21 (-17.76%)</td><td>0.21 <b>(-20.37%)</b></td><td>0.16 (-11.98%)</td><td>0.04 (-19.16%)</td><td>205.60 (+13.59%)</td><td>164.14 <b>(+21.12%)</b></td><td>156.20 <b>(+25.56%)</b></td><td>129.00 (+18.46%)</td><td>31.90 (+9.10%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>181.00 (n/a)</td><td>135.52 (n/a)</td><td>124.40 (n/a)</td><td>108.90 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (+9.08%)</td><td>0.21 (+15.86%)</td><td>0.22 <b>(+25.25%)</b></td><td>0.18 (+6.61%)</td><td>0.03 (+19.39%)</td><td>186.60 (-6.18%)</td><td>154.92 (-13.42%)</td><td>146.10 <b>(-20.16%)</b></td><td>132.80 (-8.35%)</td><td>21.57 (+6.61%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>178.94 (n/a)</td><td>183.00 (n/a)</td><td>144.90 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-7.74%)</td><td>0.22 (+9.17%)</td><td>0.22 <b>(+21.92%)</b></td><td>0.17 (+4.68%)</td><td>0.04 <b>(-21.69%)</b></td><td>197.90 (-4.49%)</td><td>154.12 (-10.01%)</td><td>149.80 (-17.96%)</td><td>121.10 (+8.32%)</td><td>31.44 (-18.43%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>207.20 (n/a)</td><td>171.26 (n/a)</td><td>182.60 (n/a)</td><td>111.80 (n/a)</td><td>38.54 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-14.10%)</td><td>0.19 (+1.58%)</td><td>0.21 (+12.87%)</td><td>0.15 <b>(+25.20%)</b></td><td>0.03 <b>(-49.16%)</b></td><td>213.70 <b>(-20.14%)</b></td><td>174.76 (-6.33%)</td><td>158.60 (-11.45%)</td><td>153.50 (+16.38%)</td><td>26.22 <b>(-52.39%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>267.60 (n/a)</td><td>186.56 (n/a)</td><td>179.10 (n/a)</td><td>131.90 (n/a)</td><td>55.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (+5.27%)</td><td>0.19 (+9.91%)</td><td>0.20 (+16.23%)</td><td>0.15 (-2.93%)</td><td>0.03 (+6.87%)</td><td>219.70 (+3.00%)</td><td>173.38 (-8.80%)</td><td>167.70 (-13.96%)</td><td>142.10 (-4.95%)</td><td>28.37 (+6.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>190.12 (n/a)</td><td>194.90 (n/a)</td><td>149.50 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (-2.29%)</td><td>0.21 (+11.22%)</td><td>0.21 (+15.06%)</td><td>0.19 (+12.31%)</td><td>0.02 <b>(-34.78%)</b></td><td>175.20 (-10.98%)</td><td>156.94 (-10.99%)</td><td>159.10 (-13.06%)</td><td>140.40 (+2.33%)</td><td>14.24 <b>(-40.16%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.80 (n/a)</td><td>176.32 (n/a)</td><td>183.00 (n/a)</td><td>137.20 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-8.22%)</td><td>0.19 (-3.60%)</td><td>0.19 (-11.74%)</td><td>0.17 (+13.07%)</td><td>0.02 <b>(-51.78%)</b></td><td>194.30 (-11.56%)</td><td>173.54 (+1.15%)</td><td>171.70 (+13.33%)</td><td>154.90 (+8.93%)</td><td>16.85 <b>(-52.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.70 (n/a)</td><td>171.56 (n/a)</td><td>151.50 (n/a)</td><td>142.20 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (+0.10%)</td><td>0.21 (-0.02%)</td><td>0.21 (-0.02%)</td><td>0.21 (-0.08%)</td><td>0.00 <b>(+116.71%)</b></td><td>40901.00 (+0.08%)</td><td>40844.96 (+0.02%)</td><td>40845.20 (+0.02%)</td><td>40759.80 (-0.10%)</td><td>54.66 <b>(+116.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40869.30 (n/a)</td><td>40835.16 (n/a)</td><td>40835.90 (n/a)</td><td>40800.70 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-0.97%)</td><td>0.21 (-0.26%)</td><td>0.21 (-0.09%)</td><td>0.20 (+0.00%)</td><td>0.00 <b>(-74.32%)</b></td><td>40921.00 (-0.00%)</td><td>40861.42 (+0.26%)</td><td>40863.20 (+0.09%)</td><td>40770.30 (+0.98%)</td><td>56.42 <b>(-74.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40921.70 (n/a)</td><td>40754.02 (n/a)</td><td>40826.20 (n/a)</td><td>40373.70 (n/a)</td><td>217.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-0.05%)</td><td>0.13 (-0.00%)</td><td>0.13 (-0.00%)</td><td>0.13 (+0.04%)</td><td>0.00 <b>(-40.49%)</b></td><td>321820.90 (-0.04%)</td><td>321682.98 (+0.00%)</td><td>321705.70 (+0.00%)</td><td>321453.30 (+0.05%)</td><td>144.61 <b>(-40.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321962.60 (n/a)</td><td>321679.28 (n/a)</td><td>321693.60 (n/a)</td><td>321294.20 (n/a)</td><td>242.96 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-11.38%)</td><td>0.02 (-11.38%)</td><td>0.02 (-2.76%)</td><td>0.02 (-13.26%)</td><td>0.00 <b>(-28.05%)</b></td><td>196.10 (+15.29%)</td><td>170.16 (+12.18%)</td><td>167.50 (+2.82%)</td><td>142.40 (+12.84%)</td><td>20.28 (-6.74%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.10 (n/a)</td><td>151.68 (n/a)</td><td>162.90 (n/a)</td><td>126.20 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-11.31%)</td><td>0.04 (-0.12%)</td><td>0.04 (+18.83%)</td><td>0.03 (-9.16%)</td><td>0.01 (-13.48%)</td><td>212.90 (+10.08%)</td><td>161.00 (-0.17%)</td><td>141.90 (-15.89%)</td><td>131.90 (+12.74%)</td><td>34.31 (+6.28%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>161.28 (n/a)</td><td>168.70 (n/a)</td><td>117.00 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-13.69%)</td><td>0.02 (-13.27%)</td><td>0.02 (-8.96%)</td><td>0.02 (-2.91%)</td><td>0.00 <b>(-27.75%)</b></td><td>209.80 (+2.99%)</td><td>175.50 (+13.80%)</td><td>171.10 (+9.89%)</td><td>136.70 (+15.85%)</td><td>29.22 (-12.50%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>154.22 (n/a)</td><td>155.70 (n/a)</td><td>118.00 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+3.73%)</td><td>0.03 (-3.01%)</td><td>0.03 (-7.62%)</td><td>0.03 (-1.57%)</td><td>0.00 <b>(+27.64%)</b></td><td>201.90 (+1.56%)</td><td>182.36 (+3.81%)</td><td>192.80 (+8.25%)</td><td>139.30 (-3.60%)</td><td>25.76 <b>(+25.15%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>175.66 (n/a)</td><td>178.10 (n/a)</td><td>144.50 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+1.87%)</td><td>0.03 (-3.89%)</td><td>0.03 (-7.19%)</td><td>0.02 (+3.83%)</td><td>0.00 (-10.15%)</td><td>186.80 (-3.66%)</td><td>162.90 (+3.74%)</td><td>157.80 (+7.79%)</td><td>140.40 (-1.82%)</td><td>17.85 (-15.69%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>157.02 (n/a)</td><td>146.40 (n/a)</td><td>143.00 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (+1.65%)</td><td>0.03 (-6.69%)</td><td>0.03 (-15.34%)</td><td>0.02 (-1.47%)</td><td>0.01 (-3.47%)</td><td>236.80 (+1.50%)</td><td>189.58 (+7.01%)</td><td>182.60 (+18.11%)</td><td>145.60 (-1.62%)</td><td>37.10 (-1.12%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>177.16 (n/a)</td><td>154.60 (n/a)</td><td>148.00 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+4.31%)</td><td>0.03 (+0.78%)</td><td>0.03 (+15.86%)</td><td>0.02 <b>(-21.89%)</b></td><td>0.01 <b>(+124.14%)</b></td><td>227.50 <b>(+28.02%)</b></td><td>167.66 (+3.01%)</td><td>144.10 (-13.71%)</td><td>134.90 (-4.12%)</td><td>41.67 <b>(+168.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>162.76 (n/a)</td><td>167.00 (n/a)</td><td>140.70 (n/a)</td><td>15.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-7.20%)</td><td>0.02 (-6.82%)</td><td>0.02 (-18.42%)</td><td>0.02 (+11.05%)</td><td>0.00 <b>(-34.53%)</b></td><td>225.80 (-9.97%)</td><td>198.00 (+5.00%)</td><td>211.60 <b>(+22.60%)</b></td><td>161.00 (+7.76%)</td><td>27.06 <b>(-36.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>188.58 (n/a)</td><td>172.60 (n/a)</td><td>149.40 (n/a)</td><td>42.60 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+8.86%)</td><td>0.03 (+11.64%)</td><td>0.03 (+5.84%)</td><td>0.02 (+18.94%)</td><td>0.00 (-13.20%)</td><td>202.70 (-15.93%)</td><td>165.06 (-11.81%)</td><td>156.40 (-5.50%)</td><td>138.00 (-8.12%)</td><td>27.87 <b>(-33.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.10 (n/a)</td><td>187.16 (n/a)</td><td>165.50 (n/a)</td><td>150.20 (n/a)</td><td>41.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+5.92%)</td><td>0.03 (-1.93%)</td><td>0.03 (-4.47%)</td><td>0.02 (-5.06%)</td><td>0.00 <b>(+43.35%)</b></td><td>207.40 (+5.33%)</td><td>179.70 (+2.99%)</td><td>184.10 (+4.66%)</td><td>137.20 (-5.57%)</td><td>26.39 <b>(+41.40%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.90 (n/a)</td><td>174.48 (n/a)</td><td>175.90 (n/a)</td><td>145.30 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (-15.65%)</td><td>0.02 (+5.04%)</td><td>0.02 <b>(+26.37%)</b></td><td>0.02 <b>(+55.76%)</b></td><td>0.00 <b>(-66.65%)</b></td><td>224.20 <b>(-35.80%)</b></td><td>188.20 (-15.94%)</td><td>190.00 <b>(-20.87%)</b></td><td>158.40 (+18.56%)</td><td>24.99 <b>(-72.42%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>349.20 (n/a)</td><td>223.90 (n/a)</td><td>240.10 (n/a)</td><td>133.60 (n/a)</td><td>90.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+0.44%)</td><td>0.02 (-1.11%)</td><td>0.02 (-3.67%)</td><td>0.02 (+0.87%)</td><td>0.00 (+16.77%)</td><td>204.50 (-0.87%)</td><td>188.56 (+1.26%)</td><td>195.60 (+3.82%)</td><td>171.40 (-0.46%)</td><td>15.29 (+14.13%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.30 (n/a)</td><td>186.22 (n/a)</td><td>188.40 (n/a)</td><td>172.20 (n/a)</td><td>13.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (+2.68%)</td><td>0.02 (+12.50%)</td><td>0.02 (+13.00%)</td><td>0.02 <b>(+41.39%)</b></td><td>0.00 <b>(-26.39%)</b></td><td>205.00 <b>(-29.29%)</b></td><td>172.90 (-14.76%)</td><td>180.30 (-11.49%)</td><td>134.90 (-2.67%)</td><td>31.05 <b>(-48.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>289.90 (n/a)</td><td>202.84 (n/a)</td><td>203.70 (n/a)</td><td>138.60 (n/a)</td><td>60.14 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-9.77%)</td><td>0.02 (-13.01%)</td><td>0.02 (-12.46%)</td><td>0.02 (-14.53%)</td><td>0.00 (+18.94%)</td><td>234.90 (+16.98%)</td><td>200.84 (+15.60%)</td><td>198.30 (+14.23%)</td><td>174.40 (+10.87%)</td><td>25.28 <b>(+51.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>173.74 (n/a)</td><td>173.60 (n/a)</td><td>157.30 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (-4.52%)</td><td>0.02 (-7.33%)</td><td>0.02 (-8.79%)</td><td>0.02 (-7.41%)</td><td>0.00 (-6.98%)</td><td>237.50 (+8.00%)</td><td>207.80 (+7.88%)</td><td>206.00 (+9.63%)</td><td>180.80 (+4.69%)</td><td>21.17 (+5.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>192.62 (n/a)</td><td>187.90 (n/a)</td><td>172.70 (n/a)</td><td>19.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-16.07%)</td><td>0.05 (+1.40%)</td><td>0.05 (-2.88%)</td><td>0.04 <b>(+28.61%)</b></td><td>0.01 <b>(-55.71%)</b></td><td>219.00 <b>(-22.26%)</b></td><td>180.34 (-6.39%)</td><td>174.70 (+2.95%)</td><td>157.20 (+19.18%)</td><td>23.39 <b>(-59.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>281.70 (n/a)</td><td>192.66 (n/a)</td><td>169.70 (n/a)</td><td>131.90 (n/a)</td><td>57.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (-10.18%)</td><td>0.08 (-12.53%)</td><td>0.07 (-19.79%)</td><td>0.06 (+14.64%)</td><td>0.02 <b>(-37.21%)</b></td><td>190.80 (-12.76%)</td><td>164.92 (+9.57%)</td><td>171.30 <b>(+24.67%)</b></td><td>120.20 (+11.30%)</td><td>29.05 <b>(-37.70%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.70 (n/a)</td><td>150.52 (n/a)</td><td>137.40 (n/a)</td><td>108.00 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-15.23%)</td><td>0.05 (-15.87%)</td><td>0.04 (-14.86%)</td><td>0.04 (-16.52%)</td><td>0.00 (-17.37%)</td><td>201.50 (+19.80%)</td><td>182.20 (+18.81%)</td><td>185.30 (+17.43%)</td><td>156.60 (+17.92%)</td><td>16.37 (+15.40%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>153.36 (n/a)</td><td>157.80 (n/a)</td><td>132.80 (n/a)</td><td>14.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (+11.28%)</td><td>0.07 (+4.23%)</td><td>0.06 (-3.72%)</td><td>0.05 (+14.74%)</td><td>0.01 (+4.74%)</td><td>213.30 (-12.87%)</td><td>161.90 (-4.73%)</td><td>164.10 (+3.93%)</td><td>121.70 (-10.12%)</td><td>36.12 (-19.22%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>169.94 (n/a)</td><td>157.90 (n/a)</td><td>135.40 (n/a)</td><td>44.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-20.81%)</b></td><td>0.05 (-9.45%)</td><td>0.05 (-7.37%)</td><td>0.04 (-1.49%)</td><td>0.00 <b>(-54.64%)</b></td><td>218.40 (+1.53%)</td><td>182.82 (+7.52%)</td><td>178.60 (+7.98%)</td><td>160.30 <b>(+26.32%)</b></td><td>21.41 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>170.04 (n/a)</td><td>165.40 (n/a)</td><td>126.90 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 <b>(-27.44%)</b></td><td>0.06 (-17.78%)</td><td>0.06 (-16.80%)</td><td>0.05 (-1.13%)</td><td>0.01 <b>(-61.80%)</b></td><td>221.10 (+1.14%)</td><td>186.52 (+17.81%)</td><td>181.30 <b>(+20.23%)</b></td><td>168.00 <b>(+37.82%)</b></td><td>20.24 <b>(-46.22%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>158.32 (n/a)</td><td>150.80 (n/a)</td><td>121.90 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-15.92%)</td><td>0.05 (-18.76%)</td><td>0.05 (-13.98%)</td><td>0.02 <b>(-54.33%)</b></td><td>0.01 <b>(+47.91%)</b></td><td>378.10 <b>(+118.93%)</b></td><td>205.76 <b>(+36.54%)</b></td><td>175.20 (+16.26%)</td><td>136.50 (+18.90%)</td><td>98.07 <b>(+312.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>150.70 (n/a)</td><td>150.70 (n/a)</td><td>114.80 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-22.54%)</b></td><td>0.05 (-18.88%)</td><td>0.05 <b>(-22.85%)</b></td><td>0.04 (-6.69%)</td><td>0.00 <b>(-60.06%)</b></td><td>217.10 (+7.16%)</td><td>198.46 <b>(+21.67%)</b></td><td>197.90 <b>(+29.60%)</b></td><td>179.50 <b>(+29.04%)</b></td><td>13.33 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>163.12 (n/a)</td><td>152.70 (n/a)</td><td>139.10 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (+12.26%)</td><td>0.05 (+0.02%)</td><td>0.05 (+12.30%)</td><td>0.04 (-18.92%)</td><td>0.01 <b>(+157.92%)</b></td><td>216.90 <b>(+23.31%)</b></td><td>169.76 (+3.98%)</td><td>153.00 (-10.94%)</td><td>129.10 (-10.90%)</td><td>41.06 <b>(+191.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.90 (n/a)</td><td>163.26 (n/a)</td><td>171.80 (n/a)</td><td>144.90 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 <b>(-29.28%)</b></td><td>0.04 <b>(-22.12%)</b></td><td>0.04 <b>(-23.31%)</b></td><td>0.04 (-15.85%)</td><td>0.01 <b>(-48.59%)</b></td><td>240.40 (+18.83%)</td><td>209.08 <b>(+26.78%)</b></td><td>212.20 <b>(+30.42%)</b></td><td>179.20 <b>(+41.32%)</b></td><td>24.02 (-13.08%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>164.92 (n/a)</td><td>162.70 (n/a)</td><td>126.80 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (-5.62%)</td><td>0.04 (-10.42%)</td><td>0.04 (-13.64%)</td><td>0.03 (-14.83%)</td><td>0.01 (+12.47%)</td><td>240.40 (+17.38%)</td><td>202.64 (+12.34%)</td><td>202.40 (+15.79%)</td><td>167.50 (+5.95%)</td><td>30.37 <b>(+37.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>180.38 (n/a)</td><td>174.80 (n/a)</td><td>158.10 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-3.05%)</td><td>0.05 (-4.30%)</td><td>0.05 (-7.92%)</td><td>0.04 (+5.80%)</td><td>0.01 <b>(-20.37%)</b></td><td>208.50 (-5.49%)</td><td>187.90 (+3.24%)</td><td>193.10 (+8.61%)</td><td>143.70 (+3.16%)</td><td>25.63 <b>(-25.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>182.00 (n/a)</td><td>177.80 (n/a)</td><td>139.30 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (-0.10%)</td><td>0.05 (-1.58%)</td><td>0.04 <b>(-23.61%)</b></td><td>0.03 <b>(+41.99%)</b></td><td>0.01 <b>(-28.77%)</b></td><td>240.70 <b>(-29.58%)</b></td><td>177.62 (-6.11%)</td><td>182.90 <b>(+30.92%)</b></td><td>137.40 (+0.07%)</td><td>42.95 <b>(-51.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>341.80 (n/a)</td><td>189.18 (n/a)</td><td>139.70 (n/a)</td><td>137.30 (n/a)</td><td>88.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (-9.89%)</td><td>0.05 (-6.47%)</td><td>0.05 (-8.68%)</td><td>0.04 <b>(+30.04%)</b></td><td>0.01 <b>(-34.93%)</b></td><td>201.30 <b>(-23.11%)</b></td><td>179.84 (+2.38%)</td><td>192.00 (+9.46%)</td><td>130.90 (+10.93%)</td><td>28.87 <b>(-46.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.80 (n/a)</td><td>175.66 (n/a)</td><td>175.40 (n/a)</td><td>118.00 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (-18.23%)</td><td>0.04 (-17.55%)</td><td>0.04 (-15.21%)</td><td>0.03 <b>(-36.70%)</b></td><td>0.01 <b>(+61.02%)</b></td><td>323.80 <b>(+58.03%)</b></td><td>231.36 <b>(+24.53%)</b></td><td>217.20 (+17.92%)</td><td>197.60 <b>(+22.28%)</b></td><td>52.52 <b>(+221.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.90 (n/a)</td><td>185.78 (n/a)</td><td>184.20 (n/a)</td><td>161.60 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 <b>(-23.64%)</b></td><td>0.09 (-13.98%)</td><td>0.10 (-6.73%)</td><td>0.08 (-12.64%)</td><td>0.01 <b>(-45.82%)</b></td><td>216.90 (+14.52%)</td><td>180.96 (+14.85%)</td><td>169.10 (+7.23%)</td><td>167.50 <b>(+30.96%)</b></td><td>21.12 (-18.42%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>157.56 (n/a)</td><td>157.70 (n/a)</td><td>127.90 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (-6.56%)</td><td>0.14 (-9.17%)</td><td>0.14 (-3.46%)</td><td>0.10 <b>(-28.20%)</b></td><td>0.02 <b>(+71.01%)</b></td><td>246.50 <b>(+39.27%)</b></td><td>184.68 (+12.43%)</td><td>171.60 (+3.62%)</td><td>152.20 (+7.03%)</td><td>36.68 <b>(+163.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>177.00 (n/a)</td><td>164.26 (n/a)</td><td>165.60 (n/a)</td><td>142.20 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (-8.79%)</td><td>0.10 (-6.31%)</td><td>0.10 (+0.09%)</td><td>0.08 (-3.00%)</td><td>0.01 <b>(-37.83%)</b></td><td>198.10 (+3.12%)</td><td>168.42 (+4.80%)</td><td>168.30 (-0.12%)</td><td>137.00 (+9.60%)</td><td>21.89 <b>(-30.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.10 (n/a)</td><td>160.70 (n/a)</td><td>168.50 (n/a)</td><td>125.00 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (+4.54%)</td><td>0.12 (+1.03%)</td><td>0.12 (+0.71%)</td><td>0.08 (-6.43%)</td><td>0.02 <b>(+25.09%)</b></td><td>247.40 (+6.87%)</td><td>176.44 (+0.32%)</td><td>164.10 (-0.67%)</td><td>146.50 (-4.31%)</td><td>41.32 <b>(+28.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>175.88 (n/a)</td><td>165.20 (n/a)</td><td>153.10 (n/a)</td><td>32.25 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-15.55%)</td><td>0.10 (-3.97%)</td><td>0.10 (-5.70%)</td><td>0.09 <b>(+67.20%)</b></td><td>0.01 <b>(-64.04%)</b></td><td>192.30 <b>(-40.19%)</b></td><td>164.14 (-6.94%)</td><td>158.50 (+6.09%)</td><td>143.00 (+18.38%)</td><td>20.35 <b>(-75.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>321.50 (n/a)</td><td>176.38 (n/a)</td><td>149.40 (n/a)</td><td>120.80 (n/a)</td><td>82.99 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-16.82%)</td><td>0.11 <b>(-20.18%)</b></td><td>0.11 <b>(-23.40%)</b></td><td>0.10 (-8.95%)</td><td>0.01 <b>(-34.11%)</b></td><td>208.40 (+9.80%)</td><td>186.22 <b>(+24.35%)</b></td><td>183.60 <b>(+30.49%)</b></td><td>157.80 <b>(+20.27%)</b></td><td>19.55 (-15.73%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.80 (n/a)</td><td>149.76 (n/a)</td><td>140.70 (n/a)</td><td>131.20 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (-16.93%)</td><td>0.09 (-15.09%)</td><td>0.10 (-4.69%)</td><td>0.06 <b>(-36.61%)</b></td><td>0.02 (+10.77%)</td><td>288.80 <b>(+57.81%)</b></td><td>186.38 <b>(+22.09%)</b></td><td>171.60 (+4.89%)</td><td>140.90 <b>(+20.32%)</b></td><td>58.80 <b>(+125.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>152.66 (n/a)</td><td>163.60 (n/a)</td><td>117.10 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (-3.53%)</td><td>0.10 (-11.34%)</td><td>0.09 (-17.72%)</td><td>0.09 (-9.27%)</td><td>0.02 <b>(+23.76%)</b></td><td>209.70 (+10.19%)</td><td>184.84 (+14.21%)</td><td>202.20 <b>(+21.51%)</b></td><td>136.40 (+3.65%)</td><td>32.46 <b>(+45.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>161.84 (n/a)</td><td>166.40 (n/a)</td><td>131.60 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (-10.21%)</td><td>0.10 (-1.38%)</td><td>0.10 (-8.91%)</td><td>0.08 (+1.32%)</td><td>0.02 <b>(-29.57%)</b></td><td>213.60 (-1.34%)</td><td>162.14 (-1.66%)</td><td>158.90 (+9.81%)</td><td>131.30 (+11.37%)</td><td>33.75 <b>(-27.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>216.50 (n/a)</td><td>164.88 (n/a)</td><td>144.70 (n/a)</td><td>117.90 (n/a)</td><td>46.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (+9.31%)</td><td>0.10 (+2.12%)</td><td>0.11 (+4.67%)</td><td>0.06 <b>(-27.93%)</b></td><td>0.03 <b>(+74.49%)</b></td><td>301.10 <b>(+38.76%)</b></td><td>191.06 (+2.78%)</td><td>170.80 (-4.42%)</td><td>144.10 (-8.57%)</td><td>62.81 <b>(+132.66%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>185.90 (n/a)</td><td>178.70 (n/a)</td><td>157.60 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (+2.27%)</td><td>0.09 (+1.38%)</td><td>0.09 (+9.06%)</td><td>0.05 (-0.35%)</td><td>0.03 (+7.70%)</td><td>339.10 (+0.33%)</td><td>209.56 (-0.19%)</td><td>180.90 (-8.31%)</td><td>128.20 (-2.21%)</td><td>80.97 (+4.73%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>338.00 (n/a)</td><td>209.96 (n/a)</td><td>197.30 (n/a)</td><td>131.10 (n/a)</td><td>77.31 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (-18.61%)</td><td>0.09 (-4.19%)</td><td>0.09 (+0.94%)</td><td>0.08 (+8.08%)</td><td>0.01 <b>(-53.16%)</b></td><td>226.50 (-7.48%)</td><td>189.68 (+0.88%)</td><td>191.80 (-0.93%)</td><td>168.70 <b>(+22.87%)</b></td><td>23.66 <b>(-46.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.80 (n/a)</td><td>188.02 (n/a)</td><td>193.60 (n/a)</td><td>137.30 (n/a)</td><td>44.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (-14.95%)</td><td>0.09 (-3.93%)</td><td>0.09 (+2.15%)</td><td>0.08 (+3.13%)</td><td>0.00 <b>(-58.78%)</b></td><td>200.30 (-3.05%)</td><td>188.04 (+3.25%)</td><td>183.90 (-2.08%)</td><td>179.40 (+17.56%)</td><td>9.46 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>182.12 (n/a)</td><td>187.80 (n/a)</td><td>152.60 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (-17.79%)</td><td>0.09 (-14.15%)</td><td>0.09 (-11.85%)</td><td>0.06 (-16.71%)</td><td>0.02 (-12.40%)</td><td>289.60 <b>(+20.07%)</b></td><td>205.94 (+16.92%)</td><td>194.40 (+13.42%)</td><td>165.80 <b>(+21.64%)</b></td><td>50.59 <b>(+25.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>241.20 (n/a)</td><td>176.14 (n/a)</td><td>171.40 (n/a)</td><td>136.30 (n/a)</td><td>40.32 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (+0.27%)</td><td>0.07 (-8.79%)</td><td>0.08 (-5.93%)</td><td>0.04 <b>(-38.15%)</b></td><td>0.02 <b>(+83.76%)</b></td><td>375.30 <b>(+61.70%)</b></td><td>236.16 (+16.40%)</td><td>204.80 (+6.28%)</td><td>169.10 (-0.24%)</td><td>81.01 <b>(+207.08%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>202.88 (n/a)</td><td>192.70 (n/a)</td><td>169.50 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-0.20%)</td><td>0.19 (+4.54%)</td><td>0.19 (+3.85%)</td><td>0.15 (-2.18%)</td><td>0.04 (+3.98%)</td><td>223.30 (+2.20%)</td><td>175.14 (-4.02%)</td><td>172.20 (-3.69%)</td><td>131.30 (+0.23%)</td><td>37.55 (+5.61%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.50 (n/a)</td><td>182.48 (n/a)</td><td>178.80 (n/a)</td><td>131.00 (n/a)</td><td>35.55 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (+5.97%)</td><td>0.19 (-7.91%)</td><td>0.17 (-17.60%)</td><td>0.12 <b>(-34.09%)</b></td><td>0.05 <b>(+170.87%)</b></td><td>277.00 <b>(+51.70%)</b></td><td>190.50 (+15.97%)</td><td>192.80 <b>(+21.33%)</b></td><td>135.20 (-5.65%)</td><td>58.88 <b>(+262.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.60 (n/a)</td><td>164.26 (n/a)</td><td>158.90 (n/a)</td><td>143.30 (n/a)</td><td>16.24 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (-13.70%)</td><td>0.21 <b>(-21.33%)</b></td><td>0.19 <b>(-28.20%)</b></td><td>0.17 <b>(-27.18%)</b></td><td>0.04 <b>(+47.74%)</b></td><td>243.80 <b>(+37.27%)</b></td><td>199.44 <b>(+29.83%)</b></td><td>211.40 <b>(+39.26%)</b></td><td>156.80 (+15.81%)</td><td>37.92 <b>(+128.61%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>177.60 (n/a)</td><td>153.62 (n/a)</td><td>151.80 (n/a)</td><td>135.40 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (+5.86%)</td><td>0.21 (-0.36%)</td><td>0.21 (-11.95%)</td><td>0.15 (-2.48%)</td><td>0.04 (+2.71%)</td><td>216.70 (+2.56%)</td><td>161.48 (+0.49%)</td><td>157.20 (+13.58%)</td><td>126.60 (-5.59%)</td><td>35.15 (+2.02%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.30 (n/a)</td><td>160.70 (n/a)</td><td>138.40 (n/a)</td><td>134.10 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-18.48%)</td><td>0.22 (-18.21%)</td><td>0.22 (-17.89%)</td><td>0.19 (-14.70%)</td><td>0.03 <b>(-28.66%)</b></td><td>215.40 (+17.19%)</td><td>189.58 <b>(+21.54%)</b></td><td>185.20 <b>(+21.84%)</b></td><td>152.10 <b>(+22.66%)</b></td><td>25.26 (+0.95%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>183.80 (n/a)</td><td>155.98 (n/a)</td><td>152.00 (n/a)</td><td>124.00 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-4.57%)</td><td>0.22 (+10.13%)</td><td>0.24 <b>(+24.16%)</b></td><td>0.17 <b>(+28.97%)</b></td><td>0.04 (-13.64%)</td><td>189.70 <b>(-22.48%)</b></td><td>154.60 (-10.84%)</td><td>133.90 (-19.48%)</td><td>132.30 (+4.75%)</td><td>29.60 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>244.70 (n/a)</td><td>173.40 (n/a)</td><td>166.30 (n/a)</td><td>126.30 (n/a)</td><td>43.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (-16.46%)</td><td>0.22 (+2.63%)</td><td>0.21 (-0.21%)</td><td>0.20 <b>(+42.13%)</b></td><td>0.02 <b>(-69.32%)</b></td><td>187.90 <b>(-29.63%)</b></td><td>171.50 (-7.44%)</td><td>173.10 (+0.23%)</td><td>152.50 (+19.70%)</td><td>12.77 <b>(-74.92%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>267.00 (n/a)</td><td>185.28 (n/a)</td><td>172.70 (n/a)</td><td>127.40 (n/a)</td><td>50.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 <b>(+27.22%)</b></td><td>0.21 (+10.93%)</td><td>0.19 (+0.42%)</td><td>0.17 (+1.48%)</td><td>0.05 <b>(+130.29%)</b></td><td>197.20 (-1.45%)</td><td>161.76 (-6.88%)</td><td>173.00 (-0.40%)</td><td>118.30 <b>(-21.40%)</b></td><td>35.86 <b>(+79.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.10 (n/a)</td><td>173.72 (n/a)</td><td>173.70 (n/a)</td><td>150.50 (n/a)</td><td>20.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-2.61%)</td><td>0.22 (-7.07%)</td><td>0.22 (+3.80%)</td><td>0.17 <b>(-20.34%)</b></td><td>0.04 (+9.37%)</td><td>221.20 <b>(+25.54%)</b></td><td>173.28 (+8.44%)</td><td>167.60 (-3.68%)</td><td>138.80 (+2.66%)</td><td>29.99 <b>(+43.12%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>176.20 (n/a)</td><td>159.80 (n/a)</td><td>174.00 (n/a)</td><td>135.20 (n/a)</td><td>20.95 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (-2.83%)</td><td>0.18 (+1.45%)</td><td>0.18 (+11.32%)</td><td>0.15 (-7.77%)</td><td>0.02 (-5.95%)</td><td>223.50 (+8.44%)</td><td>186.80 (-1.45%)</td><td>181.60 (-10.19%)</td><td>167.20 (+2.89%)</td><td>21.81 (+5.90%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.10 (n/a)</td><td>189.54 (n/a)</td><td>202.20 (n/a)</td><td>162.50 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-17.41%)</td><td>0.17 (-11.37%)</td><td>0.20 (+1.62%)</td><td>0.09 (-12.26%)</td><td>0.05 (-5.10%)</td><td>368.70 (+13.97%)</td><td>226.12 (+14.16%)</td><td>177.30 (-1.61%)</td><td>167.10 <b>(+21.09%)</b></td><td>86.89 (+19.51%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>323.50 (n/a)</td><td>198.08 (n/a)</td><td>180.20 (n/a)</td><td>138.00 (n/a)</td><td>72.71 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (+4.33%)</td><td>0.17 (+13.45%)</td><td>0.19 <b>(+33.68%)</b></td><td>0.11 (-10.86%)</td><td>0.04 (+15.06%)</td><td>310.60 (+12.21%)</td><td>200.78 (-10.19%)</td><td>172.80 <b>(-25.19%)</b></td><td>158.30 (-4.12%)</td><td>63.19 <b>(+27.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>276.80 (n/a)</td><td>223.56 (n/a)</td><td>231.00 (n/a)</td><td>165.10 (n/a)</td><td>49.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (+0.83%)</td><td>0.19 (-3.13%)</td><td>0.20 (+4.53%)</td><td>0.14 (-10.24%)</td><td>0.03 <b>(+23.96%)</b></td><td>246.30 (+11.40%)</td><td>189.76 (+4.53%)</td><td>172.80 (-4.32%)</td><td>152.80 (-0.78%)</td><td>37.88 <b>(+39.65%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>221.10 (n/a)</td><td>181.54 (n/a)</td><td>180.60 (n/a)</td><td>154.00 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (-0.88%)</td><td>0.16 (+13.17%)</td><td>0.16 (+17.72%)</td><td>0.11 (+8.78%)</td><td>0.03 (-11.60%)</td><td>294.00 (-8.07%)</td><td>214.42 (-12.73%)</td><td>205.40 (-15.05%)</td><td>172.70 (+0.88%)</td><td>48.34 (-17.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>319.80 (n/a)</td><td>245.70 (n/a)</td><td>241.80 (n/a)</td><td>171.20 (n/a)</td><td>58.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 <b>(-24.83%)</b></td><td>0.12 (-9.51%)</td><td>0.13 (+13.28%)</td><td>0.08 <b>(-24.16%)</b></td><td>0.02 <b>(-31.38%)</b></td><td>252.00 <b>(+31.87%)</b></td><td>181.50 (+9.76%)</td><td>161.70 (-11.74%)</td><td>151.10 <b>(+33.01%)</b></td><td>41.12 <b>(+21.19%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>191.10 (n/a)</td><td>165.36 (n/a)</td><td>183.20 (n/a)</td><td>113.60 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (-11.97%)</td><td>0.13 (-13.73%)</td><td>0.12 (-14.81%)</td><td>0.11 (-0.59%)</td><td>0.02 <b>(-24.44%)</b></td><td>184.90 (+0.60%)</td><td>165.94 (+14.74%)</td><td>176.60 (+17.42%)</td><td>125.80 (+13.64%)</td><td>23.45 (-15.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>144.62 (n/a)</td><td>150.40 (n/a)</td><td>110.70 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-7.05%)</td><td>0.11 (+4.17%)</td><td>0.12 (+5.26%)</td><td>0.08 (+14.13%)</td><td>0.02 <b>(-25.24%)</b></td><td>246.50 (-12.37%)</td><td>184.22 (-6.00%)</td><td>172.40 (-5.01%)</td><td>162.90 (+7.60%)</td><td>35.24 <b>(-30.58%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>281.30 (n/a)</td><td>195.98 (n/a)</td><td>181.50 (n/a)</td><td>151.40 (n/a)</td><td>50.77 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (-0.91%)</td><td>0.13 (-3.79%)</td><td>0.12 (-2.90%)</td><td>0.10 (-6.99%)</td><td>0.02 (+13.57%)</td><td>195.80 (+7.46%)</td><td>164.54 (+4.66%)</td><td>167.80 (+3.01%)</td><td>125.00 (+0.89%)</td><td>27.35 <b>(+24.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>182.20 (n/a)</td><td>157.22 (n/a)</td><td>162.90 (n/a)</td><td>123.90 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 <b>(+23.18%)</b></td><td>0.12 (-1.49%)</td><td>0.11 (-10.03%)</td><td>0.10 (-4.11%)</td><td>0.03 <b>(+134.39%)</b></td><td>202.60 (+4.27%)</td><td>175.80 (+3.85%)</td><td>181.90 (+11.12%)</td><td>125.90 (-18.83%)</td><td>30.77 <b>(+94.77%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>169.28 (n/a)</td><td>163.70 (n/a)</td><td>155.10 (n/a)</td><td>15.80 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (+14.21%)</td><td>0.12 (+4.20%)</td><td>0.12 (+6.52%)</td><td>0.10 (-10.77%)</td><td>0.02 <b>(+104.42%)</b></td><td>206.30 (+12.06%)</td><td>167.98 (-2.35%)</td><td>168.60 (-6.12%)</td><td>133.50 (-12.46%)</td><td>28.50 <b>(+98.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>172.02 (n/a)</td><td>179.60 (n/a)</td><td>152.50 (n/a)</td><td>14.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (-5.26%)</td><td>0.11 (-6.42%)</td><td>0.10 (-8.82%)</td><td>0.09 (+18.63%)</td><td>0.03 (-16.15%)</td><td>216.80 (-15.71%)</td><td>188.26 (+3.94%)</td><td>201.40 (+9.69%)</td><td>118.40 (+5.53%)</td><td>39.75 <b>(-27.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>257.20 (n/a)</td><td>181.12 (n/a)</td><td>183.60 (n/a)</td><td>112.20 (n/a)</td><td>54.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (-3.18%)</td><td>0.10 (-12.92%)</td><td>0.10 (-13.73%)</td><td>0.08 <b>(-20.60%)</b></td><td>0.02 <b>(+39.19%)</b></td><td>250.30 <b>(+25.97%)</b></td><td>209.62 (+16.71%)</td><td>213.20 (+15.93%)</td><td>151.60 (+3.27%)</td><td>35.90 <b>(+75.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>179.60 (n/a)</td><td>183.90 (n/a)</td><td>146.80 (n/a)</td><td>20.47 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (-11.09%)</td><td>0.15 (-3.39%)</td><td>0.15 (-2.26%)</td><td>0.13 <b>(+27.26%)</b></td><td>0.02 <b>(-42.17%)</b></td><td>193.80 <b>(-21.41%)</b></td><td>164.18 (-0.82%)</td><td>161.60 (+2.28%)</td><td>132.00 (+12.44%)</td><td>24.45 <b>(-50.26%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>246.60 (n/a)</td><td>165.54 (n/a)</td><td>158.00 (n/a)</td><td>117.40 (n/a)</td><td>49.16 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (+7.99%)</td><td>0.15 (+4.50%)</td><td>0.16 (+5.89%)</td><td>0.11 <b>(+21.48%)</b></td><td>0.03 (-9.19%)</td><td>218.90 (-17.71%)</td><td>169.06 (-5.92%)</td><td>154.20 (-5.51%)</td><td>140.50 (-7.38%)</td><td>32.84 <b>(-32.52%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>266.00 (n/a)</td><td>179.70 (n/a)</td><td>163.20 (n/a)</td><td>151.70 (n/a)</td><td>48.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (+16.70%)</td><td>0.16 (+9.34%)</td><td>0.16 (+7.00%)</td><td>0.13 (-2.50%)</td><td>0.02 <b>(+103.19%)</b></td><td>184.40 (+2.56%)</td><td>154.50 (-7.63%)</td><td>155.40 (-6.55%)</td><td>128.90 (-14.30%)</td><td>20.33 <b>(+79.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>179.80 (n/a)</td><td>167.26 (n/a)</td><td>166.30 (n/a)</td><td>150.40 (n/a)</td><td>11.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 <b>(+20.35%)</b></td><td>0.14 (-5.55%)</td><td>0.13 (-11.59%)</td><td>0.10 <b>(-23.36%)</b></td><td>0.04 <b>(+186.34%)</b></td><td>237.10 <b>(+30.49%)</b></td><td>181.64 (+10.18%)</td><td>183.00 (+13.10%)</td><td>122.30 (-16.92%)</td><td>40.86 <b>(+197.73%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>181.70 (n/a)</td><td>164.86 (n/a)</td><td>161.80 (n/a)</td><td>147.20 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 <b>(-28.54%)</b></td><td>0.13 <b>(-20.85%)</b></td><td>0.13 <b>(-32.10%)</b></td><td>0.11 (+1.43%)</td><td>0.01 <b>(-77.97%)</b></td><td>215.40 (-1.42%)</td><td>192.08 (+19.89%)</td><td>190.50 <b>(+47.33%)</b></td><td>178.30 <b>(+39.95%)</b></td><td>14.07 <b>(-68.30%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>218.50 (n/a)</td><td>160.22 (n/a)</td><td>129.30 (n/a)</td><td>127.40 (n/a)</td><td>44.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (-1.50%)</td><td>0.16 (-1.88%)</td><td>0.16 (+0.53%)</td><td>0.12 (+0.06%)</td><td>0.03 (-17.69%)</td><td>198.90 (-0.05%)</td><td>156.66 (+1.08%)</td><td>154.60 (-0.58%)</td><td>127.80 (+1.59%)</td><td>26.51 (-12.66%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.00 (n/a)</td><td>154.98 (n/a)</td><td>155.50 (n/a)</td><td>125.80 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 <b>(-22.58%)</b></td><td>0.12 (-12.99%)</td><td>0.12 (-3.29%)</td><td>0.10 (-13.43%)</td><td>0.02 <b>(-39.55%)</b></td><td>243.10 (+15.54%)</td><td>203.02 (+12.61%)</td><td>203.00 (+3.41%)</td><td>151.70 <b>(+29.11%)</b></td><td>33.98 (-9.43%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>210.40 (n/a)</td><td>180.28 (n/a)</td><td>196.30 (n/a)</td><td>117.50 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 <b>(+28.99%)</b></td><td>0.13 (+13.47%)</td><td>0.13 (+11.58%)</td><td>0.11 (+0.61%)</td><td>0.02 <b>(+241.11%)</b></td><td>222.30 (-0.63%)</td><td>187.68 (-10.26%)</td><td>183.70 (-10.35%)</td><td>153.10 <b>(-22.48%)</b></td><td>29.85 <b>(+165.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>209.14 (n/a)</td><td>204.90 (n/a)</td><td>197.50 (n/a)</td><td>11.26 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 <b>(+21.34%)</b></td><td>0.13 (+11.49%)</td><td>0.14 (+10.50%)</td><td>0.09 (-8.86%)</td><td>0.03 <b>(+120.62%)</b></td><td>196.40 (+9.72%)</td><td>147.12 (-7.95%)</td><td>134.50 (-9.55%)</td><td>121.40 (-17.64%)</td><td>32.00 <b>(+96.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>179.00 (n/a)</td><td>159.82 (n/a)</td><td>148.70 (n/a)</td><td>147.40 (n/a)</td><td>16.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (+7.60%)</td><td>0.12 (+2.67%)</td><td>0.12 (+1.51%)</td><td>0.09 (-4.83%)</td><td>0.02 <b>(+46.77%)</b></td><td>194.90 (+5.07%)</td><td>158.42 (-1.35%)</td><td>153.40 (-1.48%)</td><td>126.70 (-7.11%)</td><td>28.06 <b>(+43.11%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>160.58 (n/a)</td><td>155.70 (n/a)</td><td>136.40 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (+14.20%)</td><td>0.11 (+0.31%)</td><td>0.10 (-7.83%)</td><td>0.09 (+14.37%)</td><td>0.03 <b>(+24.32%)</b></td><td>205.00 (-12.58%)</td><td>172.30 (+0.10%)</td><td>181.00 (+8.45%)</td><td>114.20 (-12.42%)</td><td>34.48 (-11.38%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>234.50 (n/a)</td><td>172.12 (n/a)</td><td>166.90 (n/a)</td><td>130.40 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-4.35%)</td><td>0.11 (-5.18%)</td><td>0.10 (-8.95%)</td><td>0.10 (+3.08%)</td><td>0.01 <b>(-22.20%)</b></td><td>189.50 (-2.97%)</td><td>173.12 (+4.69%)</td><td>178.00 (+9.81%)</td><td>141.10 (+4.60%)</td><td>19.29 <b>(-22.87%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>165.36 (n/a)</td><td>162.10 (n/a)</td><td>134.90 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (-11.28%)</td><td>0.10 (-19.72%)</td><td>0.09 (-18.81%)</td><td>0.06 <b>(-47.99%)</b></td><td>0.03 <b>(+108.69%)</b></td><td>312.10 <b>(+92.30%)</b></td><td>203.72 <b>(+32.79%)</b></td><td>196.50 <b>(+23.20%)</b></td><td>144.40 (+12.72%)</td><td>66.05 <b>(+363.05%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>162.30 (n/a)</td><td>153.42 (n/a)</td><td>159.50 (n/a)</td><td>128.10 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 <b>(-34.84%)</b></td><td>0.09 <b>(-26.21%)</b></td><td>0.09 <b>(-32.68%)</b></td><td>0.09 (+3.04%)</td><td>0.01 <b>(-82.79%)</b></td><td>214.90 (-2.98%)</td><td>198.02 <b>(+29.04%)</b></td><td>197.90 <b>(+48.57%)</b></td><td>185.20 <b>(+53.44%)</b></td><td>10.88 <b>(-74.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>153.46 (n/a)</td><td>133.20 (n/a)</td><td>120.70 (n/a)</td><td>42.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 <b>(+37.08%)</b></td><td>0.11 <b>(+20.39%)</b></td><td>0.11 <b>(+22.05%)</b></td><td>0.08 (+11.52%)</td><td>0.02 <b>(+120.75%)</b></td><td>222.60 (-10.35%)</td><td>179.76 (-14.83%)</td><td>173.90 (-18.09%)</td><td>135.50 <b>(-27.03%)</b></td><td>37.88 <b>(+49.17%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>248.30 (n/a)</td><td>211.06 (n/a)</td><td>212.30 (n/a)</td><td>185.70 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 <b>(-27.83%)</b></td><td>0.07 <b>(-34.46%)</b></td><td>0.07 <b>(-25.73%)</b></td><td>0.05 <b>(-44.10%)</b></td><td>0.02 (-3.66%)</td><td>371.10 <b>(+78.93%)</b></td><td>273.08 <b>(+58.93%)</b></td><td>252.10 <b>(+34.67%)</b></td><td>176.60 <b>(+38.62%)</b></td><td>80.10 <b>(+147.18%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>171.82 (n/a)</td><td>187.20 (n/a)</td><td>127.40 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.69 (-5.11%)</td><td>0.55 (-7.64%)</td><td>0.57 (-4.03%)</td><td>0.41 (+5.69%)</td><td>0.11 <b>(-26.69%)</b></td><td>242.50 (-5.38%)</td><td>185.80 (+5.62%)</td><td>172.50 (+4.17%)</td><td>142.00 (+5.42%)</td><td>37.83 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (n/a)</td><td>0.59 (n/a)</td><td>0.59 (n/a)</td><td>0.38 (n/a)</td><td>0.15 (n/a)</td><td>256.30 (n/a)</td><td>175.92 (n/a)</td><td>165.60 (n/a)</td><td>134.70 (n/a)</td><td>50.09 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.77 (+4.56%)</td><td>0.65 (+11.57%)</td><td>0.65 <b>(+20.68%)</b></td><td>0.54 (+9.21%)</td><td>0.08 (-11.95%)</td><td>183.00 (-8.41%)</td><td>154.12 (-10.89%)</td><td>151.30 (-17.14%)</td><td>127.40 (-4.35%)</td><td>19.98 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.74 (n/a)</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.10 (n/a)</td><td>199.80 (n/a)</td><td>172.96 (n/a)</td><td>182.60 (n/a)</td><td>133.20 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.58 <b>(-29.92%)</b></td><td>0.52 <b>(-21.27%)</b></td><td>0.54 (-19.35%)</td><td>0.47 (-15.48%)</td><td>0.05 <b>(-53.83%)</b></td><td>209.20 (+18.26%)</td><td>189.36 <b>(+25.40%)</b></td><td>180.70 <b>(+24.02%)</b></td><td>169.20 <b>(+42.66%)</b></td><td>18.33 <b>(-21.03%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.83 (n/a)</td><td>0.66 (n/a)</td><td>0.67 (n/a)</td><td>0.56 (n/a)</td><td>0.11 (n/a)</td><td>176.90 (n/a)</td><td>151.00 (n/a)</td><td>145.70 (n/a)</td><td>118.60 (n/a)</td><td>23.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.49 <b>(-33.00%)</b></td><td>0.43 <b>(-23.46%)</b></td><td>0.42 <b>(-22.27%)</b></td><td>0.39 (-12.46%)</td><td>0.04 <b>(-66.91%)</b></td><td>249.00 (+14.27%)</td><td>229.10 <b>(+27.83%)</b></td><td>233.20 <b>(+28.63%)</b></td><td>202.00 <b>(+49.30%)</b></td><td>18.02 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.11 (n/a)</td><td>217.90 (n/a)</td><td>179.22 (n/a)</td><td>181.30 (n/a)</td><td>135.30 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.56 (+15.76%)</td><td>0.46 (+6.03%)</td><td>0.44 (+2.65%)</td><td>0.35 (-12.22%)</td><td>0.10 <b>(+188.35%)</b></td><td>211.50 (+13.95%)</td><td>167.26 (-2.45%)</td><td>167.50 (-2.56%)</td><td>131.00 (-13.65%)</td><td>36.43 <b>(+175.83%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.03 (n/a)</td><td>185.60 (n/a)</td><td>171.46 (n/a)</td><td>171.90 (n/a)</td><td>151.70 (n/a)</td><td>13.21 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.53 (-3.29%)</td><td>0.45 (+3.51%)</td><td>0.43 (-7.05%)</td><td>0.38 (+18.92%)</td><td>0.06 <b>(-35.61%)</b></td><td>193.40 (-15.88%)</td><td>165.80 (-5.89%)</td><td>172.80 (+7.60%)</td><td>138.40 (+3.44%)</td><td>22.18 <b>(-45.45%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>229.90 (n/a)</td><td>176.18 (n/a)</td><td>160.60 (n/a)</td><td>133.80 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.45 <b>(-22.33%)</b></td><td>0.40 (-9.68%)</td><td>0.38 (-13.84%)</td><td>0.37 (+12.86%)</td><td>0.03 <b>(-66.41%)</b></td><td>201.70 (-11.38%)</td><td>186.82 (+7.16%)</td><td>192.20 (+16.06%)</td><td>164.20 <b>(+28.78%)</b></td><td>14.26 <b>(-62.24%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>227.60 (n/a)</td><td>174.34 (n/a)</td><td>165.60 (n/a)</td><td>127.50 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.49 <b>(-32.89%)</b></td><td>0.39 (-12.04%)</td><td>0.38 (-0.73%)</td><td>0.32 (+10.85%)</td><td>0.06 <b>(-62.58%)</b></td><td>227.90 (-9.78%)</td><td>192.82 (+5.19%)</td><td>191.60 (+0.74%)</td><td>151.50 <b>(+48.97%)</b></td><td>29.90 <b>(-48.14%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>252.60 (n/a)</td><td>183.30 (n/a)</td><td>190.20 (n/a)</td><td>101.70 (n/a)</td><td>57.66 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-8.58%)</td><td>0.21 (-12.10%)</td><td>0.19 (-14.90%)</td><td>0.18 (+1.32%)</td><td>0.04 <b>(-25.89%)</b></td><td>209.90 (-1.32%)</td><td>178.74 (+11.95%)</td><td>194.70 (+17.50%)</td><td>134.70 (+9.42%)</td><td>31.22 (-16.56%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>212.70 (n/a)</td><td>159.66 (n/a)</td><td>165.70 (n/a)</td><td>123.10 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (-5.89%)</td><td>0.21 (-6.07%)</td><td>0.23 (-0.83%)</td><td>0.15 (-16.63%)</td><td>0.04 (+17.89%)</td><td>241.10 (+19.95%)</td><td>181.24 (+8.18%)</td><td>158.70 (+0.89%)</td><td>142.60 (+6.26%)</td><td>40.87 <b>(+49.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>201.00 (n/a)</td><td>167.54 (n/a)</td><td>157.30 (n/a)</td><td>134.20 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (+1.75%)</td><td>0.20 (-14.47%)</td><td>0.18 <b>(-24.40%)</b></td><td>0.15 (-10.39%)</td><td>0.05 (+19.20%)</td><td>247.00 (+11.61%)</td><td>196.84 (+18.74%)</td><td>207.80 <b>(+32.27%)</b></td><td>130.70 (-1.73%)</td><td>44.12 <b>(+25.99%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>221.30 (n/a)</td><td>165.78 (n/a)</td><td>157.10 (n/a)</td><td>133.00 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (-4.35%)</td><td>0.19 (-16.58%)</td><td>0.18 (-19.77%)</td><td>0.14 <b>(-23.86%)</b></td><td>0.05 <b>(+34.12%)</b></td><td>260.30 <b>(+31.33%)</b></td><td>203.82 <b>(+23.30%)</b></td><td>205.00 <b>(+24.62%)</b></td><td>135.30 (+4.56%)</td><td>46.83 <b>(+80.54%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>198.20 (n/a)</td><td>165.30 (n/a)</td><td>164.50 (n/a)</td><td>129.40 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.32 (+11.12%)</td><td>0.20 (-7.71%)</td><td>0.19 (-12.00%)</td><td>0.15 (-12.57%)</td><td>0.07 <b>(+51.06%)</b></td><td>240.30 (+14.37%)</td><td>191.70 (+12.16%)</td><td>190.80 (+13.64%)</td><td>116.20 (-9.99%)</td><td>47.25 <b>(+48.49%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>210.10 (n/a)</td><td>170.92 (n/a)</td><td>167.90 (n/a)</td><td>129.10 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (-9.06%)</td><td>0.24 (-9.83%)</td><td>0.24 (-13.21%)</td><td>0.19 (+0.13%)</td><td>0.03 <b>(-36.14%)</b></td><td>193.70 (-0.15%)</td><td>158.00 (+9.00%)</td><td>153.20 (+15.27%)</td><td>132.40 (+9.97%)</td><td>22.25 <b>(-27.91%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>194.00 (n/a)</td><td>144.96 (n/a)</td><td>132.90 (n/a)</td><td>120.40 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (+2.49%)</td><td>0.21 (+5.69%)</td><td>0.19 (-0.68%)</td><td>0.18 (+19.76%)</td><td>0.03 (-4.92%)</td><td>206.90 (-16.47%)</td><td>182.20 (-5.97%)</td><td>191.30 (+0.68%)</td><td>150.20 (-2.40%)</td><td>26.57 <b>(-23.27%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>247.70 (n/a)</td><td>193.76 (n/a)</td><td>190.00 (n/a)</td><td>153.90 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (+7.87%)</td><td>0.21 (+6.95%)</td><td>0.20 (+8.36%)</td><td>0.19 <b>(+20.50%)</b></td><td>0.02 (-14.10%)</td><td>194.40 (-17.03%)</td><td>180.58 (-7.22%)</td><td>184.30 (-7.71%)</td><td>147.50 (-7.29%)</td><td>19.14 <b>(-34.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>234.30 (n/a)</td><td>194.64 (n/a)</td><td>199.70 (n/a)</td><td>159.10 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-19.35%)</td><td>0.23 (-0.15%)</td><td>0.23 (+4.36%)</td><td>0.21 (+15.16%)</td><td>0.02 <b>(-68.96%)</b></td><td>195.10 (-13.17%)</td><td>182.18 (-2.99%)</td><td>182.00 (-4.16%)</td><td>163.20 <b>(+24.01%)</b></td><td>12.39 <b>(-66.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>224.70 (n/a)</td><td>187.80 (n/a)</td><td>189.90 (n/a)</td><td>131.60 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (+1.61%)</td><td>0.27 (+16.78%)</td><td>0.28 (+18.53%)</td><td>0.23 <b>(+38.82%)</b></td><td>0.03 <b>(-45.97%)</b></td><td>175.70 <b>(-27.96%)</b></td><td>152.52 (-17.01%)</td><td>148.20 (-15.60%)</td><td>132.90 (-1.56%)</td><td>15.88 <b>(-61.74%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>243.90 (n/a)</td><td>183.78 (n/a)</td><td>175.60 (n/a)</td><td>135.00 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (+16.87%)</td><td>0.25 (+1.94%)</td><td>0.25 (-1.08%)</td><td>0.18 (-16.31%)</td><td>0.06 <b>(+155.74%)</b></td><td>227.10 (+19.46%)</td><td>170.96 (+1.67%)</td><td>162.50 (+1.12%)</td><td>131.00 (-14.44%)</td><td>40.13 <b>(+158.21%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>168.16 (n/a)</td><td>160.70 (n/a)</td><td>153.10 (n/a)</td><td>15.54 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 <b>(-23.05%)</b></td><td>0.23 (-19.60%)</td><td>0.23 (-12.83%)</td><td>0.19 <b>(-25.09%)</b></td><td>0.03 <b>(-25.96%)</b></td><td>221.20 <b>(+33.49%)</b></td><td>182.18 <b>(+24.29%)</b></td><td>178.20 (+14.67%)</td><td>147.70 <b>(+29.90%)</b></td><td>26.59 <b>(+31.48%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>165.70 (n/a)</td><td>146.58 (n/a)</td><td>155.40 (n/a)</td><td>113.70 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 <b>(-25.71%)</b></td><td>0.22 (-16.69%)</td><td>0.23 (-14.00%)</td><td>0.19 (-6.97%)</td><td>0.02 <b>(-61.42%)</b></td><td>215.40 (+7.54%)</td><td>184.28 (+16.31%)</td><td>180.70 (+16.28%)</td><td>163.70 <b>(+34.62%)</b></td><td>20.13 <b>(-43.34%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>200.30 (n/a)</td><td>158.44 (n/a)</td><td>155.40 (n/a)</td><td>121.60 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.34 <b>(+22.01%)</b></td><td>0.22 (-8.40%)</td><td>0.20 (-16.72%)</td><td>0.15 <b>(-27.77%)</b></td><td>0.07 <b>(+138.56%)</b></td><td>266.80 <b>(+38.45%)</b></td><td>197.38 (+15.28%)</td><td>200.60 <b>(+20.05%)</b></td><td>120.30 (-18.05%)</td><td>51.97 <b>(+150.43%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>192.70 (n/a)</td><td>171.22 (n/a)</td><td>167.10 (n/a)</td><td>146.80 (n/a)</td><td>20.75 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (-3.43%)</td><td>0.21 (-6.88%)</td><td>0.21 (-6.00%)</td><td>0.16 (-9.90%)</td><td>0.04 (+5.41%)</td><td>261.60 (+10.99%)</td><td>202.26 (+8.13%)</td><td>197.60 (+6.41%)</td><td>148.10 (+3.57%)</td><td>40.71 <b>(+20.58%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.70 (n/a)</td><td>187.06 (n/a)</td><td>185.70 (n/a)</td><td>143.00 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 <b>(-29.22%)</b></td><td>0.18 <b>(-23.08%)</b></td><td>0.19 (-14.02%)</td><td>0.14 <b>(-20.08%)</b></td><td>0.03 <b>(-37.20%)</b></td><td>287.50 <b>(+25.11%)</b></td><td>229.18 <b>(+28.68%)</b></td><td>218.00 (+16.33%)</td><td>184.80 <b>(+41.28%)</b></td><td>42.30 (+12.61%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>229.80 (n/a)</td><td>178.10 (n/a)</td><td>187.40 (n/a)</td><td>130.80 (n/a)</td><td>37.57 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 <b>(-26.81%)</b></td><td>0.17 (-18.26%)</td><td>0.17 (-16.84%)</td><td>0.14 (+4.02%)</td><td>0.02 <b>(-51.82%)</b></td><td>243.80 (-3.86%)</td><td>212.84 (+18.42%)</td><td>206.90 <b>(+20.22%)</b></td><td>181.70 <b>(+36.62%)</b></td><td>29.33 <b>(-36.65%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>253.60 (n/a)</td><td>179.74 (n/a)</td><td>172.10 (n/a)</td><td>133.00 (n/a)</td><td>46.29 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 <b>(-30.29%)</b></td><td>0.17 <b>(-23.46%)</b></td><td>0.17 <b>(-21.64%)</b></td><td>0.14 (-19.65%)</td><td>0.02 <b>(-53.64%)</b></td><td>250.20 <b>(+24.48%)</b></td><td>207.84 <b>(+28.57%)</b></td><td>200.90 <b>(+27.64%)</b></td><td>184.30 <b>(+43.42%)</b></td><td>25.10 (-15.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.00 (n/a)</td><td>161.66 (n/a)</td><td>157.40 (n/a)</td><td>128.50 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (+4.06%)</td><td>0.22 (+5.28%)</td><td>0.20 (+11.79%)</td><td>0.20 (+17.68%)</td><td>0.03 <b>(-32.12%)</b></td><td>177.10 (-15.02%)</td><td>160.24 (-7.33%)</td><td>172.10 (-10.55%)</td><td>126.60 (-3.87%)</td><td>21.28 <b>(-43.02%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>208.40 (n/a)</td><td>172.92 (n/a)</td><td>192.40 (n/a)</td><td>131.70 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (+4.51%)</td><td>0.19 (-4.91%)</td><td>0.19 (-3.71%)</td><td>0.16 (-10.73%)</td><td>0.03 <b>(+48.77%)</b></td><td>214.70 (+12.00%)</td><td>184.78 (+6.40%)</td><td>187.40 (+3.88%)</td><td>144.10 (-4.32%)</td><td>28.31 <b>(+59.65%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>191.70 (n/a)</td><td>173.66 (n/a)</td><td>180.40 (n/a)</td><td>150.60 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (-10.63%)</td><td>0.19 (-13.48%)</td><td>0.19 (-16.40%)</td><td>0.16 (-9.53%)</td><td>0.04 (-3.16%)</td><td>212.30 (+10.57%)</td><td>184.02 (+16.03%)</td><td>186.90 (+19.58%)</td><td>137.40 (+11.89%)</td><td>30.48 <b>(+21.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>192.00 (n/a)</td><td>158.60 (n/a)</td><td>156.30 (n/a)</td><td>122.80 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (+0.23%)</td><td>0.19 (-8.61%)</td><td>0.20 (-4.87%)</td><td>0.13 <b>(-27.62%)</b></td><td>0.06 <b>(+57.08%)</b></td><td>268.70 <b>(+38.15%)</b></td><td>192.16 (+14.89%)</td><td>173.80 (+5.14%)</td><td>131.40 (-0.23%)</td><td>57.61 <b>(+115.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>194.50 (n/a)</td><td>167.26 (n/a)</td><td>165.30 (n/a)</td><td>131.70 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (+1.22%)</td><td>0.19 (-0.10%)</td><td>0.18 (-5.90%)</td><td>0.18 (+11.34%)</td><td>0.02 <b>(-28.61%)</b></td><td>198.10 (-10.16%)</td><td>182.90 (-0.82%)</td><td>192.80 (+6.28%)</td><td>155.70 (-1.21%)</td><td>17.65 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>220.50 (n/a)</td><td>184.42 (n/a)</td><td>181.40 (n/a)</td><td>157.60 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (-18.19%)</td><td>0.19 (-9.47%)</td><td>0.19 (-3.03%)</td><td>0.18 (-5.34%)</td><td>0.01 <b>(-60.94%)</b></td><td>194.70 (+5.64%)</td><td>181.42 (+9.43%)</td><td>180.30 (+3.15%)</td><td>169.00 <b>(+22.29%)</b></td><td>9.84 <b>(-49.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>184.30 (n/a)</td><td>165.78 (n/a)</td><td>174.80 (n/a)</td><td>138.20 (n/a)</td><td>19.51 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.17 <b>(+26.24%)</b></td><td>0.81 <b>(+23.66%)</b></td><td>0.70 (+13.54%)</td><td>0.54 (-0.74%)</td><td>0.27 <b>(+73.63%)</b></td><td>243.00 (+0.75%)</td><td>175.60 (-15.12%)</td><td>188.00 (-11.90%)</td><td>112.20 <b>(-20.82%)</b></td><td>54.71 <b>(+38.06%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.93 (n/a)</td><td>0.66 (n/a)</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.16 (n/a)</td><td>241.20 (n/a)</td><td>206.88 (n/a)</td><td>213.40 (n/a)</td><td>141.70 (n/a)</td><td>39.62 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.03 (-15.74%)</td><td>0.80 (+0.41%)</td><td>0.78 (+16.12%)</td><td>0.65 (-0.07%)</td><td>0.15 <b>(-37.63%)</b></td><td>200.50 (+0.10%)</td><td>168.06 (-3.31%)</td><td>167.40 (-13.89%)</td><td>127.30 (+18.64%)</td><td>29.73 <b>(-24.71%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.22 (n/a)</td><td>0.80 (n/a)</td><td>0.67 (n/a)</td><td>0.65 (n/a)</td><td>0.24 (n/a)</td><td>200.30 (n/a)</td><td>173.82 (n/a)</td><td>194.40 (n/a)</td><td>107.30 (n/a)</td><td>39.48 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.98 <b>(+23.58%)</b></td><td>0.77 <b>(+20.58%)</b></td><td>0.73 (+7.75%)</td><td>0.67 <b>(+68.95%)</b></td><td>0.12 (-19.53%)</td><td>195.90 <b>(-40.80%)</b></td><td>173.24 <b>(-20.42%)</b></td><td>178.90 (-7.21%)</td><td>133.60 (-19.08%)</td><td>23.76 <b>(-64.07%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.79 (n/a)</td><td>0.64 (n/a)</td><td>0.68 (n/a)</td><td>0.40 (n/a)</td><td>0.15 (n/a)</td><td>330.90 (n/a)</td><td>217.68 (n/a)</td><td>192.80 (n/a)</td><td>165.10 (n/a)</td><td>66.12 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.00 (+0.00%)</td><td>0.00 (-1.80%)</td><td>0.00 (-2.22%)</td><td>0.00 (-4.65%)</td><td>0.00 <b>(+87.08%)</b></td><td>1007.71 (+6.22%)</td><td>941.81 (+1.81%)</td><td>928.24 (+1.01%)</td><td>909.89 (+0.42%)</td><td>40.73 <b>(+139.60%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>948.71 (n/a)</td><td>925.10 (n/a)</td><td>918.95 (n/a)</td><td>906.07 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.01 (-1.20%)</td><td>0.01 (+0.50%)</td><td>0.01 (-1.22%)</td><td>0.01 (+3.90%)</td><td>0.00 <b>(-64.96%)</b></td><td>1028.56 (-3.41%)</td><td>1009.21 (-0.22%)</td><td>1009.45 (+1.24%)</td><td>996.16 (+1.33%)</td><td>13.40 <b>(-58.78%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1064.88 (n/a)</td><td>1011.46 (n/a)</td><td>997.09 (n/a)</td><td>983.10 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.97 (+0.09%)</td><td>0.95 (+0.78%)</td><td>0.95 (+0.91%)</td><td>0.94 (+0.39%)</td><td>0.01 (-15.31%)</td><td>2224.76 (-0.39%)</td><td>2197.36 (-0.77%)</td><td>2201.82 (-0.90%)</td><td>2170.22 (-0.10%)</td><td>20.77 (-15.60%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2233.52 (n/a)</td><td>2214.50 (n/a)</td><td>2221.80 (n/a)</td><td>2172.30 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.66 (+6.66%)</td><td>5.23 (+15.47%)</td><td>5.26 (+18.75%)</td><td>4.68 (+17.16%)</td><td>0.43 (-15.13%)</td><td>223.90 (-14.67%)</td><td>201.72 (-13.77%)</td><td>199.50 (-15.79%)</td><td>185.20 (-6.23%)</td><td>17.00 <b>(-32.44%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.31 (n/a)</td><td>4.53 (n/a)</td><td>4.43 (n/a)</td><td>4.00 (n/a)</td><td>0.51 (n/a)</td><td>262.40 (n/a)</td><td>233.92 (n/a)</td><td>236.90 (n/a)</td><td>197.50 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.27 (-6.81%)</td><td>4.73 (+0.60%)</td><td>4.56 (-8.45%)</td><td>4.46 (+14.01%)</td><td>0.35 <b>(-52.85%)</b></td><td>235.30 (-12.30%)</td><td>222.50 (-2.20%)</td><td>229.80 (+9.22%)</td><td>199.00 (+7.28%)</td><td>15.81 <b>(-56.69%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.65 (n/a)</td><td>4.70 (n/a)</td><td>4.98 (n/a)</td><td>3.91 (n/a)</td><td>0.75 (n/a)</td><td>268.30 (n/a)</td><td>227.50 (n/a)</td><td>210.40 (n/a)</td><td>185.50 (n/a)</td><td>36.50 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.17 (+9.18%)</td><td>5.13 (+10.52%)</td><td>5.12 (+12.41%)</td><td>4.30 (+11.97%)</td><td>0.79 (+19.51%)</td><td>243.60 (-10.67%)</td><td>208.30 (-9.22%)</td><td>204.90 (-11.07%)</td><td>170.10 (-8.40%)</td><td>31.83 (+0.17%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.65 (n/a)</td><td>4.64 (n/a)</td><td>4.55 (n/a)</td><td>3.84 (n/a)</td><td>0.66 (n/a)</td><td>272.70 (n/a)</td><td>229.46 (n/a)</td><td>230.40 (n/a)</td><td>185.70 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.04 <b>(+24.00%)</b></td><td>5.04 (+17.13%)</td><td>4.85 (+17.60%)</td><td>4.51 (+16.51%)</td><td>0.62 <b>(+53.77%)</b></td><td>232.30 (-14.15%)</td><td>210.26 (-14.26%)</td><td>216.40 (-14.97%)</td><td>173.70 (-19.36%)</td><td>23.61 (+6.71%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.87 (n/a)</td><td>4.30 (n/a)</td><td>4.12 (n/a)</td><td>3.87 (n/a)</td><td>0.40 (n/a)</td><td>270.60 (n/a)</td><td>245.22 (n/a)</td><td>254.50 (n/a)</td><td>215.40 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.19 (-1.41%)</td><td>7.95 (-0.16%)</td><td>8.06 (+4.33%)</td><td>6.41 (-7.59%)</td><td>1.01 (+15.04%)</td><td>327.00 (+8.21%)</td><td>267.50 (+0.62%)</td><td>260.10 (-4.16%)</td><td>228.10 (+1.42%)</td><td>36.70 <b>(+30.36%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>9.33 (n/a)</td><td>7.96 (n/a)</td><td>7.73 (n/a)</td><td>6.94 (n/a)</td><td>0.88 (n/a)</td><td>302.20 (n/a)</td><td>265.86 (n/a)</td><td>271.40 (n/a)</td><td>224.90 (n/a)</td><td>28.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.62 (+8.05%)</td><td>7.79 (+2.36%)</td><td>7.82 (+1.46%)</td><td>6.95 (-4.18%)</td><td>0.71 <b>(+114.46%)</b></td><td>301.90 (+4.36%)</td><td>270.94 (-1.80%)</td><td>268.30 (-1.43%)</td><td>243.40 (-7.45%)</td><td>24.83 <b>(+105.98%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.98 (n/a)</td><td>7.61 (n/a)</td><td>7.70 (n/a)</td><td>7.25 (n/a)</td><td>0.33 (n/a)</td><td>289.30 (n/a)</td><td>275.90 (n/a)</td><td>272.20 (n/a)</td><td>263.00 (n/a)</td><td>12.05 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.56 (-0.59%)</td><td>7.74 (+1.97%)</td><td>7.81 (+7.76%)</td><td>7.15 (+0.79%)</td><td>0.60 (-5.62%)</td><td>293.50 (-0.78%)</td><td>272.34 (-1.97%)</td><td>268.40 (-7.19%)</td><td>245.10 (+0.62%)</td><td>20.85 (-4.51%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.61 (n/a)</td><td>7.59 (n/a)</td><td>7.25 (n/a)</td><td>7.09 (n/a)</td><td>0.64 (n/a)</td><td>295.80 (n/a)</td><td>277.82 (n/a)</td><td>289.20 (n/a)</td><td>243.60 (n/a)</td><td>21.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.92 (+10.99%)</td><td>8.26 (+12.92%)</td><td>8.72 (+10.43%)</td><td>6.42 (+8.41%)</td><td>1.04 (+11.66%)</td><td>326.50 (-7.77%)</td><td>257.86 (-11.36%)</td><td>240.60 (-9.45%)</td><td>235.00 (-9.89%)</td><td>38.63 (-4.59%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.04 (n/a)</td><td>7.31 (n/a)</td><td>7.89 (n/a)</td><td>5.92 (n/a)</td><td>0.93 (n/a)</td><td>354.00 (n/a)</td><td>290.90 (n/a)</td><td>265.70 (n/a)</td><td>260.80 (n/a)</td><td>40.49 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.60 (+6.63%)</td><td>8.08 (+4.37%)</td><td>7.98 (+0.23%)</td><td>7.30 <b>(+31.04%)</b></td><td>0.94 <b>(-31.87%)</b></td><td>287.50 <b>(-23.68%)</b></td><td>262.10 (-6.07%)</td><td>262.70 (-0.23%)</td><td>218.50 (-6.22%)</td><td>28.10 <b>(-51.68%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>9.00 (n/a)</td><td>7.74 (n/a)</td><td>7.97 (n/a)</td><td>5.57 (n/a)</td><td>1.37 (n/a)</td><td>376.70 (n/a)</td><td>279.04 (n/a)</td><td>263.30 (n/a)</td><td>233.00 (n/a)</td><td>58.15 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>10.02 (+19.95%)</td><td>8.65 (+18.79%)</td><td>8.22 (+8.13%)</td><td>7.49 <b>(+36.25%)</b></td><td>1.09 (+1.83%)</td><td>280.00 <b>(-26.61%)</b></td><td>245.48 (-16.49%)</td><td>255.00 (-7.54%)</td><td>209.40 (-16.61%)</td><td>30.08 <b>(-40.64%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.35 (n/a)</td><td>7.28 (n/a)</td><td>7.60 (n/a)</td><td>5.50 (n/a)</td><td>1.07 (n/a)</td><td>381.50 (n/a)</td><td>293.94 (n/a)</td><td>275.80 (n/a)</td><td>251.10 (n/a)</td><td>50.67 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.45 (+3.74%)</td><td>11.59 (+1.51%)</td><td>12.23 (+6.91%)</td><td>10.29 (-6.96%)</td><td>1.01 <b>(+170.42%)</b></td><td>407.50 (+7.46%)</td><td>364.32 (-0.95%)</td><td>343.00 (-6.46%)</td><td>337.00 (-3.60%)</td><td>32.96 <b>(+178.63%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.00 (n/a)</td><td>11.41 (n/a)</td><td>11.44 (n/a)</td><td>11.06 (n/a)</td><td>0.37 (n/a)</td><td>379.20 (n/a)</td><td>367.80 (n/a)</td><td>366.70 (n/a)</td><td>349.60 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.94 (+0.71%)</td><td>12.12 (+8.04%)</td><td>12.14 (+9.62%)</td><td>11.22 (+13.18%)</td><td>0.64 <b>(-43.21%)</b></td><td>373.70 (-11.63%)</td><td>346.90 (-7.96%)</td><td>345.40 (-8.79%)</td><td>324.20 (-0.70%)</td><td>18.55 <b>(-49.89%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.85 (n/a)</td><td>11.22 (n/a)</td><td>11.08 (n/a)</td><td>9.92 (n/a)</td><td>1.13 (n/a)</td><td>422.90 (n/a)</td><td>376.92 (n/a)</td><td>378.70 (n/a)</td><td>326.50 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.88 (+13.35%)</td><td>11.95 (+8.97%)</td><td>12.07 (+12.47%)</td><td>10.05 (-1.90%)</td><td>1.46 <b>(+76.48%)</b></td><td>417.30 (+1.95%)</td><td>355.16 (-7.52%)</td><td>347.50 (-11.08%)</td><td>302.10 (-11.80%)</td><td>43.98 <b>(+59.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.25 (n/a)</td><td>10.97 (n/a)</td><td>10.73 (n/a)</td><td>10.25 (n/a)</td><td>0.83 (n/a)</td><td>409.30 (n/a)</td><td>384.02 (n/a)</td><td>390.80 (n/a)</td><td>342.50 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.97 (-5.82%)</td><td>12.22 (-3.17%)</td><td>12.23 (-2.94%)</td><td>11.15 (+0.25%)</td><td>0.75 <b>(-26.17%)</b></td><td>376.10 (-0.27%)</td><td>344.20 (+3.04%)</td><td>343.00 (+3.03%)</td><td>323.30 (+6.17%)</td><td>21.68 <b>(-22.59%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.77 (n/a)</td><td>12.62 (n/a)</td><td>12.60 (n/a)</td><td>11.12 (n/a)</td><td>1.02 (n/a)</td><td>377.10 (n/a)</td><td>334.06 (n/a)</td><td>332.90 (n/a)</td><td>304.50 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.88 (+7.28%)</td><td>12.69 (+6.88%)</td><td>12.55 (+5.97%)</td><td>11.18 (+2.90%)</td><td>1.01 <b>(+29.69%)</b></td><td>375.30 (-2.82%)</td><td>332.36 (-6.27%)</td><td>334.10 (-5.62%)</td><td>302.10 (-6.79%)</td><td>27.52 (+18.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.94 (n/a)</td><td>11.87 (n/a)</td><td>11.85 (n/a)</td><td>10.86 (n/a)</td><td>0.78 (n/a)</td><td>386.20 (n/a)</td><td>354.58 (n/a)</td><td>354.00 (n/a)</td><td>324.10 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.40 (+3.78%)</td><td>12.92 (+4.24%)</td><td>12.80 (+3.41%)</td><td>12.63 (+6.54%)</td><td>0.33 (-19.67%)</td><td>332.00 (-6.14%)</td><td>324.74 (-4.09%)</td><td>327.60 (-3.31%)</td><td>313.00 (-3.63%)</td><td>8.09 <b>(-27.32%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.91 (n/a)</td><td>12.40 (n/a)</td><td>12.38 (n/a)</td><td>11.86 (n/a)</td><td>0.41 (n/a)</td><td>353.70 (n/a)</td><td>338.60 (n/a)</td><td>338.80 (n/a)</td><td>324.80 (n/a)</td><td>11.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.79 (-12.54%)</td><td>11.74 (-5.25%)</td><td>11.99 (+0.85%)</td><td>9.48 (+0.60%)</td><td>1.32 <b>(-37.48%)</b></td><td>442.50 (-0.61%)</td><td>361.52 (+4.14%)</td><td>349.80 (-0.85%)</td><td>327.90 (+14.33%)</td><td>46.49 <b>(-26.75%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>14.63 (n/a)</td><td>12.39 (n/a)</td><td>11.89 (n/a)</td><td>9.42 (n/a)</td><td>2.11 (n/a)</td><td>445.20 (n/a)</td><td>347.16 (n/a)</td><td>352.80 (n/a)</td><td>286.80 (n/a)</td><td>63.46 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>14.44 (+15.84%)</td><td>12.98 (+16.16%)</td><td>12.72 (+9.49%)</td><td>11.85 <b>(+38.69%)</b></td><td>0.97 <b>(-36.84%)</b></td><td>353.90 <b>(-27.89%)</b></td><td>324.50 (-15.07%)</td><td>329.70 (-8.67%)</td><td>290.50 (-13.67%)</td><td>23.58 <b>(-62.04%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.47 (n/a)</td><td>11.18 (n/a)</td><td>11.62 (n/a)</td><td>8.55 (n/a)</td><td>1.53 (n/a)</td><td>490.80 (n/a)</td><td>382.10 (n/a)</td><td>361.00 (n/a)</td><td>336.50 (n/a)</td><td>62.13 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.64 (+13.85%)</td><td>3.18 (+19.30%)</td><td>3.23 <b>(+23.62%)</b></td><td>2.53 (+15.06%)</td><td>0.44 (+11.82%)</td><td>207.50 (-13.07%)</td><td>167.64 (-16.21%)</td><td>162.30 (-19.13%)</td><td>143.90 (-12.15%)</td><td>24.98 (-13.59%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.20 (n/a)</td><td>2.66 (n/a)</td><td>2.61 (n/a)</td><td>2.20 (n/a)</td><td>0.39 (n/a)</td><td>238.70 (n/a)</td><td>200.08 (n/a)</td><td>200.70 (n/a)</td><td>163.80 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.84 <b>(+28.53%)</b></td><td>5.08 (+19.01%)</td><td>4.86 (+10.43%)</td><td>4.40 (+19.83%)</td><td>0.60 <b>(+71.79%)</b></td><td>238.10 (-16.54%)</td><td>208.84 (-15.53%)</td><td>216.00 (-9.43%)</td><td>179.40 <b>(-22.20%)</b></td><td>24.22 (+9.22%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.55 (n/a)</td><td>4.27 (n/a)</td><td>4.40 (n/a)</td><td>3.68 (n/a)</td><td>0.35 (n/a)</td><td>285.30 (n/a)</td><td>247.24 (n/a)</td><td>238.50 (n/a)</td><td>230.60 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.11 (+15.66%)</td><td>7.53 (+13.74%)</td><td>7.40 (+12.82%)</td><td>7.20 (+13.45%)</td><td>0.35 <b>(+31.20%)</b></td><td>291.40 (-11.83%)</td><td>279.12 (-12.04%)</td><td>283.40 (-11.35%)</td><td>258.70 (-13.54%)</td><td>12.50 (-0.63%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.01 (n/a)</td><td>6.62 (n/a)</td><td>6.56 (n/a)</td><td>6.34 (n/a)</td><td>0.27 (n/a)</td><td>330.50 (n/a)</td><td>317.32 (n/a)</td><td>319.70 (n/a)</td><td>299.20 (n/a)</td><td>12.58 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.48 (+3.70%)</td><td>3.02 (+11.48%)</td><td>3.33 <b>(+26.13%)</b></td><td>2.18 (+4.33%)</td><td>0.57 <b>(+20.84%)</b></td><td>240.70 (-4.14%)</td><td>179.40 (-9.56%)</td><td>157.50 <b>(-20.73%)</b></td><td>150.90 (-3.52%)</td><td>38.69 (+9.65%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.35 (n/a)</td><td>2.71 (n/a)</td><td>2.64 (n/a)</td><td>2.09 (n/a)</td><td>0.47 (n/a)</td><td>251.10 (n/a)</td><td>198.36 (n/a)</td><td>198.70 (n/a)</td><td>156.40 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 <b>(+24.91%)</b></td><td>0.18 (+1.63%)</td><td>0.17 (+1.56%)</td><td>0.13 (+2.19%)</td><td>0.05 <b>(+42.41%)</b></td><td>249.90 (-2.12%)</td><td>197.04 (+0.66%)</td><td>191.80 (-1.54%)</td><td>122.20 (-19.97%)</td><td>49.71 (+13.34%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>255.30 (n/a)</td><td>195.74 (n/a)</td><td>194.80 (n/a)</td><td>152.70 (n/a)</td><td>43.86 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (+6.85%)</td><td>0.18 (+0.70%)</td><td>0.19 (+17.41%)</td><td>0.10 <b>(-31.19%)</b></td><td>0.06 <b>(+70.08%)</b></td><td>319.10 <b>(+45.31%)</b></td><td>203.36 (+8.09%)</td><td>171.70 (-14.83%)</td><td>126.90 (-6.42%)</td><td>80.11 <b>(+136.29%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.60 (n/a)</td><td>188.14 (n/a)</td><td>201.60 (n/a)</td><td>135.60 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.53 (+1.84%)</td><td>0.43 (+10.72%)</td><td>0.41 (+8.45%)</td><td>0.36 (+19.80%)</td><td>0.06 <b>(-21.76%)</b></td><td>184.40 (-16.52%)</td><td>155.42 (-11.09%)</td><td>159.00 (-7.77%)</td><td>123.70 (-1.75%)</td><td>21.97 <b>(-35.31%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>220.90 (n/a)</td><td>174.80 (n/a)</td><td>172.40 (n/a)</td><td>125.90 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.46 (-14.30%)</td><td>0.41 (+6.16%)</td><td>0.43 (+15.92%)</td><td>0.37 (+19.62%)</td><td>0.04 <b>(-56.15%)</b></td><td>179.10 (-16.39%)</td><td>159.34 (-8.38%)</td><td>152.80 (-13.72%)</td><td>142.90 (+16.65%)</td><td>15.06 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>214.20 (n/a)</td><td>173.92 (n/a)</td><td>177.10 (n/a)</td><td>122.50 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.43 (-17.56%)</td><td>0.40 (+1.42%)</td><td>0.41 (+6.25%)</td><td>0.35 <b>(+24.04%)</b></td><td>0.03 <b>(-65.49%)</b></td><td>186.60 (-19.36%)</td><td>165.12 (-4.78%)</td><td>161.10 (-5.84%)</td><td>151.30 <b>(+21.23%)</b></td><td>13.27 <b>(-65.73%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.53 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>231.40 (n/a)</td><td>173.40 (n/a)</td><td>171.10 (n/a)</td><td>124.80 (n/a)</td><td>38.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.99 (-1.40%)</td><td>0.89 (+13.49%)</td><td>0.93 <b>(+24.01%)</b></td><td>0.73 <b>(+36.90%)</b></td><td>0.10 <b>(-42.39%)</b></td><td>178.60 <b>(-26.95%)</b></td><td>149.46 (-14.75%)</td><td>141.30 (-19.40%)</td><td>132.00 (+1.38%)</td><td>18.34 <b>(-57.53%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.01 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.54 (n/a)</td><td>0.17 (n/a)</td><td>244.50 (n/a)</td><td>175.32 (n/a)</td><td>175.30 (n/a)</td><td>130.20 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.85 (-16.17%)</td><td>0.77 (+7.83%)</td><td>0.81 <b>(+26.90%)</b></td><td>0.62 (+4.49%)</td><td>0.09 <b>(-46.66%)</b></td><td>210.40 (-4.28%)</td><td>173.40 (-9.66%)</td><td>161.00 <b>(-21.19%)</b></td><td>153.70 (+19.33%)</td><td>23.35 <b>(-38.10%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.02 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.60 (n/a)</td><td>0.18 (n/a)</td><td>219.80 (n/a)</td><td>191.94 (n/a)</td><td>204.30 (n/a)</td><td>128.80 (n/a)</td><td>37.72 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.04 (-8.25%)</td><td>0.87 (+10.23%)</td><td>0.84 (+9.88%)</td><td>0.74 <b>(+27.75%)</b></td><td>0.13 <b>(-38.11%)</b></td><td>176.10 <b>(-21.73%)</b></td><td>152.50 (-12.01%)</td><td>155.80 (-9.00%)</td><td>126.60 (+8.95%)</td><td>21.47 <b>(-45.51%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.13 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.58 (n/a)</td><td>0.20 (n/a)</td><td>225.00 (n/a)</td><td>173.32 (n/a)</td><td>171.20 (n/a)</td><td>116.20 (n/a)</td><td>39.41 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.93 (+9.31%)</td><td>0.78 (+5.37%)</td><td>0.85 (+2.40%)</td><td>0.51 (+1.28%)</td><td>0.17 (+8.86%)</td><td>259.30 (-1.26%)</td><td>175.46 (-4.61%)</td><td>154.70 (-2.34%)</td><td>140.50 (-8.53%)</td><td>48.26 (+3.25%)</td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.85 (n/a)</td><td>0.74 (n/a)</td><td>0.83 (n/a)</td><td>0.50 (n/a)</td><td>0.15 (n/a)</td><td>262.60 (n/a)</td><td>183.94 (n/a)</td><td>158.40 (n/a)</td><td>153.60 (n/a)</td><td>46.74 (n/a)</td>
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
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 <b>(-22.68%)</b></td><td>0.09 (-16.57%)</td><td>0.09 (-6.76%)</td><td>0.07 (-16.27%)</td><td>0.02 (-12.76%)</td><td>240.30 (+19.43%)</td><td>194.22 <b>(+20.56%)</b></td><td>178.10 (+7.22%)</td><td>157.40 <b>(+29.33%)</b></td><td>39.97 <b>(+38.23%)</b></td>
</tr>
<tr>
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.20 (n/a)</td><td>161.10 (n/a)</td><td>166.10 (n/a)</td><td>121.70 (n/a)</td><td>28.92 (n/a)</td>
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
