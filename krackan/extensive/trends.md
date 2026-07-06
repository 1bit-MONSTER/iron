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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+3.54%)</td><td>0.04 (+8.47%)</td><td>0.04 (+2.53%)</td><td>0.04 <b>(+41.79%)</b></td><td>0.01 <b>(-44.57%)</b></td><td>166.60 <b>(-29.47%)</b></td><td>150.94 (-12.31%)</td><td>153.70 (-2.47%)</td><td>119.90 (-3.38%)</td><td>18.22 <b>(-63.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>172.12 (n/a)</td><td>157.60 (n/a)</td><td>124.10 (n/a)</td><td>49.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (-7.14%)</td><td>0.04 (-2.71%)</td><td>0.04 (+3.07%)</td><td>0.04 (-0.31%)</td><td>0.00 <b>(-23.47%)</b></td><td>170.40 (+0.35%)</td><td>149.36 (+2.30%)</td><td>142.90 (-2.99%)</td><td>134.40 (+7.69%)</td><td>15.88 (-16.40%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>169.80 (n/a)</td><td>146.00 (n/a)</td><td>147.30 (n/a)</td><td>124.80 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+12.24%)</td><td>0.05 <b>(+41.20%)</b></td><td>0.05 <b>(+61.24%)</b></td><td>0.04 <b>(+49.02%)</b></td><td>0.01 <b>(-22.55%)</b></td><td>162.30 <b>(-32.91%)</b></td><td>126.24 <b>(-31.14%)</b></td><td>119.80 <b>(-37.99%)</b></td><td>114.10 (-10.93%)</td><td>20.35 <b>(-52.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>183.34 (n/a)</td><td>193.20 (n/a)</td><td>128.10 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+23.93%)</b></td><td>0.04 (+18.96%)</td><td>0.04 <b>(+34.39%)</b></td><td>0.02 <b>(-38.52%)</b></td><td>0.02 <b>(+83.20%)</b></td><td>378.70 <b>(+62.60%)</b></td><td>184.00 (-2.04%)</td><td>147.80 <b>(-25.62%)</b></td><td>101.60 (-19.30%)</td><td>111.22 <b>(+170.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>187.84 (n/a)</td><td>198.70 (n/a)</td><td>125.90 (n/a)</td><td>41.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+20.01%)</b></td><td>0.04 (+15.08%)</td><td>0.05 <b>(+33.77%)</b></td><td>0.03 (+1.55%)</td><td>0.01 <b>(+67.92%)</b></td><td>213.60 (-1.52%)</td><td>157.66 (-9.10%)</td><td>132.50 <b>(-25.23%)</b></td><td>105.10 (-16.65%)</td><td>48.68 <b>(+49.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>173.44 (n/a)</td><td>177.20 (n/a)</td><td>126.10 (n/a)</td><td>32.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+18.02%)</td><td>0.05 <b>(+22.62%)</b></td><td>0.05 <b>(+28.96%)</b></td><td>0.04 <b>(+21.12%)</b></td><td>0.01 <b>(+22.98%)</b></td><td>163.40 (-17.43%)</td><td>135.66 (-18.36%)</td><td>130.60 <b>(-22.45%)</b></td><td>116.00 (-15.20%)</td><td>19.60 (-13.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>166.16 (n/a)</td><td>168.40 (n/a)</td><td>136.80 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+25.91%)</b></td><td>0.05 <b>(+30.31%)</b></td><td>0.05 <b>(+49.01%)</b></td><td>0.03 <b>(+24.70%)</b></td><td>0.01 <b>(+62.70%)</b></td><td>182.70 (-19.80%)</td><td>136.70 <b>(-20.90%)</b></td><td>113.00 <b>(-32.86%)</b></td><td>98.50 <b>(-20.56%)</b></td><td>40.86 (+9.64%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>172.82 (n/a)</td><td>168.30 (n/a)</td><td>124.00 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+31.81%)</b></td><td>0.03 (+2.44%)</td><td>0.04 <b>(+30.25%)</b></td><td>0.01 <b>(-75.83%)</b></td><td>0.03 <b>(+260.29%)</b></td><td>1023.90 <b>(+313.70%)</b></td><td>474.14 <b>(+142.97%)</b></td><td>150.20 <b>(-23.25%)</b></td><td>106.40 <b>(-24.16%)</b></td><td>482.83 <b>(+1111.84%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>247.50 (n/a)</td><td>195.14 (n/a)</td><td>195.70 (n/a)</td><td>140.30 (n/a)</td><td>39.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (+12.04%)</td><td>0.10 <b>(+24.44%)</b></td><td>0.10 <b>(+23.29%)</b></td><td>0.09 <b>(+45.89%)</b></td><td>0.01 <b>(-43.98%)</b></td><td>133.60 <b>(-31.45%)</b></td><td>122.74 <b>(-20.89%)</b></td><td>121.50 (-18.84%)</td><td>112.70 (-10.77%)</td><td>8.43 <b>(-66.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>155.16 (n/a)</td><td>149.70 (n/a)</td><td>126.30 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 <b>(+57.78%)</b></td><td>0.11 <b>(+42.46%)</b></td><td>0.11 <b>(+35.98%)</b></td><td>0.09 <b>(+38.06%)</b></td><td>0.02 <b>(+92.23%)</b></td><td>131.90 <b>(-27.57%)</b></td><td>114.00 <b>(-29.35%)</b></td><td>114.70 <b>(-26.47%)</b></td><td>90.50 <b>(-36.58%)</b></td><td>15.48 (-14.32%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>161.36 (n/a)</td><td>156.00 (n/a)</td><td>142.70 (n/a)</td><td>18.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+28.71%)</b></td><td>0.10 <b>(+36.77%)</b></td><td>0.11 <b>(+32.65%)</b></td><td>0.07 <b>(+39.14%)</b></td><td>0.02 (+6.16%)</td><td>166.40 <b>(-28.12%)</b></td><td>122.22 <b>(-28.28%)</b></td><td>116.00 <b>(-24.63%)</b></td><td>99.50 <b>(-22.27%)</b></td><td>27.00 <b>(-40.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>170.42 (n/a)</td><td>153.90 (n/a)</td><td>128.00 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 <b>(+35.77%)</b></td><td>0.11 <b>(+45.71%)</b></td><td>0.10 <b>(+43.31%)</b></td><td>0.09 <b>(+71.37%)</b></td><td>0.02 (+10.64%)</td><td>135.80 <b>(-41.64%)</b></td><td>116.04 <b>(-32.99%)</b></td><td>122.60 <b>(-30.22%)</b></td><td>83.30 <b>(-26.35%)</b></td><td>20.36 <b>(-52.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>173.18 (n/a)</td><td>175.70 (n/a)</td><td>113.10 (n/a)</td><td>42.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+27.84%)</b></td><td>0.11 <b>(+30.59%)</b></td><td>0.12 <b>(+33.44%)</b></td><td>0.07 (+14.11%)</td><td>0.02 <b>(+44.90%)</b></td><td>171.60 (-12.36%)</td><td>121.84 <b>(-22.53%)</b></td><td>106.00 <b>(-25.09%)</b></td><td>100.60 <b>(-21.77%)</b></td><td>30.10 (-2.46%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>157.28 (n/a)</td><td>141.50 (n/a)</td><td>128.60 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+27.42%)</b></td><td>0.10 <b>(+27.93%)</b></td><td>0.10 <b>(+40.53%)</b></td><td>0.08 <b>(+50.69%)</b></td><td>0.02 (-6.69%)</td><td>154.40 <b>(-33.65%)</b></td><td>130.10 <b>(-23.75%)</b></td><td>126.90 <b>(-28.83%)</b></td><td>101.10 <b>(-21.51%)</b></td><td>22.08 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>170.62 (n/a)</td><td>178.30 (n/a)</td><td>128.80 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+40.91%)</b></td><td>0.06 (-8.03%)</td><td>0.06 (-5.57%)</td><td>0.01 <b>(-78.94%)</b></td><td>0.04 <b>(+225.70%)</b></td><td>1024.00 <b>(+374.73%)</b></td><td>344.70 <b>(+88.48%)</b></td><td>191.70 (+5.91%)</td><td>105.50 <b>(-29.05%)</b></td><td>382.11 <b>(+1167.10%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>182.88 (n/a)</td><td>181.00 (n/a)</td><td>148.70 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+33.28%)</b></td><td>0.09 <b>(+36.52%)</b></td><td>0.07 (+17.62%)</td><td>0.07 <b>(+72.86%)</b></td><td>0.03 <b>(+34.34%)</b></td><td>182.40 <b>(-42.13%)</b></td><td>148.96 <b>(-27.75%)</b></td><td>167.50 (-15.02%)</td><td>99.60 <b>(-25.00%)</b></td><td>38.76 <b>(-41.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>315.20 (n/a)</td><td>206.16 (n/a)</td><td>197.10 (n/a)</td><td>132.80 (n/a)</td><td>66.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (-3.29%)</td><td>0.18 (+0.65%)</td><td>0.18 (-2.00%)</td><td>0.15 (+7.61%)</td><td>0.02 <b>(-25.38%)</b></td><td>169.10 (-7.09%)</td><td>139.40 (-1.93%)</td><td>137.20 (+2.08%)</td><td>116.50 (+3.37%)</td><td>19.66 <b>(-28.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>182.00 (n/a)</td><td>142.14 (n/a)</td><td>134.40 (n/a)</td><td>112.70 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (+19.11%)</td><td>0.17 (-1.77%)</td><td>0.15 (-17.36%)</td><td>0.12 (-5.03%)</td><td>0.05 <b>(+48.95%)</b></td><td>209.10 (+5.29%)</td><td>153.76 (+4.94%)</td><td>161.50 <b>(+21.06%)</b></td><td>96.60 (-16.07%)</td><td>42.04 <b>(+26.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>198.60 (n/a)</td><td>146.52 (n/a)</td><td>133.40 (n/a)</td><td>115.10 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 <b>(+25.27%)</b></td><td>0.19 (+8.57%)</td><td>0.19 (+1.65%)</td><td>0.16 (+7.67%)</td><td>0.03 <b>(+66.00%)</b></td><td>155.00 (-7.13%)</td><td>128.86 (-6.96%)</td><td>129.80 (-1.59%)</td><td>99.30 <b>(-20.11%)</b></td><td>19.93 (+18.09%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>166.90 (n/a)</td><td>138.50 (n/a)</td><td>131.90 (n/a)</td><td>124.30 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 <b>(+28.74%)</b></td><td>0.17 (+3.51%)</td><td>0.16 (-6.28%)</td><td>0.05 <b>(-63.52%)</b></td><td>0.08 <b>(+201.01%)</b></td><td>523.50 <b>(+174.23%)</b></td><td>208.12 <b>(+36.49%)</b></td><td>158.50 (+6.73%)</td><td>97.20 <b>(-22.30%)</b></td><td>179.05 <b>(+560.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>190.90 (n/a)</td><td>152.48 (n/a)</td><td>148.50 (n/a)</td><td>125.10 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 <b>(+39.15%)</b></td><td>0.18 (+6.68%)</td><td>0.17 (-3.20%)</td><td>0.13 (-7.18%)</td><td>0.05 <b>(+157.19%)</b></td><td>194.80 (+7.74%)</td><td>145.78 (-1.30%)</td><td>147.30 (+3.30%)</td><td>94.60 <b>(-28.17%)</b></td><td>39.67 <b>(+97.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>147.70 (n/a)</td><td>142.60 (n/a)</td><td>131.70 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 <b>(+53.28%)</b></td><td>0.23 <b>(+48.85%)</b></td><td>0.23 <b>(+42.18%)</b></td><td>0.20 <b>(+47.00%)</b></td><td>0.03 <b>(+82.97%)</b></td><td>123.70 <b>(-32.00%)</b></td><td>106.94 <b>(-32.55%)</b></td><td>109.20 <b>(-29.64%)</b></td><td>93.30 <b>(-34.76%)</b></td><td>13.48 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.90 (n/a)</td><td>158.54 (n/a)</td><td>155.20 (n/a)</td><td>143.00 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 <b>(+36.25%)</b></td><td>0.17 (+8.42%)</td><td>0.16 (+3.72%)</td><td>0.11 (-15.60%)</td><td>0.06 <b>(+131.95%)</b></td><td>216.00 (+18.49%)</td><td>153.02 (-2.02%)</td><td>149.10 (-3.56%)</td><td>94.20 <b>(-26.58%)</b></td><td>46.20 <b>(+97.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>156.18 (n/a)</td><td>154.60 (n/a)</td><td>128.30 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 <b>(+42.74%)</b></td><td>0.19 <b>(+26.52%)</b></td><td>0.19 <b>(+21.11%)</b></td><td>0.14 <b>(+22.47%)</b></td><td>0.04 <b>(+70.50%)</b></td><td>173.50 (-18.31%)</td><td>130.58 (-19.98%)</td><td>128.00 (-17.47%)</td><td>98.10 <b>(-29.93%)</b></td><td>27.40 (-4.07%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>163.18 (n/a)</td><td>155.10 (n/a)</td><td>140.00 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.40 (+3.09%)</td><td>0.34 (+4.03%)</td><td>0.33 (-6.16%)</td><td>0.28 <b>(+47.78%)</b></td><td>0.05 <b>(-37.60%)</b></td><td>172.90 <b>(-32.33%)</b></td><td>145.54 (-8.65%)</td><td>147.40 (+6.50%)</td><td>123.70 (-2.98%)</td><td>21.20 <b>(-61.02%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>255.50 (n/a)</td><td>159.32 (n/a)</td><td>138.40 (n/a)</td><td>127.50 (n/a)</td><td>54.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 <b>(+21.01%)</b></td><td>0.43 <b>(+27.66%)</b></td><td>0.47 <b>(+39.77%)</b></td><td>0.29 (+17.60%)</td><td>0.09 <b>(+35.36%)</b></td><td>167.80 (-14.95%)</td><td>118.60 <b>(-20.94%)</b></td><td>104.40 <b>(-28.44%)</b></td><td>97.50 (-17.37%)</td><td>29.23 (-4.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>197.30 (n/a)</td><td>150.02 (n/a)</td><td>145.90 (n/a)</td><td>118.00 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 <b>(+22.81%)</b></td><td>0.42 <b>(+21.17%)</b></td><td>0.39 (+2.98%)</td><td>0.35 <b>(+27.53%)</b></td><td>0.07 (+15.30%)</td><td>140.40 <b>(-21.56%)</b></td><td>119.34 (-17.82%)</td><td>126.80 (-2.91%)</td><td>97.70 (-18.58%)</td><td>18.63 <b>(-28.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>179.00 (n/a)</td><td>145.22 (n/a)</td><td>130.60 (n/a)</td><td>120.00 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.51 <b>(+30.31%)</b></td><td>0.42 <b>(+31.16%)</b></td><td>0.41 <b>(+40.73%)</b></td><td>0.30 (+10.60%)</td><td>0.09 <b>(+59.41%)</b></td><td>164.10 (-9.59%)</td><td>121.04 <b>(-22.54%)</b></td><td>120.50 <b>(-28.95%)</b></td><td>95.80 <b>(-23.30%)</b></td><td>27.91 (+8.70%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>181.50 (n/a)</td><td>156.26 (n/a)</td><td>169.60 (n/a)</td><td>124.90 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.44 (+18.64%)</td><td>0.39 <b>(+36.29%)</b></td><td>0.40 (+16.08%)</td><td>0.34 <b>(+100.95%)</b></td><td>0.04 <b>(-59.29%)</b></td><td>146.50 <b>(-50.22%)</b></td><td>125.82 <b>(-33.60%)</b></td><td>123.40 (-13.89%)</td><td>110.60 (-15.70%)</td><td>13.05 <b>(-82.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>294.30 (n/a)</td><td>189.48 (n/a)</td><td>143.30 (n/a)</td><td>131.20 (n/a)</td><td>73.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.54 <b>(+48.32%)</b></td><td>0.37 <b>(+20.13%)</b></td><td>0.37 <b>(+26.88%)</b></td><td>0.24 (-18.07%)</td><td>0.12 <b>(+258.58%)</b></td><td>208.90 <b>(+22.02%)</b></td><td>143.88 (-10.41%)</td><td>131.80 <b>(-21.17%)</b></td><td>90.70 <b>(-32.57%)</b></td><td>45.83 <b>(+199.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>171.20 (n/a)</td><td>160.60 (n/a)</td><td>167.20 (n/a)</td><td>134.50 (n/a)</td><td>15.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.50 <b>(+58.93%)</b></td><td>0.36 <b>(+42.86%)</b></td><td>0.29 (+9.77%)</td><td>0.25 <b>(+61.22%)</b></td><td>0.13 <b>(+93.18%)</b></td><td>198.70 <b>(-37.96%)</b></td><td>148.76 <b>(-28.32%)</b></td><td>171.80 (-8.91%)</td><td>98.00 <b>(-37.10%)</b></td><td>46.80 <b>(-29.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>320.30 (n/a)</td><td>207.52 (n/a)</td><td>188.60 (n/a)</td><td>155.80 (n/a)</td><td>66.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.46 (+18.37%)</td><td>0.36 <b>(+28.89%)</b></td><td>0.40 <b>(+62.74%)</b></td><td>0.22 (+12.89%)</td><td>0.10 (+13.41%)</td><td>222.00 (-11.41%)</td><td>146.20 <b>(-22.56%)</b></td><td>124.10 <b>(-38.56%)</b></td><td>107.20 (-15.52%)</td><td>48.40 (-13.58%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>250.60 (n/a)</td><td>188.80 (n/a)</td><td>202.00 (n/a)</td><td>126.90 (n/a)</td><td>56.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+43.90%)</b></td><td>0.02 <b>(+21.68%)</b></td><td>0.02 (+18.20%)</td><td>0.01 <b>(-32.54%)</b></td><td>0.01 <b>(+283.81%)</b></td><td>217.20 <b>(+48.26%)</b></td><td>125.56 (-6.97%)</td><td>118.00 (-15.41%)</td><td>77.10 <b>(-30.48%)</b></td><td>55.90 <b>(+303.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>146.50 (n/a)</td><td>134.96 (n/a)</td><td>139.50 (n/a)</td><td>110.90 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+12.53%)</td><td>0.02 (-6.25%)</td><td>0.02 (+4.00%)</td><td>0.00 <b>(-94.64%)</b></td><td>0.01 <b>(+200.32%)</b></td><td>2878.60 <b>(+1764.38%)</b></td><td>668.68 <b>(+408.66%)</b></td><td>128.60 (-3.89%)</td><td>86.40 (-11.20%)</td><td>1235.66 <b>(+5793.23%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>154.40 (n/a)</td><td>131.46 (n/a)</td><td>133.80 (n/a)</td><td>97.30 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+61.11%)</b></td><td>0.02 <b>(+43.62%)</b></td><td>0.03 <b>(+49.92%)</b></td><td>0.01 <b>(-28.07%)</b></td><td>0.01 <b>(+220.65%)</b></td><td>257.00 <b>(+38.99%)</b></td><td>125.92 (-19.02%)</td><td>96.50 <b>(-33.31%)</b></td><td>81.50 <b>(-37.93%)</b></td><td>73.60 <b>(+198.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>184.90 (n/a)</td><td>155.50 (n/a)</td><td>144.70 (n/a)</td><td>131.30 (n/a)</td><td>24.69 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (-10.17%)</td><td>0.01 (-18.81%)</td><td>0.01 (-19.64%)</td><td>0.01 <b>(-35.11%)</b></td><td>0.00 <b>(+127.35%)</b></td><td>265.10 <b>(+54.13%)</b></td><td>198.56 <b>(+27.28%)</b></td><td>192.70 <b>(+24.40%)</b></td><td>156.80 (+11.28%)</td><td>44.37 <b>(+283.58%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>156.00 (n/a)</td><td>154.90 (n/a)</td><td>140.90 (n/a)</td><td>11.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+18.53%)</td><td>0.02 (-4.93%)</td><td>0.02 (+5.50%)</td><td>0.00 <b>(-85.94%)</b></td><td>0.01 <b>(+149.34%)</b></td><td>1434.60 <b>(+611.25%)</b></td><td>404.52 <b>(+140.04%)</b></td><td>160.90 (-5.24%)</td><td>101.90 (-15.65%)</td><td>576.54 <b>(+1702.85%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>168.52 (n/a)</td><td>169.80 (n/a)</td><td>120.80 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 <b>(+47.53%)</b></td><td>0.02 (+14.03%)</td><td>0.02 (+4.76%)</td><td>0.01 (-1.66%)</td><td>0.01 <b>(+173.29%)</b></td><td>229.90 (+1.68%)</td><td>173.34 (-6.63%)</td><td>167.70 (-4.55%)</td><td>108.00 <b>(-32.20%)</b></td><td>51.76 <b>(+92.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>226.10 (n/a)</td><td>185.64 (n/a)</td><td>175.70 (n/a)</td><td>159.30 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+7.96%)</td><td>0.01 <b>(-21.60%)</b></td><td>0.01 (-9.69%)</td><td>0.00 <b>(-99.58%)</b></td><td>0.01 <b>(+142.98%)</b></td><td>48658.20 <b>(+23717.03%)</b></td><td>15414.24 <b>(+9001.46%)</b></td><td>198.40 (+10.71%)</td><td>95.00 (-7.41%)</td><td>22159.76 <b>(+52264.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>169.36 (n/a)</td><td>179.20 (n/a)</td><td>102.60 (n/a)</td><td>42.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 <b>(+48.56%)</b></td><td>0.02 <b>(+21.49%)</b></td><td>0.01 <b>(+24.09%)</b></td><td>0.01 (-9.04%)</td><td>0.00 <b>(+180.90%)</b></td><td>256.20 (+9.96%)</td><td>181.14 (-13.87%)</td><td>178.90 (-19.41%)</td><td>122.00 <b>(-32.71%)</b></td><td>48.26 <b>(+109.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>210.30 (n/a)</td><td>222.00 (n/a)</td><td>181.30 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+79.68%)</b></td><td>0.04 (+19.09%)</td><td>0.04 <b>(+29.19%)</b></td><td>0.00 <b>(-99.85%)</b></td><td>0.02 <b>(+849.53%)</b></td><td>130045.60 <b>(+64955.33%)</b></td><td>26108.38 <b>(+14734.31%)</b></td><td>134.00 <b>(-22.59%)</b></td><td>89.00 <b>(-44.38%)</b></td><td>58102.68 <b>(+398246.84%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>176.00 (n/a)</td><td>173.10 (n/a)</td><td>160.00 (n/a)</td><td>14.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 <b>(+35.81%)</b></td><td>0.04 <b>(+20.86%)</b></td><td>0.04 <b>(+39.51%)</b></td><td>0.03 (-7.21%)</td><td>0.01 <b>(+298.70%)</b></td><td>206.80 (+7.76%)</td><td>150.56 (-11.86%)</td><td>121.30 <b>(-28.31%)</b></td><td>111.80 <b>(-26.35%)</b></td><td>45.65 <b>(+219.76%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>170.82 (n/a)</td><td>169.20 (n/a)</td><td>151.80 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+22.10%)</b></td><td>0.04 (+11.13%)</td><td>0.04 <b>(+42.07%)</b></td><td>0.00 <b>(-99.85%)</b></td><td>0.02 <b>(+191.67%)</b></td><td>133788.90 <b>(+66894.94%)</b></td><td>26854.94 <b>(+16052.38%)</b></td><td>126.20 <b>(-29.58%)</b></td><td>93.80 (-18.15%)</td><td>59777.91 <b>(+182839.87%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>166.26 (n/a)</td><td>179.20 (n/a)</td><td>114.60 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (+13.62%)</td><td>0.03 (+13.99%)</td><td>0.04 <b>(+39.97%)</b></td><td>0.02 (-3.59%)</td><td>0.01 <b>(+28.46%)</b></td><td>240.60 (+3.75%)</td><td>175.22 (-10.84%)</td><td>148.90 <b>(-28.55%)</b></td><td>135.80 (-12.05%)</td><td>45.38 (+18.21%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>196.52 (n/a)</td><td>208.40 (n/a)</td><td>154.40 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 <b>(+67.97%)</b></td><td>0.03 (+3.60%)</td><td>0.03 (+11.26%)</td><td>0.00 <b>(-95.03%)</b></td><td>0.02 <b>(+924.81%)</b></td><td>4033.50 <b>(+1910.72%)</b></td><td>934.30 <b>(+400.59%)</b></td><td>170.50 (-10.12%)</td><td>101.50 <b>(-40.47%)</b></td><td>1733.23 <b>(+14247.81%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.60 (n/a)</td><td>186.64 (n/a)</td><td>189.70 (n/a)</td><td>170.50 (n/a)</td><td>12.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+30.11%)</b></td><td>0.03 (-2.78%)</td><td>0.03 (+15.41%)</td><td>0.00 <b>(-98.82%)</b></td><td>0.02 <b>(+614.30%)</b></td><td>16505.40 <b>(+8407.94%)</b></td><td>3421.74 <b>(+1803.08%)</b></td><td>160.40 (-13.34%)</td><td>122.30 <b>(-23.18%)</b></td><td>7314.02 <b>(+53843.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.00 (n/a)</td><td>179.80 (n/a)</td><td>185.10 (n/a)</td><td>159.20 (n/a)</td><td>13.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (+15.02%)</td><td>0.02 <b>(-32.16%)</b></td><td>0.03 (-1.78%)</td><td>0.00 <b>(-93.95%)</b></td><td>0.02 <b>(+256.09%)</b></td><td>3708.70 <b>(+1554.19%)</b></td><td>1527.38 <b>(+704.48%)</b></td><td>194.90 (+1.83%)</td><td>135.70 (-13.01%)</td><td>1856.03 <b>(+5824.15%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.20 (n/a)</td><td>189.86 (n/a)</td><td>191.40 (n/a)</td><td>156.00 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+28.30%)</b></td><td>0.02 (-7.69%)</td><td>0.02 (-2.69%)</td><td>0.00 <b>(-99.49%)</b></td><td>0.01 <b>(+263.62%)</b></td><td>50736.30 <b>(+19680.23%)</b></td><td>10314.66 <b>(+4365.61%)</b></td><td>249.30 (+2.76%)</td><td>137.70 <b>(-22.07%)</b></td><td>22596.43 <b>(+69721.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.50 (n/a)</td><td>230.98 (n/a)</td><td>242.60 (n/a)</td><td>176.70 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 <b>(+25.64%)</b></td><td>0.06 (-13.00%)</td><td>0.06 (+4.31%)</td><td>0.01 <b>(-85.47%)</b></td><td>0.05 <b>(+260.62%)</b></td><td>1355.30 <b>(+588.32%)</b></td><td>569.86 <b>(+240.09%)</b></td><td>166.90 (-4.14%)</td><td>98.50 <b>(-20.37%)</b></td><td>614.38 <b>(+1973.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>167.56 (n/a)</td><td>174.10 (n/a)</td><td>123.70 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 <b>(+58.32%)</b></td><td>0.07 (+5.22%)</td><td>0.08 <b>(+29.61%)</b></td><td>0.00 <b>(-91.83%)</b></td><td>0.06 <b>(+299.37%)</b></td><td>2717.10 <b>(+1124.47%)</b></td><td>855.16 <b>(+400.04%)</b></td><td>123.60 <b>(-22.85%)</b></td><td>78.40 <b>(-36.83%)</b></td><td>1155.26 <b>(+2865.98%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>171.02 (n/a)</td><td>160.20 (n/a)</td><td>124.10 (n/a)</td><td>38.95 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+44.75%)</b></td><td>0.08 (+14.07%)</td><td>0.08 <b>(+22.21%)</b></td><td>0.00 <b>(-99.66%)</b></td><td>0.05 <b>(+279.61%)</b></td><td>61448.00 <b>(+29700.19%)</b></td><td>12379.34 <b>(+7696.54%)</b></td><td>124.90 (-18.15%)</td><td>85.60 <b>(-30.91%)</b></td><td>27430.22 <b>(+89705.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>206.20 (n/a)</td><td>158.78 (n/a)</td><td>152.60 (n/a)</td><td>123.90 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 <b>(+38.52%)</b></td><td>0.06 (-5.53%)</td><td>0.06 (-8.55%)</td><td>0.00 <b>(-93.90%)</b></td><td>0.04 <b>(+347.25%)</b></td><td>3178.30 <b>(+1539.14%)</b></td><td>754.14 <b>(+363.12%)</b></td><td>182.50 (+9.35%)</td><td>99.20 <b>(-27.85%)</b></td><td>1355.71 <b>(+6073.83%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>162.84 (n/a)</td><td>166.90 (n/a)</td><td>137.50 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+40.15%)</b></td><td>0.09 <b>(+51.41%)</b></td><td>0.08 <b>(+30.64%)</b></td><td>0.07 <b>(+43.32%)</b></td><td>0.02 <b>(+61.12%)</b></td><td>145.00 <b>(-30.25%)</b></td><td>117.58 <b>(-33.32%)</b></td><td>132.60 <b>(-23.44%)</b></td><td>87.60 <b>(-28.61%)</b></td><td>26.81 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>176.34 (n/a)</td><td>173.20 (n/a)</td><td>122.70 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (+12.29%)</td><td>0.07 (+18.93%)</td><td>0.08 <b>(+46.47%)</b></td><td>0.00 <b>(-92.27%)</b></td><td>0.04 <b>(+83.34%)</b></td><td>4338.80 <b>(+1192.85%)</b></td><td>972.96 <b>(+366.96%)</b></td><td>137.30 <b>(-31.73%)</b></td><td>102.40 (-10.96%)</td><td>1881.79 <b>(+2248.55%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>335.60 (n/a)</td><td>208.36 (n/a)</td><td>201.10 (n/a)</td><td>115.00 (n/a)</td><td>80.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (+6.98%)</td><td>0.07 (+17.09%)</td><td>0.06 <b>(+22.87%)</b></td><td>0.05 (+4.63%)</td><td>0.02 (+6.53%)</td><td>218.50 (-4.42%)</td><td>164.36 (-14.35%)</td><td>166.60 (-18.65%)</td><td>107.20 (-6.54%)</td><td>44.68 (-0.33%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>228.60 (n/a)</td><td>191.90 (n/a)</td><td>204.80 (n/a)</td><td>114.70 (n/a)</td><td>44.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 <b>(+66.40%)</b></td><td>0.05 <b>(+31.40%)</b></td><td>0.06 <b>(+28.83%)</b></td><td>0.00 <b>(-90.62%)</b></td><td>0.03 <b>(+196.79%)</b></td><td>3886.40 <b>(+966.23%)</b></td><td>906.74 <b>(+235.26%)</b></td><td>176.90 <b>(-22.38%)</b></td><td>120.30 <b>(-39.91%)</b></td><td>1665.89 <b>(+2119.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>364.50 (n/a)</td><td>270.46 (n/a)</td><td>227.90 (n/a)</td><td>200.20 (n/a)</td><td>75.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 <b>(+82.34%)</b></td><td>0.17 <b>(+75.27%)</b></td><td>0.18 <b>(+91.67%)</b></td><td>0.09 (-1.76%)</td><td>0.05 <b>(+538.95%)</b></td><td>233.40 (+1.79%)</td><td>134.54 <b>(-37.64%)</b></td><td>115.10 <b>(-47.85%)</b></td><td>104.50 <b>(-45.14%)</b></td><td>55.52 <b>(+273.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>215.74 (n/a)</td><td>220.70 (n/a)</td><td>190.50 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 <b>(+39.08%)</b></td><td>0.14 <b>(+29.95%)</b></td><td>0.16 <b>(+51.70%)</b></td><td>0.06 <b>(-29.05%)</b></td><td>0.05 <b>(+201.20%)</b></td><td>327.80 <b>(+40.93%)</b></td><td>175.72 (-11.94%)</td><td>130.60 <b>(-34.11%)</b></td><td>113.00 <b>(-28.12%)</b></td><td>89.55 <b>(+212.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>199.54 (n/a)</td><td>198.20 (n/a)</td><td>157.20 (n/a)</td><td>28.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 <b>(+61.75%)</b></td><td>0.14 (+13.08%)</td><td>0.12 (+0.58%)</td><td>0.07 <b>(-29.29%)</b></td><td>0.06 <b>(+283.34%)</b></td><td>286.40 <b>(+41.43%)</b></td><td>175.32 (+1.41%)</td><td>178.20 (-0.61%)</td><td>88.90 <b>(-38.18%)</b></td><td>74.02 <b>(+232.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>172.88 (n/a)</td><td>179.30 (n/a)</td><td>143.80 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 <b>(+76.10%)</b></td><td>0.16 <b>(+39.46%)</b></td><td>0.16 <b>(+33.54%)</b></td><td>0.08 <b>(-22.39%)</b></td><td>0.05 <b>(+370.37%)</b></td><td>269.30 <b>(+28.85%)</b></td><td>150.78 (-19.72%)</td><td>133.60 <b>(-25.15%)</b></td><td>95.70 <b>(-43.20%)</b></td><td>68.29 <b>(+265.58%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>187.82 (n/a)</td><td>178.50 (n/a)</td><td>168.50 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 <b>(+41.62%)</b></td><td>0.16 <b>(+26.82%)</b></td><td>0.17 <b>(+30.27%)</b></td><td>0.12 (-1.26%)</td><td>0.03 <b>(+411.48%)</b></td><td>177.80 (+1.25%)</td><td>133.56 (-19.19%)</td><td>125.10 <b>(-23.25%)</b></td><td>112.00 <b>(-29.43%)</b></td><td>26.08 <b>(+276.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>175.60 (n/a)</td><td>165.28 (n/a)</td><td>163.00 (n/a)</td><td>158.70 (n/a)</td><td>6.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (+19.01%)</td><td>0.13 (-2.89%)</td><td>0.15 (+0.56%)</td><td>0.00 <b>(-97.91%)</b></td><td>0.08 <b>(+154.82%)</b></td><td>9890.20 <b>(+4675.57%)</b></td><td>2080.32 <b>(+1205.42%)</b></td><td>136.40 (-0.58%)</td><td>105.30 (-16.03%)</td><td>4365.88 <b>(+11615.78%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>207.10 (n/a)</td><td>159.36 (n/a)</td><td>137.20 (n/a)</td><td>125.40 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (+5.74%)</td><td>0.10 <b>(-28.05%)</b></td><td>0.11 <b>(-20.90%)</b></td><td>0.00 <b>(-99.88%)</b></td><td>0.06 <b>(+479.37%)</b></td><td>133797.50 <b>(+80891.22%)</b></td><td>26896.76 <b>(+17731.32%)</b></td><td>186.60 <b>(+26.42%)</b></td><td>130.60 (-5.43%)</td><td>59759.34 <b>(+527499.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>165.20 (n/a)</td><td>150.84 (n/a)</td><td>147.60 (n/a)</td><td>138.10 (n/a)</td><td>11.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 <b>(+68.37%)</b></td><td>0.11 (+8.08%)</td><td>0.12 (+11.18%)</td><td>0.00 <b>(-93.45%)</b></td><td>0.07 <b>(+226.45%)</b></td><td>5037.10 <b>(+1426.86%)</b></td><td>1140.02 <b>(+424.53%)</b></td><td>173.40 (-10.06%)</td><td>108.60 <b>(-40.62%)</b></td><td>2178.97 <b>(+3354.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>329.90 (n/a)</td><td>217.34 (n/a)</td><td>192.80 (n/a)</td><td>182.90 (n/a)</td><td>63.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2626.60 (n/a)</td><td>987.70 (n/a)</td><td>846.80 (n/a)</td><td>101.80 (n/a)</td><td>1012.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>5676.20 (n/a)</td><td>1536.98 (n/a)</td><td>220.90 (n/a)</td><td>133.50 (n/a)</td><td>2377.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1758.20 (n/a)</td><td>766.08 (n/a)</td><td>198.00 (n/a)</td><td>96.90 (n/a)</td><td>832.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1764.90 (n/a)</td><td>490.24 (n/a)</td><td>185.90 (n/a)</td><td>107.10 (n/a)</td><td>716.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>351.40 (n/a)</td><td>239.80 (n/a)</td><td>240.80 (n/a)</td><td>112.30 (n/a)</td><td>89.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2264.80 (n/a)</td><td>639.46 (n/a)</td><td>254.00 (n/a)</td><td>120.00 (n/a)</td><td>911.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>2519.40 (n/a)</td><td>674.00 (n/a)</td><td>206.60 (n/a)</td><td>179.10 (n/a)</td><td>1032.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>3008.10 (n/a)</td><td>786.80 (n/a)</td><td>243.30 (n/a)</td><td>195.30 (n/a)</td><td>1242.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2587.80 (n/a)</td><td>682.08 (n/a)</td><td>218.00 (n/a)</td><td>148.10 (n/a)</td><td>1066.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1478.20 (n/a)</td><td>459.04 (n/a)</td><td>221.30 (n/a)</td><td>154.10 (n/a)</td><td>570.69 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>1667.00 (n/a)</td><td>482.14 (n/a)</td><td>178.10 (n/a)</td><td>157.10 (n/a)</td><td>663.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>1952.20 (n/a)</td><td>562.72 (n/a)</td><td>239.60 (n/a)</td><td>141.70 (n/a)</td><td>777.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.32 (-9.72%)</td><td>0.26 (-11.73%)</td><td>0.30 (-2.99%)</td><td>0.04 <b>(-79.56%)</b></td><td>0.12 <b>(+102.82%)</b></td><td>1138.90 <b>(+389.01%)</b></td><td>355.60 <b>(+101.68%)</b></td><td>162.00 (+3.12%)</td><td>152.30 (+10.76%)</td><td>437.92 <b>(+1029.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>232.90 (n/a)</td><td>176.32 (n/a)</td><td>157.10 (n/a)</td><td>137.50 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>692.90 (n/a)</td><td>265.68 (n/a)</td><td>165.70 (n/a)</td><td>138.40 (n/a)</td><td>239.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.56 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.01 (n/a)</td><td>0.22 (n/a)</td><td>5448.00 (n/a)</td><td>1422.24 (n/a)</td><td>188.20 (n/a)</td><td>87.60 (n/a)</td><td>2296.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.45 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>3845.40 (n/a)</td><td>1344.36 (n/a)</td><td>245.80 (n/a)</td><td>109.60 (n/a)</td><td>1691.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>233.10 (n/a)</td><td>201.32 (n/a)</td><td>200.60 (n/a)</td><td>172.80 (n/a)</td><td>25.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>486.50 (n/a)</td><td>249.26 (n/a)</td><td>195.90 (n/a)</td><td>153.00 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>631.80 (n/a)</td><td>285.94 (n/a)</td><td>256.90 (n/a)</td><td>113.80 (n/a)</td><td>206.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>162.24 (n/a)</td><td>165.00 (n/a)</td><td>110.20 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>413.40 (n/a)</td><td>238.32 (n/a)</td><td>125.80 (n/a)</td><td>122.00 (n/a)</td><td>157.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>293.20 (n/a)</td><td>211.06 (n/a)</td><td>184.60 (n/a)</td><td>134.30 (n/a)</td><td>67.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>237.90 (n/a)</td><td>177.64 (n/a)</td><td>186.10 (n/a)</td><td>95.30 (n/a)</td><td>55.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2173.10 (n/a)</td><td>738.84 (n/a)</td><td>296.00 (n/a)</td><td>110.50 (n/a)</td><td>877.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>0.09 (n/a)</td><td>16225.20 (n/a)</td><td>3393.76 (n/a)</td><td>231.70 (n/a)</td><td>110.90 (n/a)</td><td>7173.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.15 (n/a)</td><td>0.00 (n/a)</td><td>0.07 (n/a)</td><td>16292.60 (n/a)</td><td>3400.52 (n/a)</td><td>167.70 (n/a)</td><td>154.80 (n/a)</td><td>7206.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.15 (n/a)</td><td>0.00 (n/a)</td><td>0.08 (n/a)</td><td>16380.00 (n/a)</td><td>3479.98 (n/a)</td><td>164.70 (n/a)</td><td>127.10 (n/a)</td><td>7213.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>0.07 (n/a)</td><td>16970.40 (n/a)</td><td>4070.82 (n/a)</td><td>239.50 (n/a)</td><td>181.20 (n/a)</td><td>7297.19 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.19 (n/a)</td><td>0.00 (n/a)</td><td>0.10 (n/a)</td><td>16260.50 (n/a)</td><td>4076.16 (n/a)</td><td>264.20 (n/a)</td><td>237.50 (n/a)</td><td>6944.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>258.30 (n/a)</td><td>206.32 (n/a)</td><td>221.30 (n/a)</td><td>150.60 (n/a)</td><td>50.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>284.30 (n/a)</td><td>237.94 (n/a)</td><td>253.10 (n/a)</td><td>193.20 (n/a)</td><td>42.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2292.10 (n/a)</td><td>584.90 (n/a)</td><td>159.90 (n/a)</td><td>98.00 (n/a)</td><td>955.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.60 (n/a)</td><td>190.60 (n/a)</td><td>215.70 (n/a)</td><td>80.60 (n/a)</td><td>75.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>801.30 (n/a)</td><td>330.34 (n/a)</td><td>256.40 (n/a)</td><td>105.00 (n/a)</td><td>270.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>180.46 (n/a)</td><td>179.70 (n/a)</td><td>124.10 (n/a)</td><td>37.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>172.56 (n/a)</td><td>164.80 (n/a)</td><td>124.10 (n/a)</td><td>45.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>200.78 (n/a)</td><td>213.80 (n/a)</td><td>110.20 (n/a)</td><td>53.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>14224.70 (n/a)</td><td>3095.32 (n/a)</td><td>223.60 (n/a)</td><td>124.20 (n/a)</td><td>6226.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.60 (n/a)</td><td>222.72 (n/a)</td><td>226.20 (n/a)</td><td>177.90 (n/a)</td><td>28.31 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.90 (n/a)</td><td>142.22 (n/a)</td><td>151.20 (n/a)</td><td>108.60 (n/a)</td><td>29.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>131680.20 (n/a)</td><td>26475.54 (n/a)</td><td>182.70 (n/a)</td><td>98.70 (n/a)</td><td>58811.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>168.08 (n/a)</td><td>177.20 (n/a)</td><td>120.70 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>220.30 (n/a)</td><td>151.78 (n/a)</td><td>125.10 (n/a)</td><td>96.60 (n/a)</td><td>54.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>636.00 (n/a)</td><td>243.12 (n/a)</td><td>132.70 (n/a)</td><td>96.30 (n/a)</td><td>224.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.10 (n/a)</td><td>299.48 (n/a)</td><td>203.40 (n/a)</td><td>161.90 (n/a)</td><td>205.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.40 (n/a)</td><td>215.26 (n/a)</td><td>219.90 (n/a)</td><td>157.90 (n/a)</td><td>47.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>133057.40 (n/a)</td><td>27202.74 (n/a)</td><td>1211.10 (n/a)</td><td>186.40 (n/a)</td><td>59176.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.90 (n/a)</td><td>225.44 (n/a)</td><td>236.70 (n/a)</td><td>156.10 (n/a)</td><td>39.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>230.30 (n/a)</td><td>180.60 (n/a)</td><td>175.40 (n/a)</td><td>101.40 (n/a)</td><td>53.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>433.60 (n/a)</td><td>220.32 (n/a)</td><td>180.50 (n/a)</td><td>103.90 (n/a)</td><td>135.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1010.50 (n/a)</td><td>475.20 (n/a)</td><td>209.00 (n/a)</td><td>100.70 (n/a)</td><td>429.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>568.10 (n/a)</td><td>329.36 (n/a)</td><td>242.70 (n/a)</td><td>129.20 (n/a)</td><td>191.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>861.40 (n/a)</td><td>344.00 (n/a)</td><td>215.50 (n/a)</td><td>143.70 (n/a)</td><td>295.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>303.20 (n/a)</td><td>197.50 (n/a)</td><td>196.30 (n/a)</td><td>120.30 (n/a)</td><td>67.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.04 (n/a)</td><td>4204.50 (n/a)</td><td>1409.74 (n/a)</td><td>1175.60 (n/a)</td><td>195.20 (n/a)</td><td>1638.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.10 (n/a)</td><td>3357.60 (n/a)</td><td>796.12 (n/a)</td><td>170.80 (n/a)</td><td>123.20 (n/a)</td><td>1432.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.11 (n/a)</td><td>3371.20 (n/a)</td><td>806.72 (n/a)</td><td>170.60 (n/a)</td><td>107.30 (n/a)</td><td>1434.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.09 (n/a)</td><td>2764.20 (n/a)</td><td>1009.20 (n/a)</td><td>619.80 (n/a)</td><td>161.90 (n/a)</td><td>1089.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.09 (n/a)</td><td>13770.70 (n/a)</td><td>4568.74 (n/a)</td><td>2837.50 (n/a)</td><td>164.50 (n/a)</td><td>5631.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>0.09 (n/a)</td><td>3433.60 (n/a)</td><td>1229.08 (n/a)</td><td>195.20 (n/a)</td><td>174.00 (n/a)</td><td>1500.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>0.12 (n/a)</td><td>3514.40 (n/a)</td><td>1116.16 (n/a)</td><td>240.00 (n/a)</td><td>106.50 (n/a)</td><td>1453.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.05 (n/a)</td><td>52332.30 (n/a)</td><td>11851.22 (n/a)</td><td>1990.40 (n/a)</td><td>281.90 (n/a)</td><td>22659.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.79 (+7.59%)</td><td>2.89 <b>(-24.60%)</b></td><td>4.70 <b>(+26.76%)</b></td><td>0.07 <b>(-97.98%)</b></td><td>2.53 <b>(+492.67%)</b></td><td>134812.30 <b>(+4845.24%)</b></td><td>39365.62 <b>(+1488.23%)</b></td><td>2002.30 <b>(-21.11%)</b></td><td>1961.40 (-7.06%)</td><td>58267.06 <b>(+22044.46%)</b></td><td>1886.05 (+7.59%)</td><td>1136.06 <b>(-24.60%)</b></td><td>1847.58 <b>(+26.76%)</b></td><td>27.44 <b>(-97.98%)</b></td><td>994.63 <b>(+492.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.46 (n/a)</td><td>3.83 (n/a)</td><td>3.71 (n/a)</td><td>3.45 (n/a)</td><td>0.43 (n/a)</td><td>2726.10 (n/a)</td><td>2478.58 (n/a)</td><td>2538.20 (n/a)</td><td>2110.30 (n/a)</td><td>263.12 (n/a)</td><td>1752.97 (n/a)</td><td>1506.76 (n/a)</td><td>1457.49 (n/a)</td><td>1357.04 (n/a)</td><td>167.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.50 <b>(+49.89%)</b></td><td>0.85 (-9.27%)</td><td>0.92 (-6.57%)</td><td>0.00 <b>(-99.77%)</b></td><td>0.54 <b>(+364.64%)</b></td><td>132644.60 <b>(+43633.79%)</b></td><td>26703.88 <b>(+11021.06%)</b></td><td>241.10 (+7.01%)</td><td>147.10 <b>(-33.29%)</b></td><td>59222.68 <b>(+166855.52%)</b></td><td>64.16 <b>(+49.89%)</b></td><td>36.19 (-9.27%)</td><td>39.14 (-6.57%)</td><td>0.07 <b>(-99.77%)</b></td><td>22.97 <b>(+364.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.00 (n/a)</td><td>0.93 (n/a)</td><td>0.98 (n/a)</td><td>0.73 (n/a)</td><td>0.12 (n/a)</td><td>303.30 (n/a)</td><td>240.12 (n/a)</td><td>225.30 (n/a)</td><td>220.50 (n/a)</td><td>35.47 (n/a)</td><td>42.81 (n/a)</td><td>39.89 (n/a)</td><td>41.89 (n/a)</td><td>31.12 (n/a)</td><td>4.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.47 (+18.12%)</td><td>0.93 (-7.16%)</td><td>0.97 (-3.82%)</td><td>0.16 <b>(-78.88%)</b></td><td>0.49 <b>(+181.04%)</b></td><td>1368.50 <b>(+373.37%)</b></td><td>436.78 <b>(+93.80%)</b></td><td>227.20 (+3.98%)</td><td>150.20 (-15.33%)</td><td>522.26 <b>(+1180.00%)</b></td><td>62.85 (+18.12%)</td><td>39.86 (-7.16%)</td><td>41.54 (-3.82%)</td><td>6.90 <b>(-78.88%)</b></td><td>20.81 <b>(+181.04%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.25 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>0.77 (n/a)</td><td>0.17 (n/a)</td><td>289.10 (n/a)</td><td>225.38 (n/a)</td><td>218.50 (n/a)</td><td>177.40 (n/a)</td><td>40.80 (n/a)</td><td>53.21 (n/a)</td><td>42.93 (n/a)</td><td>43.19 (n/a)</td><td>32.65 (n/a)</td><td>7.41 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.52 (+0.06%)</td><td>0.52 (+0.15%)</td><td>0.52 (+0.79%)</td><td>0.51 (-0.79%)</td><td>0.00 <b>(+97.39%)</b></td><td>49178.00 (+0.80%)</td><td>48543.88 (-0.15%)</td><td>48288.90 (-0.78%)</td><td>48196.70 (-0.06%)</td><td>446.22 <b>(+98.76%)</b></td><td>356.45 (+0.06%)</td><td>353.93 (+0.15%)</td><td>355.77 (+0.79%)</td><td>349.34 (-0.79%)</td><td>3.24 <b>(+97.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48789.30 (n/a)</td><td>48616.20 (n/a)</td><td>48668.60 (n/a)</td><td>48227.60 (n/a)</td><td>224.50 (n/a)</td><td>356.22 (n/a)</td><td>353.38 (n/a)</td><td>353.00 (n/a)</td><td>352.12 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (-0.41%)</td><td>0.19 (-10.35%)</td><td>0.21 (+0.69%)</td><td>0.10 <b>(-52.71%)</b></td><td>0.05 <b>(+2394.32%)</b></td><td>252944.50 <b>(+111.47%)</b></td><td>144751.66 <b>(+22.51%)</b></td><td>117512.60 (-0.69%)</td><td>116955.00 (+0.41%)</td><td>60489.51 <b>(+5231.49%)</b></td><td>146.89 (-0.41%)</td><td>130.36 (-10.35%)</td><td>146.20 (+0.69%)</td><td>67.92 <b>(-52.71%)</b></td><td>34.93 <b>(+2394.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119611.60 (n/a)</td><td>118155.90 (n/a)</td><td>118327.30 (n/a)</td><td>116478.50 (n/a)</td><td>1134.57 (n/a)</td><td>147.49 (n/a)</td><td>145.41 (n/a)</td><td>145.19 (n/a)</td><td>143.63 (n/a)</td><td>1.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.93 (+5.03%)</td><td>0.91 (+3.28%)</td><td>0.93 (+4.94%)</td><td>0.87 (-0.81%)</td><td>0.03 <b>(+695.77%)</b></td><td>28883.20 (+0.82%)</td><td>27608.68 (-3.11%)</td><td>27131.80 (-4.71%)</td><td>27021.10 (-4.79%)</td><td>792.80 <b>(+663.02%)</b></td><td>635.80 (+5.03%)</td><td>622.66 (+3.28%)</td><td>633.20 (+4.94%)</td><td>594.80 (-0.81%)</td><td>17.47 <b>(+695.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28649.00 (n/a)</td><td>28495.86 (n/a)</td><td>28472.50 (n/a)</td><td>28379.40 (n/a)</td><td>103.90 (n/a)</td><td>605.36 (n/a)</td><td>602.90 (n/a)</td><td>603.38 (n/a)</td><td>599.67 (n/a)</td><td>2.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.61 (+2.18%)</td><td>3.31 (-5.83%)</td><td>3.59 (+2.16%)</td><td>2.20 <b>(-37.13%)</b></td><td>0.62 <b>(+4471.33%)</b></td><td>11461.40 <b>(+59.07%)</b></td><td>7907.84 (+10.36%)</td><td>7011.90 (-2.12%)</td><td>6980.60 (-2.14%)</td><td>1986.79 <b>(+7056.16%)</b></td><td>2461.09 (+2.18%)</td><td>2257.81 (-5.83%)</td><td>2450.10 (+2.16%)</td><td>1498.94 <b>(-37.13%)</b></td><td>424.39 <b>(+4471.44%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.53 (n/a)</td><td>3.51 (n/a)</td><td>3.51 (n/a)</td><td>3.49 (n/a)</td><td>0.01 (n/a)</td><td>7205.30 (n/a)</td><td>7165.34 (n/a)</td><td>7163.50 (n/a)</td><td>7133.10 (n/a)</td><td>27.76 (n/a)</td><td>2408.47 (n/a)</td><td>2397.66 (n/a)</td><td>2398.24 (n/a)</td><td>2384.32 (n/a)</td><td>9.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.25 (+0.16%)</td><td>2.24 <b>(-22.86%)</b></td><td>2.51 (-11.64%)</td><td>0.18 <b>(-93.47%)</b></td><td>1.26 <b>(+540.99%)</b></td><td>141131.60 <b>(+1431.31%)</b></td><td>35818.18 <b>(+311.50%)</b></td><td>10040.00 (+13.18%)</td><td>7754.20 (-0.16%)</td><td>58902.45 <b>(+10615.91%)</b></td><td>2215.54 (+0.16%)</td><td>1527.74 <b>(-22.86%)</b></td><td>1711.14 (-11.64%)</td><td>121.73 <b>(-93.47%)</b></td><td>859.37 <b>(+540.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.24 (n/a)</td><td>2.90 (n/a)</td><td>2.84 (n/a)</td><td>2.73 (n/a)</td><td>0.20 (n/a)</td><td>9216.40 (n/a)</td><td>8704.28 (n/a)</td><td>8871.10 (n/a)</td><td>7766.70 (n/a)</td><td>549.67 (n/a)</td><td>2212.00 (n/a)</td><td>1980.50 (n/a)</td><td>1936.62 (n/a)</td><td>1864.06 (n/a)</td><td>134.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.42 (+2.89%)</td><td>2.76 (-15.72%)</td><td>3.37 (+1.75%)</td><td>1.02 <b>(-68.05%)</b></td><td>1.03 <b>(+1600.23%)</b></td><td>24775.20 <b>(+213.01%)</b></td><td>11323.00 <b>(+47.52%)</b></td><td>7471.20 (-1.72%)</td><td>7348.00 (-2.81%)</td><td>7579.05 <b>(+5138.44%)</b></td><td>2338.03 (+2.89%)</td><td>1886.98 (-15.72%)</td><td>2299.49 (+1.75%)</td><td>693.43 <b>(-68.05%)</b></td><td>705.17 <b>(+1600.23%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.33 (n/a)</td><td>3.28 (n/a)</td><td>3.31 (n/a)</td><td>3.18 (n/a)</td><td>0.06 (n/a)</td><td>7915.20 (n/a)</td><td>7675.54 (n/a)</td><td>7602.20 (n/a)</td><td>7560.10 (n/a)</td><td>144.68 (n/a)</td><td>2272.43 (n/a)</td><td>2238.89 (n/a)</td><td>2259.85 (n/a)</td><td>2170.50 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.79 (+0.13%)</td><td>0.60 <b>(-23.78%)</b></td><td>0.76 (-2.31%)</td><td>0.33 <b>(-57.69%)</b></td><td>0.24 <b>(+17227.07%)</b></td><td>228197.90 <b>(+136.33%)</b></td><td>149480.50 <b>(+55.04%)</b></td><td>98752.30 (+2.36%)</td><td>95993.60 (-0.13%)</td><td>70979.29 <b>(+41304.54%)</b></td><td>715.88 (+0.13%)</td><td>543.27 <b>(-23.78%)</b></td><td>695.88 (-2.31%)</td><td>301.14 <b>(-57.69%)</b></td><td>219.98 <b>(+17227.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96557.50 (n/a)</td><td>96413.38 (n/a)</td><td>96475.30 (n/a)</td><td>96119.50 (n/a)</td><td>171.43 (n/a)</td><td>714.94 (n/a)</td><td>712.76 (n/a)</td><td>712.30 (n/a)</td><td>711.70 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.73 (+0.43%)</td><td>0.65 (-11.11%)</td><td>0.73 (-0.09%)</td><td>0.32 <b>(-55.67%)</b></td><td>0.18 <b>(+55912.65%)</b></td><td>233925.80 <b>(+125.56%)</b></td><td>129657.70 <b>(+25.12%)</b></td><td>103704.80 (+0.09%)</td><td>103151.10 (-0.43%)</td><td>58289.62 <b>(+126127.74%)</b></td><td>666.20 (+0.43%)</td><td>589.46 (-11.11%)</td><td>662.64 (-0.09%)</td><td>293.77 <b>(-55.67%)</b></td><td>165.33 <b>(+55912.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103710.90 (n/a)</td><td>103630.30 (n/a)</td><td>103612.40 (n/a)</td><td>103596.20 (n/a)</td><td>46.18 (n/a)</td><td>663.34 (n/a)</td><td>663.12 (n/a)</td><td>663.24 (n/a)</td><td>662.61 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.70 (+1.81%)</td><td>0.62 (-10.63%)</td><td>0.69 (-0.06%)</td><td>0.31 <b>(-54.39%)</b></td><td>0.17 <b>(+15694.14%)</b></td><td>240559.30 <b>(+119.23%)</b></td><td>135491.58 <b>(+23.68%)</b></td><td>109597.90 (+0.06%)</td><td>107381.60 (-1.78%)</td><td>58765.49 <b>(+34399.35%)</b></td><td>639.96 (+1.81%)</td><td>560.61 (-10.63%)</td><td>627.01 (-0.06%)</td><td>285.67 <b>(-54.39%)</b></td><td>154.08 <b>(+15694.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109727.80 (n/a)</td><td>109553.90 (n/a)</td><td>109529.40 (n/a)</td><td>109323.80 (n/a)</td><td>170.34 (n/a)</td><td>628.59 (n/a)</td><td>627.27 (n/a)</td><td>627.41 (n/a)</td><td>626.27 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.25 (+4.55%)</td><td>5.83 (-7.88%)</td><td>7.16 (+9.86%)</td><td>0.52 <b>(-89.12%)</b></td><td>2.97 <b>(+235.52%)</b></td><td>17127.50 <b>(+819.25%)</b></td><td>4422.76 <b>(+207.90%)</b></td><td>1245.10 (-8.97%)</td><td>1230.00 (-4.35%)</td><td>7102.19 <b>(+2835.54%)</b></td><td>436.49 (+4.55%)</td><td>350.90 (-7.88%)</td><td>431.20 (+9.86%)</td><td>31.35 <b>(-89.12%)</b></td><td>178.76 <b>(+235.52%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.93 (n/a)</td><td>6.32 (n/a)</td><td>6.52 (n/a)</td><td>4.78 (n/a)</td><td>0.88 (n/a)</td><td>1863.20 (n/a)</td><td>1436.42 (n/a)</td><td>1367.80 (n/a)</td><td>1285.90 (n/a)</td><td>241.94 (n/a)</td><td>417.49 (n/a)</td><td>380.92 (n/a)</td><td>392.51 (n/a)</td><td>288.15 (n/a)</td><td>53.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.91 (-3.23%)</td><td>5.44 (-19.65%)</td><td>6.61 (-2.79%)</td><td>0.53 <b>(-91.59%)</b></td><td>2.75 <b>(+707.58%)</b></td><td>16777.20 <b>(+1089.37%)</b></td><td>4426.58 <b>(+235.28%)</b></td><td>1348.00 (+2.87%)</td><td>1290.70 (+3.34%)</td><td>6904.30 <b>(+10182.29%)</b></td><td>415.94 (-3.23%)</td><td>327.41 (-19.65%)</td><td>398.28 (-2.79%)</td><td>32.00 <b>(-91.59%)</b></td><td>165.49 <b>(+707.58%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.14 (n/a)</td><td>6.76 (n/a)</td><td>6.80 (n/a)</td><td>6.32 (n/a)</td><td>0.34 (n/a)</td><td>1410.60 (n/a)</td><td>1320.26 (n/a)</td><td>1310.40 (n/a)</td><td>1249.00 (n/a)</td><td>67.15 (n/a)</td><td>429.84 (n/a)</td><td>407.47 (n/a)</td><td>409.69 (n/a)</td><td>380.60 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.19 (+6.70%)</td><td>6.80 (+3.89%)</td><td>6.70 (+1.85%)</td><td>6.50 (+4.53%)</td><td>0.29 <b>(+47.63%)</b></td><td>1372.00 (-4.34%)</td><td>1313.10 (-3.68%)</td><td>1329.60 (-1.82%)</td><td>1239.00 (-6.28%)</td><td>56.10 <b>(+31.47%)</b></td><td>433.30 (+6.70%)</td><td>409.46 (+3.89%)</td><td>403.78 (+1.85%)</td><td>391.30 (+4.53%)</td><td>17.73 <b>(+47.63%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.74 (n/a)</td><td>6.54 (n/a)</td><td>6.58 (n/a)</td><td>6.21 (n/a)</td><td>0.20 (n/a)</td><td>1434.20 (n/a)</td><td>1363.20 (n/a)</td><td>1354.20 (n/a)</td><td>1322.00 (n/a)</td><td>42.67 (n/a)</td><td>406.10 (n/a)</td><td>394.14 (n/a)</td><td>396.45 (n/a)</td><td>374.34 (n/a)</td><td>12.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.45 (+4.35%)</td><td>5.95 <b>(-23.64%)</b></td><td>8.10 (+2.57%)</td><td>0.26 <b>(-96.34%)</b></td><td>3.58 <b>(+735.93%)</b></td><td>134980.30 <b>(+2629.80%)</b></td><td>31042.72 <b>(+592.56%)</b></td><td>4307.00 (-2.51%)</td><td>4126.50 (-4.17%)</td><td>58122.31 <b>(+21951.44%)</b></td><td>520.41 (+4.35%)</td><td>366.78 <b>(-23.64%)</b></td><td>498.61 (+2.57%)</td><td>15.91 <b>(-96.34%)</b></td><td>220.57 <b>(+735.93%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.10 (n/a)</td><td>7.80 (n/a)</td><td>7.89 (n/a)</td><td>7.05 (n/a)</td><td>0.43 (n/a)</td><td>4944.70 (n/a)</td><td>4482.34 (n/a)</td><td>4417.70 (n/a)</td><td>4306.00 (n/a)</td><td>263.58 (n/a)</td><td>498.72 (n/a)</td><td>480.34 (n/a)</td><td>486.11 (n/a)</td><td>434.30 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.91 (+0.08%)</td><td>7.75 (+4.12%)</td><td>7.81 (+2.14%)</td><td>7.57 (+17.56%)</td><td>0.17 <b>(-71.04%)</b></td><td>4605.20 (-14.94%)</td><td>4500.40 (-4.43%)</td><td>4466.70 (-2.09%)</td><td>4407.40 (-0.08%)</td><td>97.31 <b>(-75.75%)</b></td><td>487.25 (+0.08%)</td><td>477.35 (+4.12%)</td><td>480.77 (+2.14%)</td><td>466.32 (+17.56%)</td><td>10.27 <b>(-71.04%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.90 (n/a)</td><td>7.44 (n/a)</td><td>7.64 (n/a)</td><td>6.44 (n/a)</td><td>0.58 (n/a)</td><td>5413.90 (n/a)</td><td>4708.96 (n/a)</td><td>4562.10 (n/a)</td><td>4410.90 (n/a)</td><td>401.29 (n/a)</td><td>486.86 (n/a)</td><td>458.46 (n/a)</td><td>470.72 (n/a)</td><td>396.66 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.80 (-0.03%)</td><td>7.53 (+3.87%)</td><td>7.70 (+6.07%)</td><td>6.83 (+4.39%)</td><td>0.40 (-13.07%)</td><td>5106.40 (-4.21%)</td><td>4643.94 (-3.81%)</td><td>4527.90 (-5.73%)</td><td>4470.60 (+0.03%)</td><td>263.64 (-16.87%)</td><td>480.35 (-0.03%)</td><td>463.55 (+3.87%)</td><td>474.28 (+6.07%)</td><td>420.55 (+4.39%)</td><td>24.63 (-13.07%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.80 (n/a)</td><td>7.25 (n/a)</td><td>7.26 (n/a)</td><td>6.54 (n/a)</td><td>0.46 (n/a)</td><td>5330.70 (n/a)</td><td>4828.10 (n/a)</td><td>4802.90 (n/a)</td><td>4469.10 (n/a)</td><td>317.13 (n/a)</td><td>480.52 (n/a)</td><td>446.28 (n/a)</td><td>447.12 (n/a)</td><td>402.85 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.79 (+0.51%)</td><td>0.61 <b>(-22.97%)</b></td><td>0.78 (-0.78%)</td><td>0.33 <b>(-57.69%)</b></td><td>0.25 <b>(+45824.93%)</b></td><td>226620.60 <b>(+136.34%)</b></td><td>147806.72 <b>(+54.30%)</b></td><td>96531.70 (+0.79%)</td><td>95244.40 (-0.51%)</td><td>71372.88 <b>(+108121.92%)</b></td><td>721.51 (+0.51%)</td><td>552.56 <b>(-22.97%)</b></td><td>711.88 (-0.78%)</td><td>303.24 <b>(-57.69%)</b></td><td>226.86 <b>(+45824.97%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95886.70 (n/a)</td><td>95793.38 (n/a)</td><td>95777.20 (n/a)</td><td>95733.90 (n/a)</td><td>65.95 (n/a)</td><td>717.82 (n/a)</td><td>717.37 (n/a)</td><td>717.49 (n/a)</td><td>716.67 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.74 (+0.44%)</td><td>0.73 (+0.16%)</td><td>0.74 (+0.37%)</td><td>0.73 (-0.80%)</td><td>0.00 <b>(+3856.07%)</b></td><td>103743.10 (+0.80%)</td><td>102742.42 (-0.15%)</td><td>102523.30 (-0.37%)</td><td>102431.80 (-0.44%)</td><td>560.66 <b>(+3870.43%)</b></td><td>670.88 (+0.44%)</td><td>668.87 (+0.16%)</td><td>670.28 (+0.37%)</td><td>662.40 (-0.80%)</td><td>3.62 <b>(+3856.71%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102916.40 (n/a)</td><td>102901.18 (n/a)</td><td>102901.20 (n/a)</td><td>102884.20 (n/a)</td><td>14.12 (n/a)</td><td>667.93 (n/a)</td><td>667.82 (n/a)</td><td>667.82 (n/a)</td><td>667.72 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.71 (+1.11%)</td><td>0.55 <b>(-21.16%)</b></td><td>0.71 (+0.97%)</td><td>0.32 <b>(-54.78%)</b></td><td>0.21 <b>(+15714.91%)</b></td><td>239632.20 <b>(+121.14%)</b></td><td>159365.06 <b>(+47.53%)</b></td><td>106978.40 (-0.96%)</td><td>106651.60 (-1.10%)</td><td>72030.44 <b>(+34325.69%)</b></td><td>644.34 (+1.11%)</td><td>501.56 <b>(-21.16%)</b></td><td>642.37 (+0.97%)</td><td>286.77 <b>(-54.78%)</b></td><td>194.57 <b>(+15715.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108363.30 (n/a)</td><td>108024.18 (n/a)</td><td>108011.10 (n/a)</td><td>107835.30 (n/a)</td><td>209.23 (n/a)</td><td>637.26 (n/a)</td><td>636.15 (n/a)</td><td>636.23 (n/a)</td><td>634.16 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.22 (+1.14%)</td><td>4.16 (+11.63%)</td><td>4.16 (+15.85%)</td><td>4.12 (+15.12%)</td><td>0.04 <b>(-85.11%)</b></td><td>1956.60 (-13.14%)</td><td>1938.00 (-10.72%)</td><td>1938.80 (-13.68%)</td><td>1909.80 (-1.12%)</td><td>17.61 <b>(-87.21%)</b></td><td>1106.89 (+1.14%)</td><td>1090.85 (+11.63%)</td><td>1090.33 (+15.85%)</td><td>1080.41 (+15.12%)</td><td>9.98 <b>(-85.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.17 (n/a)</td><td>3.73 (n/a)</td><td>3.59 (n/a)</td><td>3.58 (n/a)</td><td>0.26 (n/a)</td><td>2252.50 (n/a)</td><td>2170.82 (n/a)</td><td>2246.00 (n/a)</td><td>1931.50 (n/a)</td><td>137.72 (n/a)</td><td>1094.42 (n/a)</td><td>977.18 (n/a)</td><td>941.18 (n/a)</td><td>938.48 (n/a)</td><td>67.04 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.46 (-11.29%)</td><td>0.13 <b>(-69.36%)</b></td><td>0.07 <b>(-80.56%)</b></td><td>0.01 <b>(-98.01%)</b></td><td>0.19 <b>(+145.73%)</b></td><td>176372.90 <b>(+4934.77%)</b></td><td>50647.18 <b>(+1573.30%)</b></td><td>16775.90 <b>(+414.41%)</b></td><td>2715.00 (+12.72%)</td><td>71615.22 <b>(+13850.93%)</b></td><td>24.72 (-11.29%)</td><td>6.96 <b>(-69.36%)</b></td><td>4.00 <b>(-80.56%)</b></td><td>0.38 <b>(-98.01%)</b></td><td>10.05 <b>(+145.73%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>3503.10 (n/a)</td><td>3026.78 (n/a)</td><td>3261.20 (n/a)</td><td>2408.60 (n/a)</td><td>513.34 (n/a)</td><td>27.86 (n/a)</td><td>22.73 (n/a)</td><td>20.58 (n/a)</td><td>19.16 (n/a)</td><td>4.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.45 (+0.41%)</td><td>5.29 (+7.40%)</td><td>6.08 <b>(+25.44%)</b></td><td>1.90 <b>(-49.49%)</b></td><td>1.91 <b>(+99.79%)</b></td><td>3503.00 <b>(+97.97%)</b></td><td>1568.66 (+12.85%)</td><td>1094.90 <b>(-20.28%)</b></td><td>1031.90 (-0.41%)</td><td>1081.99 <b>(+315.70%)</b></td><td>1991.73 (+0.41%)</td><td>1634.49 (+7.40%)</td><td>1877.14 <b>(+25.44%)</b></td><td>586.70 <b>(-49.49%)</b></td><td>589.45 <b>(+99.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.42 (n/a)</td><td>4.93 (n/a)</td><td>4.84 (n/a)</td><td>3.76 (n/a)</td><td>0.95 (n/a)</td><td>1769.50 (n/a)</td><td>1390.02 (n/a)</td><td>1373.40 (n/a)</td><td>1036.10 (n/a)</td><td>260.28 (n/a)</td><td>1983.54 (n/a)</td><td>1521.82 (n/a)</td><td>1496.39 (n/a)</td><td>1161.46 (n/a)</td><td>295.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 <b>(+33.47%)</b></td><td>0.21 (+11.81%)</td><td>0.19 (+0.53%)</td><td>0.16 (+9.95%)</td><td>0.05 <b>(+76.35%)</b></td><td>0.28 <b>(+33.47%)</b></td><td>0.20 (+11.81%)</td><td>0.19 (+0.53%)</td><td>0.16 (+9.95%)</td><td>0.05 <b>(+76.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.33 (-0.70%)</td><td>13.13 (+2.91%)</td><td>13.24 (+0.43%)</td><td>12.61 (+8.72%)</td><td>0.30 <b>(-60.94%)</b></td><td>13.32 (-0.70%)</td><td>13.12 (+2.91%)</td><td>13.23 (+0.43%)</td><td>12.60 (+8.72%)</td><td>0.30 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>13.42 (n/a)</td><td>12.76 (n/a)</td><td>13.18 (n/a)</td><td>11.60 (n/a)</td><td>0.76 (n/a)</td><td>13.41 (n/a)</td><td>12.75 (n/a)</td><td>13.17 (n/a)</td><td>11.59 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>24.40 (-0.68%)</td><td>23.73 (-2.09%)</td><td>23.90 (-1.34%)</td><td>22.80 (-4.63%)</td><td>0.72 <b>(+170.74%)</b></td><td>24.39 (-0.68%)</td><td>23.72 (-2.09%)</td><td>23.88 (-1.34%)</td><td>22.79 (-4.63%)</td><td>0.72 <b>(+170.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>24.57 (n/a)</td><td>24.24 (n/a)</td><td>24.22 (n/a)</td><td>23.91 (n/a)</td><td>0.27 (n/a)</td><td>24.56 (n/a)</td><td>24.22 (n/a)</td><td>24.21 (n/a)</td><td>23.89 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>41.81 (+2.34%)</td><td>38.79 (+0.22%)</td><td>39.42 (-1.29%)</td><td>34.51 (+5.69%)</td><td>2.66 <b>(-22.39%)</b></td><td>41.78 (+2.34%)</td><td>38.77 (+0.22%)</td><td>39.40 (-1.29%)</td><td>34.48 (+5.69%)</td><td>2.66 <b>(-22.39%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>40.86 (n/a)</td><td>38.71 (n/a)</td><td>39.94 (n/a)</td><td>32.65 (n/a)</td><td>3.43 (n/a)</td><td>40.83 (n/a)</td><td>38.68 (n/a)</td><td>39.92 (n/a)</td><td>32.63 (n/a)</td><td>3.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>47.33 (+6.97%)</td><td>42.71 (-1.66%)</td><td>41.70 (-3.31%)</td><td>40.95 (-4.08%)</td><td>2.63 <b>(+268.54%)</b></td><td>47.30 (+6.97%)</td><td>42.68 (-1.66%)</td><td>41.67 (-3.31%)</td><td>40.92 (-4.08%)</td><td>2.63 <b>(+268.54%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>44.24 (n/a)</td><td>43.43 (n/a)</td><td>43.12 (n/a)</td><td>42.69 (n/a)</td><td>0.71 (n/a)</td><td>44.21 (n/a)</td><td>43.40 (n/a)</td><td>43.10 (n/a)</td><td>42.66 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.44 (+0.63%)</td><td>13.21 (+0.65%)</td><td>13.29 (+0.49%)</td><td>12.81 (+2.13%)</td><td>0.24 <b>(-27.24%)</b></td><td>13.43 (+0.63%)</td><td>13.20 (+0.65%)</td><td>13.28 (+0.49%)</td><td>12.80 (+2.13%)</td><td>0.24 <b>(-27.24%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>13.35 (n/a)</td><td>13.12 (n/a)</td><td>13.22 (n/a)</td><td>12.54 (n/a)</td><td>0.33 (n/a)</td><td>13.35 (n/a)</td><td>13.11 (n/a)</td><td>13.22 (n/a)</td><td>12.54 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>24.70 (-0.38%)</td><td>23.97 (-0.74%)</td><td>23.88 (-1.21%)</td><td>23.39 (+1.23%)</td><td>0.54 <b>(-20.33%)</b></td><td>24.68 (-0.38%)</td><td>23.95 (-0.74%)</td><td>23.87 (-1.21%)</td><td>23.38 (+1.23%)</td><td>0.54 <b>(-20.33%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>24.80 (n/a)</td><td>24.15 (n/a)</td><td>24.18 (n/a)</td><td>23.11 (n/a)</td><td>0.68 (n/a)</td><td>24.78 (n/a)</td><td>24.13 (n/a)</td><td>24.16 (n/a)</td><td>23.10 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>42.91 (+6.69%)</td><td>40.38 (+2.83%)</td><td>40.88 (+4.53%)</td><td>38.22 (-0.83%)</td><td>1.88 <b>(+143.74%)</b></td><td>42.89 (+6.69%)</td><td>40.35 (+2.83%)</td><td>40.86 (+4.53%)</td><td>38.20 (-0.83%)</td><td>1.88 <b>(+143.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>40.22 (n/a)</td><td>39.27 (n/a)</td><td>39.11 (n/a)</td><td>38.54 (n/a)</td><td>0.77 (n/a)</td><td>40.20 (n/a)</td><td>39.24 (n/a)</td><td>39.08 (n/a)</td><td>38.52 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>45.04 (-0.59%)</td><td>42.02 (-2.14%)</td><td>42.75 (-0.17%)</td><td>36.70 (-9.75%)</td><td>3.14 <b>(+75.38%)</b></td><td>45.02 (-0.59%)</td><td>42.00 (-2.14%)</td><td>42.73 (-0.17%)</td><td>36.68 (-9.75%)</td><td>3.13 <b>(+75.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>45.31 (n/a)</td><td>42.94 (n/a)</td><td>42.83 (n/a)</td><td>40.67 (n/a)</td><td>1.79 (n/a)</td><td>45.28 (n/a)</td><td>42.91 (n/a)</td><td>42.80 (n/a)</td><td>40.64 (n/a)</td><td>1.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>171.54 (n/a)</td><td>174.50 (n/a)</td><td>129.30 (n/a)</td><td>26.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>158.24 (n/a)</td><td>165.70 (n/a)</td><td>107.00 (n/a)</td><td>40.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.10 (n/a)</td><td>182.66 (n/a)</td><td>173.70 (n/a)</td><td>153.50 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>173.06 (n/a)</td><td>168.90 (n/a)</td><td>143.80 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>367.50 (n/a)</td><td>214.02 (n/a)</td><td>175.00 (n/a)</td><td>150.50 (n/a)</td><td>87.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.50 (n/a)</td><td>199.70 (n/a)</td><td>190.70 (n/a)</td><td>153.10 (n/a)</td><td>39.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>188.26 (n/a)</td><td>205.80 (n/a)</td><td>113.30 (n/a)</td><td>48.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>339.90 (n/a)</td><td>255.40 (n/a)</td><td>230.60 (n/a)</td><td>209.90 (n/a)</td><td>52.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.60 (n/a)</td><td>203.36 (n/a)</td><td>187.90 (n/a)</td><td>166.00 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>166.80 (n/a)</td><td>168.80 (n/a)</td><td>146.80 (n/a)</td><td>15.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>159.76 (n/a)</td><td>167.50 (n/a)</td><td>104.30 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>171.04 (n/a)</td><td>160.80 (n/a)</td><td>143.40 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>175.02 (n/a)</td><td>178.80 (n/a)</td><td>111.10 (n/a)</td><td>40.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>169.82 (n/a)</td><td>169.40 (n/a)</td><td>130.10 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>198.90 (n/a)</td><td>163.56 (n/a)</td><td>171.30 (n/a)</td><td>102.90 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>245.90 (n/a)</td><td>210.78 (n/a)</td><td>216.00 (n/a)</td><td>176.20 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.90 (n/a)</td><td>180.36 (n/a)</td><td>169.90 (n/a)</td><td>128.80 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.10 (n/a)</td><td>164.72 (n/a)</td><td>173.70 (n/a)</td><td>116.00 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>283.30 (n/a)</td><td>190.58 (n/a)</td><td>158.30 (n/a)</td><td>132.00 (n/a)</td><td>66.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.90 (n/a)</td><td>162.60 (n/a)</td><td>173.80 (n/a)</td><td>114.80 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>205.60 (n/a)</td><td>168.50 (n/a)</td><td>189.60 (n/a)</td><td>117.20 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>167.58 (n/a)</td><td>171.30 (n/a)</td><td>129.50 (n/a)</td><td>28.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.20 (n/a)</td><td>173.76 (n/a)</td><td>174.70 (n/a)</td><td>130.20 (n/a)</td><td>38.16 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>186.68 (n/a)</td><td>188.90 (n/a)</td><td>163.40 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (-5.07%)</td><td>0.18 (+10.17%)</td><td>0.18 (+16.44%)</td><td>0.16 (+13.32%)</td><td>0.02 <b>(-42.30%)</b></td><td>200.70 (-11.74%)</td><td>184.20 (-10.34%)</td><td>183.90 (-14.11%)</td><td>165.20 (+5.36%)</td><td>15.66 <b>(-44.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>227.40 (n/a)</td><td>205.44 (n/a)</td><td>214.10 (n/a)</td><td>156.80 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>161.60 (n/a)</td><td>152.50 (n/a)</td><td>136.50 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>218.80 (n/a)</td><td>170.86 (n/a)</td><td>155.80 (n/a)</td><td>147.60 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>326.20 (n/a)</td><td>198.90 (n/a)</td><td>174.80 (n/a)</td><td>127.00 (n/a)</td><td>76.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.34 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>217.60 (n/a)</td><td>177.88 (n/a)</td><td>199.60 (n/a)</td><td>96.00 (n/a)</td><td>49.78 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>255.10 (n/a)</td><td>199.46 (n/a)</td><td>214.30 (n/a)</td><td>142.40 (n/a)</td><td>44.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>268.20 (n/a)</td><td>198.94 (n/a)</td><td>200.90 (n/a)</td><td>98.40 (n/a)</td><td>67.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>331.20 (n/a)</td><td>204.56 (n/a)</td><td>194.80 (n/a)</td><td>122.50 (n/a)</td><td>78.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-16.30%)</td><td>0.02 (-0.62%)</td><td>0.02 (+7.53%)</td><td>0.02 (+3.65%)</td><td>0.00 <b>(-51.83%)</b></td><td>189.40 (-3.52%)</td><td>171.38 (-0.86%)</td><td>170.10 (-7.00%)</td><td>155.60 (+19.51%)</td><td>14.57 <b>(-43.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.30 (n/a)</td><td>172.86 (n/a)</td><td>182.90 (n/a)</td><td>130.20 (n/a)</td><td>25.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-16.32%)</td><td>0.03 (-13.82%)</td><td>0.03 (-12.46%)</td><td>0.02 <b>(-20.78%)</b></td><td>0.00 (-6.14%)</td><td>224.70 <b>(+26.24%)</b></td><td>168.44 (+16.99%)</td><td>153.50 (+14.21%)</td><td>135.00 (+19.47%)</td><td>36.13 <b>(+41.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>143.98 (n/a)</td><td>134.40 (n/a)</td><td>113.00 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (+16.08%)</td><td>0.02 (+16.21%)</td><td>0.02 (+13.66%)</td><td>0.02 <b>(+37.85%)</b></td><td>0.00 (-3.82%)</td><td>231.00 <b>(-27.47%)</b></td><td>201.36 (-14.89%)</td><td>192.80 (-12.00%)</td><td>173.40 (-13.82%)</td><td>27.60 <b>(-41.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>318.50 (n/a)</td><td>236.58 (n/a)</td><td>219.10 (n/a)</td><td>201.20 (n/a)</td><td>46.82 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 <b>(-33.42%)</b></td><td>0.02 (-13.38%)</td><td>0.02 (+5.50%)</td><td>0.02 (-15.88%)</td><td>0.00 <b>(-56.78%)</b></td><td>257.80 (+18.86%)</td><td>205.38 (+10.90%)</td><td>193.90 (-5.23%)</td><td>165.50 <b>(+50.18%)</b></td><td>35.00 (-18.73%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>185.20 (n/a)</td><td>204.60 (n/a)</td><td>110.20 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+30.81%)</b></td><td>0.03 (+12.57%)</td><td>0.03 (+13.06%)</td><td>0.02 (-0.32%)</td><td>0.01 <b>(+116.66%)</b></td><td>192.90 (+0.31%)</td><td>158.20 (-8.67%)</td><td>156.90 (-11.56%)</td><td>108.30 <b>(-23.52%)</b></td><td>31.91 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>173.22 (n/a)</td><td>177.40 (n/a)</td><td>141.60 (n/a)</td><td>19.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+10.57%)</td><td>0.02 (-5.63%)</td><td>0.02 (-13.50%)</td><td>0.02 (-5.77%)</td><td>0.00 <b>(+49.45%)</b></td><td>202.20 (+6.14%)</td><td>176.02 (+7.38%)</td><td>181.70 (+15.59%)</td><td>130.30 (-9.58%)</td><td>29.00 <b>(+42.49%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>163.92 (n/a)</td><td>157.20 (n/a)</td><td>144.10 (n/a)</td><td>20.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+31.00%)</b></td><td>0.03 (+17.32%)</td><td>0.02 (+15.35%)</td><td>0.02 (-1.90%)</td><td>0.00 <b>(+386.89%)</b></td><td>202.20 (+1.92%)</td><td>166.22 (-13.29%)</td><td>166.00 (-13.27%)</td><td>138.70 <b>(-23.67%)</b></td><td>25.30 <b>(+275.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>191.70 (n/a)</td><td>191.40 (n/a)</td><td>181.70 (n/a)</td><td>6.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+31.85%)</b></td><td>0.03 <b>(+21.98%)</b></td><td>0.03 (+11.93%)</td><td>0.02 <b>(+28.10%)</b></td><td>0.00 <b>(+61.77%)</b></td><td>168.60 <b>(-21.94%)</b></td><td>145.26 (-17.54%)</td><td>150.20 (-10.65%)</td><td>122.60 <b>(-24.13%)</b></td><td>21.00 (-7.48%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>176.16 (n/a)</td><td>168.10 (n/a)</td><td>161.60 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+3.09%)</td><td>0.02 (+3.65%)</td><td>0.02 (+9.94%)</td><td>0.02 (-4.52%)</td><td>0.00 <b>(+30.86%)</b></td><td>217.20 (+4.73%)</td><td>173.78 (-2.24%)</td><td>166.70 (-9.06%)</td><td>137.30 (-2.97%)</td><td>34.43 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.40 (n/a)</td><td>177.76 (n/a)</td><td>183.30 (n/a)</td><td>141.50 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+52.09%)</b></td><td>0.02 (+13.68%)</td><td>0.02 (+6.19%)</td><td>0.02 (-2.79%)</td><td>0.01 <b>(+227.12%)</b></td><td>221.80 (+2.88%)</td><td>174.32 (-7.87%)</td><td>180.30 (-5.80%)</td><td>111.50 <b>(-34.26%)</b></td><td>41.11 <b>(+115.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>189.22 (n/a)</td><td>191.40 (n/a)</td><td>169.60 (n/a)</td><td>19.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-1.85%)</td><td>0.03 (+9.47%)</td><td>0.02 (+1.26%)</td><td>0.02 <b>(+31.01%)</b></td><td>0.00 <b>(-61.12%)</b></td><td>173.70 <b>(-23.65%)</b></td><td>164.10 (-10.92%)</td><td>166.70 (-1.24%)</td><td>146.70 (+1.87%)</td><td>10.20 <b>(-70.81%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.50 (n/a)</td><td>184.22 (n/a)</td><td>168.80 (n/a)</td><td>144.00 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+33.58%)</b></td><td>0.02 (+13.81%)</td><td>0.02 (+13.04%)</td><td>0.02 (-2.78%)</td><td>0.01 <b>(+138.22%)</b></td><td>224.70 (+2.84%)</td><td>173.04 (-9.76%)</td><td>168.60 (-11.50%)</td><td>125.40 <b>(-25.09%)</b></td><td>35.50 <b>(+80.95%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>191.76 (n/a)</td><td>190.50 (n/a)</td><td>167.40 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-9.43%)</td><td>0.02 (-1.17%)</td><td>0.02 (+10.12%)</td><td>0.02 (-11.81%)</td><td>0.00 (+3.31%)</td><td>247.80 (+13.36%)</td><td>186.78 (+1.99%)</td><td>170.00 (-9.19%)</td><td>155.40 (+10.45%)</td><td>37.46 <b>(+34.42%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>183.14 (n/a)</td><td>187.20 (n/a)</td><td>140.70 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(+47.87%)</b></td><td>0.03 <b>(+27.88%)</b></td><td>0.03 <b>(+39.58%)</b></td><td>0.02 (+6.30%)</td><td>0.01 <b>(+258.64%)</b></td><td>231.90 (-5.92%)</td><td>171.62 (-17.46%)</td><td>142.70 <b>(-28.36%)</b></td><td>131.30 <b>(-32.35%)</b></td><td>49.41 <b>(+125.56%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.50 (n/a)</td><td>207.92 (n/a)</td><td>199.20 (n/a)</td><td>194.10 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-5.25%)</td><td>0.02 (-3.89%)</td><td>0.02 (+13.04%)</td><td>0.02 (-7.01%)</td><td>0.00 (-13.79%)</td><td>237.70 (+7.51%)</td><td>185.74 (+3.55%)</td><td>175.30 (-11.51%)</td><td>143.80 (+5.58%)</td><td>38.29 (+1.52%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>179.38 (n/a)</td><td>198.10 (n/a)</td><td>136.20 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-13.98%)</td><td>0.02 (-4.75%)</td><td>0.02 (-2.16%)</td><td>0.02 (-11.14%)</td><td>0.00 (-9.02%)</td><td>245.50 (+12.56%)</td><td>186.44 (+5.32%)</td><td>181.30 (+2.20%)</td><td>150.70 (+16.28%)</td><td>38.44 <b>(+21.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.10 (n/a)</td><td>177.02 (n/a)</td><td>177.40 (n/a)</td><td>129.60 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (+1.94%)</td><td>0.05 (-3.63%)</td><td>0.05 (-0.61%)</td><td>0.03 <b>(-23.16%)</b></td><td>0.01 <b>(+35.24%)</b></td><td>244.80 <b>(+30.14%)</b></td><td>177.56 (+6.87%)</td><td>178.90 (+0.62%)</td><td>121.30 (-1.86%)</td><td>45.40 <b>(+74.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>166.14 (n/a)</td><td>177.80 (n/a)</td><td>123.60 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (+4.18%)</td><td>0.06 (+5.22%)</td><td>0.06 (+9.46%)</td><td>0.04 (-2.48%)</td><td>0.01 <b>(+22.70%)</b></td><td>185.50 (+2.54%)</td><td>145.30 (-4.16%)</td><td>133.20 (-8.64%)</td><td>118.00 (-3.99%)</td><td>26.95 <b>(+21.81%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.90 (n/a)</td><td>151.60 (n/a)</td><td>145.80 (n/a)</td><td>122.90 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (-7.78%)</td><td>0.04 (-4.43%)</td><td>0.04 (-5.11%)</td><td>0.04 (+16.33%)</td><td>0.00 <b>(-51.30%)</b></td><td>227.00 (-14.02%)</td><td>213.78 (+1.91%)</td><td>222.00 (+5.41%)</td><td>178.90 (+8.42%)</td><td>19.83 <b>(-54.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.00 (n/a)</td><td>209.78 (n/a)</td><td>210.60 (n/a)</td><td>165.00 (n/a)</td><td>43.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+13.93%)</td><td>0.04 (+3.05%)</td><td>0.04 (-0.07%)</td><td>0.04 (-2.37%)</td><td>0.01 <b>(+101.04%)</b></td><td>222.00 (+2.45%)</td><td>193.40 (-1.73%)</td><td>199.20 (+0.10%)</td><td>153.40 (-12.19%)</td><td>27.18 <b>(+80.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>196.80 (n/a)</td><td>199.00 (n/a)</td><td>174.70 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (-8.30%)</td><td>0.05 (-4.00%)</td><td>0.05 (+1.47%)</td><td>0.04 (-9.73%)</td><td>0.01 (-15.26%)</td><td>230.20 (+10.78%)</td><td>167.26 (+3.64%)</td><td>149.50 (-1.45%)</td><td>138.40 (+8.98%)</td><td>38.26 (+3.84%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>161.38 (n/a)</td><td>151.70 (n/a)</td><td>127.00 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (+11.16%)</td><td>0.06 (+17.09%)</td><td>0.06 (+7.96%)</td><td>0.04 <b>(+32.12%)</b></td><td>0.01 <b>(-24.78%)</b></td><td>183.60 <b>(-24.32%)</b></td><td>150.24 (-17.43%)</td><td>140.90 (-7.36%)</td><td>124.40 (-10.05%)</td><td>24.93 <b>(-49.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.60 (n/a)</td><td>181.96 (n/a)</td><td>152.10 (n/a)</td><td>138.30 (n/a)</td><td>49.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 <b>(+20.70%)</b></td><td>0.05 (+4.60%)</td><td>0.05 (-9.53%)</td><td>0.04 (-7.13%)</td><td>0.01 <b>(+210.63%)</b></td><td>191.00 (+7.73%)</td><td>161.46 (-1.10%)</td><td>175.80 (+10.57%)</td><td>122.10 (-17.11%)</td><td>33.85 <b>(+175.71%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>163.26 (n/a)</td><td>159.00 (n/a)</td><td>147.30 (n/a)</td><td>12.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (-4.01%)</td><td>0.05 <b>(-23.87%)</b></td><td>0.05 <b>(-22.98%)</b></td><td>0.02 <b>(-55.48%)</b></td><td>0.01 <b>(+217.86%)</b></td><td>345.00 <b>(+124.61%)</b></td><td>199.94 <b>(+44.65%)</b></td><td>173.60 <b>(+29.84%)</b></td><td>134.80 (+4.17%)</td><td>83.00 <b>(+708.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>153.60 (n/a)</td><td>138.22 (n/a)</td><td>133.70 (n/a)</td><td>129.40 (n/a)</td><td>10.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+0.42%)</td><td>0.05 (-1.95%)</td><td>0.05 (-4.96%)</td><td>0.04 (-8.38%)</td><td>0.01 (+14.54%)</td><td>218.60 (+9.14%)</td><td>181.20 (+2.44%)</td><td>178.30 (+5.19%)</td><td>151.70 (-0.39%)</td><td>26.06 <b>(+21.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>176.88 (n/a)</td><td>169.50 (n/a)</td><td>152.30 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 <b>(+20.10%)</b></td><td>0.05 (+3.05%)</td><td>0.05 (-0.53%)</td><td>0.04 (-19.54%)</td><td>0.01 <b>(+244.50%)</b></td><td>228.00 <b>(+24.32%)</b></td><td>166.90 (+1.56%)</td><td>165.90 (+0.55%)</td><td>125.00 (-16.72%)</td><td>42.33 <b>(+244.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>164.34 (n/a)</td><td>165.00 (n/a)</td><td>150.10 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(-24.21%)</b></td><td>0.05 (-16.45%)</td><td>0.05 (-14.25%)</td><td>0.04 (-7.43%)</td><td>0.00 <b>(-56.83%)</b></td><td>182.90 (+8.03%)</td><td>169.06 (+18.04%)</td><td>168.90 (+16.64%)</td><td>148.30 <b>(+31.94%)</b></td><td>13.13 <b>(-38.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.30 (n/a)</td><td>143.22 (n/a)</td><td>144.80 (n/a)</td><td>112.40 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (+0.09%)</td><td>0.05 (-1.05%)</td><td>0.05 (-2.83%)</td><td>0.04 (+5.18%)</td><td>0.01 (-6.36%)</td><td>203.80 (-4.94%)</td><td>167.22 (+0.60%)</td><td>165.40 (+2.86%)</td><td>134.00 (-0.07%)</td><td>27.57 (-11.77%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>166.22 (n/a)</td><td>160.80 (n/a)</td><td>134.10 (n/a)</td><td>31.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (-11.50%)</td><td>0.04 <b>(-21.87%)</b></td><td>0.04 <b>(-28.46%)</b></td><td>0.03 <b>(-29.59%)</b></td><td>0.01 (+4.42%)</td><td>288.60 <b>(+42.03%)</b></td><td>205.10 <b>(+30.69%)</b></td><td>204.60 <b>(+39.75%)</b></td><td>146.00 (+13.00%)</td><td>52.88 <b>(+71.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>156.94 (n/a)</td><td>146.40 (n/a)</td><td>129.20 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (+15.28%)</td><td>0.05 (+7.00%)</td><td>0.05 (-12.15%)</td><td>0.03 <b>(+52.99%)</b></td><td>0.01 (-17.72%)</td><td>241.80 <b>(-34.63%)</b></td><td>178.62 (-12.88%)</td><td>179.10 (+13.86%)</td><td>131.60 (-13.25%)</td><td>42.85 <b>(-54.24%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>369.90 (n/a)</td><td>205.02 (n/a)</td><td>157.30 (n/a)</td><td>151.70 (n/a)</td><td>93.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (+12.74%)</td><td>0.05 (-8.47%)</td><td>0.04 (-15.15%)</td><td>0.04 (-18.04%)</td><td>0.01 <b>(+298.85%)</b></td><td>210.20 <b>(+22.07%)</b></td><td>180.90 (+12.10%)</td><td>189.20 (+17.88%)</td><td>137.20 (-11.31%)</td><td>31.90 <b>(+341.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>161.38 (n/a)</td><td>160.50 (n/a)</td><td>154.70 (n/a)</td><td>7.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (+7.29%)</td><td>0.06 (+6.75%)</td><td>0.05 (+5.26%)</td><td>0.04 (-13.25%)</td><td>0.01 <b>(+54.48%)</b></td><td>209.10 (+15.27%)</td><td>153.72 (-3.84%)</td><td>156.90 (-4.97%)</td><td>116.30 (-6.81%)</td><td>36.86 <b>(+65.33%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>159.86 (n/a)</td><td>165.10 (n/a)</td><td>124.80 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (+19.71%)</td><td>0.11 (+10.50%)</td><td>0.11 (+16.10%)</td><td>0.07 (-9.54%)</td><td>0.02 <b>(+54.91%)</b></td><td>231.50 (+10.55%)</td><td>159.04 (-7.04%)</td><td>145.80 (-13.88%)</td><td>119.40 (-16.50%)</td><td>42.65 <b>(+52.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.40 (n/a)</td><td>171.08 (n/a)</td><td>169.30 (n/a)</td><td>143.00 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (-16.96%)</td><td>0.10 (-11.42%)</td><td>0.09 (-7.04%)</td><td>0.08 (+2.93%)</td><td>0.02 <b>(-37.09%)</b></td><td>216.30 (-2.83%)</td><td>174.40 (+8.46%)</td><td>175.20 (+7.62%)</td><td>123.20 <b>(+20.43%)</b></td><td>34.40 <b>(-27.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.60 (n/a)</td><td>160.80 (n/a)</td><td>162.80 (n/a)</td><td>102.30 (n/a)</td><td>47.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (+7.79%)</td><td>0.07 (-6.42%)</td><td>0.07 (+1.31%)</td><td>0.05 <b>(-21.40%)</b></td><td>0.02 <b>(+94.81%)</b></td><td>299.80 <b>(+27.25%)</b></td><td>235.52 (+10.13%)</td><td>220.20 (-1.30%)</td><td>173.90 (-7.25%)</td><td>51.52 <b>(+135.90%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>213.86 (n/a)</td><td>223.10 (n/a)</td><td>187.50 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-10.51%)</td><td>0.09 (+3.75%)</td><td>0.09 (+8.97%)</td><td>0.06 (+15.75%)</td><td>0.02 <b>(-27.12%)</b></td><td>274.30 (-13.61%)</td><td>188.34 (-7.27%)</td><td>175.00 (-8.28%)</td><td>139.70 (+11.76%)</td><td>50.67 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>317.50 (n/a)</td><td>203.10 (n/a)</td><td>190.80 (n/a)</td><td>125.00 (n/a)</td><td>70.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (-2.80%)</td><td>0.11 (+5.27%)</td><td>0.12 (+3.30%)</td><td>0.09 (+9.51%)</td><td>0.02 (-13.34%)</td><td>192.20 (-8.69%)</td><td>152.28 (-6.50%)</td><td>137.70 (-3.23%)</td><td>121.60 (+2.88%)</td><td>32.63 <b>(-21.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>210.50 (n/a)</td><td>162.86 (n/a)</td><td>142.30 (n/a)</td><td>118.20 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (+4.36%)</td><td>0.11 (-2.46%)</td><td>0.10 (-7.64%)</td><td>0.09 (-7.23%)</td><td>0.02 <b>(+30.44%)</b></td><td>182.30 (+7.81%)</td><td>152.96 (+3.83%)</td><td>158.40 (+8.27%)</td><td>110.70 (-4.16%)</td><td>27.51 <b>(+33.62%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.10 (n/a)</td><td>147.32 (n/a)</td><td>146.30 (n/a)</td><td>115.50 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (-1.74%)</td><td>0.10 (-9.81%)</td><td>0.09 (-16.04%)</td><td>0.08 (-4.15%)</td><td>0.02 (+13.58%)</td><td>194.20 (+4.30%)</td><td>168.96 (+11.39%)</td><td>174.70 (+19.17%)</td><td>129.50 (+1.73%)</td><td>24.86 (+15.79%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>151.68 (n/a)</td><td>146.60 (n/a)</td><td>127.30 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (+9.10%)</td><td>0.10 (-10.06%)</td><td>0.10 (-17.04%)</td><td>0.08 (-14.91%)</td><td>0.02 <b>(+77.23%)</b></td><td>198.70 (+17.50%)</td><td>163.04 (+13.11%)</td><td>164.10 <b>(+20.48%)</b></td><td>122.20 (-8.33%)</td><td>27.67 <b>(+85.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.10 (n/a)</td><td>144.14 (n/a)</td><td>136.20 (n/a)</td><td>133.30 (n/a)</td><td>14.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 <b>(+24.69%)</b></td><td>0.10 (+6.77%)</td><td>0.08 (-8.73%)</td><td>0.08 <b>(+26.76%)</b></td><td>0.02 <b>(+32.66%)</b></td><td>206.20 <b>(-21.09%)</b></td><td>177.32 (-6.03%)</td><td>195.50 (+9.52%)</td><td>124.40 (-19.79%)</td><td>35.10 (-17.39%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>261.30 (n/a)</td><td>188.70 (n/a)</td><td>178.50 (n/a)</td><td>155.10 (n/a)</td><td>42.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 <b>(-31.35%)</b></td><td>0.09 (-12.67%)</td><td>0.09 (-2.39%)</td><td>0.08 (-5.81%)</td><td>0.01 <b>(-69.61%)</b></td><td>206.70 (+6.16%)</td><td>185.30 (+11.43%)</td><td>180.70 (+2.44%)</td><td>170.70 <b>(+45.65%)</b></td><td>14.60 <b>(-51.56%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.70 (n/a)</td><td>166.30 (n/a)</td><td>176.40 (n/a)</td><td>117.20 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 <b>(-25.93%)</b></td><td>0.09 <b>(-20.83%)</b></td><td>0.09 <b>(-22.99%)</b></td><td>0.07 <b>(-20.57%)</b></td><td>0.01 <b>(-43.16%)</b></td><td>252.00 <b>(+25.87%)</b></td><td>192.16 <b>(+24.29%)</b></td><td>176.20 <b>(+29.85%)</b></td><td>171.40 <b>(+34.96%)</b></td><td>34.14 (-0.70%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.20 (n/a)</td><td>154.60 (n/a)</td><td>135.70 (n/a)</td><td>127.00 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (-19.46%)</td><td>0.09 (-9.16%)</td><td>0.09 (+1.15%)</td><td>0.07 (-13.64%)</td><td>0.01 <b>(-29.68%)</b></td><td>239.50 (+15.76%)</td><td>183.40 (+9.18%)</td><td>176.60 (-1.12%)</td><td>156.20 <b>(+24.17%)</b></td><td>33.32 (+3.83%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>167.98 (n/a)</td><td>178.60 (n/a)</td><td>125.80 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (+6.34%)</td><td>0.08 (-0.36%)</td><td>0.08 (+4.59%)</td><td>0.05 <b>(-27.66%)</b></td><td>0.02 <b>(+109.40%)</b></td><td>320.70 <b>(+38.23%)</b></td><td>214.30 (+5.49%)</td><td>198.60 (-4.43%)</td><td>160.20 (-5.99%)</td><td>64.44 <b>(+177.17%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>203.14 (n/a)</td><td>207.80 (n/a)</td><td>170.40 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 <b>(-36.16%)</b></td><td>0.08 (-19.41%)</td><td>0.08 (-19.60%)</td><td>0.07 (-3.83%)</td><td>0.02 <b>(-56.93%)</b></td><td>239.90 (+3.94%)</td><td>202.26 (+17.47%)</td><td>208.30 <b>(+24.36%)</b></td><td>155.70 <b>(+56.64%)</b></td><td>36.23 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>230.80 (n/a)</td><td>172.18 (n/a)</td><td>167.50 (n/a)</td><td>99.40 (n/a)</td><td>49.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (-1.04%)</td><td>0.08 (+0.65%)</td><td>0.08 (+10.07%)</td><td>0.06 (-13.15%)</td><td>0.02 <b>(+20.74%)</b></td><td>262.30 (+15.14%)</td><td>209.84 (+0.98%)</td><td>199.80 (-9.14%)</td><td>154.90 (+1.04%)</td><td>45.33 <b>(+47.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>207.80 (n/a)</td><td>219.90 (n/a)</td><td>153.30 (n/a)</td><td>30.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-11.27%)</td><td>0.10 (-7.90%)</td><td>0.10 (-6.69%)</td><td>0.08 (+0.22%)</td><td>0.01 <b>(-30.99%)</b></td><td>204.60 (-0.20%)</td><td>170.00 (+6.96%)</td><td>168.30 (+7.13%)</td><td>137.10 (+12.75%)</td><td>25.06 <b>(-22.52%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.00 (n/a)</td><td>158.94 (n/a)</td><td>157.10 (n/a)</td><td>121.60 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (-10.95%)</td><td>0.22 (-0.69%)</td><td>0.22 (+13.79%)</td><td>0.16 (-13.60%)</td><td>0.05 (-3.41%)</td><td>206.90 (+15.72%)</td><td>158.66 (+1.43%)</td><td>150.30 (-12.16%)</td><td>122.20 (+12.32%)</td><td>36.19 <b>(+27.55%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>178.80 (n/a)</td><td>156.42 (n/a)</td><td>171.10 (n/a)</td><td>108.80 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (-1.06%)</td><td>0.20 (+7.43%)</td><td>0.19 (+11.71%)</td><td>0.18 <b>(+22.56%)</b></td><td>0.03 <b>(-36.33%)</b></td><td>177.40 (-18.44%)</td><td>161.76 (-9.03%)</td><td>172.40 (-10.49%)</td><td>132.20 (+1.07%)</td><td>18.77 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.50 (n/a)</td><td>177.82 (n/a)</td><td>192.60 (n/a)</td><td>130.80 (n/a)</td><td>35.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (-8.54%)</td><td>0.15 (+6.35%)</td><td>0.15 (+6.10%)</td><td>0.14 (+18.10%)</td><td>0.02 <b>(-45.49%)</b></td><td>240.80 (-15.33%)</td><td>216.54 (-7.87%)</td><td>219.30 (-5.76%)</td><td>187.30 (+9.34%)</td><td>21.66 <b>(-48.09%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>284.40 (n/a)</td><td>235.04 (n/a)</td><td>232.70 (n/a)</td><td>171.30 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (-1.55%)</td><td>0.17 (-0.84%)</td><td>0.16 (+6.21%)</td><td>0.15 (+12.07%)</td><td>0.03 <b>(-23.45%)</b></td><td>225.30 (-10.81%)</td><td>195.50 (-1.08%)</td><td>201.50 (-5.84%)</td><td>147.70 (+1.58%)</td><td>31.31 <b>(-29.30%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>252.60 (n/a)</td><td>197.64 (n/a)</td><td>214.00 (n/a)</td><td>145.40 (n/a)</td><td>44.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (-9.83%)</td><td>0.21 (+7.77%)</td><td>0.21 (+17.71%)</td><td>0.16 <b>(+87.63%)</b></td><td>0.03 <b>(-57.84%)</b></td><td>208.40 <b>(-46.71%)</b></td><td>162.30 <b>(-20.21%)</b></td><td>154.20 (-15.04%)</td><td>134.60 (+10.96%)</td><td>27.65 <b>(-74.75%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>391.10 (n/a)</td><td>203.42 (n/a)</td><td>181.50 (n/a)</td><td>121.30 (n/a)</td><td>109.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (+16.27%)</td><td>0.20 (+9.46%)</td><td>0.19 (+10.68%)</td><td>0.17 (+8.71%)</td><td>0.03 (+15.53%)</td><td>193.60 (-7.98%)</td><td>166.68 (-8.59%)</td><td>172.10 (-9.66%)</td><td>129.40 (-14.02%)</td><td>24.61 (-9.22%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.40 (n/a)</td><td>182.34 (n/a)</td><td>190.50 (n/a)</td><td>150.50 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (+5.22%)</td><td>0.21 (+11.78%)</td><td>0.20 (+18.07%)</td><td>0.16 (+8.39%)</td><td>0.04 (-1.20%)</td><td>198.70 (-7.71%)</td><td>161.94 (-10.92%)</td><td>161.50 (-15.31%)</td><td>131.50 (-4.92%)</td><td>28.11 (-14.66%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>215.30 (n/a)</td><td>181.80 (n/a)</td><td>190.70 (n/a)</td><td>138.30 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (-8.92%)</td><td>0.21 (+0.28%)</td><td>0.21 (+2.43%)</td><td>0.17 (+9.40%)</td><td>0.04 <b>(-26.08%)</b></td><td>195.00 (-8.58%)</td><td>159.68 (-2.08%)</td><td>159.60 (-2.39%)</td><td>123.00 (+9.72%)</td><td>27.37 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.30 (n/a)</td><td>163.08 (n/a)</td><td>163.50 (n/a)</td><td>112.10 (n/a)</td><td>36.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 <b>(-25.87%)</b></td><td>0.19 (-15.45%)</td><td>0.20 (+1.98%)</td><td>0.11 <b>(-31.59%)</b></td><td>0.05 <b>(-26.95%)</b></td><td>309.60 <b>(+46.18%)</b></td><td>190.46 (+18.99%)</td><td>160.20 (-1.96%)</td><td>147.10 <b>(+34.83%)</b></td><td>67.95 <b>(+49.83%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>211.80 (n/a)</td><td>160.06 (n/a)</td><td>163.40 (n/a)</td><td>109.10 (n/a)</td><td>45.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 (-12.35%)</td><td>0.18 (-3.78%)</td><td>0.19 (-4.77%)</td><td>0.16 (+8.44%)</td><td>0.01 <b>(-62.37%)</b></td><td>200.10 (-7.79%)</td><td>178.56 (+1.54%)</td><td>174.10 (+5.01%)</td><td>165.90 (+14.10%)</td><td>13.33 <b>(-59.73%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.00 (n/a)</td><td>175.86 (n/a)</td><td>165.80 (n/a)</td><td>145.40 (n/a)</td><td>33.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (-0.46%)</td><td>0.19 (-0.15%)</td><td>0.20 (+4.38%)</td><td>0.17 (+8.70%)</td><td>0.02 (-16.48%)</td><td>193.90 (-8.02%)</td><td>171.52 (-0.41%)</td><td>165.10 (-4.23%)</td><td>147.70 (+0.48%)</td><td>20.19 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>210.80 (n/a)</td><td>172.22 (n/a)</td><td>172.40 (n/a)</td><td>147.00 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (+1.49%)</td><td>0.19 (+13.62%)</td><td>0.19 (+13.90%)</td><td>0.17 <b>(+26.31%)</b></td><td>0.02 <b>(-42.68%)</b></td><td>190.90 <b>(-20.82%)</b></td><td>169.40 (-13.49%)</td><td>170.40 (-12.21%)</td><td>153.20 (-1.48%)</td><td>14.87 <b>(-55.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.10 (n/a)</td><td>195.82 (n/a)</td><td>194.10 (n/a)</td><td>155.50 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.23 (+3.31%)</td><td>0.20 <b>(+26.33%)</b></td><td>0.19 (+19.51%)</td><td>0.17 <b>(+59.00%)</b></td><td>0.02 <b>(-51.45%)</b></td><td>193.10 <b>(-37.12%)</b></td><td>168.20 <b>(-25.38%)</b></td><td>171.30 (-16.32%)</td><td>141.90 (-3.21%)</td><td>18.60 <b>(-71.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>307.10 (n/a)</td><td>225.40 (n/a)</td><td>204.70 (n/a)</td><td>146.60 (n/a)</td><td>64.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 <b>(-23.75%)</b></td><td>0.18 (-16.82%)</td><td>0.18 (-16.65%)</td><td>0.16 (-2.86%)</td><td>0.02 <b>(-61.84%)</b></td><td>210.70 (+2.93%)</td><td>184.38 (+16.21%)</td><td>183.30 (+19.96%)</td><td>159.10 <b>(+31.16%)</b></td><td>19.03 <b>(-48.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.70 (n/a)</td><td>158.66 (n/a)</td><td>152.80 (n/a)</td><td>121.30 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 <b>(-20.45%)</b></td><td>0.16 (-18.28%)</td><td>0.15 <b>(-23.57%)</b></td><td>0.12 (-10.15%)</td><td>0.03 (-16.55%)</td><td>263.80 (+11.31%)</td><td>216.82 <b>(+22.28%)</b></td><td>222.20 <b>(+30.78%)</b></td><td>166.60 <b>(+25.74%)</b></td><td>43.53 (+14.86%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.00 (n/a)</td><td>177.32 (n/a)</td><td>169.90 (n/a)</td><td>132.50 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (-16.05%)</td><td>0.18 (-11.84%)</td><td>0.18 (-5.64%)</td><td>0.15 (-12.55%)</td><td>0.01 <b>(-34.86%)</b></td><td>213.70 (+14.34%)</td><td>187.00 (+12.96%)</td><td>182.20 (+5.93%)</td><td>169.40 (+19.13%)</td><td>16.48 (-9.35%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>165.54 (n/a)</td><td>172.00 (n/a)</td><td>142.20 (n/a)</td><td>18.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+23.40%)</b></td><td>0.03 <b>(+27.26%)</b></td><td>0.03 <b>(+29.39%)</b></td><td>0.03 (+15.61%)</td><td>0.00 <b>(+45.74%)</b></td><td>158.10 (-13.51%)</td><td>133.76 <b>(-20.89%)</b></td><td>134.10 <b>(-22.71%)</b></td><td>108.70 (-18.94%)</td><td>20.87 (+3.85%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.80 (n/a)</td><td>169.08 (n/a)</td><td>173.50 (n/a)</td><td>134.10 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (+11.11%)</td><td>0.05 <b>(+31.44%)</b></td><td>0.05 <b>(+34.32%)</b></td><td>0.04 <b>(+41.39%)</b></td><td>0.00 <b>(-40.22%)</b></td><td>149.50 <b>(-29.28%)</b></td><td>134.66 <b>(-25.51%)</b></td><td>129.90 <b>(-25.56%)</b></td><td>120.80 (-9.99%)</td><td>12.09 <b>(-62.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>180.78 (n/a)</td><td>174.50 (n/a)</td><td>134.20 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+3.66%)</td><td>0.03 (+2.38%)</td><td>0.03 <b>(+20.74%)</b></td><td>0.02 (-15.07%)</td><td>0.01 <b>(+44.95%)</b></td><td>231.40 (+17.76%)</td><td>163.42 (+0.28%)</td><td>140.70 (-17.14%)</td><td>132.50 (-3.50%)</td><td>41.96 <b>(+68.17%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>162.96 (n/a)</td><td>169.80 (n/a)</td><td>137.30 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.04 <b>(+37.66%)</b></td><td>0.03 (+13.60%)</td><td>0.03 (-2.26%)</td><td>0.02 (-4.37%)</td><td>0.01 <b>(+324.22%)</b></td><td>206.80 (+4.55%)</td><td>169.92 (-7.04%)</td><td>189.80 (+2.32%)</td><td>117.80 <b>(-27.33%)</b></td><td>43.37 <b>(+231.48%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.80 (n/a)</td><td>182.78 (n/a)</td><td>185.50 (n/a)</td><td>162.10 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+10.10%)</td><td>0.03 <b>(+22.59%)</b></td><td>0.03 (+15.34%)</td><td>0.03 <b>(+43.67%)</b></td><td>0.00 <b>(-57.88%)</b></td><td>155.70 <b>(-30.37%)</b></td><td>147.56 (-19.93%)</td><td>150.70 (-13.29%)</td><td>135.60 (-9.18%)</td><td>7.88 <b>(-73.74%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>184.28 (n/a)</td><td>173.80 (n/a)</td><td>149.30 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+6.04%)</td><td>0.03 (+6.96%)</td><td>0.03 (+15.98%)</td><td>0.02 (-2.99%)</td><td>0.00 (+19.00%)</td><td>234.30 (+3.08%)</td><td>192.40 (-6.07%)</td><td>182.50 (-13.79%)</td><td>159.10 (-5.69%)</td><td>28.81 (+15.95%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.30 (n/a)</td><td>204.84 (n/a)</td><td>211.70 (n/a)</td><td>168.70 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+13.23%)</td><td>0.03 (+9.96%)</td><td>0.03 (+10.66%)</td><td>0.02 (+2.11%)</td><td>0.01 <b>(+57.22%)</b></td><td>203.10 (-2.03%)</td><td>160.52 (-7.61%)</td><td>159.60 (-9.63%)</td><td>127.10 (-11.67%)</td><td>31.32 <b>(+34.48%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.30 (n/a)</td><td>173.74 (n/a)</td><td>176.60 (n/a)</td><td>143.90 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+17.63%)</td><td>0.03 (+13.29%)</td><td>0.03 <b>(+20.65%)</b></td><td>0.02 (-1.14%)</td><td>0.01 <b>(+82.08%)</b></td><td>238.20 (+1.15%)</td><td>174.10 (-8.84%)</td><td>151.10 (-17.11%)</td><td>134.10 (-14.97%)</td><td>45.50 <b>(+54.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.50 (n/a)</td><td>190.98 (n/a)</td><td>182.30 (n/a)</td><td>157.70 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-3.46%)</td><td>0.02 (-3.04%)</td><td>0.02 (-1.53%)</td><td>0.02 (-1.59%)</td><td>0.00 (-3.70%)</td><td>191.30 (+1.59%)</td><td>173.80 (+3.11%)</td><td>173.00 (+1.53%)</td><td>153.10 (+3.59%)</td><td>14.84 (+1.84%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.30 (n/a)</td><td>168.56 (n/a)</td><td>170.40 (n/a)</td><td>147.80 (n/a)</td><td>14.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 <b>(-24.82%)</b></td><td>0.02 (-17.70%)</td><td>0.02 (-14.07%)</td><td>0.02 <b>(-20.88%)</b></td><td>0.00 <b>(-36.02%)</b></td><td>278.10 <b>(+26.41%)</b></td><td>210.12 (+19.55%)</td><td>215.00 (+16.40%)</td><td>155.20 <b>(+32.99%)</b></td><td>45.39 (+7.99%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>175.76 (n/a)</td><td>184.70 (n/a)</td><td>116.70 (n/a)</td><td>42.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 <b>(-30.62%)</b></td><td>0.02 (-12.21%)</td><td>0.02 (-8.16%)</td><td>0.02 <b>(+49.63%)</b></td><td>0.00 <b>(-73.19%)</b></td><td>216.20 <b>(-33.19%)</b></td><td>200.30 (+2.51%)</td><td>206.30 (+8.87%)</td><td>166.80 <b>(+44.04%)</b></td><td>19.31 <b>(-75.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>323.60 (n/a)</td><td>195.40 (n/a)</td><td>189.50 (n/a)</td><td>115.80 (n/a)</td><td>78.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (+9.06%)</td><td>0.02 (+11.08%)</td><td>0.02 (+7.57%)</td><td>0.02 (+7.59%)</td><td>0.00 (+19.97%)</td><td>215.50 (-7.07%)</td><td>186.62 (-9.70%)</td><td>195.30 (-7.04%)</td><td>152.70 (-8.34%)</td><td>26.51 (+2.32%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.90 (n/a)</td><td>206.66 (n/a)</td><td>210.10 (n/a)</td><td>166.60 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 <b>(-27.76%)</b></td><td>0.02 (-19.09%)</td><td>0.02 <b>(-23.43%)</b></td><td>0.02 <b>(+23.65%)</b></td><td>0.00 <b>(-66.41%)</b></td><td>236.00 (-19.12%)</td><td>200.44 (+12.22%)</td><td>197.80 <b>(+30.56%)</b></td><td>164.50 <b>(+38.47%)</b></td><td>27.56 <b>(-61.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>291.80 (n/a)</td><td>178.62 (n/a)</td><td>151.50 (n/a)</td><td>118.80 (n/a)</td><td>72.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.03 (-0.31%)</td><td>0.02 (+4.61%)</td><td>0.02 (+9.67%)</td><td>0.02 (+14.50%)</td><td>0.00 (-8.81%)</td><td>278.90 (-12.65%)</td><td>218.24 (-5.56%)</td><td>202.80 (-8.81%)</td><td>159.90 (+0.31%)</td><td>46.44 (-19.44%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>319.30 (n/a)</td><td>231.08 (n/a)</td><td>222.40 (n/a)</td><td>159.40 (n/a)</td><td>57.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.02 (-6.92%)</td><td>0.02 (+8.87%)</td><td>0.02 (+4.07%)</td><td>0.02 <b>(+52.66%)</b></td><td>0.00 <b>(-57.58%)</b></td><td>244.40 <b>(-34.49%)</b></td><td>211.54 (-13.09%)</td><td>203.90 (-3.91%)</td><td>190.20 (+7.46%)</td><td>21.70 <b>(-71.53%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>373.10 (n/a)</td><td>243.40 (n/a)</td><td>212.20 (n/a)</td><td>177.00 (n/a)</td><td>76.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (-13.70%)</td><td>0.05 (-3.17%)</td><td>0.05 (-5.42%)</td><td>0.04 (+5.28%)</td><td>0.01 <b>(-36.14%)</b></td><td>218.50 (-5.00%)</td><td>174.76 (+0.68%)</td><td>175.70 (+5.72%)</td><td>148.70 (+15.90%)</td><td>28.79 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.00 (n/a)</td><td>173.58 (n/a)</td><td>166.20 (n/a)</td><td>128.30 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (+1.54%)</td><td>0.07 (-6.72%)</td><td>0.07 (-7.33%)</td><td>0.05 <b>(-22.35%)</b></td><td>0.02 <b>(+60.48%)</b></td><td>247.70 <b>(+28.81%)</b></td><td>179.28 (+11.91%)</td><td>179.20 (+7.89%)</td><td>127.10 (-1.55%)</td><td>50.35 <b>(+99.82%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>160.20 (n/a)</td><td>166.10 (n/a)</td><td>129.10 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (-18.95%)</td><td>0.04 (-15.41%)</td><td>0.04 (-12.61%)</td><td>0.03 (-14.11%)</td><td>0.01 <b>(-20.05%)</b></td><td>263.00 (+16.42%)</td><td>195.04 (+17.85%)</td><td>182.70 (+14.40%)</td><td>156.70 <b>(+23.39%)</b></td><td>41.99 (+13.36%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>165.50 (n/a)</td><td>159.70 (n/a)</td><td>127.00 (n/a)</td><td>37.04 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (+0.00%)</td><td>0.06 (-3.45%)</td><td>0.06 (-5.97%)</td><td>0.05 (+2.22%)</td><td>0.01 (-8.85%)</td><td>192.90 (-2.18%)</td><td>175.66 (+3.37%)</td><td>176.60 (+6.32%)</td><td>149.40 (+0.00%)</td><td>16.14 (-13.10%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>169.94 (n/a)</td><td>166.10 (n/a)</td><td>149.40 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (-6.03%)</td><td>0.05 (+12.86%)</td><td>0.05 (+11.14%)</td><td>0.04 <b>(+45.14%)</b></td><td>0.01 <b>(-49.46%)</b></td><td>203.70 <b>(-31.11%)</b></td><td>166.12 (-16.13%)</td><td>160.40 (-10.04%)</td><td>148.60 (+6.37%)</td><td>22.48 <b>(-63.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.70 (n/a)</td><td>198.06 (n/a)</td><td>178.30 (n/a)</td><td>139.70 (n/a)</td><td>61.51 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.09 (+12.32%)</td><td>0.07 (+7.23%)</td><td>0.06 (+9.76%)</td><td>0.05 (+2.35%)</td><td>0.02 (+15.12%)</td><td>199.20 (-2.31%)</td><td>161.16 (-6.25%)</td><td>175.00 (-8.90%)</td><td>112.50 (-11.00%)</td><td>36.74 (-0.82%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>171.90 (n/a)</td><td>192.10 (n/a)</td><td>126.40 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 <b>(+35.55%)</b></td><td>0.05 (+11.88%)</td><td>0.05 (+5.20%)</td><td>0.04 (-6.46%)</td><td>0.01 <b>(+120.30%)</b></td><td>226.20 (+6.90%)</td><td>169.76 (-7.86%)</td><td>168.00 (-4.92%)</td><td>120.50 <b>(-26.25%)</b></td><td>38.52 <b>(+73.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>184.24 (n/a)</td><td>176.70 (n/a)</td><td>163.40 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.07 (-15.69%)</td><td>0.06 (+18.16%)</td><td>0.06 <b>(+30.99%)</b></td><td>0.06 <b>(+47.57%)</b></td><td>0.01 <b>(-70.32%)</b></td><td>162.50 <b>(-32.21%)</b></td><td>150.52 <b>(-20.34%)</b></td><td>149.50 <b>(-23.65%)</b></td><td>133.80 (+18.62%)</td><td>12.10 <b>(-74.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>239.70 (n/a)</td><td>188.96 (n/a)</td><td>195.80 (n/a)</td><td>112.80 (n/a)</td><td>47.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (-13.26%)</td><td>0.04 (-0.42%)</td><td>0.04 (-6.78%)</td><td>0.04 <b>(+33.59%)</b></td><td>0.01 <b>(-46.48%)</b></td><td>220.40 <b>(-25.16%)</b></td><td>186.18 (-4.86%)</td><td>186.40 (+7.25%)</td><td>152.50 (+15.27%)</td><td>28.01 <b>(-55.02%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.50 (n/a)</td><td>195.70 (n/a)</td><td>173.80 (n/a)</td><td>132.30 (n/a)</td><td>62.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.08 <b>(-20.01%)</b></td><td>0.06 (+6.71%)</td><td>0.05 (+14.02%)</td><td>0.05 <b>(+20.03%)</b></td><td>0.01 <b>(-50.31%)</b></td><td>187.10 (-16.70%)</td><td>161.78 (-12.56%)</td><td>176.30 (-12.29%)</td><td>120.10 <b>(+24.97%)</b></td><td>27.94 <b>(-45.13%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>224.60 (n/a)</td><td>185.02 (n/a)</td><td>201.00 (n/a)</td><td>96.10 (n/a)</td><td>50.92 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+22.33%)</b></td><td>0.05 (+10.68%)</td><td>0.04 (+5.03%)</td><td>0.04 (+8.04%)</td><td>0.01 <b>(+41.40%)</b></td><td>216.50 (-7.44%)</td><td>180.16 (-9.04%)</td><td>182.90 (-4.79%)</td><td>138.40 (-18.30%)</td><td>28.39 (+4.74%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>198.06 (n/a)</td><td>192.10 (n/a)</td><td>169.40 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 (-9.14%)</td><td>0.04 (-9.67%)</td><td>0.04 (+2.07%)</td><td>0.03 <b>(-27.40%)</b></td><td>0.01 (+17.30%)</td><td>298.70 <b>(+37.78%)</b></td><td>222.76 (+13.19%)</td><td>204.10 (-2.02%)</td><td>162.50 (+10.02%)</td><td>52.20 <b>(+82.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>196.80 (n/a)</td><td>208.30 (n/a)</td><td>147.70 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 (+7.47%)</td><td>0.05 (+17.21%)</td><td>0.04 (+2.23%)</td><td>0.04 <b>(+39.41%)</b></td><td>0.01 (-0.42%)</td><td>210.70 <b>(-28.26%)</b></td><td>178.00 (-16.22%)</td><td>197.10 (-2.18%)</td><td>137.80 (-6.95%)</td><td>36.29 <b>(-35.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.70 (n/a)</td><td>212.46 (n/a)</td><td>201.50 (n/a)</td><td>148.10 (n/a)</td><td>55.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.05 <b>(+26.29%)</b></td><td>0.04 <b>(+20.18%)</b></td><td>0.05 (+13.90%)</td><td>0.04 <b>(+41.58%)</b></td><td>0.01 (+2.57%)</td><td>235.10 <b>(-29.36%)</b></td><td>198.82 (-17.90%)</td><td>188.20 (-12.18%)</td><td>160.00 <b>(-20.83%)</b></td><td>30.53 <b>(-42.82%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>332.80 (n/a)</td><td>242.16 (n/a)</td><td>214.30 (n/a)</td><td>202.10 (n/a)</td><td>53.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.06 <b>(+33.10%)</b></td><td>0.04 <b>(+26.64%)</b></td><td>0.04 (+5.78%)</td><td>0.03 <b>(+49.80%)</b></td><td>0.01 (-8.41%)</td><td>238.30 <b>(-33.25%)</b></td><td>198.66 <b>(-24.52%)</b></td><td>204.50 (-5.46%)</td><td>143.30 <b>(-24.90%)</b></td><td>36.01 <b>(-56.71%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>357.00 (n/a)</td><td>263.20 (n/a)</td><td>216.30 (n/a)</td><td>190.80 (n/a)</td><td>83.19 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (+11.47%)</td><td>0.11 (+17.96%)</td><td>0.11 (+14.25%)</td><td>0.10 <b>(+42.87%)</b></td><td>0.01 <b>(-24.55%)</b></td><td>168.30 <b>(-30.02%)</b></td><td>147.92 (-17.10%)</td><td>146.10 (-12.46%)</td><td>123.60 (-10.30%)</td><td>18.37 <b>(-53.15%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.50 (n/a)</td><td>178.44 (n/a)</td><td>166.90 (n/a)</td><td>137.80 (n/a)</td><td>39.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 <b>(+42.42%)</b></td><td>0.16 <b>(+30.46%)</b></td><td>0.16 <b>(+32.70%)</b></td><td>0.11 (+13.01%)</td><td>0.04 <b>(+96.96%)</b></td><td>218.50 (-11.54%)</td><td>163.52 <b>(-21.28%)</b></td><td>149.30 <b>(-24.67%)</b></td><td>123.50 <b>(-29.83%)</b></td><td>40.39 <b>(+22.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>247.00 (n/a)</td><td>207.72 (n/a)</td><td>198.20 (n/a)</td><td>176.00 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 <b>(-22.26%)</b></td><td>0.11 (-11.87%)</td><td>0.10 (-6.34%)</td><td>0.09 (-10.45%)</td><td>0.01 <b>(-45.94%)</b></td><td>180.20 (+11.65%)</td><td>154.62 (+11.24%)</td><td>159.60 (+6.76%)</td><td>130.00 <b>(+28.59%)</b></td><td>20.11 <b>(-24.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>161.40 (n/a)</td><td>139.00 (n/a)</td><td>149.50 (n/a)</td><td>101.10 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 <b>(+32.42%)</b></td><td>0.12 (+16.25%)</td><td>0.12 (+1.71%)</td><td>0.08 (+2.46%)</td><td>0.03 <b>(+60.18%)</b></td><td>242.70 (-2.41%)</td><td>176.60 (-12.07%)</td><td>177.90 (-1.71%)</td><td>120.40 <b>(-24.51%)</b></td><td>44.27 (+14.56%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>200.84 (n/a)</td><td>181.00 (n/a)</td><td>159.50 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-6.09%)</td><td>0.10 (-5.96%)</td><td>0.10 (-9.72%)</td><td>0.09 (+8.35%)</td><td>0.01 <b>(-34.26%)</b></td><td>176.30 (-7.70%)</td><td>161.82 (+5.21%)</td><td>163.90 (+10.74%)</td><td>137.20 (+6.44%)</td><td>15.32 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.00 (n/a)</td><td>153.80 (n/a)</td><td>148.00 (n/a)</td><td>128.90 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.16 (-1.48%)</td><td>0.11 (-11.49%)</td><td>0.09 <b>(-22.58%)</b></td><td>0.09 (-19.65%)</td><td>0.03 <b>(+62.03%)</b></td><td>233.00 <b>(+24.47%)</b></td><td>191.40 (+17.50%)</td><td>216.50 <b>(+29.18%)</b></td><td>130.90 (+1.47%)</td><td>47.24 <b>(+110.80%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.20 (n/a)</td><td>162.90 (n/a)</td><td>167.60 (n/a)</td><td>129.00 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (-8.55%)</td><td>0.10 (-0.18%)</td><td>0.10 (+0.46%)</td><td>0.09 (+15.38%)</td><td>0.01 <b>(-52.88%)</b></td><td>176.30 (-13.32%)</td><td>166.40 (-1.27%)</td><td>171.10 (-0.47%)</td><td>147.60 (+9.33%)</td><td>11.21 <b>(-55.53%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.40 (n/a)</td><td>168.54 (n/a)</td><td>171.90 (n/a)</td><td>135.00 (n/a)</td><td>25.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (+11.75%)</td><td>0.10 (+0.10%)</td><td>0.09 (-5.32%)</td><td>0.07 (-12.56%)</td><td>0.02 <b>(+116.89%)</b></td><td>246.00 (+14.37%)</td><td>196.12 (+1.74%)</td><td>197.30 (+5.62%)</td><td>159.90 (-10.52%)</td><td>34.03 <b>(+120.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>192.76 (n/a)</td><td>186.80 (n/a)</td><td>178.70 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (-7.76%)</td><td>0.11 (+11.99%)</td><td>0.11 <b>(+21.61%)</b></td><td>0.10 (+17.77%)</td><td>0.01 <b>(-46.10%)</b></td><td>168.50 (-15.07%)</td><td>148.64 (-13.15%)</td><td>150.80 (-17.78%)</td><td>124.20 (+8.38%)</td><td>16.82 <b>(-48.53%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.40 (n/a)</td><td>171.14 (n/a)</td><td>183.40 (n/a)</td><td>114.60 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-14.33%)</td><td>0.10 (-7.01%)</td><td>0.09 (+7.46%)</td><td>0.07 (-13.96%)</td><td>0.02 <b>(-29.48%)</b></td><td>263.30 (+16.20%)</td><td>195.14 (+5.78%)</td><td>194.70 (-6.93%)</td><td>157.60 (+16.74%)</td><td>42.93 (-3.42%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>226.60 (n/a)</td><td>184.48 (n/a)</td><td>209.20 (n/a)</td><td>135.00 (n/a)</td><td>44.45 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (-11.04%)</td><td>0.09 (+4.03%)</td><td>0.09 (+15.80%)</td><td>0.07 (-7.83%)</td><td>0.01 (-19.16%)</td><td>245.10 (+8.50%)</td><td>185.46 (-4.44%)</td><td>177.60 (-13.62%)</td><td>160.40 (+12.40%)</td><td>34.85 (-1.50%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.90 (n/a)</td><td>194.08 (n/a)</td><td>205.60 (n/a)</td><td>142.70 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 (+1.97%)</td><td>0.09 (-1.53%)</td><td>0.09 (-1.30%)</td><td>0.06 (-16.24%)</td><td>0.01 <b>(+51.85%)</b></td><td>278.00 (+19.42%)</td><td>209.70 (+3.12%)</td><td>197.60 (+1.28%)</td><td>180.60 (-1.95%)</td><td>39.52 <b>(+83.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>203.36 (n/a)</td><td>195.10 (n/a)</td><td>184.20 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (+14.17%)</td><td>0.10 (+17.71%)</td><td>0.10 <b>(+23.26%)</b></td><td>0.08 <b>(+41.86%)</b></td><td>0.02 (-17.92%)</td><td>215.10 <b>(-29.50%)</b></td><td>175.02 (-17.62%)</td><td>170.30 (-18.90%)</td><td>136.30 (-12.40%)</td><td>28.82 <b>(-50.14%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>305.10 (n/a)</td><td>212.46 (n/a)</td><td>210.00 (n/a)</td><td>155.60 (n/a)</td><td>57.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (+2.67%)</td><td>0.09 (+1.09%)</td><td>0.08 (-0.30%)</td><td>0.07 (-9.77%)</td><td>0.02 <b>(+44.27%)</b></td><td>244.10 (+10.80%)</td><td>203.74 (+0.47%)</td><td>210.70 (+0.29%)</td><td>158.60 (-2.58%)</td><td>37.24 <b>(+56.41%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>202.78 (n/a)</td><td>210.10 (n/a)</td><td>162.80 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 <b>(+32.81%)</b></td><td>0.08 (+12.80%)</td><td>0.07 (+8.23%)</td><td>0.04 (-4.37%)</td><td>0.03 <b>(+61.92%)</b></td><td>368.10 (+4.54%)</td><td>248.86 (-4.82%)</td><td>223.20 (-7.62%)</td><td>128.70 <b>(-24.69%)</b></td><td>101.12 <b>(+27.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>352.10 (n/a)</td><td>261.46 (n/a)</td><td>241.60 (n/a)</td><td>170.90 (n/a)</td><td>79.31 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (-10.70%)</td><td>0.18 (-9.50%)</td><td>0.18 (-8.96%)</td><td>0.13 (-19.84%)</td><td>0.03 (+11.55%)</td><td>247.20 <b>(+24.79%)</b></td><td>189.58 (+11.83%)</td><td>185.80 (+9.81%)</td><td>152.80 (+12.02%)</td><td>36.98 <b>(+57.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.10 (n/a)</td><td>169.52 (n/a)</td><td>169.20 (n/a)</td><td>136.40 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 <b>(+28.56%)</b></td><td>0.19 (+7.07%)</td><td>0.20 (+8.85%)</td><td>0.11 <b>(-22.45%)</b></td><td>0.07 <b>(+171.93%)</b></td><td>297.60 <b>(+28.94%)</b></td><td>199.60 (+4.36%)</td><td>167.50 (-8.12%)</td><td>120.70 <b>(-22.23%)</b></td><td>80.84 <b>(+182.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>230.80 (n/a)</td><td>191.26 (n/a)</td><td>182.30 (n/a)</td><td>155.20 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.36 <b>(+26.91%)</b></td><td>0.27 (+12.12%)</td><td>0.23 (+0.50%)</td><td>0.21 (+13.77%)</td><td>0.06 <b>(+73.10%)</b></td><td>190.60 (-12.08%)</td><td>160.36 (-9.03%)</td><td>176.70 (-0.51%)</td><td>114.70 <b>(-21.22%)</b></td><td>32.85 <b>(+20.75%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>216.80 (n/a)</td><td>176.28 (n/a)</td><td>177.60 (n/a)</td><td>145.60 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 <b>(+52.41%)</b></td><td>0.20 <b>(+23.28%)</b></td><td>0.18 (+1.51%)</td><td>0.16 (+17.43%)</td><td>0.05 <b>(+93.38%)</b></td><td>206.00 (-14.84%)</td><td>167.96 (-17.24%)</td><td>177.60 (-1.50%)</td><td>116.10 <b>(-34.41%)</b></td><td>35.02 (+6.23%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.90 (n/a)</td><td>202.94 (n/a)</td><td>180.30 (n/a)</td><td>177.00 (n/a)</td><td>32.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.33 <b>(+26.38%)</b></td><td>0.27 <b>(+35.44%)</b></td><td>0.26 <b>(+33.41%)</b></td><td>0.23 <b>(+82.21%)</b></td><td>0.03 <b>(-30.08%)</b></td><td>175.10 <b>(-45.13%)</b></td><td>152.76 <b>(-29.40%)</b></td><td>156.90 <b>(-25.04%)</b></td><td>125.40 <b>(-20.83%)</b></td><td>18.15 <b>(-70.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>319.10 (n/a)</td><td>216.38 (n/a)</td><td>209.30 (n/a)</td><td>158.40 (n/a)</td><td>62.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 <b>(+26.26%)</b></td><td>0.20 <b>(+24.19%)</b></td><td>0.20 <b>(+20.63%)</b></td><td>0.16 (+15.22%)</td><td>0.03 <b>(+42.74%)</b></td><td>204.40 (-13.21%)</td><td>163.44 (-19.03%)</td><td>162.80 (-17.11%)</td><td>134.90 <b>(-20.83%)</b></td><td>26.36 (-1.72%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>235.50 (n/a)</td><td>201.86 (n/a)</td><td>196.40 (n/a)</td><td>170.40 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (+12.76%)</td><td>0.22 (+12.21%)</td><td>0.22 (+13.28%)</td><td>0.19 (+18.47%)</td><td>0.03 (+18.40%)</td><td>195.60 (-15.58%)</td><td>171.74 (-10.80%)</td><td>166.50 (-11.76%)</td><td>143.50 (-11.31%)</td><td>22.52 (-10.23%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>231.70 (n/a)</td><td>192.54 (n/a)</td><td>188.70 (n/a)</td><td>161.80 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (+17.73%)</td><td>0.20 <b>(+22.00%)</b></td><td>0.19 (+6.15%)</td><td>0.17 <b>(+63.21%)</b></td><td>0.03 <b>(-24.90%)</b></td><td>187.30 <b>(-38.71%)</b></td><td>165.26 <b>(-21.33%)</b></td><td>169.50 (-5.78%)</td><td>131.30 (-15.07%)</td><td>23.65 <b>(-61.12%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>305.60 (n/a)</td><td>210.08 (n/a)</td><td>179.90 (n/a)</td><td>154.60 (n/a)</td><td>60.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.29 <b>(+39.76%)</b></td><td>0.23 <b>(+31.77%)</b></td><td>0.24 <b>(+38.59%)</b></td><td>0.14 (+5.92%)</td><td>0.06 <b>(+78.69%)</b></td><td>266.20 (-5.60%)</td><td>169.58 <b>(-21.29%)</b></td><td>154.90 <b>(-27.85%)</b></td><td>125.60 <b>(-28.47%)</b></td><td>55.48 <b>(+29.93%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>282.00 (n/a)</td><td>215.44 (n/a)</td><td>214.70 (n/a)</td><td>175.60 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (+5.61%)</td><td>0.19 (-3.25%)</td><td>0.19 (-2.81%)</td><td>0.15 (+5.08%)</td><td>0.04 (-0.56%)</td><td>215.20 (-4.82%)</td><td>174.76 (+3.03%)</td><td>171.50 (+2.88%)</td><td>128.40 (-5.31%)</td><td>33.92 (-8.47%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>226.10 (n/a)</td><td>169.62 (n/a)</td><td>166.70 (n/a)</td><td>135.60 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.22 (+18.20%)</td><td>0.18 (+17.82%)</td><td>0.17 (+3.33%)</td><td>0.13 <b>(+28.19%)</b></td><td>0.04 <b>(+21.64%)</b></td><td>274.00 <b>(-22.00%)</b></td><td>206.22 (-15.48%)</td><td>210.80 (-3.21%)</td><td>160.00 (-15.39%)</td><td>47.52 <b>(-25.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>351.30 (n/a)</td><td>243.98 (n/a)</td><td>217.80 (n/a)</td><td>189.10 (n/a)</td><td>63.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (+3.12%)</td><td>0.18 (-6.11%)</td><td>0.19 (+11.88%)</td><td>0.09 <b>(-41.73%)</b></td><td>0.06 <b>(+46.80%)</b></td><td>362.00 <b>(+71.56%)</b></td><td>207.14 (+15.60%)</td><td>169.60 (-10.60%)</td><td>132.70 (-3.00%)</td><td>90.20 <b>(+157.28%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.00 (n/a)</td><td>179.18 (n/a)</td><td>189.70 (n/a)</td><td>136.80 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (+14.03%)</td><td>0.19 (+18.06%)</td><td>0.20 (+10.77%)</td><td>0.15 <b>(+37.33%)</b></td><td>0.03 <b>(-22.00%)</b></td><td>238.70 <b>(-27.18%)</b></td><td>185.16 (-17.57%)</td><td>172.40 (-9.74%)</td><td>164.00 (-12.30%)</td><td>30.65 <b>(-49.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>327.80 (n/a)</td><td>224.64 (n/a)</td><td>191.00 (n/a)</td><td>187.00 (n/a)</td><td>60.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (+17.73%)</td><td>0.19 <b>(+22.34%)</b></td><td>0.19 <b>(+25.19%)</b></td><td>0.15 (+11.22%)</td><td>0.02 <b>(+29.23%)</b></td><td>215.20 (-10.11%)</td><td>177.76 (-18.01%)</td><td>175.40 <b>(-20.09%)</b></td><td>154.10 (-15.05%)</td><td>22.77 (+2.02%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>239.40 (n/a)</td><td>216.82 (n/a)</td><td>219.50 (n/a)</td><td>181.40 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.17 (+5.55%)</td><td>0.13 (-4.84%)</td><td>0.13 (+3.38%)</td><td>0.10 (-16.54%)</td><td>0.03 <b>(+53.74%)</b></td><td>208.70 (+19.80%)</td><td>161.42 (+7.79%)</td><td>151.70 (-3.31%)</td><td>120.30 (-5.20%)</td><td>36.25 <b>(+80.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>174.20 (n/a)</td><td>149.76 (n/a)</td><td>156.90 (n/a)</td><td>126.90 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 <b>(+21.64%)</b></td><td>0.13 (+1.72%)</td><td>0.13 (+0.27%)</td><td>0.09 <b>(-29.14%)</b></td><td>0.04 <b>(+223.84%)</b></td><td>240.70 <b>(+41.09%)</b></td><td>163.76 (+4.59%)</td><td>154.40 (-0.32%)</td><td>113.10 (-17.81%)</td><td>49.79 <b>(+277.16%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>170.60 (n/a)</td><td>156.58 (n/a)</td><td>154.90 (n/a)</td><td>137.60 (n/a)</td><td>13.20 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (-8.81%)</td><td>0.12 (-11.94%)</td><td>0.10 <b>(-26.15%)</b></td><td>0.10 (+15.00%)</td><td>0.02 <b>(-31.07%)</b></td><td>210.80 (-13.04%)</td><td>180.82 (+10.51%)</td><td>196.20 <b>(+35.40%)</b></td><td>145.40 (+9.65%)</td><td>29.32 <b>(-35.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>242.40 (n/a)</td><td>163.62 (n/a)</td><td>144.90 (n/a)</td><td>132.60 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-10.81%)</td><td>0.11 (-9.52%)</td><td>0.11 (-12.78%)</td><td>0.09 (+0.65%)</td><td>0.01 <b>(-37.35%)</b></td><td>224.70 (-0.62%)</td><td>190.34 (+9.33%)</td><td>183.10 (+14.65%)</td><td>174.20 (+12.10%)</td><td>20.50 <b>(-30.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>174.10 (n/a)</td><td>159.70 (n/a)</td><td>155.40 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (-5.77%)</td><td>0.12 (-9.65%)</td><td>0.10 <b>(-21.77%)</b></td><td>0.10 <b>(+28.17%)</b></td><td>0.03 <b>(-26.20%)</b></td><td>214.10 <b>(-22.00%)</b></td><td>184.18 (+6.27%)</td><td>208.10 <b>(+27.83%)</b></td><td>132.90 (+6.07%)</td><td>36.78 <b>(-38.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>274.50 (n/a)</td><td>173.32 (n/a)</td><td>162.80 (n/a)</td><td>125.30 (n/a)</td><td>59.94 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (-6.65%)</td><td>0.11 <b>(-20.48%)</b></td><td>0.11 <b>(-31.38%)</b></td><td>0.09 (-7.76%)</td><td>0.02 (-17.99%)</td><td>229.80 (+8.40%)</td><td>192.30 <b>(+24.61%)</b></td><td>191.30 <b>(+45.70%)</b></td><td>136.00 (+7.17%)</td><td>36.37 (-3.75%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>154.32 (n/a)</td><td>131.30 (n/a)</td><td>126.90 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (+3.72%)</td><td>0.10 (+2.86%)</td><td>0.10 (-6.44%)</td><td>0.09 <b>(+48.64%)</b></td><td>0.01 <b>(-41.17%)</b></td><td>232.10 <b>(-32.74%)</b></td><td>199.34 (-7.93%)</td><td>201.00 (+6.86%)</td><td>159.80 (-3.62%)</td><td>26.56 <b>(-63.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>345.10 (n/a)</td><td>216.52 (n/a)</td><td>188.10 (n/a)</td><td>165.80 (n/a)</td><td>73.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.10 <b>(-20.89%)</b></td><td>0.09 (-0.99%)</td><td>0.09 (+3.12%)</td><td>0.08 (+11.44%)</td><td>0.01 <b>(-65.68%)</b></td><td>261.30 (-10.30%)</td><td>228.96 (-2.26%)</td><td>226.30 (-3.04%)</td><td>211.30 <b>(+26.45%)</b></td><td>19.29 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>291.30 (n/a)</td><td>234.26 (n/a)</td><td>233.40 (n/a)</td><td>167.10 (n/a)</td><td>48.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (-2.94%)</td><td>0.15 (-10.73%)</td><td>0.16 (-10.90%)</td><td>0.07 <b>(-45.59%)</b></td><td>0.05 <b>(+45.58%)</b></td><td>375.80 <b>(+83.86%)</b></td><td>196.40 <b>(+25.58%)</b></td><td>157.90 (+12.30%)</td><td>127.00 (+3.00%)</td><td>103.38 <b>(+183.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>204.40 (n/a)</td><td>156.40 (n/a)</td><td>140.60 (n/a)</td><td>123.30 (n/a)</td><td>36.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 (-10.05%)</td><td>0.13 (-19.48%)</td><td>0.12 <b>(-26.70%)</b></td><td>0.10 (-16.58%)</td><td>0.03 (+4.28%)</td><td>244.70 (+19.89%)</td><td>193.82 <b>(+25.87%)</b></td><td>197.90 <b>(+36.39%)</b></td><td>135.60 (+11.15%)</td><td>44.18 <b>(+37.32%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>204.10 (n/a)</td><td>153.98 (n/a)</td><td>145.10 (n/a)</td><td>122.00 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 <b>(-26.42%)</b></td><td>0.13 (-14.94%)</td><td>0.13 (-11.93%)</td><td>0.11 (-10.12%)</td><td>0.01 <b>(-59.18%)</b></td><td>213.90 (+11.29%)</td><td>189.60 (+15.95%)</td><td>188.90 (+13.52%)</td><td>172.50 <b>(+35.93%)</b></td><td>15.28 <b>(-36.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>163.52 (n/a)</td><td>166.40 (n/a)</td><td>126.90 (n/a)</td><td>23.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 <b>(-29.87%)</b></td><td>0.12 <b>(-24.81%)</b></td><td>0.12 <b>(-21.15%)</b></td><td>0.11 (-10.71%)</td><td>0.01 <b>(-72.86%)</b></td><td>222.20 (+12.00%)</td><td>210.20 <b>(+30.24%)</b></td><td>212.50 <b>(+26.87%)</b></td><td>189.70 <b>(+42.63%)</b></td><td>12.40 <b>(-55.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.40 (n/a)</td><td>161.40 (n/a)</td><td>167.50 (n/a)</td><td>133.00 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.19 (-0.42%)</td><td>0.14 (-17.20%)</td><td>0.15 (-18.59%)</td><td>0.10 <b>(-21.05%)</b></td><td>0.04 <b>(+34.32%)</b></td><td>245.10 <b>(+26.67%)</b></td><td>185.90 <b>(+24.61%)</b></td><td>166.70 <b>(+22.84%)</b></td><td>126.90 (+0.48%)</td><td>48.18 <b>(+74.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>149.18 (n/a)</td><td>135.70 (n/a)</td><td>126.30 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.18 (+13.27%)</td><td>0.13 (-4.46%)</td><td>0.13 (-6.96%)</td><td>0.09 (-11.36%)</td><td>0.03 <b>(+50.98%)</b></td><td>274.20 (+12.84%)</td><td>197.80 (+7.59%)</td><td>191.50 (+7.46%)</td><td>136.60 (-11.70%)</td><td>50.71 <b>(+46.45%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>183.84 (n/a)</td><td>178.20 (n/a)</td><td>154.70 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (-12.46%)</td><td>0.12 (-7.81%)</td><td>0.11 (-10.95%)</td><td>0.10 (-11.26%)</td><td>0.02 (-3.76%)</td><td>236.00 (+12.70%)</td><td>207.16 (+8.94%)</td><td>225.80 (+12.28%)</td><td>163.80 (+14.23%)</td><td>34.84 <b>(+26.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>209.40 (n/a)</td><td>190.16 (n/a)</td><td>201.10 (n/a)</td><td>143.40 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 (-2.67%)</td><td>0.12 (+1.66%)</td><td>0.12 (-0.63%)</td><td>0.08 (-5.48%)</td><td>0.03 (+17.64%)</td><td>306.80 (+5.79%)</td><td>213.24 (+0.17%)</td><td>206.20 (+0.63%)</td><td>158.90 (+2.71%)</td><td>61.31 <b>(+21.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>290.00 (n/a)</td><td>212.88 (n/a)</td><td>204.90 (n/a)</td><td>154.70 (n/a)</td><td>50.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (+10.22%)</td><td>0.12 (+15.47%)</td><td>0.14 <b>(+34.77%)</b></td><td>0.09 (+18.92%)</td><td>0.03 <b>(+35.43%)</b></td><td>203.00 (-15.91%)</td><td>159.62 (-12.24%)</td><td>134.00 <b>(-25.80%)</b></td><td>127.60 (-9.31%)</td><td>38.85 (+3.69%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.40 (n/a)</td><td>181.88 (n/a)</td><td>180.60 (n/a)</td><td>140.70 (n/a)</td><td>37.47 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 <b>(+31.81%)</b></td><td>0.11 (+18.55%)</td><td>0.10 (+4.96%)</td><td>0.09 (+8.88%)</td><td>0.02 <b>(+120.06%)</b></td><td>201.70 (-8.15%)</td><td>170.56 (-13.97%)</td><td>184.50 (-4.70%)</td><td>130.60 <b>(-24.11%)</b></td><td>30.59 <b>(+50.03%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>198.26 (n/a)</td><td>193.60 (n/a)</td><td>172.10 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.14 (+0.20%)</td><td>0.11 (-10.05%)</td><td>0.10 (-16.82%)</td><td>0.10 (-2.81%)</td><td>0.02 (-6.45%)</td><td>187.40 (+2.91%)</td><td>169.92 (+10.93%)</td><td>179.40 <b>(+20.24%)</b></td><td>128.60 (-0.16%)</td><td>24.48 (-3.94%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>182.10 (n/a)</td><td>153.18 (n/a)</td><td>149.20 (n/a)</td><td>128.80 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 (-14.28%)</td><td>0.10 <b>(-23.35%)</b></td><td>0.09 <b>(-27.18%)</b></td><td>0.08 <b>(-21.79%)</b></td><td>0.02 (+7.22%)</td><td>227.40 <b>(+27.90%)</b></td><td>196.14 <b>(+31.67%)</b></td><td>206.40 <b>(+37.33%)</b></td><td>153.60 (+16.63%)</td><td>30.98 <b>(+63.05%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>177.80 (n/a)</td><td>148.96 (n/a)</td><td>150.30 (n/a)</td><td>131.70 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (-10.11%)</td><td>0.08 (-13.12%)</td><td>0.08 (-19.11%)</td><td>0.07 (-0.02%)</td><td>0.02 <b>(-23.43%)</b></td><td>270.60 (+0.00%)</td><td>230.42 (+13.51%)</td><td>231.20 <b>(+23.64%)</b></td><td>171.20 (+11.24%)</td><td>37.18 (-18.49%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>270.60 (n/a)</td><td>203.00 (n/a)</td><td>187.00 (n/a)</td><td>153.90 (n/a)</td><td>45.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.15 <b>(+24.65%)</b></td><td>0.11 (+7.53%)</td><td>0.11 (+6.49%)</td><td>0.08 (-14.96%)</td><td>0.03 <b>(+185.01%)</b></td><td>243.10 (+17.61%)</td><td>181.22 (-1.67%)</td><td>173.70 (-6.11%)</td><td>125.40 (-19.82%)</td><td>50.92 <b>(+175.26%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>184.30 (n/a)</td><td>185.00 (n/a)</td><td>156.40 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.12 <b>(+21.05%)</b></td><td>0.09 (-5.71%)</td><td>0.08 (-12.27%)</td><td>0.06 <b>(-26.71%)</b></td><td>0.02 <b>(+177.65%)</b></td><td>312.80 <b>(+36.47%)</b></td><td>225.86 (+12.00%)</td><td>232.80 (+14.01%)</td><td>148.50 (-17.41%)</td><td>61.53 <b>(+211.35%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>201.66 (n/a)</td><td>204.20 (n/a)</td><td>179.80 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.11 (+14.38%)</td><td>0.09 (+0.85%)</td><td>0.08 (-7.30%)</td><td>0.07 (+0.22%)</td><td>0.02 <b>(+49.73%)</b></td><td>263.40 (-0.23%)</td><td>215.22 (+0.52%)</td><td>218.90 (+7.89%)</td><td>164.30 (-12.56%)</td><td>39.64 <b>(+29.13%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>264.00 (n/a)</td><td>214.10 (n/a)</td><td>202.90 (n/a)</td><td>187.90 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.69 (-9.94%)</td><td>0.58 (-10.13%)</td><td>0.54 (-14.80%)</td><td>0.52 (-2.67%)</td><td>0.07 <b>(-20.95%)</b></td><td>187.40 (+2.74%)</td><td>171.06 (+10.83%)</td><td>181.10 (+17.37%)</td><td>143.00 (+11.02%)</td><td>18.21 (-10.05%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.08 (n/a)</td><td>182.40 (n/a)</td><td>154.34 (n/a)</td><td>154.30 (n/a)</td><td>128.80 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.66 (-1.51%)</td><td>0.56 (-1.36%)</td><td>0.52 (-0.42%)</td><td>0.48 (-4.31%)</td><td>0.08 (+0.10%)</td><td>203.70 (+4.52%)</td><td>178.70 (+1.44%)</td><td>188.30 (+0.37%)</td><td>148.40 (+1.57%)</td><td>23.59 (+4.25%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.67 (n/a)</td><td>0.57 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>194.90 (n/a)</td><td>176.16 (n/a)</td><td>187.60 (n/a)</td><td>146.10 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.58 <b>(-32.32%)</b></td><td>0.53 (-13.13%)</td><td>0.56 (-2.32%)</td><td>0.44 (-6.12%)</td><td>0.06 <b>(-62.61%)</b></td><td>222.10 (+6.52%)</td><td>185.84 (+11.50%)</td><td>176.40 (+2.38%)</td><td>168.20 <b>(+47.80%)</b></td><td>21.72 <b>(-38.64%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.86 (n/a)</td><td>0.61 (n/a)</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.15 (n/a)</td><td>208.50 (n/a)</td><td>166.68 (n/a)</td><td>172.30 (n/a)</td><td>113.80 (n/a)</td><td>35.40 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.58 (+1.93%)</td><td>0.50 (+1.91%)</td><td>0.49 (-1.05%)</td><td>0.42 (-0.75%)</td><td>0.07 (+6.10%)</td><td>236.50 (+0.77%)</td><td>199.00 (-1.76%)</td><td>200.50 (+1.06%)</td><td>169.10 (-1.86%)</td><td>27.40 (+3.09%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.06 (n/a)</td><td>234.70 (n/a)</td><td>202.56 (n/a)</td><td>198.40 (n/a)</td><td>172.30 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.55 (+12.97%)</td><td>0.44 (+7.75%)</td><td>0.46 (+11.26%)</td><td>0.31 (-6.87%)</td><td>0.11 <b>(+69.38%)</b></td><td>238.70 (+7.38%)</td><td>176.82 (-3.79%)</td><td>159.40 (-10.15%)</td><td>133.80 (-11.45%)</td><td>48.68 <b>(+57.77%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>222.30 (n/a)</td><td>183.78 (n/a)</td><td>177.40 (n/a)</td><td>151.10 (n/a)</td><td>30.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.59 (+6.63%)</td><td>0.40 <b>(-22.41%)</b></td><td>0.39 <b>(-29.65%)</b></td><td>0.27 <b>(-40.84%)</b></td><td>0.12 <b>(+142.47%)</b></td><td>273.00 <b>(+69.04%)</b></td><td>196.90 <b>(+36.77%)</b></td><td>191.40 <b>(+42.20%)</b></td><td>124.30 (-6.26%)</td><td>54.83 <b>(+278.54%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.05 (n/a)</td><td>161.50 (n/a)</td><td>143.96 (n/a)</td><td>134.60 (n/a)</td><td>132.60 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.44 (-12.17%)</td><td>0.39 (-6.73%)</td><td>0.40 (-6.38%)</td><td>0.33 (-2.12%)</td><td>0.05 <b>(-27.84%)</b></td><td>222.10 (+2.16%)</td><td>192.26 (+6.31%)</td><td>183.80 (+6.86%)</td><td>167.50 (+13.87%)</td><td>24.92 (-16.80%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>217.40 (n/a)</td><td>180.84 (n/a)</td><td>172.00 (n/a)</td><td>147.10 (n/a)</td><td>29.95 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.47 (+11.48%)</td><td>0.38 (+0.49%)</td><td>0.36 (-6.76%)</td><td>0.31 (-4.10%)</td><td>0.07 <b>(+54.37%)</b></td><td>234.50 (+4.27%)</td><td>200.58 (+0.91%)</td><td>205.90 (+7.24%)</td><td>155.70 (-10.26%)</td><td>34.56 <b>(+43.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.04 (n/a)</td><td>224.90 (n/a)</td><td>198.78 (n/a)</td><td>192.00 (n/a)</td><td>173.50 (n/a)</td><td>24.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 <b>(-20.17%)</b></td><td>0.22 (-11.78%)</td><td>0.22 (-12.17%)</td><td>0.16 (-5.72%)</td><td>0.04 <b>(-32.95%)</b></td><td>236.70 (+6.05%)</td><td>170.52 (+10.93%)</td><td>165.50 (+13.82%)</td><td>135.70 <b>(+25.30%)</b></td><td>39.06 (-9.83%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>223.20 (n/a)</td><td>153.72 (n/a)</td><td>145.40 (n/a)</td><td>108.30 (n/a)</td><td>43.32 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (-9.07%)</td><td>0.22 (-15.14%)</td><td>0.20 <b>(-21.82%)</b></td><td>0.19 (-18.59%)</td><td>0.04 <b>(+48.95%)</b></td><td>197.20 <b>(+22.87%)</b></td><td>173.82 (+19.53%)</td><td>186.80 <b>(+27.86%)</b></td><td>139.80 (+9.99%)</td><td>27.31 <b>(+102.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>160.50 (n/a)</td><td>145.42 (n/a)</td><td>146.10 (n/a)</td><td>127.10 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.24 (-15.93%)</td><td>0.20 (-18.03%)</td><td>0.20 <b>(-22.04%)</b></td><td>0.14 <b>(-26.20%)</b></td><td>0.04 (-7.83%)</td><td>254.80 <b>(+35.53%)</b></td><td>188.14 <b>(+23.08%)</b></td><td>181.60 <b>(+28.25%)</b></td><td>152.90 (+18.90%)</td><td>40.88 <b>(+49.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>188.00 (n/a)</td><td>152.86 (n/a)</td><td>141.60 (n/a)</td><td>128.60 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 (+0.99%)</td><td>0.21 (-1.09%)</td><td>0.19 (-4.93%)</td><td>0.17 (-3.32%)</td><td>0.04 (+18.49%)</td><td>212.60 (+3.45%)</td><td>178.30 (+1.94%)</td><td>192.60 (+5.13%)</td><td>137.90 (-0.93%)</td><td>31.75 <b>(+21.29%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>205.50 (n/a)</td><td>174.90 (n/a)</td><td>183.20 (n/a)</td><td>139.20 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (-3.78%)</td><td>0.21 (+8.02%)</td><td>0.20 (+12.42%)</td><td>0.16 <b>(+23.41%)</b></td><td>0.04 <b>(-26.98%)</b></td><td>224.00 (-18.96%)</td><td>177.16 (-10.62%)</td><td>184.10 (-11.02%)</td><td>133.80 (+3.96%)</td><td>34.34 <b>(-38.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>276.40 (n/a)</td><td>198.20 (n/a)</td><td>206.90 (n/a)</td><td>128.70 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.30 <b>(+36.39%)</b></td><td>0.22 (+15.62%)</td><td>0.20 (+0.39%)</td><td>0.16 <b>(+27.57%)</b></td><td>0.05 <b>(+48.04%)</b></td><td>223.80 <b>(-21.64%)</b></td><td>179.54 (-12.69%)</td><td>181.90 (-0.38%)</td><td>124.70 <b>(-26.69%)</b></td><td>41.16 (-14.35%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>285.60 (n/a)</td><td>205.64 (n/a)</td><td>182.60 (n/a)</td><td>170.10 (n/a)</td><td>48.05 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.23 (+12.33%)</td><td>0.19 (+4.89%)</td><td>0.19 (+1.58%)</td><td>0.16 (+15.10%)</td><td>0.03 (+1.28%)</td><td>233.20 (-13.11%)</td><td>197.48 (-5.07%)</td><td>190.90 (-1.55%)</td><td>161.70 (-11.01%)</td><td>28.50 <b>(-21.03%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>268.40 (n/a)</td><td>208.02 (n/a)</td><td>193.90 (n/a)</td><td>181.70 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 <b>(+36.80%)</b></td><td>0.19 (+4.42%)</td><td>0.16 (-16.59%)</td><td>0.15 <b>(+34.04%)</b></td><td>0.05 <b>(+34.50%)</b></td><td>243.00 <b>(-25.41%)</b></td><td>204.64 (-4.53%)</td><td>223.80 (+19.87%)</td><td>133.50 <b>(-26.93%)</b></td><td>43.88 <b>(-29.62%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>325.80 (n/a)</td><td>214.36 (n/a)</td><td>186.70 (n/a)</td><td>182.70 (n/a)</td><td>62.35 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.30 (-6.26%)</td><td>0.22 (-16.86%)</td><td>0.21 <b>(-24.79%)</b></td><td>0.17 <b>(-24.57%)</b></td><td>0.05 <b>(+28.37%)</b></td><td>238.40 <b>(+32.59%)</b></td><td>189.30 <b>(+22.70%)</b></td><td>197.20 <b>(+32.97%)</b></td><td>135.70 (+6.68%)</td><td>38.75 <b>(+75.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>179.80 (n/a)</td><td>154.28 (n/a)</td><td>148.30 (n/a)</td><td>127.20 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (+0.58%)</td><td>0.26 (-8.95%)</td><td>0.27 (-7.80%)</td><td>0.18 <b>(-21.22%)</b></td><td>0.05 <b>(+86.07%)</b></td><td>224.60 <b>(+26.89%)</b></td><td>166.62 (+13.13%)</td><td>154.50 (+8.50%)</td><td>133.40 (-0.52%)</td><td>38.51 <b>(+125.42%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>177.00 (n/a)</td><td>147.28 (n/a)</td><td>142.40 (n/a)</td><td>134.10 (n/a)</td><td>17.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.34 <b>(+25.32%)</b></td><td>0.26 (+7.26%)</td><td>0.23 (-9.15%)</td><td>0.20 (+1.01%)</td><td>0.07 <b>(+158.90%)</b></td><td>200.10 (-1.04%)</td><td>163.96 (-3.17%)</td><td>181.30 (+10.08%)</td><td>121.90 <b>(-20.22%)</b></td><td>38.13 <b>(+96.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>202.20 (n/a)</td><td>169.32 (n/a)</td><td>164.70 (n/a)</td><td>152.80 (n/a)</td><td>19.45 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 (+3.70%)</td><td>0.22 (-8.21%)</td><td>0.21 (-7.15%)</td><td>0.17 (-14.29%)</td><td>0.05 (+14.31%)</td><td>242.80 (+16.67%)</td><td>193.88 (+10.16%)</td><td>197.80 (+7.73%)</td><td>131.80 (-3.58%)</td><td>40.24 <b>(+22.37%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>208.10 (n/a)</td><td>176.00 (n/a)</td><td>183.60 (n/a)</td><td>136.70 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.32 (-3.21%)</td><td>0.22 (-11.60%)</td><td>0.19 <b>(-26.63%)</b></td><td>0.16 (+8.42%)</td><td>0.06 (-19.11%)</td><td>253.70 (-7.78%)</td><td>199.28 (+9.37%)</td><td>220.30 <b>(+36.32%)</b></td><td>128.10 (+3.31%)</td><td>49.54 <b>(-22.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>275.10 (n/a)</td><td>182.20 (n/a)</td><td>161.60 (n/a)</td><td>124.00 (n/a)</td><td>64.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (+13.19%)</td><td>0.23 (+15.66%)</td><td>0.23 (+3.72%)</td><td>0.18 <b>(+40.65%)</b></td><td>0.04 (-8.49%)</td><td>228.90 <b>(-28.89%)</b></td><td>187.76 (-15.80%)</td><td>181.20 (-3.57%)</td><td>146.80 (-11.62%)</td><td>37.26 <b>(-41.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>321.90 (n/a)</td><td>222.98 (n/a)</td><td>187.90 (n/a)</td><td>166.10 (n/a)</td><td>64.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 <b>(-24.19%)</b></td><td>0.22 (+9.19%)</td><td>0.20 <b>(+21.16%)</b></td><td>0.18 <b>(+46.38%)</b></td><td>0.05 <b>(-53.27%)</b></td><td>227.00 <b>(-31.67%)</b></td><td>191.30 (-18.61%)</td><td>207.60 (-17.46%)</td><td>145.60 <b>(+31.88%)</b></td><td>37.84 <b>(-56.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.37 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>332.20 (n/a)</td><td>235.04 (n/a)</td><td>251.50 (n/a)</td><td>110.40 (n/a)</td><td>87.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.31 <b>(+29.59%)</b></td><td>0.23 (+19.55%)</td><td>0.20 (-0.89%)</td><td>0.18 <b>(+42.13%)</b></td><td>0.05 <b>(+29.07%)</b></td><td>229.90 <b>(-29.65%)</b></td><td>187.86 (-16.88%)</td><td>206.80 (+0.88%)</td><td>131.90 <b>(-22.87%)</b></td><td>39.53 <b>(-33.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>326.80 (n/a)</td><td>226.02 (n/a)</td><td>205.00 (n/a)</td><td>171.00 (n/a)</td><td>59.65 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (-13.83%)</td><td>0.20 (-0.52%)</td><td>0.21 (-5.27%)</td><td>0.17 <b>(+92.15%)</b></td><td>0.03 <b>(-57.21%)</b></td><td>205.70 <b>(-47.95%)</b></td><td>173.80 (-13.64%)</td><td>169.30 (+5.55%)</td><td>141.80 (+16.04%)</td><td>27.98 <b>(-74.98%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>395.20 (n/a)</td><td>201.24 (n/a)</td><td>160.40 (n/a)</td><td>122.20 (n/a)</td><td>111.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.25 (-4.31%)</td><td>0.21 (-4.53%)</td><td>0.19 (-4.26%)</td><td>0.17 (-3.80%)</td><td>0.04 (+3.19%)</td><td>205.10 (+3.95%)</td><td>174.56 (+5.19%)</td><td>184.80 (+4.47%)</td><td>137.40 (+4.49%)</td><td>32.80 (+13.48%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>197.30 (n/a)</td><td>165.94 (n/a)</td><td>176.90 (n/a)</td><td>131.50 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.21 (-19.70%)</td><td>0.18 (-18.25%)</td><td>0.20 (-15.26%)</td><td>0.14 <b>(-21.36%)</b></td><td>0.03 <b>(-20.36%)</b></td><td>254.70 <b>(+27.16%)</b></td><td>193.72 <b>(+22.36%)</b></td><td>171.00 (+18.01%)</td><td>165.60 <b>(+24.60%)</b></td><td>38.45 <b>(+26.37%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>200.30 (n/a)</td><td>158.32 (n/a)</td><td>144.90 (n/a)</td><td>132.90 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.20 <b>(-26.43%)</b></td><td>0.18 (-16.98%)</td><td>0.19 (-19.18%)</td><td>0.15 (-7.14%)</td><td>0.02 <b>(-60.60%)</b></td><td>235.60 (+7.68%)</td><td>194.30 (+15.83%)</td><td>182.90 <b>(+23.75%)</b></td><td>173.30 <b>(+35.92%)</b></td><td>24.78 <b>(-42.75%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>218.80 (n/a)</td><td>167.74 (n/a)</td><td>147.80 (n/a)</td><td>127.50 (n/a)</td><td>43.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (+12.41%)</td><td>0.20 (+18.52%)</td><td>0.19 (+4.24%)</td><td>0.16 <b>(+47.90%)</b></td><td>0.04 (-16.78%)</td><td>224.50 <b>(-32.40%)</b></td><td>177.30 (-19.82%)</td><td>179.00 (-4.07%)</td><td>131.50 (-11.03%)</td><td>37.58 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>332.10 (n/a)</td><td>221.12 (n/a)</td><td>186.60 (n/a)</td><td>147.80 (n/a)</td><td>76.57 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.27 <b>(+22.26%)</b></td><td>0.22 (+15.23%)</td><td>0.22 <b>(+24.61%)</b></td><td>0.15 (-4.59%)</td><td>0.06 <b>(+97.52%)</b></td><td>232.20 (+4.78%)</td><td>168.68 (-9.74%)</td><td>155.50 (-19.76%)</td><td>127.40 (-18.18%)</td><td>46.12 <b>(+67.61%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>221.60 (n/a)</td><td>186.88 (n/a)</td><td>193.80 (n/a)</td><td>155.70 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 <b>(+37.24%)</b></td><td>0.18 (+7.94%)</td><td>0.16 (-12.52%)</td><td>0.11 <b>(+21.16%)</b></td><td>0.06 <b>(+35.62%)</b></td><td>305.50 (-17.45%)</td><td>210.04 (-7.19%)</td><td>213.90 (+14.32%)</td><td>122.40 <b>(-27.10%)</b></td><td>65.66 <b>(-22.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>370.10 (n/a)</td><td>226.30 (n/a)</td><td>187.10 (n/a)</td><td>167.90 (n/a)</td><td>84.26 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 <b>(-26.86%)</b></td><td>0.16 (-8.30%)</td><td>0.15 (-3.32%)</td><td>0.10 (-1.40%)</td><td>0.06 <b>(-43.94%)</b></td><td>335.40 (+1.42%)</td><td>229.96 (-1.57%)</td><td>229.20 (+3.43%)</td><td>135.30 <b>(+36.67%)</b></td><td>71.35 <b>(-24.32%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>330.70 (n/a)</td><td>233.62 (n/a)</td><td>221.60 (n/a)</td><td>99.00 (n/a)</td><td>94.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.03 (+10.77%)</td><td>0.87 (+6.37%)</td><td>0.88 (+10.62%)</td><td>0.75 (-2.88%)</td><td>0.10 <b>(+57.20%)</b></td><td>174.50 (+2.95%)</td><td>151.90 (-5.46%)</td><td>149.40 (-9.62%)</td><td>127.80 (-9.75%)</td><td>16.98 <b>(+45.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.06 (n/a)</td><td>169.50 (n/a)</td><td>160.68 (n/a)</td><td>165.30 (n/a)</td><td>141.60 (n/a)</td><td>11.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.99 (-1.91%)</td><td>0.75 (-5.23%)</td><td>0.77 (-3.68%)</td><td>0.46 <b>(-22.21%)</b></td><td>0.19 (+19.19%)</td><td>283.60 <b>(+28.56%)</b></td><td>185.76 (+8.68%)</td><td>170.60 (+3.77%)</td><td>132.00 (+1.93%)</td><td>57.25 <b>(+65.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.01 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.59 (n/a)</td><td>0.16 (n/a)</td><td>220.60 (n/a)</td><td>170.92 (n/a)</td><td>164.40 (n/a)</td><td>129.50 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.14 (+2.68%)</td><td>0.86 (+4.23%)</td><td>0.83 (+4.81%)</td><td>0.67 (-6.75%)</td><td>0.18 (+11.83%)</td><td>196.40 (+7.26%)</td><td>157.32 (-3.29%)</td><td>158.60 (-4.57%)</td><td>114.70 (-2.63%)</td><td>31.16 (+18.18%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.11 (n/a)</td><td>0.83 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.16 (n/a)</td><td>183.10 (n/a)</td><td>162.68 (n/a)</td><td>166.20 (n/a)</td><td>117.80 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.00 (+0.00%)</td><td>0.00 (+3.57%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.22%)</b></td><td>0.00 <b>(-57.99%)</b></td><td>3622.37 <b>(-21.01%)</b></td><td>3531.91 (-5.86%)</td><td>3554.65 (+1.20%)</td><td>3448.90 (-0.94%)</td><td>72.61 <b>(-84.63%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4586.06 (n/a)</td><td>3751.68 (n/a)</td><td>3512.41 (n/a)</td><td>3481.47 (n/a)</td><td>472.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.00 (+0.00%)</td><td>0.00 (+2.75%)</td><td>0.00 (+0.00%)</td><td>0.00 (+16.67%)</td><td>0.00 <b>(-58.74%)</b></td><td>3959.08 (-14.33%)</td><td>3648.74 (-4.36%)</td><td>3537.05 (-1.90%)</td><td>3521.27 (-1.24%)</td><td>189.41 <b>(-58.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4621.24 (n/a)</td><td>3815.04 (n/a)</td><td>3605.43 (n/a)</td><td>3565.40 (n/a)</td><td>453.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.28 (+0.47%)</td><td>0.22 (-5.48%)</td><td>0.24 (-12.64%)</td><td>0.15 (-3.86%)</td><td>0.06 (-10.48%)</td><td>14270.97 (+4.04%)</td><td>10222.58 (+4.83%)</td><td>8694.24 (+14.45%)</td><td>7539.73 (-0.50%)</td><td>2921.02 (-2.79%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.28 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>13716.74 (n/a)</td><td>9751.59 (n/a)</td><td>7596.25 (n/a)</td><td>7577.42 (n/a)</td><td>3004.92 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.25 (+9.30%)</td><td>5.10 (+5.36%)</td><td>4.89 (-1.43%)</td><td>3.86 (-4.12%)</td><td>0.91 <b>(+29.48%)</b></td><td>271.70 (+4.30%)</td><td>211.36 (-4.15%)</td><td>214.40 (+1.47%)</td><td>167.90 (-8.50%)</td><td>39.80 <b>(+21.96%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>5.71 (n/a)</td><td>4.84 (n/a)</td><td>4.96 (n/a)</td><td>4.02 (n/a)</td><td>0.71 (n/a)</td><td>260.50 (n/a)</td><td>220.52 (n/a)</td><td>211.30 (n/a)</td><td>183.50 (n/a)</td><td>32.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>5.78 <b>(+21.47%)</b></td><td>4.83 (+13.77%)</td><td>4.96 (+11.23%)</td><td>3.72 (+17.43%)</td><td>0.74 (+12.95%)</td><td>282.10 (-14.82%)</td><td>221.70 (-12.28%)</td><td>211.20 (-10.09%)</td><td>181.50 (-17.65%)</td><td>37.23 (-19.29%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.76 (n/a)</td><td>4.24 (n/a)</td><td>4.46 (n/a)</td><td>3.17 (n/a)</td><td>0.66 (n/a)</td><td>331.20 (n/a)</td><td>252.74 (n/a)</td><td>234.90 (n/a)</td><td>220.40 (n/a)</td><td>46.13 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>4.85 <b>(-21.73%)</b></td><td>4.38 (-11.31%)</td><td>4.26 (-10.78%)</td><td>4.00 (-1.48%)</td><td>0.37 <b>(-53.03%)</b></td><td>262.00 (+1.51%)</td><td>240.98 (+11.31%)</td><td>246.30 (+12.11%)</td><td>216.40 <b>(+27.82%)</b></td><td>19.76 <b>(-37.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.19 (n/a)</td><td>4.93 (n/a)</td><td>4.77 (n/a)</td><td>4.06 (n/a)</td><td>0.78 (n/a)</td><td>258.10 (n/a)</td><td>216.50 (n/a)</td><td>219.70 (n/a)</td><td>169.30 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>6.17 <b>(+27.91%)</b></td><td>5.12 (+16.74%)</td><td>5.40 <b>(+24.68%)</b></td><td>3.99 (+2.97%)</td><td>1.06 <b>(+173.27%)</b></td><td>262.70 (-2.88%)</td><td>212.42 (-11.72%)</td><td>194.40 (-19.77%)</td><td>169.80 <b>(-21.82%)</b></td><td>46.02 <b>(+113.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>4.83 (n/a)</td><td>4.39 (n/a)</td><td>4.33 (n/a)</td><td>3.88 (n/a)</td><td>0.39 (n/a)</td><td>270.50 (n/a)</td><td>240.62 (n/a)</td><td>242.30 (n/a)</td><td>217.20 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.49 (+4.97%)</td><td>7.53 (+1.61%)</td><td>7.34 (+2.32%)</td><td>6.38 (-8.59%)</td><td>0.85 <b>(+79.72%)</b></td><td>328.50 (+9.39%)</td><td>281.48 (-0.87%)</td><td>285.70 (-2.26%)</td><td>246.90 (-4.75%)</td><td>32.54 <b>(+85.56%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.09 (n/a)</td><td>7.41 (n/a)</td><td>7.17 (n/a)</td><td>6.98 (n/a)</td><td>0.47 (n/a)</td><td>300.30 (n/a)</td><td>283.94 (n/a)</td><td>292.30 (n/a)</td><td>259.20 (n/a)</td><td>17.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>9.24 (+8.19%)</td><td>7.80 (-0.69%)</td><td>8.19 (+1.38%)</td><td>6.29 (-9.50%)</td><td>1.20 <b>(+78.27%)</b></td><td>333.50 (+10.50%)</td><td>274.42 (+2.09%)</td><td>256.00 (-1.35%)</td><td>226.90 (-7.58%)</td><td>43.90 <b>(+84.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.54 (n/a)</td><td>7.85 (n/a)</td><td>8.08 (n/a)</td><td>6.95 (n/a)</td><td>0.67 (n/a)</td><td>301.80 (n/a)</td><td>268.80 (n/a)</td><td>259.50 (n/a)</td><td>245.50 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>8.60 (+9.72%)</td><td>7.79 (+5.21%)</td><td>7.85 (+6.68%)</td><td>6.78 (-4.89%)</td><td>0.72 <b>(+145.31%)</b></td><td>309.40 (+5.13%)</td><td>270.96 (-4.40%)</td><td>267.10 (-6.25%)</td><td>243.80 (-8.86%)</td><td>25.89 <b>(+134.92%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>7.84 (n/a)</td><td>7.41 (n/a)</td><td>7.36 (n/a)</td><td>7.13 (n/a)</td><td>0.29 (n/a)</td><td>294.30 (n/a)</td><td>283.44 (n/a)</td><td>284.90 (n/a)</td><td>267.50 (n/a)</td><td>11.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>10.06 (+1.64%)</td><td>8.40 (-2.76%)</td><td>8.79 (-0.43%)</td><td>6.79 (-5.66%)</td><td>1.35 <b>(+34.29%)</b></td><td>308.70 (+5.97%)</td><td>255.16 (+3.88%)</td><td>238.50 (+0.46%)</td><td>208.40 (-1.61%)</td><td>42.19 <b>(+40.78%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.90 (n/a)</td><td>8.64 (n/a)</td><td>8.83 (n/a)</td><td>7.20 (n/a)</td><td>1.01 (n/a)</td><td>291.30 (n/a)</td><td>245.62 (n/a)</td><td>237.40 (n/a)</td><td>211.80 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.96 (-17.62%)</td><td>7.47 (-12.89%)</td><td>7.41 (-15.10%)</td><td>6.97 (-1.02%)</td><td>0.37 <b>(-61.84%)</b></td><td>300.70 (+1.04%)</td><td>281.42 (+13.73%)</td><td>283.10 (+17.76%)</td><td>263.30 <b>(+21.39%)</b></td><td>14.07 <b>(-54.03%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.67 (n/a)</td><td>8.57 (n/a)</td><td>8.73 (n/a)</td><td>7.05 (n/a)</td><td>0.98 (n/a)</td><td>297.60 (n/a)</td><td>247.44 (n/a)</td><td>240.40 (n/a)</td><td>216.90 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>9.91 (+8.19%)</td><td>8.32 (-2.53%)</td><td>8.43 (-0.82%)</td><td>7.14 (-9.71%)</td><td>1.16 <b>(+98.70%)</b></td><td>293.50 (+10.75%)</td><td>256.06 (+3.79%)</td><td>248.90 (+0.81%)</td><td>211.70 (-7.55%)</td><td>35.13 <b>(+108.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>9.16 (n/a)</td><td>8.53 (n/a)</td><td>8.50 (n/a)</td><td>7.91 (n/a)</td><td>0.58 (n/a)</td><td>265.00 (n/a)</td><td>246.70 (n/a)</td><td>246.90 (n/a)</td><td>229.00 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>12.20 (+0.65%)</td><td>11.06 (+1.85%)</td><td>10.88 (+0.02%)</td><td>9.98 (+4.10%)</td><td>1.01 (+11.66%)</td><td>420.30 (-3.93%)</td><td>381.78 (-1.71%)</td><td>385.50 (-0.03%)</td><td>343.90 (-0.64%)</td><td>34.61 (+5.42%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.12 (n/a)</td><td>10.86 (n/a)</td><td>10.88 (n/a)</td><td>9.59 (n/a)</td><td>0.91 (n/a)</td><td>437.50 (n/a)</td><td>388.44 (n/a)</td><td>385.60 (n/a)</td><td>346.10 (n/a)</td><td>32.83 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.16 (+2.87%)</td><td>11.22 (-6.77%)</td><td>10.88 (-10.84%)</td><td>10.16 (-5.65%)</td><td>1.21 <b>(+56.80%)</b></td><td>412.70 (+6.01%)</td><td>377.22 (+7.82%)</td><td>385.40 (+12.17%)</td><td>318.70 (-2.81%)</td><td>37.79 <b>(+59.43%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.79 (n/a)</td><td>12.03 (n/a)</td><td>12.21 (n/a)</td><td>10.77 (n/a)</td><td>0.77 (n/a)</td><td>389.30 (n/a)</td><td>349.86 (n/a)</td><td>343.60 (n/a)</td><td>327.90 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>12.01 (-5.04%)</td><td>10.77 (-9.81%)</td><td>11.01 (-11.11%)</td><td>8.85 (-16.56%)</td><td>1.29 <b>(+54.42%)</b></td><td>474.00 (+19.85%)</td><td>394.20 (+11.79%)</td><td>380.80 (+12.50%)</td><td>349.30 (+5.27%)</td><td>50.78 <b>(+94.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>12.64 (n/a)</td><td>11.94 (n/a)</td><td>12.39 (n/a)</td><td>10.61 (n/a)</td><td>0.83 (n/a)</td><td>395.50 (n/a)</td><td>352.64 (n/a)</td><td>338.50 (n/a)</td><td>331.80 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.35 (-5.71%)</td><td>12.87 (-2.07%)</td><td>12.83 (-6.93%)</td><td>12.19 (+3.44%)</td><td>0.44 <b>(-62.37%)</b></td><td>344.00 (-3.34%)</td><td>326.34 (+1.55%)</td><td>327.00 (+7.46%)</td><td>314.20 (+6.08%)</td><td>11.33 <b>(-61.53%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.16 (n/a)</td><td>13.14 (n/a)</td><td>13.78 (n/a)</td><td>11.79 (n/a)</td><td>1.17 (n/a)</td><td>355.90 (n/a)</td><td>321.36 (n/a)</td><td>304.30 (n/a)</td><td>296.20 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>13.50 (-4.47%)</td><td>12.08 (-10.41%)</td><td>12.67 (-6.91%)</td><td>10.16 (-17.04%)</td><td>1.44 <b>(+90.41%)</b></td><td>412.70 <b>(+20.53%)</b></td><td>351.44 (+12.68%)</td><td>331.10 (+7.43%)</td><td>310.80 (+4.68%)</td><td>43.95 <b>(+139.16%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.13 (n/a)</td><td>13.48 (n/a)</td><td>13.61 (n/a)</td><td>12.25 (n/a)</td><td>0.76 (n/a)</td><td>342.40 (n/a)</td><td>311.90 (n/a)</td><td>308.20 (n/a)</td><td>296.90 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>14.46 (-0.73%)</td><td>12.99 (+9.27%)</td><td>13.49 (+13.77%)</td><td>11.14 (+18.09%)</td><td>1.33 <b>(-40.40%)</b></td><td>376.40 (-15.32%)</td><td>325.82 (-10.28%)</td><td>310.90 (-12.10%)</td><td>290.00 (+0.73%)</td><td>34.79 <b>(-49.21%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.57 (n/a)</td><td>11.89 (n/a)</td><td>11.86 (n/a)</td><td>9.44 (n/a)</td><td>2.23 (n/a)</td><td>444.50 (n/a)</td><td>363.14 (n/a)</td><td>353.70 (n/a)</td><td>287.90 (n/a)</td><td>68.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>14.51 (-13.55%)</td><td>12.19 (-9.16%)</td><td>12.12 (-7.54%)</td><td>9.08 <b>(-24.49%)</b></td><td>2.00 (+2.20%)</td><td>461.70 <b>(+32.41%)</b></td><td>352.42 (+11.12%)</td><td>346.00 (+8.16%)</td><td>289.10 (+15.64%)</td><td>65.45 <b>(+62.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>16.78 (n/a)</td><td>13.42 (n/a)</td><td>13.11 (n/a)</td><td>12.03 (n/a)</td><td>1.95 (n/a)</td><td>348.70 (n/a)</td><td>317.16 (n/a)</td><td>319.90 (n/a)</td><td>250.00 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>16.04 (+9.41%)</td><td>12.87 (+2.11%)</td><td>12.47 (-2.10%)</td><td>9.68 (+4.85%)</td><td>2.87 <b>(+37.49%)</b></td><td>433.30 (-4.62%)</td><td>339.34 (-0.63%)</td><td>336.40 (+2.16%)</td><td>261.50 (-8.60%)</td><td>75.89 (+14.39%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>14.66 (n/a)</td><td>12.60 (n/a)</td><td>12.74 (n/a)</td><td>9.23 (n/a)</td><td>2.09 (n/a)</td><td>454.30 (n/a)</td><td>341.48 (n/a)</td><td>329.30 (n/a)</td><td>286.10 (n/a)</td><td>66.34 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.44 (+11.45%)</td><td>3.08 <b>(+20.45%)</b></td><td>3.31 <b>(+28.98%)</b></td><td>2.42 (+17.60%)</td><td>0.43 (+15.92%)</td><td>216.40 (-14.97%)</td><td>172.92 (-16.94%)</td><td>158.30 <b>(-22.44%)</b></td><td>152.40 (-10.25%)</td><td>26.74 (-12.13%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.09 (n/a)</td><td>2.56 (n/a)</td><td>2.57 (n/a)</td><td>2.06 (n/a)</td><td>0.37 (n/a)</td><td>254.50 (n/a)</td><td>208.18 (n/a)</td><td>204.10 (n/a)</td><td>169.80 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>5.38 (-11.15%)</td><td>4.51 (-9.00%)</td><td>4.55 (-4.27%)</td><td>3.51 (-15.05%)</td><td>0.68 (-7.17%)</td><td>299.00 (+17.72%)</td><td>237.04 (+10.20%)</td><td>230.40 (+4.44%)</td><td>195.00 (+12.59%)</td><td>38.67 <b>(+26.60%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>6.05 (n/a)</td><td>4.96 (n/a)</td><td>4.75 (n/a)</td><td>4.13 (n/a)</td><td>0.73 (n/a)</td><td>254.00 (n/a)</td><td>215.10 (n/a)</td><td>220.60 (n/a)</td><td>173.20 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>7.97 (-0.51%)</td><td>7.23 (+3.64%)</td><td>7.14 (-0.14%)</td><td>6.22 (+15.68%)</td><td>0.75 <b>(-29.09%)</b></td><td>337.00 (-13.57%)</td><td>292.78 (-4.64%)</td><td>293.90 (+0.14%)</td><td>263.10 (+0.50%)</td><td>31.18 <b>(-39.67%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>8.01 (n/a)</td><td>6.97 (n/a)</td><td>7.15 (n/a)</td><td>5.38 (n/a)</td><td>1.06 (n/a)</td><td>389.90 (n/a)</td><td>307.02 (n/a)</td><td>293.50 (n/a)</td><td>261.80 (n/a)</td><td>51.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>3.51 (+5.77%)</td><td>2.93 (+2.04%)</td><td>2.89 (+1.88%)</td><td>2.42 (-2.09%)</td><td>0.42 <b>(+38.95%)</b></td><td>216.70 (+2.12%)</td><td>181.64 (-1.24%)</td><td>181.30 (-1.84%)</td><td>149.20 (-5.45%)</td><td>26.12 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>3.32 (n/a)</td><td>2.88 (n/a)</td><td>2.84 (n/a)</td><td>2.47 (n/a)</td><td>0.31 (n/a)</td><td>212.20 (n/a)</td><td>183.92 (n/a)</td><td>184.70 (n/a)</td><td>157.80 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.29 (+4.00%)</td><td>0.23 (+6.28%)</td><td>0.24 (+12.62%)</td><td>0.17 (-2.54%)</td><td>0.05 <b>(+22.99%)</b></td><td>188.80 (+2.61%)</td><td>146.90 (-4.70%)</td><td>137.80 (-11.21%)</td><td>111.80 (-3.79%)</td><td>31.17 <b>(+26.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>184.00 (n/a)</td><td>154.14 (n/a)</td><td>155.20 (n/a)</td><td>116.20 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.26 (-12.90%)</td><td>0.21 (-2.63%)</td><td>0.21 (+12.68%)</td><td>0.18 <b>(+24.72%)</b></td><td>0.03 <b>(-54.62%)</b></td><td>186.70 (-19.84%)</td><td>158.56 (-3.66%)</td><td>155.90 (-11.22%)</td><td>128.00 (+14.80%)</td><td>22.66 <b>(-55.76%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>232.90 (n/a)</td><td>164.58 (n/a)</td><td>175.60 (n/a)</td><td>111.50 (n/a)</td><td>51.22 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.57 (-3.24%)</td><td>0.45 (-6.87%)</td><td>0.42 (-15.38%)</td><td>0.35 (-8.13%)</td><td>0.09 (-4.83%)</td><td>189.30 (+8.86%)</td><td>149.62 (+7.35%)</td><td>155.30 (+18.10%)</td><td>114.90 (+3.33%)</td><td>29.13 (+5.05%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.09 (n/a)</td><td>173.90 (n/a)</td><td>139.38 (n/a)</td><td>131.50 (n/a)</td><td>111.20 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.47 (+6.77%)</td><td>0.42 (+8.57%)</td><td>0.43 (+14.66%)</td><td>0.37 (+10.05%)</td><td>0.04 (-16.79%)</td><td>177.10 (-9.13%)</td><td>157.08 (-8.38%)</td><td>151.10 (-12.81%)</td><td>138.30 (-6.36%)</td><td>15.41 <b>(-28.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.05 (n/a)</td><td>194.90 (n/a)</td><td>171.44 (n/a)</td><td>173.30 (n/a)</td><td>147.70 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.51 (+12.61%)</td><td>0.43 <b>(+20.52%)</b></td><td>0.42 <b>(+21.97%)</b></td><td>0.32 (+7.93%)</td><td>0.08 <b>(+34.10%)</b></td><td>206.30 (-7.32%)</td><td>157.14 (-16.17%)</td><td>154.70 (-18.02%)</td><td>127.40 (-11.16%)</td><td>32.29 (+10.54%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>222.60 (n/a)</td><td>187.44 (n/a)</td><td>188.70 (n/a)</td><td>143.40 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.98 (-16.79%)</td><td>0.87 (+4.76%)</td><td>0.94 (+8.17%)</td><td>0.74 <b>(+85.60%)</b></td><td>0.11 <b>(-60.51%)</b></td><td>176.40 <b>(-46.12%)</b></td><td>152.16 (-15.39%)</td><td>139.60 (-7.55%)</td><td>134.10 <b>(+20.16%)</b></td><td>20.83 <b>(-75.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.17 (n/a)</td><td>0.83 (n/a)</td><td>0.87 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>327.40 (n/a)</td><td>179.84 (n/a)</td><td>151.00 (n/a)</td><td>111.60 (n/a)</td><td>85.80 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.07 (+6.34%)</td><td>0.85 (+2.48%)</td><td>0.86 (+1.38%)</td><td>0.65 (-0.20%)</td><td>0.15 (+16.89%)</td><td>201.60 (+0.20%)</td><td>157.44 (-1.89%)</td><td>152.40 (-1.36%)</td><td>122.60 (-5.98%)</td><td>28.66 (+9.65%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.01 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>0.13 (n/a)</td><td>201.20 (n/a)</td><td>160.48 (n/a)</td><td>154.50 (n/a)</td><td>130.40 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>1.04 (+4.04%)</td><td>0.81 (+0.62%)</td><td>0.85 (+7.05%)</td><td>0.55 (-15.12%)</td><td>0.18 <b>(+31.93%)</b></td><td>236.60 (+17.83%)</td><td>168.46 (+1.58%)</td><td>153.40 (-6.58%)</td><td>125.50 (-3.83%)</td><td>41.79 <b>(+54.30%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>1.00 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.65 (n/a)</td><td>0.14 (n/a)</td><td>200.80 (n/a)</td><td>165.84 (n/a)</td><td>164.20 (n/a)</td><td>130.50 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.93 (+17.15%)</td><td>0.78 <b>(+31.52%)</b></td><td>0.77 <b>(+21.05%)</b></td><td>0.60 <b>(+38.99%)</b></td><td>0.12 <b>(-21.14%)</b></td><td>218.30 <b>(-28.07%)</b></td><td>171.80 <b>(-26.61%)</b></td><td>171.10 (-17.38%)</td><td>140.90 (-14.66%)</td><td>29.09 <b>(-53.36%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.79 (n/a)</td><td>0.59 (n/a)</td><td>0.63 (n/a)</td><td>0.43 (n/a)</td><td>0.15 (n/a)</td><td>303.50 (n/a)</td><td>234.10 (n/a)</td><td>207.10 (n/a)</td><td>165.10 (n/a)</td><td>62.37 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:22</td><td>0.13 (-2.83%)</td><td>0.11 (-0.34%)</td><td>0.11 (-14.03%)</td><td>0.09 <b>(+76.83%)</b></td><td>0.01 <b>(-58.46%)</b></td><td>181.40 <b>(-43.45%)</b></td><td>153.98 (-10.63%)</td><td>150.50 (+16.31%)</td><td>128.50 (+2.88%)</td><td>20.26 <b>(-75.99%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:24:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>320.80 (n/a)</td><td>172.30 (n/a)</td><td>129.40 (n/a)</td><td>124.90 (n/a)</td><td>84.35 (n/a)</td>
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
