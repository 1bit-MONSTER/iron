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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(+20.43%)</b></td><td>0.04 (+9.01%)</td><td>0.04 (+2.29%)</td><td>0.03 (+10.88%)</td><td>0.01 <b>(+63.80%)</b></td><td>207.90 (-9.80%)</td><td>168.40 (-6.39%)</td><td>172.10 (-2.27%)</td><td>122.50 (-16.95%)</td><td>36.97 <b>(+20.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>179.90 (n/a)</td><td>176.10 (n/a)</td><td>147.50 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(+23.13%)</b></td><td>0.04 (+2.35%)</td><td>0.03 (-0.84%)</td><td>0.03 (-8.11%)</td><td>0.01 <b>(+105.17%)</b></td><td>222.70 (+8.79%)</td><td>179.22 (+0.11%)</td><td>180.00 (+0.84%)</td><td>130.00 (-18.75%)</td><td>35.21 <b>(+81.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.70 (n/a)</td><td>179.02 (n/a)</td><td>178.50 (n/a)</td><td>160.00 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+5.74%)</td><td>0.03 (-1.94%)</td><td>0.03 (-14.00%)</td><td>0.02 <b>(+42.09%)</b></td><td>0.01 <b>(-25.77%)</b></td><td>272.60 <b>(-29.63%)</b></td><td>215.20 (-4.28%)</td><td>212.20 (+16.27%)</td><td>153.80 (-5.47%)</td><td>42.43 <b>(-54.27%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>387.40 (n/a)</td><td>224.82 (n/a)</td><td>182.50 (n/a)</td><td>162.70 (n/a)</td><td>92.78 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+14.70%)</td><td>0.04 (+6.91%)</td><td>0.04 (+7.83%)</td><td>0.03 (-0.74%)</td><td>0.00 <b>(+75.94%)</b></td><td>203.40 (+0.74%)</td><td>175.92 (-5.60%)</td><td>172.70 (-7.25%)</td><td>144.30 (-12.81%)</td><td>23.43 <b>(+54.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>186.36 (n/a)</td><td>186.20 (n/a)</td><td>165.50 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (+13.36%)</td><td>0.04 <b>(+23.23%)</b></td><td>0.04 <b>(+37.20%)</b></td><td>0.03 (+3.79%)</td><td>0.01 <b>(+42.68%)</b></td><td>229.20 (-3.66%)</td><td>161.64 (-17.54%)</td><td>145.80 <b>(-27.14%)</b></td><td>135.50 (-11.78%)</td><td>38.52 <b>(+26.91%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>196.02 (n/a)</td><td>200.10 (n/a)</td><td>153.60 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+0.81%)</td><td>0.04 (+1.44%)</td><td>0.04 (+0.66%)</td><td>0.03 (+0.65%)</td><td>0.01 (-10.95%)</td><td>208.70 (-0.62%)</td><td>167.18 (-1.89%)</td><td>163.00 (-0.67%)</td><td>138.40 (-0.79%)</td><td>26.29 (-10.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>170.40 (n/a)</td><td>164.10 (n/a)</td><td>139.50 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(+24.10%)</b></td><td>0.04 (+8.32%)</td><td>0.03 (+3.13%)</td><td>0.03 (+13.81%)</td><td>0.01 <b>(+25.07%)</b></td><td>220.10 (-12.10%)</td><td>179.68 (-7.47%)</td><td>182.90 (-3.02%)</td><td>130.00 (-19.40%)</td><td>32.22 (-12.95%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.40 (n/a)</td><td>194.18 (n/a)</td><td>188.60 (n/a)</td><td>161.30 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-11.88%)</td><td>0.03 (+8.28%)</td><td>0.03 (+10.16%)</td><td>0.03 <b>(+41.61%)</b></td><td>0.00 <b>(-59.91%)</b></td><td>223.10 <b>(-29.38%)</b></td><td>194.10 (-12.03%)</td><td>184.40 (-9.21%)</td><td>178.70 (+13.53%)</td><td>19.17 <b>(-68.67%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>315.90 (n/a)</td><td>220.64 (n/a)</td><td>203.10 (n/a)</td><td>157.40 (n/a)</td><td>61.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (+4.59%)</td><td>0.08 (+10.35%)</td><td>0.08 (+1.26%)</td><td>0.06 <b>(+59.81%)</b></td><td>0.01 <b>(-34.03%)</b></td><td>199.20 <b>(-37.42%)</b></td><td>159.72 (-15.48%)</td><td>155.40 (-1.27%)</td><td>127.00 (-4.37%)</td><td>28.32 <b>(-62.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>318.30 (n/a)</td><td>188.98 (n/a)</td><td>157.40 (n/a)</td><td>132.80 (n/a)</td><td>75.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (+11.60%)</td><td>0.08 (+17.90%)</td><td>0.07 (+11.17%)</td><td>0.07 (+16.11%)</td><td>0.01 <b>(+26.91%)</b></td><td>178.80 (-13.87%)</td><td>156.74 (-14.94%)</td><td>166.20 (-10.02%)</td><td>134.00 (-10.43%)</td><td>21.07 (-2.21%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>184.28 (n/a)</td><td>184.70 (n/a)</td><td>149.60 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (+18.76%)</td><td>0.08 <b>(+24.32%)</b></td><td>0.09 <b>(+24.63%)</b></td><td>0.07 <b>(+38.96%)</b></td><td>0.01 (+0.83%)</td><td>177.90 <b>(-28.03%)</b></td><td>150.84 <b>(-20.38%)</b></td><td>142.80 (-19.78%)</td><td>127.70 (-15.77%)</td><td>22.18 <b>(-39.30%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>247.20 (n/a)</td><td>189.46 (n/a)</td><td>178.00 (n/a)</td><td>151.60 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (-1.00%)</td><td>0.08 (+5.80%)</td><td>0.07 (-0.51%)</td><td>0.06 <b>(+29.54%)</b></td><td>0.01 <b>(-32.63%)</b></td><td>199.00 <b>(-22.81%)</b></td><td>163.94 (-8.76%)</td><td>166.60 (+0.48%)</td><td>131.00 (+1.00%)</td><td>25.36 <b>(-48.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>257.80 (n/a)</td><td>179.68 (n/a)</td><td>165.80 (n/a)</td><td>129.70 (n/a)</td><td>49.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 <b>(+24.29%)</b></td><td>0.09 <b>(+27.31%)</b></td><td>0.08 <b>(+30.58%)</b></td><td>0.07 (+17.68%)</td><td>0.01 <b>(+61.67%)</b></td><td>173.50 (-15.03%)</td><td>146.10 <b>(-20.78%)</b></td><td>148.10 <b>(-23.42%)</b></td><td>122.20 (-19.55%)</td><td>23.20 (+8.35%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>184.42 (n/a)</td><td>193.40 (n/a)</td><td>151.90 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (-16.94%)</td><td>0.08 <b>(+22.57%)</b></td><td>0.08 <b>(+36.68%)</b></td><td>0.07 <b>(+55.87%)</b></td><td>0.00 <b>(-77.20%)</b></td><td>174.40 <b>(-35.84%)</b></td><td>159.70 <b>(-23.32%)</b></td><td>155.90 <b>(-26.84%)</b></td><td>151.30 <b>(+20.37%)</b></td><td>9.84 <b>(-81.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>271.80 (n/a)</td><td>208.28 (n/a)</td><td>213.10 (n/a)</td><td>125.70 (n/a)</td><td>52.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (+10.66%)</td><td>0.06 (+2.55%)</td><td>0.06 (-5.41%)</td><td>0.04 (+19.86%)</td><td>0.01 (+2.23%)</td><td>287.60 (-16.57%)</td><td>218.06 (-3.77%)</td><td>211.20 (+5.71%)</td><td>161.00 (-9.60%)</td><td>50.62 <b>(-25.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>344.70 (n/a)</td><td>226.60 (n/a)</td><td>199.80 (n/a)</td><td>178.10 (n/a)</td><td>67.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (+8.78%)</td><td>0.06 (+13.36%)</td><td>0.06 (+0.06%)</td><td>0.04 <b>(+32.71%)</b></td><td>0.02 (-2.75%)</td><td>273.50 <b>(-24.66%)</b></td><td>203.74 (-14.07%)</td><td>206.10 (-0.05%)</td><td>149.20 (-8.07%)</td><td>49.58 <b>(-35.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>363.00 (n/a)</td><td>237.10 (n/a)</td><td>206.20 (n/a)</td><td>162.30 (n/a)</td><td>77.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (+3.97%)</td><td>0.17 (+10.57%)</td><td>0.16 (+11.67%)</td><td>0.14 <b>(+22.18%)</b></td><td>0.02 (-16.41%)</td><td>177.50 (-18.17%)</td><td>151.40 (-10.84%)</td><td>153.70 (-10.43%)</td><td>128.70 (-3.81%)</td><td>22.35 <b>(-34.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.90 (n/a)</td><td>169.80 (n/a)</td><td>171.60 (n/a)</td><td>133.80 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 <b>(+29.16%)</b></td><td>0.15 <b>(+23.00%)</b></td><td>0.15 <b>(+24.71%)</b></td><td>0.13 (+14.71%)</td><td>0.01 <b>(+149.14%)</b></td><td>189.70 (-12.82%)</td><td>168.96 (-18.21%)</td><td>164.80 (-19.84%)</td><td>152.10 <b>(-22.56%)</b></td><td>16.85 <b>(+68.26%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>206.58 (n/a)</td><td>205.60 (n/a)</td><td>196.40 (n/a)</td><td>10.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 <b>(+43.39%)</b></td><td>0.17 <b>(+39.43%)</b></td><td>0.16 <b>(+36.81%)</b></td><td>0.14 <b>(+48.86%)</b></td><td>0.03 <b>(+34.19%)</b></td><td>177.40 <b>(-32.83%)</b></td><td>150.62 <b>(-28.53%)</b></td><td>154.60 <b>(-26.90%)</b></td><td>118.70 <b>(-30.30%)</b></td><td>22.23 <b>(-37.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>264.10 (n/a)</td><td>210.76 (n/a)</td><td>211.50 (n/a)</td><td>170.30 (n/a)</td><td>35.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (-18.91%)</td><td>0.15 (+1.81%)</td><td>0.16 <b>(+24.16%)</b></td><td>0.11 (-6.04%)</td><td>0.02 <b>(-39.00%)</b></td><td>222.50 (+6.46%)</td><td>165.58 (-4.16%)</td><td>150.80 (-19.44%)</td><td>149.70 <b>(+23.31%)</b></td><td>31.87 <b>(-20.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>209.00 (n/a)</td><td>172.76 (n/a)</td><td>187.20 (n/a)</td><td>121.40 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 <b>(+54.23%)</b></td><td>0.15 <b>(+23.23%)</b></td><td>0.17 <b>(+28.45%)</b></td><td>0.07 <b>(-38.93%)</b></td><td>0.05 <b>(+753.63%)</b></td><td>350.70 <b>(+63.73%)</b></td><td>184.32 (-5.96%)</td><td>148.70 <b>(-22.15%)</b></td><td>122.70 <b>(-35.15%)</b></td><td>95.53 <b>(+815.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>196.00 (n/a)</td><td>191.00 (n/a)</td><td>189.20 (n/a)</td><td>10.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (+15.07%)</td><td>0.14 (+1.79%)</td><td>0.14 (-1.99%)</td><td>0.09 (-12.52%)</td><td>0.03 <b>(+47.81%)</b></td><td>274.60 (+14.32%)</td><td>190.38 (+0.95%)</td><td>176.50 (+2.02%)</td><td>137.10 (-13.06%)</td><td>51.12 <b>(+51.30%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>240.20 (n/a)</td><td>188.58 (n/a)</td><td>173.00 (n/a)</td><td>157.70 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 <b>(+25.76%)</b></td><td>0.13 <b>(+20.52%)</b></td><td>0.13 (+11.42%)</td><td>0.11 <b>(+64.83%)</b></td><td>0.02 (-12.07%)</td><td>217.20 <b>(-39.31%)</b></td><td>190.52 (-19.73%)</td><td>195.00 (-10.26%)</td><td>148.00 <b>(-20.47%)</b></td><td>27.05 <b>(-60.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>357.90 (n/a)</td><td>237.34 (n/a)</td><td>217.30 (n/a)</td><td>186.10 (n/a)</td><td>68.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 <b>(+24.73%)</b></td><td>0.13 <b>(+39.07%)</b></td><td>0.13 <b>(+25.37%)</b></td><td>0.12 <b>(+64.71%)</b></td><td>0.01 <b>(-41.32%)</b></td><td>207.40 <b>(-39.30%)</b></td><td>185.04 <b>(-31.07%)</b></td><td>190.40 <b>(-20.23%)</b></td><td>158.90 (-19.83%)</td><td>18.28 <b>(-73.22%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>341.70 (n/a)</td><td>268.46 (n/a)</td><td>238.70 (n/a)</td><td>198.20 (n/a)</td><td>68.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.38 (-13.12%)</td><td>0.30 (+2.34%)</td><td>0.28 (+10.31%)</td><td>0.26 (+12.51%)</td><td>0.05 <b>(-40.70%)</b></td><td>192.00 (-11.11%)</td><td>169.40 (-5.70%)</td><td>175.30 (-9.36%)</td><td>128.60 (+15.13%)</td><td>26.03 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>216.00 (n/a)</td><td>179.64 (n/a)</td><td>193.40 (n/a)</td><td>111.70 (n/a)</td><td>42.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.42 (+13.94%)</td><td>0.31 (-2.54%)</td><td>0.29 (-11.32%)</td><td>0.27 (+7.00%)</td><td>0.06 (+19.89%)</td><td>183.80 (-6.51%)</td><td>162.82 (+3.00%)</td><td>166.90 (+12.77%)</td><td>118.30 (-12.24%)</td><td>26.58 (-1.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>196.60 (n/a)</td><td>158.08 (n/a)</td><td>148.00 (n/a)</td><td>134.80 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (-12.20%)</td><td>0.27 (-9.96%)</td><td>0.27 (-18.65%)</td><td>0.24 (+2.41%)</td><td>0.03 <b>(-51.38%)</b></td><td>206.10 (-2.32%)</td><td>183.28 (+8.55%)</td><td>183.70 <b>(+22.88%)</b></td><td>160.40 (+13.92%)</td><td>18.59 <b>(-45.68%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.00 (n/a)</td><td>168.84 (n/a)</td><td>149.50 (n/a)</td><td>140.80 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (-11.95%)</td><td>0.27 (-0.93%)</td><td>0.29 (+8.87%)</td><td>0.22 (+4.88%)</td><td>0.03 <b>(-40.88%)</b></td><td>220.70 (-4.67%)</td><td>183.90 (-0.73%)</td><td>171.60 (-8.14%)</td><td>168.50 (+13.54%)</td><td>22.24 <b>(-35.13%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>231.50 (n/a)</td><td>185.26 (n/a)</td><td>186.80 (n/a)</td><td>148.40 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 (-1.50%)</td><td>0.26 (-11.29%)</td><td>0.25 (-11.91%)</td><td>0.21 <b>(-21.63%)</b></td><td>0.05 <b>(+48.98%)</b></td><td>234.40 <b>(+27.60%)</b></td><td>191.70 (+14.45%)</td><td>197.90 (+13.54%)</td><td>150.50 (+1.55%)</td><td>32.21 <b>(+92.73%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>167.50 (n/a)</td><td>174.30 (n/a)</td><td>148.20 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 <b>(-20.56%)</b></td><td>0.29 (+4.82%)</td><td>0.30 <b>(+21.63%)</b></td><td>0.24 (+2.43%)</td><td>0.03 <b>(-55.44%)</b></td><td>202.60 (-2.41%)</td><td>171.42 (-6.91%)</td><td>161.30 (-17.79%)</td><td>159.50 <b>(+25.89%)</b></td><td>18.42 <b>(-43.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>207.60 (n/a)</td><td>184.14 (n/a)</td><td>196.20 (n/a)</td><td>126.70 (n/a)</td><td>32.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 <b>(-20.03%)</b></td><td>0.28 (-3.88%)</td><td>0.28 (+10.94%)</td><td>0.26 (+9.44%)</td><td>0.02 <b>(-70.10%)</b></td><td>191.00 (-8.61%)</td><td>176.68 (+0.22%)</td><td>178.50 (-9.89%)</td><td>156.60 <b>(+24.98%)</b></td><td>12.48 <b>(-66.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>209.00 (n/a)</td><td>176.30 (n/a)</td><td>198.10 (n/a)</td><td>125.30 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (-7.98%)</td><td>0.24 (+3.33%)</td><td>0.27 (+13.84%)</td><td>0.16 (-3.26%)</td><td>0.05 (-2.58%)</td><td>298.00 (+3.36%)</td><td>211.92 (-2.95%)</td><td>183.60 (-12.15%)</td><td>174.80 (+8.71%)</td><td>51.48 (+9.32%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>288.30 (n/a)</td><td>218.36 (n/a)</td><td>209.00 (n/a)</td><td>160.80 (n/a)</td><td>47.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 <b>(+55.49%)</b></td><td>0.02 <b>(+40.98%)</b></td><td>0.02 <b>(+55.29%)</b></td><td>0.01 <b>(-28.25%)</b></td><td>0.01 <b>(+286.31%)</b></td><td>335.40 <b>(+39.34%)</b></td><td>163.72 (-16.97%)</td><td>119.60 <b>(-35.63%)</b></td><td>111.00 <b>(-35.65%)</b></td><td>96.30 <b>(+260.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>240.70 (n/a)</td><td>197.18 (n/a)</td><td>185.80 (n/a)</td><td>172.50 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (+1.99%)</td><td>0.02 <b>(+27.45%)</b></td><td>0.02 <b>(+58.46%)</b></td><td>0.02 <b>(+42.85%)</b></td><td>0.00 <b>(-44.42%)</b></td><td>166.30 <b>(-30.01%)</b></td><td>132.92 <b>(-26.44%)</b></td><td>130.20 <b>(-36.89%)</b></td><td>113.40 (-1.90%)</td><td>21.06 <b>(-61.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>180.70 (n/a)</td><td>206.30 (n/a)</td><td>115.60 (n/a)</td><td>54.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+13.95%)</td><td>0.02 (+5.68%)</td><td>0.02 (+2.32%)</td><td>0.01 (-14.19%)</td><td>0.00 <b>(+54.10%)</b></td><td>212.60 (+16.56%)</td><td>153.42 (-2.34%)</td><td>150.90 (-2.27%)</td><td>104.40 (-12.27%)</td><td>40.37 <b>(+55.84%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>182.40 (n/a)</td><td>157.10 (n/a)</td><td>154.40 (n/a)</td><td>119.00 (n/a)</td><td>25.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 <b>(+28.74%)</b></td><td>0.02 (-1.97%)</td><td>0.02 (+6.08%)</td><td>0.01 <b>(-38.40%)</b></td><td>0.01 <b>(+82.61%)</b></td><td>377.00 <b>(+62.36%)</b></td><td>204.76 (+15.76%)</td><td>170.60 (-5.75%)</td><td>105.40 <b>(-22.33%)</b></td><td>102.89 <b>(+151.22%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>232.20 (n/a)</td><td>176.88 (n/a)</td><td>181.00 (n/a)</td><td>135.70 (n/a)</td><td>40.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (+18.78%)</td><td>0.01 (+1.65%)</td><td>0.02 (+9.03%)</td><td>0.01 (-9.65%)</td><td>0.00 <b>(+107.00%)</b></td><td>219.90 (+10.67%)</td><td>182.08 (+1.00%)</td><td>173.30 (-8.26%)</td><td>130.70 (-15.79%)</td><td>36.28 <b>(+95.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.70 (n/a)</td><td>180.28 (n/a)</td><td>188.90 (n/a)</td><td>155.20 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 <b>(+29.71%)</b></td><td>0.02 (+14.81%)</td><td>0.01 (-1.27%)</td><td>0.01 (-5.17%)</td><td>0.00 <b>(+186.58%)</b></td><td>228.20 (+5.45%)</td><td>174.66 (-7.40%)</td><td>188.80 (+1.29%)</td><td>121.00 <b>(-22.88%)</b></td><td>50.12 <b>(+124.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>188.62 (n/a)</td><td>186.40 (n/a)</td><td>156.90 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (-11.48%)</td><td>0.01 (+15.23%)</td><td>0.01 <b>(+22.31%)</b></td><td>0.01 <b>(+62.35%)</b></td><td>0.00 <b>(-50.20%)</b></td><td>223.00 <b>(-38.41%)</b></td><td>186.70 (-19.23%)</td><td>176.50 (-18.25%)</td><td>163.60 (+12.98%)</td><td>26.85 <b>(-66.72%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>362.10 (n/a)</td><td>231.16 (n/a)</td><td>215.90 (n/a)</td><td>144.80 (n/a)</td><td>80.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.01 (+3.27%)</td><td>0.01 (-2.52%)</td><td>0.01 (+1.17%)</td><td>0.01 <b>(-24.47%)</b></td><td>0.00 <b>(+132.35%)</b></td><td>313.00 <b>(+32.40%)</b></td><td>224.62 (+5.95%)</td><td>206.20 (-1.15%)</td><td>183.90 (-3.16%)</td><td>53.07 <b>(+198.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>236.40 (n/a)</td><td>212.00 (n/a)</td><td>208.60 (n/a)</td><td>189.90 (n/a)</td><td>17.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (-0.81%)</td><td>0.03 (+2.00%)</td><td>0.03 (+1.15%)</td><td>0.02 (+3.13%)</td><td>0.01 (-9.01%)</td><td>229.60 (-3.04%)</td><td>166.86 (-2.63%)</td><td>154.40 (-1.15%)</td><td>135.10 (+0.82%)</td><td>36.77 (-9.30%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>171.36 (n/a)</td><td>156.20 (n/a)</td><td>134.00 (n/a)</td><td>40.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+14.15%)</td><td>0.04 (+18.55%)</td><td>0.04 <b>(+33.21%)</b></td><td>0.03 <b>(+52.69%)</b></td><td>0.01 (-8.03%)</td><td>188.70 <b>(-34.50%)</b></td><td>148.26 (-18.70%)</td><td>130.00 <b>(-24.94%)</b></td><td>117.60 (-12.43%)</td><td>33.55 <b>(-46.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>288.10 (n/a)</td><td>182.36 (n/a)</td><td>173.20 (n/a)</td><td>134.30 (n/a)</td><td>62.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(+26.04%)</b></td><td>0.04 <b>(+23.93%)</b></td><td>0.04 <b>(+24.78%)</b></td><td>0.03 (+18.08%)</td><td>0.01 <b>(+38.57%)</b></td><td>157.80 (-15.30%)</td><td>134.28 (-19.04%)</td><td>135.80 (-19.88%)</td><td>107.50 <b>(-20.66%)</b></td><td>18.19 (-7.36%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>165.86 (n/a)</td><td>169.50 (n/a)</td><td>135.50 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+5.99%)</td><td>0.03 (-0.64%)</td><td>0.03 (-2.74%)</td><td>0.02 <b>(-25.55%)</b></td><td>0.01 <b>(+47.98%)</b></td><td>284.20 <b>(+34.31%)</b></td><td>180.12 (+5.48%)</td><td>166.50 (+2.78%)</td><td>126.60 (-5.66%)</td><td>61.18 <b>(+94.72%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>170.76 (n/a)</td><td>162.00 (n/a)</td><td>134.20 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+9.79%)</td><td>0.04 (+17.57%)</td><td>0.04 <b>(+31.86%)</b></td><td>0.03 <b>(+22.73%)</b></td><td>0.01 (-8.58%)</td><td>188.90 (-18.51%)</td><td>150.10 (-15.88%)</td><td>140.10 <b>(-24.15%)</b></td><td>128.50 (-8.93%)</td><td>24.70 <b>(-31.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>178.44 (n/a)</td><td>184.70 (n/a)</td><td>141.10 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (-9.49%)</td><td>0.03 (+2.49%)</td><td>0.03 (-5.22%)</td><td>0.03 <b>(+30.36%)</b></td><td>0.00 <b>(-50.63%)</b></td><td>189.20 <b>(-23.31%)</b></td><td>163.08 (-6.52%)</td><td>165.00 (+5.50%)</td><td>135.70 (+10.50%)</td><td>19.04 <b>(-59.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>174.46 (n/a)</td><td>156.40 (n/a)</td><td>122.80 (n/a)</td><td>46.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 <b>(-31.74%)</b></td><td>0.03 (-17.77%)</td><td>0.03 (-14.10%)</td><td>0.03 (+1.75%)</td><td>0.00 <b>(-80.23%)</b></td><td>193.10 (-1.73%)</td><td>182.82 (+18.51%)</td><td>181.00 (+16.40%)</td><td>172.00 <b>(+46.51%)</b></td><td>8.15 <b>(-71.45%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>154.26 (n/a)</td><td>155.50 (n/a)</td><td>117.40 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+16.79%)</td><td>0.03 (+2.43%)</td><td>0.03 (-11.64%)</td><td>0.02 (-5.54%)</td><td>0.01 <b>(+204.68%)</b></td><td>218.60 (+5.86%)</td><td>190.44 (-0.01%)</td><td>207.90 (+13.11%)</td><td>152.90 (-14.34%)</td><td>33.91 <b>(+173.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>190.46 (n/a)</td><td>183.80 (n/a)</td><td>178.50 (n/a)</td><td>12.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (-11.04%)</td><td>0.07 (-5.13%)</td><td>0.07 (+2.77%)</td><td>0.05 (+15.38%)</td><td>0.01 <b>(-32.49%)</b></td><td>201.70 (-13.32%)</td><td>159.80 (+1.45%)</td><td>147.10 (-2.71%)</td><td>126.10 (+12.39%)</td><td>34.55 <b>(-30.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>157.52 (n/a)</td><td>151.20 (n/a)</td><td>112.20 (n/a)</td><td>49.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-15.58%)</td><td>0.06 (-18.26%)</td><td>0.06 (-16.58%)</td><td>0.04 <b>(-28.91%)</b></td><td>0.01 (-4.55%)</td><td>246.80 <b>(+40.63%)</b></td><td>185.30 <b>(+23.48%)</b></td><td>176.90 (+19.85%)</td><td>153.00 (+18.42%)</td><td>35.83 <b>(+67.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>175.50 (n/a)</td><td>150.06 (n/a)</td><td>147.60 (n/a)</td><td>129.20 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (+2.92%)</td><td>0.07 (+2.87%)</td><td>0.07 (-0.45%)</td><td>0.05 (-0.43%)</td><td>0.01 (-2.10%)</td><td>231.10 (+0.43%)</td><td>168.42 (-3.11%)</td><td>153.70 (+0.46%)</td><td>124.80 (-2.80%)</td><td>40.33 (-4.69%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>173.82 (n/a)</td><td>153.00 (n/a)</td><td>128.40 (n/a)</td><td>42.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-18.75%)</td><td>0.06 (-7.72%)</td><td>0.06 (-3.82%)</td><td>0.05 (+0.58%)</td><td>0.01 <b>(-55.02%)</b></td><td>201.70 (-0.59%)</td><td>169.12 (+4.77%)</td><td>169.20 (+3.93%)</td><td>145.70 <b>(+23.06%)</b></td><td>20.75 <b>(-44.58%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>202.90 (n/a)</td><td>161.42 (n/a)</td><td>162.80 (n/a)</td><td>118.40 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 <b>(-20.05%)</b></td><td>0.06 (-12.57%)</td><td>0.07 (+2.19%)</td><td>0.04 <b>(-24.79%)</b></td><td>0.01 <b>(-23.56%)</b></td><td>267.80 <b>(+32.97%)</b></td><td>186.42 (+14.20%)</td><td>160.00 (-2.14%)</td><td>154.20 <b>(+25.06%)</b></td><td>47.96 <b>(+26.52%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>163.24 (n/a)</td><td>163.50 (n/a)</td><td>123.30 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (-8.79%)</td><td>0.06 (-10.24%)</td><td>0.06 (-11.96%)</td><td>0.04 (-19.98%)</td><td>0.01 (+1.87%)</td><td>274.70 <b>(+24.98%)</b></td><td>192.10 (+13.21%)</td><td>186.50 (+13.58%)</td><td>133.30 (+9.62%)</td><td>51.31 <b>(+44.44%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>169.68 (n/a)</td><td>164.20 (n/a)</td><td>121.60 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-1.65%)</td><td>0.06 (-6.90%)</td><td>0.05 (-17.38%)</td><td>0.05 (+15.74%)</td><td>0.01 <b>(-29.58%)</b></td><td>199.60 (-13.63%)</td><td>184.38 (+5.76%)</td><td>193.60 <b>(+21.00%)</b></td><td>148.80 (+1.71%)</td><td>20.53 <b>(-40.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>174.34 (n/a)</td><td>160.00 (n/a)</td><td>146.30 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-18.83%)</td><td>0.05 (-13.35%)</td><td>0.05 <b>(-22.73%)</b></td><td>0.04 (+3.08%)</td><td>0.01 <b>(-46.71%)</b></td><td>234.30 (-2.98%)</td><td>210.72 (+12.85%)</td><td>220.40 <b>(+29.42%)</b></td><td>176.40 <b>(+23.18%)</b></td><td>24.68 <b>(-37.03%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>241.50 (n/a)</td><td>186.72 (n/a)</td><td>170.30 (n/a)</td><td>143.20 (n/a)</td><td>39.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 <b>(-20.18%)</b></td><td>0.12 (+12.90%)</td><td>0.12 <b>(+26.63%)</b></td><td>0.10 <b>(+81.55%)</b></td><td>0.02 <b>(-66.42%)</b></td><td>201.00 <b>(-44.93%)</b></td><td>173.78 <b>(-21.71%)</b></td><td>170.00 <b>(-21.04%)</b></td><td>146.00 <b>(+25.21%)</b></td><td>21.34 <b>(-76.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>365.00 (n/a)</td><td>221.96 (n/a)</td><td>215.30 (n/a)</td><td>116.60 (n/a)</td><td>91.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (-17.31%)</td><td>0.11 <b>(-23.41%)</b></td><td>0.11 <b>(-21.75%)</b></td><td>0.08 <b>(-25.75%)</b></td><td>0.02 (-14.57%)</td><td>273.60 <b>(+34.71%)</b></td><td>201.92 <b>(+31.42%)</b></td><td>197.00 <b>(+27.84%)</b></td><td>150.20 <b>(+20.93%)</b></td><td>45.31 <b>(+43.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.10 (n/a)</td><td>153.64 (n/a)</td><td>154.10 (n/a)</td><td>124.20 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (-2.92%)</td><td>0.13 (+3.24%)</td><td>0.13 (+0.69%)</td><td>0.10 <b>(+29.65%)</b></td><td>0.02 <b>(-28.06%)</b></td><td>211.50 <b>(-22.87%)</b></td><td>163.78 (-6.77%)</td><td>159.00 (-0.69%)</td><td>136.50 (+3.02%)</td><td>30.37 <b>(-46.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>274.20 (n/a)</td><td>175.68 (n/a)</td><td>160.10 (n/a)</td><td>132.50 (n/a)</td><td>56.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 <b>(+43.54%)</b></td><td>0.13 (+15.15%)</td><td>0.13 (+6.29%)</td><td>0.11 (+15.37%)</td><td>0.03 <b>(+115.24%)</b></td><td>190.30 (-13.34%)</td><td>162.94 (-10.98%)</td><td>167.50 (-5.95%)</td><td>111.30 <b>(-30.31%)</b></td><td>32.49 <b>(+30.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>183.04 (n/a)</td><td>178.10 (n/a)</td><td>159.70 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-9.71%)</td><td>0.11 (-13.25%)</td><td>0.11 (-11.01%)</td><td>0.09 <b>(-20.60%)</b></td><td>0.02 <b>(+58.87%)</b></td><td>237.40 <b>(+25.94%)</b></td><td>198.38 (+17.32%)</td><td>190.80 (+12.37%)</td><td>162.00 (+10.81%)</td><td>34.67 <b>(+127.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>169.10 (n/a)</td><td>169.80 (n/a)</td><td>146.20 (n/a)</td><td>15.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (-14.83%)</td><td>0.12 (-4.90%)</td><td>0.13 (+1.19%)</td><td>0.08 (-15.46%)</td><td>0.03 (-6.15%)</td><td>260.50 (+18.30%)</td><td>179.10 (+6.28%)</td><td>161.50 (-1.16%)</td><td>137.70 (+17.39%)</td><td>50.20 <b>(+32.36%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>220.20 (n/a)</td><td>168.52 (n/a)</td><td>163.40 (n/a)</td><td>117.30 (n/a)</td><td>37.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-2.85%)</td><td>0.11 (-8.41%)</td><td>0.11 (-7.98%)</td><td>0.08 (-17.78%)</td><td>0.02 <b>(+31.48%)</b></td><td>267.10 <b>(+21.57%)</b></td><td>199.58 (+11.16%)</td><td>197.20 (+8.65%)</td><td>160.10 (+2.96%)</td><td>43.06 <b>(+64.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>219.70 (n/a)</td><td>179.54 (n/a)</td><td>181.50 (n/a)</td><td>155.50 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 <b>(-27.28%)</b></td><td>0.09 (-11.58%)</td><td>0.10 (-16.83%)</td><td>0.08 <b>(+36.07%)</b></td><td>0.01 <b>(-72.85%)</b></td><td>262.80 <b>(-26.51%)</b></td><td>224.68 (+4.12%)</td><td>217.20 <b>(+20.20%)</b></td><td>206.70 <b>(+37.52%)</b></td><td>21.93 <b>(-73.44%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>357.60 (n/a)</td><td>215.78 (n/a)</td><td>180.70 (n/a)</td><td>150.30 (n/a)</td><td>82.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>170.86 (n/a)</td><td>175.70 (n/a)</td><td>144.00 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>159.12 (n/a)</td><td>145.60 (n/a)</td><td>113.40 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>192.24 (n/a)</td><td>179.20 (n/a)</td><td>144.70 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>192.74 (n/a)</td><td>200.70 (n/a)</td><td>167.10 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>329.30 (n/a)</td><td>193.66 (n/a)</td><td>169.00 (n/a)</td><td>146.60 (n/a)</td><td>76.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>172.10 (n/a)</td><td>164.16 (n/a)</td><td>164.90 (n/a)</td><td>156.30 (n/a)</td><td>6.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>197.64 (n/a)</td><td>200.60 (n/a)</td><td>155.60 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>211.16 (n/a)</td><td>214.90 (n/a)</td><td>174.40 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>197.70 (n/a)</td><td>202.70 (n/a)</td><td>171.50 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>279.10 (n/a)</td><td>204.92 (n/a)</td><td>186.10 (n/a)</td><td>166.20 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>196.42 (n/a)</td><td>194.70 (n/a)</td><td>174.50 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>196.30 (n/a)</td><td>196.40 (n/a)</td><td>170.40 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 <b>(-31.87%)</b></td><td>0.23 (-17.71%)</td><td>0.22 (-18.12%)</td><td>0.22 (-4.36%)</td><td>0.02 <b>(-68.79%)</b></td><td>227.50 (+4.55%)</td><td>213.68 (+17.64%)</td><td>223.20 <b>(+22.10%)</b></td><td>186.00 <b>(+46.80%)</b></td><td>17.71 <b>(-52.18%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>217.60 (n/a)</td><td>181.64 (n/a)</td><td>182.80 (n/a)</td><td>126.70 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>224.90 (n/a)</td><td>188.08 (n/a)</td><td>181.90 (n/a)</td><td>170.00 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>220.60 (n/a)</td><td>192.58 (n/a)</td><td>196.30 (n/a)</td><td>156.10 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>274.60 (n/a)</td><td>212.42 (n/a)</td><td>214.60 (n/a)</td><td>145.90 (n/a)</td><td>45.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>179.46 (n/a)</td><td>176.00 (n/a)</td><td>122.10 (n/a)</td><td>45.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.00 (n/a)</td><td>162.20 (n/a)</td><td>170.10 (n/a)</td><td>122.00 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.60 (n/a)</td><td>179.06 (n/a)</td><td>187.80 (n/a)</td><td>118.50 (n/a)</td><td>47.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>168.06 (n/a)</td><td>164.30 (n/a)</td><td>142.40 (n/a)</td><td>19.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>153.02 (n/a)</td><td>151.90 (n/a)</td><td>117.50 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>241.10 (n/a)</td><td>173.64 (n/a)</td><td>167.80 (n/a)</td><td>127.30 (n/a)</td><td>44.70 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>167.90 (n/a)</td><td>161.50 (n/a)</td><td>135.90 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>184.36 (n/a)</td><td>182.40 (n/a)</td><td>157.10 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>215.60 (n/a)</td><td>167.04 (n/a)</td><td>169.70 (n/a)</td><td>111.10 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>166.10 (n/a)</td><td>144.34 (n/a)</td><td>146.90 (n/a)</td><td>119.80 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>181.50 (n/a)</td><td>156.26 (n/a)</td><td>164.40 (n/a)</td><td>126.80 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>181.18 (n/a)</td><td>175.90 (n/a)</td><td>166.60 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>177.60 (n/a)</td><td>143.60 (n/a)</td><td>142.20 (n/a)</td><td>114.10 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>264.60 (n/a)</td><td>207.26 (n/a)</td><td>209.80 (n/a)</td><td>156.50 (n/a)</td><td>44.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>174.54 (n/a)</td><td>170.80 (n/a)</td><td>162.80 (n/a)</td><td>12.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.70 (n/a)</td><td>157.14 (n/a)</td><td>151.60 (n/a)</td><td>137.20 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>163.00 (n/a)</td><td>172.10 (n/a)</td><td>123.30 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>165.84 (n/a)</td><td>189.60 (n/a)</td><td>100.80 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>194.96 (n/a)</td><td>197.00 (n/a)</td><td>121.80 (n/a)</td><td>46.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>189.72 (n/a)</td><td>213.70 (n/a)</td><td>145.70 (n/a)</td><td>39.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.10 (n/a)</td><td>195.62 (n/a)</td><td>180.40 (n/a)</td><td>157.40 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.70 (n/a)</td><td>196.70 (n/a)</td><td>193.80 (n/a)</td><td>137.50 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.10 (n/a)</td><td>209.90 (n/a)</td><td>207.40 (n/a)</td><td>174.40 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.20 (n/a)</td><td>200.82 (n/a)</td><td>197.40 (n/a)</td><td>153.00 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>174.82 (n/a)</td><td>185.50 (n/a)</td><td>123.40 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.50 (n/a)</td><td>199.40 (n/a)</td><td>198.40 (n/a)</td><td>189.00 (n/a)</td><td>7.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>229.10 (n/a)</td><td>188.06 (n/a)</td><td>182.70 (n/a)</td><td>167.40 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>196.40 (n/a)</td><td>197.70 (n/a)</td><td>158.50 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.90 (n/a)</td><td>198.08 (n/a)</td><td>192.70 (n/a)</td><td>153.00 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.70 (n/a)</td><td>206.82 (n/a)</td><td>192.90 (n/a)</td><td>145.30 (n/a)</td><td>64.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.30 (n/a)</td><td>217.52 (n/a)</td><td>216.00 (n/a)</td><td>155.10 (n/a)</td><td>42.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>187.94 (n/a)</td><td>183.70 (n/a)</td><td>149.60 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>176.58 (n/a)</td><td>176.50 (n/a)</td><td>134.50 (n/a)</td><td>38.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>193.26 (n/a)</td><td>183.30 (n/a)</td><td>163.90 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.60 (n/a)</td><td>167.66 (n/a)</td><td>172.00 (n/a)</td><td>119.80 (n/a)</td><td>34.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>183.94 (n/a)</td><td>176.40 (n/a)</td><td>155.30 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>253.80 (n/a)</td><td>203.86 (n/a)</td><td>188.10 (n/a)</td><td>149.20 (n/a)</td><td>45.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>180.60 (n/a)</td><td>182.80 (n/a)</td><td>139.00 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>262.60 (n/a)</td><td>212.82 (n/a)</td><td>205.80 (n/a)</td><td>178.80 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>246.50 (n/a)</td><td>198.82 (n/a)</td><td>198.70 (n/a)</td><td>169.20 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.80 (n/a)</td><td>191.70 (n/a)</td><td>198.10 (n/a)</td><td>132.90 (n/a)</td><td>40.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>242.60 (n/a)</td><td>203.34 (n/a)</td><td>230.50 (n/a)</td><td>138.50 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>184.16 (n/a)</td><td>182.60 (n/a)</td><td>159.60 (n/a)</td><td>22.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>300.80 (n/a)</td><td>217.48 (n/a)</td><td>216.20 (n/a)</td><td>159.90 (n/a)</td><td>51.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>189.34 (n/a)</td><td>187.40 (n/a)</td><td>179.10 (n/a)</td><td>8.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.70 (n/a)</td><td>209.22 (n/a)</td><td>215.00 (n/a)</td><td>185.90 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>4.95 (+2.54%)</td><td>4.43 (+2.29%)</td><td>4.18 (-2.21%)</td><td>4.05 (-0.28%)</td><td>0.43 <b>(+39.04%)</b></td><td>2324.00 (+0.28%)</td><td>2136.18 (-1.90%)</td><td>2250.50 (+2.26%)</td><td>1901.10 (-2.47%)</td><td>200.96 <b>(+35.04%)</b></td><td>1945.91 (+2.54%)</td><td>1744.51 (+2.29%)</td><td>1643.80 (-2.21%)</td><td>1591.80 (-0.28%)</td><td>169.44 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>4.82 (n/a)</td><td>4.34 (n/a)</td><td>4.27 (n/a)</td><td>4.06 (n/a)</td><td>0.31 (n/a)</td><td>2317.40 (n/a)</td><td>2177.60 (n/a)</td><td>2200.70 (n/a)</td><td>1949.30 (n/a)</td><td>148.82 (n/a)</td><td>1897.78 (n/a)</td><td>1705.49 (n/a)</td><td>1681.01 (n/a)</td><td>1596.34 (n/a)</td><td>121.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.18 (+19.00%)</td><td>1.07 <b>(+27.68%)</b></td><td>1.04 (+8.04%)</td><td>0.96 <b>(+72.75%)</b></td><td>0.10 <b>(-49.72%)</b></td><td>229.90 <b>(-42.12%)</b></td><td>208.40 <b>(-25.25%)</b></td><td>212.70 (-7.44%)</td><td>186.70 (-15.94%)</td><td>19.20 <b>(-75.11%)</b></td><td>50.56 (+19.00%)</td><td>45.60 <b>(+27.68%)</b></td><td>44.38 (+8.04%)</td><td>41.05 <b>(+72.75%)</b></td><td>4.26 <b>(-49.72%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.00 (n/a)</td><td>0.84 (n/a)</td><td>0.96 (n/a)</td><td>0.56 (n/a)</td><td>0.20 (n/a)</td><td>397.20 (n/a)</td><td>278.80 (n/a)</td><td>229.80 (n/a)</td><td>222.10 (n/a)</td><td>77.15 (n/a)</td><td>42.49 (n/a)</td><td>35.71 (n/a)</td><td>41.07 (n/a)</td><td>23.76 (n/a)</td><td>8.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.22 (+6.46%)</td><td>1.13 <b>(+21.30%)</b></td><td>1.14 <b>(+22.42%)</b></td><td>1.03 <b>(+49.33%)</b></td><td>0.08 <b>(-55.33%)</b></td><td>215.40 <b>(-33.04%)</b></td><td>196.10 (-19.67%)</td><td>193.50 (-18.32%)</td><td>180.60 (-6.04%)</td><td>13.56 <b>(-72.35%)</b></td><td>52.27 (+6.46%)</td><td>48.31 <b>(+21.30%)</b></td><td>48.78 <b>(+22.42%)</b></td><td>43.80 <b>(+49.33%)</b></td><td>3.29 <b>(-55.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.15 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.69 (n/a)</td><td>0.17 (n/a)</td><td>321.70 (n/a)</td><td>244.12 (n/a)</td><td>236.90 (n/a)</td><td>192.20 (n/a)</td><td>49.04 (n/a)</td><td>49.09 (n/a)</td><td>39.82 (n/a)</td><td>39.84 (n/a)</td><td>29.33 (n/a)</td><td>7.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.52 (-0.09%)</td><td>0.52 (-0.09%)</td><td>0.52 (-0.06%)</td><td>0.52 (-0.09%)</td><td>0.00 (+11.00%)</td><td>48738.20 (+0.09%)</td><td>48677.34 (+0.09%)</td><td>48653.50 (+0.06%)</td><td>48643.00 (+0.09%)</td><td>42.24 (+11.15%)</td><td>353.18 (-0.09%)</td><td>352.93 (-0.09%)</td><td>353.11 (-0.06%)</td><td>352.49 (-0.09%)</td><td>0.31 (+11.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48694.20 (n/a)</td><td>48632.26 (n/a)</td><td>48622.40 (n/a)</td><td>48597.60 (n/a)</td><td>38.00 (n/a)</td><td>353.51 (n/a)</td><td>353.26 (n/a)</td><td>353.33 (n/a)</td><td>352.81 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (-0.75%)</td><td>0.21 (-0.43%)</td><td>0.21 (-0.73%)</td><td>0.21 (+0.65%)</td><td>0.00 <b>(-39.55%)</b></td><td>119043.80 (-0.64%)</td><td>118167.18 (+0.42%)</td><td>118441.00 (+0.74%)</td><td>117179.00 (+0.75%)</td><td>837.97 <b>(-39.54%)</b></td><td>146.61 (-0.75%)</td><td>145.39 (-0.43%)</td><td>145.05 (-0.73%)</td><td>144.32 (+0.65%)</td><td>1.03 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119815.00 (n/a)</td><td>117670.22 (n/a)</td><td>117574.50 (n/a)</td><td>116304.40 (n/a)</td><td>1385.89 (n/a)</td><td>147.71 (n/a)</td><td>146.02 (n/a)</td><td>146.12 (n/a)</td><td>143.39 (n/a)</td><td>1.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.90 (+0.21%)</td><td>0.89 (+0.12%)</td><td>0.88 (-0.56%)</td><td>0.88 (+0.53%)</td><td>0.01 (-17.52%)</td><td>28508.30 (-0.53%)</td><td>28359.82 (-0.12%)</td><td>28464.80 (+0.56%)</td><td>28079.40 (-0.21%)</td><td>182.46 (-18.19%)</td><td>611.83 (+0.21%)</td><td>605.80 (+0.12%)</td><td>603.55 (-0.56%)</td><td>602.63 (+0.53%)</td><td>3.91 (-17.52%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28660.20 (n/a)</td><td>28394.78 (n/a)</td><td>28306.80 (n/a)</td><td>28137.80 (n/a)</td><td>223.02 (n/a)</td><td>610.56 (n/a)</td><td>605.07 (n/a)</td><td>606.92 (n/a)</td><td>599.43 (n/a)</td><td>4.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.55 (+0.87%)</td><td>3.52 (+1.48%)</td><td>3.53 (+0.54%)</td><td>3.49 (+5.14%)</td><td>0.02 <b>(-75.42%)</b></td><td>7203.80 (-4.89%)</td><td>7140.12 (-1.50%)</td><td>7134.20 (-0.53%)</td><td>7085.80 (-0.86%)</td><td>42.25 <b>(-76.87%)</b></td><td>2424.54 (+0.87%)</td><td>2406.17 (+1.48%)</td><td>2408.08 (+0.54%)</td><td>2384.82 (+5.14%)</td><td>14.21 <b>(-75.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.52 (n/a)</td><td>3.47 (n/a)</td><td>3.51 (n/a)</td><td>3.32 (n/a)</td><td>0.08 (n/a)</td><td>7574.20 (n/a)</td><td>7248.82 (n/a)</td><td>7172.50 (n/a)</td><td>7147.30 (n/a)</td><td>182.66 (n/a)</td><td>2403.69 (n/a)</td><td>2371.19 (n/a)</td><td>2395.23 (n/a)</td><td>2268.22 (n/a)</td><td>57.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>2.85 (-8.78%)</td><td>2.80 (-3.22%)</td><td>2.82 (-2.02%)</td><td>2.71 (-0.36%)</td><td>0.06 <b>(-61.42%)</b></td><td>9302.30 (+0.36%)</td><td>8985.84 (+3.14%)</td><td>8923.40 (+2.07%)</td><td>8821.10 (+9.62%)</td><td>194.51 <b>(-57.33%)</b></td><td>1947.58 (-8.78%)</td><td>1912.58 (-3.22%)</td><td>1925.25 (-2.02%)</td><td>1846.84 (-0.36%)</td><td>40.67 <b>(-61.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.13 (n/a)</td><td>2.89 (n/a)</td><td>2.88 (n/a)</td><td>2.72 (n/a)</td><td>0.15 (n/a)</td><td>9268.90 (n/a)</td><td>8712.56 (n/a)</td><td>8742.70 (n/a)</td><td>8046.90 (n/a)</td><td>455.87 (n/a)</td><td>2134.97 (n/a)</td><td>1976.26 (n/a)</td><td>1965.05 (n/a)</td><td>1853.50 (n/a)</td><td>105.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.45 (+3.34%)</td><td>3.29 (+1.06%)</td><td>3.26 (+0.18%)</td><td>3.21 (+0.64%)</td><td>0.10 <b>(+50.52%)</b></td><td>7841.10 (-0.64%)</td><td>7648.06 (-1.01%)</td><td>7709.60 (-0.18%)</td><td>7288.40 (-3.24%)</td><td>225.73 <b>(+44.34%)</b></td><td>2357.17 (+3.34%)</td><td>2247.91 (+1.06%)</td><td>2228.37 (+0.18%)</td><td>2190.99 (+0.64%)</td><td>67.90 <b>(+50.52%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.34 (n/a)</td><td>3.26 (n/a)</td><td>3.26 (n/a)</td><td>3.19 (n/a)</td><td>0.07 (n/a)</td><td>7891.30 (n/a)</td><td>7726.24 (n/a)</td><td>7723.70 (n/a)</td><td>7532.10 (n/a)</td><td>156.39 (n/a)</td><td>2280.88 (n/a)</td><td>2224.31 (n/a)</td><td>2224.32 (n/a)</td><td>2177.05 (n/a)</td><td>45.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 (-0.05%)</td><td>0.78 (+0.01%)</td><td>0.78 (-0.01%)</td><td>0.78 (+0.11%)</td><td>0.00 <b>(-90.48%)</b></td><td>96452.20 (-0.11%)</td><td>96445.02 (-0.01%)</td><td>96447.10 (+0.01%)</td><td>96438.90 (+0.05%)</td><td>5.76 <b>(-90.47%)</b></td><td>712.57 (-0.05%)</td><td>712.52 (+0.01%)</td><td>712.51 (-0.01%)</td><td>712.47 (+0.11%)</td><td>0.04 <b>(-90.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96555.70 (n/a)</td><td>96456.16 (n/a)</td><td>96441.30 (n/a)</td><td>96392.20 (n/a)</td><td>60.46 (n/a)</td><td>712.92 (n/a)</td><td>712.44 (n/a)</td><td>712.55 (n/a)</td><td>711.71 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.73 (-0.02%)</td><td>0.73 (+0.09%)</td><td>0.73 (+0.11%)</td><td>0.73 (+0.20%)</td><td>0.00 <b>(-72.35%)</b></td><td>103702.10 (-0.19%)</td><td>103653.74 (-0.09%)</td><td>103638.20 (-0.11%)</td><td>103630.50 (+0.02%)</td><td>30.89 <b>(-72.41%)</b></td><td>663.12 (-0.02%)</td><td>662.97 (+0.09%)</td><td>663.07 (+0.11%)</td><td>662.66 (+0.20%)</td><td>0.20 <b>(-72.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103904.40 (n/a)</td><td>103744.98 (n/a)</td><td>103756.00 (n/a)</td><td>103614.40 (n/a)</td><td>111.96 (n/a)</td><td>663.22 (n/a)</td><td>662.39 (n/a)</td><td>662.32 (n/a)</td><td>661.37 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.70 (-0.23%)</td><td>0.69 (-0.18%)</td><td>0.69 (-0.13%)</td><td>0.69 (-0.16%)</td><td>0.00 (-6.83%)</td><td>109089.50 (+0.16%)</td><td>108784.50 (+0.18%)</td><td>108722.90 (+0.13%)</td><td>108575.80 (+0.23%)</td><td>204.72 (-6.47%)</td><td>632.92 (-0.23%)</td><td>631.70 (-0.18%)</td><td>632.06 (-0.13%)</td><td>629.94 (-0.16%)</td><td>1.19 (-6.83%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108910.50 (n/a)</td><td>108587.94 (n/a)</td><td>108581.30 (n/a)</td><td>108322.10 (n/a)</td><td>218.89 (n/a)</td><td>634.40 (n/a)</td><td>632.85 (n/a)</td><td>632.88 (n/a)</td><td>630.97 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.47 (-1.29%)</td><td>7.02 (+2.82%)</td><td>6.96 (-3.51%)</td><td>6.74 <b>(+35.58%)</b></td><td>0.30 <b>(-71.31%)</b></td><td>1323.30 <b>(-26.25%)</b></td><td>1271.80 (-4.92%)</td><td>1281.10 (+3.65%)</td><td>1192.50 (+1.32%)</td><td>53.82 <b>(-79.10%)</b></td><td>450.22 (-1.29%)</td><td>422.76 (+2.82%)</td><td>419.08 (-3.51%)</td><td>405.70 <b>(+35.58%)</b></td><td>18.28 <b>(-71.31%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.57 (n/a)</td><td>6.83 (n/a)</td><td>7.21 (n/a)</td><td>4.97 (n/a)</td><td>1.06 (n/a)</td><td>1794.20 (n/a)</td><td>1337.56 (n/a)</td><td>1236.00 (n/a)</td><td>1177.00 (n/a)</td><td>257.47 (n/a)</td><td>456.12 (n/a)</td><td>411.17 (n/a)</td><td>434.34 (n/a)</td><td>299.23 (n/a)</td><td>63.74 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.78 (-4.53%)</td><td>6.30 (+5.21%)</td><td>6.61 (+2.28%)</td><td>4.79 (+2.94%)</td><td>0.85 <b>(-29.89%)</b></td><td>1859.80 (-2.86%)</td><td>1440.84 (-6.61%)</td><td>1347.80 (-2.23%)</td><td>1314.70 (+4.75%)</td><td>235.19 <b>(-29.00%)</b></td><td>408.36 (-4.53%)</td><td>379.28 (+5.21%)</td><td>398.33 (+2.28%)</td><td>288.67 (+2.94%)</td><td>51.06 <b>(-29.89%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.10 (n/a)</td><td>5.98 (n/a)</td><td>6.47 (n/a)</td><td>4.66 (n/a)</td><td>1.21 (n/a)</td><td>1914.50 (n/a)</td><td>1542.78 (n/a)</td><td>1378.60 (n/a)</td><td>1255.10 (n/a)</td><td>331.26 (n/a)</td><td>427.75 (n/a)</td><td>360.48 (n/a)</td><td>389.43 (n/a)</td><td>280.43 (n/a)</td><td>72.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.82 (-2.95%)</td><td>6.42 (+12.38%)</td><td>6.32 (+5.50%)</td><td>6.14 <b>(+35.42%)</b></td><td>0.31 <b>(-71.38%)</b></td><td>1452.60 <b>(-26.16%)</b></td><td>1391.76 (-13.41%)</td><td>1409.80 (-5.21%)</td><td>1306.20 (+3.04%)</td><td>65.50 <b>(-78.77%)</b></td><td>411.01 (-2.95%)</td><td>386.44 (+12.38%)</td><td>380.80 (+5.50%)</td><td>369.59 <b>(+35.42%)</b></td><td>18.46 <b>(-71.38%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.03 (n/a)</td><td>5.71 (n/a)</td><td>5.99 (n/a)</td><td>4.53 (n/a)</td><td>1.07 (n/a)</td><td>1967.20 (n/a)</td><td>1607.26 (n/a)</td><td>1487.30 (n/a)</td><td>1267.70 (n/a)</td><td>308.47 (n/a)</td><td>423.51 (n/a)</td><td>343.88 (n/a)</td><td>360.96 (n/a)</td><td>272.91 (n/a)</td><td>64.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.39 (+2.06%)</td><td>7.78 (-1.05%)</td><td>8.02 (+0.43%)</td><td>7.06 (+0.87%)</td><td>0.54 (+8.18%)</td><td>4941.50 (-0.87%)</td><td>4499.26 (+1.11%)</td><td>4349.70 (-0.43%)</td><td>4157.10 (-2.02%)</td><td>322.31 (+4.87%)</td><td>516.59 (+2.06%)</td><td>479.22 (-1.05%)</td><td>493.71 (+0.43%)</td><td>434.58 (+0.87%)</td><td>33.54 (+8.18%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.22 (n/a)</td><td>7.86 (n/a)</td><td>7.98 (n/a)</td><td>6.99 (n/a)</td><td>0.50 (n/a)</td><td>4984.70 (n/a)</td><td>4450.08 (n/a)</td><td>4368.40 (n/a)</td><td>4242.70 (n/a)</td><td>307.35 (n/a)</td><td>506.16 (n/a)</td><td>484.28 (n/a)</td><td>491.60 (n/a)</td><td>430.82 (n/a)</td><td>31.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.77 (-1.98%)</td><td>7.49 (+1.43%)</td><td>7.55 (+5.80%)</td><td>7.12 (+2.27%)</td><td>0.25 <b>(-45.19%)</b></td><td>4895.50 (-2.22%)</td><td>4659.76 (-1.62%)</td><td>4620.20 (-5.48%)</td><td>4487.90 (+2.02%)</td><td>159.80 <b>(-44.97%)</b></td><td>478.51 (-1.98%)</td><td>461.29 (+1.43%)</td><td>464.80 (+5.80%)</td><td>438.67 (+2.27%)</td><td>15.59 <b>(-45.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.93 (n/a)</td><td>7.38 (n/a)</td><td>7.13 (n/a)</td><td>6.96 (n/a)</td><td>0.46 (n/a)</td><td>5006.70 (n/a)</td><td>4736.38 (n/a)</td><td>4888.30 (n/a)</td><td>4398.90 (n/a)</td><td>290.36 (n/a)</td><td>488.19 (n/a)</td><td>454.80 (n/a)</td><td>439.31 (n/a)</td><td>428.92 (n/a)</td><td>28.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>7.40 (-0.30%)</td><td>7.19 (+0.45%)</td><td>7.31 (+1.77%)</td><td>6.81 (-1.38%)</td><td>0.25 (+9.21%)</td><td>5119.10 (+1.40%)</td><td>4856.04 (-0.43%)</td><td>4771.30 (-1.73%)</td><td>4711.80 (+0.30%)</td><td>170.72 (+10.67%)</td><td>455.77 (-0.30%)</td><td>442.66 (+0.45%)</td><td>450.08 (+1.77%)</td><td>419.50 (-1.38%)</td><td>15.21 (+9.21%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>7.42 (n/a)</td><td>7.15 (n/a)</td><td>7.18 (n/a)</td><td>6.91 (n/a)</td><td>0.23 (n/a)</td><td>5048.60 (n/a)</td><td>4877.04 (n/a)</td><td>4855.50 (n/a)</td><td>4697.50 (n/a)</td><td>154.26 (n/a)</td><td>457.16 (n/a)</td><td>440.68 (n/a)</td><td>442.27 (n/a)</td><td>425.36 (n/a)</td><td>13.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.79 (-0.04%)</td><td>0.79 (-0.04%)</td><td>0.79 (-0.12%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(-27.15%)</b></td><td>95913.00 (+0.02%)</td><td>95808.18 (+0.04%)</td><td>95826.00 (+0.12%)</td><td>95730.70 (+0.04%)</td><td>74.47 <b>(-27.09%)</b></td><td>717.84 (-0.04%)</td><td>717.26 (-0.04%)</td><td>717.13 (-0.12%)</td><td>716.48 (-0.02%)</td><td>0.56 <b>(-27.16%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95894.70 (n/a)</td><td>95773.68 (n/a)</td><td>95708.40 (n/a)</td><td>95693.60 (n/a)</td><td>102.14 (n/a)</td><td>718.12 (n/a)</td><td>717.52 (n/a)</td><td>718.01 (n/a)</td><td>716.61 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.73 (-0.01%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.02%)</td><td>0.73 (+0.07%)</td><td>0.00 <b>(-47.29%)</b></td><td>103008.10 (-0.07%)</td><td>102937.40 (-0.00%)</td><td>102932.80 (+0.02%)</td><td>102893.70 (+0.01%)</td><td>42.66 <b>(-47.37%)</b></td><td>667.87 (-0.01%)</td><td>667.59 (+0.00%)</td><td>667.61 (-0.02%)</td><td>667.13 (+0.07%)</td><td>0.28 <b>(-47.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103082.20 (n/a)</td><td>102940.22 (n/a)</td><td>102911.00 (n/a)</td><td>102878.60 (n/a)</td><td>81.05 (n/a)</td><td>667.97 (n/a)</td><td>667.57 (n/a)</td><td>667.76 (n/a)</td><td>666.65 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.70 (+0.12%)</td><td>0.70 (+0.04%)</td><td>0.70 (+0.06%)</td><td>0.70 (-0.17%)</td><td>0.00 <b>(+97.13%)</b></td><td>108174.70 (+0.17%)</td><td>107823.26 (-0.04%)</td><td>107809.90 (-0.06%)</td><td>107539.10 (-0.12%)</td><td>241.71 <b>(+97.30%)</b></td><td>639.02 (+0.12%)</td><td>637.34 (+0.04%)</td><td>637.41 (+0.06%)</td><td>635.26 (-0.17%)</td><td>1.43 <b>(+97.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107992.60 (n/a)</td><td>107866.86 (n/a)</td><td>107878.00 (n/a)</td><td>107664.40 (n/a)</td><td>122.51 (n/a)</td><td>638.27 (n/a)</td><td>637.08 (n/a)</td><td>637.01 (n/a)</td><td>636.34 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>4.23 (-2.69%)</td><td>3.60 (-8.55%)</td><td>3.71 (-4.82%)</td><td>2.96 (-17.15%)</td><td>0.60 <b>(+110.28%)</b></td><td>2727.00 <b>(+20.70%)</b></td><td>2293.30 (+11.46%)</td><td>2175.20 (+5.07%)</td><td>1906.20 (+2.76%)</td><td>394.98 <b>(+165.76%)</b></td><td>1108.97 (-2.69%)</td><td>943.50 (-8.55%)</td><td>971.85 (-4.82%)</td><td>775.18 (-17.15%)</td><td>158.03 <b>(+110.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>4.35 (n/a)</td><td>3.93 (n/a)</td><td>3.89 (n/a)</td><td>3.57 (n/a)</td><td>0.29 (n/a)</td><td>2259.40 (n/a)</td><td>2057.52 (n/a)</td><td>2070.30 (n/a)</td><td>1855.00 (n/a)</td><td>148.62 (n/a)</td><td>1139.60 (n/a)</td><td>1031.74 (n/a)</td><td>1021.05 (n/a)</td><td>935.63 (n/a)</td><td>75.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.50 <b>(+44.67%)</b></td><td>0.39 <b>(+25.13%)</b></td><td>0.36 (+9.91%)</td><td>0.32 (+12.88%)</td><td>0.08 <b>(+185.93%)</b></td><td>3866.10 (-11.41%)</td><td>3256.36 (-18.10%)</td><td>3502.00 (-9.02%)</td><td>2503.70 <b>(-30.88%)</b></td><td>616.82 <b>(+72.25%)</b></td><td>26.80 <b>(+44.67%)</b></td><td>21.26 <b>(+25.13%)</b></td><td>19.16 (+9.91%)</td><td>17.36 (+12.88%)</td><td>4.29 <b>(+185.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4364.10 (n/a)</td><td>3975.80 (n/a)</td><td>3849.30 (n/a)</td><td>3622.20 (n/a)</td><td>358.09 (n/a)</td><td>18.53 (n/a)</td><td>16.99 (n/a)</td><td>17.43 (n/a)</td><td>15.38 (n/a)</td><td>1.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.37 (+5.29%)</td><td>4.92 (-0.81%)</td><td>4.87 (-3.80%)</td><td>3.38 (+4.33%)</td><td>1.40 <b>(+22.57%)</b></td><td>1966.60 (-4.15%)</td><td>1445.90 (+2.53%)</td><td>1365.00 (+3.94%)</td><td>1043.70 (-5.01%)</td><td>421.86 (+8.90%)</td><td>1969.24 (+5.29%)</td><td>1521.22 (-0.81%)</td><td>1505.65 (-3.80%)</td><td>1045.04 (+4.33%)</td><td>431.95 <b>(+22.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.05 (n/a)</td><td>4.96 (n/a)</td><td>5.07 (n/a)</td><td>3.24 (n/a)</td><td>1.14 (n/a)</td><td>2051.70 (n/a)</td><td>1410.16 (n/a)</td><td>1313.20 (n/a)</td><td>1098.80 (n/a)</td><td>387.38 (n/a)</td><td>1870.35 (n/a)</td><td>1533.62 (n/a)</td><td>1565.09 (n/a)</td><td>1001.69 (n/a)</td><td>352.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (-10.53%)</td><td>0.19 (-11.82%)</td><td>0.18 <b>(-20.15%)</b></td><td>0.14 (-19.01%)</td><td>0.03 (+1.44%)</td><td>0.22 (-10.53%)</td><td>0.18 (-11.82%)</td><td>0.18 <b>(-20.15%)</b></td><td>0.14 (-19.01%)</td><td>0.03 (+1.44%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.45 (+0.07%)</td><td>12.62 (-0.30%)</td><td>12.36 (-6.96%)</td><td>12.10 (+5.23%)</td><td>0.57 <b>(-42.10%)</b></td><td>13.44 (+0.07%)</td><td>12.61 (-0.30%)</td><td>12.35 (-6.96%)</td><td>12.09 (+5.23%)</td><td>0.57 <b>(-42.10%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.44 (n/a)</td><td>12.66 (n/a)</td><td>13.28 (n/a)</td><td>11.50 (n/a)</td><td>0.99 (n/a)</td><td>13.43 (n/a)</td><td>12.65 (n/a)</td><td>13.27 (n/a)</td><td>11.49 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>25.42 (+2.62%)</td><td>24.36 (+1.00%)</td><td>24.73 (+2.20%)</td><td>22.66 (-3.04%)</td><td>1.08 <b>(+100.45%)</b></td><td>25.40 (+2.62%)</td><td>24.34 (+1.00%)</td><td>24.72 (+2.20%)</td><td>22.65 (-3.04%)</td><td>1.08 <b>(+100.45%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>24.77 (n/a)</td><td>24.12 (n/a)</td><td>24.20 (n/a)</td><td>23.37 (n/a)</td><td>0.54 (n/a)</td><td>24.76 (n/a)</td><td>24.10 (n/a)</td><td>24.19 (n/a)</td><td>23.36 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>43.46 (+5.29%)</td><td>40.83 (+2.24%)</td><td>40.68 (+1.45%)</td><td>36.80 (-3.34%)</td><td>2.66 <b>(+119.58%)</b></td><td>43.43 (+5.29%)</td><td>40.80 (+2.24%)</td><td>40.65 (+1.45%)</td><td>36.77 (-3.34%)</td><td>2.66 <b>(+119.58%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>41.28 (n/a)</td><td>39.93 (n/a)</td><td>40.09 (n/a)</td><td>38.07 (n/a)</td><td>1.21 (n/a)</td><td>41.25 (n/a)</td><td>39.90 (n/a)</td><td>40.07 (n/a)</td><td>38.05 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>45.41 (-0.65%)</td><td>43.77 (+0.58%)</td><td>45.24 (+4.06%)</td><td>41.00 (+0.98%)</td><td>2.17 (-0.83%)</td><td>45.38 (-0.65%)</td><td>43.74 (+0.58%)</td><td>45.21 (+4.06%)</td><td>40.97 (+0.98%)</td><td>2.17 (-0.83%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>45.71 (n/a)</td><td>43.52 (n/a)</td><td>43.47 (n/a)</td><td>40.60 (n/a)</td><td>2.19 (n/a)</td><td>45.68 (n/a)</td><td>43.49 (n/a)</td><td>43.45 (n/a)</td><td>40.58 (n/a)</td><td>2.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.31 (-1.59%)</td><td>12.68 (+3.52%)</td><td>13.08 (-2.55%)</td><td>11.13 <b>(+21.16%)</b></td><td>0.91 <b>(-51.75%)</b></td><td>13.31 (-1.59%)</td><td>12.67 (+3.52%)</td><td>13.07 (-2.55%)</td><td>11.13 <b>(+21.16%)</b></td><td>0.91 <b>(-51.75%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.53 (n/a)</td><td>12.25 (n/a)</td><td>13.42 (n/a)</td><td>9.19 (n/a)</td><td>1.89 (n/a)</td><td>13.52 (n/a)</td><td>12.24 (n/a)</td><td>13.41 (n/a)</td><td>9.18 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>25.11 (-0.18%)</td><td>24.51 (-0.39%)</td><td>24.21 (-0.87%)</td><td>24.02 (+0.38%)</td><td>0.53 (+0.56%)</td><td>25.10 (-0.18%)</td><td>24.50 (-0.39%)</td><td>24.20 (-0.87%)</td><td>24.00 (+0.38%)</td><td>0.53 (+0.56%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>25.16 (n/a)</td><td>24.61 (n/a)</td><td>24.42 (n/a)</td><td>23.92 (n/a)</td><td>0.52 (n/a)</td><td>25.14 (n/a)</td><td>24.59 (n/a)</td><td>24.41 (n/a)</td><td>23.91 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>42.26 (-1.42%)</td><td>39.32 (-1.02%)</td><td>40.30 (+2.76%)</td><td>34.93 (-8.71%)</td><td>2.78 <b>(+46.87%)</b></td><td>42.24 (-1.42%)</td><td>39.29 (-1.02%)</td><td>40.28 (+2.76%)</td><td>34.91 (-8.71%)</td><td>2.78 <b>(+46.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>42.87 (n/a)</td><td>39.72 (n/a)</td><td>39.22 (n/a)</td><td>38.27 (n/a)</td><td>1.89 (n/a)</td><td>42.85 (n/a)</td><td>39.70 (n/a)</td><td>39.20 (n/a)</td><td>38.24 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>45.22 (-4.17%)</td><td>43.51 (-1.71%)</td><td>44.64 (+2.43%)</td><td>39.51 (-6.16%)</td><td>2.42 <b>(+22.59%)</b></td><td>45.20 (-4.17%)</td><td>43.49 (-1.71%)</td><td>44.61 (+2.43%)</td><td>39.48 (-6.16%)</td><td>2.42 <b>(+22.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>47.19 (n/a)</td><td>44.27 (n/a)</td><td>43.58 (n/a)</td><td>42.10 (n/a)</td><td>1.97 (n/a)</td><td>47.16 (n/a)</td><td>44.24 (n/a)</td><td>43.55 (n/a)</td><td>42.07 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.69 (+3.78%)</td><td>9.01 (+0.54%)</td><td>9.18 (+1.42%)</td><td>7.99 (-4.78%)</td><td>0.68 <b>(+85.53%)</b></td><td>9.67 (+3.78%)</td><td>8.99 (+0.54%)</td><td>9.16 (+1.42%)</td><td>7.98 (-4.78%)</td><td>0.68 <b>(+85.53%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.34 (n/a)</td><td>8.96 (n/a)</td><td>9.05 (n/a)</td><td>8.39 (n/a)</td><td>0.37 (n/a)</td><td>9.32 (n/a)</td><td>8.95 (n/a)</td><td>9.03 (n/a)</td><td>8.38 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.94 (+6.37%)</td><td>0.78 (-0.74%)</td><td>0.72 (-3.46%)</td><td>0.68 (-3.69%)</td><td>0.11 <b>(+40.56%)</b></td><td>0.93 (+6.37%)</td><td>0.76 (-0.74%)</td><td>0.71 (-3.46%)</td><td>0.67 (-3.69%)</td><td>0.11 <b>(+40.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.89 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.71 (n/a)</td><td>0.08 (n/a)</td><td>0.87 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.70 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.38 <b>(+23.68%)</b></td><td>1.19 (+16.68%)</td><td>1.18 (+10.29%)</td><td>1.03 (+13.54%)</td><td>0.14 <b>(+40.06%)</b></td><td>1.37 <b>(+23.68%)</b></td><td>1.18 (+16.68%)</td><td>1.17 (+10.29%)</td><td>1.02 (+13.54%)</td><td>0.14 <b>(+40.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.12 (n/a)</td><td>1.02 (n/a)</td><td>1.07 (n/a)</td><td>0.91 (n/a)</td><td>0.10 (n/a)</td><td>1.11 (n/a)</td><td>1.01 (n/a)</td><td>1.06 (n/a)</td><td>0.90 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>17.79 (+7.80%)</td><td>16.20 (+7.62%)</td><td>16.39 (+11.76%)</td><td>14.44 (+5.89%)</td><td>1.34 (+12.46%)</td><td>17.58 (+7.80%)</td><td>16.01 (+7.62%)</td><td>16.20 (+11.76%)</td><td>14.27 (+5.89%)</td><td>1.32 (+12.46%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>16.50 (n/a)</td><td>15.05 (n/a)</td><td>14.66 (n/a)</td><td>13.63 (n/a)</td><td>1.19 (n/a)</td><td>16.31 (n/a)</td><td>14.88 (n/a)</td><td>14.49 (n/a)</td><td>13.47 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.45 (+4.81%)</td><td>11.87 (+2.83%)</td><td>11.88 (+0.63%)</td><td>11.15 (+6.33%)</td><td>0.47 <b>(-21.27%)</b></td><td>12.23 (+4.81%)</td><td>11.66 (+2.83%)</td><td>11.67 (+0.63%)</td><td>10.96 (+6.33%)</td><td>0.46 <b>(-21.27%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>11.88 (n/a)</td><td>11.54 (n/a)</td><td>11.80 (n/a)</td><td>10.49 (n/a)</td><td>0.59 (n/a)</td><td>11.67 (n/a)</td><td>11.34 (n/a)</td><td>11.60 (n/a)</td><td>10.30 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.46 (+4.36%)</td><td>7.67 (+1.77%)</td><td>7.85 (+1.86%)</td><td>6.76 (+1.92%)</td><td>0.70 <b>(+21.56%)</b></td><td>8.31 (+4.36%)</td><td>7.54 (+1.77%)</td><td>7.71 (+1.86%)</td><td>6.65 (+1.92%)</td><td>0.69 <b>(+21.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.10 (n/a)</td><td>7.54 (n/a)</td><td>7.70 (n/a)</td><td>6.64 (n/a)</td><td>0.57 (n/a)</td><td>7.96 (n/a)</td><td>7.41 (n/a)</td><td>7.57 (n/a)</td><td>6.52 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>6.40 (+8.35%)</td><td>5.86 (+12.51%)</td><td>5.69 (+13.92%)</td><td>5.58 (+19.55%)</td><td>0.35 <b>(-30.32%)</b></td><td>6.29 (+8.35%)</td><td>5.76 (+12.51%)</td><td>5.59 (+13.92%)</td><td>5.49 (+19.55%)</td><td>0.34 <b>(-30.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.90 (n/a)</td><td>5.20 (n/a)</td><td>4.99 (n/a)</td><td>4.67 (n/a)</td><td>0.50 (n/a)</td><td>5.81 (n/a)</td><td>5.12 (n/a)</td><td>4.91 (n/a)</td><td>4.59 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>161.76 (n/a)</td><td>164.10 (n/a)</td><td>116.60 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>155.70 (n/a)</td><td>151.60 (n/a)</td><td>121.90 (n/a)</td><td>35.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>166.70 (n/a)</td><td>137.92 (n/a)</td><td>146.90 (n/a)</td><td>99.70 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.30 (n/a)</td><td>194.62 (n/a)</td><td>195.90 (n/a)</td><td>118.70 (n/a)</td><td>62.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>143.60 (n/a)</td><td>138.60 (n/a)</td><td>116.60 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>171.98 (n/a)</td><td>160.40 (n/a)</td><td>153.30 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>190.82 (n/a)</td><td>184.80 (n/a)</td><td>163.30 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>340.60 (n/a)</td><td>230.04 (n/a)</td><td>222.60 (n/a)</td><td>172.20 (n/a)</td><td>65.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>164.00 (n/a)</td><td>152.70 (n/a)</td><td>133.40 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>168.36 (n/a)</td><td>169.70 (n/a)</td><td>114.90 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>190.48 (n/a)</td><td>188.40 (n/a)</td><td>124.40 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>159.64 (n/a)</td><td>165.80 (n/a)</td><td>124.00 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.30 (n/a)</td><td>161.30 (n/a)</td><td>173.40 (n/a)</td><td>122.50 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.80 (n/a)</td><td>184.98 (n/a)</td><td>192.60 (n/a)</td><td>160.50 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.80 (n/a)</td><td>199.26 (n/a)</td><td>176.70 (n/a)</td><td>163.40 (n/a)</td><td>57.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.60 (n/a)</td><td>237.58 (n/a)</td><td>220.00 (n/a)</td><td>200.10 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.40 (n/a)</td><td>157.76 (n/a)</td><td>155.40 (n/a)</td><td>139.40 (n/a)</td><td>15.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>189.96 (n/a)</td><td>170.00 (n/a)</td><td>168.10 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>258.60 (n/a)</td><td>191.22 (n/a)</td><td>184.70 (n/a)</td><td>141.30 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.10 (n/a)</td><td>186.84 (n/a)</td><td>163.00 (n/a)</td><td>145.70 (n/a)</td><td>43.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.00 (n/a)</td><td>157.44 (n/a)</td><td>155.20 (n/a)</td><td>127.80 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>171.56 (n/a)</td><td>160.70 (n/a)</td><td>140.80 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.20 (n/a)</td><td>215.88 (n/a)</td><td>218.80 (n/a)</td><td>180.10 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.90 (n/a)</td><td>195.24 (n/a)</td><td>196.00 (n/a)</td><td>153.20 (n/a)</td><td>37.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (-11.50%)</td><td>0.16 (-0.55%)</td><td>0.17 (+12.90%)</td><td>0.14 (+12.35%)</td><td>0.02 <b>(-42.39%)</b></td><td>228.50 (-10.99%)</td><td>201.42 (-1.29%)</td><td>189.40 (-11.41%)</td><td>177.40 (+12.99%)</td><td>22.73 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>256.70 (n/a)</td><td>204.06 (n/a)</td><td>213.80 (n/a)</td><td>157.00 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>171.50 (n/a)</td><td>161.00 (n/a)</td><td>154.90 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>286.90 (n/a)</td><td>196.68 (n/a)</td><td>188.30 (n/a)</td><td>120.40 (n/a)</td><td>64.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.80 (n/a)</td><td>197.32 (n/a)</td><td>195.50 (n/a)</td><td>161.70 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.10 (n/a)</td><td>180.78 (n/a)</td><td>183.60 (n/a)</td><td>142.60 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.20 (n/a)</td><td>178.04 (n/a)</td><td>184.80 (n/a)</td><td>136.60 (n/a)</td><td>32.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.20 (n/a)</td><td>173.72 (n/a)</td><td>168.00 (n/a)</td><td>134.40 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>197.82 (n/a)</td><td>202.90 (n/a)</td><td>179.80 (n/a)</td><td>11.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+3.22%)</td><td>0.02 (-1.26%)</td><td>0.02 (+2.54%)</td><td>0.02 (+1.03%)</td><td>0.00 (+4.07%)</td><td>205.70 (-1.01%)</td><td>175.86 (+1.35%)</td><td>171.50 (-2.50%)</td><td>132.10 (-3.08%)</td><td>29.01 (-0.71%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>173.52 (n/a)</td><td>175.90 (n/a)</td><td>136.30 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (-15.39%)</td><td>0.02 (-10.70%)</td><td>0.02 (-9.84%)</td><td>0.02 (-8.88%)</td><td>0.00 <b>(-38.58%)</b></td><td>209.10 (+9.76%)</td><td>190.98 (+11.65%)</td><td>187.70 (+10.87%)</td><td>179.40 (+18.18%)</td><td>11.67 (-19.94%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>171.06 (n/a)</td><td>169.30 (n/a)</td><td>151.80 (n/a)</td><td>14.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-6.63%)</td><td>0.02 (-12.38%)</td><td>0.02 (-19.38%)</td><td>0.02 (-4.21%)</td><td>0.00 (-7.03%)</td><td>211.20 (+4.40%)</td><td>175.04 (+13.99%)</td><td>177.70 <b>(+24.01%)</b></td><td>134.80 (+7.15%)</td><td>31.04 (+2.44%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>153.56 (n/a)</td><td>143.30 (n/a)</td><td>125.80 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-14.85%)</td><td>0.03 (+4.13%)</td><td>0.03 (+8.58%)</td><td>0.02 (+4.84%)</td><td>0.00 <b>(-51.66%)</b></td><td>179.00 (-4.58%)</td><td>153.74 (-5.53%)</td><td>148.90 (-7.92%)</td><td>143.50 (+17.43%)</td><td>14.33 <b>(-44.00%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.60 (n/a)</td><td>162.74 (n/a)</td><td>161.70 (n/a)</td><td>122.20 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 <b>(+35.30%)</b></td><td>0.03 (+18.71%)</td><td>0.02 (+1.34%)</td><td>0.02 (+12.72%)</td><td>0.01 <b>(+166.88%)</b></td><td>181.00 (-11.32%)</td><td>153.08 (-13.48%)</td><td>167.70 (-1.35%)</td><td>117.40 <b>(-26.07%)</b></td><td>30.37 <b>(+72.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>176.94 (n/a)</td><td>170.00 (n/a)</td><td>158.80 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+16.16%)</td><td>0.02 (+4.55%)</td><td>0.02 (-2.68%)</td><td>0.02 <b>(+20.78%)</b></td><td>0.00 (+16.69%)</td><td>215.80 (-17.19%)</td><td>196.74 (-4.46%)</td><td>204.30 (+2.71%)</td><td>150.70 (-13.89%)</td><td>26.59 (-19.85%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>260.60 (n/a)</td><td>205.92 (n/a)</td><td>198.90 (n/a)</td><td>175.00 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 <b>(+36.83%)</b></td><td>0.02 (+1.87%)</td><td>0.02 (+2.20%)</td><td>0.01 <b>(-28.07%)</b></td><td>0.01 <b>(+249.77%)</b></td><td>299.50 <b>(+39.04%)</b></td><td>207.14 (+6.20%)</td><td>198.60 (-2.17%)</td><td>124.80 <b>(-26.93%)</b></td><td>66.04 <b>(+254.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.40 (n/a)</td><td>195.04 (n/a)</td><td>203.00 (n/a)</td><td>170.80 (n/a)</td><td>18.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+19.05%)</td><td>0.02 (-2.09%)</td><td>0.02 (+1.06%)</td><td>0.01 <b>(-31.54%)</b></td><td>0.01 <b>(+146.94%)</b></td><td>353.90 <b>(+46.06%)</b></td><td>232.28 (+8.49%)</td><td>217.30 (-1.05%)</td><td>155.70 (-16.02%)</td><td>73.59 <b>(+216.61%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>214.10 (n/a)</td><td>219.60 (n/a)</td><td>185.40 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-18.87%)</td><td>0.05 (-15.48%)</td><td>0.05 (-6.47%)</td><td>0.03 (-16.37%)</td><td>0.01 <b>(-38.30%)</b></td><td>246.50 (+19.54%)</td><td>182.36 (+15.80%)</td><td>178.70 (+6.94%)</td><td>141.50 <b>(+23.26%)</b></td><td>39.02 (-2.09%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>157.48 (n/a)</td><td>167.10 (n/a)</td><td>114.80 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (-0.75%)</td><td>0.05 (+3.69%)</td><td>0.05 (+4.57%)</td><td>0.04 (+11.42%)</td><td>0.00 <b>(-21.78%)</b></td><td>207.80 (-10.24%)</td><td>178.64 (-4.24%)</td><td>169.90 (-4.39%)</td><td>161.80 (+0.75%)</td><td>18.94 <b>(-30.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>186.54 (n/a)</td><td>177.70 (n/a)</td><td>160.60 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (-8.92%)</td><td>0.05 (-9.72%)</td><td>0.04 (-12.52%)</td><td>0.04 (-9.19%)</td><td>0.01 (+7.08%)</td><td>208.00 (+10.11%)</td><td>181.84 (+11.27%)</td><td>188.20 (+14.34%)</td><td>152.90 (+9.84%)</td><td>25.74 <b>(+28.72%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>163.42 (n/a)</td><td>164.60 (n/a)</td><td>139.20 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-17.64%)</td><td>0.05 (-8.86%)</td><td>0.04 (-14.16%)</td><td>0.04 (-8.60%)</td><td>0.01 (-8.01%)</td><td>227.30 (+9.38%)</td><td>186.06 (+10.58%)</td><td>207.10 (+16.48%)</td><td>135.20 <b>(+21.47%)</b></td><td>45.00 <b>(+26.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>168.26 (n/a)</td><td>177.80 (n/a)</td><td>111.30 (n/a)</td><td>35.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-8.01%)</td><td>0.05 (-8.72%)</td><td>0.04 (-6.77%)</td><td>0.04 (-1.06%)</td><td>0.01 <b>(-32.91%)</b></td><td>198.40 (+1.07%)</td><td>178.46 (+7.77%)</td><td>188.60 (+7.28%)</td><td>139.80 (+8.71%)</td><td>23.74 <b>(-26.78%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>165.60 (n/a)</td><td>175.80 (n/a)</td><td>128.60 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(-22.97%)</b></td><td>0.05 (-5.29%)</td><td>0.05 (+2.37%)</td><td>0.04 <b>(+20.07%)</b></td><td>0.00 <b>(-72.37%)</b></td><td>191.60 (-16.73%)</td><td>179.40 (+1.39%)</td><td>180.60 (-2.27%)</td><td>160.80 <b>(+29.78%)</b></td><td>12.19 <b>(-69.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>176.94 (n/a)</td><td>184.80 (n/a)</td><td>123.90 (n/a)</td><td>40.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+19.17%)</td><td>0.05 (+2.56%)</td><td>0.05 (-9.65%)</td><td>0.04 (+3.55%)</td><td>0.01 <b>(+45.39%)</b></td><td>204.10 (-3.41%)</td><td>173.52 (-1.60%)</td><td>180.50 (+10.67%)</td><td>133.10 (-16.08%)</td><td>27.51 (+17.87%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>176.34 (n/a)</td><td>163.10 (n/a)</td><td>158.60 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+3.32%)</td><td>0.05 (-1.10%)</td><td>0.05 (+5.78%)</td><td>0.04 (-7.64%)</td><td>0.01 (+9.24%)</td><td>222.40 (+8.28%)</td><td>182.44 (+1.51%)</td><td>172.80 (-5.47%)</td><td>147.30 (-3.22%)</td><td>28.76 (+15.60%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>179.72 (n/a)</td><td>182.80 (n/a)</td><td>152.20 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (-8.75%)</td><td>0.04 (-3.76%)</td><td>0.04 (+0.31%)</td><td>0.04 (-1.89%)</td><td>0.00 <b>(-40.18%)</b></td><td>218.40 (+1.96%)</td><td>199.28 (+3.20%)</td><td>201.50 (-0.30%)</td><td>180.80 (+9.58%)</td><td>15.02 <b>(-33.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>193.10 (n/a)</td><td>202.10 (n/a)</td><td>165.00 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (-16.76%)</td><td>0.04 (-3.58%)</td><td>0.04 (+0.76%)</td><td>0.04 (+1.83%)</td><td>0.00 <b>(-56.41%)</b></td><td>231.80 (-1.78%)</td><td>215.10 (+2.01%)</td><td>217.90 (-0.77%)</td><td>187.90 <b>(+20.14%)</b></td><td>16.33 <b>(-47.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>210.86 (n/a)</td><td>219.60 (n/a)</td><td>156.40 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-1.68%)</td><td>0.10 (-1.70%)</td><td>0.10 (+4.73%)</td><td>0.07 <b>(-28.67%)</b></td><td>0.02 <b>(+53.86%)</b></td><td>242.80 <b>(+40.18%)</b></td><td>166.22 (+5.67%)</td><td>157.60 (-4.48%)</td><td>124.40 (+1.72%)</td><td>46.57 <b>(+127.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>173.20 (n/a)</td><td>157.30 (n/a)</td><td>165.00 (n/a)</td><td>122.30 (n/a)</td><td>20.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-15.80%)</td><td>0.09 (-12.57%)</td><td>0.10 (-2.31%)</td><td>0.07 <b>(-24.60%)</b></td><td>0.02 (+6.01%)</td><td>234.30 <b>(+32.60%)</b></td><td>183.46 (+16.13%)</td><td>165.90 (+2.34%)</td><td>143.10 (+18.76%)</td><td>38.23 <b>(+75.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>157.98 (n/a)</td><td>162.10 (n/a)</td><td>120.50 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-12.85%)</td><td>0.10 (-5.83%)</td><td>0.10 (-6.09%)</td><td>0.09 (+8.71%)</td><td>0.01 <b>(-46.55%)</b></td><td>190.00 (-8.03%)</td><td>172.14 (+4.56%)</td><td>171.50 (+6.46%)</td><td>148.40 (+14.77%)</td><td>15.37 <b>(-44.55%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>164.64 (n/a)</td><td>161.10 (n/a)</td><td>129.30 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-6.00%)</td><td>0.09 (-4.37%)</td><td>0.09 (+3.07%)</td><td>0.08 (-6.97%)</td><td>0.01 (-0.75%)</td><td>218.20 (+7.49%)</td><td>188.34 (+4.69%)</td><td>182.20 (-2.98%)</td><td>164.20 (+6.35%)</td><td>22.23 (+14.93%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>179.90 (n/a)</td><td>187.80 (n/a)</td><td>154.40 (n/a)</td><td>19.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 <b>(-23.47%)</b></td><td>0.09 (-11.99%)</td><td>0.09 <b>(-23.09%)</b></td><td>0.08 (+18.61%)</td><td>0.01 <b>(-77.58%)</b></td><td>197.30 (-15.68%)</td><td>182.60 (+7.79%)</td><td>183.40 <b>(+29.98%)</b></td><td>170.60 <b>(+30.63%)</b></td><td>11.52 <b>(-75.31%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>234.00 (n/a)</td><td>169.40 (n/a)</td><td>141.10 (n/a)</td><td>130.60 (n/a)</td><td>46.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-0.25%)</td><td>0.10 (+1.59%)</td><td>0.09 (-0.21%)</td><td>0.09 <b>(+20.24%)</b></td><td>0.01 <b>(-45.34%)</b></td><td>182.10 (-16.85%)</td><td>172.70 (-2.70%)</td><td>177.40 (+0.23%)</td><td>154.20 (+0.26%)</td><td>11.72 <b>(-54.55%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>177.50 (n/a)</td><td>177.00 (n/a)</td><td>153.80 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-5.35%)</td><td>0.09 (+3.60%)</td><td>0.09 (+10.30%)</td><td>0.08 (+0.49%)</td><td>0.01 <b>(-20.73%)</b></td><td>215.00 (-0.51%)</td><td>190.18 (-3.81%)</td><td>181.40 (-9.30%)</td><td>169.20 (+5.68%)</td><td>19.04 (-14.84%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>197.72 (n/a)</td><td>200.00 (n/a)</td><td>160.10 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 (-12.39%)</td><td>0.07 (-7.87%)</td><td>0.08 (+4.65%)</td><td>0.05 <b>(-22.85%)</b></td><td>0.01 <b>(+36.27%)</b></td><td>301.70 <b>(+29.60%)</b></td><td>236.54 (+10.14%)</td><td>210.70 (-4.44%)</td><td>204.40 (+14.13%)</td><td>42.19 <b>(+103.98%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>214.76 (n/a)</td><td>220.50 (n/a)</td><td>179.10 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (+17.22%)</td><td>0.21 (+18.38%)</td><td>0.22 <b>(+24.35%)</b></td><td>0.17 (+16.78%)</td><td>0.02 <b>(+27.51%)</b></td><td>188.20 (-14.34%)</td><td>158.52 (-15.37%)</td><td>147.50 (-19.57%)</td><td>142.10 (-14.71%)</td><td>19.64 (-7.10%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.70 (n/a)</td><td>187.30 (n/a)</td><td>183.40 (n/a)</td><td>166.60 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (-6.30%)</td><td>0.20 (-13.38%)</td><td>0.19 (-16.63%)</td><td>0.15 (-12.55%)</td><td>0.05 (+7.86%)</td><td>212.40 (+14.32%)</td><td>171.72 (+16.88%)</td><td>176.10 (+19.96%)</td><td>113.40 (+6.78%)</td><td>36.60 <b>(+28.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>185.80 (n/a)</td><td>146.92 (n/a)</td><td>146.80 (n/a)</td><td>106.20 (n/a)</td><td>28.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (-19.24%)</td><td>0.17 (-14.54%)</td><td>0.16 (-6.43%)</td><td>0.15 (-12.27%)</td><td>0.03 <b>(-33.53%)</b></td><td>225.70 (+13.99%)</td><td>196.78 (+15.59%)</td><td>198.90 (+6.88%)</td><td>153.20 <b>(+23.85%)</b></td><td>30.16 (-6.18%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.00 (n/a)</td><td>170.24 (n/a)</td><td>186.10 (n/a)</td><td>123.70 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (-0.22%)</td><td>0.19 (-4.81%)</td><td>0.19 (-4.09%)</td><td>0.13 <b>(-28.63%)</b></td><td>0.04 <b>(+96.43%)</b></td><td>257.10 <b>(+40.11%)</b></td><td>179.28 (+8.60%)</td><td>169.70 (+4.24%)</td><td>143.80 (+0.28%)</td><td>44.90 <b>(+186.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.50 (n/a)</td><td>165.08 (n/a)</td><td>162.80 (n/a)</td><td>143.40 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 <b>(+30.43%)</b></td><td>0.18 <b>(+25.09%)</b></td><td>0.18 <b>(+35.61%)</b></td><td>0.15 (+13.43%)</td><td>0.02 <b>(+66.27%)</b></td><td>221.60 (-11.82%)</td><td>186.18 (-19.49%)</td><td>178.20 <b>(-26.27%)</b></td><td>153.40 <b>(-23.34%)</b></td><td>26.02 (+12.08%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>251.30 (n/a)</td><td>231.24 (n/a)</td><td>241.70 (n/a)</td><td>200.10 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (+5.54%)</td><td>0.17 (-2.11%)</td><td>0.17 (+2.11%)</td><td>0.13 (-12.68%)</td><td>0.03 <b>(+63.51%)</b></td><td>243.30 (+14.55%)</td><td>199.20 (+3.77%)</td><td>193.10 (-2.08%)</td><td>155.30 (-5.25%)</td><td>33.99 <b>(+79.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>191.96 (n/a)</td><td>197.20 (n/a)</td><td>163.90 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (+2.43%)</td><td>0.15 (+11.84%)</td><td>0.15 (+8.36%)</td><td>0.12 <b>(+21.08%)</b></td><td>0.02 <b>(-38.60%)</b></td><td>278.10 (-17.43%)</td><td>228.60 (-13.01%)</td><td>221.50 (-7.71%)</td><td>202.90 (-2.36%)</td><td>29.92 <b>(-50.08%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>336.80 (n/a)</td><td>262.80 (n/a)</td><td>240.00 (n/a)</td><td>207.80 (n/a)</td><td>59.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 <b>(+32.53%)</b></td><td>0.03 (+15.16%)</td><td>0.03 <b>(+24.55%)</b></td><td>0.02 (-11.65%)</td><td>0.01 <b>(+123.23%)</b></td><td>247.70 (+13.21%)</td><td>169.40 (-7.00%)</td><td>151.90 (-19.71%)</td><td>110.30 <b>(-24.56%)</b></td><td>57.70 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>182.16 (n/a)</td><td>189.20 (n/a)</td><td>146.20 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+19.23%)</td><td>0.03 <b>(+23.10%)</b></td><td>0.03 <b>(+43.52%)</b></td><td>0.02 (+10.97%)</td><td>0.01 (+16.85%)</td><td>186.90 (-9.88%)</td><td>139.58 (-18.67%)</td><td>131.80 <b>(-30.34%)</b></td><td>109.50 (-16.09%)</td><td>32.49 (-11.08%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>171.62 (n/a)</td><td>189.20 (n/a)</td><td>130.50 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 <b>(+20.94%)</b></td><td>0.02 (+5.64%)</td><td>0.02 (-1.97%)</td><td>0.01 (-7.21%)</td><td>0.01 <b>(+82.39%)</b></td><td>273.40 (+7.77%)</td><td>207.66 (-0.89%)</td><td>221.90 (+2.02%)</td><td>138.10 (-17.31%)</td><td>58.51 <b>(+62.75%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.70 (n/a)</td><td>209.52 (n/a)</td><td>217.50 (n/a)</td><td>167.00 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 <b>(+36.61%)</b></td><td>0.02 (+5.75%)</td><td>0.02 (-10.58%)</td><td>0.02 (-12.49%)</td><td>0.01 <b>(+292.18%)</b></td><td>255.40 (+14.27%)</td><td>200.08 (+0.36%)</td><td>217.20 (+11.84%)</td><td>133.60 <b>(-26.79%)</b></td><td>53.63 <b>(+226.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.50 (n/a)</td><td>199.36 (n/a)</td><td>194.20 (n/a)</td><td>182.50 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+11.41%)</td><td>0.03 (-0.33%)</td><td>0.02 (-7.82%)</td><td>0.02 (+7.65%)</td><td>0.01 (+19.85%)</td><td>186.20 (-7.09%)</td><td>159.52 (+0.77%)</td><td>166.90 (+8.45%)</td><td>113.90 (-10.24%)</td><td>28.32 (-2.48%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>158.30 (n/a)</td><td>153.90 (n/a)</td><td>126.90 (n/a)</td><td>29.04 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+12.32%)</td><td>0.03 (+3.06%)</td><td>0.03 (+11.87%)</td><td>0.02 (-1.88%)</td><td>0.01 <b>(+51.06%)</b></td><td>193.50 (+1.90%)</td><td>148.52 (+0.04%)</td><td>127.60 (-10.58%)</td><td>107.10 (-10.97%)</td><td>40.12 <b>(+44.36%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>148.46 (n/a)</td><td>142.70 (n/a)</td><td>120.30 (n/a)</td><td>27.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-17.54%)</td><td>0.02 <b>(-22.67%)</b></td><td>0.02 <b>(-33.50%)</b></td><td>0.02 (-17.62%)</td><td>0.00 <b>(-23.43%)</b></td><td>225.00 <b>(+21.36%)</b></td><td>198.40 <b>(+29.00%)</b></td><td>212.70 <b>(+50.32%)</b></td><td>162.80 <b>(+21.22%)</b></td><td>26.54 (+13.53%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>153.80 (n/a)</td><td>141.50 (n/a)</td><td>134.30 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-13.39%)</td><td>0.03 (-9.24%)</td><td>0.03 (-14.09%)</td><td>0.02 (-4.61%)</td><td>0.00 <b>(-21.38%)</b></td><td>198.30 (+4.81%)</td><td>159.50 (+9.10%)</td><td>155.90 (+16.43%)</td><td>131.40 (+15.47%)</td><td>29.42 (-8.17%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>146.20 (n/a)</td><td>133.90 (n/a)</td><td>113.80 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-0.11%)</td><td>0.02 (-7.26%)</td><td>0.02 (-11.07%)</td><td>0.02 (-12.29%)</td><td>0.01 <b>(+28.75%)</b></td><td>202.90 (+13.99%)</td><td>181.34 (+9.39%)</td><td>196.70 (+12.40%)</td><td>127.60 (+0.08%)</td><td>31.86 <b>(+47.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>165.78 (n/a)</td><td>175.00 (n/a)</td><td>127.50 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+4.76%)</td><td>0.03 (+6.18%)</td><td>0.02 (+3.31%)</td><td>0.02 (-12.03%)</td><td>0.01 <b>(+55.60%)</b></td><td>215.00 (+13.64%)</td><td>162.60 (-3.76%)</td><td>165.90 (-3.21%)</td><td>128.40 (-4.54%)</td><td>35.05 <b>(+69.14%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>168.96 (n/a)</td><td>171.40 (n/a)</td><td>134.50 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+5.25%)</td><td>0.02 (-1.07%)</td><td>0.02 <b>(-23.04%)</b></td><td>0.02 <b>(+38.88%)</b></td><td>0.00 <b>(-27.92%)</b></td><td>216.30 <b>(-28.02%)</b></td><td>188.24 (-3.90%)</td><td>203.00 <b>(+29.96%)</b></td><td>136.20 (-4.95%)</td><td>33.39 <b>(-50.26%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>300.50 (n/a)</td><td>195.88 (n/a)</td><td>156.20 (n/a)</td><td>143.30 (n/a)</td><td>67.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+3.58%)</td><td>0.02 (-10.08%)</td><td>0.02 (-19.54%)</td><td>0.02 <b>(-21.50%)</b></td><td>0.01 <b>(+47.54%)</b></td><td>234.90 <b>(+27.39%)</b></td><td>173.78 (+14.57%)</td><td>180.60 <b>(+24.29%)</b></td><td>120.20 (-3.45%)</td><td>42.52 <b>(+78.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>151.68 (n/a)</td><td>145.30 (n/a)</td><td>124.50 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 <b>(-22.06%)</b></td><td>0.02 (-8.94%)</td><td>0.02 (+6.20%)</td><td>0.01 <b>(-22.05%)</b></td><td>0.00 <b>(-28.75%)</b></td><td>282.00 <b>(+28.30%)</b></td><td>204.58 (+9.16%)</td><td>192.20 (-5.83%)</td><td>167.10 <b>(+28.34%)</b></td><td>45.68 (+19.00%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>187.42 (n/a)</td><td>204.10 (n/a)</td><td>130.20 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-5.13%)</td><td>0.02 (-13.10%)</td><td>0.02 (-16.80%)</td><td>0.02 (-19.99%)</td><td>0.01 (+12.63%)</td><td>237.20 <b>(+24.97%)</b></td><td>180.88 (+17.29%)</td><td>193.30 <b>(+20.14%)</b></td><td>121.40 (+5.47%)</td><td>43.29 <b>(+46.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>154.22 (n/a)</td><td>160.90 (n/a)</td><td>115.10 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+6.43%)</td><td>0.02 (+1.71%)</td><td>0.02 (-1.47%)</td><td>0.02 (-4.59%)</td><td>0.01 (+18.66%)</td><td>234.10 (+4.84%)</td><td>191.34 (+0.35%)</td><td>222.70 (+1.50%)</td><td>114.60 (-6.07%)</td><td>52.53 (+16.52%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>190.68 (n/a)</td><td>219.40 (n/a)</td><td>122.00 (n/a)</td><td>45.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-0.85%)</td><td>0.02 (-3.79%)</td><td>0.02 (-3.44%)</td><td>0.02 (+7.90%)</td><td>0.00 (-11.04%)</td><td>219.50 (-7.31%)</td><td>177.44 (+2.91%)</td><td>180.40 (+3.56%)</td><td>136.00 (+0.89%)</td><td>34.70 (-15.62%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>172.42 (n/a)</td><td>174.20 (n/a)</td><td>134.80 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (+6.94%)</td><td>0.05 (-9.29%)</td><td>0.05 (-11.31%)</td><td>0.04 (-16.77%)</td><td>0.01 <b>(+76.63%)</b></td><td>210.00 <b>(+20.21%)</b></td><td>173.06 (+13.51%)</td><td>167.70 (+12.78%)</td><td>118.40 (-6.48%)</td><td>36.34 <b>(+97.97%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>152.46 (n/a)</td><td>148.70 (n/a)</td><td>126.60 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-4.98%)</td><td>0.05 (-2.54%)</td><td>0.05 (-2.90%)</td><td>0.04 (+1.42%)</td><td>0.01 (-0.55%)</td><td>209.00 (-1.42%)</td><td>165.26 (+2.63%)</td><td>160.50 (+3.02%)</td><td>130.70 (+5.23%)</td><td>32.10 (+0.84%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>161.02 (n/a)</td><td>155.80 (n/a)</td><td>124.20 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 <b>(+47.35%)</b></td><td>0.04 <b>(+21.29%)</b></td><td>0.04 (+9.39%)</td><td>0.03 (+15.04%)</td><td>0.01 <b>(+114.30%)</b></td><td>260.30 (-13.06%)</td><td>201.06 (-15.31%)</td><td>211.80 (-8.59%)</td><td>141.40 <b>(-32.12%)</b></td><td>45.44 <b>(+23.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>299.40 (n/a)</td><td>237.42 (n/a)</td><td>231.70 (n/a)</td><td>208.30 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-14.62%)</td><td>0.04 (+0.16%)</td><td>0.04 (+7.43%)</td><td>0.03 <b>(+27.65%)</b></td><td>0.01 <b>(-34.20%)</b></td><td>238.80 <b>(-21.68%)</b></td><td>195.26 (-5.05%)</td><td>199.50 (-6.95%)</td><td>145.20 (+17.10%)</td><td>41.58 <b>(-38.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.90 (n/a)</td><td>205.64 (n/a)</td><td>214.40 (n/a)</td><td>124.00 (n/a)</td><td>67.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-16.12%)</td><td>0.05 (+2.12%)</td><td>0.06 <b>(+26.78%)</b></td><td>0.04 <b>(+29.50%)</b></td><td>0.01 <b>(-26.11%)</b></td><td>223.50 <b>(-22.77%)</b></td><td>165.70 (-6.77%)</td><td>136.70 <b>(-21.07%)</b></td><td>124.30 (+19.18%)</td><td>46.71 <b>(-32.13%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>289.40 (n/a)</td><td>177.74 (n/a)</td><td>173.20 (n/a)</td><td>104.30 (n/a)</td><td>68.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-12.68%)</td><td>0.05 (+4.13%)</td><td>0.05 <b>(+24.61%)</b></td><td>0.05 <b>(+29.78%)</b></td><td>0.01 <b>(-62.13%)</b></td><td>175.10 <b>(-22.93%)</b></td><td>159.48 (-10.13%)</td><td>161.40 (-19.74%)</td><td>131.50 (+14.55%)</td><td>16.67 <b>(-67.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>177.46 (n/a)</td><td>201.10 (n/a)</td><td>114.80 (n/a)</td><td>50.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (-0.80%)</td><td>0.04 (+10.12%)</td><td>0.05 <b>(+23.71%)</b></td><td>0.03 (+3.81%)</td><td>0.01 (-2.24%)</td><td>299.50 (-3.67%)</td><td>193.78 (-9.42%)</td><td>165.80 (-19.16%)</td><td>155.20 (+0.84%)</td><td>60.96 (-3.15%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.90 (n/a)</td><td>213.94 (n/a)</td><td>205.10 (n/a)</td><td>153.90 (n/a)</td><td>62.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (+1.71%)</td><td>0.05 (-11.44%)</td><td>0.05 (-12.75%)</td><td>0.03 <b>(-24.83%)</b></td><td>0.01 <b>(+33.01%)</b></td><td>278.10 <b>(+33.06%)</b></td><td>185.10 (+17.20%)</td><td>177.20 (+14.62%)</td><td>125.10 (-1.65%)</td><td>56.72 <b>(+77.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>157.94 (n/a)</td><td>154.60 (n/a)</td><td>127.20 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (+5.19%)</td><td>0.05 (+7.95%)</td><td>0.05 (+13.46%)</td><td>0.04 (-6.33%)</td><td>0.01 <b>(+56.20%)</b></td><td>219.30 (+6.77%)</td><td>178.30 (-6.63%)</td><td>169.20 (-11.88%)</td><td>158.50 (-4.92%)</td><td>24.08 <b>(+64.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.40 (n/a)</td><td>190.96 (n/a)</td><td>192.00 (n/a)</td><td>166.70 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-10.95%)</td><td>0.05 (-7.84%)</td><td>0.04 (-10.79%)</td><td>0.04 (+4.63%)</td><td>0.01 <b>(-26.68%)</b></td><td>194.40 (-4.42%)</td><td>165.90 (+6.26%)</td><td>184.20 (+12.11%)</td><td>124.60 (+12.35%)</td><td>31.61 (-19.09%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>156.12 (n/a)</td><td>164.30 (n/a)</td><td>110.90 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-11.64%)</td><td>0.05 (+7.74%)</td><td>0.06 <b>(+23.32%)</b></td><td>0.04 (+1.00%)</td><td>0.01 <b>(-21.06%)</b></td><td>188.70 (-1.00%)</td><td>154.68 (-8.14%)</td><td>143.40 (-18.89%)</td><td>128.50 (+13.22%)</td><td>28.84 (-9.28%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>168.38 (n/a)</td><td>176.80 (n/a)</td><td>113.50 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+8.09%)</td><td>0.05 (+3.15%)</td><td>0.05 (+9.30%)</td><td>0.04 (-18.01%)</td><td>0.01 <b>(+113.46%)</b></td><td>230.40 <b>(+21.97%)</b></td><td>174.76 (+1.27%)</td><td>160.80 (-8.53%)</td><td>130.50 (-7.45%)</td><td>45.99 <b>(+147.17%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>172.56 (n/a)</td><td>175.80 (n/a)</td><td>141.00 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-6.62%)</td><td>0.05 (-7.99%)</td><td>0.05 (-1.80%)</td><td>0.04 (-12.05%)</td><td>0.01 (+13.88%)</td><td>233.60 (+13.73%)</td><td>187.44 (+10.39%)</td><td>175.60 (+1.86%)</td><td>142.20 (+7.08%)</td><td>42.18 <b>(+44.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>169.80 (n/a)</td><td>172.40 (n/a)</td><td>132.80 (n/a)</td><td>29.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-9.39%)</td><td>0.04 (-18.31%)</td><td>0.04 <b>(-20.88%)</b></td><td>0.03 <b>(-39.51%)</b></td><td>0.01 <b>(+63.83%)</b></td><td>277.70 <b>(+65.40%)</b></td><td>196.56 <b>(+29.13%)</b></td><td>200.20 <b>(+26.39%)</b></td><td>132.60 (+10.41%)</td><td>57.00 <b>(+200.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.90 (n/a)</td><td>152.22 (n/a)</td><td>158.40 (n/a)</td><td>120.10 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 <b>(+26.34%)</b></td><td>0.05 (+9.36%)</td><td>0.04 (+1.07%)</td><td>0.04 (-1.07%)</td><td>0.01 <b>(+92.07%)</b></td><td>214.50 (+1.08%)</td><td>173.94 (-6.70%)</td><td>183.60 (-1.08%)</td><td>127.90 <b>(-20.85%)</b></td><td>32.75 <b>(+50.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>186.44 (n/a)</td><td>185.60 (n/a)</td><td>161.60 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+11.59%)</td><td>0.05 (+1.73%)</td><td>0.05 (+3.60%)</td><td>0.03 <b>(-26.18%)</b></td><td>0.01 <b>(+151.56%)</b></td><td>264.30 <b>(+35.47%)</b></td><td>180.40 (+2.14%)</td><td>164.70 (-3.46%)</td><td>146.30 (-10.36%)</td><td>47.77 <b>(+220.07%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.10 (n/a)</td><td>176.62 (n/a)</td><td>170.60 (n/a)</td><td>163.20 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 <b>(+23.41%)</b></td><td>0.10 (+16.68%)</td><td>0.11 <b>(+27.00%)</b></td><td>0.08 (+0.02%)</td><td>0.02 <b>(+111.36%)</b></td><td>210.60 (+0.00%)</td><td>164.72 (-12.83%)</td><td>149.30 <b>(-21.26%)</b></td><td>138.60 (-18.99%)</td><td>29.58 <b>(+74.15%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>188.96 (n/a)</td><td>189.60 (n/a)</td><td>171.10 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (+0.05%)</td><td>0.11 (+7.61%)</td><td>0.11 (+2.53%)</td><td>0.08 <b>(+29.38%)</b></td><td>0.02 <b>(-27.74%)</b></td><td>206.20 <b>(-22.71%)</b></td><td>154.16 (-10.46%)</td><td>146.30 (-2.47%)</td><td>128.50 (+0.00%)</td><td>30.10 <b>(-44.96%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>266.80 (n/a)</td><td>172.16 (n/a)</td><td>150.00 (n/a)</td><td>128.50 (n/a)</td><td>54.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (+9.79%)</td><td>0.08 (-7.38%)</td><td>0.07 (-14.69%)</td><td>0.05 <b>(-32.85%)</b></td><td>0.02 <b>(+101.96%)</b></td><td>352.30 <b>(+48.90%)</b></td><td>228.56 (+14.97%)</td><td>227.60 (+17.20%)</td><td>154.00 (-8.88%)</td><td>76.02 <b>(+179.29%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>198.80 (n/a)</td><td>194.20 (n/a)</td><td>169.00 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (+8.51%)</td><td>0.09 (-4.39%)</td><td>0.09 (-5.66%)</td><td>0.05 <b>(-34.27%)</b></td><td>0.02 <b>(+113.83%)</b></td><td>340.80 <b>(+52.14%)</b></td><td>207.70 (+11.94%)</td><td>186.60 (+6.02%)</td><td>152.90 (-7.84%)</td><td>76.29 <b>(+215.27%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>185.54 (n/a)</td><td>176.00 (n/a)</td><td>165.90 (n/a)</td><td>24.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (+18.37%)</td><td>0.10 (-3.31%)</td><td>0.09 (-9.69%)</td><td>0.07 (-13.37%)</td><td>0.03 <b>(+116.00%)</b></td><td>223.50 (+15.44%)</td><td>173.52 (+8.46%)</td><td>178.10 (+10.69%)</td><td>116.60 (-15.51%)</td><td>45.90 <b>(+112.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.60 (n/a)</td><td>159.98 (n/a)</td><td>160.90 (n/a)</td><td>138.00 (n/a)</td><td>21.62 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 <b>(+56.15%)</b></td><td>0.11 <b>(+28.36%)</b></td><td>0.12 <b>(+35.82%)</b></td><td>0.04 <b>(-36.64%)</b></td><td>0.04 <b>(+329.73%)</b></td><td>386.20 <b>(+57.83%)</b></td><td>187.48 (-6.10%)</td><td>141.60 <b>(-26.37%)</b></td><td>113.90 <b>(-35.98%)</b></td><td>113.98 <b>(+334.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>244.70 (n/a)</td><td>199.66 (n/a)</td><td>192.30 (n/a)</td><td>177.90 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-7.24%)</td><td>0.09 (-3.50%)</td><td>0.10 (+6.21%)</td><td>0.07 (-11.16%)</td><td>0.02 (+10.72%)</td><td>240.70 (+12.58%)</td><td>181.12 (+4.50%)</td><td>164.30 (-5.85%)</td><td>158.00 (+7.85%)</td><td>34.92 <b>(+34.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>173.32 (n/a)</td><td>174.50 (n/a)</td><td>146.50 (n/a)</td><td>26.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 <b>(+38.21%)</b></td><td>0.12 <b>(+21.63%)</b></td><td>0.13 <b>(+36.68%)</b></td><td>0.08 (-8.57%)</td><td>0.03 <b>(+219.65%)</b></td><td>210.20 (+9.37%)</td><td>151.74 (-12.46%)</td><td>126.00 <b>(-26.83%)</b></td><td>107.90 <b>(-27.63%)</b></td><td>46.75 <b>(+156.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>173.34 (n/a)</td><td>172.20 (n/a)</td><td>149.10 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-4.46%)</td><td>0.10 (+3.96%)</td><td>0.10 (+16.97%)</td><td>0.07 <b>(+28.60%)</b></td><td>0.03 (-15.81%)</td><td>242.70 <b>(-22.26%)</b></td><td>182.38 (-7.34%)</td><td>164.80 (-14.52%)</td><td>122.20 (+4.71%)</td><td>49.71 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>312.20 (n/a)</td><td>196.82 (n/a)</td><td>192.80 (n/a)</td><td>116.70 (n/a)</td><td>71.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (+14.96%)</td><td>0.11 (+4.00%)</td><td>0.11 (+0.91%)</td><td>0.08 (+2.00%)</td><td>0.02 <b>(+26.54%)</b></td><td>213.00 (-1.98%)</td><td>160.44 (-3.06%)</td><td>150.40 (-0.86%)</td><td>127.60 (-12.96%)</td><td>32.57 (+9.30%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>165.50 (n/a)</td><td>151.70 (n/a)</td><td>146.60 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (-15.75%)</td><td>0.10 (-12.97%)</td><td>0.11 (-12.33%)</td><td>0.07 (+18.53%)</td><td>0.02 <b>(-31.31%)</b></td><td>219.40 (-15.65%)</td><td>172.84 (+9.81%)</td><td>154.60 (+14.10%)</td><td>135.20 (+18.70%)</td><td>41.52 <b>(-30.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>260.10 (n/a)</td><td>157.40 (n/a)</td><td>135.50 (n/a)</td><td>113.90 (n/a)</td><td>60.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (-10.81%)</td><td>0.10 (-3.61%)</td><td>0.10 (-4.30%)</td><td>0.09 (+11.25%)</td><td>0.01 <b>(-46.72%)</b></td><td>190.80 (-10.13%)</td><td>162.40 (+0.17%)</td><td>156.40 (+4.48%)</td><td>138.40 (+12.06%)</td><td>22.12 <b>(-45.80%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>212.30 (n/a)</td><td>162.12 (n/a)</td><td>149.70 (n/a)</td><td>123.50 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-8.17%)</td><td>0.09 (+0.83%)</td><td>0.09 (+4.22%)</td><td>0.07 (-0.60%)</td><td>0.01 <b>(-24.51%)</b></td><td>222.70 (+0.63%)</td><td>185.50 (-1.43%)</td><td>179.60 (-4.06%)</td><td>160.70 (+8.88%)</td><td>23.09 (-13.78%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>188.20 (n/a)</td><td>187.20 (n/a)</td><td>147.60 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (+7.01%)</td><td>0.09 (-6.61%)</td><td>0.08 (-7.64%)</td><td>0.08 (-8.97%)</td><td>0.02 <b>(+40.14%)</b></td><td>217.80 (+9.83%)</td><td>187.72 (+8.68%)</td><td>197.50 (+8.28%)</td><td>131.50 (-6.54%)</td><td>33.00 <b>(+38.47%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>172.72 (n/a)</td><td>182.40 (n/a)</td><td>140.70 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (+15.25%)</td><td>0.09 (+7.30%)</td><td>0.09 (+12.97%)</td><td>0.06 (-9.81%)</td><td>0.03 <b>(+54.72%)</b></td><td>256.90 (+10.88%)</td><td>187.64 (-3.59%)</td><td>176.50 (-11.48%)</td><td>129.10 (-13.18%)</td><td>51.84 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.70 (n/a)</td><td>194.62 (n/a)</td><td>199.40 (n/a)</td><td>148.70 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (+4.50%)</td><td>0.09 (-2.35%)</td><td>0.10 (-3.24%)</td><td>0.07 (-8.46%)</td><td>0.02 <b>(+22.93%)</b></td><td>220.60 (+9.26%)</td><td>179.38 (+3.34%)</td><td>168.60 (+3.37%)</td><td>145.60 (-4.34%)</td><td>31.76 <b>(+29.61%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>173.58 (n/a)</td><td>163.10 (n/a)</td><td>152.20 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+6.83%)</td><td>0.20 (-4.56%)</td><td>0.18 (-17.85%)</td><td>0.15 (-0.10%)</td><td>0.05 <b>(+28.74%)</b></td><td>213.80 (+0.09%)</td><td>169.66 (+6.58%)</td><td>180.60 <b>(+21.78%)</b></td><td>113.30 (-6.44%)</td><td>40.11 (+16.87%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.60 (n/a)</td><td>159.18 (n/a)</td><td>148.30 (n/a)</td><td>121.10 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (-2.54%)</td><td>0.19 (-10.37%)</td><td>0.19 (-9.38%)</td><td>0.15 (-17.07%)</td><td>0.04 (-3.52%)</td><td>225.70 <b>(+20.57%)</b></td><td>176.36 (+11.93%)</td><td>175.40 (+10.31%)</td><td>130.50 (+2.59%)</td><td>34.30 (+18.57%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>187.20 (n/a)</td><td>157.56 (n/a)</td><td>159.00 (n/a)</td><td>127.20 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.18 (-8.82%)</td><td>0.15 (-12.70%)</td><td>0.15 (-18.97%)</td><td>0.13 (-6.51%)</td><td>0.02 (-10.02%)</td><td>253.30 (+6.97%)</td><td>219.94 (+14.42%)</td><td>223.50 <b>(+23.41%)</b></td><td>179.20 (+9.74%)</td><td>28.76 (+2.94%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>236.80 (n/a)</td><td>192.22 (n/a)</td><td>181.10 (n/a)</td><td>163.30 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 <b>(+24.92%)</b></td><td>0.17 (-5.07%)</td><td>0.15 (-14.65%)</td><td>0.14 (-14.88%)</td><td>0.04 <b>(+242.85%)</b></td><td>237.00 (+17.50%)</td><td>200.40 (+9.01%)</td><td>211.60 (+17.17%)</td><td>135.20 (-19.95%)</td><td>38.51 <b>(+205.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>183.84 (n/a)</td><td>180.60 (n/a)</td><td>168.90 (n/a)</td><td>12.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (+2.23%)</td><td>0.21 (+4.84%)</td><td>0.23 (+8.90%)</td><td>0.15 (+7.33%)</td><td>0.05 (-12.35%)</td><td>225.40 (-6.82%)</td><td>161.02 (-6.48%)</td><td>144.10 (-8.16%)</td><td>121.70 (-2.17%)</td><td>43.23 (-18.09%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>241.90 (n/a)</td><td>172.18 (n/a)</td><td>156.90 (n/a)</td><td>124.40 (n/a)</td><td>52.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+10.43%)</td><td>0.21 (-2.29%)</td><td>0.20 (+2.15%)</td><td>0.14 <b>(-24.15%)</b></td><td>0.06 <b>(+65.88%)</b></td><td>230.60 <b>(+31.85%)</b></td><td>166.22 (+6.20%)</td><td>161.40 (-2.12%)</td><td>111.10 (-9.45%)</td><td>43.06 <b>(+95.32%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>174.90 (n/a)</td><td>156.52 (n/a)</td><td>164.90 (n/a)</td><td>122.70 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (-16.73%)</td><td>0.19 (-7.14%)</td><td>0.18 (-7.93%)</td><td>0.16 (+1.01%)</td><td>0.03 <b>(-40.01%)</b></td><td>199.80 (-0.99%)</td><td>174.08 (+5.71%)</td><td>183.80 (+8.63%)</td><td>150.50 <b>(+20.11%)</b></td><td>22.39 <b>(-30.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.80 (n/a)</td><td>164.68 (n/a)</td><td>169.20 (n/a)</td><td>125.30 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (+13.03%)</td><td>0.22 (+18.22%)</td><td>0.22 (+14.46%)</td><td>0.19 <b>(+21.03%)</b></td><td>0.03 (+0.30%)</td><td>173.90 (-17.39%)</td><td>150.14 (-15.94%)</td><td>150.70 (-12.64%)</td><td>129.10 (-11.51%)</td><td>20.42 <b>(-29.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>178.60 (n/a)</td><td>172.50 (n/a)</td><td>145.90 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+11.07%)</td><td>0.20 (-15.03%)</td><td>0.17 <b>(-32.99%)</b></td><td>0.16 (-5.90%)</td><td>0.05 <b>(+44.58%)</b></td><td>198.60 (+6.26%)</td><td>169.56 <b>(+20.37%)</b></td><td>190.10 <b>(+49.22%)</b></td><td>112.40 (-9.94%)</td><td>36.52 <b>(+37.97%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.90 (n/a)</td><td>140.86 (n/a)</td><td>127.40 (n/a)</td><td>124.80 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+16.04%)</td><td>0.22 (+8.65%)</td><td>0.21 (+0.79%)</td><td>0.19 (+16.51%)</td><td>0.04 (+12.88%)</td><td>176.50 (-14.15%)</td><td>150.78 (-8.14%)</td><td>155.00 (-0.77%)</td><td>111.20 (-13.80%)</td><td>26.30 (-17.57%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.60 (n/a)</td><td>164.14 (n/a)</td><td>156.20 (n/a)</td><td>129.00 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (-9.64%)</td><td>0.19 (-13.06%)</td><td>0.20 (-8.74%)</td><td>0.13 <b>(-25.86%)</b></td><td>0.04 <b>(+43.71%)</b></td><td>251.60 <b>(+34.83%)</b></td><td>183.40 (+18.38%)</td><td>160.10 (+9.58%)</td><td>147.00 (+10.69%)</td><td>45.24 <b>(+109.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.60 (n/a)</td><td>154.92 (n/a)</td><td>146.10 (n/a)</td><td>132.80 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (-14.03%)</td><td>0.19 (-13.86%)</td><td>0.18 (-15.91%)</td><td>0.15 (-7.22%)</td><td>0.03 <b>(-33.05%)</b></td><td>213.30 (+7.78%)</td><td>176.40 (+14.46%)</td><td>178.10 (+18.89%)</td><td>140.90 (+16.35%)</td><td>26.36 (-16.16%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.90 (n/a)</td><td>154.12 (n/a)</td><td>149.80 (n/a)</td><td>121.10 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (-8.27%)</td><td>0.16 (-14.41%)</td><td>0.16 <b>(-22.81%)</b></td><td>0.13 (-12.74%)</td><td>0.03 (+8.80%)</td><td>244.90 (+14.60%)</td><td>205.86 (+17.80%)</td><td>205.50 <b>(+29.57%)</b></td><td>167.40 (+9.06%)</td><td>35.88 <b>(+36.85%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.70 (n/a)</td><td>174.76 (n/a)</td><td>158.60 (n/a)</td><td>153.50 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (+6.00%)</td><td>0.19 (-0.86%)</td><td>0.19 (-3.60%)</td><td>0.14 (-7.06%)</td><td>0.05 <b>(+66.80%)</b></td><td>236.40 (+7.60%)</td><td>180.80 (+4.28%)</td><td>174.00 (+3.76%)</td><td>134.00 (-5.70%)</td><td>46.48 <b>(+63.85%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.70 (n/a)</td><td>173.38 (n/a)</td><td>167.70 (n/a)</td><td>142.10 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (-2.09%)</td><td>0.18 (-13.64%)</td><td>0.15 <b>(-24.76%)</b></td><td>0.15 <b>(-21.25%)</b></td><td>0.04 <b>(+117.06%)</b></td><td>222.50 <b>(+27.00%)</b></td><td>187.78 (+19.65%)</td><td>211.40 <b>(+32.87%)</b></td><td>143.40 (+2.14%)</td><td>39.76 <b>(+179.17%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.20 (n/a)</td><td>156.94 (n/a)</td><td>159.10 (n/a)</td><td>140.40 (n/a)</td><td>14.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (+11.12%)</td><td>0.18 (-4.30%)</td><td>0.16 (-16.94%)</td><td>0.14 (-15.60%)</td><td>0.04 <b>(+123.20%)</b></td><td>230.20 (+18.48%)</td><td>187.04 (+7.78%)</td><td>206.70 <b>(+20.38%)</b></td><td>139.40 (-10.01%)</td><td>39.39 <b>(+133.80%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.30 (n/a)</td><td>173.54 (n/a)</td><td>171.70 (n/a)</td><td>154.90 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (+0.03%)</td><td>0.21 (+0.05%)</td><td>0.21 (+0.06%)</td><td>0.20 (-0.06%)</td><td>0.00 (+19.81%)</td><td>40927.60 (+0.07%)</td><td>40824.24 (-0.05%)</td><td>40820.60 (-0.06%)</td><td>40747.70 (-0.03%)</td><td>65.53 (+19.87%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40901.00 (n/a)</td><td>40844.96 (n/a)</td><td>40845.20 (n/a)</td><td>40759.80 (n/a)</td><td>54.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (+0.50%)</td><td>0.21 (+0.13%)</td><td>0.21 (+0.08%)</td><td>0.20 (-0.04%)</td><td>0.00 <b>(+171.34%)</b></td><td>40938.90 (+0.04%)</td><td>40809.64 (-0.13%)</td><td>40829.70 (-0.08%)</td><td>40569.00 (-0.49%)</td><td>152.42 <b>(+170.18%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40921.00 (n/a)</td><td>40861.42 (n/a)</td><td>40863.20 (n/a)</td><td>40770.30 (n/a)</td><td>56.42 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-0.05%)</td><td>0.13 (-0.01%)</td><td>0.13 (-0.01%)</td><td>0.13 (+0.02%)</td><td>0.00 <b>(-58.32%)</b></td><td>321768.20 (-0.02%)</td><td>321722.80 (+0.01%)</td><td>321747.00 (+0.01%)</td><td>321620.10 (+0.05%)</td><td>60.20 <b>(-58.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321820.90 (n/a)</td><td>321682.98 (n/a)</td><td>321705.70 (n/a)</td><td>321453.30 (n/a)</td><td>144.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 <b>(+30.40%)</b></td><td>0.03 <b>(+28.16%)</b></td><td>0.03 <b>(+41.44%)</b></td><td>0.02 (+9.42%)</td><td>0.01 <b>(+129.78%)</b></td><td>179.20 (-8.62%)</td><td>136.94 (-19.52%)</td><td>118.40 <b>(-29.31%)</b></td><td>109.20 <b>(-23.31%)</b></td><td>32.69 <b>(+61.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.10 (n/a)</td><td>170.16 (n/a)</td><td>167.50 (n/a)</td><td>142.40 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (+16.11%)</td><td>0.04 (+12.59%)</td><td>0.05 (+8.60%)</td><td>0.04 <b>(+27.85%)</b></td><td>0.01 (-1.40%)</td><td>166.50 <b>(-21.79%)</b></td><td>141.54 (-12.09%)</td><td>130.70 (-7.89%)</td><td>113.60 (-13.87%)</td><td>23.78 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>161.00 (n/a)</td><td>141.90 (n/a)</td><td>131.90 (n/a)</td><td>34.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 <b>(+25.18%)</b></td><td>0.03 <b>(+26.67%)</b></td><td>0.03 <b>(+37.15%)</b></td><td>0.02 (+0.86%)</td><td>0.01 <b>(+76.82%)</b></td><td>208.00 (-0.86%)</td><td>143.14 (-18.44%)</td><td>124.70 <b>(-27.12%)</b></td><td>109.20 <b>(-20.12%)</b></td><td>40.72 <b>(+39.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>175.50 (n/a)</td><td>171.10 (n/a)</td><td>136.70 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+12.71%)</td><td>0.03 (+14.44%)</td><td>0.03 (+17.86%)</td><td>0.03 (+3.37%)</td><td>0.01 (+17.34%)</td><td>195.40 (-3.22%)</td><td>159.86 (-12.34%)</td><td>163.60 (-15.15%)</td><td>123.60 (-11.27%)</td><td>25.87 (+0.41%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>182.36 (n/a)</td><td>192.80 (n/a)</td><td>139.30 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+14.54%)</td><td>0.03 (+10.15%)</td><td>0.03 (+6.61%)</td><td>0.02 (+12.37%)</td><td>0.00 (+19.67%)</td><td>166.20 (-11.03%)</td><td>148.02 (-9.13%)</td><td>148.00 (-6.21%)</td><td>122.60 (-12.68%)</td><td>16.20 (-9.22%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.80 (n/a)</td><td>162.90 (n/a)</td><td>157.80 (n/a)</td><td>140.40 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-5.88%)</td><td>0.03 (+0.39%)</td><td>0.03 (+0.84%)</td><td>0.02 (+10.92%)</td><td>0.00 <b>(-33.65%)</b></td><td>213.40 (-9.88%)</td><td>185.52 (-2.14%)</td><td>181.10 (-0.82%)</td><td>154.70 (+6.25%)</td><td>23.52 <b>(-36.61%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.80 (n/a)</td><td>189.58 (n/a)</td><td>182.60 (n/a)</td><td>145.60 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+5.91%)</td><td>0.02 (-5.73%)</td><td>0.02 (-14.43%)</td><td>0.02 (-15.31%)</td><td>0.01 (+6.21%)</td><td>268.60 (+18.07%)</td><td>180.24 (+7.50%)</td><td>168.40 (+16.86%)</td><td>127.30 (-5.63%)</td><td>52.76 <b>(+26.64%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>167.66 (n/a)</td><td>144.10 (n/a)</td><td>134.90 (n/a)</td><td>41.67 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+5.50%)</td><td>0.03 (+15.96%)</td><td>0.03 <b>(+27.04%)</b></td><td>0.02 (+5.91%)</td><td>0.00 (+0.73%)</td><td>213.20 (-5.58%)</td><td>170.54 (-13.87%)</td><td>166.50 <b>(-21.31%)</b></td><td>152.70 (-5.16%)</td><td>24.75 (-8.51%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.80 (n/a)</td><td>198.00 (n/a)</td><td>211.60 (n/a)</td><td>161.00 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+3.20%)</td><td>0.02 (-9.04%)</td><td>0.02 (-5.41%)</td><td>0.01 <b>(-47.80%)</b></td><td>0.01 <b>(+85.30%)</b></td><td>388.40 <b>(+91.61%)</b></td><td>204.24 <b>(+23.74%)</b></td><td>165.30 (+5.69%)</td><td>133.70 (-3.12%)</td><td>104.37 <b>(+274.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.70 (n/a)</td><td>165.06 (n/a)</td><td>156.40 (n/a)</td><td>138.00 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.04 (+15.23%)</td><td>0.03 (+0.44%)</td><td>0.02 (-5.98%)</td><td>0.02 (-5.34%)</td><td>0.01 <b>(+62.08%)</b></td><td>219.10 (+5.64%)</td><td>183.66 (+2.20%)</td><td>195.80 (+6.36%)</td><td>119.00 (-13.27%)</td><td>38.61 <b>(+46.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.40 (n/a)</td><td>179.70 (n/a)</td><td>184.10 (n/a)</td><td>137.20 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (+0.03%)</td><td>0.02 (-0.70%)</td><td>0.02 (-1.88%)</td><td>0.02 (+8.81%)</td><td>0.00 (-18.02%)</td><td>206.00 (-8.12%)</td><td>188.52 (+0.17%)</td><td>193.70 (+1.95%)</td><td>158.40 (+0.00%)</td><td>18.56 <b>(-25.71%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.20 (n/a)</td><td>188.20 (n/a)</td><td>190.00 (n/a)</td><td>158.40 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (-3.95%)</td><td>0.02 (-6.78%)</td><td>0.02 (+0.58%)</td><td>0.02 (-11.18%)</td><td>0.00 <b>(+32.39%)</b></td><td>230.30 (+12.62%)</td><td>203.50 (+7.92%)</td><td>194.40 (-0.61%)</td><td>178.50 (+4.14%)</td><td>24.49 <b>(+60.17%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>188.56 (n/a)</td><td>195.60 (n/a)</td><td>171.40 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.03 (-10.25%)</td><td>0.02 (-1.71%)</td><td>0.03 (+14.00%)</td><td>0.02 (-0.71%)</td><td>0.00 (-18.37%)</td><td>206.50 (+0.73%)</td><td>174.82 (+1.11%)</td><td>158.10 (-12.31%)</td><td>150.40 (+11.49%)</td><td>28.87 (-7.02%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>172.90 (n/a)</td><td>180.30 (n/a)</td><td>134.90 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (-0.21%)</td><td>0.02 (+0.56%)</td><td>0.02 (+4.47%)</td><td>0.02 (+2.43%)</td><td>0.00 (+7.34%)</td><td>229.30 (-2.38%)</td><td>200.08 (-0.38%)</td><td>189.80 (-4.29%)</td><td>174.70 (+0.17%)</td><td>27.18 (+7.54%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>200.84 (n/a)</td><td>198.30 (n/a)</td><td>174.40 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.02 (-9.76%)</td><td>0.02 (-19.96%)</td><td>0.02 (-18.55%)</td><td>0.01 <b>(-28.37%)</b></td><td>0.00 <b>(+56.67%)</b></td><td>331.50 <b>(+39.58%)</b></td><td>265.60 <b>(+27.82%)</b></td><td>253.00 <b>(+22.82%)</b></td><td>200.40 (+10.84%)</td><td>51.64 <b>(+143.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.50 (n/a)</td><td>207.80 (n/a)</td><td>206.00 (n/a)</td><td>180.80 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 <b>(+21.20%)</b></td><td>0.05 (+14.45%)</td><td>0.05 (+4.13%)</td><td>0.04 (+18.56%)</td><td>0.01 <b>(+62.64%)</b></td><td>184.80 (-15.62%)</td><td>159.10 (-11.78%)</td><td>167.80 (-3.95%)</td><td>129.70 (-17.49%)</td><td>25.66 (+9.74%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>180.34 (n/a)</td><td>174.70 (n/a)</td><td>157.20 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (+8.54%)</td><td>0.08 (+3.30%)</td><td>0.07 (+1.18%)</td><td>0.06 (-2.54%)</td><td>0.02 (+19.80%)</td><td>195.80 (+2.62%)</td><td>161.00 (-2.38%)</td><td>169.40 (-1.11%)</td><td>110.80 (-7.82%)</td><td>31.49 (+8.40%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>164.92 (n/a)</td><td>171.30 (n/a)</td><td>120.20 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+19.52%)</td><td>0.05 (+12.21%)</td><td>0.05 (+11.93%)</td><td>0.04 (+0.72%)</td><td>0.01 <b>(+85.54%)</b></td><td>200.10 (-0.69%)</td><td>164.48 (-9.73%)</td><td>165.50 (-10.69%)</td><td>131.10 (-16.28%)</td><td>25.51 <b>(+55.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>182.20 (n/a)</td><td>185.30 (n/a)</td><td>156.60 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (-11.73%)</td><td>0.06 (-6.52%)</td><td>0.06 (-2.98%)</td><td>0.05 (-1.17%)</td><td>0.01 <b>(-32.64%)</b></td><td>215.90 (+1.22%)</td><td>170.10 (+5.06%)</td><td>169.10 (+3.05%)</td><td>137.80 (+13.23%)</td><td>28.74 <b>(-20.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>161.90 (n/a)</td><td>164.10 (n/a)</td><td>121.70 (n/a)</td><td>36.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 <b>(+20.45%)</b></td><td>0.05 (+4.77%)</td><td>0.05 (+10.80%)</td><td>0.03 (-17.58%)</td><td>0.01 <b>(+133.79%)</b></td><td>265.00 <b>(+21.34%)</b></td><td>182.30 (-0.28%)</td><td>161.20 (-9.74%)</td><td>133.00 (-17.03%)</td><td>50.84 <b>(+137.43%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>182.82 (n/a)</td><td>178.60 (n/a)</td><td>160.30 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 (+13.59%)</td><td>0.06 (+4.82%)</td><td>0.06 (-0.41%)</td><td>0.04 (-9.43%)</td><td>0.01 <b>(+102.12%)</b></td><td>244.10 (+10.40%)</td><td>182.22 (-2.31%)</td><td>182.00 (+0.39%)</td><td>147.90 (-11.96%)</td><td>38.54 <b>(+90.44%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>186.52 (n/a)</td><td>181.30 (n/a)</td><td>168.00 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (+3.87%)</td><td>0.05 (+1.07%)</td><td>0.04 (-3.85%)</td><td>0.04 <b>(+72.72%)</b></td><td>0.01 <b>(-29.62%)</b></td><td>218.90 <b>(-42.11%)</b></td><td>185.84 (-9.68%)</td><td>182.30 (+4.05%)</td><td>131.40 (-3.74%)</td><td>36.01 <b>(-63.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>378.10 (n/a)</td><td>205.76 (n/a)</td><td>175.20 (n/a)</td><td>136.50 (n/a)</td><td>98.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 <b>(+41.46%)</b></td><td>0.06 <b>(+21.48%)</b></td><td>0.05 (+11.80%)</td><td>0.04 (-10.93%)</td><td>0.01 <b>(+357.08%)</b></td><td>243.80 (+12.30%)</td><td>172.20 (-13.23%)</td><td>177.00 (-10.56%)</td><td>126.90 <b>(-29.30%)</b></td><td>47.12 <b>(+253.54%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>198.46 (n/a)</td><td>197.90 (n/a)</td><td>179.50 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-2.06%)</td><td>0.05 (-0.02%)</td><td>0.05 (-10.94%)</td><td>0.05 <b>(+20.16%)</b></td><td>0.01 <b>(-41.91%)</b></td><td>180.50 (-16.78%)</td><td>164.30 (-3.22%)</td><td>171.80 (+12.29%)</td><td>131.80 (+2.09%)</td><td>19.26 <b>(-53.10%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>169.76 (n/a)</td><td>153.00 (n/a)</td><td>129.10 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.07 <b>(+32.26%)</b></td><td>0.06 <b>(+24.97%)</b></td><td>0.05 <b>(+26.15%)</b></td><td>0.04 (-3.29%)</td><td>0.01 <b>(+130.94%)</b></td><td>248.50 (+3.37%)</td><td>173.06 (-17.23%)</td><td>168.20 <b>(-20.74%)</b></td><td>135.50 <b>(-24.39%)</b></td><td>44.67 <b>(+85.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>209.08 (n/a)</td><td>212.20 (n/a)</td><td>179.20 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 <b>(+21.31%)</b></td><td>0.05 (+14.29%)</td><td>0.05 (+12.61%)</td><td>0.04 (+18.84%)</td><td>0.01 (+16.49%)</td><td>202.30 (-15.85%)</td><td>177.02 (-12.64%)</td><td>179.70 (-11.22%)</td><td>138.10 (-17.55%)</td><td>23.87 <b>(-21.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>202.64 (n/a)</td><td>202.40 (n/a)</td><td>167.50 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.08 <b>(+30.71%)</b></td><td>0.05 (+15.88%)</td><td>0.05 (+13.43%)</td><td>0.04 (+0.59%)</td><td>0.01 <b>(+89.89%)</b></td><td>207.30 (-0.58%)</td><td>166.94 (-11.15%)</td><td>170.20 (-11.86%)</td><td>109.90 <b>(-23.52%)</b></td><td>36.71 <b>(+43.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>187.90 (n/a)</td><td>193.10 (n/a)</td><td>143.70 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.06 (-5.10%)</td><td>0.04 (-8.63%)</td><td>0.04 (-2.00%)</td><td>0.03 (-4.50%)</td><td>0.01 <b>(-23.31%)</b></td><td>252.00 (+4.69%)</td><td>191.70 (+7.93%)</td><td>186.70 (+2.08%)</td><td>144.80 (+5.39%)</td><td>38.52 (-10.31%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>177.62 (n/a)</td><td>182.90 (n/a)</td><td>137.40 (n/a)</td><td>42.95 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 (-17.81%)</td><td>0.05 (-9.09%)</td><td>0.05 (+3.86%)</td><td>0.04 (-13.23%)</td><td>0.01 <b>(-25.85%)</b></td><td>232.00 (+15.25%)</td><td>196.88 (+9.48%)</td><td>184.90 (-3.70%)</td><td>159.30 <b>(+21.70%)</b></td><td>31.36 (+8.63%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>179.84 (n/a)</td><td>192.00 (n/a)</td><td>130.90 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.05 <b>(+24.07%)</b></td><td>0.04 (+11.47%)</td><td>0.04 (+6.17%)</td><td>0.03 <b>(+35.51%)</b></td><td>0.01 (+9.56%)</td><td>238.90 <b>(-26.22%)</b></td><td>205.60 (-11.13%)</td><td>204.60 (-5.80%)</td><td>159.30 (-19.38%)</td><td>34.18 <b>(-34.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>323.80 (n/a)</td><td>231.36 (n/a)</td><td>217.20 (n/a)</td><td>197.60 (n/a)</td><td>52.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 <b>(+26.34%)</b></td><td>0.08 (-11.23%)</td><td>0.08 (-15.94%)</td><td>0.04 <b>(-45.44%)</b></td><td>0.03 <b>(+214.53%)</b></td><td>397.50 <b>(+83.26%)</b></td><td>229.68 <b>(+26.92%)</b></td><td>201.20 (+18.98%)</td><td>132.60 <b>(-20.84%)</b></td><td>100.78 <b>(+377.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>180.96 (n/a)</td><td>169.10 (n/a)</td><td>167.50 (n/a)</td><td>21.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 <b>(+31.28%)</b></td><td>0.16 (+15.46%)</td><td>0.16 (+9.49%)</td><td>0.11 (+11.09%)</td><td>0.04 <b>(+79.30%)</b></td><td>221.90 (-9.98%)</td><td>164.86 (-10.73%)</td><td>156.70 (-8.68%)</td><td>116.00 <b>(-23.78%)</b></td><td>44.01 (+19.99%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>246.50 (n/a)</td><td>184.68 (n/a)</td><td>171.60 (n/a)</td><td>152.20 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-9.03%)</td><td>0.10 (-1.71%)</td><td>0.10 (-1.40%)</td><td>0.09 (+4.58%)</td><td>0.01 <b>(-25.69%)</b></td><td>189.40 (-4.39%)</td><td>170.38 (+1.16%)</td><td>170.70 (+1.43%)</td><td>150.60 (+9.93%)</td><td>17.34 <b>(-20.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>168.42 (n/a)</td><td>168.30 (n/a)</td><td>137.00 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 <b>(+22.21%)</b></td><td>0.14 (+13.39%)</td><td>0.14 (+11.71%)</td><td>0.11 <b>(+29.60%)</b></td><td>0.02 (+1.88%)</td><td>190.90 <b>(-22.84%)</b></td><td>153.62 (-12.93%)</td><td>146.90 (-10.48%)</td><td>119.80 (-18.23%)</td><td>26.13 <b>(-36.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>247.40 (n/a)</td><td>176.44 (n/a)</td><td>164.10 (n/a)</td><td>146.50 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-7.17%)</td><td>0.09 (-12.75%)</td><td>0.09 (-15.52%)</td><td>0.07 (-14.32%)</td><td>0.01 (-0.79%)</td><td>224.40 (+16.69%)</td><td>188.62 (+14.91%)</td><td>187.60 (+18.36%)</td><td>154.10 (+7.76%)</td><td>25.16 <b>(+23.62%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>164.14 (n/a)</td><td>158.50 (n/a)</td><td>143.00 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 <b>(+33.29%)</b></td><td>0.13 (+16.58%)</td><td>0.12 (+6.40%)</td><td>0.11 (+12.18%)</td><td>0.03 <b>(+114.69%)</b></td><td>185.80 (-10.84%)</td><td>162.84 (-12.56%)</td><td>172.60 (-5.99%)</td><td>118.40 <b>(-24.97%)</b></td><td>28.19 <b>(+44.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>186.22 (n/a)</td><td>183.60 (n/a)</td><td>157.80 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-13.51%)</td><td>0.09 (-6.71%)</td><td>0.08 (-13.05%)</td><td>0.08 <b>(+42.84%)</b></td><td>0.01 <b>(-64.09%)</b></td><td>202.20 <b>(-29.99%)</b></td><td>189.12 (+1.47%)</td><td>197.40 (+15.03%)</td><td>163.00 (+15.68%)</td><td>16.08 <b>(-72.66%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>288.80 (n/a)</td><td>186.38 (n/a)</td><td>171.60 (n/a)</td><td>140.90 (n/a)</td><td>58.80 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (+12.38%)</td><td>0.12 (+17.05%)</td><td>0.12 <b>(+30.72%)</b></td><td>0.09 (-1.67%)</td><td>0.02 (+17.92%)</td><td>213.30 (+1.72%)</td><td>159.00 (-13.98%)</td><td>154.70 <b>(-23.49%)</b></td><td>121.40 (-11.00%)</td><td>34.53 (+6.39%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>209.70 (n/a)</td><td>184.84 (n/a)</td><td>202.20 (n/a)</td><td>136.40 (n/a)</td><td>32.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 <b>(+24.08%)</b></td><td>0.11 (+3.26%)</td><td>0.09 (-9.22%)</td><td>0.08 (+6.53%)</td><td>0.03 <b>(+54.82%)</b></td><td>200.50 (-6.13%)</td><td>161.34 (-0.49%)</td><td>175.00 (+10.13%)</td><td>105.80 (-19.42%)</td><td>40.79 <b>(+20.87%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>162.14 (n/a)</td><td>158.90 (n/a)</td><td>131.30 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 <b>(+23.22%)</b></td><td>0.12 (+11.94%)</td><td>0.12 (+8.22%)</td><td>0.09 <b>(+45.83%)</b></td><td>0.03 (+9.08%)</td><td>206.50 <b>(-31.42%)</b></td><td>166.74 (-12.73%)</td><td>157.80 (-7.61%)</td><td>117.00 (-18.81%)</td><td>36.46 <b>(-41.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>301.10 (n/a)</td><td>191.06 (n/a)</td><td>170.80 (n/a)</td><td>144.10 (n/a)</td><td>62.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.10 (-19.34%)</td><td>0.09 (+3.69%)</td><td>0.09 (-4.96%)</td><td>0.08 <b>(+56.15%)</b></td><td>0.01 <b>(-58.95%)</b></td><td>217.20 <b>(-35.95%)</b></td><td>184.50 (-11.96%)</td><td>190.30 (+5.20%)</td><td>158.90 <b>(+23.95%)</b></td><td>24.93 <b>(-69.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>339.10 (n/a)</td><td>209.56 (n/a)</td><td>180.90 (n/a)</td><td>128.20 (n/a)</td><td>80.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (+17.71%)</td><td>0.09 (+1.60%)</td><td>0.09 (+0.87%)</td><td>0.05 <b>(-29.25%)</b></td><td>0.03 <b>(+139.23%)</b></td><td>320.10 <b>(+41.32%)</b></td><td>199.72 (+5.29%)</td><td>190.10 (-0.89%)</td><td>143.30 (-15.06%)</td><td>70.72 <b>(+198.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>189.68 (n/a)</td><td>191.80 (n/a)</td><td>168.70 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 <b>(+22.30%)</b></td><td>0.09 (+6.19%)</td><td>0.10 (+7.45%)</td><td>0.06 <b>(-23.85%)</b></td><td>0.02 <b>(+334.92%)</b></td><td>263.00 <b>(+31.30%)</b></td><td>184.08 (-2.11%)</td><td>171.10 (-6.96%)</td><td>146.70 (-18.23%)</td><td>45.96 <b>(+385.95%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>188.04 (n/a)</td><td>183.90 (n/a)</td><td>179.40 (n/a)</td><td>9.46 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 <b>(+23.92%)</b></td><td>0.09 (+3.16%)</td><td>0.09 (+0.51%)</td><td>0.06 (-2.42%)</td><td>0.03 <b>(+48.80%)</b></td><td>296.80 (+2.49%)</td><td>206.20 (+0.13%)</td><td>193.50 (-0.46%)</td><td>133.80 (-19.30%)</td><td>62.77 <b>(+24.08%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>289.60 (n/a)</td><td>205.94 (n/a)</td><td>194.40 (n/a)</td><td>165.80 (n/a)</td><td>50.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.09 (-4.75%)</td><td>0.08 (+5.35%)</td><td>0.08 (-5.93%)</td><td>0.07 <b>(+51.78%)</b></td><td>0.01 <b>(-38.78%)</b></td><td>247.30 <b>(-34.11%)</b></td><td>212.18 (-10.15%)</td><td>217.70 (+6.30%)</td><td>177.50 (+4.97%)</td><td>31.92 <b>(-60.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>375.30 (n/a)</td><td>236.16 (n/a)</td><td>204.80 (n/a)</td><td>169.10 (n/a)</td><td>81.01 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (-1.39%)</td><td>0.20 (+3.61%)</td><td>0.18 (-5.24%)</td><td>0.17 (+12.62%)</td><td>0.04 (-9.69%)</td><td>198.30 (-11.20%)</td><td>167.32 (-4.46%)</td><td>181.70 (+5.52%)</td><td>133.10 (+1.37%)</td><td>29.86 <b>(-20.48%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>175.14 (n/a)</td><td>172.20 (n/a)</td><td>131.30 (n/a)</td><td>37.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 (-2.03%)</td><td>0.20 (+7.37%)</td><td>0.22 <b>(+27.25%)</b></td><td>0.14 (+14.97%)</td><td>0.04 <b>(-24.14%)</b></td><td>240.90 (-13.03%)</td><td>171.74 (-9.85%)</td><td>151.50 <b>(-21.42%)</b></td><td>138.00 (+2.07%)</td><td>42.26 <b>(-28.23%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>277.00 (n/a)</td><td>190.50 (n/a)</td><td>192.80 (n/a)</td><td>135.20 (n/a)</td><td>58.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (+19.05%)</td><td>0.24 (+12.47%)</td><td>0.22 (+15.17%)</td><td>0.18 (+9.41%)</td><td>0.05 <b>(+21.15%)</b></td><td>222.90 (-8.57%)</td><td>178.08 (-10.71%)</td><td>183.60 (-13.15%)</td><td>131.70 (-16.01%)</td><td>35.94 (-5.22%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>243.80 (n/a)</td><td>199.44 (n/a)</td><td>211.40 (n/a)</td><td>156.80 (n/a)</td><td>37.92 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+12.53%)</td><td>0.20 (-5.29%)</td><td>0.20 (-5.41%)</td><td>0.13 (-14.05%)</td><td>0.06 <b>(+41.88%)</b></td><td>252.10 (+16.34%)</td><td>176.26 (+9.15%)</td><td>166.20 (+5.73%)</td><td>112.50 (-11.14%)</td><td>50.88 <b>(+44.77%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.70 (n/a)</td><td>161.48 (n/a)</td><td>157.20 (n/a)</td><td>126.60 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 <b>(+23.30%)</b></td><td>0.27 <b>(+22.03%)</b></td><td>0.26 (+18.97%)</td><td>0.22 (+15.73%)</td><td>0.04 <b>(+38.70%)</b></td><td>186.20 (-13.56%)</td><td>156.16 (-17.63%)</td><td>155.60 (-15.98%)</td><td>123.40 (-18.87%)</td><td>24.45 (-3.22%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>215.40 (n/a)</td><td>189.58 (n/a)</td><td>185.20 (n/a)</td><td>152.10 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (-18.04%)</td><td>0.18 (-17.11%)</td><td>0.18 <b>(-28.42%)</b></td><td>0.16 (-6.45%)</td><td>0.02 <b>(-59.70%)</b></td><td>202.80 (+6.91%)</td><td>182.50 (+18.05%)</td><td>187.10 <b>(+39.73%)</b></td><td>161.40 <b>(+22.00%)</b></td><td>15.62 <b>(-47.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.70 (n/a)</td><td>154.60 (n/a)</td><td>133.90 (n/a)</td><td>132.30 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 <b>(+26.77%)</b></td><td>0.21 (-2.04%)</td><td>0.20 (-4.02%)</td><td>0.14 <b>(-28.34%)</b></td><td>0.07 <b>(+292.42%)</b></td><td>262.20 <b>(+39.54%)</b></td><td>187.64 (+9.41%)</td><td>180.30 (+4.16%)</td><td>120.30 <b>(-21.11%)</b></td><td>55.78 <b>(+336.83%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>187.90 (n/a)</td><td>171.50 (n/a)</td><td>173.10 (n/a)</td><td>152.50 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (-19.74%)</td><td>0.20 (-6.28%)</td><td>0.20 (+6.78%)</td><td>0.18 (+7.07%)</td><td>0.02 <b>(-64.92%)</b></td><td>184.20 (-6.59%)</td><td>166.40 (+2.87%)</td><td>162.00 (-6.36%)</td><td>147.40 <b>(+24.60%)</b></td><td>14.73 <b>(-58.92%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>197.20 (n/a)</td><td>161.76 (n/a)</td><td>173.00 (n/a)</td><td>118.30 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (+15.35%)</td><td>0.22 (+2.77%)</td><td>0.21 (-3.83%)</td><td>0.15 (-8.05%)</td><td>0.06 <b>(+63.23%)</b></td><td>240.60 (+8.77%)</td><td>173.98 (+0.40%)</td><td>174.30 (+4.00%)</td><td>120.40 (-13.26%)</td><td>45.14 <b>(+50.52%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>221.20 (n/a)</td><td>173.28 (n/a)</td><td>167.60 (n/a)</td><td>138.80 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (+11.40%)</td><td>0.18 (+3.66%)</td><td>0.18 (+0.59%)</td><td>0.16 (+7.76%)</td><td>0.02 (+18.35%)</td><td>207.40 (-7.20%)</td><td>180.44 (-3.40%)</td><td>180.60 (-0.55%)</td><td>150.10 (-10.23%)</td><td>20.85 (-4.40%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>223.50 (n/a)</td><td>186.80 (n/a)</td><td>181.60 (n/a)</td><td>167.20 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (+4.89%)</td><td>0.18 (+8.20%)</td><td>0.18 (-7.31%)</td><td>0.15 <b>(+63.99%)</b></td><td>0.03 <b>(-48.92%)</b></td><td>224.80 <b>(-39.03%)</b></td><td>193.12 (-14.59%)</td><td>191.30 (+7.90%)</td><td>159.40 (-4.61%)</td><td>26.75 <b>(-69.22%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>368.70 (n/a)</td><td>226.12 (n/a)</td><td>177.30 (n/a)</td><td>167.10 (n/a)</td><td>86.89 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 (+1.87%)</td><td>0.18 (+3.98%)</td><td>0.18 (-4.33%)</td><td>0.15 <b>(+44.38%)</b></td><td>0.02 <b>(-47.06%)</b></td><td>215.10 <b>(-30.75%)</b></td><td>183.84 (-8.44%)</td><td>180.60 (+4.51%)</td><td>155.40 (-1.83%)</td><td>22.18 <b>(-64.90%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>310.60 (n/a)</td><td>200.78 (n/a)</td><td>172.80 (n/a)</td><td>158.30 (n/a)</td><td>63.19 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.22 (-1.35%)</td><td>0.19 (-0.86%)</td><td>0.18 (-12.81%)</td><td>0.16 (+15.76%)</td><td>0.03 <b>(-23.38%)</b></td><td>212.80 (-13.60%)</td><td>188.70 (-0.56%)</td><td>198.20 (+14.70%)</td><td>154.90 (+1.37%)</td><td>25.29 <b>(-33.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>246.30 (n/a)</td><td>189.76 (n/a)</td><td>172.80 (n/a)</td><td>152.80 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (+3.89%)</td><td>0.16 (+2.36%)</td><td>0.15 (-7.48%)</td><td>0.14 <b>(+24.17%)</b></td><td>0.03 (-18.12%)</td><td>236.80 (-19.46%)</td><td>205.96 (-3.95%)</td><td>222.00 (+8.08%)</td><td>166.20 (-3.76%)</td><td>30.30 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>294.00 (n/a)</td><td>214.42 (n/a)</td><td>205.40 (n/a)</td><td>172.70 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 <b>(+25.09%)</b></td><td>0.13 (+12.26%)</td><td>0.13 (+0.01%)</td><td>0.10 <b>(+28.19%)</b></td><td>0.03 (+18.00%)</td><td>196.60 <b>(-21.98%)</b></td><td>160.82 (-11.39%)</td><td>161.70 (+0.00%)</td><td>120.80 <b>(-20.05%)</b></td><td>29.38 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>252.00 (n/a)</td><td>181.50 (n/a)</td><td>161.70 (n/a)</td><td>151.10 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 (-18.67%)</td><td>0.11 (-14.61%)</td><td>0.12 (+7.48%)</td><td>0.06 <b>(-44.41%)</b></td><td>0.03 <b>(+50.63%)</b></td><td>332.70 <b>(+79.94%)</b></td><td>208.74 <b>(+25.79%)</b></td><td>164.30 (-6.96%)</td><td>154.60 <b>(+22.89%)</b></td><td>77.40 <b>(+230.03%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>184.90 (n/a)</td><td>165.94 (n/a)</td><td>176.60 (n/a)</td><td>125.80 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 <b>(+36.94%)</b></td><td>0.13 (+17.75%)</td><td>0.14 (+14.53%)</td><td>0.10 <b>(+20.93%)</b></td><td>0.03 <b>(+66.98%)</b></td><td>203.90 (-17.28%)</td><td>158.92 (-13.73%)</td><td>150.60 (-12.65%)</td><td>118.90 <b>(-27.01%)</b></td><td>35.39 (+0.42%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>246.50 (n/a)</td><td>184.22 (n/a)</td><td>172.40 (n/a)</td><td>162.90 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (-8.51%)</td><td>0.13 (-1.73%)</td><td>0.12 (-3.24%)</td><td>0.10 (-7.30%)</td><td>0.02 (-6.40%)</td><td>211.30 (+7.92%)</td><td>167.56 (+1.84%)</td><td>173.40 (+3.34%)</td><td>136.60 (+9.28%)</td><td>30.00 (+9.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>195.80 (n/a)</td><td>164.54 (n/a)</td><td>167.80 (n/a)</td><td>125.00 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.16 (-1.23%)</td><td>0.12 (+2.49%)</td><td>0.12 (+5.55%)</td><td>0.10 (+1.07%)</td><td>0.02 (-9.88%)</td><td>200.50 (-1.04%)</td><td>170.58 (-2.97%)</td><td>172.40 (-5.22%)</td><td>127.50 (+1.27%)</td><td>27.50 (-10.64%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>202.60 (n/a)</td><td>175.80 (n/a)</td><td>181.90 (n/a)</td><td>125.90 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (-7.53%)</td><td>0.12 (-5.02%)</td><td>0.12 (+0.59%)</td><td>0.08 (-16.92%)</td><td>0.02 (+5.26%)</td><td>248.40 <b>(+20.41%)</b></td><td>178.90 (+6.50%)</td><td>167.60 (-0.59%)</td><td>144.40 (+8.16%)</td><td>40.70 <b>(+42.82%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>206.30 (n/a)</td><td>167.98 (n/a)</td><td>168.60 (n/a)</td><td>133.50 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.13 <b>(-22.67%)</b></td><td>0.11 (-1.54%)</td><td>0.11 (+11.86%)</td><td>0.09 (-2.66%)</td><td>0.02 <b>(-52.03%)</b></td><td>222.80 (+2.77%)</td><td>184.86 (-1.81%)</td><td>180.00 (-10.63%)</td><td>153.10 <b>(+29.31%)</b></td><td>26.48 <b>(-33.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.80 (n/a)</td><td>188.26 (n/a)</td><td>201.40 (n/a)</td><td>118.40 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.21 <b>(+57.78%)</b></td><td>0.13 <b>(+24.95%)</b></td><td>0.11 (+16.25%)</td><td>0.08 (-2.40%)</td><td>0.05 <b>(+152.71%)</b></td><td>256.50 (+2.48%)</td><td>181.06 (-13.62%)</td><td>183.40 (-13.98%)</td><td>96.10 <b>(-36.61%)</b></td><td>57.56 <b>(+60.33%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>250.30 (n/a)</td><td>209.62 (n/a)</td><td>213.20 (n/a)</td><td>151.60 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (+8.32%)</td><td>0.15 (+0.20%)</td><td>0.15 (-4.44%)</td><td>0.12 (-2.94%)</td><td>0.03 <b>(+32.44%)</b></td><td>199.60 (+2.99%)</td><td>165.74 (+0.95%)</td><td>169.10 (+4.64%)</td><td>121.90 (-7.65%)</td><td>30.37 <b>(+24.21%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.80 (n/a)</td><td>164.18 (n/a)</td><td>161.60 (n/a)</td><td>132.00 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (-3.65%)</td><td>0.15 (-0.48%)</td><td>0.16 (-1.99%)</td><td>0.11 (-0.54%)</td><td>0.02 (-14.94%)</td><td>220.10 (+0.55%)</td><td>168.84 (-0.13%)</td><td>157.30 (+2.01%)</td><td>145.90 (+3.84%)</td><td>29.89 (-8.97%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>218.90 (n/a)</td><td>169.06 (n/a)</td><td>154.20 (n/a)</td><td>140.50 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (+2.73%)</td><td>0.16 (-0.73%)</td><td>0.14 (-11.25%)</td><td>0.14 (+1.57%)</td><td>0.03 <b>(+47.75%)</b></td><td>181.60 (-1.52%)</td><td>157.94 (+2.23%)</td><td>175.10 (+12.68%)</td><td>125.40 (-2.72%)</td><td>28.67 <b>(+41.04%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>154.50 (n/a)</td><td>155.40 (n/a)</td><td>128.90 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (-13.94%)</td><td>0.14 (-2.89%)</td><td>0.14 (+1.38%)</td><td>0.11 (+4.59%)</td><td>0.03 <b>(-20.24%)</b></td><td>226.70 (-4.39%)</td><td>185.10 (+1.90%)</td><td>180.50 (-1.37%)</td><td>142.10 (+16.19%)</td><td>38.33 (-6.20%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>237.10 (n/a)</td><td>181.64 (n/a)</td><td>183.00 (n/a)</td><td>122.30 (n/a)</td><td>40.86 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 <b>(+36.59%)</b></td><td>0.14 (+11.99%)</td><td>0.13 (+2.16%)</td><td>0.12 (+1.94%)</td><td>0.03 <b>(+221.31%)</b></td><td>211.30 (-1.90%)</td><td>175.84 (-8.45%)</td><td>186.50 (-2.10%)</td><td>130.60 <b>(-26.75%)</b></td><td>31.63 <b>(+124.76%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>192.08 (n/a)</td><td>190.50 (n/a)</td><td>178.30 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 (-0.38%)</td><td>0.17 (+2.98%)</td><td>0.17 (+6.61%)</td><td>0.14 (+11.91%)</td><td>0.02 (-9.84%)</td><td>177.70 (-10.66%)</td><td>151.24 (-3.46%)</td><td>145.00 (-6.21%)</td><td>128.20 (+0.31%)</td><td>21.30 (-19.63%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.90 (n/a)</td><td>156.66 (n/a)</td><td>154.60 (n/a)</td><td>127.80 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 <b>(+25.78%)</b></td><td>0.13 (+5.45%)</td><td>0.12 (-1.65%)</td><td>0.09 (-13.93%)</td><td>0.04 <b>(+92.11%)</b></td><td>282.40 (+16.17%)</td><td>203.32 (+0.15%)</td><td>206.40 (+1.67%)</td><td>120.60 <b>(-20.50%)</b></td><td>59.54 <b>(+75.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>243.10 (n/a)</td><td>203.02 (n/a)</td><td>203.00 (n/a)</td><td>151.70 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.17 (+7.92%)</td><td>0.14 (+3.15%)</td><td>0.14 (+4.50%)</td><td>0.10 (-9.10%)</td><td>0.03 <b>(+29.48%)</b></td><td>244.60 (+10.03%)</td><td>184.52 (-1.68%)</td><td>175.80 (-4.30%)</td><td>141.90 (-7.32%)</td><td>39.39 <b>(+31.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>187.68 (n/a)</td><td>183.70 (n/a)</td><td>153.10 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (-6.69%)</td><td>0.12 (-6.32%)</td><td>0.12 (-9.06%)</td><td>0.09 (+0.75%)</td><td>0.02 <b>(-28.19%)</b></td><td>195.00 (-0.71%)</td><td>154.74 (+5.18%)</td><td>147.90 (+9.96%)</td><td>130.10 (+7.17%)</td><td>25.26 <b>(-21.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>196.40 (n/a)</td><td>147.12 (n/a)</td><td>134.50 (n/a)</td><td>121.40 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 (+3.54%)</td><td>0.12 (+4.35%)</td><td>0.12 (-0.26%)</td><td>0.10 (+6.63%)</td><td>0.02 (-1.49%)</td><td>182.80 (-6.21%)</td><td>151.36 (-4.46%)</td><td>153.80 (+0.26%)</td><td>122.40 (-3.39%)</td><td>24.68 (-12.05%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>158.42 (n/a)</td><td>153.40 (n/a)</td><td>126.70 (n/a)</td><td>28.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (-11.14%)</td><td>0.11 (+0.78%)</td><td>0.11 (+5.30%)</td><td>0.09 (+5.34%)</td><td>0.02 <b>(-34.28%)</b></td><td>194.60 (-5.07%)</td><td>167.30 (-2.90%)</td><td>171.90 (-5.03%)</td><td>128.50 (+12.52%)</td><td>24.83 <b>(-27.99%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>205.00 (n/a)</td><td>172.30 (n/a)</td><td>181.00 (n/a)</td><td>114.20 (n/a)</td><td>34.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 (+10.06%)</td><td>0.10 (-4.33%)</td><td>0.11 (+5.88%)</td><td>0.07 <b>(-27.05%)</b></td><td>0.03 <b>(+116.04%)</b></td><td>259.70 <b>(+37.04%)</b></td><td>190.92 (+10.28%)</td><td>168.10 (-5.56%)</td><td>128.20 (-9.14%)</td><td>54.07 <b>(+180.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>173.12 (n/a)</td><td>178.00 (n/a)</td><td>141.10 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.12 (-4.92%)</td><td>0.11 (+11.98%)</td><td>0.11 (+16.69%)</td><td>0.10 <b>(+61.31%)</b></td><td>0.01 <b>(-57.06%)</b></td><td>193.50 <b>(-38.00%)</b></td><td>170.84 (-16.14%)</td><td>168.40 (-14.30%)</td><td>151.90 (+5.19%)</td><td>18.23 <b>(-72.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>312.10 (n/a)</td><td>203.72 (n/a)</td><td>196.50 (n/a)</td><td>144.40 (n/a)</td><td>66.05 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 <b>(+39.97%)</b></td><td>0.11 (+12.62%)</td><td>0.10 (+4.41%)</td><td>0.09 (+5.38%)</td><td>0.02 <b>(+293.81%)</b></td><td>204.00 (-5.07%)</td><td>179.60 (-9.30%)</td><td>189.50 (-4.24%)</td><td>132.30 <b>(-28.56%)</b></td><td>28.11 <b>(+158.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>198.02 (n/a)</td><td>197.90 (n/a)</td><td>185.20 (n/a)</td><td>10.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.11 (-18.90%)</td><td>0.09 (-11.54%)</td><td>0.10 (-4.55%)</td><td>0.07 (-10.61%)</td><td>0.02 <b>(-30.92%)</b></td><td>249.10 (+11.90%)</td><td>200.68 (+11.64%)</td><td>182.20 (+4.77%)</td><td>167.00 <b>(+23.25%)</b></td><td>35.58 (-6.09%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>179.76 (n/a)</td><td>173.90 (n/a)</td><td>135.50 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.14 <b>(+31.85%)</b></td><td>0.12 <b>(+69.20%)</b></td><td>0.12 <b>(+67.86%)</b></td><td>0.10 <b>(+103.64%)</b></td><td>0.02 <b>(-28.97%)</b></td><td>182.20 <b>(-50.90%)</b></td><td>152.22 <b>(-44.26%)</b></td><td>150.20 <b>(-40.42%)</b></td><td>133.90 <b>(-24.18%)</b></td><td>20.31 <b>(-74.65%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>371.10 (n/a)</td><td>273.08 (n/a)</td><td>252.10 (n/a)</td><td>176.60 (n/a)</td><td>80.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.66 (-4.60%)</td><td>0.53 (-2.66%)</td><td>0.54 (-5.67%)</td><td>0.34 (-15.07%)</td><td>0.12 (+9.57%)</td><td>285.60 (+17.77%)</td><td>194.12 (+4.48%)</td><td>182.90 (+6.03%)</td><td>148.80 (+4.79%)</td><td>53.19 <b>(+40.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.69 (n/a)</td><td>0.55 (n/a)</td><td>0.57 (n/a)</td><td>0.41 (n/a)</td><td>0.11 (n/a)</td><td>242.50 (n/a)</td><td>185.80 (n/a)</td><td>172.50 (n/a)</td><td>142.00 (n/a)</td><td>37.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 (+0.64%)</td><td>0.62 (-3.85%)</td><td>0.61 (-5.95%)</td><td>0.55 (+2.19%)</td><td>0.09 (+8.04%)</td><td>179.10 (-2.13%)</td><td>160.58 (+4.19%)</td><td>160.90 (+6.35%)</td><td>126.60 (-0.63%)</td><td>20.72 (+3.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.77 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.08 (n/a)</td><td>183.00 (n/a)</td><td>154.12 (n/a)</td><td>151.30 (n/a)</td><td>127.40 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.63 (+8.05%)</td><td>0.56 (+7.59%)</td><td>0.60 (+9.49%)</td><td>0.42 (-10.60%)</td><td>0.09 <b>(+71.86%)</b></td><td>234.10 (+11.90%)</td><td>178.64 (-5.66%)</td><td>165.00 (-8.69%)</td><td>156.60 (-7.45%)</td><td>32.29 <b>(+76.11%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.58 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>209.20 (n/a)</td><td>189.36 (n/a)</td><td>180.70 (n/a)</td><td>169.20 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.82 <b>(+68.26%)</b></td><td>0.60 <b>(+39.11%)</b></td><td>0.61 <b>(+45.07%)</b></td><td>0.45 (+14.02%)</td><td>0.14 <b>(+301.39%)</b></td><td>218.40 (-12.29%)</td><td>170.92 <b>(-25.40%)</b></td><td>160.80 <b>(-31.05%)</b></td><td>120.00 <b>(-40.59%)</b></td><td>38.03 <b>(+111.12%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.04 (n/a)</td><td>249.00 (n/a)</td><td>229.10 (n/a)</td><td>233.20 (n/a)</td><td>202.00 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.54 (-3.43%)</td><td>0.43 (-5.85%)</td><td>0.45 (+1.09%)</td><td>0.33 (-4.18%)</td><td>0.08 <b>(-21.73%)</b></td><td>220.70 (+4.35%)</td><td>175.52 (+4.94%)</td><td>165.70 (-1.07%)</td><td>135.70 (+3.59%)</td><td>31.98 (-12.23%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>211.50 (n/a)</td><td>167.26 (n/a)</td><td>167.50 (n/a)</td><td>131.00 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (-16.98%)</td><td>0.36 <b>(-20.75%)</b></td><td>0.39 (-8.89%)</td><td>0.21 <b>(-44.99%)</b></td><td>0.09 <b>(+50.87%)</b></td><td>351.50 <b>(+81.75%)</b></td><td>221.72 <b>(+33.73%)</b></td><td>189.70 (+9.78%)</td><td>166.70 <b>(+20.45%)</b></td><td>75.88 <b>(+242.09%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>193.40 (n/a)</td><td>165.80 (n/a)</td><td>172.80 (n/a)</td><td>138.40 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.48 (+6.31%)</td><td>0.43 (+7.66%)</td><td>0.44 (+14.40%)</td><td>0.35 (-5.39%)</td><td>0.05 <b>(+51.81%)</b></td><td>213.10 (+5.65%)</td><td>174.74 (-6.47%)</td><td>168.10 (-12.54%)</td><td>154.50 (-5.91%)</td><td>22.37 <b>(+56.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.03 (n/a)</td><td>201.70 (n/a)</td><td>186.82 (n/a)</td><td>192.20 (n/a)</td><td>164.20 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (-9.19%)</td><td>0.38 (-2.27%)</td><td>0.38 (-0.95%)</td><td>0.33 (+1.25%)</td><td>0.05 <b>(-27.53%)</b></td><td>225.10 (-1.23%)</td><td>195.60 (+1.44%)</td><td>193.40 (+0.94%)</td><td>166.80 (+10.10%)</td><td>23.67 <b>(-20.85%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>227.90 (n/a)</td><td>192.82 (n/a)</td><td>191.60 (n/a)</td><td>151.50 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.30 (+9.23%)</td><td>0.20 (-5.10%)</td><td>0.19 (+2.81%)</td><td>0.11 <b>(-37.82%)</b></td><td>0.07 <b>(+76.22%)</b></td><td>337.60 <b>(+60.84%)</b></td><td>205.80 (+15.14%)</td><td>189.30 (-2.77%)</td><td>123.30 (-8.46%)</td><td>82.70 <b>(+164.85%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>209.90 (n/a)</td><td>178.74 (n/a)</td><td>194.70 (n/a)</td><td>134.70 (n/a)</td><td>31.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 (+0.30%)</td><td>0.21 (+0.27%)</td><td>0.20 (-13.15%)</td><td>0.19 <b>(+25.66%)</b></td><td>0.03 <b>(-37.55%)</b></td><td>191.80 <b>(-20.45%)</b></td><td>176.06 (-2.86%)</td><td>182.70 (+15.12%)</td><td>142.10 (-0.35%)</td><td>19.60 <b>(-52.03%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>241.10 (n/a)</td><td>181.24 (n/a)</td><td>158.70 (n/a)</td><td>142.60 (n/a)</td><td>40.87 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (-1.73%)</td><td>0.23 (+18.57%)</td><td>0.27 <b>(+52.59%)</b></td><td>0.15 (-0.90%)</td><td>0.06 (+15.05%)</td><td>249.20 (+0.89%)</td><td>168.78 (-14.26%)</td><td>136.20 <b>(-34.46%)</b></td><td>133.10 (+1.84%)</td><td>51.55 (+16.82%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>247.00 (n/a)</td><td>196.84 (n/a)</td><td>207.80 (n/a)</td><td>130.70 (n/a)</td><td>44.12 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+6.56%)</td><td>0.25 <b>(+32.87%)</b></td><td>0.27 <b>(+50.23%)</b></td><td>0.20 <b>(+40.27%)</b></td><td>0.04 <b>(-26.97%)</b></td><td>185.50 <b>(-28.74%)</b></td><td>148.82 <b>(-26.98%)</b></td><td>136.50 <b>(-33.41%)</b></td><td>127.00 (-6.13%)</td><td>23.66 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>260.30 (n/a)</td><td>203.82 (n/a)</td><td>205.00 (n/a)</td><td>135.30 (n/a)</td><td>46.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.24 <b>(-23.70%)</b></td><td>0.20 (-0.32%)</td><td>0.20 (+2.80%)</td><td>0.18 (+18.70%)</td><td>0.02 <b>(-64.67%)</b></td><td>202.40 (-15.77%)</td><td>182.14 (-4.99%)</td><td>185.60 (-2.73%)</td><td>152.20 <b>(+30.98%)</b></td><td>18.96 <b>(-59.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>240.30 (n/a)</td><td>191.70 (n/a)</td><td>190.80 (n/a)</td><td>116.20 (n/a)</td><td>47.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.19 <b>(-31.39%)</b></td><td>0.17 <b>(-29.45%)</b></td><td>0.18 <b>(-26.89%)</b></td><td>0.12 <b>(-37.56%)</b></td><td>0.03 (-10.10%)</td><td>310.30 <b>(+60.20%)</b></td><td>227.02 <b>(+43.68%)</b></td><td>209.50 <b>(+36.75%)</b></td><td>192.90 <b>(+45.69%)</b></td><td>47.54 <b>(+113.60%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>193.70 (n/a)</td><td>158.00 (n/a)</td><td>153.20 (n/a)</td><td>132.40 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (+15.43%)</td><td>0.22 (+6.79%)</td><td>0.21 (+7.99%)</td><td>0.19 (+5.56%)</td><td>0.04 (+18.41%)</td><td>196.00 (-5.27%)</td><td>170.92 (-6.19%)</td><td>177.10 (-7.42%)</td><td>130.10 (-13.38%)</td><td>25.00 (-5.88%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>206.90 (n/a)</td><td>182.20 (n/a)</td><td>191.30 (n/a)</td><td>150.20 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+14.36%)</td><td>0.21 (+3.56%)</td><td>0.21 (+6.22%)</td><td>0.17 (-12.38%)</td><td>0.05 <b>(+81.51%)</b></td><td>221.90 (+14.15%)</td><td>178.36 (-1.23%)</td><td>173.50 (-5.86%)</td><td>129.00 (-12.54%)</td><td>34.60 <b>(+80.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>180.58 (n/a)</td><td>184.30 (n/a)</td><td>147.50 (n/a)</td><td>19.14 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 <b>(+21.79%)</b></td><td>0.24 (+5.79%)</td><td>0.23 (+1.86%)</td><td>0.20 (-5.14%)</td><td>0.04 <b>(+162.39%)</b></td><td>205.70 (+5.43%)</td><td>175.44 (-3.70%)</td><td>178.70 (-1.81%)</td><td>134.00 (-17.89%)</td><td>27.92 <b>(+125.39%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>182.18 (n/a)</td><td>182.00 (n/a)</td><td>163.20 (n/a)</td><td>12.39 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.32 (+2.52%)</td><td>0.27 (+0.53%)</td><td>0.28 (+2.35%)</td><td>0.21 (-9.19%)</td><td>0.04 <b>(+41.70%)</b></td><td>193.40 (+10.07%)</td><td>153.22 (+0.46%)</td><td>144.80 (-2.29%)</td><td>129.60 (-2.48%)</td><td>24.54 <b>(+54.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>175.70 (n/a)</td><td>152.52 (n/a)</td><td>148.20 (n/a)</td><td>132.90 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.32 (+2.90%)</td><td>0.29 (+14.98%)</td><td>0.31 <b>(+24.42%)</b></td><td>0.23 <b>(+28.69%)</b></td><td>0.04 <b>(-21.93%)</b></td><td>176.50 <b>(-22.28%)</b></td><td>145.36 (-14.97%)</td><td>130.60 (-19.63%)</td><td>127.30 (-2.82%)</td><td>23.49 <b>(-41.46%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>227.10 (n/a)</td><td>170.96 (n/a)</td><td>162.50 (n/a)</td><td>131.00 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.36 <b>(+30.48%)</b></td><td>0.28 <b>(+20.44%)</b></td><td>0.28 <b>(+21.50%)</b></td><td>0.17 (-6.24%)</td><td>0.08 <b>(+128.24%)</b></td><td>235.90 (+6.65%)</td><td>159.40 (-12.50%)</td><td>146.70 (-17.68%)</td><td>113.20 <b>(-23.36%)</b></td><td>49.45 <b>(+85.98%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>221.20 (n/a)</td><td>182.18 (n/a)</td><td>178.20 (n/a)</td><td>147.70 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.29 (+14.13%)</td><td>0.23 (+2.08%)</td><td>0.23 (+0.42%)</td><td>0.17 (-9.97%)</td><td>0.05 <b>(+107.31%)</b></td><td>239.20 (+11.05%)</td><td>185.58 (+0.71%)</td><td>179.90 (-0.44%)</td><td>143.50 (-12.34%)</td><td>40.06 <b>(+98.97%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>215.40 (n/a)</td><td>184.28 (n/a)</td><td>180.70 (n/a)</td><td>163.70 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (-17.63%)</td><td>0.22 (+0.41%)</td><td>0.23 (+12.04%)</td><td>0.17 (+13.18%)</td><td>0.04 <b>(-40.23%)</b></td><td>235.70 (-11.66%)</td><td>189.22 (-4.13%)</td><td>179.00 (-10.77%)</td><td>146.00 <b>(+21.36%)</b></td><td>35.58 <b>(-31.53%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>266.80 (n/a)</td><td>197.38 (n/a)</td><td>200.60 (n/a)</td><td>120.30 (n/a)</td><td>51.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.33 (+19.76%)</td><td>0.25 <b>(+21.74%)</b></td><td>0.24 (+15.75%)</td><td>0.21 <b>(+36.08%)</b></td><td>0.05 (+6.48%)</td><td>192.30 <b>(-26.49%)</b></td><td>164.50 (-18.67%)</td><td>170.70 (-13.61%)</td><td>123.60 (-16.54%)</td><td>26.32 <b>(-35.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>261.60 (n/a)</td><td>202.26 (n/a)</td><td>197.60 (n/a)</td><td>148.10 (n/a)</td><td>40.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 <b>(+20.13%)</b></td><td>0.23 <b>(+24.48%)</b></td><td>0.22 (+16.88%)</td><td>0.20 <b>(+42.10%)</b></td><td>0.03 (-11.79%)</td><td>202.30 <b>(-29.63%)</b></td><td>181.52 <b>(-20.80%)</b></td><td>186.50 (-14.45%)</td><td>153.80 (-16.77%)</td><td>22.03 <b>(-47.92%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>287.50 (n/a)</td><td>229.18 (n/a)</td><td>218.00 (n/a)</td><td>184.80 (n/a)</td><td>42.30 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 <b>(+45.27%)</b></td><td>0.23 <b>(+35.65%)</b></td><td>0.21 <b>(+25.98%)</b></td><td>0.17 <b>(+21.00%)</b></td><td>0.05 <b>(+120.37%)</b></td><td>201.50 (-17.35%)</td><td>160.72 <b>(-24.49%)</b></td><td>164.30 <b>(-20.59%)</b></td><td>125.10 <b>(-31.15%)</b></td><td>34.86 (+18.88%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>243.80 (n/a)</td><td>212.84 (n/a)</td><td>206.90 (n/a)</td><td>181.70 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.26 <b>(+39.28%)</b></td><td>0.18 (+7.38%)</td><td>0.18 (+5.60%)</td><td>0.13 (-8.84%)</td><td>0.05 <b>(+180.08%)</b></td><td>274.40 (+9.67%)</td><td>203.36 (-2.16%)</td><td>190.20 (-5.33%)</td><td>132.30 <b>(-28.21%)</b></td><td>53.58 <b>(+113.51%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>250.20 (n/a)</td><td>207.84 (n/a)</td><td>200.90 (n/a)</td><td>184.30 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.28 (+3.29%)</td><td>0.23 (+6.02%)</td><td>0.23 (+15.76%)</td><td>0.19 (-4.99%)</td><td>0.05 <b>(+40.50%)</b></td><td>186.40 (+5.25%)</td><td>153.60 (-4.14%)</td><td>148.70 (-13.60%)</td><td>122.50 (-3.24%)</td><td>30.83 <b>(+44.88%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>177.10 (n/a)</td><td>160.24 (n/a)</td><td>172.10 (n/a)</td><td>126.60 (n/a)</td><td>21.28 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (+10.97%)</td><td>0.23 (+17.35%)</td><td>0.24 <b>(+31.75%)</b></td><td>0.14 (-13.38%)</td><td>0.05 <b>(+58.29%)</b></td><td>247.90 (+15.46%)</td><td>162.88 (-11.85%)</td><td>142.20 <b>(-24.12%)</b></td><td>129.80 (-9.92%)</td><td>48.53 <b>(+71.42%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>214.70 (n/a)</td><td>184.78 (n/a)</td><td>187.40 (n/a)</td><td>144.10 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.25 (-0.07%)</td><td>0.22 (+13.08%)</td><td>0.23 <b>(+23.56%)</b></td><td>0.17 (+5.53%)</td><td>0.04 (-1.28%)</td><td>201.20 (-5.23%)</td><td>162.42 (-11.74%)</td><td>151.30 (-19.05%)</td><td>137.50 (+0.07%)</td><td>28.24 (-7.36%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>212.30 (n/a)</td><td>184.02 (n/a)</td><td>186.90 (n/a)</td><td>137.40 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.27 (+0.37%)</td><td>0.23 (+15.80%)</td><td>0.22 (+11.07%)</td><td>0.19 <b>(+50.29%)</b></td><td>0.03 <b>(-45.63%)</b></td><td>178.80 <b>(-33.46%)</b></td><td>156.94 (-18.33%)</td><td>156.50 (-9.95%)</td><td>131.00 (-0.30%)</td><td>20.73 <b>(-64.02%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>268.70 (n/a)</td><td>192.16 (n/a)</td><td>173.80 (n/a)</td><td>131.40 (n/a)</td><td>57.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.20 (-11.99%)</td><td>0.18 (-8.46%)</td><td>0.18 (-1.64%)</td><td>0.15 (-15.07%)</td><td>0.02 (-4.98%)</td><td>233.20 (+17.72%)</td><td>200.12 (+9.41%)</td><td>196.00 (+1.66%)</td><td>176.90 (+13.62%)</td><td>22.46 <b>(+27.27%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>198.10 (n/a)</td><td>182.90 (n/a)</td><td>192.80 (n/a)</td><td>155.70 (n/a)</td><td>17.65 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 <b>(+51.24%)</b></td><td>0.21 (+11.74%)</td><td>0.18 (-8.01%)</td><td>0.15 (-15.18%)</td><td>0.07 <b>(+548.45%)</b></td><td>229.50 (+17.87%)</td><td>174.08 (-4.05%)</td><td>196.00 (+8.71%)</td><td>111.70 <b>(-33.91%)</b></td><td>48.96 <b>(+397.79%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>194.70 (n/a)</td><td>181.42 (n/a)</td><td>180.30 (n/a)</td><td>169.00 (n/a)</td><td>9.84 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.08 (-7.82%)</td><td>0.89 (+10.07%)</td><td>0.90 <b>(+29.61%)</b></td><td>0.71 <b>(+30.83%)</b></td><td>0.16 <b>(-41.10%)</b></td><td>185.70 <b>(-23.58%)</b></td><td>150.42 (-14.34%)</td><td>145.00 <b>(-22.87%)</b></td><td>121.80 (+8.56%)</td><td>27.39 <b>(-49.93%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.17 (n/a)</td><td>0.81 (n/a)</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.27 (n/a)</td><td>243.00 (n/a)</td><td>175.60 (n/a)</td><td>188.00 (n/a)</td><td>112.20 (n/a)</td><td>54.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.88 (-14.63%)</td><td>0.76 (-4.73%)</td><td>0.82 (+4.31%)</td><td>0.54 (-17.53%)</td><td>0.13 (-11.49%)</td><td>243.10 <b>(+21.25%)</b></td><td>177.06 (+5.36%)</td><td>160.50 (-4.12%)</td><td>149.10 (+17.12%)</td><td>38.15 <b>(+28.34%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.03 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.15 (n/a)</td><td>200.50 (n/a)</td><td>168.06 (n/a)</td><td>167.40 (n/a)</td><td>127.30 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.98 (-0.48%)</td><td>0.69 (-10.89%)</td><td>0.74 (+0.68%)</td><td>0.44 <b>(-34.60%)</b></td><td>0.22 <b>(+75.61%)</b></td><td>299.50 <b>(+52.88%)</b></td><td>207.66 (+19.87%)</td><td>177.70 (-0.67%)</td><td>134.30 (+0.52%)</td><td>67.78 <b>(+185.28%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.98 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.67 (n/a)</td><td>0.12 (n/a)</td><td>195.90 (n/a)</td><td>173.24 (n/a)</td><td>178.90 (n/a)</td><td>133.60 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.00 (+0.00%)</td><td>0.00 (-3.21%)</td><td>0.00 (-4.55%)</td><td>0.00 (-2.44%)</td><td>0.00 (+14.95%)</td><td>1011.78 (+0.40%)</td><td>968.63 (+2.85%)</td><td>979.63 (+5.54%)</td><td>910.05 (+0.02%)</td><td>41.01 (+0.68%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1007.71 (n/a)</td><td>941.81 (n/a)</td><td>928.24 (n/a)</td><td>909.89 (n/a)</td><td>40.73 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.01 (+2.44%)</td><td>0.01 (+1.72%)</td><td>0.01 (+2.47%)</td><td>0.01 (+1.25%)</td><td>0.00 <b>(+81.27%)</b></td><td>1017.25 (-1.10%)</td><td>993.90 (-1.52%)</td><td>990.19 (-1.91%)</td><td>970.11 (-2.62%)</td><td>20.60 <b>(+53.72%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1028.56 (n/a)</td><td>1009.21 (n/a)</td><td>1009.45 (n/a)</td><td>996.16 (n/a)</td><td>13.40 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.98 (+1.60%)</td><td>0.96 (+0.07%)</td><td>0.95 (-0.14%)</td><td>0.94 (-0.52%)</td><td>0.02 <b>(+85.04%)</b></td><td>2236.59 (+0.53%)</td><td>2196.16 (-0.05%)</td><td>2204.66 (+0.13%)</td><td>2136.09 (-1.57%)</td><td>37.99 <b>(+82.90%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2224.76 (n/a)</td><td>2197.36 (n/a)</td><td>2201.82 (n/a)</td><td>2170.22 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.26 (-7.15%)</td><td>4.60 (-12.03%)</td><td>4.66 (-11.41%)</td><td>4.19 (-10.56%)</td><td>0.44 (+1.82%)</td><td>250.40 (+11.84%)</td><td>229.66 (+13.85%)</td><td>225.10 (+12.83%)</td><td>199.40 (+7.67%)</td><td>21.39 <b>(+25.80%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.66 (n/a)</td><td>5.23 (n/a)</td><td>5.26 (n/a)</td><td>4.68 (n/a)</td><td>0.43 (n/a)</td><td>223.90 (n/a)</td><td>201.72 (n/a)</td><td>199.50 (n/a)</td><td>185.20 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.23 (-0.71%)</td><td>4.27 (-9.87%)</td><td>4.21 (-7.73%)</td><td>3.66 (-17.88%)</td><td>0.63 <b>(+77.98%)</b></td><td>286.50 <b>(+21.76%)</b></td><td>249.80 (+12.27%)</td><td>249.00 (+8.36%)</td><td>200.50 (+0.75%)</td><td>34.34 <b>(+117.19%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.27 (n/a)</td><td>4.73 (n/a)</td><td>4.56 (n/a)</td><td>4.46 (n/a)</td><td>0.35 (n/a)</td><td>235.30 (n/a)</td><td>222.50 (n/a)</td><td>229.80 (n/a)</td><td>199.00 (n/a)</td><td>15.81 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.62 (-8.90%)</td><td>4.73 (-7.82%)</td><td>4.66 (-8.96%)</td><td>4.12 (-4.31%)</td><td>0.57 <b>(-27.80%)</b></td><td>254.60 (+4.52%)</td><td>224.20 (+7.63%)</td><td>225.10 (+9.86%)</td><td>186.70 (+9.76%)</td><td>25.75 (-19.09%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.17 (n/a)</td><td>5.13 (n/a)</td><td>5.12 (n/a)</td><td>4.30 (n/a)</td><td>0.79 (n/a)</td><td>243.60 (n/a)</td><td>208.30 (n/a)</td><td>204.90 (n/a)</td><td>170.10 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.47 (-9.34%)</td><td>4.87 (-3.39%)</td><td>5.15 (+6.38%)</td><td>3.73 (-17.27%)</td><td>0.70 (+13.36%)</td><td>280.80 <b>(+20.88%)</b></td><td>219.38 (+4.34%)</td><td>203.40 (-6.01%)</td><td>191.60 (+10.31%)</td><td>36.33 <b>(+53.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>6.04 (n/a)</td><td>5.04 (n/a)</td><td>4.85 (n/a)</td><td>4.51 (n/a)</td><td>0.62 (n/a)</td><td>232.30 (n/a)</td><td>210.26 (n/a)</td><td>216.40 (n/a)</td><td>173.70 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.78 (-4.51%)</td><td>8.04 (+1.08%)</td><td>8.07 (+0.06%)</td><td>7.08 (+10.46%)</td><td>0.68 <b>(-32.74%)</b></td><td>296.00 (-9.48%)</td><td>262.54 (-1.85%)</td><td>260.00 (-0.04%)</td><td>238.90 (+4.73%)</td><td>22.87 <b>(-37.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.19 (n/a)</td><td>7.95 (n/a)</td><td>8.06 (n/a)</td><td>6.41 (n/a)</td><td>1.01 (n/a)</td><td>327.00 (n/a)</td><td>267.50 (n/a)</td><td>260.10 (n/a)</td><td>228.10 (n/a)</td><td>36.70 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.55 (-0.83%)</td><td>7.77 (-0.29%)</td><td>7.81 (-0.10%)</td><td>7.01 (+0.98%)</td><td>0.55 <b>(-22.07%)</b></td><td>299.00 (-0.96%)</td><td>271.02 (+0.03%)</td><td>268.60 (+0.11%)</td><td>245.40 (+0.82%)</td><td>19.38 <b>(-21.94%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.62 (n/a)</td><td>7.79 (n/a)</td><td>7.82 (n/a)</td><td>6.95 (n/a)</td><td>0.71 (n/a)</td><td>301.90 (n/a)</td><td>270.94 (n/a)</td><td>268.30 (n/a)</td><td>243.40 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.05 (+5.75%)</td><td>7.79 (+0.69%)</td><td>7.61 (-2.65%)</td><td>6.66 (-6.86%)</td><td>1.09 <b>(+82.28%)</b></td><td>315.10 (+7.36%)</td><td>273.40 (+0.39%)</td><td>275.70 (+2.72%)</td><td>231.70 (-5.47%)</td><td>37.92 <b>(+81.84%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.56 (n/a)</td><td>7.74 (n/a)</td><td>7.81 (n/a)</td><td>7.15 (n/a)</td><td>0.60 (n/a)</td><td>293.50 (n/a)</td><td>272.34 (n/a)</td><td>268.40 (n/a)</td><td>245.10 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.36 (+4.89%)</td><td>8.93 (+8.14%)</td><td>9.03 (+3.61%)</td><td>8.45 <b>(+31.58%)</b></td><td>0.39 <b>(-62.66%)</b></td><td>248.20 <b>(-23.98%)</b></td><td>235.22 (-8.78%)</td><td>232.20 (-3.49%)</td><td>224.00 (-4.68%)</td><td>10.34 <b>(-73.24%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.92 (n/a)</td><td>8.26 (n/a)</td><td>8.72 (n/a)</td><td>6.42 (n/a)</td><td>1.04 (n/a)</td><td>326.50 (n/a)</td><td>257.86 (n/a)</td><td>240.60 (n/a)</td><td>235.00 (n/a)</td><td>38.63 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>11.35 (+18.28%)</td><td>8.41 (+4.09%)</td><td>7.96 (-0.31%)</td><td>6.48 (-11.15%)</td><td>1.99 <b>(+112.11%)</b></td><td>323.50 (+12.52%)</td><td>259.88 (-0.85%)</td><td>263.50 (+0.30%)</td><td>184.70 (-15.47%)</td><td>56.87 <b>(+102.41%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>9.60 (n/a)</td><td>8.08 (n/a)</td><td>7.98 (n/a)</td><td>7.30 (n/a)</td><td>0.94 (n/a)</td><td>287.50 (n/a)</td><td>262.10 (n/a)</td><td>262.70 (n/a)</td><td>218.50 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>9.43 (-5.83%)</td><td>7.62 (-11.87%)</td><td>7.37 (-10.39%)</td><td>5.26 <b>(-29.72%)</b></td><td>1.59 <b>(+46.12%)</b></td><td>398.40 <b>(+42.29%)</b></td><td>286.34 (+16.64%)</td><td>284.60 (+11.61%)</td><td>222.30 (+6.16%)</td><td>68.36 <b>(+127.26%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>10.02 (n/a)</td><td>8.65 (n/a)</td><td>8.22 (n/a)</td><td>7.49 (n/a)</td><td>1.09 (n/a)</td><td>280.00 (n/a)</td><td>245.48 (n/a)</td><td>255.00 (n/a)</td><td>209.40 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.41 (-0.27%)</td><td>11.21 (-3.26%)</td><td>10.95 (-10.48%)</td><td>10.69 (+3.88%)</td><td>0.70 <b>(-30.91%)</b></td><td>392.30 (-3.73%)</td><td>375.34 (+3.02%)</td><td>383.10 (+11.69%)</td><td>337.90 (+0.27%)</td><td>21.90 <b>(-33.57%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.45 (n/a)</td><td>11.59 (n/a)</td><td>12.23 (n/a)</td><td>10.29 (n/a)</td><td>1.01 (n/a)</td><td>407.50 (n/a)</td><td>364.32 (n/a)</td><td>343.00 (n/a)</td><td>337.00 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.54 (-3.09%)</td><td>11.84 (-2.32%)</td><td>12.30 (+1.31%)</td><td>10.43 (-7.10%)</td><td>0.89 <b>(+38.90%)</b></td><td>402.30 (+7.65%)</td><td>356.06 (+2.64%)</td><td>341.00 (-1.27%)</td><td>334.50 (+3.18%)</td><td>28.55 <b>(+53.86%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.94 (n/a)</td><td>12.12 (n/a)</td><td>12.14 (n/a)</td><td>11.22 (n/a)</td><td>0.64 (n/a)</td><td>373.70 (n/a)</td><td>346.90 (n/a)</td><td>345.40 (n/a)</td><td>324.20 (n/a)</td><td>18.55 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>11.76 (-15.30%)</td><td>11.41 (-4.58%)</td><td>11.44 (-5.20%)</td><td>10.99 (+9.34%)</td><td>0.36 <b>(-75.51%)</b></td><td>381.60 (-8.55%)</td><td>368.04 (+3.63%)</td><td>366.60 (+5.50%)</td><td>356.70 (+18.07%)</td><td>11.55 <b>(-73.74%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.88 (n/a)</td><td>11.95 (n/a)</td><td>12.07 (n/a)</td><td>10.05 (n/a)</td><td>1.46 (n/a)</td><td>417.30 (n/a)</td><td>355.16 (n/a)</td><td>347.50 (n/a)</td><td>302.10 (n/a)</td><td>43.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>13.84 (+6.67%)</td><td>12.54 (+2.62%)</td><td>12.44 (+1.76%)</td><td>11.54 (+3.49%)</td><td>0.84 (+12.19%)</td><td>363.50 (-3.35%)</td><td>335.58 (-2.50%)</td><td>337.10 (-1.72%)</td><td>303.10 (-6.25%)</td><td>22.04 (+1.66%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.97 (n/a)</td><td>12.22 (n/a)</td><td>12.23 (n/a)</td><td>11.15 (n/a)</td><td>0.75 (n/a)</td><td>376.10 (n/a)</td><td>344.20 (n/a)</td><td>343.00 (n/a)</td><td>323.30 (n/a)</td><td>21.68 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>12.81 (-7.71%)</td><td>12.04 (-5.08%)</td><td>12.50 (-0.47%)</td><td>10.75 (-3.85%)</td><td>0.87 (-14.08%)</td><td>390.30 (+4.00%)</td><td>349.84 (+5.26%)</td><td>335.70 (+0.48%)</td><td>327.40 (+8.37%)</td><td>26.42 (-4.01%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.88 (n/a)</td><td>12.69 (n/a)</td><td>12.55 (n/a)</td><td>11.18 (n/a)</td><td>1.01 (n/a)</td><td>375.30 (n/a)</td><td>332.36 (n/a)</td><td>334.10 (n/a)</td><td>302.10 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.03 (+4.71%)</td><td>12.69 (-1.78%)</td><td>12.73 (-0.59%)</td><td>11.67 (-7.59%)</td><td>0.96 <b>(+193.95%)</b></td><td>359.30 (+8.22%)</td><td>331.98 (+2.23%)</td><td>329.60 (+0.61%)</td><td>298.90 (-4.50%)</td><td>24.74 <b>(+205.84%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>13.40 (n/a)</td><td>12.92 (n/a)</td><td>12.80 (n/a)</td><td>12.63 (n/a)</td><td>0.33 (n/a)</td><td>332.00 (n/a)</td><td>324.74 (n/a)</td><td>327.60 (n/a)</td><td>313.00 (n/a)</td><td>8.09 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.39 (+12.52%)</td><td>13.71 (+16.79%)</td><td>13.88 (+15.76%)</td><td>12.74 <b>(+34.43%)</b></td><td>0.61 <b>(-53.50%)</b></td><td>329.20 <b>(-25.60%)</b></td><td>306.48 (-15.22%)</td><td>302.10 (-13.64%)</td><td>291.40 (-11.13%)</td><td>14.15 <b>(-69.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>12.79 (n/a)</td><td>11.74 (n/a)</td><td>11.99 (n/a)</td><td>9.48 (n/a)</td><td>1.32 (n/a)</td><td>442.50 (n/a)</td><td>361.52 (n/a)</td><td>349.80 (n/a)</td><td>327.90 (n/a)</td><td>46.49 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>14.11 (-2.26%)</td><td>12.59 (-3.03%)</td><td>13.07 (+2.76%)</td><td>9.99 (-15.68%)</td><td>1.65 <b>(+70.45%)</b></td><td>419.70 (+18.59%)</td><td>338.34 (+4.27%)</td><td>320.80 (-2.70%)</td><td>297.20 (+2.31%)</td><td>49.50 <b>(+109.92%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>14.44 (n/a)</td><td>12.98 (n/a)</td><td>12.72 (n/a)</td><td>11.85 (n/a)</td><td>0.97 (n/a)</td><td>353.90 (n/a)</td><td>324.50 (n/a)</td><td>329.70 (n/a)</td><td>290.50 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.44 (-5.51%)</td><td>3.00 (-5.69%)</td><td>2.93 (-9.38%)</td><td>2.71 (+7.42%)</td><td>0.30 <b>(-32.05%)</b></td><td>193.20 (-6.89%)</td><td>176.18 (+5.09%)</td><td>179.20 (+10.41%)</td><td>152.30 (+5.84%)</td><td>16.59 <b>(-33.59%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.64 (n/a)</td><td>3.18 (n/a)</td><td>3.23 (n/a)</td><td>2.53 (n/a)</td><td>0.44 (n/a)</td><td>207.50 (n/a)</td><td>167.64 (n/a)</td><td>162.30 (n/a)</td><td>143.90 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>5.77 (-1.23%)</td><td>5.31 (+4.55%)</td><td>5.70 (+17.30%)</td><td>3.98 (-9.51%)</td><td>0.76 <b>(+26.70%)</b></td><td>263.10 (+10.50%)</td><td>201.54 (-3.50%)</td><td>184.10 (-14.77%)</td><td>181.60 (+1.23%)</td><td>34.96 <b>(+44.35%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>5.84 (n/a)</td><td>5.08 (n/a)</td><td>4.86 (n/a)</td><td>4.40 (n/a)</td><td>0.60 (n/a)</td><td>238.10 (n/a)</td><td>208.84 (n/a)</td><td>216.00 (n/a)</td><td>179.40 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>8.83 (+8.94%)</td><td>7.73 (+2.71%)</td><td>7.83 (+5.79%)</td><td>6.99 (-2.85%)</td><td>0.77 <b>(+120.37%)</b></td><td>299.90 (+2.92%)</td><td>273.40 (-2.05%)</td><td>267.80 (-5.50%)</td><td>237.50 (-8.19%)</td><td>26.69 <b>(+113.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>8.11 (n/a)</td><td>7.53 (n/a)</td><td>7.40 (n/a)</td><td>7.20 (n/a)</td><td>0.35 (n/a)</td><td>291.40 (n/a)</td><td>279.12 (n/a)</td><td>283.40 (n/a)</td><td>258.70 (n/a)</td><td>12.50 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>3.61 (+3.88%)</td><td>2.85 (-5.75%)</td><td>2.69 (-19.29%)</td><td>2.32 (+6.28%)</td><td>0.51 (-9.71%)</td><td>226.50 (-5.90%)</td><td>188.74 (+5.21%)</td><td>195.20 <b>(+23.94%)</b></td><td>145.20 (-3.78%)</td><td>31.84 (-17.70%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>3.48 (n/a)</td><td>3.02 (n/a)</td><td>3.33 (n/a)</td><td>2.18 (n/a)</td><td>0.57 (n/a)</td><td>240.70 (n/a)</td><td>179.40 (n/a)</td><td>157.50 (n/a)</td><td>150.90 (n/a)</td><td>38.69 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.31 (+16.10%)</td><td>0.21 (+18.62%)</td><td>0.19 (+10.85%)</td><td>0.16 <b>(+25.79%)</b></td><td>0.06 (+10.58%)</td><td>198.60 <b>(-20.53%)</b></td><td>164.64 (-16.44%)</td><td>173.00 (-9.80%)</td><td>105.30 (-13.83%)</td><td>38.00 <b>(-23.56%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>249.90 (n/a)</td><td>197.04 (n/a)</td><td>191.80 (n/a)</td><td>122.20 (n/a)</td><td>49.71 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.23 (-10.88%)</td><td>0.20 (+10.24%)</td><td>0.22 (+13.57%)</td><td>0.16 <b>(+56.47%)</b></td><td>0.03 <b>(-51.14%)</b></td><td>203.90 <b>(-36.10%)</b></td><td>167.90 (-17.44%)</td><td>151.20 (-11.94%)</td><td>142.40 (+12.21%)</td><td>27.96 <b>(-65.10%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>319.10 (n/a)</td><td>203.36 (n/a)</td><td>171.70 (n/a)</td><td>126.90 (n/a)</td><td>80.11 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.48 (-10.13%)</td><td>0.39 (-10.05%)</td><td>0.37 (-9.99%)</td><td>0.30 (-16.66%)</td><td>0.07 (+10.15%)</td><td>221.20 (+19.96%)</td><td>174.60 (+12.34%)</td><td>176.60 (+11.07%)</td><td>137.60 (+11.24%)</td><td>32.61 <b>(+48.40%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>184.40 (n/a)</td><td>155.42 (n/a)</td><td>159.00 (n/a)</td><td>123.70 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.44 (-3.68%)</td><td>0.37 (-10.10%)</td><td>0.37 (-12.74%)</td><td>0.32 (-11.83%)</td><td>0.05 <b>(+31.94%)</b></td><td>203.10 (+13.40%)</td><td>178.56 (+12.06%)</td><td>175.10 (+14.59%)</td><td>148.40 (+3.85%)</td><td>23.71 <b>(+57.51%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>179.10 (n/a)</td><td>159.34 (n/a)</td><td>152.80 (n/a)</td><td>142.90 (n/a)</td><td>15.06 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.53 <b>(+21.97%)</b></td><td>0.40 (+0.91%)</td><td>0.37 (-9.20%)</td><td>0.28 (-19.13%)</td><td>0.09 <b>(+211.05%)</b></td><td>230.70 <b>(+23.63%)</b></td><td>170.36 (+3.17%)</td><td>177.40 (+10.12%)</td><td>124.10 (-17.98%)</td><td>40.95 <b>(+208.69%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>186.60 (n/a)</td><td>165.12 (n/a)</td><td>161.10 (n/a)</td><td>151.30 (n/a)</td><td>13.27 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.01 (+1.27%)</td><td>0.88 (-0.66%)</td><td>0.98 (+6.00%)</td><td>0.68 (-6.85%)</td><td>0.15 <b>(+52.66%)</b></td><td>191.80 (+7.39%)</td><td>152.82 (+2.25%)</td><td>133.30 (-5.66%)</td><td>130.40 (-1.21%)</td><td>28.86 <b>(+57.37%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.99 (n/a)</td><td>0.89 (n/a)</td><td>0.93 (n/a)</td><td>0.73 (n/a)</td><td>0.10 (n/a)</td><td>178.60 (n/a)</td><td>149.46 (n/a)</td><td>141.30 (n/a)</td><td>132.00 (n/a)</td><td>18.34 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.91 (+7.20%)</td><td>0.74 (-2.85%)</td><td>0.75 (-7.91%)</td><td>0.64 (+2.65%)</td><td>0.11 (+15.25%)</td><td>205.00 (-2.57%)</td><td>178.94 (+3.19%)</td><td>174.80 (+8.57%)</td><td>143.30 (-6.77%)</td><td>24.43 (+4.66%)</td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.81 (n/a)</td><td>0.62 (n/a)</td><td>0.09 (n/a)</td><td>210.40 (n/a)</td><td>173.40 (n/a)</td><td>161.00 (n/a)</td><td>153.70 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.78 <b>(-24.46%)</b></td><td>0.69 <b>(-21.22%)</b></td><td>0.73 (-13.53%)</td><td>0.53 <b>(-29.38%)</b></td><td>0.10 <b>(-21.13%)</b></td><td>249.40 <b>(+41.62%)</b></td><td>194.20 <b>(+27.34%)</b></td><td>180.20 (+15.66%)</td><td>167.60 <b>(+32.39%)</b></td><td>32.53 <b>(+51.50%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>1.04 (n/a)</td><td>0.87 (n/a)</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.13 (n/a)</td><td>176.10 (n/a)</td><td>152.50 (n/a)</td><td>155.80 (n/a)</td><td>126.60 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>1.01 (+7.85%)</td><td>0.87 (+10.66%)</td><td>0.88 (+3.55%)</td><td>0.65 <b>(+27.82%)</b></td><td>0.15 (-10.73%)</td><td>202.90 <b>(-21.75%)</b></td><td>155.26 (-11.51%)</td><td>149.40 (-3.43%)</td><td>130.30 (-7.26%)</td><td>29.80 <b>(-38.25%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.85 (n/a)</td><td>0.51 (n/a)</td><td>0.17 (n/a)</td><td>259.30 (n/a)</td><td>175.46 (n/a)</td><td>154.70 (n/a)</td><td>140.50 (n/a)</td><td>48.26 (n/a)</td>
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
<td><code>2fadeda</code> — 2026-07-24 02:27:00</td><td>0.15 <b>(+39.36%)</b></td><td>0.11 <b>(+21.68%)</b></td><td>0.10 (+6.99%)</td><td>0.09 <b>(+26.42%)</b></td><td>0.02 <b>(+32.43%)</b></td><td>190.10 <b>(-20.89%)</b></td><td>159.24 (-18.01%)</td><td>166.50 (-6.51%)</td><td>112.90 <b>(-28.27%)</b></td><td>28.35 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>8bdb3ed</code> — 2026-07-23 21:46:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.30 (n/a)</td><td>194.22 (n/a)</td><td>178.10 (n/a)</td><td>157.40 (n/a)</td><td>39.97 (n/a)</td>
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
