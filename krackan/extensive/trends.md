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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+6.76%)</td><td>0.04 (+18.66%)</td><td>0.04 (+17.71%)</td><td>0.03 <b>(+66.24%)</b></td><td>0.01 <b>(-29.37%)</b></td><td>191.00 <b>(-39.84%)</b></td><td>157.50 <b>(-20.81%)</b></td><td>162.60 (-15.05%)</td><td>128.80 (-6.33%)</td><td>27.64 <b>(-61.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>317.50 (n/a)</td><td>198.90 (n/a)</td><td>191.40 (n/a)</td><td>137.50 (n/a)</td><td>71.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+9.32%)</td><td>0.04 (+8.62%)</td><td>0.04 (+15.07%)</td><td>0.03 (-0.58%)</td><td>0.01 <b>(+26.70%)</b></td><td>202.00 (+0.60%)</td><td>158.80 (-7.22%)</td><td>152.70 (-13.09%)</td><td>126.30 (-8.48%)</td><td>27.61 (+19.96%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>171.16 (n/a)</td><td>175.70 (n/a)</td><td>138.00 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+7.09%)</td><td>0.04 (+17.60%)</td><td>0.04 <b>(+20.47%)</b></td><td>0.04 <b>(+31.89%)</b></td><td>0.00 <b>(-48.15%)</b></td><td>168.50 <b>(-24.17%)</b></td><td>158.14 (-16.13%)</td><td>160.90 (-16.98%)</td><td>142.50 (-6.62%)</td><td>9.98 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>222.20 (n/a)</td><td>188.56 (n/a)</td><td>193.80 (n/a)</td><td>152.60 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (-6.32%)</td><td>0.03 (-4.65%)</td><td>0.03 (-13.06%)</td><td>0.03 (+19.91%)</td><td>0.01 (-19.82%)</td><td>235.50 (-16.61%)</td><td>194.56 (+1.13%)</td><td>202.50 (+14.99%)</td><td>125.90 (+6.79%)</td><td>45.53 <b>(-28.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>282.40 (n/a)</td><td>192.38 (n/a)</td><td>176.10 (n/a)</td><td>117.90 (n/a)</td><td>63.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 <b>(+25.84%)</b></td><td>0.04 <b>(+33.66%)</b></td><td>0.04 <b>(+36.55%)</b></td><td>0.03 <b>(+47.00%)</b></td><td>0.01 (+5.10%)</td><td>199.40 <b>(-31.99%)</b></td><td>155.50 <b>(-26.41%)</b></td><td>150.60 <b>(-26.75%)</b></td><td>124.60 <b>(-20.54%)</b></td><td>28.43 <b>(-43.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>293.20 (n/a)</td><td>211.30 (n/a)</td><td>205.60 (n/a)</td><td>156.80 (n/a)</td><td>50.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+7.79%)</td><td>0.04 (-3.96%)</td><td>0.04 (+1.74%)</td><td>0.02 (-13.66%)</td><td>0.01 <b>(+42.88%)</b></td><td>267.50 (+15.85%)</td><td>182.88 (+8.44%)</td><td>154.60 (-1.72%)</td><td>125.00 (-7.20%)</td><td>58.64 <b>(+53.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>168.64 (n/a)</td><td>157.30 (n/a)</td><td>134.70 (n/a)</td><td>38.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+2.85%)</td><td>0.03 (-11.11%)</td><td>0.03 <b>(-24.14%)</b></td><td>0.02 <b>(-37.58%)</b></td><td>0.01 <b>(+96.42%)</b></td><td>342.30 <b>(+60.25%)</b></td><td>225.12 <b>(+23.03%)</b></td><td>244.90 <b>(+31.81%)</b></td><td>144.40 (-2.76%)</td><td>82.89 <b>(+179.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>182.98 (n/a)</td><td>185.80 (n/a)</td><td>148.50 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+7.11%)</td><td>0.03 (-7.90%)</td><td>0.03 <b>(-22.43%)</b></td><td>0.02 (+4.29%)</td><td>0.01 (+1.38%)</td><td>314.20 (-4.12%)</td><td>221.88 (+7.77%)</td><td>215.70 <b>(+28.93%)</b></td><td>142.90 (-6.60%)</td><td>65.99 (-9.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.70 (n/a)</td><td>205.88 (n/a)</td><td>167.30 (n/a)</td><td>153.00 (n/a)</td><td>73.08 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 <b>(+20.66%)</b></td><td>0.07 (+5.99%)</td><td>0.07 (-4.22%)</td><td>0.06 <b>(+62.06%)</b></td><td>0.02 (-13.98%)</td><td>217.60 <b>(-38.29%)</b></td><td>180.28 (-11.14%)</td><td>179.40 (+4.36%)</td><td>127.90 (-17.11%)</td><td>35.71 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>352.60 (n/a)</td><td>202.88 (n/a)</td><td>171.90 (n/a)</td><td>154.30 (n/a)</td><td>84.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (-1.60%)</td><td>0.07 (-3.50%)</td><td>0.08 <b>(+20.17%)</b></td><td>0.06 (-10.74%)</td><td>0.02 (+0.22%)</td><td>213.40 (+12.02%)</td><td>172.54 (+4.28%)</td><td>155.80 (-16.77%)</td><td>132.00 (+1.62%)</td><td>38.19 <b>(+20.42%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.50 (n/a)</td><td>165.46 (n/a)</td><td>187.20 (n/a)</td><td>129.90 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (-12.88%)</td><td>0.07 <b>(-21.26%)</b></td><td>0.07 <b>(-25.18%)</b></td><td>0.06 (-19.15%)</td><td>0.01 (-2.59%)</td><td>215.40 <b>(+23.65%)</b></td><td>179.82 <b>(+27.50%)</b></td><td>181.80 <b>(+33.68%)</b></td><td>140.70 (+14.76%)</td><td>26.49 <b>(+32.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>141.04 (n/a)</td><td>136.00 (n/a)</td><td>122.60 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (-8.96%)</td><td>0.07 (-14.03%)</td><td>0.07 (-17.63%)</td><td>0.06 (-1.05%)</td><td>0.01 <b>(-31.05%)</b></td><td>190.60 (+1.06%)</td><td>167.90 (+14.40%)</td><td>173.30 <b>(+21.36%)</b></td><td>128.30 (+9.85%)</td><td>23.57 <b>(-24.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>146.76 (n/a)</td><td>142.80 (n/a)</td><td>116.80 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (-8.75%)</td><td>0.06 (-19.87%)</td><td>0.06 (-16.76%)</td><td>0.03 <b>(-43.36%)</b></td><td>0.02 (+9.42%)</td><td>390.80 <b>(+76.51%)</b></td><td>226.14 <b>(+34.50%)</b></td><td>205.90 <b>(+20.13%)</b></td><td>128.90 (+9.61%)</td><td>100.82 <b>(+120.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>168.14 (n/a)</td><td>171.40 (n/a)</td><td>117.60 (n/a)</td><td>45.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 <b>(-20.17%)</b></td><td>0.07 (-19.58%)</td><td>0.07 (-11.18%)</td><td>0.05 (-11.08%)</td><td>0.01 <b>(-40.45%)</b></td><td>223.60 (+12.42%)</td><td>190.88 <b>(+22.11%)</b></td><td>188.30 (+12.62%)</td><td>148.70 <b>(+25.27%)</b></td><td>28.14 (-15.22%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>156.32 (n/a)</td><td>167.20 (n/a)</td><td>118.70 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 <b>(-26.86%)</b></td><td>0.06 (-8.41%)</td><td>0.06 (+5.30%)</td><td>0.05 <b>(+44.44%)</b></td><td>0.00 <b>(-85.04%)</b></td><td>224.70 <b>(-30.76%)</b></td><td>211.20 (-0.50%)</td><td>211.20 (-5.04%)</td><td>196.30 <b>(+36.70%)</b></td><td>11.38 <b>(-84.77%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>324.50 (n/a)</td><td>212.26 (n/a)</td><td>222.40 (n/a)</td><td>143.60 (n/a)</td><td>74.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(-23.16%)</b></td><td>0.07 <b>(-21.00%)</b></td><td>0.06 <b>(-31.62%)</b></td><td>0.06 (+10.55%)</td><td>0.01 <b>(-66.82%)</b></td><td>203.40 (-9.52%)</td><td>187.96 <b>(+21.97%)</b></td><td>196.20 <b>(+46.20%)</b></td><td>168.70 <b>(+30.17%)</b></td><td>15.37 <b>(-61.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.80 (n/a)</td><td>154.10 (n/a)</td><td>134.20 (n/a)</td><td>129.60 (n/a)</td><td>40.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 <b>(-28.34%)</b></td><td>0.14 (-9.64%)</td><td>0.15 (+1.95%)</td><td>0.13 (+15.67%)</td><td>0.01 <b>(-72.73%)</b></td><td>193.50 (-13.54%)</td><td>170.90 (+5.08%)</td><td>169.20 (-1.91%)</td><td>158.30 <b>(+39.59%)</b></td><td>14.43 <b>(-66.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>223.80 (n/a)</td><td>162.64 (n/a)</td><td>172.50 (n/a)</td><td>113.40 (n/a)</td><td>43.30 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (-18.93%)</td><td>0.14 <b>(-20.43%)</b></td><td>0.14 (-15.28%)</td><td>0.12 <b>(-20.11%)</b></td><td>0.02 (-2.50%)</td><td>202.10 <b>(+25.14%)</b></td><td>179.12 <b>(+26.18%)</b></td><td>170.80 (+18.04%)</td><td>153.30 <b>(+23.33%)</b></td><td>21.98 <b>(+55.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>161.50 (n/a)</td><td>141.96 (n/a)</td><td>144.70 (n/a)</td><td>124.30 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (-0.05%)</td><td>0.15 (+7.71%)</td><td>0.15 (-0.18%)</td><td>0.13 <b>(+23.69%)</b></td><td>0.02 <b>(-39.71%)</b></td><td>191.80 (-19.14%)</td><td>162.54 (-9.69%)</td><td>164.80 (+0.18%)</td><td>140.40 (+0.07%)</td><td>19.98 <b>(-51.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>237.20 (n/a)</td><td>179.98 (n/a)</td><td>164.50 (n/a)</td><td>140.30 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 <b>(-28.24%)</b></td><td>0.13 (-16.25%)</td><td>0.13 (-18.32%)</td><td>0.12 <b>(+32.07%)</b></td><td>0.01 <b>(-80.33%)</b></td><td>203.00 <b>(-24.28%)</b></td><td>186.78 (+11.47%)</td><td>185.30 <b>(+22.47%)</b></td><td>175.20 <b>(+39.27%)</b></td><td>11.40 <b>(-80.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>268.10 (n/a)</td><td>167.56 (n/a)</td><td>151.30 (n/a)</td><td>125.80 (n/a)</td><td>57.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (+1.32%)</td><td>0.13 (-19.86%)</td><td>0.13 <b>(-22.18%)</b></td><td>0.06 <b>(-50.27%)</b></td><td>0.04 <b>(+66.72%)</b></td><td>383.80 <b>(+101.15%)</b></td><td>218.86 <b>(+37.84%)</b></td><td>195.00 <b>(+28.46%)</b></td><td>130.10 (-1.29%)</td><td>96.55 <b>(+252.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.80 (n/a)</td><td>158.78 (n/a)</td><td>151.80 (n/a)</td><td>131.80 (n/a)</td><td>27.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (-17.16%)</td><td>0.13 <b>(-24.28%)</b></td><td>0.13 <b>(-27.62%)</b></td><td>0.08 <b>(-33.27%)</b></td><td>0.03 (+4.86%)</td><td>289.50 <b>(+49.84%)</b></td><td>204.26 <b>(+35.59%)</b></td><td>189.00 <b>(+38.16%)</b></td><td>151.20 <b>(+20.67%)</b></td><td>55.66 <b>(+91.14%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>193.20 (n/a)</td><td>150.64 (n/a)</td><td>136.80 (n/a)</td><td>125.30 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 <b>(-25.16%)</b></td><td>0.11 <b>(-20.12%)</b></td><td>0.11 <b>(-28.27%)</b></td><td>0.11 <b>(+43.33%)</b></td><td>0.01 <b>(-85.87%)</b></td><td>230.00 <b>(-30.22%)</b></td><td>218.36 (+14.59%)</td><td>218.00 <b>(+39.39%)</b></td><td>204.40 <b>(+33.59%)</b></td><td>10.14 <b>(-86.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>329.60 (n/a)</td><td>190.56 (n/a)</td><td>156.40 (n/a)</td><td>153.00 (n/a)</td><td>77.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (+0.04%)</td><td>0.13 (-0.17%)</td><td>0.13 (-5.11%)</td><td>0.10 <b>(+23.40%)</b></td><td>0.03 (-11.04%)</td><td>246.10 (-18.97%)</td><td>196.98 (-1.98%)</td><td>193.60 (+5.39%)</td><td>149.00 (-0.07%)</td><td>43.29 <b>(-29.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>303.70 (n/a)</td><td>200.96 (n/a)</td><td>183.70 (n/a)</td><td>149.10 (n/a)</td><td>61.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.33 (-0.85%)</td><td>0.27 (-5.00%)</td><td>0.27 (-3.99%)</td><td>0.20 (-19.06%)</td><td>0.05 <b>(+45.73%)</b></td><td>241.30 <b>(+23.55%)</b></td><td>188.34 (+6.95%)</td><td>185.10 (+4.16%)</td><td>148.30 (+0.88%)</td><td>34.32 <b>(+85.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>195.30 (n/a)</td><td>176.10 (n/a)</td><td>177.70 (n/a)</td><td>147.00 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 <b>(-24.98%)</b></td><td>0.27 (-12.52%)</td><td>0.27 (-12.60%)</td><td>0.25 (-4.38%)</td><td>0.02 <b>(-64.75%)</b></td><td>200.10 (+4.60%)</td><td>182.70 (+12.68%)</td><td>184.10 (+14.42%)</td><td>171.80 <b>(+33.28%)</b></td><td>11.49 <b>(-50.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>191.30 (n/a)</td><td>162.14 (n/a)</td><td>160.90 (n/a)</td><td>128.90 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.38 (+13.66%)</td><td>0.28 (-1.97%)</td><td>0.25 (-5.28%)</td><td>0.23 (+2.49%)</td><td>0.06 <b>(+20.32%)</b></td><td>213.40 (-2.47%)</td><td>184.10 (+2.60%)</td><td>196.80 (+5.58%)</td><td>129.70 (-12.01%)</td><td>32.24 (+3.15%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>218.80 (n/a)</td><td>179.44 (n/a)</td><td>186.40 (n/a)</td><td>147.40 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.37 (-2.29%)</td><td>0.25 (-13.38%)</td><td>0.22 (-19.01%)</td><td>0.20 (-12.82%)</td><td>0.07 (+15.74%)</td><td>249.80 (+14.69%)</td><td>209.72 (+17.44%)</td><td>221.60 <b>(+23.45%)</b></td><td>132.00 (+2.33%)</td><td>45.91 <b>(+30.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>217.80 (n/a)</td><td>178.58 (n/a)</td><td>179.50 (n/a)</td><td>129.00 (n/a)</td><td>35.30 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.39 <b>(+25.53%)</b></td><td>0.35 <b>(+30.47%)</b></td><td>0.36 <b>(+28.63%)</b></td><td>0.29 <b>(+25.46%)</b></td><td>0.05 <b>(+29.41%)</b></td><td>171.80 <b>(-20.32%)</b></td><td>144.26 <b>(-23.32%)</b></td><td>137.80 <b>(-22.23%)</b></td><td>126.30 <b>(-20.32%)</b></td><td>19.75 <b>(-20.68%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>215.60 (n/a)</td><td>188.14 (n/a)</td><td>177.20 (n/a)</td><td>158.50 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.32 (+7.91%)</td><td>0.29 (+10.77%)</td><td>0.28 (+3.56%)</td><td>0.26 (+14.29%)</td><td>0.03 (+10.85%)</td><td>188.80 (-12.51%)</td><td>170.44 (-9.73%)</td><td>177.80 (-3.42%)</td><td>152.30 (-7.30%)</td><td>16.99 (-12.35%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>188.82 (n/a)</td><td>184.10 (n/a)</td><td>164.30 (n/a)</td><td>19.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (+9.38%)</td><td>0.23 (+2.86%)</td><td>0.22 (-5.59%)</td><td>0.15 (+1.11%)</td><td>0.05 <b>(+24.92%)</b></td><td>319.20 (-1.12%)</td><td>224.26 (-1.56%)</td><td>224.70 (+5.89%)</td><td>165.20 (-8.53%)</td><td>59.36 (+8.18%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>322.80 (n/a)</td><td>227.82 (n/a)</td><td>212.20 (n/a)</td><td>180.60 (n/a)</td><td>54.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (+8.69%)</td><td>0.24 (-3.41%)</td><td>0.24 (-6.15%)</td><td>0.16 (-19.85%)</td><td>0.05 <b>(+84.42%)</b></td><td>299.10 <b>(+24.73%)</b></td><td>214.40 (+6.51%)</td><td>206.60 (+6.55%)</td><td>164.70 (-7.99%)</td><td>50.58 <b>(+116.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>239.80 (n/a)</td><td>201.30 (n/a)</td><td>193.90 (n/a)</td><td>179.00 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (-6.56%)</td><td>0.02 (+1.19%)</td><td>0.02 (-5.36%)</td><td>0.01 (+7.66%)</td><td>0.00 (-8.29%)</td><td>193.60 (-7.10%)</td><td>156.66 (-1.73%)</td><td>165.30 (+5.69%)</td><td>123.50 (+7.02%)</td><td>29.84 (-10.65%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>159.42 (n/a)</td><td>156.40 (n/a)</td><td>115.40 (n/a)</td><td>33.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+1.59%)</td><td>0.02 (+2.32%)</td><td>0.02 (+8.85%)</td><td>0.01 (-5.92%)</td><td>0.00 <b>(+20.54%)</b></td><td>195.40 (+6.31%)</td><td>158.12 (-0.99%)</td><td>155.90 (-8.13%)</td><td>117.70 (-1.51%)</td><td>32.38 <b>(+31.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>159.70 (n/a)</td><td>169.70 (n/a)</td><td>119.50 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 <b>(+21.43%)</b></td><td>0.02 (+7.82%)</td><td>0.02 (-6.53%)</td><td>0.01 <b>(+27.28%)</b></td><td>0.00 (+9.98%)</td><td>189.80 <b>(-21.44%)</b></td><td>157.94 (-8.23%)</td><td>160.30 (+7.01%)</td><td>112.00 (-17.65%)</td><td>29.45 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>241.60 (n/a)</td><td>172.10 (n/a)</td><td>149.80 (n/a)</td><td>136.00 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+4.42%)</td><td>0.02 (+6.09%)</td><td>0.02 (+6.57%)</td><td>0.01 (+3.66%)</td><td>0.00 (+19.26%)</td><td>184.90 (-3.50%)</td><td>162.12 (-5.43%)</td><td>160.30 (-6.15%)</td><td>137.40 (-4.25%)</td><td>20.40 (+13.12%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>171.42 (n/a)</td><td>170.80 (n/a)</td><td>143.50 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+6.66%)</td><td>0.01 (-9.99%)</td><td>0.01 (-13.83%)</td><td>0.01 (-10.14%)</td><td>0.00 <b>(+34.98%)</b></td><td>239.50 (+11.29%)</td><td>193.88 (+12.90%)</td><td>189.30 (+16.06%)</td><td>139.80 (-6.30%)</td><td>38.76 <b>(+41.52%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>171.72 (n/a)</td><td>163.10 (n/a)</td><td>149.20 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 <b>(+45.65%)</b></td><td>0.02 <b>(+23.25%)</b></td><td>0.02 <b>(+22.05%)</b></td><td>0.01 (+19.58%)</td><td>0.00 <b>(+105.33%)</b></td><td>196.70 (-16.37%)</td><td>159.50 (-17.72%)</td><td>153.80 (-18.06%)</td><td>122.50 <b>(-31.33%)</b></td><td>27.42 (+15.92%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>235.20 (n/a)</td><td>193.84 (n/a)</td><td>187.70 (n/a)</td><td>178.40 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+5.14%)</td><td>0.02 (+10.23%)</td><td>0.02 (+15.77%)</td><td>0.01 (+16.74%)</td><td>0.00 <b>(-25.59%)</b></td><td>199.20 (-14.32%)</td><td>173.84 (-10.42%)</td><td>173.40 (-13.60%)</td><td>145.00 (-4.86%)</td><td>19.41 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>232.50 (n/a)</td><td>194.06 (n/a)</td><td>200.70 (n/a)</td><td>152.40 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.01 (-11.65%)</td><td>0.01 (-5.24%)</td><td>0.01 (+0.40%)</td><td>0.01 (-7.49%)</td><td>0.00 (-14.17%)</td><td>261.90 (+8.09%)</td><td>225.46 (+5.36%)</td><td>206.40 (-0.39%)</td><td>205.20 (+13.18%)</td><td>27.37 (+0.68%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>214.00 (n/a)</td><td>207.20 (n/a)</td><td>181.30 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (-8.39%)</td><td>0.03 (-2.19%)</td><td>0.03 (+2.51%)</td><td>0.03 (-9.51%)</td><td>0.00 (-0.07%)</td><td>186.20 (+10.50%)</td><td>157.76 (+2.47%)</td><td>160.30 (-2.43%)</td><td>135.80 (+9.16%)</td><td>22.02 (+16.40%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>168.50 (n/a)</td><td>153.96 (n/a)</td><td>164.30 (n/a)</td><td>124.40 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (-6.32%)</td><td>0.03 (+7.33%)</td><td>0.03 (+11.82%)</td><td>0.03 <b>(+27.06%)</b></td><td>0.00 <b>(-37.25%)</b></td><td>182.10 <b>(-21.27%)</b></td><td>155.24 (-9.61%)</td><td>157.10 (-10.54%)</td><td>126.40 (+6.67%)</td><td>21.65 <b>(-46.78%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.30 (n/a)</td><td>171.74 (n/a)</td><td>175.60 (n/a)</td><td>118.50 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-4.45%)</td><td>0.03 (-15.96%)</td><td>0.03 (-10.07%)</td><td>0.01 <b>(-50.66%)</b></td><td>0.01 <b>(+239.56%)</b></td><td>373.70 <b>(+102.66%)</b></td><td>220.54 <b>(+30.57%)</b></td><td>186.10 (+11.24%)</td><td>159.70 (+4.65%)</td><td>88.91 <b>(+630.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>168.90 (n/a)</td><td>167.30 (n/a)</td><td>152.60 (n/a)</td><td>12.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 <b>(+33.96%)</b></td><td>0.03 <b>(+26.63%)</b></td><td>0.03 (+18.21%)</td><td>0.02 <b>(+57.29%)</b></td><td>0.01 (-3.54%)</td><td>217.10 <b>(-36.43%)</b></td><td>173.92 <b>(-23.50%)</b></td><td>169.80 (-15.44%)</td><td>133.30 <b>(-25.36%)</b></td><td>30.33 <b>(-54.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>341.50 (n/a)</td><td>227.34 (n/a)</td><td>200.80 (n/a)</td><td>178.60 (n/a)</td><td>67.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+8.39%)</td><td>0.03 (-2.15%)</td><td>0.03 (+1.15%)</td><td>0.02 (-11.96%)</td><td>0.00 <b>(+101.93%)</b></td><td>212.80 (+13.55%)</td><td>180.24 (+3.88%)</td><td>174.00 (-1.14%)</td><td>141.60 (-7.75%)</td><td>28.89 <b>(+115.09%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>173.50 (n/a)</td><td>176.00 (n/a)</td><td>153.50 (n/a)</td><td>13.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+15.01%)</td><td>0.03 (+6.46%)</td><td>0.03 (+15.63%)</td><td>0.03 (+10.39%)</td><td>0.01 (+13.82%)</td><td>194.70 (-9.44%)</td><td>167.10 (-6.06%)</td><td>169.90 (-13.54%)</td><td>113.50 (-13.03%)</td><td>32.78 (-11.47%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>177.88 (n/a)</td><td>196.50 (n/a)</td><td>130.50 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+16.86%)</td><td>0.03 (+6.64%)</td><td>0.03 (+0.93%)</td><td>0.02 (-7.79%)</td><td>0.00 <b>(+138.72%)</b></td><td>227.30 (+8.44%)</td><td>185.76 (-4.78%)</td><td>190.50 (-0.94%)</td><td>155.00 (-14.41%)</td><td>28.95 <b>(+116.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>209.60 (n/a)</td><td>195.08 (n/a)</td><td>192.30 (n/a)</td><td>181.10 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(-26.39%)</b></td><td>0.02 (-13.81%)</td><td>0.03 (-1.31%)</td><td>0.01 (-13.26%)</td><td>0.00 <b>(-34.02%)</b></td><td>353.60 (+15.25%)</td><td>239.80 (+13.92%)</td><td>207.10 (+1.32%)</td><td>201.40 <b>(+35.81%)</b></td><td>64.73 (+4.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>306.80 (n/a)</td><td>210.50 (n/a)</td><td>204.40 (n/a)</td><td>148.30 (n/a)</td><td>61.82 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (-5.06%)</td><td>0.07 (-4.16%)</td><td>0.07 (+13.14%)</td><td>0.05 (-17.02%)</td><td>0.01 (+6.35%)</td><td>202.80 <b>(+20.57%)</b></td><td>158.22 (+5.14%)</td><td>143.70 (-11.62%)</td><td>129.40 (+5.29%)</td><td>29.42 <b>(+35.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>150.48 (n/a)</td><td>162.60 (n/a)</td><td>122.90 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-6.60%)</td><td>0.06 (+9.03%)</td><td>0.06 <b>(+28.26%)</b></td><td>0.04 (+7.27%)</td><td>0.01 <b>(-35.62%)</b></td><td>238.10 (-6.77%)</td><td>182.32 (-10.53%)</td><td>172.30 <b>(-22.04%)</b></td><td>163.10 (+7.02%)</td><td>31.47 <b>(-32.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>203.78 (n/a)</td><td>221.00 (n/a)</td><td>152.40 (n/a)</td><td>46.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (-9.78%)</td><td>0.07 (-3.63%)</td><td>0.07 (+7.62%)</td><td>0.05 (+0.05%)</td><td>0.01 <b>(-28.94%)</b></td><td>193.20 (+0.00%)</td><td>157.94 (+2.72%)</td><td>145.70 (-7.08%)</td><td>141.00 (+10.85%)</td><td>22.05 (-19.14%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>153.76 (n/a)</td><td>156.80 (n/a)</td><td>127.20 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (+2.25%)</td><td>0.06 (-16.79%)</td><td>0.06 (-18.28%)</td><td>0.04 <b>(-26.84%)</b></td><td>0.02 <b>(+57.36%)</b></td><td>251.00 <b>(+36.71%)</b></td><td>183.22 <b>(+26.01%)</b></td><td>180.60 <b>(+22.36%)</b></td><td>116.10 (-2.19%)</td><td>51.85 <b>(+108.21%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>145.40 (n/a)</td><td>147.60 (n/a)</td><td>118.70 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (+17.02%)</td><td>0.06 (-4.10%)</td><td>0.05 <b>(-26.54%)</b></td><td>0.05 (+3.83%)</td><td>0.02 <b>(+55.54%)</b></td><td>205.90 (-3.70%)</td><td>174.04 (+7.56%)</td><td>201.40 <b>(+36.17%)</b></td><td>108.00 (-14.49%)</td><td>43.11 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>161.80 (n/a)</td><td>147.90 (n/a)</td><td>126.30 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 <b>(+22.52%)</b></td><td>0.06 (+15.15%)</td><td>0.06 (+8.20%)</td><td>0.05 <b>(+50.88%)</b></td><td>0.02 (+4.32%)</td><td>226.90 <b>(-33.73%)</b></td><td>179.44 (-16.14%)</td><td>177.00 (-7.57%)</td><td>121.00 (-18.41%)</td><td>40.62 <b>(-46.63%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>342.40 (n/a)</td><td>213.98 (n/a)</td><td>191.50 (n/a)</td><td>148.30 (n/a)</td><td>76.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (-15.78%)</td><td>0.06 (-9.21%)</td><td>0.06 (+3.26%)</td><td>0.04 <b>(-21.06%)</b></td><td>0.01 (-10.41%)</td><td>275.10 <b>(+26.66%)</b></td><td>194.80 (+11.10%)</td><td>174.50 (-3.16%)</td><td>150.70 (+18.75%)</td><td>48.80 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>175.34 (n/a)</td><td>180.20 (n/a)</td><td>126.90 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+44.98%)</b></td><td>0.05 <b>(+25.39%)</b></td><td>0.04 (+1.03%)</td><td>0.03 (+14.45%)</td><td>0.02 <b>(+72.83%)</b></td><td>313.50 (-12.63%)</td><td>225.60 (-17.80%)</td><td>236.30 (-1.05%)</td><td>144.70 <b>(-31.00%)</b></td><td>66.68 (+0.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>358.80 (n/a)</td><td>274.46 (n/a)</td><td>238.80 (n/a)</td><td>209.70 (n/a)</td><td>66.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (-17.53%)</td><td>0.12 (-0.17%)</td><td>0.12 (-0.24%)</td><td>0.10 (-2.85%)</td><td>0.02 <b>(-40.04%)</b></td><td>215.00 (+2.92%)</td><td>175.64 (-1.59%)</td><td>177.10 (+0.23%)</td><td>153.40 <b>(+21.26%)</b></td><td>24.77 <b>(-24.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>208.90 (n/a)</td><td>178.48 (n/a)</td><td>176.70 (n/a)</td><td>126.50 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (-10.52%)</td><td>0.13 (+3.67%)</td><td>0.13 (-3.20%)</td><td>0.09 <b>(+45.06%)</b></td><td>0.03 <b>(-36.88%)</b></td><td>233.00 <b>(-31.07%)</b></td><td>166.80 (-12.57%)</td><td>158.60 (+3.26%)</td><td>118.90 (+11.75%)</td><td>42.16 <b>(-52.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>338.00 (n/a)</td><td>190.78 (n/a)</td><td>153.60 (n/a)</td><td>106.40 (n/a)</td><td>89.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (-7.54%)</td><td>0.14 (-3.73%)</td><td>0.15 (+7.13%)</td><td>0.10 (-17.39%)</td><td>0.02 (+18.54%)</td><td>209.90 <b>(+21.05%)</b></td><td>157.82 (+5.12%)</td><td>144.40 (-6.66%)</td><td>134.60 (+8.20%)</td><td>30.50 <b>(+59.63%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>173.40 (n/a)</td><td>150.14 (n/a)</td><td>154.70 (n/a)</td><td>124.40 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+3.27%)</td><td>0.12 (+6.80%)</td><td>0.12 (+4.65%)</td><td>0.11 <b>(+21.37%)</b></td><td>0.01 <b>(-38.51%)</b></td><td>184.20 (-17.58%)</td><td>169.14 (-7.19%)</td><td>170.00 (-4.44%)</td><td>157.70 (-3.13%)</td><td>11.55 <b>(-52.30%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>182.24 (n/a)</td><td>177.90 (n/a)</td><td>162.80 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (+13.87%)</td><td>0.14 (+6.89%)</td><td>0.14 (+9.32%)</td><td>0.11 (-7.97%)</td><td>0.02 <b>(+97.54%)</b></td><td>196.80 (+8.67%)</td><td>155.60 (-4.94%)</td><td>147.80 (-8.54%)</td><td>128.80 (-12.20%)</td><td>26.80 <b>(+89.35%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>181.10 (n/a)</td><td>163.68 (n/a)</td><td>161.60 (n/a)</td><td>146.70 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-5.10%)</td><td>0.11 (-10.33%)</td><td>0.11 (-8.74%)</td><td>0.09 (-15.19%)</td><td>0.02 (+17.08%)</td><td>222.90 (+17.94%)</td><td>195.04 (+12.18%)</td><td>199.60 (+9.61%)</td><td>157.00 (+5.37%)</td><td>25.18 <b>(+42.49%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>173.86 (n/a)</td><td>182.10 (n/a)</td><td>149.00 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(-22.46%)</b></td><td>0.12 (+0.65%)</td><td>0.12 (-4.66%)</td><td>0.11 <b>(+49.73%)</b></td><td>0.01 <b>(-78.83%)</b></td><td>194.40 <b>(-33.22%)</b></td><td>180.36 (-8.66%)</td><td>177.30 (+4.85%)</td><td>166.30 <b>(+28.91%)</b></td><td>12.06 <b>(-82.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>291.10 (n/a)</td><td>197.46 (n/a)</td><td>169.10 (n/a)</td><td>129.00 (n/a)</td><td>67.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 <b>(+21.72%)</b></td><td>0.11 (+2.71%)</td><td>0.10 (-7.20%)</td><td>0.09 (-3.26%)</td><td>0.02 <b>(+109.65%)</b></td><td>233.70 (+3.36%)</td><td>200.64 (-0.42%)</td><td>217.50 (+7.78%)</td><td>143.60 (-17.85%)</td><td>36.34 <b>(+75.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>201.48 (n/a)</td><td>201.80 (n/a)</td><td>174.80 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>169.80 (n/a)</td><td>142.84 (n/a)</td><td>129.10 (n/a)</td><td>127.70 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>156.70 (n/a)</td><td>147.00 (n/a)</td><td>107.50 (n/a)</td><td>57.54 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.50 (n/a)</td><td>183.78 (n/a)</td><td>170.70 (n/a)</td><td>166.00 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>177.26 (n/a)</td><td>178.80 (n/a)</td><td>148.90 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>182.90 (n/a)</td><td>171.60 (n/a)</td><td>164.30 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>170.20 (n/a)</td><td>158.88 (n/a)</td><td>155.80 (n/a)</td><td>148.30 (n/a)</td><td>8.60 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>289.40 (n/a)</td><td>198.18 (n/a)</td><td>178.30 (n/a)</td><td>147.90 (n/a)</td><td>57.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>302.00 (n/a)</td><td>183.58 (n/a)</td><td>152.20 (n/a)</td><td>109.20 (n/a)</td><td>81.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>197.60 (n/a)</td><td>165.06 (n/a)</td><td>171.60 (n/a)</td><td>114.60 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>194.60 (n/a)</td><td>150.70 (n/a)</td><td>144.70 (n/a)</td><td>110.70 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>241.00 (n/a)</td><td>193.36 (n/a)</td><td>190.90 (n/a)</td><td>156.50 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>187.22 (n/a)</td><td>198.50 (n/a)</td><td>161.20 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.37 (+11.80%)</td><td>0.30 (+6.81%)</td><td>0.29 (-3.25%)</td><td>0.24 (+12.37%)</td><td>0.05 (-9.17%)</td><td>202.40 (-11.03%)</td><td>169.56 (-7.37%)</td><td>170.70 (+3.33%)</td><td>134.40 (-10.58%)</td><td>25.83 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>227.50 (n/a)</td><td>183.06 (n/a)</td><td>165.20 (n/a)</td><td>150.30 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>205.90 (n/a)</td><td>175.82 (n/a)</td><td>198.70 (n/a)</td><td>130.00 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>220.00 (n/a)</td><td>171.52 (n/a)</td><td>172.10 (n/a)</td><td>117.20 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>258.50 (n/a)</td><td>189.22 (n/a)</td><td>168.00 (n/a)</td><td>162.70 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.40 (n/a)</td><td>175.62 (n/a)</td><td>176.20 (n/a)</td><td>165.00 (n/a)</td><td>9.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>168.10 (n/a)</td><td>168.90 (n/a)</td><td>119.80 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>173.62 (n/a)</td><td>183.80 (n/a)</td><td>131.40 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>291.60 (n/a)</td><td>209.16 (n/a)</td><td>193.60 (n/a)</td><td>168.90 (n/a)</td><td>47.52 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>177.26 (n/a)</td><td>174.30 (n/a)</td><td>170.90 (n/a)</td><td>6.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>157.72 (n/a)</td><td>162.60 (n/a)</td><td>132.50 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>178.02 (n/a)</td><td>174.10 (n/a)</td><td>145.40 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.00 (n/a)</td><td>183.52 (n/a)</td><td>166.30 (n/a)</td><td>149.70 (n/a)</td><td>39.55 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>242.80 (n/a)</td><td>178.68 (n/a)</td><td>151.40 (n/a)</td><td>138.10 (n/a)</td><td>46.30 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>170.90 (n/a)</td><td>174.80 (n/a)</td><td>138.40 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>221.80 (n/a)</td><td>190.28 (n/a)</td><td>197.30 (n/a)</td><td>152.30 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>232.10 (n/a)</td><td>186.82 (n/a)</td><td>194.90 (n/a)</td><td>145.50 (n/a)</td><td>37.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>178.70 (n/a)</td><td>170.68 (n/a)</td><td>175.30 (n/a)</td><td>152.60 (n/a)</td><td>10.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>175.04 (n/a)</td><td>168.70 (n/a)</td><td>154.10 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>336.80 (n/a)</td><td>234.26 (n/a)</td><td>217.40 (n/a)</td><td>176.10 (n/a)</td><td>60.52 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.70 (n/a)</td><td>162.36 (n/a)</td><td>152.20 (n/a)</td><td>128.60 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>147.08 (n/a)</td><td>136.60 (n/a)</td><td>99.50 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>166.60 (n/a)</td><td>158.30 (n/a)</td><td>136.80 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>152.78 (n/a)</td><td>147.80 (n/a)</td><td>120.80 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.20 (n/a)</td><td>186.84 (n/a)</td><td>208.30 (n/a)</td><td>143.50 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>211.44 (n/a)</td><td>212.50 (n/a)</td><td>199.50 (n/a)</td><td>10.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.90 (n/a)</td><td>205.72 (n/a)</td><td>203.70 (n/a)</td><td>180.60 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>354.70 (n/a)</td><td>243.88 (n/a)</td><td>235.10 (n/a)</td><td>187.60 (n/a)</td><td>65.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>160.20 (n/a)</td><td>172.00 (n/a)</td><td>137.90 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>185.48 (n/a)</td><td>178.20 (n/a)</td><td>155.50 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.70 (n/a)</td><td>172.28 (n/a)</td><td>165.90 (n/a)</td><td>136.50 (n/a)</td><td>45.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.20 (n/a)</td><td>184.14 (n/a)</td><td>178.50 (n/a)</td><td>139.40 (n/a)</td><td>39.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>174.60 (n/a)</td><td>166.50 (n/a)</td><td>149.10 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>181.20 (n/a)</td><td>180.70 (n/a)</td><td>149.70 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>187.62 (n/a)</td><td>192.20 (n/a)</td><td>157.20 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>212.68 (n/a)</td><td>224.00 (n/a)</td><td>170.20 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>185.02 (n/a)</td><td>173.00 (n/a)</td><td>134.50 (n/a)</td><td>39.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>169.04 (n/a)</td><td>165.50 (n/a)</td><td>122.60 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>197.86 (n/a)</td><td>200.60 (n/a)</td><td>167.30 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>178.10 (n/a)</td><td>189.10 (n/a)</td><td>138.10 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>181.92 (n/a)</td><td>162.80 (n/a)</td><td>155.90 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.80 (n/a)</td><td>200.28 (n/a)</td><td>209.00 (n/a)</td><td>145.30 (n/a)</td><td>46.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>206.34 (n/a)</td><td>205.80 (n/a)</td><td>165.20 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>209.92 (n/a)</td><td>210.70 (n/a)</td><td>181.20 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>176.44 (n/a)</td><td>174.30 (n/a)</td><td>148.10 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.40 (n/a)</td><td>175.88 (n/a)</td><td>170.30 (n/a)</td><td>135.60 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>245.20 (n/a)</td><td>208.50 (n/a)</td><td>214.50 (n/a)</td><td>153.80 (n/a)</td><td>36.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.80 (n/a)</td><td>173.46 (n/a)</td><td>166.40 (n/a)</td><td>119.00 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>196.50 (n/a)</td><td>168.40 (n/a)</td><td>193.70 (n/a)</td><td>110.70 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.10 (n/a)</td><td>168.46 (n/a)</td><td>150.20 (n/a)</td><td>122.90 (n/a)</td><td>40.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>185.80 (n/a)</td><td>185.30 (n/a)</td><td>170.20 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.23 (-8.38%)</td><td>4.03 (+1.04%)</td><td>4.11 (+1.23%)</td><td>3.53 (+1.54%)</td><td>0.28 <b>(-36.45%)</b></td><td>2665.20 (-1.52%)</td><td>2346.42 (-1.57%)</td><td>2286.30 (-1.21%)</td><td>2220.70 (+9.15%)</td><td>180.52 <b>(-30.99%)</b></td><td>1665.86 (-8.38%)</td><td>1583.44 (+1.04%)</td><td>1618.09 (+1.23%)</td><td>1388.01 (+1.54%)</td><td>111.24 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>4.62 (n/a)</td><td>3.98 (n/a)</td><td>4.06 (n/a)</td><td>3.48 (n/a)</td><td>0.45 (n/a)</td><td>2706.20 (n/a)</td><td>2383.88 (n/a)</td><td>2314.30 (n/a)</td><td>2034.50 (n/a)</td><td>261.59 (n/a)</td><td>1818.31 (n/a)</td><td>1567.13 (n/a)</td><td>1598.46 (n/a)</td><td>1367.02 (n/a)</td><td>175.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.11 (-18.43%)</td><td>0.84 (-15.55%)</td><td>0.89 (-13.74%)</td><td>0.58 (-11.84%)</td><td>0.24 <b>(-20.32%)</b></td><td>383.40 (+13.43%)</td><td>283.34 (+17.49%)</td><td>248.10 (+15.93%)</td><td>200.00 <b>(+22.55%)</b></td><td>85.53 (+12.05%)</td><td>47.18 (-18.43%)</td><td>35.74 (-15.55%)</td><td>38.04 (-13.74%)</td><td>24.61 (-11.84%)</td><td>10.17 <b>(-20.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.36 (n/a)</td><td>0.99 (n/a)</td><td>1.03 (n/a)</td><td>0.65 (n/a)</td><td>0.30 (n/a)</td><td>338.00 (n/a)</td><td>241.16 (n/a)</td><td>214.00 (n/a)</td><td>163.20 (n/a)</td><td>76.34 (n/a)</td><td>57.84 (n/a)</td><td>42.32 (n/a)</td><td>44.10 (n/a)</td><td>27.92 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.04 (-0.45%)</td><td>0.90 (-2.89%)</td><td>0.96 (+1.19%)</td><td>0.57 <b>(-24.87%)</b></td><td>0.19 <b>(+82.37%)</b></td><td>386.90 <b>(+33.09%)</b></td><td>257.50 (+6.89%)</td><td>230.30 (-1.16%)</td><td>213.40 (+0.42%)</td><td>72.88 <b>(+146.38%)</b></td><td>44.21 (-0.45%)</td><td>38.46 (-2.89%)</td><td>40.98 (+1.19%)</td><td>24.39 <b>(-24.87%)</b></td><td>8.04 <b>(+82.37%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.04 (n/a)</td><td>0.93 (n/a)</td><td>0.95 (n/a)</td><td>0.76 (n/a)</td><td>0.10 (n/a)</td><td>290.70 (n/a)</td><td>240.90 (n/a)</td><td>233.00 (n/a)</td><td>212.50 (n/a)</td><td>29.58 (n/a)</td><td>44.41 (n/a)</td><td>39.61 (n/a)</td><td>40.50 (n/a)</td><td>32.47 (n/a)</td><td>4.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.52 (+0.02%)</td><td>0.52 (-0.29%)</td><td>0.52 (-0.01%)</td><td>0.51 (-1.16%)</td><td>0.00 <b>(+435.23%)</b></td><td>49327.70 (+1.17%)</td><td>48798.02 (+0.29%)</td><td>48632.10 (+0.01%)</td><td>48616.00 (-0.02%)</td><td>305.73 <b>(+441.31%)</b></td><td>353.38 (+0.02%)</td><td>352.07 (-0.29%)</td><td>353.26 (-0.01%)</td><td>348.28 (-1.16%)</td><td>2.19 <b>(+435.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48755.00 (n/a)</td><td>48656.00 (n/a)</td><td>48626.40 (n/a)</td><td>48623.90 (n/a)</td><td>56.48 (n/a)</td><td>353.32 (n/a)</td><td>353.09 (n/a)</td><td>353.30 (n/a)</td><td>352.37 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (-0.98%)</td><td>0.21 (-0.81%)</td><td>0.21 (-0.66%)</td><td>0.21 (-1.40%)</td><td>0.00 <b>(+40.26%)</b></td><td>119588.10 (+1.42%)</td><td>118228.50 (+0.83%)</td><td>118241.20 (+0.67%)</td><td>117010.70 (+0.98%)</td><td>1151.05 <b>(+43.77%)</b></td><td>146.82 (-0.98%)</td><td>145.32 (-0.81%)</td><td>145.30 (-0.66%)</td><td>143.66 (-1.40%)</td><td>1.41 <b>(+40.26%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>117911.50 (n/a)</td><td>117260.90 (n/a)</td><td>117457.90 (n/a)</td><td>115869.40 (n/a)</td><td>800.61 (n/a)</td><td>148.27 (n/a)</td><td>146.52 (n/a)</td><td>146.26 (n/a)</td><td>145.70 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.89 (-0.65%)</td><td>0.88 (-0.07%)</td><td>0.88 (+0.12%)</td><td>0.88 (+0.60%)</td><td>0.00 <b>(-47.12%)</b></td><td>28753.60 (-0.59%)</td><td>28586.58 (+0.07%)</td><td>28583.40 (-0.12%)</td><td>28424.70 (+0.65%)</td><td>135.72 <b>(-47.08%)</b></td><td>604.40 (-0.65%)</td><td>600.99 (-0.07%)</td><td>601.04 (+0.12%)</td><td>597.49 (+0.60%)</td><td>2.85 <b>(-47.12%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28924.80 (n/a)</td><td>28568.00 (n/a)</td><td>28618.30 (n/a)</td><td>28240.50 (n/a)</td><td>256.45 (n/a)</td><td>608.34 (n/a)</td><td>601.41 (n/a)</td><td>600.31 (n/a)</td><td>593.95 (n/a)</td><td>5.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.54 (+1.11%)</td><td>3.43 (+0.41%)</td><td>3.50 (+1.25%)</td><td>3.23 (-1.54%)</td><td>0.13 <b>(+31.39%)</b></td><td>7786.30 (+1.57%)</td><td>7353.26 (-0.36%)</td><td>7191.20 (-1.23%)</td><td>7110.50 (-1.10%)</td><td>289.84 <b>(+32.03%)</b></td><td>2416.12 (+1.11%)</td><td>2339.20 (+0.41%)</td><td>2389.00 (+1.25%)</td><td>2206.42 (-1.54%)</td><td>90.07 <b>(+31.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.50 (n/a)</td><td>3.41 (n/a)</td><td>3.46 (n/a)</td><td>3.28 (n/a)</td><td>0.10 (n/a)</td><td>7666.20 (n/a)</td><td>7379.52 (n/a)</td><td>7281.00 (n/a)</td><td>7189.60 (n/a)</td><td>219.52 (n/a)</td><td>2389.56 (n/a)</td><td>2329.68 (n/a)</td><td>2359.55 (n/a)</td><td>2240.98 (n/a)</td><td>68.55 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>2.87 (-3.55%)</td><td>2.76 (-1.84%)</td><td>2.81 (+0.04%)</td><td>2.58 (-4.09%)</td><td>0.11 (+3.54%)</td><td>9746.30 (+4.26%)</td><td>9122.14 (+1.89%)</td><td>8951.30 (-0.04%)</td><td>8781.40 (+3.68%)</td><td>390.15 (+12.13%)</td><td>1956.39 (-3.55%)</td><td>1885.99 (-1.84%)</td><td>1919.26 (+0.04%)</td><td>1762.70 (-4.09%)</td><td>78.13 (+3.54%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>2.97 (n/a)</td><td>2.81 (n/a)</td><td>2.81 (n/a)</td><td>2.69 (n/a)</td><td>0.11 (n/a)</td><td>9347.90 (n/a)</td><td>8952.90 (n/a)</td><td>8955.20 (n/a)</td><td>8469.60 (n/a)</td><td>347.96 (n/a)</td><td>2028.42 (n/a)</td><td>1921.26 (n/a)</td><td>1918.42 (n/a)</td><td>1837.84 (n/a)</td><td>75.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.28 (+3.19%)</td><td>3.20 (+1.79%)</td><td>3.21 (+1.86%)</td><td>3.14 (+2.34%)</td><td>0.05 <b>(+25.38%)</b></td><td>8006.10 (-2.29%)</td><td>7865.74 (-1.75%)</td><td>7840.60 (-1.82%)</td><td>7669.00 (-3.09%)</td><td>133.88 (+18.65%)</td><td>2240.18 (+3.19%)</td><td>2184.64 (+1.79%)</td><td>2191.14 (+1.86%)</td><td>2145.84 (+2.34%)</td><td>37.44 <b>(+25.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.18 (n/a)</td><td>3.14 (n/a)</td><td>3.15 (n/a)</td><td>3.07 (n/a)</td><td>0.04 (n/a)</td><td>8193.80 (n/a)</td><td>8005.64 (n/a)</td><td>7986.10 (n/a)</td><td>7913.80 (n/a)</td><td>112.83 (n/a)</td><td>2170.87 (n/a)</td><td>2146.31 (n/a)</td><td>2151.22 (n/a)</td><td>2096.69 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.78 (+0.03%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.14%)</td><td>0.00 <b>(+343.62%)</b></td><td>96630.40 (+0.14%)</td><td>96482.92 (+0.02%)</td><td>96457.20 (+0.01%)</td><td>96415.60 (-0.03%)</td><td>84.32 <b>(+344.47%)</b></td><td>712.74 (+0.03%)</td><td>712.25 (-0.02%)</td><td>712.43 (-0.01%)</td><td>711.16 (-0.14%)</td><td>0.62 <b>(+343.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96491.40 (n/a)</td><td>96459.18 (n/a)</td><td>96451.10 (n/a)</td><td>96444.80 (n/a)</td><td>18.97 (n/a)</td><td>712.53 (n/a)</td><td>712.42 (n/a)</td><td>712.48 (n/a)</td><td>712.18 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (-0.32%)</td><td>0.73 (-0.14%)</td><td>0.73 (-0.03%)</td><td>0.73 (-0.29%)</td><td>0.00 (-18.63%)</td><td>103933.50 (+0.29%)</td><td>103703.72 (+0.14%)</td><td>103655.70 (+0.03%)</td><td>103601.60 (+0.33%)</td><td>132.17 (-18.10%)</td><td>663.31 (-0.32%)</td><td>662.65 (-0.14%)</td><td>662.96 (-0.03%)</td><td>661.19 (-0.29%)</td><td>0.84 (-18.63%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103635.70 (n/a)</td><td>103553.76 (n/a)</td><td>103626.20 (n/a)</td><td>103265.60 (n/a)</td><td>161.38 (n/a)</td><td>665.46 (n/a)</td><td>663.61 (n/a)</td><td>663.15 (n/a)</td><td>663.09 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.69 (+0.05%)</td><td>0.69 (-0.02%)</td><td>0.69 (-0.16%)</td><td>0.69 (+0.12%)</td><td>0.00 (-1.10%)</td><td>109733.50 (-0.12%)</td><td>109442.22 (+0.02%)</td><td>109457.70 (+0.16%)</td><td>109107.80 (-0.05%)</td><td>294.15 (-1.22%)</td><td>629.83 (+0.05%)</td><td>627.91 (-0.02%)</td><td>627.82 (-0.16%)</td><td>626.24 (+0.12%)</td><td>1.69 (-1.10%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109864.30 (n/a)</td><td>109417.12 (n/a)</td><td>109279.10 (n/a)</td><td>109165.60 (n/a)</td><td>297.79 (n/a)</td><td>629.50 (n/a)</td><td>628.05 (n/a)</td><td>628.84 (n/a)</td><td>625.49 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.37 (+1.50%)</td><td>6.82 (-1.40%)</td><td>6.76 (-4.65%)</td><td>6.41 (+2.34%)</td><td>0.40 (+2.50%)</td><td>1390.60 (-2.28%)</td><td>1311.08 (+1.42%)</td><td>1318.60 (+4.88%)</td><td>1209.70 (-1.48%)</td><td>76.50 (-1.66%)</td><td>443.79 (+1.50%)</td><td>410.62 (-1.40%)</td><td>407.15 (-4.65%)</td><td>386.08 (+2.34%)</td><td>24.31 (+2.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.26 (n/a)</td><td>6.91 (n/a)</td><td>7.09 (n/a)</td><td>6.26 (n/a)</td><td>0.39 (n/a)</td><td>1423.10 (n/a)</td><td>1292.72 (n/a)</td><td>1257.30 (n/a)</td><td>1227.90 (n/a)</td><td>77.79 (n/a)</td><td>437.22 (n/a)</td><td>416.44 (n/a)</td><td>427.01 (n/a)</td><td>377.24 (n/a)</td><td>23.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.94 (-1.83%)</td><td>6.79 (+5.00%)</td><td>6.78 (-1.36%)</td><td>6.70 <b>(+29.80%)</b></td><td>0.10 <b>(-87.99%)</b></td><td>1329.40 <b>(-22.96%)</b></td><td>1312.40 (-6.12%)</td><td>1314.00 (+1.37%)</td><td>1284.00 (+1.86%)</td><td>18.87 <b>(-90.50%)</b></td><td>418.11 (-1.83%)</td><td>409.14 (+5.00%)</td><td>408.57 (-1.36%)</td><td>403.84 <b>(+29.80%)</b></td><td>5.92 <b>(-87.99%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.07 (n/a)</td><td>6.47 (n/a)</td><td>6.88 (n/a)</td><td>5.17 (n/a)</td><td>0.82 (n/a)</td><td>1725.50 (n/a)</td><td>1397.92 (n/a)</td><td>1296.20 (n/a)</td><td>1260.50 (n/a)</td><td>198.59 (n/a)</td><td>425.93 (n/a)</td><td>389.64 (n/a)</td><td>414.19 (n/a)</td><td>311.14 (n/a)</td><td>49.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.95 (+1.18%)</td><td>6.56 (+7.72%)</td><td>6.55 (+7.86%)</td><td>6.14 (+13.91%)</td><td>0.33 <b>(-37.10%)</b></td><td>1450.80 (-12.22%)</td><td>1362.28 (-7.53%)</td><td>1361.00 (-7.29%)</td><td>1281.80 (-1.17%)</td><td>68.96 <b>(-45.31%)</b></td><td>418.84 (+1.18%)</td><td>394.90 (+7.72%)</td><td>394.48 (+7.86%)</td><td>370.04 (+13.91%)</td><td>19.93 <b>(-37.10%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>6.87 (n/a)</td><td>6.09 (n/a)</td><td>6.07 (n/a)</td><td>5.39 (n/a)</td><td>0.53 (n/a)</td><td>1652.70 (n/a)</td><td>1473.18 (n/a)</td><td>1468.00 (n/a)</td><td>1297.00 (n/a)</td><td>126.09 (n/a)</td><td>413.94 (n/a)</td><td>366.60 (n/a)</td><td>365.72 (n/a)</td><td>324.85 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.27 (+3.71%)</td><td>7.78 (+5.31%)</td><td>7.95 (+9.97%)</td><td>7.30 (+2.10%)</td><td>0.41 (+18.45%)</td><td>4776.10 (-2.06%)</td><td>4491.60 (-4.99%)</td><td>4385.50 (-9.07%)</td><td>4214.80 (-3.58%)</td><td>235.96 (+13.04%)</td><td>509.51 (+3.71%)</td><td>479.16 (+5.31%)</td><td>489.68 (+9.97%)</td><td>449.63 (+2.10%)</td><td>25.00 (+18.45%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.98 (n/a)</td><td>7.39 (n/a)</td><td>7.23 (n/a)</td><td>7.15 (n/a)</td><td>0.34 (n/a)</td><td>4876.60 (n/a)</td><td>4727.56 (n/a)</td><td>4822.90 (n/a)</td><td>4371.20 (n/a)</td><td>208.74 (n/a)</td><td>491.28 (n/a)</td><td>454.99 (n/a)</td><td>445.27 (n/a)</td><td>440.37 (n/a)</td><td>21.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.86 (-1.65%)</td><td>7.62 (-1.02%)</td><td>7.62 (-0.16%)</td><td>7.36 (-2.66%)</td><td>0.18 (-1.20%)</td><td>4734.40 (+2.73%)</td><td>4578.24 (+1.03%)</td><td>4576.90 (+0.16%)</td><td>4436.50 (+1.68%)</td><td>105.81 (+3.38%)</td><td>484.05 (-1.65%)</td><td>469.26 (-1.02%)</td><td>469.20 (-0.16%)</td><td>453.59 (-2.66%)</td><td>10.80 (-1.20%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.99 (n/a)</td><td>7.70 (n/a)</td><td>7.63 (n/a)</td><td>7.57 (n/a)</td><td>0.18 (n/a)</td><td>4608.60 (n/a)</td><td>4531.62 (n/a)</td><td>4569.50 (n/a)</td><td>4363.40 (n/a)</td><td>102.35 (n/a)</td><td>492.16 (n/a)</td><td>474.09 (n/a)</td><td>469.96 (n/a)</td><td>465.97 (n/a)</td><td>10.93 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.67 (-1.63%)</td><td>7.36 (+2.92%)</td><td>7.35 (+5.44%)</td><td>7.19 (+6.00%)</td><td>0.20 <b>(-53.16%)</b></td><td>4847.60 (-5.66%)</td><td>4736.60 (-3.04%)</td><td>4746.00 (-5.16%)</td><td>4545.30 (+1.66%)</td><td>123.83 <b>(-54.98%)</b></td><td>472.46 (-1.63%)</td><td>453.63 (+2.92%)</td><td>452.48 (+5.44%)</td><td>443.00 (+6.00%)</td><td>12.05 <b>(-53.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>7.80 (n/a)</td><td>7.16 (n/a)</td><td>6.97 (n/a)</td><td>6.79 (n/a)</td><td>0.42 (n/a)</td><td>5138.50 (n/a)</td><td>4885.14 (n/a)</td><td>5004.10 (n/a)</td><td>4471.10 (n/a)</td><td>275.05 (n/a)</td><td>480.31 (n/a)</td><td>440.75 (n/a)</td><td>429.15 (n/a)</td><td>417.92 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.79 (-0.35%)</td><td>0.79 (-0.17%)</td><td>0.79 (-0.04%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(-62.67%)</b></td><td>95929.40 (+0.02%)</td><td>95801.40 (+0.17%)</td><td>95774.50 (+0.04%)</td><td>95717.20 (+0.35%)</td><td>88.08 <b>(-62.52%)</b></td><td>717.94 (-0.35%)</td><td>717.31 (-0.17%)</td><td>717.51 (-0.04%)</td><td>716.35 (-0.02%)</td><td>0.66 <b>(-62.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95913.50 (n/a)</td><td>95635.72 (n/a)</td><td>95737.10 (n/a)</td><td>95386.00 (n/a)</td><td>235.00 (n/a)</td><td>720.44 (n/a)</td><td>718.56 (n/a)</td><td>717.79 (n/a)</td><td>716.47 (n/a)</td><td>1.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (-0.34%)</td><td>0.73 (-0.07%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.02%)</td><td>0.00 <b>(-85.76%)</b></td><td>102951.40 (+0.02%)</td><td>102914.54 (+0.07%)</td><td>102914.50 (-0.00%)</td><td>102881.00 (+0.35%)</td><td>25.04 <b>(-85.70%)</b></td><td>667.95 (-0.34%)</td><td>667.73 (-0.07%)</td><td>667.73 (+0.00%)</td><td>667.49 (-0.02%)</td><td>0.16 <b>(-85.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102930.40 (n/a)</td><td>102839.42 (n/a)</td><td>102915.10 (n/a)</td><td>102526.60 (n/a)</td><td>175.06 (n/a)</td><td>670.26 (n/a)</td><td>668.22 (n/a)</td><td>667.73 (n/a)</td><td>667.63 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.70 (+0.11%)</td><td>0.70 (+0.18%)</td><td>0.70 (+0.17%)</td><td>0.70 (+0.39%)</td><td>0.00 <b>(-63.40%)</b></td><td>108044.10 (-0.39%)</td><td>107962.18 (-0.18%)</td><td>107940.30 (-0.17%)</td><td>107876.80 (-0.11%)</td><td>67.77 <b>(-63.59%)</b></td><td>637.02 (+0.11%)</td><td>636.51 (+0.18%)</td><td>636.64 (+0.17%)</td><td>636.03 (+0.39%)</td><td>0.40 <b>(-63.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108466.80 (n/a)</td><td>108152.72 (n/a)</td><td>108122.40 (n/a)</td><td>107990.40 (n/a)</td><td>186.13 (n/a)</td><td>636.35 (n/a)</td><td>635.39 (n/a)</td><td>635.57 (n/a)</td><td>633.55 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.74 (-11.43%)</td><td>3.20 (-15.87%)</td><td>3.11 (-13.36%)</td><td>2.92 (-17.19%)</td><td>0.32 (-2.59%)</td><td>2759.00 <b>(+20.76%)</b></td><td>2539.52 (+19.04%)</td><td>2589.40 (+15.43%)</td><td>2156.20 (+12.90%)</td><td>232.15 <b>(+30.36%)</b></td><td>980.40 (-11.43%)</td><td>838.53 (-15.87%)</td><td>816.39 (-13.36%)</td><td>766.19 (-17.19%)</td><td>83.82 (-2.59%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>4.22 (n/a)</td><td>3.80 (n/a)</td><td>3.59 (n/a)</td><td>3.53 (n/a)</td><td>0.33 (n/a)</td><td>2284.70 (n/a)</td><td>2133.26 (n/a)</td><td>2243.30 (n/a)</td><td>1909.80 (n/a)</td><td>178.08 (n/a)</td><td>1106.91 (n/a)</td><td>996.69 (n/a)</td><td>942.32 (n/a)</td><td>925.26 (n/a)</td><td>86.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.41 (-6.16%)</td><td>0.35 (-3.78%)</td><td>0.35 (-2.51%)</td><td>0.32 (-3.30%)</td><td>0.03 (-13.65%)</td><td>3860.90 (+3.42%)</td><td>3565.44 (+3.79%)</td><td>3598.70 (+2.58%)</td><td>3061.60 (+6.57%)</td><td>318.52 (-2.86%)</td><td>21.92 (-6.16%)</td><td>18.95 (-3.78%)</td><td>18.65 (-2.51%)</td><td>17.38 (-3.30%)</td><td>1.82 (-13.66%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.04 (n/a)</td><td>3733.30 (n/a)</td><td>3435.20 (n/a)</td><td>3508.30 (n/a)</td><td>2872.90 (n/a)</td><td>327.91 (n/a)</td><td>23.36 (n/a)</td><td>19.70 (n/a)</td><td>19.13 (n/a)</td><td>17.98 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>6.01 (+16.49%)</td><td>4.60 (+6.73%)</td><td>4.75 (+1.13%)</td><td>3.57 (+10.66%)</td><td>1.02 <b>(+25.61%)</b></td><td>1865.50 (-9.63%)</td><td>1502.46 (-5.56%)</td><td>1401.70 (-1.11%)</td><td>1106.80 (-14.15%)</td><td>327.89 (+0.54%)</td><td>1856.93 (+16.49%)</td><td>1422.25 (+6.73%)</td><td>1466.23 (+1.13%)</td><td>1101.68 (+10.66%)</td><td>314.66 <b>(+25.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.16 (n/a)</td><td>4.31 (n/a)</td><td>4.69 (n/a)</td><td>3.22 (n/a)</td><td>0.81 (n/a)</td><td>2064.40 (n/a)</td><td>1590.98 (n/a)</td><td>1417.50 (n/a)</td><td>1289.30 (n/a)</td><td>326.13 (n/a)</td><td>1594.03 (n/a)</td><td>1332.63 (n/a)</td><td>1449.90 (n/a)</td><td>995.54 (n/a)</td><td>250.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (-7.39%)</td><td>0.20 (-1.62%)</td><td>0.20 (-0.34%)</td><td>0.13 (-14.56%)</td><td>0.05 (+3.91%)</td><td>0.25 (-7.39%)</td><td>0.20 (-1.62%)</td><td>0.20 (-0.34%)</td><td>0.13 (-14.56%)</td><td>0.05 (+3.91%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.33 (-1.22%)</td><td>12.28 (-4.33%)</td><td>13.17 (-0.49%)</td><td>10.29 (-7.05%)</td><td>1.37 <b>(+36.48%)</b></td><td>13.32 (-1.22%)</td><td>12.27 (-4.33%)</td><td>13.16 (-0.49%)</td><td>10.28 (-7.05%)</td><td>1.37 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.49 (n/a)</td><td>12.84 (n/a)</td><td>13.23 (n/a)</td><td>11.07 (n/a)</td><td>1.00 (n/a)</td><td>13.48 (n/a)</td><td>12.83 (n/a)</td><td>13.22 (n/a)</td><td>11.07 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>25.69 (+3.04%)</td><td>24.45 (-0.00%)</td><td>24.61 (+0.51%)</td><td>23.28 (-3.02%)</td><td>0.88 <b>(+158.22%)</b></td><td>25.68 (+3.04%)</td><td>24.44 (-0.00%)</td><td>24.59 (+0.51%)</td><td>23.27 (-3.02%)</td><td>0.88 <b>(+158.22%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>24.94 (n/a)</td><td>24.45 (n/a)</td><td>24.48 (n/a)</td><td>24.01 (n/a)</td><td>0.34 (n/a)</td><td>24.92 (n/a)</td><td>24.44 (n/a)</td><td>24.47 (n/a)</td><td>24.00 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>41.83 (-1.49%)</td><td>40.54 (-1.96%)</td><td>40.67 (-3.87%)</td><td>39.15 (+0.23%)</td><td>1.22 <b>(-20.55%)</b></td><td>41.80 (-1.49%)</td><td>40.52 (-1.96%)</td><td>40.65 (-3.87%)</td><td>39.13 (+0.23%)</td><td>1.22 <b>(-20.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>42.46 (n/a)</td><td>41.35 (n/a)</td><td>42.31 (n/a)</td><td>39.06 (n/a)</td><td>1.53 (n/a)</td><td>42.43 (n/a)</td><td>41.32 (n/a)</td><td>42.29 (n/a)</td><td>39.04 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>43.89 (-3.04%)</td><td>42.74 (+4.30%)</td><td>42.85 (-3.12%)</td><td>40.96 <b>(+56.58%)</b></td><td>1.10 <b>(-86.77%)</b></td><td>43.86 (-3.04%)</td><td>42.72 (+4.30%)</td><td>42.83 (-3.12%)</td><td>40.93 <b>(+56.58%)</b></td><td>1.10 <b>(-86.77%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>45.26 (n/a)</td><td>40.98 (n/a)</td><td>44.23 (n/a)</td><td>26.16 (n/a)</td><td>8.30 (n/a)</td><td>45.24 (n/a)</td><td>40.96 (n/a)</td><td>44.21 (n/a)</td><td>26.14 (n/a)</td><td>8.30 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.44 (-1.47%)</td><td>12.58 (+6.42%)</td><td>13.27 (+19.08%)</td><td>10.49 (-3.19%)</td><td>1.25 (+1.24%)</td><td>13.43 (-1.47%)</td><td>12.58 (+6.42%)</td><td>13.27 (+19.08%)</td><td>10.48 (-3.19%)</td><td>1.25 (+1.24%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.64 (n/a)</td><td>11.83 (n/a)</td><td>11.15 (n/a)</td><td>10.83 (n/a)</td><td>1.24 (n/a)</td><td>13.63 (n/a)</td><td>11.82 (n/a)</td><td>11.14 (n/a)</td><td>10.82 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>25.28 (+1.21%)</td><td>24.10 (-1.56%)</td><td>23.77 (-2.93%)</td><td>23.72 (-1.16%)</td><td>0.67 <b>(+90.09%)</b></td><td>25.26 (+1.21%)</td><td>24.09 (-1.56%)</td><td>23.75 (-2.93%)</td><td>23.70 (-1.16%)</td><td>0.67 <b>(+90.09%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>24.98 (n/a)</td><td>24.48 (n/a)</td><td>24.49 (n/a)</td><td>24.00 (n/a)</td><td>0.35 (n/a)</td><td>24.96 (n/a)</td><td>24.47 (n/a)</td><td>24.47 (n/a)</td><td>23.98 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>40.47 (+0.01%)</td><td>39.39 (-1.27%)</td><td>39.21 (-1.99%)</td><td>38.49 (-1.93%)</td><td>0.86 <b>(+87.34%)</b></td><td>40.45 (+0.01%)</td><td>39.36 (-1.27%)</td><td>39.19 (-1.99%)</td><td>38.46 (-1.93%)</td><td>0.86 <b>(+87.34%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>40.47 (n/a)</td><td>39.89 (n/a)</td><td>40.01 (n/a)</td><td>39.24 (n/a)</td><td>0.46 (n/a)</td><td>40.45 (n/a)</td><td>39.87 (n/a)</td><td>39.98 (n/a)</td><td>39.22 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>43.10 (-6.46%)</td><td>42.43 (-2.92%)</td><td>42.82 (+0.57%)</td><td>41.47 (-0.86%)</td><td>0.74 <b>(-65.86%)</b></td><td>43.08 (-6.46%)</td><td>42.40 (-2.92%)</td><td>42.79 (+0.57%)</td><td>41.44 (-0.86%)</td><td>0.74 <b>(-65.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>46.08 (n/a)</td><td>43.70 (n/a)</td><td>42.57 (n/a)</td><td>41.83 (n/a)</td><td>2.16 (n/a)</td><td>46.05 (n/a)</td><td>43.67 (n/a)</td><td>42.55 (n/a)</td><td>41.80 (n/a)</td><td>2.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>152.46 (n/a)</td><td>154.20 (n/a)</td><td>110.80 (n/a)</td><td>42.07 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>328.90 (n/a)</td><td>236.10 (n/a)</td><td>204.20 (n/a)</td><td>168.90 (n/a)</td><td>74.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>172.62 (n/a)</td><td>169.10 (n/a)</td><td>152.10 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>188.04 (n/a)</td><td>185.40 (n/a)</td><td>136.90 (n/a)</td><td>47.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>161.48 (n/a)</td><td>157.40 (n/a)</td><td>116.60 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>184.62 (n/a)</td><td>171.50 (n/a)</td><td>162.60 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>161.10 (n/a)</td><td>151.30 (n/a)</td><td>132.50 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.80 (n/a)</td><td>215.42 (n/a)</td><td>212.00 (n/a)</td><td>203.80 (n/a)</td><td>12.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>165.40 (n/a)</td><td>156.30 (n/a)</td><td>109.10 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.20 (n/a)</td><td>202.70 (n/a)</td><td>185.10 (n/a)</td><td>155.00 (n/a)</td><td>62.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>179.20 (n/a)</td><td>179.80 (n/a)</td><td>143.30 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.20 (n/a)</td><td>185.38 (n/a)</td><td>155.00 (n/a)</td><td>141.10 (n/a)</td><td>66.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>154.96 (n/a)</td><td>153.90 (n/a)</td><td>111.40 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>179.28 (n/a)</td><td>199.00 (n/a)</td><td>138.60 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>180.36 (n/a)</td><td>195.80 (n/a)</td><td>132.20 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.90 (n/a)</td><td>216.42 (n/a)</td><td>224.00 (n/a)</td><td>187.50 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>256.70 (n/a)</td><td>203.36 (n/a)</td><td>217.80 (n/a)</td><td>118.10 (n/a)</td><td>59.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>260.40 (n/a)</td><td>186.84 (n/a)</td><td>217.30 (n/a)</td><td>113.70 (n/a)</td><td>64.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>187.08 (n/a)</td><td>191.00 (n/a)</td><td>156.40 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.20 (n/a)</td><td>191.96 (n/a)</td><td>177.90 (n/a)</td><td>145.10 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.60 (n/a)</td><td>195.14 (n/a)</td><td>197.50 (n/a)</td><td>165.00 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>256.60 (n/a)</td><td>198.56 (n/a)</td><td>189.60 (n/a)</td><td>174.90 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>305.90 (n/a)</td><td>204.88 (n/a)</td><td>202.00 (n/a)</td><td>124.20 (n/a)</td><td>67.14 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>212.40 (n/a)</td><td>227.60 (n/a)</td><td>168.40 (n/a)</td><td>27.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 <b>(+23.48%)</b></td><td>0.17 (-4.15%)</td><td>0.16 (-14.99%)</td><td>0.14 (-10.91%)</td><td>0.04 <b>(+196.75%)</b></td><td>227.50 (+12.23%)</td><td>197.06 (+7.11%)</td><td>206.80 (+17.63%)</td><td>140.60 (-19.01%)</td><td>34.83 <b>(+167.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>183.98 (n/a)</td><td>175.80 (n/a)</td><td>173.60 (n/a)</td><td>13.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>199.34 (n/a)</td><td>199.90 (n/a)</td><td>175.90 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.20 (n/a)</td><td>161.36 (n/a)</td><td>156.40 (n/a)</td><td>141.00 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.90 (n/a)</td><td>173.74 (n/a)</td><td>168.30 (n/a)</td><td>152.00 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.50 (n/a)</td><td>169.46 (n/a)</td><td>167.10 (n/a)</td><td>115.80 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.60 (n/a)</td><td>182.54 (n/a)</td><td>184.80 (n/a)</td><td>150.00 (n/a)</td><td>19.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>196.68 (n/a)</td><td>200.00 (n/a)</td><td>176.50 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>238.30 (n/a)</td><td>212.64 (n/a)</td><td>217.50 (n/a)</td><td>171.80 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-16.73%)</td><td>0.03 (-8.60%)</td><td>0.03 (-8.39%)</td><td>0.02 <b>(-22.54%)</b></td><td>0.01 (-0.54%)</td><td>224.30 <b>(+29.06%)</b></td><td>162.36 (+10.92%)</td><td>159.30 (+9.18%)</td><td>129.30 <b>(+20.06%)</b></td><td>38.98 <b>(+52.65%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>146.38 (n/a)</td><td>145.90 (n/a)</td><td>107.70 (n/a)</td><td>25.53 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-5.04%)</td><td>0.02 (+2.91%)</td><td>0.02 (+0.24%)</td><td>0.02 (+1.16%)</td><td>0.00 (-12.24%)</td><td>210.30 (-1.13%)</td><td>172.20 (-3.51%)</td><td>172.40 (-0.29%)</td><td>132.60 (+5.24%)</td><td>32.17 (-8.96%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>178.46 (n/a)</td><td>172.90 (n/a)</td><td>126.00 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+2.82%)</td><td>0.03 (-2.19%)</td><td>0.03 (+5.98%)</td><td>0.01 <b>(-35.37%)</b></td><td>0.01 <b>(+26.19%)</b></td><td>325.70 <b>(+54.73%)</b></td><td>185.16 (+9.70%)</td><td>159.80 (-5.61%)</td><td>109.90 (-2.74%)</td><td>82.50 <b>(+96.70%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>168.78 (n/a)</td><td>169.30 (n/a)</td><td>113.00 (n/a)</td><td>41.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-8.87%)</td><td>0.02 (-3.66%)</td><td>0.03 (+10.93%)</td><td>0.01 <b>(-38.88%)</b></td><td>0.01 <b>(+53.78%)</b></td><td>359.50 <b>(+63.63%)</b></td><td>206.60 (+12.77%)</td><td>162.10 (-9.84%)</td><td>148.80 (+9.73%)</td><td>89.00 <b>(+182.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.70 (n/a)</td><td>183.20 (n/a)</td><td>179.80 (n/a)</td><td>135.60 (n/a)</td><td>31.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-1.81%)</td><td>0.02 (+15.35%)</td><td>0.03 <b>(+37.90%)</b></td><td>0.02 <b>(+24.49%)</b></td><td>0.00 <b>(-56.04%)</b></td><td>192.10 (-19.66%)</td><td>168.74 (-16.34%)</td><td>163.60 <b>(-27.48%)</b></td><td>151.90 (+1.88%)</td><td>15.86 <b>(-64.10%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>201.70 (n/a)</td><td>225.60 (n/a)</td><td>149.10 (n/a)</td><td>44.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-4.85%)</td><td>0.02 (+10.57%)</td><td>0.02 (+4.41%)</td><td>0.02 <b>(+25.05%)</b></td><td>0.00 <b>(-35.78%)</b></td><td>208.70 <b>(-20.04%)</b></td><td>184.60 (-12.12%)</td><td>198.10 (-4.21%)</td><td>147.50 (+5.13%)</td><td>25.31 <b>(-44.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.00 (n/a)</td><td>210.06 (n/a)</td><td>206.80 (n/a)</td><td>140.30 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-4.02%)</td><td>0.02 (+6.43%)</td><td>0.02 (+10.75%)</td><td>0.02 (+11.92%)</td><td>0.00 <b>(-34.02%)</b></td><td>200.50 (-10.65%)</td><td>181.56 (-7.20%)</td><td>181.90 (-9.68%)</td><td>157.70 (+4.16%)</td><td>18.77 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.40 (n/a)</td><td>195.64 (n/a)</td><td>201.40 (n/a)</td><td>151.40 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+4.54%)</td><td>0.02 <b>(+20.60%)</b></td><td>0.02 <b>(+23.95%)</b></td><td>0.02 <b>(+26.42%)</b></td><td>0.00 <b>(-26.73%)</b></td><td>259.10 <b>(-20.91%)</b></td><td>207.14 (-19.22%)</td><td>205.80 (-19.29%)</td><td>174.70 (-4.33%)</td><td>32.80 <b>(-44.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>327.60 (n/a)</td><td>256.44 (n/a)</td><td>255.00 (n/a)</td><td>182.60 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 <b>(+52.74%)</b></td><td>0.06 <b>(+45.61%)</b></td><td>0.06 <b>(+39.71%)</b></td><td>0.05 <b>(+34.00%)</b></td><td>0.01 <b>(+90.98%)</b></td><td>160.80 <b>(-25.38%)</b></td><td>130.40 <b>(-30.66%)</b></td><td>126.70 <b>(-28.42%)</b></td><td>104.30 <b>(-34.57%)</b></td><td>22.30 (-8.40%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>188.06 (n/a)</td><td>177.00 (n/a)</td><td>159.40 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+10.87%)</td><td>0.05 (+17.30%)</td><td>0.06 <b>(+25.35%)</b></td><td>0.05 (+18.74%)</td><td>0.01 (-16.65%)</td><td>181.50 (-15.82%)</td><td>151.62 (-16.08%)</td><td>146.50 <b>(-20.21%)</b></td><td>123.60 (-9.78%)</td><td>22.13 <b>(-37.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>180.68 (n/a)</td><td>183.60 (n/a)</td><td>137.00 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+21.59%)</b></td><td>0.06 <b>(+26.74%)</b></td><td>0.06 <b>(+30.05%)</b></td><td>0.05 <b>(+37.14%)</b></td><td>0.01 (-10.70%)</td><td>164.90 <b>(-27.10%)</b></td><td>136.52 <b>(-22.42%)</b></td><td>132.40 <b>(-23.07%)</b></td><td>115.30 (-17.76%)</td><td>20.00 <b>(-45.22%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>175.98 (n/a)</td><td>172.10 (n/a)</td><td>140.20 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+27.04%)</b></td><td>0.05 <b>(+31.11%)</b></td><td>0.06 <b>(+26.71%)</b></td><td>0.05 <b>(+54.93%)</b></td><td>0.01 (-8.26%)</td><td>179.30 <b>(-35.43%)</b></td><td>155.10 <b>(-25.43%)</b></td><td>148.30 <b>(-21.08%)</b></td><td>125.30 <b>(-21.24%)</b></td><td>22.89 <b>(-52.78%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.70 (n/a)</td><td>208.00 (n/a)</td><td>187.90 (n/a)</td><td>159.10 (n/a)</td><td>48.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-4.20%)</td><td>0.05 (+8.71%)</td><td>0.05 (-0.48%)</td><td>0.05 <b>(+85.77%)</b></td><td>0.00 <b>(-65.08%)</b></td><td>177.70 <b>(-46.15%)</b></td><td>163.22 (-15.47%)</td><td>164.00 (+0.49%)</td><td>148.20 (+4.37%)</td><td>14.29 <b>(-81.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.00 (n/a)</td><td>193.10 (n/a)</td><td>163.20 (n/a)</td><td>142.00 (n/a)</td><td>77.45 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+12.36%)</td><td>0.05 (+3.24%)</td><td>0.05 (+6.37%)</td><td>0.04 (-7.10%)</td><td>0.01 <b>(+51.73%)</b></td><td>222.20 (+7.66%)</td><td>180.66 (-0.86%)</td><td>182.00 (-5.99%)</td><td>123.90 (-10.99%)</td><td>38.95 <b>(+47.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>182.22 (n/a)</td><td>193.60 (n/a)</td><td>139.20 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (+13.08%)</td><td>0.05 (+9.38%)</td><td>0.05 (+3.00%)</td><td>0.03 (+6.41%)</td><td>0.01 <b>(+25.17%)</b></td><td>266.10 (-6.04%)</td><td>185.26 (-7.57%)</td><td>181.30 (-2.89%)</td><td>133.50 (-11.53%)</td><td>50.16 (+1.70%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.20 (n/a)</td><td>200.44 (n/a)</td><td>186.70 (n/a)</td><td>150.90 (n/a)</td><td>49.32 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 <b>(+38.33%)</b></td><td>0.05 (+16.75%)</td><td>0.05 (+14.80%)</td><td>0.04 (+14.51%)</td><td>0.01 <b>(+122.45%)</b></td><td>209.20 (-12.69%)</td><td>175.34 (-12.69%)</td><td>172.10 (-12.90%)</td><td>130.90 <b>(-27.72%)</b></td><td>31.91 <b>(+39.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.60 (n/a)</td><td>200.82 (n/a)</td><td>197.60 (n/a)</td><td>181.10 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 <b>(+54.68%)</b></td><td>0.05 (+17.07%)</td><td>0.04 (+10.50%)</td><td>0.03 (-15.47%)</td><td>0.01 <b>(+1285.61%)</b></td><td>247.00 (+18.30%)</td><td>182.72 (-10.42%)</td><td>185.80 (-9.50%)</td><td>128.50 <b>(-35.33%)</b></td><td>44.44 <b>(+957.68%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.80 (n/a)</td><td>203.98 (n/a)</td><td>205.30 (n/a)</td><td>198.70 (n/a)</td><td>4.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+19.60%)</td><td>0.04 (+4.95%)</td><td>0.04 (+12.26%)</td><td>0.02 <b>(-36.60%)</b></td><td>0.01 <b>(+354.02%)</b></td><td>375.60 <b>(+57.75%)</b></td><td>235.08 (+2.61%)</td><td>211.10 (-10.93%)</td><td>172.90 (-16.39%)</td><td>82.39 <b>(+510.04%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>229.10 (n/a)</td><td>237.00 (n/a)</td><td>206.80 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-2.60%)</td><td>0.10 (+3.19%)</td><td>0.10 (-0.66%)</td><td>0.08 <b>(+21.77%)</b></td><td>0.02 <b>(-28.00%)</b></td><td>198.70 (-17.86%)</td><td>165.60 (-6.39%)</td><td>168.00 (+0.66%)</td><td>125.40 (+2.62%)</td><td>29.82 <b>(-39.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>241.90 (n/a)</td><td>176.90 (n/a)</td><td>166.90 (n/a)</td><td>122.20 (n/a)</td><td>49.36 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(+25.07%)</b></td><td>0.10 (+5.83%)</td><td>0.09 (-5.84%)</td><td>0.08 (-2.15%)</td><td>0.02 <b>(+162.95%)</b></td><td>195.30 (+2.20%)</td><td>166.06 (-3.78%)</td><td>177.10 (+6.18%)</td><td>128.40 <b>(-20.05%)</b></td><td>26.53 <b>(+112.46%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>172.58 (n/a)</td><td>166.80 (n/a)</td><td>160.60 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(+39.24%)</b></td><td>0.11 <b>(+34.27%)</b></td><td>0.11 <b>(+36.07%)</b></td><td>0.09 (+19.67%)</td><td>0.01 <b>(+161.26%)</b></td><td>173.40 (-16.43%)</td><td>149.30 <b>(-24.72%)</b></td><td>150.10 <b>(-26.49%)</b></td><td>127.20 <b>(-28.22%)</b></td><td>19.83 <b>(+56.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>198.32 (n/a)</td><td>204.20 (n/a)</td><td>177.20 (n/a)</td><td>12.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+17.04%)</td><td>0.10 (+12.92%)</td><td>0.09 (+11.51%)</td><td>0.07 (-10.32%)</td><td>0.03 <b>(+100.51%)</b></td><td>236.60 (+11.50%)</td><td>180.08 (-6.77%)</td><td>183.10 (-10.33%)</td><td>125.20 (-14.60%)</td><td>51.84 <b>(+90.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>193.16 (n/a)</td><td>204.20 (n/a)</td><td>146.60 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+14.05%)</td><td>0.10 (+10.94%)</td><td>0.11 (+14.75%)</td><td>0.07 <b>(+41.92%)</b></td><td>0.03 (+6.79%)</td><td>240.20 <b>(-29.52%)</b></td><td>177.24 (-12.29%)</td><td>152.60 (-12.85%)</td><td>124.80 (-12.30%)</td><td>50.14 <b>(-36.66%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>340.80 (n/a)</td><td>202.08 (n/a)</td><td>175.10 (n/a)</td><td>142.30 (n/a)</td><td>79.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (+19.50%)</td><td>0.10 <b>(+23.65%)</b></td><td>0.10 <b>(+28.35%)</b></td><td>0.07 <b>(+27.24%)</b></td><td>0.02 (+9.18%)</td><td>239.80 <b>(-21.40%)</b></td><td>168.64 (-19.90%)</td><td>156.40 <b>(-22.07%)</b></td><td>131.40 (-16.31%)</td><td>41.63 <b>(-26.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>305.10 (n/a)</td><td>210.54 (n/a)</td><td>200.70 (n/a)</td><td>157.00 (n/a)</td><td>56.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 <b>(+26.23%)</b></td><td>0.09 (+13.37%)</td><td>0.09 (+13.61%)</td><td>0.07 (+14.11%)</td><td>0.02 <b>(+49.31%)</b></td><td>248.20 (-12.36%)</td><td>190.60 (-10.80%)</td><td>174.80 (-11.98%)</td><td>152.70 <b>(-20.76%)</b></td><td>39.93 (+2.42%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>283.20 (n/a)</td><td>213.68 (n/a)</td><td>198.60 (n/a)</td><td>192.70 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (+14.66%)</td><td>0.09 <b>(+42.90%)</b></td><td>0.10 <b>(+38.73%)</b></td><td>0.07 <b>(+70.83%)</b></td><td>0.01 <b>(-41.01%)</b></td><td>224.10 <b>(-41.46%)</b></td><td>178.74 <b>(-34.32%)</b></td><td>170.00 <b>(-27.91%)</b></td><td>160.20 (-12.75%)</td><td>25.88 <b>(-70.03%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>382.80 (n/a)</td><td>272.14 (n/a)</td><td>235.80 (n/a)</td><td>183.60 (n/a)</td><td>86.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (+13.54%)</td><td>0.20 (+15.68%)</td><td>0.22 <b>(+30.53%)</b></td><td>0.16 (+1.40%)</td><td>0.03 <b>(+88.04%)</b></td><td>205.30 (-1.35%)</td><td>166.46 (-12.30%)</td><td>147.90 <b>(-23.41%)</b></td><td>144.20 (-11.91%)</td><td>28.15 <b>(+62.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>189.80 (n/a)</td><td>193.10 (n/a)</td><td>163.70 (n/a)</td><td>17.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (+14.37%)</td><td>0.21 (+12.06%)</td><td>0.21 (+10.69%)</td><td>0.19 (+19.94%)</td><td>0.03 (+9.48%)</td><td>172.40 (-16.59%)</td><td>155.72 (-10.91%)</td><td>159.80 (-9.67%)</td><td>127.70 (-12.59%)</td><td>17.21 <b>(-21.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>174.78 (n/a)</td><td>176.90 (n/a)</td><td>146.10 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (+11.39%)</td><td>0.18 (-6.01%)</td><td>0.15 (-18.25%)</td><td>0.09 <b>(-31.83%)</b></td><td>0.07 <b>(+52.58%)</b></td><td>346.30 <b>(+46.68%)</b></td><td>210.40 (+15.21%)</td><td>212.10 <b>(+22.32%)</b></td><td>124.30 (-10.25%)</td><td>86.27 <b>(+99.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>236.10 (n/a)</td><td>182.62 (n/a)</td><td>173.40 (n/a)</td><td>138.50 (n/a)</td><td>43.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (+7.79%)</td><td>0.20 (+15.37%)</td><td>0.20 (+12.69%)</td><td>0.18 <b>(+35.61%)</b></td><td>0.02 <b>(-29.27%)</b></td><td>180.70 <b>(-26.24%)</b></td><td>162.62 (-15.02%)</td><td>164.30 (-11.24%)</td><td>137.20 (-7.23%)</td><td>18.47 <b>(-51.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>245.00 (n/a)</td><td>191.36 (n/a)</td><td>185.10 (n/a)</td><td>147.90 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (+4.59%)</td><td>0.19 (+14.53%)</td><td>0.21 <b>(+35.20%)</b></td><td>0.16 (+3.74%)</td><td>0.03 <b>(+23.58%)</b></td><td>208.20 (-3.61%)</td><td>173.62 (-12.05%)</td><td>157.10 <b>(-26.04%)</b></td><td>146.70 (-4.37%)</td><td>30.94 (+15.63%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.00 (n/a)</td><td>197.40 (n/a)</td><td>212.40 (n/a)</td><td>153.40 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (+14.75%)</td><td>0.19 (+8.63%)</td><td>0.21 (+18.34%)</td><td>0.13 (-16.97%)</td><td>0.04 <b>(+135.79%)</b></td><td>258.90 <b>(+20.42%)</b></td><td>180.70 (-4.56%)</td><td>157.10 (-15.54%)</td><td>148.50 (-12.85%)</td><td>46.59 <b>(+147.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>189.34 (n/a)</td><td>186.00 (n/a)</td><td>170.40 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 (-9.50%)</td><td>0.16 (+8.32%)</td><td>0.16 (-0.79%)</td><td>0.15 <b>(+76.30%)</b></td><td>0.01 <b>(-70.69%)</b></td><td>215.50 <b>(-43.29%)</b></td><td>203.56 (-14.61%)</td><td>208.80 (+0.77%)</td><td>179.10 (+10.49%)</td><td>14.76 <b>(-82.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>380.00 (n/a)</td><td>238.40 (n/a)</td><td>207.20 (n/a)</td><td>162.10 (n/a)</td><td>84.62 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+16.88%)</td><td>0.03 (+9.93%)</td><td>0.03 <b>(+25.30%)</b></td><td>0.02 (-3.84%)</td><td>0.01 <b>(+37.23%)</b></td><td>234.00 (+3.95%)</td><td>169.36 (-7.04%)</td><td>149.40 <b>(-20.15%)</b></td><td>121.70 (-14.48%)</td><td>44.83 <b>(+26.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>182.18 (n/a)</td><td>187.10 (n/a)</td><td>142.30 (n/a)</td><td>35.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+3.35%)</td><td>0.03 (+8.25%)</td><td>0.03 (+11.51%)</td><td>0.02 (+6.49%)</td><td>0.00 (-8.03%)</td><td>198.80 (-6.09%)</td><td>158.08 (-8.09%)</td><td>151.00 (-10.33%)</td><td>131.20 (-3.17%)</td><td>25.31 (-15.00%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>172.00 (n/a)</td><td>168.40 (n/a)</td><td>135.50 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (-10.61%)</td><td>0.02 (-2.98%)</td><td>0.02 (+3.17%)</td><td>0.02 (-12.76%)</td><td>0.00 (-3.82%)</td><td>267.00 (+14.59%)</td><td>202.78 (+3.62%)</td><td>196.10 (-3.11%)</td><td>163.90 (+11.88%)</td><td>40.70 <b>(+27.34%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>195.70 (n/a)</td><td>202.40 (n/a)</td><td>146.50 (n/a)</td><td>31.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+16.76%)</td><td>0.02 (+5.44%)</td><td>0.02 (+16.98%)</td><td>0.01 <b>(-20.60%)</b></td><td>0.01 <b>(+97.07%)</b></td><td>284.60 <b>(+25.93%)</b></td><td>199.02 (-1.27%)</td><td>176.30 (-14.50%)</td><td>146.70 (-14.36%)</td><td>54.45 <b>(+115.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>201.58 (n/a)</td><td>206.20 (n/a)</td><td>171.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+4.34%)</td><td>0.03 (+17.82%)</td><td>0.03 (+18.25%)</td><td>0.02 <b>(+41.60%)</b></td><td>0.00 <b>(-30.09%)</b></td><td>166.80 <b>(-29.38%)</b></td><td>139.40 (-17.63%)</td><td>139.30 (-15.42%)</td><td>116.80 (-4.11%)</td><td>19.36 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>169.24 (n/a)</td><td>164.70 (n/a)</td><td>121.80 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-17.94%)</td><td>0.02 (-5.22%)</td><td>0.02 (-13.24%)</td><td>0.02 (+15.79%)</td><td>0.00 <b>(-43.70%)</b></td><td>203.30 (-13.64%)</td><td>179.48 (-0.11%)</td><td>200.90 (+15.26%)</td><td>135.00 <b>(+21.84%)</b></td><td>31.98 <b>(-41.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>179.68 (n/a)</td><td>174.30 (n/a)</td><td>110.80 (n/a)</td><td>55.10 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+3.14%)</td><td>0.03 (+8.13%)</td><td>0.03 <b>(+23.56%)</b></td><td>0.02 (-3.14%)</td><td>0.01 <b>(+23.26%)</b></td><td>215.40 (+3.21%)</td><td>158.72 (-5.13%)</td><td>149.70 (-19.04%)</td><td>110.30 (-2.99%)</td><td>48.22 <b>(+24.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>167.30 (n/a)</td><td>184.90 (n/a)</td><td>113.70 (n/a)</td><td>38.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+10.15%)</td><td>0.03 (+11.86%)</td><td>0.03 (+9.44%)</td><td>0.02 <b>(+35.25%)</b></td><td>0.00 <b>(-20.47%)</b></td><td>213.10 <b>(-26.06%)</b></td><td>160.78 (-13.53%)</td><td>149.10 (-8.64%)</td><td>134.10 (-9.21%)</td><td>30.57 <b>(-47.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>288.20 (n/a)</td><td>185.94 (n/a)</td><td>163.20 (n/a)</td><td>147.70 (n/a)</td><td>57.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-0.65%)</td><td>0.02 (-19.17%)</td><td>0.02 <b>(-38.76%)</b></td><td>0.02 <b>(-21.86%)</b></td><td>0.01 <b>(+25.68%)</b></td><td>239.70 <b>(+27.98%)</b></td><td>193.52 <b>(+28.01%)</b></td><td>213.70 <b>(+63.38%)</b></td><td>125.40 (+0.64%)</td><td>52.32 <b>(+63.45%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>151.18 (n/a)</td><td>130.80 (n/a)</td><td>124.60 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(+25.20%)</b></td><td>0.03 (+14.15%)</td><td>0.02 (+7.98%)</td><td>0.02 (+0.08%)</td><td>0.01 <b>(+151.95%)</b></td><td>203.10 (-0.10%)</td><td>163.06 (-8.77%)</td><td>166.90 (-7.38%)</td><td>119.30 <b>(-20.15%)</b></td><td>39.92 <b>(+104.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.30 (n/a)</td><td>178.74 (n/a)</td><td>180.20 (n/a)</td><td>149.40 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(+28.52%)</b></td><td>0.02 (+19.66%)</td><td>0.03 (+9.76%)</td><td>0.02 <b>(+72.77%)</b></td><td>0.00 (-19.56%)</td><td>215.80 <b>(-42.11%)</b></td><td>169.14 <b>(-21.70%)</b></td><td>161.00 (-8.89%)</td><td>130.40 <b>(-22.20%)</b></td><td>31.23 <b>(-64.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>372.80 (n/a)</td><td>216.02 (n/a)</td><td>176.70 (n/a)</td><td>167.60 (n/a)</td><td>88.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+9.36%)</td><td>0.03 (-5.57%)</td><td>0.02 (-18.10%)</td><td>0.02 <b>(-28.69%)</b></td><td>0.01 <b>(+94.30%)</b></td><td>258.20 <b>(+40.25%)</b></td><td>180.56 (+14.21%)</td><td>183.90 <b>(+22.11%)</b></td><td>112.90 (-8.58%)</td><td>61.15 <b>(+137.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.10 (n/a)</td><td>158.10 (n/a)</td><td>150.60 (n/a)</td><td>123.50 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(+28.31%)</b></td><td>0.02 (+6.33%)</td><td>0.02 (+3.84%)</td><td>0.02 (-7.45%)</td><td>0.01 <b>(+126.93%)</b></td><td>235.60 (+8.07%)</td><td>194.06 (-2.80%)</td><td>201.40 (-3.73%)</td><td>130.10 <b>(-22.05%)</b></td><td>41.18 <b>(+84.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.00 (n/a)</td><td>199.64 (n/a)</td><td>209.20 (n/a)</td><td>166.90 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-18.46%)</td><td>0.02 (-5.98%)</td><td>0.03 (+12.39%)</td><td>0.02 (-5.43%)</td><td>0.00 <b>(-48.45%)</b></td><td>235.90 (+5.74%)</td><td>170.72 (+0.49%)</td><td>160.70 (-11.02%)</td><td>135.50 <b>(+22.62%)</b></td><td>38.10 <b>(-29.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>169.88 (n/a)</td><td>180.60 (n/a)</td><td>110.50 (n/a)</td><td>53.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-10.38%)</td><td>0.02 (+1.48%)</td><td>0.02 (+15.40%)</td><td>0.02 (+15.34%)</td><td>0.00 <b>(-34.05%)</b></td><td>217.60 (-13.27%)</td><td>178.32 (-4.26%)</td><td>164.50 (-13.33%)</td><td>143.60 (+11.58%)</td><td>30.67 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.90 (n/a)</td><td>186.26 (n/a)</td><td>189.80 (n/a)</td><td>128.70 (n/a)</td><td>46.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(-21.42%)</b></td><td>0.02 (-4.60%)</td><td>0.03 (+8.40%)</td><td>0.02 (+1.51%)</td><td>0.00 <b>(-41.74%)</b></td><td>203.70 (-1.50%)</td><td>169.64 (+2.11%)</td><td>156.40 (-7.73%)</td><td>136.10 <b>(+27.32%)</b></td><td>29.15 <b>(-20.98%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>166.14 (n/a)</td><td>169.50 (n/a)</td><td>106.90 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+3.11%)</td><td>0.05 (+10.16%)</td><td>0.05 (-6.65%)</td><td>0.04 <b>(+79.74%)</b></td><td>0.01 <b>(-41.59%)</b></td><td>186.40 <b>(-44.36%)</b></td><td>152.52 (-17.84%)</td><td>153.80 (+7.10%)</td><td>124.10 (-2.97%)</td><td>25.94 <b>(-69.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>335.00 (n/a)</td><td>185.64 (n/a)</td><td>143.60 (n/a)</td><td>127.90 (n/a)</td><td>86.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (+18.26%)</td><td>0.06 <b>(+28.86%)</b></td><td>0.06 <b>(+35.68%)</b></td><td>0.06 <b>(+39.20%)</b></td><td>0.01 <b>(-22.09%)</b></td><td>144.90 <b>(-28.16%)</b></td><td>128.16 <b>(-23.93%)</b></td><td>126.40 <b>(-26.30%)</b></td><td>105.90 (-15.48%)</td><td>14.83 <b>(-53.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>168.48 (n/a)</td><td>171.50 (n/a)</td><td>125.30 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+10.11%)</td><td>0.04 (+14.93%)</td><td>0.05 <b>(+22.51%)</b></td><td>0.04 (+6.22%)</td><td>0.01 (+16.17%)</td><td>218.00 (-5.87%)</td><td>185.42 (-12.84%)</td><td>181.00 (-18.36%)</td><td>160.90 (-9.20%)</td><td>21.64 (+1.85%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.60 (n/a)</td><td>212.74 (n/a)</td><td>221.70 (n/a)</td><td>177.20 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-2.66%)</td><td>0.05 (+5.38%)</td><td>0.04 (-2.48%)</td><td>0.04 <b>(+20.23%)</b></td><td>0.01 <b>(-28.69%)</b></td><td>195.70 (-16.79%)</td><td>177.80 (-7.27%)</td><td>188.70 (+2.55%)</td><td>136.10 (+2.72%)</td><td>24.60 <b>(-39.81%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.20 (n/a)</td><td>191.74 (n/a)</td><td>184.00 (n/a)</td><td>132.50 (n/a)</td><td>40.88 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 <b>(+40.50%)</b></td><td>0.06 <b>(+22.18%)</b></td><td>0.06 <b>(+24.04%)</b></td><td>0.05 (-0.23%)</td><td>0.01 <b>(+279.21%)</b></td><td>170.80 (+0.23%)</td><td>133.56 (-16.22%)</td><td>129.20 (-19.40%)</td><td>104.10 <b>(-28.84%)</b></td><td>24.46 <b>(+174.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>170.40 (n/a)</td><td>159.42 (n/a)</td><td>160.30 (n/a)</td><td>146.30 (n/a)</td><td>8.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+9.75%)</td><td>0.05 (+13.02%)</td><td>0.05 (+6.24%)</td><td>0.04 <b>(+21.31%)</b></td><td>0.01 <b>(-20.41%)</b></td><td>197.20 (-17.56%)</td><td>155.08 (-13.60%)</td><td>149.30 (-5.86%)</td><td>124.10 (-8.88%)</td><td>26.56 <b>(-39.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>179.50 (n/a)</td><td>158.60 (n/a)</td><td>136.20 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+13.80%)</td><td>0.06 (+10.13%)</td><td>0.05 (+6.78%)</td><td>0.05 (+3.06%)</td><td>0.01 <b>(+30.66%)</b></td><td>177.10 (-2.96%)</td><td>148.44 (-8.78%)</td><td>149.90 (-6.31%)</td><td>119.10 (-12.17%)</td><td>20.63 (+9.48%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>162.72 (n/a)</td><td>160.00 (n/a)</td><td>135.60 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-7.83%)</td><td>0.05 (-5.36%)</td><td>0.06 (-3.93%)</td><td>0.02 <b>(-36.61%)</b></td><td>0.02 <b>(+20.01%)</b></td><td>368.00 <b>(+57.74%)</b></td><td>189.10 (+15.16%)</td><td>148.10 (+4.15%)</td><td>132.00 (+8.46%)</td><td>100.31 <b>(+117.58%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>164.20 (n/a)</td><td>142.20 (n/a)</td><td>121.70 (n/a)</td><td>46.10 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (+9.26%)</td><td>0.05 (+8.97%)</td><td>0.05 (+10.88%)</td><td>0.04 (+6.14%)</td><td>0.01 (+10.59%)</td><td>226.30 (-5.79%)</td><td>175.56 (-8.09%)</td><td>166.40 (-9.86%)</td><td>134.40 (-8.45%)</td><td>36.83 (-4.57%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.20 (n/a)</td><td>191.02 (n/a)</td><td>184.60 (n/a)</td><td>146.80 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+6.11%)</td><td>0.06 (+10.92%)</td><td>0.05 (+5.96%)</td><td>0.05 <b>(+44.47%)</b></td><td>0.01 <b>(-29.85%)</b></td><td>168.30 <b>(-30.77%)</b></td><td>148.72 (-12.59%)</td><td>152.00 (-5.65%)</td><td>124.60 (-5.75%)</td><td>20.22 <b>(-54.26%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>170.14 (n/a)</td><td>161.10 (n/a)</td><td>132.20 (n/a)</td><td>44.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (+14.00%)</td><td>0.05 (+17.03%)</td><td>0.05 (+8.21%)</td><td>0.04 <b>(+32.58%)</b></td><td>0.01 (-15.71%)</td><td>186.10 <b>(-24.56%)</b></td><td>154.14 (-16.47%)</td><td>152.10 (-7.59%)</td><td>124.40 (-12.27%)</td><td>24.53 <b>(-44.64%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>184.54 (n/a)</td><td>164.60 (n/a)</td><td>141.80 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-3.21%)</td><td>0.05 <b>(+21.96%)</b></td><td>0.05 <b>(+33.27%)</b></td><td>0.05 <b>(+33.19%)</b></td><td>0.01 <b>(-52.56%)</b></td><td>170.40 <b>(-24.93%)</b></td><td>153.92 <b>(-20.68%)</b></td><td>150.70 <b>(-24.95%)</b></td><td>133.30 (+3.33%)</td><td>14.74 <b>(-61.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>194.04 (n/a)</td><td>200.80 (n/a)</td><td>129.00 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+4.72%)</td><td>0.04 (+5.82%)</td><td>0.04 (-5.88%)</td><td>0.04 (+9.10%)</td><td>0.01 (-5.15%)</td><td>229.60 (-8.34%)</td><td>190.14 (-6.26%)</td><td>202.20 (+6.25%)</td><td>154.20 (-4.52%)</td><td>32.79 <b>(-20.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.50 (n/a)</td><td>202.84 (n/a)</td><td>190.30 (n/a)</td><td>161.50 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-9.46%)</td><td>0.04 (+11.14%)</td><td>0.04 (+15.01%)</td><td>0.03 <b>(+49.76%)</b></td><td>0.01 <b>(-33.23%)</b></td><td>248.10 <b>(-33.22%)</b></td><td>191.18 (-16.14%)</td><td>188.00 (-13.04%)</td><td>145.60 (+10.39%)</td><td>42.06 <b>(-52.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>371.50 (n/a)</td><td>227.98 (n/a)</td><td>216.20 (n/a)</td><td>131.90 (n/a)</td><td>87.94 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+1.66%)</td><td>0.05 (+14.41%)</td><td>0.05 <b>(+23.30%)</b></td><td>0.04 (+13.75%)</td><td>0.00 <b>(-26.36%)</b></td><td>201.10 (-12.07%)</td><td>170.38 (-13.38%)</td><td>162.30 (-18.93%)</td><td>155.90 (-1.64%)</td><td>18.19 <b>(-35.40%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>196.70 (n/a)</td><td>200.20 (n/a)</td><td>158.50 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+25.08%)</b></td><td>0.06 <b>(+38.20%)</b></td><td>0.06 <b>(+42.21%)</b></td><td>0.05 <b>(+117.58%)</b></td><td>0.01 <b>(-26.80%)</b></td><td>179.70 <b>(-54.04%)</b></td><td>147.88 <b>(-34.06%)</b></td><td>148.30 <b>(-29.68%)</b></td><td>121.80 <b>(-20.03%)</b></td><td>25.93 <b>(-73.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>391.00 (n/a)</td><td>224.28 (n/a)</td><td>210.90 (n/a)</td><td>152.30 (n/a)</td><td>97.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+4.96%)</td><td>0.13 <b>(+22.53%)</b></td><td>0.13 <b>(+45.96%)</b></td><td>0.11 <b>(+24.83%)</b></td><td>0.01 <b>(-37.75%)</b></td><td>154.40 (-19.88%)</td><td>128.82 <b>(-20.39%)</b></td><td>121.80 <b>(-31.46%)</b></td><td>116.00 (-4.76%)</td><td>15.68 <b>(-52.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>161.82 (n/a)</td><td>177.70 (n/a)</td><td>121.80 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+15.29%)</td><td>0.12 (+13.25%)</td><td>0.11 (+3.84%)</td><td>0.10 <b>(+43.05%)</b></td><td>0.02 (-16.46%)</td><td>163.20 <b>(-30.08%)</b></td><td>141.90 (-13.76%)</td><td>143.10 (-3.70%)</td><td>115.50 (-13.22%)</td><td>21.11 <b>(-48.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.40 (n/a)</td><td>164.54 (n/a)</td><td>148.60 (n/a)</td><td>133.10 (n/a)</td><td>41.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.09 (-5.28%)</td><td>0.08 (-11.71%)</td><td>0.07 (-17.96%)</td><td>0.06 (-11.20%)</td><td>0.01 (+12.10%)</td><td>256.30 (+12.61%)</td><td>216.40 (+13.76%)</td><td>221.10 <b>(+21.89%)</b></td><td>184.10 (+5.62%)</td><td>28.33 <b>(+30.41%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>190.22 (n/a)</td><td>181.40 (n/a)</td><td>174.30 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (-12.06%)</td><td>0.09 (-4.01%)</td><td>0.09 (+3.80%)</td><td>0.08 (-3.46%)</td><td>0.01 <b>(-43.24%)</b></td><td>207.20 (+3.60%)</td><td>181.14 (+3.26%)</td><td>175.20 (-3.63%)</td><td>165.80 (+13.72%)</td><td>15.76 <b>(-31.95%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>175.42 (n/a)</td><td>181.80 (n/a)</td><td>145.80 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 <b>(+32.89%)</b></td><td>0.11 (+13.59%)</td><td>0.10 (-0.88%)</td><td>0.09 <b>(+35.52%)</b></td><td>0.02 <b>(+26.34%)</b></td><td>186.90 <b>(-26.21%)</b></td><td>157.60 (-12.43%)</td><td>161.30 (+0.88%)</td><td>111.00 <b>(-24.75%)</b></td><td>29.84 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>253.30 (n/a)</td><td>179.98 (n/a)</td><td>159.90 (n/a)</td><td>147.50 (n/a)</td><td>43.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+1.39%)</td><td>0.11 (-3.19%)</td><td>0.11 (-10.84%)</td><td>0.10 (+6.08%)</td><td>0.01 <b>(-25.29%)</b></td><td>161.70 (-5.71%)</td><td>145.96 (+2.10%)</td><td>150.00 (+12.19%)</td><td>117.90 (-1.34%)</td><td>16.74 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>171.50 (n/a)</td><td>142.96 (n/a)</td><td>133.70 (n/a)</td><td>119.50 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 <b>(-23.11%)</b></td><td>0.09 (-16.43%)</td><td>0.09 (-16.89%)</td><td>0.08 (-4.41%)</td><td>0.01 <b>(-52.82%)</b></td><td>195.70 (+4.60%)</td><td>176.20 (+17.65%)</td><td>181.20 <b>(+20.32%)</b></td><td>157.50 <b>(+30.06%)</b></td><td>16.85 <b>(-36.14%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>149.76 (n/a)</td><td>150.60 (n/a)</td><td>121.10 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (-1.42%)</td><td>0.11 (-4.76%)</td><td>0.13 (+14.72%)</td><td>0.08 <b>(-22.12%)</b></td><td>0.03 <b>(+76.16%)</b></td><td>216.60 <b>(+28.47%)</b></td><td>161.42 (+10.76%)</td><td>130.20 (-12.85%)</td><td>121.00 (+1.42%)</td><td>49.71 <b>(+134.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>168.60 (n/a)</td><td>145.74 (n/a)</td><td>149.40 (n/a)</td><td>119.30 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (-9.62%)</td><td>0.10 (-6.20%)</td><td>0.10 (-5.11%)</td><td>0.08 (-6.13%)</td><td>0.01 (-16.29%)</td><td>201.30 (+6.51%)</td><td>165.76 (+6.32%)</td><td>164.10 (+5.39%)</td><td>140.90 (+10.60%)</td><td>22.11 (+0.24%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>155.90 (n/a)</td><td>155.70 (n/a)</td><td>127.40 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 <b>(-24.91%)</b></td><td>0.09 <b>(-23.38%)</b></td><td>0.09 <b>(-26.21%)</b></td><td>0.07 (-9.10%)</td><td>0.01 <b>(-53.53%)</b></td><td>228.00 (+9.99%)</td><td>192.58 <b>(+27.84%)</b></td><td>188.50 <b>(+35.51%)</b></td><td>171.40 <b>(+33.18%)</b></td><td>21.81 <b>(-32.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.30 (n/a)</td><td>150.64 (n/a)</td><td>139.10 (n/a)</td><td>128.70 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (-9.06%)</td><td>0.09 (-15.36%)</td><td>0.08 <b>(-22.68%)</b></td><td>0.08 (-13.94%)</td><td>0.01 (+11.43%)</td><td>204.70 (+16.17%)</td><td>184.54 (+18.84%)</td><td>197.00 <b>(+29.35%)</b></td><td>146.50 (+9.98%)</td><td>24.79 <b>(+41.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>155.28 (n/a)</td><td>152.30 (n/a)</td><td>133.20 (n/a)</td><td>17.49 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (-10.31%)</td><td>0.10 (-14.09%)</td><td>0.10 (-17.12%)</td><td>0.08 (-17.17%)</td><td>0.02 (-2.76%)</td><td>208.90 <b>(+20.75%)</b></td><td>166.74 (+16.90%)</td><td>164.40 <b>(+20.62%)</b></td><td>135.40 (+11.44%)</td><td>27.58 <b>(+31.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>173.00 (n/a)</td><td>142.64 (n/a)</td><td>136.30 (n/a)</td><td>121.50 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (-14.57%)</td><td>0.09 <b>(-24.79%)</b></td><td>0.08 <b>(-30.98%)</b></td><td>0.07 <b>(-23.39%)</b></td><td>0.01 <b>(+22.43%)</b></td><td>222.00 <b>(+30.51%)</b></td><td>196.26 <b>(+34.31%)</b></td><td>202.00 <b>(+44.91%)</b></td><td>154.40 (+17.06%)</td><td>28.31 <b>(+86.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.10 (n/a)</td><td>146.12 (n/a)</td><td>139.40 (n/a)</td><td>131.90 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (-10.01%)</td><td>0.10 (-10.32%)</td><td>0.09 (-8.44%)</td><td>0.08 (-12.85%)</td><td>0.01 (-13.24%)</td><td>211.20 (+14.78%)</td><td>170.54 (+11.49%)</td><td>173.60 (+9.25%)</td><td>143.00 (+11.11%)</td><td>26.57 (+13.80%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.00 (n/a)</td><td>152.96 (n/a)</td><td>158.90 (n/a)</td><td>128.70 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (-7.37%)</td><td>0.10 (-6.74%)</td><td>0.09 (-8.38%)</td><td>0.08 (-11.13%)</td><td>0.01 (+6.58%)</td><td>202.10 (+12.53%)</td><td>169.26 (+7.71%)</td><td>173.30 (+9.13%)</td><td>139.70 (+7.96%)</td><td>23.60 <b>(+31.71%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.60 (n/a)</td><td>157.14 (n/a)</td><td>158.80 (n/a)</td><td>129.40 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-3.92%)</td><td>0.10 (-6.86%)</td><td>0.10 (-13.46%)</td><td>0.09 <b>(+24.42%)</b></td><td>0.01 <b>(-36.95%)</b></td><td>189.10 (-19.60%)</td><td>164.26 (+3.83%)</td><td>162.20 (+15.53%)</td><td>130.50 (+4.15%)</td><td>22.08 <b>(-50.18%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.20 (n/a)</td><td>158.20 (n/a)</td><td>140.40 (n/a)</td><td>125.30 (n/a)</td><td>44.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (+7.11%)</td><td>0.19 (-12.34%)</td><td>0.16 <b>(-23.71%)</b></td><td>0.15 (-15.03%)</td><td>0.04 <b>(+94.95%)</b></td><td>213.10 (+17.67%)</td><td>182.38 (+17.14%)</td><td>202.30 <b>(+31.11%)</b></td><td>130.20 (-6.67%)</td><td>35.42 <b>(+115.47%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>181.10 (n/a)</td><td>155.70 (n/a)</td><td>154.30 (n/a)</td><td>139.50 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (-4.44%)</td><td>0.21 (+3.97%)</td><td>0.21 (+0.49%)</td><td>0.17 (+16.58%)</td><td>0.03 <b>(-27.71%)</b></td><td>197.60 (-14.24%)</td><td>157.92 (-5.92%)</td><td>152.70 (-0.46%)</td><td>131.00 (+4.63%)</td><td>25.74 <b>(-35.84%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.40 (n/a)</td><td>167.86 (n/a)</td><td>153.40 (n/a)</td><td>125.20 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (-3.27%)</td><td>0.16 (+3.70%)</td><td>0.16 (+4.22%)</td><td>0.15 (+5.06%)</td><td>0.01 <b>(-31.81%)</b></td><td>221.40 (-4.82%)</td><td>204.52 (-3.93%)</td><td>200.30 (-4.07%)</td><td>193.10 (+3.37%)</td><td>12.79 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>212.88 (n/a)</td><td>208.80 (n/a)</td><td>186.80 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (-3.83%)</td><td>0.17 (+0.66%)</td><td>0.17 (-2.67%)</td><td>0.13 (-7.08%)</td><td>0.02 (+0.42%)</td><td>249.30 (+7.60%)</td><td>198.48 (-0.51%)</td><td>192.60 (+2.72%)</td><td>171.90 (+3.99%)</td><td>31.52 (+8.80%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.70 (n/a)</td><td>199.50 (n/a)</td><td>187.50 (n/a)</td><td>165.30 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 <b>(+23.46%)</b></td><td>0.24 <b>(+38.25%)</b></td><td>0.24 <b>(+33.38%)</b></td><td>0.16 <b>(+58.04%)</b></td><td>0.06 (+11.07%)</td><td>200.80 <b>(-36.74%)</b></td><td>142.26 <b>(-29.81%)</b></td><td>138.00 <b>(-25.04%)</b></td><td>106.40 (-19.03%)</td><td>37.66 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>317.40 (n/a)</td><td>202.68 (n/a)</td><td>184.10 (n/a)</td><td>131.40 (n/a)</td><td>69.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 <b>(+30.19%)</b></td><td>0.22 <b>(+32.47%)</b></td><td>0.19 (+4.80%)</td><td>0.14 <b>(+62.44%)</b></td><td>0.07 (+19.71%)</td><td>237.00 <b>(-38.46%)</b></td><td>161.80 <b>(-27.84%)</b></td><td>169.20 (-4.57%)</td><td>107.80 <b>(-23.16%)</b></td><td>52.95 <b>(-47.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>385.10 (n/a)</td><td>224.22 (n/a)</td><td>177.30 (n/a)</td><td>140.30 (n/a)</td><td>99.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (-7.46%)</td><td>0.20 (-13.74%)</td><td>0.22 (+0.96%)</td><td>0.11 <b>(-38.57%)</b></td><td>0.06 <b>(+50.28%)</b></td><td>285.90 <b>(+62.81%)</b></td><td>182.48 <b>(+24.19%)</b></td><td>147.70 (-0.94%)</td><td>124.10 (+8.10%)</td><td>66.86 <b>(+167.01%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>175.60 (n/a)</td><td>146.94 (n/a)</td><td>149.10 (n/a)</td><td>114.80 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (-6.30%)</td><td>0.19 (-7.77%)</td><td>0.19 (-0.47%)</td><td>0.14 (-19.39%)</td><td>0.04 <b>(+39.43%)</b></td><td>229.30 <b>(+24.01%)</b></td><td>182.62 (+11.50%)</td><td>170.00 (+0.47%)</td><td>139.10 (+6.75%)</td><td>44.05 <b>(+87.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.90 (n/a)</td><td>163.78 (n/a)</td><td>169.20 (n/a)</td><td>130.30 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 <b>(-22.85%)</b></td><td>0.19 (-7.65%)</td><td>0.20 (-3.07%)</td><td>0.16 (-6.89%)</td><td>0.02 <b>(-43.57%)</b></td><td>209.30 (+7.39%)</td><td>170.94 (+6.84%)</td><td>166.00 (+3.17%)</td><td>154.80 <b>(+29.65%)</b></td><td>22.24 (-18.34%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.90 (n/a)</td><td>160.00 (n/a)</td><td>160.90 (n/a)</td><td>119.40 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 <b>(+39.51%)</b></td><td>0.25 <b>(+27.47%)</b></td><td>0.26 <b>(+35.79%)</b></td><td>0.18 (+7.52%)</td><td>0.05 <b>(+156.35%)</b></td><td>181.00 (-6.99%)</td><td>135.52 (-19.49%)</td><td>124.40 <b>(-26.35%)</b></td><td>108.90 <b>(-28.31%)</b></td><td>29.24 <b>(+72.25%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>168.32 (n/a)</td><td>168.90 (n/a)</td><td>151.90 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (-14.86%)</td><td>0.19 (-2.97%)</td><td>0.18 (-1.29%)</td><td>0.16 (+18.86%)</td><td>0.02 <b>(-48.84%)</b></td><td>198.90 (-15.86%)</td><td>178.94 (-0.13%)</td><td>183.00 (+1.33%)</td><td>144.90 (+17.52%)</td><td>20.24 <b>(-49.74%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.40 (n/a)</td><td>179.18 (n/a)</td><td>180.60 (n/a)</td><td>123.30 (n/a)</td><td>40.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (+4.29%)</td><td>0.20 (+7.82%)</td><td>0.18 (+1.45%)</td><td>0.16 <b>(+29.96%)</b></td><td>0.06 (-8.52%)</td><td>207.20 <b>(-23.03%)</b></td><td>171.26 (-9.78%)</td><td>182.60 (-1.46%)</td><td>111.80 (-4.12%)</td><td>38.54 <b>(-32.30%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>269.20 (n/a)</td><td>189.82 (n/a)</td><td>185.30 (n/a)</td><td>116.60 (n/a)</td><td>56.93 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (+12.88%)</td><td>0.19 (+2.36%)</td><td>0.18 (+3.91%)</td><td>0.12 (-19.51%)</td><td>0.05 <b>(+75.31%)</b></td><td>267.60 <b>(+24.23%)</b></td><td>186.56 (+2.26%)</td><td>179.10 (-3.76%)</td><td>131.90 (-11.42%)</td><td>55.07 <b>(+91.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.40 (n/a)</td><td>182.44 (n/a)</td><td>186.10 (n/a)</td><td>148.90 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (-10.10%)</td><td>0.18 (-5.87%)</td><td>0.17 (-2.90%)</td><td>0.15 (+16.01%)</td><td>0.03 <b>(-45.70%)</b></td><td>213.30 (-13.78%)</td><td>190.12 (+2.03%)</td><td>194.90 (+3.01%)</td><td>149.50 (+11.24%)</td><td>26.70 <b>(-45.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>247.40 (n/a)</td><td>186.34 (n/a)</td><td>189.20 (n/a)</td><td>134.40 (n/a)</td><td>49.28 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (+12.25%)</td><td>0.19 (+4.92%)</td><td>0.18 (+2.78%)</td><td>0.17 (+18.33%)</td><td>0.03 (+5.49%)</td><td>196.80 (-15.50%)</td><td>176.32 (-5.02%)</td><td>183.00 (-2.71%)</td><td>137.20 (-10.91%)</td><td>23.80 <b>(-21.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>232.90 (n/a)</td><td>185.64 (n/a)</td><td>188.10 (n/a)</td><td>154.00 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (-0.40%)</td><td>0.20 (-1.89%)</td><td>0.22 (+10.27%)</td><td>0.15 (-11.87%)</td><td>0.04 <b>(+63.75%)</b></td><td>219.70 (+13.48%)</td><td>171.56 (+4.17%)</td><td>151.50 (-9.34%)</td><td>142.20 (+0.42%)</td><td>35.85 <b>(+84.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>164.70 (n/a)</td><td>167.10 (n/a)</td><td>141.60 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (+0.02%)</td><td>0.21 (+0.08%)</td><td>0.21 (-0.02%)</td><td>0.21 (+0.35%)</td><td>0.00 <b>(-69.73%)</b></td><td>40869.30 (-0.35%)</td><td>40835.16 (-0.08%)</td><td>40835.90 (+0.02%)</td><td>40800.70 (-0.02%)</td><td>25.24 <b>(-69.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>41013.10 (n/a)</td><td>40867.64 (n/a)</td><td>40828.60 (n/a)</td><td>40807.80 (n/a)</td><td>83.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (+1.02%)</td><td>0.21 (+0.22%)</td><td>0.21 (-0.02%)</td><td>0.20 (+0.03%)</td><td>0.00 <b>(+255.39%)</b></td><td>40921.70 (-0.03%)</td><td>40754.02 (-0.22%)</td><td>40826.20 (+0.02%)</td><td>40373.70 (-1.01%)</td><td>217.31 <b>(+251.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40933.30 (n/a)</td><td>40841.94 (n/a)</td><td>40817.50 (n/a)</td><td>40786.30 (n/a)</td><td>61.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+0.11%)</td><td>0.13 (+0.02%)</td><td>0.13 (-0.00%)</td><td>0.13 (-0.01%)</td><td>0.00 <b>(+88.76%)</b></td><td>321962.60 (+0.01%)</td><td>321679.28 (-0.02%)</td><td>321693.60 (+0.00%)</td><td>321294.20 (-0.11%)</td><td>242.96 <b>(+88.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321919.60 (n/a)</td><td>321754.58 (n/a)</td><td>321678.70 (n/a)</td><td>321643.20 (n/a)</td><td>128.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+4.03%)</td><td>0.03 (+12.41%)</td><td>0.03 (+5.46%)</td><td>0.02 <b>(+38.75%)</b></td><td>0.00 (-17.47%)</td><td>170.10 <b>(-27.92%)</b></td><td>151.68 (-12.73%)</td><td>162.90 (-5.18%)</td><td>126.20 (-3.88%)</td><td>21.75 <b>(-43.92%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>173.80 (n/a)</td><td>171.80 (n/a)</td><td>131.30 (n/a)</td><td>38.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 <b>(+22.41%)</b></td><td>0.04 <b>(+25.00%)</b></td><td>0.04 (+14.53%)</td><td>0.03 <b>(+42.67%)</b></td><td>0.01 (+15.81%)</td><td>193.40 <b>(-29.90%)</b></td><td>161.28 <b>(-20.72%)</b></td><td>168.70 (-12.64%)</td><td>117.00 (-18.30%)</td><td>32.28 <b>(-33.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.90 (n/a)</td><td>203.44 (n/a)</td><td>193.10 (n/a)</td><td>143.20 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(+21.94%)</b></td><td>0.03 (+18.64%)</td><td>0.03 (+17.14%)</td><td>0.02 (+15.30%)</td><td>0.01 <b>(+34.98%)</b></td><td>203.70 (-13.25%)</td><td>154.22 (-15.03%)</td><td>155.70 (-14.64%)</td><td>118.00 (-18.00%)</td><td>33.39 (-4.65%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.80 (n/a)</td><td>181.50 (n/a)</td><td>182.40 (n/a)</td><td>143.90 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.04 (+7.46%)</td><td>0.03 (+3.10%)</td><td>0.03 (-0.41%)</td><td>0.03 (+2.62%)</td><td>0.00 <b>(+20.63%)</b></td><td>198.80 (-2.55%)</td><td>175.66 (-2.74%)</td><td>178.10 (+0.39%)</td><td>144.50 (-6.89%)</td><td>20.59 (+7.49%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.00 (n/a)</td><td>180.60 (n/a)</td><td>177.40 (n/a)</td><td>155.20 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-3.27%)</td><td>0.03 (+7.67%)</td><td>0.03 (+13.21%)</td><td>0.02 (+6.90%)</td><td>0.00 <b>(-33.01%)</b></td><td>193.90 (-6.46%)</td><td>157.02 (-8.63%)</td><td>146.40 (-11.70%)</td><td>143.00 (+3.40%)</td><td>21.17 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.30 (n/a)</td><td>171.86 (n/a)</td><td>165.80 (n/a)</td><td>138.30 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+3.15%)</td><td>0.03 (+4.69%)</td><td>0.03 (+11.89%)</td><td>0.02 (+0.14%)</td><td>0.01 <b>(+26.05%)</b></td><td>233.30 (-0.13%)</td><td>177.16 (-3.48%)</td><td>154.60 (-10.64%)</td><td>148.00 (-3.08%)</td><td>37.52 (+18.50%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.60 (n/a)</td><td>183.54 (n/a)</td><td>173.00 (n/a)</td><td>152.70 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(+24.54%)</b></td><td>0.03 <b>(+23.93%)</b></td><td>0.02 <b>(+23.75%)</b></td><td>0.02 <b>(+29.32%)</b></td><td>0.00 (-3.96%)</td><td>177.70 <b>(-22.67%)</b></td><td>162.76 (-19.75%)</td><td>167.00 (-19.17%)</td><td>140.70 (-19.69%)</td><td>15.53 <b>(-39.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>202.82 (n/a)</td><td>206.60 (n/a)</td><td>175.20 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-8.35%)</td><td>0.03 (-10.16%)</td><td>0.03 (-10.22%)</td><td>0.02 (-12.69%)</td><td>0.01 (-4.19%)</td><td>250.80 (+14.52%)</td><td>188.58 (+11.85%)</td><td>172.60 (+11.43%)</td><td>149.40 (+9.05%)</td><td>42.60 <b>(+20.45%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>168.60 (n/a)</td><td>154.90 (n/a)</td><td>137.00 (n/a)</td><td>35.37 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 <b>(-20.04%)</b></td><td>0.02 (-11.45%)</td><td>0.02 (+3.30%)</td><td>0.02 (-7.31%)</td><td>0.00 <b>(-21.08%)</b></td><td>241.10 (+7.87%)</td><td>187.16 (+12.25%)</td><td>165.50 (-3.22%)</td><td>150.20 <b>(+25.06%)</b></td><td>41.83 (+7.30%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>166.74 (n/a)</td><td>171.00 (n/a)</td><td>120.10 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-1.79%)</td><td>0.03 (-1.06%)</td><td>0.03 (-1.04%)</td><td>0.02 (+10.21%)</td><td>0.00 <b>(-29.97%)</b></td><td>196.90 (-9.26%)</td><td>174.48 (-0.11%)</td><td>175.90 (+1.09%)</td><td>145.30 (+1.82%)</td><td>18.66 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>174.68 (n/a)</td><td>174.00 (n/a)</td><td>142.70 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+4.00%)</td><td>0.02 (-11.51%)</td><td>0.02 <b>(-25.25%)</b></td><td>0.01 <b>(-32.47%)</b></td><td>0.01 <b>(+67.53%)</b></td><td>349.20 <b>(+48.09%)</b></td><td>223.90 <b>(+24.78%)</b></td><td>240.10 <b>(+33.76%)</b></td><td>133.60 (-3.88%)</td><td>90.62 <b>(+125.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>179.44 (n/a)</td><td>179.50 (n/a)</td><td>139.00 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-4.95%)</td><td>0.02 (+0.23%)</td><td>0.02 (+2.93%)</td><td>0.02 (+1.18%)</td><td>0.00 <b>(-36.40%)</b></td><td>206.30 (-1.15%)</td><td>186.22 (-0.77%)</td><td>188.40 (-2.84%)</td><td>172.20 (+5.19%)</td><td>13.40 <b>(-33.55%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>187.66 (n/a)</td><td>193.90 (n/a)</td><td>163.70 (n/a)</td><td>20.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (+15.29%)</td><td>0.02 (-9.31%)</td><td>0.02 (-17.97%)</td><td>0.01 <b>(-29.27%)</b></td><td>0.01 <b>(+177.96%)</b></td><td>289.90 <b>(+41.41%)</b></td><td>202.84 (+17.22%)</td><td>203.70 <b>(+21.90%)</b></td><td>138.60 (-13.27%)</td><td>60.14 <b>(+229.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>173.04 (n/a)</td><td>167.10 (n/a)</td><td>159.80 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.03 (-8.76%)</td><td>0.03 (+3.18%)</td><td>0.03 (+5.85%)</td><td>0.02 (+4.13%)</td><td>0.00 <b>(-37.27%)</b></td><td>200.80 (-3.92%)</td><td>173.74 (-3.95%)</td><td>173.60 (-5.50%)</td><td>157.30 (+9.62%)</td><td>16.70 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>180.88 (n/a)</td><td>183.70 (n/a)</td><td>143.50 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.02 (+4.67%)</td><td>0.02 (+13.80%)</td><td>0.02 (+14.94%)</td><td>0.02 (+19.30%)</td><td>0.00 (-14.90%)</td><td>219.90 (-16.16%)</td><td>192.62 (-12.64%)</td><td>187.90 (-13.01%)</td><td>172.70 (-4.43%)</td><td>19.99 <b>(-31.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.30 (n/a)</td><td>220.48 (n/a)</td><td>216.00 (n/a)</td><td>180.70 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (+2.81%)</td><td>0.05 (-13.89%)</td><td>0.05 (-13.30%)</td><td>0.03 <b>(-23.03%)</b></td><td>0.01 <b>(+33.50%)</b></td><td>281.70 <b>(+29.94%)</b></td><td>192.66 <b>(+20.28%)</b></td><td>169.70 (+15.36%)</td><td>131.90 (-2.73%)</td><td>57.09 <b>(+70.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>160.18 (n/a)</td><td>147.10 (n/a)</td><td>135.60 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 <b>(+23.34%)</b></td><td>0.09 (+11.52%)</td><td>0.09 <b>(+22.28%)</b></td><td>0.06 (-13.97%)</td><td>0.02 <b>(+99.99%)</b></td><td>218.70 (+16.21%)</td><td>150.52 (-5.58%)</td><td>137.40 (-18.26%)</td><td>108.00 (-18.92%)</td><td>46.63 <b>(+90.71%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>159.42 (n/a)</td><td>168.10 (n/a)</td><td>133.20 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 <b>(+20.27%)</b></td><td>0.05 (+15.35%)</td><td>0.05 (+9.15%)</td><td>0.05 <b>(+36.47%)</b></td><td>0.01 (-18.49%)</td><td>168.20 <b>(-26.74%)</b></td><td>153.36 (-14.24%)</td><td>157.80 (-8.36%)</td><td>132.80 (-16.84%)</td><td>14.18 <b>(-51.23%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>178.82 (n/a)</td><td>172.20 (n/a)</td><td>159.70 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 (+2.29%)</td><td>0.06 (-3.47%)</td><td>0.06 (-9.15%)</td><td>0.04 (-18.71%)</td><td>0.01 <b>(+39.97%)</b></td><td>244.80 <b>(+23.02%)</b></td><td>169.94 (+6.37%)</td><td>157.90 (+10.03%)</td><td>135.40 (-2.24%)</td><td>44.71 <b>(+70.32%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>159.76 (n/a)</td><td>143.50 (n/a)</td><td>138.50 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (+11.19%)</td><td>0.05 (+4.67%)</td><td>0.05 (+8.93%)</td><td>0.04 (-2.74%)</td><td>0.01 (+19.97%)</td><td>215.10 (+2.82%)</td><td>170.04 (-3.58%)</td><td>165.40 (-8.21%)</td><td>126.90 (-10.06%)</td><td>36.26 (+12.16%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>176.36 (n/a)</td><td>180.20 (n/a)</td><td>141.10 (n/a)</td><td>32.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.08 <b>(+29.83%)</b></td><td>0.07 (+14.58%)</td><td>0.07 (+12.36%)</td><td>0.05 (-9.89%)</td><td>0.01 <b>(+133.18%)</b></td><td>218.60 (+10.96%)</td><td>158.32 (-9.94%)</td><td>150.80 (-11.03%)</td><td>121.90 <b>(-22.99%)</b></td><td>37.63 <b>(+101.35%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>175.80 (n/a)</td><td>169.50 (n/a)</td><td>158.30 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+23.81%)</b></td><td>0.06 (+9.54%)</td><td>0.05 (+12.34%)</td><td>0.05 (+0.12%)</td><td>0.01 <b>(+129.65%)</b></td><td>172.70 (-0.12%)</td><td>150.70 (-7.14%)</td><td>150.70 (-10.99%)</td><td>114.80 (-19.21%)</td><td>23.79 <b>(+86.90%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.90 (n/a)</td><td>162.28 (n/a)</td><td>169.30 (n/a)</td><td>142.10 (n/a)</td><td>12.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (-13.25%)</td><td>0.06 (+1.51%)</td><td>0.06 (+7.49%)</td><td>0.05 (+19.81%)</td><td>0.01 <b>(-48.69%)</b></td><td>202.60 (-16.52%)</td><td>163.12 (-5.87%)</td><td>152.70 (-6.95%)</td><td>139.10 (+15.34%)</td><td>24.61 <b>(-49.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>173.30 (n/a)</td><td>164.10 (n/a)</td><td>120.60 (n/a)</td><td>49.08 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-11.70%)</td><td>0.05 (+1.32%)</td><td>0.05 (-8.55%)</td><td>0.05 <b>(+23.32%)</b></td><td>0.00 <b>(-55.46%)</b></td><td>175.90 (-18.90%)</td><td>163.26 (-3.94%)</td><td>171.80 (+9.36%)</td><td>144.90 (+13.29%)</td><td>14.07 <b>(-59.46%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>169.96 (n/a)</td><td>157.10 (n/a)</td><td>127.90 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 (-6.73%)</td><td>0.06 (-0.80%)</td><td>0.06 (+7.12%)</td><td>0.05 (-2.49%)</td><td>0.01 (-18.65%)</td><td>202.30 (+2.59%)</td><td>164.92 (-0.04%)</td><td>162.70 (-6.66%)</td><td>126.80 (+7.28%)</td><td>27.64 (-9.63%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>164.98 (n/a)</td><td>174.30 (n/a)</td><td>118.20 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (-17.19%)</td><td>0.05 (+7.10%)</td><td>0.05 <b>(+26.40%)</b></td><td>0.04 <b>(+39.92%)</b></td><td>0.01 <b>(-59.02%)</b></td><td>204.80 <b>(-28.54%)</b></td><td>180.38 (-12.30%)</td><td>174.80 <b>(-20.87%)</b></td><td>158.10 <b>(+20.78%)</b></td><td>22.01 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.60 (n/a)</td><td>205.68 (n/a)</td><td>220.90 (n/a)</td><td>130.90 (n/a)</td><td>60.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 (-8.38%)</td><td>0.05 (+14.44%)</td><td>0.05 (+7.59%)</td><td>0.04 <b>(+65.25%)</b></td><td>0.01 <b>(-45.89%)</b></td><td>220.60 <b>(-39.48%)</b></td><td>182.00 <b>(-21.98%)</b></td><td>177.80 (-7.06%)</td><td>139.30 (+9.17%)</td><td>34.59 <b>(-64.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>364.50 (n/a)</td><td>233.28 (n/a)</td><td>191.30 (n/a)</td><td>127.60 (n/a)</td><td>98.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.06 <b>(+23.41%)</b></td><td>0.05 (+5.95%)</td><td>0.06 <b>(+26.20%)</b></td><td>0.02 <b>(-45.94%)</b></td><td>0.02 <b>(+932.74%)</b></td><td>341.80 <b>(+84.96%)</b></td><td>189.18 (+6.75%)</td><td>139.70 <b>(-20.80%)</b></td><td>137.30 (-18.95%)</td><td>88.21 <b>(+1418.58%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.80 (n/a)</td><td>177.22 (n/a)</td><td>176.40 (n/a)</td><td>169.40 (n/a)</td><td>5.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.07 <b>(+28.36%)</b></td><td>0.05 (+14.00%)</td><td>0.05 (+6.18%)</td><td>0.03 (-12.56%)</td><td>0.01 <b>(+106.26%)</b></td><td>261.80 (+14.37%)</td><td>175.66 (-7.78%)</td><td>175.40 (-5.80%)</td><td>118.00 <b>(-22.06%)</b></td><td>53.81 <b>(+88.24%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>190.48 (n/a)</td><td>186.20 (n/a)</td><td>151.40 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.05 (+14.75%)</td><td>0.04 <b>(+31.85%)</b></td><td>0.04 <b>(+32.86%)</b></td><td>0.04 <b>(+81.94%)</b></td><td>0.00 <b>(-54.47%)</b></td><td>204.90 <b>(-45.05%)</b></td><td>185.78 <b>(-28.28%)</b></td><td>184.20 <b>(-24.72%)</b></td><td>161.60 (-12.84%)</td><td>16.36 <b>(-78.25%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.90 (n/a)</td><td>259.04 (n/a)</td><td>244.70 (n/a)</td><td>185.40 (n/a)</td><td>75.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-3.34%)</td><td>0.11 (-2.59%)</td><td>0.10 (-0.77%)</td><td>0.09 (+16.53%)</td><td>0.02 <b>(-25.98%)</b></td><td>189.40 (-14.22%)</td><td>157.56 (+0.42%)</td><td>157.70 (+0.77%)</td><td>127.90 (+3.40%)</td><td>25.89 <b>(-34.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.80 (n/a)</td><td>156.90 (n/a)</td><td>156.50 (n/a)</td><td>123.70 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (+0.69%)</td><td>0.15 (+2.15%)</td><td>0.15 (+8.70%)</td><td>0.14 (+10.97%)</td><td>0.01 <b>(-37.87%)</b></td><td>177.00 (-9.88%)</td><td>164.26 (-3.19%)</td><td>165.60 (-8.05%)</td><td>142.20 (-0.70%)</td><td>13.91 <b>(-42.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.40 (n/a)</td><td>169.68 (n/a)</td><td>180.10 (n/a)</td><td>143.20 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+1.68%)</td><td>0.11 (+2.29%)</td><td>0.10 (-7.54%)</td><td>0.09 (+10.87%)</td><td>0.02 (+3.53%)</td><td>192.10 (-9.81%)</td><td>160.70 (-2.42%)</td><td>168.50 (+8.15%)</td><td>125.00 (-1.65%)</td><td>31.32 (-9.34%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.00 (n/a)</td><td>164.68 (n/a)</td><td>155.80 (n/a)</td><td>127.10 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-16.58%)</td><td>0.12 (-13.01%)</td><td>0.12 (-15.83%)</td><td>0.09 (-15.38%)</td><td>0.02 <b>(-27.21%)</b></td><td>231.50 (+18.17%)</td><td>175.88 (+14.16%)</td><td>165.20 (+18.76%)</td><td>153.10 (+19.89%)</td><td>32.25 (+5.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>195.90 (n/a)</td><td>154.06 (n/a)</td><td>139.10 (n/a)</td><td>127.70 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+19.34%)</td><td>0.11 (+1.70%)</td><td>0.11 (+3.10%)</td><td>0.05 <b>(-43.63%)</b></td><td>0.03 <b>(+240.30%)</b></td><td>321.50 <b>(+77.43%)</b></td><td>176.38 (+10.50%)</td><td>149.40 (-3.05%)</td><td>120.80 (-16.23%)</td><td>82.99 <b>(+427.63%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>159.62 (n/a)</td><td>154.10 (n/a)</td><td>144.20 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (-1.69%)</td><td>0.14 (+15.63%)</td><td>0.15 <b>(+29.29%)</b></td><td>0.11 (+11.22%)</td><td>0.02 <b>(-22.83%)</b></td><td>189.80 (-10.09%)</td><td>149.76 (-14.56%)</td><td>140.70 <b>(-22.65%)</b></td><td>131.20 (+1.71%)</td><td>23.19 <b>(-26.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.10 (n/a)</td><td>175.28 (n/a)</td><td>181.90 (n/a)</td><td>129.00 (n/a)</td><td>31.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+4.53%)</td><td>0.11 (+4.38%)</td><td>0.10 (-4.32%)</td><td>0.09 (+13.84%)</td><td>0.02 (-1.43%)</td><td>183.00 (-12.19%)</td><td>152.66 (-4.77%)</td><td>163.60 (+4.54%)</td><td>117.10 (-4.33%)</td><td>26.10 (-18.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>160.30 (n/a)</td><td>156.50 (n/a)</td><td>122.40 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+0.45%)</td><td>0.12 (+15.78%)</td><td>0.11 (+11.18%)</td><td>0.10 <b>(+25.58%)</b></td><td>0.02 <b>(-33.16%)</b></td><td>190.30 <b>(-20.34%)</b></td><td>161.84 (-16.06%)</td><td>166.40 (-10.05%)</td><td>131.60 (-0.45%)</td><td>22.35 <b>(-47.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>238.90 (n/a)</td><td>192.80 (n/a)</td><td>185.00 (n/a)</td><td>132.20 (n/a)</td><td>42.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+19.53%)</td><td>0.11 (+7.51%)</td><td>0.11 (+12.29%)</td><td>0.08 (-7.03%)</td><td>0.03 <b>(+119.17%)</b></td><td>216.50 (+7.55%)</td><td>164.88 (-2.37%)</td><td>144.70 (-10.95%)</td><td>117.90 (-16.32%)</td><td>46.82 <b>(+106.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>168.88 (n/a)</td><td>162.50 (n/a)</td><td>140.90 (n/a)</td><td>22.71 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 (+0.87%)</td><td>0.10 (+5.24%)</td><td>0.10 (+8.47%)</td><td>0.08 (+10.93%)</td><td>0.01 (-8.43%)</td><td>217.00 (-9.85%)</td><td>185.90 (-5.46%)</td><td>178.70 (-7.84%)</td><td>157.60 (-0.82%)</td><td>27.00 (-17.08%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>240.70 (n/a)</td><td>196.64 (n/a)</td><td>193.90 (n/a)</td><td>158.90 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 <b>(+38.43%)</b></td><td>0.09 (+8.40%)</td><td>0.08 (+4.41%)</td><td>0.05 <b>(-23.09%)</b></td><td>0.03 <b>(+146.18%)</b></td><td>338.00 <b>(+30.05%)</b></td><td>209.96 (-0.41%)</td><td>197.30 (-4.22%)</td><td>131.10 <b>(-27.77%)</b></td><td>77.31 <b>(+142.17%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>259.90 (n/a)</td><td>210.82 (n/a)</td><td>206.00 (n/a)</td><td>181.50 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(+41.38%)</b></td><td>0.10 (+17.26%)</td><td>0.09 (+9.36%)</td><td>0.07 (-7.88%)</td><td>0.02 <b>(+378.52%)</b></td><td>244.80 (+8.56%)</td><td>188.02 (-10.97%)</td><td>193.60 (-8.55%)</td><td>137.30 <b>(-29.26%)</b></td><td>44.24 <b>(+261.13%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>211.18 (n/a)</td><td>211.70 (n/a)</td><td>194.10 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.11 (+7.32%)</td><td>0.09 <b>(+22.31%)</b></td><td>0.09 <b>(+28.79%)</b></td><td>0.08 <b>(+32.07%)</b></td><td>0.01 <b>(-37.48%)</b></td><td>206.60 <b>(-24.27%)</b></td><td>182.12 <b>(-20.37%)</b></td><td>187.80 <b>(-22.36%)</b></td><td>152.60 (-6.78%)</td><td>19.86 <b>(-56.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>272.80 (n/a)</td><td>228.72 (n/a)</td><td>241.90 (n/a)</td><td>163.70 (n/a)</td><td>46.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(+41.39%)</b></td><td>0.10 <b>(+46.21%)</b></td><td>0.10 <b>(+33.66%)</b></td><td>0.07 <b>(+34.57%)</b></td><td>0.02 <b>(+33.13%)</b></td><td>241.20 <b>(-25.69%)</b></td><td>176.14 <b>(-31.90%)</b></td><td>171.40 <b>(-25.19%)</b></td><td>136.30 <b>(-29.27%)</b></td><td>40.32 <b>(-32.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>324.60 (n/a)</td><td>258.64 (n/a)</td><td>229.10 (n/a)</td><td>192.70 (n/a)</td><td>59.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (+3.86%)</td><td>0.08 (+18.48%)</td><td>0.09 (+17.09%)</td><td>0.07 <b>(+34.07%)</b></td><td>0.01 <b>(-34.92%)</b></td><td>232.10 <b>(-25.42%)</b></td><td>202.88 (-18.17%)</td><td>192.70 (-14.58%)</td><td>169.50 (-3.75%)</td><td>26.38 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>311.20 (n/a)</td><td>247.92 (n/a)</td><td>225.60 (n/a)</td><td>176.10 (n/a)</td><td>57.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (+7.76%)</td><td>0.19 (-1.88%)</td><td>0.18 (+5.10%)</td><td>0.15 (-7.50%)</td><td>0.04 <b>(+28.27%)</b></td><td>218.50 (+8.11%)</td><td>182.48 (+3.27%)</td><td>178.80 (-4.84%)</td><td>131.00 (-7.22%)</td><td>35.55 <b>(+28.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>202.10 (n/a)</td><td>176.70 (n/a)</td><td>187.90 (n/a)</td><td>141.20 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (-5.62%)</td><td>0.20 (-1.21%)</td><td>0.21 (+4.34%)</td><td>0.18 (+3.35%)</td><td>0.02 <b>(-26.78%)</b></td><td>182.60 (-3.23%)</td><td>164.26 (+0.61%)</td><td>158.90 (-4.16%)</td><td>143.30 (+5.99%)</td><td>16.24 <b>(-23.80%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>188.70 (n/a)</td><td>163.26 (n/a)</td><td>165.80 (n/a)</td><td>135.20 (n/a)</td><td>21.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 <b>(+24.86%)</b></td><td>0.27 <b>(+31.30%)</b></td><td>0.27 <b>(+28.53%)</b></td><td>0.23 <b>(+48.96%)</b></td><td>0.03 (-14.28%)</td><td>177.60 <b>(-32.85%)</b></td><td>153.62 <b>(-24.89%)</b></td><td>151.80 <b>(-22.19%)</b></td><td>135.40 (-19.88%)</td><td>16.59 <b>(-54.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>264.50 (n/a)</td><td>204.54 (n/a)</td><td>195.10 (n/a)</td><td>169.00 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (-2.73%)</td><td>0.21 (+4.72%)</td><td>0.24 <b>(+30.12%)</b></td><td>0.16 (-12.91%)</td><td>0.04 <b>(+29.18%)</b></td><td>211.30 (+14.84%)</td><td>160.70 (-2.98%)</td><td>138.40 <b>(-23.15%)</b></td><td>134.10 (+2.84%)</td><td>34.45 <b>(+48.51%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.00 (n/a)</td><td>165.64 (n/a)</td><td>180.10 (n/a)</td><td>130.40 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.33 <b>(+41.19%)</b></td><td>0.27 <b>(+39.50%)</b></td><td>0.27 <b>(+38.56%)</b></td><td>0.22 <b>(+41.23%)</b></td><td>0.04 <b>(+47.95%)</b></td><td>183.80 <b>(-29.20%)</b></td><td>155.98 <b>(-28.17%)</b></td><td>152.00 <b>(-27.86%)</b></td><td>124.00 <b>(-29.18%)</b></td><td>25.02 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>259.60 (n/a)</td><td>217.16 (n/a)</td><td>210.70 (n/a)</td><td>175.10 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (-8.43%)</td><td>0.20 (+2.02%)</td><td>0.20 (+8.21%)</td><td>0.13 (-12.47%)</td><td>0.05 (-13.13%)</td><td>244.70 (+14.24%)</td><td>173.40 (-2.00%)</td><td>166.30 (-7.56%)</td><td>126.30 (+9.26%)</td><td>43.77 (+15.89%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>214.20 (n/a)</td><td>176.94 (n/a)</td><td>179.90 (n/a)</td><td>115.60 (n/a)</td><td>37.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 <b>(+33.43%)</b></td><td>0.21 <b>(+24.88%)</b></td><td>0.21 <b>(+33.31%)</b></td><td>0.14 (+9.65%)</td><td>0.05 <b>(+44.96%)</b></td><td>267.00 (-8.81%)</td><td>185.28 (-18.56%)</td><td>172.70 <b>(-24.98%)</b></td><td>127.40 <b>(-25.06%)</b></td><td>50.91 (+2.27%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>292.80 (n/a)</td><td>227.50 (n/a)</td><td>230.20 (n/a)</td><td>170.00 (n/a)</td><td>49.78 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (+3.38%)</td><td>0.19 (+2.46%)</td><td>0.19 (-2.95%)</td><td>0.16 (+6.26%)</td><td>0.02 (-3.77%)</td><td>200.10 (-5.88%)</td><td>173.72 (-2.60%)</td><td>173.70 (+3.02%)</td><td>150.50 (-3.28%)</td><td>20.01 (-13.18%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.60 (n/a)</td><td>178.36 (n/a)</td><td>168.60 (n/a)</td><td>155.60 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (+14.00%)</td><td>0.23 (+17.58%)</td><td>0.21 (+6.68%)</td><td>0.21 <b>(+28.57%)</b></td><td>0.03 (-0.44%)</td><td>176.20 <b>(-22.24%)</b></td><td>159.80 (-15.52%)</td><td>174.00 (-6.25%)</td><td>135.20 (-12.26%)</td><td>20.95 <b>(-32.11%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>226.60 (n/a)</td><td>189.16 (n/a)</td><td>185.60 (n/a)</td><td>154.10 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 (+4.94%)</td><td>0.17 (-0.43%)</td><td>0.16 (-8.86%)</td><td>0.16 (+3.83%)</td><td>0.02 <b>(+35.24%)</b></td><td>206.10 (-3.69%)</td><td>189.54 (+0.84%)</td><td>202.20 (+9.71%)</td><td>162.50 (-4.69%)</td><td>20.59 <b>(+24.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>187.96 (n/a)</td><td>184.30 (n/a)</td><td>170.50 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (+1.50%)</td><td>0.19 (+14.78%)</td><td>0.19 (+19.76%)</td><td>0.11 (+2.66%)</td><td>0.05 (-8.28%)</td><td>323.50 (-2.59%)</td><td>198.08 (-14.14%)</td><td>180.20 (-16.50%)</td><td>138.00 (-1.50%)</td><td>72.71 (-7.75%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>332.10 (n/a)</td><td>230.70 (n/a)</td><td>215.80 (n/a)</td><td>140.10 (n/a)</td><td>78.82 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 (-16.00%)</td><td>0.15 (-13.88%)</td><td>0.14 (-16.53%)</td><td>0.12 (-18.35%)</td><td>0.04 (+3.04%)</td><td>276.80 <b>(+22.42%)</b></td><td>223.56 (+17.96%)</td><td>231.00 (+19.81%)</td><td>165.10 (+19.03%)</td><td>49.74 <b>(+56.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>226.10 (n/a)</td><td>189.52 (n/a)</td><td>192.80 (n/a)</td><td>138.70 (n/a)</td><td>31.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (-8.21%)</td><td>0.20 (+10.92%)</td><td>0.19 <b>(+21.42%)</b></td><td>0.16 (+2.01%)</td><td>0.03 <b>(-29.07%)</b></td><td>221.10 (-1.95%)</td><td>181.54 (-11.14%)</td><td>180.60 (-17.65%)</td><td>154.00 (+8.91%)</td><td>27.13 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.50 (n/a)</td><td>204.30 (n/a)</td><td>219.30 (n/a)</td><td>141.40 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 (+9.54%)</td><td>0.14 (-10.28%)</td><td>0.14 (-15.57%)</td><td>0.10 <b>(-24.12%)</b></td><td>0.03 <b>(+119.73%)</b></td><td>319.80 <b>(+31.77%)</b></td><td>245.70 (+15.93%)</td><td>241.80 (+18.47%)</td><td>171.20 (-8.69%)</td><td>58.42 <b>(+162.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>242.70 (n/a)</td><td>211.94 (n/a)</td><td>204.10 (n/a)</td><td>187.50 (n/a)</td><td>22.23 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 <b>(+35.53%)</b></td><td>0.13 (+7.97%)</td><td>0.11 (-9.00%)</td><td>0.11 (+13.37%)</td><td>0.03 <b>(+105.29%)</b></td><td>191.10 (-11.77%)</td><td>165.36 (-4.95%)</td><td>183.20 (+9.90%)</td><td>113.60 <b>(-26.19%)</b></td><td>33.93 <b>(+34.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>216.60 (n/a)</td><td>173.98 (n/a)</td><td>166.70 (n/a)</td><td>153.90 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 <b>(+20.27%)</b></td><td>0.15 <b>(+22.95%)</b></td><td>0.14 <b>(+22.23%)</b></td><td>0.11 (+5.56%)</td><td>0.03 <b>(+41.00%)</b></td><td>183.80 (-5.26%)</td><td>144.62 (-17.78%)</td><td>150.40 (-18.22%)</td><td>110.70 (-16.83%)</td><td>27.67 (+13.15%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.00 (n/a)</td><td>175.90 (n/a)</td><td>183.90 (n/a)</td><td>133.10 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+2.64%)</td><td>0.11 (-4.10%)</td><td>0.11 (-0.05%)</td><td>0.07 <b>(-31.33%)</b></td><td>0.02 <b>(+123.89%)</b></td><td>281.30 <b>(+45.60%)</b></td><td>195.98 (+8.38%)</td><td>181.50 (+0.06%)</td><td>151.40 (-2.57%)</td><td>50.77 <b>(+229.76%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>180.82 (n/a)</td><td>181.40 (n/a)</td><td>155.40 (n/a)</td><td>15.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 <b>(+44.56%)</b></td><td>0.13 <b>(+25.67%)</b></td><td>0.13 (+15.07%)</td><td>0.11 <b>(+22.46%)</b></td><td>0.02 <b>(+103.98%)</b></td><td>182.20 (-18.33%)</td><td>157.22 (-19.64%)</td><td>162.90 (-13.12%)</td><td>123.90 <b>(-30.78%)</b></td><td>22.03 (+13.82%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>195.64 (n/a)</td><td>187.50 (n/a)</td><td>179.00 (n/a)</td><td>19.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-18.10%)</td><td>0.12 (+0.93%)</td><td>0.13 (-1.69%)</td><td>0.11 <b>(+59.16%)</b></td><td>0.01 <b>(-69.00%)</b></td><td>194.30 <b>(-37.16%)</b></td><td>169.28 (-8.74%)</td><td>163.70 (+1.74%)</td><td>155.10 <b>(+22.03%)</b></td><td>15.80 <b>(-77.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>309.20 (n/a)</td><td>185.50 (n/a)</td><td>160.90 (n/a)</td><td>127.10 (n/a)</td><td>71.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (+3.02%)</td><td>0.12 (+3.38%)</td><td>0.11 (-0.53%)</td><td>0.11 (+3.59%)</td><td>0.01 (+9.68%)</td><td>184.10 (-3.46%)</td><td>172.02 (-3.21%)</td><td>179.60 (+0.50%)</td><td>152.50 (-2.93%)</td><td>14.35 (+2.76%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>177.72 (n/a)</td><td>178.70 (n/a)</td><td>157.10 (n/a)</td><td>13.97 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.18 <b>(+38.42%)</b></td><td>0.12 (+4.99%)</td><td>0.11 (-11.48%)</td><td>0.08 (-14.86%)</td><td>0.04 <b>(+135.21%)</b></td><td>257.20 (+17.44%)</td><td>181.12 (+1.11%)</td><td>183.60 (+12.98%)</td><td>112.20 <b>(-27.75%)</b></td><td>54.50 <b>(+96.91%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>219.00 (n/a)</td><td>179.14 (n/a)</td><td>162.50 (n/a)</td><td>155.30 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+6.72%)</td><td>0.12 (+14.29%)</td><td>0.11 (+9.63%)</td><td>0.10 <b>(+88.50%)</b></td><td>0.01 <b>(-50.85%)</b></td><td>198.70 <b>(-46.96%)</b></td><td>179.60 (-19.45%)</td><td>183.90 (-8.78%)</td><td>146.80 (-6.32%)</td><td>20.47 <b>(-76.73%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>374.60 (n/a)</td><td>222.98 (n/a)</td><td>201.60 (n/a)</td><td>156.70 (n/a)</td><td>87.98 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 <b>(+27.70%)</b></td><td>0.16 (+10.79%)</td><td>0.16 (+6.02%)</td><td>0.10 (-19.91%)</td><td>0.04 <b>(+156.44%)</b></td><td>246.60 <b>(+24.86%)</b></td><td>165.54 (-4.98%)</td><td>158.00 (-5.67%)</td><td>117.40 <b>(-21.68%)</b></td><td>49.16 <b>(+156.57%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.50 (n/a)</td><td>174.22 (n/a)</td><td>167.50 (n/a)</td><td>149.90 (n/a)</td><td>19.16 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (+0.76%)</td><td>0.14 (-1.21%)</td><td>0.15 (-3.66%)</td><td>0.09 <b>(-21.85%)</b></td><td>0.03 <b>(+53.98%)</b></td><td>266.00 <b>(+27.95%)</b></td><td>179.70 (+4.29%)</td><td>163.20 (+3.75%)</td><td>151.70 (-0.78%)</td><td>48.66 <b>(+101.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.90 (n/a)</td><td>172.30 (n/a)</td><td>157.30 (n/a)</td><td>152.90 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.16 (+8.37%)</td><td>0.15 (+14.36%)</td><td>0.15 (+11.62%)</td><td>0.14 <b>(+31.11%)</b></td><td>0.01 <b>(-51.48%)</b></td><td>179.80 <b>(-23.75%)</b></td><td>167.26 (-14.22%)</td><td>166.30 (-10.45%)</td><td>150.40 (-7.73%)</td><td>11.34 <b>(-65.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>235.80 (n/a)</td><td>194.98 (n/a)</td><td>185.70 (n/a)</td><td>163.00 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.17 (+1.18%)</td><td>0.15 (-0.10%)</td><td>0.15 (+1.62%)</td><td>0.14 (+3.61%)</td><td>0.01 (-11.28%)</td><td>181.70 (-3.51%)</td><td>164.86 (-0.10%)</td><td>161.80 (-1.58%)</td><td>147.20 (-1.21%)</td><td>13.72 (-14.26%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>165.02 (n/a)</td><td>164.40 (n/a)</td><td>149.00 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.19 <b>(+20.48%)</b></td><td>0.16 (+14.42%)</td><td>0.19 <b>(+34.90%)</b></td><td>0.11 (-11.44%)</td><td>0.04 <b>(+197.76%)</b></td><td>218.50 (+12.92%)</td><td>160.22 (-8.19%)</td><td>129.30 <b>(-25.90%)</b></td><td>127.40 (-17.00%)</td><td>44.41 <b>(+169.62%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>174.52 (n/a)</td><td>174.50 (n/a)</td><td>153.50 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.20 <b>(+29.91%)</b></td><td>0.16 <b>(+28.44%)</b></td><td>0.16 <b>(+22.49%)</b></td><td>0.12 (+9.62%)</td><td>0.03 <b>(+99.18%)</b></td><td>199.00 (-8.80%)</td><td>154.98 <b>(-20.71%)</b></td><td>155.50 (-18.33%)</td><td>125.80 <b>(-23.06%)</b></td><td>30.35 <b>(+33.97%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>195.46 (n/a)</td><td>190.40 (n/a)</td><td>163.50 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 <b>(+28.62%)</b></td><td>0.14 (+17.38%)</td><td>0.13 (+5.61%)</td><td>0.12 <b>(+28.70%)</b></td><td>0.04 <b>(+47.68%)</b></td><td>210.40 <b>(-22.30%)</b></td><td>180.28 (-13.87%)</td><td>196.30 (-5.31%)</td><td>117.50 <b>(-22.24%)</b></td><td>37.52 (-11.64%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>270.80 (n/a)</td><td>209.30 (n/a)</td><td>207.30 (n/a)</td><td>151.10 (n/a)</td><td>42.46 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.12 <b>(-32.53%)</b></td><td>0.12 (-18.39%)</td><td>0.12 (-12.32%)</td><td>0.11 (-5.48%)</td><td>0.01 <b>(-75.61%)</b></td><td>223.70 (+5.82%)</td><td>209.14 (+19.96%)</td><td>204.90 (+14.02%)</td><td>197.50 <b>(+48.16%)</b></td><td>11.26 <b>(-60.92%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.40 (n/a)</td><td>174.34 (n/a)</td><td>179.70 (n/a)</td><td>133.30 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 (-10.70%)</td><td>0.12 (+1.80%)</td><td>0.12 <b>(+23.37%)</b></td><td>0.10 (+6.05%)</td><td>0.01 <b>(-47.22%)</b></td><td>179.00 (-5.74%)</td><td>159.82 (-3.64%)</td><td>148.70 (-18.92%)</td><td>147.40 (+12.01%)</td><td>16.27 <b>(-44.68%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>189.90 (n/a)</td><td>165.86 (n/a)</td><td>183.40 (n/a)</td><td>131.60 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+0.39%)</td><td>0.12 (+9.54%)</td><td>0.12 (+8.30%)</td><td>0.10 <b>(+27.26%)</b></td><td>0.01 <b>(-31.40%)</b></td><td>185.50 <b>(-21.43%)</b></td><td>160.58 (-10.52%)</td><td>155.70 (-7.65%)</td><td>136.40 (-0.37%)</td><td>19.61 <b>(-46.72%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>236.10 (n/a)</td><td>179.46 (n/a)</td><td>168.60 (n/a)</td><td>136.90 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (-2.44%)</td><td>0.11 (+6.68%)</td><td>0.11 (+1.89%)</td><td>0.08 <b>(+41.45%)</b></td><td>0.02 <b>(-28.83%)</b></td><td>234.50 <b>(-29.30%)</b></td><td>172.12 (-12.03%)</td><td>166.90 (-1.82%)</td><td>130.40 (+2.52%)</td><td>38.91 <b>(-50.83%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>331.70 (n/a)</td><td>195.66 (n/a)</td><td>170.00 (n/a)</td><td>127.20 (n/a)</td><td>79.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+11.29%)</td><td>0.11 (+7.27%)</td><td>0.11 (+8.47%)</td><td>0.09 (+9.58%)</td><td>0.02 <b>(+20.51%)</b></td><td>195.30 (-8.74%)</td><td>165.36 (-6.49%)</td><td>162.10 (-7.79%)</td><td>134.90 (-10.19%)</td><td>25.00 (-0.00%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>176.84 (n/a)</td><td>175.80 (n/a)</td><td>150.20 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 (+4.35%)</td><td>0.12 (+9.36%)</td><td>0.12 (+10.49%)</td><td>0.11 (+17.84%)</td><td>0.01 <b>(-25.69%)</b></td><td>162.30 (-15.16%)</td><td>153.42 (-9.47%)</td><td>159.50 (-9.53%)</td><td>128.10 (-4.19%)</td><td>14.27 <b>(-40.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>191.30 (n/a)</td><td>169.46 (n/a)</td><td>176.30 (n/a)</td><td>133.70 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.15 (+1.67%)</td><td>0.13 (+10.33%)</td><td>0.14 (+9.60%)</td><td>0.08 <b>(+33.20%)</b></td><td>0.03 (-17.24%)</td><td>221.50 <b>(-24.92%)</b></td><td>153.46 (-13.64%)</td><td>133.20 (-8.77%)</td><td>120.70 (-1.63%)</td><td>42.12 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>295.00 (n/a)</td><td>177.70 (n/a)</td><td>146.00 (n/a)</td><td>122.70 (n/a)</td><td>70.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.10 (-15.17%)</td><td>0.09 (-11.47%)</td><td>0.09 <b>(-20.27%)</b></td><td>0.07 (-2.00%)</td><td>0.01 <b>(-41.05%)</b></td><td>248.30 (+2.06%)</td><td>211.06 (+11.22%)</td><td>212.30 <b>(+25.47%)</b></td><td>185.70 (+17.90%)</td><td>25.40 <b>(-29.99%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>243.30 (n/a)</td><td>189.76 (n/a)</td><td>169.20 (n/a)</td><td>157.50 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.14 <b>(+27.29%)</b></td><td>0.11 <b>(+32.33%)</b></td><td>0.10 (+19.70%)</td><td>0.09 <b>(+77.43%)</b></td><td>0.02 (-0.10%)</td><td>207.40 <b>(-43.66%)</b></td><td>171.82 <b>(-27.43%)</b></td><td>187.20 (-16.47%)</td><td>127.40 <b>(-21.45%)</b></td><td>32.40 <b>(-58.37%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>368.10 (n/a)</td><td>236.78 (n/a)</td><td>224.10 (n/a)</td><td>162.20 (n/a)</td><td>77.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 (+9.18%)</td><td>0.59 (+2.95%)</td><td>0.59 (-3.24%)</td><td>0.38 (-7.35%)</td><td>0.15 <b>(+32.89%)</b></td><td>256.30 (+7.92%)</td><td>175.92 (-0.59%)</td><td>165.60 (+3.37%)</td><td>134.70 (-8.43%)</td><td>50.09 <b>(+30.39%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.67 (n/a)</td><td>0.57 (n/a)</td><td>0.61 (n/a)</td><td>0.41 (n/a)</td><td>0.11 (n/a)</td><td>237.50 (n/a)</td><td>176.96 (n/a)</td><td>160.20 (n/a)</td><td>147.10 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.74 (-6.40%)</td><td>0.58 (-7.91%)</td><td>0.54 (-18.15%)</td><td>0.49 <b>(+23.58%)</b></td><td>0.10 <b>(-34.58%)</b></td><td>199.80 (-19.11%)</td><td>172.96 (+4.81%)</td><td>182.60 <b>(+22.14%)</b></td><td>133.20 (+6.90%)</td><td>25.36 <b>(-47.20%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.66 (n/a)</td><td>0.40 (n/a)</td><td>0.15 (n/a)</td><td>247.00 (n/a)</td><td>165.02 (n/a)</td><td>149.50 (n/a)</td><td>124.60 (n/a)</td><td>48.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.83 <b>(+30.38%)</b></td><td>0.66 <b>(+26.90%)</b></td><td>0.67 <b>(+28.82%)</b></td><td>0.56 <b>(+44.88%)</b></td><td>0.11 (+10.75%)</td><td>176.90 <b>(-30.95%)</b></td><td>151.00 <b>(-22.02%)</b></td><td>145.70 <b>(-22.38%)</b></td><td>118.60 <b>(-23.29%)</b></td><td>23.22 <b>(-41.43%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.64 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.10 (n/a)</td><td>256.20 (n/a)</td><td>193.64 (n/a)</td><td>187.70 (n/a)</td><td>154.60 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 <b>(+35.20%)</b></td><td>0.56 (+13.97%)</td><td>0.54 (+11.91%)</td><td>0.45 (+2.15%)</td><td>0.11 <b>(+158.39%)</b></td><td>217.90 (-2.11%)</td><td>179.22 (-10.35%)</td><td>181.30 (-10.60%)</td><td>135.30 <b>(-26.03%)</b></td><td>31.92 <b>(+88.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.44 (n/a)</td><td>0.04 (n/a)</td><td>222.60 (n/a)</td><td>199.90 (n/a)</td><td>202.80 (n/a)</td><td>182.90 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.49 (-2.52%)</td><td>0.43 (+1.44%)</td><td>0.43 (-0.81%)</td><td>0.40 <b>(+30.27%)</b></td><td>0.03 <b>(-53.10%)</b></td><td>185.60 <b>(-23.24%)</b></td><td>171.46 (-3.78%)</td><td>171.90 (+0.82%)</td><td>151.70 (+2.57%)</td><td>13.21 <b>(-64.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>241.80 (n/a)</td><td>178.20 (n/a)</td><td>170.50 (n/a)</td><td>147.90 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.55 (+16.57%)</td><td>0.44 (+8.72%)</td><td>0.46 <b>(+21.21%)</b></td><td>0.32 (-8.20%)</td><td>0.10 <b>(+83.85%)</b></td><td>229.90 (+8.91%)</td><td>176.18 (-5.42%)</td><td>160.60 (-17.51%)</td><td>133.80 (-14.23%)</td><td>40.67 <b>(+75.31%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.05 (n/a)</td><td>211.10 (n/a)</td><td>186.28 (n/a)</td><td>194.70 (n/a)</td><td>156.00 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.58 (-0.74%)</td><td>0.44 (-8.30%)</td><td>0.45 (-10.39%)</td><td>0.32 <b>(+32.04%)</b></td><td>0.10 <b>(-30.38%)</b></td><td>227.60 <b>(-24.26%)</b></td><td>174.34 (+2.22%)</td><td>165.60 (+11.59%)</td><td>127.50 (+0.71%)</td><td>37.75 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>300.50 (n/a)</td><td>170.56 (n/a)</td><td>148.40 (n/a)</td><td>126.60 (n/a)</td><td>73.45 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.73 <b>(+47.55%)</b></td><td>0.44 (+15.33%)</td><td>0.39 (+2.64%)</td><td>0.29 (-0.09%)</td><td>0.17 <b>(+136.26%)</b></td><td>252.60 (+0.08%)</td><td>183.30 (-7.01%)</td><td>190.20 (-2.56%)</td><td>101.70 <b>(-32.20%)</b></td><td>57.66 <b>(+55.28%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>252.40 (n/a)</td><td>197.12 (n/a)</td><td>195.20 (n/a)</td><td>150.00 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (+19.98%)</td><td>0.24 (+13.42%)</td><td>0.22 (+7.26%)</td><td>0.17 (-5.64%)</td><td>0.06 <b>(+131.63%)</b></td><td>212.70 (+5.98%)</td><td>159.66 (-8.83%)</td><td>165.70 (-6.75%)</td><td>123.10 (-16.66%)</td><td>37.42 <b>(+97.44%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>200.70 (n/a)</td><td>175.12 (n/a)</td><td>177.70 (n/a)</td><td>147.70 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 <b>(+26.25%)</b></td><td>0.22 <b>(+34.43%)</b></td><td>0.23 <b>(+34.13%)</b></td><td>0.18 <b>(+78.67%)</b></td><td>0.04 (-11.67%)</td><td>201.00 <b>(-44.03%)</b></td><td>167.54 <b>(-28.58%)</b></td><td>157.30 <b>(-25.45%)</b></td><td>134.20 <b>(-20.78%)</b></td><td>27.42 <b>(-62.36%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>359.10 (n/a)</td><td>234.58 (n/a)</td><td>211.00 (n/a)</td><td>169.40 (n/a)</td><td>72.83 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (-8.70%)</td><td>0.23 (-3.31%)</td><td>0.23 (-5.43%)</td><td>0.17 (-2.09%)</td><td>0.04 <b>(-20.08%)</b></td><td>221.30 (+2.12%)</td><td>165.78 (+2.11%)</td><td>157.10 (+5.72%)</td><td>133.00 (+9.47%)</td><td>35.02 (-10.86%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>216.70 (n/a)</td><td>162.36 (n/a)</td><td>148.60 (n/a)</td><td>121.50 (n/a)</td><td>39.29 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (-0.87%)</td><td>0.23 (-1.87%)</td><td>0.22 (-2.44%)</td><td>0.19 (+7.54%)</td><td>0.04 (-9.34%)</td><td>198.20 (-6.99%)</td><td>165.30 (+1.24%)</td><td>164.50 (+2.49%)</td><td>129.40 (+0.86%)</td><td>25.94 (-17.09%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>213.10 (n/a)</td><td>163.28 (n/a)</td><td>160.50 (n/a)</td><td>128.30 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 <b>(+25.22%)</b></td><td>0.22 <b>(+22.01%)</b></td><td>0.22 (+18.49%)</td><td>0.18 <b>(+72.65%)</b></td><td>0.04 (-13.09%)</td><td>210.10 <b>(-42.07%)</b></td><td>170.92 <b>(-22.33%)</b></td><td>167.90 (-15.59%)</td><td>129.10 <b>(-20.11%)</b></td><td>31.82 <b>(-61.21%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>362.70 (n/a)</td><td>220.06 (n/a)</td><td>198.90 (n/a)</td><td>161.60 (n/a)</td><td>82.03 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (+0.61%)</td><td>0.26 (+10.80%)</td><td>0.28 <b>(+25.66%)</b></td><td>0.19 (+6.01%)</td><td>0.05 (-4.84%)</td><td>194.00 (-5.69%)</td><td>144.96 (-10.21%)</td><td>132.90 <b>(-20.42%)</b></td><td>120.40 (-0.58%)</td><td>30.87 (-10.31%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>205.70 (n/a)</td><td>161.44 (n/a)</td><td>167.00 (n/a)</td><td>121.10 (n/a)</td><td>34.42 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 (+2.15%)</td><td>0.19 (-5.65%)</td><td>0.19 (-12.52%)</td><td>0.15 (-12.90%)</td><td>0.03 (+4.97%)</td><td>247.70 (+14.78%)</td><td>193.76 (+6.46%)</td><td>190.00 (+14.32%)</td><td>153.90 (-2.10%)</td><td>34.62 (+18.70%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>182.00 (n/a)</td><td>166.20 (n/a)</td><td>157.20 (n/a)</td><td>29.17 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 <b>(-22.41%)</b></td><td>0.19 (-9.15%)</td><td>0.18 (-12.10%)</td><td>0.16 (+13.73%)</td><td>0.03 <b>(-49.19%)</b></td><td>234.30 (-12.08%)</td><td>194.64 (+5.56%)</td><td>199.70 (+13.72%)</td><td>159.10 <b>(+28.83%)</b></td><td>29.15 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>266.50 (n/a)</td><td>184.38 (n/a)</td><td>175.60 (n/a)</td><td>123.50 (n/a)</td><td>51.66 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (+7.52%)</td><td>0.23 (-8.28%)</td><td>0.22 (-9.78%)</td><td>0.18 (-16.64%)</td><td>0.05 <b>(+67.11%)</b></td><td>224.70 (+19.97%)</td><td>187.80 (+11.64%)</td><td>189.90 (+10.79%)</td><td>131.60 (-7.00%)</td><td>36.75 <b>(+81.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>187.30 (n/a)</td><td>168.22 (n/a)</td><td>171.40 (n/a)</td><td>141.50 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.30 (-0.62%)</td><td>0.23 (+4.50%)</td><td>0.23 (+10.52%)</td><td>0.17 (+3.60%)</td><td>0.05 (-3.16%)</td><td>243.90 (-3.44%)</td><td>183.78 (-4.55%)</td><td>175.60 (-9.53%)</td><td>135.00 (+0.60%)</td><td>41.50 (-3.58%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>252.60 (n/a)</td><td>192.54 (n/a)</td><td>194.10 (n/a)</td><td>134.20 (n/a)</td><td>43.04 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (-19.97%)</td><td>0.25 (-16.19%)</td><td>0.25 (-18.86%)</td><td>0.22 (-9.85%)</td><td>0.02 <b>(-47.06%)</b></td><td>190.10 (+10.91%)</td><td>168.16 (+18.11%)</td><td>160.70 <b>(+23.24%)</b></td><td>153.10 <b>(+24.98%)</b></td><td>15.54 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>171.40 (n/a)</td><td>142.38 (n/a)</td><td>130.40 (n/a)</td><td>122.50 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.36 (+14.16%)</td><td>0.28 (+4.90%)</td><td>0.26 (-9.82%)</td><td>0.25 (+17.01%)</td><td>0.04 (-2.36%)</td><td>165.70 (-14.50%)</td><td>146.58 (-5.36%)</td><td>155.40 (+10.92%)</td><td>113.70 (-12.40%)</td><td>20.22 <b>(-28.30%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>193.80 (n/a)</td><td>154.88 (n/a)</td><td>140.10 (n/a)</td><td>129.80 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.34 (+5.68%)</td><td>0.27 (+9.65%)</td><td>0.26 (+18.33%)</td><td>0.20 (-2.47%)</td><td>0.06 <b>(+32.90%)</b></td><td>200.30 (+2.51%)</td><td>158.44 (-7.27%)</td><td>155.40 (-15.45%)</td><td>121.60 (-5.37%)</td><td>35.53 <b>(+28.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>195.40 (n/a)</td><td>170.86 (n/a)</td><td>183.80 (n/a)</td><td>128.50 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (-11.03%)</td><td>0.24 (-2.99%)</td><td>0.25 (-1.82%)</td><td>0.21 <b>(+28.18%)</b></td><td>0.03 <b>(-46.18%)</b></td><td>192.70 <b>(-21.98%)</b></td><td>171.22 (-0.34%)</td><td>167.10 (+1.89%)</td><td>146.80 (+12.40%)</td><td>20.75 <b>(-53.54%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>247.00 (n/a)</td><td>171.80 (n/a)</td><td>164.00 (n/a)</td><td>130.60 (n/a)</td><td>44.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.29 (+9.61%)</td><td>0.22 (+6.37%)</td><td>0.22 (+13.82%)</td><td>0.17 (+5.52%)</td><td>0.04 (-8.78%)</td><td>235.70 (-5.23%)</td><td>187.06 (-6.87%)</td><td>185.70 (-12.16%)</td><td>143.00 (-8.74%)</td><td>33.76 (-18.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>248.70 (n/a)</td><td>200.86 (n/a)</td><td>211.40 (n/a)</td><td>156.70 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.31 (-13.31%)</td><td>0.24 (-6.11%)</td><td>0.22 (-9.88%)</td><td>0.18 (+14.36%)</td><td>0.05 <b>(-31.51%)</b></td><td>229.80 (-12.56%)</td><td>178.10 (+2.39%)</td><td>187.40 (+10.95%)</td><td>130.80 (+15.34%)</td><td>37.57 <b>(-32.79%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>262.80 (n/a)</td><td>173.94 (n/a)</td><td>168.90 (n/a)</td><td>113.40 (n/a)</td><td>55.90 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (+3.73%)</td><td>0.20 (+15.15%)</td><td>0.20 (+15.62%)</td><td>0.14 <b>(+33.74%)</b></td><td>0.05 (-11.60%)</td><td>253.60 <b>(-25.24%)</b></td><td>179.74 (-16.18%)</td><td>172.10 (-13.52%)</td><td>133.00 (-3.55%)</td><td>46.29 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>339.20 (n/a)</td><td>214.44 (n/a)</td><td>199.00 (n/a)</td><td>137.90 (n/a)</td><td>74.67 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.27 (+7.49%)</td><td>0.22 (+16.25%)</td><td>0.22 <b>(+22.93%)</b></td><td>0.17 (+11.45%)</td><td>0.04 (+8.97%)</td><td>201.00 (-10.27%)</td><td>161.66 (-13.90%)</td><td>157.40 (-18.66%)</td><td>128.50 (-6.95%)</td><td>29.61 (-5.48%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>224.00 (n/a)</td><td>187.76 (n/a)</td><td>193.50 (n/a)</td><td>138.10 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (+4.29%)</td><td>0.21 (+4.15%)</td><td>0.18 (-14.64%)</td><td>0.17 (+4.37%)</td><td>0.05 (+19.61%)</td><td>208.40 (-4.23%)</td><td>172.92 (-3.28%)</td><td>192.40 (+17.17%)</td><td>131.70 (-4.15%)</td><td>37.34 (+1.88%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>217.60 (n/a)</td><td>178.78 (n/a)</td><td>164.20 (n/a)</td><td>137.40 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.23 (-12.90%)</td><td>0.20 (+9.91%)</td><td>0.19 (+5.06%)</td><td>0.18 <b>(+35.77%)</b></td><td>0.02 <b>(-58.69%)</b></td><td>191.70 <b>(-26.35%)</b></td><td>173.66 (-13.39%)</td><td>180.40 (-4.85%)</td><td>150.60 (+14.87%)</td><td>17.73 <b>(-65.35%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>260.30 (n/a)</td><td>200.50 (n/a)</td><td>189.60 (n/a)</td><td>131.10 (n/a)</td><td>51.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.28 (+17.98%)</td><td>0.22 <b>(+27.39%)</b></td><td>0.22 <b>(+33.03%)</b></td><td>0.18 <b>(+39.54%)</b></td><td>0.04 (-8.12%)</td><td>192.00 <b>(-28.36%)</b></td><td>158.60 <b>(-22.99%)</b></td><td>156.30 <b>(-24.82%)</b></td><td>122.80 (-15.19%)</td><td>25.01 <b>(-44.14%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>268.00 (n/a)</td><td>205.94 (n/a)</td><td>207.90 (n/a)</td><td>144.80 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.26 (+3.52%)</td><td>0.21 (+4.04%)</td><td>0.21 (+10.53%)</td><td>0.18 <b>(+29.45%)</b></td><td>0.04 <b>(-27.45%)</b></td><td>194.50 <b>(-22.73%)</b></td><td>167.26 (-6.64%)</td><td>165.30 (-9.52%)</td><td>131.70 (-3.45%)</td><td>26.79 <b>(-42.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>251.70 (n/a)</td><td>179.16 (n/a)</td><td>182.70 (n/a)</td><td>136.40 (n/a)</td><td>46.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.22 (-1.24%)</td><td>0.19 (+0.70%)</td><td>0.19 (+3.09%)</td><td>0.16 (-1.54%)</td><td>0.03 (-10.63%)</td><td>220.50 (+1.57%)</td><td>184.42 (-1.09%)</td><td>181.40 (-2.99%)</td><td>157.60 (+1.22%)</td><td>27.39 (-9.26%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>217.10 (n/a)</td><td>186.46 (n/a)</td><td>187.00 (n/a)</td><td>155.70 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.25 (-14.34%)</td><td>0.21 (+11.53%)</td><td>0.20 (+12.26%)</td><td>0.19 <b>(+49.13%)</b></td><td>0.03 <b>(-57.06%)</b></td><td>184.30 <b>(-32.96%)</b></td><td>165.78 (-15.67%)</td><td>174.80 (-10.95%)</td><td>138.20 (+16.72%)</td><td>19.51 <b>(-64.86%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>274.90 (n/a)</td><td>196.58 (n/a)</td><td>196.30 (n/a)</td><td>118.40 (n/a)</td><td>55.53 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.93 (+1.99%)</td><td>0.66 (-2.82%)</td><td>0.61 (-4.32%)</td><td>0.54 (+1.92%)</td><td>0.16 (+3.51%)</td><td>241.20 (-1.87%)</td><td>206.88 (+2.95%)</td><td>213.40 (+4.51%)</td><td>141.70 (-1.94%)</td><td>39.62 (-2.69%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.91 (n/a)</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.53 (n/a)</td><td>0.15 (n/a)</td><td>245.80 (n/a)</td><td>200.96 (n/a)</td><td>204.20 (n/a)</td><td>144.50 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.22 <b>(+29.90%)</b></td><td>0.80 (+4.47%)</td><td>0.67 (-6.98%)</td><td>0.65 (+3.94%)</td><td>0.24 <b>(+106.74%)</b></td><td>200.30 (-3.79%)</td><td>173.82 (-0.53%)</td><td>194.40 (+7.52%)</td><td>107.30 <b>(-22.97%)</b></td><td>39.48 <b>(+53.65%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.94 (n/a)</td><td>0.76 (n/a)</td><td>0.72 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>208.20 (n/a)</td><td>174.74 (n/a)</td><td>180.80 (n/a)</td><td>139.30 (n/a)</td><td>25.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.79 <b>(-31.56%)</b></td><td>0.64 <b>(-20.21%)</b></td><td>0.68 (-6.79%)</td><td>0.40 <b>(-35.54%)</b></td><td>0.15 <b>(-27.63%)</b></td><td>330.90 <b>(+55.13%)</b></td><td>217.68 <b>(+27.00%)</b></td><td>192.80 (+7.29%)</td><td>165.10 <b>(+46.11%)</b></td><td>66.12 <b>(+79.46%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.16 (n/a)</td><td>0.80 (n/a)</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.21 (n/a)</td><td>213.30 (n/a)</td><td>171.40 (n/a)</td><td>179.70 (n/a)</td><td>113.00 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.00 (+0.00%)</td><td>0.00 (+2.78%)</td><td>0.00 (+2.27%)</td><td>0.00 (+7.50%)</td><td>0.00 <b>(-58.74%)</b></td><td>948.71 (-8.36%)</td><td>925.10 (-2.84%)</td><td>918.95 (-1.00%)</td><td>906.07 (+0.03%)</td><td>17.00 <b>(-67.58%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1035.23 (n/a)</td><td>952.12 (n/a)</td><td>928.26 (n/a)</td><td>905.79 (n/a)</td><td>52.44 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.01 (-2.35%)</td><td>0.01 (-1.22%)</td><td>0.01 (-2.38%)</td><td>0.01 (+2.67%)</td><td>0.00 <b>(-44.79%)</b></td><td>1064.88 (-2.48%)</td><td>1011.46 (+1.06%)</td><td>997.09 (+2.12%)</td><td>983.10 (+2.55%)</td><td>32.50 <b>(-42.48%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1091.94 (n/a)</td><td>1000.87 (n/a)</td><td>976.35 (n/a)</td><td>958.67 (n/a)</td><td>56.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.97 (-0.18%)</td><td>0.95 (-0.18%)</td><td>0.94 (-0.17%)</td><td>0.94 (-0.13%)</td><td>0.01 (-3.62%)</td><td>2233.52 (+0.12%)</td><td>2214.50 (+0.17%)</td><td>2221.80 (+0.17%)</td><td>2172.30 (+0.17%)</td><td>24.61 (-3.48%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2230.78 (n/a)</td><td>2210.65 (n/a)</td><td>2218.02 (n/a)</td><td>2168.52 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.31 (-1.76%)</td><td>4.53 (-2.14%)</td><td>4.43 (-5.64%)</td><td>4.00 (+8.56%)</td><td>0.51 (-17.25%)</td><td>262.40 (-7.87%)</td><td>233.92 (+1.62%)</td><td>236.90 (+6.00%)</td><td>197.50 (+1.80%)</td><td>25.17 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.41 (n/a)</td><td>4.63 (n/a)</td><td>4.69 (n/a)</td><td>3.68 (n/a)</td><td>0.62 (n/a)</td><td>284.80 (n/a)</td><td>230.20 (n/a)</td><td>223.50 (n/a)</td><td>194.00 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.65 (-3.33%)</td><td>4.70 (-2.30%)</td><td>4.98 (+11.88%)</td><td>3.91 (+6.25%)</td><td>0.75 <b>(-23.78%)</b></td><td>268.30 (-5.86%)</td><td>227.50 (+1.07%)</td><td>210.40 (-10.62%)</td><td>185.50 (+3.46%)</td><td>36.50 (-19.77%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.85 (n/a)</td><td>4.82 (n/a)</td><td>4.46 (n/a)</td><td>3.68 (n/a)</td><td>0.98 (n/a)</td><td>285.00 (n/a)</td><td>225.10 (n/a)</td><td>235.40 (n/a)</td><td>179.30 (n/a)</td><td>45.50 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>5.65 (-1.38%)</td><td>4.64 (-5.14%)</td><td>4.55 (-2.57%)</td><td>3.84 (-10.61%)</td><td>0.66 (+18.68%)</td><td>272.70 (+11.85%)</td><td>229.46 (+6.03%)</td><td>230.40 (+2.63%)</td><td>185.70 (+1.42%)</td><td>31.78 <b>(+34.50%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.73 (n/a)</td><td>4.89 (n/a)</td><td>4.67 (n/a)</td><td>4.30 (n/a)</td><td>0.56 (n/a)</td><td>243.80 (n/a)</td><td>216.42 (n/a)</td><td>224.50 (n/a)</td><td>183.10 (n/a)</td><td>23.62 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.87 (-5.89%)</td><td>4.30 (-5.87%)</td><td>4.12 (-18.85%)</td><td>3.87 <b>(+39.69%)</b></td><td>0.40 <b>(-60.89%)</b></td><td>270.60 <b>(-28.41%)</b></td><td>245.22 (+0.98%)</td><td>254.50 <b>(+23.24%)</b></td><td>215.40 (+6.27%)</td><td>22.13 <b>(-70.89%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>5.17 (n/a)</td><td>4.57 (n/a)</td><td>5.08 (n/a)</td><td>2.77 (n/a)</td><td>1.02 (n/a)</td><td>378.00 (n/a)</td><td>242.84 (n/a)</td><td>206.50 (n/a)</td><td>202.70 (n/a)</td><td>76.01 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>9.33 (+0.75%)</td><td>7.96 (+1.43%)</td><td>7.73 (-4.15%)</td><td>6.94 (+2.77%)</td><td>0.88 (-11.78%)</td><td>302.20 (-2.67%)</td><td>265.86 (-1.74%)</td><td>271.40 (+4.34%)</td><td>224.90 (-0.75%)</td><td>28.15 (-16.60%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.26 (n/a)</td><td>7.85 (n/a)</td><td>8.06 (n/a)</td><td>6.75 (n/a)</td><td>1.00 (n/a)</td><td>310.50 (n/a)</td><td>270.56 (n/a)</td><td>260.10 (n/a)</td><td>226.60 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.98 (-12.55%)</td><td>7.61 (+0.02%)</td><td>7.70 (-2.56%)</td><td>7.25 <b>(+28.82%)</b></td><td>0.33 <b>(-79.23%)</b></td><td>289.30 <b>(-22.36%)</b></td><td>275.90 (-3.57%)</td><td>272.20 (+2.64%)</td><td>263.00 (+14.40%)</td><td>12.05 <b>(-81.08%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.12 (n/a)</td><td>7.61 (n/a)</td><td>7.91 (n/a)</td><td>5.63 (n/a)</td><td>1.59 (n/a)</td><td>372.60 (n/a)</td><td>286.12 (n/a)</td><td>265.20 (n/a)</td><td>229.90 (n/a)</td><td>63.70 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.61 (-8.79%)</td><td>7.59 (-3.43%)</td><td>7.25 (-5.67%)</td><td>7.09 (+14.81%)</td><td>0.64 <b>(-48.07%)</b></td><td>295.80 (-12.90%)</td><td>277.82 (+2.01%)</td><td>289.20 (+6.01%)</td><td>243.60 (+9.63%)</td><td>21.83 <b>(-50.67%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.44 (n/a)</td><td>7.86 (n/a)</td><td>7.69 (n/a)</td><td>6.18 (n/a)</td><td>1.22 (n/a)</td><td>339.60 (n/a)</td><td>272.34 (n/a)</td><td>272.80 (n/a)</td><td>222.20 (n/a)</td><td>44.26 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.04 (-19.21%)</td><td>7.31 (-16.18%)</td><td>7.89 (-8.93%)</td><td>5.92 (-9.54%)</td><td>0.93 <b>(-32.41%)</b></td><td>354.00 (+10.56%)</td><td>290.90 (+18.27%)</td><td>265.70 (+9.79%)</td><td>260.80 <b>(+23.78%)</b></td><td>40.49 (-8.82%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>9.95 (n/a)</td><td>8.72 (n/a)</td><td>8.67 (n/a)</td><td>6.55 (n/a)</td><td>1.38 (n/a)</td><td>320.20 (n/a)</td><td>245.96 (n/a)</td><td>242.00 (n/a)</td><td>210.70 (n/a)</td><td>44.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>9.00 (-16.11%)</td><td>7.74 (-16.65%)</td><td>7.97 (-18.12%)</td><td>5.57 <b>(-23.03%)</b></td><td>1.37 (-9.98%)</td><td>376.70 <b>(+29.90%)</b></td><td>279.04 <b>(+20.75%)</b></td><td>263.30 <b>(+22.18%)</b></td><td>233.00 (+19.24%)</td><td>58.15 <b>(+42.53%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>10.73 (n/a)</td><td>9.29 (n/a)</td><td>9.73 (n/a)</td><td>7.23 (n/a)</td><td>1.53 (n/a)</td><td>290.00 (n/a)</td><td>231.08 (n/a)</td><td>215.50 (n/a)</td><td>195.40 (n/a)</td><td>40.80 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>8.35 (+2.73%)</td><td>7.28 (-1.51%)</td><td>7.60 (+3.87%)</td><td>5.50 (-15.37%)</td><td>1.07 <b>(+74.98%)</b></td><td>381.50 (+18.15%)</td><td>293.94 (+3.04%)</td><td>275.80 (-3.70%)</td><td>251.10 (-2.67%)</td><td>50.67 <b>(+107.60%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>8.13 (n/a)</td><td>7.39 (n/a)</td><td>7.32 (n/a)</td><td>6.50 (n/a)</td><td>0.61 (n/a)</td><td>322.90 (n/a)</td><td>285.28 (n/a)</td><td>286.40 (n/a)</td><td>258.00 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.00 (-2.42%)</td><td>11.41 (+1.65%)</td><td>11.44 (+1.34%)</td><td>11.06 (+8.96%)</td><td>0.37 <b>(-51.15%)</b></td><td>379.20 (-8.21%)</td><td>367.80 (-1.90%)</td><td>366.70 (-1.32%)</td><td>349.60 (+2.46%)</td><td>11.83 <b>(-54.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.29 (n/a)</td><td>11.23 (n/a)</td><td>11.29 (n/a)</td><td>10.15 (n/a)</td><td>0.76 (n/a)</td><td>413.10 (n/a)</td><td>374.94 (n/a)</td><td>371.60 (n/a)</td><td>341.20 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.85 (+1.22%)</td><td>11.22 (-5.86%)</td><td>11.08 (-8.52%)</td><td>9.92 (-10.74%)</td><td>1.13 <b>(+67.77%)</b></td><td>422.90 (+12.03%)</td><td>376.92 (+6.79%)</td><td>378.70 (+9.32%)</td><td>326.50 (-1.21%)</td><td>37.02 <b>(+84.07%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.69 (n/a)</td><td>11.91 (n/a)</td><td>12.11 (n/a)</td><td>11.11 (n/a)</td><td>0.67 (n/a)</td><td>377.50 (n/a)</td><td>352.94 (n/a)</td><td>346.40 (n/a)</td><td>330.50 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.25 (-4.26%)</td><td>10.97 (-6.06%)</td><td>10.73 (-8.65%)</td><td>10.25 (-1.55%)</td><td>0.83 (-4.46%)</td><td>409.30 (+1.56%)</td><td>384.02 (+6.44%)</td><td>390.80 (+9.47%)</td><td>342.50 (+4.45%)</td><td>27.61 (+0.71%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.79 (n/a)</td><td>11.68 (n/a)</td><td>11.75 (n/a)</td><td>10.41 (n/a)</td><td>0.86 (n/a)</td><td>403.00 (n/a)</td><td>360.78 (n/a)</td><td>357.00 (n/a)</td><td>327.90 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>13.77 (+5.70%)</td><td>12.62 (+0.85%)</td><td>12.60 (+1.41%)</td><td>11.12 (-6.60%)</td><td>1.02 <b>(+127.67%)</b></td><td>377.10 (+7.07%)</td><td>334.06 (-0.41%)</td><td>332.90 (-1.39%)</td><td>304.50 (-5.41%)</td><td>28.00 <b>(+132.16%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.03 (n/a)</td><td>12.52 (n/a)</td><td>12.42 (n/a)</td><td>11.91 (n/a)</td><td>0.45 (n/a)</td><td>352.20 (n/a)</td><td>335.42 (n/a)</td><td>337.60 (n/a)</td><td>321.90 (n/a)</td><td>12.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.94 (+1.28%)</td><td>11.87 (-5.13%)</td><td>11.85 (-4.94%)</td><td>10.86 (-11.36%)</td><td>0.78 <b>(+227.53%)</b></td><td>386.20 (+12.83%)</td><td>354.58 (+5.73%)</td><td>354.00 (+5.20%)</td><td>324.10 (-1.28%)</td><td>23.28 <b>(+266.38%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>12.78 (n/a)</td><td>12.51 (n/a)</td><td>12.46 (n/a)</td><td>12.25 (n/a)</td><td>0.24 (n/a)</td><td>342.30 (n/a)</td><td>335.36 (n/a)</td><td>336.50 (n/a)</td><td>328.30 (n/a)</td><td>6.35 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.91 (-1.51%)</td><td>12.40 (+5.33%)</td><td>12.38 (-2.57%)</td><td>11.86 <b>(+23.88%)</b></td><td>0.41 <b>(-75.74%)</b></td><td>353.70 (-19.28%)</td><td>338.60 (-6.63%)</td><td>338.80 (+2.64%)</td><td>324.80 (+1.53%)</td><td>11.13 <b>(-79.82%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>13.11 (n/a)</td><td>11.77 (n/a)</td><td>12.71 (n/a)</td><td>9.57 (n/a)</td><td>1.68 (n/a)</td><td>438.20 (n/a)</td><td>362.64 (n/a)</td><td>330.10 (n/a)</td><td>319.90 (n/a)</td><td>55.13 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>14.63 (+3.98%)</td><td>12.39 (+5.39%)</td><td>11.89 (-5.24%)</td><td>9.42 (+6.64%)</td><td>2.11 (-3.72%)</td><td>445.20 (-6.21%)</td><td>347.16 (-5.62%)</td><td>352.80 (+5.53%)</td><td>286.80 (-3.82%)</td><td>63.46 (-14.52%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>14.07 (n/a)</td><td>11.75 (n/a)</td><td>12.55 (n/a)</td><td>8.84 (n/a)</td><td>2.19 (n/a)</td><td>474.70 (n/a)</td><td>367.84 (n/a)</td><td>334.30 (n/a)</td><td>298.20 (n/a)</td><td>74.24 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>12.47 (-14.43%)</td><td>11.18 (-12.36%)</td><td>11.62 (-4.30%)</td><td>8.55 <b>(-26.63%)</b></td><td>1.53 (+15.19%)</td><td>490.80 <b>(+36.30%)</b></td><td>382.10 (+15.20%)</td><td>361.00 (+4.52%)</td><td>336.50 (+16.88%)</td><td>62.13 <b>(+86.99%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>14.57 (n/a)</td><td>12.75 (n/a)</td><td>12.14 (n/a)</td><td>11.65 (n/a)</td><td>1.33 (n/a)</td><td>360.10 (n/a)</td><td>331.68 (n/a)</td><td>345.40 (n/a)</td><td>287.90 (n/a)</td><td>33.22 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.20 (+18.33%)</td><td>2.66 (+8.84%)</td><td>2.61 (+6.41%)</td><td>2.20 (+9.62%)</td><td>0.39 <b>(+41.26%)</b></td><td>238.70 (-8.79%)</td><td>200.08 (-7.61%)</td><td>200.70 (-6.04%)</td><td>163.80 (-15.48%)</td><td>28.91 (+7.27%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>2.71 (n/a)</td><td>2.45 (n/a)</td><td>2.45 (n/a)</td><td>2.00 (n/a)</td><td>0.28 (n/a)</td><td>261.70 (n/a)</td><td>216.56 (n/a)</td><td>213.60 (n/a)</td><td>193.80 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>4.55 <b>(-25.12%)</b></td><td>4.27 (-8.54%)</td><td>4.40 (+0.16%)</td><td>3.68 (-2.52%)</td><td>0.35 <b>(-61.68%)</b></td><td>285.30 (+2.59%)</td><td>247.24 (+6.92%)</td><td>238.50 (-0.17%)</td><td>230.60 <b>(+33.53%)</b></td><td>22.17 <b>(-46.44%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>6.07 (n/a)</td><td>4.66 (n/a)</td><td>4.39 (n/a)</td><td>3.77 (n/a)</td><td>0.91 (n/a)</td><td>278.10 (n/a)</td><td>231.24 (n/a)</td><td>238.90 (n/a)</td><td>172.70 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>7.01 (-12.42%)</td><td>6.62 (-6.92%)</td><td>6.56 (-8.21%)</td><td>6.34 (+4.20%)</td><td>0.27 <b>(-65.04%)</b></td><td>330.50 (-4.04%)</td><td>317.32 (+6.55%)</td><td>319.70 (+8.96%)</td><td>299.20 (+14.20%)</td><td>12.58 <b>(-61.72%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>8.00 (n/a)</td><td>7.11 (n/a)</td><td>7.15 (n/a)</td><td>6.09 (n/a)</td><td>0.76 (n/a)</td><td>344.40 (n/a)</td><td>297.80 (n/a)</td><td>293.40 (n/a)</td><td>262.00 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>3.35 (-12.82%)</td><td>2.71 (+4.84%)</td><td>2.64 (+3.77%)</td><td>2.09 (+16.03%)</td><td>0.47 <b>(-40.67%)</b></td><td>251.10 (-13.83%)</td><td>198.36 (-8.61%)</td><td>198.70 (-3.64%)</td><td>156.40 (+14.66%)</td><td>35.28 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>3.84 (n/a)</td><td>2.58 (n/a)</td><td>2.54 (n/a)</td><td>1.80 (n/a)</td><td>0.79 (n/a)</td><td>291.40 (n/a)</td><td>217.04 (n/a)</td><td>206.20 (n/a)</td><td>136.40 (n/a)</td><td>59.39 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.21 (+8.56%)</td><td>0.17 (+0.85%)</td><td>0.17 (-0.55%)</td><td>0.13 (-9.68%)</td><td>0.04 <b>(+67.34%)</b></td><td>255.30 (+10.71%)</td><td>195.74 (+1.69%)</td><td>194.80 (+0.57%)</td><td>152.70 (-7.85%)</td><td>43.86 <b>(+66.88%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>192.48 (n/a)</td><td>193.70 (n/a)</td><td>165.70 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.24 <b>(+32.31%)</b></td><td>0.18 (+7.97%)</td><td>0.16 (-8.17%)</td><td>0.15 (+4.11%)</td><td>0.04 <b>(+94.04%)</b></td><td>219.60 (-3.94%)</td><td>188.14 (-5.61%)</td><td>201.60 (+8.86%)</td><td>135.60 <b>(-24.41%)</b></td><td>33.90 <b>(+39.47%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>228.60 (n/a)</td><td>199.32 (n/a)</td><td>185.20 (n/a)</td><td>179.40 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.52 <b>(+38.02%)</b></td><td>0.39 (+12.26%)</td><td>0.38 (+11.26%)</td><td>0.30 (-6.07%)</td><td>0.08 <b>(+207.46%)</b></td><td>220.90 (+6.51%)</td><td>174.80 (-8.39%)</td><td>172.40 (-10.11%)</td><td>125.90 <b>(-27.56%)</b></td><td>33.97 <b>(+131.85%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>207.40 (n/a)</td><td>190.80 (n/a)</td><td>191.80 (n/a)</td><td>173.80 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.54 <b>(+53.97%)</b></td><td>0.39 <b>(+27.08%)</b></td><td>0.37 (+17.65%)</td><td>0.31 <b>(+23.46%)</b></td><td>0.09 <b>(+138.90%)</b></td><td>214.20 (-19.02%)</td><td>173.92 (-19.55%)</td><td>177.10 (-14.98%)</td><td>122.50 <b>(-35.05%)</b></td><td>33.79 (+18.17%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>264.50 (n/a)</td><td>216.18 (n/a)</td><td>208.30 (n/a)</td><td>188.60 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.53 <b>(+45.85%)</b></td><td>0.39 <b>(+21.21%)</b></td><td>0.38 (+13.47%)</td><td>0.28 (+3.86%)</td><td>0.09 <b>(+155.10%)</b></td><td>231.40 (-3.70%)</td><td>173.40 (-14.98%)</td><td>171.10 (-11.89%)</td><td>124.80 <b>(-31.43%)</b></td><td>38.72 <b>(+67.06%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>240.30 (n/a)</td><td>203.96 (n/a)</td><td>194.20 (n/a)</td><td>182.00 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.01 <b>(+31.39%)</b></td><td>0.78 (+19.09%)</td><td>0.75 (+17.88%)</td><td>0.54 (-0.84%)</td><td>0.17 <b>(+93.16%)</b></td><td>244.50 (+0.82%)</td><td>175.32 (-13.59%)</td><td>175.30 (-15.15%)</td><td>130.20 <b>(-23.86%)</b></td><td>43.18 <b>(+52.15%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.09 (n/a)</td><td>242.50 (n/a)</td><td>202.90 (n/a)</td><td>206.60 (n/a)</td><td>171.00 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.02 (+16.35%)</td><td>0.71 (+11.68%)</td><td>0.64 (+14.13%)</td><td>0.60 <b>(+39.70%)</b></td><td>0.18 (-6.05%)</td><td>219.80 <b>(-28.43%)</b></td><td>191.94 (-13.13%)</td><td>204.30 (-12.39%)</td><td>128.80 (-14.08%)</td><td>37.72 <b>(-41.12%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.87 (n/a)</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.19 (n/a)</td><td>307.10 (n/a)</td><td>220.94 (n/a)</td><td>233.20 (n/a)</td><td>149.90 (n/a)</td><td>64.06 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>1.13 (+1.66%)</td><td>0.79 (+3.21%)</td><td>0.77 (+13.11%)</td><td>0.58 (+3.36%)</td><td>0.20 (-11.58%)</td><td>225.00 (-3.27%)</td><td>173.32 (-4.92%)</td><td>171.20 (-11.57%)</td><td>116.20 (-1.61%)</td><td>39.41 (-19.31%)</td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>1.11 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.56 (n/a)</td><td>0.23 (n/a)</td><td>232.60 (n/a)</td><td>182.28 (n/a)</td><td>193.60 (n/a)</td><td>118.10 (n/a)</td><td>48.84 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.85 (+10.50%)</td><td>0.74 (+10.35%)</td><td>0.83 <b>(+26.20%)</b></td><td>0.50 (-12.94%)</td><td>0.15 <b>(+80.36%)</b></td><td>262.60 (+14.87%)</td><td>183.94 (-6.65%)</td><td>158.40 <b>(-20.80%)</b></td><td>153.60 (-9.49%)</td><td>46.74 <b>(+87.94%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.09 (n/a)</td><td>228.60 (n/a)</td><td>197.04 (n/a)</td><td>200.00 (n/a)</td><td>169.70 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>e216c2f</code> — 2026-07-13 22:02:53</td><td>0.13 <b>(+50.88%)</b></td><td>0.10 <b>(+31.59%)</b></td><td>0.10 <b>(+21.76%)</b></td><td>0.08 (+15.26%)</td><td>0.02 <b>(+137.13%)</b></td><td>201.20 (-13.24%)</td><td>161.10 <b>(-22.62%)</b></td><td>166.10 (-17.85%)</td><td>121.70 <b>(-33.71%)</b></td><td>28.92 <b>(+32.05%)</b></td>
</tr>
<tr>
<td><code>1f9e5a9</code> — 2026-07-13 18:14:05</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>208.18 (n/a)</td><td>202.20 (n/a)</td><td>183.60 (n/a)</td><td>21.90 (n/a)</td>
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
