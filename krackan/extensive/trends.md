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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-20.74%)</b></td><td>0.03 (-15.64%)</td><td>0.03 (-15.30%)</td><td>0.03 (-13.91%)</td><td>0.00 <b>(-40.47%)</b></td><td>193.50 (+16.15%)</td><td>177.78 (+17.78%)</td><td>181.50 (+18.09%)</td><td>151.30 <b>(+26.19%)</b></td><td>15.95 (-12.45%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>166.60 (n/a)</td><td>150.94 (n/a)</td><td>153.70 (n/a)</td><td>119.90 (n/a)</td><td>18.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-1.13%)</td><td>0.03 (-15.73%)</td><td>0.03 <b>(-24.83%)</b></td><td>0.03 (-19.69%)</td><td>0.01 <b>(+46.66%)</b></td><td>212.10 <b>(+24.47%)</b></td><td>179.74 <b>(+20.34%)</b></td><td>190.10 <b>(+33.03%)</b></td><td>135.90 (+1.12%)</td><td>28.62 <b>(+80.27%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>170.40 (n/a)</td><td>149.36 (n/a)</td><td>142.90 (n/a)</td><td>134.40 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-23.47%)</b></td><td>0.03 <b>(-37.60%)</b></td><td>0.03 <b>(-42.45%)</b></td><td>0.02 <b>(-38.88%)</b></td><td>0.01 (-1.66%)</td><td>265.60 <b>(+63.65%)</b></td><td>205.70 <b>(+62.94%)</b></td><td>208.20 <b>(+73.79%)</b></td><td>149.20 <b>(+30.76%)</b></td><td>41.47 <b>(+103.79%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>162.30 (n/a)</td><td>126.24 (n/a)</td><td>119.80 (n/a)</td><td>114.10 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-20.40%)</b></td><td>0.03 (-14.87%)</td><td>0.03 (-17.05%)</td><td>0.03 <b>(+65.20%)</b></td><td>0.01 <b>(-48.85%)</b></td><td>229.30 <b>(-39.45%)</b></td><td>184.52 (+0.28%)</td><td>178.20 <b>(+20.57%)</b></td><td>127.60 <b>(+25.59%)</b></td><td>38.87 <b>(-65.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>378.70 (n/a)</td><td>184.00 (n/a)</td><td>147.80 (n/a)</td><td>101.60 (n/a)</td><td>111.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-23.65%)</b></td><td>0.03 <b>(-24.51%)</b></td><td>0.03 <b>(-28.97%)</b></td><td>0.02 <b>(-25.81%)</b></td><td>0.01 <b>(-28.95%)</b></td><td>287.90 <b>(+34.78%)</b></td><td>206.42 <b>(+30.93%)</b></td><td>186.50 <b>(+40.75%)</b></td><td>137.70 <b>(+31.02%)</b></td><td>58.33 (+19.82%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>157.66 (n/a)</td><td>132.50 (n/a)</td><td>105.10 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-29.67%)</b></td><td>0.03 <b>(-25.68%)</b></td><td>0.04 <b>(-25.07%)</b></td><td>0.03 <b>(-24.75%)</b></td><td>0.00 <b>(-41.81%)</b></td><td>217.10 <b>(+32.86%)</b></td><td>181.48 <b>(+33.78%)</b></td><td>174.30 <b>(+33.46%)</b></td><td>164.90 <b>(+42.16%)</b></td><td>21.58 (+10.10%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>163.40 (n/a)</td><td>135.66 (n/a)</td><td>130.60 (n/a)</td><td>116.00 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-50.72%)</b></td><td>0.03 <b>(-38.83%)</b></td><td>0.03 <b>(-45.84%)</b></td><td>0.03 (-17.72%)</td><td>0.00 <b>(-91.44%)</b></td><td>222.00 <b>(+21.51%)</b></td><td>208.98 <b>(+52.87%)</b></td><td>208.50 <b>(+84.51%)</b></td><td>199.80 <b>(+102.84%)</b></td><td>8.26 <b>(-79.77%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>136.70 (n/a)</td><td>113.00 (n/a)</td><td>98.50 (n/a)</td><td>40.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-49.45%)</b></td><td>0.03 (-18.61%)</td><td>0.03 <b>(-34.50%)</b></td><td>0.03 <b>(+327.90%)</b></td><td>0.00 <b>(-93.97%)</b></td><td>239.30 <b>(-76.63%)</b></td><td>226.38 <b>(-52.25%)</b></td><td>229.30 <b>(+52.66%)</b></td><td>210.60 <b>(+97.93%)</b></td><td>12.76 <b>(-97.36%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1023.90 (n/a)</td><td>474.14 (n/a)</td><td>150.20 (n/a)</td><td>106.40 (n/a)</td><td>482.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-27.95%)</b></td><td>0.06 <b>(-35.54%)</b></td><td>0.06 <b>(-36.05%)</b></td><td>0.05 <b>(-44.77%)</b></td><td>0.01 <b>(+47.51%)</b></td><td>241.90 <b>(+81.06%)</b></td><td>193.60 <b>(+57.73%)</b></td><td>189.90 <b>(+56.30%)</b></td><td>156.40 <b>(+38.78%)</b></td><td>31.52 <b>(+273.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>133.60 (n/a)</td><td>122.74 (n/a)</td><td>121.50 (n/a)</td><td>112.70 (n/a)</td><td>8.43 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-44.04%)</b></td><td>0.07 <b>(-40.14%)</b></td><td>0.07 <b>(-38.79%)</b></td><td>0.06 <b>(-40.56%)</b></td><td>0.01 <b>(-51.47%)</b></td><td>221.90 <b>(+68.23%)</b></td><td>189.60 <b>(+66.32%)</b></td><td>187.50 <b>(+63.47%)</b></td><td>161.60 <b>(+78.56%)</b></td><td>23.06 <b>(+48.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>131.90 (n/a)</td><td>114.00 (n/a)</td><td>114.70 (n/a)</td><td>90.50 (n/a)</td><td>15.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-34.11%)</b></td><td>0.07 <b>(-32.22%)</b></td><td>0.07 <b>(-33.81%)</b></td><td>0.06 <b>(-20.09%)</b></td><td>0.01 <b>(-59.53%)</b></td><td>208.20 <b>(+25.12%)</b></td><td>176.18 <b>(+44.15%)</b></td><td>175.30 <b>(+51.12%)</b></td><td>150.90 <b>(+51.66%)</b></td><td>20.87 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>166.40 (n/a)</td><td>122.22 (n/a)</td><td>116.00 (n/a)</td><td>99.50 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 <b>(-38.23%)</b></td><td>0.08 <b>(-31.23%)</b></td><td>0.07 <b>(-26.50%)</b></td><td>0.06 <b>(-29.29%)</b></td><td>0.01 <b>(-53.33%)</b></td><td>192.00 <b>(+41.38%)</b></td><td>166.32 <b>(+43.33%)</b></td><td>166.80 <b>(+36.05%)</b></td><td>134.80 <b>(+61.82%)</b></td><td>22.28 (+9.39%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>135.80 (n/a)</td><td>116.04 (n/a)</td><td>122.60 (n/a)</td><td>83.30 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 <b>(-27.56%)</b></td><td>0.07 <b>(-35.93%)</b></td><td>0.07 <b>(-43.31%)</b></td><td>0.06 <b>(-21.93%)</b></td><td>0.01 <b>(-41.35%)</b></td><td>219.80 <b>(+28.09%)</b></td><td>187.08 <b>(+53.55%)</b></td><td>187.00 <b>(+76.42%)</b></td><td>138.80 <b>(+37.97%)</b></td><td>30.65 (+1.83%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>171.60 (n/a)</td><td>121.84 (n/a)</td><td>106.00 (n/a)</td><td>100.60 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 <b>(-42.61%)</b></td><td>0.06 <b>(-37.90%)</b></td><td>0.06 <b>(-39.34%)</b></td><td>0.05 <b>(-36.27%)</b></td><td>0.01 <b>(-56.88%)</b></td><td>242.30 <b>(+56.93%)</b></td><td>207.00 <b>(+59.11%)</b></td><td>209.20 <b>(+64.85%)</b></td><td>176.20 <b>(+74.28%)</b></td><td>25.52 (+15.59%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>154.40 (n/a)</td><td>130.10 (n/a)</td><td>126.90 (n/a)</td><td>101.10 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 <b>(-39.59%)</b></td><td>0.06 (-2.31%)</td><td>0.06 (-4.72%)</td><td>0.06 <b>(+369.28%)</b></td><td>0.01 <b>(-85.73%)</b></td><td>218.20 <b>(-78.69%)</b></td><td>200.24 <b>(-41.91%)</b></td><td>201.20 (+4.96%)</td><td>174.70 <b>(+65.59%)</b></td><td>16.24 <b>(-95.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1024.00 (n/a)</td><td>344.70 (n/a)</td><td>191.70 (n/a)</td><td>105.50 (n/a)</td><td>382.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-32.08%)</b></td><td>0.06 <b>(-29.69%)</b></td><td>0.06 (-11.77%)</td><td>0.03 <b>(-49.59%)</b></td><td>0.02 <b>(-27.91%)</b></td><td>361.80 <b>(+98.36%)</b></td><td>218.56 <b>(+46.72%)</b></td><td>189.90 (+13.37%)</td><td>146.70 <b>(+47.29%)</b></td><td>84.19 <b>(+117.22%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>182.40 (n/a)</td><td>148.96 (n/a)</td><td>167.50 (n/a)</td><td>99.60 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(-20.05%)</b></td><td>0.15 (-18.90%)</td><td>0.14 <b>(-20.56%)</b></td><td>0.13 (-8.41%)</td><td>0.01 <b>(-43.82%)</b></td><td>184.60 (+9.17%)</td><td>170.36 <b>(+22.21%)</b></td><td>172.70 <b>(+25.87%)</b></td><td>145.70 <b>(+25.06%)</b></td><td>14.68 <b>(-25.37%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>169.10 (n/a)</td><td>139.40 (n/a)</td><td>137.20 (n/a)</td><td>116.50 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 <b>(-30.07%)</b></td><td>0.14 (-15.97%)</td><td>0.14 (-7.84%)</td><td>0.11 (-4.49%)</td><td>0.03 <b>(-40.62%)</b></td><td>219.00 (+4.73%)</td><td>177.70 (+15.57%)</td><td>175.20 (+8.48%)</td><td>138.20 <b>(+43.06%)</b></td><td>38.41 (-8.64%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>209.10 (n/a)</td><td>153.76 (n/a)</td><td>161.50 (n/a)</td><td>96.60 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(-30.06%)</b></td><td>0.14 <b>(-27.35%)</b></td><td>0.14 <b>(-25.40%)</b></td><td>0.11 <b>(-28.70%)</b></td><td>0.03 (-15.71%)</td><td>217.40 <b>(+40.26%)</b></td><td>179.16 <b>(+39.03%)</b></td><td>173.90 <b>(+33.98%)</b></td><td>141.90 <b>(+42.90%)</b></td><td>35.04 <b>(+75.81%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>155.00 (n/a)</td><td>128.86 (n/a)</td><td>129.80 (n/a)</td><td>99.30 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(-32.41%)</b></td><td>0.13 <b>(-21.74%)</b></td><td>0.13 (-19.30%)</td><td>0.12 <b>(+148.54%)</b></td><td>0.02 <b>(-74.49%)</b></td><td>210.60 <b>(-59.77%)</b></td><td>187.04 (-10.13%)</td><td>196.40 <b>(+23.91%)</b></td><td>143.80 <b>(+47.94%)</b></td><td>25.98 <b>(-85.49%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.08 (n/a)</td><td>523.50 (n/a)</td><td>208.12 (n/a)</td><td>158.50 (n/a)</td><td>97.20 (n/a)</td><td>179.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(-34.74%)</b></td><td>0.13 <b>(-25.86%)</b></td><td>0.13 <b>(-20.84%)</b></td><td>0.11 (-15.83%)</td><td>0.02 <b>(-55.42%)</b></td><td>231.50 (+18.84%)</td><td>188.74 <b>(+29.47%)</b></td><td>186.00 <b>(+26.27%)</b></td><td>145.00 <b>(+53.28%)</b></td><td>32.14 (-18.99%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>194.80 (n/a)</td><td>145.78 (n/a)</td><td>147.30 (n/a)</td><td>94.60 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(-35.60%)</b></td><td>0.14 <b>(-38.79%)</b></td><td>0.14 <b>(-38.92%)</b></td><td>0.12 <b>(-41.16%)</b></td><td>0.02 <b>(-26.38%)</b></td><td>210.30 <b>(+70.01%)</b></td><td>175.70 <b>(+64.30%)</b></td><td>178.70 <b>(+63.64%)</b></td><td>144.90 <b>(+55.31%)</b></td><td>26.61 <b>(+97.50%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>123.70 (n/a)</td><td>106.94 (n/a)</td><td>109.20 (n/a)</td><td>93.30 (n/a)</td><td>13.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 <b>(-28.34%)</b></td><td>0.14 (-19.91%)</td><td>0.13 <b>(-22.10%)</b></td><td>0.11 (-2.29%)</td><td>0.03 <b>(-48.95%)</b></td><td>221.10 (+2.36%)</td><td>182.04 (+18.96%)</td><td>191.40 <b>(+28.37%)</b></td><td>131.50 <b>(+39.60%)</b></td><td>32.91 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>216.00 (n/a)</td><td>153.02 (n/a)</td><td>149.10 (n/a)</td><td>94.20 (n/a)</td><td>46.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 <b>(-49.93%)</b></td><td>0.11 <b>(-44.31%)</b></td><td>0.11 <b>(-41.17%)</b></td><td>0.08 <b>(-45.93%)</b></td><td>0.02 <b>(-52.32%)</b></td><td>320.80 <b>(+84.90%)</b></td><td>233.60 <b>(+78.89%)</b></td><td>217.60 <b>(+70.00%)</b></td><td>196.00 <b>(+99.80%)</b></td><td>49.72 <b>(+81.46%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>173.50 (n/a)</td><td>130.58 (n/a)</td><td>128.00 (n/a)</td><td>98.10 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.38 (-3.78%)</td><td>0.29 (-15.62%)</td><td>0.25 <b>(-24.92%)</b></td><td>0.23 (-19.60%)</td><td>0.07 <b>(+36.09%)</b></td><td>215.10 <b>(+24.41%)</b></td><td>176.64 <b>(+21.37%)</b></td><td>196.40 <b>(+33.24%)</b></td><td>128.50 (+3.88%)</td><td>38.02 <b>(+79.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>172.90 (n/a)</td><td>145.54 (n/a)</td><td>147.40 (n/a)</td><td>123.70 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 <b>(-33.72%)</b></td><td>0.27 <b>(-38.05%)</b></td><td>0.27 <b>(-42.36%)</b></td><td>0.21 <b>(-26.86%)</b></td><td>0.05 <b>(-43.57%)</b></td><td>229.40 <b>(+36.71%)</b></td><td>188.92 <b>(+59.29%)</b></td><td>181.10 <b>(+73.47%)</b></td><td>147.20 <b>(+50.97%)</b></td><td>34.41 (+17.73%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>167.80 (n/a)</td><td>118.60 (n/a)</td><td>104.40 (n/a)</td><td>97.50 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 <b>(-33.58%)</b></td><td>0.28 <b>(-33.50%)</b></td><td>0.27 <b>(-30.92%)</b></td><td>0.24 <b>(-30.99%)</b></td><td>0.04 <b>(-45.16%)</b></td><td>203.40 <b>(+44.87%)</b></td><td>178.24 <b>(+49.35%)</b></td><td>183.60 <b>(+44.79%)</b></td><td>147.10 <b>(+50.56%)</b></td><td>22.60 <b>(+21.30%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>140.40 (n/a)</td><td>119.34 (n/a)</td><td>126.80 (n/a)</td><td>97.70 (n/a)</td><td>18.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 <b>(-41.16%)</b></td><td>0.27 <b>(-36.61%)</b></td><td>0.26 <b>(-36.48%)</b></td><td>0.24 <b>(-20.94%)</b></td><td>0.03 <b>(-64.38%)</b></td><td>207.60 <b>(+26.51%)</b></td><td>185.70 <b>(+53.42%)</b></td><td>189.80 <b>(+57.51%)</b></td><td>162.90 <b>(+70.04%)</b></td><td>21.67 <b>(-22.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>164.10 (n/a)</td><td>121.04 (n/a)</td><td>120.50 (n/a)</td><td>95.80 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.33 <b>(-25.84%)</b></td><td>0.27 <b>(-32.29%)</b></td><td>0.27 <b>(-32.04%)</b></td><td>0.23 <b>(-32.74%)</b></td><td>0.04 (+8.15%)</td><td>217.80 <b>(+48.67%)</b></td><td>187.88 <b>(+49.32%)</b></td><td>181.60 <b>(+47.16%)</b></td><td>149.10 <b>(+34.81%)</b></td><td>28.43 <b>(+117.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.04 (n/a)</td><td>146.50 (n/a)</td><td>125.82 (n/a)</td><td>123.40 (n/a)</td><td>110.60 (n/a)</td><td>13.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 <b>(-44.42%)</b></td><td>0.27 <b>(-26.26%)</b></td><td>0.27 <b>(-27.91%)</b></td><td>0.26 (+10.16%)</td><td>0.02 <b>(-86.25%)</b></td><td>189.70 (-9.19%)</td><td>180.32 <b>(+25.33%)</b></td><td>182.80 <b>(+38.69%)</b></td><td>163.10 <b>(+79.82%)</b></td><td>10.10 <b>(-77.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>208.90 (n/a)</td><td>143.88 (n/a)</td><td>131.80 (n/a)</td><td>90.70 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.36 <b>(-29.16%)</b></td><td>0.26 <b>(-28.56%)</b></td><td>0.24 (-15.83%)</td><td>0.21 (-13.41%)</td><td>0.06 <b>(-55.40%)</b></td><td>229.40 (+15.45%)</td><td>196.14 <b>(+31.85%)</b></td><td>204.10 (+18.80%)</td><td>138.40 <b>(+41.22%)</b></td><td>34.54 <b>(-26.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>198.70 (n/a)</td><td>148.76 (n/a)</td><td>171.80 (n/a)</td><td>98.00 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.34 <b>(-25.16%)</b></td><td>0.26 <b>(-27.94%)</b></td><td>0.22 <b>(-43.81%)</b></td><td>0.22 (-0.36%)</td><td>0.06 <b>(-43.91%)</b></td><td>222.80 (+0.36%)</td><td>194.74 <b>(+33.20%)</b></td><td>220.90 <b>(+78.00%)</b></td><td>143.30 <b>(+33.68%)</b></td><td>38.03 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>222.00 (n/a)</td><td>146.20 (n/a)</td><td>124.10 (n/a)</td><td>107.20 (n/a)</td><td>48.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-24.78%)</b></td><td>0.02 <b>(-31.04%)</b></td><td>0.01 <b>(-41.44%)</b></td><td>0.01 (-1.55%)</td><td>0.01 <b>(-33.72%)</b></td><td>220.60 (+1.57%)</td><td>173.48 <b>(+38.17%)</b></td><td>201.50 <b>(+70.76%)</b></td><td>102.50 <b>(+32.94%)</b></td><td>50.74 (-9.24%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>125.56 (n/a)</td><td>118.00 (n/a)</td><td>77.10 (n/a)</td><td>55.90 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-39.24%)</b></td><td>0.02 <b>(-20.03%)</b></td><td>0.02 (-19.97%)</td><td>0.01 <b>(+1168.21%)</b></td><td>0.00 <b>(-73.12%)</b></td><td>227.00 <b>(-92.11%)</b></td><td>177.26 <b>(-73.49%)</b></td><td>160.70 <b>(+24.96%)</b></td><td>142.30 <b>(+64.70%)</b></td><td>37.97 <b>(-96.93%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2878.60 (n/a)</td><td>668.68 (n/a)</td><td>128.60 (n/a)</td><td>86.40 (n/a)</td><td>1235.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-48.80%)</b></td><td>0.02 <b>(-39.19%)</b></td><td>0.02 <b>(-42.54%)</b></td><td>0.01 <b>(+26.70%)</b></td><td>0.00 <b>(-80.37%)</b></td><td>202.90 <b>(-21.05%)</b></td><td>176.38 <b>(+40.07%)</b></td><td>168.00 <b>(+74.09%)</b></td><td>159.20 <b>(+95.34%)</b></td><td>20.17 <b>(-72.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>257.00 (n/a)</td><td>125.92 (n/a)</td><td>96.50 (n/a)</td><td>81.50 (n/a)</td><td>73.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (+16.54%)</td><td>0.02 (+19.80%)</td><td>0.02 <b>(+28.19%)</b></td><td>0.01 <b>(+25.24%)</b></td><td>0.00 (+9.39%)</td><td>211.70 <b>(-20.14%)</b></td><td>164.76 (-17.02%)</td><td>150.30 <b>(-22.00%)</b></td><td>134.60 (-14.16%)</td><td>33.64 <b>(-24.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>265.10 (n/a)</td><td>198.56 (n/a)</td><td>192.70 (n/a)</td><td>156.80 (n/a)</td><td>44.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (-17.24%)</td><td>0.02 (+9.80%)</td><td>0.02 (+11.58%)</td><td>0.01 <b>(+606.35%)</b></td><td>0.00 <b>(-57.54%)</b></td><td>203.10 <b>(-85.84%)</b></td><td>162.58 <b>(-59.81%)</b></td><td>144.20 (-10.38%)</td><td>123.10 <b>(+20.80%)</b></td><td>36.74 <b>(-93.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1434.60 (n/a)</td><td>404.52 (n/a)</td><td>160.90 (n/a)</td><td>101.90 (n/a)</td><td>576.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-23.40%)</b></td><td>0.02 (-3.45%)</td><td>0.01 (-4.82%)</td><td>0.01 <b>(+20.02%)</b></td><td>0.00 <b>(-57.51%)</b></td><td>191.50 (-16.70%)</td><td>168.60 (-2.73%)</td><td>176.20 (+5.07%)</td><td>141.00 <b>(+30.56%)</b></td><td>23.11 <b>(-55.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>173.34 (n/a)</td><td>167.70 (n/a)</td><td>108.00 (n/a)</td><td>51.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-33.42%)</b></td><td>0.01 (+13.56%)</td><td>0.02 (+15.05%)</td><td>0.01 <b>(+22432.15%)</b></td><td>0.00 <b>(-80.56%)</b></td><td>215.90 <b>(-99.56%)</b></td><td>182.24 <b>(-98.82%)</b></td><td>172.50 (-13.05%)</td><td>142.70 <b>(+50.21%)</b></td><td>29.94 <b>(-99.86%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>48658.20 (n/a)</td><td>15414.24 (n/a)</td><td>198.40 (n/a)</td><td>95.00 (n/a)</td><td>22159.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-26.56%)</b></td><td>0.01 (-19.07%)</td><td>0.01 (-17.22%)</td><td>0.01 (-4.59%)</td><td>0.00 <b>(-46.44%)</b></td><td>268.50 (+4.80%)</td><td>216.72 (+19.64%)</td><td>216.10 <b>(+20.79%)</b></td><td>166.20 <b>(+36.23%)</b></td><td>36.25 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>256.20 (n/a)</td><td>181.14 (n/a)</td><td>178.90 (n/a)</td><td>122.00 (n/a)</td><td>48.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-32.22%)</b></td><td>0.03 (-5.97%)</td><td>0.03 (-18.45%)</td><td>0.03 <b>(+73191.12%)</b></td><td>0.00 <b>(-81.23%)</b></td><td>177.40 <b>(-99.86%)</b></td><td>158.22 <b>(-99.39%)</b></td><td>164.30 <b>(+22.61%)</b></td><td>131.40 <b>(+47.64%)</b></td><td>18.58 <b>(-99.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>130045.60 (n/a)</td><td>26108.38 (n/a)</td><td>134.00 (n/a)</td><td>89.00 (n/a)</td><td>58102.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-3.23%)</td><td>0.03 (-8.46%)</td><td>0.03 <b>(-24.80%)</b></td><td>0.03 (+11.72%)</td><td>0.01 <b>(-33.03%)</b></td><td>185.10 (-10.49%)</td><td>157.94 (+4.90%)</td><td>161.30 <b>(+32.98%)</b></td><td>115.50 (+3.31%)</td><td>27.68 <b>(-39.36%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>150.56 (n/a)</td><td>121.30 (n/a)</td><td>111.80 (n/a)</td><td>45.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-22.36%)</b></td><td>0.04 (-3.52%)</td><td>0.04 (-7.59%)</td><td>0.02 <b>(+62125.06%)</b></td><td>0.01 <b>(-65.53%)</b></td><td>215.00 <b>(-99.84%)</b></td><td>156.18 <b>(-99.42%)</b></td><td>136.50 (+8.16%)</td><td>120.90 <b>(+28.89%)</b></td><td>38.79 <b>(-99.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>133788.90 (n/a)</td><td>26854.94 (n/a)</td><td>126.20 (n/a)</td><td>93.80 (n/a)</td><td>59777.91 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (+9.72%)</td><td>0.03 (+7.50%)</td><td>0.03 (-12.74%)</td><td>0.03 <b>(+32.04%)</b></td><td>0.01 (-19.24%)</td><td>182.20 <b>(-24.27%)</b></td><td>158.76 (-9.39%)</td><td>170.60 (+14.57%)</td><td>123.80 (-8.84%)</td><td>25.48 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>175.22 (n/a)</td><td>148.90 (n/a)</td><td>135.80 (n/a)</td><td>45.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (-13.28%)</td><td>0.03 (+9.46%)</td><td>0.03 (+6.94%)</td><td>0.02 <b>(+1666.10%)</b></td><td>0.01 <b>(-55.68%)</b></td><td>228.40 <b>(-94.34%)</b></td><td>172.96 <b>(-81.49%)</b></td><td>159.50 (-6.45%)</td><td>117.10 (+15.37%)</td><td>43.20 <b>(-97.51%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>4033.50 (n/a)</td><td>934.30 (n/a)</td><td>170.50 (n/a)</td><td>101.50 (n/a)</td><td>1733.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (+15.68%)</td><td>0.03 (+7.94%)</td><td>0.03 (-12.38%)</td><td>0.02 <b>(+6308.41%)</b></td><td>0.01 <b>(-31.50%)</b></td><td>257.60 <b>(-98.44%)</b></td><td>186.86 <b>(-94.54%)</b></td><td>183.10 (+14.15%)</td><td>105.80 (-13.49%)</td><td>57.40 <b>(-99.22%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>16505.40 (n/a)</td><td>3421.74 (n/a)</td><td>160.40 (n/a)</td><td>122.30 (n/a)</td><td>7314.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-15.59%)</td><td>0.03 <b>(+52.34%)</b></td><td>0.03 (+11.96%)</td><td>0.02 <b>(+1658.67%)</b></td><td>0.00 <b>(-81.59%)</b></td><td>210.90 <b>(-94.31%)</b></td><td>181.40 <b>(-88.12%)</b></td><td>174.10 (-10.67%)</td><td>160.70 (+18.42%)</td><td>20.12 <b>(-98.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>3708.70 (n/a)</td><td>1527.38 (n/a)</td><td>194.90 (n/a)</td><td>135.70 (n/a)</td><td>1856.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-21.69%)</b></td><td>0.03 <b>(+20.90%)</b></td><td>0.03 <b>(+25.80%)</b></td><td>0.02 <b>(+21186.18%)</b></td><td>0.00 <b>(-74.52%)</b></td><td>238.40 <b>(-99.53%)</b></td><td>206.30 <b>(-98.00%)</b></td><td>198.20 <b>(-20.50%)</b></td><td>175.80 <b>(+27.67%)</b></td><td>28.69 <b>(-99.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>50736.30 (n/a)</td><td>10314.66 (n/a)</td><td>249.30 (n/a)</td><td>137.70 (n/a)</td><td>22596.43 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-24.64%)</b></td><td>0.07 (+18.35%)</td><td>0.07 (+4.21%)</td><td>0.05 <b>(+599.38%)</b></td><td>0.01 <b>(-75.86%)</b></td><td>193.80 <b>(-85.70%)</b></td><td>161.82 <b>(-71.60%)</b></td><td>160.20 (-4.01%)</td><td>130.60 <b>(+32.59%)</b></td><td>27.02 <b>(-95.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>1355.30 (n/a)</td><td>569.86 (n/a)</td><td>166.90 (n/a)</td><td>98.50 (n/a)</td><td>614.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-43.20%)</b></td><td>0.06 (-9.10%)</td><td>0.06 <b>(-34.12%)</b></td><td>0.05 <b>(+1201.75%)</b></td><td>0.01 <b>(-81.62%)</b></td><td>208.70 <b>(-92.32%)</b></td><td>175.54 <b>(-79.47%)</b></td><td>187.60 <b>(+51.78%)</b></td><td>138.00 <b>(+76.02%)</b></td><td>29.21 <b>(-97.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>0.06 (n/a)</td><td>2717.10 (n/a)</td><td>855.16 (n/a)</td><td>123.60 (n/a)</td><td>78.40 (n/a)</td><td>1155.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 <b>(-27.66%)</b></td><td>0.06 (-18.48%)</td><td>0.06 <b>(-28.41%)</b></td><td>0.05 <b>(+28881.76%)</b></td><td>0.02 <b>(-67.28%)</b></td><td>212.00 <b>(-99.65%)</b></td><td>172.88 <b>(-98.60%)</b></td><td>174.40 <b>(+39.63%)</b></td><td>118.30 <b>(+38.20%)</b></td><td>35.90 <b>(-99.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>0.05 (n/a)</td><td>61448.00 (n/a)</td><td>12379.34 (n/a)</td><td>124.90 (n/a)</td><td>85.60 (n/a)</td><td>27430.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 <b>(-37.47%)</b></td><td>0.06 (+2.56%)</td><td>0.06 (+8.74%)</td><td>0.06 <b>(+1735.56%)</b></td><td>0.00 <b>(-94.39%)</b></td><td>173.10 <b>(-94.55%)</b></td><td>165.80 <b>(-78.01%)</b></td><td>167.80 (-8.05%)</td><td>158.70 <b>(+59.98%)</b></td><td>5.69 <b>(-99.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>0.04 (n/a)</td><td>3178.30 (n/a)</td><td>754.14 (n/a)</td><td>182.50 (n/a)</td><td>99.20 (n/a)</td><td>1355.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 <b>(-43.26%)</b></td><td>0.06 <b>(-35.34%)</b></td><td>0.06 <b>(-22.38%)</b></td><td>0.05 <b>(-29.21%)</b></td><td>0.01 <b>(-68.84%)</b></td><td>204.90 <b>(+41.31%)</b></td><td>175.74 <b>(+49.46%)</b></td><td>170.80 <b>(+28.81%)</b></td><td>154.30 <b>(+76.14%)</b></td><td>21.41 <b>(-20.11%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>145.00 (n/a)</td><td>117.58 (n/a)</td><td>132.60 (n/a)</td><td>87.60 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (-8.54%)</td><td>0.07 (+6.14%)</td><td>0.07 (-6.02%)</td><td>0.05 <b>(+2095.33%)</b></td><td>0.02 <b>(-62.21%)</b></td><td>197.60 <b>(-95.45%)</b></td><td>152.28 <b>(-84.35%)</b></td><td>146.10 (+6.41%)</td><td>112.00 (+9.37%)</td><td>31.86 <b>(-98.31%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>0.04 (n/a)</td><td>4338.80 (n/a)</td><td>972.96 (n/a)</td><td>137.30 (n/a)</td><td>102.40 (n/a)</td><td>1881.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 <b>(-29.68%)</b></td><td>0.06 (-7.86%)</td><td>0.06 (-0.98%)</td><td>0.06 (+18.18%)</td><td>0.00 <b>(-77.69%)</b></td><td>184.90 (-15.38%)</td><td>167.86 (+2.13%)</td><td>168.30 (+1.02%)</td><td>152.40 <b>(+42.16%)</b></td><td>12.05 <b>(-73.04%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>218.50 (n/a)</td><td>164.36 (n/a)</td><td>166.60 (n/a)</td><td>107.20 (n/a)</td><td>44.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (-16.82%)</td><td>0.05 (-2.20%)</td><td>0.05 <b>(-22.10%)</b></td><td>0.04 <b>(+1526.21%)</b></td><td>0.01 <b>(-60.93%)</b></td><td>239.00 <b>(-93.85%)</b></td><td>206.06 <b>(-77.27%)</b></td><td>227.10 <b>(+28.38%)</b></td><td>144.70 <b>(+20.28%)</b></td><td>40.70 <b>(-97.56%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>3886.40 (n/a)</td><td>906.74 (n/a)</td><td>176.90 (n/a)</td><td>120.30 (n/a)</td><td>1665.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (-10.75%)</td><td>0.13 <b>(-22.39%)</b></td><td>0.13 <b>(-30.93%)</b></td><td>0.10 (+5.85%)</td><td>0.03 <b>(-27.18%)</b></td><td>220.40 (-5.57%)</td><td>166.20 <b>(+23.53%)</b></td><td>166.70 <b>(+44.83%)</b></td><td>117.10 (+12.06%)</td><td>41.23 <b>(-25.73%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>233.40 (n/a)</td><td>134.54 (n/a)</td><td>115.10 (n/a)</td><td>104.50 (n/a)</td><td>55.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (-15.23%)</td><td>0.13 (-7.12%)</td><td>0.12 <b>(-25.85%)</b></td><td>0.11 <b>(+75.49%)</b></td><td>0.02 <b>(-59.54%)</b></td><td>186.80 <b>(-43.01%)</b></td><td>165.42 (-5.86%)</td><td>176.20 <b>(+34.92%)</b></td><td>133.30 (+17.96%)</td><td>24.32 <b>(-72.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>327.80 (n/a)</td><td>175.72 (n/a)</td><td>130.60 (n/a)</td><td>113.00 (n/a)</td><td>89.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 <b>(-39.10%)</b></td><td>0.13 (-4.48%)</td><td>0.14 (+18.55%)</td><td>0.12 <b>(+61.17%)</b></td><td>0.01 <b>(-80.27%)</b></td><td>177.70 <b>(-37.95%)</b></td><td>158.98 (-9.32%)</td><td>150.30 (-15.66%)</td><td>145.90 <b>(+64.12%)</b></td><td>15.16 <b>(-79.52%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>286.40 (n/a)</td><td>175.32 (n/a)</td><td>178.20 (n/a)</td><td>88.90 (n/a)</td><td>74.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-5.19%)</td><td>0.15 (-5.21%)</td><td>0.14 (-9.84%)</td><td>0.12 <b>(+47.89%)</b></td><td>0.04 <b>(-30.62%)</b></td><td>182.10 <b>(-32.38%)</b></td><td>146.76 (-2.67%)</td><td>148.20 (+10.93%)</td><td>100.90 (+5.43%)</td><td>30.47 <b>(-55.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>269.30 (n/a)</td><td>150.78 (n/a)</td><td>133.60 (n/a)</td><td>95.70 (n/a)</td><td>68.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (-14.58%)</td><td>0.12 <b>(-28.04%)</b></td><td>0.12 <b>(-30.75%)</b></td><td>0.06 <b>(-50.10%)</b></td><td>0.04 <b>(+56.46%)</b></td><td>356.40 <b>(+100.45%)</b></td><td>206.36 <b>(+54.51%)</b></td><td>180.70 <b>(+44.44%)</b></td><td>131.20 (+17.14%)</td><td>92.00 <b>(+252.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>177.80 (n/a)</td><td>133.56 (n/a)</td><td>125.10 (n/a)</td><td>112.00 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 <b>(-26.93%)</b></td><td>0.12 (-11.56%)</td><td>0.12 <b>(-23.94%)</b></td><td>0.10 <b>(+4818.22%)</b></td><td>0.02 <b>(-77.84%)</b></td><td>201.10 <b>(-97.97%)</b></td><td>180.68 <b>(-91.31%)</b></td><td>179.40 <b>(+31.52%)</b></td><td>144.20 <b>(+36.94%)</b></td><td>23.25 <b>(-99.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.00 (n/a)</td><td>0.08 (n/a)</td><td>9890.20 (n/a)</td><td>2080.32 (n/a)</td><td>136.40 (n/a)</td><td>105.30 (n/a)</td><td>4365.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (-5.43%)</td><td>0.13 <b>(+25.84%)</b></td><td>0.12 (+9.12%)</td><td>0.11 <b>(+69410.54%)</b></td><td>0.02 <b>(-71.21%)</b></td><td>192.50 <b>(-99.86%)</b></td><td>168.24 <b>(-99.37%)</b></td><td>171.00 (-8.36%)</td><td>138.10 (+5.74%)</td><td>21.93 <b>(-99.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>0.06 (n/a)</td><td>133797.50 (n/a)</td><td>26896.76 (n/a)</td><td>186.60 (n/a)</td><td>130.60 (n/a)</td><td>59759.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 <b>(-33.59%)</b></td><td>0.11 (+1.20%)</td><td>0.11 (-8.88%)</td><td>0.09 <b>(+2077.28%)</b></td><td>0.02 <b>(-75.77%)</b></td><td>231.30 <b>(-95.41%)</b></td><td>192.60 <b>(-83.11%)</b></td><td>190.30 (+9.75%)</td><td>163.60 <b>(+50.64%)</b></td><td>29.80 <b>(-98.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.00 (n/a)</td><td>0.07 (n/a)</td><td>5037.10 (n/a)</td><td>1140.02 (n/a)</td><td>173.40 (n/a)</td><td>108.60 (n/a)</td><td>2178.97 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.30 (n/a)</td><td>163.70 (n/a)</td><td>174.30 (n/a)</td><td>134.50 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>155.86 (n/a)</td><td>152.80 (n/a)</td><td>117.00 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>171.70 (n/a)</td><td>167.60 (n/a)</td><td>159.80 (n/a)</td><td>11.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>185.52 (n/a)</td><td>186.80 (n/a)</td><td>134.80 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>165.00 (n/a)</td><td>150.42 (n/a)</td><td>158.30 (n/a)</td><td>121.30 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.60 (n/a)</td><td>152.28 (n/a)</td><td>162.90 (n/a)</td><td>120.20 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>206.20 (n/a)</td><td>197.36 (n/a)</td><td>196.50 (n/a)</td><td>188.80 (n/a)</td><td>6.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>185.50 (n/a)</td><td>190.80 (n/a)</td><td>144.40 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.10 (n/a)</td><td>173.78 (n/a)</td><td>163.00 (n/a)</td><td>137.80 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>213.50 (n/a)</td><td>159.22 (n/a)</td><td>150.10 (n/a)</td><td>123.40 (n/a)</td><td>39.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>192.90 (n/a)</td><td>147.10 (n/a)</td><td>127.60 (n/a)</td><td>111.20 (n/a)</td><td>38.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>185.20 (n/a)</td><td>189.20 (n/a)</td><td>148.00 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.37 (+15.32%)</td><td>0.30 (+17.90%)</td><td>0.29 (-4.46%)</td><td>0.24 <b>(+460.43%)</b></td><td>0.05 <b>(-59.66%)</b></td><td>203.20 <b>(-82.16%)</b></td><td>166.70 <b>(-53.12%)</b></td><td>169.50 (+4.63%)</td><td>132.10 (-13.26%)</td><td>26.04 <b>(-94.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>1138.90 (n/a)</td><td>355.60 (n/a)</td><td>162.00 (n/a)</td><td>152.30 (n/a)</td><td>437.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>247.70 (n/a)</td><td>184.82 (n/a)</td><td>178.90 (n/a)</td><td>127.90 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>219.30 (n/a)</td><td>173.58 (n/a)</td><td>185.70 (n/a)</td><td>125.40 (n/a)</td><td>43.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>206.10 (n/a)</td><td>184.70 (n/a)</td><td>178.80 (n/a)</td><td>163.10 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>151.02 (n/a)</td><td>146.10 (n/a)</td><td>107.90 (n/a)</td><td>40.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>157.98 (n/a)</td><td>153.70 (n/a)</td><td>116.40 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.80 (n/a)</td><td>170.44 (n/a)</td><td>171.40 (n/a)</td><td>126.10 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>183.02 (n/a)</td><td>175.00 (n/a)</td><td>168.40 (n/a)</td><td>15.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>156.18 (n/a)</td><td>160.90 (n/a)</td><td>134.70 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>295.90 (n/a)</td><td>183.88 (n/a)</td><td>164.30 (n/a)</td><td>116.30 (n/a)</td><td>67.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>206.00 (n/a)</td><td>178.86 (n/a)</td><td>190.00 (n/a)</td><td>119.90 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>190.56 (n/a)</td><td>183.60 (n/a)</td><td>157.80 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>359.50 (n/a)</td><td>223.60 (n/a)</td><td>193.80 (n/a)</td><td>177.80 (n/a)</td><td>76.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>168.32 (n/a)</td><td>176.40 (n/a)</td><td>140.70 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>196.78 (n/a)</td><td>206.20 (n/a)</td><td>164.20 (n/a)</td><td>29.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>199.50 (n/a)</td><td>166.22 (n/a)</td><td>158.10 (n/a)</td><td>149.60 (n/a)</td><td>19.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>200.30 (n/a)</td><td>156.48 (n/a)</td><td>144.00 (n/a)</td><td>118.00 (n/a)</td><td>32.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>222.20 (n/a)</td><td>190.80 (n/a)</td><td>193.50 (n/a)</td><td>155.20 (n/a)</td><td>24.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>229.60 (n/a)</td><td>183.42 (n/a)</td><td>176.80 (n/a)</td><td>140.30 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>177.18 (n/a)</td><td>170.40 (n/a)</td><td>131.70 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>176.72 (n/a)</td><td>155.10 (n/a)</td><td>152.50 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.20 (n/a)</td><td>229.32 (n/a)</td><td>215.80 (n/a)</td><td>171.60 (n/a)</td><td>51.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>179.82 (n/a)</td><td>174.70 (n/a)</td><td>155.80 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.40 (n/a)</td><td>181.98 (n/a)</td><td>174.20 (n/a)</td><td>158.20 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.10 (n/a)</td><td>179.50 (n/a)</td><td>178.60 (n/a)</td><td>164.00 (n/a)</td><td>12.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>170.24 (n/a)</td><td>180.30 (n/a)</td><td>128.50 (n/a)</td><td>30.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.00 (n/a)</td><td>216.44 (n/a)</td><td>216.60 (n/a)</td><td>180.10 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>173.30 (n/a)</td><td>166.00 (n/a)</td><td>140.00 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>173.68 (n/a)</td><td>168.60 (n/a)</td><td>149.10 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>158.38 (n/a)</td><td>140.90 (n/a)</td><td>116.80 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>166.36 (n/a)</td><td>172.40 (n/a)</td><td>116.20 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>172.14 (n/a)</td><td>167.60 (n/a)</td><td>123.50 (n/a)</td><td>47.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>183.30 (n/a)</td><td>171.20 (n/a)</td><td>159.00 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.30 (n/a)</td><td>185.28 (n/a)</td><td>187.30 (n/a)</td><td>148.10 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.60 (n/a)</td><td>214.50 (n/a)</td><td>185.20 (n/a)</td><td>155.20 (n/a)</td><td>79.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>177.74 (n/a)</td><td>174.50 (n/a)</td><td>146.80 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>183.24 (n/a)</td><td>189.40 (n/a)</td><td>154.90 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>169.78 (n/a)</td><td>165.80 (n/a)</td><td>123.70 (n/a)</td><td>32.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>160.20 (n/a)</td><td>158.50 (n/a)</td><td>138.80 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>182.90 (n/a)</td><td>182.60 (n/a)</td><td>149.80 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.20 (n/a)</td><td>162.34 (n/a)</td><td>163.10 (n/a)</td><td>128.60 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.00 (n/a)</td><td>189.08 (n/a)</td><td>180.20 (n/a)</td><td>151.70 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>206.06 (n/a)</td><td>218.10 (n/a)</td><td>165.70 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.40 (n/a)</td><td>173.16 (n/a)</td><td>166.10 (n/a)</td><td>157.20 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.30 (n/a)</td><td>178.18 (n/a)</td><td>194.90 (n/a)</td><td>124.70 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.20 (n/a)</td><td>177.38 (n/a)</td><td>164.70 (n/a)</td><td>141.60 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.30 (n/a)</td><td>174.86 (n/a)</td><td>146.70 (n/a)</td><td>133.40 (n/a)</td><td>50.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>245.00 (n/a)</td><td>219.58 (n/a)</td><td>221.80 (n/a)</td><td>173.10 (n/a)</td><td>28.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>237.30 (n/a)</td><td>186.48 (n/a)</td><td>166.70 (n/a)</td><td>127.00 (n/a)</td><td>48.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.70 (n/a)</td><td>208.92 (n/a)</td><td>222.50 (n/a)</td><td>169.10 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.35 (-9.17%)</td><td>4.18 <b>(+44.76%)</b></td><td>4.18 (-11.05%)</td><td>3.95 <b>(+5563.61%)</b></td><td>0.17 <b>(-93.39%)</b></td><td>2380.30 <b>(-98.23%)</b></td><td>2252.32 <b>(-94.28%)</b></td><td>2251.00 (+12.42%)</td><td>2159.50 (+10.10%)</td><td>90.95 <b>(-99.84%)</b></td><td>1713.09 (-9.17%)</td><td>1644.59 <b>(+44.76%)</b></td><td>1643.43 (-11.05%)</td><td>1554.15 <b>(+5563.61%)</b></td><td>65.70 <b>(-93.39%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.79 (n/a)</td><td>2.89 (n/a)</td><td>4.70 (n/a)</td><td>0.07 (n/a)</td><td>2.53 (n/a)</td><td>134812.30 (n/a)</td><td>39365.62 (n/a)</td><td>2002.30 (n/a)</td><td>1961.40 (n/a)</td><td>58267.06 (n/a)</td><td>1886.05 (n/a)</td><td>1136.06 (n/a)</td><td>1847.58 (n/a)</td><td>27.44 (n/a)</td><td>994.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.12 <b>(-25.74%)</b></td><td>1.02 (+19.71%)</td><td>1.00 (+9.18%)</td><td>0.93 <b>(+55792.50%)</b></td><td>0.07 <b>(-86.87%)</b></td><td>237.30 <b>(-99.82%)</b></td><td>218.68 <b>(-99.18%)</b></td><td>220.90 (-8.38%)</td><td>198.10 <b>(+34.67%)</b></td><td>14.96 <b>(-99.97%)</b></td><td>47.64 <b>(-25.74%)</b></td><td>43.32 (+19.71%)</td><td>42.73 (+9.18%)</td><td>39.77 <b>(+55792.48%)</b></td><td>3.02 <b>(-86.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.50 (n/a)</td><td>0.85 (n/a)</td><td>0.92 (n/a)</td><td>0.00 (n/a)</td><td>0.54 (n/a)</td><td>132644.60 (n/a)</td><td>26703.88 (n/a)</td><td>241.10 (n/a)</td><td>147.10 (n/a)</td><td>59222.68 (n/a)</td><td>64.16 (n/a)</td><td>36.19 (n/a)</td><td>39.14 (n/a)</td><td>0.07 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.11 <b>(-24.48%)</b></td><td>0.90 (-4.00%)</td><td>0.94 (-3.16%)</td><td>0.64 <b>(+296.15%)</b></td><td>0.18 <b>(-63.27%)</b></td><td>345.50 <b>(-74.75%)</b></td><td>255.60 <b>(-41.48%)</b></td><td>234.60 (+3.26%)</td><td>198.80 <b>(+32.36%)</b></td><td>56.82 <b>(-89.12%)</b></td><td>47.46 <b>(-24.48%)</b></td><td>38.26 (-4.00%)</td><td>40.23 (-3.16%)</td><td>27.32 <b>(+296.15%)</b></td><td>7.65 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.47 (n/a)</td><td>0.93 (n/a)</td><td>0.97 (n/a)</td><td>0.16 (n/a)</td><td>0.49 (n/a)</td><td>1368.50 (n/a)</td><td>436.78 (n/a)</td><td>227.20 (n/a)</td><td>150.20 (n/a)</td><td>522.26 (n/a)</td><td>62.85 (n/a)</td><td>39.86 (n/a)</td><td>41.54 (n/a)</td><td>6.90 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.52 (-0.50%)</td><td>0.52 (-0.24%)</td><td>0.52 (-0.70%)</td><td>0.52 (+0.69%)</td><td>0.00 <b>(-65.36%)</b></td><td>48839.80 (-0.69%)</td><td>48656.88 (+0.23%)</td><td>48628.60 (+0.70%)</td><td>48440.10 (+0.51%)</td><td>154.43 <b>(-65.39%)</b></td><td>354.66 (-0.50%)</td><td>353.08 (-0.24%)</td><td>353.29 (-0.70%)</td><td>351.76 (+0.69%)</td><td>1.12 <b>(-65.36%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>49178.00 (n/a)</td><td>48543.88 (n/a)</td><td>48288.90 (n/a)</td><td>48196.70 (n/a)</td><td>446.22 (n/a)</td><td>356.45 (n/a)</td><td>353.93 (n/a)</td><td>355.77 (n/a)</td><td>349.34 (n/a)</td><td>3.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (+1.80%)</td><td>0.22 (+13.29%)</td><td>0.22 (+0.99%)</td><td>0.21 <b>(+113.47%)</b></td><td>0.00 <b>(-94.82%)</b></td><td>118489.30 <b>(-53.16%)</b></td><td>116347.74 (-19.62%)</td><td>116360.20 (-0.98%)</td><td>114889.80 (-1.77%)</td><td>1432.39 <b>(-97.63%)</b></td><td>149.53 (+1.80%)</td><td>147.68 (+13.29%)</td><td>147.64 (+0.99%)</td><td>144.99 <b>(+113.47%)</b></td><td>1.81 <b>(-94.82%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>252944.50 (n/a)</td><td>144751.66 (n/a)</td><td>117512.60 (n/a)</td><td>116955.00 (n/a)</td><td>60489.51 (n/a)</td><td>146.89 (n/a)</td><td>130.36 (n/a)</td><td>146.20 (n/a)</td><td>67.92 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 (-4.79%)</td><td>0.88 (-4.06%)</td><td>0.87 (-6.01%)</td><td>0.87 (-0.04%)</td><td>0.01 <b>(-73.85%)</b></td><td>28893.70 (+0.04%)</td><td>28758.68 (+4.17%)</td><td>28867.60 (+6.40%)</td><td>28379.80 (+5.03%)</td><td>217.91 <b>(-72.51%)</b></td><td>605.36 (-4.79%)</td><td>597.41 (-4.06%)</td><td>595.13 (-6.01%)</td><td>594.59 (-0.04%)</td><td>4.57 <b>(-73.85%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.93 (n/a)</td><td>0.91 (n/a)</td><td>0.93 (n/a)</td><td>0.87 (n/a)</td><td>0.03 (n/a)</td><td>28883.20 (n/a)</td><td>27608.68 (n/a)</td><td>27131.80 (n/a)</td><td>27021.10 (n/a)</td><td>792.80 (n/a)</td><td>635.80 (n/a)</td><td>622.66 (n/a)</td><td>633.20 (n/a)</td><td>594.80 (n/a)</td><td>17.47 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.50 (-2.79%)</td><td>3.39 (+2.37%)</td><td>3.35 (-6.53%)</td><td>3.24 <b>(+47.61%)</b></td><td>0.11 <b>(-82.03%)</b></td><td>7764.50 <b>(-32.26%)</b></td><td>7439.24 (-5.93%)</td><td>7501.60 (+6.98%)</td><td>7180.70 (+2.87%)</td><td>246.09 <b>(-87.61%)</b></td><td>2392.50 (-2.79%)</td><td>2311.38 (+2.37%)</td><td>2290.17 (-6.53%)</td><td>2212.61 <b>(+47.61%)</b></td><td>76.27 <b>(-82.03%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.61 (n/a)</td><td>3.31 (n/a)</td><td>3.59 (n/a)</td><td>2.20 (n/a)</td><td>0.62 (n/a)</td><td>11461.40 (n/a)</td><td>7907.84 (n/a)</td><td>7011.90 (n/a)</td><td>6980.60 (n/a)</td><td>1986.79 (n/a)</td><td>2461.09 (n/a)</td><td>2257.81 (n/a)</td><td>2450.10 (n/a)</td><td>1498.94 (n/a)</td><td>424.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>2.84 (-12.64%)</td><td>2.79 <b>(+24.76%)</b></td><td>2.81 (+12.17%)</td><td>2.73 <b>(+1433.01%)</b></td><td>0.04 <b>(-96.63%)</b></td><td>9206.20 <b>(-93.48%)</b></td><td>9015.10 <b>(-74.83%)</b></td><td>8951.00 (-10.85%)</td><td>8875.80 (+14.46%)</td><td>138.01 <b>(-99.77%)</b></td><td>1935.59 (-12.64%)</td><td>1906.03 <b>(+24.76%)</b></td><td>1919.32 (+12.17%)</td><td>1866.12 <b>(+1433.01%)</b></td><td>29.00 <b>(-96.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.25 (n/a)</td><td>2.24 (n/a)</td><td>2.51 (n/a)</td><td>0.18 (n/a)</td><td>1.26 (n/a)</td><td>141131.60 (n/a)</td><td>35818.18 (n/a)</td><td>10040.00 (n/a)</td><td>7754.20 (n/a)</td><td>58902.45 (n/a)</td><td>2215.54 (n/a)</td><td>1527.74 (n/a)</td><td>1711.14 (n/a)</td><td>121.73 (n/a)</td><td>859.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.31 (-3.41%)</td><td>3.21 (+16.12%)</td><td>3.16 (-6.05%)</td><td>3.14 <b>(+209.21%)</b></td><td>0.08 <b>(-92.37%)</b></td><td>8012.50 <b>(-67.66%)</b></td><td>7844.10 <b>(-30.72%)</b></td><td>7951.90 (+6.43%)</td><td>7607.20 (+3.53%)</td><td>190.90 <b>(-97.48%)</b></td><td>2258.36 (-3.41%)</td><td>2191.21 (+16.12%)</td><td>2160.47 (-6.05%)</td><td>2144.14 <b>(+209.21%)</b></td><td>53.80 <b>(-92.37%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.42 (n/a)</td><td>2.76 (n/a)</td><td>3.37 (n/a)</td><td>1.02 (n/a)</td><td>1.03 (n/a)</td><td>24775.20 (n/a)</td><td>11323.00 (n/a)</td><td>7471.20 (n/a)</td><td>7348.00 (n/a)</td><td>7579.05 (n/a)</td><td>2338.03 (n/a)</td><td>1886.98 (n/a)</td><td>2299.49 (n/a)</td><td>693.43 (n/a)</td><td>705.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.78 (-0.47%)</td><td>0.78 <b>(+31.13%)</b></td><td>0.78 (+2.38%)</td><td>0.78 <b>(+136.51%)</b></td><td>0.00 <b>(-99.94%)</b></td><td>96485.40 <b>(-57.72%)</b></td><td>96461.48 <b>(-35.47%)</b></td><td>96452.40 (-2.33%)</td><td>96447.00 (+0.47%)</td><td>16.66 <b>(-99.98%)</b></td><td>712.51 (-0.47%)</td><td>712.40 <b>(+31.13%)</b></td><td>712.47 (+2.38%)</td><td>712.23 <b>(+136.51%)</b></td><td>0.12 <b>(-99.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.76 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>228197.90 (n/a)</td><td>149480.50 (n/a)</td><td>98752.30 (n/a)</td><td>95993.60 (n/a)</td><td>70979.29 (n/a)</td><td>715.88 (n/a)</td><td>543.27 (n/a)</td><td>695.88 (n/a)</td><td>301.14 (n/a)</td><td>219.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.73 (-0.04%)</td><td>0.73 (+12.53%)</td><td>0.73 (+0.04%)</td><td>0.73 <b>(+125.39%)</b></td><td>0.00 <b>(-99.10%)</b></td><td>103788.40 <b>(-55.63%)</b></td><td>103596.80 <b>(-20.10%)</b></td><td>103660.40 (-0.04%)</td><td>103195.00 (+0.04%)</td><td>232.46 <b>(-99.60%)</b></td><td>665.92 (-0.04%)</td><td>663.34 (+12.53%)</td><td>662.93 (+0.04%)</td><td>662.11 <b>(+125.39%)</b></td><td>1.49 <b>(-99.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.73 (n/a)</td><td>0.65 (n/a)</td><td>0.73 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>233925.80 (n/a)</td><td>129657.70 (n/a)</td><td>103704.80 (n/a)</td><td>103151.10 (n/a)</td><td>58289.62 (n/a)</td><td>666.20 (n/a)</td><td>589.46 (n/a)</td><td>662.64 (n/a)</td><td>293.77 (n/a)</td><td>165.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.69 (-1.43%)</td><td>0.69 (+12.10%)</td><td>0.69 (+0.28%)</td><td>0.69 <b>(+119.23%)</b></td><td>0.00 <b>(-98.83%)</b></td><td>109728.60 <b>(-54.39%)</b></td><td>109349.16 (-19.29%)</td><td>109293.70 (-0.28%)</td><td>108942.20 (+1.45%)</td><td>312.60 <b>(-99.47%)</b></td><td>630.79 (-1.43%)</td><td>628.45 (+12.10%)</td><td>628.76 (+0.28%)</td><td>626.27 <b>(+119.23%)</b></td><td>1.80 <b>(-98.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.70 (n/a)</td><td>0.62 (n/a)</td><td>0.69 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>240559.30 (n/a)</td><td>135491.58 (n/a)</td><td>109597.90 (n/a)</td><td>107381.60 (n/a)</td><td>58765.49 (n/a)</td><td>639.96 (n/a)</td><td>560.61 (n/a)</td><td>627.01 (n/a)</td><td>285.67 (n/a)</td><td>154.08 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.29 (+0.59%)</td><td>6.98 (+19.73%)</td><td>7.04 (-1.66%)</td><td>6.46 <b>(+1141.49%)</b></td><td>0.33 <b>(-88.99%)</b></td><td>1379.60 <b>(-91.95%)</b></td><td>1280.12 <b>(-71.06%)</b></td><td>1266.10 (+1.69%)</td><td>1222.70 (-0.59%)</td><td>62.04 <b>(-99.13%)</b></td><td>439.07 (+0.59%)</td><td>420.14 (+19.73%)</td><td>424.02 (-1.66%)</td><td>389.15 <b>(+1141.49%)</b></td><td>19.67 <b>(-88.99%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.25 (n/a)</td><td>5.83 (n/a)</td><td>7.16 (n/a)</td><td>0.52 (n/a)</td><td>2.97 (n/a)</td><td>17127.50 (n/a)</td><td>4422.76 (n/a)</td><td>1245.10 (n/a)</td><td>1230.00 (n/a)</td><td>7102.19 (n/a)</td><td>436.49 (n/a)</td><td>350.90 (n/a)</td><td>431.20 (n/a)</td><td>31.35 (n/a)</td><td>178.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.05 (+2.07%)</td><td>6.82 <b>(+25.48%)</b></td><td>6.85 (+3.64%)</td><td>6.55 <b>(+1133.00%)</b></td><td>0.18 <b>(-93.48%)</b></td><td>1360.70 <b>(-91.89%)</b></td><td>1307.54 <b>(-70.46%)</b></td><td>1300.60 (-3.52%)</td><td>1264.60 (-2.02%)</td><td>34.71 <b>(-99.50%)</b></td><td>424.54 (+2.07%)</td><td>410.82 <b>(+25.48%)</b></td><td>412.78 (+3.64%)</td><td>394.56 <b>(+1133.00%)</b></td><td>10.79 <b>(-93.48%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.91 (n/a)</td><td>5.44 (n/a)</td><td>6.61 (n/a)</td><td>0.53 (n/a)</td><td>2.75 (n/a)</td><td>16777.20 (n/a)</td><td>4426.58 (n/a)</td><td>1348.00 (n/a)</td><td>1290.70 (n/a)</td><td>6904.30 (n/a)</td><td>415.94 (n/a)</td><td>327.41 (n/a)</td><td>398.28 (n/a)</td><td>32.00 (n/a)</td><td>165.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.87 (-4.53%)</td><td>6.07 (-10.76%)</td><td>6.30 (-5.96%)</td><td>4.62 <b>(-28.93%)</b></td><td>0.86 <b>(+191.92%)</b></td><td>1930.50 <b>(+40.71%)</b></td><td>1497.44 (+14.04%)</td><td>1413.90 (+6.34%)</td><td>1297.90 (+4.75%)</td><td>249.58 <b>(+344.93%)</b></td><td>413.66 (-4.53%)</td><td>365.40 (-10.76%)</td><td>379.71 (-5.96%)</td><td>278.11 <b>(-28.93%)</b></td><td>51.75 <b>(+191.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.19 (n/a)</td><td>6.80 (n/a)</td><td>6.70 (n/a)</td><td>6.50 (n/a)</td><td>0.29 (n/a)</td><td>1372.00 (n/a)</td><td>1313.10 (n/a)</td><td>1329.60 (n/a)</td><td>1239.00 (n/a)</td><td>56.10 (n/a)</td><td>433.30 (n/a)</td><td>409.46 (n/a)</td><td>403.78 (n/a)</td><td>391.30 (n/a)</td><td>17.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.19 (-3.03%)</td><td>7.88 <b>(+32.29%)</b></td><td>7.90 (-2.41%)</td><td>7.54 <b>(+2817.75%)</b></td><td>0.24 <b>(-93.23%)</b></td><td>4626.20 <b>(-96.57%)</b></td><td>4429.12 <b>(-85.73%)</b></td><td>4413.10 (+2.46%)</td><td>4255.40 (+3.12%)</td><td>137.12 <b>(-99.76%)</b></td><td>504.65 (-3.03%)</td><td>485.22 <b>(+32.29%)</b></td><td>486.61 (-2.41%)</td><td>464.20 <b>(+2817.75%)</b></td><td>14.93 <b>(-93.23%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.45 (n/a)</td><td>5.95 (n/a)</td><td>8.10 (n/a)</td><td>0.26 (n/a)</td><td>3.58 (n/a)</td><td>134980.30 (n/a)</td><td>31042.72 (n/a)</td><td>4307.00 (n/a)</td><td>4126.50 (n/a)</td><td>58122.31 (n/a)</td><td>520.41 (n/a)</td><td>366.78 (n/a)</td><td>498.61 (n/a)</td><td>15.91 (n/a)</td><td>220.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.82 (-1.09%)</td><td>7.45 (-3.90%)</td><td>7.59 (-2.81%)</td><td>6.83 (-9.74%)</td><td>0.38 <b>(+127.72%)</b></td><td>5102.00 (+10.79%)</td><td>4691.60 (+4.25%)</td><td>4595.80 (+2.89%)</td><td>4455.90 (+1.10%)</td><td>249.61 <b>(+156.50%)</b></td><td>481.94 (-1.09%)</td><td>458.72 (-3.90%)</td><td>467.27 (-2.81%)</td><td>420.91 (-9.74%)</td><td>23.39 <b>(+127.72%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.91 (n/a)</td><td>7.75 (n/a)</td><td>7.81 (n/a)</td><td>7.57 (n/a)</td><td>0.17 (n/a)</td><td>4605.20 (n/a)</td><td>4500.40 (n/a)</td><td>4466.70 (n/a)</td><td>4407.40 (n/a)</td><td>97.31 (n/a)</td><td>487.25 (n/a)</td><td>477.35 (n/a)</td><td>480.77 (n/a)</td><td>466.32 (n/a)</td><td>10.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.60 (-2.55%)</td><td>7.37 (-2.10%)</td><td>7.31 (-5.01%)</td><td>7.24 (+6.11%)</td><td>0.14 <b>(-64.60%)</b></td><td>4812.50 (-5.76%)</td><td>4733.68 (+1.93%)</td><td>4766.80 (+5.28%)</td><td>4587.60 (+2.62%)</td><td>89.49 <b>(-66.05%)</b></td><td>468.10 (-2.55%)</td><td>453.79 (-2.10%)</td><td>450.51 (-5.01%)</td><td>446.23 (+6.11%)</td><td>8.72 <b>(-64.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.80 (n/a)</td><td>7.53 (n/a)</td><td>7.70 (n/a)</td><td>6.83 (n/a)</td><td>0.40 (n/a)</td><td>5106.40 (n/a)</td><td>4643.94 (n/a)</td><td>4527.90 (n/a)</td><td>4470.60 (n/a)</td><td>263.64 (n/a)</td><td>480.35 (n/a)</td><td>463.55 (n/a)</td><td>474.28 (n/a)</td><td>420.55 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.79 (-0.51%)</td><td>0.79 <b>(+29.87%)</b></td><td>0.79 (+0.82%)</td><td>0.79 <b>(+136.53%)</b></td><td>0.00 <b>(-99.89%)</b></td><td>95809.70 <b>(-57.72%)</b></td><td>95764.80 <b>(-35.21%)</b></td><td>95745.70 (-0.81%)</td><td>95733.40 (+0.51%)</td><td>33.74 <b>(-99.95%)</b></td><td>717.82 (-0.51%)</td><td>717.59 <b>(+29.87%)</b></td><td>717.73 (+0.82%)</td><td>717.25 <b>(+136.53%)</b></td><td>0.25 <b>(-99.89%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.79 (n/a)</td><td>0.61 (n/a)</td><td>0.78 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>226620.60 (n/a)</td><td>147806.72 (n/a)</td><td>96531.70 (n/a)</td><td>95244.40 (n/a)</td><td>71372.88 (n/a)</td><td>721.51 (n/a)</td><td>552.56 (n/a)</td><td>711.88 (n/a)</td><td>303.24 (n/a)</td><td>226.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.73 (-0.45%)</td><td>0.73 (-0.23%)</td><td>0.73 (-0.41%)</td><td>0.73 (+0.56%)</td><td>0.00 <b>(-80.54%)</b></td><td>103167.40 (-0.55%)</td><td>102979.90 (+0.23%)</td><td>102946.80 (+0.41%)</td><td>102898.50 (+0.46%)</td><td>108.96 <b>(-80.57%)</b></td><td>667.84 (-0.45%)</td><td>667.31 (-0.23%)</td><td>667.52 (-0.41%)</td><td>666.10 (+0.56%)</td><td>0.71 <b>(-80.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103743.10 (n/a)</td><td>102742.42 (n/a)</td><td>102523.30 (n/a)</td><td>102431.80 (n/a)</td><td>560.66 (n/a)</td><td>670.88 (n/a)</td><td>668.87 (n/a)</td><td>670.28 (n/a)</td><td>662.40 (n/a)</td><td>3.62 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.70 (-1.33%)</td><td>0.70 <b>(+26.60%)</b></td><td>0.70 (-1.10%)</td><td>0.70 <b>(+120.72%)</b></td><td>0.00 <b>(-99.41%)</b></td><td>108570.60 <b>(-54.69%)</b></td><td>108224.64 <b>(-32.09%)</b></td><td>108163.10 (+1.11%)</td><td>108084.10 (+1.34%)</td><td>197.04 <b>(-99.73%)</b></td><td>635.80 (-1.33%)</td><td>634.97 <b>(+26.60%)</b></td><td>635.33 (-1.10%)</td><td>632.95 <b>(+120.72%)</b></td><td>1.15 <b>(-99.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.71 (n/a)</td><td>0.55 (n/a)</td><td>0.71 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>239632.20 (n/a)</td><td>159365.06 (n/a)</td><td>106978.40 (n/a)</td><td>106651.60 (n/a)</td><td>72030.44 (n/a)</td><td>644.34 (n/a)</td><td>501.56 (n/a)</td><td>642.37 (n/a)</td><td>286.77 (n/a)</td><td>194.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.19 (-0.65%)</td><td>3.47 (-16.58%)</td><td>3.47 (-16.51%)</td><td>2.89 <b>(-29.74%)</b></td><td>0.48 <b>(+1169.98%)</b></td><td>2784.70 <b>(+42.32%)</b></td><td>2358.22 <b>(+21.68%)</b></td><td>2322.20 (+19.78%)</td><td>1922.30 (+0.65%)</td><td>319.46 <b>(+1713.65%)</b></td><td>1099.70 (-0.65%)</td><td>910.04 (-16.58%)</td><td>910.33 (-16.51%)</td><td>759.13 <b>(-29.74%)</b></td><td>126.75 <b>(+1169.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.22 (n/a)</td><td>4.16 (n/a)</td><td>4.16 (n/a)</td><td>4.12 (n/a)</td><td>0.04 (n/a)</td><td>1956.60 (n/a)</td><td>1938.00 (n/a)</td><td>1938.80 (n/a)</td><td>1909.80 (n/a)</td><td>17.61 (n/a)</td><td>1106.89 (n/a)</td><td>1090.85 (n/a)</td><td>1090.33 (n/a)</td><td>1080.41 (n/a)</td><td>9.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.38 (-16.72%)</td><td>0.33 <b>(+158.88%)</b></td><td>0.34 <b>(+362.48%)</b></td><td>0.29 <b>(+3995.09%)</b></td><td>0.04 <b>(-81.19%)</b></td><td>4306.90 <b>(-97.56%)</b></td><td>3756.12 <b>(-92.58%)</b></td><td>3627.40 <b>(-78.38%)</b></td><td>3260.10 <b>(+20.08%)</b></td><td>397.25 <b>(-99.45%)</b></td><td>20.58 (-16.72%)</td><td>18.03 <b>(+158.88%)</b></td><td>18.50 <b>(+362.48%)</b></td><td>15.58 <b>(+3995.09%)</b></td><td>1.89 <b>(-81.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.46 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>176372.90 (n/a)</td><td>50647.18 (n/a)</td><td>16775.90 (n/a)</td><td>2715.00 (n/a)</td><td>71615.22 (n/a)</td><td>24.72 (n/a)</td><td>6.96 (n/a)</td><td>4.00 (n/a)</td><td>0.38 (n/a)</td><td>10.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.53 (+1.24%)</td><td>4.92 (-7.06%)</td><td>4.99 (-17.87%)</td><td>3.51 <b>(+84.69%)</b></td><td>1.39 <b>(-27.12%)</b></td><td>1896.60 <b>(-45.86%)</b></td><td>1447.20 (-7.74%)</td><td>1333.00 <b>(+21.75%)</b></td><td>1019.20 (-1.23%)</td><td>420.23 <b>(-61.16%)</b></td><td>2016.50 (+1.24%)</td><td>1519.01 (-7.06%)</td><td>1541.76 (-17.87%)</td><td>1083.60 <b>(+84.69%)</b></td><td>429.61 <b>(-27.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.45 (n/a)</td><td>5.29 (n/a)</td><td>6.08 (n/a)</td><td>1.90 (n/a)</td><td>1.91 (n/a)</td><td>3503.00 (n/a)</td><td>1568.66 (n/a)</td><td>1094.90 (n/a)</td><td>1031.90 (n/a)</td><td>1081.99 (n/a)</td><td>1991.73 (n/a)</td><td>1634.49 (n/a)</td><td>1877.14 (n/a)</td><td>586.70 (n/a)</td><td>589.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (-3.83%)</td><td>0.22 (+4.60%)</td><td>0.19 (+0.69%)</td><td>0.18 (+13.68%)</td><td>0.04 <b>(-22.28%)</b></td><td>0.27 (-3.83%)</td><td>0.21 (+4.60%)</td><td>0.19 (+0.69%)</td><td>0.18 (+13.68%)</td><td>0.04 <b>(-22.28%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.47 (+1.03%)</td><td>12.91 (-1.68%)</td><td>13.17 (-0.50%)</td><td>12.09 (-4.14%)</td><td>0.59 <b>(+98.61%)</b></td><td>13.46 (+1.03%)</td><td>12.90 (-1.68%)</td><td>13.17 (-0.50%)</td><td>12.08 (-4.14%)</td><td>0.59 <b>(+98.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.33 (n/a)</td><td>13.13 (n/a)</td><td>13.24 (n/a)</td><td>12.61 (n/a)</td><td>0.30 (n/a)</td><td>13.32 (n/a)</td><td>13.12 (n/a)</td><td>13.23 (n/a)</td><td>12.60 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>25.09 (+2.82%)</td><td>24.26 (+2.24%)</td><td>23.89 (-0.04%)</td><td>23.69 (+3.90%)</td><td>0.63 (-12.93%)</td><td>25.07 (+2.82%)</td><td>24.25 (+2.24%)</td><td>23.87 (-0.04%)</td><td>23.67 (+3.90%)</td><td>0.63 (-12.93%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>24.40 (n/a)</td><td>23.73 (n/a)</td><td>23.90 (n/a)</td><td>22.80 (n/a)</td><td>0.72 (n/a)</td><td>24.39 (n/a)</td><td>23.72 (n/a)</td><td>23.88 (n/a)</td><td>22.79 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>40.32 (-3.56%)</td><td>39.65 (+2.22%)</td><td>40.01 (+1.48%)</td><td>38.55 (+11.72%)</td><td>0.74 <b>(-72.20%)</b></td><td>40.30 (-3.56%)</td><td>39.63 (+2.22%)</td><td>39.98 (+1.48%)</td><td>38.53 (+11.72%)</td><td>0.74 <b>(-72.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>41.81 (n/a)</td><td>38.79 (n/a)</td><td>39.42 (n/a)</td><td>34.51 (n/a)</td><td>2.66 (n/a)</td><td>41.78 (n/a)</td><td>38.77 (n/a)</td><td>39.40 (n/a)</td><td>34.48 (n/a)</td><td>2.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>45.14 (-4.62%)</td><td>43.48 (+1.81%)</td><td>43.11 (+3.38%)</td><td>41.78 (+2.04%)</td><td>1.50 <b>(-43.07%)</b></td><td>45.11 (-4.62%)</td><td>43.46 (+1.81%)</td><td>43.08 (+3.38%)</td><td>41.76 (+2.04%)</td><td>1.49 <b>(-43.07%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>47.33 (n/a)</td><td>42.71 (n/a)</td><td>41.70 (n/a)</td><td>40.95 (n/a)</td><td>2.63 (n/a)</td><td>47.30 (n/a)</td><td>42.68 (n/a)</td><td>41.67 (n/a)</td><td>40.92 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.38 (-0.43%)</td><td>13.05 (-1.20%)</td><td>13.18 (-0.84%)</td><td>12.29 (-4.07%)</td><td>0.43 <b>(+82.56%)</b></td><td>13.37 (-0.43%)</td><td>13.04 (-1.20%)</td><td>13.17 (-0.84%)</td><td>12.28 (-4.07%)</td><td>0.43 <b>(+82.56%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.44 (n/a)</td><td>13.21 (n/a)</td><td>13.29 (n/a)</td><td>12.81 (n/a)</td><td>0.24 (n/a)</td><td>13.43 (n/a)</td><td>13.20 (n/a)</td><td>13.28 (n/a)</td><td>12.80 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>24.79 (+0.36%)</td><td>23.82 (-0.63%)</td><td>23.66 (-0.92%)</td><td>23.05 (-1.47%)</td><td>0.80 <b>(+49.05%)</b></td><td>24.77 (+0.36%)</td><td>23.80 (-0.63%)</td><td>23.65 (-0.92%)</td><td>23.04 (-1.47%)</td><td>0.80 <b>(+49.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>24.70 (n/a)</td><td>23.97 (n/a)</td><td>23.88 (n/a)</td><td>23.39 (n/a)</td><td>0.54 (n/a)</td><td>24.68 (n/a)</td><td>23.95 (n/a)</td><td>23.87 (n/a)</td><td>23.38 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>40.56 (-5.49%)</td><td>39.03 (-3.34%)</td><td>38.71 (-5.31%)</td><td>37.55 (-1.76%)</td><td>1.15 <b>(-39.06%)</b></td><td>40.53 (-5.49%)</td><td>39.00 (-3.34%)</td><td>38.68 (-5.31%)</td><td>37.53 (-1.76%)</td><td>1.15 <b>(-39.06%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>42.91 (n/a)</td><td>40.38 (n/a)</td><td>40.88 (n/a)</td><td>38.22 (n/a)</td><td>1.88 (n/a)</td><td>42.89 (n/a)</td><td>40.35 (n/a)</td><td>40.86 (n/a)</td><td>38.20 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>44.57 (-1.05%)</td><td>42.82 (+1.90%)</td><td>42.53 (-0.52%)</td><td>41.88 (+14.10%)</td><td>1.03 <b>(-67.19%)</b></td><td>44.54 (-1.05%)</td><td>42.79 (+1.90%)</td><td>42.50 (-0.52%)</td><td>41.85 (+14.10%)</td><td>1.03 <b>(-67.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>45.04 (n/a)</td><td>42.02 (n/a)</td><td>42.75 (n/a)</td><td>36.70 (n/a)</td><td>3.14 (n/a)</td><td>45.02 (n/a)</td><td>42.00 (n/a)</td><td>42.73 (n/a)</td><td>36.68 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>180.80 (n/a)</td><td>182.10 (n/a)</td><td>141.00 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>177.12 (n/a)</td><td>179.70 (n/a)</td><td>141.40 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.00 (n/a)</td><td>179.86 (n/a)</td><td>172.70 (n/a)</td><td>127.50 (n/a)</td><td>42.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.40 (n/a)</td><td>177.48 (n/a)</td><td>170.80 (n/a)</td><td>150.50 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>183.02 (n/a)</td><td>177.60 (n/a)</td><td>168.20 (n/a)</td><td>13.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>313.00 (n/a)</td><td>236.24 (n/a)</td><td>225.40 (n/a)</td><td>165.50 (n/a)</td><td>60.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.00 (n/a)</td><td>187.14 (n/a)</td><td>196.90 (n/a)</td><td>160.50 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>269.50 (n/a)</td><td>231.52 (n/a)</td><td>231.70 (n/a)</td><td>191.10 (n/a)</td><td>32.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>202.68 (n/a)</td><td>204.50 (n/a)</td><td>164.90 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>202.18 (n/a)</td><td>204.70 (n/a)</td><td>146.50 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>177.14 (n/a)</td><td>153.70 (n/a)</td><td>148.00 (n/a)</td><td>39.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>160.72 (n/a)</td><td>137.60 (n/a)</td><td>118.30 (n/a)</td><td>48.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>171.24 (n/a)</td><td>171.30 (n/a)</td><td>147.10 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.40 (n/a)</td><td>207.82 (n/a)</td><td>205.50 (n/a)</td><td>166.70 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.90 (n/a)</td><td>198.34 (n/a)</td><td>200.00 (n/a)</td><td>179.30 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>252.60 (n/a)</td><td>224.90 (n/a)</td><td>222.70 (n/a)</td><td>203.60 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>195.96 (n/a)</td><td>191.90 (n/a)</td><td>182.70 (n/a)</td><td>17.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>204.52 (n/a)</td><td>201.70 (n/a)</td><td>185.40 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>206.50 (n/a)</td><td>201.30 (n/a)</td><td>171.70 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>260.80 (n/a)</td><td>205.22 (n/a)</td><td>220.30 (n/a)</td><td>129.20 (n/a)</td><td>51.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>206.18 (n/a)</td><td>206.70 (n/a)</td><td>179.50 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>218.80 (n/a)</td><td>197.04 (n/a)</td><td>206.20 (n/a)</td><td>169.10 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>189.00 (n/a)</td><td>180.60 (n/a)</td><td>175.90 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>337.10 (n/a)</td><td>247.08 (n/a)</td><td>231.90 (n/a)</td><td>200.80 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (+6.05%)</td><td>0.17 (-4.80%)</td><td>0.17 (-6.66%)</td><td>0.15 (-8.47%)</td><td>0.02 <b>(+55.26%)</b></td><td>219.30 (+9.27%)</td><td>195.08 (+5.91%)</td><td>197.00 (+7.12%)</td><td>155.80 (-5.69%)</td><td>24.37 <b>(+55.68%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.70 (n/a)</td><td>184.20 (n/a)</td><td>183.90 (n/a)</td><td>165.20 (n/a)</td><td>15.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>298.80 (n/a)</td><td>192.46 (n/a)</td><td>170.10 (n/a)</td><td>143.40 (n/a)</td><td>62.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>192.62 (n/a)</td><td>195.80 (n/a)</td><td>172.20 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>248.80 (n/a)</td><td>203.02 (n/a)</td><td>208.80 (n/a)</td><td>147.00 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>297.40 (n/a)</td><td>207.46 (n/a)</td><td>191.30 (n/a)</td><td>149.30 (n/a)</td><td>54.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>251.50 (n/a)</td><td>216.76 (n/a)</td><td>207.60 (n/a)</td><td>175.80 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>260.60 (n/a)</td><td>196.06 (n/a)</td><td>198.60 (n/a)</td><td>137.80 (n/a)</td><td>48.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>273.60 (n/a)</td><td>243.54 (n/a)</td><td>248.90 (n/a)</td><td>211.80 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-0.19%)</td><td>0.02 (-9.46%)</td><td>0.02 (-0.26%)</td><td>0.01 <b>(-52.02%)</b></td><td>0.01 <b>(+219.11%)</b></td><td>394.80 <b>(+108.45%)</b></td><td>212.42 <b>(+23.95%)</b></td><td>170.50 (+0.24%)</td><td>155.90 (+0.19%)</td><td>102.29 <b>(+601.85%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.40 (n/a)</td><td>171.38 (n/a)</td><td>170.10 (n/a)</td><td>155.60 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-7.36%)</td><td>0.02 (-8.10%)</td><td>0.02 (-8.96%)</td><td>0.02 (-15.46%)</td><td>0.01 (+13.47%)</td><td>265.80 (+18.29%)</td><td>186.78 (+10.89%)</td><td>168.60 (+9.84%)</td><td>145.70 (+7.93%)</td><td>50.73 <b>(+40.40%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>168.44 (n/a)</td><td>153.50 (n/a)</td><td>135.00 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+10.80%)</td><td>0.02 (-4.68%)</td><td>0.02 (-16.45%)</td><td>0.01 <b>(-30.12%)</b></td><td>0.01 <b>(+122.82%)</b></td><td>330.60 <b>(+43.12%)</b></td><td>226.04 (+12.26%)</td><td>230.70 (+19.66%)</td><td>156.50 (-9.75%)</td><td>73.01 <b>(+164.50%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.00 (n/a)</td><td>201.36 (n/a)</td><td>192.80 (n/a)</td><td>173.40 (n/a)</td><td>27.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+1.14%)</td><td>0.02 (+0.02%)</td><td>0.02 (-6.75%)</td><td>0.02 (+9.08%)</td><td>0.00 (+0.12%)</td><td>236.30 (-8.34%)</td><td>204.96 (-0.20%)</td><td>208.00 (+7.27%)</td><td>163.60 (-1.15%)</td><td>31.95 (-8.71%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>257.80 (n/a)</td><td>205.38 (n/a)</td><td>193.90 (n/a)</td><td>165.50 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-26.78%)</b></td><td>0.02 (-7.48%)</td><td>0.02 (-4.44%)</td><td>0.02 (-5.87%)</td><td>0.00 <b>(-51.51%)</b></td><td>204.90 (+6.22%)</td><td>166.78 (+5.42%)</td><td>164.20 (+4.65%)</td><td>147.90 <b>(+36.57%)</b></td><td>23.16 <b>(-27.42%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>158.20 (n/a)</td><td>156.90 (n/a)</td><td>108.30 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (+11.40%)</td><td>0.03 (+15.84%)</td><td>0.03 (+13.39%)</td><td>0.02 (-1.89%)</td><td>0.01 <b>(+46.59%)</b></td><td>206.00 (+1.88%)</td><td>155.30 (-11.77%)</td><td>160.20 (-11.83%)</td><td>117.00 (-10.21%)</td><td>37.52 <b>(+29.40%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>176.02 (n/a)</td><td>181.70 (n/a)</td><td>130.30 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-3.42%)</td><td>0.02 (-14.30%)</td><td>0.02 (-6.55%)</td><td>0.01 <b>(-48.61%)</b></td><td>0.01 <b>(+90.00%)</b></td><td>393.40 <b>(+94.56%)</b></td><td>216.42 <b>(+30.20%)</b></td><td>177.60 (+6.99%)</td><td>143.60 (+3.53%)</td><td>102.07 <b>(+303.46%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>166.22 (n/a)</td><td>166.00 (n/a)</td><td>138.70 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+2.12%)</td><td>0.02 (-14.64%)</td><td>0.02 (-14.86%)</td><td>0.02 <b>(-27.83%)</b></td><td>0.01 <b>(+50.18%)</b></td><td>233.70 <b>(+38.61%)</b></td><td>176.08 <b>(+21.22%)</b></td><td>176.40 (+17.44%)</td><td>120.00 (-2.12%)</td><td>43.33 <b>(+106.32%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.60 (n/a)</td><td>145.26 (n/a)</td><td>150.20 (n/a)</td><td>122.60 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-12.18%)</td><td>0.02 (-15.86%)</td><td>0.02 (-12.41%)</td><td>0.01 <b>(-27.74%)</b></td><td>0.00 (-2.68%)</td><td>300.60 <b>(+38.40%)</b></td><td>209.86 <b>(+20.76%)</b></td><td>190.40 (+14.22%)</td><td>156.30 (+13.84%)</td><td>54.68 <b>(+58.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>173.78 (n/a)</td><td>166.70 (n/a)</td><td>137.30 (n/a)</td><td>34.43 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-6.66%)</td><td>0.02 (-4.72%)</td><td>0.02 (-3.91%)</td><td>0.02 (+0.19%)</td><td>0.01 (-9.19%)</td><td>221.30 (-0.23%)</td><td>182.20 (+4.52%)</td><td>187.60 (+4.05%)</td><td>119.50 (+7.17%)</td><td>41.43 (+0.77%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>174.32 (n/a)</td><td>180.30 (n/a)</td><td>111.50 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-4.55%)</td><td>0.02 (-12.25%)</td><td>0.02 <b>(-20.09%)</b></td><td>0.02 (-18.12%)</td><td>0.00 <b>(+108.17%)</b></td><td>212.10 <b>(+22.11%)</b></td><td>189.92 (+15.73%)</td><td>208.60 <b>(+25.13%)</b></td><td>153.80 (+4.84%)</td><td>27.93 <b>(+173.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.70 (n/a)</td><td>164.10 (n/a)</td><td>166.70 (n/a)</td><td>146.70 (n/a)</td><td>10.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 <b>(-27.22%)</b></td><td>0.02 (-11.86%)</td><td>0.02 (-2.47%)</td><td>0.02 (-3.17%)</td><td>0.00 <b>(-43.01%)</b></td><td>232.10 (+3.29%)</td><td>192.72 (+11.37%)</td><td>172.80 (+2.49%)</td><td>172.20 <b>(+37.32%)</b></td><td>28.42 (-19.95%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>173.04 (n/a)</td><td>168.60 (n/a)</td><td>125.40 (n/a)</td><td>35.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (-17.37%)</td><td>0.02 (-9.99%)</td><td>0.02 (-11.57%)</td><td>0.02 (+5.08%)</td><td>0.00 <b>(-52.46%)</b></td><td>235.90 (-4.80%)</td><td>203.22 (+8.80%)</td><td>192.20 (+13.06%)</td><td>188.00 <b>(+20.98%)</b></td><td>20.26 <b>(-45.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.80 (n/a)</td><td>186.78 (n/a)</td><td>170.00 (n/a)</td><td>155.40 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-17.79%)</td><td>0.02 (-5.39%)</td><td>0.03 (-12.90%)</td><td>0.02 (+14.64%)</td><td>0.00 <b>(-67.16%)</b></td><td>202.30 (-12.76%)</td><td>171.76 (+0.08%)</td><td>163.80 (+14.79%)</td><td>159.70 <b>(+21.63%)</b></td><td>17.47 <b>(-64.64%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>171.62 (n/a)</td><td>142.70 (n/a)</td><td>131.30 (n/a)</td><td>49.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+13.43%)</td><td>0.02 (+0.48%)</td><td>0.02 (-12.56%)</td><td>0.02 (+4.99%)</td><td>0.01 <b>(+30.54%)</b></td><td>226.40 (-4.75%)</td><td>187.40 (+0.89%)</td><td>200.40 (+14.32%)</td><td>126.80 (-11.82%)</td><td>41.90 (+9.45%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.70 (n/a)</td><td>185.74 (n/a)</td><td>175.30 (n/a)</td><td>143.80 (n/a)</td><td>38.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(+33.20%)</b></td><td>0.02 (+4.49%)</td><td>0.02 (-9.02%)</td><td>0.02 (+6.16%)</td><td>0.01 <b>(+76.15%)</b></td><td>231.20 (-5.82%)</td><td>184.96 (-0.79%)</td><td>199.30 (+9.93%)</td><td>113.10 <b>(-24.95%)</b></td><td>48.04 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.50 (n/a)</td><td>186.44 (n/a)</td><td>181.30 (n/a)</td><td>150.70 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-31.24%)</b></td><td>0.04 (-12.97%)</td><td>0.04 (-6.29%)</td><td>0.04 (+15.34%)</td><td>0.00 <b>(-75.38%)</b></td><td>212.20 (-13.32%)</td><td>194.36 (+9.46%)</td><td>190.90 (+6.71%)</td><td>176.40 <b>(+45.42%)</b></td><td>14.22 <b>(-68.68%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>177.56 (n/a)</td><td>178.90 (n/a)</td><td>121.30 (n/a)</td><td>45.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-28.40%)</b></td><td>0.05 <b>(-20.38%)</b></td><td>0.05 <b>(-25.86%)</b></td><td>0.04 (-6.32%)</td><td>0.00 <b>(-67.29%)</b></td><td>198.00 (+6.74%)</td><td>178.56 <b>(+22.89%)</b></td><td>179.60 <b>(+34.83%)</b></td><td>164.70 <b>(+39.58%)</b></td><td>13.00 <b>(-51.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>145.30 (n/a)</td><td>133.20 (n/a)</td><td>118.00 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (-2.63%)</td><td>0.04 (+4.46%)</td><td>0.04 (+14.69%)</td><td>0.03 (-3.43%)</td><td>0.00 (+2.26%)</td><td>235.00 (+3.52%)</td><td>204.82 (-4.19%)</td><td>193.50 (-12.84%)</td><td>183.70 (+2.68%)</td><td>21.92 (+10.58%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.00 (n/a)</td><td>213.78 (n/a)</td><td>222.00 (n/a)</td><td>178.90 (n/a)</td><td>19.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-1.68%)</td><td>0.04 (+1.36%)</td><td>0.04 (+8.14%)</td><td>0.04 (-2.64%)</td><td>0.01 (+6.73%)</td><td>228.00 (+2.70%)</td><td>191.52 (-0.97%)</td><td>184.20 (-7.53%)</td><td>156.00 (+1.69%)</td><td>31.01 (+14.12%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>193.40 (n/a)</td><td>199.20 (n/a)</td><td>153.40 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-18.31%)</td><td>0.04 (-16.63%)</td><td>0.04 <b>(-24.13%)</b></td><td>0.04 (+5.55%)</td><td>0.00 <b>(-51.73%)</b></td><td>218.10 (-5.26%)</td><td>195.52 (+16.90%)</td><td>197.10 <b>(+31.84%)</b></td><td>169.50 <b>(+22.47%)</b></td><td>21.55 <b>(-43.68%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>167.26 (n/a)</td><td>149.50 (n/a)</td><td>138.40 (n/a)</td><td>38.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (-12.01%)</td><td>0.05 (-11.56%)</td><td>0.05 (-12.26%)</td><td>0.04 (-15.33%)</td><td>0.01 (-15.52%)</td><td>216.80 (+18.08%)</td><td>169.78 (+13.01%)</td><td>160.60 (+13.98%)</td><td>141.40 (+13.67%)</td><td>28.70 (+15.14%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>150.24 (n/a)</td><td>140.90 (n/a)</td><td>124.40 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-22.40%)</b></td><td>0.04 (-14.95%)</td><td>0.05 (+0.92%)</td><td>0.04 (-17.99%)</td><td>0.01 <b>(-35.80%)</b></td><td>232.90 <b>(+21.94%)</b></td><td>187.26 (+15.98%)</td><td>174.20 (-0.91%)</td><td>157.30 <b>(+28.83%)</b></td><td>33.70 (-0.45%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>161.46 (n/a)</td><td>175.80 (n/a)</td><td>122.10 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (-5.64%)</td><td>0.05 (+5.71%)</td><td>0.05 (+0.27%)</td><td>0.04 <b>(+64.73%)</b></td><td>0.01 <b>(-51.02%)</b></td><td>209.40 <b>(-39.30%)</b></td><td>173.68 (-13.13%)</td><td>173.20 (-0.23%)</td><td>142.90 (+6.01%)</td><td>24.15 <b>(-70.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.00 (n/a)</td><td>199.94 (n/a)</td><td>173.60 (n/a)</td><td>134.80 (n/a)</td><td>83.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-13.42%)</td><td>0.04 (-7.57%)</td><td>0.04 (-3.53%)</td><td>0.04 (-0.07%)</td><td>0.00 <b>(-39.16%)</b></td><td>218.80 (+0.09%)</td><td>194.26 (+7.21%)</td><td>184.80 (+3.65%)</td><td>175.20 (+15.49%)</td><td>18.43 <b>(-29.29%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>181.20 (n/a)</td><td>178.30 (n/a)</td><td>151.70 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-23.23%)</b></td><td>0.05 (-11.22%)</td><td>0.05 (+0.05%)</td><td>0.04 (+8.85%)</td><td>0.01 <b>(-56.62%)</b></td><td>209.40 (-8.16%)</td><td>181.00 (+8.45%)</td><td>165.80 (-0.06%)</td><td>162.80 <b>(+30.24%)</b></td><td>22.48 <b>(-46.89%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>166.90 (n/a)</td><td>165.90 (n/a)</td><td>125.00 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (+1.02%)</td><td>0.05 (-2.28%)</td><td>0.05 (-0.44%)</td><td>0.04 (-15.62%)</td><td>0.01 <b>(+68.97%)</b></td><td>216.70 (+18.48%)</td><td>175.12 (+3.58%)</td><td>169.70 (+0.47%)</td><td>146.80 (-1.01%)</td><td>26.59 <b>(+102.48%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>169.06 (n/a)</td><td>168.90 (n/a)</td><td>148.30 (n/a)</td><td>13.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-18.34%)</td><td>0.04 (-14.84%)</td><td>0.04 (-15.46%)</td><td>0.04 (-6.97%)</td><td>0.01 <b>(-35.06%)</b></td><td>219.10 (+7.51%)</td><td>194.50 (+16.31%)</td><td>195.70 (+18.32%)</td><td>164.10 <b>(+22.46%)</b></td><td>23.87 (-13.44%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>167.22 (n/a)</td><td>165.40 (n/a)</td><td>134.00 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (+5.19%)</td><td>0.04 (-2.93%)</td><td>0.04 (-6.44%)</td><td>0.03 (-10.07%)</td><td>0.01 <b>(+23.88%)</b></td><td>320.90 (+11.19%)</td><td>217.20 (+5.90%)</td><td>218.70 (+6.89%)</td><td>138.80 (-4.93%)</td><td>68.18 <b>(+28.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.60 (n/a)</td><td>205.10 (n/a)</td><td>204.60 (n/a)</td><td>146.00 (n/a)</td><td>52.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-14.33%)</td><td>0.04 (-6.74%)</td><td>0.04 (-2.21%)</td><td>0.04 (+8.12%)</td><td>0.01 <b>(-31.03%)</b></td><td>223.70 (-7.49%)</td><td>187.60 (+5.03%)</td><td>183.10 (+2.23%)</td><td>153.60 (+16.72%)</td><td>32.36 <b>(-24.49%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>178.62 (n/a)</td><td>179.10 (n/a)</td><td>131.60 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-10.71%)</td><td>0.04 (-10.24%)</td><td>0.04 (-8.59%)</td><td>0.04 (-7.38%)</td><td>0.01 <b>(-25.19%)</b></td><td>226.90 (+7.94%)</td><td>199.62 (+10.35%)</td><td>207.00 (+9.41%)</td><td>153.70 (+12.03%)</td><td>27.37 (-14.21%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>180.90 (n/a)</td><td>189.20 (n/a)</td><td>137.20 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-30.97%)</b></td><td>0.04 <b>(-20.23%)</b></td><td>0.04 (-14.90%)</td><td>0.04 (+1.56%)</td><td>0.00 <b>(-74.76%)</b></td><td>205.90 (-1.53%)</td><td>185.24 <b>(+20.50%)</b></td><td>184.30 (+17.46%)</td><td>168.50 <b>(+44.88%)</b></td><td>13.58 <b>(-63.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>153.72 (n/a)</td><td>156.90 (n/a)</td><td>116.30 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-12.89%)</td><td>0.10 (-4.42%)</td><td>0.10 (-8.48%)</td><td>0.09 <b>(+30.73%)</b></td><td>0.01 <b>(-55.08%)</b></td><td>177.10 <b>(-23.50%)</b></td><td>159.98 (+0.59%)</td><td>159.30 (+9.26%)</td><td>137.10 (+14.82%)</td><td>16.08 <b>(-62.30%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>159.04 (n/a)</td><td>145.80 (n/a)</td><td>119.40 (n/a)</td><td>42.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (-0.66%)</td><td>0.11 (+10.73%)</td><td>0.11 (+15.03%)</td><td>0.09 (+17.33%)</td><td>0.02 <b>(-27.17%)</b></td><td>184.30 (-14.79%)</td><td>154.60 (-11.35%)</td><td>152.30 (-13.07%)</td><td>124.00 (+0.65%)</td><td>21.89 <b>(-36.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>174.40 (n/a)</td><td>175.20 (n/a)</td><td>123.20 (n/a)</td><td>34.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (-6.39%)</td><td>0.08 (+4.64%)</td><td>0.08 (+0.96%)</td><td>0.07 <b>(+23.74%)</b></td><td>0.01 <b>(-50.32%)</b></td><td>242.30 (-19.18%)</td><td>218.32 (-7.30%)</td><td>218.10 (-0.95%)</td><td>185.80 (+6.84%)</td><td>21.51 <b>(-58.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>299.80 (n/a)</td><td>235.52 (n/a)</td><td>220.20 (n/a)</td><td>173.90 (n/a)</td><td>51.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (-9.51%)</td><td>0.09 (-2.43%)</td><td>0.09 (-3.45%)</td><td>0.07 <b>(+23.50%)</b></td><td>0.01 <b>(-40.49%)</b></td><td>222.10 (-19.03%)</td><td>186.72 (-0.86%)</td><td>181.30 (+3.60%)</td><td>154.40 (+10.52%)</td><td>25.72 <b>(-49.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>274.30 (n/a)</td><td>188.34 (n/a)</td><td>175.00 (n/a)</td><td>139.70 (n/a)</td><td>50.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-11.66%)</td><td>0.10 (-6.65%)</td><td>0.10 (-12.92%)</td><td>0.10 (+11.64%)</td><td>0.01 <b>(-56.41%)</b></td><td>172.20 (-10.41%)</td><td>158.58 (+4.14%)</td><td>158.10 (+14.81%)</td><td>137.70 (+13.24%)</td><td>14.37 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>152.28 (n/a)</td><td>137.70 (n/a)</td><td>121.60 (n/a)</td><td>32.63 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-18.67%)</td><td>0.10 (-10.24%)</td><td>0.10 (-6.57%)</td><td>0.09 (-5.03%)</td><td>0.01 <b>(-43.34%)</b></td><td>191.90 (+5.27%)</td><td>167.44 (+9.47%)</td><td>169.50 (+7.01%)</td><td>136.00 <b>(+22.85%)</b></td><td>20.15 <b>(-26.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>152.96 (n/a)</td><td>158.40 (n/a)</td><td>110.70 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-8.36%)</td><td>0.09 (-4.29%)</td><td>0.09 (-0.26%)</td><td>0.08 (-10.27%)</td><td>0.02 (+12.34%)</td><td>216.50 (+11.48%)</td><td>178.56 (+5.68%)</td><td>175.10 (+0.23%)</td><td>141.30 (+9.11%)</td><td>35.04 <b>(+40.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.20 (n/a)</td><td>168.96 (n/a)</td><td>174.70 (n/a)</td><td>129.50 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-11.99%)</td><td>0.10 (-2.29%)</td><td>0.10 (+0.68%)</td><td>0.08 (+2.79%)</td><td>0.01 <b>(-36.21%)</b></td><td>193.30 (-2.72%)</td><td>164.64 (+0.98%)</td><td>163.00 (-0.67%)</td><td>138.80 (+13.58%)</td><td>20.02 <b>(-27.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>163.04 (n/a)</td><td>164.10 (n/a)</td><td>122.20 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-11.66%)</td><td>0.10 (+1.52%)</td><td>0.10 <b>(+23.04%)</b></td><td>0.08 (-1.52%)</td><td>0.02 <b>(-26.34%)</b></td><td>209.30 (+1.50%)</td><td>172.32 (-2.82%)</td><td>158.90 (-18.72%)</td><td>140.80 (+13.18%)</td><td>30.01 (-14.49%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>177.32 (n/a)</td><td>195.50 (n/a)</td><td>124.40 (n/a)</td><td>35.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (+14.13%)</td><td>0.10 (+11.13%)</td><td>0.10 (+15.09%)</td><td>0.09 (+8.42%)</td><td>0.01 <b>(+72.45%)</b></td><td>190.70 (-7.74%)</td><td>167.92 (-9.38%)</td><td>157.00 (-13.12%)</td><td>149.60 (-12.36%)</td><td>20.65 <b>(+41.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>185.30 (n/a)</td><td>180.70 (n/a)</td><td>170.70 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (+2.62%)</td><td>0.09 (-0.42%)</td><td>0.08 (-8.78%)</td><td>0.07 (+15.20%)</td><td>0.01 <b>(-28.87%)</b></td><td>218.80 (-13.17%)</td><td>190.66 (-0.78%)</td><td>193.20 (+9.65%)</td><td>167.00 (-2.57%)</td><td>20.22 <b>(-40.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>252.00 (n/a)</td><td>192.16 (n/a)</td><td>176.20 (n/a)</td><td>171.40 (n/a)</td><td>34.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (+6.59%)</td><td>0.09 (-5.03%)</td><td>0.09 (-6.23%)</td><td>0.07 (-0.16%)</td><td>0.02 (+11.95%)</td><td>239.90 (+0.17%)</td><td>193.72 (+5.63%)</td><td>188.30 (+6.63%)</td><td>146.50 (-6.21%)</td><td>34.19 (+2.61%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>183.40 (n/a)</td><td>176.60 (n/a)</td><td>156.20 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (-3.64%)</td><td>0.08 (-0.67%)</td><td>0.08 (-3.04%)</td><td>0.07 <b>(+27.90%)</b></td><td>0.01 <b>(-41.43%)</b></td><td>250.70 <b>(-21.83%)</b></td><td>206.58 (-3.60%)</td><td>204.90 (+3.17%)</td><td>166.30 (+3.81%)</td><td>30.25 <b>(-53.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>320.70 (n/a)</td><td>214.30 (n/a)</td><td>198.60 (n/a)</td><td>160.20 (n/a)</td><td>64.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (-1.77%)</td><td>0.09 (+6.38%)</td><td>0.09 (+12.82%)</td><td>0.08 (+10.31%)</td><td>0.01 <b>(-24.41%)</b></td><td>217.50 (-9.34%)</td><td>187.72 (-7.19%)</td><td>184.60 (-11.38%)</td><td>158.50 (+1.80%)</td><td>25.27 <b>(-30.25%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.90 (n/a)</td><td>202.26 (n/a)</td><td>208.30 (n/a)</td><td>155.70 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (+0.67%)</td><td>0.09 (+13.10%)</td><td>0.10 (+19.53%)</td><td>0.07 (+9.63%)</td><td>0.02 (-5.38%)</td><td>239.20 (-8.81%)</td><td>184.00 (-12.31%)</td><td>167.10 (-16.37%)</td><td>153.90 (-0.65%)</td><td>37.22 (-17.89%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>262.30 (n/a)</td><td>209.84 (n/a)</td><td>199.80 (n/a)</td><td>154.90 (n/a)</td><td>45.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (-5.67%)</td><td>0.08 (-14.41%)</td><td>0.09 (-9.49%)</td><td>0.06 <b>(-27.50%)</b></td><td>0.02 <b>(+42.72%)</b></td><td>282.20 <b>(+37.93%)</b></td><td>205.58 <b>(+20.93%)</b></td><td>186.00 (+10.52%)</td><td>145.30 (+5.98%)</td><td>53.17 <b>(+112.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>170.00 (n/a)</td><td>168.30 (n/a)</td><td>137.10 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (+5.31%)</td><td>0.21 (-4.57%)</td><td>0.19 (-12.02%)</td><td>0.17 (+6.29%)</td><td>0.04 (-5.30%)</td><td>194.70 (-5.90%)</td><td>164.78 (+3.86%)</td><td>170.90 (+13.71%)</td><td>116.10 (-4.99%)</td><td>29.45 (-18.62%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>206.90 (n/a)</td><td>158.66 (n/a)</td><td>150.30 (n/a)</td><td>122.20 (n/a)</td><td>36.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-13.26%)</td><td>0.19 (-8.77%)</td><td>0.18 (-4.18%)</td><td>0.15 (-17.29%)</td><td>0.02 (-7.24%)</td><td>214.50 <b>(+20.91%)</b></td><td>177.72 (+9.87%)</td><td>180.00 (+4.41%)</td><td>152.40 (+15.28%)</td><td>24.27 <b>(+29.26%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.40 (n/a)</td><td>161.76 (n/a)</td><td>172.40 (n/a)</td><td>132.20 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.18 (+3.99%)</td><td>0.12 <b>(-23.61%)</b></td><td>0.10 <b>(-34.96%)</b></td><td>0.10 <b>(-30.09%)</b></td><td>0.04 <b>(+136.43%)</b></td><td>344.40 <b>(+43.02%)</b></td><td>298.80 <b>(+37.99%)</b></td><td>337.30 <b>(+53.81%)</b></td><td>180.10 (-3.84%)</td><td>69.61 <b>(+221.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>240.80 (n/a)</td><td>216.54 (n/a)</td><td>219.30 (n/a)</td><td>187.30 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (-13.91%)</td><td>0.17 (-2.91%)</td><td>0.16 (-0.34%)</td><td>0.15 (+2.76%)</td><td>0.02 <b>(-39.78%)</b></td><td>219.30 (-2.66%)</td><td>198.68 (+1.63%)</td><td>202.20 (+0.35%)</td><td>171.50 (+16.11%)</td><td>21.68 <b>(-30.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.30 (n/a)</td><td>195.50 (n/a)</td><td>201.50 (n/a)</td><td>147.70 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-14.43%)</td><td>0.17 (-16.08%)</td><td>0.18 (-15.60%)</td><td>0.15 (-7.19%)</td><td>0.03 (-19.37%)</td><td>224.60 (+7.77%)</td><td>192.66 (+18.71%)</td><td>182.70 (+18.48%)</td><td>157.30 (+16.86%)</td><td>27.70 (+0.16%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.40 (n/a)</td><td>162.30 (n/a)</td><td>154.20 (n/a)</td><td>134.60 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (-5.40%)</td><td>0.19 (-3.27%)</td><td>0.19 (-2.37%)</td><td>0.18 (+4.16%)</td><td>0.03 <b>(-20.70%)</b></td><td>185.90 (-3.98%)</td><td>171.16 (+2.69%)</td><td>176.30 (+2.44%)</td><td>136.80 (+5.72%)</td><td>19.73 (-19.85%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.60 (n/a)</td><td>166.68 (n/a)</td><td>172.10 (n/a)</td><td>129.40 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 <b>(-20.78%)</b></td><td>0.15 <b>(-26.74%)</b></td><td>0.15 <b>(-25.54%)</b></td><td>0.10 <b>(-42.15%)</b></td><td>0.04 (+14.17%)</td><td>343.40 <b>(+72.82%)</b></td><td>230.62 <b>(+42.41%)</b></td><td>217.00 <b>(+34.37%)</b></td><td>165.90 <b>(+26.16%)</b></td><td>70.83 <b>(+151.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>161.94 (n/a)</td><td>161.50 (n/a)</td><td>131.50 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (+8.21%)</td><td>0.18 (-13.20%)</td><td>0.18 (-14.05%)</td><td>0.09 <b>(-48.37%)</b></td><td>0.08 <b>(+102.17%)</b></td><td>377.70 <b>(+93.69%)</b></td><td>211.18 <b>(+32.25%)</b></td><td>185.70 (+16.35%)</td><td>113.70 (-7.56%)</td><td>102.27 <b>(+273.62%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.00 (n/a)</td><td>159.68 (n/a)</td><td>159.60 (n/a)</td><td>123.00 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-7.14%)</td><td>0.17 (-10.64%)</td><td>0.16 <b>(-21.66%)</b></td><td>0.12 (+14.32%)</td><td>0.04 (-16.90%)</td><td>270.80 (-12.53%)</td><td>207.16 (+8.77%)</td><td>204.60 <b>(+27.72%)</b></td><td>158.40 (+7.68%)</td><td>49.76 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>309.60 (n/a)</td><td>190.46 (n/a)</td><td>160.20 (n/a)</td><td>147.10 (n/a)</td><td>67.95 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 <b>(+35.75%)</b></td><td>0.20 (+5.84%)</td><td>0.19 (+2.57%)</td><td>0.14 (-16.16%)</td><td>0.05 <b>(+261.55%)</b></td><td>238.70 (+19.29%)</td><td>175.82 (-1.53%)</td><td>169.70 (-2.53%)</td><td>122.20 <b>(-26.34%)</b></td><td>41.82 <b>(+213.62%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>178.56 (n/a)</td><td>174.10 (n/a)</td><td>165.90 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (-9.98%)</td><td>0.17 (-11.69%)</td><td>0.17 (-16.76%)</td><td>0.13 <b>(-21.49%)</b></td><td>0.03 <b>(+20.47%)</b></td><td>247.00 <b>(+27.39%)</b></td><td>196.32 (+14.46%)</td><td>198.40 <b>(+20.17%)</b></td><td>164.10 (+11.10%)</td><td>33.28 <b>(+64.86%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.90 (n/a)</td><td>171.52 (n/a)</td><td>165.10 (n/a)</td><td>147.70 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-0.55%)</td><td>0.16 (-18.80%)</td><td>0.19 (-2.99%)</td><td>0.09 <b>(-45.27%)</b></td><td>0.06 <b>(+252.66%)</b></td><td>348.80 <b>(+82.71%)</b></td><td>237.40 <b>(+40.14%)</b></td><td>175.70 (+3.11%)</td><td>154.10 (+0.59%)</td><td>100.90 <b>(+578.34%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>169.40 (n/a)</td><td>170.40 (n/a)</td><td>153.20 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (-4.65%)</td><td>0.18 (-10.19%)</td><td>0.18 (-6.75%)</td><td>0.12 <b>(-27.07%)</b></td><td>0.03 <b>(+53.30%)</b></td><td>264.80 <b>(+37.13%)</b></td><td>192.00 (+14.15%)</td><td>183.70 (+7.24%)</td><td>148.80 (+4.86%)</td><td>43.23 <b>(+132.40%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.10 (n/a)</td><td>168.20 (n/a)</td><td>171.30 (n/a)</td><td>141.90 (n/a)</td><td>18.60 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 <b>(+23.36%)</b></td><td>0.16 (-12.69%)</td><td>0.15 (-18.34%)</td><td>0.09 <b>(-42.63%)</b></td><td>0.06 <b>(+229.72%)</b></td><td>367.20 <b>(+74.28%)</b></td><td>235.12 <b>(+27.52%)</b></td><td>224.40 <b>(+22.42%)</b></td><td>129.00 (-18.92%)</td><td>87.70 <b>(+360.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>184.38 (n/a)</td><td>183.30 (n/a)</td><td>159.10 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (+8.50%)</td><td>0.17 (+8.79%)</td><td>0.16 (+11.06%)</td><td>0.14 (+11.92%)</td><td>0.03 (-15.10%)</td><td>235.70 (-10.65%)</td><td>196.52 (-9.36%)</td><td>200.10 (-9.95%)</td><td>153.50 (-7.86%)</td><td>30.00 <b>(-31.08%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>263.80 (n/a)</td><td>216.82 (n/a)</td><td>222.20 (n/a)</td><td>166.60 (n/a)</td><td>43.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (+11.35%)</td><td>0.17 (-1.32%)</td><td>0.18 (+2.28%)</td><td>0.13 (-14.58%)</td><td>0.03 <b>(+118.39%)</b></td><td>250.20 (+17.08%)</td><td>193.90 (+3.69%)</td><td>178.20 (-2.20%)</td><td>152.10 (-10.21%)</td><td>37.82 <b>(+129.52%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>187.00 (n/a)</td><td>182.20 (n/a)</td><td>169.40 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.13%)</td><td>0.21 (-0.15%)</td><td>0.21 (-0.17%)</td><td>0.20 (-0.13%)</td><td>0.00 (+4.71%)</td><td>40958.10 (+0.14%)</td><td>40915.30 (+0.15%)</td><td>40918.30 (+0.17%)</td><td>40860.30 (+0.13%)</td><td>38.74 (+5.11%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40902.80 (n/a)</td><td>40854.42 (n/a)</td><td>40850.10 (n/a)</td><td>40806.80 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-0.56%)</td><td>0.21 (-0.08%)</td><td>0.21 (+0.05%)</td><td>0.21 (+0.03%)</td><td>0.00 <b>(-68.21%)</b></td><td>40883.90 (-0.03%)</td><td>40838.70 (+0.08%)</td><td>40856.30 (-0.05%)</td><td>40779.70 (+0.56%)</td><td>46.63 <b>(-68.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40896.60 (n/a)</td><td>40806.44 (n/a)</td><td>40877.50 (n/a)</td><td>40552.10 (n/a)</td><td>145.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+0.05%)</td><td>0.13 (+0.03%)</td><td>0.13 (+0.08%)</td><td>0.13 (-0.06%)</td><td>0.00 <b>(+105.19%)</b></td><td>322554.50 (+0.06%)</td><td>322126.10 (-0.03%)</td><td>321997.90 (-0.08%)</td><td>321880.20 (-0.05%)</td><td>284.43 <b>(+105.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>322375.00 (n/a)</td><td>322208.68 (n/a)</td><td>322255.30 (n/a)</td><td>322049.60 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-28.67%)</b></td><td>0.02 <b>(-23.78%)</b></td><td>0.02 <b>(-24.78%)</b></td><td>0.02 <b>(-20.04%)</b></td><td>0.00 <b>(-47.03%)</b></td><td>197.70 <b>(+25.05%)</b></td><td>173.72 <b>(+29.87%)</b></td><td>178.30 <b>(+32.96%)</b></td><td>152.30 <b>(+40.11%)</b></td><td>19.06 (-8.68%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>158.10 (n/a)</td><td>133.76 (n/a)</td><td>134.10 (n/a)</td><td>108.70 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (-12.37%)</td><td>0.03 <b>(-27.12%)</b></td><td>0.03 <b>(-31.63%)</b></td><td>0.02 <b>(-56.95%)</b></td><td>0.01 <b>(+164.35%)</b></td><td>347.20 <b>(+132.24%)</b></td><td>204.50 <b>(+51.86%)</b></td><td>190.00 <b>(+46.27%)</b></td><td>137.80 (+14.07%)</td><td>84.54 <b>(+599.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>149.50 (n/a)</td><td>134.66 (n/a)</td><td>129.90 (n/a)</td><td>120.80 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-13.94%)</td><td>0.02 (-14.48%)</td><td>0.02 <b>(-20.95%)</b></td><td>0.02 (+9.83%)</td><td>0.00 <b>(-49.12%)</b></td><td>210.60 (-8.99%)</td><td>185.02 (+13.22%)</td><td>177.90 <b>(+26.44%)</b></td><td>153.90 (+16.15%)</td><td>23.06 <b>(-45.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>163.42 (n/a)</td><td>140.70 (n/a)</td><td>132.50 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-20.83%)</b></td><td>0.03 (-10.18%)</td><td>0.03 (+5.39%)</td><td>0.02 (-1.02%)</td><td>0.00 <b>(-53.37%)</b></td><td>208.90 (+1.02%)</td><td>181.36 (+6.73%)</td><td>180.10 (-5.11%)</td><td>148.80 <b>(+26.32%)</b></td><td>25.77 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>169.92 (n/a)</td><td>189.80 (n/a)</td><td>117.80 (n/a)</td><td>43.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+3.47%)</td><td>0.03 (-6.93%)</td><td>0.03 (-4.38%)</td><td>0.02 (-14.96%)</td><td>0.00 <b>(+121.61%)</b></td><td>183.00 (+17.53%)</td><td>160.24 (+8.59%)</td><td>157.60 (+4.58%)</td><td>131.10 (-3.32%)</td><td>19.69 <b>(+149.94%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.70 (n/a)</td><td>147.56 (n/a)</td><td>150.70 (n/a)</td><td>135.60 (n/a)</td><td>7.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-1.18%)</td><td>0.03 (-1.55%)</td><td>0.03 (+4.44%)</td><td>0.02 <b>(-28.80%)</b></td><td>0.01 <b>(+68.77%)</b></td><td>329.00 <b>(+40.42%)</b></td><td>205.88 (+7.01%)</td><td>174.80 (-4.22%)</td><td>161.00 (+1.19%)</td><td>70.34 <b>(+144.15%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.30 (n/a)</td><td>192.40 (n/a)</td><td>182.50 (n/a)</td><td>159.10 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+1.81%)</td><td>0.03 (-1.66%)</td><td>0.02 (-5.25%)</td><td>0.02 (-8.60%)</td><td>0.01 (+11.94%)</td><td>222.20 (+9.40%)</td><td>164.90 (+2.73%)</td><td>168.40 (+5.51%)</td><td>124.80 (-1.81%)</td><td>37.93 <b>(+21.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>160.52 (n/a)</td><td>159.60 (n/a)</td><td>127.10 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(-26.91%)</b></td><td>0.02 (-16.98%)</td><td>0.02 <b>(-21.48%)</b></td><td>0.02 (-0.45%)</td><td>0.00 <b>(-64.54%)</b></td><td>239.30 (+0.46%)</td><td>201.24 (+15.59%)</td><td>192.40 <b>(+27.33%)</b></td><td>183.50 <b>(+36.84%)</b></td><td>22.50 <b>(-50.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>174.10 (n/a)</td><td>151.10 (n/a)</td><td>134.10 (n/a)</td><td>45.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+6.50%)</td><td>0.02 (-3.16%)</td><td>0.02 (-2.79%)</td><td>0.02 (-12.21%)</td><td>0.00 <b>(+85.32%)</b></td><td>217.90 (+13.90%)</td><td>182.36 (+4.93%)</td><td>178.00 (+2.89%)</td><td>143.70 (-6.14%)</td><td>29.69 <b>(+100.06%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.30 (n/a)</td><td>173.80 (n/a)</td><td>173.00 (n/a)</td><td>153.10 (n/a)</td><td>14.84 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (-0.99%)</td><td>0.02 (+8.44%)</td><td>0.02 (+9.88%)</td><td>0.02 <b>(+29.53%)</b></td><td>0.00 <b>(-36.04%)</b></td><td>214.70 <b>(-22.80%)</b></td><td>189.02 (-10.04%)</td><td>195.60 (-9.02%)</td><td>156.80 (+1.03%)</td><td>22.39 <b>(-50.67%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>278.10 (n/a)</td><td>210.12 (n/a)</td><td>215.00 (n/a)</td><td>155.20 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (-0.67%)</td><td>0.02 (-4.27%)</td><td>0.02 (+0.38%)</td><td>0.01 <b>(-32.00%)</b></td><td>0.00 <b>(+102.92%)</b></td><td>318.00 <b>(+47.09%)</b></td><td>218.34 (+9.01%)</td><td>205.50 (-0.39%)</td><td>168.00 (+0.72%)</td><td>60.02 <b>(+210.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.20 (n/a)</td><td>200.30 (n/a)</td><td>206.30 (n/a)</td><td>166.80 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (-20.00%)</td><td>0.02 (-13.71%)</td><td>0.02 (-7.81%)</td><td>0.02 (-7.38%)</td><td>0.00 <b>(-53.86%)</b></td><td>232.70 (+7.98%)</td><td>213.70 (+14.51%)</td><td>211.90 (+8.50%)</td><td>190.90 <b>(+25.02%)</b></td><td>16.67 <b>(-37.11%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>186.62 (n/a)</td><td>195.30 (n/a)</td><td>152.70 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 (+7.37%)</td><td>0.02 (+9.38%)</td><td>0.02 (+4.50%)</td><td>0.02 (+15.23%)</td><td>0.00 (-3.49%)</td><td>204.80 (-13.22%)</td><td>182.56 (-8.92%)</td><td>189.30 (-4.30%)</td><td>153.20 (-6.87%)</td><td>21.47 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.00 (n/a)</td><td>200.44 (n/a)</td><td>197.80 (n/a)</td><td>164.50 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.02 (-19.78%)</td><td>0.02 (-1.29%)</td><td>0.02 (-3.88%)</td><td>0.02 <b>(+22.77%)</b></td><td>0.00 <b>(-77.57%)</b></td><td>227.10 (-18.57%)</td><td>213.46 (-2.19%)</td><td>211.00 (+4.04%)</td><td>199.40 <b>(+24.70%)</b></td><td>10.47 <b>(-77.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>278.90 (n/a)</td><td>218.24 (n/a)</td><td>202.80 (n/a)</td><td>159.90 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.03 <b>(+26.08%)</b></td><td>0.02 (+2.54%)</td><td>0.02 (-13.19%)</td><td>0.01 (-10.53%)</td><td>0.01 <b>(+184.60%)</b></td><td>273.20 (+11.78%)</td><td>216.26 (+2.23%)</td><td>234.80 (+15.15%)</td><td>150.80 <b>(-20.72%)</b></td><td>54.12 <b>(+149.34%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.40 (n/a)</td><td>211.54 (n/a)</td><td>203.90 (n/a)</td><td>190.20 (n/a)</td><td>21.70 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (+2.57%)</td><td>0.05 (-2.20%)</td><td>0.05 (-1.27%)</td><td>0.04 (+5.84%)</td><td>0.01 (-15.09%)</td><td>206.40 (-5.54%)</td><td>177.52 (+1.58%)</td><td>178.00 (+1.31%)</td><td>145.00 (-2.49%)</td><td>22.79 <b>(-20.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>174.76 (n/a)</td><td>175.70 (n/a)</td><td>148.70 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.08 <b>(-21.35%)</b></td><td>0.07 (-7.94%)</td><td>0.07 (-1.87%)</td><td>0.06 (+19.47%)</td><td>0.01 <b>(-64.44%)</b></td><td>207.30 (-16.31%)</td><td>184.48 (+2.90%)</td><td>182.60 (+1.90%)</td><td>161.60 <b>(+27.14%)</b></td><td>19.74 <b>(-60.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>247.70 (n/a)</td><td>179.28 (n/a)</td><td>179.20 (n/a)</td><td>127.10 (n/a)</td><td>50.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (-14.74%)</td><td>0.04 (-2.95%)</td><td>0.04 (-3.40%)</td><td>0.04 (+17.38%)</td><td>0.00 <b>(-61.16%)</b></td><td>224.10 (-14.79%)</td><td>195.46 (+0.22%)</td><td>189.10 (+3.50%)</td><td>183.80 (+17.29%)</td><td>16.32 <b>(-61.14%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.00 (n/a)</td><td>195.04 (n/a)</td><td>182.70 (n/a)</td><td>156.70 (n/a)</td><td>41.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (-15.32%)</td><td>0.05 (-9.51%)</td><td>0.05 (-11.18%)</td><td>0.05 (-8.10%)</td><td>0.00 <b>(-27.47%)</b></td><td>210.00 (+8.86%)</td><td>193.70 (+10.27%)</td><td>198.90 (+12.63%)</td><td>176.40 (+18.07%)</td><td>15.24 (-5.61%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>175.66 (n/a)</td><td>176.60 (n/a)</td><td>149.40 (n/a)</td><td>16.14 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-7.35%)</td><td>0.05 (-7.42%)</td><td>0.05 (-8.48%)</td><td>0.04 (+2.23%)</td><td>0.00 <b>(-39.95%)</b></td><td>199.30 (-2.16%)</td><td>178.02 (+7.16%)</td><td>175.30 (+9.29%)</td><td>160.40 (+7.94%)</td><td>14.27 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>166.12 (n/a)</td><td>160.40 (n/a)</td><td>148.60 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 <b>(-35.37%)</b></td><td>0.05 <b>(-25.65%)</b></td><td>0.05 (-13.15%)</td><td>0.04 <b>(-20.62%)</b></td><td>0.01 <b>(-58.18%)</b></td><td>251.00 <b>(+26.00%)</b></td><td>210.28 <b>(+30.48%)</b></td><td>201.50 (+15.14%)</td><td>174.10 <b>(+54.76%)</b></td><td>30.21 (-17.77%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>199.20 (n/a)</td><td>161.16 (n/a)</td><td>175.00 (n/a)</td><td>112.50 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-29.70%)</b></td><td>0.04 <b>(-20.26%)</b></td><td>0.04 <b>(-23.44%)</b></td><td>0.03 (-7.75%)</td><td>0.01 <b>(-43.28%)</b></td><td>245.20 (+8.40%)</td><td>208.52 <b>(+22.83%)</b></td><td>219.40 <b>(+30.60%)</b></td><td>171.50 <b>(+42.32%)</b></td><td>33.11 (-14.03%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>169.76 (n/a)</td><td>168.00 (n/a)</td><td>120.50 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.06 (-16.25%)</td><td>0.05 <b>(-22.83%)</b></td><td>0.05 <b>(-24.98%)</b></td><td>0.04 <b>(-24.86%)</b></td><td>0.01 <b>(+20.44%)</b></td><td>216.20 <b>(+33.05%)</b></td><td>196.34 <b>(+30.44%)</b></td><td>199.30 <b>(+33.31%)</b></td><td>159.80 (+19.43%)</td><td>22.70 <b>(+87.69%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>162.50 (n/a)</td><td>150.52 (n/a)</td><td>149.50 (n/a)</td><td>133.80 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-6.91%)</td><td>0.04 (-8.69%)</td><td>0.04 (-7.81%)</td><td>0.03 (-12.81%)</td><td>0.01 (+0.44%)</td><td>252.80 (+14.70%)</td><td>204.80 (+10.00%)</td><td>202.20 (+8.48%)</td><td>163.90 (+7.48%)</td><td>34.66 <b>(+23.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>186.18 (n/a)</td><td>186.40 (n/a)</td><td>152.50 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-37.40%)</b></td><td>0.04 <b>(-23.89%)</b></td><td>0.04 (-15.86%)</td><td>0.04 (-14.24%)</td><td>0.00 <b>(-78.51%)</b></td><td>218.20 (+16.62%)</td><td>207.36 <b>(+28.17%)</b></td><td>209.50 (+18.83%)</td><td>191.90 <b>(+59.78%)</b></td><td>11.24 <b>(-59.77%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>161.78 (n/a)</td><td>176.30 (n/a)</td><td>120.10 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 <b>(-22.38%)</b></td><td>0.04 (-13.14%)</td><td>0.04 (-9.31%)</td><td>0.03 (-13.04%)</td><td>0.00 <b>(-39.57%)</b></td><td>249.00 (+15.01%)</td><td>205.54 (+14.09%)</td><td>201.70 (+10.28%)</td><td>178.40 <b>(+28.90%)</b></td><td>26.48 (-6.72%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>180.16 (n/a)</td><td>182.90 (n/a)</td><td>138.40 (n/a)</td><td>28.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 (-19.87%)</td><td>0.04 (-11.19%)</td><td>0.04 (-9.24%)</td><td>0.02 <b>(-23.36%)</b></td><td>0.01 (-10.20%)</td><td>389.70 <b>(+30.47%)</b></td><td>254.44 (+14.22%)</td><td>224.90 (+10.19%)</td><td>202.80 <b>(+24.80%)</b></td><td>77.50 <b>(+48.48%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>298.70 (n/a)</td><td>222.76 (n/a)</td><td>204.10 (n/a)</td><td>162.50 (n/a)</td><td>52.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.05 (-9.76%)</td><td>0.04 (-14.27%)</td><td>0.04 (-4.54%)</td><td>0.03 <b>(-20.25%)</b></td><td>0.01 <b>(-20.02%)</b></td><td>264.10 <b>(+25.34%)</b></td><td>206.76 (+16.16%)</td><td>206.50 (+4.77%)</td><td>152.70 (+10.81%)</td><td>40.69 (+12.10%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>178.00 (n/a)</td><td>197.10 (n/a)</td><td>137.80 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-26.78%)</b></td><td>0.04 (-12.55%)</td><td>0.04 (-15.71%)</td><td>0.04 (+3.47%)</td><td>0.00 <b>(-92.18%)</b></td><td>227.20 (-3.36%)</td><td>223.08 (+12.20%)</td><td>223.20 (+18.60%)</td><td>218.60 <b>(+36.62%)</b></td><td>3.08 <b>(-89.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>198.82 (n/a)</td><td>188.20 (n/a)</td><td>160.00 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.04 <b>(-30.12%)</b></td><td>0.04 (-15.46%)</td><td>0.04 (-10.92%)</td><td>0.03 (-17.07%)</td><td>0.00 <b>(-47.34%)</b></td><td>287.40 <b>(+20.60%)</b></td><td>231.46 (+16.51%)</td><td>229.60 (+12.27%)</td><td>205.10 <b>(+43.13%)</b></td><td>33.58 (-6.76%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>198.66 (n/a)</td><td>204.50 (n/a)</td><td>143.30 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 <b>(-22.59%)</b></td><td>0.09 <b>(-22.02%)</b></td><td>0.09 <b>(-21.31%)</b></td><td>0.07 <b>(-27.90%)</b></td><td>0.01 (-10.92%)</td><td>233.50 <b>(+38.74%)</b></td><td>190.70 <b>(+28.92%)</b></td><td>185.70 <b>(+27.10%)</b></td><td>159.70 <b>(+29.21%)</b></td><td>29.12 <b>(+58.56%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>168.30 (n/a)</td><td>147.92 (n/a)</td><td>146.10 (n/a)</td><td>123.60 (n/a)</td><td>18.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 <b>(-24.14%)</b></td><td>0.13 (-19.11%)</td><td>0.12 <b>(-26.39%)</b></td><td>0.12 (+6.55%)</td><td>0.01 <b>(-63.67%)</b></td><td>205.10 (-6.13%)</td><td>194.50 (+18.95%)</td><td>202.90 <b>(+35.90%)</b></td><td>162.90 <b>(+31.90%)</b></td><td>17.91 <b>(-55.67%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>218.50 (n/a)</td><td>163.52 (n/a)</td><td>149.30 (n/a)</td><td>123.50 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (+3.51%)</td><td>0.09 (-15.23%)</td><td>0.09 (-16.52%)</td><td>0.07 <b>(-21.66%)</b></td><td>0.02 <b>(+63.99%)</b></td><td>230.00 <b>(+27.64%)</b></td><td>187.90 <b>(+21.52%)</b></td><td>191.20 (+19.80%)</td><td>125.60 (-3.38%)</td><td>39.76 <b>(+97.68%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>154.62 (n/a)</td><td>159.60 (n/a)</td><td>130.00 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 <b>(-30.51%)</b></td><td>0.11 (-8.57%)</td><td>0.11 (-0.78%)</td><td>0.10 (+14.98%)</td><td>0.01 <b>(-72.09%)</b></td><td>211.10 (-13.02%)</td><td>184.54 (+4.50%)</td><td>179.30 (+0.79%)</td><td>173.30 <b>(+43.94%)</b></td><td>15.63 <b>(-64.69%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.70 (n/a)</td><td>176.60 (n/a)</td><td>177.90 (n/a)</td><td>120.40 (n/a)</td><td>44.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (+7.71%)</td><td>0.09 (-7.52%)</td><td>0.09 (-10.30%)</td><td>0.08 (-12.83%)</td><td>0.02 <b>(+87.40%)</b></td><td>202.30 (+14.75%)</td><td>178.62 (+10.38%)</td><td>182.70 (+11.47%)</td><td>127.40 (-7.14%)</td><td>30.21 <b>(+97.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>161.82 (n/a)</td><td>163.90 (n/a)</td><td>137.20 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 <b>(-23.91%)</b></td><td>0.11 (+1.43%)</td><td>0.12 <b>(+24.81%)</b></td><td>0.10 (+17.76%)</td><td>0.01 <b>(-79.07%)</b></td><td>197.90 (-15.06%)</td><td>178.98 (-6.49%)</td><td>173.50 (-19.86%)</td><td>172.10 <b>(+31.47%)</b></td><td>10.91 <b>(-76.91%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>233.00 (n/a)</td><td>191.40 (n/a)</td><td>216.50 (n/a)</td><td>130.90 (n/a)</td><td>47.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (-17.71%)</td><td>0.08 (-15.67%)</td><td>0.08 (-11.62%)</td><td>0.07 (-19.65%)</td><td>0.01 (+12.95%)</td><td>219.30 <b>(+24.39%)</b></td><td>198.06 (+19.03%)</td><td>193.60 (+13.15%)</td><td>179.40 <b>(+21.54%)</b></td><td>19.40 <b>(+73.03%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>166.40 (n/a)</td><td>171.10 (n/a)</td><td>147.60 (n/a)</td><td>11.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (+0.66%)</td><td>0.10 (+8.86%)</td><td>0.11 (+16.33%)</td><td>0.08 (+13.34%)</td><td>0.01 <b>(-26.83%)</b></td><td>217.10 (-11.75%)</td><td>178.06 (-9.21%)</td><td>169.60 (-14.04%)</td><td>158.90 (-0.63%)</td><td>22.62 <b>(-33.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.00 (n/a)</td><td>196.12 (n/a)</td><td>197.30 (n/a)</td><td>159.90 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (+0.82%)</td><td>0.10 (-6.77%)</td><td>0.10 (-9.64%)</td><td>0.09 (-8.96%)</td><td>0.02 <b>(+36.80%)</b></td><td>185.10 (+9.85%)</td><td>161.24 (+8.48%)</td><td>166.90 (+10.68%)</td><td>123.20 (-0.81%)</td><td>25.29 <b>(+50.34%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>148.64 (n/a)</td><td>150.80 (n/a)</td><td>124.20 (n/a)</td><td>16.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (-3.96%)</td><td>0.10 (+0.53%)</td><td>0.10 (+4.34%)</td><td>0.08 (+9.69%)</td><td>0.01 <b>(-25.62%)</b></td><td>240.10 (-8.81%)</td><td>191.02 (-2.11%)</td><td>186.60 (-4.16%)</td><td>164.10 (+4.12%)</td><td>30.75 <b>(-28.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>263.30 (n/a)</td><td>195.14 (n/a)</td><td>194.70 (n/a)</td><td>157.60 (n/a)</td><td>42.93 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 (-8.86%)</td><td>0.08 (-13.51%)</td><td>0.08 (-11.64%)</td><td>0.05 <b>(-30.77%)</b></td><td>0.02 <b>(+30.14%)</b></td><td>354.10 <b>(+44.47%)</b></td><td>223.40 <b>(+20.46%)</b></td><td>201.00 (+13.18%)</td><td>176.00 (+9.73%)</td><td>74.10 <b>(+112.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>245.10 (n/a)</td><td>185.46 (n/a)</td><td>177.60 (n/a)</td><td>160.40 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (+4.89%)</td><td>0.08 (-5.30%)</td><td>0.08 (-7.51%)</td><td>0.07 (+5.76%)</td><td>0.01 (+1.90%)</td><td>262.80 (-5.47%)</td><td>221.00 (+5.39%)</td><td>213.70 (+8.15%)</td><td>172.20 (-4.65%)</td><td>35.61 (-9.90%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>278.00 (n/a)</td><td>209.70 (n/a)</td><td>197.60 (n/a)</td><td>180.60 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.10 (-19.84%)</td><td>0.09 (-8.97%)</td><td>0.09 (-5.36%)</td><td>0.08 (-0.23%)</td><td>0.01 <b>(-45.01%)</b></td><td>215.60 (+0.23%)</td><td>189.68 (+8.38%)</td><td>180.00 (+5.70%)</td><td>170.00 <b>(+24.72%)</b></td><td>20.05 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>175.02 (n/a)</td><td>170.30 (n/a)</td><td>136.30 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.09 <b>(-21.68%)</b></td><td>0.08 (-10.71%)</td><td>0.08 (-4.44%)</td><td>0.07 (-1.36%)</td><td>0.01 <b>(-66.24%)</b></td><td>247.50 (+1.39%)</td><td>222.76 (+9.34%)</td><td>220.50 (+4.65%)</td><td>202.40 <b>(+27.62%)</b></td><td>16.40 <b>(-55.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.10 (n/a)</td><td>203.74 (n/a)</td><td>210.70 (n/a)</td><td>158.60 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (-4.94%)</td><td>0.08 (+6.29%)</td><td>0.08 (+4.62%)</td><td>0.05 (+2.28%)</td><td>0.03 (-16.51%)</td><td>359.90 (-2.23%)</td><td>224.34 (-9.85%)</td><td>213.40 (-4.39%)</td><td>135.40 (+5.21%)</td><td>84.85 (-16.10%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>368.10 (n/a)</td><td>248.86 (n/a)</td><td>223.20 (n/a)</td><td>128.70 (n/a)</td><td>101.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (-13.32%)</td><td>0.16 (-12.14%)</td><td>0.16 (-10.84%)</td><td>0.13 (-4.84%)</td><td>0.03 (-13.33%)</td><td>259.80 (+5.10%)</td><td>215.26 (+13.55%)</td><td>208.40 (+12.16%)</td><td>176.20 (+15.31%)</td><td>38.82 (+4.98%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.20 (n/a)</td><td>189.58 (n/a)</td><td>185.80 (n/a)</td><td>152.80 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (-15.85%)</td><td>0.20 (+4.48%)</td><td>0.19 (-3.25%)</td><td>0.18 <b>(+62.11%)</b></td><td>0.02 <b>(-72.03%)</b></td><td>183.60 <b>(-38.31%)</b></td><td>169.22 (-15.22%)</td><td>173.10 (+3.34%)</td><td>143.50 (+18.89%)</td><td>15.77 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>297.60 (n/a)</td><td>199.60 (n/a)</td><td>167.50 (n/a)</td><td>120.70 (n/a)</td><td>80.84 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 <b>(-24.24%)</b></td><td>0.22 (-18.97%)</td><td>0.19 (-16.32%)</td><td>0.18 (-16.40%)</td><td>0.04 <b>(-37.57%)</b></td><td>228.00 (+19.62%)</td><td>195.00 <b>(+21.60%)</b></td><td>211.10 (+19.47%)</td><td>151.50 <b>(+32.08%)</b></td><td>31.97 (-2.67%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>190.60 (n/a)</td><td>160.36 (n/a)</td><td>176.70 (n/a)</td><td>114.70 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 <b>(-25.36%)</b></td><td>0.18 (-10.53%)</td><td>0.18 (-4.85%)</td><td>0.17 (+3.79%)</td><td>0.02 <b>(-60.94%)</b></td><td>198.50 (-3.64%)</td><td>181.84 (+8.26%)</td><td>186.60 (+5.07%)</td><td>155.60 <b>(+34.02%)</b></td><td>18.07 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>206.00 (n/a)</td><td>167.96 (n/a)</td><td>177.60 (n/a)</td><td>116.10 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 <b>(-26.94%)</b></td><td>0.22 (-19.13%)</td><td>0.22 (-14.37%)</td><td>0.20 (-15.60%)</td><td>0.02 <b>(-45.55%)</b></td><td>207.50 (+18.50%)</td><td>187.74 <b>(+22.90%)</b></td><td>183.20 (+16.76%)</td><td>171.60 <b>(+36.84%)</b></td><td>16.35 (-9.89%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>175.10 (n/a)</td><td>152.76 (n/a)</td><td>156.90 (n/a)</td><td>125.40 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 <b>(-20.64%)</b></td><td>0.17 (-17.57%)</td><td>0.16 (-18.18%)</td><td>0.15 (-7.96%)</td><td>0.02 <b>(-46.68%)</b></td><td>222.10 (+8.66%)</td><td>195.92 (+19.87%)</td><td>199.00 <b>(+22.24%)</b></td><td>170.00 <b>(+26.02%)</b></td><td>19.01 <b>(-27.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.40 (n/a)</td><td>163.44 (n/a)</td><td>162.80 (n/a)</td><td>134.90 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (-4.35%)</td><td>0.20 (-6.41%)</td><td>0.19 (-15.15%)</td><td>0.18 (-5.17%)</td><td>0.03 (+2.54%)</td><td>206.20 (+5.42%)</td><td>183.84 (+7.05%)</td><td>196.30 (+17.90%)</td><td>150.00 (+4.53%)</td><td>25.02 (+11.10%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>195.60 (n/a)</td><td>171.74 (n/a)</td><td>166.50 (n/a)</td><td>143.50 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 <b>(-25.54%)</b></td><td>0.18 (-12.51%)</td><td>0.17 (-9.51%)</td><td>0.17 (-3.21%)</td><td>0.01 <b>(-78.77%)</b></td><td>193.50 (+3.31%)</td><td>185.80 (+12.43%)</td><td>187.30 (+10.50%)</td><td>176.40 <b>(+34.35%)</b></td><td>6.87 <b>(-70.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>187.30 (n/a)</td><td>165.26 (n/a)</td><td>169.50 (n/a)</td><td>131.30 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 <b>(-31.61%)</b></td><td>0.17 <b>(-28.90%)</b></td><td>0.16 <b>(-32.57%)</b></td><td>0.13 (-6.17%)</td><td>0.03 <b>(-51.61%)</b></td><td>283.70 (+6.57%)</td><td>228.58 <b>(+34.79%)</b></td><td>229.70 <b>(+48.29%)</b></td><td>183.70 <b>(+46.26%)</b></td><td>39.09 <b>(-29.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>266.20 (n/a)</td><td>169.58 (n/a)</td><td>154.90 (n/a)</td><td>125.60 (n/a)</td><td>55.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 (-14.38%)</td><td>0.20 (+2.48%)</td><td>0.20 (+3.94%)</td><td>0.17 (+12.08%)</td><td>0.02 <b>(-49.98%)</b></td><td>192.00 (-10.78%)</td><td>166.50 (-4.73%)</td><td>165.00 (-3.79%)</td><td>149.90 (+16.74%)</td><td>17.50 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>215.20 (n/a)</td><td>174.76 (n/a)</td><td>171.50 (n/a)</td><td>128.40 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-3.14%)</td><td>0.17 (-4.56%)</td><td>0.17 (+0.62%)</td><td>0.11 (-16.20%)</td><td>0.04 (+4.80%)</td><td>327.00 (+19.34%)</td><td>219.72 (+6.55%)</td><td>209.50 (-0.62%)</td><td>165.20 (+3.25%)</td><td>64.61 <b>(+35.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>274.00 (n/a)</td><td>206.22 (n/a)</td><td>210.80 (n/a)</td><td>160.00 (n/a)</td><td>47.52 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 <b>(-20.63%)</b></td><td>0.18 (-0.53%)</td><td>0.18 (-9.36%)</td><td>0.16 <b>(+75.71%)</b></td><td>0.02 <b>(-70.63%)</b></td><td>206.00 <b>(-43.09%)</b></td><td>187.02 (-9.71%)</td><td>187.10 (+10.32%)</td><td>167.20 <b>(+26.00%)</b></td><td>17.83 <b>(-80.23%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>362.00 (n/a)</td><td>207.14 (n/a)</td><td>169.60 (n/a)</td><td>132.70 (n/a)</td><td>90.20 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (+13.00%)</td><td>0.19 (-3.16%)</td><td>0.17 (-13.67%)</td><td>0.17 (+13.22%)</td><td>0.03 (+15.03%)</td><td>210.80 (-11.69%)</td><td>191.16 (+3.24%)</td><td>199.80 (+15.89%)</td><td>145.10 (-11.52%)</td><td>26.19 (-14.56%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>238.70 (n/a)</td><td>185.16 (n/a)</td><td>172.40 (n/a)</td><td>164.00 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 (-12.18%)</td><td>0.16 (-13.89%)</td><td>0.16 (-16.79%)</td><td>0.15 (-3.86%)</td><td>0.02 <b>(-28.80%)</b></td><td>223.90 (+4.04%)</td><td>205.38 (+15.54%)</td><td>210.70 <b>(+20.13%)</b></td><td>175.50 (+13.89%)</td><td>18.52 (-18.66%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>177.76 (n/a)</td><td>175.40 (n/a)</td><td>154.10 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (-0.50%)</td><td>0.12 (-5.94%)</td><td>0.11 (-18.18%)</td><td>0.09 (-3.99%)</td><td>0.03 (+11.21%)</td><td>217.40 (+4.17%)</td><td>173.54 (+7.51%)</td><td>185.50 <b>(+22.28%)</b></td><td>120.90 (+0.50%)</td><td>41.64 (+14.86%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>208.70 (n/a)</td><td>161.42 (n/a)</td><td>151.70 (n/a)</td><td>120.30 (n/a)</td><td>36.25 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 <b>(-26.01%)</b></td><td>0.10 <b>(-22.06%)</b></td><td>0.10 <b>(-23.46%)</b></td><td>0.08 (-1.56%)</td><td>0.02 <b>(-50.71%)</b></td><td>244.50 (+1.58%)</td><td>200.84 <b>(+22.64%)</b></td><td>201.80 <b>(+30.70%)</b></td><td>152.90 <b>(+35.19%)</b></td><td>32.63 <b>(-34.47%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>240.70 (n/a)</td><td>163.76 (n/a)</td><td>154.40 (n/a)</td><td>113.10 (n/a)</td><td>49.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.13 (-5.03%)</td><td>0.11 (-2.76%)</td><td>0.12 (+15.17%)</td><td>0.08 (-19.85%)</td><td>0.02 (+8.95%)</td><td>263.00 <b>(+24.76%)</b></td><td>188.52 (+4.26%)</td><td>170.40 (-13.15%)</td><td>153.10 (+5.30%)</td><td>43.80 <b>(+49.40%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>180.82 (n/a)</td><td>196.20 (n/a)</td><td>145.40 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (+15.97%)</td><td>0.11 (+5.80%)</td><td>0.12 (+3.32%)</td><td>0.10 (+5.34%)</td><td>0.01 <b>(+37.40%)</b></td><td>213.30 (-5.07%)</td><td>180.68 (-5.08%)</td><td>177.20 (-3.22%)</td><td>150.20 (-13.78%)</td><td>22.84 (+11.44%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>190.34 (n/a)</td><td>183.10 (n/a)</td><td>174.20 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (+6.82%)</td><td>0.13 (+12.99%)</td><td>0.14 <b>(+38.24%)</b></td><td>0.10 (+1.93%)</td><td>0.03 (-3.14%)</td><td>210.10 (-1.87%)</td><td>162.10 (-11.99%)</td><td>150.50 <b>(-27.68%)</b></td><td>124.40 (-6.40%)</td><td>32.43 (-11.83%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>214.10 (n/a)</td><td>184.18 (n/a)</td><td>208.10 (n/a)</td><td>132.90 (n/a)</td><td>36.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (-7.89%)</td><td>0.12 (+9.78%)</td><td>0.12 (+14.49%)</td><td>0.10 (+15.04%)</td><td>0.02 <b>(-35.22%)</b></td><td>199.80 (-13.05%)</td><td>171.76 (-10.68%)</td><td>167.10 (-12.65%)</td><td>147.60 (+8.53%)</td><td>22.72 <b>(-37.52%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>229.80 (n/a)</td><td>192.30 (n/a)</td><td>191.30 (n/a)</td><td>136.00 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (+9.62%)</td><td>0.11 (+3.54%)</td><td>0.10 (+0.61%)</td><td>0.09 (+2.03%)</td><td>0.02 <b>(+28.08%)</b></td><td>227.50 (-1.98%)</td><td>193.80 (-2.78%)</td><td>199.80 (-0.60%)</td><td>145.80 (-8.76%)</td><td>29.81 (+12.22%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>199.34 (n/a)</td><td>201.00 (n/a)</td><td>159.80 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 <b>(+43.88%)</b></td><td>0.10 (+7.26%)</td><td>0.09 (-3.88%)</td><td>0.07 (-12.00%)</td><td>0.03 <b>(+319.98%)</b></td><td>297.00 (+13.66%)</td><td>227.80 (-0.51%)</td><td>235.40 (+4.02%)</td><td>146.80 <b>(-30.53%)</b></td><td>63.87 <b>(+231.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>261.30 (n/a)</td><td>228.96 (n/a)</td><td>226.30 (n/a)</td><td>211.30 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 <b>(-24.33%)</b></td><td>0.13 (-10.91%)</td><td>0.13 (-14.75%)</td><td>0.11 <b>(+71.09%)</b></td><td>0.01 <b>(-75.57%)</b></td><td>219.60 <b>(-41.56%)</b></td><td>190.20 (-3.16%)</td><td>185.20 (+17.29%)</td><td>167.80 <b>(+32.13%)</b></td><td>19.22 <b>(-81.41%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>375.80 (n/a)</td><td>196.40 (n/a)</td><td>157.90 (n/a)</td><td>127.00 (n/a)</td><td>103.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.20 (+8.36%)</td><td>0.16 <b>(+21.54%)</b></td><td>0.17 <b>(+34.32%)</b></td><td>0.13 <b>(+30.39%)</b></td><td>0.03 (-11.68%)</td><td>187.60 <b>(-23.33%)</b></td><td>156.46 (-19.28%)</td><td>147.40 <b>(-25.52%)</b></td><td>125.10 (-7.74%)</td><td>28.55 <b>(-35.38%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.70 (n/a)</td><td>193.82 (n/a)</td><td>197.90 (n/a)</td><td>135.60 (n/a)</td><td>44.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 <b>(+35.99%)</b></td><td>0.16 <b>(+22.79%)</b></td><td>0.15 (+12.16%)</td><td>0.13 (+16.06%)</td><td>0.03 <b>(+179.34%)</b></td><td>184.30 (-13.84%)</td><td>157.36 (-17.00%)</td><td>168.50 (-10.80%)</td><td>126.90 <b>(-26.43%)</b></td><td>26.32 <b>(+72.21%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>189.60 (n/a)</td><td>188.90 (n/a)</td><td>172.50 (n/a)</td><td>15.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 <b>(+33.36%)</b></td><td>0.14 <b>(+22.51%)</b></td><td>0.16 <b>(+34.19%)</b></td><td>0.10 (-6.09%)</td><td>0.03 <b>(+301.99%)</b></td><td>236.60 (+6.48%)</td><td>177.58 (-15.52%)</td><td>158.30 <b>(-25.51%)</b></td><td>142.20 <b>(-25.04%)</b></td><td>40.18 <b>(+224.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>210.20 (n/a)</td><td>212.50 (n/a)</td><td>189.70 (n/a)</td><td>12.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (-13.39%)</td><td>0.14 (+2.09%)</td><td>0.14 (-2.77%)</td><td>0.12 (+16.21%)</td><td>0.02 <b>(-43.89%)</b></td><td>210.90 (-13.95%)</td><td>175.26 (-5.72%)</td><td>171.40 (+2.82%)</td><td>146.50 (+15.45%)</td><td>26.21 <b>(-45.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>245.10 (n/a)</td><td>185.90 (n/a)</td><td>166.70 (n/a)</td><td>126.90 (n/a)</td><td>48.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.16 (-10.22%)</td><td>0.13 (-4.34%)</td><td>0.12 (-6.46%)</td><td>0.08 (-5.25%)</td><td>0.03 (-8.79%)</td><td>289.40 (+5.54%)</td><td>206.54 (+4.42%)</td><td>204.70 (+6.89%)</td><td>152.20 (+11.42%)</td><td>53.91 (+6.32%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>274.20 (n/a)</td><td>197.80 (n/a)</td><td>191.50 (n/a)</td><td>136.60 (n/a)</td><td>50.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.17 (+12.93%)</td><td>0.13 (+8.71%)</td><td>0.14 <b>(+31.95%)</b></td><td>0.10 (-2.82%)</td><td>0.03 <b>(+34.51%)</b></td><td>242.80 (+2.88%)</td><td>193.76 (-6.47%)</td><td>171.10 <b>(-24.22%)</b></td><td>145.00 (-11.48%)</td><td>44.27 <b>(+27.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>207.16 (n/a)</td><td>225.80 (n/a)</td><td>163.80 (n/a)</td><td>34.84 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.19 <b>(+24.81%)</b></td><td>0.15 <b>(+22.17%)</b></td><td>0.16 <b>(+36.16%)</b></td><td>0.08 (+1.79%)</td><td>0.04 <b>(+31.90%)</b></td><td>301.40 (-1.76%)</td><td>179.72 (-15.72%)</td><td>151.40 <b>(-26.58%)</b></td><td>127.30 (-19.89%)</td><td>70.04 (+14.25%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>306.80 (n/a)</td><td>213.24 (n/a)</td><td>206.20 (n/a)</td><td>158.90 (n/a)</td><td>61.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 <b>(-26.25%)</b></td><td>0.10 (-19.68%)</td><td>0.10 <b>(-29.99%)</b></td><td>0.09 (-4.91%)</td><td>0.01 <b>(-67.60%)</b></td><td>213.50 (+5.17%)</td><td>191.30 (+19.85%)</td><td>191.40 <b>(+42.84%)</b></td><td>173.10 <b>(+35.66%)</b></td><td>17.40 <b>(-55.23%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>203.00 (n/a)</td><td>159.62 (n/a)</td><td>134.00 (n/a)</td><td>127.60 (n/a)</td><td>38.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (+1.59%)</td><td>0.10 (-9.62%)</td><td>0.09 (-10.17%)</td><td>0.08 (-8.58%)</td><td>0.02 (+13.60%)</td><td>220.60 (+9.37%)</td><td>190.46 (+11.67%)</td><td>205.40 (+11.33%)</td><td>128.50 (-1.61%)</td><td>36.06 (+17.89%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>201.70 (n/a)</td><td>170.56 (n/a)</td><td>184.50 (n/a)</td><td>130.60 (n/a)</td><td>30.59 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (-3.79%)</td><td>0.11 (-3.75%)</td><td>0.10 (-0.34%)</td><td>0.08 (-14.73%)</td><td>0.02 (+7.22%)</td><td>219.80 (+17.29%)</td><td>177.86 (+4.67%)</td><td>180.00 (+0.33%)</td><td>133.70 (+3.97%)</td><td>31.81 <b>(+29.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>187.40 (n/a)</td><td>169.92 (n/a)</td><td>179.40 (n/a)</td><td>128.60 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (+15.77%)</td><td>0.11 (+17.74%)</td><td>0.11 <b>(+23.65%)</b></td><td>0.10 <b>(+22.15%)</b></td><td>0.02 (+0.04%)</td><td>186.20 (-18.12%)</td><td>165.58 (-15.58%)</td><td>166.90 (-19.14%)</td><td>132.70 (-13.61%)</td><td>22.06 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>196.14 (n/a)</td><td>206.40 (n/a)</td><td>153.60 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.12 (+15.05%)</td><td>0.11 <b>(+30.35%)</b></td><td>0.12 <b>(+51.14%)</b></td><td>0.06 (-14.07%)</td><td>0.03 <b>(+80.24%)</b></td><td>315.00 (+16.41%)</td><td>187.26 (-18.73%)</td><td>153.00 <b>(-33.82%)</b></td><td>148.80 (-13.08%)</td><td>71.75 <b>(+93.01%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>270.60 (n/a)</td><td>230.42 (n/a)</td><td>231.20 (n/a)</td><td>171.20 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (-5.51%)</td><td>0.10 (-3.56%)</td><td>0.11 (+2.85%)</td><td>0.06 <b>(-22.74%)</b></td><td>0.03 (-0.78%)</td><td>314.60 <b>(+29.41%)</b></td><td>192.32 (+6.13%)</td><td>168.90 (-2.76%)</td><td>132.80 (+5.90%)</td><td>71.83 <b>(+41.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>243.10 (n/a)</td><td>181.22 (n/a)</td><td>173.70 (n/a)</td><td>125.40 (n/a)</td><td>50.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.14 (+10.40%)</td><td>0.10 (+15.25%)</td><td>0.10 <b>(+29.62%)</b></td><td>0.06 (+1.51%)</td><td>0.03 (+11.58%)</td><td>308.10 (-1.50%)</td><td>198.06 (-12.31%)</td><td>179.60 <b>(-22.85%)</b></td><td>134.50 (-9.43%)</td><td>65.33 (+6.18%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>312.80 (n/a)</td><td>225.86 (n/a)</td><td>232.80 (n/a)</td><td>148.50 (n/a)</td><td>61.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.11 (+1.95%)</td><td>0.10 (+9.94%)</td><td>0.09 (+11.45%)</td><td>0.08 (+17.57%)</td><td>0.01 <b>(-27.98%)</b></td><td>224.10 (-14.92%)</td><td>192.68 (-10.47%)</td><td>196.40 (-10.28%)</td><td>161.20 (-1.89%)</td><td>23.77 <b>(-40.02%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>263.40 (n/a)</td><td>215.22 (n/a)</td><td>218.90 (n/a)</td><td>164.30 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.74 (+8.22%)</td><td>0.57 (-1.82%)</td><td>0.50 (-8.30%)</td><td>0.50 (-5.50%)</td><td>0.11 <b>(+63.95%)</b></td><td>198.30 (+5.82%)</td><td>177.12 (+3.54%)</td><td>197.50 (+9.06%)</td><td>132.10 (-7.62%)</td><td>30.06 <b>(+65.12%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.69 (n/a)</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.07 (n/a)</td><td>187.40 (n/a)</td><td>171.06 (n/a)</td><td>181.10 (n/a)</td><td>143.00 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.64 (-4.01%)</td><td>0.55 (-1.76%)</td><td>0.53 (+2.15%)</td><td>0.52 (+7.45%)</td><td>0.05 <b>(-35.77%)</b></td><td>189.60 (-6.92%)</td><td>180.32 (+0.91%)</td><td>184.40 (-2.07%)</td><td>154.60 (+4.18%)</td><td>14.63 <b>(-37.97%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.66 (n/a)</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>203.70 (n/a)</td><td>178.70 (n/a)</td><td>188.30 (n/a)</td><td>148.40 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.65 (+10.39%)</td><td>0.54 (+0.50%)</td><td>0.52 (-7.33%)</td><td>0.45 (+2.38%)</td><td>0.07 <b>(+27.04%)</b></td><td>216.90 (-2.34%)</td><td>185.62 (-0.12%)</td><td>190.40 (+7.94%)</td><td>152.30 (-9.45%)</td><td>23.89 (+9.99%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.58 (n/a)</td><td>0.53 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.06 (n/a)</td><td>222.10 (n/a)</td><td>185.84 (n/a)</td><td>176.40 (n/a)</td><td>168.20 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.82 <b>(+41.04%)</b></td><td>0.56 (+11.02%)</td><td>0.52 (+6.22%)</td><td>0.39 (-5.66%)</td><td>0.17 <b>(+144.59%)</b></td><td>250.70 (+6.00%)</td><td>188.32 (-5.37%)</td><td>188.80 (-5.84%)</td><td>119.90 <b>(-29.10%)</b></td><td>50.20 <b>(+83.21%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>236.50 (n/a)</td><td>199.00 (n/a)</td><td>200.50 (n/a)</td><td>169.10 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.48 (-13.50%)</td><td>0.41 (-6.76%)</td><td>0.40 (-13.58%)</td><td>0.39 <b>(+26.11%)</b></td><td>0.04 <b>(-68.14%)</b></td><td>189.30 <b>(-20.70%)</b></td><td>179.90 (+1.74%)</td><td>184.50 (+15.75%)</td><td>154.60 (+15.55%)</td><td>14.31 <b>(-70.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>238.70 (n/a)</td><td>176.82 (n/a)</td><td>159.40 (n/a)</td><td>133.80 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.53 (-10.12%)</td><td>0.45 (+12.57%)</td><td>0.45 (+16.28%)</td><td>0.39 <b>(+42.60%)</b></td><td>0.05 <b>(-54.83%)</b></td><td>191.40 <b>(-29.89%)</b></td><td>165.42 (-15.99%)</td><td>164.60 (-14.00%)</td><td>138.30 (+11.26%)</td><td>19.55 <b>(-64.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.59 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>273.00 (n/a)</td><td>196.90 (n/a)</td><td>191.40 (n/a)</td><td>124.30 (n/a)</td><td>54.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.63 <b>(+42.09%)</b></td><td>0.44 (+12.60%)</td><td>0.39 (-3.00%)</td><td>0.36 (+6.96%)</td><td>0.11 <b>(+127.67%)</b></td><td>207.70 (-6.48%)</td><td>175.92 (-8.50%)</td><td>189.40 (+3.05%)</td><td>117.90 <b>(-29.61%)</b></td><td>36.66 <b>(+47.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>222.10 (n/a)</td><td>192.26 (n/a)</td><td>183.80 (n/a)</td><td>167.50 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.43 (-8.40%)</td><td>0.40 (+6.85%)</td><td>0.43 (+19.31%)</td><td>0.35 (+10.30%)</td><td>0.04 <b>(-42.44%)</b></td><td>212.60 (-9.34%)</td><td>184.52 (-8.01%)</td><td>172.60 (-16.17%)</td><td>169.90 (+9.12%)</td><td>19.17 <b>(-44.52%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>234.50 (n/a)</td><td>200.58 (n/a)</td><td>205.90 (n/a)</td><td>155.70 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (+4.56%)</td><td>0.22 (-2.95%)</td><td>0.22 (-1.41%)</td><td>0.17 (+7.75%)</td><td>0.05 (+8.88%)</td><td>219.70 (-7.18%)</td><td>175.96 (+3.19%)</td><td>167.90 (+1.45%)</td><td>129.80 (-4.35%)</td><td>37.13 (-4.94%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>236.70 (n/a)</td><td>170.52 (n/a)</td><td>165.50 (n/a)</td><td>135.70 (n/a)</td><td>39.06 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (-4.48%)</td><td>0.22 (+0.12%)</td><td>0.22 (+11.26%)</td><td>0.16 (-12.37%)</td><td>0.03 (-9.92%)</td><td>225.00 (+14.10%)</td><td>173.58 (-0.14%)</td><td>167.90 (-10.12%)</td><td>146.40 (+4.72%)</td><td>30.13 (+10.31%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>197.20 (n/a)</td><td>173.82 (n/a)</td><td>186.80 (n/a)</td><td>139.80 (n/a)</td><td>27.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (+17.27%)</td><td>0.20 (-1.55%)</td><td>0.20 (-2.56%)</td><td>0.14 (-2.38%)</td><td>0.06 <b>(+45.64%)</b></td><td>261.00 (+2.43%)</td><td>196.46 (+4.42%)</td><td>186.40 (+2.64%)</td><td>130.40 (-14.72%)</td><td>52.61 <b>(+28.68%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>254.80 (n/a)</td><td>188.14 (n/a)</td><td>181.60 (n/a)</td><td>152.90 (n/a)</td><td>40.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.24 (-11.07%)</td><td>0.21 (-0.28%)</td><td>0.20 (+6.51%)</td><td>0.19 (+7.58%)</td><td>0.02 <b>(-47.54%)</b></td><td>197.60 (-7.06%)</td><td>175.36 (-1.65%)</td><td>180.90 (-6.07%)</td><td>155.00 (+12.40%)</td><td>17.40 <b>(-45.19%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>178.30 (n/a)</td><td>192.60 (n/a)</td><td>137.90 (n/a)</td><td>31.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (-10.46%)</td><td>0.20 (-7.35%)</td><td>0.20 (+0.54%)</td><td>0.17 (+2.37%)</td><td>0.03 <b>(-28.20%)</b></td><td>218.80 (-2.32%)</td><td>188.70 (+6.51%)</td><td>183.10 (-0.54%)</td><td>149.40 (+11.66%)</td><td>27.18 <b>(-20.85%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>224.00 (n/a)</td><td>177.16 (n/a)</td><td>184.10 (n/a)</td><td>133.80 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (-16.81%)</td><td>0.19 (-9.41%)</td><td>0.19 (-6.71%)</td><td>0.15 (-8.40%)</td><td>0.03 <b>(-36.73%)</b></td><td>244.40 (+9.20%)</td><td>193.86 (+7.98%)</td><td>195.00 (+7.20%)</td><td>149.90 <b>(+20.21%)</b></td><td>33.80 (-17.88%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>223.80 (n/a)</td><td>179.54 (n/a)</td><td>181.90 (n/a)</td><td>124.70 (n/a)</td><td>41.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (+13.29%)</td><td>0.20 (+6.63%)</td><td>0.19 (-0.39%)</td><td>0.16 (+2.23%)</td><td>0.04 <b>(+29.76%)</b></td><td>228.10 (-2.19%)</td><td>186.48 (-5.57%)</td><td>191.60 (+0.37%)</td><td>142.80 (-11.69%)</td><td>31.13 (+9.26%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>233.20 (n/a)</td><td>197.48 (n/a)</td><td>190.90 (n/a)</td><td>161.70 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (+4.80%)</td><td>0.21 (+13.54%)</td><td>0.19 (+13.67%)</td><td>0.17 (+12.16%)</td><td>0.05 (-1.01%)</td><td>216.70 (-10.82%)</td><td>179.04 (-12.51%)</td><td>196.90 (-12.02%)</td><td>127.40 (-4.57%)</td><td>37.79 (-13.89%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>243.00 (n/a)</td><td>204.64 (n/a)</td><td>223.80 (n/a)</td><td>133.50 (n/a)</td><td>43.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (-12.36%)</td><td>0.23 (+3.54%)</td><td>0.24 (+15.40%)</td><td>0.20 (+16.38%)</td><td>0.03 <b>(-46.69%)</b></td><td>204.90 (-14.05%)</td><td>178.16 (-5.88%)</td><td>170.90 (-13.34%)</td><td>154.80 (+14.08%)</td><td>20.83 <b>(-46.25%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>238.40 (n/a)</td><td>189.30 (n/a)</td><td>197.20 (n/a)</td><td>135.70 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (-0.83%)</td><td>0.26 (+1.16%)</td><td>0.26 (-2.82%)</td><td>0.21 (+15.32%)</td><td>0.04 <b>(-20.30%)</b></td><td>194.80 (-13.27%)</td><td>161.94 (-2.81%)</td><td>158.90 (+2.85%)</td><td>134.50 (+0.82%)</td><td>27.09 <b>(-29.66%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>224.60 (n/a)</td><td>166.62 (n/a)</td><td>154.50 (n/a)</td><td>133.40 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (-19.66%)</td><td>0.23 (-12.50%)</td><td>0.22 (-0.84%)</td><td>0.20 (-3.39%)</td><td>0.03 <b>(-59.80%)</b></td><td>207.20 (+3.55%)</td><td>180.54 (+10.11%)</td><td>182.90 (+0.88%)</td><td>151.70 <b>(+24.45%)</b></td><td>20.07 <b>(-47.35%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>200.10 (n/a)</td><td>163.96 (n/a)</td><td>181.30 (n/a)</td><td>121.90 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.31 (+0.45%)</td><td>0.26 (+17.93%)</td><td>0.26 <b>(+25.89%)</b></td><td>0.22 <b>(+30.68%)</b></td><td>0.04 <b>(-27.66%)</b></td><td>185.80 <b>(-23.48%)</b></td><td>160.68 (-17.12%)</td><td>157.10 <b>(-20.58%)</b></td><td>131.20 (-0.46%)</td><td>23.70 <b>(-41.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>242.80 (n/a)</td><td>193.88 (n/a)</td><td>197.80 (n/a)</td><td>131.80 (n/a)</td><td>40.24 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (-6.15%)</td><td>0.23 (+5.20%)</td><td>0.21 (+10.93%)</td><td>0.19 (+17.70%)</td><td>0.04 <b>(-29.94%)</b></td><td>215.60 (-15.02%)</td><td>183.52 (-7.91%)</td><td>198.60 (-9.85%)</td><td>136.50 (+6.56%)</td><td>31.71 <b>(-35.99%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>253.70 (n/a)</td><td>199.28 (n/a)</td><td>220.30 (n/a)</td><td>128.10 (n/a)</td><td>49.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.25 (-8.93%)</td><td>0.22 (-0.92%)</td><td>0.23 (+2.62%)</td><td>0.17 (-6.41%)</td><td>0.03 <b>(-25.56%)</b></td><td>244.60 (+6.86%)</td><td>187.48 (-0.15%)</td><td>176.60 (-2.54%)</td><td>161.20 (+9.81%)</td><td>32.95 (-11.56%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>228.90 (n/a)</td><td>187.76 (n/a)</td><td>181.20 (n/a)</td><td>146.80 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.35 <b>(+23.15%)</b></td><td>0.25 (+12.16%)</td><td>0.21 (+6.76%)</td><td>0.17 (-3.83%)</td><td>0.08 <b>(+60.38%)</b></td><td>236.00 (+3.96%)</td><td>176.80 (-7.58%)</td><td>194.40 (-6.36%)</td><td>118.20 (-18.82%)</td><td>49.91 <b>(+31.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>227.00 (n/a)</td><td>191.30 (n/a)</td><td>207.60 (n/a)</td><td>145.60 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.22 <b>(-29.91%)</b></td><td>0.20 (-12.93%)</td><td>0.20 (+2.45%)</td><td>0.16 (-9.41%)</td><td>0.02 <b>(-59.12%)</b></td><td>253.80 (+10.40%)</td><td>209.54 (+11.54%)</td><td>201.90 (-2.37%)</td><td>188.20 <b>(+42.68%)</b></td><td>26.13 <b>(-33.91%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>229.90 (n/a)</td><td>187.86 (n/a)</td><td>206.80 (n/a)</td><td>131.90 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 (+10.76%)</td><td>0.20 (-3.30%)</td><td>0.19 (-9.44%)</td><td>0.13 <b>(-25.43%)</b></td><td>0.06 <b>(+90.95%)</b></td><td>275.80 <b>(+34.08%)</b></td><td>191.48 (+10.17%)</td><td>187.00 (+10.45%)</td><td>128.00 (-9.73%)</td><td>62.04 <b>(+121.78%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>205.70 (n/a)</td><td>173.80 (n/a)</td><td>169.30 (n/a)</td><td>141.80 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (+4.56%)</td><td>0.21 (+0.13%)</td><td>0.18 (-5.74%)</td><td>0.16 (-6.28%)</td><td>0.05 <b>(+20.06%)</b></td><td>218.90 (+6.73%)</td><td>176.60 (+1.17%)</td><td>196.10 (+6.11%)</td><td>131.40 (-4.37%)</td><td>39.25 (+19.66%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.10 (n/a)</td><td>174.56 (n/a)</td><td>184.80 (n/a)</td><td>137.40 (n/a)</td><td>32.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.27 <b>(+26.05%)</b></td><td>0.21 (+11.75%)</td><td>0.19 (-7.32%)</td><td>0.17 <b>(+22.80%)</b></td><td>0.04 <b>(+21.99%)</b></td><td>207.40 (-18.57%)</td><td>173.16 (-10.61%)</td><td>184.50 (+7.89%)</td><td>131.30 <b>(-20.71%)</b></td><td>30.45 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>254.70 (n/a)</td><td>193.72 (n/a)</td><td>171.00 (n/a)</td><td>165.60 (n/a)</td><td>38.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (+12.31%)</td><td>0.18 (-0.11%)</td><td>0.17 (-8.60%)</td><td>0.15 (+0.97%)</td><td>0.03 <b>(+50.30%)</b></td><td>233.30 (-0.98%)</td><td>196.68 (+1.22%)</td><td>200.10 (+9.40%)</td><td>154.30 (-10.96%)</td><td>32.39 <b>(+30.71%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>235.60 (n/a)</td><td>194.30 (n/a)</td><td>182.90 (n/a)</td><td>173.30 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.23 (-13.80%)</td><td>0.17 (-17.35%)</td><td>0.18 (-6.87%)</td><td>0.09 <b>(-40.69%)</b></td><td>0.05 (+16.79%)</td><td>378.60 <b>(+68.64%)</b></td><td>228.10 <b>(+28.65%)</b></td><td>192.20 (+7.37%)</td><td>152.60 (+16.05%)</td><td>89.75 <b>(+138.83%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>224.50 (n/a)</td><td>177.30 (n/a)</td><td>179.00 (n/a)</td><td>131.50 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (+7.07%)</td><td>0.20 (-9.21%)</td><td>0.17 <b>(-23.34%)</b></td><td>0.16 (+6.60%)</td><td>0.06 (-0.22%)</td><td>217.90 (-6.16%)</td><td>184.68 (+9.49%)</td><td>202.80 <b>(+30.42%)</b></td><td>118.90 (-6.67%)</td><td>41.38 (-10.29%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>232.20 (n/a)</td><td>168.68 (n/a)</td><td>155.50 (n/a)</td><td>127.40 (n/a)</td><td>46.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.30 (+7.12%)</td><td>0.21 (+17.21%)</td><td>0.23 <b>(+38.74%)</b></td><td>0.14 <b>(+24.86%)</b></td><td>0.06 (+1.70%)</td><td>244.70 (-19.90%)</td><td>176.86 (-15.80%)</td><td>154.20 <b>(-27.91%)</b></td><td>114.20 (-6.70%)</td><td>52.93 (-19.40%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>305.50 (n/a)</td><td>210.04 (n/a)</td><td>213.90 (n/a)</td><td>122.40 (n/a)</td><td>65.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.26 (+2.50%)</td><td>0.20 <b>(+23.97%)</b></td><td>0.21 <b>(+38.67%)</b></td><td>0.14 <b>(+38.58%)</b></td><td>0.04 <b>(-22.52%)</b></td><td>242.00 <b>(-27.85%)</b></td><td>177.42 <b>(-22.85%)</b></td><td>165.30 <b>(-27.88%)</b></td><td>132.00 (-2.44%)</td><td>40.95 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>335.40 (n/a)</td><td>229.96 (n/a)</td><td>229.20 (n/a)</td><td>135.30 (n/a)</td><td>71.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.86 (-15.66%)</td><td>0.75 (-13.41%)</td><td>0.79 (-10.41%)</td><td>0.66 (-12.54%)</td><td>0.09 (-6.89%)</td><td>199.50 (+14.33%)</td><td>175.84 (+15.76%)</td><td>166.80 (+11.65%)</td><td>151.60 (+18.62%)</td><td>22.20 <b>(+30.70%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.75 (n/a)</td><td>0.10 (n/a)</td><td>174.50 (n/a)</td><td>151.90 (n/a)</td><td>149.40 (n/a)</td><td>127.80 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.91 (-8.14%)</td><td>0.79 (+4.66%)</td><td>0.74 (-3.93%)</td><td>0.68 <b>(+47.02%)</b></td><td>0.10 <b>(-47.15%)</b></td><td>192.90 <b>(-31.98%)</b></td><td>168.92 (-9.07%)</td><td>177.60 (+4.10%)</td><td>143.70 (+8.86%)</td><td>20.82 <b>(-63.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.99 (n/a)</td><td>0.75 (n/a)</td><td>0.77 (n/a)</td><td>0.46 (n/a)</td><td>0.19 (n/a)</td><td>283.60 (n/a)</td><td>185.76 (n/a)</td><td>170.60 (n/a)</td><td>132.00 (n/a)</td><td>57.25 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 <b>(-22.40%)</b></td><td>0.75 (-13.36%)</td><td>0.71 (-14.50%)</td><td>0.66 (-1.16%)</td><td>0.09 <b>(-50.06%)</b></td><td>198.70 (+1.17%)</td><td>177.54 (+12.85%)</td><td>185.50 (+16.96%)</td><td>147.80 <b>(+28.86%)</b></td><td>20.36 <b>(-34.65%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.14 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.67 (n/a)</td><td>0.18 (n/a)</td><td>196.40 (n/a)</td><td>157.32 (n/a)</td><td>158.60 (n/a)</td><td>114.70 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.00 (+0.00%)</td><td>0.00 (-5.17%)</td><td>0.00 (-8.33%)</td><td>0.00 (-9.09%)</td><td>0.00 <b>(+29.10%)</b></td><td>3941.55 (+8.81%)</td><td>3766.17 (+6.63%)</td><td>3814.62 (+7.31%)</td><td>3555.25 (+3.08%)</td><td>150.52 <b>(+107.29%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3622.37 (n/a)</td><td>3531.91 (n/a)</td><td>3554.65 (n/a)</td><td>3448.90 (n/a)</td><td>72.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.00 (+0.00%)</td><td>0.00 (-1.79%)</td><td>0.00 (-4.35%)</td><td>0.00 (+0.00%)</td><td>0.00 (+11.80%)</td><td>3892.29 (-1.69%)</td><td>3714.59 (+1.80%)</td><td>3674.48 (+3.89%)</td><td>3514.47 (-0.19%)</td><td>167.55 (-11.54%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>3959.08 (n/a)</td><td>3648.74 (n/a)</td><td>3537.05 (n/a)</td><td>3521.27 (n/a)</td><td>189.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.28 (+0.43%)</td><td>0.18 (-15.83%)</td><td>0.16 <b>(-32.75%)</b></td><td>0.15 (+4.83%)</td><td>0.05 (-4.74%)</td><td>13606.27 (-4.66%)</td><td>12028.65 (+17.67%)</td><td>12929.34 <b>(+48.71%)</b></td><td>7507.78 (-0.42%)</td><td>2549.31 (-12.73%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>14270.97 (n/a)</td><td>10222.58 (n/a)</td><td>8694.24 (n/a)</td><td>7539.73 (n/a)</td><td>2921.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>6.48 (+3.81%)</td><td>5.02 (-1.57%)</td><td>4.61 (-5.77%)</td><td>4.15 (+7.66%)</td><td>0.91 (-0.59%)</td><td>252.40 (-7.10%)</td><td>213.96 (+1.23%)</td><td>227.50 (+6.11%)</td><td>161.70 (-3.69%)</td><td>34.73 (-12.74%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.25 (n/a)</td><td>5.10 (n/a)</td><td>4.89 (n/a)</td><td>3.86 (n/a)</td><td>0.91 (n/a)</td><td>271.70 (n/a)</td><td>211.36 (n/a)</td><td>214.40 (n/a)</td><td>167.90 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.32 (-7.86%)</td><td>4.51 (-6.62%)</td><td>4.45 (-10.37%)</td><td>4.08 (+9.78%)</td><td>0.50 <b>(-33.19%)</b></td><td>257.00 (-8.90%)</td><td>234.64 (+5.84%)</td><td>235.70 (+11.60%)</td><td>196.90 (+8.48%)</td><td>23.92 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>5.78 (n/a)</td><td>4.83 (n/a)</td><td>4.96 (n/a)</td><td>3.72 (n/a)</td><td>0.74 (n/a)</td><td>282.10 (n/a)</td><td>221.70 (n/a)</td><td>211.20 (n/a)</td><td>181.50 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.14 (+6.07%)</td><td>4.74 (+8.40%)</td><td>4.77 (+12.10%)</td><td>4.41 (+10.18%)</td><td>0.27 <b>(-25.04%)</b></td><td>237.80 (-9.24%)</td><td>221.66 (-8.02%)</td><td>219.70 (-10.80%)</td><td>204.00 (-5.73%)</td><td>12.70 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.85 (n/a)</td><td>4.38 (n/a)</td><td>4.26 (n/a)</td><td>4.00 (n/a)</td><td>0.37 (n/a)</td><td>262.00 (n/a)</td><td>240.98 (n/a)</td><td>246.30 (n/a)</td><td>216.40 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.43 (-12.10%)</td><td>4.69 (-8.43%)</td><td>5.23 (-3.05%)</td><td>3.69 (-7.42%)</td><td>0.87 (-18.21%)</td><td>283.80 (+8.03%)</td><td>230.42 (+8.47%)</td><td>200.50 (+3.14%)</td><td>193.20 (+13.78%)</td><td>45.55 (-1.04%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.17 (n/a)</td><td>5.12 (n/a)</td><td>5.40 (n/a)</td><td>3.99 (n/a)</td><td>1.06 (n/a)</td><td>262.70 (n/a)</td><td>212.42 (n/a)</td><td>194.40 (n/a)</td><td>169.80 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>9.58 (+12.85%)</td><td>8.06 (+7.04%)</td><td>7.84 (+6.86%)</td><td>7.02 (+9.90%)</td><td>0.97 (+14.38%)</td><td>298.90 (-9.01%)</td><td>263.08 (-6.54%)</td><td>267.30 (-6.44%)</td><td>218.80 (-11.38%)</td><td>29.89 (-8.16%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.49 (n/a)</td><td>7.53 (n/a)</td><td>7.34 (n/a)</td><td>6.38 (n/a)</td><td>0.85 (n/a)</td><td>328.50 (n/a)</td><td>281.48 (n/a)</td><td>285.70 (n/a)</td><td>246.90 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.94 (-3.32%)</td><td>8.21 (+5.30%)</td><td>8.00 (-2.38%)</td><td>7.33 (+16.50%)</td><td>0.70 <b>(-41.40%)</b></td><td>286.20 (-14.18%)</td><td>256.98 (-6.36%)</td><td>262.20 (+2.42%)</td><td>234.70 (+3.44%)</td><td>22.12 <b>(-49.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>9.24 (n/a)</td><td>7.80 (n/a)</td><td>8.19 (n/a)</td><td>6.29 (n/a)</td><td>1.20 (n/a)</td><td>333.50 (n/a)</td><td>274.42 (n/a)</td><td>256.00 (n/a)</td><td>226.90 (n/a)</td><td>43.90 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.97 (+4.22%)</td><td>8.27 (+6.05%)</td><td>8.68 (+10.49%)</td><td>7.24 (+6.76%)</td><td>0.74 (+2.42%)</td><td>289.90 (-6.30%)</td><td>255.42 (-5.74%)</td><td>241.70 (-9.51%)</td><td>233.90 (-4.06%)</td><td>23.84 (-7.93%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.60 (n/a)</td><td>7.79 (n/a)</td><td>7.85 (n/a)</td><td>6.78 (n/a)</td><td>0.72 (n/a)</td><td>309.40 (n/a)</td><td>270.96 (n/a)</td><td>267.10 (n/a)</td><td>243.80 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>9.10 (-9.61%)</td><td>7.97 (-5.14%)</td><td>8.27 (-5.91%)</td><td>5.44 (-19.97%)</td><td>1.48 (+9.65%)</td><td>385.80 <b>(+24.98%)</b></td><td>272.80 (+6.91%)</td><td>253.40 (+6.25%)</td><td>230.50 (+10.60%)</td><td>64.48 <b>(+52.82%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>10.06 (n/a)</td><td>8.40 (n/a)</td><td>8.79 (n/a)</td><td>6.79 (n/a)</td><td>1.35 (n/a)</td><td>308.70 (n/a)</td><td>255.16 (n/a)</td><td>238.50 (n/a)</td><td>208.40 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>10.59 <b>(+33.02%)</b></td><td>8.55 (+14.55%)</td><td>8.35 (+12.66%)</td><td>7.16 (+2.64%)</td><td>1.32 <b>(+255.06%)</b></td><td>293.00 (-2.56%)</td><td>249.66 (-11.29%)</td><td>251.30 (-11.23%)</td><td>198.00 <b>(-24.80%)</b></td><td>36.25 <b>(+157.72%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.96 (n/a)</td><td>7.47 (n/a)</td><td>7.41 (n/a)</td><td>6.97 (n/a)</td><td>0.37 (n/a)</td><td>300.70 (n/a)</td><td>281.42 (n/a)</td><td>283.10 (n/a)</td><td>263.30 (n/a)</td><td>14.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>8.85 (-10.64%)</td><td>8.46 (+1.71%)</td><td>8.42 (-0.08%)</td><td>8.06 (+12.75%)</td><td>0.29 <b>(-75.12%)</b></td><td>260.30 (-11.31%)</td><td>248.12 (-3.10%)</td><td>249.10 (+0.08%)</td><td>236.90 (+11.90%)</td><td>8.47 <b>(-75.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>9.91 (n/a)</td><td>8.32 (n/a)</td><td>8.43 (n/a)</td><td>7.14 (n/a)</td><td>1.16 (n/a)</td><td>293.50 (n/a)</td><td>256.06 (n/a)</td><td>248.90 (n/a)</td><td>211.70 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>11.53 (-5.47%)</td><td>10.66 (-3.59%)</td><td>10.72 (-1.49%)</td><td>9.73 (-2.46%)</td><td>0.73 <b>(-27.61%)</b></td><td>430.90 (+2.52%)</td><td>394.90 (+3.44%)</td><td>391.40 (+1.53%)</td><td>363.70 (+5.76%)</td><td>27.39 <b>(-20.85%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>12.20 (n/a)</td><td>11.06 (n/a)</td><td>10.88 (n/a)</td><td>9.98 (n/a)</td><td>1.01 (n/a)</td><td>420.30 (n/a)</td><td>381.78 (n/a)</td><td>385.50 (n/a)</td><td>343.90 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>12.83 (-2.50%)</td><td>11.43 (+1.90%)</td><td>10.88 (+0.01%)</td><td>10.69 (+5.22%)</td><td>0.94 <b>(-22.57%)</b></td><td>392.20 (-4.97%)</td><td>368.90 (-2.21%)</td><td>385.40 (+0.00%)</td><td>326.90 (+2.57%)</td><td>28.77 <b>(-23.87%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.16 (n/a)</td><td>11.22 (n/a)</td><td>10.88 (n/a)</td><td>10.16 (n/a)</td><td>1.21 (n/a)</td><td>412.70 (n/a)</td><td>377.22 (n/a)</td><td>385.40 (n/a)</td><td>318.70 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.16 (+9.62%)</td><td>11.50 (+6.72%)</td><td>11.11 (+0.84%)</td><td>10.90 <b>(+23.20%)</b></td><td>0.95 <b>(-25.92%)</b></td><td>384.70 (-18.84%)</td><td>366.68 (-6.98%)</td><td>377.60 (-0.84%)</td><td>318.70 (-8.76%)</td><td>27.70 <b>(-45.45%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>12.01 (n/a)</td><td>10.77 (n/a)</td><td>11.01 (n/a)</td><td>8.85 (n/a)</td><td>1.29 (n/a)</td><td>474.00 (n/a)</td><td>394.20 (n/a)</td><td>380.80 (n/a)</td><td>349.30 (n/a)</td><td>50.78 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>14.75 (+10.49%)</td><td>13.66 (+6.19%)</td><td>13.63 (+6.22%)</td><td>12.45 (+2.09%)</td><td>0.96 <b>(+119.73%)</b></td><td>337.00 (-2.03%)</td><td>308.26 (-5.54%)</td><td>307.80 (-5.87%)</td><td>284.30 (-9.52%)</td><td>21.95 <b>(+93.82%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.35 (n/a)</td><td>12.87 (n/a)</td><td>12.83 (n/a)</td><td>12.19 (n/a)</td><td>0.44 (n/a)</td><td>344.00 (n/a)</td><td>326.34 (n/a)</td><td>327.00 (n/a)</td><td>314.20 (n/a)</td><td>11.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.62 (+0.94%)</td><td>12.76 (+5.66%)</td><td>12.55 (-0.95%)</td><td>12.10 (+19.05%)</td><td>0.59 <b>(-59.21%)</b></td><td>346.70 (-15.99%)</td><td>329.20 (-6.33%)</td><td>334.20 (+0.94%)</td><td>307.90 (-0.93%)</td><td>14.86 <b>(-66.18%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.50 (n/a)</td><td>12.08 (n/a)</td><td>12.67 (n/a)</td><td>10.16 (n/a)</td><td>1.44 (n/a)</td><td>412.70 (n/a)</td><td>351.44 (n/a)</td><td>331.10 (n/a)</td><td>310.80 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.54 (-6.38%)</td><td>11.98 (-7.76%)</td><td>12.37 (-8.29%)</td><td>9.41 (-15.55%)</td><td>1.65 <b>(+24.21%)</b></td><td>445.70 (+18.41%)</td><td>356.12 (+9.30%)</td><td>338.90 (+9.01%)</td><td>309.80 (+6.83%)</td><td>54.74 <b>(+57.37%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>14.46 (n/a)</td><td>12.99 (n/a)</td><td>13.49 (n/a)</td><td>11.14 (n/a)</td><td>1.33 (n/a)</td><td>376.40 (n/a)</td><td>325.82 (n/a)</td><td>310.90 (n/a)</td><td>290.00 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>15.56 (+7.25%)</td><td>13.70 (+12.36%)</td><td>13.11 (+8.14%)</td><td>12.26 <b>(+34.91%)</b></td><td>1.42 <b>(-28.98%)</b></td><td>342.20 <b>(-25.88%)</b></td><td>308.70 (-12.41%)</td><td>320.00 (-7.51%)</td><td>269.60 (-6.75%)</td><td>30.98 <b>(-52.67%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>14.51 (n/a)</td><td>12.19 (n/a)</td><td>12.12 (n/a)</td><td>9.08 (n/a)</td><td>2.00 (n/a)</td><td>461.70 (n/a)</td><td>352.42 (n/a)</td><td>346.00 (n/a)</td><td>289.10 (n/a)</td><td>65.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>13.45 (-16.16%)</td><td>12.04 (-6.49%)</td><td>12.71 (+1.95%)</td><td>9.68 (+0.00%)</td><td>1.65 <b>(-42.32%)</b></td><td>433.30 (+0.00%)</td><td>354.28 (+4.40%)</td><td>329.90 (-1.93%)</td><td>311.90 (+19.27%)</td><td>52.67 <b>(-30.59%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>16.04 (n/a)</td><td>12.87 (n/a)</td><td>12.47 (n/a)</td><td>9.68 (n/a)</td><td>2.87 (n/a)</td><td>433.30 (n/a)</td><td>339.34 (n/a)</td><td>336.40 (n/a)</td><td>261.50 (n/a)</td><td>75.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>3.46 (+0.58%)</td><td>2.72 (-11.80%)</td><td>2.52 <b>(-24.05%)</b></td><td>2.27 (-6.21%)</td><td>0.48 (+13.06%)</td><td>230.70 (+6.61%)</td><td>197.16 (+14.02%)</td><td>208.40 <b>(+31.65%)</b></td><td>151.50 (-0.59%)</td><td>31.79 (+18.90%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.44 (n/a)</td><td>3.08 (n/a)</td><td>3.31 (n/a)</td><td>2.42 (n/a)</td><td>0.43 (n/a)</td><td>216.40 (n/a)</td><td>172.92 (n/a)</td><td>158.30 (n/a)</td><td>152.40 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>5.58 (+3.79%)</td><td>4.97 (+10.14%)</td><td>5.16 (+13.28%)</td><td>4.23 <b>(+20.58%)</b></td><td>0.58 (-15.30%)</td><td>248.00 (-17.06%)</td><td>213.44 (-9.96%)</td><td>203.40 (-11.72%)</td><td>187.90 (-3.64%)</td><td>25.74 <b>(-33.42%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>5.38 (n/a)</td><td>4.51 (n/a)</td><td>4.55 (n/a)</td><td>3.51 (n/a)</td><td>0.68 (n/a)</td><td>299.00 (n/a)</td><td>237.04 (n/a)</td><td>230.40 (n/a)</td><td>195.00 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>7.89 (-1.00%)</td><td>7.51 (+3.90%)</td><td>7.63 (+6.90%)</td><td>6.94 (+11.49%)</td><td>0.40 <b>(-46.64%)</b></td><td>302.30 (-10.30%)</td><td>279.98 (-4.37%)</td><td>274.90 (-6.46%)</td><td>265.80 (+1.03%)</td><td>15.33 <b>(-50.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.97 (n/a)</td><td>7.23 (n/a)</td><td>7.14 (n/a)</td><td>6.22 (n/a)</td><td>0.75 (n/a)</td><td>337.00 (n/a)</td><td>292.78 (n/a)</td><td>293.90 (n/a)</td><td>263.10 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>4.01 (+14.07%)</td><td>3.10 (+5.53%)</td><td>3.03 (+4.73%)</td><td>2.63 (+8.90%)</td><td>0.54 <b>(+27.41%)</b></td><td>199.00 (-8.17%)</td><td>172.92 (-4.80%)</td><td>173.10 (-4.52%)</td><td>130.80 (-12.33%)</td><td>26.26 (+0.56%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.51 (n/a)</td><td>2.93 (n/a)</td><td>2.89 (n/a)</td><td>2.42 (n/a)</td><td>0.42 (n/a)</td><td>216.70 (n/a)</td><td>181.64 (n/a)</td><td>181.30 (n/a)</td><td>149.20 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.29 (+0.59%)</td><td>0.20 (-15.51%)</td><td>0.19 (-19.71%)</td><td>0.10 <b>(-41.42%)</b></td><td>0.07 <b>(+51.02%)</b></td><td>322.30 <b>(+70.71%)</b></td><td>190.42 <b>(+29.63%)</b></td><td>171.60 <b>(+24.53%)</b></td><td>111.10 (-0.63%)</td><td>81.15 <b>(+160.39%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>188.80 (n/a)</td><td>146.90 (n/a)</td><td>137.80 (n/a)</td><td>111.80 (n/a)</td><td>31.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.21 (-17.61%)</td><td>0.18 (-14.98%)</td><td>0.18 (-15.26%)</td><td>0.16 (-10.49%)</td><td>0.02 <b>(-34.18%)</b></td><td>208.60 (+11.73%)</td><td>185.18 (+16.79%)</td><td>183.90 (+17.96%)</td><td>155.30 <b>(+21.33%)</b></td><td>20.06 (-11.48%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.70 (n/a)</td><td>158.56 (n/a)</td><td>155.90 (n/a)</td><td>128.00 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.42 <b>(-26.23%)</b></td><td>0.38 (-16.68%)</td><td>0.35 (-16.08%)</td><td>0.34 (-2.86%)</td><td>0.04 <b>(-54.02%)</b></td><td>194.90 (+2.96%)</td><td>175.74 (+17.46%)</td><td>185.10 (+19.19%)</td><td>155.70 <b>(+35.51%)</b></td><td>18.57 <b>(-36.26%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>189.30 (n/a)</td><td>149.62 (n/a)</td><td>155.30 (n/a)</td><td>114.90 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.57 (+19.48%)</td><td>0.41 (-1.97%)</td><td>0.38 (-11.70%)</td><td>0.32 (-13.75%)</td><td>0.09 <b>(+126.99%)</b></td><td>205.30 (+15.92%)</td><td>164.80 (+4.91%)</td><td>171.10 (+13.24%)</td><td>115.80 (-16.27%)</td><td>32.52 <b>(+111.03%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.04 (n/a)</td><td>177.10 (n/a)</td><td>157.08 (n/a)</td><td>151.10 (n/a)</td><td>138.30 (n/a)</td><td>15.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.60 (+17.22%)</td><td>0.42 (-2.28%)</td><td>0.35 (-17.83%)</td><td>0.33 (+2.54%)</td><td>0.12 <b>(+47.00%)</b></td><td>201.10 (-2.52%)</td><td>165.12 (+5.08%)</td><td>188.30 <b>(+21.72%)</b></td><td>108.70 (-14.68%)</td><td>40.91 <b>(+26.72%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>206.30 (n/a)</td><td>157.14 (n/a)</td><td>154.70 (n/a)</td><td>127.40 (n/a)</td><td>32.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.09 (+11.22%)</td><td>0.81 (-7.84%)</td><td>0.75 (-19.86%)</td><td>0.62 (-16.24%)</td><td>0.17 <b>(+50.59%)</b></td><td>210.60 (+19.39%)</td><td>168.16 (+10.52%)</td><td>174.20 <b>(+24.79%)</b></td><td>120.60 (-10.07%)</td><td>32.37 <b>(+55.39%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.98 (n/a)</td><td>0.87 (n/a)</td><td>0.94 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td><td>176.40 (n/a)</td><td>152.16 (n/a)</td><td>139.60 (n/a)</td><td>134.10 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>1.02 (-4.85%)</td><td>0.83 (-3.01%)</td><td>0.85 (-1.13%)</td><td>0.63 (-2.51%)</td><td>0.15 (+2.58%)</td><td>206.80 (+2.58%)</td><td>162.90 (+3.47%)</td><td>154.10 (+1.12%)</td><td>128.80 (+5.06%)</td><td>31.62 (+10.34%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.86 (n/a)</td><td>0.65 (n/a)</td><td>0.15 (n/a)</td><td>201.60 (n/a)</td><td>157.44 (n/a)</td><td>152.40 (n/a)</td><td>122.60 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.97 (-6.86%)</td><td>0.82 (+0.73%)</td><td>0.80 (-6.84%)</td><td>0.68 <b>(+22.25%)</b></td><td>0.12 <b>(-35.62%)</b></td><td>193.50 (-18.22%)</td><td>162.64 (-3.45%)</td><td>164.70 (+7.37%)</td><td>134.70 (+7.33%)</td><td>22.77 <b>(-45.51%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.04 (n/a)</td><td>0.81 (n/a)</td><td>0.85 (n/a)</td><td>0.55 (n/a)</td><td>0.18 (n/a)</td><td>236.60 (n/a)</td><td>168.46 (n/a)</td><td>153.40 (n/a)</td><td>125.50 (n/a)</td><td>41.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.89 (-4.61%)</td><td>0.71 (-8.37%)</td><td>0.75 (-2.57%)</td><td>0.51 (-14.67%)</td><td>0.14 (+16.40%)</td><td>255.80 (+17.18%)</td><td>190.08 (+10.64%)</td><td>175.60 (+2.63%)</td><td>147.70 (+4.83%)</td><td>41.73 <b>(+43.45%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>218.30 (n/a)</td><td>171.80 (n/a)</td><td>171.10 (n/a)</td><td>140.90 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:27:18</td><td>0.15 (+16.47%)</td><td>0.10 (-9.70%)</td><td>0.09 <b>(-20.14%)</b></td><td>0.07 <b>(-26.28%)</b></td><td>0.03 <b>(+119.31%)</b></td><td>246.10 <b>(+35.67%)</b></td><td>180.42 (+17.17%)</td><td>188.40 <b>(+25.18%)</b></td><td>110.30 (-14.16%)</td><td>49.76 <b>(+145.64%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>153.98 (n/a)</td><td>150.50 (n/a)</td><td>128.50 (n/a)</td><td>20.26 (n/a)</td>
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
