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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.13 <b>(+32.09%)</b></td><td>0.11 <b>(+63.16%)</b></td><td>0.13 <b>(+76.58%)</b></td><td>0.06 <b>(+69.58%)</b></td><td>0.03 (+19.97%)</td><td>223.20 <b>(-41.03%)</b></td><td>126.04 <b>(-41.70%)</b></td><td>98.20 <b>(-43.37%)</b></td><td>91.50 <b>(-24.25%)</b></td><td>55.49 <b>(-46.25%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>378.50 (n/a)</td><td>216.20 (n/a)</td><td>173.40 (n/a)</td><td>120.80 (n/a)</td><td>103.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.16 <b>(+41.35%)</b></td><td>0.11 <b>(+39.78%)</b></td><td>0.10 <b>(+45.01%)</b></td><td>0.08 <b>(+24.20%)</b></td><td>0.03 <b>(+53.45%)</b></td><td>162.10 (-19.51%)</td><td>121.04 <b>(-27.45%)</b></td><td>121.00 <b>(-31.05%)</b></td><td>77.80 <b>(-29.27%)</b></td><td>30.35 (-10.93%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>166.84 (n/a)</td><td>175.50 (n/a)</td><td>110.00 (n/a)</td><td>34.07 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (+14.57%)</td><td>0.08 (+8.63%)</td><td>0.08 (+4.78%)</td><td>0.01 <b>(-67.39%)</b></td><td>0.04 <b>(+67.39%)</b></td><td>1011.90 <b>(+206.64%)</b></td><td>309.76 <b>(+62.35%)</b></td><td>160.10 (-4.53%)</td><td>104.00 (-12.68%)</td><td>393.61 <b>(+368.66%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>330.00 (n/a)</td><td>190.80 (n/a)</td><td>167.70 (n/a)</td><td>119.10 (n/a)</td><td>83.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 <b>(+65.46%)</b></td><td>0.09 <b>(+44.97%)</b></td><td>0.08 <b>(+35.10%)</b></td><td>0.05 <b>(+31.24%)</b></td><td>0.03 <b>(+100.70%)</b></td><td>246.00 <b>(-23.79%)</b></td><td>156.82 <b>(-28.33%)</b></td><td>155.50 <b>(-25.99%)</b></td><td>104.80 <b>(-39.56%)</b></td><td>55.61 (-8.82%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>322.80 (n/a)</td><td>218.80 (n/a)</td><td>210.10 (n/a)</td><td>173.40 (n/a)</td><td>60.99 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 <b>(+53.57%)</b></td><td>0.04 <b>(+27.57%)</b></td><td>0.04 (+11.50%)</td><td>0.03 (-3.04%)</td><td>0.01 <b>(+190.64%)</b></td><td>198.20 (+3.12%)</td><td>138.94 (-16.69%)</td><td>144.60 (-10.35%)</td><td>91.10 <b>(-34.88%)</b></td><td>42.19 <b>(+87.85%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>166.78 (n/a)</td><td>161.30 (n/a)</td><td>139.90 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (+19.16%)</td><td>0.04 (+7.72%)</td><td>0.05 <b>(+28.87%)</b></td><td>0.02 <b>(-29.77%)</b></td><td>0.01 <b>(+171.76%)</b></td><td>216.00 <b>(+42.39%)</b></td><td>137.42 (+1.45%)</td><td>111.90 <b>(-22.40%)</b></td><td>96.10 (-16.07%)</td><td>52.22 <b>(+216.68%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>151.70 (n/a)</td><td>135.46 (n/a)</td><td>144.20 (n/a)</td><td>114.50 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 <b>(+28.76%)</b></td><td>0.04 (+19.44%)</td><td>0.04 (+18.67%)</td><td>0.03 (+9.43%)</td><td>0.01 <b>(+105.24%)</b></td><td>190.90 (-8.62%)</td><td>148.26 (-14.49%)</td><td>140.00 (-15.76%)</td><td>120.20 <b>(-22.30%)</b></td><td>30.55 <b>(+41.73%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>208.90 (n/a)</td><td>173.38 (n/a)</td><td>166.20 (n/a)</td><td>154.70 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 <b>(+26.67%)</b></td><td>0.03 (-11.57%)</td><td>0.03 (-9.59%)</td><td>0.01 <b>(-66.29%)</b></td><td>0.02 <b>(+250.29%)</b></td><td>493.80 <b>(+196.58%)</b></td><td>213.56 <b>(+49.93%)</b></td><td>156.20 (+10.62%)</td><td>99.40 <b>(-21.05%)</b></td><td>159.79 <b>(+822.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>166.50 (n/a)</td><td>142.44 (n/a)</td><td>141.20 (n/a)</td><td>125.90 (n/a)</td><td>17.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (+18.17%)</td><td>0.04 (+2.41%)</td><td>0.03 (-5.29%)</td><td>0.03 (-3.13%)</td><td>0.01 <b>(+62.97%)</b></td><td>196.10 (+3.21%)</td><td>151.54 (+0.52%)</td><td>157.30 (+5.57%)</td><td>99.80 (-15.35%)</td><td>36.40 <b>(+38.40%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>150.76 (n/a)</td><td>149.00 (n/a)</td><td>117.90 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (+0.58%)</td><td>0.03 (+3.27%)</td><td>0.03 (+4.50%)</td><td>0.03 (-0.33%)</td><td>0.01 (+1.36%)</td><td>201.50 (+0.35%)</td><td>162.48 (-3.10%)</td><td>170.20 (-4.33%)</td><td>117.60 (-0.59%)</td><td>33.90 (+0.81%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>167.68 (n/a)</td><td>177.90 (n/a)</td><td>118.30 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (+14.19%)</td><td>0.04 <b>(+33.77%)</b></td><td>0.04 <b>(+40.09%)</b></td><td>0.04 <b>(+51.04%)</b></td><td>0.00 <b>(-69.98%)</b></td><td>146.10 <b>(-33.80%)</b></td><td>136.24 <b>(-27.14%)</b></td><td>134.80 <b>(-28.60%)</b></td><td>131.60 (-12.38%)</td><td>5.88 <b>(-82.72%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>187.00 (n/a)</td><td>188.80 (n/a)</td><td>150.20 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (+10.47%)</td><td>0.03 (+14.85%)</td><td>0.03 (+7.09%)</td><td>0.03 (+16.03%)</td><td>0.00 (-1.35%)</td><td>192.00 (-13.82%)</td><td>171.06 (-13.19%)</td><td>178.50 (-6.64%)</td><td>148.90 (-9.48%)</td><td>17.89 <b>(-24.70%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>197.06 (n/a)</td><td>191.20 (n/a)</td><td>164.50 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>165.40 (n/a)</td><td>122.06 (n/a)</td><td>121.40 (n/a)</td><td>89.80 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.70 (n/a)</td><td>172.34 (n/a)</td><td>164.80 (n/a)</td><td>124.60 (n/a)</td><td>49.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1263.80 (n/a)</td><td>369.32 (n/a)</td><td>159.50 (n/a)</td><td>101.90 (n/a)</td><td>500.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>220.80 (n/a)</td><td>187.32 (n/a)</td><td>215.40 (n/a)</td><td>99.40 (n/a)</td><td>51.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.20 (n/a)</td><td>125.34 (n/a)</td><td>109.90 (n/a)</td><td>98.30 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.50 (n/a)</td><td>155.82 (n/a)</td><td>168.10 (n/a)</td><td>125.00 (n/a)</td><td>20.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1053.30 (n/a)</td><td>331.54 (n/a)</td><td>177.60 (n/a)</td><td>103.70 (n/a)</td><td>404.66 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>173.80 (n/a)</td><td>130.38 (n/a)</td><td>125.30 (n/a)</td><td>92.40 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>181.96 (n/a)</td><td>170.00 (n/a)</td><td>159.40 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>141.38 (n/a)</td><td>127.20 (n/a)</td><td>117.70 (n/a)</td><td>36.72 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.00 (n/a)</td><td>139.40 (n/a)</td><td>136.30 (n/a)</td><td>114.20 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>218.60 (n/a)</td><td>170.12 (n/a)</td><td>156.40 (n/a)</td><td>109.10 (n/a)</td><td>47.02 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>166.30 (n/a)</td><td>158.60 (n/a)</td><td>158.90 (n/a)</td><td>148.70 (n/a)</td><td>7.25 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>165.14 (n/a)</td><td>166.00 (n/a)</td><td>128.50 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>168.08 (n/a)</td><td>174.10 (n/a)</td><td>129.10 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>265.00 (n/a)</td><td>182.64 (n/a)</td><td>176.40 (n/a)</td><td>123.00 (n/a)</td><td>62.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.85 (+11.46%)</td><td>2.30 <b>(-42.99%)</b></td><td>1.87 <b>(-53.44%)</b></td><td>0.07 <b>(-98.09%)</b></td><td>2.35 <b>(+826.20%)</b></td><td>134781.90 <b>(+5128.97%)</b></td><td>55705.60 <b>(+2278.10%)</b></td><td>5017.60 <b>(+114.76%)</b></td><td>1937.60 (-10.28%)</td><td>72183.69 <b>(+47696.43%)</b></td><td>1909.22 (+11.46%)</td><td>903.27 <b>(-42.99%)</b></td><td>737.28 <b>(-53.44%)</b></td><td>27.45 <b>(-98.09%)</b></td><td>922.61 <b>(+826.20%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.35 (n/a)</td><td>4.03 (n/a)</td><td>4.03 (n/a)</td><td>3.65 (n/a)</td><td>0.25 (n/a)</td><td>2577.60 (n/a)</td><td>2342.44 (n/a)</td><td>2336.40 (n/a)</td><td>2159.60 (n/a)</td><td>151.02 (n/a)</td><td>1712.99 (n/a)</td><td>1584.41 (n/a)</td><td>1583.36 (n/a)</td><td>1435.20 (n/a)</td><td>99.61 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.14 (+12.20%)</td><td>0.93 (-3.35%)</td><td>0.95 (-1.31%)</td><td>0.68 <b>(-25.47%)</b></td><td>0.17 <b>(+297.38%)</b></td><td>325.50 <b>(+34.17%)</b></td><td>246.24 (+6.50%)</td><td>232.50 (+1.35%)</td><td>193.30 (-10.88%)</td><td>50.18 <b>(+381.88%)</b></td><td>48.81 (+12.20%)</td><td>39.51 (-3.35%)</td><td>40.59 (-1.31%)</td><td>29.00 <b>(-25.47%)</b></td><td>7.38 <b>(+297.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>1.02 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.91 (n/a)</td><td>0.04 (n/a)</td><td>242.60 (n/a)</td><td>231.22 (n/a)</td><td>229.40 (n/a)</td><td>216.90 (n/a)</td><td>10.41 (n/a)</td><td>43.50 (n/a)</td><td>40.88 (n/a)</td><td>41.13 (n/a)</td><td>38.91 (n/a)</td><td>1.86 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.57 <b>(+37.19%)</b></td><td>0.78 (-13.59%)</td><td>1.00 (+17.46%)</td><td>0.07 <b>(-89.49%)</b></td><td>0.65 <b>(+223.01%)</b></td><td>3270.00 <b>(+851.13%)</b></td><td>1051.56 <b>(+309.49%)</b></td><td>221.90 (-14.85%)</td><td>140.60 <b>(-27.11%)</b></td><td>1350.44 <b>(+2179.03%)</b></td><td>67.13 <b>(+37.19%)</b></td><td>33.09 (-13.59%)</td><td>42.54 (+17.46%)</td><td>2.89 <b>(-89.49%)</b></td><td>27.54 <b>(+223.01%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>1.15 (n/a)</td><td>0.90 (n/a)</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.20 (n/a)</td><td>343.80 (n/a)</td><td>256.80 (n/a)</td><td>260.60 (n/a)</td><td>192.90 (n/a)</td><td>59.25 (n/a)</td><td>48.93 (n/a)</td><td>38.30 (n/a)</td><td>36.22 (n/a)</td><td>27.45 (n/a)</td><td>8.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.52 (+1.08%)</td><td>0.44 (-15.14%)</td><td>0.52 (+0.71%)</td><td>0.14 <b>(-72.83%)</b></td><td>0.17 <b>(+53555.43%)</b></td><td>179220.70 <b>(+268.02%)</b></td><td>75077.54 <b>(+54.32%)</b></td><td>48302.60 (-0.70%)</td><td>48104.40 (-1.07%)</td><td>58236.88 <b>(+198119.62%)</b></td><td>357.14 (+1.08%)</td><td>299.67 (-15.14%)</td><td>355.67 (+0.71%)</td><td>95.86 <b>(-72.83%)</b></td><td>114.40 <b>(+53555.59%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48698.80 (n/a)</td><td>48651.26 (n/a)</td><td>48644.30 (n/a)</td><td>48625.70 (n/a)</td><td>29.38 (n/a)</td><td>353.31 (n/a)</td><td>353.12 (n/a)</td><td>353.17 (n/a)</td><td>352.78 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.93 (+4.59%)</td><td>0.89 (+1.53%)</td><td>0.90 (+2.04%)</td><td>0.83 (-5.40%)</td><td>0.04 <b>(+713.94%)</b></td><td>30425.10 (+5.70%)</td><td>28192.66 (-1.33%)</td><td>27997.30 (-2.00%)</td><td>27098.00 (-4.39%)</td><td>1363.31 <b>(+722.36%)</b></td><td>633.99 (+4.59%)</td><td>610.47 (+1.53%)</td><td>613.63 (+2.04%)</td><td>564.66 (-5.40%)</td><td>28.42 <b>(+713.94%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28783.60 (n/a)</td><td>28574.08 (n/a)</td><td>28568.40 (n/a)</td><td>28342.90 (n/a)</td><td>165.78 (n/a)</td><td>606.14 (n/a)</td><td>601.26 (n/a)</td><td>601.36 (n/a)</td><td>596.86 (n/a)</td><td>3.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.45 (+0.02%)</td><td>2.63 (-19.63%)</td><td>3.37 (+3.88%)</td><td>0.41 <b>(-87.03%)</b></td><td>1.30 <b>(+1205.84%)</b></td><td>60755.30 <b>(+670.95%)</b></td><td>18580.82 <b>(+141.53%)</b></td><td>7460.60 (-3.73%)</td><td>7301.50 (-0.02%)</td><td>23603.19 <b>(+10353.90%)</b></td><td>2352.92 (+0.02%)</td><td>1796.09 (-19.63%)</td><td>2302.76 (+3.88%)</td><td>282.77 <b>(-87.03%)</b></td><td>885.87 <b>(+1205.84%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>3.45 (n/a)</td><td>3.27 (n/a)</td><td>3.25 (n/a)</td><td>3.19 (n/a)</td><td>0.10 (n/a)</td><td>7880.60 (n/a)</td><td>7693.12 (n/a)</td><td>7749.80 (n/a)</td><td>7302.80 (n/a)</td><td>225.78 (n/a)</td><td>2352.51 (n/a)</td><td>2234.74 (n/a)</td><td>2216.80 (n/a)</td><td>2180.03 (n/a)</td><td>67.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.16 (-2.14%)</td><td>2.67 <b>(-22.19%)</b></td><td>2.55 <b>(-22.50%)</b></td><td>0.06 <b>(-97.81%)</b></td><td>1.67 <b>(+169.07%)</b></td><td>133850.00 <b>(+4471.38%)</b></td><td>28839.70 <b>(+1095.45%)</b></td><td>3163.90 <b>(+29.04%)</b></td><td>1938.80 (+2.18%)</td><td>58706.05 <b>(+13662.24%)</b></td><td>1090.33 (-2.14%)</td><td>699.64 <b>(-22.19%)</b></td><td>668.15 <b>(-22.50%)</b></td><td>15.79 <b>(-97.81%)</b></td><td>438.89 <b>(+169.07%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.25 (n/a)</td><td>3.43 (n/a)</td><td>3.29 (n/a)</td><td>2.75 (n/a)</td><td>0.62 (n/a)</td><td>2928.00 (n/a)</td><td>2412.46 (n/a)</td><td>2451.90 (n/a)</td><td>1897.40 (n/a)</td><td>426.57 (n/a)</td><td>1114.14 (n/a)</td><td>899.19 (n/a)</td><td>862.16 (n/a)</td><td>721.97 (n/a)</td><td>163.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.61 (+16.97%)</td><td>0.15 <b>(-55.06%)</b></td><td>0.05 <b>(-85.15%)</b></td><td>0.01 <b>(-94.74%)</b></td><td>0.25 <b>(+142.06%)</b></td><td>92184.70 <b>(+1802.01%)</b></td><td>36248.28 <b>(+835.34%)</b></td><td>27090.90 <b>(+573.20%)</b></td><td>2050.50 (-14.51%)</td><td>34564.49 <b>(+3510.72%)</b></td><td>32.73 (+16.97%)</td><td>8.28 <b>(-55.06%)</b></td><td>2.48 <b>(-85.15%)</b></td><td>0.73 <b>(-94.74%)</b></td><td>13.72 <b>(+142.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>4846.70 (n/a)</td><td>3875.42 (n/a)</td><td>4024.20 (n/a)</td><td>2398.40 (n/a)</td><td>957.27 (n/a)</td><td>27.98 (n/a)</td><td>18.42 (n/a)</td><td>16.68 (n/a)</td><td>13.85 (n/a)</td><td>5.67 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>6.29 <b>(+26.70%)</b></td><td>2.46 <b>(-45.15%)</b></td><td>0.05 <b>(-98.93%)</b></td><td>0.05 <b>(-98.59%)</b></td><td>3.31 <b>(+490.17%)</b></td><td>134045.70 <b>(+6984.87%)</b></td><td>80573.92 <b>(+5258.88%)</b></td><td>133213.80 <b>(+9235.89%)</b></td><td>1058.40 <b>(-21.07%)</b></td><td>72554.60 <b>(+32809.00%)</b></td><td>1941.89 <b>(+26.70%)</b></td><td>760.82 <b>(-45.15%)</b></td><td>15.43 <b>(-98.93%)</b></td><td>15.33 <b>(-98.59%)</b></td><td>1021.69 <b>(+490.17%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>4.96 (n/a)</td><td>4.49 (n/a)</td><td>4.66 (n/a)</td><td>3.52 (n/a)</td><td>0.56 (n/a)</td><td>1892.00 (n/a)</td><td>1503.56 (n/a)</td><td>1426.90 (n/a)</td><td>1340.90 (n/a)</td><td>220.47 (n/a)</td><td>1532.72 (n/a)</td><td>1387.16 (n/a)</td><td>1440.38 (n/a)</td><td>1086.24 (n/a)</td><td>173.12 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.27 <b>(+30.28%)</b></td><td>0.20 (+12.10%)</td><td>0.17 (-11.41%)</td><td>0.15 <b>(+23.69%)</b></td><td>0.05 <b>(+59.46%)</b></td><td>0.26 <b>(+30.28%)</b></td><td>0.19 (+12.10%)</td><td>0.17 (-11.41%)</td><td>0.15 <b>(+23.69%)</b></td><td>0.05 <b>(+59.46%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>12.71 (-4.15%)</td><td>9.86 <b>(-21.19%)</b></td><td>12.35 (-1.46%)</td><td>0.25 <b>(-97.88%)</b></td><td>5.39 <b>(+915.13%)</b></td><td>12.70 (-4.15%)</td><td>9.85 <b>(-21.19%)</b></td><td>12.35 (-1.46%)</td><td>0.25 <b>(-97.88%)</b></td><td>5.38 <b>(+915.13%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>13.26 (n/a)</td><td>12.51 (n/a)</td><td>12.54 (n/a)</td><td>11.91 (n/a)</td><td>0.53 (n/a)</td><td>13.25 (n/a)</td><td>12.50 (n/a)</td><td>12.53 (n/a)</td><td>11.90 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>25.77 (+7.30%)</td><td>19.44 (-17.47%)</td><td>20.64 (-13.51%)</td><td>7.74 <b>(-65.28%)</b></td><td>6.96 <b>(+880.44%)</b></td><td>25.75 (+7.30%)</td><td>19.43 (-17.47%)</td><td>20.62 (-13.51%)</td><td>7.74 <b>(-65.28%)</b></td><td>6.96 <b>(+880.43%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>24.01 (n/a)</td><td>23.56 (n/a)</td><td>23.86 (n/a)</td><td>22.30 (n/a)</td><td>0.71 (n/a)</td><td>24.00 (n/a)</td><td>23.55 (n/a)</td><td>23.85 (n/a)</td><td>22.29 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>44.21 (+11.55%)</td><td>36.89 (-1.40%)</td><td>42.17 (+7.09%)</td><td>27.33 (-10.83%)</td><td>8.31 <b>(+116.10%)</b></td><td>44.18 (+11.55%)</td><td>36.87 (-1.40%)</td><td>42.15 (+7.09%)</td><td>27.32 (-10.83%)</td><td>8.31 <b>(+116.10%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>39.63 (n/a)</td><td>37.41 (n/a)</td><td>39.38 (n/a)</td><td>30.65 (n/a)</td><td>3.85 (n/a)</td><td>39.61 (n/a)</td><td>37.39 (n/a)</td><td>39.35 (n/a)</td><td>30.63 (n/a)</td><td>3.84 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>42.77 (-4.25%)</td><td>32.38 <b>(-23.95%)</b></td><td>34.47 <b>(-20.41%)</b></td><td>19.71 <b>(-49.49%)</b></td><td>10.14 <b>(+358.84%)</b></td><td>42.74 (-4.25%)</td><td>32.36 <b>(-23.95%)</b></td><td>34.45 <b>(-20.41%)</b></td><td>19.70 <b>(-49.49%)</b></td><td>10.13 <b>(+358.84%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>44.67 (n/a)</td><td>42.57 (n/a)</td><td>43.32 (n/a)</td><td>39.02 (n/a)</td><td>2.21 (n/a)</td><td>44.64 (n/a)</td><td>42.55 (n/a)</td><td>43.29 (n/a)</td><td>39.00 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>12.93 (-2.12%)</td><td>12.26 (-1.55%)</td><td>12.56 (+1.62%)</td><td>10.54 (-11.95%)</td><td>0.99 <b>(+116.24%)</b></td><td>12.92 (-2.12%)</td><td>12.26 (-1.55%)</td><td>12.55 (+1.62%)</td><td>10.53 (-11.95%)</td><td>0.99 <b>(+116.24%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>13.21 (n/a)</td><td>12.46 (n/a)</td><td>12.36 (n/a)</td><td>11.97 (n/a)</td><td>0.46 (n/a)</td><td>13.20 (n/a)</td><td>12.45 (n/a)</td><td>12.35 (n/a)</td><td>11.96 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>24.31 (-0.11%)</td><td>17.68 <b>(-25.37%)</b></td><td>21.36 (-10.49%)</td><td>1.97 <b>(-91.25%)</b></td><td>9.22 <b>(+1204.54%)</b></td><td>24.29 (-0.11%)</td><td>17.67 <b>(-25.37%)</b></td><td>21.34 (-10.49%)</td><td>1.97 <b>(-91.25%)</b></td><td>9.22 <b>(+1204.54%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>24.33 (n/a)</td><td>23.69 (n/a)</td><td>23.86 (n/a)</td><td>22.48 (n/a)</td><td>0.71 (n/a)</td><td>24.32 (n/a)</td><td>23.67 (n/a)</td><td>23.84 (n/a)</td><td>22.46 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>43.02 (+5.44%)</td><td>30.39 (-13.67%)</td><td>35.02 (-7.11%)</td><td>8.60 <b>(-65.14%)</b></td><td>13.70 <b>(+108.04%)</b></td><td>42.99 (+5.44%)</td><td>30.38 (-13.67%)</td><td>35.00 (-7.11%)</td><td>8.60 <b>(-65.14%)</b></td><td>13.70 <b>(+108.04%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>40.80 (n/a)</td><td>35.21 (n/a)</td><td>37.70 (n/a)</td><td>24.68 (n/a)</td><td>6.59 (n/a)</td><td>40.77 (n/a)</td><td>35.18 (n/a)</td><td>37.67 (n/a)</td><td>24.67 (n/a)</td><td>6.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>48.38 (+6.29%)</td><td>35.81 (-14.82%)</td><td>42.10 (-0.25%)</td><td>19.28 <b>(-50.43%)</b></td><td>14.54 <b>(+471.27%)</b></td><td>48.35 (+6.29%)</td><td>35.79 (-14.82%)</td><td>42.07 (-0.25%)</td><td>19.27 <b>(-50.43%)</b></td><td>14.53 <b>(+471.27%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>45.51 (n/a)</td><td>42.04 (n/a)</td><td>42.21 (n/a)</td><td>38.89 (n/a)</td><td>2.55 (n/a)</td><td>45.48 (n/a)</td><td>42.02 (n/a)</td><td>42.18 (n/a)</td><td>38.86 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>16436.20 (n/a)</td><td>3983.78 (n/a)</td><td>278.40 (n/a)</td><td>226.00 (n/a)</td><td>7042.62 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>3397.20 (n/a)</td><td>822.06 (n/a)</td><td>161.40 (n/a)</td><td>126.10 (n/a)</td><td>1440.78 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>51895.70 (n/a)</td><td>10549.08 (n/a)</td><td>234.30 (n/a)</td><td>111.90 (n/a)</td><td>23113.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>2344.10 (n/a)</td><td>619.26 (n/a)</td><td>237.30 (n/a)</td><td>117.00 (n/a)</td><td>966.33 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.03 (n/a)</td><td>3208.00 (n/a)</td><td>795.98 (n/a)</td><td>223.70 (n/a)</td><td>110.50 (n/a)</td><td>1349.74 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2229.80 (n/a)</td><td>642.40 (n/a)</td><td>263.50 (n/a)</td><td>201.20 (n/a)</td><td>887.78 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1096.40 (n/a)</td><td>346.28 (n/a)</td><td>167.60 (n/a)</td><td>97.30 (n/a)</td><td>424.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>273.20 (n/a)</td><td>211.74 (n/a)</td><td>248.50 (n/a)</td><td>135.60 (n/a)</td><td>65.70 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 (+13.01%)</td><td>0.05 (-13.63%)</td><td>0.05 (+1.53%)</td><td>0.00 <b>(-98.78%)</b></td><td>0.03 <b>(+186.61%)</b></td><td>15984.60 <b>(+8101.44%)</b></td><td>3330.04 <b>(+1951.53%)</b></td><td>168.00 (-1.52%)</td><td>107.20 (-11.55%)</td><td>7074.41 <b>(+22738.79%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>162.32 (n/a)</td><td>170.60 (n/a)</td><td>121.20 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (+19.29%)</td><td>0.04 (+9.11%)</td><td>0.05 <b>(+47.20%)</b></td><td>0.00 <b>(-98.02%)</b></td><td>0.02 <b>(+103.69%)</b></td><td>17212.60 <b>(+4952.13%)</b></td><td>3580.24 <b>(+1357.87%)</b></td><td>168.10 <b>(-32.08%)</b></td><td>133.00 (-16.14%)</td><td>7620.79 <b>(+10024.50%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>340.70 (n/a)</td><td>245.58 (n/a)</td><td>247.50 (n/a)</td><td>158.60 (n/a)</td><td>75.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 <b>(+60.16%)</b></td><td>0.04 (-12.50%)</td><td>0.04 <b>(-21.51%)</b></td><td>0.00 <b>(-93.59%)</b></td><td>0.03 <b>(+409.76%)</b></td><td>3391.40 <b>(+1460.70%)</b></td><td>828.50 <b>(+372.13%)</b></td><td>220.00 <b>(+27.46%)</b></td><td>96.40 <b>(-37.56%)</b></td><td>1434.39 <b>(+5662.86%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>175.48 (n/a)</td><td>172.60 (n/a)</td><td>154.40 (n/a)</td><td>24.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (-13.18%)</td><td>0.04 <b>(-25.98%)</b></td><td>0.05 (-6.96%)</td><td>0.01 <b>(-85.27%)</b></td><td>0.02 <b>(+214.58%)</b></td><td>1194.70 <b>(+579.19%)</b></td><td>374.64 <b>(+150.60%)</b></td><td>157.30 (+7.45%)</td><td>148.60 (+15.19%)</td><td>459.39 <b>(+2440.95%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.90 (n/a)</td><td>149.50 (n/a)</td><td>146.40 (n/a)</td><td>129.00 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 <b>(+20.56%)</b></td><td>0.04 (-16.46%)</td><td>0.05 (-11.95%)</td><td>0.01 <b>(-85.36%)</b></td><td>0.02 <b>(+313.11%)</b></td><td>1248.00 <b>(+583.09%)</b></td><td>378.16 <b>(+138.89%)</b></td><td>174.80 (+13.58%)</td><td>117.30 (-17.10%)</td><td>487.17 <b>(+2655.21%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>158.30 (n/a)</td><td>153.90 (n/a)</td><td>141.50 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (-8.47%)</td><td>0.03 <b>(-41.60%)</b></td><td>0.04 <b>(-26.31%)</b></td><td>0.00 <b>(-99.65%)</b></td><td>0.02 <b>(+405.81%)</b></td><td>50989.10 <b>(+28691.13%)</b></td><td>10419.14 <b>(+6507.78%)</b></td><td>217.40 <b>(+35.71%)</b></td><td>156.80 (+9.27%)</td><td>22679.90 <b>(+166703.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.10 (n/a)</td><td>157.68 (n/a)</td><td>160.20 (n/a)</td><td>143.50 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.08 <b>(+50.79%)</b></td><td>0.05 (-1.07%)</td><td>0.04 <b>(-20.16%)</b></td><td>0.03 <b>(-32.33%)</b></td><td>0.02 <b>(+526.80%)</b></td><td>257.70 <b>(+47.76%)</b></td><td>186.72 (+13.62%)</td><td>205.90 <b>(+25.24%)</b></td><td>98.60 <b>(-33.69%)</b></td><td>64.39 <b>(+502.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.40 (n/a)</td><td>164.34 (n/a)</td><td>164.40 (n/a)</td><td>148.70 (n/a)</td><td>10.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (+16.87%)</td><td>0.05 (+8.89%)</td><td>0.05 (-4.51%)</td><td>0.04 (+3.43%)</td><td>0.01 <b>(+47.81%)</b></td><td>233.20 (-3.32%)</td><td>166.34 (-6.23%)</td><td>171.40 (+4.77%)</td><td>124.30 (-14.39%)</td><td>43.52 (+15.81%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>177.40 (n/a)</td><td>163.60 (n/a)</td><td>145.20 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.09 <b>(+70.81%)</b></td><td>0.05 (+2.94%)</td><td>0.04 (-19.03%)</td><td>0.04 (-10.18%)</td><td>0.02 <b>(+529.16%)</b></td><td>220.40 (+11.37%)</td><td>191.74 (+7.80%)</td><td>215.40 <b>(+23.51%)</b></td><td>94.80 <b>(-41.48%)</b></td><td>54.27 <b>(+301.00%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>177.86 (n/a)</td><td>174.40 (n/a)</td><td>162.00 (n/a)</td><td>13.53 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.09 (-6.49%)</td><td>0.04 <b>(-51.86%)</b></td><td>0.03 <b>(-66.38%)</b></td><td>0.00 <b>(-94.58%)</b></td><td>0.04 <b>(+284.60%)</b></td><td>3130.40 <b>(+1744.67%)</b></td><td>1003.96 <b>(+606.42%)</b></td><td>419.50 <b>(+197.52%)</b></td><td>130.30 (+6.98%)</td><td>1260.01 <b>(+7075.91%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.70 (n/a)</td><td>142.12 (n/a)</td><td>141.00 (n/a)</td><td>121.80 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (-8.12%)</td><td>0.05 (-15.75%)</td><td>0.04 (-17.28%)</td><td>0.04 <b>(-21.42%)</b></td><td>0.01 <b>(+33.50%)</b></td><td>212.50 <b>(+27.25%)</b></td><td>178.60 <b>(+20.97%)</b></td><td>189.40 <b>(+20.95%)</b></td><td>134.70 (+8.80%)</td><td>34.22 <b>(+87.24%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.00 (n/a)</td><td>147.64 (n/a)</td><td>156.60 (n/a)</td><td>123.80 (n/a)</td><td>18.28 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 <b>(-33.64%)</b></td><td>0.03 <b>(-51.93%)</b></td><td>0.04 <b>(-31.25%)</b></td><td>0.01 <b>(-85.00%)</b></td><td>0.02 <b>(+233.62%)</b></td><td>1290.00 <b>(+566.67%)</b></td><td>648.10 <b>(+272.56%)</b></td><td>259.10 <b>(+45.48%)</b></td><td>229.20 <b>(+50.69%)</b></td><td>553.71 <b>(+3365.29%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>173.96 (n/a)</td><td>178.10 (n/a)</td><td>152.10 (n/a)</td><td>15.98 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (-18.84%)</td><td>0.02 <b>(-50.53%)</b></td><td>0.01 <b>(-76.74%)</b></td><td>0.00 <b>(-88.76%)</b></td><td>0.02 <b>(+116.85%)</b></td><td>1859.50 <b>(+789.71%)</b></td><td>828.60 <b>(+372.30%)</b></td><td>783.50 <b>(+330.02%)</b></td><td>157.30 <b>(+23.18%)</b></td><td>715.74 <b>(+1938.48%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>175.44 (n/a)</td><td>182.20 (n/a)</td><td>127.70 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.11 <b>(+48.07%)</b></td><td>0.05 <b>(-23.02%)</b></td><td>0.04 <b>(-35.72%)</b></td><td>0.00 <b>(-99.60%)</b></td><td>0.04 <b>(+252.68%)</b></td><td>50651.40 <b>(+24656.30%)</b></td><td>10282.26 <b>(+6319.99%)</b></td><td>229.50 <b>(+55.59%)</b></td><td>89.80 <b>(-32.48%)</b></td><td>22567.12 <b>(+73738.18%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>160.16 (n/a)</td><td>147.50 (n/a)</td><td>133.00 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (+10.42%)</td><td>0.04 (-17.97%)</td><td>0.04 (-10.01%)</td><td>0.01 <b>(-84.59%)</b></td><td>0.02 <b>(+154.10%)</b></td><td>1350.20 <b>(+548.82%)</b></td><td>412.86 <b>(+139.92%)</b></td><td>197.90 (+11.12%)</td><td>123.80 (-9.44%)</td><td>525.61 <b>(+1643.89%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>172.08 (n/a)</td><td>178.10 (n/a)</td><td>136.70 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 <b>(-28.64%)</b></td><td>0.04 <b>(-41.22%)</b></td><td>0.04 <b>(-34.76%)</b></td><td>0.01 <b>(-87.42%)</b></td><td>0.02 <b>(+92.18%)</b></td><td>1300.90 <b>(+695.17%)</b></td><td>425.12 <b>(+192.70%)</b></td><td>220.70 <b>(+53.26%)</b></td><td>160.60 <b>(+40.14%)</b></td><td>490.33 <b>(+2409.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>163.60 (n/a)</td><td>145.24 (n/a)</td><td>144.00 (n/a)</td><td>114.60 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 (+11.33%)</td><td>0.03 <b>(-35.23%)</b></td><td>0.04 (-17.94%)</td><td>0.00 <b>(-99.53%)</b></td><td>0.03 <b>(+188.69%)</b></td><td>51992.80 <b>(+20992.41%)</b></td><td>11617.72 <b>(+6162.92%)</b></td><td>222.30 <b>(+21.88%)</b></td><td>121.60 (-10.19%)</td><td>22690.36 <b>(+55677.38%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.50 (n/a)</td><td>185.50 (n/a)</td><td>182.40 (n/a)</td><td>135.40 (n/a)</td><td>40.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 (-2.09%)</td><td>0.05 (-7.96%)</td><td>0.04 (-14.53%)</td><td>0.03 (+0.09%)</td><td>0.01 (-5.79%)</td><td>288.60 (-0.10%)</td><td>211.90 (+7.95%)</td><td>208.60 (+16.99%)</td><td>156.90 (+2.15%)</td><td>48.83 (-8.00%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.90 (n/a)</td><td>196.30 (n/a)</td><td>178.30 (n/a)</td><td>153.60 (n/a)</td><td>53.08 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.06 <b>(+27.41%)</b></td><td>0.03 <b>(-40.97%)</b></td><td>0.01 <b>(-77.49%)</b></td><td>0.00 <b>(-99.83%)</b></td><td>0.03 <b>(+372.66%)</b></td><td>131699.70 <b>(+58071.25%)</b></td><td>26849.44 <b>(+14447.81%)</b></td><td>755.90 <b>(+344.12%)</b></td><td>126.90 <b>(-21.47%)</b></td><td>58615.77 <b>(+210700.65%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>184.56 (n/a)</td><td>170.20 (n/a)</td><td>161.60 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 (-9.65%)</td><td>0.03 <b>(-31.49%)</b></td><td>0.03 <b>(-24.37%)</b></td><td>0.00 <b>(-88.29%)</b></td><td>0.02 <b>(+205.77%)</b></td><td>1916.70 <b>(+753.76%)</b></td><td>574.16 <b>(+193.00%)</b></td><td>260.60 <b>(+32.22%)</b></td><td>183.70 (+10.66%)</td><td>751.22 <b>(+3312.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>195.96 (n/a)</td><td>197.10 (n/a)</td><td>166.00 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.07 <b>(+32.24%)</b></td><td>0.04 (-7.77%)</td><td>0.03 <b>(-26.57%)</b></td><td>0.01 <b>(-86.33%)</b></td><td>0.03 <b>(+391.90%)</b></td><td>1523.80 <b>(+631.54%)</b></td><td>455.48 <b>(+143.70%)</b></td><td>246.80 <b>(+36.20%)</b></td><td>118.20 <b>(-24.38%)</b></td><td>600.96 <b>(+2645.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>186.90 (n/a)</td><td>181.20 (n/a)</td><td>156.30 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.05 <b>(-29.14%)</b></td><td>0.03 <b>(-41.87%)</b></td><td>0.04 (-13.81%)</td><td>0.01 <b>(-79.51%)</b></td><td>0.02 <b>(+81.03%)</b></td><td>1086.90 <b>(+388.06%)</b></td><td>565.30 <b>(+194.46%)</b></td><td>238.00 (+15.98%)</td><td>193.20 <b>(+41.12%)</b></td><td>472.99 <b>(+1323.48%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>191.98 (n/a)</td><td>205.20 (n/a)</td><td>136.90 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.04 (-3.85%)</td><td>0.03 (-13.88%)</td><td>0.04 <b>(+26.51%)</b></td><td>0.00 <b>(-85.40%)</b></td><td>0.02 <b>(+100.70%)</b></td><td>2722.10 <b>(+584.81%)</b></td><td>935.66 <b>(+211.37%)</b></td><td>226.40 <b>(-20.98%)</b></td><td>195.80 (+4.04%)</td><td>1110.20 <b>(+1118.57%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>397.50 (n/a)</td><td>300.50 (n/a)</td><td>286.50 (n/a)</td><td>188.20 (n/a)</td><td>91.11 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.71 (-9.63%)</td><td>0.52 (-9.27%)</td><td>0.46 (-19.70%)</td><td>0.36 (-16.91%)</td><td>0.15 (+5.20%)</td><td>270.80 <b>(+20.36%)</b></td><td>201.00 (+12.24%)</td><td>211.40 <b>(+24.50%)</b></td><td>138.00 (+10.67%)</td><td>54.02 <b>(+36.33%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.79 (n/a)</td><td>0.57 (n/a)</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>225.00 (n/a)</td><td>179.08 (n/a)</td><td>169.80 (n/a)</td><td>124.70 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.66 (-19.28%)</td><td>0.48 <b>(-28.87%)</b></td><td>0.46 <b>(-30.10%)</b></td><td>0.39 <b>(-32.47%)</b></td><td>0.11 <b>(+20.57%)</b></td><td>250.60 <b>(+48.11%)</b></td><td>212.62 <b>(+43.70%)</b></td><td>212.50 <b>(+43.00%)</b></td><td>148.20 <b>(+23.91%)</b></td><td>40.69 <b>(+122.71%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.09 (n/a)</td><td>169.20 (n/a)</td><td>147.96 (n/a)</td><td>148.60 (n/a)</td><td>119.60 (n/a)</td><td>18.27 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.54 (-7.56%)</td><td>0.32 <b>(-36.06%)</b></td><td>0.35 <b>(-28.80%)</b></td><td>0.03 <b>(-92.97%)</b></td><td>0.19 <b>(+156.76%)</b></td><td>3556.20 <b>(+1322.48%)</b></td><td>919.98 <b>(+361.98%)</b></td><td>277.10 <b>(+40.45%)</b></td><td>181.10 (+8.18%)</td><td>1474.65 <b>(+4572.34%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.59 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>250.00 (n/a)</td><td>199.14 (n/a)</td><td>197.30 (n/a)</td><td>167.40 (n/a)</td><td>31.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.76 <b>(+25.10%)</b></td><td>0.51 (-0.71%)</td><td>0.44 (-12.37%)</td><td>0.41 (-6.39%)</td><td>0.15 <b>(+132.27%)</b></td><td>241.80 (+6.85%)</td><td>203.22 (+5.11%)</td><td>222.80 (+14.14%)</td><td>129.50 <b>(-20.06%)</b></td><td>47.28 <b>(+99.61%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.61 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.06 (n/a)</td><td>226.30 (n/a)</td><td>193.34 (n/a)</td><td>195.20 (n/a)</td><td>162.00 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.33 <b>(-50.16%)</b></td><td>0.30 <b>(-34.06%)</b></td><td>0.31 <b>(-32.66%)</b></td><td>0.27 (-9.89%)</td><td>0.03 <b>(-78.38%)</b></td><td>276.80 (+10.99%)</td><td>248.56 <b>(+41.99%)</b></td><td>237.30 <b>(+48.50%)</b></td><td>220.60 <b>(+100.73%)</b></td><td>25.79 <b>(-50.76%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.67 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.14 (n/a)</td><td>249.40 (n/a)</td><td>175.06 (n/a)</td><td>159.80 (n/a)</td><td>109.90 (n/a)</td><td>52.38 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.69 <b>(+33.07%)</b></td><td>0.42 (+6.00%)</td><td>0.39 (+6.82%)</td><td>0.29 (+6.35%)</td><td>0.16 <b>(+55.67%)</b></td><td>250.70 (-5.96%)</td><td>192.96 (-2.20%)</td><td>187.50 (-6.39%)</td><td>106.30 <b>(-24.88%)</b></td><td>56.62 (+9.82%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>266.60 (n/a)</td><td>197.30 (n/a)</td><td>200.30 (n/a)</td><td>141.50 (n/a)</td><td>51.56 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.68 <b>(+38.58%)</b></td><td>0.39 (-6.50%)</td><td>0.32 <b>(-23.17%)</b></td><td>0.09 <b>(-73.67%)</b></td><td>0.24 <b>(+289.17%)</b></td><td>838.70 <b>(+279.85%)</b></td><td>313.36 <b>(+74.87%)</b></td><td>227.60 <b>(+30.13%)</b></td><td>108.70 <b>(-27.82%)</b></td><td>301.29 <b>(+977.66%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>220.80 (n/a)</td><td>179.20 (n/a)</td><td>174.90 (n/a)</td><td>150.60 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.41 <b>(-33.15%)</b></td><td>0.36 (-18.21%)</td><td>0.36 (-15.86%)</td><td>0.27 (-16.42%)</td><td>0.06 <b>(-46.72%)</b></td><td>272.60 (+19.67%)</td><td>211.36 (+19.70%)</td><td>205.00 (+18.84%)</td><td>179.80 <b>(+49.58%)</b></td><td>38.25 (-3.63%)</td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.61 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>227.80 (n/a)</td><td>176.58 (n/a)</td><td>172.50 (n/a)</td><td>120.20 (n/a)</td><td>39.69 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.38 <b>(+55.86%)</b></td><td>0.69 (-3.15%)</td><td>0.63 (-7.09%)</td><td>0.10 <b>(-83.32%)</b></td><td>0.46 <b>(+336.35%)</b></td><td>1268.40 <b>(+499.43%)</b></td><td>393.86 <b>(+111.28%)</b></td><td>209.30 (+7.61%)</td><td>94.90 <b>(-35.84%)</b></td><td>491.49 <b>(+1885.88%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.89 (n/a)</td><td>0.71 (n/a)</td><td>0.67 (n/a)</td><td>0.62 (n/a)</td><td>0.11 (n/a)</td><td>211.60 (n/a)</td><td>186.42 (n/a)</td><td>194.50 (n/a)</td><td>147.90 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.05 (+10.61%)</td><td>0.59 (-16.12%)</td><td>0.74 (+11.55%)</td><td>0.01 <b>(-98.59%)</b></td><td>0.40 <b>(+176.21%)</b></td><td>16260.50 <b>(+7000.66%)</b></td><td>3411.50 <b>(+1687.44%)</b></td><td>177.20 (-10.37%)</td><td>124.60 (-9.58%)</td><td>7183.19 <b>(+21385.16%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.95 (n/a)</td><td>0.71 (n/a)</td><td>0.66 (n/a)</td><td>0.57 (n/a)</td><td>0.14 (n/a)</td><td>229.00 (n/a)</td><td>190.86 (n/a)</td><td>197.70 (n/a)</td><td>137.80 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>1.03 <b>(+29.98%)</b></td><td>0.46 <b>(-33.88%)</b></td><td>0.53 <b>(-24.44%)</b></td><td>0.07 <b>(-87.79%)</b></td><td>0.40 <b>(+333.60%)</b></td><td>1992.30 <b>(+719.20%)</b></td><td>877.44 <b>(+354.35%)</b></td><td>246.60 <b>(+32.37%)</b></td><td>127.20 <b>(-23.05%)</b></td><td>931.42 <b>(+3058.69%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.09 (n/a)</td><td>243.20 (n/a)</td><td>193.12 (n/a)</td><td>186.30 (n/a)</td><td>165.30 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.00 (+0.00%)</td><td>0.00 (+2.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+11.11%)</td><td>0.00 <b>(-55.28%)</b></td><td>4113.25 (-10.91%)</td><td>4004.38 (-3.68%)</td><td>4020.47 (-3.57%)</td><td>3790.67 (+0.66%)</td><td>130.67 <b>(-64.19%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4616.74 (n/a)</td><td>4157.53 (n/a)</td><td>4169.13 (n/a)</td><td>3765.84 (n/a)</td><td>364.88 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.00 (-8.70%)</td><td>0.00 (+7.37%)</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+26.67%)</b></td><td>0.00 <b>(-73.62%)</b></td><td>4279.42 <b>(-22.90%)</b></td><td>3991.39 (-9.95%)</td><td>3931.05 (-13.41%)</td><td>3835.13 (+7.50%)</td><td>185.74 <b>(-76.36%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>5550.60 (n/a)</td><td>4432.38 (n/a)</td><td>4539.79 (n/a)</td><td>3567.47 (n/a)</td><td>785.64 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>0.25 (-9.76%)</td><td>0.20 <b>(-20.75%)</b></td><td>0.21 <b>(-23.05%)</b></td><td>0.09 <b>(-49.02%)</b></td><td>0.06 <b>(+39.61%)</b></td><td>24431.47 <b>(+96.05%)</b></td><td>12360.57 <b>(+41.75%)</b></td><td>9957.05 <b>(+29.96%)</b></td><td>8368.62 (+10.80%)</td><td>6781.88 <b>(+221.11%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>12461.92 (n/a)</td><td>8720.16 (n/a)</td><td>7661.84 (n/a)</td><td>7552.69 (n/a)</td><td>2112.03 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.44 (+17.52%)</td><td>1.89 <b>(-22.00%)</b></td><td>2.11 (-13.98%)</td><td>0.00 <b>(-99.76%)</b></td><td>1.26 <b>(+211.41%)</b></td><td>117485.30 <b>(+41384.92%)</b></td><td>23690.72 <b>(+10582.08%)</b></td><td>248.40 (+16.24%)</td><td>152.20 (-14.92%)</td><td>52432.81 <b>(+131887.31%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>2.93 (n/a)</td><td>2.42 (n/a)</td><td>2.45 (n/a)</td><td>1.85 (n/a)</td><td>0.41 (n/a)</td><td>283.20 (n/a)</td><td>221.78 (n/a)</td><td>213.70 (n/a)</td><td>178.90 (n/a)</td><td>39.73 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>4.67 <b>(-20.50%)</b></td><td>4.10 (-9.26%)</td><td>4.33 (-6.76%)</td><td>3.27 (-4.67%)</td><td>0.55 <b>(-46.50%)</b></td><td>320.60 (+4.91%)</td><td>259.64 (+7.40%)</td><td>241.90 (+7.23%)</td><td>224.80 <b>(+25.80%)</b></td><td>38.02 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>5.87 (n/a)</td><td>4.52 (n/a)</td><td>4.65 (n/a)</td><td>3.43 (n/a)</td><td>1.02 (n/a)</td><td>305.60 (n/a)</td><td>241.74 (n/a)</td><td>225.60 (n/a)</td><td>178.70 (n/a)</td><td>54.79 (n/a)</td>
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
<td><code>9547629</code> — 2026-07-06 22:52:23</td><td>3.58 (+12.94%)</td><td>3.00 (+10.20%)</td><td>2.92 (+6.34%)</td><td>2.58 (+19.06%)</td><td>0.36 (-19.90%)</td><td>203.50 (-16.01%)</td><td>176.94 (-10.35%)</td><td>179.60 (-5.97%)</td><td>146.60 (-11.47%)</td><td>20.45 <b>(-40.06%)</b></td>
</tr>
<tr>
<td><code>573678d</code> — 2026-06-29 18:46:46</td><td>3.17 (n/a)</td><td>2.72 (n/a)</td><td>2.74 (n/a)</td><td>2.16 (n/a)</td><td>0.46 (n/a)</td><td>242.30 (n/a)</td><td>197.36 (n/a)</td><td>191.00 (n/a)</td><td>165.60 (n/a)</td><td>34.11 (n/a)</td>
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
