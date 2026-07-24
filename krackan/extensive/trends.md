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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-13.41%)</td><td>0.04 (-7.77%)</td><td>0.03 (-3.99%)</td><td>0.03 (-6.22%)</td><td>0.01 <b>(-30.71%)</b></td><td>221.70 (+6.64%)</td><td>179.52 (+6.60%)</td><td>179.30 (+4.18%)</td><td>141.40 (+15.43%)</td><td>31.15 (-15.75%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>168.40 (n/a)</td><td>172.10 (n/a)</td><td>122.50 (n/a)</td><td>36.97 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+18.52%)</td><td>0.04 (+16.65%)</td><td>0.04 (+7.76%)</td><td>0.03 <b>(+23.03%)</b></td><td>0.01 (+19.85%)</td><td>181.00 (-18.72%)</td><td>153.62 (-14.28%)</td><td>167.00 (-7.22%)</td><td>109.70 (-15.62%)</td><td>29.07 (-17.43%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>179.22 (n/a)</td><td>180.00 (n/a)</td><td>130.00 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (+16.82%)</td><td>0.04 <b>(+26.83%)</b></td><td>0.04 <b>(+24.28%)</b></td><td>0.03 <b>(+39.47%)</b></td><td>0.01 (-10.60%)</td><td>195.50 <b>(-28.28%)</b></td><td>166.88 <b>(-22.45%)</b></td><td>170.80 (-19.51%)</td><td>131.70 (-14.37%)</td><td>23.45 <b>(-44.73%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.60 (n/a)</td><td>215.20 (n/a)</td><td>212.20 (n/a)</td><td>153.80 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (+6.94%)</td><td>0.04 (+6.13%)</td><td>0.04 (+9.12%)</td><td>0.03 (-3.75%)</td><td>0.01 <b>(+67.52%)</b></td><td>211.40 (+3.93%)</td><td>170.00 (-3.37%)</td><td>158.30 (-8.34%)</td><td>134.90 (-6.51%)</td><td>38.34 <b>(+63.64%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>175.92 (n/a)</td><td>172.70 (n/a)</td><td>144.30 (n/a)</td><td>23.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-2.67%)</td><td>0.04 (-8.76%)</td><td>0.03 <b>(-21.24%)</b></td><td>0.03 <b>(+20.12%)</b></td><td>0.01 <b>(-31.67%)</b></td><td>190.80 (-16.75%)</td><td>173.34 (+7.24%)</td><td>185.10 <b>(+26.95%)</b></td><td>139.20 (+2.73%)</td><td>21.84 <b>(-43.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>161.64 (n/a)</td><td>145.80 (n/a)</td><td>135.50 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (+4.54%)</td><td>0.04 (+1.98%)</td><td>0.04 (+0.06%)</td><td>0.03 (-2.94%)</td><td>0.01 <b>(+24.42%)</b></td><td>215.00 (+3.02%)</td><td>165.46 (-1.03%)</td><td>162.90 (-0.06%)</td><td>132.40 (-4.34%)</td><td>31.93 <b>(+21.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>167.18 (n/a)</td><td>163.00 (n/a)</td><td>138.40 (n/a)</td><td>26.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-19.42%)</td><td>0.03 (-10.59%)</td><td>0.03 (-10.69%)</td><td>0.03 (-9.35%)</td><td>0.00 <b>(-30.98%)</b></td><td>242.80 (+10.31%)</td><td>199.10 (+10.81%)</td><td>204.80 (+11.97%)</td><td>161.30 <b>(+24.08%)</b></td><td>31.43 (-2.46%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>179.68 (n/a)</td><td>182.90 (n/a)</td><td>130.00 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 <b>(+26.54%)</b></td><td>0.03 (-1.38%)</td><td>0.03 (-11.68%)</td><td>0.02 (-10.29%)</td><td>0.01 <b>(+144.19%)</b></td><td>248.70 (+11.47%)</td><td>202.68 (+4.42%)</td><td>208.70 (+13.18%)</td><td>141.20 <b>(-20.98%)</b></td><td>40.30 <b>(+110.21%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>223.10 (n/a)</td><td>194.10 (n/a)</td><td>184.40 (n/a)</td><td>178.70 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (-7.06%)</td><td>0.07 (-6.35%)</td><td>0.08 (-4.66%)</td><td>0.06 (-3.22%)</td><td>0.01 (-3.13%)</td><td>205.80 (+3.31%)</td><td>170.84 (+6.96%)</td><td>163.00 (+4.89%)</td><td>136.60 (+7.56%)</td><td>31.13 (+9.90%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>159.72 (n/a)</td><td>155.40 (n/a)</td><td>127.00 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (+11.23%)</td><td>0.08 (+0.59%)</td><td>0.08 (+8.37%)</td><td>0.06 (-6.28%)</td><td>0.02 <b>(+43.36%)</b></td><td>190.80 (+6.71%)</td><td>158.32 (+1.01%)</td><td>153.30 (-7.76%)</td><td>120.50 (-10.07%)</td><td>30.64 <b>(+45.40%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>156.74 (n/a)</td><td>166.20 (n/a)</td><td>134.00 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (-2.07%)</td><td>0.08 (-9.25%)</td><td>0.08 (-5.70%)</td><td>0.05 <b>(-23.72%)</b></td><td>0.02 <b>(+35.28%)</b></td><td>233.20 <b>(+31.08%)</b></td><td>170.18 (+12.82%)</td><td>151.40 (+6.02%)</td><td>130.40 (+2.11%)</td><td>40.41 <b>(+82.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>150.84 (n/a)</td><td>142.80 (n/a)</td><td>127.70 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (+1.93%)</td><td>0.08 (+1.37%)</td><td>0.07 (-1.88%)</td><td>0.07 (+9.88%)</td><td>0.01 (-8.46%)</td><td>181.10 (-8.99%)</td><td>160.94 (-1.83%)</td><td>169.80 (+1.92%)</td><td>128.50 (-1.91%)</td><td>20.53 (-19.05%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>163.94 (n/a)</td><td>166.60 (n/a)</td><td>131.00 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 <b>(-27.79%)</b></td><td>0.06 <b>(-24.99%)</b></td><td>0.07 <b>(-20.50%)</b></td><td>0.06 <b>(-20.98%)</b></td><td>0.01 <b>(-53.64%)</b></td><td>219.60 <b>(+26.57%)</b></td><td>192.38 <b>(+31.68%)</b></td><td>186.30 <b>(+25.79%)</b></td><td>169.30 <b>(+38.54%)</b></td><td>19.38 (-16.46%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.50 (n/a)</td><td>146.10 (n/a)</td><td>148.10 (n/a)</td><td>122.20 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (-4.43%)</td><td>0.07 (-8.07%)</td><td>0.07 (-9.11%)</td><td>0.06 (-11.97%)</td><td>0.01 <b>(+24.75%)</b></td><td>198.10 (+13.59%)</td><td>174.18 (+9.07%)</td><td>171.50 (+10.01%)</td><td>158.30 (+4.63%)</td><td>14.83 <b>(+50.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>159.70 (n/a)</td><td>155.90 (n/a)</td><td>151.30 (n/a)</td><td>9.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-14.85%)</td><td>0.06 (+4.60%)</td><td>0.06 (+11.18%)</td><td>0.05 <b>(+27.67%)</b></td><td>0.00 <b>(-64.65%)</b></td><td>225.30 <b>(-21.66%)</b></td><td>200.78 (-7.92%)</td><td>190.00 (-10.04%)</td><td>189.10 (+17.45%)</td><td>16.26 <b>(-67.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>287.60 (n/a)</td><td>218.06 (n/a)</td><td>211.20 (n/a)</td><td>161.00 (n/a)</td><td>50.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (-9.81%)</td><td>0.07 (+6.69%)</td><td>0.07 (+17.51%)</td><td>0.05 (+10.90%)</td><td>0.01 <b>(-33.16%)</b></td><td>246.60 (-9.84%)</td><td>186.28 (-8.57%)</td><td>175.40 (-14.90%)</td><td>165.40 (+10.86%)</td><td>34.19 <b>(-31.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>273.50 (n/a)</td><td>203.74 (n/a)</td><td>206.10 (n/a)</td><td>149.20 (n/a)</td><td>49.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 <b>(-22.04%)</b></td><td>0.13 <b>(-20.54%)</b></td><td>0.13 (-18.32%)</td><td>0.11 <b>(-20.75%)</b></td><td>0.01 <b>(-39.58%)</b></td><td>224.00 <b>(+26.20%)</b></td><td>189.20 <b>(+24.97%)</b></td><td>188.20 <b>(+22.45%)</b></td><td>165.00 <b>(+28.21%)</b></td><td>22.56 (+0.94%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.50 (n/a)</td><td>151.40 (n/a)</td><td>153.70 (n/a)</td><td>128.70 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (+6.15%)</td><td>0.15 (-0.27%)</td><td>0.15 (+1.64%)</td><td>0.11 (-11.74%)</td><td>0.03 <b>(+78.69%)</b></td><td>214.90 (+13.28%)</td><td>172.56 (+2.13%)</td><td>162.20 (-1.58%)</td><td>143.30 (-5.79%)</td><td>31.78 <b>(+88.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>168.96 (n/a)</td><td>164.80 (n/a)</td><td>152.10 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (-15.14%)</td><td>0.14 (-18.41%)</td><td>0.13 (-19.89%)</td><td>0.11 <b>(-21.39%)</b></td><td>0.03 (-2.98%)</td><td>225.70 <b>(+27.23%)</b></td><td>185.98 <b>(+23.48%)</b></td><td>193.00 <b>(+24.84%)</b></td><td>139.90 (+17.86%)</td><td>32.17 <b>(+44.69%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>177.40 (n/a)</td><td>150.62 (n/a)</td><td>154.60 (n/a)</td><td>118.70 (n/a)</td><td>22.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-6.94%)</td><td>0.13 (-15.49%)</td><td>0.12 <b>(-23.79%)</b></td><td>0.12 (+4.74%)</td><td>0.02 <b>(-33.45%)</b></td><td>212.40 (-4.54%)</td><td>193.38 (+16.79%)</td><td>197.80 <b>(+31.17%)</b></td><td>160.90 (+7.48%)</td><td>21.75 <b>(-31.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>165.58 (n/a)</td><td>150.80 (n/a)</td><td>149.70 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (-16.58%)</td><td>0.14 (-8.61%)</td><td>0.14 (-14.90%)</td><td>0.11 <b>(+54.76%)</b></td><td>0.02 <b>(-54.21%)</b></td><td>226.60 <b>(-35.39%)</b></td><td>178.20 (-3.32%)</td><td>174.70 (+17.48%)</td><td>147.10 (+19.89%)</td><td>32.75 <b>(-65.72%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>350.70 (n/a)</td><td>184.32 (n/a)</td><td>148.70 (n/a)</td><td>122.70 (n/a)</td><td>95.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (-11.89%)</td><td>0.13 (-1.74%)</td><td>0.14 (+1.06%)</td><td>0.11 (+19.76%)</td><td>0.02 <b>(-38.67%)</b></td><td>229.20 (-16.53%)</td><td>187.56 (-1.48%)</td><td>174.70 (-1.02%)</td><td>155.60 (+13.49%)</td><td>28.94 <b>(-43.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>274.60 (n/a)</td><td>190.38 (n/a)</td><td>176.50 (n/a)</td><td>137.10 (n/a)</td><td>51.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (+12.47%)</td><td>0.14 (+6.80%)</td><td>0.15 (+15.19%)</td><td>0.08 <b>(-26.87%)</b></td><td>0.04 <b>(+86.52%)</b></td><td>296.90 <b>(+36.69%)</b></td><td>189.14 (-0.72%)</td><td>169.30 (-13.18%)</td><td>131.60 (-11.08%)</td><td>64.56 <b>(+138.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.20 (n/a)</td><td>190.52 (n/a)</td><td>195.00 (n/a)</td><td>148.00 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (-9.97%)</td><td>0.12 (-13.47%)</td><td>0.12 (-8.20%)</td><td>0.08 <b>(-28.73%)</b></td><td>0.02 <b>(+61.16%)</b></td><td>291.00 <b>(+40.31%)</b></td><td>219.12 (+18.42%)</td><td>207.40 (+8.93%)</td><td>176.50 (+11.08%)</td><td>46.29 <b>(+153.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>185.04 (n/a)</td><td>190.40 (n/a)</td><td>158.90 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.39 (+1.01%)</td><td>0.32 (+6.62%)</td><td>0.30 (+6.41%)</td><td>0.26 (+0.82%)</td><td>0.06 (+7.55%)</td><td>190.40 (-0.83%)</td><td>159.30 (-5.96%)</td><td>164.80 (-5.99%)</td><td>127.30 (-1.01%)</td><td>27.23 (+4.62%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>192.00 (n/a)</td><td>169.40 (n/a)</td><td>175.30 (n/a)</td><td>128.60 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (-14.57%)</td><td>0.30 (-4.09%)</td><td>0.29 (-0.04%)</td><td>0.24 (-12.01%)</td><td>0.04 <b>(-27.86%)</b></td><td>208.80 (+13.60%)</td><td>168.46 (+3.46%)</td><td>166.90 (+0.00%)</td><td>138.40 (+16.99%)</td><td>26.18 (-1.52%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>183.80 (n/a)</td><td>162.82 (n/a)</td><td>166.90 (n/a)</td><td>118.30 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 (+14.63%)</td><td>0.30 (+10.18%)</td><td>0.30 (+13.32%)</td><td>0.24 (+2.29%)</td><td>0.04 <b>(+39.99%)</b></td><td>201.50 (-2.23%)</td><td>167.26 (-8.74%)</td><td>162.10 (-11.76%)</td><td>140.00 (-12.72%)</td><td>22.40 <b>(+20.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>206.10 (n/a)</td><td>183.28 (n/a)</td><td>183.70 (n/a)</td><td>160.40 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 <b>(+22.68%)</b></td><td>0.27 (+1.48%)</td><td>0.26 (-9.00%)</td><td>0.21 (-7.72%)</td><td>0.07 <b>(+138.72%)</b></td><td>239.20 (+8.38%)</td><td>189.02 (+2.78%)</td><td>188.50 (+9.85%)</td><td>137.40 (-18.46%)</td><td>47.49 <b>(+113.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>183.90 (n/a)</td><td>171.60 (n/a)</td><td>168.50 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (-8.38%)</td><td>0.26 (-1.05%)</td><td>0.25 (-0.05%)</td><td>0.22 (+7.22%)</td><td>0.03 <b>(-28.24%)</b></td><td>218.60 (-6.74%)</td><td>191.60 (-0.05%)</td><td>198.00 (+0.05%)</td><td>164.20 (+9.10%)</td><td>23.46 <b>(-27.17%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>234.40 (n/a)</td><td>191.70 (n/a)</td><td>197.90 (n/a)</td><td>150.50 (n/a)</td><td>32.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (+2.75%)</td><td>0.28 (-3.17%)</td><td>0.28 (-6.73%)</td><td>0.21 (-12.76%)</td><td>0.04 <b>(+46.74%)</b></td><td>232.30 (+14.66%)</td><td>179.16 (+4.52%)</td><td>172.90 (+7.19%)</td><td>155.20 (-2.70%)</td><td>30.92 <b>(+67.83%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>202.60 (n/a)</td><td>171.42 (n/a)</td><td>161.30 (n/a)</td><td>159.50 (n/a)</td><td>18.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 <b>(-20.07%)</b></td><td>0.23 (-16.07%)</td><td>0.24 (-12.37%)</td><td>0.20 <b>(-23.04%)</b></td><td>0.02 (+4.39%)</td><td>248.10 <b>(+29.90%)</b></td><td>211.22 (+19.55%)</td><td>203.70 (+14.12%)</td><td>196.00 <b>(+25.16%)</b></td><td>21.58 <b>(+72.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>191.00 (n/a)</td><td>176.68 (n/a)</td><td>178.50 (n/a)</td><td>156.60 (n/a)</td><td>12.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (+1.04%)</td><td>0.25 (+2.79%)</td><td>0.26 (-1.43%)</td><td>0.17 (+2.65%)</td><td>0.05 (-4.01%)</td><td>290.30 (-2.58%)</td><td>205.42 (-3.07%)</td><td>186.20 (+1.42%)</td><td>173.00 (-1.03%)</td><td>48.61 (-5.59%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>298.00 (n/a)</td><td>211.92 (n/a)</td><td>183.60 (n/a)</td><td>174.80 (n/a)</td><td>51.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (-10.71%)</td><td>0.02 (-8.53%)</td><td>0.02 <b>(-26.98%)</b></td><td>0.01 <b>(+76.18%)</b></td><td>0.00 <b>(-49.15%)</b></td><td>190.40 <b>(-43.23%)</b></td><td>155.14 (-5.24%)</td><td>163.80 <b>(+36.96%)</b></td><td>124.30 (+11.98%)</td><td>28.45 <b>(-70.46%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>335.40 (n/a)</td><td>163.72 (n/a)</td><td>119.60 (n/a)</td><td>111.00 (n/a)</td><td>96.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (+7.73%)</td><td>0.02 (-4.99%)</td><td>0.02 (-5.72%)</td><td>0.02 (-2.54%)</td><td>0.00 <b>(+36.33%)</b></td><td>170.70 (+2.65%)</td><td>142.04 (+6.86%)</td><td>138.10 (+6.07%)</td><td>105.20 (-7.23%)</td><td>28.29 <b>(+34.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.30 (n/a)</td><td>132.92 (n/a)</td><td>130.20 (n/a)</td><td>113.40 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (-5.32%)</td><td>0.02 (-3.03%)</td><td>0.02 (-12.46%)</td><td>0.01 (+9.08%)</td><td>0.00 (-7.40%)</td><td>194.90 (-8.33%)</td><td>156.90 (+2.27%)</td><td>172.40 (+14.25%)</td><td>110.30 (+5.65%)</td><td>36.04 (-10.73%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>153.42 (n/a)</td><td>150.90 (n/a)</td><td>104.40 (n/a)</td><td>40.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (-17.27%)</td><td>0.01 (-9.27%)</td><td>0.01 (-15.29%)</td><td>0.01 (+9.70%)</td><td>0.00 <b>(-26.71%)</b></td><td>343.70 (-8.83%)</td><td>211.70 (+3.39%)</td><td>201.40 (+18.05%)</td><td>127.40 <b>(+20.87%)</b></td><td>81.36 <b>(-20.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>377.00 (n/a)</td><td>204.76 (n/a)</td><td>170.60 (n/a)</td><td>105.40 (n/a)</td><td>102.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (+5.57%)</td><td>0.02 (+9.20%)</td><td>0.02 (+0.95%)</td><td>0.01 (+9.44%)</td><td>0.00 (+11.09%)</td><td>201.00 (-8.59%)</td><td>167.26 (-8.14%)</td><td>171.70 (-0.92%)</td><td>123.80 (-5.28%)</td><td>35.34 (-2.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>219.90 (n/a)</td><td>182.08 (n/a)</td><td>173.30 (n/a)</td><td>130.70 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 <b>(-20.83%)</b></td><td>0.02 (-5.18%)</td><td>0.01 (+6.22%)</td><td>0.01 (+15.61%)</td><td>0.00 <b>(-67.98%)</b></td><td>197.40 (-13.50%)</td><td>172.76 (-1.09%)</td><td>177.80 (-5.83%)</td><td>152.80 <b>(+26.28%)</b></td><td>18.11 <b>(-63.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>228.20 (n/a)</td><td>174.66 (n/a)</td><td>188.80 (n/a)</td><td>121.00 (n/a)</td><td>50.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (+14.45%)</td><td>0.01 (-2.73%)</td><td>0.01 (-16.54%)</td><td>0.01 (-8.52%)</td><td>0.00 <b>(+57.09%)</b></td><td>243.80 (+9.33%)</td><td>195.96 (+4.96%)</td><td>211.50 (+19.83%)</td><td>142.90 (-12.65%)</td><td>40.32 <b>(+50.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.00 (n/a)</td><td>186.70 (n/a)</td><td>176.50 (n/a)</td><td>163.60 (n/a)</td><td>26.85 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.01 (+4.96%)</td><td>0.01 (+6.95%)</td><td>0.01 (-1.09%)</td><td>0.01 <b>(+42.02%)</b></td><td>0.00 <b>(-51.04%)</b></td><td>220.40 <b>(-29.58%)</b></td><td>203.46 (-9.42%)</td><td>208.50 (+1.12%)</td><td>175.20 (-4.73%)</td><td>17.05 <b>(-67.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>313.00 (n/a)</td><td>224.62 (n/a)</td><td>206.20 (n/a)</td><td>183.90 (n/a)</td><td>53.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (+9.87%)</td><td>0.03 (-0.13%)</td><td>0.03 (-5.91%)</td><td>0.02 (+3.16%)</td><td>0.01 (+16.73%)</td><td>222.50 (-3.09%)</td><td>167.84 (+0.59%)</td><td>164.10 (+6.28%)</td><td>122.90 (-9.03%)</td><td>36.52 (-0.70%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>166.86 (n/a)</td><td>154.40 (n/a)</td><td>135.10 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-6.35%)</td><td>0.04 (-3.74%)</td><td>0.03 <b>(-22.05%)</b></td><td>0.03 (+11.78%)</td><td>0.01 <b>(-27.29%)</b></td><td>168.80 (-10.55%)</td><td>151.06 (+1.89%)</td><td>166.80 <b>(+28.31%)</b></td><td>125.60 (+6.80%)</td><td>22.80 <b>(-32.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>148.26 (n/a)</td><td>130.00 (n/a)</td><td>117.60 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(-28.35%)</b></td><td>0.03 <b>(-23.11%)</b></td><td>0.03 <b>(-25.97%)</b></td><td>0.03 (-17.87%)</td><td>0.00 <b>(-40.95%)</b></td><td>192.10 <b>(+21.74%)</b></td><td>173.56 <b>(+29.25%)</b></td><td>183.50 <b>(+35.13%)</b></td><td>150.00 <b>(+39.53%)</b></td><td>18.50 (+1.71%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>157.80 (n/a)</td><td>134.28 (n/a)</td><td>135.80 (n/a)</td><td>107.50 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(-27.25%)</b></td><td>0.03 (-11.80%)</td><td>0.03 (-8.45%)</td><td>0.02 <b>(+29.52%)</b></td><td>0.00 <b>(-69.74%)</b></td><td>219.50 <b>(-22.77%)</b></td><td>191.06 (+6.07%)</td><td>181.90 (+9.25%)</td><td>174.00 <b>(+37.44%)</b></td><td>18.77 <b>(-69.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>284.20 (n/a)</td><td>180.12 (n/a)</td><td>166.50 (n/a)</td><td>126.60 (n/a)</td><td>61.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (+0.08%)</td><td>0.03 (-10.18%)</td><td>0.03 (-17.06%)</td><td>0.03 (-3.04%)</td><td>0.01 (+0.15%)</td><td>194.80 (+3.12%)</td><td>167.08 (+11.31%)</td><td>168.90 <b>(+20.56%)</b></td><td>128.40 (-0.08%)</td><td>24.83 (+0.51%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>150.10 (n/a)</td><td>140.10 (n/a)</td><td>128.50 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-8.27%)</td><td>0.03 (-6.74%)</td><td>0.03 (+7.56%)</td><td>0.02 <b>(-36.49%)</b></td><td>0.01 <b>(+90.12%)</b></td><td>298.00 <b>(+57.51%)</b></td><td>185.44 (+13.71%)</td><td>153.40 (-7.03%)</td><td>148.00 (+9.06%)</td><td>63.98 <b>(+236.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>163.08 (n/a)</td><td>165.00 (n/a)</td><td>135.70 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+4.00%)</td><td>0.03 (-1.31%)</td><td>0.03 (-6.43%)</td><td>0.02 (-10.21%)</td><td>0.00 <b>(+146.54%)</b></td><td>215.00 (+11.34%)</td><td>186.80 (+2.18%)</td><td>193.40 (+6.85%)</td><td>165.40 (-3.84%)</td><td>20.99 <b>(+157.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>182.82 (n/a)</td><td>181.00 (n/a)</td><td>172.00 (n/a)</td><td>8.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(-21.62%)</b></td><td>0.02 (-18.19%)</td><td>0.03 (+1.71%)</td><td>0.02 <b>(-36.66%)</b></td><td>0.00 (-9.98%)</td><td>345.20 <b>(+57.91%)</b></td><td>236.92 <b>(+24.41%)</b></td><td>204.50 (-1.64%)</td><td>195.10 <b>(+27.60%)</b></td><td>62.83 <b>(+85.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>190.44 (n/a)</td><td>207.90 (n/a)</td><td>152.90 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (-3.12%)</td><td>0.07 (-2.19%)</td><td>0.07 (-5.72%)</td><td>0.06 (+8.49%)</td><td>0.01 <b>(-29.68%)</b></td><td>185.90 (-7.83%)</td><td>160.30 (+0.31%)</td><td>156.00 (+6.05%)</td><td>130.20 (+3.25%)</td><td>23.18 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>159.80 (n/a)</td><td>147.10 (n/a)</td><td>126.10 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (-3.42%)</td><td>0.06 (+7.15%)</td><td>0.06 (+5.71%)</td><td>0.05 <b>(+29.26%)</b></td><td>0.00 <b>(-54.19%)</b></td><td>190.90 <b>(-22.65%)</b></td><td>169.28 (-8.65%)</td><td>167.40 (-5.37%)</td><td>158.40 (+3.53%)</td><td>12.74 <b>(-64.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>246.80 (n/a)</td><td>185.30 (n/a)</td><td>176.90 (n/a)</td><td>153.00 (n/a)</td><td>35.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 <b>(-22.75%)</b></td><td>0.06 (-9.02%)</td><td>0.06 (-6.98%)</td><td>0.04 (-2.61%)</td><td>0.01 <b>(-39.90%)</b></td><td>237.30 (+2.68%)</td><td>181.18 (+7.58%)</td><td>165.30 (+7.55%)</td><td>161.50 <b>(+29.41%)</b></td><td>32.00 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>168.42 (n/a)</td><td>153.70 (n/a)</td><td>124.80 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (+6.89%)</td><td>0.06 (+0.96%)</td><td>0.06 (-4.98%)</td><td>0.05 (-1.97%)</td><td>0.01 <b>(+55.37%)</b></td><td>205.80 (+2.03%)</td><td>169.88 (+0.45%)</td><td>178.10 (+5.26%)</td><td>136.30 (-6.45%)</td><td>29.73 <b>(+43.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>169.12 (n/a)</td><td>169.20 (n/a)</td><td>145.70 (n/a)</td><td>20.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+9.34%)</td><td>0.06 (-3.06%)</td><td>0.05 <b>(-25.99%)</b></td><td>0.05 (+15.93%)</td><td>0.01 (+11.03%)</td><td>231.00 (-13.74%)</td><td>192.10 (+3.05%)</td><td>216.20 <b>(+35.12%)</b></td><td>141.00 (-8.56%)</td><td>41.83 (-12.76%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>267.80 (n/a)</td><td>186.42 (n/a)</td><td>160.00 (n/a)</td><td>154.20 (n/a)</td><td>47.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (+0.65%)</td><td>0.05 (-10.47%)</td><td>0.05 (-14.67%)</td><td>0.03 (-18.80%)</td><td>0.02 <b>(+25.39%)</b></td><td>338.40 <b>(+23.19%)</b></td><td>223.90 (+16.55%)</td><td>218.60 (+17.21%)</td><td>132.40 (-0.68%)</td><td>76.64 <b>(+49.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>274.70 (n/a)</td><td>192.10 (n/a)</td><td>186.50 (n/a)</td><td>133.30 (n/a)</td><td>51.31 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+2.75%)</td><td>0.06 (+8.11%)</td><td>0.06 (+11.01%)</td><td>0.05 (+3.21%)</td><td>0.01 (+0.07%)</td><td>193.40 (-3.11%)</td><td>170.46 (-7.55%)</td><td>174.40 (-9.92%)</td><td>144.80 (-2.69%)</td><td>19.63 (-4.38%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>184.38 (n/a)</td><td>193.60 (n/a)</td><td>148.80 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-17.07%)</td><td>0.05 (-9.65%)</td><td>0.05 (+0.10%)</td><td>0.04 (-14.58%)</td><td>0.00 <b>(-23.26%)</b></td><td>274.30 (+17.07%)</td><td>232.74 (+10.45%)</td><td>220.20 (-0.09%)</td><td>212.70 <b>(+20.58%)</b></td><td>26.45 (+7.14%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>210.72 (n/a)</td><td>220.40 (n/a)</td><td>176.40 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (+12.71%)</td><td>0.13 (+8.61%)</td><td>0.13 (+6.32%)</td><td>0.11 (+3.92%)</td><td>0.02 <b>(+46.61%)</b></td><td>193.40 (-3.78%)</td><td>161.64 (-6.99%)</td><td>159.90 (-5.94%)</td><td>129.60 (-11.23%)</td><td>26.78 <b>(+25.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>201.00 (n/a)</td><td>173.78 (n/a)</td><td>170.00 (n/a)</td><td>146.00 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (-1.54%)</td><td>0.13 (+16.95%)</td><td>0.13 (+19.20%)</td><td>0.12 <b>(+51.32%)</b></td><td>0.01 <b>(-65.30%)</b></td><td>180.80 <b>(-33.92%)</b></td><td>166.78 (-17.40%)</td><td>165.20 (-16.14%)</td><td>152.50 (+1.53%)</td><td>10.38 <b>(-77.10%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>273.60 (n/a)</td><td>201.92 (n/a)</td><td>197.00 (n/a)</td><td>150.20 (n/a)</td><td>45.31 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-3.41%)</td><td>0.13 (+0.25%)</td><td>0.13 (-1.08%)</td><td>0.12 (+16.60%)</td><td>0.01 <b>(-47.46%)</b></td><td>181.40 (-14.23%)</td><td>160.32 (-2.11%)</td><td>160.70 (+1.07%)</td><td>141.30 (+3.52%)</td><td>14.29 <b>(-52.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.50 (n/a)</td><td>163.78 (n/a)</td><td>159.00 (n/a)</td><td>136.50 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-19.19%)</td><td>0.11 (-15.62%)</td><td>0.10 (-17.28%)</td><td>0.10 (-7.65%)</td><td>0.02 <b>(-31.73%)</b></td><td>206.10 (+8.30%)</td><td>190.34 (+16.82%)</td><td>202.50 <b>(+20.90%)</b></td><td>137.70 <b>(+23.72%)</b></td><td>29.48 (-9.26%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>190.30 (n/a)</td><td>162.94 (n/a)</td><td>167.50 (n/a)</td><td>111.30 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+6.77%)</td><td>0.12 (+14.23%)</td><td>0.13 (+16.67%)</td><td>0.10 (+8.87%)</td><td>0.02 (-9.56%)</td><td>218.10 (-8.13%)</td><td>172.44 (-13.08%)</td><td>163.60 (-14.26%)</td><td>151.70 (-6.36%)</td><td>26.94 <b>(-22.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>237.40 (n/a)</td><td>198.38 (n/a)</td><td>190.80 (n/a)</td><td>162.00 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (-10.95%)</td><td>0.11 (-9.91%)</td><td>0.11 (-12.22%)</td><td>0.08 (+1.84%)</td><td>0.02 <b>(-30.42%)</b></td><td>255.80 (-1.80%)</td><td>194.08 (+8.36%)</td><td>184.00 (+13.93%)</td><td>154.70 (+12.35%)</td><td>39.04 <b>(-22.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>260.50 (n/a)</td><td>179.10 (n/a)</td><td>161.50 (n/a)</td><td>137.70 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 <b>(+30.26%)</b></td><td>0.12 (+8.18%)</td><td>0.12 (+10.41%)</td><td>0.07 (-7.13%)</td><td>0.04 <b>(+68.28%)</b></td><td>287.70 (+7.71%)</td><td>192.68 (-3.46%)</td><td>178.60 (-9.43%)</td><td>122.90 <b>(-23.24%)</b></td><td>61.37 <b>(+42.53%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>267.10 (n/a)</td><td>199.58 (n/a)</td><td>197.20 (n/a)</td><td>160.10 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+28.33%)</b></td><td>0.11 (+15.56%)</td><td>0.11 (+16.68%)</td><td>0.08 (+4.78%)</td><td>0.02 <b>(+160.06%)</b></td><td>250.80 (-4.57%)</td><td>199.64 (-11.14%)</td><td>186.20 (-14.27%)</td><td>161.10 <b>(-22.06%)</b></td><td>41.35 <b>(+88.57%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>262.80 (n/a)</td><td>224.68 (n/a)</td><td>217.20 (n/a)</td><td>206.70 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>161.72 (n/a)</td><td>153.50 (n/a)</td><td>129.70 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>161.66 (n/a)</td><td>153.10 (n/a)</td><td>121.70 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.50 (n/a)</td><td>165.44 (n/a)</td><td>158.10 (n/a)</td><td>132.30 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>179.92 (n/a)</td><td>189.30 (n/a)</td><td>138.50 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>175.52 (n/a)</td><td>194.40 (n/a)</td><td>127.80 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>171.02 (n/a)</td><td>177.10 (n/a)</td><td>139.10 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>172.16 (n/a)</td><td>157.90 (n/a)</td><td>144.70 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.70 (n/a)</td><td>189.54 (n/a)</td><td>179.00 (n/a)</td><td>172.20 (n/a)</td><td>23.22 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>166.70 (n/a)</td><td>159.70 (n/a)</td><td>143.40 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>238.20 (n/a)</td><td>188.54 (n/a)</td><td>176.50 (n/a)</td><td>157.70 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>237.90 (n/a)</td><td>189.58 (n/a)</td><td>190.30 (n/a)</td><td>148.90 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>205.20 (n/a)</td><td>181.26 (n/a)</td><td>182.40 (n/a)</td><td>152.70 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.29 (+10.93%)</td><td>0.25 (+9.03%)</td><td>0.28 <b>(+25.02%)</b></td><td>0.14 <b>(-33.78%)</b></td><td>0.06 <b>(+200.32%)</b></td><td>343.50 <b>(+50.99%)</b></td><td>209.44 (-1.98%)</td><td>178.50 <b>(-20.03%)</b></td><td>167.70 (-9.84%)</td><td>75.10 <b>(+323.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>227.50 (n/a)</td><td>213.68 (n/a)</td><td>223.20 (n/a)</td><td>186.00 (n/a)</td><td>17.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>205.50 (n/a)</td><td>172.58 (n/a)</td><td>184.90 (n/a)</td><td>139.00 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>189.20 (n/a)</td><td>151.90 (n/a)</td><td>145.80 (n/a)</td><td>121.50 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>305.70 (n/a)</td><td>205.94 (n/a)</td><td>182.80 (n/a)</td><td>146.60 (n/a)</td><td>61.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.20 (n/a)</td><td>171.38 (n/a)</td><td>170.40 (n/a)</td><td>152.90 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>197.38 (n/a)</td><td>208.20 (n/a)</td><td>152.70 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>282.00 (n/a)</td><td>181.16 (n/a)</td><td>163.60 (n/a)</td><td>126.10 (n/a)</td><td>59.47 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.50 (n/a)</td><td>195.00 (n/a)</td><td>199.40 (n/a)</td><td>149.30 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>161.22 (n/a)</td><td>160.20 (n/a)</td><td>132.50 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>181.00 (n/a)</td><td>172.40 (n/a)</td><td>136.50 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>198.58 (n/a)</td><td>209.10 (n/a)</td><td>139.10 (n/a)</td><td>40.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>330.70 (n/a)</td><td>241.20 (n/a)</td><td>230.90 (n/a)</td><td>194.40 (n/a)</td><td>54.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.10 (n/a)</td><td>178.06 (n/a)</td><td>178.50 (n/a)</td><td>140.40 (n/a)</td><td>24.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>237.50 (n/a)</td><td>185.22 (n/a)</td><td>172.40 (n/a)</td><td>155.20 (n/a)</td><td>34.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>197.38 (n/a)</td><td>190.80 (n/a)</td><td>174.40 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>264.10 (n/a)</td><td>225.94 (n/a)</td><td>240.90 (n/a)</td><td>159.20 (n/a)</td><td>40.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>235.40 (n/a)</td><td>193.86 (n/a)</td><td>209.60 (n/a)</td><td>141.80 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>237.90 (n/a)</td><td>198.48 (n/a)</td><td>187.30 (n/a)</td><td>150.60 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>203.80 (n/a)</td><td>183.50 (n/a)</td><td>185.50 (n/a)</td><td>148.10 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>350.10 (n/a)</td><td>197.92 (n/a)</td><td>184.70 (n/a)</td><td>122.40 (n/a)</td><td>89.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>167.72 (n/a)</td><td>171.00 (n/a)</td><td>131.20 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>156.78 (n/a)</td><td>165.40 (n/a)</td><td>126.00 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>174.54 (n/a)</td><td>188.10 (n/a)</td><td>123.10 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>166.06 (n/a)</td><td>166.40 (n/a)</td><td>147.80 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.40 (n/a)</td><td>182.82 (n/a)</td><td>168.60 (n/a)</td><td>149.10 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>173.82 (n/a)</td><td>186.80 (n/a)</td><td>131.30 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.60 (n/a)</td><td>195.66 (n/a)</td><td>188.10 (n/a)</td><td>148.20 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>154.06 (n/a)</td><td>144.40 (n/a)</td><td>118.60 (n/a)</td><td>36.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>158.28 (n/a)</td><td>150.40 (n/a)</td><td>128.60 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>150.32 (n/a)</td><td>145.40 (n/a)</td><td>119.40 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>166.14 (n/a)</td><td>168.60 (n/a)</td><td>125.10 (n/a)</td><td>25.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.60 (n/a)</td><td>155.26 (n/a)</td><td>154.30 (n/a)</td><td>132.10 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>173.24 (n/a)</td><td>171.10 (n/a)</td><td>128.20 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>177.36 (n/a)</td><td>171.70 (n/a)</td><td>165.60 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>188.22 (n/a)</td><td>198.50 (n/a)</td><td>154.90 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>164.10 (n/a)</td><td>151.30 (n/a)</td><td>124.60 (n/a)</td><td>43.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>151.38 (n/a)</td><td>147.00 (n/a)</td><td>130.80 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.90 (n/a)</td><td>166.02 (n/a)</td><td>169.40 (n/a)</td><td>132.90 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>261.00 (n/a)</td><td>170.28 (n/a)</td><td>148.30 (n/a)</td><td>123.80 (n/a)</td><td>53.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.40 (n/a)</td><td>162.50 (n/a)</td><td>171.80 (n/a)</td><td>119.60 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>173.34 (n/a)</td><td>166.90 (n/a)</td><td>138.80 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>173.08 (n/a)</td><td>176.50 (n/a)</td><td>155.60 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>266.40 (n/a)</td><td>219.22 (n/a)</td><td>220.90 (n/a)</td><td>178.40 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>207.40 (n/a)</td><td>170.58 (n/a)</td><td>174.30 (n/a)</td><td>131.40 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>178.90 (n/a)</td><td>161.52 (n/a)</td><td>161.50 (n/a)</td><td>139.10 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.80 (n/a)</td><td>170.26 (n/a)</td><td>161.00 (n/a)</td><td>151.10 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.00 (n/a)</td><td>163.50 (n/a)</td><td>166.20 (n/a)</td><td>141.90 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.20 (n/a)</td><td>193.72 (n/a)</td><td>200.00 (n/a)</td><td>154.70 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.90 (n/a)</td><td>197.28 (n/a)</td><td>188.60 (n/a)</td><td>155.10 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>253.30 (n/a)</td><td>201.90 (n/a)</td><td>194.90 (n/a)</td><td>163.40 (n/a)</td><td>35.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>4.31 (-12.82%)</td><td>4.04 (-8.90%)</td><td>4.06 (-2.73%)</td><td>3.74 (-7.64%)</td><td>0.21 <b>(-52.41%)</b></td><td>2516.20 (+8.27%)</td><td>2332.68 (+9.20%)</td><td>2313.70 (+2.81%)</td><td>2180.70 (+14.71%)</td><td>120.21 <b>(-40.18%)</b></td><td>1696.41 (-12.82%)</td><td>1589.20 (-8.90%)</td><td>1598.88 (-2.73%)</td><td>1470.25 (-7.64%)</td><td>80.64 <b>(-52.41%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>4.95 (n/a)</td><td>4.43 (n/a)</td><td>4.18 (n/a)</td><td>4.05 (n/a)</td><td>0.43 (n/a)</td><td>2324.00 (n/a)</td><td>2136.18 (n/a)</td><td>2250.50 (n/a)</td><td>1901.10 (n/a)</td><td>200.96 (n/a)</td><td>1945.91 (n/a)</td><td>1744.51 (n/a)</td><td>1643.80 (n/a)</td><td>1591.80 (n/a)</td><td>169.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.05 (-11.55%)</td><td>0.93 (-13.36%)</td><td>1.01 (-2.63%)</td><td>0.68 <b>(-29.71%)</b></td><td>0.16 <b>(+61.14%)</b></td><td>327.10 <b>(+42.28%)</b></td><td>245.76 (+17.93%)</td><td>218.40 (+2.68%)</td><td>211.00 (+13.02%)</td><td>49.71 <b>(+158.87%)</b></td><td>44.72 (-11.55%)</td><td>39.51 (-13.36%)</td><td>43.21 (-2.63%)</td><td>28.85 <b>(-29.71%)</b></td><td>6.87 <b>(+61.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.18 (n/a)</td><td>1.07 (n/a)</td><td>1.04 (n/a)</td><td>0.96 (n/a)</td><td>0.10 (n/a)</td><td>229.90 (n/a)</td><td>208.40 (n/a)</td><td>212.70 (n/a)</td><td>186.70 (n/a)</td><td>19.20 (n/a)</td><td>50.56 (n/a)</td><td>45.60 (n/a)</td><td>44.38 (n/a)</td><td>41.05 (n/a)</td><td>4.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.18 (-3.42%)</td><td>1.05 (-7.69%)</td><td>1.03 (-9.93%)</td><td>0.88 (-13.83%)</td><td>0.11 <b>(+44.48%)</b></td><td>250.00 (+16.06%)</td><td>213.64 (+8.94%)</td><td>214.80 (+11.01%)</td><td>187.00 (+3.54%)</td><td>23.68 <b>(+74.63%)</b></td><td>50.48 (-3.42%)</td><td>44.59 (-7.69%)</td><td>43.94 (-9.93%)</td><td>37.75 (-13.83%)</td><td>4.75 <b>(+44.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.22 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.03 (n/a)</td><td>0.08 (n/a)</td><td>215.40 (n/a)</td><td>196.10 (n/a)</td><td>193.50 (n/a)</td><td>180.60 (n/a)</td><td>13.56 (n/a)</td><td>52.27 (n/a)</td><td>48.31 (n/a)</td><td>48.78 (n/a)</td><td>43.80 (n/a)</td><td>3.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.52 (+0.05%)</td><td>0.52 (-0.00%)</td><td>0.52 (+0.00%)</td><td>0.52 (-0.04%)</td><td>0.00 <b>(+56.12%)</b></td><td>48759.80 (+0.04%)</td><td>48679.28 (+0.00%)</td><td>48651.10 (-0.00%)</td><td>48620.40 (-0.05%)</td><td>65.94 <b>(+56.09%)</b></td><td>353.35 (+0.05%)</td><td>352.92 (-0.00%)</td><td>353.12 (+0.00%)</td><td>352.34 (-0.04%)</td><td>0.48 <b>(+56.12%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48738.20 (n/a)</td><td>48677.34 (n/a)</td><td>48653.50 (n/a)</td><td>48643.00 (n/a)</td><td>42.24 (n/a)</td><td>353.18 (n/a)</td><td>352.93 (n/a)</td><td>353.11 (n/a)</td><td>352.49 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (-0.20%)</td><td>0.21 (-0.16%)</td><td>0.21 (+0.05%)</td><td>0.21 (-0.10%)</td><td>0.00 <b>(-22.68%)</b></td><td>119161.50 (+0.10%)</td><td>118350.20 (+0.15%)</td><td>118387.10 (-0.05%)</td><td>117411.90 (+0.20%)</td><td>650.06 <b>(-22.42%)</b></td><td>146.32 (-0.20%)</td><td>145.16 (-0.16%)</td><td>145.12 (+0.05%)</td><td>144.17 (-0.10%)</td><td>0.80 <b>(-22.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119043.80 (n/a)</td><td>118167.18 (n/a)</td><td>118441.00 (n/a)</td><td>117179.00 (n/a)</td><td>837.97 (n/a)</td><td>146.61 (n/a)</td><td>145.39 (n/a)</td><td>145.05 (n/a)</td><td>144.32 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.90 (+0.33%)</td><td>0.89 (+0.36%)</td><td>0.89 (+0.97%)</td><td>0.88 (-0.26%)</td><td>0.01 <b>(+31.90%)</b></td><td>28583.00 (+0.26%)</td><td>28259.88 (-0.35%)</td><td>28191.70 (-0.96%)</td><td>27987.90 (-0.33%)</td><td>240.56 <b>(+31.84%)</b></td><td>613.83 (+0.33%)</td><td>607.96 (+0.36%)</td><td>609.39 (+0.97%)</td><td>601.05 (-0.26%)</td><td>5.16 <b>(+31.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28508.30 (n/a)</td><td>28359.82 (n/a)</td><td>28464.80 (n/a)</td><td>28079.40 (n/a)</td><td>182.46 (n/a)</td><td>611.83 (n/a)</td><td>605.80 (n/a)</td><td>603.55 (n/a)</td><td>602.63 (n/a)</td><td>3.91 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.51 (-1.26%)</td><td>3.43 (-2.59%)</td><td>3.50 (-0.90%)</td><td>3.32 (-5.07%)</td><td>0.09 <b>(+355.85%)</b></td><td>7588.50 (+5.34%)</td><td>7334.38 (+2.72%)</td><td>7199.10 (+0.91%)</td><td>7175.90 (+1.27%)</td><td>204.95 <b>(+385.12%)</b></td><td>2394.10 (-1.26%)</td><td>2343.82 (-2.59%)</td><td>2386.40 (-0.90%)</td><td>2263.93 (-5.07%)</td><td>64.79 <b>(+355.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.55 (n/a)</td><td>3.52 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>0.02 (n/a)</td><td>7203.80 (n/a)</td><td>7140.12 (n/a)</td><td>7134.20 (n/a)</td><td>7085.80 (n/a)</td><td>42.25 (n/a)</td><td>2424.54 (n/a)</td><td>2406.17 (n/a)</td><td>2408.08 (n/a)</td><td>2384.82 (n/a)</td><td>14.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.16 (+10.62%)</td><td>2.84 (+1.30%)</td><td>2.80 (-0.67%)</td><td>2.67 (-1.34%)</td><td>0.19 <b>(+219.93%)</b></td><td>9428.90 (+1.36%)</td><td>8897.32 (-0.99%)</td><td>8983.20 (+0.67%)</td><td>7974.30 (-9.60%)</td><td>564.61 <b>(+190.27%)</b></td><td>2154.39 (+10.62%)</td><td>1937.50 (+1.30%)</td><td>1912.45 (-0.67%)</td><td>1822.04 (-1.34%)</td><td>130.13 <b>(+219.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>2.85 (n/a)</td><td>2.80 (n/a)</td><td>2.82 (n/a)</td><td>2.71 (n/a)</td><td>0.06 (n/a)</td><td>9302.30 (n/a)</td><td>8985.84 (n/a)</td><td>8923.40 (n/a)</td><td>8821.10 (n/a)</td><td>194.51 (n/a)</td><td>1947.58 (n/a)</td><td>1912.58 (n/a)</td><td>1925.25 (n/a)</td><td>1846.84 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.34 (-3.26%)</td><td>3.26 (-1.12%)</td><td>3.24 (-0.67%)</td><td>3.15 (-1.75%)</td><td>0.08 <b>(-21.24%)</b></td><td>7980.90 (+1.78%)</td><td>7732.38 (+1.10%)</td><td>7761.90 (+0.68%)</td><td>7533.80 (+3.37%)</td><td>186.55 (-17.36%)</td><td>2280.36 (-3.26%)</td><td>2222.84 (-1.12%)</td><td>2213.37 (-0.67%)</td><td>2152.63 (-1.75%)</td><td>53.48 <b>(-21.24%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.45 (n/a)</td><td>3.29 (n/a)</td><td>3.26 (n/a)</td><td>3.21 (n/a)</td><td>0.10 (n/a)</td><td>7841.10 (n/a)</td><td>7648.06 (n/a)</td><td>7709.60 (n/a)</td><td>7288.40 (n/a)</td><td>225.73 (n/a)</td><td>2357.17 (n/a)</td><td>2247.91 (n/a)</td><td>2228.37 (n/a)</td><td>2190.99 (n/a)</td><td>67.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.78 (-0.00%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.04%)</td><td>0.00 <b>(+254.32%)</b></td><td>96492.70 (+0.04%)</td><td>96466.54 (+0.02%)</td><td>96459.50 (+0.01%)</td><td>96443.60 (+0.00%)</td><td>20.39 <b>(+253.92%)</b></td><td>712.54 (-0.00%)</td><td>712.37 (-0.02%)</td><td>712.42 (-0.01%)</td><td>712.17 (-0.04%)</td><td>0.15 <b>(+254.38%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96452.20 (n/a)</td><td>96445.02 (n/a)</td><td>96447.10 (n/a)</td><td>96438.90 (n/a)</td><td>5.76 (n/a)</td><td>712.57 (n/a)</td><td>712.52 (n/a)</td><td>712.51 (n/a)</td><td>712.47 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.73 (+0.38%)</td><td>0.73 (+0.06%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.09%)</td><td>0.00 <b>(+567.14%)</b></td><td>103793.10 (+0.09%)</td><td>103586.80 (-0.06%)</td><td>103632.00 (-0.01%)</td><td>103240.70 (-0.38%)</td><td>205.49 <b>(+565.16%)</b></td><td>665.62 (+0.38%)</td><td>663.40 (+0.06%)</td><td>663.11 (+0.01%)</td><td>662.08 (-0.09%)</td><td>1.32 <b>(+567.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103702.10 (n/a)</td><td>103653.74 (n/a)</td><td>103638.20 (n/a)</td><td>103630.50 (n/a)</td><td>30.89 (n/a)</td><td>663.12 (n/a)</td><td>662.97 (n/a)</td><td>663.07 (n/a)</td><td>662.66 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.70 (+0.75%)</td><td>0.70 (+0.22%)</td><td>0.69 (+0.01%)</td><td>0.69 (+0.15%)</td><td>0.00 <b>(+134.15%)</b></td><td>108928.70 (-0.15%)</td><td>108550.08 (-0.22%)</td><td>108713.80 (-0.01%)</td><td>107770.90 (-0.74%)</td><td>475.02 <b>(+132.04%)</b></td><td>637.64 (+0.75%)</td><td>633.08 (+0.22%)</td><td>632.11 (+0.01%)</td><td>630.87 (+0.15%)</td><td>2.78 <b>(+134.15%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109089.50 (n/a)</td><td>108784.50 (n/a)</td><td>108722.90 (n/a)</td><td>108575.80 (n/a)</td><td>204.72 (n/a)</td><td>632.92 (n/a)</td><td>631.70 (n/a)</td><td>632.06 (n/a)</td><td>629.94 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.49 (+0.16%)</td><td>6.98 (-0.54%)</td><td>6.92 (-0.53%)</td><td>6.35 (-5.75%)</td><td>0.46 <b>(+51.90%)</b></td><td>1404.00 (+6.10%)</td><td>1281.34 (+0.75%)</td><td>1287.90 (+0.53%)</td><td>1190.60 (-0.16%)</td><td>85.99 <b>(+59.77%)</b></td><td>450.94 (+0.16%)</td><td>420.48 (-0.54%)</td><td>416.85 (-0.53%)</td><td>382.37 (-5.75%)</td><td>27.77 <b>(+51.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.47 (n/a)</td><td>7.02 (n/a)</td><td>6.96 (n/a)</td><td>6.74 (n/a)</td><td>0.30 (n/a)</td><td>1323.30 (n/a)</td><td>1271.80 (n/a)</td><td>1281.10 (n/a)</td><td>1192.50 (n/a)</td><td>53.82 (n/a)</td><td>450.22 (n/a)</td><td>422.76 (n/a)</td><td>419.08 (n/a)</td><td>405.70 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.97 (+2.84%)</td><td>6.43 (+2.17%)</td><td>6.78 (+2.56%)</td><td>5.07 (+5.88%)</td><td>0.79 (-6.66%)</td><td>1756.50 (-5.55%)</td><td>1405.22 (-2.47%)</td><td>1314.10 (-2.50%)</td><td>1278.40 (-2.76%)</td><td>201.29 (-14.41%)</td><td>419.95 (+2.84%)</td><td>387.50 (+2.17%)</td><td>408.53 (+2.56%)</td><td>305.65 (+5.88%)</td><td>47.65 (-6.66%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.78 (n/a)</td><td>6.30 (n/a)</td><td>6.61 (n/a)</td><td>4.79 (n/a)</td><td>0.85 (n/a)</td><td>1859.80 (n/a)</td><td>1440.84 (n/a)</td><td>1347.80 (n/a)</td><td>1314.70 (n/a)</td><td>235.19 (n/a)</td><td>408.36 (n/a)</td><td>379.28 (n/a)</td><td>398.33 (n/a)</td><td>288.67 (n/a)</td><td>51.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.45 (-5.52%)</td><td>5.94 (-7.44%)</td><td>6.17 (-2.43%)</td><td>4.85 <b>(-20.96%)</b></td><td>0.63 <b>(+104.16%)</b></td><td>1837.70 <b>(+26.51%)</b></td><td>1516.32 (+8.95%)</td><td>1445.00 (+2.50%)</td><td>1382.60 (+5.85%)</td><td>182.74 <b>(+179.01%)</b></td><td>388.32 (-5.52%)</td><td>357.69 (-7.44%)</td><td>371.55 (-2.43%)</td><td>292.14 <b>(-20.96%)</b></td><td>37.70 <b>(+104.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.82 (n/a)</td><td>6.42 (n/a)</td><td>6.32 (n/a)</td><td>6.14 (n/a)</td><td>0.31 (n/a)</td><td>1452.60 (n/a)</td><td>1391.76 (n/a)</td><td>1409.80 (n/a)</td><td>1306.20 (n/a)</td><td>65.50 (n/a)</td><td>411.01 (n/a)</td><td>386.44 (n/a)</td><td>380.80 (n/a)</td><td>369.59 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.45 (+0.77%)</td><td>7.76 (-0.30%)</td><td>7.84 (-2.13%)</td><td>7.17 (+1.66%)</td><td>0.53 (-1.81%)</td><td>4860.70 (-1.64%)</td><td>4511.80 (+0.28%)</td><td>4444.30 (+2.17%)</td><td>4125.40 (-0.76%)</td><td>310.34 (-3.71%)</td><td>520.55 (+0.77%)</td><td>477.78 (-0.30%)</td><td>483.20 (-2.13%)</td><td>441.80 (+1.66%)</td><td>32.94 (-1.81%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.39 (n/a)</td><td>7.78 (n/a)</td><td>8.02 (n/a)</td><td>7.06 (n/a)</td><td>0.54 (n/a)</td><td>4941.50 (n/a)</td><td>4499.26 (n/a)</td><td>4349.70 (n/a)</td><td>4157.10 (n/a)</td><td>322.31 (n/a)</td><td>516.59 (n/a)</td><td>479.22 (n/a)</td><td>493.71 (n/a)</td><td>434.58 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.98 (+2.71%)</td><td>7.58 (+1.22%)</td><td>7.61 (+0.86%)</td><td>6.86 (-3.65%)</td><td>0.44 <b>(+72.64%)</b></td><td>5081.00 (+3.79%)</td><td>4612.26 (-1.02%)</td><td>4580.90 (-0.85%)</td><td>4369.50 (-2.64%)</td><td>280.26 <b>(+75.38%)</b></td><td>491.47 (+2.71%)</td><td>466.91 (+1.22%)</td><td>468.79 (+0.86%)</td><td>422.65 (-3.65%)</td><td>26.92 <b>(+72.64%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.77 (n/a)</td><td>7.49 (n/a)</td><td>7.55 (n/a)</td><td>7.12 (n/a)</td><td>0.25 (n/a)</td><td>4895.50 (n/a)</td><td>4659.76 (n/a)</td><td>4620.20 (n/a)</td><td>4487.90 (n/a)</td><td>159.80 (n/a)</td><td>478.51 (n/a)</td><td>461.29 (n/a)</td><td>464.80 (n/a)</td><td>438.67 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.53 (+1.81%)</td><td>7.32 (+1.81%)</td><td>7.39 (+1.11%)</td><td>6.83 (+0.29%)</td><td>0.28 (+13.60%)</td><td>5104.50 (-0.29%)</td><td>4771.02 (-1.75%)</td><td>4718.90 (-1.10%)</td><td>4628.10 (-1.78%)</td><td>191.37 (+12.09%)</td><td>464.01 (+1.81%)</td><td>450.67 (+1.81%)</td><td>455.08 (+1.11%)</td><td>420.70 (+0.29%)</td><td>17.28 (+13.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.40 (n/a)</td><td>7.19 (n/a)</td><td>7.31 (n/a)</td><td>6.81 (n/a)</td><td>0.25 (n/a)</td><td>5119.10 (n/a)</td><td>4856.04 (n/a)</td><td>4771.30 (n/a)</td><td>4711.80 (n/a)</td><td>170.72 (n/a)</td><td>455.77 (n/a)</td><td>442.66 (n/a)</td><td>450.08 (n/a)</td><td>419.50 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.79 (+0.02%)</td><td>0.79 (+0.04%)</td><td>0.79 (+0.09%)</td><td>0.79 (+0.01%)</td><td>0.00 (+4.59%)</td><td>95902.10 (-0.01%)</td><td>95765.88 (-0.04%)</td><td>95740.70 (-0.09%)</td><td>95707.20 (-0.02%)</td><td>77.87 (+4.57%)</td><td>718.02 (+0.02%)</td><td>717.58 (+0.04%)</td><td>717.77 (+0.09%)</td><td>716.56 (+0.01%)</td><td>0.58 (+4.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95913.00 (n/a)</td><td>95808.18 (n/a)</td><td>95826.00 (n/a)</td><td>95730.70 (n/a)</td><td>74.47 (n/a)</td><td>717.84 (n/a)</td><td>717.26 (n/a)</td><td>717.13 (n/a)</td><td>716.48 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.73 (+0.01%)</td><td>0.73 (+0.02%)</td><td>0.73 (+0.01%)</td><td>0.73 (+0.06%)</td><td>0.00 <b>(-39.84%)</b></td><td>102942.40 (-0.06%)</td><td>102914.40 (-0.02%)</td><td>102918.50 (-0.01%)</td><td>102884.80 (-0.01%)</td><td>25.67 <b>(-39.83%)</b></td><td>667.93 (+0.01%)</td><td>667.73 (+0.02%)</td><td>667.71 (+0.01%)</td><td>667.55 (+0.06%)</td><td>0.17 <b>(-39.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103008.10 (n/a)</td><td>102937.40 (n/a)</td><td>102932.80 (n/a)</td><td>102893.70 (n/a)</td><td>42.66 (n/a)</td><td>667.87 (n/a)</td><td>667.59 (n/a)</td><td>667.61 (n/a)</td><td>667.13 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.70 (-0.15%)</td><td>0.70 (-0.02%)</td><td>0.70 (-0.04%)</td><td>0.70 (+0.17%)</td><td>0.00 <b>(-54.88%)</b></td><td>107990.30 (-0.17%)</td><td>107843.24 (+0.02%)</td><td>107855.00 (+0.04%)</td><td>107695.50 (+0.15%)</td><td>109.00 <b>(-54.90%)</b></td><td>638.09 (-0.15%)</td><td>637.22 (-0.02%)</td><td>637.15 (-0.04%)</td><td>636.35 (+0.17%)</td><td>0.64 <b>(-54.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108174.70 (n/a)</td><td>107823.26 (n/a)</td><td>107809.90 (n/a)</td><td>107539.10 (n/a)</td><td>241.71 (n/a)</td><td>639.02 (n/a)</td><td>637.34 (n/a)</td><td>637.41 (n/a)</td><td>635.26 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>4.08 (-3.60%)</td><td>3.65 (+1.56%)</td><td>3.65 (-1.60%)</td><td>3.25 (+10.08%)</td><td>0.29 <b>(-51.58%)</b></td><td>2477.20 (-9.16%)</td><td>2217.42 (-3.31%)</td><td>2210.60 (+1.63%)</td><td>1977.40 (+3.74%)</td><td>177.40 <b>(-55.09%)</b></td><td>1069.06 (-3.60%)</td><td>958.22 (+1.56%)</td><td>956.28 (-1.60%)</td><td>853.35 (+10.08%)</td><td>76.51 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>4.23 (n/a)</td><td>3.60 (n/a)</td><td>3.71 (n/a)</td><td>2.96 (n/a)</td><td>0.60 (n/a)</td><td>2727.00 (n/a)</td><td>2293.30 (n/a)</td><td>2175.20 (n/a)</td><td>1906.20 (n/a)</td><td>394.98 (n/a)</td><td>1108.97 (n/a)</td><td>943.50 (n/a)</td><td>971.85 (n/a)</td><td>775.18 (n/a)</td><td>158.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 <b>(-30.49%)</b></td><td>0.32 (-17.82%)</td><td>0.32 (-10.59%)</td><td>0.30 (-5.57%)</td><td>0.02 <b>(-79.16%)</b></td><td>4094.20 (+5.90%)</td><td>3849.40 (+18.21%)</td><td>3916.90 (+11.85%)</td><td>3602.20 <b>(+43.88%)</b></td><td>195.84 <b>(-68.25%)</b></td><td>18.63 <b>(-30.49%)</b></td><td>17.47 (-17.82%)</td><td>17.13 (-10.59%)</td><td>16.39 (-5.57%)</td><td>0.89 <b>(-79.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>3866.10 (n/a)</td><td>3256.36 (n/a)</td><td>3502.00 (n/a)</td><td>2503.70 (n/a)</td><td>616.82 (n/a)</td><td>26.80 (n/a)</td><td>21.26 (n/a)</td><td>19.16 (n/a)</td><td>17.36 (n/a)</td><td>4.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.36 (-0.20%)</td><td>4.78 (-2.88%)</td><td>4.78 (-2.01%)</td><td>3.29 (-2.62%)</td><td>1.09 <b>(-22.31%)</b></td><td>2019.60 (+2.70%)</td><td>1453.18 (+0.50%)</td><td>1393.00 (+2.05%)</td><td>1045.80 (+0.20%)</td><td>352.12 (-16.53%)</td><td>1965.27 (-0.20%)</td><td>1477.40 (-2.88%)</td><td>1475.40 (-2.01%)</td><td>1017.65 (-2.62%)</td><td>335.57 <b>(-22.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.37 (n/a)</td><td>4.92 (n/a)</td><td>4.87 (n/a)</td><td>3.38 (n/a)</td><td>1.40 (n/a)</td><td>1966.60 (n/a)</td><td>1445.90 (n/a)</td><td>1365.00 (n/a)</td><td>1043.70 (n/a)</td><td>421.86 (n/a)</td><td>1969.24 (n/a)</td><td>1521.22 (n/a)</td><td>1505.65 (n/a)</td><td>1045.04 (n/a)</td><td>431.95 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+10.01%)</td><td>0.19 (-0.29%)</td><td>0.18 (-2.98%)</td><td>0.16 (+10.31%)</td><td>0.03 (+3.60%)</td><td>0.24 (+10.01%)</td><td>0.18 (-0.29%)</td><td>0.17 (-2.98%)</td><td>0.16 (+10.31%)</td><td>0.03 (+3.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.27 (-1.34%)</td><td>12.19 (-3.43%)</td><td>12.03 (-2.67%)</td><td>10.92 (-9.70%)</td><td>1.02 <b>(+78.01%)</b></td><td>13.26 (-1.34%)</td><td>12.18 (-3.43%)</td><td>12.02 (-2.67%)</td><td>10.92 (-9.70%)</td><td>1.02 <b>(+78.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.45 (n/a)</td><td>12.62 (n/a)</td><td>12.36 (n/a)</td><td>12.10 (n/a)</td><td>0.57 (n/a)</td><td>13.44 (n/a)</td><td>12.61 (n/a)</td><td>12.35 (n/a)</td><td>12.09 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>24.23 (-4.66%)</td><td>23.44 (-3.78%)</td><td>24.11 (-2.52%)</td><td>21.09 (-6.91%)</td><td>1.34 <b>(+23.51%)</b></td><td>24.22 (-4.66%)</td><td>23.42 (-3.78%)</td><td>24.10 (-2.52%)</td><td>21.08 (-6.91%)</td><td>1.33 <b>(+23.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>25.42 (n/a)</td><td>24.36 (n/a)</td><td>24.73 (n/a)</td><td>22.66 (n/a)</td><td>1.08 (n/a)</td><td>25.40 (n/a)</td><td>24.34 (n/a)</td><td>24.72 (n/a)</td><td>22.65 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>41.11 (-5.40%)</td><td>40.00 (-2.02%)</td><td>39.75 (-2.27%)</td><td>38.68 (+5.12%)</td><td>1.01 <b>(-61.94%)</b></td><td>41.09 (-5.40%)</td><td>39.98 (-2.02%)</td><td>39.73 (-2.27%)</td><td>38.66 (+5.12%)</td><td>1.01 <b>(-61.94%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>43.46 (n/a)</td><td>40.83 (n/a)</td><td>40.68 (n/a)</td><td>36.80 (n/a)</td><td>2.66 (n/a)</td><td>43.43 (n/a)</td><td>40.80 (n/a)</td><td>40.65 (n/a)</td><td>36.77 (n/a)</td><td>2.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>45.07 (-0.75%)</td><td>43.69 (-0.18%)</td><td>43.34 (-4.20%)</td><td>42.44 (+3.51%)</td><td>1.19 <b>(-45.09%)</b></td><td>45.04 (-0.75%)</td><td>43.66 (-0.18%)</td><td>43.31 (-4.20%)</td><td>42.41 (+3.51%)</td><td>1.19 <b>(-45.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>45.41 (n/a)</td><td>43.77 (n/a)</td><td>45.24 (n/a)</td><td>41.00 (n/a)</td><td>2.17 (n/a)</td><td>45.38 (n/a)</td><td>43.74 (n/a)</td><td>45.21 (n/a)</td><td>40.97 (n/a)</td><td>2.17 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.39 (+0.57%)</td><td>12.60 (-0.64%)</td><td>13.17 (+0.74%)</td><td>11.16 (+0.25%)</td><td>0.98 (+7.85%)</td><td>13.38 (+0.57%)</td><td>12.59 (-0.64%)</td><td>13.16 (+0.74%)</td><td>11.16 (+0.25%)</td><td>0.98 (+7.85%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.31 (n/a)</td><td>12.68 (n/a)</td><td>13.08 (n/a)</td><td>11.13 (n/a)</td><td>0.91 (n/a)</td><td>13.31 (n/a)</td><td>12.67 (n/a)</td><td>13.07 (n/a)</td><td>11.13 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>24.43 (-2.70%)</td><td>23.78 (-2.96%)</td><td>24.16 (-0.21%)</td><td>22.50 (-6.29%)</td><td>0.82 <b>(+54.57%)</b></td><td>24.42 (-2.70%)</td><td>23.77 (-2.96%)</td><td>24.15 (-0.21%)</td><td>22.49 (-6.29%)</td><td>0.82 <b>(+54.57%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>25.11 (n/a)</td><td>24.51 (n/a)</td><td>24.21 (n/a)</td><td>24.02 (n/a)</td><td>0.53 (n/a)</td><td>25.10 (n/a)</td><td>24.50 (n/a)</td><td>24.20 (n/a)</td><td>24.00 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>41.39 (-2.07%)</td><td>40.17 (+2.16%)</td><td>39.57 (-1.82%)</td><td>39.16 (+12.10%)</td><td>1.07 <b>(-61.36%)</b></td><td>41.36 (-2.07%)</td><td>40.14 (+2.16%)</td><td>39.55 (-1.82%)</td><td>39.14 (+12.10%)</td><td>1.07 <b>(-61.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>42.26 (n/a)</td><td>39.32 (n/a)</td><td>40.30 (n/a)</td><td>34.93 (n/a)</td><td>2.78 (n/a)</td><td>42.24 (n/a)</td><td>39.29 (n/a)</td><td>40.28 (n/a)</td><td>34.91 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>45.04 (-0.41%)</td><td>43.84 (+0.76%)</td><td>44.68 (+0.10%)</td><td>42.00 (+6.32%)</td><td>1.37 <b>(-43.49%)</b></td><td>45.01 (-0.41%)</td><td>43.82 (+0.76%)</td><td>44.65 (+0.10%)</td><td>41.98 (+6.32%)</td><td>1.36 <b>(-43.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>45.22 (n/a)</td><td>43.51 (n/a)</td><td>44.64 (n/a)</td><td>39.51 (n/a)</td><td>2.42 (n/a)</td><td>45.20 (n/a)</td><td>43.49 (n/a)</td><td>44.61 (n/a)</td><td>39.48 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.29 (-4.15%)</td><td>8.84 (-1.87%)</td><td>9.05 (-1.33%)</td><td>8.21 (+2.74%)</td><td>0.49 <b>(-28.37%)</b></td><td>9.27 (-4.15%)</td><td>8.83 (-1.87%)</td><td>9.04 (-1.33%)</td><td>8.20 (+2.74%)</td><td>0.49 <b>(-28.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.69 (n/a)</td><td>9.01 (n/a)</td><td>9.18 (n/a)</td><td>7.99 (n/a)</td><td>0.68 (n/a)</td><td>9.67 (n/a)</td><td>8.99 (n/a)</td><td>9.16 (n/a)</td><td>7.98 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.91 (-3.29%)</td><td>0.81 (+4.04%)</td><td>0.81 (+12.31%)</td><td>0.71 (+4.11%)</td><td>0.07 <b>(-33.03%)</b></td><td>0.90 (-3.29%)</td><td>0.80 (+4.04%)</td><td>0.79 (+12.31%)</td><td>0.70 (+4.11%)</td><td>0.07 <b>(-33.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.94 (n/a)</td><td>0.78 (n/a)</td><td>0.72 (n/a)</td><td>0.68 (n/a)</td><td>0.11 (n/a)</td><td>0.93 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.67 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.23 (-11.23%)</td><td>1.15 (-3.71%)</td><td>1.18 (-0.14%)</td><td>1.06 (+2.53%)</td><td>0.08 <b>(-41.11%)</b></td><td>1.21 (-11.23%)</td><td>1.13 (-3.71%)</td><td>1.17 (-0.14%)</td><td>1.04 (+2.53%)</td><td>0.08 <b>(-41.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.38 (n/a)</td><td>1.19 (n/a)</td><td>1.18 (n/a)</td><td>1.03 (n/a)</td><td>0.14 (n/a)</td><td>1.37 (n/a)</td><td>1.18 (n/a)</td><td>1.17 (n/a)</td><td>1.02 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>17.03 (-4.25%)</td><td>14.94 (-7.75%)</td><td>14.49 (-11.56%)</td><td>12.56 (-12.98%)</td><td>1.80 <b>(+34.44%)</b></td><td>16.84 (-4.25%)</td><td>14.77 (-7.75%)</td><td>14.33 (-11.56%)</td><td>12.42 (-12.98%)</td><td>1.78 <b>(+34.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>17.79 (n/a)</td><td>16.20 (n/a)</td><td>16.39 (n/a)</td><td>14.44 (n/a)</td><td>1.34 (n/a)</td><td>17.58 (n/a)</td><td>16.01 (n/a)</td><td>16.20 (n/a)</td><td>14.27 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>12.24 (-1.67%)</td><td>11.14 (-6.14%)</td><td>12.07 (+1.60%)</td><td>7.17 <b>(-35.72%)</b></td><td>2.22 <b>(+376.37%)</b></td><td>12.03 (-1.67%)</td><td>10.95 (-6.14%)</td><td>11.86 (+1.60%)</td><td>7.04 <b>(-35.72%)</b></td><td>2.18 <b>(+376.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.45 (n/a)</td><td>11.87 (n/a)</td><td>11.88 (n/a)</td><td>11.15 (n/a)</td><td>0.47 (n/a)</td><td>12.23 (n/a)</td><td>11.66 (n/a)</td><td>11.67 (n/a)</td><td>10.96 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.82 (+4.31%)</td><td>8.22 (+7.16%)</td><td>8.42 (+7.35%)</td><td>7.00 (+3.53%)</td><td>0.72 (+3.41%)</td><td>8.67 (+4.31%)</td><td>8.08 (+7.16%)</td><td>8.28 (+7.35%)</td><td>6.88 (+3.53%)</td><td>0.71 (+3.41%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.46 (n/a)</td><td>7.67 (n/a)</td><td>7.85 (n/a)</td><td>6.76 (n/a)</td><td>0.70 (n/a)</td><td>8.31 (n/a)</td><td>7.54 (n/a)</td><td>7.71 (n/a)</td><td>6.65 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.23 (-2.59%)</td><td>5.49 (-6.23%)</td><td>5.55 (-2.42%)</td><td>4.72 (-15.45%)</td><td>0.54 <b>(+54.13%)</b></td><td>6.13 (-2.59%)</td><td>5.40 (-6.23%)</td><td>5.46 (-2.42%)</td><td>4.64 (-15.45%)</td><td>0.53 <b>(+54.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.40 (n/a)</td><td>5.86 (n/a)</td><td>5.69 (n/a)</td><td>5.58 (n/a)</td><td>0.35 (n/a)</td><td>6.29 (n/a)</td><td>5.76 (n/a)</td><td>5.59 (n/a)</td><td>5.49 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.30 (n/a)</td><td>188.36 (n/a)</td><td>202.20 (n/a)</td><td>126.00 (n/a)</td><td>44.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>172.90 (n/a)</td><td>182.50 (n/a)</td><td>95.70 (n/a)</td><td>47.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.70 (n/a)</td><td>184.76 (n/a)</td><td>183.10 (n/a)</td><td>156.20 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>177.04 (n/a)</td><td>173.10 (n/a)</td><td>120.20 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.30 (n/a)</td><td>170.62 (n/a)</td><td>163.50 (n/a)</td><td>139.20 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.20 (n/a)</td><td>196.60 (n/a)</td><td>191.40 (n/a)</td><td>163.40 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>302.10 (n/a)</td><td>231.84 (n/a)</td><td>220.40 (n/a)</td><td>194.00 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>292.80 (n/a)</td><td>229.02 (n/a)</td><td>230.00 (n/a)</td><td>179.00 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>165.78 (n/a)</td><td>163.60 (n/a)</td><td>141.20 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>171.26 (n/a)</td><td>188.40 (n/a)</td><td>129.30 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.20 (n/a)</td><td>188.24 (n/a)</td><td>178.80 (n/a)</td><td>126.80 (n/a)</td><td>50.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>289.90 (n/a)</td><td>209.76 (n/a)</td><td>201.70 (n/a)</td><td>116.00 (n/a)</td><td>73.80 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>184.94 (n/a)</td><td>191.50 (n/a)</td><td>132.80 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>211.42 (n/a)</td><td>214.30 (n/a)</td><td>183.00 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>178.34 (n/a)</td><td>179.20 (n/a)</td><td>150.70 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>340.80 (n/a)</td><td>235.30 (n/a)</td><td>212.60 (n/a)</td><td>203.00 (n/a)</td><td>59.25 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>180.38 (n/a)</td><td>184.90 (n/a)</td><td>129.40 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>255.40 (n/a)</td><td>188.30 (n/a)</td><td>197.00 (n/a)</td><td>121.60 (n/a)</td><td>52.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>174.32 (n/a)</td><td>190.60 (n/a)</td><td>136.90 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.20 (n/a)</td><td>184.26 (n/a)</td><td>197.00 (n/a)</td><td>140.70 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>183.68 (n/a)</td><td>179.60 (n/a)</td><td>158.10 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>362.90 (n/a)</td><td>231.22 (n/a)</td><td>221.80 (n/a)</td><td>165.90 (n/a)</td><td>78.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>211.20 (n/a)</td><td>212.60 (n/a)</td><td>194.40 (n/a)</td><td>15.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>388.20 (n/a)</td><td>306.36 (n/a)</td><td>359.20 (n/a)</td><td>200.10 (n/a)</td><td>87.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (-6.24%)</td><td>0.17 (+1.10%)</td><td>0.17 (-3.62%)</td><td>0.16 (+10.01%)</td><td>0.01 <b>(-65.43%)</b></td><td>207.70 (-9.10%)</td><td>197.48 (-1.96%)</td><td>196.50 (+3.75%)</td><td>189.20 (+6.65%)</td><td>7.49 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>228.50 (n/a)</td><td>201.42 (n/a)</td><td>189.40 (n/a)</td><td>177.40 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.00 (n/a)</td><td>179.20 (n/a)</td><td>180.20 (n/a)</td><td>135.00 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>242.70 (n/a)</td><td>198.72 (n/a)</td><td>204.10 (n/a)</td><td>160.00 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>192.62 (n/a)</td><td>197.50 (n/a)</td><td>169.90 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>166.48 (n/a)</td><td>163.40 (n/a)</td><td>149.90 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>289.60 (n/a)</td><td>213.16 (n/a)</td><td>191.20 (n/a)</td><td>182.80 (n/a)</td><td>45.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>251.10 (n/a)</td><td>199.44 (n/a)</td><td>189.30 (n/a)</td><td>159.60 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>362.50 (n/a)</td><td>269.62 (n/a)</td><td>244.00 (n/a)</td><td>175.90 (n/a)</td><td>81.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-0.84%)</td><td>0.02 (-3.94%)</td><td>0.02 (-6.92%)</td><td>0.02 <b>(-22.84%)</b></td><td>0.01 <b>(+30.24%)</b></td><td>266.60 <b>(+29.61%)</b></td><td>188.44 (+7.15%)</td><td>184.30 (+7.46%)</td><td>133.20 (+0.83%)</td><td>50.20 <b>(+73.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>175.86 (n/a)</td><td>171.50 (n/a)</td><td>132.10 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(+45.32%)</b></td><td>0.03 <b>(+27.22%)</b></td><td>0.03 <b>(+29.32%)</b></td><td>0.02 (+3.35%)</td><td>0.00 <b>(+268.39%)</b></td><td>202.30 (-3.25%)</td><td>153.66 (-19.54%)</td><td>145.20 <b>(-22.64%)</b></td><td>123.40 <b>(-31.22%)</b></td><td>29.42 <b>(+152.15%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>190.98 (n/a)</td><td>187.70 (n/a)</td><td>179.40 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-9.96%)</td><td>0.02 (-0.08%)</td><td>0.02 (+2.56%)</td><td>0.02 (+7.80%)</td><td>0.00 <b>(-30.08%)</b></td><td>195.90 (-7.24%)</td><td>172.92 (-1.21%)</td><td>173.30 (-2.48%)</td><td>149.70 (+11.05%)</td><td>22.34 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>175.04 (n/a)</td><td>177.70 (n/a)</td><td>134.80 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+15.15%)</td><td>0.03 (+1.30%)</td><td>0.03 (-7.13%)</td><td>0.02 (-3.60%)</td><td>0.00 <b>(+92.65%)</b></td><td>185.70 (+3.74%)</td><td>153.88 (+0.09%)</td><td>160.40 (+7.72%)</td><td>124.60 (-13.17%)</td><td>24.14 <b>(+68.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>153.74 (n/a)</td><td>148.90 (n/a)</td><td>143.50 (n/a)</td><td>14.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-19.52%)</td><td>0.03 (-7.95%)</td><td>0.03 (+2.81%)</td><td>0.02 (+0.07%)</td><td>0.00 <b>(-57.18%)</b></td><td>180.90 (-0.06%)</td><td>161.94 (+5.79%)</td><td>163.10 (-2.74%)</td><td>145.80 <b>(+24.19%)</b></td><td>16.00 <b>(-47.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>153.08 (n/a)</td><td>167.70 (n/a)</td><td>117.40 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-3.17%)</td><td>0.02 (+14.78%)</td><td>0.02 <b>(+22.11%)</b></td><td>0.02 (+17.57%)</td><td>0.00 <b>(-53.48%)</b></td><td>183.50 (-14.97%)</td><td>168.98 (-14.11%)</td><td>167.30 (-18.11%)</td><td>155.60 (+3.25%)</td><td>11.09 <b>(-58.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>196.74 (n/a)</td><td>204.30 (n/a)</td><td>150.70 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-10.70%)</td><td>0.02 (+7.95%)</td><td>0.03 <b>(+30.12%)</b></td><td>0.01 (-18.24%)</td><td>0.01 (-0.77%)</td><td>366.30 <b>(+22.30%)</b></td><td>199.20 (-3.83%)</td><td>152.70 <b>(-23.11%)</b></td><td>139.80 (+12.02%)</td><td>94.87 <b>(+43.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>207.14 (n/a)</td><td>198.60 (n/a)</td><td>124.80 (n/a)</td><td>66.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (-9.54%)</td><td>0.02 (+8.77%)</td><td>0.02 (+14.51%)</td><td>0.02 <b>(+40.54%)</b></td><td>0.00 <b>(-39.43%)</b></td><td>251.80 <b>(-28.85%)</b></td><td>203.28 (-12.48%)</td><td>189.80 (-12.66%)</td><td>172.20 (+10.60%)</td><td>33.69 <b>(-54.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>353.90 (n/a)</td><td>232.28 (n/a)</td><td>217.30 (n/a)</td><td>155.70 (n/a)</td><td>73.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+10.46%)</td><td>0.05 (+16.59%)</td><td>0.05 (+13.84%)</td><td>0.04 <b>(+31.54%)</b></td><td>0.01 (-3.07%)</td><td>187.40 <b>(-23.98%)</b></td><td>154.52 (-15.27%)</td><td>157.00 (-12.14%)</td><td>128.10 (-9.47%)</td><td>24.74 <b>(-36.59%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.50 (n/a)</td><td>182.36 (n/a)</td><td>178.70 (n/a)</td><td>141.50 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 <b>(+27.12%)</b></td><td>0.05 (+12.06%)</td><td>0.05 (+2.52%)</td><td>0.04 (+13.00%)</td><td>0.01 <b>(+82.30%)</b></td><td>183.90 (-11.50%)</td><td>161.24 (-9.74%)</td><td>165.80 (-2.41%)</td><td>127.30 <b>(-21.32%)</b></td><td>24.35 <b>(+28.54%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>178.64 (n/a)</td><td>169.90 (n/a)</td><td>161.80 (n/a)</td><td>18.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+14.33%)</td><td>0.05 (+4.50%)</td><td>0.05 (+5.03%)</td><td>0.03 (-19.64%)</td><td>0.01 <b>(+67.88%)</b></td><td>258.90 <b>(+24.47%)</b></td><td>180.02 (-1.00%)</td><td>179.20 (-4.78%)</td><td>133.70 (-12.56%)</td><td>48.35 <b>(+87.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>181.84 (n/a)</td><td>188.20 (n/a)</td><td>152.90 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-5.82%)</td><td>0.05 (+4.35%)</td><td>0.05 <b>(+22.17%)</b></td><td>0.04 (+7.83%)</td><td>0.01 <b>(-39.19%)</b></td><td>210.80 (-7.26%)</td><td>172.58 (-7.24%)</td><td>169.60 (-18.11%)</td><td>143.50 (+6.14%)</td><td>27.24 <b>(-39.47%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>186.06 (n/a)</td><td>207.10 (n/a)</td><td>135.20 (n/a)</td><td>45.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+10.72%)</td><td>0.06 <b>(+22.92%)</b></td><td>0.06 <b>(+30.67%)</b></td><td>0.05 (+19.58%)</td><td>0.01 (-0.12%)</td><td>165.90 (-16.38%)</td><td>144.60 (-18.97%)</td><td>144.30 <b>(-23.49%)</b></td><td>126.30 (-9.66%)</td><td>17.86 <b>(-24.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>178.46 (n/a)</td><td>188.60 (n/a)</td><td>139.80 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (+4.53%)</td><td>0.05 (+0.05%)</td><td>0.05 (+11.86%)</td><td>0.02 <b>(-43.46%)</b></td><td>0.01 <b>(+276.84%)</b></td><td>339.00 <b>(+76.93%)</b></td><td>195.72 (+9.10%)</td><td>161.40 (-10.63%)</td><td>153.90 (-4.29%)</td><td>80.26 <b>(+558.46%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>179.40 (n/a)</td><td>180.60 (n/a)</td><td>160.80 (n/a)</td><td>12.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+1.68%)</td><td>0.05 (+7.83%)</td><td>0.05 (+19.54%)</td><td>0.04 (-11.02%)</td><td>0.01 (+17.84%)</td><td>229.30 (+12.35%)</td><td>163.14 (-5.98%)</td><td>151.00 (-16.34%)</td><td>130.90 (-1.65%)</td><td>38.19 <b>(+38.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>173.52 (n/a)</td><td>180.50 (n/a)</td><td>133.10 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+10.68%)</td><td>0.05 (+6.43%)</td><td>0.05 (+6.71%)</td><td>0.04 (+3.90%)</td><td>0.01 <b>(+36.88%)</b></td><td>214.10 (-3.73%)</td><td>173.70 (-4.79%)</td><td>162.00 (-6.25%)</td><td>133.10 (-9.64%)</td><td>35.07 <b>(+21.93%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>182.44 (n/a)</td><td>172.80 (n/a)</td><td>147.30 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 <b>(+34.36%)</b></td><td>0.05 (+18.10%)</td><td>0.05 <b>(+21.55%)</b></td><td>0.04 (+7.86%)</td><td>0.01 <b>(+163.72%)</b></td><td>202.40 (-7.33%)</td><td>171.70 (-13.84%)</td><td>165.80 (-17.72%)</td><td>134.60 <b>(-25.55%)</b></td><td>27.85 <b>(+85.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>199.28 (n/a)</td><td>201.50 (n/a)</td><td>180.80 (n/a)</td><td>15.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (+9.15%)</td><td>0.04 (-2.50%)</td><td>0.04 (-2.30%)</td><td>0.02 <b>(-38.11%)</b></td><td>0.01 <b>(+223.89%)</b></td><td>374.50 <b>(+61.56%)</b></td><td>236.72 (+10.05%)</td><td>223.00 (+2.34%)</td><td>172.20 (-8.36%)</td><td>81.24 <b>(+397.38%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.80 (n/a)</td><td>215.10 (n/a)</td><td>217.90 (n/a)</td><td>187.90 (n/a)</td><td>16.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+3.90%)</td><td>0.12 (+10.65%)</td><td>0.11 (+7.94%)</td><td>0.09 <b>(+34.36%)</b></td><td>0.02 (-18.77%)</td><td>180.70 <b>(-25.58%)</b></td><td>145.96 (-12.19%)</td><td>146.00 (-7.36%)</td><td>119.70 (-3.78%)</td><td>25.99 <b>(-44.20%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.80 (n/a)</td><td>166.22 (n/a)</td><td>157.60 (n/a)</td><td>124.40 (n/a)</td><td>46.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 <b>(+24.09%)</b></td><td>0.10 (+12.26%)</td><td>0.10 (+0.91%)</td><td>0.08 (+16.86%)</td><td>0.02 <b>(+23.54%)</b></td><td>200.50 (-14.43%)</td><td>163.34 (-10.97%)</td><td>164.40 (-0.90%)</td><td>115.30 (-19.43%)</td><td>30.69 (-19.73%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>183.46 (n/a)</td><td>165.90 (n/a)</td><td>143.10 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (+18.71%)</td><td>0.10 (+1.10%)</td><td>0.10 (+1.49%)</td><td>0.04 <b>(-49.92%)</b></td><td>0.03 <b>(+269.46%)</b></td><td>379.40 <b>(+99.68%)</b></td><td>196.78 (+14.31%)</td><td>169.00 (-1.46%)</td><td>125.00 (-15.77%)</td><td>103.92 <b>(+576.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>172.14 (n/a)</td><td>171.50 (n/a)</td><td>148.40 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+32.83%)</b></td><td>0.11 <b>(+20.19%)</b></td><td>0.10 (+8.02%)</td><td>0.08 (+3.52%)</td><td>0.02 <b>(+138.86%)</b></td><td>210.80 (-3.39%)</td><td>161.70 (-14.14%)</td><td>168.70 (-7.41%)</td><td>123.60 <b>(-24.73%)</b></td><td>36.86 <b>(+65.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>188.34 (n/a)</td><td>182.20 (n/a)</td><td>164.20 (n/a)</td><td>22.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+31.36%)</b></td><td>0.09 (+4.08%)</td><td>0.10 (+7.15%)</td><td>0.06 <b>(-32.50%)</b></td><td>0.03 <b>(+355.97%)</b></td><td>292.30 <b>(+48.15%)</b></td><td>188.18 (+3.06%)</td><td>171.20 (-6.65%)</td><td>129.90 <b>(-23.86%)</b></td><td>62.34 <b>(+441.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>182.60 (n/a)</td><td>183.40 (n/a)</td><td>170.60 (n/a)</td><td>11.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-0.96%)</td><td>0.09 (-10.35%)</td><td>0.08 (-9.12%)</td><td>0.07 <b>(-22.95%)</b></td><td>0.01 <b>(+99.15%)</b></td><td>236.40 <b>(+29.82%)</b></td><td>195.72 (+13.33%)</td><td>195.20 (+10.03%)</td><td>155.60 (+0.91%)</td><td>30.47 <b>(+160.00%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>172.70 (n/a)</td><td>177.40 (n/a)</td><td>154.20 (n/a)</td><td>11.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (+10.17%)</td><td>0.09 (+7.69%)</td><td>0.10 (+7.09%)</td><td>0.08 (+7.54%)</td><td>0.01 <b>(+28.99%)</b></td><td>200.00 (-6.98%)</td><td>177.20 (-6.83%)</td><td>169.40 (-6.62%)</td><td>153.60 (-9.22%)</td><td>21.10 (+10.78%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>190.18 (n/a)</td><td>181.40 (n/a)</td><td>169.20 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (+15.45%)</td><td>0.08 (+11.81%)</td><td>0.08 (+3.87%)</td><td>0.06 (+18.62%)</td><td>0.01 (-7.28%)</td><td>254.40 (-15.68%)</td><td>209.86 (-11.28%)</td><td>202.90 (-3.70%)</td><td>177.00 (-13.41%)</td><td>29.24 <b>(-30.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>236.54 (n/a)</td><td>210.70 (n/a)</td><td>204.40 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (+11.48%)</td><td>0.22 (+7.13%)</td><td>0.25 (+11.48%)</td><td>0.14 (-17.09%)</td><td>0.05 <b>(+98.41%)</b></td><td>226.90 <b>(+20.56%)</b></td><td>153.48 (-3.18%)</td><td>132.30 (-10.31%)</td><td>127.50 (-10.27%)</td><td>42.38 <b>(+115.73%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.20 (n/a)</td><td>158.52 (n/a)</td><td>147.50 (n/a)</td><td>142.10 (n/a)</td><td>19.64 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (-8.92%)</td><td>0.21 (+3.78%)</td><td>0.20 (+10.06%)</td><td>0.17 (+9.87%)</td><td>0.04 <b>(-27.48%)</b></td><td>193.40 (-8.95%)</td><td>162.30 (-5.49%)</td><td>160.00 (-9.14%)</td><td>124.50 (+9.79%)</td><td>28.16 <b>(-23.06%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>212.40 (n/a)</td><td>171.72 (n/a)</td><td>176.10 (n/a)</td><td>113.40 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 <b>(+23.24%)</b></td><td>0.21 <b>(+25.40%)</b></td><td>0.22 <b>(+31.89%)</b></td><td>0.16 (+11.45%)</td><td>0.04 <b>(+43.10%)</b></td><td>202.50 (-10.28%)</td><td>158.44 (-19.48%)</td><td>150.80 <b>(-24.18%)</b></td><td>124.30 (-18.86%)</td><td>31.28 (+3.70%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.70 (n/a)</td><td>196.78 (n/a)</td><td>198.90 (n/a)</td><td>153.20 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+6.34%)</td><td>0.21 (+11.73%)</td><td>0.22 (+14.10%)</td><td>0.16 <b>(+26.22%)</b></td><td>0.03 (-19.73%)</td><td>203.70 <b>(-20.77%)</b></td><td>157.14 (-12.35%)</td><td>148.70 (-12.37%)</td><td>135.20 (-5.98%)</td><td>26.74 <b>(-40.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>257.10 (n/a)</td><td>179.28 (n/a)</td><td>169.70 (n/a)</td><td>143.80 (n/a)</td><td>44.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (-0.21%)</td><td>0.19 (+4.31%)</td><td>0.19 (+2.79%)</td><td>0.16 (+5.96%)</td><td>0.02 (-4.69%)</td><td>209.10 (-5.64%)</td><td>178.08 (-4.35%)</td><td>173.40 (-2.69%)</td><td>153.70 (+0.20%)</td><td>23.30 (-10.43%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.60 (n/a)</td><td>186.18 (n/a)</td><td>178.20 (n/a)</td><td>153.40 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+14.72%)</td><td>0.20 (+17.03%)</td><td>0.21 <b>(+24.01%)</b></td><td>0.16 (+15.08%)</td><td>0.04 <b>(+20.48%)</b></td><td>211.40 (-13.11%)</td><td>170.68 (-14.32%)</td><td>155.70 (-19.37%)</td><td>135.30 (-12.88%)</td><td>31.51 (-7.29%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>243.30 (n/a)</td><td>199.20 (n/a)</td><td>193.10 (n/a)</td><td>155.30 (n/a)</td><td>33.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (+18.11%)</td><td>0.17 (+18.08%)</td><td>0.17 (+17.53%)</td><td>0.15 <b>(+25.85%)</b></td><td>0.02 (+11.31%)</td><td>221.00 <b>(-20.53%)</b></td><td>193.18 (-15.49%)</td><td>188.50 (-14.90%)</td><td>171.80 (-15.33%)</td><td>22.06 <b>(-26.28%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>278.10 (n/a)</td><td>228.60 (n/a)</td><td>221.50 (n/a)</td><td>202.90 (n/a)</td><td>29.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(-27.28%)</b></td><td>0.02 (-11.81%)</td><td>0.02 (-18.91%)</td><td>0.02 <b>(+24.25%)</b></td><td>0.00 <b>(-63.45%)</b></td><td>199.30 (-19.54%)</td><td>177.96 (+5.05%)</td><td>187.30 <b>(+23.30%)</b></td><td>151.70 <b>(+37.53%)</b></td><td>22.93 <b>(-60.26%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.70 (n/a)</td><td>169.40 (n/a)</td><td>151.90 (n/a)</td><td>110.30 (n/a)</td><td>57.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-13.48%)</td><td>0.03 (-12.29%)</td><td>0.03 (-10.42%)</td><td>0.02 (-19.64%)</td><td>0.01 (-7.04%)</td><td>232.60 <b>(+24.45%)</b></td><td>160.74 (+15.16%)</td><td>147.20 (+11.68%)</td><td>126.50 (+15.53%)</td><td>43.83 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>139.58 (n/a)</td><td>131.80 (n/a)</td><td>109.50 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 <b>(-21.46%)</b></td><td>0.02 (-11.56%)</td><td>0.02 (-7.13%)</td><td>0.02 (+6.43%)</td><td>0.00 <b>(-49.43%)</b></td><td>256.90 (-6.04%)</td><td>223.86 (+7.80%)</td><td>238.90 (+7.66%)</td><td>175.80 <b>(+27.30%)</b></td><td>36.22 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>273.40 (n/a)</td><td>207.66 (n/a)</td><td>221.90 (n/a)</td><td>138.10 (n/a)</td><td>58.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 <b>(-23.37%)</b></td><td>0.02 (-8.76%)</td><td>0.02 (+10.71%)</td><td>0.02 (+4.49%)</td><td>0.00 <b>(-54.99%)</b></td><td>244.40 (-4.31%)</td><td>209.14 (+4.53%)</td><td>196.20 (-9.67%)</td><td>174.40 <b>(+30.54%)</b></td><td>30.91 <b>(-42.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.40 (n/a)</td><td>200.08 (n/a)</td><td>217.20 (n/a)</td><td>133.60 (n/a)</td><td>53.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-4.02%)</td><td>0.03 (-4.32%)</td><td>0.03 (+2.23%)</td><td>0.02 (-11.29%)</td><td>0.01 (+7.09%)</td><td>209.90 (+12.73%)</td><td>168.64 (+5.72%)</td><td>163.30 (-2.16%)</td><td>118.70 (+4.21%)</td><td>36.88 <b>(+30.26%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>159.52 (n/a)</td><td>166.90 (n/a)</td><td>113.90 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(-23.60%)</b></td><td>0.02 (-17.03%)</td><td>0.02 <b>(-27.80%)</b></td><td>0.02 (-8.96%)</td><td>0.00 <b>(-46.80%)</b></td><td>212.50 (+9.82%)</td><td>172.88 (+16.40%)</td><td>176.70 <b>(+38.48%)</b></td><td>140.20 <b>(+30.91%)</b></td><td>28.73 <b>(-28.39%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>148.52 (n/a)</td><td>127.60 (n/a)</td><td>107.10 (n/a)</td><td>40.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+12.74%)</td><td>0.02 (+11.62%)</td><td>0.02 <b>(+21.27%)</b></td><td>0.02 (-4.09%)</td><td>0.00 <b>(+36.09%)</b></td><td>234.60 (+4.27%)</td><td>179.74 (-9.41%)</td><td>175.40 (-17.54%)</td><td>144.40 (-11.30%)</td><td>34.11 <b>(+28.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.00 (n/a)</td><td>198.40 (n/a)</td><td>212.70 (n/a)</td><td>162.80 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+0.21%)</td><td>0.02 (-6.26%)</td><td>0.02 (-9.35%)</td><td>0.02 (-18.12%)</td><td>0.01 <b>(+34.56%)</b></td><td>242.20 <b>(+22.14%)</b></td><td>175.24 (+9.87%)</td><td>171.90 (+10.26%)</td><td>131.10 (-0.23%)</td><td>47.25 <b>(+60.63%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>159.50 (n/a)</td><td>155.90 (n/a)</td><td>131.40 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-18.40%)</td><td>0.02 (-8.79%)</td><td>0.02 (-8.34%)</td><td>0.02 (-15.73%)</td><td>0.00 (-19.12%)</td><td>240.70 (+18.63%)</td><td>198.40 (+9.41%)</td><td>214.60 (+9.10%)</td><td>156.40 <b>(+22.57%)</b></td><td>36.68 (+15.14%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>181.34 (n/a)</td><td>196.70 (n/a)</td><td>127.60 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-6.52%)</td><td>0.03 (+0.60%)</td><td>0.02 (+0.46%)</td><td>0.02 <b>(+20.49%)</b></td><td>0.00 <b>(-43.85%)</b></td><td>178.50 (-16.98%)</td><td>157.64 (-3.05%)</td><td>165.20 (-0.42%)</td><td>137.40 (+7.01%)</td><td>17.61 <b>(-49.76%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>162.60 (n/a)</td><td>165.90 (n/a)</td><td>128.40 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+14.98%)</td><td>0.03 (+15.29%)</td><td>0.02 (+8.89%)</td><td>0.02 (+8.21%)</td><td>0.01 <b>(+39.57%)</b></td><td>199.90 (-7.58%)</td><td>166.08 (-11.77%)</td><td>186.40 (-8.18%)</td><td>118.40 (-13.07%)</td><td>37.85 (+13.36%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>188.24 (n/a)</td><td>203.00 (n/a)</td><td>136.20 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 <b>(-27.24%)</b></td><td>0.02 (-8.73%)</td><td>0.02 (+3.12%)</td><td>0.02 (+10.26%)</td><td>0.00 <b>(-64.59%)</b></td><td>213.10 (-9.28%)</td><td>182.74 (+5.16%)</td><td>175.10 (-3.05%)</td><td>165.20 <b>(+37.44%)</b></td><td>19.11 <b>(-55.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>173.78 (n/a)</td><td>180.60 (n/a)</td><td>120.20 (n/a)</td><td>42.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+19.35%)</td><td>0.02 (+14.49%)</td><td>0.02 (+12.24%)</td><td>0.02 <b>(+31.19%)</b></td><td>0.00 (+12.87%)</td><td>214.90 <b>(-23.79%)</b></td><td>177.58 (-13.20%)</td><td>171.20 (-10.93%)</td><td>140.00 (-16.22%)</td><td>32.72 <b>(-28.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>282.00 (n/a)</td><td>204.58 (n/a)</td><td>192.20 (n/a)</td><td>167.10 (n/a)</td><td>45.68 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+1.03%)</td><td>0.02 (+4.39%)</td><td>0.02 (+12.64%)</td><td>0.02 (+14.23%)</td><td>0.01 (-13.71%)</td><td>207.60 (-12.48%)</td><td>170.18 (-5.92%)</td><td>171.60 (-11.23%)</td><td>120.10 (-1.07%)</td><td>31.76 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>180.88 (n/a)</td><td>193.30 (n/a)</td><td>121.40 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-5.07%)</td><td>0.02 (+6.70%)</td><td>0.02 <b>(+34.18%)</b></td><td>0.02 (+7.77%)</td><td>0.01 <b>(-25.27%)</b></td><td>217.20 (-7.22%)</td><td>173.10 (-9.53%)</td><td>166.00 <b>(-25.46%)</b></td><td>120.70 (+5.32%)</td><td>37.41 <b>(-28.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>191.34 (n/a)</td><td>222.70 (n/a)</td><td>114.60 (n/a)</td><td>52.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (-17.51%)</td><td>0.02 (-10.85%)</td><td>0.02 (+6.31%)</td><td>0.02 (-12.91%)</td><td>0.00 (-10.06%)</td><td>252.00 (+14.81%)</td><td>199.92 (+12.67%)</td><td>169.70 (-5.93%)</td><td>164.90 <b>(+21.25%)</b></td><td>43.77 <b>(+26.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>177.44 (n/a)</td><td>180.40 (n/a)</td><td>136.00 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-14.83%)</td><td>0.05 (-2.50%)</td><td>0.05 (-4.41%)</td><td>0.04 (+8.79%)</td><td>0.01 <b>(-44.92%)</b></td><td>193.00 (-8.10%)</td><td>172.70 (-0.21%)</td><td>175.50 (+4.65%)</td><td>139.00 (+17.40%)</td><td>21.61 <b>(-40.54%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>173.06 (n/a)</td><td>167.70 (n/a)</td><td>118.40 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-13.33%)</td><td>0.05 (-9.80%)</td><td>0.05 (-7.64%)</td><td>0.03 (-13.62%)</td><td>0.01 <b>(-22.39%)</b></td><td>241.90 (+15.74%)</td><td>182.38 (+10.36%)</td><td>173.80 (+8.29%)</td><td>150.80 (+15.38%)</td><td>34.75 (+8.26%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>165.26 (n/a)</td><td>160.50 (n/a)</td><td>130.70 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-17.83%)</td><td>0.04 (-5.49%)</td><td>0.04 (+5.79%)</td><td>0.03 (+3.48%)</td><td>0.01 <b>(-43.28%)</b></td><td>251.50 (-3.38%)</td><td>207.18 (+3.04%)</td><td>200.20 (-5.48%)</td><td>172.10 <b>(+21.71%)</b></td><td>30.96 <b>(-31.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.30 (n/a)</td><td>201.06 (n/a)</td><td>211.80 (n/a)</td><td>141.40 (n/a)</td><td>45.44 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 <b>(-23.70%)</b></td><td>0.04 (-10.15%)</td><td>0.04 (-1.84%)</td><td>0.03 (-6.48%)</td><td>0.00 <b>(-56.98%)</b></td><td>255.40 (+6.95%)</td><td>211.30 (+8.21%)</td><td>203.30 (+1.90%)</td><td>190.30 <b>(+31.06%)</b></td><td>25.46 <b>(-38.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.80 (n/a)</td><td>195.26 (n/a)</td><td>199.50 (n/a)</td><td>145.20 (n/a)</td><td>41.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+0.15%)</td><td>0.05 (-1.24%)</td><td>0.05 (-16.64%)</td><td>0.04 (+19.51%)</td><td>0.01 <b>(-32.50%)</b></td><td>187.00 (-16.33%)</td><td>161.70 (-2.41%)</td><td>163.90 (+19.90%)</td><td>124.10 (-0.16%)</td><td>26.14 <b>(-44.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>165.70 (n/a)</td><td>136.70 (n/a)</td><td>124.30 (n/a)</td><td>46.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+4.94%)</td><td>0.05 (-0.11%)</td><td>0.05 (+3.26%)</td><td>0.04 (-19.40%)</td><td>0.01 <b>(+62.16%)</b></td><td>217.20 <b>(+24.04%)</b></td><td>163.06 (+2.24%)</td><td>156.30 (-3.16%)</td><td>125.30 (-4.71%)</td><td>33.47 <b>(+100.85%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>159.48 (n/a)</td><td>161.40 (n/a)</td><td>131.50 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+6.05%)</td><td>0.04 (-0.84%)</td><td>0.04 (-11.55%)</td><td>0.04 <b>(+42.82%)</b></td><td>0.01 <b>(-36.38%)</b></td><td>209.70 <b>(-29.98%)</b></td><td>186.90 (-3.55%)</td><td>187.40 (+13.03%)</td><td>146.30 (-5.73%)</td><td>25.02 <b>(-58.95%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>193.78 (n/a)</td><td>165.80 (n/a)</td><td>155.20 (n/a)</td><td>60.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-2.02%)</td><td>0.05 (+11.54%)</td><td>0.05 (+16.69%)</td><td>0.04 <b>(+26.57%)</b></td><td>0.01 (-8.53%)</td><td>219.70 <b>(-21.00%)</b></td><td>162.28 (-12.33%)</td><td>151.90 (-14.28%)</td><td>127.70 (+2.08%)</td><td>39.39 <b>(-30.55%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.10 (n/a)</td><td>185.10 (n/a)</td><td>177.20 (n/a)</td><td>125.10 (n/a)</td><td>56.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+16.41%)</td><td>0.05 (+15.31%)</td><td>0.05 (+11.47%)</td><td>0.04 (+18.35%)</td><td>0.01 (+7.90%)</td><td>185.30 (-15.50%)</td><td>154.30 (-13.46%)</td><td>151.80 (-10.28%)</td><td>136.10 (-14.13%)</td><td>18.81 <b>(-21.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>178.30 (n/a)</td><td>169.20 (n/a)</td><td>158.50 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (-0.74%)</td><td>0.06 (+18.09%)</td><td>0.06 <b>(+37.57%)</b></td><td>0.05 (+18.89%)</td><td>0.01 <b>(-44.12%)</b></td><td>163.50 (-15.90%)</td><td>137.22 (-17.29%)</td><td>133.90 <b>(-27.31%)</b></td><td>125.50 (+0.72%)</td><td>15.15 <b>(-52.07%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>165.90 (n/a)</td><td>184.20 (n/a)</td><td>124.60 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-3.23%)</td><td>0.05 (-5.70%)</td><td>0.05 (-5.88%)</td><td>0.04 (-12.65%)</td><td>0.01 (-4.32%)</td><td>216.00 (+14.47%)</td><td>164.38 (+6.27%)</td><td>152.30 (+6.21%)</td><td>132.70 (+3.27%)</td><td>32.94 (+14.21%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>154.68 (n/a)</td><td>143.40 (n/a)</td><td>128.50 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+4.94%)</td><td>0.05 (+0.22%)</td><td>0.05 (-10.76%)</td><td>0.04 (+17.77%)</td><td>0.01 <b>(-23.73%)</b></td><td>195.60 (-15.10%)</td><td>169.36 (-3.09%)</td><td>180.20 (+12.06%)</td><td>124.30 (-4.75%)</td><td>27.39 <b>(-40.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>174.76 (n/a)</td><td>160.80 (n/a)</td><td>130.50 (n/a)</td><td>45.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+0.47%)</td><td>0.05 (+9.86%)</td><td>0.05 (+10.65%)</td><td>0.04 (+17.23%)</td><td>0.01 <b>(-38.72%)</b></td><td>199.20 (-14.73%)</td><td>165.96 (-11.46%)</td><td>158.70 (-9.62%)</td><td>141.50 (-0.49%)</td><td>21.47 <b>(-49.09%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>187.44 (n/a)</td><td>175.60 (n/a)</td><td>142.20 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-14.07%)</td><td>0.05 (+8.53%)</td><td>0.05 (+15.67%)</td><td>0.05 <b>(+54.53%)</b></td><td>0.00 <b>(-76.91%)</b></td><td>179.70 <b>(-35.29%)</b></td><td>169.74 (-13.64%)</td><td>173.00 (-13.59%)</td><td>154.30 (+16.37%)</td><td>10.00 <b>(-82.46%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.70 (n/a)</td><td>196.56 (n/a)</td><td>200.20 (n/a)</td><td>132.60 (n/a)</td><td>57.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+13.26%)</td><td>0.05 (+11.92%)</td><td>0.05 (+10.19%)</td><td>0.04 (-0.75%)</td><td>0.01 <b>(+45.63%)</b></td><td>216.10 (+0.75%)</td><td>159.48 (-8.31%)</td><td>166.60 (-9.26%)</td><td>112.90 (-11.73%)</td><td>42.02 <b>(+28.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>173.94 (n/a)</td><td>183.60 (n/a)</td><td>127.90 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+0.72%)</td><td>0.05 (+1.80%)</td><td>0.05 (+1.20%)</td><td>0.04 (+17.74%)</td><td>0.01 <b>(-24.42%)</b></td><td>224.50 (-15.06%)</td><td>173.22 (-3.98%)</td><td>162.70 (-1.21%)</td><td>145.20 (-0.75%)</td><td>30.17 <b>(-36.85%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.30 (n/a)</td><td>180.40 (n/a)</td><td>164.70 (n/a)</td><td>146.30 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 <b>(+25.04%)</b></td><td>0.10 (-0.04%)</td><td>0.10 (-10.75%)</td><td>0.07 (-13.43%)</td><td>0.03 <b>(+80.22%)</b></td><td>243.20 (+15.48%)</td><td>171.88 (+4.35%)</td><td>167.30 (+12.06%)</td><td>110.80 <b>(-20.06%)</b></td><td>48.55 <b>(+64.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>164.72 (n/a)</td><td>149.30 (n/a)</td><td>138.60 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (-6.09%)</td><td>0.10 (-7.96%)</td><td>0.11 (-1.48%)</td><td>0.07 (-6.08%)</td><td>0.02 (+11.20%)</td><td>219.60 (+6.50%)</td><td>169.00 (+9.63%)</td><td>148.60 (+1.57%)</td><td>136.80 (+6.46%)</td><td>36.39 <b>(+20.88%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>154.16 (n/a)</td><td>146.30 (n/a)</td><td>128.50 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-0.08%)</td><td>0.08 (+0.24%)</td><td>0.08 (+4.43%)</td><td>0.05 (+8.18%)</td><td>0.02 (-8.91%)</td><td>325.70 (-7.55%)</td><td>224.08 (-1.96%)</td><td>218.00 (-4.22%)</td><td>154.10 (+0.06%)</td><td>63.91 (-15.92%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>352.30 (n/a)</td><td>228.56 (n/a)</td><td>227.60 (n/a)</td><td>154.00 (n/a)</td><td>76.02 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (-4.67%)</td><td>0.09 (+4.29%)</td><td>0.09 (-2.16%)</td><td>0.08 <b>(+62.03%)</b></td><td>0.01 <b>(-49.92%)</b></td><td>210.30 <b>(-38.29%)</b></td><td>186.18 (-10.36%)</td><td>190.70 (+2.20%)</td><td>160.40 (+4.91%)</td><td>23.40 <b>(-69.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>340.80 (n/a)</td><td>207.70 (n/a)</td><td>186.60 (n/a)</td><td>152.90 (n/a)</td><td>76.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+1.33%)</td><td>0.11 (+12.27%)</td><td>0.11 <b>(+21.61%)</b></td><td>0.09 <b>(+23.38%)</b></td><td>0.02 <b>(-33.14%)</b></td><td>181.20 (-18.93%)</td><td>148.60 (-14.36%)</td><td>146.50 (-17.74%)</td><td>115.10 (-1.29%)</td><td>24.03 <b>(-47.65%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>223.50 (n/a)</td><td>173.52 (n/a)</td><td>178.10 (n/a)</td><td>116.60 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (+14.92%)</td><td>0.12 (+15.31%)</td><td>0.11 (-4.76%)</td><td>0.10 <b>(+144.91%)</b></td><td>0.03 <b>(-38.48%)</b></td><td>157.70 <b>(-59.17%)</b></td><td>137.22 <b>(-26.81%)</b></td><td>148.70 (+5.01%)</td><td>99.10 (-12.99%)</td><td>24.19 <b>(-78.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>386.20 (n/a)</td><td>187.48 (n/a)</td><td>141.60 (n/a)</td><td>113.90 (n/a)</td><td>113.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 <b>(+39.69%)</b></td><td>0.10 (+9.79%)</td><td>0.10 (-2.12%)</td><td>0.06 (-9.90%)</td><td>0.03 <b>(+99.73%)</b></td><td>267.10 (+10.97%)</td><td>173.68 (-4.11%)</td><td>167.90 (+2.19%)</td><td>113.10 <b>(-28.42%)</b></td><td>57.01 <b>(+63.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.70 (n/a)</td><td>181.12 (n/a)</td><td>164.30 (n/a)</td><td>158.00 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-11.67%)</td><td>0.12 (+2.79%)</td><td>0.11 (-12.87%)</td><td>0.11 <b>(+36.17%)</b></td><td>0.01 <b>(-62.53%)</b></td><td>154.40 <b>(-26.55%)</b></td><td>138.54 (-8.70%)</td><td>144.60 (+14.76%)</td><td>122.10 (+13.16%)</td><td>13.98 <b>(-70.10%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.20 (n/a)</td><td>151.74 (n/a)</td><td>126.00 (n/a)</td><td>107.90 (n/a)</td><td>46.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (-7.30%)</td><td>0.10 (+2.60%)</td><td>0.10 (+3.62%)</td><td>0.05 <b>(-26.61%)</b></td><td>0.03 (+7.83%)</td><td>330.80 <b>(+36.30%)</b></td><td>186.10 (+2.04%)</td><td>159.10 (-3.46%)</td><td>131.80 (+7.86%)</td><td>81.92 <b>(+64.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>242.70 (n/a)</td><td>182.38 (n/a)</td><td>164.80 (n/a)</td><td>122.20 (n/a)</td><td>49.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-15.55%)</td><td>0.10 (-6.54%)</td><td>0.10 (-6.49%)</td><td>0.08 (+1.97%)</td><td>0.01 <b>(-39.09%)</b></td><td>208.90 (-1.92%)</td><td>168.80 (+5.21%)</td><td>160.80 (+6.91%)</td><td>151.00 (+18.34%)</td><td>23.08 <b>(-29.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.00 (n/a)</td><td>160.44 (n/a)</td><td>150.40 (n/a)</td><td>127.60 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (+0.42%)</td><td>0.10 (+5.41%)</td><td>0.10 (-6.81%)</td><td>0.09 (+16.33%)</td><td>0.02 <b>(-30.20%)</b></td><td>188.60 (-14.04%)</td><td>159.68 (-7.61%)</td><td>165.90 (+7.31%)</td><td>134.60 (-0.44%)</td><td>23.60 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>172.84 (n/a)</td><td>154.60 (n/a)</td><td>135.20 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+14.47%)</td><td>0.11 (+10.46%)</td><td>0.11 (+2.44%)</td><td>0.10 (+15.45%)</td><td>0.01 (+7.69%)</td><td>165.30 (-13.36%)</td><td>146.76 (-9.63%)</td><td>152.70 (-2.37%)</td><td>120.90 (-12.64%)</td><td>17.83 (-19.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>162.40 (n/a)</td><td>156.40 (n/a)</td><td>138.40 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (-2.69%)</td><td>0.09 (+1.22%)</td><td>0.09 (-3.95%)</td><td>0.08 (+14.25%)</td><td>0.01 <b>(-41.33%)</b></td><td>194.90 (-12.48%)</td><td>181.82 (-1.98%)</td><td>187.00 (+4.12%)</td><td>165.20 (+2.80%)</td><td>11.89 <b>(-48.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>185.50 (n/a)</td><td>179.60 (n/a)</td><td>160.70 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (-7.05%)</td><td>0.10 (+8.09%)</td><td>0.10 <b>(+22.19%)</b></td><td>0.07 (-2.96%)</td><td>0.02 <b>(-20.37%)</b></td><td>224.50 (+3.08%)</td><td>172.38 (-8.17%)</td><td>161.60 (-18.18%)</td><td>141.50 (+7.60%)</td><td>31.39 (-4.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.80 (n/a)</td><td>187.72 (n/a)</td><td>197.50 (n/a)</td><td>131.50 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 <b>(+27.96%)</b></td><td>0.11 (+17.96%)</td><td>0.10 (+6.90%)</td><td>0.08 (+19.69%)</td><td>0.03 <b>(+30.31%)</b></td><td>214.60 (-16.47%)</td><td>159.62 (-14.93%)</td><td>165.10 (-6.46%)</td><td>100.90 <b>(-21.84%)</b></td><td>42.53 (-17.95%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>256.90 (n/a)</td><td>187.64 (n/a)</td><td>176.50 (n/a)</td><td>129.10 (n/a)</td><td>51.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (+6.53%)</td><td>0.10 (+6.77%)</td><td>0.10 (+4.10%)</td><td>0.07 (-6.55%)</td><td>0.02 (+19.59%)</td><td>236.00 (+6.98%)</td><td>169.86 (-5.31%)</td><td>161.90 (-3.97%)</td><td>136.70 (-6.11%)</td><td>38.94 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.60 (n/a)</td><td>179.38 (n/a)</td><td>168.60 (n/a)</td><td>145.60 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.31 (+7.32%)</td><td>0.24 (+15.61%)</td><td>0.23 <b>(+26.63%)</b></td><td>0.19 <b>(+27.01%)</b></td><td>0.05 (-16.18%)</td><td>168.40 <b>(-21.23%)</b></td><td>143.22 (-15.58%)</td><td>142.60 <b>(-21.04%)</b></td><td>105.60 (-6.80%)</td><td>24.77 <b>(-38.24%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.80 (n/a)</td><td>169.66 (n/a)</td><td>180.60 (n/a)</td><td>113.30 (n/a)</td><td>40.11 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (+12.17%)</td><td>0.20 (+3.56%)</td><td>0.20 (+6.70%)</td><td>0.14 (-1.02%)</td><td>0.05 <b>(+35.14%)</b></td><td>228.00 (+1.02%)</td><td>173.56 (-1.59%)</td><td>164.40 (-6.27%)</td><td>116.40 (-10.80%)</td><td>41.41 <b>(+20.72%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.70 (n/a)</td><td>176.36 (n/a)</td><td>175.40 (n/a)</td><td>130.50 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (-13.51%)</td><td>0.14 (-6.92%)</td><td>0.15 (+0.23%)</td><td>0.12 (-6.87%)</td><td>0.02 <b>(-23.78%)</b></td><td>271.90 (+7.34%)</td><td>235.34 (+7.00%)</td><td>223.00 (-0.22%)</td><td>207.10 (+15.57%)</td><td>27.58 (-4.08%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>253.30 (n/a)</td><td>219.94 (n/a)</td><td>223.50 (n/a)</td><td>179.20 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (-16.51%)</td><td>0.17 (-1.57%)</td><td>0.16 (+3.04%)</td><td>0.13 (-2.56%)</td><td>0.03 <b>(-35.11%)</b></td><td>243.20 (+2.62%)</td><td>200.08 (-0.16%)</td><td>205.30 (-2.98%)</td><td>161.90 (+19.75%)</td><td>32.00 (-16.91%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.00 (n/a)</td><td>200.40 (n/a)</td><td>211.60 (n/a)</td><td>135.20 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (-7.21%)</td><td>0.21 (-1.42%)</td><td>0.21 (-6.63%)</td><td>0.17 (+13.82%)</td><td>0.03 <b>(-38.74%)</b></td><td>198.00 (-12.16%)</td><td>158.00 (-1.88%)</td><td>154.30 (+7.08%)</td><td>131.20 (+7.81%)</td><td>25.41 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.40 (n/a)</td><td>161.02 (n/a)</td><td>144.10 (n/a)</td><td>121.70 (n/a)</td><td>43.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (-10.99%)</td><td>0.21 (+1.41%)</td><td>0.21 (+3.31%)</td><td>0.15 (+5.68%)</td><td>0.05 (-12.65%)</td><td>218.20 (-5.38%)</td><td>162.34 (-2.33%)</td><td>156.20 (-3.22%)</td><td>124.90 (+12.42%)</td><td>39.34 (-8.62%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>230.60 (n/a)</td><td>166.22 (n/a)</td><td>161.40 (n/a)</td><td>111.10 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (+14.07%)</td><td>0.22 (+14.52%)</td><td>0.22 <b>(+26.10%)</b></td><td>0.17 (+4.43%)</td><td>0.03 <b>(+31.15%)</b></td><td>191.30 (-4.25%)</td><td>152.96 (-12.13%)</td><td>145.80 <b>(-20.67%)</b></td><td>131.90 (-12.36%)</td><td>25.04 (+11.85%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.80 (n/a)</td><td>174.08 (n/a)</td><td>183.80 (n/a)</td><td>150.50 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (+16.57%)</td><td>0.20 (-7.88%)</td><td>0.21 (-4.54%)</td><td>0.13 <b>(-30.00%)</b></td><td>0.07 <b>(+130.53%)</b></td><td>248.40 <b>(+42.84%)</b></td><td>176.98 (+17.88%)</td><td>157.90 (+4.78%)</td><td>110.70 (-14.25%)</td><td>61.29 <b>(+200.12%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>173.90 (n/a)</td><td>150.14 (n/a)</td><td>150.70 (n/a)</td><td>129.10 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (-14.62%)</td><td>0.20 (-3.03%)</td><td>0.19 (+10.73%)</td><td>0.14 (-12.53%)</td><td>0.04 <b>(-29.52%)</b></td><td>227.10 (+14.35%)</td><td>172.22 (+1.57%)</td><td>171.70 (-9.68%)</td><td>131.60 (+17.08%)</td><td>34.89 (-4.44%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>198.60 (n/a)</td><td>169.56 (n/a)</td><td>190.10 (n/a)</td><td>112.40 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (-16.55%)</td><td>0.20 (-9.73%)</td><td>0.21 (+1.40%)</td><td>0.15 <b>(-20.98%)</b></td><td>0.04 (-4.99%)</td><td>223.30 <b>(+26.52%)</b></td><td>168.74 (+11.91%)</td><td>152.90 (-1.35%)</td><td>133.20 (+19.78%)</td><td>38.05 <b>(+44.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>176.50 (n/a)</td><td>150.78 (n/a)</td><td>155.00 (n/a)</td><td>111.20 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+6.61%)</td><td>0.19 (+3.19%)</td><td>0.18 (-11.48%)</td><td>0.14 (+7.79%)</td><td>0.04 (+2.03%)</td><td>233.40 (-7.23%)</td><td>176.86 (-3.57%)</td><td>180.90 (+12.99%)</td><td>137.90 (-6.19%)</td><td>39.37 (-12.97%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>251.60 (n/a)</td><td>183.40 (n/a)</td><td>160.10 (n/a)</td><td>147.00 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+3.10%)</td><td>0.20 (+5.60%)</td><td>0.18 (-0.55%)</td><td>0.18 (+16.61%)</td><td>0.03 (-7.64%)</td><td>182.90 (-14.25%)</td><td>166.24 (-5.76%)</td><td>179.10 (+0.56%)</td><td>136.70 (-2.98%)</td><td>20.61 <b>(-21.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>176.40 (n/a)</td><td>178.10 (n/a)</td><td>140.90 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (+11.30%)</td><td>0.17 (+4.60%)</td><td>0.16 (+0.21%)</td><td>0.14 (+7.35%)</td><td>0.03 (-0.21%)</td><td>228.20 (-6.82%)</td><td>195.92 (-4.83%)</td><td>205.10 (-0.19%)</td><td>150.40 (-10.16%)</td><td>29.28 (-18.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.90 (n/a)</td><td>205.86 (n/a)</td><td>205.50 (n/a)</td><td>167.40 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (-4.09%)</td><td>0.19 (-0.25%)</td><td>0.19 (-0.73%)</td><td>0.15 (+7.88%)</td><td>0.04 <b>(-23.76%)</b></td><td>219.10 (-7.32%)</td><td>177.16 (-2.01%)</td><td>175.20 (+0.69%)</td><td>139.70 (+4.25%)</td><td>34.37 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.40 (n/a)</td><td>180.80 (n/a)</td><td>174.00 (n/a)</td><td>134.00 (n/a)</td><td>46.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (+3.84%)</td><td>0.18 (-0.01%)</td><td>0.17 (+12.11%)</td><td>0.15 (+0.70%)</td><td>0.03 (-19.01%)</td><td>220.90 (-0.72%)</td><td>184.96 (-1.50%)</td><td>188.60 (-10.79%)</td><td>138.10 (-3.70%)</td><td>30.37 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.50 (n/a)</td><td>187.78 (n/a)</td><td>211.40 (n/a)</td><td>143.40 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (+13.93%)</td><td>0.19 (+2.23%)</td><td>0.17 (+6.62%)</td><td>0.16 (+10.58%)</td><td>0.05 (+12.86%)</td><td>208.20 (-9.56%)</td><td>182.96 (-2.18%)</td><td>193.90 (-6.19%)</td><td>122.30 (-12.27%)</td><td>34.92 (-11.36%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.20 (n/a)</td><td>187.04 (n/a)</td><td>206.70 (n/a)</td><td>139.40 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (+0.91%)</td><td>0.21 (+0.19%)</td><td>0.21 (+0.01%)</td><td>0.20 (+0.00%)</td><td>0.00 <b>(+227.14%)</b></td><td>40926.30 (-0.00%)</td><td>40746.78 (-0.19%)</td><td>40814.60 (-0.01%)</td><td>40379.30 (-0.90%)</td><td>212.12 <b>(+223.72%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40927.60 (n/a)</td><td>40824.24 (n/a)</td><td>40820.60 (n/a)</td><td>40747.70 (n/a)</td><td>65.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (-0.59%)</td><td>0.21 (-0.10%)</td><td>0.21 (-0.09%)</td><td>0.21 (+0.13%)</td><td>0.00 <b>(-76.80%)</b></td><td>40884.00 (-0.13%)</td><td>40851.58 (+0.10%)</td><td>40864.40 (+0.08%)</td><td>40807.90 (+0.59%)</td><td>35.52 <b>(-76.70%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40938.90 (n/a)</td><td>40809.64 (n/a)</td><td>40829.70 (n/a)</td><td>40569.00 (n/a)</td><td>152.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-0.01%)</td><td>0.13 (+0.01%)</td><td>0.13 (+0.02%)</td><td>0.13 (+0.01%)</td><td>0.00 <b>(-45.50%)</b></td><td>321748.80 (-0.01%)</td><td>321699.70 (-0.01%)</td><td>321689.00 (-0.02%)</td><td>321662.60 (+0.01%)</td><td>32.89 <b>(-45.38%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321768.20 (n/a)</td><td>321722.80 (n/a)</td><td>321747.00 (n/a)</td><td>321620.10 (n/a)</td><td>60.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-7.12%)</td><td>0.03 (-15.18%)</td><td>0.02 <b>(-28.97%)</b></td><td>0.02 (-7.01%)</td><td>0.01 <b>(-20.23%)</b></td><td>192.70 (+7.53%)</td><td>159.62 (+16.56%)</td><td>166.70 <b>(+40.79%)</b></td><td>117.60 (+7.69%)</td><td>30.00 (-8.23%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.20 (n/a)</td><td>136.94 (n/a)</td><td>118.40 (n/a)</td><td>109.20 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-12.50%)</td><td>0.04 (-5.45%)</td><td>0.04 (-12.52%)</td><td>0.04 (+1.43%)</td><td>0.00 <b>(-50.83%)</b></td><td>164.20 (-1.38%)</td><td>147.22 (+4.01%)</td><td>149.40 (+14.31%)</td><td>129.80 (+14.26%)</td><td>12.61 <b>(-46.97%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>166.50 (n/a)</td><td>141.54 (n/a)</td><td>130.70 (n/a)</td><td>113.60 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-12.61%)</td><td>0.03 (-15.09%)</td><td>0.03 (-19.12%)</td><td>0.02 (-16.43%)</td><td>0.01 (-1.91%)</td><td>248.90 (+19.66%)</td><td>171.10 (+19.53%)</td><td>154.20 <b>(+23.66%)</b></td><td>125.00 (+14.47%)</td><td>53.00 <b>(+30.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>143.14 (n/a)</td><td>124.70 (n/a)</td><td>109.20 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (-4.51%)</td><td>0.03 (-3.58%)</td><td>0.03 (+6.59%)</td><td>0.02 (-13.18%)</td><td>0.01 <b>(+24.15%)</b></td><td>225.00 (+15.15%)</td><td>169.06 (+5.76%)</td><td>153.50 (-6.17%)</td><td>129.40 (+4.69%)</td><td>39.68 <b>(+53.36%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.40 (n/a)</td><td>159.86 (n/a)</td><td>163.60 (n/a)</td><td>123.60 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (+12.48%)</td><td>0.03 (-5.97%)</td><td>0.02 (-10.07%)</td><td>0.02 (-17.40%)</td><td>0.01 <b>(+114.46%)</b></td><td>201.20 <b>(+21.06%)</b></td><td>164.06 (+10.84%)</td><td>164.50 (+11.15%)</td><td>109.00 (-11.09%)</td><td>39.01 <b>(+140.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.20 (n/a)</td><td>148.02 (n/a)</td><td>148.00 (n/a)</td><td>122.60 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (+6.35%)</td><td>0.03 (+10.69%)</td><td>0.03 (+13.12%)</td><td>0.03 (+11.11%)</td><td>0.00 (-2.79%)</td><td>192.10 (-9.98%)</td><td>167.18 (-9.89%)</td><td>160.10 (-11.60%)</td><td>145.50 (-5.95%)</td><td>19.38 (-17.59%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>185.52 (n/a)</td><td>181.10 (n/a)</td><td>154.70 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+0.26%)</td><td>0.02 (+1.34%)</td><td>0.02 (-11.58%)</td><td>0.02 <b>(+27.20%)</b></td><td>0.01 (-6.52%)</td><td>211.20 <b>(-21.37%)</b></td><td>174.58 (-3.14%)</td><td>190.50 (+13.12%)</td><td>127.00 (-0.24%)</td><td>36.99 <b>(-29.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>180.24 (n/a)</td><td>168.40 (n/a)</td><td>127.30 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+4.81%)</td><td>0.03 (-0.53%)</td><td>0.03 (+4.45%)</td><td>0.02 (+3.89%)</td><td>0.00 (+18.72%)</td><td>205.30 (-3.71%)</td><td>172.20 (+0.97%)</td><td>159.40 (-4.26%)</td><td>145.60 (-4.65%)</td><td>27.08 (+9.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.20 (n/a)</td><td>170.54 (n/a)</td><td>166.50 (n/a)</td><td>152.70 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-1.13%)</td><td>0.02 (+3.79%)</td><td>0.02 (-3.80%)</td><td>0.01 <b>(+32.91%)</b></td><td>0.01 (-18.07%)</td><td>292.20 <b>(-24.77%)</b></td><td>183.78 (-10.02%)</td><td>171.90 (+3.99%)</td><td>135.20 (+1.12%)</td><td>62.76 <b>(-39.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>388.40 (n/a)</td><td>204.24 (n/a)</td><td>165.30 (n/a)</td><td>133.70 (n/a)</td><td>104.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (-12.43%)</td><td>0.03 (+8.63%)</td><td>0.03 <b>(+24.39%)</b></td><td>0.02 (+13.65%)</td><td>0.00 <b>(-45.50%)</b></td><td>192.80 (-12.00%)</td><td>163.86 (-10.78%)</td><td>157.40 (-19.61%)</td><td>135.90 (+14.20%)</td><td>22.27 <b>(-42.33%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>183.66 (n/a)</td><td>195.80 (n/a)</td><td>119.00 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+18.49%)</td><td>0.02 (-6.19%)</td><td>0.02 (-10.76%)</td><td>0.01 <b>(-25.51%)</b></td><td>0.01 <b>(+152.42%)</b></td><td>276.60 <b>(+34.27%)</b></td><td>210.80 (+11.82%)</td><td>217.00 (+12.03%)</td><td>133.70 (-15.59%)</td><td>51.20 <b>(+175.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>188.52 (n/a)</td><td>193.70 (n/a)</td><td>158.40 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+10.64%)</td><td>0.02 (+4.90%)</td><td>0.02 (+0.45%)</td><td>0.02 (-5.24%)</td><td>0.00 <b>(+37.33%)</b></td><td>243.00 (+5.51%)</td><td>195.64 (-3.86%)</td><td>193.60 (-0.41%)</td><td>161.30 (-9.64%)</td><td>31.55 <b>(+28.85%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.30 (n/a)</td><td>203.50 (n/a)</td><td>194.40 (n/a)</td><td>178.50 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (+3.44%)</td><td>0.03 (+5.19%)</td><td>0.02 (-4.27%)</td><td>0.02 (+10.35%)</td><td>0.00 <b>(-31.06%)</b></td><td>187.10 (-9.39%)</td><td>164.12 (-6.12%)</td><td>165.20 (+4.49%)</td><td>145.40 (-3.32%)</td><td>17.00 <b>(-41.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>174.82 (n/a)</td><td>158.10 (n/a)</td><td>150.40 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 <b>(+39.90%)</b></td><td>0.02 (+8.85%)</td><td>0.02 (+1.70%)</td><td>0.02 (-14.63%)</td><td>0.01 <b>(+147.02%)</b></td><td>268.60 (+17.14%)</td><td>194.00 (-3.04%)</td><td>186.70 (-1.63%)</td><td>124.90 <b>(-28.51%)</b></td><td>55.19 <b>(+103.02%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.30 (n/a)</td><td>200.08 (n/a)</td><td>189.80 (n/a)</td><td>174.70 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (+15.85%)</td><td>0.02 <b>(+22.83%)</b></td><td>0.02 (+18.00%)</td><td>0.02 <b>(+42.48%)</b></td><td>0.00 <b>(-22.02%)</b></td><td>232.70 <b>(-29.80%)</b></td><td>212.04 <b>(-20.17%)</b></td><td>214.40 (-15.26%)</td><td>173.00 (-13.67%)</td><td>24.02 <b>(-53.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>331.50 (n/a)</td><td>265.60 (n/a)</td><td>253.00 (n/a)</td><td>200.40 (n/a)</td><td>51.64 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+16.91%)</td><td>0.05 (+3.98%)</td><td>0.05 (+5.64%)</td><td>0.04 (-2.40%)</td><td>0.01 <b>(+45.00%)</b></td><td>189.30 (+2.44%)</td><td>155.94 (-1.99%)</td><td>158.90 (-5.30%)</td><td>110.90 (-14.49%)</td><td>33.65 <b>(+31.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>159.10 (n/a)</td><td>167.80 (n/a)</td><td>129.70 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 <b>(-27.36%)</b></td><td>0.07 (-7.83%)</td><td>0.08 (+8.20%)</td><td>0.06 (-12.05%)</td><td>0.01 <b>(-42.81%)</b></td><td>222.60 (+13.69%)</td><td>171.76 (+6.68%)</td><td>156.50 (-7.62%)</td><td>152.50 <b>(+37.64%)</b></td><td>29.59 (-6.04%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>161.00 (n/a)</td><td>169.40 (n/a)</td><td>110.80 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-9.64%)</td><td>0.05 (-2.80%)</td><td>0.05 (-6.28%)</td><td>0.04 (+3.50%)</td><td>0.01 <b>(-21.25%)</b></td><td>193.30 (-3.40%)</td><td>168.08 (+2.19%)</td><td>176.60 (+6.71%)</td><td>145.00 (+10.60%)</td><td>21.07 (-17.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>164.48 (n/a)</td><td>165.50 (n/a)</td><td>131.10 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (-7.86%)</td><td>0.06 (-9.81%)</td><td>0.06 (-2.15%)</td><td>0.03 <b>(-26.86%)</b></td><td>0.01 <b>(+46.78%)</b></td><td>295.20 <b>(+36.73%)</b></td><td>196.92 (+15.77%)</td><td>172.80 (+2.19%)</td><td>149.60 (+8.56%)</td><td>60.78 <b>(+111.49%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>170.10 (n/a)</td><td>169.10 (n/a)</td><td>137.80 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (+4.39%)</td><td>0.05 (+0.98%)</td><td>0.05 (-3.48%)</td><td>0.03 (+12.24%)</td><td>0.01 (+5.89%)</td><td>236.10 (-10.91%)</td><td>180.16 (-1.17%)</td><td>167.00 (+3.60%)</td><td>127.50 (-4.14%)</td><td>45.63 (-10.24%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.00 (n/a)</td><td>182.30 (n/a)</td><td>161.20 (n/a)</td><td>133.00 (n/a)</td><td>50.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-16.53%)</td><td>0.05 (-10.96%)</td><td>0.06 (-1.77%)</td><td>0.04 (-13.43%)</td><td>0.01 (-19.42%)</td><td>281.90 (+15.49%)</td><td>204.16 (+12.04%)</td><td>185.30 (+1.81%)</td><td>177.20 (+19.81%)</td><td>44.10 (+14.43%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>182.22 (n/a)</td><td>182.00 (n/a)</td><td>147.90 (n/a)</td><td>38.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (+13.68%)</td><td>0.05 (+4.26%)</td><td>0.04 (-4.57%)</td><td>0.03 (-7.57%)</td><td>0.01 <b>(+37.00%)</b></td><td>236.90 (+8.22%)</td><td>182.36 (-1.87%)</td><td>191.00 (+4.77%)</td><td>115.60 (-12.02%)</td><td>44.61 <b>(+23.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>185.84 (n/a)</td><td>182.30 (n/a)</td><td>131.40 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 <b>(-20.07%)</b></td><td>0.05 (-17.83%)</td><td>0.04 (-15.42%)</td><td>0.04 (-2.27%)</td><td>0.01 <b>(-45.62%)</b></td><td>249.40 (+2.30%)</td><td>202.56 (+17.63%)</td><td>209.30 (+18.25%)</td><td>158.80 <b>(+25.14%)</b></td><td>33.51 <b>(-28.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>172.20 (n/a)</td><td>177.00 (n/a)</td><td>126.90 (n/a)</td><td>47.12 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-11.79%)</td><td>0.04 (-15.77%)</td><td>0.04 (-13.54%)</td><td>0.03 <b>(-28.49%)</b></td><td>0.01 (+19.40%)</td><td>252.50 <b>(+39.89%)</b></td><td>198.16 <b>(+20.61%)</b></td><td>198.70 (+15.66%)</td><td>149.40 (+13.35%)</td><td>36.99 <b>(+92.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>164.30 (n/a)</td><td>171.80 (n/a)</td><td>131.80 (n/a)</td><td>19.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-8.62%)</td><td>0.05 (-9.49%)</td><td>0.05 (-8.84%)</td><td>0.03 (-16.45%)</td><td>0.01 (+6.95%)</td><td>297.50 (+19.72%)</td><td>194.96 (+12.65%)</td><td>184.50 (+9.69%)</td><td>148.30 (+9.45%)</td><td>60.95 <b>(+36.45%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>173.06 (n/a)</td><td>168.20 (n/a)</td><td>135.50 (n/a)</td><td>44.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (-1.42%)</td><td>0.05 (+0.83%)</td><td>0.05 (+13.46%)</td><td>0.04 (-9.88%)</td><td>0.01 <b>(+39.86%)</b></td><td>224.50 (+10.97%)</td><td>179.52 (+1.41%)</td><td>158.40 (-11.85%)</td><td>140.10 (+1.45%)</td><td>40.35 <b>(+69.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>177.02 (n/a)</td><td>179.70 (n/a)</td><td>138.10 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 <b>(-42.36%)</b></td><td>0.04 <b>(-31.13%)</b></td><td>0.04 <b>(-21.72%)</b></td><td>0.02 <b>(-45.10%)</b></td><td>0.01 <b>(-40.83%)</b></td><td>377.50 <b>(+82.10%)</b></td><td>244.88 <b>(+46.69%)</b></td><td>217.40 <b>(+27.73%)</b></td><td>190.70 <b>(+73.52%)</b></td><td>75.35 <b>(+105.27%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>166.94 (n/a)</td><td>170.20 (n/a)</td><td>109.90 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-5.52%)</td><td>0.04 (+1.38%)</td><td>0.04 (-0.66%)</td><td>0.04 (+16.05%)</td><td>0.01 <b>(-27.56%)</b></td><td>217.20 (-13.81%)</td><td>186.10 (-2.92%)</td><td>187.90 (+0.64%)</td><td>153.30 (+5.87%)</td><td>25.09 <b>(-34.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.00 (n/a)</td><td>191.70 (n/a)</td><td>186.70 (n/a)</td><td>144.80 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-15.08%)</td><td>0.04 (-4.50%)</td><td>0.04 (-8.42%)</td><td>0.04 (+3.17%)</td><td>0.00 <b>(-59.77%)</b></td><td>224.90 (-3.06%)</td><td>202.76 (+2.99%)</td><td>201.90 (+9.19%)</td><td>187.60 (+17.77%)</td><td>14.10 <b>(-55.02%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>196.88 (n/a)</td><td>184.90 (n/a)</td><td>159.30 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (-7.66%)</td><td>0.04 (-5.63%)</td><td>0.04 (-1.62%)</td><td>0.03 (-4.79%)</td><td>0.01 (-16.85%)</td><td>251.00 (+5.06%)</td><td>216.78 (+5.44%)</td><td>208.00 (+1.66%)</td><td>172.50 (+8.29%)</td><td>32.02 (-6.32%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>205.60 (n/a)</td><td>204.60 (n/a)</td><td>159.30 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-7.16%)</td><td>0.10 (+19.38%)</td><td>0.09 (+15.10%)</td><td>0.08 <b>(+98.71%)</b></td><td>0.01 <b>(-55.52%)</b></td><td>200.00 <b>(-49.69%)</b></td><td>171.62 <b>(-25.28%)</b></td><td>174.80 (-13.12%)</td><td>142.80 (+7.69%)</td><td>23.13 <b>(-77.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>397.50 (n/a)</td><td>229.68 (n/a)</td><td>201.20 (n/a)</td><td>132.60 (n/a)</td><td>100.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 <b>(-30.05%)</b></td><td>0.13 (-15.20%)</td><td>0.13 (-15.85%)</td><td>0.12 (+8.56%)</td><td>0.01 <b>(-74.56%)</b></td><td>204.40 (-7.89%)</td><td>184.50 (+11.91%)</td><td>186.20 (+18.83%)</td><td>165.80 <b>(+42.93%)</b></td><td>14.60 <b>(-66.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>221.90 (n/a)</td><td>164.86 (n/a)</td><td>156.70 (n/a)</td><td>116.00 (n/a)</td><td>44.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+23.46%)</b></td><td>0.09 (-3.90%)</td><td>0.09 (-8.31%)</td><td>0.07 <b>(-20.60%)</b></td><td>0.03 <b>(+156.63%)</b></td><td>238.50 <b>(+25.92%)</b></td><td>185.34 (+8.78%)</td><td>186.20 (+9.08%)</td><td>122.00 (-18.99%)</td><td>44.48 <b>(+156.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>170.38 (n/a)</td><td>170.70 (n/a)</td><td>150.60 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(-24.99%)</b></td><td>0.11 (-16.80%)</td><td>0.11 (-18.96%)</td><td>0.10 (-4.06%)</td><td>0.01 <b>(-56.74%)</b></td><td>199.00 (+4.24%)</td><td>181.54 (+18.17%)</td><td>181.20 <b>(+23.35%)</b></td><td>159.80 <b>(+33.39%)</b></td><td>15.73 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>153.62 (n/a)</td><td>146.90 (n/a)</td><td>119.80 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+23.44%)</b></td><td>0.10 (+10.54%)</td><td>0.10 (+12.04%)</td><td>0.08 (+4.71%)</td><td>0.02 <b>(+75.61%)</b></td><td>214.30 (-4.50%)</td><td>173.92 (-7.79%)</td><td>167.40 (-10.77%)</td><td>124.80 (-19.01%)</td><td>33.96 <b>(+35.01%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>188.62 (n/a)</td><td>187.60 (n/a)</td><td>154.10 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(-24.93%)</b></td><td>0.11 (-15.99%)</td><td>0.10 (-14.61%)</td><td>0.10 (-10.51%)</td><td>0.01 <b>(-49.16%)</b></td><td>207.60 (+11.73%)</td><td>190.48 (+16.97%)</td><td>202.10 (+17.09%)</td><td>157.70 <b>(+33.19%)</b></td><td>21.41 <b>(-24.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>185.80 (n/a)</td><td>162.84 (n/a)</td><td>172.60 (n/a)</td><td>118.40 (n/a)</td><td>28.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(+27.29%)</b></td><td>0.11 <b>(+21.44%)</b></td><td>0.11 <b>(+31.71%)</b></td><td>0.09 (+6.85%)</td><td>0.02 <b>(+121.74%)</b></td><td>189.20 (-6.43%)</td><td>158.36 (-16.26%)</td><td>149.90 <b>(-24.06%)</b></td><td>128.00 <b>(-21.47%)</b></td><td>27.03 <b>(+68.11%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>189.12 (n/a)</td><td>197.40 (n/a)</td><td>163.00 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 <b>(-26.64%)</b></td><td>0.10 (-15.63%)</td><td>0.10 (-13.11%)</td><td>0.09 (+0.50%)</td><td>0.01 <b>(-62.31%)</b></td><td>212.20 (-0.52%)</td><td>183.22 (+15.23%)</td><td>178.00 (+15.06%)</td><td>165.50 <b>(+36.33%)</b></td><td>17.65 <b>(-48.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>213.30 (n/a)</td><td>159.00 (n/a)</td><td>154.70 (n/a)</td><td>121.40 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-18.80%)</td><td>0.11 (+0.29%)</td><td>0.11 (+18.90%)</td><td>0.09 (+9.97%)</td><td>0.01 <b>(-57.48%)</b></td><td>182.40 (-9.03%)</td><td>153.50 (-4.86%)</td><td>147.20 (-15.89%)</td><td>130.30 <b>(+23.16%)</b></td><td>19.38 <b>(-52.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>161.34 (n/a)</td><td>175.00 (n/a)</td><td>105.80 (n/a)</td><td>40.79 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 <b>(-24.65%)</b></td><td>0.10 (-12.82%)</td><td>0.11 (-10.05%)</td><td>0.08 (-10.96%)</td><td>0.02 <b>(-38.61%)</b></td><td>231.90 (+12.30%)</td><td>187.82 (+12.64%)</td><td>175.40 (+11.15%)</td><td>155.20 <b>(+32.65%)</b></td><td>32.99 (-9.53%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>206.50 (n/a)</td><td>166.74 (n/a)</td><td>157.80 (n/a)</td><td>117.00 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (+17.71%)</td><td>0.11 <b>(+22.88%)</b></td><td>0.11 <b>(+23.72%)</b></td><td>0.10 <b>(+34.71%)</b></td><td>0.01 <b>(-29.26%)</b></td><td>161.20 <b>(-25.78%)</b></td><td>148.66 (-19.43%)</td><td>153.80 (-19.18%)</td><td>135.00 (-15.04%)</td><td>11.34 <b>(-54.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>184.50 (n/a)</td><td>190.30 (n/a)</td><td>158.90 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-8.73%)</td><td>0.09 (-1.73%)</td><td>0.09 (-2.58%)</td><td>0.08 <b>(+52.92%)</b></td><td>0.01 <b>(-59.46%)</b></td><td>209.30 <b>(-34.61%)</b></td><td>189.50 (-5.12%)</td><td>195.20 (+2.68%)</td><td>157.00 (+9.56%)</td><td>19.49 <b>(-72.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>320.10 (n/a)</td><td>199.72 (n/a)</td><td>190.10 (n/a)</td><td>143.30 (n/a)</td><td>70.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (+7.58%)</td><td>0.11 (+15.60%)</td><td>0.11 (+11.30%)</td><td>0.10 <b>(+58.65%)</b></td><td>0.01 <b>(-57.15%)</b></td><td>165.80 <b>(-36.96%)</b></td><td>153.54 (-16.59%)</td><td>153.80 (-10.11%)</td><td>136.30 (-7.09%)</td><td>11.01 <b>(-76.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>263.00 (n/a)</td><td>184.08 (n/a)</td><td>171.10 (n/a)</td><td>146.70 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (-11.89%)</td><td>0.09 (+4.10%)</td><td>0.09 (-0.64%)</td><td>0.08 <b>(+43.01%)</b></td><td>0.01 <b>(-53.54%)</b></td><td>207.50 <b>(-30.09%)</b></td><td>186.44 (-9.58%)</td><td>194.70 (+0.62%)</td><td>151.80 (+13.45%)</td><td>23.01 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>296.80 (n/a)</td><td>206.20 (n/a)</td><td>193.50 (n/a)</td><td>133.80 (n/a)</td><td>62.77 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 <b>(+22.25%)</b></td><td>0.09 (+18.44%)</td><td>0.09 <b>(+24.86%)</b></td><td>0.07 (+3.42%)</td><td>0.02 <b>(+31.15%)</b></td><td>239.10 (-3.32%)</td><td>180.56 (-14.90%)</td><td>174.40 (-19.89%)</td><td>145.20 (-18.20%)</td><td>34.90 (+9.35%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>212.18 (n/a)</td><td>217.70 (n/a)</td><td>177.50 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (+0.51%)</td><td>0.21 (+5.16%)</td><td>0.21 (+17.58%)</td><td>0.16 (-3.44%)</td><td>0.03 (-13.96%)</td><td>205.40 (+3.58%)</td><td>158.24 (-5.43%)</td><td>154.50 (-14.97%)</td><td>132.40 (-0.53%)</td><td>27.94 (-6.43%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.30 (n/a)</td><td>167.32 (n/a)</td><td>181.70 (n/a)</td><td>133.10 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (+11.85%)</td><td>0.22 (+10.01%)</td><td>0.25 (+14.62%)</td><td>0.14 (+3.57%)</td><td>0.05 <b>(+30.57%)</b></td><td>232.60 (-3.45%)</td><td>158.90 (-7.48%)</td><td>132.20 (-12.74%)</td><td>123.40 (-10.58%)</td><td>46.63 (+10.34%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>240.90 (n/a)</td><td>171.74 (n/a)</td><td>151.50 (n/a)</td><td>138.00 (n/a)</td><td>42.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.33 (+5.79%)</td><td>0.24 (-0.72%)</td><td>0.23 (+0.87%)</td><td>0.19 (+1.41%)</td><td>0.06 (+9.62%)</td><td>219.80 (-1.39%)</td><td>179.96 (+1.06%)</td><td>182.00 (-0.87%)</td><td>124.50 (-5.47%)</td><td>36.04 (+0.27%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>222.90 (n/a)</td><td>178.08 (n/a)</td><td>183.60 (n/a)</td><td>131.70 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (-16.94%)</td><td>0.18 (-9.49%)</td><td>0.20 (+1.55%)</td><td>0.11 (-18.91%)</td><td>0.06 (-2.44%)</td><td>310.90 <b>(+23.32%)</b></td><td>200.70 (+13.87%)</td><td>163.70 (-1.50%)</td><td>135.50 <b>(+20.44%)</b></td><td>74.40 <b>(+46.22%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>252.10 (n/a)</td><td>176.26 (n/a)</td><td>166.20 (n/a)</td><td>112.50 (n/a)</td><td>50.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 <b>(-25.59%)</b></td><td>0.22 (-17.69%)</td><td>0.22 (-16.86%)</td><td>0.20 (-8.17%)</td><td>0.02 <b>(-61.13%)</b></td><td>202.70 (+8.86%)</td><td>186.72 (+19.57%)</td><td>187.20 <b>(+20.31%)</b></td><td>165.80 <b>(+34.36%)</b></td><td>13.81 <b>(-43.52%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>186.20 (n/a)</td><td>156.16 (n/a)</td><td>155.60 (n/a)</td><td>123.40 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 <b>(+26.11%)</b></td><td>0.19 (+5.49%)</td><td>0.18 (+0.48%)</td><td>0.14 (-14.11%)</td><td>0.05 <b>(+198.12%)</b></td><td>236.10 (+16.42%)</td><td>180.22 (-1.25%)</td><td>186.20 (-0.48%)</td><td>128.00 <b>(-20.69%)</b></td><td>42.61 <b>(+172.87%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>182.50 (n/a)</td><td>187.10 (n/a)</td><td>161.40 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.31 (+0.54%)</td><td>0.23 (+8.59%)</td><td>0.20 (-1.04%)</td><td>0.15 (+7.53%)</td><td>0.07 (+3.57%)</td><td>243.80 (-7.02%)</td><td>172.20 (-8.23%)</td><td>182.20 (+1.05%)</td><td>119.60 (-0.58%)</td><td>50.99 (-8.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>262.20 (n/a)</td><td>187.64 (n/a)</td><td>180.30 (n/a)</td><td>120.30 (n/a)</td><td>55.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (+16.34%)</td><td>0.21 (+4.18%)</td><td>0.22 (+8.58%)</td><td>0.16 (-12.71%)</td><td>0.04 <b>(+127.85%)</b></td><td>211.00 (+14.55%)</td><td>163.84 (-1.54%)</td><td>149.20 (-7.90%)</td><td>126.70 (-14.04%)</td><td>33.23 <b>(+125.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>184.20 (n/a)</td><td>166.40 (n/a)</td><td>162.00 (n/a)</td><td>147.40 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 <b>(-29.28%)</b></td><td>0.18 (-19.09%)</td><td>0.17 <b>(-20.78%)</b></td><td>0.16 (+3.48%)</td><td>0.03 <b>(-55.99%)</b></td><td>232.50 (-3.37%)</td><td>206.88 (+18.91%)</td><td>220.00 <b>(+26.22%)</b></td><td>170.20 <b>(+41.36%)</b></td><td>27.29 <b>(-39.53%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>240.60 (n/a)</td><td>173.98 (n/a)</td><td>174.30 (n/a)</td><td>120.40 (n/a)</td><td>45.14 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (-7.22%)</td><td>0.19 (+5.54%)</td><td>0.19 (+7.10%)</td><td>0.18 (+15.89%)</td><td>0.01 <b>(-63.38%)</b></td><td>179.00 (-13.69%)</td><td>169.32 (-6.16%)</td><td>168.60 (-6.64%)</td><td>161.80 (+7.79%)</td><td>7.17 <b>(-65.59%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>180.44 (n/a)</td><td>180.60 (n/a)</td><td>150.10 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (+19.66%)</td><td>0.19 (+4.16%)</td><td>0.19 (+3.64%)</td><td>0.14 (-11.13%)</td><td>0.05 <b>(+110.17%)</b></td><td>253.00 (+12.54%)</td><td>194.92 (+0.93%)</td><td>184.60 (-3.50%)</td><td>133.20 (-16.44%)</td><td>54.98 <b>(+105.54%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>224.80 (n/a)</td><td>193.12 (n/a)</td><td>191.30 (n/a)</td><td>159.40 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 <b>(+29.74%)</b></td><td>0.17 (-3.43%)</td><td>0.16 (-13.47%)</td><td>0.11 <b>(-29.47%)</b></td><td>0.07 <b>(+204.54%)</b></td><td>305.00 <b>(+41.79%)</b></td><td>209.62 (+14.02%)</td><td>208.80 (+15.61%)</td><td>119.80 <b>(-22.91%)</b></td><td>73.17 <b>(+229.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>183.84 (n/a)</td><td>180.60 (n/a)</td><td>155.40 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (-2.96%)</td><td>0.17 (-10.10%)</td><td>0.18 (+2.05%)</td><td>0.10 <b>(-37.82%)</b></td><td>0.05 <b>(+74.03%)</b></td><td>342.20 <b>(+60.81%)</b></td><td>222.56 (+17.94%)</td><td>194.20 (-2.02%)</td><td>159.60 (+3.03%)</td><td>73.68 <b>(+191.33%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>212.80 (n/a)</td><td>188.70 (n/a)</td><td>198.20 (n/a)</td><td>154.90 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (+4.89%)</td><td>0.18 (+14.03%)</td><td>0.18 <b>(+23.33%)</b></td><td>0.17 <b>(+25.06%)</b></td><td>0.01 <b>(-49.30%)</b></td><td>189.40 <b>(-20.02%)</b></td><td>177.98 (-13.59%)</td><td>180.00 (-18.92%)</td><td>158.50 (-4.63%)</td><td>11.57 <b>(-61.82%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.80 (n/a)</td><td>205.96 (n/a)</td><td>222.00 (n/a)</td><td>166.20 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (-4.29%)</td><td>0.14 (+5.25%)</td><td>0.13 (+3.40%)</td><td>0.12 (+17.73%)</td><td>0.02 <b>(-30.32%)</b></td><td>166.90 (-15.11%)</td><td>150.38 (-6.49%)</td><td>156.40 (-3.28%)</td><td>126.20 (+4.47%)</td><td>18.46 <b>(-37.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>196.60 (n/a)</td><td>160.82 (n/a)</td><td>161.70 (n/a)</td><td>120.80 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (+19.22%)</td><td>0.12 (+15.33%)</td><td>0.12 (-2.45%)</td><td>0.11 <b>(+75.35%)</b></td><td>0.02 <b>(-36.77%)</b></td><td>189.70 <b>(-42.98%)</b></td><td>168.40 (-19.33%)</td><td>168.40 (+2.50%)</td><td>129.70 (-16.11%)</td><td>24.06 <b>(-68.92%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>332.70 (n/a)</td><td>208.74 (n/a)</td><td>164.30 (n/a)</td><td>154.60 (n/a)</td><td>77.40 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (-0.84%)</td><td>0.14 (+0.92%)</td><td>0.13 (-7.30%)</td><td>0.12 (+18.94%)</td><td>0.02 <b>(-29.97%)</b></td><td>171.40 (-15.94%)</td><td>153.80 (-3.22%)</td><td>162.40 (+7.84%)</td><td>119.90 (+0.84%)</td><td>20.32 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>158.92 (n/a)</td><td>150.60 (n/a)</td><td>118.90 (n/a)</td><td>35.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (+3.68%)</td><td>0.13 (+7.55%)</td><td>0.13 (+13.26%)</td><td>0.12 (+18.81%)</td><td>0.02 <b>(-23.16%)</b></td><td>177.80 (-15.85%)</td><td>153.84 (-8.19%)</td><td>153.10 (-11.71%)</td><td>131.80 (-3.51%)</td><td>19.00 <b>(-36.66%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>211.30 (n/a)</td><td>167.56 (n/a)</td><td>173.40 (n/a)</td><td>136.60 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-8.56%)</td><td>0.12 (-2.91%)</td><td>0.12 (-1.59%)</td><td>0.09 (-8.73%)</td><td>0.02 (-14.43%)</td><td>219.60 (+9.53%)</td><td>175.24 (+2.73%)</td><td>175.10 (+1.57%)</td><td>139.40 (+9.33%)</td><td>29.09 (+5.77%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>170.58 (n/a)</td><td>172.40 (n/a)</td><td>127.50 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+0.97%)</td><td>0.12 (+1.69%)</td><td>0.12 (-5.07%)</td><td>0.10 (+16.32%)</td><td>0.02 (-12.22%)</td><td>213.50 (-14.05%)</td><td>173.66 (-2.93%)</td><td>176.60 (+5.37%)</td><td>143.00 (-0.97%)</td><td>28.79 <b>(-29.26%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>248.40 (n/a)</td><td>178.90 (n/a)</td><td>167.60 (n/a)</td><td>144.40 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-3.74%)</td><td>0.10 (-9.06%)</td><td>0.10 (-12.07%)</td><td>0.08 (-13.27%)</td><td>0.02 (+13.36%)</td><td>256.90 (+15.31%)</td><td>204.98 (+10.88%)</td><td>204.70 (+13.72%)</td><td>159.10 (+3.92%)</td><td>35.69 <b>(+34.77%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.80 (n/a)</td><td>184.86 (n/a)</td><td>180.00 (n/a)</td><td>153.10 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 <b>(-39.41%)</b></td><td>0.11 (-15.39%)</td><td>0.10 (-10.11%)</td><td>0.08 (+0.58%)</td><td>0.02 <b>(-59.55%)</b></td><td>255.00 (-0.58%)</td><td>198.98 (+9.90%)</td><td>204.00 (+11.23%)</td><td>158.60 <b>(+65.04%)</b></td><td>39.70 <b>(-31.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>256.50 (n/a)</td><td>181.06 (n/a)</td><td>183.40 (n/a)</td><td>96.10 (n/a)</td><td>57.56 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (+6.16%)</td><td>0.16 (+4.15%)</td><td>0.16 (+8.28%)</td><td>0.12 (-4.51%)</td><td>0.04 (+13.48%)</td><td>209.10 (+4.76%)</td><td>160.32 (-3.27%)</td><td>156.20 (-7.63%)</td><td>114.80 (-5.82%)</td><td>33.92 (+11.67%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.60 (n/a)</td><td>165.74 (n/a)</td><td>169.10 (n/a)</td><td>121.90 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-11.93%)</td><td>0.13 (-13.91%)</td><td>0.14 (-11.31%)</td><td>0.08 <b>(-29.80%)</b></td><td>0.03 <b>(+27.68%)</b></td><td>313.60 <b>(+42.48%)</b></td><td>203.02 <b>(+20.24%)</b></td><td>177.40 (+12.78%)</td><td>165.60 (+13.50%)</td><td>62.41 <b>(+108.78%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>168.84 (n/a)</td><td>157.30 (n/a)</td><td>145.90 (n/a)</td><td>29.89 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (+0.51%)</td><td>0.16 (-0.56%)</td><td>0.14 (+2.71%)</td><td>0.13 (-0.30%)</td><td>0.03 (-13.64%)</td><td>182.10 (+0.28%)</td><td>157.70 (-0.15%)</td><td>170.50 (-2.63%)</td><td>124.80 (-0.48%)</td><td>24.76 (-13.64%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>181.60 (n/a)</td><td>157.94 (n/a)</td><td>175.10 (n/a)</td><td>125.40 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (+17.03%)</td><td>0.15 (+5.77%)</td><td>0.14 (+5.64%)</td><td>0.10 (-4.60%)</td><td>0.04 <b>(+26.06%)</b></td><td>237.60 (+4.81%)</td><td>177.06 (-4.34%)</td><td>170.90 (-5.32%)</td><td>121.50 (-14.50%)</td><td>41.78 (+8.99%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>226.70 (n/a)</td><td>185.10 (n/a)</td><td>180.50 (n/a)</td><td>142.10 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (+2.39%)</td><td>0.13 (-7.52%)</td><td>0.14 (+3.86%)</td><td>0.07 <b>(-38.69%)</b></td><td>0.04 <b>(+51.72%)</b></td><td>344.70 <b>(+63.13%)</b></td><td>205.02 (+16.59%)</td><td>179.50 (-3.75%)</td><td>127.50 (-2.37%)</td><td>82.31 <b>(+160.18%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.30 (n/a)</td><td>175.84 (n/a)</td><td>186.50 (n/a)</td><td>130.60 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (+10.37%)</td><td>0.16 (-2.29%)</td><td>0.16 (-7.82%)</td><td>0.11 (-18.36%)</td><td>0.04 <b>(+65.29%)</b></td><td>217.70 <b>(+22.51%)</b></td><td>159.50 (+5.46%)</td><td>157.40 (+8.55%)</td><td>116.20 (-9.36%)</td><td>38.77 <b>(+81.98%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.70 (n/a)</td><td>151.24 (n/a)</td><td>145.00 (n/a)</td><td>128.20 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (-11.18%)</td><td>0.13 (+2.71%)</td><td>0.12 (+0.56%)</td><td>0.10 (+17.12%)</td><td>0.03 <b>(-26.36%)</b></td><td>241.10 (-14.62%)</td><td>191.14 (-5.99%)</td><td>205.30 (-0.53%)</td><td>135.80 (+12.60%)</td><td>43.09 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>282.40 (n/a)</td><td>203.32 (n/a)</td><td>206.40 (n/a)</td><td>120.60 (n/a)</td><td>59.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (-13.29%)</td><td>0.14 (+3.79%)</td><td>0.14 (+2.60%)</td><td>0.13 <b>(+32.59%)</b></td><td>0.01 <b>(-74.44%)</b></td><td>184.50 <b>(-24.57%)</b></td><td>172.14 (-6.71%)</td><td>171.30 (-2.56%)</td><td>163.70 (+15.36%)</td><td>8.61 <b>(-78.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.60 (n/a)</td><td>184.52 (n/a)</td><td>175.80 (n/a)</td><td>141.90 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-5.96%)</td><td>0.12 (-4.68%)</td><td>0.11 (-10.97%)</td><td>0.11 (+14.11%)</td><td>0.01 <b>(-43.10%)</b></td><td>170.90 (-12.36%)</td><td>160.18 (+3.52%)</td><td>166.20 (+12.37%)</td><td>138.40 (+6.38%)</td><td>13.10 <b>(-48.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>195.00 (n/a)</td><td>154.74 (n/a)</td><td>147.90 (n/a)</td><td>130.10 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (+2.01%)</td><td>0.11 (-11.03%)</td><td>0.12 (-3.73%)</td><td>0.07 <b>(-30.80%)</b></td><td>0.03 <b>(+63.87%)</b></td><td>264.20 <b>(+44.53%)</b></td><td>180.42 (+19.20%)</td><td>159.70 (+3.84%)</td><td>120.00 (-1.96%)</td><td>58.70 <b>(+137.81%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>182.80 (n/a)</td><td>151.36 (n/a)</td><td>153.80 (n/a)</td><td>122.40 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (+6.74%)</td><td>0.12 (+9.44%)</td><td>0.11 (+3.01%)</td><td>0.11 (+11.74%)</td><td>0.02 (+9.13%)</td><td>174.20 (-10.48%)</td><td>153.00 (-8.55%)</td><td>166.90 (-2.91%)</td><td>120.40 (-6.30%)</td><td>23.41 (-5.73%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>167.30 (n/a)</td><td>171.90 (n/a)</td><td>128.50 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (-18.34%)</td><td>0.11 (+2.30%)</td><td>0.10 (-5.90%)</td><td>0.10 <b>(+37.48%)</b></td><td>0.01 <b>(-71.47%)</b></td><td>188.90 <b>(-27.26%)</b></td><td>175.78 (-7.93%)</td><td>178.70 (+6.31%)</td><td>157.00 <b>(+22.46%)</b></td><td>13.41 <b>(-75.19%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>259.70 (n/a)</td><td>190.92 (n/a)</td><td>168.10 (n/a)</td><td>128.20 (n/a)</td><td>54.07 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (+15.01%)</td><td>0.13 (+15.49%)</td><td>0.13 <b>(+22.20%)</b></td><td>0.10 (+2.62%)</td><td>0.02 <b>(+54.23%)</b></td><td>188.50 (-2.58%)</td><td>149.26 (-12.63%)</td><td>137.80 (-18.17%)</td><td>132.10 (-13.03%)</td><td>23.80 <b>(+30.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>170.84 (n/a)</td><td>168.40 (n/a)</td><td>151.90 (n/a)</td><td>18.23 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-7.37%)</td><td>0.11 (+5.02%)</td><td>0.11 (+13.02%)</td><td>0.09 (-1.79%)</td><td>0.01 <b>(-24.04%)</b></td><td>207.70 (+1.81%)</td><td>169.66 (-5.53%)</td><td>167.70 (-11.50%)</td><td>142.80 (+7.94%)</td><td>24.40 (-13.17%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>179.60 (n/a)</td><td>189.50 (n/a)</td><td>132.30 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 <b>(+26.75%)</b></td><td>0.11 (+13.42%)</td><td>0.10 (+1.29%)</td><td>0.08 (+6.30%)</td><td>0.02 <b>(+47.77%)</b></td><td>234.30 (-5.94%)</td><td>179.34 (-10.63%)</td><td>179.90 (-1.26%)</td><td>131.80 <b>(-21.08%)</b></td><td>38.59 (+8.48%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.10 (n/a)</td><td>200.68 (n/a)</td><td>182.20 (n/a)</td><td>167.00 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (-10.94%)</td><td>0.10 (-19.93%)</td><td>0.11 (-14.41%)</td><td>0.07 <b>(-33.68%)</b></td><td>0.02 <b>(+45.77%)</b></td><td>274.80 <b>(+50.82%)</b></td><td>196.96 <b>(+29.39%)</b></td><td>175.50 (+16.84%)</td><td>150.40 (+12.32%)</td><td>51.25 <b>(+152.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>182.20 (n/a)</td><td>152.22 (n/a)</td><td>150.20 (n/a)</td><td>133.90 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.57 (-13.60%)</td><td>0.50 (-6.23%)</td><td>0.48 (-10.04%)</td><td>0.41 (+19.76%)</td><td>0.06 <b>(-44.54%)</b></td><td>238.40 (-16.53%)</td><td>199.96 (+3.01%)</td><td>203.30 (+11.15%)</td><td>172.30 (+15.79%)</td><td>26.71 <b>(-49.79%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>285.60 (n/a)</td><td>194.12 (n/a)</td><td>182.90 (n/a)</td><td>148.80 (n/a)</td><td>53.19 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.59 <b>(-24.06%)</b></td><td>0.53 (-15.53%)</td><td>0.55 (-10.50%)</td><td>0.43 <b>(-21.95%)</b></td><td>0.07 <b>(-25.04%)</b></td><td>229.40 <b>(+28.08%)</b></td><td>189.96 (+18.30%)</td><td>179.80 (+11.75%)</td><td>166.70 <b>(+31.67%)</b></td><td>26.45 <b>(+27.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.61 (n/a)</td><td>0.55 (n/a)</td><td>0.09 (n/a)</td><td>179.10 (n/a)</td><td>160.58 (n/a)</td><td>160.90 (n/a)</td><td>126.60 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.74 (+17.10%)</td><td>0.59 (+5.09%)</td><td>0.58 (-3.37%)</td><td>0.49 (+16.91%)</td><td>0.10 (+19.43%)</td><td>200.20 (-14.48%)</td><td>170.14 (-4.76%)</td><td>170.80 (+3.52%)</td><td>133.70 (-14.62%)</td><td>28.28 (-12.42%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.63 (n/a)</td><td>0.56 (n/a)</td><td>0.60 (n/a)</td><td>0.42 (n/a)</td><td>0.09 (n/a)</td><td>234.10 (n/a)</td><td>178.64 (n/a)</td><td>165.00 (n/a)</td><td>156.60 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.62 <b>(-23.90%)</b></td><td>0.49 (-17.92%)</td><td>0.47 <b>(-22.70%)</b></td><td>0.36 <b>(-20.87%)</b></td><td>0.10 <b>(-26.81%)</b></td><td>276.00 <b>(+26.37%)</b></td><td>207.28 <b>(+21.27%)</b></td><td>208.00 <b>(+29.35%)</b></td><td>157.70 <b>(+31.42%)</b></td><td>45.99 <b>(+20.91%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.82 (n/a)</td><td>0.60 (n/a)</td><td>0.61 (n/a)</td><td>0.45 (n/a)</td><td>0.14 (n/a)</td><td>218.40 (n/a)</td><td>170.92 (n/a)</td><td>160.80 (n/a)</td><td>120.00 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.58 (+6.47%)</td><td>0.38 (-11.71%)</td><td>0.39 (-13.45%)</td><td>0.19 <b>(-43.38%)</b></td><td>0.14 <b>(+77.78%)</b></td><td>389.80 <b>(+76.62%)</b></td><td>220.70 <b>(+25.74%)</b></td><td>191.40 (+15.51%)</td><td>127.40 (-6.12%)</td><td>99.66 <b>(+211.68%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>220.70 (n/a)</td><td>175.52 (n/a)</td><td>165.70 (n/a)</td><td>135.70 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.56 <b>(+25.65%)</b></td><td>0.46 <b>(+28.14%)</b></td><td>0.50 <b>(+27.72%)</b></td><td>0.34 <b>(+64.17%)</b></td><td>0.09 (-6.95%)</td><td>214.10 <b>(-39.09%)</b></td><td>165.96 <b>(-25.15%)</b></td><td>148.50 <b>(-21.72%)</b></td><td>132.70 <b>(-20.40%)</b></td><td>33.76 <b>(-55.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>351.50 (n/a)</td><td>221.72 (n/a)</td><td>189.70 (n/a)</td><td>166.70 (n/a)</td><td>75.88 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.55 (+15.79%)</td><td>0.46 (+8.86%)</td><td>0.45 (+2.06%)</td><td>0.40 (+15.78%)</td><td>0.06 <b>(+31.29%)</b></td><td>184.10 (-13.61%)</td><td>160.96 (-7.89%)</td><td>164.70 (-2.02%)</td><td>133.40 (-13.66%)</td><td>21.34 (-4.61%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.05 (n/a)</td><td>213.10 (n/a)</td><td>174.74 (n/a)</td><td>168.10 (n/a)</td><td>154.50 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.44 (-0.55%)</td><td>0.38 (-0.46%)</td><td>0.37 (-4.04%)</td><td>0.33 (+0.30%)</td><td>0.05 (+1.43%)</td><td>224.40 (-0.31%)</td><td>196.54 (+0.48%)</td><td>201.60 (+4.24%)</td><td>167.70 (+0.54%)</td><td>23.81 (+0.63%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>225.10 (n/a)</td><td>195.60 (n/a)</td><td>193.40 (n/a)</td><td>166.80 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (-19.65%)</td><td>0.20 (-0.33%)</td><td>0.20 (+4.22%)</td><td>0.16 <b>(+46.53%)</b></td><td>0.03 <b>(-58.66%)</b></td><td>230.40 <b>(-31.75%)</b></td><td>187.32 (-8.98%)</td><td>181.70 (-4.01%)</td><td>153.50 <b>(+24.49%)</b></td><td>28.77 <b>(-65.21%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>337.60 (n/a)</td><td>205.80 (n/a)</td><td>189.30 (n/a)</td><td>123.30 (n/a)</td><td>82.70 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (-2.68%)</td><td>0.20 (-4.21%)</td><td>0.19 (-6.36%)</td><td>0.15 <b>(-20.52%)</b></td><td>0.04 <b>(+57.42%)</b></td><td>241.30 <b>(+25.81%)</b></td><td>188.32 (+6.96%)</td><td>195.10 (+6.79%)</td><td>146.00 (+2.74%)</td><td>39.61 <b>(+102.04%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>191.80 (n/a)</td><td>176.06 (n/a)</td><td>182.70 (n/a)</td><td>142.10 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.29 (+5.90%)</td><td>0.25 (+7.06%)</td><td>0.26 (-4.20%)</td><td>0.21 <b>(+39.83%)</b></td><td>0.04 <b>(-40.96%)</b></td><td>178.20 <b>(-28.49%)</b></td><td>150.30 (-10.95%)</td><td>142.20 (+4.41%)</td><td>125.60 (-5.63%)</td><td>21.67 <b>(-57.96%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>249.20 (n/a)</td><td>168.78 (n/a)</td><td>136.20 (n/a)</td><td>133.10 (n/a)</td><td>51.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (+3.56%)</td><td>0.21 (-18.22%)</td><td>0.18 <b>(-32.32%)</b></td><td>0.17 (-14.51%)</td><td>0.05 <b>(+46.36%)</b></td><td>217.00 (+16.98%)</td><td>186.38 <b>(+25.24%)</b></td><td>201.60 <b>(+47.69%)</b></td><td>122.60 (-3.46%)</td><td>37.50 <b>(+58.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>185.50 (n/a)</td><td>148.82 (n/a)</td><td>136.50 (n/a)</td><td>127.00 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 <b>(-24.57%)</b></td><td>0.17 (-17.13%)</td><td>0.17 (-15.99%)</td><td>0.15 (-16.68%)</td><td>0.01 <b>(-46.23%)</b></td><td>243.00 <b>(+20.06%)</b></td><td>218.70 <b>(+20.07%)</b></td><td>220.90 (+19.02%)</td><td>201.80 <b>(+32.59%)</b></td><td>16.42 (-13.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>202.40 (n/a)</td><td>182.14 (n/a)</td><td>185.60 (n/a)</td><td>152.20 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 <b>(+23.25%)</b></td><td>0.19 (+11.84%)</td><td>0.18 (+1.47%)</td><td>0.14 (+17.50%)</td><td>0.04 <b>(+32.96%)</b></td><td>264.10 (-14.89%)</td><td>203.92 (-10.18%)</td><td>206.50 (-1.43%)</td><td>156.50 (-18.87%)</td><td>41.84 (-11.98%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>310.30 (n/a)</td><td>227.02 (n/a)</td><td>209.50 (n/a)</td><td>192.90 (n/a)</td><td>47.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (-17.89%)</td><td>0.21 (-5.81%)</td><td>0.20 (-3.17%)</td><td>0.18 (-5.28%)</td><td>0.02 <b>(-41.88%)</b></td><td>206.90 (+5.56%)</td><td>179.50 (+5.02%)</td><td>182.90 (+3.27%)</td><td>158.50 <b>(+21.83%)</b></td><td>19.10 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>196.00 (n/a)</td><td>170.92 (n/a)</td><td>177.10 (n/a)</td><td>130.10 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (+3.87%)</td><td>0.24 (+12.16%)</td><td>0.25 (+16.65%)</td><td>0.18 (+5.41%)</td><td>0.05 (+0.21%)</td><td>210.60 (-5.09%)</td><td>158.80 (-10.97%)</td><td>148.80 (-14.24%)</td><td>124.20 (-3.72%)</td><td>32.84 (-5.08%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>221.90 (n/a)</td><td>178.36 (n/a)</td><td>173.50 (n/a)</td><td>129.00 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (-8.52%)</td><td>0.20 (-14.52%)</td><td>0.19 (-18.97%)</td><td>0.17 (-15.35%)</td><td>0.05 (+10.26%)</td><td>242.90 (+18.08%)</td><td>207.90 (+18.50%)</td><td>220.50 <b>(+23.39%)</b></td><td>146.50 (+9.33%)</td><td>40.28 <b>(+44.24%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>205.70 (n/a)</td><td>175.44 (n/a)</td><td>178.70 (n/a)</td><td>134.00 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (-5.67%)</td><td>0.24 (-10.74%)</td><td>0.23 (-17.81%)</td><td>0.18 (-12.89%)</td><td>0.04 (+9.99%)</td><td>222.10 (+14.84%)</td><td>173.02 (+12.92%)</td><td>176.10 <b>(+21.62%)</b></td><td>137.40 (+6.02%)</td><td>32.27 <b>(+31.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>193.40 (n/a)</td><td>153.22 (n/a)</td><td>144.80 (n/a)</td><td>129.60 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.34 (+6.72%)</td><td>0.26 (-7.85%)</td><td>0.27 (-13.51%)</td><td>0.20 (-12.02%)</td><td>0.06 <b>(+40.02%)</b></td><td>200.60 (+13.65%)</td><td>161.46 (+11.08%)</td><td>151.00 (+15.62%)</td><td>119.30 (-6.28%)</td><td>37.36 <b>(+59.05%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>176.50 (n/a)</td><td>145.36 (n/a)</td><td>130.60 (n/a)</td><td>127.30 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (-10.33%)</td><td>0.29 (+6.77%)</td><td>0.31 (+9.38%)</td><td>0.22 <b>(+28.27%)</b></td><td>0.04 <b>(-46.33%)</b></td><td>183.90 <b>(-22.04%)</b></td><td>141.92 (-10.97%)</td><td>134.10 (-8.59%)</td><td>126.30 (+11.57%)</td><td>23.72 <b>(-52.03%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>235.90 (n/a)</td><td>159.40 (n/a)</td><td>146.70 (n/a)</td><td>113.20 (n/a)</td><td>49.45 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (-6.74%)</td><td>0.21 (-8.24%)</td><td>0.21 (-9.95%)</td><td>0.17 (+0.92%)</td><td>0.03 <b>(-28.54%)</b></td><td>237.00 (-0.92%)</td><td>198.80 (+7.12%)</td><td>199.80 (+11.06%)</td><td>153.80 (+7.18%)</td><td>29.87 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>239.20 (n/a)</td><td>185.58 (n/a)</td><td>179.90 (n/a)</td><td>143.50 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (+14.45%)</td><td>0.25 (+10.95%)</td><td>0.23 (-0.96%)</td><td>0.20 (+16.76%)</td><td>0.05 (+12.65%)</td><td>201.90 (-14.34%)</td><td>170.24 (-10.03%)</td><td>180.80 (+1.01%)</td><td>127.60 (-12.60%)</td><td>29.30 (-17.65%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.70 (n/a)</td><td>189.22 (n/a)</td><td>179.00 (n/a)</td><td>146.00 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (+10.09%)</td><td>0.29 (+13.58%)</td><td>0.30 <b>(+24.10%)</b></td><td>0.18 (-14.72%)</td><td>0.07 <b>(+47.75%)</b></td><td>225.40 (+17.21%)</td><td>149.68 (-9.01%)</td><td>137.50 (-19.45%)</td><td>112.30 (-9.14%)</td><td>44.25 <b>(+68.16%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>192.30 (n/a)</td><td>164.50 (n/a)</td><td>170.70 (n/a)</td><td>123.60 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 <b>(+33.99%)</b></td><td>0.24 (+6.02%)</td><td>0.22 (-1.93%)</td><td>0.19 (-6.12%)</td><td>0.07 <b>(+136.72%)</b></td><td>215.50 (+6.52%)</td><td>178.04 (-1.92%)</td><td>190.20 (+1.98%)</td><td>114.80 <b>(-25.36%)</b></td><td>40.25 <b>(+82.69%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>202.30 (n/a)</td><td>181.52 (n/a)</td><td>186.50 (n/a)</td><td>153.80 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (-15.64%)</td><td>0.18 (-19.20%)</td><td>0.19 (-11.20%)</td><td>0.13 <b>(-25.98%)</b></td><td>0.04 (-19.95%)</td><td>272.20 <b>(+35.09%)</b></td><td>199.40 <b>(+24.07%)</b></td><td>185.00 (+12.60%)</td><td>148.30 (+18.55%)</td><td>47.11 <b>(+35.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>201.50 (n/a)</td><td>160.72 (n/a)</td><td>164.30 (n/a)</td><td>125.10 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (-2.24%)</td><td>0.20 (+7.52%)</td><td>0.18 (-1.92%)</td><td>0.17 <b>(+34.28%)</b></td><td>0.04 <b>(-29.93%)</b></td><td>204.40 <b>(-25.51%)</b></td><td>182.34 (-10.34%)</td><td>193.90 (+1.95%)</td><td>135.30 (+2.27%)</td><td>28.70 <b>(-46.43%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>274.40 (n/a)</td><td>203.36 (n/a)</td><td>190.20 (n/a)</td><td>132.30 (n/a)</td><td>53.58 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 <b>(-37.44%)</b></td><td>0.16 <b>(-32.36%)</b></td><td>0.15 <b>(-35.20%)</b></td><td>0.14 <b>(-23.51%)</b></td><td>0.01 <b>(-68.39%)</b></td><td>243.70 <b>(+30.74%)</b></td><td>221.38 <b>(+44.13%)</b></td><td>229.40 <b>(+54.27%)</b></td><td>195.90 <b>(+59.92%)</b></td><td>19.98 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>186.40 (n/a)</td><td>153.60 (n/a)</td><td>148.70 (n/a)</td><td>122.50 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (-18.36%)</td><td>0.17 <b>(-24.89%)</b></td><td>0.17 <b>(-30.56%)</b></td><td>0.13 (-8.61%)</td><td>0.03 <b>(-35.55%)</b></td><td>271.30 (+9.44%)</td><td>211.46 <b>(+29.83%)</b></td><td>204.80 <b>(+44.02%)</b></td><td>159.00 <b>(+22.50%)</b></td><td>40.21 (-17.15%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>247.90 (n/a)</td><td>162.88 (n/a)</td><td>142.20 (n/a)</td><td>129.80 (n/a)</td><td>48.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (-18.78%)</td><td>0.17 <b>(-20.35%)</b></td><td>0.18 <b>(-23.57%)</b></td><td>0.14 (-17.87%)</td><td>0.02 <b>(-36.65%)</b></td><td>244.90 <b>(+21.72%)</b></td><td>202.10 <b>(+24.43%)</b></td><td>197.90 <b>(+30.80%)</b></td><td>169.30 <b>(+23.13%)</b></td><td>27.41 (-2.94%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.20 (n/a)</td><td>162.42 (n/a)</td><td>151.30 (n/a)</td><td>137.50 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 <b>(-22.42%)</b></td><td>0.18 (-18.73%)</td><td>0.19 (-16.69%)</td><td>0.16 <b>(-20.24%)</b></td><td>0.02 <b>(-33.09%)</b></td><td>224.10 <b>(+25.34%)</b></td><td>192.28 <b>(+22.52%)</b></td><td>187.80 <b>(+20.00%)</b></td><td>168.80 <b>(+28.85%)</b></td><td>22.10 (+6.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>178.80 (n/a)</td><td>156.94 (n/a)</td><td>156.50 (n/a)</td><td>131.00 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 <b>(+29.48%)</b></td><td>0.21 (+19.58%)</td><td>0.21 (+19.35%)</td><td>0.15 (+1.28%)</td><td>0.04 <b>(+116.24%)</b></td><td>230.30 (-1.24%)</td><td>171.46 (-14.32%)</td><td>164.20 (-16.22%)</td><td>136.70 <b>(-22.72%)</b></td><td>37.16 <b>(+65.44%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>200.12 (n/a)</td><td>196.00 (n/a)</td><td>176.90 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 <b>(-29.40%)</b></td><td>0.20 (-5.78%)</td><td>0.21 (+19.19%)</td><td>0.17 (+12.57%)</td><td>0.02 <b>(-69.04%)</b></td><td>203.90 (-11.15%)</td><td>173.48 (-0.34%)</td><td>164.40 (-16.12%)</td><td>158.30 <b>(+41.72%)</b></td><td>19.28 <b>(-60.63%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>229.50 (n/a)</td><td>174.08 (n/a)</td><td>196.00 (n/a)</td><td>111.70 (n/a)</td><td>48.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.93 (-13.87%)</td><td>0.78 (-12.41%)</td><td>0.75 (-17.21%)</td><td>0.72 (+2.19%)</td><td>0.09 <b>(-46.40%)</b></td><td>181.70 (-2.15%)</td><td>168.76 (+12.19%)</td><td>175.20 <b>(+20.83%)</b></td><td>141.40 (+16.09%)</td><td>16.61 <b>(-39.37%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.08 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.71 (n/a)</td><td>0.16 (n/a)</td><td>185.70 (n/a)</td><td>150.42 (n/a)</td><td>145.00 (n/a)</td><td>121.80 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.98 (+11.77%)</td><td>0.70 (-8.36%)</td><td>0.69 (-15.29%)</td><td>0.53 (-1.01%)</td><td>0.18 <b>(+34.96%)</b></td><td>245.50 (+0.99%)</td><td>196.76 (+11.13%)</td><td>189.50 (+18.07%)</td><td>133.40 (-10.53%)</td><td>46.02 <b>(+20.62%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.82 (n/a)</td><td>0.54 (n/a)</td><td>0.13 (n/a)</td><td>243.10 (n/a)</td><td>177.06 (n/a)</td><td>160.50 (n/a)</td><td>149.10 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.99 (+1.51%)</td><td>0.75 (+8.77%)</td><td>0.73 (-0.93%)</td><td>0.54 <b>(+24.30%)</b></td><td>0.17 <b>(-22.80%)</b></td><td>241.00 (-19.53%)</td><td>182.68 (-12.03%)</td><td>179.40 (+0.96%)</td><td>132.30 (-1.49%)</td><td>40.32 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.98 (n/a)</td><td>0.69 (n/a)</td><td>0.74 (n/a)</td><td>0.44 (n/a)</td><td>0.22 (n/a)</td><td>299.50 (n/a)</td><td>207.66 (n/a)</td><td>177.70 (n/a)</td><td>134.30 (n/a)</td><td>67.78 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.00 (-2.22%)</td><td>0.00 (+1.90%)</td><td>0.00 (+2.38%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(-48.01%)</b></td><td>981.91 (-2.95%)</td><td>953.07 (-1.61%)</td><td>942.97 (-3.74%)</td><td>930.12 (+2.21%)</td><td>21.92 <b>(-46.55%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1011.78 (n/a)</td><td>968.63 (n/a)</td><td>979.63 (n/a)</td><td>910.05 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.01 (-2.38%)</td><td>0.01 (-3.15%)</td><td>0.01 (-2.41%)</td><td>0.01 (-7.41%)</td><td>0.00 <b>(+92.24%)</b></td><td>1093.54 (+7.50%)</td><td>1026.35 (+3.26%)</td><td>1012.48 (+2.25%)</td><td>1002.84 (+3.37%)</td><td>38.20 <b>(+85.46%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1017.25 (n/a)</td><td>993.90 (n/a)</td><td>990.19 (n/a)</td><td>970.11 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.96 (-2.27%)</td><td>0.94 (-1.48%)</td><td>0.94 (-1.38%)</td><td>0.93 (-1.02%)</td><td>0.01 <b>(-30.27%)</b></td><td>2259.54 (+1.03%)</td><td>2228.92 (+1.49%)</td><td>2235.58 (+1.40%)</td><td>2185.66 (+2.32%)</td><td>27.39 <b>(-27.90%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2236.59 (n/a)</td><td>2196.16 (n/a)</td><td>2204.66 (n/a)</td><td>2136.09 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.63 (+7.02%)</td><td>4.35 (-5.37%)</td><td>4.27 (-8.26%)</td><td>3.49 (-16.74%)</td><td>0.81 <b>(+83.47%)</b></td><td>300.70 <b>(+20.09%)</b></td><td>247.28 (+7.67%)</td><td>245.40 (+9.02%)</td><td>186.30 (-6.57%)</td><td>42.84 <b>(+100.29%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.26 (n/a)</td><td>4.60 (n/a)</td><td>4.66 (n/a)</td><td>4.19 (n/a)</td><td>0.44 (n/a)</td><td>250.40 (n/a)</td><td>229.66 (n/a)</td><td>225.10 (n/a)</td><td>199.40 (n/a)</td><td>21.39 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.20 (-0.54%)</td><td>4.74 (+11.18%)</td><td>4.86 (+15.53%)</td><td>4.05 (+10.59%)</td><td>0.43 <b>(-31.07%)</b></td><td>259.10 (-9.56%)</td><td>222.66 (-10.86%)</td><td>215.60 (-13.41%)</td><td>201.50 (+0.50%)</td><td>21.89 <b>(-36.26%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.23 (n/a)</td><td>4.27 (n/a)</td><td>4.21 (n/a)</td><td>3.66 (n/a)</td><td>0.63 (n/a)</td><td>286.50 (n/a)</td><td>249.80 (n/a)</td><td>249.00 (n/a)</td><td>200.50 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.96 (+6.08%)</td><td>4.88 (+3.24%)</td><td>4.85 (+4.20%)</td><td>3.76 (-8.83%)</td><td>1.01 <b>(+77.11%)</b></td><td>279.20 (+9.66%)</td><td>222.54 (-0.74%)</td><td>216.00 (-4.04%)</td><td>176.00 (-5.73%)</td><td>46.94 <b>(+82.25%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.62 (n/a)</td><td>4.73 (n/a)</td><td>4.66 (n/a)</td><td>4.12 (n/a)</td><td>0.57 (n/a)</td><td>254.60 (n/a)</td><td>224.20 (n/a)</td><td>225.10 (n/a)</td><td>186.70 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.44 (+17.75%)</td><td>4.91 (+0.73%)</td><td>4.83 (-6.37%)</td><td>4.01 (+7.47%)</td><td>0.92 <b>(+32.17%)</b></td><td>261.20 (-6.98%)</td><td>219.10 (-0.13%)</td><td>217.30 (+6.83%)</td><td>162.70 (-15.08%)</td><td>36.33 (-0.00%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.47 (n/a)</td><td>4.87 (n/a)</td><td>5.15 (n/a)</td><td>3.73 (n/a)</td><td>0.70 (n/a)</td><td>280.80 (n/a)</td><td>219.38 (n/a)</td><td>203.40 (n/a)</td><td>191.60 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.77 (-0.14%)</td><td>8.17 (+1.69%)</td><td>8.08 (+0.20%)</td><td>7.62 (+7.53%)</td><td>0.51 <b>(-24.66%)</b></td><td>275.30 (-6.99%)</td><td>257.44 (-1.94%)</td><td>259.40 (-0.23%)</td><td>239.20 (+0.13%)</td><td>16.04 <b>(-29.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.78 (n/a)</td><td>8.04 (n/a)</td><td>8.07 (n/a)</td><td>7.08 (n/a)</td><td>0.68 (n/a)</td><td>296.00 (n/a)</td><td>262.54 (n/a)</td><td>260.00 (n/a)</td><td>238.90 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.44 (-1.28%)</td><td>7.60 (-2.22%)</td><td>7.57 (-3.05%)</td><td>6.92 (-1.42%)</td><td>0.55 (+0.41%)</td><td>303.30 (+1.44%)</td><td>277.22 (+2.29%)</td><td>277.00 (+3.13%)</td><td>248.60 (+1.30%)</td><td>19.84 (+2.39%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.55 (n/a)</td><td>7.77 (n/a)</td><td>7.81 (n/a)</td><td>7.01 (n/a)</td><td>0.55 (n/a)</td><td>299.00 (n/a)</td><td>271.02 (n/a)</td><td>268.60 (n/a)</td><td>245.40 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.55 (-5.55%)</td><td>7.55 (-3.09%)</td><td>7.69 (+1.15%)</td><td>6.20 (-6.80%)</td><td>0.85 <b>(-21.76%)</b></td><td>338.00 (+7.27%)</td><td>280.88 (+2.74%)</td><td>272.60 (-1.12%)</td><td>245.40 (+5.91%)</td><td>34.55 (-8.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.05 (n/a)</td><td>7.79 (n/a)</td><td>7.61 (n/a)</td><td>6.66 (n/a)</td><td>1.09 (n/a)</td><td>315.10 (n/a)</td><td>273.40 (n/a)</td><td>275.70 (n/a)</td><td>231.70 (n/a)</td><td>37.92 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.09 (-2.90%)</td><td>8.69 (-2.71%)</td><td>9.00 (-0.36%)</td><td>7.99 (-5.49%)</td><td>0.51 <b>(+32.49%)</b></td><td>262.60 (+5.80%)</td><td>242.12 (+2.93%)</td><td>233.10 (+0.39%)</td><td>230.70 (+2.99%)</td><td>14.74 <b>(+42.56%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.36 (n/a)</td><td>8.93 (n/a)</td><td>9.03 (n/a)</td><td>8.45 (n/a)</td><td>0.39 (n/a)</td><td>248.20 (n/a)</td><td>235.22 (n/a)</td><td>232.20 (n/a)</td><td>224.00 (n/a)</td><td>10.34 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>10.21 (-10.07%)</td><td>8.55 (+1.66%)</td><td>8.16 (+2.50%)</td><td>7.21 (+11.28%)</td><td>1.18 <b>(-40.48%)</b></td><td>290.70 (-10.14%)</td><td>248.90 (-4.23%)</td><td>257.10 (-2.43%)</td><td>205.40 (+11.21%)</td><td>33.37 <b>(-41.32%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>11.35 (n/a)</td><td>8.41 (n/a)</td><td>7.96 (n/a)</td><td>6.48 (n/a)</td><td>1.99 (n/a)</td><td>323.50 (n/a)</td><td>259.88 (n/a)</td><td>263.50 (n/a)</td><td>184.70 (n/a)</td><td>56.87 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.65 (+2.31%)</td><td>8.56 (+12.30%)</td><td>8.54 (+15.94%)</td><td>7.60 <b>(+44.44%)</b></td><td>0.80 <b>(-49.63%)</b></td><td>275.80 <b>(-30.77%)</b></td><td>246.68 (-13.85%)</td><td>245.50 (-13.74%)</td><td>217.30 (-2.25%)</td><td>22.91 <b>(-66.48%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.43 (n/a)</td><td>7.62 (n/a)</td><td>7.37 (n/a)</td><td>5.26 (n/a)</td><td>1.59 (n/a)</td><td>398.40 (n/a)</td><td>286.34 (n/a)</td><td>284.60 (n/a)</td><td>222.30 (n/a)</td><td>68.36 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>12.29 (-1.01%)</td><td>12.00 (+7.08%)</td><td>11.89 (+8.63%)</td><td>11.79 (+10.23%)</td><td>0.22 <b>(-67.90%)</b></td><td>355.80 (-9.30%)</td><td>349.60 (-6.86%)</td><td>352.70 (-7.94%)</td><td>341.40 (+1.04%)</td><td>6.46 <b>(-70.50%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.41 (n/a)</td><td>11.21 (n/a)</td><td>10.95 (n/a)</td><td>10.69 (n/a)</td><td>0.70 (n/a)</td><td>392.30 (n/a)</td><td>375.34 (n/a)</td><td>383.10 (n/a)</td><td>337.90 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.03 (+3.93%)</td><td>11.51 (-2.80%)</td><td>11.96 (-2.79%)</td><td>10.16 (-2.57%)</td><td>1.21 <b>(+35.67%)</b></td><td>412.90 (+2.63%)</td><td>367.80 (+3.30%)</td><td>350.70 (+2.84%)</td><td>321.90 (-3.77%)</td><td>38.91 <b>(+36.31%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.54 (n/a)</td><td>11.84 (n/a)</td><td>12.30 (n/a)</td><td>10.43 (n/a)</td><td>0.89 (n/a)</td><td>402.30 (n/a)</td><td>356.06 (n/a)</td><td>341.00 (n/a)</td><td>334.50 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.51 (+14.88%)</td><td>12.06 (+5.71%)</td><td>12.27 (+7.27%)</td><td>10.34 (-5.94%)</td><td>1.24 <b>(+247.95%)</b></td><td>405.70 (+6.32%)</td><td>350.94 (-4.65%)</td><td>341.70 (-6.79%)</td><td>310.50 (-12.95%)</td><td>37.44 <b>(+224.23%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>11.76 (n/a)</td><td>11.41 (n/a)</td><td>11.44 (n/a)</td><td>10.99 (n/a)</td><td>0.36 (n/a)</td><td>381.60 (n/a)</td><td>368.04 (n/a)</td><td>366.60 (n/a)</td><td>356.70 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.93 (+7.90%)</td><td>13.38 (+6.63%)</td><td>13.17 (+5.84%)</td><td>11.78 (+2.09%)</td><td>1.24 <b>(+47.54%)</b></td><td>356.00 (-2.06%)</td><td>315.76 (-5.91%)</td><td>318.50 (-5.52%)</td><td>280.90 (-7.32%)</td><td>29.56 <b>(+34.13%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.84 (n/a)</td><td>12.54 (n/a)</td><td>12.44 (n/a)</td><td>11.54 (n/a)</td><td>0.84 (n/a)</td><td>363.50 (n/a)</td><td>335.58 (n/a)</td><td>337.10 (n/a)</td><td>303.10 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.01 (+9.32%)</td><td>13.37 (+11.03%)</td><td>13.44 (+7.55%)</td><td>12.41 (+15.49%)</td><td>0.60 <b>(-30.84%)</b></td><td>338.00 (-13.40%)</td><td>314.24 (-10.18%)</td><td>312.10 (-7.03%)</td><td>299.50 (-8.52%)</td><td>14.60 <b>(-44.75%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.81 (n/a)</td><td>12.04 (n/a)</td><td>12.50 (n/a)</td><td>10.75 (n/a)</td><td>0.87 (n/a)</td><td>390.30 (n/a)</td><td>349.84 (n/a)</td><td>335.70 (n/a)</td><td>327.40 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.24 (+1.50%)</td><td>12.78 (+0.67%)</td><td>13.22 (+3.90%)</td><td>11.33 (-2.97%)</td><td>1.25 <b>(+29.83%)</b></td><td>370.30 (+3.06%)</td><td>330.80 (-0.36%)</td><td>317.20 (-3.76%)</td><td>294.50 (-1.47%)</td><td>32.82 <b>(+32.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.03 (n/a)</td><td>12.69 (n/a)</td><td>12.73 (n/a)</td><td>11.67 (n/a)</td><td>0.96 (n/a)</td><td>359.30 (n/a)</td><td>331.98 (n/a)</td><td>329.60 (n/a)</td><td>298.90 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>16.11 (+11.94%)</td><td>12.97 (-5.37%)</td><td>13.00 (-6.37%)</td><td>9.60 <b>(-24.67%)</b></td><td>2.31 <b>(+275.95%)</b></td><td>437.00 <b>(+32.75%)</b></td><td>332.32 (+8.43%)</td><td>322.70 (+6.82%)</td><td>260.30 (-10.67%)</td><td>64.26 <b>(+354.14%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.39 (n/a)</td><td>13.71 (n/a)</td><td>13.88 (n/a)</td><td>12.74 (n/a)</td><td>0.61 (n/a)</td><td>329.20 (n/a)</td><td>306.48 (n/a)</td><td>302.10 (n/a)</td><td>291.40 (n/a)</td><td>14.15 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>15.22 (+7.82%)</td><td>13.39 (+6.37%)</td><td>13.24 (+1.26%)</td><td>10.91 (+9.16%)</td><td>1.65 (+0.22%)</td><td>384.50 (-8.39%)</td><td>317.38 (-6.19%)</td><td>316.90 (-1.22%)</td><td>275.60 (-7.27%)</td><td>42.13 (-14.88%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.11 (n/a)</td><td>12.59 (n/a)</td><td>13.07 (n/a)</td><td>9.99 (n/a)</td><td>1.65 (n/a)</td><td>419.70 (n/a)</td><td>338.34 (n/a)</td><td>320.80 (n/a)</td><td>297.20 (n/a)</td><td>49.50 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.01 (-12.67%)</td><td>2.65 (-11.62%)</td><td>2.60 (-11.05%)</td><td>2.50 (-7.79%)</td><td>0.20 <b>(-30.72%)</b></td><td>209.50 (+8.44%)</td><td>198.74 (+12.81%)</td><td>201.40 (+12.39%)</td><td>174.40 (+14.51%)</td><td>14.09 (-15.08%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.44 (n/a)</td><td>3.00 (n/a)</td><td>2.93 (n/a)</td><td>2.71 (n/a)</td><td>0.30 (n/a)</td><td>193.20 (n/a)</td><td>176.18 (n/a)</td><td>179.20 (n/a)</td><td>152.30 (n/a)</td><td>16.59 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.75 (-0.47%)</td><td>4.66 (-12.12%)</td><td>4.45 <b>(-21.93%)</b></td><td>3.82 (-4.17%)</td><td>0.77 (+1.41%)</td><td>274.60 (+4.37%)</td><td>229.62 (+13.93%)</td><td>235.80 <b>(+28.08%)</b></td><td>182.50 (+0.50%)</td><td>36.63 (+4.77%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.77 (n/a)</td><td>5.31 (n/a)</td><td>5.70 (n/a)</td><td>3.98 (n/a)</td><td>0.76 (n/a)</td><td>263.10 (n/a)</td><td>201.54 (n/a)</td><td>184.10 (n/a)</td><td>181.60 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.82 (-0.12%)</td><td>8.06 (+4.28%)</td><td>8.14 (+3.94%)</td><td>7.34 (+4.94%)</td><td>0.59 <b>(-23.11%)</b></td><td>285.80 (-4.70%)</td><td>261.28 (-4.43%)</td><td>257.70 (-3.77%)</td><td>237.80 (+0.13%)</td><td>19.29 <b>(-27.72%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.83 (n/a)</td><td>7.73 (n/a)</td><td>7.83 (n/a)</td><td>6.99 (n/a)</td><td>0.77 (n/a)</td><td>299.90 (n/a)</td><td>273.40 (n/a)</td><td>267.80 (n/a)</td><td>237.50 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.60 (-0.36%)</td><td>2.91 (+2.18%)</td><td>2.90 (+7.98%)</td><td>2.23 (-3.74%)</td><td>0.57 (+11.59%)</td><td>235.30 (+3.89%)</td><td>186.08 (-1.41%)</td><td>180.80 (-7.38%)</td><td>145.70 (+0.34%)</td><td>37.31 (+17.16%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.61 (n/a)</td><td>2.85 (n/a)</td><td>2.69 (n/a)</td><td>2.32 (n/a)</td><td>0.51 (n/a)</td><td>226.50 (n/a)</td><td>188.74 (n/a)</td><td>195.20 (n/a)</td><td>145.20 (n/a)</td><td>31.84 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 <b>(-20.88%)</b></td><td>0.20 (-3.28%)</td><td>0.19 (+2.09%)</td><td>0.18 (+6.53%)</td><td>0.03 <b>(-49.77%)</b></td><td>186.50 (-6.09%)</td><td>164.08 (-0.34%)</td><td>169.50 (-2.02%)</td><td>133.00 <b>(+26.31%)</b></td><td>23.08 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>198.60 (n/a)</td><td>164.64 (n/a)</td><td>173.00 (n/a)</td><td>105.30 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (+11.62%)</td><td>0.20 (+2.23%)</td><td>0.19 (-11.05%)</td><td>0.15 (-4.36%)</td><td>0.04 <b>(+29.83%)</b></td><td>213.20 (+4.56%)</td><td>166.08 (-1.08%)</td><td>170.00 (+12.43%)</td><td>127.60 (-10.39%)</td><td>33.44 (+19.60%)</td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>167.90 (n/a)</td><td>151.20 (n/a)</td><td>142.40 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.45 (-4.96%)</td><td>0.37 (-3.82%)</td><td>0.41 (+10.39%)</td><td>0.22 <b>(-24.62%)</b></td><td>0.09 <b>(+26.66%)</b></td><td>293.40 <b>(+32.64%)</b></td><td>188.16 (+7.77%)</td><td>160.00 (-9.40%)</td><td>144.80 (+5.23%)</td><td>60.54 <b>(+85.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>221.20 (n/a)</td><td>174.60 (n/a)</td><td>176.60 (n/a)</td><td>137.60 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.56 <b>(+26.19%)</b></td><td>0.39 (+5.39%)</td><td>0.34 (-8.35%)</td><td>0.30 (-8.23%)</td><td>0.11 <b>(+121.11%)</b></td><td>221.30 (+8.96%)</td><td>177.06 (-0.84%)</td><td>191.00 (+9.08%)</td><td>117.60 <b>(-20.75%)</b></td><td>44.72 <b>(+88.58%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>203.10 (n/a)</td><td>178.56 (n/a)</td><td>175.10 (n/a)</td><td>148.40 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.42 <b>(-21.32%)</b></td><td>0.35 (-12.43%)</td><td>0.34 (-8.30%)</td><td>0.32 (+12.72%)</td><td>0.04 <b>(-59.66%)</b></td><td>204.70 (-11.27%)</td><td>187.54 (+10.08%)</td><td>193.40 (+9.02%)</td><td>157.70 <b>(+27.07%)</b></td><td>18.56 <b>(-54.67%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>230.70 (n/a)</td><td>170.36 (n/a)</td><td>177.40 (n/a)</td><td>124.10 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.07 (+6.11%)</td><td>0.82 (-7.20%)</td><td>0.73 <b>(-25.30%)</b></td><td>0.61 (-10.15%)</td><td>0.20 <b>(+28.51%)</b></td><td>213.40 (+11.26%)</td><td>167.76 (+9.78%)</td><td>178.50 <b>(+33.91%)</b></td><td>122.90 (-5.75%)</td><td>38.64 <b>(+33.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td><td>0.98 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>191.80 (n/a)</td><td>152.82 (n/a)</td><td>133.30 (n/a)</td><td>130.40 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.04 (+13.73%)</td><td>0.83 (+11.17%)</td><td>0.73 (-3.10%)</td><td>0.65 (+1.21%)</td><td>0.18 <b>(+68.13%)</b></td><td>202.50 (-1.22%)</td><td>164.46 (-8.09%)</td><td>180.40 (+3.20%)</td><td>126.00 (-12.07%)</td><td>34.41 <b>(+40.84%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.91 (n/a)</td><td>0.74 (n/a)</td><td>0.75 (n/a)</td><td>0.64 (n/a)</td><td>0.11 (n/a)</td><td>205.00 (n/a)</td><td>178.94 (n/a)</td><td>174.80 (n/a)</td><td>143.30 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.97 <b>(+24.28%)</b></td><td>0.71 (+3.54%)</td><td>0.63 (-14.03%)</td><td>0.51 (-2.58%)</td><td>0.19 <b>(+94.49%)</b></td><td>256.00 (+2.65%)</td><td>194.68 (+0.25%)</td><td>209.60 (+16.32%)</td><td>134.80 (-19.57%)</td><td>50.00 <b>(+53.69%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.73 (n/a)</td><td>0.53 (n/a)</td><td>0.10 (n/a)</td><td>249.40 (n/a)</td><td>194.20 (n/a)</td><td>180.20 (n/a)</td><td>167.60 (n/a)</td><td>32.53 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.98 (-2.90%)</td><td>0.83 (-4.64%)</td><td>0.79 (-10.22%)</td><td>0.74 (+14.73%)</td><td>0.09 <b>(-38.61%)</b></td><td>176.80 (-12.86%)</td><td>159.98 (+3.04%)</td><td>166.40 (+11.38%)</td><td>134.20 (+2.99%)</td><td>16.32 <b>(-45.24%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.01 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.65 (n/a)</td><td>0.15 (n/a)</td><td>202.90 (n/a)</td><td>155.26 (n/a)</td><td>149.40 (n/a)</td><td>130.30 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (-13.22%)</td><td>0.11 (+2.09%)</td><td>0.10 (+6.01%)</td><td>0.09 (+5.14%)</td><td>0.02 <b>(-33.34%)</b></td><td>180.80 (-4.89%)</td><td>153.70 (-3.48%)</td><td>157.10 (-5.65%)</td><td>130.20 (+15.32%)</td><td>21.31 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>159.24 (n/a)</td><td>166.50 (n/a)</td><td>112.90 (n/a)</td><td>28.35 (n/a)</td>
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
