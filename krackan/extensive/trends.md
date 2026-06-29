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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 <b>(-27.05%)</b></td><td>0.04 (-15.54%)</td><td>0.04 (-3.02%)</td><td>0.03 <b>(-26.01%)</b></td><td>0.01 <b>(-21.60%)</b></td><td>236.20 <b>(+35.20%)</b></td><td>172.12 (+19.54%)</td><td>157.60 (+3.14%)</td><td>124.10 <b>(+36.98%)</b></td><td>49.34 <b>(+50.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>143.98 (n/a)</td><td>152.80 (n/a)</td><td>90.60 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-4.50%)</td><td>0.04 (+18.04%)</td><td>0.04 <b>(+25.66%)</b></td><td>0.04 <b>(+23.44%)</b></td><td>0.01 <b>(-39.42%)</b></td><td>169.80 (-19.03%)</td><td>146.00 (-17.77%)</td><td>147.30 <b>(-20.42%)</b></td><td>124.80 (+4.70%)</td><td>18.99 <b>(-49.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>177.54 (n/a)</td><td>185.10 (n/a)</td><td>119.20 (n/a)</td><td>37.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-1.43%)</td><td>0.04 (-12.16%)</td><td>0.03 <b>(-22.79%)</b></td><td>0.03 (-16.71%)</td><td>0.01 (+12.67%)</td><td>241.90 <b>(+20.05%)</b></td><td>183.34 (+15.53%)</td><td>193.20 <b>(+29.49%)</b></td><td>128.10 (+1.43%)</td><td>42.62 <b>(+34.66%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>158.70 (n/a)</td><td>149.20 (n/a)</td><td>126.30 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-10.61%)</td><td>0.03 (-10.89%)</td><td>0.03 (-13.09%)</td><td>0.03 (-7.70%)</td><td>0.01 (-13.15%)</td><td>232.90 (+8.38%)</td><td>187.84 (+11.73%)</td><td>198.70 (+15.06%)</td><td>125.90 (+11.91%)</td><td>41.08 (+4.30%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>168.12 (n/a)</td><td>172.70 (n/a)</td><td>112.50 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (+7.64%)</td><td>0.04 (-5.41%)</td><td>0.03 (-11.28%)</td><td>0.03 (-14.20%)</td><td>0.01 <b>(+64.20%)</b></td><td>216.90 (+16.55%)</td><td>173.44 (+7.81%)</td><td>177.20 (+12.72%)</td><td>126.10 (-7.14%)</td><td>32.47 <b>(+73.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>160.88 (n/a)</td><td>157.20 (n/a)</td><td>135.80 (n/a)</td><td>18.74 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (-4.36%)</td><td>0.04 (-4.94%)</td><td>0.04 (-8.24%)</td><td>0.03 (+3.71%)</td><td>0.01 <b>(-28.37%)</b></td><td>197.90 (-3.56%)</td><td>166.16 (+3.79%)</td><td>168.40 (+8.93%)</td><td>136.80 (+4.51%)</td><td>22.76 <b>(-26.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>160.10 (n/a)</td><td>154.60 (n/a)</td><td>130.90 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 <b>(+28.64%)</b></td><td>0.04 (+14.67%)</td><td>0.04 (+9.64%)</td><td>0.03 (+8.40%)</td><td>0.01 <b>(+31.54%)</b></td><td>227.80 (-7.74%)</td><td>172.82 (-12.22%)</td><td>168.30 (-8.78%)</td><td>124.00 <b>(-22.26%)</b></td><td>37.27 (-5.92%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>196.88 (n/a)</td><td>184.50 (n/a)</td><td>159.50 (n/a)</td><td>39.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (-0.24%)</td><td>0.03 (-4.45%)</td><td>0.03 (+4.26%)</td><td>0.02 (-12.17%)</td><td>0.01 (+3.27%)</td><td>247.50 (+13.85%)</td><td>195.14 (+5.22%)</td><td>195.70 (-4.07%)</td><td>140.30 (+0.21%)</td><td>39.84 (+15.51%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>185.46 (n/a)</td><td>204.00 (n/a)</td><td>140.00 (n/a)</td><td>34.49 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (-8.03%)</td><td>0.08 (-0.76%)</td><td>0.08 (-6.64%)</td><td>0.06 (+4.39%)</td><td>0.01 <b>(-37.91%)</b></td><td>194.90 (-4.23%)</td><td>155.16 (-2.23%)</td><td>149.70 (+7.08%)</td><td>126.30 (+8.79%)</td><td>24.99 <b>(-37.39%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>158.70 (n/a)</td><td>139.80 (n/a)</td><td>116.10 (n/a)</td><td>39.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (-14.56%)</td><td>0.08 (-6.12%)</td><td>0.08 (+0.66%)</td><td>0.07 (+4.87%)</td><td>0.01 <b>(-40.01%)</b></td><td>182.10 (-4.66%)</td><td>161.36 (+5.04%)</td><td>156.00 (-0.70%)</td><td>142.70 (+17.06%)</td><td>18.07 <b>(-31.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>153.62 (n/a)</td><td>157.10 (n/a)</td><td>121.90 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (-10.68%)</td><td>0.08 (-9.89%)</td><td>0.08 (-0.92%)</td><td>0.05 <b>(-25.37%)</b></td><td>0.02 <b>(+33.80%)</b></td><td>231.50 <b>(+33.97%)</b></td><td>170.42 (+14.76%)</td><td>153.90 (+0.92%)</td><td>128.00 (+11.99%)</td><td>45.26 <b>(+104.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>148.50 (n/a)</td><td>152.50 (n/a)</td><td>114.30 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (+5.80%)</td><td>0.07 (-7.27%)</td><td>0.07 (-8.57%)</td><td>0.05 (-13.18%)</td><td>0.02 (+13.56%)</td><td>232.70 (+15.20%)</td><td>173.18 (+9.30%)</td><td>175.70 (+9.40%)</td><td>113.10 (-5.43%)</td><td>42.49 <b>(+21.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>202.00 (n/a)</td><td>158.44 (n/a)</td><td>160.60 (n/a)</td><td>119.60 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 <b>(+20.64%)</b></td><td>0.08 <b>(+20.57%)</b></td><td>0.09 <b>(+24.91%)</b></td><td>0.06 <b>(+40.29%)</b></td><td>0.01 (+13.77%)</td><td>195.80 <b>(-28.72%)</b></td><td>157.28 (-17.88%)</td><td>141.50 (-19.92%)</td><td>128.60 (-17.09%)</td><td>30.85 <b>(-35.19%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>274.70 (n/a)</td><td>191.52 (n/a)</td><td>176.70 (n/a)</td><td>155.10 (n/a)</td><td>47.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (+14.20%)</td><td>0.08 (-0.64%)</td><td>0.07 (-8.31%)</td><td>0.05 (-19.28%)</td><td>0.02 <b>(+159.50%)</b></td><td>232.70 <b>(+23.91%)</b></td><td>170.62 (+4.95%)</td><td>178.30 (+9.05%)</td><td>128.80 (-12.44%)</td><td>42.80 <b>(+168.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>162.58 (n/a)</td><td>163.50 (n/a)</td><td>147.10 (n/a)</td><td>15.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (-15.02%)</td><td>0.07 (+6.26%)</td><td>0.07 (+16.14%)</td><td>0.06 (+9.50%)</td><td>0.01 <b>(-39.03%)</b></td><td>215.70 (-8.68%)</td><td>182.88 (-8.69%)</td><td>181.00 (-13.89%)</td><td>148.70 (+17.74%)</td><td>30.16 <b>(-32.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>236.20 (n/a)</td><td>200.28 (n/a)</td><td>210.20 (n/a)</td><td>126.30 (n/a)</td><td>44.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 <b>(+30.86%)</b></td><td>0.06 (+5.55%)</td><td>0.06 (-0.65%)</td><td>0.04 <b>(-20.00%)</b></td><td>0.02 <b>(+113.74%)</b></td><td>315.20 <b>(+24.98%)</b></td><td>206.16 (+0.36%)</td><td>197.10 (+0.66%)</td><td>132.80 <b>(-23.59%)</b></td><td>66.75 <b>(+109.32%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.20 (n/a)</td><td>205.42 (n/a)</td><td>195.80 (n/a)</td><td>173.80 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 <b>(+38.53%)</b></td><td>0.18 (+16.23%)</td><td>0.18 (+18.30%)</td><td>0.14 (-7.68%)</td><td>0.03 <b>(+647.08%)</b></td><td>182.00 (+8.33%)</td><td>142.14 (-11.54%)</td><td>134.40 (-15.47%)</td><td>112.70 <b>(-27.80%)</b></td><td>27.44 <b>(+487.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.00 (n/a)</td><td>168.00 (n/a)</td><td>160.68 (n/a)</td><td>159.00 (n/a)</td><td>156.10 (n/a)</td><td>4.67 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (+12.77%)</td><td>0.17 (+12.97%)</td><td>0.18 (+18.31%)</td><td>0.12 (+3.11%)</td><td>0.04 <b>(+42.75%)</b></td><td>198.60 (-3.03%)</td><td>146.52 (-10.08%)</td><td>133.40 (-15.46%)</td><td>115.10 (-11.33%)</td><td>33.25 <b>(+23.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>162.94 (n/a)</td><td>157.80 (n/a)</td><td>129.80 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (+15.52%)</td><td>0.18 <b>(+22.60%)</b></td><td>0.19 <b>(+25.45%)</b></td><td>0.15 <b>(+35.12%)</b></td><td>0.02 (-17.54%)</td><td>166.90 <b>(-25.99%)</b></td><td>138.50 (-19.54%)</td><td>131.90 <b>(-20.30%)</b></td><td>124.30 (-13.44%)</td><td>16.87 <b>(-47.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>225.50 (n/a)</td><td>172.14 (n/a)</td><td>165.50 (n/a)</td><td>143.60 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (-4.25%)</td><td>0.17 (+5.04%)</td><td>0.17 <b>(+20.35%)</b></td><td>0.13 (-3.90%)</td><td>0.03 (-10.67%)</td><td>190.90 (+4.03%)</td><td>152.48 (-5.23%)</td><td>148.50 (-16.90%)</td><td>125.10 (+4.42%)</td><td>27.11 (-5.80%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.50 (n/a)</td><td>160.90 (n/a)</td><td>178.70 (n/a)</td><td>119.80 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (+10.25%)</td><td>0.17 <b>(+27.68%)</b></td><td>0.17 <b>(+36.72%)</b></td><td>0.14 <b>(+24.40%)</b></td><td>0.02 (-9.11%)</td><td>180.80 (-19.64%)</td><td>147.70 <b>(-22.30%)</b></td><td>142.60 <b>(-26.83%)</b></td><td>131.70 (-9.30%)</td><td>20.05 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>190.08 (n/a)</td><td>194.90 (n/a)</td><td>145.20 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (-19.34%)</td><td>0.16 (+3.81%)</td><td>0.16 (+8.79%)</td><td>0.14 <b>(+21.56%)</b></td><td>0.02 <b>(-57.30%)</b></td><td>181.90 (-17.73%)</td><td>158.54 (-7.01%)</td><td>155.20 (-8.11%)</td><td>143.00 <b>(+24.02%)</b></td><td>16.85 <b>(-55.39%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>221.10 (n/a)</td><td>170.50 (n/a)</td><td>168.90 (n/a)</td><td>115.30 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (+17.34%)</td><td>0.16 <b>(+23.50%)</b></td><td>0.16 <b>(+33.19%)</b></td><td>0.13 <b>(+51.81%)</b></td><td>0.02 <b>(-22.92%)</b></td><td>182.30 <b>(-34.14%)</b></td><td>156.18 <b>(-21.63%)</b></td><td>154.60 <b>(-24.95%)</b></td><td>128.30 (-14.81%)</td><td>23.42 <b>(-54.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>276.80 (n/a)</td><td>199.28 (n/a)</td><td>206.00 (n/a)</td><td>150.60 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (-10.09%)</td><td>0.15 (+8.65%)</td><td>0.16 (+9.56%)</td><td>0.12 (+10.30%)</td><td>0.02 <b>(-34.81%)</b></td><td>212.40 (-9.35%)</td><td>163.18 (-10.27%)</td><td>155.10 (-8.71%)</td><td>140.00 (+11.20%)</td><td>28.56 <b>(-32.60%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>234.30 (n/a)</td><td>181.86 (n/a)</td><td>169.90 (n/a)</td><td>125.90 (n/a)</td><td>42.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (+1.74%)</td><td>0.33 (+15.15%)</td><td>0.36 (+13.68%)</td><td>0.19 <b>(+26.30%)</b></td><td>0.08 (-14.62%)</td><td>255.50 <b>(-20.82%)</b></td><td>159.32 (-16.87%)</td><td>138.40 (-12.02%)</td><td>127.50 (-1.70%)</td><td>54.38 <b>(-31.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>322.70 (n/a)</td><td>191.66 (n/a)</td><td>157.30 (n/a)</td><td>129.70 (n/a)</td><td>79.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.42 (-5.86%)</td><td>0.34 (-2.27%)</td><td>0.34 (-0.23%)</td><td>0.25 (-5.00%)</td><td>0.06 (-0.94%)</td><td>197.30 (+5.23%)</td><td>150.02 (+2.61%)</td><td>145.90 (+0.21%)</td><td>118.00 (+6.21%)</td><td>30.72 (+11.37%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>187.50 (n/a)</td><td>146.20 (n/a)</td><td>145.60 (n/a)</td><td>111.10 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.41 (-0.36%)</td><td>0.35 (+9.24%)</td><td>0.38 (+18.57%)</td><td>0.27 (+7.93%)</td><td>0.06 (+0.51%)</td><td>179.00 (-7.35%)</td><td>145.22 (-8.53%)</td><td>130.60 (-15.69%)</td><td>120.00 (+0.33%)</td><td>26.11 (-3.72%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>193.20 (n/a)</td><td>158.76 (n/a)</td><td>154.90 (n/a)</td><td>119.60 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (-5.67%)</td><td>0.32 (-3.71%)</td><td>0.29 (-14.28%)</td><td>0.27 (-2.25%)</td><td>0.06 (+3.65%)</td><td>181.50 (+2.25%)</td><td>156.26 (+4.20%)</td><td>169.60 (+16.64%)</td><td>124.90 (+6.03%)</td><td>25.67 (+11.58%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>177.50 (n/a)</td><td>149.96 (n/a)</td><td>145.40 (n/a)</td><td>117.80 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (+6.27%)</td><td>0.29 (+6.62%)</td><td>0.34 <b>(+31.40%)</b></td><td>0.17 <b>(-25.79%)</b></td><td>0.10 <b>(+99.42%)</b></td><td>294.30 <b>(+34.75%)</b></td><td>189.48 (+2.22%)</td><td>143.30 <b>(-23.86%)</b></td><td>131.20 (-5.88%)</td><td>73.76 <b>(+156.58%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>218.40 (n/a)</td><td>185.36 (n/a)</td><td>188.20 (n/a)</td><td>139.40 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (+0.97%)</td><td>0.31 (+17.38%)</td><td>0.29 (+16.60%)</td><td>0.29 <b>(+42.40%)</b></td><td>0.03 <b>(-47.36%)</b></td><td>171.20 <b>(-29.78%)</b></td><td>160.60 (-17.54%)</td><td>167.20 (-14.21%)</td><td>134.50 (-0.96%)</td><td>15.30 <b>(-63.24%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>243.80 (n/a)</td><td>194.76 (n/a)</td><td>194.90 (n/a)</td><td>135.80 (n/a)</td><td>41.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (-6.36%)</td><td>0.25 (-9.36%)</td><td>0.26 (+3.22%)</td><td>0.15 <b>(-37.87%)</b></td><td>0.06 <b>(+56.57%)</b></td><td>320.30 <b>(+60.95%)</b></td><td>207.52 (+16.01%)</td><td>188.60 (-3.08%)</td><td>155.80 (+6.79%)</td><td>66.72 <b>(+169.77%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>199.00 (n/a)</td><td>178.88 (n/a)</td><td>194.60 (n/a)</td><td>145.90 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (+14.13%)</td><td>0.28 (+18.48%)</td><td>0.24 (+8.89%)</td><td>0.20 <b>(+44.92%)</b></td><td>0.09 (+16.30%)</td><td>250.60 <b>(-31.00%)</b></td><td>188.80 (-17.08%)</td><td>202.00 (-8.18%)</td><td>126.90 (-12.36%)</td><td>56.01 <b>(-33.07%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>363.20 (n/a)</td><td>227.68 (n/a)</td><td>220.00 (n/a)</td><td>144.80 (n/a)</td><td>83.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(+22.75%)</b></td><td>0.02 (+16.98%)</td><td>0.02 (+11.80%)</td><td>0.02 <b>(+27.77%)</b></td><td>0.00 (-3.93%)</td><td>146.50 <b>(-21.74%)</b></td><td>134.96 (-15.10%)</td><td>139.50 (-10.52%)</td><td>110.90 (-18.52%)</td><td>13.86 <b>(-39.62%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>187.20 (n/a)</td><td>158.96 (n/a)</td><td>155.90 (n/a)</td><td>136.10 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(+33.35%)</b></td><td>0.02 <b>(+37.24%)</b></td><td>0.02 <b>(+32.64%)</b></td><td>0.02 <b>(+64.46%)</b></td><td>0.00 (+7.92%)</td><td>154.40 <b>(-39.19%)</b></td><td>131.46 <b>(-28.69%)</b></td><td>133.80 <b>(-24.58%)</b></td><td>97.30 <b>(-24.98%)</b></td><td>20.97 <b>(-53.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>253.90 (n/a)</td><td>184.34 (n/a)</td><td>177.40 (n/a)</td><td>129.70 (n/a)</td><td>44.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (+2.86%)</td><td>0.02 (+9.82%)</td><td>0.02 (+17.40%)</td><td>0.01 (+13.96%)</td><td>0.00 (+5.73%)</td><td>184.90 (-12.24%)</td><td>155.50 (-8.98%)</td><td>144.70 (-14.83%)</td><td>131.30 (-2.81%)</td><td>24.69 (-8.10%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>170.84 (n/a)</td><td>169.90 (n/a)</td><td>135.10 (n/a)</td><td>26.87 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (-8.81%)</td><td>0.02 (+9.20%)</td><td>0.02 (+19.98%)</td><td>0.02 <b>(+26.13%)</b></td><td>0.00 <b>(-61.78%)</b></td><td>172.00 <b>(-20.74%)</b></td><td>156.00 (-11.03%)</td><td>154.90 (-16.63%)</td><td>140.90 (+9.65%)</td><td>11.57 <b>(-66.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>175.34 (n/a)</td><td>185.80 (n/a)</td><td>128.50 (n/a)</td><td>34.31 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (-7.09%)</td><td>0.02 (+2.38%)</td><td>0.02 (+15.28%)</td><td>0.01 (+6.42%)</td><td>0.00 <b>(-26.56%)</b></td><td>201.70 (-6.05%)</td><td>168.52 (-4.98%)</td><td>169.80 (-13.23%)</td><td>120.80 (+7.66%)</td><td>31.98 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>214.70 (n/a)</td><td>177.36 (n/a)</td><td>195.70 (n/a)</td><td>112.20 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (-16.06%)</td><td>0.01 (+0.22%)</td><td>0.01 (+9.00%)</td><td>0.01 (+3.24%)</td><td>0.00 <b>(-42.79%)</b></td><td>226.10 (-3.13%)</td><td>185.64 (-2.67%)</td><td>175.70 (-8.25%)</td><td>159.30 (+19.15%)</td><td>26.83 <b>(-34.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.40 (n/a)</td><td>190.74 (n/a)</td><td>191.50 (n/a)</td><td>133.70 (n/a)</td><td>40.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(+43.07%)</b></td><td>0.02 <b>(+21.48%)</b></td><td>0.01 (+6.18%)</td><td>0.01 <b>(+20.44%)</b></td><td>0.01 <b>(+88.83%)</b></td><td>204.30 (-16.98%)</td><td>169.36 (-14.94%)</td><td>179.20 (-5.83%)</td><td>102.60 <b>(-30.11%)</b></td><td>42.32 (+8.97%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>246.10 (n/a)</td><td>199.10 (n/a)</td><td>190.30 (n/a)</td><td>146.80 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.01 (-0.68%)</td><td>0.01 (+9.57%)</td><td>0.01 (-1.43%)</td><td>0.01 <b>(+73.51%)</b></td><td>0.00 <b>(-53.28%)</b></td><td>233.00 <b>(-42.37%)</b></td><td>210.30 (-14.88%)</td><td>222.00 (+1.46%)</td><td>181.30 (+0.67%)</td><td>23.02 <b>(-74.48%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>404.30 (n/a)</td><td>247.06 (n/a)</td><td>218.80 (n/a)</td><td>180.10 (n/a)</td><td>90.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-24.44%)</b></td><td>0.03 (-14.17%)</td><td>0.03 (-0.58%)</td><td>0.03 (-7.48%)</td><td>0.00 <b>(-67.01%)</b></td><td>199.90 (+8.05%)</td><td>176.00 (+13.42%)</td><td>173.10 (+0.58%)</td><td>160.00 <b>(+32.34%)</b></td><td>14.59 <b>(-51.08%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>155.18 (n/a)</td><td>172.10 (n/a)</td><td>120.90 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-0.05%)</td><td>0.03 (+14.11%)</td><td>0.03 <b>(+21.06%)</b></td><td>0.03 <b>(+44.15%)</b></td><td>0.00 <b>(-61.53%)</b></td><td>191.90 <b>(-30.65%)</b></td><td>170.82 (-16.23%)</td><td>169.20 (-17.42%)</td><td>151.80 (+0.07%)</td><td>14.28 <b>(-72.40%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>276.70 (n/a)</td><td>203.92 (n/a)</td><td>204.90 (n/a)</td><td>151.70 (n/a)</td><td>51.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (+13.97%)</td><td>0.03 (+9.67%)</td><td>0.03 (+2.91%)</td><td>0.03 (+13.66%)</td><td>0.01 (+11.51%)</td><td>199.70 (-11.99%)</td><td>166.26 (-9.07%)</td><td>179.20 (-2.82%)</td><td>114.60 (-12.25%)</td><td>32.68 (-17.01%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>182.84 (n/a)</td><td>184.40 (n/a)</td><td>130.60 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+2.59%)</td><td>0.03 (+10.12%)</td><td>0.03 (+8.89%)</td><td>0.02 <b>(+64.58%)</b></td><td>0.01 <b>(-28.41%)</b></td><td>231.90 <b>(-39.25%)</b></td><td>196.52 (-15.10%)</td><td>208.40 (-8.15%)</td><td>154.40 (-2.53%)</td><td>38.39 <b>(-57.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>381.70 (n/a)</td><td>231.48 (n/a)</td><td>226.90 (n/a)</td><td>158.40 (n/a)</td><td>90.31 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-4.99%)</td><td>0.03 (+1.51%)</td><td>0.03 (-1.60%)</td><td>0.03 (+10.89%)</td><td>0.00 <b>(-50.10%)</b></td><td>200.60 (-9.84%)</td><td>186.64 (-2.58%)</td><td>189.70 (+1.61%)</td><td>170.50 (+5.25%)</td><td>12.08 <b>(-53.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.50 (n/a)</td><td>191.58 (n/a)</td><td>186.70 (n/a)</td><td>162.00 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+14.55%)</td><td>0.03 (+9.39%)</td><td>0.03 (+6.37%)</td><td>0.03 (+10.12%)</td><td>0.00 <b>(+50.25%)</b></td><td>194.00 (-9.22%)</td><td>179.80 (-8.39%)</td><td>185.10 (-5.99%)</td><td>159.20 (-12.67%)</td><td>13.56 (+17.36%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>196.26 (n/a)</td><td>196.90 (n/a)</td><td>182.30 (n/a)</td><td>11.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+12.20%)</td><td>0.03 (+7.22%)</td><td>0.03 (+4.29%)</td><td>0.02 (-3.87%)</td><td>0.00 <b>(+111.76%)</b></td><td>224.20 (+4.04%)</td><td>189.86 (-5.16%)</td><td>191.40 (-4.11%)</td><td>156.00 (-10.91%)</td><td>31.33 <b>(+95.94%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.50 (n/a)</td><td>200.18 (n/a)</td><td>199.60 (n/a)</td><td>175.10 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+3.17%)</td><td>0.02 (-1.97%)</td><td>0.02 (-4.78%)</td><td>0.02 (+6.48%)</td><td>0.00 (+3.13%)</td><td>256.50 (-6.11%)</td><td>230.98 (+1.93%)</td><td>242.60 (+5.02%)</td><td>176.70 (-3.07%)</td><td>32.36 (-6.98%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>273.20 (n/a)</td><td>226.60 (n/a)</td><td>231.00 (n/a)</td><td>182.30 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (+11.14%)</td><td>0.06 (+2.28%)</td><td>0.06 (-7.09%)</td><td>0.05 (+14.46%)</td><td>0.01 (+0.44%)</td><td>196.90 (-12.64%)</td><td>167.56 (-2.91%)</td><td>174.10 (+7.67%)</td><td>123.70 (-10.04%)</td><td>29.63 <b>(-20.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>172.58 (n/a)</td><td>161.70 (n/a)</td><td>137.50 (n/a)</td><td>37.29 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 <b>(+23.80%)</b></td><td>0.06 (+6.10%)</td><td>0.07 (+0.86%)</td><td>0.05 (+14.03%)</td><td>0.01 <b>(+33.82%)</b></td><td>221.90 (-12.29%)</td><td>171.02 (-4.99%)</td><td>160.20 (-0.87%)</td><td>124.10 (-19.21%)</td><td>38.95 (-6.24%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>253.00 (n/a)</td><td>180.00 (n/a)</td><td>161.60 (n/a)</td><td>153.60 (n/a)</td><td>41.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (+10.05%)</td><td>0.07 <b>(+25.00%)</b></td><td>0.07 (+11.58%)</td><td>0.05 <b>(+49.74%)</b></td><td>0.01 <b>(-32.76%)</b></td><td>206.20 <b>(-33.20%)</b></td><td>158.78 <b>(-25.69%)</b></td><td>152.60 (-10.39%)</td><td>123.90 (-9.10%)</td><td>30.54 <b>(-60.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>308.70 (n/a)</td><td>213.68 (n/a)</td><td>170.30 (n/a)</td><td>136.30 (n/a)</td><td>77.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (-4.57%)</td><td>0.07 (+5.22%)</td><td>0.06 (+6.27%)</td><td>0.05 (+9.38%)</td><td>0.01 <b>(-23.37%)</b></td><td>193.90 (-8.58%)</td><td>162.84 (-5.94%)</td><td>166.90 (-5.87%)</td><td>137.50 (+4.80%)</td><td>21.96 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>173.12 (n/a)</td><td>177.30 (n/a)</td><td>131.20 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 <b>(+24.45%)</b></td><td>0.06 (+4.40%)</td><td>0.06 (+2.26%)</td><td>0.05 (+13.87%)</td><td>0.01 <b>(+54.52%)</b></td><td>207.90 (-12.17%)</td><td>176.34 (-2.89%)</td><td>173.20 (-2.20%)</td><td>122.70 (-19.65%)</td><td>34.41 (+5.63%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>181.58 (n/a)</td><td>177.10 (n/a)</td><td>152.70 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (-1.63%)</td><td>0.06 (-9.33%)</td><td>0.05 (-4.43%)</td><td>0.03 <b>(-30.59%)</b></td><td>0.02 (+8.14%)</td><td>335.60 <b>(+44.10%)</b></td><td>208.36 (+14.91%)</td><td>201.10 (+4.63%)</td><td>115.00 (+1.59%)</td><td>80.13 <b>(+55.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>181.32 (n/a)</td><td>192.20 (n/a)</td><td>113.20 (n/a)</td><td>51.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (+10.59%)</td><td>0.06 (-11.24%)</td><td>0.05 <b>(-25.79%)</b></td><td>0.05 (+3.82%)</td><td>0.02 <b>(+29.13%)</b></td><td>228.60 (-3.67%)</td><td>191.90 (+14.51%)</td><td>204.80 <b>(+34.83%)</b></td><td>114.70 (-9.54%)</td><td>44.83 (+4.32%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>167.58 (n/a)</td><td>151.90 (n/a)</td><td>126.80 (n/a)</td><td>42.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-8.35%)</td><td>0.04 (-16.49%)</td><td>0.05 (-14.43%)</td><td>0.03 <b>(-26.68%)</b></td><td>0.01 <b>(+26.68%)</b></td><td>364.50 <b>(+36.41%)</b></td><td>270.46 <b>(+23.86%)</b></td><td>227.90 (+16.87%)</td><td>200.20 (+9.10%)</td><td>75.05 <b>(+91.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>267.20 (n/a)</td><td>218.36 (n/a)</td><td>195.00 (n/a)</td><td>183.50 (n/a)</td><td>39.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 <b>(-30.10%)</b></td><td>0.10 <b>(-27.35%)</b></td><td>0.10 <b>(-26.56%)</b></td><td>0.09 <b>(-27.73%)</b></td><td>0.01 <b>(-44.39%)</b></td><td>229.30 <b>(+38.38%)</b></td><td>215.74 <b>(+37.29%)</b></td><td>220.70 <b>(+36.15%)</b></td><td>190.50 <b>(+43.02%)</b></td><td>14.87 (+9.76%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>165.70 (n/a)</td><td>157.14 (n/a)</td><td>162.10 (n/a)</td><td>133.20 (n/a)</td><td>13.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (-17.48%)</td><td>0.11 <b>(-28.26%)</b></td><td>0.11 <b>(-30.94%)</b></td><td>0.09 <b>(-27.60%)</b></td><td>0.02 (+15.08%)</td><td>232.60 <b>(+38.12%)</b></td><td>199.54 <b>(+40.72%)</b></td><td>198.20 <b>(+44.78%)</b></td><td>157.20 <b>(+21.20%)</b></td><td>28.63 <b>(+86.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>168.40 (n/a)</td><td>141.80 (n/a)</td><td>136.90 (n/a)</td><td>129.70 (n/a)</td><td>15.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (-5.87%)</td><td>0.12 (+0.09%)</td><td>0.12 (-9.55%)</td><td>0.10 <b>(+77.86%)</b></td><td>0.02 <b>(-59.17%)</b></td><td>202.50 <b>(-43.78%)</b></td><td>172.88 (-11.09%)</td><td>179.30 (+10.54%)</td><td>143.80 (+6.28%)</td><td>22.30 <b>(-76.41%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>360.20 (n/a)</td><td>194.44 (n/a)</td><td>162.20 (n/a)</td><td>135.30 (n/a)</td><td>94.49 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (-19.09%)</td><td>0.11 (-12.20%)</td><td>0.12 (-11.10%)</td><td>0.10 (+13.96%)</td><td>0.01 <b>(-55.06%)</b></td><td>209.00 (-12.26%)</td><td>187.82 (+10.76%)</td><td>178.50 (+12.55%)</td><td>168.50 <b>(+23.62%)</b></td><td>18.68 <b>(-52.87%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>238.20 (n/a)</td><td>169.58 (n/a)</td><td>158.60 (n/a)</td><td>136.30 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (-11.42%)</td><td>0.13 (+2.48%)</td><td>0.13 (-0.62%)</td><td>0.12 <b>(+24.77%)</b></td><td>0.01 <b>(-77.94%)</b></td><td>175.60 (-19.85%)</td><td>165.28 (-5.27%)</td><td>163.00 (+0.62%)</td><td>158.70 (+12.87%)</td><td>6.93 <b>(-80.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>219.10 (n/a)</td><td>174.48 (n/a)</td><td>162.00 (n/a)</td><td>140.60 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 <b>(+22.14%)</b></td><td>0.14 (+17.98%)</td><td>0.15 (+18.88%)</td><td>0.10 <b>(+24.61%)</b></td><td>0.03 <b>(+28.42%)</b></td><td>207.10 (-19.76%)</td><td>159.36 (-14.91%)</td><td>137.20 (-15.88%)</td><td>125.40 (-18.09%)</td><td>37.26 (-14.79%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>258.10 (n/a)</td><td>187.28 (n/a)</td><td>163.10 (n/a)</td><td>153.10 (n/a)</td><td>43.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (-12.01%)</td><td>0.14 (+11.49%)</td><td>0.14 (+12.04%)</td><td>0.13 <b>(+34.53%)</b></td><td>0.01 <b>(-66.02%)</b></td><td>165.20 <b>(-25.69%)</b></td><td>150.84 (-13.80%)</td><td>147.60 (-10.76%)</td><td>138.10 (+13.66%)</td><td>11.33 <b>(-71.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>222.30 (n/a)</td><td>174.98 (n/a)</td><td>165.40 (n/a)</td><td>121.50 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 <b>(-22.10%)</b></td><td>0.10 (-5.59%)</td><td>0.11 (+11.18%)</td><td>0.06 <b>(-33.14%)</b></td><td>0.02 (-4.59%)</td><td>329.90 <b>(+49.61%)</b></td><td>217.34 (+8.32%)</td><td>192.80 (-10.03%)</td><td>182.90 <b>(+28.35%)</b></td><td>63.08 <b>(+91.24%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>200.64 (n/a)</td><td>214.30 (n/a)</td><td>142.50 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>170.74 (n/a)</td><td>168.90 (n/a)</td><td>147.20 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.80 (n/a)</td><td>193.78 (n/a)</td><td>193.90 (n/a)</td><td>159.70 (n/a)</td><td>28.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>186.08 (n/a)</td><td>183.60 (n/a)</td><td>165.10 (n/a)</td><td>17.08 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>177.72 (n/a)</td><td>168.50 (n/a)</td><td>142.70 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>152.38 (n/a)</td><td>147.70 (n/a)</td><td>122.20 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>260.70 (n/a)</td><td>181.48 (n/a)</td><td>173.30 (n/a)</td><td>143.20 (n/a)</td><td>47.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>173.50 (n/a)</td><td>177.60 (n/a)</td><td>135.00 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>188.84 (n/a)</td><td>193.70 (n/a)</td><td>144.70 (n/a)</td><td>38.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>178.00 (n/a)</td><td>159.24 (n/a)</td><td>161.70 (n/a)</td><td>127.80 (n/a)</td><td>20.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>161.76 (n/a)</td><td>144.70 (n/a)</td><td>140.20 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>250.10 (n/a)</td><td>205.14 (n/a)</td><td>198.10 (n/a)</td><td>164.60 (n/a)</td><td>34.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>247.20 (n/a)</td><td>209.30 (n/a)</td><td>203.00 (n/a)</td><td>168.90 (n/a)</td><td>30.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.36 (-13.30%)</td><td>0.29 (-16.19%)</td><td>0.31 (-3.69%)</td><td>0.21 <b>(-24.81%)</b></td><td>0.06 (-4.75%)</td><td>232.90 <b>(+33.01%)</b></td><td>176.32 <b>(+20.62%)</b></td><td>157.10 (+3.83%)</td><td>137.50 (+15.35%)</td><td>38.75 <b>(+52.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>175.10 (n/a)</td><td>146.18 (n/a)</td><td>151.30 (n/a)</td><td>119.20 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>267.10 (n/a)</td><td>186.82 (n/a)</td><td>175.20 (n/a)</td><td>149.90 (n/a)</td><td>46.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>372.40 (n/a)</td><td>236.56 (n/a)</td><td>198.10 (n/a)</td><td>152.90 (n/a)</td><td>88.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.00 (n/a)</td><td>183.70 (n/a)</td><td>179.72 (n/a)</td><td>179.60 (n/a)</td><td>176.90 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.00 (n/a)</td><td>164.22 (n/a)</td><td>166.80 (n/a)</td><td>139.50 (n/a)</td><td>15.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>163.20 (n/a)</td><td>153.52 (n/a)</td><td>156.50 (n/a)</td><td>134.00 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>169.86 (n/a)</td><td>149.30 (n/a)</td><td>148.30 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>192.08 (n/a)</td><td>189.70 (n/a)</td><td>147.40 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>166.40 (n/a)</td><td>177.00 (n/a)</td><td>131.60 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>164.00 (n/a)</td><td>142.90 (n/a)</td><td>128.40 (n/a)</td><td>41.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>310.00 (n/a)</td><td>212.28 (n/a)</td><td>174.90 (n/a)</td><td>151.40 (n/a)</td><td>69.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>175.96 (n/a)</td><td>192.50 (n/a)</td><td>128.80 (n/a)</td><td>36.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>379.80 (n/a)</td><td>219.24 (n/a)</td><td>191.90 (n/a)</td><td>140.70 (n/a)</td><td>92.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>161.28 (n/a)</td><td>169.10 (n/a)</td><td>116.60 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>237.80 (n/a)</td><td>172.76 (n/a)</td><td>176.40 (n/a)</td><td>133.90 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>337.70 (n/a)</td><td>238.72 (n/a)</td><td>264.80 (n/a)</td><td>150.90 (n/a)</td><td>78.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>176.24 (n/a)</td><td>180.00 (n/a)</td><td>153.50 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>242.20 (n/a)</td><td>178.06 (n/a)</td><td>174.40 (n/a)</td><td>120.00 (n/a)</td><td>50.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>228.70 (n/a)</td><td>197.76 (n/a)</td><td>207.60 (n/a)</td><td>152.10 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.00 (n/a)</td><td>125.86 (n/a)</td><td>117.00 (n/a)</td><td>110.60 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>169.12 (n/a)</td><td>163.30 (n/a)</td><td>119.20 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>160.92 (n/a)</td><td>152.30 (n/a)</td><td>129.60 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>166.14 (n/a)</td><td>165.70 (n/a)</td><td>115.80 (n/a)</td><td>47.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>319.70 (n/a)</td><td>197.48 (n/a)</td><td>182.00 (n/a)</td><td>115.80 (n/a)</td><td>75.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.50 (n/a)</td><td>188.88 (n/a)</td><td>175.80 (n/a)</td><td>162.40 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>290.20 (n/a)</td><td>209.22 (n/a)</td><td>200.60 (n/a)</td><td>173.40 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>327.50 (n/a)</td><td>239.24 (n/a)</td><td>226.00 (n/a)</td><td>187.50 (n/a)</td><td>53.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>179.48 (n/a)</td><td>183.80 (n/a)</td><td>155.80 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.90 (n/a)</td><td>144.54 (n/a)</td><td>142.80 (n/a)</td><td>118.10 (n/a)</td><td>19.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>155.96 (n/a)</td><td>159.60 (n/a)</td><td>115.60 (n/a)</td><td>38.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>163.28 (n/a)</td><td>151.80 (n/a)</td><td>142.70 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>183.66 (n/a)</td><td>181.10 (n/a)</td><td>148.00 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.00 (n/a)</td><td>199.96 (n/a)</td><td>193.00 (n/a)</td><td>159.60 (n/a)</td><td>43.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>182.78 (n/a)</td><td>175.50 (n/a)</td><td>148.10 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.20 (n/a)</td><td>199.36 (n/a)</td><td>189.30 (n/a)</td><td>175.90 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>175.60 (n/a)</td><td>145.86 (n/a)</td><td>149.40 (n/a)</td><td>114.20 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.90 (n/a)</td><td>168.86 (n/a)</td><td>176.20 (n/a)</td><td>129.50 (n/a)</td><td>27.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>173.40 (n/a)</td><td>184.50 (n/a)</td><td>138.50 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>161.82 (n/a)</td><td>167.80 (n/a)</td><td>119.80 (n/a)</td><td>25.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.40 (n/a)</td><td>168.70 (n/a)</td><td>175.30 (n/a)</td><td>123.70 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>197.60 (n/a)</td><td>187.90 (n/a)</td><td>175.10 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>168.76 (n/a)</td><td>157.40 (n/a)</td><td>131.60 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.40 (n/a)</td><td>220.22 (n/a)</td><td>233.90 (n/a)</td><td>179.30 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.30 (n/a)</td><td>154.20 (n/a)</td><td>151.20 (n/a)</td><td>127.00 (n/a)</td><td>26.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>235.10 (n/a)</td><td>186.24 (n/a)</td><td>200.00 (n/a)</td><td>133.50 (n/a)</td><td>46.00 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.60 (n/a)</td><td>161.96 (n/a)</td><td>172.70 (n/a)</td><td>122.20 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.20 (n/a)</td><td>157.64 (n/a)</td><td>153.00 (n/a)</td><td>127.40 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>265.30 (n/a)</td><td>187.04 (n/a)</td><td>171.20 (n/a)</td><td>153.30 (n/a)</td><td>44.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>169.48 (n/a)</td><td>167.60 (n/a)</td><td>145.10 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>214.12 (n/a)</td><td>213.10 (n/a)</td><td>187.00 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.46 (+4.07%)</td><td>3.83 (-3.64%)</td><td>3.71 (-8.56%)</td><td>3.45 (-0.49%)</td><td>0.43 <b>(+40.10%)</b></td><td>2726.10 (+0.49%)</td><td>2478.58 (+4.24%)</td><td>2538.20 (+9.36%)</td><td>2110.30 (-3.92%)</td><td>263.12 <b>(+33.86%)</b></td><td>1752.97 (+4.07%)</td><td>1506.76 (-3.64%)</td><td>1457.49 (-8.56%)</td><td>1357.04 (-0.49%)</td><td>167.82 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>4.28 (n/a)</td><td>3.98 (n/a)</td><td>4.05 (n/a)</td><td>3.47 (n/a)</td><td>0.30 (n/a)</td><td>2712.80 (n/a)</td><td>2377.84 (n/a)</td><td>2321.00 (n/a)</td><td>2196.30 (n/a)</td><td>196.57 (n/a)</td><td>1684.37 (n/a)</td><td>1563.67 (n/a)</td><td>1593.88 (n/a)</td><td>1363.66 (n/a)</td><td>119.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.00 (-10.25%)</td><td>0.93 (-2.52%)</td><td>0.98 (-10.62%)</td><td>0.73 (+19.51%)</td><td>0.12 <b>(-48.18%)</b></td><td>303.30 (-16.33%)</td><td>240.12 (-1.50%)</td><td>225.30 (+11.87%)</td><td>220.50 (+11.42%)</td><td>35.47 <b>(-50.09%)</b></td><td>42.81 (-10.25%)</td><td>39.89 (-2.52%)</td><td>41.89 (-10.62%)</td><td>31.12 (+19.51%)</td><td>4.94 <b>(-48.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.12 (n/a)</td><td>0.96 (n/a)</td><td>1.10 (n/a)</td><td>0.61 (n/a)</td><td>0.22 (n/a)</td><td>362.50 (n/a)</td><td>243.78 (n/a)</td><td>201.40 (n/a)</td><td>197.90 (n/a)</td><td>71.07 (n/a)</td><td>47.69 (n/a)</td><td>40.92 (n/a)</td><td>46.87 (n/a)</td><td>26.04 (n/a)</td><td>9.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.25 (+7.29%)</td><td>1.01 (+11.03%)</td><td>1.01 (+10.15%)</td><td>0.77 <b>(+33.43%)</b></td><td>0.17 <b>(-21.15%)</b></td><td>289.10 <b>(-25.05%)</b></td><td>225.38 (-12.80%)</td><td>218.50 (-9.22%)</td><td>177.40 (-6.78%)</td><td>40.80 <b>(-46.18%)</b></td><td>53.21 (+7.29%)</td><td>42.93 (+11.03%)</td><td>43.19 (+10.15%)</td><td>32.65 <b>(+33.43%)</b></td><td>7.41 <b>(-21.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.16 (n/a)</td><td>0.91 (n/a)</td><td>0.92 (n/a)</td><td>0.57 (n/a)</td><td>0.22 (n/a)</td><td>385.70 (n/a)</td><td>258.46 (n/a)</td><td>240.70 (n/a)</td><td>190.30 (n/a)</td><td>75.81 (n/a)</td><td>49.59 (n/a)</td><td>38.67 (n/a)</td><td>39.21 (n/a)</td><td>24.47 (n/a)</td><td>9.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.52 (+0.79%)</td><td>0.52 (+0.25%)</td><td>0.52 (+0.16%)</td><td>0.52 (+0.17%)</td><td>0.00 <b>(+107.92%)</b></td><td>48789.30 (-0.17%)</td><td>48616.20 (-0.25%)</td><td>48668.60 (-0.16%)</td><td>48227.60 (-0.78%)</td><td>224.50 <b>(+105.81%)</b></td><td>356.22 (+0.79%)</td><td>353.38 (+0.25%)</td><td>353.00 (+0.16%)</td><td>352.12 (+0.17%)</td><td>1.64 <b>(+107.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.00 (n/a)</td><td>48871.20 (n/a)</td><td>48737.48 (n/a)</td><td>48748.90 (n/a)</td><td>48608.70 (n/a)</td><td>109.08 (n/a)</td><td>353.43 (n/a)</td><td>352.50 (n/a)</td><td>352.42 (n/a)</td><td>351.53 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (-0.70%)</td><td>0.21 (-0.97%)</td><td>0.21 (-0.93%)</td><td>0.21 (-1.41%)</td><td>0.00 <b>(+23.56%)</b></td><td>119611.60 (+1.43%)</td><td>118155.90 (+0.98%)</td><td>118327.30 (+0.94%)</td><td>116478.50 (+0.70%)</td><td>1134.57 <b>(+26.14%)</b></td><td>147.49 (-0.70%)</td><td>145.41 (-0.97%)</td><td>145.19 (-0.93%)</td><td>143.63 (-1.41%)</td><td>1.40 <b>(+23.56%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>117925.70 (n/a)</td><td>117008.20 (n/a)</td><td>117227.10 (n/a)</td><td>115663.40 (n/a)</td><td>899.45 (n/a)</td><td>148.53 (n/a)</td><td>146.83 (n/a)</td><td>146.55 (n/a)</td><td>145.68 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.89 (-0.02%)</td><td>0.88 (+0.53%)</td><td>0.88 (+0.58%)</td><td>0.88 (+0.64%)</td><td>0.00 <b>(-44.11%)</b></td><td>28649.00 (-0.64%)</td><td>28495.86 (-0.53%)</td><td>28472.50 (-0.57%)</td><td>28379.40 (+0.02%)</td><td>103.90 <b>(-44.48%)</b></td><td>605.36 (-0.02%)</td><td>602.90 (+0.53%)</td><td>603.38 (+0.58%)</td><td>599.67 (+0.64%)</td><td>2.20 <b>(-44.11%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28833.80 (n/a)</td><td>28648.94 (n/a)</td><td>28636.60 (n/a)</td><td>28372.70 (n/a)</td><td>187.14 (n/a)</td><td>605.51 (n/a)</td><td>599.69 (n/a)</td><td>599.93 (n/a)</td><td>595.82 (n/a)</td><td>3.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.53 (+1.42%)</td><td>3.51 (+3.81%)</td><td>3.51 (+4.48%)</td><td>3.49 (+4.70%)</td><td>0.01 <b>(-76.67%)</b></td><td>7205.30 (-4.49%)</td><td>7165.34 (-3.69%)</td><td>7163.50 (-4.29%)</td><td>7133.10 (-1.40%)</td><td>27.76 <b>(-78.03%)</b></td><td>2408.47 (+1.42%)</td><td>2397.66 (+3.81%)</td><td>2398.24 (+4.48%)</td><td>2384.32 (+4.70%)</td><td>9.28 <b>(-76.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.48 (n/a)</td><td>3.38 (n/a)</td><td>3.36 (n/a)</td><td>3.34 (n/a)</td><td>0.06 (n/a)</td><td>7543.90 (n/a)</td><td>7439.82 (n/a)</td><td>7484.50 (n/a)</td><td>7234.60 (n/a)</td><td>126.36 (n/a)</td><td>2374.67 (n/a)</td><td>2309.71 (n/a)</td><td>2295.41 (n/a)</td><td>2277.30 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.24 (+8.29%)</td><td>2.90 (+1.65%)</td><td>2.84 (-0.24%)</td><td>2.73 (-0.27%)</td><td>0.20 <b>(+114.14%)</b></td><td>9216.40 (+0.27%)</td><td>8704.28 (-1.37%)</td><td>8871.10 (+0.24%)</td><td>7766.70 (-7.65%)</td><td>549.67 <b>(+95.66%)</b></td><td>2212.00 (+8.29%)</td><td>1980.50 (+1.65%)</td><td>1936.62 (-0.24%)</td><td>1864.06 (-0.27%)</td><td>134.07 <b>(+114.14%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>2.99 (n/a)</td><td>2.85 (n/a)</td><td>2.84 (n/a)</td><td>2.74 (n/a)</td><td>0.09 (n/a)</td><td>9191.70 (n/a)</td><td>8824.96 (n/a)</td><td>8849.50 (n/a)</td><td>8410.50 (n/a)</td><td>280.93 (n/a)</td><td>2042.68 (n/a)</td><td>1948.33 (n/a)</td><td>1941.34 (n/a)</td><td>1869.07 (n/a)</td><td>62.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.33 (-2.78%)</td><td>3.28 (+1.37%)</td><td>3.31 (+4.75%)</td><td>3.18 (+1.26%)</td><td>0.06 <b>(-52.09%)</b></td><td>7915.20 (-1.24%)</td><td>7675.54 (-1.44%)</td><td>7602.20 (-4.53%)</td><td>7560.10 (+2.86%)</td><td>144.68 <b>(-51.49%)</b></td><td>2272.43 (-2.78%)</td><td>2238.89 (+1.37%)</td><td>2259.85 (+4.75%)</td><td>2170.50 (+1.26%)</td><td>41.47 <b>(-52.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.42 (n/a)</td><td>3.24 (n/a)</td><td>3.16 (n/a)</td><td>3.14 (n/a)</td><td>0.13 (n/a)</td><td>8014.70 (n/a)</td><td>7787.98 (n/a)</td><td>7963.10 (n/a)</td><td>7349.90 (n/a)</td><td>298.23 (n/a)</td><td>2337.42 (n/a)</td><td>2208.59 (n/a)</td><td>2157.44 (n/a)</td><td>2143.55 (n/a)</td><td>86.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (+0.31%)</td><td>0.78 (+0.05%)</td><td>0.78 (-0.02%)</td><td>0.78 (-0.06%)</td><td>0.00 <b>(+407.64%)</b></td><td>96557.50 (+0.06%)</td><td>96413.38 (-0.05%)</td><td>96475.30 (+0.02%)</td><td>96119.50 (-0.30%)</td><td>171.43 <b>(+406.40%)</b></td><td>714.94 (+0.31%)</td><td>712.76 (+0.05%)</td><td>712.30 (-0.02%)</td><td>711.70 (-0.06%)</td><td>1.27 <b>(+407.63%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96495.80 (n/a)</td><td>96459.82 (n/a)</td><td>96452.20 (n/a)</td><td>96413.50 (n/a)</td><td>33.85 (n/a)</td><td>712.76 (n/a)</td><td>712.42 (n/a)</td><td>712.47 (n/a)</td><td>712.15 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.73 (-0.16%)</td><td>0.73 (-0.03%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.01%)</td><td>0.00 <b>(-55.33%)</b></td><td>103710.90 (+0.01%)</td><td>103630.30 (+0.03%)</td><td>103612.40 (-0.00%)</td><td>103596.20 (+0.16%)</td><td>46.18 <b>(-55.22%)</b></td><td>663.34 (-0.16%)</td><td>663.12 (-0.03%)</td><td>663.24 (+0.00%)</td><td>662.61 (-0.01%)</td><td>0.30 <b>(-55.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103696.10 (n/a)</td><td>103601.64 (n/a)</td><td>103613.90 (n/a)</td><td>103430.50 (n/a)</td><td>103.13 (n/a)</td><td>664.40 (n/a)</td><td>663.31 (n/a)</td><td>663.23 (n/a)</td><td>662.70 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.69 (-0.45%)</td><td>0.69 (+0.06%)</td><td>0.69 (-0.00%)</td><td>0.69 (+0.52%)</td><td>0.00 <b>(-71.02%)</b></td><td>109727.80 (-0.52%)</td><td>109553.90 (-0.06%)</td><td>109529.40 (+0.00%)</td><td>109323.80 (+0.45%)</td><td>170.34 <b>(-71.05%)</b></td><td>628.59 (-0.45%)</td><td>627.27 (+0.06%)</td><td>627.41 (-0.00%)</td><td>626.27 (+0.52%)</td><td>0.98 <b>(-71.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110295.90 (n/a)</td><td>109620.18 (n/a)</td><td>109525.70 (n/a)</td><td>108832.80 (n/a)</td><td>588.32 (n/a)</td><td>631.42 (n/a)</td><td>626.90 (n/a)</td><td>627.43 (n/a)</td><td>623.05 (n/a)</td><td>3.37 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.93 (-7.81%)</td><td>6.32 (+0.66%)</td><td>6.52 (+2.89%)</td><td>4.78 (+7.20%)</td><td>0.88 <b>(-22.67%)</b></td><td>1863.20 (-6.72%)</td><td>1436.42 (-1.89%)</td><td>1367.80 (-2.81%)</td><td>1285.90 (+8.47%)</td><td>241.94 <b>(-23.08%)</b></td><td>417.49 (-7.81%)</td><td>380.92 (+0.66%)</td><td>392.51 (+2.89%)</td><td>288.15 (+7.20%)</td><td>53.28 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.52 (n/a)</td><td>6.28 (n/a)</td><td>6.33 (n/a)</td><td>4.46 (n/a)</td><td>1.14 (n/a)</td><td>1997.40 (n/a)</td><td>1464.02 (n/a)</td><td>1407.40 (n/a)</td><td>1185.50 (n/a)</td><td>314.53 (n/a)</td><td>452.86 (n/a)</td><td>378.42 (n/a)</td><td>381.47 (n/a)</td><td>268.78 (n/a)</td><td>68.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.14 (+2.38%)</td><td>6.76 (+5.16%)</td><td>6.80 (+0.72%)</td><td>6.32 <b>(+31.99%)</b></td><td>0.34 <b>(-63.27%)</b></td><td>1410.60 <b>(-24.23%)</b></td><td>1320.26 (-6.65%)</td><td>1310.40 (-0.72%)</td><td>1249.00 (-2.33%)</td><td>67.15 <b>(-73.24%)</b></td><td>429.84 (+2.38%)</td><td>407.47 (+5.16%)</td><td>409.69 (+0.72%)</td><td>380.60 <b>(+31.99%)</b></td><td>20.49 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.97 (n/a)</td><td>6.43 (n/a)</td><td>6.75 (n/a)</td><td>4.79 (n/a)</td><td>0.93 (n/a)</td><td>1861.80 (n/a)</td><td>1414.38 (n/a)</td><td>1319.90 (n/a)</td><td>1278.80 (n/a)</td><td>250.93 (n/a)</td><td>419.84 (n/a)</td><td>387.49 (n/a)</td><td>406.75 (n/a)</td><td>288.36 (n/a)</td><td>55.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.74 (-2.66%)</td><td>6.54 (+2.65%)</td><td>6.58 (-4.57%)</td><td>6.21 <b>(+33.25%)</b></td><td>0.20 <b>(-79.56%)</b></td><td>1434.20 <b>(-24.95%)</b></td><td>1363.20 (-4.77%)</td><td>1354.20 (+4.79%)</td><td>1322.00 (+2.74%)</td><td>42.67 <b>(-84.25%)</b></td><td>406.10 (-2.66%)</td><td>394.14 (+2.65%)</td><td>396.45 (-4.57%)</td><td>374.34 <b>(+33.25%)</b></td><td>12.01 <b>(-79.56%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.93 (n/a)</td><td>6.37 (n/a)</td><td>6.90 (n/a)</td><td>4.66 (n/a)</td><td>0.98 (n/a)</td><td>1911.00 (n/a)</td><td>1431.42 (n/a)</td><td>1292.30 (n/a)</td><td>1286.80 (n/a)</td><td>270.85 (n/a)</td><td>417.22 (n/a)</td><td>383.95 (n/a)</td><td>415.45 (n/a)</td><td>280.94 (n/a)</td><td>58.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.10 (-1.95%)</td><td>7.80 (-0.10%)</td><td>7.89 (-0.80%)</td><td>7.05 (-4.48%)</td><td>0.43 (+14.48%)</td><td>4944.70 (+4.69%)</td><td>4482.34 (+0.17%)</td><td>4417.70 (+0.81%)</td><td>4306.00 (+1.99%)</td><td>263.58 <b>(+22.22%)</b></td><td>498.72 (-1.95%)</td><td>480.34 (-0.10%)</td><td>486.11 (-0.80%)</td><td>434.30 (-4.48%)</td><td>26.39 (+14.48%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>8.26 (n/a)</td><td>7.81 (n/a)</td><td>7.96 (n/a)</td><td>7.38 (n/a)</td><td>0.37 (n/a)</td><td>4723.10 (n/a)</td><td>4474.74 (n/a)</td><td>4382.40 (n/a)</td><td>4222.10 (n/a)</td><td>215.66 (n/a)</td><td>508.63 (n/a)</td><td>480.80 (n/a)</td><td>490.03 (n/a)</td><td>454.68 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.90 (+1.47%)</td><td>7.44 (-2.77%)</td><td>7.64 (-0.13%)</td><td>6.44 (-14.64%)</td><td>0.58 <b>(+516.68%)</b></td><td>5413.90 (+17.15%)</td><td>4708.96 (+3.38%)</td><td>4562.10 (+0.13%)</td><td>4410.90 (-1.45%)</td><td>401.29 <b>(+624.96%)</b></td><td>486.86 (+1.47%)</td><td>458.46 (-2.77%)</td><td>470.72 (-0.13%)</td><td>396.66 (-14.64%)</td><td>35.46 <b>(+516.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.79 (n/a)</td><td>7.66 (n/a)</td><td>7.65 (n/a)</td><td>7.54 (n/a)</td><td>0.09 (n/a)</td><td>4621.30 (n/a)</td><td>4554.82 (n/a)</td><td>4556.30 (n/a)</td><td>4475.80 (n/a)</td><td>55.35 (n/a)</td><td>479.80 (n/a)</td><td>471.53 (n/a)</td><td>471.32 (n/a)</td><td>464.69 (n/a)</td><td>5.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.80 (+0.74%)</td><td>7.25 (-3.93%)</td><td>7.26 (-3.63%)</td><td>6.54 (-11.11%)</td><td>0.46 <b>(+180.92%)</b></td><td>5330.70 (+12.50%)</td><td>4828.10 (+4.40%)</td><td>4802.90 (+3.76%)</td><td>4469.10 (-0.74%)</td><td>317.13 <b>(+216.43%)</b></td><td>480.52 (+0.74%)</td><td>446.28 (-3.93%)</td><td>447.12 (-3.63%)</td><td>402.85 (-11.11%)</td><td>28.33 <b>(+180.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>7.74 (n/a)</td><td>7.54 (n/a)</td><td>7.53 (n/a)</td><td>7.36 (n/a)</td><td>0.16 (n/a)</td><td>4738.50 (n/a)</td><td>4624.48 (n/a)</td><td>4628.70 (n/a)</td><td>4502.20 (n/a)</td><td>100.22 (n/a)</td><td>476.98 (n/a)</td><td>464.55 (n/a)</td><td>463.95 (n/a)</td><td>453.20 (n/a)</td><td>10.09 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (-0.01%)</td><td>0.79 (-0.01%)</td><td>0.79 (-0.02%)</td><td>0.79 (-0.04%)</td><td>0.00 <b>(+21.52%)</b></td><td>95886.70 (+0.04%)</td><td>95793.38 (+0.01%)</td><td>95777.20 (+0.02%)</td><td>95733.90 (+0.01%)</td><td>65.95 <b>(+21.51%)</b></td><td>717.82 (-0.01%)</td><td>717.37 (-0.01%)</td><td>717.49 (-0.02%)</td><td>716.67 (-0.04%)</td><td>0.49 <b>(+21.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95847.90 (n/a)</td><td>95780.60 (n/a)</td><td>95755.40 (n/a)</td><td>95727.30 (n/a)</td><td>54.28 (n/a)</td><td>717.87 (n/a)</td><td>717.47 (n/a)</td><td>717.66 (n/a)</td><td>716.96 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.73 (-0.34%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.00%)</td><td>0.73 (+0.07%)</td><td>0.00 <b>(-92.38%)</b></td><td>102916.40 (-0.07%)</td><td>102901.18 (+0.04%)</td><td>102901.20 (+0.00%)</td><td>102884.20 (+0.34%)</td><td>14.12 <b>(-92.36%)</b></td><td>667.93 (-0.34%)</td><td>667.82 (-0.04%)</td><td>667.82 (-0.00%)</td><td>667.72 (+0.07%)</td><td>0.09 <b>(-92.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102985.90 (n/a)</td><td>102856.98 (n/a)</td><td>102898.80 (n/a)</td><td>102535.00 (n/a)</td><td>184.73 (n/a)</td><td>670.21 (n/a)</td><td>668.11 (n/a)</td><td>667.84 (n/a)</td><td>667.27 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.70 (-0.17%)</td><td>0.70 (-0.04%)</td><td>0.70 (-0.03%)</td><td>0.70 (+0.01%)</td><td>0.00 <b>(-20.68%)</b></td><td>108363.30 (-0.01%)</td><td>108024.18 (+0.04%)</td><td>108011.10 (+0.03%)</td><td>107835.30 (+0.17%)</td><td>209.23 <b>(-20.56%)</b></td><td>637.26 (-0.17%)</td><td>636.15 (-0.04%)</td><td>636.23 (-0.03%)</td><td>634.16 (+0.01%)</td><td>1.23 <b>(-20.69%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108372.70 (n/a)</td><td>107985.48 (n/a)</td><td>107973.90 (n/a)</td><td>107649.20 (n/a)</td><td>263.38 (n/a)</td><td>638.37 (n/a)</td><td>636.38 (n/a)</td><td>636.45 (n/a)</td><td>634.10 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.17 (-2.68%)</td><td>3.73 (+9.71%)</td><td>3.59 (+13.05%)</td><td>3.58 <b>(+22.59%)</b></td><td>0.26 <b>(-55.08%)</b></td><td>2252.50 (-18.43%)</td><td>2170.82 (-10.39%)</td><td>2246.00 (-11.55%)</td><td>1931.50 (+2.75%)</td><td>137.72 <b>(-62.56%)</b></td><td>1094.42 (-2.68%)</td><td>977.18 (+9.71%)</td><td>941.18 (+13.05%)</td><td>938.48 <b>(+22.59%)</b></td><td>67.04 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>4.29 (n/a)</td><td>3.40 (n/a)</td><td>3.17 (n/a)</td><td>2.92 (n/a)</td><td>0.57 (n/a)</td><td>2761.40 (n/a)</td><td>2422.44 (n/a)</td><td>2539.20 (n/a)</td><td>1879.80 (n/a)</td><td>367.80 (n/a)</td><td>1124.53 (n/a)</td><td>890.67 (n/a)</td><td>832.50 (n/a)</td><td>765.52 (n/a)</td><td>149.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.52 <b>(+30.18%)</b></td><td>0.42 <b>(+26.90%)</b></td><td>0.38 (+15.27%)</td><td>0.36 <b>(+23.71%)</b></td><td>0.08 <b>(+86.47%)</b></td><td>3503.10 (-19.17%)</td><td>3026.78 <b>(-20.14%)</b></td><td>3261.20 (-13.25%)</td><td>2408.60 <b>(-23.18%)</b></td><td>513.34 (+17.27%)</td><td>27.86 <b>(+30.18%)</b></td><td>22.73 <b>(+26.90%)</b></td><td>20.58 (+15.27%)</td><td>19.16 <b>(+23.71%)</b></td><td>4.09 <b>(+86.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>4333.90 (n/a)</td><td>3790.00 (n/a)</td><td>3759.20 (n/a)</td><td>3135.40 (n/a)</td><td>437.73 (n/a)</td><td>21.40 (n/a)</td><td>17.91 (n/a)</td><td>17.85 (n/a)</td><td>15.48 (n/a)</td><td>2.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.42 (-2.56%)</td><td>4.93 (+2.35%)</td><td>4.84 (+5.39%)</td><td>3.76 (+3.59%)</td><td>0.95 (-17.73%)</td><td>1769.50 (-3.47%)</td><td>1390.02 (-3.68%)</td><td>1373.40 (-5.12%)</td><td>1036.10 (+2.62%)</td><td>260.28 (-18.93%)</td><td>1983.54 (-2.56%)</td><td>1521.82 (+2.35%)</td><td>1496.39 (+5.39%)</td><td>1161.46 (+3.59%)</td><td>295.03 (-17.73%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.59 (n/a)</td><td>4.81 (n/a)</td><td>4.60 (n/a)</td><td>3.63 (n/a)</td><td>1.16 (n/a)</td><td>1833.10 (n/a)</td><td>1443.16 (n/a)</td><td>1447.50 (n/a)</td><td>1009.60 (n/a)</td><td>321.07 (n/a)</td><td>2035.71 (n/a)</td><td>1486.89 (n/a)</td><td>1419.79 (n/a)</td><td>1121.18 (n/a)</td><td>358.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 <b>(-27.87%)</b></td><td>0.18 (-17.97%)</td><td>0.19 (-5.88%)</td><td>0.15 <b>(-25.87%)</b></td><td>0.03 <b>(-34.42%)</b></td><td>0.21 <b>(-27.87%)</b></td><td>0.18 (-17.97%)</td><td>0.19 (-5.88%)</td><td>0.14 <b>(-25.87%)</b></td><td>0.03 <b>(-34.42%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>13.42 (-1.17%)</td><td>12.76 (-0.29%)</td><td>13.18 (+0.19%)</td><td>11.60 (+1.87%)</td><td>0.76 (-11.85%)</td><td>13.41 (-1.17%)</td><td>12.75 (-0.29%)</td><td>13.17 (+0.19%)</td><td>11.59 (+1.87%)</td><td>0.76 (-11.85%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.58 (n/a)</td><td>12.80 (n/a)</td><td>13.16 (n/a)</td><td>11.38 (n/a)</td><td>0.86 (n/a)</td><td>13.57 (n/a)</td><td>12.79 (n/a)</td><td>13.15 (n/a)</td><td>11.38 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>24.57 (-0.87%)</td><td>24.24 (+0.51%)</td><td>24.22 (-1.47%)</td><td>23.91 (+5.68%)</td><td>0.27 <b>(-70.57%)</b></td><td>24.56 (-0.87%)</td><td>24.22 (+0.51%)</td><td>24.21 (-1.47%)</td><td>23.89 (+5.68%)</td><td>0.27 <b>(-70.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>24.79 (n/a)</td><td>24.11 (n/a)</td><td>24.58 (n/a)</td><td>22.62 (n/a)</td><td>0.90 (n/a)</td><td>24.77 (n/a)</td><td>24.10 (n/a)</td><td>24.57 (n/a)</td><td>22.61 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>40.86 (-0.69%)</td><td>38.71 (-0.31%)</td><td>39.94 (+1.61%)</td><td>32.65 (-5.86%)</td><td>3.43 <b>(+34.97%)</b></td><td>40.83 (-0.69%)</td><td>38.68 (-0.31%)</td><td>39.92 (+1.61%)</td><td>32.63 (-5.86%)</td><td>3.43 <b>(+34.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>41.14 (n/a)</td><td>38.83 (n/a)</td><td>39.31 (n/a)</td><td>34.68 (n/a)</td><td>2.54 (n/a)</td><td>41.12 (n/a)</td><td>38.80 (n/a)</td><td>39.28 (n/a)</td><td>34.66 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>44.24 (+4.17%)</td><td>43.43 (+5.39%)</td><td>43.12 (+3.10%)</td><td>42.69 (+10.94%)</td><td>0.71 <b>(-54.73%)</b></td><td>44.21 (+4.17%)</td><td>43.40 (+5.39%)</td><td>43.10 (+3.10%)</td><td>42.66 (+10.94%)</td><td>0.71 <b>(-54.73%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>42.47 (n/a)</td><td>41.21 (n/a)</td><td>41.83 (n/a)</td><td>38.48 (n/a)</td><td>1.57 (n/a)</td><td>42.44 (n/a)</td><td>41.18 (n/a)</td><td>41.80 (n/a)</td><td>38.45 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>13.35 (+0.71%)</td><td>13.12 (+4.41%)</td><td>13.22 (+0.70%)</td><td>12.54 (+12.40%)</td><td>0.33 <b>(-64.18%)</b></td><td>13.35 (+0.71%)</td><td>13.11 (+4.41%)</td><td>13.22 (+0.70%)</td><td>12.54 (+12.40%)</td><td>0.33 <b>(-64.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.26 (n/a)</td><td>12.57 (n/a)</td><td>13.13 (n/a)</td><td>11.16 (n/a)</td><td>0.91 (n/a)</td><td>13.25 (n/a)</td><td>12.56 (n/a)</td><td>13.12 (n/a)</td><td>11.15 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>24.80 (+0.46%)</td><td>24.15 (-0.29%)</td><td>24.18 (+0.18%)</td><td>23.11 (-2.85%)</td><td>0.68 <b>(+77.87%)</b></td><td>24.78 (+0.46%)</td><td>24.13 (-0.29%)</td><td>24.16 (+0.18%)</td><td>23.10 (-2.85%)</td><td>0.68 <b>(+77.87%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>24.68 (n/a)</td><td>24.22 (n/a)</td><td>24.13 (n/a)</td><td>23.79 (n/a)</td><td>0.38 (n/a)</td><td>24.67 (n/a)</td><td>24.20 (n/a)</td><td>24.12 (n/a)</td><td>23.77 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>40.22 (-6.88%)</td><td>39.27 (-3.64%)</td><td>39.11 (-2.03%)</td><td>38.54 (-1.43%)</td><td>0.77 <b>(-56.72%)</b></td><td>40.20 (-6.88%)</td><td>39.24 (-3.64%)</td><td>39.08 (-2.03%)</td><td>38.52 (-1.43%)</td><td>0.77 <b>(-56.72%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>43.19 (n/a)</td><td>40.75 (n/a)</td><td>39.92 (n/a)</td><td>39.10 (n/a)</td><td>1.78 (n/a)</td><td>43.17 (n/a)</td><td>40.72 (n/a)</td><td>39.90 (n/a)</td><td>39.08 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>45.31 (-0.36%)</td><td>42.94 (-0.96%)</td><td>42.83 (+0.21%)</td><td>40.67 (-1.39%)</td><td>1.79 (-0.99%)</td><td>45.28 (-0.36%)</td><td>42.91 (-0.96%)</td><td>42.80 (+0.21%)</td><td>40.64 (-1.39%)</td><td>1.79 (-0.99%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>45.48 (n/a)</td><td>43.36 (n/a)</td><td>42.74 (n/a)</td><td>41.24 (n/a)</td><td>1.81 (n/a)</td><td>45.45 (n/a)</td><td>43.33 (n/a)</td><td>42.71 (n/a)</td><td>41.22 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.80 (n/a)</td><td>154.54 (n/a)</td><td>156.30 (n/a)</td><td>128.00 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>157.10 (n/a)</td><td>158.00 (n/a)</td><td>116.00 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>156.90 (n/a)</td><td>158.40 (n/a)</td><td>127.50 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>157.74 (n/a)</td><td>131.80 (n/a)</td><td>119.40 (n/a)</td><td>44.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.60 (n/a)</td><td>162.16 (n/a)</td><td>160.50 (n/a)</td><td>127.40 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.50 (n/a)</td><td>178.32 (n/a)</td><td>184.50 (n/a)</td><td>140.30 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.70 (n/a)</td><td>187.04 (n/a)</td><td>179.10 (n/a)</td><td>156.30 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.10 (n/a)</td><td>192.44 (n/a)</td><td>189.10 (n/a)</td><td>170.40 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>170.48 (n/a)</td><td>168.60 (n/a)</td><td>149.10 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>179.62 (n/a)</td><td>186.20 (n/a)</td><td>137.20 (n/a)</td><td>32.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>187.84 (n/a)</td><td>182.70 (n/a)</td><td>156.90 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.20 (n/a)</td><td>183.82 (n/a)</td><td>186.80 (n/a)</td><td>159.40 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>166.00 (n/a)</td><td>170.10 (n/a)</td><td>136.90 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>190.84 (n/a)</td><td>194.60 (n/a)</td><td>156.40 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.70 (n/a)</td><td>191.40 (n/a)</td><td>162.90 (n/a)</td><td>152.30 (n/a)</td><td>63.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>212.04 (n/a)</td><td>221.70 (n/a)</td><td>192.30 (n/a)</td><td>15.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>176.82 (n/a)</td><td>165.20 (n/a)</td><td>133.70 (n/a)</td><td>37.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>273.30 (n/a)</td><td>211.12 (n/a)</td><td>208.30 (n/a)</td><td>151.10 (n/a)</td><td>60.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>265.20 (n/a)</td><td>156.44 (n/a)</td><td>131.80 (n/a)</td><td>120.00 (n/a)</td><td>61.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.60 (n/a)</td><td>167.14 (n/a)</td><td>147.20 (n/a)</td><td>120.60 (n/a)</td><td>51.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>160.88 (n/a)</td><td>172.50 (n/a)</td><td>124.40 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>201.24 (n/a)</td><td>208.10 (n/a)</td><td>151.20 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.60 (n/a)</td><td>197.26 (n/a)</td><td>197.80 (n/a)</td><td>156.40 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>220.98 (n/a)</td><td>242.90 (n/a)</td><td>170.40 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (+11.20%)</td><td>0.16 (-9.68%)</td><td>0.15 (-15.30%)</td><td>0.14 (-15.67%)</td><td>0.03 <b>(+264.09%)</b></td><td>227.40 (+18.56%)</td><td>205.44 (+12.58%)</td><td>214.10 (+18.03%)</td><td>156.80 (-10.09%)</td><td>28.32 <b>(+279.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>182.48 (n/a)</td><td>181.40 (n/a)</td><td>174.40 (n/a)</td><td>7.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>258.10 (n/a)</td><td>201.64 (n/a)</td><td>194.10 (n/a)</td><td>162.60 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>262.80 (n/a)</td><td>181.60 (n/a)</td><td>155.10 (n/a)</td><td>134.40 (n/a)</td><td>54.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>227.10 (n/a)</td><td>169.42 (n/a)</td><td>179.10 (n/a)</td><td>125.50 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.20 (n/a)</td><td>157.66 (n/a)</td><td>162.20 (n/a)</td><td>134.00 (n/a)</td><td>16.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.40 (n/a)</td><td>172.46 (n/a)</td><td>163.70 (n/a)</td><td>140.30 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>225.70 (n/a)</td><td>181.42 (n/a)</td><td>195.80 (n/a)</td><td>122.90 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.30 (n/a)</td><td>208.52 (n/a)</td><td>211.70 (n/a)</td><td>172.50 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-8.59%)</td><td>0.02 (-11.45%)</td><td>0.02 <b>(-21.50%)</b></td><td>0.02 (+16.68%)</td><td>0.00 <b>(-39.38%)</b></td><td>196.30 (-14.28%)</td><td>172.86 (+8.63%)</td><td>182.90 <b>(+27.37%)</b></td><td>130.20 (+9.41%)</td><td>25.59 <b>(-44.12%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.00 (n/a)</td><td>159.12 (n/a)</td><td>143.60 (n/a)</td><td>119.00 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (+10.71%)</td><td>0.03 (-1.68%)</td><td>0.03 (+8.82%)</td><td>0.02 (-16.51%)</td><td>0.01 <b>(+98.99%)</b></td><td>178.00 (+19.78%)</td><td>143.98 (+3.70%)</td><td>134.40 (-8.07%)</td><td>113.00 (-9.60%)</td><td>25.51 <b>(+117.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>148.60 (n/a)</td><td>138.84 (n/a)</td><td>146.20 (n/a)</td><td>125.00 (n/a)</td><td>11.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(-32.89%)</b></td><td>0.02 (-16.46%)</td><td>0.02 (-16.45%)</td><td>0.01 <b>(+27.06%)</b></td><td>0.00 <b>(-60.92%)</b></td><td>318.50 <b>(-21.30%)</b></td><td>236.58 (+7.26%)</td><td>219.10 (+19.73%)</td><td>201.20 <b>(+49.04%)</b></td><td>46.82 <b>(-55.94%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>404.70 (n/a)</td><td>220.56 (n/a)</td><td>183.00 (n/a)</td><td>135.00 (n/a)</td><td>106.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (+9.57%)</td><td>0.02 (-0.31%)</td><td>0.02 (-10.88%)</td><td>0.02 (+5.30%)</td><td>0.01 (+19.46%)</td><td>216.90 (-5.04%)</td><td>185.20 (+1.34%)</td><td>204.60 (+12.23%)</td><td>110.20 (-8.70%)</td><td>43.06 (-0.99%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>182.76 (n/a)</td><td>182.30 (n/a)</td><td>120.70 (n/a)</td><td>43.50 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-13.78%)</td><td>0.02 (-18.56%)</td><td>0.02 <b>(-27.10%)</b></td><td>0.02 (+2.17%)</td><td>0.00 <b>(-44.68%)</b></td><td>192.30 (-2.14%)</td><td>173.22 <b>(+20.24%)</b></td><td>177.40 <b>(+37.20%)</b></td><td>141.60 (+15.97%)</td><td>19.49 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>144.06 (n/a)</td><td>129.30 (n/a)</td><td>122.10 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-10.39%)</td><td>0.03 (-5.93%)</td><td>0.03 (-6.02%)</td><td>0.02 (+6.30%)</td><td>0.00 <b>(-41.07%)</b></td><td>190.50 (-5.93%)</td><td>163.92 (+4.24%)</td><td>157.20 (+6.43%)</td><td>144.10 (+11.62%)</td><td>20.35 <b>(-36.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>157.26 (n/a)</td><td>147.70 (n/a)</td><td>129.10 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(-41.39%)</b></td><td>0.02 <b>(-22.66%)</b></td><td>0.02 (-10.17%)</td><td>0.02 (-5.13%)</td><td>0.00 <b>(-89.63%)</b></td><td>198.40 (+5.42%)</td><td>191.70 <b>(+22.96%)</b></td><td>191.40 (+11.28%)</td><td>181.70 <b>(+70.61%)</b></td><td>6.74 <b>(-81.67%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>155.90 (n/a)</td><td>172.00 (n/a)</td><td>106.50 (n/a)</td><td>36.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-23.11%)</b></td><td>0.02 (-6.90%)</td><td>0.02 (+2.04%)</td><td>0.02 (-4.61%)</td><td>0.00 <b>(-48.48%)</b></td><td>216.00 (+4.80%)</td><td>176.16 (+5.37%)</td><td>168.10 (-2.04%)</td><td>161.60 <b>(+30.11%)</b></td><td>22.70 <b>(-28.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>167.18 (n/a)</td><td>171.60 (n/a)</td><td>124.20 (n/a)</td><td>31.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-12.74%)</td><td>0.02 (-16.48%)</td><td>0.02 (-17.81%)</td><td>0.02 (-7.09%)</td><td>0.00 <b>(-27.87%)</b></td><td>207.40 (+7.63%)</td><td>177.76 (+18.62%)</td><td>183.30 <b>(+21.63%)</b></td><td>141.50 (+14.57%)</td><td>25.58 (-9.75%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>149.86 (n/a)</td><td>150.70 (n/a)</td><td>123.50 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(-31.86%)</b></td><td>0.02 <b>(-26.08%)</b></td><td>0.02 <b>(-23.31%)</b></td><td>0.02 <b>(-22.44%)</b></td><td>0.00 <b>(-50.02%)</b></td><td>215.60 <b>(+28.95%)</b></td><td>189.22 <b>(+34.08%)</b></td><td>191.40 <b>(+30.38%)</b></td><td>169.60 <b>(+46.84%)</b></td><td>19.08 (-5.81%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.20 (n/a)</td><td>141.12 (n/a)</td><td>146.80 (n/a)</td><td>115.50 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-15.94%)</td><td>0.02 (-18.99%)</td><td>0.02 <b>(-22.84%)</b></td><td>0.02 (-14.67%)</td><td>0.00 <b>(-32.48%)</b></td><td>227.50 (+17.21%)</td><td>184.22 <b>(+21.52%)</b></td><td>168.80 <b>(+29.65%)</b></td><td>144.00 (+18.91%)</td><td>34.93 (-4.84%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>151.60 (n/a)</td><td>130.20 (n/a)</td><td>121.10 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(-34.40%)</b></td><td>0.02 <b>(-25.88%)</b></td><td>0.02 <b>(-21.17%)</b></td><td>0.02 <b>(-22.12%)</b></td><td>0.00 <b>(-59.41%)</b></td><td>218.50 <b>(+28.45%)</b></td><td>191.76 <b>(+32.65%)</b></td><td>190.50 <b>(+26.83%)</b></td><td>167.40 <b>(+52.46%)</b></td><td>19.62 <b>(-20.35%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>170.10 (n/a)</td><td>144.56 (n/a)</td><td>150.20 (n/a)</td><td>109.80 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+10.45%)</td><td>0.02 (-6.13%)</td><td>0.02 (-14.93%)</td><td>0.02 (-5.02%)</td><td>0.00 <b>(+34.94%)</b></td><td>218.60 (+5.30%)</td><td>183.14 (+7.41%)</td><td>187.20 (+17.59%)</td><td>140.70 (-9.46%)</td><td>27.87 <b>(+25.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.60 (n/a)</td><td>170.50 (n/a)</td><td>159.20 (n/a)</td><td>155.40 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 <b>(-39.98%)</b></td><td>0.02 <b>(-26.39%)</b></td><td>0.02 <b>(-20.34%)</b></td><td>0.02 <b>(-25.68%)</b></td><td>0.00 <b>(-63.83%)</b></td><td>246.50 <b>(+34.55%)</b></td><td>207.92 <b>(+33.42%)</b></td><td>199.20 <b>(+25.52%)</b></td><td>194.10 <b>(+66.61%)</b></td><td>21.91 (-17.68%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>155.84 (n/a)</td><td>158.70 (n/a)</td><td>116.50 (n/a)</td><td>26.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+15.27%)</td><td>0.02 (+1.72%)</td><td>0.02 (-12.84%)</td><td>0.02 (-4.73%)</td><td>0.01 <b>(+119.30%)</b></td><td>221.10 (+4.99%)</td><td>179.38 (+1.17%)</td><td>198.10 (+14.71%)</td><td>136.20 (-13.25%)</td><td>37.71 <b>(+89.43%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>177.30 (n/a)</td><td>172.70 (n/a)</td><td>157.00 (n/a)</td><td>19.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-11.09%)</td><td>0.02 (-4.80%)</td><td>0.02 (-4.43%)</td><td>0.02 (+7.97%)</td><td>0.00 <b>(-29.63%)</b></td><td>218.10 (-7.39%)</td><td>177.02 (+2.36%)</td><td>177.40 (+4.66%)</td><td>129.60 (+12.50%)</td><td>31.66 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>172.94 (n/a)</td><td>169.50 (n/a)</td><td>115.20 (n/a)</td><td>43.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (-1.77%)</td><td>0.05 (-8.00%)</td><td>0.05 (-19.18%)</td><td>0.04 (+6.52%)</td><td>0.01 <b>(-24.60%)</b></td><td>188.10 (-6.14%)</td><td>166.14 (+6.54%)</td><td>177.80 <b>(+23.73%)</b></td><td>123.60 (+1.73%)</td><td>26.09 <b>(-29.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>155.94 (n/a)</td><td>143.70 (n/a)</td><td>121.50 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 <b>(+22.09%)</b></td><td>0.05 (+8.64%)</td><td>0.06 (+8.29%)</td><td>0.05 (-1.45%)</td><td>0.01 <b>(+94.02%)</b></td><td>180.90 (+1.46%)</td><td>151.60 (-6.86%)</td><td>145.80 (-7.60%)</td><td>122.90 (-18.07%)</td><td>22.13 <b>(+60.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.30 (n/a)</td><td>162.76 (n/a)</td><td>157.80 (n/a)</td><td>150.00 (n/a)</td><td>13.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 <b>(-28.55%)</b></td><td>0.04 (-15.25%)</td><td>0.04 (-13.76%)</td><td>0.03 (-16.72%)</td><td>0.01 <b>(-34.71%)</b></td><td>264.00 <b>(+20.05%)</b></td><td>209.78 (+16.56%)</td><td>210.60 (+15.97%)</td><td>165.00 <b>(+39.95%)</b></td><td>43.17 (+11.06%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>179.98 (n/a)</td><td>181.60 (n/a)</td><td>117.90 (n/a)</td><td>38.87 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-2.36%)</td><td>0.04 (-0.77%)</td><td>0.04 (-3.33%)</td><td>0.04 (+0.92%)</td><td>0.00 <b>(-24.19%)</b></td><td>216.70 (-0.91%)</td><td>196.80 (+0.41%)</td><td>199.00 (+3.43%)</td><td>174.70 (+2.40%)</td><td>15.01 <b>(-24.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>196.00 (n/a)</td><td>192.40 (n/a)</td><td>170.60 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-4.90%)</td><td>0.05 (+13.03%)</td><td>0.05 <b>(+30.39%)</b></td><td>0.04 (+10.79%)</td><td>0.01 (-9.22%)</td><td>207.80 (-9.73%)</td><td>161.38 (-12.38%)</td><td>151.70 <b>(-23.35%)</b></td><td>127.00 (+5.22%)</td><td>36.85 (-12.69%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>184.18 (n/a)</td><td>197.90 (n/a)</td><td>120.70 (n/a)</td><td>42.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-6.73%)</td><td>0.05 (-12.77%)</td><td>0.05 (-1.43%)</td><td>0.03 <b>(-31.55%)</b></td><td>0.01 <b>(+108.38%)</b></td><td>242.60 <b>(+46.14%)</b></td><td>181.96 <b>(+20.15%)</b></td><td>152.10 (+1.47%)</td><td>138.30 (+7.21%)</td><td>49.15 <b>(+232.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.00 (n/a)</td><td>151.44 (n/a)</td><td>149.90 (n/a)</td><td>129.00 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-15.46%)</td><td>0.05 (+1.47%)</td><td>0.05 (+7.54%)</td><td>0.05 <b>(+21.15%)</b></td><td>0.00 <b>(-65.28%)</b></td><td>177.30 (-17.46%)</td><td>163.26 (-4.63%)</td><td>159.00 (-7.02%)</td><td>147.30 (+18.22%)</td><td>12.28 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>171.18 (n/a)</td><td>171.00 (n/a)</td><td>124.60 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (+7.69%)</td><td>0.06 (+12.53%)</td><td>0.06 (+12.63%)</td><td>0.05 <b>(+21.76%)</b></td><td>0.00 <b>(-23.76%)</b></td><td>153.60 (-17.86%)</td><td>138.22 (-11.62%)</td><td>133.70 (-11.22%)</td><td>129.40 (-7.11%)</td><td>10.26 <b>(-43.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.00 (n/a)</td><td>156.40 (n/a)</td><td>150.60 (n/a)</td><td>139.30 (n/a)</td><td>18.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-12.25%)</td><td>0.05 (-12.20%)</td><td>0.05 (-11.20%)</td><td>0.04 (-9.05%)</td><td>0.01 (-14.43%)</td><td>200.30 (+9.93%)</td><td>176.88 (+13.81%)</td><td>169.50 (+12.62%)</td><td>152.30 (+14.00%)</td><td>21.40 (+9.06%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.20 (n/a)</td><td>155.42 (n/a)</td><td>150.50 (n/a)</td><td>133.60 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-12.16%)</td><td>0.05 (-8.48%)</td><td>0.05 (-10.03%)</td><td>0.04 (+4.87%)</td><td>0.00 <b>(-51.14%)</b></td><td>183.40 (-4.63%)</td><td>164.34 (+7.89%)</td><td>165.00 (+11.11%)</td><td>150.10 (+13.80%)</td><td>12.29 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>152.32 (n/a)</td><td>148.50 (n/a)</td><td>131.90 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (+18.57%)</td><td>0.06 (+6.93%)</td><td>0.06 (+4.30%)</td><td>0.05 (-2.37%)</td><td>0.01 <b>(+110.53%)</b></td><td>169.30 (+2.42%)</td><td>143.22 (-5.18%)</td><td>144.80 (-4.17%)</td><td>112.40 (-15.68%)</td><td>21.23 <b>(+80.97%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.30 (n/a)</td><td>151.04 (n/a)</td><td>151.10 (n/a)</td><td>133.30 (n/a)</td><td>11.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 <b>(-23.31%)</b></td><td>0.05 (-13.70%)</td><td>0.05 (-8.35%)</td><td>0.04 (-12.04%)</td><td>0.01 <b>(-36.70%)</b></td><td>214.40 (+13.68%)</td><td>166.22 (+13.99%)</td><td>160.80 (+9.16%)</td><td>134.10 <b>(+30.45%)</b></td><td>31.25 (-4.56%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>145.82 (n/a)</td><td>147.30 (n/a)</td><td>102.80 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-16.33%)</td><td>0.05 (-11.85%)</td><td>0.06 (-5.79%)</td><td>0.04 <b>(-22.32%)</b></td><td>0.01 (+8.74%)</td><td>203.20 <b>(+28.69%)</b></td><td>156.94 (+14.94%)</td><td>146.40 (+6.16%)</td><td>129.20 (+19.52%)</td><td>30.89 <b>(+70.65%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>157.90 (n/a)</td><td>136.54 (n/a)</td><td>137.90 (n/a)</td><td>108.10 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 <b>(-25.58%)</b></td><td>0.04 (-15.01%)</td><td>0.05 (-0.36%)</td><td>0.02 <b>(-43.34%)</b></td><td>0.01 (+8.06%)</td><td>369.90 <b>(+76.48%)</b></td><td>205.02 <b>(+26.63%)</b></td><td>157.30 (+0.38%)</td><td>151.70 <b>(+34.37%)</b></td><td>93.65 <b>(+164.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>161.90 (n/a)</td><td>156.70 (n/a)</td><td>112.90 (n/a)</td><td>35.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-3.83%)</td><td>0.05 (+3.70%)</td><td>0.05 (-6.15%)</td><td>0.05 <b>(+63.72%)</b></td><td>0.00 <b>(-80.11%)</b></td><td>172.20 <b>(-38.94%)</b></td><td>161.38 (-9.22%)</td><td>160.50 (+6.50%)</td><td>154.70 (+3.97%)</td><td>7.23 <b>(-87.61%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.00 (n/a)</td><td>177.78 (n/a)</td><td>150.70 (n/a)</td><td>148.80 (n/a)</td><td>58.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (+2.66%)</td><td>0.05 (-0.53%)</td><td>0.05 (-8.30%)</td><td>0.05 <b>(+32.57%)</b></td><td>0.01 <b>(-33.34%)</b></td><td>181.40 <b>(-24.57%)</b></td><td>159.86 (-2.94%)</td><td>165.10 (+9.05%)</td><td>124.80 (-2.58%)</td><td>22.29 <b>(-51.54%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>164.70 (n/a)</td><td>151.40 (n/a)</td><td>128.10 (n/a)</td><td>46.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (-14.41%)</td><td>0.10 (-10.18%)</td><td>0.10 (-2.46%)</td><td>0.08 (-12.98%)</td><td>0.02 (-19.62%)</td><td>209.40 (+14.93%)</td><td>171.08 (+10.96%)</td><td>169.30 (+2.48%)</td><td>143.00 (+16.83%)</td><td>27.87 (+7.45%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.20 (n/a)</td><td>154.18 (n/a)</td><td>165.20 (n/a)</td><td>122.40 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (+12.49%)</td><td>0.11 (+1.10%)</td><td>0.10 (-3.89%)</td><td>0.07 (-5.52%)</td><td>0.03 <b>(+31.07%)</b></td><td>222.60 (+5.85%)</td><td>160.80 (+1.66%)</td><td>162.80 (+4.03%)</td><td>102.30 (-11.12%)</td><td>47.61 <b>(+23.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.30 (n/a)</td><td>158.18 (n/a)</td><td>156.50 (n/a)</td><td>115.10 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 <b>(-27.26%)</b></td><td>0.08 (-7.56%)</td><td>0.07 (-6.81%)</td><td>0.07 (+11.32%)</td><td>0.01 <b>(-62.33%)</b></td><td>235.60 (-10.18%)</td><td>213.86 (+4.27%)</td><td>223.10 (+7.31%)</td><td>187.50 <b>(+37.56%)</b></td><td>21.84 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>262.30 (n/a)</td><td>205.10 (n/a)</td><td>207.90 (n/a)</td><td>136.30 (n/a)</td><td>45.11 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+9.55%)</td><td>0.09 (+4.13%)</td><td>0.09 (+10.34%)</td><td>0.05 (-19.19%)</td><td>0.03 <b>(+33.09%)</b></td><td>317.50 <b>(+23.73%)</b></td><td>203.10 (+0.30%)</td><td>190.80 (-9.36%)</td><td>125.00 (-8.69%)</td><td>70.05 <b>(+59.30%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>256.60 (n/a)</td><td>202.50 (n/a)</td><td>210.50 (n/a)</td><td>136.90 (n/a)</td><td>43.98 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (+11.95%)</td><td>0.11 (+4.48%)</td><td>0.12 (+10.97%)</td><td>0.08 (-2.05%)</td><td>0.03 <b>(+53.16%)</b></td><td>210.50 (+2.09%)</td><td>162.86 (-1.61%)</td><td>142.30 (-9.88%)</td><td>118.20 (-10.66%)</td><td>41.40 <b>(+45.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>165.52 (n/a)</td><td>157.90 (n/a)</td><td>132.30 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (+6.34%)</td><td>0.11 (-4.47%)</td><td>0.11 (-11.67%)</td><td>0.10 (-0.74%)</td><td>0.02 (+5.61%)</td><td>169.10 (+0.77%)</td><td>147.32 (+4.76%)</td><td>146.30 (+13.24%)</td><td>115.50 (-5.94%)</td><td>20.59 (-1.01%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>167.80 (n/a)</td><td>140.62 (n/a)</td><td>129.20 (n/a)</td><td>122.80 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+3.05%)</td><td>0.11 (+9.14%)</td><td>0.11 (+4.50%)</td><td>0.09 (+13.11%)</td><td>0.01 <b>(-29.73%)</b></td><td>186.20 (-11.59%)</td><td>151.68 (-10.25%)</td><td>146.60 (-4.31%)</td><td>127.30 (-2.97%)</td><td>21.47 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>169.00 (n/a)</td><td>153.20 (n/a)</td><td>131.20 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (-6.67%)</td><td>0.11 (+4.45%)</td><td>0.12 (+9.64%)</td><td>0.10 (+14.33%)</td><td>0.01 <b>(-47.42%)</b></td><td>169.10 (-12.52%)</td><td>144.14 (-6.27%)</td><td>136.20 (-8.77%)</td><td>133.30 (+7.15%)</td><td>14.91 <b>(-49.78%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.30 (n/a)</td><td>153.78 (n/a)</td><td>149.30 (n/a)</td><td>124.40 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (-17.85%)</td><td>0.09 (-14.07%)</td><td>0.09 (-17.03%)</td><td>0.06 (-17.96%)</td><td>0.02 (-17.67%)</td><td>261.30 <b>(+21.88%)</b></td><td>188.70 (+16.44%)</td><td>178.50 <b>(+20.53%)</b></td><td>155.10 <b>(+21.74%)</b></td><td>42.49 <b>(+23.59%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>162.06 (n/a)</td><td>148.10 (n/a)</td><td>127.40 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (+10.10%)</td><td>0.10 (-3.39%)</td><td>0.09 (-13.78%)</td><td>0.08 (-4.01%)</td><td>0.02 <b>(+33.85%)</b></td><td>194.70 (+4.17%)</td><td>166.30 (+4.75%)</td><td>176.40 (+15.98%)</td><td>117.20 (-9.15%)</td><td>30.15 <b>(+20.00%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>158.76 (n/a)</td><td>152.10 (n/a)</td><td>129.00 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+4.44%)</td><td>0.11 (+11.09%)</td><td>0.12 (+18.95%)</td><td>0.08 (+5.82%)</td><td>0.02 <b>(+28.65%)</b></td><td>200.20 (-5.48%)</td><td>154.60 (-8.91%)</td><td>135.70 (-15.92%)</td><td>127.00 (-4.22%)</td><td>34.38 (+13.90%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>169.72 (n/a)</td><td>161.40 (n/a)</td><td>132.60 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+17.84%)</td><td>0.10 (+9.48%)</td><td>0.09 (+3.79%)</td><td>0.08 (-2.18%)</td><td>0.02 <b>(+83.50%)</b></td><td>206.90 (+2.22%)</td><td>167.98 (-6.78%)</td><td>178.60 (-3.67%)</td><td>125.80 (-15.11%)</td><td>32.09 <b>(+60.69%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>180.20 (n/a)</td><td>185.40 (n/a)</td><td>148.20 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (-18.42%)</td><td>0.08 (-6.26%)</td><td>0.08 (-3.81%)</td><td>0.07 (+6.43%)</td><td>0.01 <b>(-48.98%)</b></td><td>232.00 (-6.03%)</td><td>203.14 (+4.16%)</td><td>207.80 (+4.00%)</td><td>170.40 <b>(+22.59%)</b></td><td>23.25 <b>(-40.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.90 (n/a)</td><td>195.02 (n/a)</td><td>199.80 (n/a)</td><td>139.00 (n/a)</td><td>38.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 <b>(+25.01%)</b></td><td>0.10 (+2.60%)</td><td>0.10 (-3.79%)</td><td>0.07 (-11.68%)</td><td>0.04 <b>(+70.87%)</b></td><td>230.80 (+13.25%)</td><td>172.18 (+2.18%)</td><td>167.50 (+3.97%)</td><td>99.40 (-19.97%)</td><td>49.47 <b>(+44.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>168.50 (n/a)</td><td>161.10 (n/a)</td><td>124.20 (n/a)</td><td>34.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (+0.35%)</td><td>0.08 (-6.97%)</td><td>0.07 (-15.70%)</td><td>0.07 <b>(+25.30%)</b></td><td>0.01 <b>(-20.24%)</b></td><td>227.80 <b>(-20.18%)</b></td><td>207.80 (+5.07%)</td><td>219.90 (+18.61%)</td><td>153.30 (-0.33%)</td><td>30.84 <b>(-40.16%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>285.40 (n/a)</td><td>197.78 (n/a)</td><td>185.40 (n/a)</td><td>153.80 (n/a)</td><td>51.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+11.91%)</td><td>0.11 (+7.69%)</td><td>0.10 (+4.06%)</td><td>0.08 (+7.80%)</td><td>0.02 (-1.24%)</td><td>205.00 (-7.24%)</td><td>158.94 (-7.81%)</td><td>157.10 (-3.91%)</td><td>121.60 (-10.65%)</td><td>32.34 (-16.75%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.00 (n/a)</td><td>172.40 (n/a)</td><td>163.50 (n/a)</td><td>136.10 (n/a)</td><td>38.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 <b>(+52.08%)</b></td><td>0.22 <b>(+30.31%)</b></td><td>0.19 (+19.00%)</td><td>0.18 <b>(+26.59%)</b></td><td>0.05 <b>(+148.78%)</b></td><td>178.80 <b>(-20.99%)</b></td><td>156.42 <b>(-21.50%)</b></td><td>171.10 (-15.96%)</td><td>108.80 <b>(-34.26%)</b></td><td>28.37 <b>(+29.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>226.30 (n/a)</td><td>199.26 (n/a)</td><td>203.60 (n/a)</td><td>165.50 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (+14.94%)</td><td>0.19 (+9.05%)</td><td>0.17 (-1.61%)</td><td>0.15 (+4.66%)</td><td>0.04 <b>(+52.32%)</b></td><td>217.50 (-4.44%)</td><td>177.82 (-6.74%)</td><td>192.60 (+1.64%)</td><td>130.80 (-13.03%)</td><td>35.48 <b>(+27.45%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>227.60 (n/a)</td><td>190.68 (n/a)</td><td>189.50 (n/a)</td><td>150.40 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (-0.54%)</td><td>0.14 (-13.50%)</td><td>0.14 <b>(-22.25%)</b></td><td>0.12 (+19.39%)</td><td>0.03 <b>(-26.79%)</b></td><td>284.40 (-16.23%)</td><td>235.04 (+11.29%)</td><td>232.70 <b>(+28.63%)</b></td><td>171.30 (+0.53%)</td><td>41.73 <b>(-42.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>339.50 (n/a)</td><td>211.20 (n/a)</td><td>180.90 (n/a)</td><td>170.40 (n/a)</td><td>72.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (-19.59%)</td><td>0.17 (-13.84%)</td><td>0.15 <b>(-20.78%)</b></td><td>0.13 (-5.80%)</td><td>0.04 <b>(-22.46%)</b></td><td>252.60 (+6.18%)</td><td>197.64 (+14.87%)</td><td>214.00 <b>(+26.18%)</b></td><td>145.40 <b>(+24.38%)</b></td><td>44.29 (+0.36%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>237.90 (n/a)</td><td>172.06 (n/a)</td><td>169.60 (n/a)</td><td>116.90 (n/a)</td><td>44.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 <b>(+24.62%)</b></td><td>0.19 (+6.71%)</td><td>0.18 (+3.70%)</td><td>0.08 <b>(-39.52%)</b></td><td>0.07 <b>(+158.85%)</b></td><td>391.10 <b>(+65.37%)</b></td><td>203.42 (+8.87%)</td><td>181.50 (-3.56%)</td><td>121.30 (-19.78%)</td><td>109.51 <b>(+245.27%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.50 (n/a)</td><td>186.84 (n/a)</td><td>188.20 (n/a)</td><td>151.20 (n/a)</td><td>31.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (-19.31%)</td><td>0.18 (-10.65%)</td><td>0.17 (-8.60%)</td><td>0.16 (-5.42%)</td><td>0.03 <b>(-35.16%)</b></td><td>210.40 (+5.73%)</td><td>182.34 (+10.27%)</td><td>190.50 (+9.42%)</td><td>150.50 <b>(+23.97%)</b></td><td>27.11 (-15.74%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.00 (n/a)</td><td>165.36 (n/a)</td><td>174.10 (n/a)</td><td>121.40 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (-16.81%)</td><td>0.19 (-10.71%)</td><td>0.17 (-10.30%)</td><td>0.15 (-6.68%)</td><td>0.04 <b>(-22.58%)</b></td><td>215.30 (+7.11%)</td><td>181.80 (+11.22%)</td><td>190.70 (+11.46%)</td><td>138.30 <b>(+20.16%)</b></td><td>32.94 (+3.33%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>201.00 (n/a)</td><td>163.46 (n/a)</td><td>171.10 (n/a)</td><td>115.10 (n/a)</td><td>31.88 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (+3.39%)</td><td>0.21 (+5.20%)</td><td>0.20 (-3.26%)</td><td>0.15 <b>(+73.05%)</b></td><td>0.05 <b>(-29.42%)</b></td><td>213.30 <b>(-42.23%)</b></td><td>163.08 (-15.20%)</td><td>163.50 (+3.42%)</td><td>112.10 (-3.20%)</td><td>36.07 <b>(-64.49%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>369.20 (n/a)</td><td>192.32 (n/a)</td><td>158.10 (n/a)</td><td>115.80 (n/a)</td><td>101.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 <b>(+38.88%)</b></td><td>0.22 (+16.48%)</td><td>0.20 (+7.72%)</td><td>0.15 (+1.39%)</td><td>0.06 <b>(+130.07%)</b></td><td>211.80 (-1.35%)</td><td>160.06 (-9.73%)</td><td>163.40 (-7.16%)</td><td>109.10 <b>(-27.99%)</b></td><td>45.35 <b>(+66.53%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>214.70 (n/a)</td><td>177.32 (n/a)</td><td>176.00 (n/a)</td><td>151.50 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (-18.73%)</td><td>0.19 <b>(-21.79%)</b></td><td>0.20 (-19.25%)</td><td>0.15 <b>(-28.71%)</b></td><td>0.03 <b>(+21.93%)</b></td><td>217.00 <b>(+40.27%)</b></td><td>175.86 <b>(+30.02%)</b></td><td>165.80 <b>(+23.92%)</b></td><td>145.40 <b>(+23.01%)</b></td><td>33.11 <b>(+108.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>154.70 (n/a)</td><td>135.26 (n/a)</td><td>133.80 (n/a)</td><td>118.20 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (-18.98%)</td><td>0.19 (-7.33%)</td><td>0.19 (-6.93%)</td><td>0.16 (-6.13%)</td><td>0.03 <b>(-40.04%)</b></td><td>210.80 (+6.57%)</td><td>172.22 (+5.89%)</td><td>172.40 (+7.48%)</td><td>147.00 <b>(+23.43%)</b></td><td>25.44 <b>(-23.28%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>197.80 (n/a)</td><td>162.64 (n/a)</td><td>160.40 (n/a)</td><td>119.10 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 <b>(-29.16%)</b></td><td>0.17 (-11.64%)</td><td>0.17 (-4.17%)</td><td>0.14 (-10.85%)</td><td>0.03 <b>(-50.42%)</b></td><td>241.10 (+12.14%)</td><td>195.82 (+9.57%)</td><td>194.10 (+4.35%)</td><td>155.50 <b>(+41.11%)</b></td><td>33.33 (-16.97%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>215.00 (n/a)</td><td>178.72 (n/a)</td><td>186.00 (n/a)</td><td>110.20 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (-9.01%)</td><td>0.16 <b>(-20.19%)</b></td><td>0.16 (-12.56%)</td><td>0.11 <b>(-37.68%)</b></td><td>0.05 <b>(+52.43%)</b></td><td>307.10 <b>(+60.45%)</b></td><td>225.40 <b>(+31.98%)</b></td><td>204.70 (+14.36%)</td><td>146.60 (+9.90%)</td><td>64.93 <b>(+177.01%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.40 (n/a)</td><td>170.78 (n/a)</td><td>179.00 (n/a)</td><td>133.40 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (+18.60%)</td><td>0.22 (+5.54%)</td><td>0.21 (+3.77%)</td><td>0.16 (-4.91%)</td><td>0.05 <b>(+98.71%)</b></td><td>204.70 (+5.19%)</td><td>158.66 (-2.35%)</td><td>152.80 (-3.60%)</td><td>121.30 (-15.71%)</td><td>36.73 <b>(+76.30%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.60 (n/a)</td><td>162.48 (n/a)</td><td>158.50 (n/a)</td><td>143.90 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (-3.24%)</td><td>0.19 (-1.15%)</td><td>0.19 (-6.45%)</td><td>0.14 (+7.78%)</td><td>0.04 <b>(-22.99%)</b></td><td>237.00 (-7.24%)</td><td>177.32 (-1.42%)</td><td>169.90 (+6.92%)</td><td>132.50 (+3.35%)</td><td>37.90 <b>(-26.20%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>255.50 (n/a)</td><td>179.88 (n/a)</td><td>158.90 (n/a)</td><td>128.20 (n/a)</td><td>51.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 <b>(-25.46%)</b></td><td>0.20 <b>(-20.26%)</b></td><td>0.19 <b>(-28.68%)</b></td><td>0.18 (-11.72%)</td><td>0.02 <b>(-51.50%)</b></td><td>186.90 (+13.27%)</td><td>165.54 <b>(+23.11%)</b></td><td>172.00 <b>(+40.29%)</b></td><td>142.20 <b>(+34.15%)</b></td><td>18.18 <b>(-28.86%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>165.00 (n/a)</td><td>134.46 (n/a)</td><td>122.60 (n/a)</td><td>106.00 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+4.58%)</td><td>0.02 (-8.22%)</td><td>0.02 (-16.62%)</td><td>0.02 (-0.72%)</td><td>0.00 (+17.08%)</td><td>182.80 (+0.72%)</td><td>169.08 (+9.28%)</td><td>173.50 (+19.90%)</td><td>134.10 (-4.35%)</td><td>20.10 (+11.87%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>154.72 (n/a)</td><td>144.70 (n/a)</td><td>140.20 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (+6.81%)</td><td>0.03 (-0.05%)</td><td>0.04 (-12.71%)</td><td>0.03 <b>(+37.74%)</b></td><td>0.01 <b>(-27.58%)</b></td><td>211.40 <b>(-27.38%)</b></td><td>180.78 (-4.41%)</td><td>174.50 (+14.58%)</td><td>134.20 (-6.35%)</td><td>31.99 <b>(-49.22%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>291.10 (n/a)</td><td>189.12 (n/a)</td><td>152.30 (n/a)</td><td>143.30 (n/a)</td><td>62.99 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (+4.01%)</td><td>0.03 (+7.60%)</td><td>0.02 (-11.99%)</td><td>0.02 <b>(+57.43%)</b></td><td>0.00 <b>(-39.12%)</b></td><td>196.50 <b>(-36.47%)</b></td><td>162.96 (-12.87%)</td><td>169.80 (+13.58%)</td><td>137.30 (-3.85%)</td><td>24.95 <b>(-64.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>309.30 (n/a)</td><td>187.04 (n/a)</td><td>149.50 (n/a)</td><td>142.80 (n/a)</td><td>70.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-24.02%)</b></td><td>0.03 (-19.54%)</td><td>0.03 <b>(-23.63%)</b></td><td>0.03 (-5.53%)</td><td>0.00 <b>(-60.49%)</b></td><td>197.80 (+5.89%)</td><td>182.78 <b>(+22.34%)</b></td><td>185.50 <b>(+30.91%)</b></td><td>162.10 <b>(+31.57%)</b></td><td>13.08 <b>(-46.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.80 (n/a)</td><td>149.40 (n/a)</td><td>141.70 (n/a)</td><td>123.20 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-7.09%)</td><td>0.02 (+5.55%)</td><td>0.02 <b>(+20.58%)</b></td><td>0.02 <b>(+36.34%)</b></td><td>0.00 <b>(-46.17%)</b></td><td>223.60 <b>(-26.66%)</b></td><td>184.28 (-10.96%)</td><td>173.80 (-17.04%)</td><td>149.30 (+7.64%)</td><td>30.01 <b>(-55.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>304.90 (n/a)</td><td>206.96 (n/a)</td><td>209.50 (n/a)</td><td>138.70 (n/a)</td><td>67.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-25.98%)</b></td><td>0.03 <b>(-29.46%)</b></td><td>0.02 <b>(-31.16%)</b></td><td>0.02 <b>(-26.12%)</b></td><td>0.00 <b>(-32.69%)</b></td><td>227.30 <b>(+35.38%)</b></td><td>204.84 <b>(+41.44%)</b></td><td>211.70 <b>(+45.30%)</b></td><td>168.70 <b>(+35.07%)</b></td><td>24.85 <b>(+26.46%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>167.90 (n/a)</td><td>144.82 (n/a)</td><td>145.70 (n/a)</td><td>124.90 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-27.24%)</b></td><td>0.02 <b>(-22.10%)</b></td><td>0.02 (-16.69%)</td><td>0.02 (-19.91%)</td><td>0.00 <b>(-50.97%)</b></td><td>207.30 <b>(+24.80%)</b></td><td>173.74 <b>(+25.79%)</b></td><td>176.60 <b>(+20.05%)</b></td><td>143.90 <b>(+37.44%)</b></td><td>23.29 (-15.77%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>166.10 (n/a)</td><td>138.12 (n/a)</td><td>147.10 (n/a)</td><td>104.70 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-18.00%)</td><td>0.02 <b>(-20.01%)</b></td><td>0.03 (-16.58%)</td><td>0.02 <b>(-29.85%)</b></td><td>0.00 <b>(+23.00%)</b></td><td>235.50 <b>(+42.55%)</b></td><td>190.98 <b>(+26.48%)</b></td><td>182.30 (+19.93%)</td><td>157.70 <b>(+21.96%)</b></td><td>29.48 <b>(+119.73%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>165.20 (n/a)</td><td>151.00 (n/a)</td><td>152.00 (n/a)</td><td>129.30 (n/a)</td><td>13.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(-26.21%)</b></td><td>0.02 (-9.34%)</td><td>0.02 (-11.44%)</td><td>0.02 <b>(+36.48%)</b></td><td>0.00 <b>(-72.41%)</b></td><td>188.30 <b>(-26.73%)</b></td><td>168.56 (+2.59%)</td><td>170.40 (+12.92%)</td><td>147.80 <b>(+35.60%)</b></td><td>14.57 <b>(-73.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.00 (n/a)</td><td>164.30 (n/a)</td><td>150.90 (n/a)</td><td>109.00 (n/a)</td><td>55.83 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (+11.96%)</td><td>0.03 (-11.14%)</td><td>0.02 <b>(-21.64%)</b></td><td>0.02 <b>(-20.72%)</b></td><td>0.01 <b>(+120.76%)</b></td><td>220.00 <b>(+26.15%)</b></td><td>175.76 (+17.47%)</td><td>184.70 <b>(+27.64%)</b></td><td>116.70 (-10.71%)</td><td>42.03 <b>(+146.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>149.62 (n/a)</td><td>144.70 (n/a)</td><td>130.70 (n/a)</td><td>17.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (+8.22%)</td><td>0.02 (+1.12%)</td><td>0.02 (-15.33%)</td><td>0.01 (-17.45%)</td><td>0.01 (+17.41%)</td><td>323.60 <b>(+21.15%)</b></td><td>195.40 (+2.36%)</td><td>189.50 (+18.14%)</td><td>115.80 (-7.58%)</td><td>78.44 <b>(+29.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>267.10 (n/a)</td><td>190.90 (n/a)</td><td>160.40 (n/a)</td><td>125.30 (n/a)</td><td>60.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-9.57%)</td><td>0.02 (-15.81%)</td><td>0.02 <b>(-21.56%)</b></td><td>0.02 (-12.11%)</td><td>0.00 (-1.29%)</td><td>231.90 (+13.79%)</td><td>206.66 (+19.06%)</td><td>210.10 <b>(+27.49%)</b></td><td>166.60 (+10.62%)</td><td>25.91 <b>(+22.29%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>173.58 (n/a)</td><td>164.80 (n/a)</td><td>150.60 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 <b>(+28.14%)</b></td><td>0.03 (+8.21%)</td><td>0.03 (+11.42%)</td><td>0.01 <b>(-32.02%)</b></td><td>0.01 <b>(+264.75%)</b></td><td>291.80 <b>(+47.08%)</b></td><td>178.62 (+2.54%)</td><td>151.50 (-10.25%)</td><td>118.80 <b>(-21.94%)</b></td><td>72.11 <b>(+309.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>174.20 (n/a)</td><td>168.80 (n/a)</td><td>152.20 (n/a)</td><td>17.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (-5.33%)</td><td>0.02 (-13.69%)</td><td>0.02 (-18.95%)</td><td>0.01 (+9.74%)</td><td>0.00 <b>(-24.03%)</b></td><td>319.30 (-8.88%)</td><td>231.08 (+11.11%)</td><td>222.40 <b>(+23.35%)</b></td><td>159.40 (+5.63%)</td><td>57.65 <b>(-29.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>350.40 (n/a)</td><td>207.98 (n/a)</td><td>180.30 (n/a)</td><td>150.90 (n/a)</td><td>81.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (+7.95%)</td><td>0.02 (-0.47%)</td><td>0.02 (+8.76%)</td><td>0.01 <b>(-23.95%)</b></td><td>0.00 <b>(+57.65%)</b></td><td>373.10 <b>(+31.47%)</b></td><td>243.40 (+4.88%)</td><td>212.20 (-8.02%)</td><td>177.00 (-7.38%)</td><td>76.24 <b>(+103.38%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>283.80 (n/a)</td><td>232.08 (n/a)</td><td>230.70 (n/a)</td><td>191.10 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-7.78%)</td><td>0.05 (-10.64%)</td><td>0.05 (-7.98%)</td><td>0.04 <b>(-22.03%)</b></td><td>0.01 <b>(+35.45%)</b></td><td>230.00 <b>(+28.28%)</b></td><td>173.58 (+15.11%)</td><td>166.20 (+8.70%)</td><td>128.30 (+8.45%)</td><td>41.90 <b>(+92.94%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.30 (n/a)</td><td>150.80 (n/a)</td><td>152.90 (n/a)</td><td>118.30 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (-14.59%)</td><td>0.08 (-16.66%)</td><td>0.07 <b>(-20.36%)</b></td><td>0.06 (-3.18%)</td><td>0.01 <b>(-30.79%)</b></td><td>192.30 (+3.28%)</td><td>160.20 (+18.23%)</td><td>166.10 <b>(+25.55%)</b></td><td>129.10 (+17.15%)</td><td>25.20 (-17.55%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.20 (n/a)</td><td>135.50 (n/a)</td><td>132.30 (n/a)</td><td>110.20 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-9.55%)</td><td>0.05 (-12.51%)</td><td>0.05 (-16.96%)</td><td>0.04 (-9.88%)</td><td>0.01 (-10.29%)</td><td>225.90 (+10.95%)</td><td>165.50 (+14.14%)</td><td>159.70 <b>(+20.44%)</b></td><td>127.00 (+10.53%)</td><td>37.04 (+8.12%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>145.00 (n/a)</td><td>132.60 (n/a)</td><td>114.90 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (-17.65%)</td><td>0.06 (-13.70%)</td><td>0.06 <b>(-22.11%)</b></td><td>0.05 (+2.99%)</td><td>0.01 <b>(-56.66%)</b></td><td>197.20 (-2.90%)</td><td>169.94 (+12.33%)</td><td>166.10 <b>(+28.36%)</b></td><td>149.40 <b>(+21.46%)</b></td><td>18.57 <b>(-47.85%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>151.28 (n/a)</td><td>129.40 (n/a)</td><td>123.00 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-15.55%)</td><td>0.04 (-4.94%)</td><td>0.05 (-3.12%)</td><td>0.03 (+9.13%)</td><td>0.01 <b>(-26.05%)</b></td><td>295.70 (-8.37%)</td><td>198.06 (+0.87%)</td><td>178.30 (+3.24%)</td><td>139.70 (+18.39%)</td><td>61.51 <b>(-20.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>322.70 (n/a)</td><td>196.36 (n/a)</td><td>172.70 (n/a)</td><td>118.00 (n/a)</td><td>77.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (-14.39%)</td><td>0.06 (-13.96%)</td><td>0.05 <b>(-21.38%)</b></td><td>0.05 (-15.81%)</td><td>0.01 (-0.93%)</td><td>203.90 (+18.75%)</td><td>171.90 (+17.48%)</td><td>192.10 <b>(+27.22%)</b></td><td>126.40 (+16.82%)</td><td>37.05 <b>(+36.29%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>146.32 (n/a)</td><td>151.00 (n/a)</td><td>108.20 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 <b>(-31.29%)</b></td><td>0.04 (-18.72%)</td><td>0.05 (-10.99%)</td><td>0.04 (-16.63%)</td><td>0.01 <b>(-49.96%)</b></td><td>211.60 (+19.95%)</td><td>184.24 <b>(+21.34%)</b></td><td>176.70 (+12.33%)</td><td>163.40 <b>(+45.50%)</b></td><td>22.26 (-11.00%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>151.84 (n/a)</td><td>157.30 (n/a)</td><td>112.30 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (+10.35%)</td><td>0.05 (-13.54%)</td><td>0.05 (-16.23%)</td><td>0.04 <b>(-28.92%)</b></td><td>0.02 <b>(+106.99%)</b></td><td>239.70 <b>(+40.67%)</b></td><td>188.96 <b>(+21.91%)</b></td><td>195.80 (+19.39%)</td><td>112.80 (-9.40%)</td><td>47.09 <b>(+150.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>155.00 (n/a)</td><td>164.00 (n/a)</td><td>124.50 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-10.15%)</td><td>0.05 (-7.71%)</td><td>0.05 (-3.51%)</td><td>0.03 (+0.16%)</td><td>0.01 (-14.34%)</td><td>294.50 (-0.17%)</td><td>195.70 (+6.61%)</td><td>173.80 (+3.64%)</td><td>132.30 (+11.27%)</td><td>62.27 (-6.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.00 (n/a)</td><td>183.56 (n/a)</td><td>167.70 (n/a)</td><td>118.90 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 <b>(+63.05%)</b></td><td>0.05 (+4.53%)</td><td>0.05 (-19.63%)</td><td>0.04 <b>(+22.73%)</b></td><td>0.02 <b>(+113.52%)</b></td><td>224.60 (-18.51%)</td><td>185.02 (+0.52%)</td><td>201.00 <b>(+24.38%)</b></td><td>96.10 <b>(-38.63%)</b></td><td>50.92 (-1.05%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.60 (n/a)</td><td>184.06 (n/a)</td><td>161.60 (n/a)</td><td>156.60 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (-19.12%)</td><td>0.04 (-19.81%)</td><td>0.04 (-14.58%)</td><td>0.04 <b>(-26.43%)</b></td><td>0.01 (+9.88%)</td><td>233.90 <b>(+35.91%)</b></td><td>198.06 <b>(+25.62%)</b></td><td>192.10 (+17.06%)</td><td>169.40 <b>(+23.65%)</b></td><td>27.10 <b>(+84.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>157.66 (n/a)</td><td>164.10 (n/a)</td><td>137.00 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-16.41%)</td><td>0.05 (-12.72%)</td><td>0.04 <b>(-22.94%)</b></td><td>0.04 <b>(+35.21%)</b></td><td>0.01 <b>(-46.07%)</b></td><td>216.80 <b>(-26.06%)</b></td><td>196.80 (+7.91%)</td><td>208.30 <b>(+29.78%)</b></td><td>147.70 (+19.69%)</td><td>28.53 <b>(-55.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.20 (n/a)</td><td>182.38 (n/a)</td><td>160.50 (n/a)</td><td>123.40 (n/a)</td><td>64.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (-16.75%)</td><td>0.04 <b>(-22.48%)</b></td><td>0.04 (-19.79%)</td><td>0.03 <b>(-40.39%)</b></td><td>0.01 <b>(+30.29%)</b></td><td>293.70 <b>(+67.73%)</b></td><td>212.46 <b>(+34.04%)</b></td><td>201.50 <b>(+24.69%)</b></td><td>148.10 <b>(+20.11%)</b></td><td>55.99 <b>(+168.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>158.50 (n/a)</td><td>161.60 (n/a)</td><td>123.30 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 <b>(-31.84%)</b></td><td>0.04 <b>(-26.63%)</b></td><td>0.04 <b>(-26.13%)</b></td><td>0.03 (-11.33%)</td><td>0.01 <b>(-46.64%)</b></td><td>332.80 (+12.78%)</td><td>242.16 <b>(+31.27%)</b></td><td>214.30 <b>(+35.38%)</b></td><td>202.10 <b>(+46.66%)</b></td><td>53.40 (-15.45%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.10 (n/a)</td><td>184.48 (n/a)</td><td>158.30 (n/a)</td><td>137.80 (n/a)</td><td>63.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (-5.98%)</td><td>0.03 (-7.97%)</td><td>0.04 (+2.29%)</td><td>0.02 (-15.49%)</td><td>0.01 (+13.95%)</td><td>357.00 (+18.33%)</td><td>263.20 (+11.97%)</td><td>216.30 (-2.26%)</td><td>190.80 (+6.35%)</td><td>83.19 <b>(+47.85%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.70 (n/a)</td><td>235.06 (n/a)</td><td>221.30 (n/a)</td><td>179.40 (n/a)</td><td>56.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (+5.06%)</td><td>0.10 (-8.49%)</td><td>0.10 (-9.42%)</td><td>0.07 <b>(-23.29%)</b></td><td>0.02 <b>(+88.97%)</b></td><td>240.50 <b>(+30.35%)</b></td><td>178.44 (+12.28%)</td><td>166.90 (+10.38%)</td><td>137.80 (-4.77%)</td><td>39.20 <b>(+138.83%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>158.92 (n/a)</td><td>151.20 (n/a)</td><td>144.70 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 <b>(-28.11%)</b></td><td>0.12 (-14.77%)</td><td>0.12 (-15.94%)</td><td>0.10 (+14.45%)</td><td>0.02 <b>(-52.11%)</b></td><td>247.00 (-12.63%)</td><td>207.72 (+11.69%)</td><td>198.20 (+18.97%)</td><td>176.00 <b>(+39.13%)</b></td><td>32.88 <b>(-43.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>282.70 (n/a)</td><td>185.98 (n/a)</td><td>166.60 (n/a)</td><td>126.50 (n/a)</td><td>58.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 <b>(+29.05%)</b></td><td>0.12 (+14.58%)</td><td>0.11 (-0.03%)</td><td>0.10 <b>(+39.62%)</b></td><td>0.03 <b>(+25.26%)</b></td><td>161.40 <b>(-28.36%)</b></td><td>139.00 (-13.11%)</td><td>149.50 (+0.00%)</td><td>101.10 <b>(-22.47%)</b></td><td>26.67 <b>(-30.47%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.30 (n/a)</td><td>159.98 (n/a)</td><td>149.50 (n/a)</td><td>130.40 (n/a)</td><td>38.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 <b>(-24.96%)</b></td><td>0.10 <b>(-25.97%)</b></td><td>0.11 (-17.64%)</td><td>0.08 <b>(-25.54%)</b></td><td>0.02 <b>(-24.12%)</b></td><td>248.70 <b>(+34.29%)</b></td><td>200.84 <b>(+35.37%)</b></td><td>181.00 <b>(+21.48%)</b></td><td>159.50 <b>(+33.25%)</b></td><td>38.64 <b>(+41.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>185.20 (n/a)</td><td>148.36 (n/a)</td><td>149.00 (n/a)</td><td>119.70 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+7.56%)</td><td>0.11 (+6.14%)</td><td>0.11 (+4.63%)</td><td>0.09 (+14.92%)</td><td>0.02 (-5.66%)</td><td>191.00 (-12.98%)</td><td>153.80 (-6.49%)</td><td>148.00 (-4.39%)</td><td>128.90 (-7.00%)</td><td>24.14 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>164.48 (n/a)</td><td>154.80 (n/a)</td><td>138.60 (n/a)</td><td>32.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (-6.08%)</td><td>0.13 (-8.83%)</td><td>0.12 (-13.07%)</td><td>0.11 (+0.18%)</td><td>0.02 <b>(-21.83%)</b></td><td>187.20 (-0.21%)</td><td>162.90 (+8.67%)</td><td>167.60 (+15.03%)</td><td>129.00 (+6.52%)</td><td>22.41 (-17.82%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.60 (n/a)</td><td>149.90 (n/a)</td><td>145.70 (n/a)</td><td>121.10 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (+17.72%)</td><td>0.10 (+8.65%)</td><td>0.10 (-2.58%)</td><td>0.08 <b>(+22.32%)</b></td><td>0.02 (-0.77%)</td><td>203.40 (-18.21%)</td><td>168.54 (-8.76%)</td><td>171.90 (+2.69%)</td><td>135.00 (-15.04%)</td><td>25.21 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>184.72 (n/a)</td><td>167.40 (n/a)</td><td>158.90 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 <b>(-27.59%)</b></td><td>0.10 (-11.11%)</td><td>0.10 (-18.32%)</td><td>0.09 <b>(+61.71%)</b></td><td>0.01 <b>(-78.95%)</b></td><td>215.10 <b>(-38.17%)</b></td><td>192.76 (-0.22%)</td><td>186.80 <b>(+22.41%)</b></td><td>178.70 <b>(+38.10%)</b></td><td>15.42 <b>(-82.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>347.90 (n/a)</td><td>193.18 (n/a)</td><td>152.60 (n/a)</td><td>129.40 (n/a)</td><td>89.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (+1.71%)</td><td>0.10 (-15.07%)</td><td>0.09 <b>(-28.33%)</b></td><td>0.08 (+3.69%)</td><td>0.02 (-0.31%)</td><td>198.40 (-3.55%)</td><td>171.14 (+17.25%)</td><td>183.40 <b>(+39.47%)</b></td><td>114.60 (-1.63%)</td><td>32.68 (-10.26%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>145.96 (n/a)</td><td>131.50 (n/a)</td><td>116.50 (n/a)</td><td>36.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (-4.26%)</td><td>0.11 (-6.13%)</td><td>0.09 <b>(-27.70%)</b></td><td>0.08 <b>(+25.60%)</b></td><td>0.03 (-11.97%)</td><td>226.60 <b>(-20.38%)</b></td><td>184.48 (+3.44%)</td><td>209.20 <b>(+38.27%)</b></td><td>135.00 (+4.41%)</td><td>44.45 <b>(-29.98%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>284.60 (n/a)</td><td>178.34 (n/a)</td><td>151.30 (n/a)</td><td>129.30 (n/a)</td><td>63.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (-15.59%)</td><td>0.09 (-13.83%)</td><td>0.08 (-14.76%)</td><td>0.07 (-11.63%)</td><td>0.02 <b>(-20.22%)</b></td><td>225.90 (+13.12%)</td><td>194.08 (+15.48%)</td><td>205.60 (+17.28%)</td><td>142.70 (+18.52%)</td><td>35.38 (+7.14%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.70 (n/a)</td><td>168.06 (n/a)</td><td>175.30 (n/a)</td><td>120.40 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (-14.01%)</td><td>0.09 (-5.36%)</td><td>0.09 (-11.16%)</td><td>0.07 <b>(+34.50%)</b></td><td>0.01 <b>(-61.66%)</b></td><td>232.80 <b>(-25.65%)</b></td><td>203.36 (-0.20%)</td><td>195.10 (+12.58%)</td><td>184.20 (+16.29%)</td><td>21.56 <b>(-66.92%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>313.10 (n/a)</td><td>203.76 (n/a)</td><td>173.30 (n/a)</td><td>158.40 (n/a)</td><td>65.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (-18.40%)</td><td>0.08 (-18.27%)</td><td>0.08 <b>(-25.63%)</b></td><td>0.05 (-2.08%)</td><td>0.02 <b>(-32.98%)</b></td><td>305.10 (+2.11%)</td><td>212.46 (+17.52%)</td><td>210.00 <b>(+34.44%)</b></td><td>155.60 <b>(+22.52%)</b></td><td>57.80 (-17.13%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>298.80 (n/a)</td><td>180.78 (n/a)</td><td>156.20 (n/a)</td><td>127.00 (n/a)</td><td>69.74 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (-4.25%)</td><td>0.09 (+5.64%)</td><td>0.08 (-1.84%)</td><td>0.08 <b>(+69.02%)</b></td><td>0.01 <b>(-60.22%)</b></td><td>220.30 <b>(-40.83%)</b></td><td>202.78 (-14.66%)</td><td>210.10 (+1.89%)</td><td>162.80 (+4.43%)</td><td>23.81 <b>(-74.65%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>372.30 (n/a)</td><td>237.62 (n/a)</td><td>206.20 (n/a)</td><td>155.90 (n/a)</td><td>93.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (+11.43%)</td><td>0.07 (-8.23%)</td><td>0.07 (-11.37%)</td><td>0.05 (-15.04%)</td><td>0.02 <b>(+80.32%)</b></td><td>352.10 (+17.72%)</td><td>261.46 (+14.90%)</td><td>241.60 (+12.84%)</td><td>170.90 (-10.29%)</td><td>79.31 <b>(+90.48%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>299.10 (n/a)</td><td>227.56 (n/a)</td><td>214.10 (n/a)</td><td>190.50 (n/a)</td><td>41.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (-17.14%)</td><td>0.20 (-12.03%)</td><td>0.19 (-8.59%)</td><td>0.17 (-4.77%)</td><td>0.03 <b>(-35.35%)</b></td><td>198.10 (+4.98%)</td><td>169.52 (+12.10%)</td><td>169.20 (+9.37%)</td><td>136.40 <b>(+20.71%)</b></td><td>23.49 (-17.72%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.70 (n/a)</td><td>151.22 (n/a)</td><td>154.70 (n/a)</td><td>113.00 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-12.85%)</td><td>0.17 (-15.42%)</td><td>0.18 (-7.46%)</td><td>0.14 <b>(-23.78%)</b></td><td>0.03 (+11.97%)</td><td>230.80 <b>(+31.21%)</b></td><td>191.26 (+19.24%)</td><td>182.30 (+8.06%)</td><td>155.20 (+14.79%)</td><td>28.66 <b>(+69.12%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>175.90 (n/a)</td><td>160.40 (n/a)</td><td>168.70 (n/a)</td><td>135.20 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (-0.85%)</td><td>0.24 (-3.52%)</td><td>0.23 (-11.46%)</td><td>0.19 (+0.87%)</td><td>0.04 (-6.48%)</td><td>216.80 (-0.87%)</td><td>176.28 (+3.34%)</td><td>177.60 (+12.98%)</td><td>145.60 (+0.83%)</td><td>27.20 (-7.92%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>218.70 (n/a)</td><td>170.58 (n/a)</td><td>157.20 (n/a)</td><td>144.40 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (-17.69%)</td><td>0.16 (-12.85%)</td><td>0.18 (+1.71%)</td><td>0.14 (-17.50%)</td><td>0.03 (+6.32%)</td><td>241.90 <b>(+21.19%)</b></td><td>202.94 (+15.69%)</td><td>180.30 (-1.64%)</td><td>177.00 <b>(+21.48%)</b></td><td>32.96 <b>(+57.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.60 (n/a)</td><td>175.42 (n/a)</td><td>183.30 (n/a)</td><td>145.70 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 <b>(-22.29%)</b></td><td>0.20 (-9.65%)</td><td>0.20 (+4.26%)</td><td>0.13 (-11.90%)</td><td>0.05 <b>(-33.96%)</b></td><td>319.10 (+13.52%)</td><td>216.38 (+7.71%)</td><td>209.30 (-4.12%)</td><td>158.40 <b>(+28.68%)</b></td><td>62.33 (+0.85%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>281.10 (n/a)</td><td>200.90 (n/a)</td><td>218.30 (n/a)</td><td>123.10 (n/a)</td><td>61.81 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 <b>(-24.70%)</b></td><td>0.16 (-19.42%)</td><td>0.17 <b>(-20.55%)</b></td><td>0.14 (-15.13%)</td><td>0.02 <b>(-37.31%)</b></td><td>235.50 (+17.81%)</td><td>201.86 <b>(+23.04%)</b></td><td>196.40 <b>(+25.82%)</b></td><td>170.40 <b>(+32.81%)</b></td><td>26.83 (-1.31%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.90 (n/a)</td><td>164.06 (n/a)</td><td>156.10 (n/a)</td><td>128.30 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (-19.86%)</td><td>0.19 (-13.56%)</td><td>0.20 (-6.23%)</td><td>0.16 (-12.25%)</td><td>0.02 <b>(-40.37%)</b></td><td>231.70 (+13.97%)</td><td>192.54 (+14.31%)</td><td>188.70 (+6.67%)</td><td>161.80 <b>(+24.85%)</b></td><td>25.09 (-13.31%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>203.30 (n/a)</td><td>168.44 (n/a)</td><td>176.90 (n/a)</td><td>129.60 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-6.76%)</td><td>0.17 (-19.09%)</td><td>0.18 (-9.41%)</td><td>0.11 <b>(-40.30%)</b></td><td>0.04 <b>(+117.45%)</b></td><td>305.60 <b>(+67.45%)</b></td><td>210.08 <b>(+30.16%)</b></td><td>179.90 (+10.44%)</td><td>154.60 (+7.21%)</td><td>60.83 <b>(+299.58%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>182.50 (n/a)</td><td>161.40 (n/a)</td><td>162.90 (n/a)</td><td>144.20 (n/a)</td><td>15.22 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (-10.12%)</td><td>0.18 (-18.77%)</td><td>0.17 <b>(-24.66%)</b></td><td>0.13 <b>(-28.08%)</b></td><td>0.03 <b>(+46.37%)</b></td><td>282.00 <b>(+39.05%)</b></td><td>215.44 <b>(+25.62%)</b></td><td>214.70 <b>(+32.78%)</b></td><td>175.60 (+11.28%)</td><td>42.70 <b>(+124.37%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>171.50 (n/a)</td><td>161.70 (n/a)</td><td>157.80 (n/a)</td><td>19.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (-8.89%)</td><td>0.20 (-11.94%)</td><td>0.20 (-10.99%)</td><td>0.14 <b>(-25.93%)</b></td><td>0.04 <b>(+28.47%)</b></td><td>226.10 <b>(+34.99%)</b></td><td>169.62 (+15.89%)</td><td>166.70 (+12.33%)</td><td>135.60 (+9.80%)</td><td>37.06 <b>(+86.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>167.50 (n/a)</td><td>146.36 (n/a)</td><td>148.40 (n/a)</td><td>123.50 (n/a)</td><td>19.91 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (-15.20%)</td><td>0.15 (-14.77%)</td><td>0.16 (-7.46%)</td><td>0.10 <b>(-26.72%)</b></td><td>0.03 (+10.48%)</td><td>351.30 <b>(+36.48%)</b></td><td>243.98 <b>(+20.06%)</b></td><td>217.80 (+8.09%)</td><td>189.10 (+17.97%)</td><td>63.87 <b>(+82.26%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>257.40 (n/a)</td><td>203.22 (n/a)</td><td>201.50 (n/a)</td><td>160.30 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (+14.31%)</td><td>0.19 (+15.30%)</td><td>0.17 (-2.47%)</td><td>0.16 <b>(+56.47%)</b></td><td>0.04 (-11.56%)</td><td>211.00 <b>(-36.08%)</b></td><td>179.18 (-16.64%)</td><td>189.70 (+2.54%)</td><td>136.80 (-12.53%)</td><td>35.06 <b>(-50.45%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>330.10 (n/a)</td><td>214.94 (n/a)</td><td>185.00 (n/a)</td><td>156.40 (n/a)</td><td>70.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (+7.06%)</td><td>0.16 (+4.79%)</td><td>0.18 (+10.01%)</td><td>0.11 (-17.44%)</td><td>0.03 <b>(+57.41%)</b></td><td>327.80 <b>(+21.14%)</b></td><td>224.64 (-1.77%)</td><td>191.00 (-9.09%)</td><td>187.00 (-6.59%)</td><td>60.11 <b>(+78.08%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>270.60 (n/a)</td><td>228.68 (n/a)</td><td>210.10 (n/a)</td><td>200.20 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (-8.29%)</td><td>0.15 (-1.28%)</td><td>0.15 (-2.21%)</td><td>0.14 <b>(+36.36%)</b></td><td>0.02 <b>(-57.88%)</b></td><td>239.40 <b>(-26.65%)</b></td><td>216.82 (-3.89%)</td><td>219.50 (+2.24%)</td><td>181.40 (+9.01%)</td><td>22.32 <b>(-65.96%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>326.40 (n/a)</td><td>225.60 (n/a)</td><td>214.70 (n/a)</td><td>166.40 (n/a)</td><td>65.57 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (-0.46%)</td><td>0.14 (+4.34%)</td><td>0.13 (+1.29%)</td><td>0.12 (+4.54%)</td><td>0.02 (+0.14%)</td><td>174.20 (-4.34%)</td><td>149.76 (-4.23%)</td><td>156.90 (-1.26%)</td><td>126.90 (+0.40%)</td><td>20.11 (-4.51%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>182.10 (n/a)</td><td>156.38 (n/a)</td><td>158.90 (n/a)</td><td>126.40 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (-2.50%)</td><td>0.13 (+0.77%)</td><td>0.13 (-3.60%)</td><td>0.12 (+9.19%)</td><td>0.01 <b>(-36.74%)</b></td><td>170.60 (-8.43%)</td><td>156.58 (-1.73%)</td><td>154.90 (+3.75%)</td><td>137.60 (+2.61%)</td><td>13.20 <b>(-41.59%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.30 (n/a)</td><td>159.34 (n/a)</td><td>149.30 (n/a)</td><td>134.10 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (-2.67%)</td><td>0.13 (+5.31%)</td><td>0.14 (+17.21%)</td><td>0.08 (-15.89%)</td><td>0.03 <b>(+35.45%)</b></td><td>242.40 (+18.94%)</td><td>163.62 (-2.35%)</td><td>144.90 (-14.71%)</td><td>132.60 (+2.79%)</td><td>45.75 <b>(+70.95%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>167.56 (n/a)</td><td>169.90 (n/a)</td><td>129.00 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (+6.84%)</td><td>0.12 (+14.49%)</td><td>0.13 <b>(+29.71%)</b></td><td>0.09 (+9.25%)</td><td>0.02 (-1.45%)</td><td>226.10 (-8.50%)</td><td>174.10 (-12.90%)</td><td>159.70 <b>(-22.92%)</b></td><td>155.40 (-6.39%)</td><td>29.60 (-11.79%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>247.10 (n/a)</td><td>199.88 (n/a)</td><td>207.20 (n/a)</td><td>166.00 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 <b>(+20.84%)</b></td><td>0.13 (+7.38%)</td><td>0.13 (+2.44%)</td><td>0.07 <b>(-27.88%)</b></td><td>0.04 <b>(+179.93%)</b></td><td>274.50 <b>(+38.71%)</b></td><td>173.32 (-0.31%)</td><td>162.80 (-2.40%)</td><td>125.30 (-17.24%)</td><td>59.94 <b>(+224.65%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>173.86 (n/a)</td><td>166.80 (n/a)</td><td>151.40 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (-1.94%)</td><td>0.14 (+9.72%)</td><td>0.16 (+19.27%)</td><td>0.10 (+11.09%)</td><td>0.03 (+5.39%)</td><td>212.00 (-9.98%)</td><td>154.32 (-8.92%)</td><td>131.30 (-16.16%)</td><td>126.90 (+1.93%)</td><td>37.79 (-8.29%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>235.50 (n/a)</td><td>169.44 (n/a)</td><td>156.60 (n/a)</td><td>124.50 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (+12.43%)</td><td>0.10 (+2.40%)</td><td>0.11 (+12.49%)</td><td>0.06 <b>(-37.90%)</b></td><td>0.03 <b>(+315.69%)</b></td><td>345.10 <b>(+61.04%)</b></td><td>216.52 (+4.39%)</td><td>188.10 (-11.11%)</td><td>165.80 (-11.05%)</td><td>73.65 <b>(+523.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>207.42 (n/a)</td><td>211.60 (n/a)</td><td>186.40 (n/a)</td><td>11.82 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (-15.60%)</td><td>0.09 <b>(-26.50%)</b></td><td>0.09 <b>(-28.02%)</b></td><td>0.07 <b>(-29.77%)</b></td><td>0.02 (+11.01%)</td><td>291.30 <b>(+42.38%)</b></td><td>234.26 <b>(+38.73%)</b></td><td>233.40 <b>(+38.93%)</b></td><td>167.10 (+18.43%)</td><td>48.89 <b>(+88.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>168.86 (n/a)</td><td>168.00 (n/a)</td><td>141.10 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (+4.81%)</td><td>0.16 (-8.00%)</td><td>0.17 (-6.25%)</td><td>0.12 (-17.92%)</td><td>0.04 <b>(+95.74%)</b></td><td>204.40 <b>(+21.81%)</b></td><td>156.40 (+12.21%)</td><td>140.60 (+6.60%)</td><td>123.30 (-4.57%)</td><td>36.53 <b>(+125.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>167.80 (n/a)</td><td>139.38 (n/a)</td><td>131.90 (n/a)</td><td>129.20 (n/a)</td><td>16.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (+6.99%)</td><td>0.16 (+2.02%)</td><td>0.17 (+4.17%)</td><td>0.12 (-14.17%)</td><td>0.03 <b>(+64.37%)</b></td><td>204.10 (+16.50%)</td><td>153.98 (+0.09%)</td><td>145.10 (-3.97%)</td><td>122.00 (-6.51%)</td><td>32.17 <b>(+79.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>175.20 (n/a)</td><td>153.84 (n/a)</td><td>151.10 (n/a)</td><td>130.50 (n/a)</td><td>17.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (+5.02%)</td><td>0.15 (-0.63%)</td><td>0.15 (-1.96%)</td><td>0.13 (+6.23%)</td><td>0.02 (+4.43%)</td><td>192.20 (-5.88%)</td><td>163.52 (+0.52%)</td><td>166.40 (+1.96%)</td><td>126.90 (-4.80%)</td><td>23.88 (-9.80%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.20 (n/a)</td><td>162.68 (n/a)</td><td>163.20 (n/a)</td><td>133.30 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (+15.88%)</td><td>0.16 (+8.04%)</td><td>0.15 (+4.29%)</td><td>0.12 (-8.08%)</td><td>0.03 <b>(+176.57%)</b></td><td>198.40 (+8.77%)</td><td>161.40 (-5.53%)</td><td>167.50 (-4.12%)</td><td>133.00 (-13.69%)</td><td>27.91 <b>(+151.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>170.84 (n/a)</td><td>174.70 (n/a)</td><td>154.10 (n/a)</td><td>11.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (-4.91%)</td><td>0.17 (-1.23%)</td><td>0.18 (+1.70%)</td><td>0.13 (+14.59%)</td><td>0.03 <b>(-21.64%)</b></td><td>193.50 (-12.72%)</td><td>149.18 (-0.82%)</td><td>135.70 (-1.67%)</td><td>126.30 (+5.16%)</td><td>27.66 <b>(-31.75%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>221.70 (n/a)</td><td>150.42 (n/a)</td><td>138.00 (n/a)</td><td>120.10 (n/a)</td><td>40.53 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 <b>(-21.86%)</b></td><td>0.14 (-15.42%)</td><td>0.14 (-19.26%)</td><td>0.10 (-3.97%)</td><td>0.02 <b>(-48.11%)</b></td><td>243.00 (+4.11%)</td><td>183.84 (+13.76%)</td><td>178.20 <b>(+23.84%)</b></td><td>154.70 <b>(+27.96%)</b></td><td>34.62 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>233.40 (n/a)</td><td>161.60 (n/a)</td><td>143.90 (n/a)</td><td>120.90 (n/a)</td><td>47.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (+18.63%)</td><td>0.13 (+16.14%)</td><td>0.12 (+6.68%)</td><td>0.12 <b>(+66.10%)</b></td><td>0.02 (-15.58%)</td><td>209.40 <b>(-39.81%)</b></td><td>190.16 (-17.05%)</td><td>201.10 (-6.25%)</td><td>143.40 (-15.70%)</td><td>27.50 <b>(-60.04%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>347.90 (n/a)</td><td>229.24 (n/a)</td><td>214.50 (n/a)</td><td>170.10 (n/a)</td><td>68.80 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (-1.54%)</td><td>0.12 (-10.45%)</td><td>0.12 (-8.29%)</td><td>0.08 <b>(-24.29%)</b></td><td>0.03 <b>(+35.24%)</b></td><td>290.00 <b>(+32.06%)</b></td><td>212.88 (+14.50%)</td><td>204.90 (+9.05%)</td><td>154.70 (+1.58%)</td><td>50.30 <b>(+83.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>185.92 (n/a)</td><td>187.90 (n/a)</td><td>152.30 (n/a)</td><td>27.35 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (-12.22%)</td><td>0.10 <b>(-23.09%)</b></td><td>0.10 <b>(-26.82%)</b></td><td>0.08 <b>(-35.17%)</b></td><td>0.02 <b>(+66.84%)</b></td><td>241.40 <b>(+54.25%)</b></td><td>181.88 <b>(+33.30%)</b></td><td>180.60 <b>(+36.61%)</b></td><td>140.70 (+13.93%)</td><td>37.47 <b>(+195.33%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>156.50 (n/a)</td><td>136.44 (n/a)</td><td>132.20 (n/a)</td><td>123.50 (n/a)</td><td>12.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 <b>(-31.06%)</b></td><td>0.09 <b>(-22.69%)</b></td><td>0.10 <b>(-21.40%)</b></td><td>0.08 (-10.31%)</td><td>0.01 <b>(-62.08%)</b></td><td>219.60 (+11.47%)</td><td>198.26 <b>(+25.83%)</b></td><td>193.60 <b>(+27.20%)</b></td><td>172.10 <b>(+45.11%)</b></td><td>20.39 <b>(-38.56%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>197.00 (n/a)</td><td>157.56 (n/a)</td><td>152.20 (n/a)</td><td>118.60 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (-9.06%)</td><td>0.12 (+0.72%)</td><td>0.12 (+6.32%)</td><td>0.10 (+1.00%)</td><td>0.02 (-7.33%)</td><td>182.10 (-0.98%)</td><td>153.18 (-0.83%)</td><td>149.20 (-5.99%)</td><td>128.80 (+9.90%)</td><td>25.49 (+2.25%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>183.90 (n/a)</td><td>154.46 (n/a)</td><td>158.70 (n/a)</td><td>117.20 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 <b>(+20.23%)</b></td><td>0.13 (+17.77%)</td><td>0.12 (+12.50%)</td><td>0.10 (+10.20%)</td><td>0.02 <b>(+82.14%)</b></td><td>177.80 (-9.29%)</td><td>148.96 (-14.48%)</td><td>150.30 (-11.12%)</td><td>131.70 (-16.80%)</td><td>19.00 <b>(+33.72%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>174.18 (n/a)</td><td>169.10 (n/a)</td><td>158.30 (n/a)</td><td>14.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 <b>(-21.35%)</b></td><td>0.09 (-19.16%)</td><td>0.10 (-11.86%)</td><td>0.07 <b>(-30.07%)</b></td><td>0.02 (-10.92%)</td><td>270.60 <b>(+43.02%)</b></td><td>203.00 <b>(+25.15%)</b></td><td>187.00 (+13.47%)</td><td>153.90 <b>(+27.19%)</b></td><td>45.61 <b>(+63.31%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>162.20 (n/a)</td><td>164.80 (n/a)</td><td>121.00 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (-16.71%)</td><td>0.10 (-7.12%)</td><td>0.10 (-16.70%)</td><td>0.09 <b>(+41.60%)</b></td><td>0.01 <b>(-63.93%)</b></td><td>206.70 <b>(-29.38%)</b></td><td>184.30 (+0.50%)</td><td>185.00 <b>(+20.05%)</b></td><td>156.40 <b>(+20.12%)</b></td><td>18.50 <b>(-71.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>292.70 (n/a)</td><td>183.38 (n/a)</td><td>154.10 (n/a)</td><td>130.20 (n/a)</td><td>64.31 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (-11.02%)</td><td>0.09 (-7.20%)</td><td>0.09 (-12.47%)</td><td>0.08 (-6.47%)</td><td>0.01 <b>(-26.93%)</b></td><td>229.20 (+6.90%)</td><td>201.66 (+7.25%)</td><td>204.20 (+14.21%)</td><td>179.80 (+12.38%)</td><td>19.76 (-14.57%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>188.02 (n/a)</td><td>178.80 (n/a)</td><td>160.00 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 <b>(-31.28%)</b></td><td>0.09 (-18.13%)</td><td>0.09 (-16.29%)</td><td>0.07 (-19.05%)</td><td>0.01 <b>(-51.12%)</b></td><td>264.00 <b>(+23.54%)</b></td><td>214.10 (+19.73%)</td><td>202.90 (+19.49%)</td><td>187.90 <b>(+45.43%)</b></td><td>30.70 (-13.96%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>213.70 (n/a)</td><td>178.82 (n/a)</td><td>169.80 (n/a)</td><td>129.20 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.76 (+2.28%)</td><td>0.65 (-3.89%)</td><td>0.64 (-10.99%)</td><td>0.54 (-3.84%)</td><td>0.08 (-1.51%)</td><td>182.40 (+3.99%)</td><td>154.34 (+4.03%)</td><td>154.30 (+12.38%)</td><td>128.80 (-2.20%)</td><td>20.24 (+0.83%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.72 (n/a)</td><td>0.56 (n/a)</td><td>0.09 (n/a)</td><td>175.40 (n/a)</td><td>148.36 (n/a)</td><td>137.30 (n/a)</td><td>131.70 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.67 <b>(-22.58%)</b></td><td>0.57 (-14.27%)</td><td>0.52 (-10.89%)</td><td>0.50 (-9.23%)</td><td>0.08 <b>(-41.65%)</b></td><td>194.90 (+10.18%)</td><td>176.16 (+14.97%)</td><td>187.60 (+12.27%)</td><td>146.10 <b>(+29.18%)</b></td><td>22.63 (-16.21%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.87 (n/a)</td><td>0.66 (n/a)</td><td>0.59 (n/a)</td><td>0.56 (n/a)</td><td>0.13 (n/a)</td><td>176.90 (n/a)</td><td>153.22 (n/a)</td><td>167.10 (n/a)</td><td>113.10 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.86 <b>(+21.61%)</b></td><td>0.61 (+0.52%)</td><td>0.57 (-6.03%)</td><td>0.47 (-9.44%)</td><td>0.15 <b>(+97.50%)</b></td><td>208.50 (+10.43%)</td><td>166.68 (+2.45%)</td><td>172.30 (+6.42%)</td><td>113.80 (-17.77%)</td><td>35.40 <b>(+74.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.71 (n/a)</td><td>0.61 (n/a)</td><td>0.61 (n/a)</td><td>0.52 (n/a)</td><td>0.08 (n/a)</td><td>188.80 (n/a)</td><td>162.70 (n/a)</td><td>161.90 (n/a)</td><td>138.40 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.57 (-5.78%)</td><td>0.49 (+1.15%)</td><td>0.50 (-1.18%)</td><td>0.42 <b>(+52.96%)</b></td><td>0.06 <b>(-50.29%)</b></td><td>234.70 <b>(-34.62%)</b></td><td>202.56 (-7.43%)</td><td>198.40 (+1.17%)</td><td>172.30 (+6.10%)</td><td>26.58 <b>(-66.86%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.50 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>359.00 (n/a)</td><td>218.82 (n/a)</td><td>196.10 (n/a)</td><td>162.40 (n/a)</td><td>80.19 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.49 (-10.01%)</td><td>0.41 (-12.17%)</td><td>0.42 (-13.61%)</td><td>0.33 (-4.07%)</td><td>0.07 (-7.06%)</td><td>222.30 (+4.22%)</td><td>183.78 (+13.75%)</td><td>177.40 (+15.80%)</td><td>151.10 (+11.10%)</td><td>30.85 (+3.40%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>213.30 (n/a)</td><td>161.56 (n/a)</td><td>153.20 (n/a)</td><td>136.00 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.56 (-5.50%)</td><td>0.52 <b>(+21.59%)</b></td><td>0.55 <b>(+27.81%)</b></td><td>0.46 <b>(+53.86%)</b></td><td>0.05 <b>(-53.22%)</b></td><td>161.50 <b>(-35.01%)</b></td><td>143.96 <b>(-21.11%)</b></td><td>134.60 <b>(-21.79%)</b></td><td>132.60 (+5.83%)</td><td>14.49 <b>(-67.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>248.50 (n/a)</td><td>182.48 (n/a)</td><td>172.10 (n/a)</td><td>125.30 (n/a)</td><td>44.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.50 (-11.09%)</td><td>0.42 (-2.59%)</td><td>0.43 (+7.38%)</td><td>0.34 (-2.15%)</td><td>0.07 <b>(-22.98%)</b></td><td>217.40 (+2.21%)</td><td>180.84 (+1.70%)</td><td>172.00 (-6.88%)</td><td>147.10 (+12.46%)</td><td>29.95 (-9.78%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>212.70 (n/a)</td><td>177.82 (n/a)</td><td>184.70 (n/a)</td><td>130.80 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.42 (-15.04%)</td><td>0.38 (-6.08%)</td><td>0.38 (-0.01%)</td><td>0.33 (+5.09%)</td><td>0.04 <b>(-40.71%)</b></td><td>224.90 (-4.86%)</td><td>198.78 (+4.72%)</td><td>192.00 (+0.00%)</td><td>173.50 (+17.71%)</td><td>24.01 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>236.40 (n/a)</td><td>189.82 (n/a)</td><td>192.00 (n/a)</td><td>147.40 (n/a)</td><td>35.30 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.34 (+17.15%)</td><td>0.25 (+12.23%)</td><td>0.25 <b>(+20.56%)</b></td><td>0.17 (-6.22%)</td><td>0.06 <b>(+45.07%)</b></td><td>223.20 (+6.64%)</td><td>153.72 (-8.42%)</td><td>145.40 (-17.06%)</td><td>108.30 (-14.66%)</td><td>43.32 <b>(+36.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>209.30 (n/a)</td><td>167.86 (n/a)</td><td>175.30 (n/a)</td><td>126.90 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (+1.10%)</td><td>0.26 (+7.71%)</td><td>0.25 (+9.95%)</td><td>0.23 (+15.08%)</td><td>0.02 <b>(-26.02%)</b></td><td>160.50 (-13.10%)</td><td>145.42 (-7.86%)</td><td>146.10 (-9.03%)</td><td>127.10 (-1.09%)</td><td>13.46 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>184.70 (n/a)</td><td>157.82 (n/a)</td><td>160.60 (n/a)</td><td>128.50 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 <b>(+34.17%)</b></td><td>0.25 <b>(+35.75%)</b></td><td>0.26 <b>(+51.37%)</b></td><td>0.20 <b>(+25.09%)</b></td><td>0.04 <b>(+79.69%)</b></td><td>188.00 <b>(-20.07%)</b></td><td>152.86 <b>(-25.46%)</b></td><td>141.60 <b>(-33.92%)</b></td><td>128.60 <b>(-25.45%)</b></td><td>27.28 (+7.36%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>235.20 (n/a)</td><td>205.08 (n/a)</td><td>214.30 (n/a)</td><td>172.50 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (-18.87%)</td><td>0.21 (-7.11%)</td><td>0.20 <b>(-21.27%)</b></td><td>0.18 <b>(+86.27%)</b></td><td>0.03 <b>(-61.11%)</b></td><td>205.50 <b>(-46.32%)</b></td><td>174.90 (-8.51%)</td><td>183.20 <b>(+27.05%)</b></td><td>139.20 <b>(+23.19%)</b></td><td>26.18 <b>(-76.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>382.80 (n/a)</td><td>191.16 (n/a)</td><td>144.20 (n/a)</td><td>113.00 (n/a)</td><td>110.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (+7.05%)</td><td>0.20 (-7.02%)</td><td>0.18 (-7.36%)</td><td>0.13 (-13.90%)</td><td>0.06 (+15.80%)</td><td>276.40 (+16.13%)</td><td>198.20 (+9.83%)</td><td>206.90 (+7.93%)</td><td>128.70 (-6.60%)</td><td>55.55 <b>(+30.52%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>238.00 (n/a)</td><td>180.46 (n/a)</td><td>191.70 (n/a)</td><td>137.80 (n/a)</td><td>42.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 <b>(-31.57%)</b></td><td>0.19 (-19.16%)</td><td>0.20 (-9.56%)</td><td>0.13 (-14.26%)</td><td>0.04 <b>(-43.72%)</b></td><td>285.60 (+16.67%)</td><td>205.64 <b>(+20.16%)</b></td><td>182.60 (+10.53%)</td><td>170.10 <b>(+46.13%)</b></td><td>48.05 (-3.76%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>244.80 (n/a)</td><td>171.14 (n/a)</td><td>165.20 (n/a)</td><td>116.40 (n/a)</td><td>49.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 <b>(-33.11%)</b></td><td>0.18 (-14.18%)</td><td>0.19 (+0.95%)</td><td>0.14 <b>(+29.89%)</b></td><td>0.03 <b>(-64.93%)</b></td><td>268.40 <b>(-23.01%)</b></td><td>208.02 (+4.08%)</td><td>193.90 (-0.92%)</td><td>181.70 <b>(+49.55%)</b></td><td>36.08 <b>(-59.84%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>348.60 (n/a)</td><td>199.86 (n/a)</td><td>195.70 (n/a)</td><td>121.50 (n/a)</td><td>89.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 <b>(-27.65%)</b></td><td>0.18 (-0.06%)</td><td>0.20 (+2.37%)</td><td>0.11 (+5.56%)</td><td>0.04 <b>(-48.43%)</b></td><td>325.80 (-5.26%)</td><td>214.36 (-8.84%)</td><td>186.70 (-2.30%)</td><td>182.70 <b>(+38.20%)</b></td><td>62.35 <b>(-37.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>343.90 (n/a)</td><td>235.14 (n/a)</td><td>191.10 (n/a)</td><td>132.20 (n/a)</td><td>99.03 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (+3.05%)</td><td>0.27 (+1.59%)</td><td>0.28 (+8.07%)</td><td>0.23 (-5.32%)</td><td>0.04 <b>(+37.61%)</b></td><td>179.80 (+5.58%)</td><td>154.28 (-0.73%)</td><td>148.30 (-7.49%)</td><td>127.20 (-2.90%)</td><td>22.12 <b>(+45.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>170.30 (n/a)</td><td>155.42 (n/a)</td><td>160.30 (n/a)</td><td>131.00 (n/a)</td><td>15.23 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.31 (-5.24%)</td><td>0.28 (+3.02%)</td><td>0.29 (+9.84%)</td><td>0.23 (-0.11%)</td><td>0.03 <b>(-24.90%)</b></td><td>177.00 (+0.11%)</td><td>147.28 (-3.50%)</td><td>142.40 (-8.95%)</td><td>134.10 (+5.51%)</td><td>17.08 (-18.38%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>176.80 (n/a)</td><td>152.62 (n/a)</td><td>156.40 (n/a)</td><td>127.10 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (-16.48%)</td><td>0.24 (-12.43%)</td><td>0.25 (-11.04%)</td><td>0.20 (-14.88%)</td><td>0.03 <b>(-36.96%)</b></td><td>202.20 (+17.49%)</td><td>169.32 (+13.36%)</td><td>164.70 (+12.42%)</td><td>152.80 (+19.75%)</td><td>19.45 (-10.36%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>172.10 (n/a)</td><td>149.36 (n/a)</td><td>146.50 (n/a)</td><td>127.60 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 (-6.36%)</td><td>0.24 (+11.13%)</td><td>0.22 (-2.17%)</td><td>0.20 <b>(+80.40%)</b></td><td>0.05 <b>(-42.34%)</b></td><td>208.10 <b>(-44.57%)</b></td><td>176.00 (-19.34%)</td><td>183.60 (+2.23%)</td><td>136.70 (+6.80%)</td><td>32.89 <b>(-66.55%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>375.40 (n/a)</td><td>218.20 (n/a)</td><td>179.60 (n/a)</td><td>128.00 (n/a)</td><td>98.32 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.33 <b>(+41.45%)</b></td><td>0.25 <b>(+20.81%)</b></td><td>0.25 (+16.69%)</td><td>0.15 (-5.43%)</td><td>0.08 <b>(+164.41%)</b></td><td>275.10 (+5.73%)</td><td>182.20 (-10.95%)</td><td>161.60 (-14.32%)</td><td>124.00 <b>(-29.30%)</b></td><td>64.28 <b>(+90.56%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>260.20 (n/a)</td><td>204.60 (n/a)</td><td>188.60 (n/a)</td><td>175.40 (n/a)</td><td>33.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (-4.52%)</td><td>0.19 (-11.61%)</td><td>0.22 (-1.60%)</td><td>0.13 <b>(-29.46%)</b></td><td>0.05 <b>(+56.84%)</b></td><td>321.90 <b>(+41.74%)</b></td><td>222.98 (+17.97%)</td><td>187.90 (+1.62%)</td><td>166.10 (+4.73%)</td><td>64.11 <b>(+134.88%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>227.10 (n/a)</td><td>189.02 (n/a)</td><td>184.90 (n/a)</td><td>158.60 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (+13.14%)</td><td>0.20 (-1.46%)</td><td>0.16 <b>(-20.73%)</b></td><td>0.12 (+12.45%)</td><td>0.10 (+12.37%)</td><td>332.20 (-11.08%)</td><td>235.04 (+0.51%)</td><td>251.50 <b>(+26.19%)</b></td><td>110.40 (-11.61%)</td><td>87.58 (-16.24%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>373.60 (n/a)</td><td>233.84 (n/a)</td><td>199.30 (n/a)</td><td>124.90 (n/a)</td><td>104.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (-5.25%)</td><td>0.19 (-3.60%)</td><td>0.20 (-1.86%)</td><td>0.13 (+7.47%)</td><td>0.04 <b>(-27.88%)</b></td><td>326.80 (-6.95%)</td><td>226.02 (-0.01%)</td><td>205.00 (+1.89%)</td><td>171.00 (+5.56%)</td><td>59.65 <b>(-24.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>351.20 (n/a)</td><td>226.04 (n/a)</td><td>201.20 (n/a)</td><td>162.00 (n/a)</td><td>78.70 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (+5.19%)</td><td>0.21 (-6.02%)</td><td>0.22 (+0.95%)</td><td>0.09 <b>(-54.39%)</b></td><td>0.08 <b>(+142.21%)</b></td><td>395.20 <b>(+119.31%)</b></td><td>201.24 <b>(+24.56%)</b></td><td>160.40 (-0.93%)</td><td>122.20 (-4.90%)</td><td>111.80 <b>(+427.09%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>180.20 (n/a)</td><td>161.56 (n/a)</td><td>161.90 (n/a)</td><td>128.50 (n/a)</td><td>21.21 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (-3.03%)</td><td>0.22 (-6.07%)</td><td>0.20 (-18.74%)</td><td>0.18 (+1.88%)</td><td>0.04 (-7.88%)</td><td>197.30 (-1.84%)</td><td>165.94 (+5.98%)</td><td>176.90 <b>(+23.02%)</b></td><td>131.50 (+3.14%)</td><td>28.91 (-7.95%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>201.00 (n/a)</td><td>156.58 (n/a)</td><td>143.80 (n/a)</td><td>127.50 (n/a)</td><td>31.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (-4.21%)</td><td>0.23 (+12.29%)</td><td>0.24 (+19.26%)</td><td>0.17 <b>(+33.49%)</b></td><td>0.04 <b>(-20.47%)</b></td><td>200.30 <b>(-25.07%)</b></td><td>158.32 (-13.45%)</td><td>144.90 (-16.15%)</td><td>132.90 (+4.32%)</td><td>30.43 <b>(-40.76%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>267.30 (n/a)</td><td>182.92 (n/a)</td><td>172.80 (n/a)</td><td>127.40 (n/a)</td><td>51.36 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 <b>(+31.27%)</b></td><td>0.22 <b>(+25.58%)</b></td><td>0.24 <b>(+37.49%)</b></td><td>0.16 <b>(+23.53%)</b></td><td>0.05 <b>(+56.94%)</b></td><td>218.80 (-19.05%)</td><td>167.74 (-18.86%)</td><td>147.80 <b>(-27.26%)</b></td><td>127.50 <b>(-23.84%)</b></td><td>43.28 (+1.51%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>270.30 (n/a)</td><td>206.74 (n/a)</td><td>203.20 (n/a)</td><td>167.40 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (-5.61%)</td><td>0.17 (-15.19%)</td><td>0.19 (-5.46%)</td><td>0.10 <b>(-39.54%)</b></td><td>0.05 <b>(+85.63%)</b></td><td>332.10 <b>(+65.39%)</b></td><td>221.12 <b>(+26.89%)</b></td><td>186.60 (+5.78%)</td><td>147.80 (+5.95%)</td><td>76.57 <b>(+236.02%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>200.80 (n/a)</td><td>174.26 (n/a)</td><td>176.40 (n/a)</td><td>139.50 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 <b>(-38.89%)</b></td><td>0.19 <b>(-24.21%)</b></td><td>0.18 <b>(-23.19%)</b></td><td>0.16 (-16.25%)</td><td>0.03 <b>(-58.29%)</b></td><td>221.60 (+19.40%)</td><td>186.88 <b>(+27.91%)</b></td><td>193.80 <b>(+30.24%)</b></td><td>155.70 <b>(+63.55%)</b></td><td>27.52 (-15.57%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>185.60 (n/a)</td><td>146.10 (n/a)</td><td>148.80 (n/a)</td><td>95.20 (n/a)</td><td>32.59 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 <b>(-24.40%)</b></td><td>0.17 <b>(-24.27%)</b></td><td>0.19 (-15.93%)</td><td>0.09 <b>(-43.29%)</b></td><td>0.05 (-7.19%)</td><td>370.10 <b>(+76.32%)</b></td><td>226.30 <b>(+37.70%)</b></td><td>187.10 (+18.94%)</td><td>167.90 <b>(+32.20%)</b></td><td>84.26 <b>(+121.05%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>209.90 (n/a)</td><td>164.34 (n/a)</td><td>157.30 (n/a)</td><td>127.00 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.35 <b>(+31.48%)</b></td><td>0.18 (-11.59%)</td><td>0.16 <b>(-26.02%)</b></td><td>0.11 (+0.31%)</td><td>0.10 <b>(+59.19%)</b></td><td>330.70 (-0.30%)</td><td>233.62 <b>(+22.24%)</b></td><td>221.60 <b>(+35.20%)</b></td><td>99.00 <b>(-23.90%)</b></td><td>94.28 (+15.47%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>331.70 (n/a)</td><td>191.12 (n/a)</td><td>163.90 (n/a)</td><td>130.10 (n/a)</td><td>81.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.93 (+13.75%)</td><td>0.82 (+14.54%)</td><td>0.79 (+5.75%)</td><td>0.77 <b>(+27.63%)</b></td><td>0.06 <b>(-26.66%)</b></td><td>169.50 <b>(-21.64%)</b></td><td>160.68 (-13.37%)</td><td>165.30 (-5.43%)</td><td>141.60 (-12.10%)</td><td>11.71 <b>(-49.90%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.81 (n/a)</td><td>0.72 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.09 (n/a)</td><td>216.30 (n/a)</td><td>185.48 (n/a)</td><td>174.80 (n/a)</td><td>161.10 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.01 (-10.42%)</td><td>0.79 (-1.03%)</td><td>0.80 (+7.39%)</td><td>0.59 (-3.63%)</td><td>0.16 <b>(-24.46%)</b></td><td>220.60 (+3.76%)</td><td>170.92 (-0.58%)</td><td>164.40 (-6.86%)</td><td>129.50 (+11.64%)</td><td>34.70 (-12.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.13 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.21 (n/a)</td><td>212.60 (n/a)</td><td>171.92 (n/a)</td><td>176.50 (n/a)</td><td>116.00 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.11 <b>(+30.60%)</b></td><td>0.83 (+18.04%)</td><td>0.79 (+5.81%)</td><td>0.72 <b>(+105.87%)</b></td><td>0.16 <b>(-20.44%)</b></td><td>183.10 <b>(-51.42%)</b></td><td>162.68 <b>(-22.19%)</b></td><td>166.20 (-5.51%)</td><td>117.80 <b>(-23.41%)</b></td><td>26.36 <b>(-72.15%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.85 (n/a)</td><td>0.70 (n/a)</td><td>0.75 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>376.90 (n/a)</td><td>209.08 (n/a)</td><td>175.90 (n/a)</td><td>153.80 (n/a)</td><td>94.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.00 (+0.00%)</td><td>0.00 (+5.66%)</td><td>0.00 (+9.09%)</td><td>0.00 (+0.00%)</td><td>0.00 (-14.03%)</td><td>4586.06 (-3.65%)</td><td>3751.68 (-7.35%)</td><td>3512.41 (-5.66%)</td><td>3481.47 (-0.94%)</td><td>472.37 <b>(-26.40%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4759.67 (n/a)</td><td>4049.40 (n/a)</td><td>3723.25 (n/a)</td><td>3514.63 (n/a)</td><td>641.77 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.00 (+0.00%)</td><td>0.00 (+3.81%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.88%)</td><td>0.00 <b>(-23.35%)</b></td><td>4621.24 (-5.43%)</td><td>3815.04 (-4.01%)</td><td>3605.43 (+1.16%)</td><td>3565.40 (+0.78%)</td><td>453.13 <b>(-25.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4886.68 (n/a)</td><td>3974.46 (n/a)</td><td>3563.96 (n/a)</td><td>3537.80 (n/a)</td><td>608.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (-0.50%)</td><td>0.23 (-2.60%)</td><td>0.28 (+6.31%)</td><td>0.15 (-15.80%)</td><td>0.06 <b>(+32.15%)</b></td><td>13716.74 (+18.79%)</td><td>9751.59 (+6.26%)</td><td>7596.25 (-5.92%)</td><td>7577.42 (+0.51%)</td><td>3004.92 <b>(+51.64%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>11546.64 (n/a)</td><td>9176.72 (n/a)</td><td>8073.83 (n/a)</td><td>7538.74 (n/a)</td><td>1981.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>5.71 (-0.24%)</td><td>4.84 (-4.54%)</td><td>4.96 (+4.14%)</td><td>4.02 (-12.92%)</td><td>0.71 <b>(+33.14%)</b></td><td>260.50 (+14.81%)</td><td>220.52 (+5.68%)</td><td>211.30 (-3.95%)</td><td>183.50 (+0.22%)</td><td>32.63 <b>(+55.25%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.73 (n/a)</td><td>5.07 (n/a)</td><td>4.77 (n/a)</td><td>4.62 (n/a)</td><td>0.53 (n/a)</td><td>226.90 (n/a)</td><td>208.66 (n/a)</td><td>220.00 (n/a)</td><td>183.10 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.76 (-7.68%)</td><td>4.24 (-9.28%)</td><td>4.46 (-3.68%)</td><td>3.17 <b>(-23.67%)</b></td><td>0.66 <b>(+48.41%)</b></td><td>331.20 <b>(+31.01%)</b></td><td>252.74 (+11.96%)</td><td>234.90 (+3.80%)</td><td>220.40 (+8.30%)</td><td>46.13 <b>(+114.46%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.15 (n/a)</td><td>4.68 (n/a)</td><td>4.63 (n/a)</td><td>4.15 (n/a)</td><td>0.44 (n/a)</td><td>252.80 (n/a)</td><td>225.74 (n/a)</td><td>226.30 (n/a)</td><td>203.50 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.19 (+5.27%)</td><td>4.93 (-3.68%)</td><td>4.77 (-10.47%)</td><td>4.06 (-3.90%)</td><td>0.78 (+13.01%)</td><td>258.10 (+4.07%)</td><td>216.50 (+4.17%)</td><td>219.70 (+11.69%)</td><td>169.30 (-5.05%)</td><td>31.87 (+8.92%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>5.88 (n/a)</td><td>5.12 (n/a)</td><td>5.33 (n/a)</td><td>4.23 (n/a)</td><td>0.69 (n/a)</td><td>248.00 (n/a)</td><td>207.84 (n/a)</td><td>196.70 (n/a)</td><td>178.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.83 (-19.49%)</td><td>4.39 (-16.66%)</td><td>4.33 (-14.53%)</td><td>3.88 (-18.57%)</td><td>0.39 <b>(-31.06%)</b></td><td>270.50 <b>(+22.79%)</b></td><td>240.62 (+19.69%)</td><td>242.30 (+17.00%)</td><td>217.20 <b>(+24.19%)</b></td><td>21.54 (+3.60%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.00 (n/a)</td><td>5.26 (n/a)</td><td>5.06 (n/a)</td><td>4.76 (n/a)</td><td>0.56 (n/a)</td><td>220.30 (n/a)</td><td>201.04 (n/a)</td><td>207.10 (n/a)</td><td>174.90 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.09 (-13.00%)</td><td>7.41 (-11.84%)</td><td>7.17 (-15.78%)</td><td>6.98 (-6.99%)</td><td>0.47 <b>(-39.28%)</b></td><td>300.30 (+7.52%)</td><td>283.94 (+13.02%)</td><td>292.30 (+18.72%)</td><td>259.20 (+14.94%)</td><td>17.54 <b>(-25.36%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.30 (n/a)</td><td>8.41 (n/a)</td><td>8.52 (n/a)</td><td>7.51 (n/a)</td><td>0.78 (n/a)</td><td>279.30 (n/a)</td><td>251.24 (n/a)</td><td>246.20 (n/a)</td><td>225.50 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.54 (-2.49%)</td><td>7.85 (-2.43%)</td><td>8.08 (+0.39%)</td><td>6.95 (-4.09%)</td><td>0.67 <b>(+24.98%)</b></td><td>301.80 (+4.28%)</td><td>268.80 (+2.75%)</td><td>259.50 (-0.38%)</td><td>245.50 (+2.55%)</td><td>23.85 <b>(+33.03%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>8.76 (n/a)</td><td>8.05 (n/a)</td><td>8.05 (n/a)</td><td>7.25 (n/a)</td><td>0.54 (n/a)</td><td>289.40 (n/a)</td><td>261.60 (n/a)</td><td>260.50 (n/a)</td><td>239.40 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.84 (-19.14%)</td><td>7.41 (-9.77%)</td><td>7.36 (-7.12%)</td><td>7.13 (-4.86%)</td><td>0.29 <b>(-66.98%)</b></td><td>294.30 (+5.11%)</td><td>283.44 (+10.02%)</td><td>284.90 (+7.67%)</td><td>267.50 <b>(+23.67%)</b></td><td>11.02 <b>(-56.60%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.70 (n/a)</td><td>8.21 (n/a)</td><td>7.93 (n/a)</td><td>7.49 (n/a)</td><td>0.89 (n/a)</td><td>280.00 (n/a)</td><td>257.62 (n/a)</td><td>264.60 (n/a)</td><td>216.30 (n/a)</td><td>25.39 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.90 (+4.01%)</td><td>8.64 (-4.51%)</td><td>8.83 (-2.86%)</td><td>7.20 (-12.75%)</td><td>1.01 <b>(+110.78%)</b></td><td>291.30 (+14.64%)</td><td>245.62 (+5.68%)</td><td>237.40 (+2.90%)</td><td>211.80 (-3.86%)</td><td>29.97 <b>(+132.58%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.52 (n/a)</td><td>9.04 (n/a)</td><td>9.09 (n/a)</td><td>8.25 (n/a)</td><td>0.48 (n/a)</td><td>254.10 (n/a)</td><td>232.42 (n/a)</td><td>230.70 (n/a)</td><td>220.30 (n/a)</td><td>12.89 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.67 (-9.20%)</td><td>8.57 (-6.32%)</td><td>8.73 (-16.13%)</td><td>7.05 (+16.67%)</td><td>0.98 <b>(-52.67%)</b></td><td>297.60 (-14.29%)</td><td>247.44 (+2.71%)</td><td>240.40 (+19.25%)</td><td>216.90 (+10.10%)</td><td>30.60 <b>(-53.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>10.65 (n/a)</td><td>9.15 (n/a)</td><td>10.40 (n/a)</td><td>6.04 (n/a)</td><td>2.06 (n/a)</td><td>347.20 (n/a)</td><td>240.90 (n/a)</td><td>201.60 (n/a)</td><td>197.00 (n/a)</td><td>65.42 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.16 (-16.81%)</td><td>8.53 (-10.82%)</td><td>8.50 (-11.28%)</td><td>7.91 (-2.20%)</td><td>0.58 <b>(-44.96%)</b></td><td>265.00 (+2.24%)</td><td>246.70 (+11.44%)</td><td>246.90 (+12.74%)</td><td>229.00 <b>(+20.21%)</b></td><td>16.85 <b>(-32.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>11.01 (n/a)</td><td>9.57 (n/a)</td><td>9.58 (n/a)</td><td>8.09 (n/a)</td><td>1.06 (n/a)</td><td>259.20 (n/a)</td><td>221.38 (n/a)</td><td>219.00 (n/a)</td><td>190.50 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.12 (-4.07%)</td><td>10.86 (-9.61%)</td><td>10.88 (-8.29%)</td><td>9.59 (-14.27%)</td><td>0.91 <b>(+53.77%)</b></td><td>437.50 (+16.64%)</td><td>388.44 (+11.03%)</td><td>385.60 (+9.05%)</td><td>346.10 (+4.25%)</td><td>32.83 <b>(+88.62%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>12.63 (n/a)</td><td>12.01 (n/a)</td><td>11.86 (n/a)</td><td>11.18 (n/a)</td><td>0.59 (n/a)</td><td>375.10 (n/a)</td><td>349.84 (n/a)</td><td>353.60 (n/a)</td><td>332.00 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.79 (+3.23%)</td><td>12.03 (+2.10%)</td><td>12.21 (-0.32%)</td><td>10.77 (-1.59%)</td><td>0.77 (+6.19%)</td><td>389.30 (+1.62%)</td><td>349.86 (-2.03%)</td><td>343.60 (+0.29%)</td><td>327.90 (-3.13%)</td><td>23.71 (+5.44%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>12.39 (n/a)</td><td>11.78 (n/a)</td><td>12.24 (n/a)</td><td>10.95 (n/a)</td><td>0.73 (n/a)</td><td>383.10 (n/a)</td><td>357.10 (n/a)</td><td>342.60 (n/a)</td><td>338.50 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.64 (-5.51%)</td><td>11.94 (+1.22%)</td><td>12.39 (+5.45%)</td><td>10.61 (+4.05%)</td><td>0.83 <b>(-28.08%)</b></td><td>395.50 (-3.89%)</td><td>352.64 (-1.56%)</td><td>338.50 (-5.16%)</td><td>331.80 (+5.84%)</td><td>26.17 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>13.38 (n/a)</td><td>11.80 (n/a)</td><td>11.75 (n/a)</td><td>10.19 (n/a)</td><td>1.16 (n/a)</td><td>411.50 (n/a)</td><td>358.24 (n/a)</td><td>356.90 (n/a)</td><td>313.50 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.16 (-7.46%)</td><td>13.14 (-2.01%)</td><td>13.78 (+7.49%)</td><td>11.79 (-3.82%)</td><td>1.17 (-13.84%)</td><td>355.90 (+3.97%)</td><td>321.36 (+1.92%)</td><td>304.30 (-6.97%)</td><td>296.20 (+8.06%)</td><td>29.44 (-3.65%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>15.30 (n/a)</td><td>13.41 (n/a)</td><td>12.82 (n/a)</td><td>12.26 (n/a)</td><td>1.35 (n/a)</td><td>342.30 (n/a)</td><td>315.32 (n/a)</td><td>327.10 (n/a)</td><td>274.10 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.13 (-0.59%)</td><td>13.48 (+1.38%)</td><td>13.61 (+1.33%)</td><td>12.25 (+2.97%)</td><td>0.76 <b>(-22.73%)</b></td><td>342.40 (-2.89%)</td><td>311.90 (-1.54%)</td><td>308.20 (-1.31%)</td><td>296.90 (+0.61%)</td><td>18.38 <b>(-23.73%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>14.21 (n/a)</td><td>13.30 (n/a)</td><td>13.43 (n/a)</td><td>11.90 (n/a)</td><td>0.98 (n/a)</td><td>352.60 (n/a)</td><td>316.78 (n/a)</td><td>312.30 (n/a)</td><td>295.10 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.57 (-4.28%)</td><td>11.89 (-14.58%)</td><td>11.86 (-17.26%)</td><td>9.44 (-18.67%)</td><td>2.23 <b>(+55.46%)</b></td><td>444.50 <b>(+22.96%)</b></td><td>363.14 (+19.35%)</td><td>353.70 <b>(+20.88%)</b></td><td>287.90 (+4.50%)</td><td>68.48 <b>(+98.99%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>15.22 (n/a)</td><td>13.91 (n/a)</td><td>14.33 (n/a)</td><td>11.60 (n/a)</td><td>1.43 (n/a)</td><td>361.50 (n/a)</td><td>304.26 (n/a)</td><td>292.60 (n/a)</td><td>275.50 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>16.78 (+16.41%)</td><td>13.42 (+5.13%)</td><td>13.11 (+5.24%)</td><td>12.03 (+17.22%)</td><td>1.95 (+14.34%)</td><td>348.70 (-14.68%)</td><td>317.16 (-4.93%)</td><td>319.90 (-4.99%)</td><td>250.00 (-14.09%)</td><td>40.18 (-16.03%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>14.41 (n/a)</td><td>12.77 (n/a)</td><td>12.46 (n/a)</td><td>10.26 (n/a)</td><td>1.71 (n/a)</td><td>408.70 (n/a)</td><td>333.62 (n/a)</td><td>336.70 (n/a)</td><td>291.00 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.66 (-9.41%)</td><td>12.60 (-8.99%)</td><td>12.74 (-15.09%)</td><td>9.23 (-13.62%)</td><td>2.09 (-9.25%)</td><td>454.30 (+15.77%)</td><td>341.48 (+10.07%)</td><td>329.30 (+17.78%)</td><td>286.10 (+10.38%)</td><td>66.34 (+18.62%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>16.18 (n/a)</td><td>13.85 (n/a)</td><td>15.00 (n/a)</td><td>10.69 (n/a)</td><td>2.30 (n/a)</td><td>392.40 (n/a)</td><td>310.24 (n/a)</td><td>279.60 (n/a)</td><td>259.20 (n/a)</td><td>55.93 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.09 (-9.57%)</td><td>2.56 (-1.62%)</td><td>2.57 (-1.54%)</td><td>2.06 (+6.60%)</td><td>0.37 <b>(-35.38%)</b></td><td>254.50 (-6.19%)</td><td>208.18 (-0.48%)</td><td>204.10 (+1.54%)</td><td>169.80 (+10.55%)</td><td>30.43 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.41 (n/a)</td><td>2.60 (n/a)</td><td>2.61 (n/a)</td><td>1.93 (n/a)</td><td>0.57 (n/a)</td><td>271.30 (n/a)</td><td>209.18 (n/a)</td><td>201.00 (n/a)</td><td>153.60 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.05 (-1.59%)</td><td>4.96 (-4.34%)</td><td>4.75 (-6.25%)</td><td>4.13 (-11.04%)</td><td>0.73 <b>(+28.11%)</b></td><td>254.00 (+12.39%)</td><td>215.10 (+5.36%)</td><td>220.60 (+6.67%)</td><td>173.20 (+1.58%)</td><td>30.54 <b>(+48.21%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>6.15 (n/a)</td><td>5.18 (n/a)</td><td>5.07 (n/a)</td><td>4.64 (n/a)</td><td>0.57 (n/a)</td><td>226.00 (n/a)</td><td>204.16 (n/a)</td><td>206.80 (n/a)</td><td>170.50 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.01 (-13.95%)</td><td>6.97 (-17.50%)</td><td>7.15 <b>(-20.79%)</b></td><td>5.38 <b>(-22.19%)</b></td><td>1.06 (+3.06%)</td><td>389.90 <b>(+28.51%)</b></td><td>307.02 <b>(+22.12%)</b></td><td>293.50 <b>(+26.24%)</b></td><td>261.80 (+16.20%)</td><td>51.68 <b>(+55.18%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>9.31 (n/a)</td><td>8.45 (n/a)</td><td>9.02 (n/a)</td><td>6.91 (n/a)</td><td>1.03 (n/a)</td><td>303.40 (n/a)</td><td>251.40 (n/a)</td><td>232.50 (n/a)</td><td>225.30 (n/a)</td><td>33.30 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.32 (-14.98%)</td><td>2.88 (-8.98%)</td><td>2.84 (-13.26%)</td><td>2.47 (+14.20%)</td><td>0.31 <b>(-59.20%)</b></td><td>212.20 (-12.46%)</td><td>183.92 (+5.41%)</td><td>184.70 (+15.29%)</td><td>157.80 (+17.59%)</td><td>19.48 <b>(-57.31%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>3.91 (n/a)</td><td>3.16 (n/a)</td><td>3.27 (n/a)</td><td>2.16 (n/a)</td><td>0.75 (n/a)</td><td>242.40 (n/a)</td><td>174.48 (n/a)</td><td>160.20 (n/a)</td><td>134.20 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (+10.07%)</td><td>0.22 (+3.31%)</td><td>0.21 (-0.50%)</td><td>0.18 <b>(+25.01%)</b></td><td>0.04 (-7.59%)</td><td>184.00 <b>(-20.03%)</b></td><td>154.14 (-4.79%)</td><td>155.20 (+0.52%)</td><td>116.20 (-9.15%)</td><td>24.66 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.10 (n/a)</td><td>161.90 (n/a)</td><td>154.40 (n/a)</td><td>127.90 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (+4.45%)</td><td>0.22 (-4.66%)</td><td>0.19 (-16.45%)</td><td>0.14 (-12.68%)</td><td>0.07 <b>(+52.30%)</b></td><td>232.90 (+14.50%)</td><td>164.58 (+9.79%)</td><td>175.60 (+19.70%)</td><td>111.50 (-4.21%)</td><td>51.22 <b>(+54.50%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.40 (n/a)</td><td>149.90 (n/a)</td><td>146.70 (n/a)</td><td>116.40 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.59 (+2.50%)</td><td>0.48 (+3.77%)</td><td>0.50 (-1.93%)</td><td>0.38 (+12.56%)</td><td>0.09 (-7.45%)</td><td>173.90 (-11.18%)</td><td>139.38 (-4.64%)</td><td>131.50 (+2.02%)</td><td>111.20 (-2.37%)</td><td>27.73 (-19.86%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>195.80 (n/a)</td><td>146.16 (n/a)</td><td>128.90 (n/a)</td><td>113.90 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.44 (-18.52%)</td><td>0.39 (-9.52%)</td><td>0.38 (-11.73%)</td><td>0.34 (+4.53%)</td><td>0.05 <b>(-53.63%)</b></td><td>194.90 (-4.32%)</td><td>171.44 (+6.39%)</td><td>173.30 (+13.34%)</td><td>147.70 <b>(+22.78%)</b></td><td>21.52 <b>(-47.07%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>203.70 (n/a)</td><td>161.14 (n/a)</td><td>152.90 (n/a)</td><td>120.30 (n/a)</td><td>40.65 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.46 (-16.76%)</td><td>0.36 (-14.83%)</td><td>0.35 (-10.48%)</td><td>0.29 (-19.18%)</td><td>0.06 (-17.63%)</td><td>222.60 <b>(+23.74%)</b></td><td>187.44 (+17.43%)</td><td>188.70 (+11.72%)</td><td>143.40 <b>(+20.10%)</b></td><td>29.21 <b>(+23.35%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>179.90 (n/a)</td><td>159.62 (n/a)</td><td>168.90 (n/a)</td><td>119.40 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.17 <b>(+38.88%)</b></td><td>0.83 (+5.89%)</td><td>0.87 (+5.83%)</td><td>0.40 <b>(-39.12%)</b></td><td>0.29 <b>(+272.20%)</b></td><td>327.40 <b>(+64.27%)</b></td><td>179.84 (+7.15%)</td><td>151.00 (-5.51%)</td><td>111.60 <b>(-28.00%)</b></td><td>85.80 <b>(+365.57%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.82 (n/a)</td><td>0.66 (n/a)</td><td>0.08 (n/a)</td><td>199.30 (n/a)</td><td>167.84 (n/a)</td><td>159.80 (n/a)</td><td>155.00 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.01 (-1.88%)</td><td>0.83 (+2.22%)</td><td>0.85 (+18.78%)</td><td>0.65 (-0.13%)</td><td>0.13 <b>(-29.82%)</b></td><td>201.20 (+0.15%)</td><td>160.48 (-3.94%)</td><td>154.50 (-15.80%)</td><td>130.40 (+1.95%)</td><td>26.14 <b>(-25.66%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>1.02 (n/a)</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.18 (n/a)</td><td>200.90 (n/a)</td><td>167.06 (n/a)</td><td>183.50 (n/a)</td><td>127.90 (n/a)</td><td>35.16 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.00 (+12.25%)</td><td>0.81 (+12.07%)</td><td>0.80 (+16.27%)</td><td>0.65 (+14.89%)</td><td>0.14 (+10.19%)</td><td>200.80 (-12.96%)</td><td>165.84 (-10.90%)</td><td>164.20 (-14.03%)</td><td>130.50 (-10.92%)</td><td>27.09 (-14.22%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.89 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.57 (n/a)</td><td>0.12 (n/a)</td><td>230.70 (n/a)</td><td>186.12 (n/a)</td><td>191.00 (n/a)</td><td>146.50 (n/a)</td><td>31.58 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (-18.15%)</td><td>0.59 (-12.95%)</td><td>0.63 (-2.36%)</td><td>0.43 (-15.32%)</td><td>0.15 (-15.07%)</td><td>303.50 (+18.09%)</td><td>234.10 (+15.51%)</td><td>207.10 (+2.42%)</td><td>165.10 <b>(+22.21%)</b></td><td>62.37 <b>(+29.80%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.97 (n/a)</td><td>0.68 (n/a)</td><td>0.65 (n/a)</td><td>0.51 (n/a)</td><td>0.18 (n/a)</td><td>257.00 (n/a)</td><td>202.66 (n/a)</td><td>202.20 (n/a)</td><td>135.10 (n/a)</td><td>48.05 (n/a)</td>
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
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (-18.20%)</td><td>0.11 (-12.23%)</td><td>0.13 (+4.55%)</td><td>0.05 <b>(-42.45%)</b></td><td>0.03 <b>(+28.22%)</b></td><td>320.80 <b>(+73.78%)</b></td><td>172.30 <b>(+24.80%)</b></td><td>129.40 (-4.36%)</td><td>124.90 <b>(+22.33%)</b></td><td>84.35 <b>(+173.23%)</b></td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:29:21</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>138.06 (n/a)</td><td>135.30 (n/a)</td><td>102.10 (n/a)</td><td>30.87 (n/a)</td>
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
