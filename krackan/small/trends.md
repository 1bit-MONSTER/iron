# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(-52.76%)</b></td><td>0.06 <b>(-45.78%)</b></td><td>0.06 <b>(-51.49%)</b></td><td>0.05 (-5.73%)</td><td>0.00 <b>(-85.24%)</b></td><td>236.70 (+6.05%)</td><td>209.54 <b>(+66.25%)</b></td><td>202.40 <b>(+106.11%)</b></td><td>193.60 <b>(+111.58%)</b></td><td>17.86 <b>(-67.82%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>223.20 (n/a)</td><td>126.04 (n/a)</td><td>98.20 (n/a)</td><td>91.50 (n/a)</td><td>55.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 <b>(-54.59%)</b></td><td>0.06 <b>(-41.04%)</b></td><td>0.06 <b>(-36.71%)</b></td><td>0.06 <b>(-23.63%)</b></td><td>0.01 <b>(-81.37%)</b></td><td>212.30 <b>(+30.97%)</b></td><td>195.18 <b>(+61.25%)</b></td><td>191.20 <b>(+58.02%)</b></td><td>171.40 <b>(+120.31%)</b></td><td>17.12 <b>(-43.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>162.10 (n/a)</td><td>121.04 (n/a)</td><td>121.00 (n/a)</td><td>77.80 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(-45.91%)</b></td><td>0.05 <b>(-35.59%)</b></td><td>0.05 <b>(-30.47%)</b></td><td>0.04 <b>(+213.62%)</b></td><td>0.01 <b>(-72.36%)</b></td><td>322.60 <b>(-68.12%)</b></td><td>251.78 (-18.72%)</td><td>230.20 <b>(+43.79%)</b></td><td>192.20 <b>(+84.81%)</b></td><td>61.27 <b>(-84.43%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1011.90 (n/a)</td><td>309.76 (n/a)</td><td>160.10 (n/a)</td><td>104.00 (n/a)</td><td>393.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 <b>(-39.66%)</b></td><td>0.06 <b>(-30.14%)</b></td><td>0.06 <b>(-24.57%)</b></td><td>0.05 (+8.37%)</td><td>0.01 <b>(-74.87%)</b></td><td>227.00 (-7.72%)</td><td>207.30 <b>(+32.19%)</b></td><td>206.10 <b>(+32.54%)</b></td><td>173.70 <b>(+65.74%)</b></td><td>21.44 <b>(-61.45%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>246.00 (n/a)</td><td>156.82 (n/a)</td><td>155.50 (n/a)</td><td>104.80 (n/a)</td><td>55.61 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-27.79%)</b></td><td>0.03 <b>(-22.64%)</b></td><td>0.03 <b>(-22.26%)</b></td><td>0.03 (-1.06%)</td><td>0.01 <b>(-46.74%)</b></td><td>200.40 (+1.11%)</td><td>172.02 <b>(+23.81%)</b></td><td>186.10 <b>(+28.70%)</b></td><td>126.10 <b>(+38.42%)</b></td><td>32.58 <b>(-22.78%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>138.94 (n/a)</td><td>144.60 (n/a)</td><td>91.10 (n/a)</td><td>42.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-31.68%)</b></td><td>0.03 <b>(-28.25%)</b></td><td>0.03 <b>(-36.53%)</b></td><td>0.03 (+5.20%)</td><td>0.00 <b>(-65.05%)</b></td><td>205.30 (-4.95%)</td><td>176.36 <b>(+28.34%)</b></td><td>176.30 <b>(+57.55%)</b></td><td>140.60 <b>(+46.31%)</b></td><td>26.33 <b>(-49.57%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>137.42 (n/a)</td><td>111.90 (n/a)</td><td>96.10 (n/a)</td><td>52.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (-13.49%)</td><td>0.03 (-9.32%)</td><td>0.03 (-11.87%)</td><td>0.03 (+3.29%)</td><td>0.00 <b>(-50.80%)</b></td><td>184.90 (-3.14%)</td><td>159.74 (+7.74%)</td><td>158.90 (+13.50%)</td><td>138.90 (+15.56%)</td><td>17.18 <b>(-43.76%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>148.26 (n/a)</td><td>140.00 (n/a)</td><td>120.20 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-29.53%)</b></td><td>0.03 (-2.40%)</td><td>0.03 (-1.71%)</td><td>0.03 <b>(+157.23%)</b></td><td>0.00 <b>(-70.35%)</b></td><td>192.00 <b>(-61.12%)</b></td><td>165.90 <b>(-22.32%)</b></td><td>158.90 (+1.73%)</td><td>141.00 <b>(+41.85%)</b></td><td>24.16 <b>(-84.88%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>493.80 (n/a)</td><td>213.56 (n/a)</td><td>156.20 (n/a)</td><td>99.40 (n/a)</td><td>159.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-24.41%)</b></td><td>0.03 (-15.32%)</td><td>0.03 (-6.94%)</td><td>0.02 (-9.63%)</td><td>0.01 <b>(-41.10%)</b></td><td>217.00 (+10.66%)</td><td>174.56 (+15.19%)</td><td>169.00 (+7.44%)</td><td>132.00 <b>(+32.26%)</b></td><td>32.08 (-11.87%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>151.54 (n/a)</td><td>157.30 (n/a)</td><td>99.80 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 <b>(-33.93%)</b></td><td>0.03 <b>(-21.77%)</b></td><td>0.03 (-17.25%)</td><td>0.02 (-7.76%)</td><td>0.00 <b>(-69.24%)</b></td><td>218.40 (+8.39%)</td><td>201.18 <b>(+23.82%)</b></td><td>205.70 <b>(+20.86%)</b></td><td>178.00 <b>(+51.36%)</b></td><td>17.27 <b>(-49.05%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>162.48 (n/a)</td><td>170.20 (n/a)</td><td>117.60 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 <b>(-32.81%)</b></td><td>0.02 <b>(-35.54%)</b></td><td>0.02 <b>(-36.87%)</b></td><td>0.02 <b>(-38.70%)</b></td><td>0.00 (+18.02%)</td><td>238.40 <b>(+63.18%)</b></td><td>212.04 <b>(+55.64%)</b></td><td>213.50 <b>(+58.38%)</b></td><td>195.80 <b>(+48.78%)</b></td><td>16.85 <b>(+186.79%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>146.10 (n/a)</td><td>136.24 (n/a)</td><td>134.80 (n/a)</td><td>131.60 (n/a)</td><td>5.88 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.03 (-14.80%)</td><td>0.02 <b>(-22.07%)</b></td><td>0.02 <b>(-22.02%)</b></td><td>0.02 <b>(-38.54%)</b></td><td>0.01 <b>(+62.38%)</b></td><td>312.30 <b>(+62.66%)</b></td><td>227.20 <b>(+32.82%)</b></td><td>228.90 <b>(+28.24%)</b></td><td>174.80 (+17.39%)</td><td>55.04 <b>(+207.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.00 (n/a)</td><td>171.06 (n/a)</td><td>178.50 (n/a)</td><td>148.90 (n/a)</td><td>17.89 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>151.66 (n/a)</td><td>157.30 (n/a)</td><td>119.00 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>155.44 (n/a)</td><td>160.00 (n/a)</td><td>120.40 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>168.44 (n/a)</td><td>166.90 (n/a)</td><td>128.60 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>309.00 (n/a)</td><td>218.70 (n/a)</td><td>207.70 (n/a)</td><td>129.10 (n/a)</td><td>87.25 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>185.86 (n/a)</td><td>184.20 (n/a)</td><td>165.50 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>191.82 (n/a)</td><td>188.80 (n/a)</td><td>171.20 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>167.30 (n/a)</td><td>160.60 (n/a)</td><td>137.40 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>319.60 (n/a)</td><td>221.54 (n/a)</td><td>206.30 (n/a)</td><td>183.20 (n/a)</td><td>55.75 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>168.92 (n/a)</td><td>185.50 (n/a)</td><td>110.00 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>167.78 (n/a)</td><td>162.60 (n/a)</td><td>142.90 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>162.70 (n/a)</td><td>174.40 (n/a)</td><td>126.60 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>157.96 (n/a)</td><td>142.50 (n/a)</td><td>127.70 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>170.28 (n/a)</td><td>172.60 (n/a)</td><td>144.50 (n/a)</td><td>16.45 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>173.48 (n/a)</td><td>173.80 (n/a)</td><td>144.40 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>170.16 (n/a)</td><td>169.30 (n/a)</td><td>144.40 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>353.60 (n/a)</td><td>254.04 (n/a)</td><td>221.00 (n/a)</td><td>187.80 (n/a)</td><td>71.23 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>4.80 (-1.04%)</td><td>3.98 <b>(+73.45%)</b></td><td>4.06 <b>(+116.69%)</b></td><td>3.43 <b>(+4822.90%)</b></td><td>0.55 <b>(-76.54%)</b></td><td>2737.90 <b>(-97.97%)</b></td><td>2396.10 <b>(-95.70%)</b></td><td>2315.50 <b>(-53.85%)</b></td><td>1958.10 (+1.06%)</td><td>317.65 <b>(-99.56%)</b></td><td>1889.27 (-1.04%)</td><td>1566.75 <b>(+73.45%)</b></td><td>1597.63 <b>(+116.69%)</b></td><td>1351.20 <b>(+4822.90%)</b></td><td>216.45 <b>(-76.54%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.85 (n/a)</td><td>2.30 (n/a)</td><td>1.87 (n/a)</td><td>0.07 (n/a)</td><td>2.35 (n/a)</td><td>134781.90 (n/a)</td><td>55705.60 (n/a)</td><td>5017.60 (n/a)</td><td>1937.60 (n/a)</td><td>72183.69 (n/a)</td><td>1909.22 (n/a)</td><td>903.27 (n/a)</td><td>737.28 (n/a)</td><td>27.45 (n/a)</td><td>922.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>1.25 (+9.64%)</td><td>0.89 (-4.27%)</td><td>0.70 <b>(-26.17%)</b></td><td>0.56 (-18.07%)</td><td>0.33 <b>(+93.69%)</b></td><td>397.30 <b>(+22.06%)</b></td><td>278.72 (+13.19%)</td><td>314.90 <b>(+35.44%)</b></td><td>176.40 (-8.74%)</td><td>97.87 <b>(+95.05%)</b></td><td>53.51 (+9.64%)</td><td>37.82 (-4.27%)</td><td>29.97 <b>(-26.17%)</b></td><td>23.76 (-18.07%)</td><td>14.29 <b>(+93.69%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.14 (n/a)</td><td>0.93 (n/a)</td><td>0.95 (n/a)</td><td>0.68 (n/a)</td><td>0.17 (n/a)</td><td>325.50 (n/a)</td><td>246.24 (n/a)</td><td>232.50 (n/a)</td><td>193.30 (n/a)</td><td>50.18 (n/a)</td><td>48.81 (n/a)</td><td>39.51 (n/a)</td><td>40.59 (n/a)</td><td>29.00 (n/a)</td><td>7.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>1.07 <b>(-31.94%)</b></td><td>1.03 <b>(+33.16%)</b></td><td>1.04 (+4.17%)</td><td>0.99 <b>(+1357.25%)</b></td><td>0.03 <b>(-94.93%)</b></td><td>224.40 <b>(-93.14%)</b></td><td>214.34 <b>(-79.62%)</b></td><td>213.00 (-4.01%)</td><td>206.60 <b>(+46.94%)</b></td><td>6.87 <b>(-99.49%)</b></td><td>45.69 <b>(-31.94%)</b></td><td>44.07 <b>(+33.16%)</b></td><td>44.31 (+4.17%)</td><td>42.06 <b>(+1357.25%)</b></td><td>1.40 <b>(-94.93%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.57 (n/a)</td><td>0.78 (n/a)</td><td>1.00 (n/a)</td><td>0.07 (n/a)</td><td>0.65 (n/a)</td><td>3270.00 (n/a)</td><td>1051.56 (n/a)</td><td>221.90 (n/a)</td><td>140.60 (n/a)</td><td>1350.44 (n/a)</td><td>67.13 (n/a)</td><td>33.09 (n/a)</td><td>42.54 (n/a)</td><td>2.89 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.52 (-0.99%)</td><td>0.52 (+17.66%)</td><td>0.52 (-0.72%)</td><td>0.51 <b>(+265.40%)</b></td><td>0.00 <b>(-98.84%)</b></td><td>49047.20 <b>(-72.63%)</b></td><td>48726.04 <b>(-35.10%)</b></td><td>48651.10 (+0.72%)</td><td>48583.30 (+1.00%)</td><td>184.16 <b>(-99.68%)</b></td><td>353.62 (-0.99%)</td><td>352.58 (+17.66%)</td><td>353.12 (-0.72%)</td><td>350.27 <b>(+265.40%)</b></td><td>1.33 <b>(-98.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>179220.70 (n/a)</td><td>75077.54 (n/a)</td><td>48302.60 (n/a)</td><td>48104.40 (n/a)</td><td>58236.88 (n/a)</td><td>357.14 (n/a)</td><td>299.67 (n/a)</td><td>355.67 (n/a)</td><td>95.86 (n/a)</td><td>114.40 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.89 (-4.28%)</td><td>0.88 (-1.55%)</td><td>0.88 (-2.28%)</td><td>0.88 (+5.97%)</td><td>0.01 <b>(-87.90%)</b></td><td>28711.90 (-5.63%)</td><td>28584.60 (+1.39%)</td><td>28650.10 (+2.33%)</td><td>28309.30 (+4.47%)</td><td>162.53 <b>(-88.08%)</b></td><td>606.86 (-4.28%)</td><td>601.03 (-1.55%)</td><td>599.64 (-2.28%)</td><td>598.35 (+5.97%)</td><td>3.44 <b>(-87.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.93 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.83 (n/a)</td><td>0.04 (n/a)</td><td>30425.10 (n/a)</td><td>28192.66 (n/a)</td><td>27997.30 (n/a)</td><td>27098.00 (n/a)</td><td>1363.31 (n/a)</td><td>633.99 (n/a)</td><td>610.47 (n/a)</td><td>613.63 (n/a)</td><td>564.66 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.35 (-2.87%)</td><td>3.26 <b>(+23.99%)</b></td><td>3.28 (-2.72%)</td><td>3.17 <b>(+664.56%)</b></td><td>0.08 <b>(-93.58%)</b></td><td>7946.50 <b>(-86.92%)</b></td><td>7718.80 <b>(-58.46%)</b></td><td>7669.10 (+2.79%)</td><td>7517.40 (+2.96%)</td><td>198.18 <b>(-99.16%)</b></td><td>2285.34 (-2.87%)</td><td>2226.89 <b>(+23.99%)</b></td><td>2240.14 (-2.72%)</td><td>2161.95 <b>(+664.56%)</b></td><td>56.91 <b>(-93.58%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.45 (n/a)</td><td>2.63 (n/a)</td><td>3.37 (n/a)</td><td>0.41 (n/a)</td><td>1.30 (n/a)</td><td>60755.30 (n/a)</td><td>18580.82 (n/a)</td><td>7460.60 (n/a)</td><td>7301.50 (n/a)</td><td>23603.19 (n/a)</td><td>2352.92 (n/a)</td><td>1796.09 (n/a)</td><td>2302.76 (n/a)</td><td>282.77 (n/a)</td><td>885.87 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>4.23 (+1.72%)</td><td>3.95 <b>(+48.17%)</b></td><td>3.94 <b>(+54.61%)</b></td><td>3.54 <b>(+5776.20%)</b></td><td>0.29 <b>(-82.82%)</b></td><td>2277.80 <b>(-98.30%)</b></td><td>2048.02 <b>(-92.90%)</b></td><td>2046.30 <b>(-35.32%)</b></td><td>1905.90 (-1.70%)</td><td>153.49 <b>(-99.74%)</b></td><td>1109.14 (+1.72%)</td><td>1036.69 <b>(+48.17%)</b></td><td>1033.05 <b>(+54.61%)</b></td><td>928.04 <b>(+5776.20%)</b></td><td>75.38 <b>(-82.82%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.16 (n/a)</td><td>2.67 (n/a)</td><td>2.55 (n/a)</td><td>0.06 (n/a)</td><td>1.67 (n/a)</td><td>133850.00 (n/a)</td><td>28839.70 (n/a)</td><td>3163.90 (n/a)</td><td>1938.80 (n/a)</td><td>58706.05 (n/a)</td><td>1090.33 (n/a)</td><td>699.64 (n/a)</td><td>668.15 (n/a)</td><td>15.79 (n/a)</td><td>438.89 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.36 <b>(-41.04%)</b></td><td>0.34 <b>(+121.51%)</b></td><td>0.34 <b>(+645.16%)</b></td><td>0.33 <b>(+2312.48%)</b></td><td>0.01 <b>(-95.10%)</b></td><td>3821.20 <b>(-95.85%)</b></td><td>3664.98 <b>(-89.89%)</b></td><td>3635.60 <b>(-86.58%)</b></td><td>3477.80 <b>(+69.61%)</b></td><td>133.34 <b>(-99.61%)</b></td><td>19.30 <b>(-41.04%)</b></td><td>18.33 <b>(+121.51%)</b></td><td>18.46 <b>(+645.16%)</b></td><td>17.56 <b>(+2312.48%)</b></td><td>0.67 <b>(-95.10%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.61 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.25 (n/a)</td><td>92184.70 (n/a)</td><td>36248.28 (n/a)</td><td>27090.90 (n/a)</td><td>2050.50 (n/a)</td><td>34564.49 (n/a)</td><td>32.73 (n/a)</td><td>8.28 (n/a)</td><td>2.48 (n/a)</td><td>0.73 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>6.36 (+1.13%)</td><td>4.25 <b>(+72.65%)</b></td><td>3.37 <b>(+6638.90%)</b></td><td>3.21 <b>(+6363.63%)</b></td><td>1.39 <b>(-57.89%)</b></td><td>2073.80 <b>(-98.45%)</b></td><td>1686.02 <b>(-97.91%)</b></td><td>1976.80 <b>(-98.52%)</b></td><td>1046.50 (-1.12%)</td><td>467.65 <b>(-99.36%)</b></td><td>1963.86 (+1.13%)</td><td>1313.54 <b>(+72.65%)</b></td><td>1039.67 <b>(+6638.90%)</b></td><td>991.01 <b>(+6363.63%)</b></td><td>430.28 <b>(-57.89%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>6.29 (n/a)</td><td>2.46 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>3.31 (n/a)</td><td>134045.70 (n/a)</td><td>80573.92 (n/a)</td><td>133213.80 (n/a)</td><td>1058.40 (n/a)</td><td>72554.60 (n/a)</td><td>1941.89 (n/a)</td><td>760.82 (n/a)</td><td>15.43 (n/a)</td><td>15.33 (n/a)</td><td>1021.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.21 (-19.95%)</td><td>0.20 (+2.05%)</td><td>0.20 <b>(+20.79%)</b></td><td>0.19 <b>(+24.04%)</b></td><td>0.01 <b>(-80.98%)</b></td><td>0.21 (-19.95%)</td><td>0.20 (+2.05%)</td><td>0.20 <b>(+20.79%)</b></td><td>0.19 <b>(+24.04%)</b></td><td>0.01 <b>(-80.98%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>13.30 (+4.64%)</td><td>12.47 <b>(+26.48%)</b></td><td>12.30 (-0.43%)</td><td>12.13 <b>(+4693.99%)</b></td><td>0.47 <b>(-91.24%)</b></td><td>13.29 (+4.64%)</td><td>12.46 <b>(+26.48%)</b></td><td>12.29 (-0.43%)</td><td>12.13 <b>(+4693.99%)</b></td><td>0.47 <b>(-91.24%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>12.71 (n/a)</td><td>9.86 (n/a)</td><td>12.35 (n/a)</td><td>0.25 (n/a)</td><td>5.39 (n/a)</td><td>12.70 (n/a)</td><td>9.85 (n/a)</td><td>12.35 (n/a)</td><td>0.25 (n/a)</td><td>5.38 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>25.35 (-1.62%)</td><td>22.87 (+17.63%)</td><td>24.10 (+16.79%)</td><td>16.43 <b>(+112.21%)</b></td><td>3.64 <b>(-47.70%)</b></td><td>25.33 (-1.62%)</td><td>22.86 (+17.63%)</td><td>24.09 (+16.79%)</td><td>16.42 <b>(+112.21%)</b></td><td>3.64 <b>(-47.70%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>25.77 (n/a)</td><td>19.44 (n/a)</td><td>20.64 (n/a)</td><td>7.74 (n/a)</td><td>6.96 (n/a)</td><td>25.75 (n/a)</td><td>19.43 (n/a)</td><td>20.62 (n/a)</td><td>7.74 (n/a)</td><td>6.96 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>41.41 (-6.34%)</td><td>40.96 (+11.01%)</td><td>40.98 (-2.82%)</td><td>40.40 <b>(+47.79%)</b></td><td>0.40 <b>(-95.17%)</b></td><td>41.38 (-6.34%)</td><td>40.93 (+11.01%)</td><td>40.95 (-2.82%)</td><td>40.37 <b>(+47.79%)</b></td><td>0.40 <b>(-95.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>44.21 (n/a)</td><td>36.89 (n/a)</td><td>42.17 (n/a)</td><td>27.33 (n/a)</td><td>8.31 (n/a)</td><td>44.18 (n/a)</td><td>36.87 (n/a)</td><td>42.15 (n/a)</td><td>27.32 (n/a)</td><td>8.31 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>46.79 (+9.40%)</td><td>42.37 <b>(+30.88%)</b></td><td>42.14 <b>(+22.23%)</b></td><td>38.75 <b>(+96.62%)</b></td><td>2.89 <b>(-71.45%)</b></td><td>46.76 (+9.40%)</td><td>42.35 <b>(+30.88%)</b></td><td>42.11 <b>(+22.23%)</b></td><td>38.73 <b>(+96.62%)</b></td><td>2.89 <b>(-71.45%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>42.77 (n/a)</td><td>32.38 (n/a)</td><td>34.47 (n/a)</td><td>19.71 (n/a)</td><td>10.14 (n/a)</td><td>42.74 (n/a)</td><td>32.36 (n/a)</td><td>34.45 (n/a)</td><td>19.70 (n/a)</td><td>10.13 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>13.23 (+2.31%)</td><td>12.16 (-0.87%)</td><td>12.19 (-2.92%)</td><td>10.58 (+0.39%)</td><td>0.98 (-0.59%)</td><td>13.22 (+2.31%)</td><td>12.15 (-0.87%)</td><td>12.18 (-2.92%)</td><td>10.58 (+0.39%)</td><td>0.98 (-0.59%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>12.93 (n/a)</td><td>12.26 (n/a)</td><td>12.56 (n/a)</td><td>10.54 (n/a)</td><td>0.99 (n/a)</td><td>12.92 (n/a)</td><td>12.26 (n/a)</td><td>12.55 (n/a)</td><td>10.53 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>25.18 (+3.59%)</td><td>23.16 <b>(+31.01%)</b></td><td>22.80 (+6.77%)</td><td>21.89 <b>(+1012.98%)</b></td><td>1.25 <b>(-86.42%)</b></td><td>25.16 (+3.59%)</td><td>23.15 <b>(+31.01%)</b></td><td>22.79 (+6.77%)</td><td>21.87 <b>(+1012.98%)</b></td><td>1.25 <b>(-86.42%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>24.31 (n/a)</td><td>17.68 (n/a)</td><td>21.36 (n/a)</td><td>1.97 (n/a)</td><td>9.22 (n/a)</td><td>24.29 (n/a)</td><td>17.67 (n/a)</td><td>21.34 (n/a)</td><td>1.97 (n/a)</td><td>9.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>41.56 (-3.38%)</td><td>36.74 <b>(+20.87%)</b></td><td>39.76 (+13.55%)</td><td>29.40 <b>(+241.75%)</b></td><td>5.32 <b>(-61.17%)</b></td><td>41.54 (-3.38%)</td><td>36.72 <b>(+20.87%)</b></td><td>39.74 (+13.55%)</td><td>29.39 <b>(+241.75%)</b></td><td>5.32 <b>(-61.17%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>43.02 (n/a)</td><td>30.39 (n/a)</td><td>35.02 (n/a)</td><td>8.60 (n/a)</td><td>13.70 (n/a)</td><td>42.99 (n/a)</td><td>30.38 (n/a)</td><td>35.00 (n/a)</td><td>8.60 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>43.83 (-9.41%)</td><td>42.83 (+19.58%)</td><td>43.41 (+3.12%)</td><td>40.46 <b>(+109.89%)</b></td><td>1.37 <b>(-90.57%)</b></td><td>43.80 (-9.41%)</td><td>42.80 (+19.58%)</td><td>43.39 (+3.12%)</td><td>40.44 <b>(+109.89%)</b></td><td>1.37 <b>(-90.57%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>48.38 (n/a)</td><td>35.81 (n/a)</td><td>42.10 (n/a)</td><td>19.28 (n/a)</td><td>14.54 (n/a)</td><td>48.35 (n/a)</td><td>35.79 (n/a)</td><td>42.07 (n/a)</td><td>19.27 (n/a)</td><td>14.53 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>180.04 (n/a)</td><td>185.90 (n/a)</td><td>122.20 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>191.20 (n/a)</td><td>182.80 (n/a)</td><td>176.20 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>173.52 (n/a)</td><td>176.40 (n/a)</td><td>135.70 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>194.32 (n/a)</td><td>191.70 (n/a)</td><td>160.40 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.80 (n/a)</td><td>212.30 (n/a)</td><td>209.10 (n/a)</td><td>191.00 (n/a)</td><td>19.04 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>163.44 (n/a)</td><td>165.70 (n/a)</td><td>145.30 (n/a)</td><td>11.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>193.28 (n/a)</td><td>201.20 (n/a)</td><td>155.60 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>261.50 (n/a)</td><td>232.12 (n/a)</td><td>227.40 (n/a)</td><td>208.50 (n/a)</td><td>20.25 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(-21.02%)</b></td><td>0.05 (+10.66%)</td><td>0.05 (-1.83%)</td><td>0.04 <b>(+7392.36%)</b></td><td>0.01 <b>(-66.95%)</b></td><td>213.30 <b>(-98.67%)</b></td><td>170.14 <b>(-94.89%)</b></td><td>171.10 (+1.85%)</td><td>135.80 <b>(+26.68%)</b></td><td>34.69 <b>(-99.51%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>15984.60 (n/a)</td><td>3330.04 (n/a)</td><td>168.00 (n/a)</td><td>107.20 (n/a)</td><td>7074.41 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-32.98%)</b></td><td>0.04 (-4.21%)</td><td>0.04 <b>(-22.57%)</b></td><td>0.03 <b>(+7139.13%)</b></td><td>0.00 <b>(-89.43%)</b></td><td>237.80 <b>(-98.62%)</b></td><td>217.74 <b>(-93.92%)</b></td><td>217.20 <b>(+29.21%)</b></td><td>198.40 <b>(+49.17%)</b></td><td>14.29 <b>(-99.81%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>17212.60 (n/a)</td><td>3580.24 (n/a)</td><td>168.10 (n/a)</td><td>133.00 (n/a)</td><td>7620.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 <b>(-41.52%)</b></td><td>0.04 (-1.49%)</td><td>0.04 (+12.48%)</td><td>0.02 <b>(+873.82%)</b></td><td>0.01 <b>(-66.08%)</b></td><td>348.30 <b>(-89.73%)</b></td><td>215.84 <b>(-73.95%)</b></td><td>195.60 (-11.09%)</td><td>164.90 <b>(+71.06%)</b></td><td>75.55 <b>(-94.73%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>3391.40 (n/a)</td><td>828.50 (n/a)</td><td>220.00 (n/a)</td><td>96.40 (n/a)</td><td>1434.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (+10.16%)</td><td>0.05 <b>(+20.04%)</b></td><td>0.05 (-12.79%)</td><td>0.04 <b>(+494.06%)</b></td><td>0.01 <b>(-56.30%)</b></td><td>201.10 <b>(-83.17%)</b></td><td>170.62 <b>(-54.46%)</b></td><td>180.40 (+14.69%)</td><td>134.90 (-9.22%)</td><td>29.40 <b>(-93.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1194.70 (n/a)</td><td>374.64 (n/a)</td><td>157.30 (n/a)</td><td>148.60 (n/a)</td><td>459.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 <b>(-33.95%)</b></td><td>0.04 (-5.34%)</td><td>0.04 (-4.09%)</td><td>0.03 <b>(+389.81%)</b></td><td>0.01 <b>(-74.18%)</b></td><td>254.80 <b>(-79.58%)</b></td><td>202.08 <b>(-46.56%)</b></td><td>182.20 (+4.23%)</td><td>177.60 <b>(+51.41%)</b></td><td>33.01 <b>(-93.22%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1248.00 (n/a)</td><td>378.16 (n/a)</td><td>174.80 (n/a)</td><td>117.30 (n/a)</td><td>487.17 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (-13.85%)</td><td>0.04 <b>(+32.93%)</b></td><td>0.04 (+5.56%)</td><td>0.03 <b>(+21448.10%)</b></td><td>0.00 <b>(-81.04%)</b></td><td>236.60 <b>(-99.54%)</b></td><td>203.74 <b>(-98.04%)</b></td><td>206.00 (-5.24%)</td><td>182.00 (+16.07%)</td><td>22.06 <b>(-99.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>50989.10 (n/a)</td><td>10419.14 (n/a)</td><td>217.40 (n/a)</td><td>156.80 (n/a)</td><td>22679.90 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 <b>(-41.93%)</b></td><td>0.04 (-12.80%)</td><td>0.04 (+5.65%)</td><td>0.04 <b>(+21.59%)</b></td><td>0.00 <b>(-82.73%)</b></td><td>212.00 (-17.73%)</td><td>190.88 (+2.23%)</td><td>194.90 (-5.34%)</td><td>169.80 <b>(+72.21%)</b></td><td>15.90 <b>(-75.30%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>257.70 (n/a)</td><td>186.72 (n/a)</td><td>205.90 (n/a)</td><td>98.60 (n/a)</td><td>64.39 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-31.77%)</b></td><td>0.04 <b>(-21.47%)</b></td><td>0.04 (-13.10%)</td><td>0.03 (-1.33%)</td><td>0.00 <b>(-64.08%)</b></td><td>236.40 (+1.37%)</td><td>203.34 <b>(+22.24%)</b></td><td>197.20 (+15.05%)</td><td>182.10 <b>(+46.50%)</b></td><td>23.47 <b>(-46.07%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>166.34 (n/a)</td><td>171.40 (n/a)</td><td>124.30 (n/a)</td><td>43.52 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


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
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.21 (+0.02%)</td><td>0.20 (+0.01%)</td><td>0.20 (-0.07%)</td><td>0.20 (+0.07%)</td><td>0.00 (-18.47%)</td><td>40961.20 (-0.07%)</td><td>40924.92 (-0.01%)</td><td>40941.50 (+0.07%)</td><td>40859.60 (-0.02%)</td><td>41.66 (-18.49%)</td>
</tr>
<tr>
<td><code>9c70ba8</code> — 2026-06-29 16:51:59</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40988.20 (n/a)</td><td>40927.74 (n/a)</td><td>40913.30 (n/a)</td><td>40866.90 (n/a)</td><td>51.11 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 <b>(-38.85%)</b></td><td>0.05 (-1.56%)</td><td>0.05 (+19.22%)</td><td>0.04 (+19.49%)</td><td>0.00 <b>(-84.20%)</b></td><td>184.40 (-16.33%)</td><td>175.40 (-8.52%)</td><td>180.70 (-16.11%)</td><td>155.10 <b>(+63.61%)</b></td><td>11.83 <b>(-78.20%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>220.40 (n/a)</td><td>191.74 (n/a)</td><td>215.40 (n/a)</td><td>94.80 (n/a)</td><td>54.27 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.09 (-8.90%)</td><td>0.06 <b>(+50.09%)</b></td><td>0.06 <b>(+92.06%)</b></td><td>0.05 <b>(+1192.26%)</b></td><td>0.02 <b>(-62.05%)</b></td><td>242.20 <b>(-92.26%)</b></td><td>202.50 <b>(-79.83%)</b></td><td>218.40 <b>(-47.94%)</b></td><td>143.00 (+9.75%)</td><td>42.84 <b>(-96.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.04 (n/a)</td><td>3130.40 (n/a)</td><td>1003.96 (n/a)</td><td>419.50 (n/a)</td><td>130.30 (n/a)</td><td>1260.01 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (+3.02%)</td><td>0.05 (+7.37%)</td><td>0.05 <b>(+20.67%)</b></td><td>0.04 (+2.67%)</td><td>0.01 (-2.58%)</td><td>207.00 (-2.59%)</td><td>165.82 (-7.16%)</td><td>156.90 (-17.16%)</td><td>130.80 (-2.90%)</td><td>31.69 (-7.38%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>178.60 (n/a)</td><td>189.40 (n/a)</td><td>134.70 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(+30.50%)</b></td><td>0.05 <b>(+81.86%)</b></td><td>0.05 <b>(+31.99%)</b></td><td>0.05 <b>(+484.66%)</b></td><td>0.00 <b>(-76.40%)</b></td><td>220.60 <b>(-82.90%)</b></td><td>198.76 <b>(-69.33%)</b></td><td>196.30 <b>(-24.24%)</b></td><td>175.70 <b>(-23.34%)</b></td><td>16.57 <b>(-97.01%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1290.00 (n/a)</td><td>648.10 (n/a)</td><td>259.10 (n/a)</td><td>229.20 (n/a)</td><td>553.71 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (+2.57%)</td><td>0.04 <b>(+82.29%)</b></td><td>0.05 <b>(+344.69%)</b></td><td>0.03 <b>(+664.70%)</b></td><td>0.01 <b>(-64.63%)</b></td><td>243.20 <b>(-86.92%)</b></td><td>193.34 <b>(-76.67%)</b></td><td>176.20 <b>(-77.51%)</b></td><td>153.40 (-2.48%)</td><td>37.60 <b>(-94.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1859.50 (n/a)</td><td>828.60 (n/a)</td><td>783.50 (n/a)</td><td>157.30 (n/a)</td><td>715.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(-46.12%)</b></td><td>0.06 (+11.75%)</td><td>0.06 <b>(+31.91%)</b></td><td>0.05 <b>(+23852.94%)</b></td><td>0.01 <b>(-86.19%)</b></td><td>211.50 <b>(-99.58%)</b></td><td>182.74 <b>(-98.22%)</b></td><td>174.00 <b>(-24.18%)</b></td><td>166.70 <b>(+85.63%)</b></td><td>19.29 <b>(-99.91%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.04 (n/a)</td><td>50651.40 (n/a)</td><td>10282.26 (n/a)</td><td>229.50 (n/a)</td><td>89.80 (n/a)</td><td>22567.12 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (-18.16%)</td><td>0.04 (+12.29%)</td><td>0.05 (+12.55%)</td><td>0.04 <b>(+485.59%)</b></td><td>0.01 <b>(-60.64%)</b></td><td>230.60 <b>(-82.92%)</b></td><td>188.10 <b>(-54.44%)</b></td><td>175.90 (-11.12%)</td><td>151.30 <b>(+22.21%)</b></td><td>38.08 <b>(-92.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1350.20 (n/a)</td><td>412.86 (n/a)</td><td>197.90 (n/a)</td><td>123.80 (n/a)</td><td>525.61 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 (-6.37%)</td><td>0.05 <b>(+23.98%)</b></td><td>0.05 (+17.80%)</td><td>0.03 <b>(+377.13%)</b></td><td>0.01 <b>(-58.77%)</b></td><td>272.70 <b>(-79.04%)</b></td><td>201.38 <b>(-52.63%)</b></td><td>187.30 (-15.13%)</td><td>171.50 (+6.79%)</td><td>40.52 <b>(-91.74%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1300.90 (n/a)</td><td>425.12 (n/a)</td><td>220.70 (n/a)</td><td>160.60 (n/a)</td><td>490.33 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.05 <b>(-25.40%)</b></td><td>0.04 <b>(+49.78%)</b></td><td>0.05 <b>(+26.59%)</b></td><td>0.04 <b>(+24589.09%)</b></td><td>0.01 <b>(-81.84%)</b></td><td>210.60 <b>(-99.59%)</b></td><td>186.20 <b>(-98.40%)</b></td><td>175.60 <b>(-21.01%)</b></td><td>163.10 <b>(+34.13%)</b></td><td>22.42 <b>(-99.90%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>51992.80 (n/a)</td><td>11617.72 (n/a)</td><td>222.30 (n/a)</td><td>121.60 (n/a)</td><td>22690.36 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (-5.68%)</td><td>0.05 (+9.93%)</td><td>0.05 (+11.63%)</td><td>0.04 <b>(+35.68%)</b></td><td>0.01 <b>(-42.92%)</b></td><td>212.70 <b>(-26.30%)</b></td><td>187.12 (-11.69%)</td><td>186.80 (-10.45%)</td><td>166.30 (+5.99%)</td><td>21.11 <b>(-56.77%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.60 (n/a)</td><td>211.90 (n/a)</td><td>208.60 (n/a)</td><td>156.90 (n/a)</td><td>48.83 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 (-9.87%)</td><td>0.05 <b>(+74.37%)</b></td><td>0.04 <b>(+298.14%)</b></td><td>0.04 <b>(+65602.01%)</b></td><td>0.01 <b>(-75.42%)</b></td><td>200.40 <b>(-99.85%)</b></td><td>179.44 <b>(-99.33%)</b></td><td>189.90 <b>(-74.88%)</b></td><td>140.70 (+10.87%)</td><td>25.16 <b>(-99.96%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>131699.70 (n/a)</td><td>26849.44 (n/a)</td><td>755.90 (n/a)</td><td>126.90 (n/a)</td><td>58615.77 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (-14.37%)</td><td>0.04 <b>(+21.12%)</b></td><td>0.04 (+11.21%)</td><td>0.03 <b>(+643.23%)</b></td><td>0.00 <b>(-84.52%)</b></td><td>257.90 <b>(-86.54%)</b></td><td>234.56 <b>(-59.15%)</b></td><td>234.40 (-10.05%)</td><td>214.60 (+16.82%)</td><td>15.61 <b>(-97.92%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1916.70 (n/a)</td><td>574.16 (n/a)</td><td>260.60 (n/a)</td><td>183.70 (n/a)</td><td>751.22 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 <b>(-36.96%)</b></td><td>0.04 (-4.31%)</td><td>0.04 (+15.41%)</td><td>0.03 <b>(+544.55%)</b></td><td>0.00 <b>(-85.92%)</b></td><td>236.40 <b>(-84.49%)</b></td><td>210.92 <b>(-53.69%)</b></td><td>213.80 (-13.37%)</td><td>187.50 <b>(+58.63%)</b></td><td>20.08 <b>(-96.66%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1523.80 (n/a)</td><td>455.48 (n/a)</td><td>246.80 (n/a)</td><td>118.20 (n/a)</td><td>600.96 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.06 <b>(+25.20%)</b></td><td>0.04 <b>(+59.01%)</b></td><td>0.04 (+10.78%)</td><td>0.04 <b>(+375.15%)</b></td><td>0.01 <b>(-57.82%)</b></td><td>228.80 <b>(-78.95%)</b></td><td>205.82 <b>(-63.59%)</b></td><td>214.90 (-9.71%)</td><td>154.40 <b>(-20.08%)</b></td><td>29.35 <b>(-93.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1086.90 (n/a)</td><td>565.30 (n/a)</td><td>238.00 (n/a)</td><td>193.20 (n/a)</td><td>472.99 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.04 (-8.24%)</td><td>0.03 <b>(+30.99%)</b></td><td>0.04 (-1.97%)</td><td>0.02 <b>(+664.72%)</b></td><td>0.01 <b>(-68.82%)</b></td><td>356.00 <b>(-86.92%)</b></td><td>254.22 <b>(-72.83%)</b></td><td>231.00 (+2.03%)</td><td>213.40 (+8.99%)</td><td>57.78 <b>(-94.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2722.10 (n/a)</td><td>935.66 (n/a)</td><td>226.40 (n/a)</td><td>195.80 (n/a)</td><td>1110.20 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.65 (-9.04%)</td><td>0.58 (+12.13%)</td><td>0.61 <b>(+32.02%)</b></td><td>0.50 <b>(+38.71%)</b></td><td>0.07 <b>(-52.01%)</b></td><td>195.20 <b>(-27.92%)</b></td><td>170.70 (-15.07%)</td><td>160.20 <b>(-24.22%)</b></td><td>151.80 (+10.00%)</td><td>21.16 <b>(-60.84%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.71 (n/a)</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.15 (n/a)</td><td>270.80 (n/a)</td><td>201.00 (n/a)</td><td>211.40 (n/a)</td><td>138.00 (n/a)</td><td>54.02 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.66 (-0.39%)</td><td>0.57 (+19.52%)</td><td>0.59 <b>(+26.57%)</b></td><td>0.46 (+16.99%)</td><td>0.07 <b>(-31.95%)</b></td><td>214.20 (-14.53%)</td><td>174.30 (-18.02%)</td><td>167.90 <b>(-20.99%)</b></td><td>148.80 (+0.40%)</td><td>24.58 <b>(-39.60%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.66 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.11 (n/a)</td><td>250.60 (n/a)</td><td>212.62 (n/a)</td><td>212.50 (n/a)</td><td>148.20 (n/a)</td><td>40.69 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.70 <b>(+28.14%)</b></td><td>0.58 <b>(+79.13%)</b></td><td>0.57 <b>(+61.22%)</b></td><td>0.47 <b>(+1594.98%)</b></td><td>0.11 <b>(-43.50%)</b></td><td>209.80 <b>(-94.10%)</b></td><td>175.46 <b>(-80.93%)</b></td><td>171.90 <b>(-37.96%)</b></td><td>141.30 <b>(-21.98%)</b></td><td>32.38 <b>(-97.80%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>0.19 (n/a)</td><td>3556.20 (n/a)</td><td>919.98 (n/a)</td><td>277.10 (n/a)</td><td>181.10 (n/a)</td><td>1474.65 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.48 <b>(-36.19%)</b></td><td>0.45 (-12.83%)</td><td>0.45 (+2.46%)</td><td>0.37 (-8.35%)</td><td>0.05 <b>(-68.97%)</b></td><td>263.80 (+9.10%)</td><td>222.74 (+9.61%)</td><td>217.40 (-2.42%)</td><td>202.90 <b>(+56.68%)</b></td><td>24.99 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.76 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.15 (n/a)</td><td>241.80 (n/a)</td><td>203.22 (n/a)</td><td>222.80 (n/a)</td><td>129.50 (n/a)</td><td>47.28 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.51 <b>(+52.36%)</b></td><td>0.43 <b>(+44.61%)</b></td><td>0.43 <b>(+39.40%)</b></td><td>0.36 <b>(+34.59%)</b></td><td>0.06 <b>(+86.39%)</b></td><td>205.70 <b>(-25.69%)</b></td><td>172.84 <b>(-30.46%)</b></td><td>170.20 <b>(-28.28%)</b></td><td>144.80 <b>(-34.36%)</b></td><td>23.04 (-10.66%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>276.80 (n/a)</td><td>248.56 (n/a)</td><td>237.30 (n/a)</td><td>220.60 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.46 <b>(-33.56%)</b></td><td>0.39 (-5.72%)</td><td>0.40 (+1.04%)</td><td>0.31 (+3.99%)</td><td>0.06 <b>(-64.68%)</b></td><td>241.10 (-3.83%)</td><td>190.26 (-1.40%)</td><td>185.50 (-1.07%)</td><td>160.10 <b>(+50.61%)</b></td><td>30.53 <b>(-46.08%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.69 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>250.70 (n/a)</td><td>192.96 (n/a)</td><td>187.50 (n/a)</td><td>106.30 (n/a)</td><td>56.62 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.45 <b>(-33.81%)</b></td><td>0.41 (+5.05%)</td><td>0.41 <b>(+25.89%)</b></td><td>0.38 <b>(+328.50%)</b></td><td>0.03 <b>(-88.97%)</b></td><td>195.70 <b>(-76.67%)</b></td><td>179.68 <b>(-42.66%)</b></td><td>180.80 <b>(-20.56%)</b></td><td>164.20 <b>(+51.06%)</b></td><td>11.58 <b>(-96.16%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.68 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>0.24 (n/a)</td><td>838.70 (n/a)</td><td>313.36 (n/a)</td><td>227.60 (n/a)</td><td>108.70 (n/a)</td><td>301.29 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.44 (+6.18%)</td><td>0.35 (-3.16%)</td><td>0.34 (-6.77%)</td><td>0.29 (+6.40%)</td><td>0.05 (-6.17%)</td><td>256.20 (-6.02%)</td><td>217.06 (+2.70%)</td><td>219.90 (+7.27%)</td><td>169.30 (-5.84%)</td><td>31.37 (-17.97%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>272.60 (n/a)</td><td>211.36 (n/a)</td><td>205.00 (n/a)</td><td>179.80 (n/a)</td><td>38.25 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.86 <b>(-37.41%)</b></td><td>0.69 (-0.95%)</td><td>0.78 <b>(+23.82%)</b></td><td>0.50 <b>(+382.42%)</b></td><td>0.17 <b>(-62.80%)</b></td><td>262.90 <b>(-79.27%)</b></td><td>202.08 <b>(-48.69%)</b></td><td>169.00 (-19.25%)</td><td>151.60 <b>(+59.75%)</b></td><td>54.32 <b>(-88.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.38 (n/a)</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.10 (n/a)</td><td>0.46 (n/a)</td><td>1268.40 (n/a)</td><td>393.86 (n/a)</td><td>209.30 (n/a)</td><td>94.90 (n/a)</td><td>491.49 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.93 (-11.26%)</td><td>0.73 <b>(+23.42%)</b></td><td>0.69 (-7.14%)</td><td>0.60 <b>(+7400.89%)</b></td><td>0.12 <b>(-68.70%)</b></td><td>216.80 <b>(-98.67%)</b></td><td>182.98 <b>(-94.64%)</b></td><td>190.90 (+7.73%)</td><td>140.40 (+12.68%)</td><td>28.32 <b>(-99.61%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.05 (n/a)</td><td>0.59 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>0.40 (n/a)</td><td>16260.50 (n/a)</td><td>3411.50 (n/a)</td><td>177.20 (n/a)</td><td>124.60 (n/a)</td><td>7183.19 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.85 (-17.59%)</td><td>0.72 <b>(+57.67%)</b></td><td>0.75 <b>(+41.71%)</b></td><td>0.56 <b>(+750.32%)</b></td><td>0.11 <b>(-73.31%)</b></td><td>234.30 <b>(-88.24%)</b></td><td>185.82 <b>(-78.82%)</b></td><td>174.00 <b>(-29.44%)</b></td><td>154.30 <b>(+21.31%)</b></td><td>30.31 <b>(-96.75%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.03 (n/a)</td><td>0.46 (n/a)</td><td>0.53 (n/a)</td><td>0.07 (n/a)</td><td>0.40 (n/a)</td><td>1992.30 (n/a)</td><td>877.44 (n/a)</td><td>246.60 (n/a)</td><td>127.20 (n/a)</td><td>931.42 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.00 (+9.09%)</td><td>0.00 (+3.92%)</td><td>0.00 (+10.00%)</td><td>0.00 (-10.00%)</td><td>0.00 <b>(+239.12%)</b></td><td>4451.35 (+8.22%)</td><td>3927.18 (-1.93%)</td><td>3844.19 (-4.38%)</td><td>3472.28 (-8.40%)</td><td>468.63 <b>(+258.63%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4113.25 (n/a)</td><td>4004.38 (n/a)</td><td>4020.47 (n/a)</td><td>3790.67 (n/a)</td><td>130.67 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.00 (+0.00%)</td><td>0.00 (-8.82%)</td><td>0.00 (-14.29%)</td><td>0.00 (-5.26%)</td><td>0.00 <b>(+50.00%)</b></td><td>4577.20 (+6.96%)</td><td>4415.88 (+10.64%)</td><td>4536.16 (+15.39%)</td><td>3948.49 (+2.96%)</td><td>263.99 <b>(+42.13%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4279.42 (n/a)</td><td>3991.39 (n/a)</td><td>3931.05 (n/a)</td><td>3835.13 (n/a)</td><td>185.74 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>0.28 (+10.02%)</td><td>0.21 (+6.28%)</td><td>0.18 (-13.15%)</td><td>0.16 <b>(+82.17%)</b></td><td>0.06 (-6.54%)</td><td>13419.47 <b>(-45.07%)</b></td><td>10637.06 (-13.94%)</td><td>11464.28 (+15.14%)</td><td>7607.60 (-9.09%)</td><td>2858.67 <b>(-57.85%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>24431.47 (n/a)</td><td>12360.57 (n/a)</td><td>9957.05 (n/a)</td><td>8368.62 (n/a)</td><td>6781.88 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.65 (+5.85%)</td><td>2.84 <b>(+50.59%)</b></td><td>2.69 <b>(+27.33%)</b></td><td>2.52 <b>(+56330.41%)</b></td><td>0.45 <b>(-64.10%)</b></td><td>208.20 <b>(-99.82%)</b></td><td>187.50 <b>(-99.21%)</b></td><td>195.10 <b>(-21.46%)</b></td><td>143.80 (-5.52%)</td><td>25.08 <b>(-99.95%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.44 (n/a)</td><td>1.89 (n/a)</td><td>2.11 (n/a)</td><td>0.00 (n/a)</td><td>1.26 (n/a)</td><td>117485.30 (n/a)</td><td>23690.72 (n/a)</td><td>248.40 (n/a)</td><td>152.20 (n/a)</td><td>52432.81 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>5.56 (+19.17%)</td><td>4.47 (+9.04%)</td><td>4.20 (-3.04%)</td><td>3.92 (+19.82%)</td><td>0.67 <b>(+23.01%)</b></td><td>267.60 (-16.53%)</td><td>238.28 (-8.23%)</td><td>249.50 (+3.14%)</td><td>188.60 (-16.10%)</td><td>32.23 (-15.24%)</td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.67 (n/a)</td><td>4.10 (n/a)</td><td>4.33 (n/a)</td><td>3.27 (n/a)</td><td>0.55 (n/a)</td><td>320.60 (n/a)</td><td>259.64 (n/a)</td><td>241.90 (n/a)</td><td>224.80 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.72 <b>(+20.32%)</b></td><td>3.12 (+16.02%)</td><td>3.04 (+6.32%)</td><td>2.73 <b>(+32.06%)</b></td><td>0.43 (+8.15%)</td><td>192.20 <b>(-24.30%)</b></td><td>170.32 (-14.26%)</td><td>172.50 (-5.94%)</td><td>141.00 (-16.86%)</td><td>22.57 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (n/a)</td><td>2.69 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.40 (n/a)</td><td>253.90 (n/a)</td><td>198.64 (n/a)</td><td>183.40 (n/a)</td><td>169.60 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>2dd32af</code> — 2026-07-09 03:19:52</td><td>3.31 (-7.33%)</td><td>2.84 (-5.28%)</td><td>3.00 (+2.68%)</td><td>2.33 (-9.75%)</td><td>0.43 (+17.92%)</td><td>225.50 (+10.81%)</td><td>188.32 (+6.43%)</td><td>175.00 (-2.56%)</td><td>158.20 (+7.91%)</td><td>29.67 <b>(+45.11%)</b></td>
</tr>
<tr>
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.58 (n/a)</td><td>3.00 (n/a)</td><td>2.92 (n/a)</td><td>2.58 (n/a)</td><td>0.36 (n/a)</td><td>203.50 (n/a)</td><td>176.94 (n/a)</td><td>179.60 (n/a)</td><td>146.60 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.36 (+7.95%)</td><td>3.26 (+13.04%)</td><td>3.33 <b>(+22.37%)</b></td><td>2.38 (+18.97%)</td><td>0.79 (-14.92%)</td><td>220.70 (-15.96%)</td><td>168.40 (-14.68%)</td><td>157.40 (-18.28%)</td><td>120.30 (-7.39%)</td><td>40.78 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (n/a)</td><td>2.89 (n/a)</td><td>2.72 (n/a)</td><td>2.00 (n/a)</td><td>0.93 (n/a)</td><td>262.60 (n/a)</td><td>197.38 (n/a)</td><td>192.60 (n/a)</td><td>129.90 (n/a)</td><td>62.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>
