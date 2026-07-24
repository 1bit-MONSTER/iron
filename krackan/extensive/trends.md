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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+4.38%)</td><td>0.03 (-4.02%)</td><td>0.03 (+1.53%)</td><td>0.02 (-19.12%)</td><td>0.01 <b>(+39.32%)</b></td><td>274.10 <b>(+23.64%)</b></td><td>192.88 (+7.44%)</td><td>176.60 (-1.51%)</td><td>135.50 (-4.17%)</td><td>52.46 <b>(+68.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>179.52 (n/a)</td><td>179.30 (n/a)</td><td>141.40 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-17.18%)</td><td>0.04 (-3.12%)</td><td>0.04 (+14.80%)</td><td>0.03 (-4.18%)</td><td>0.01 <b>(-39.34%)</b></td><td>188.90 (+4.36%)</td><td>155.80 (+1.42%)</td><td>145.50 (-12.87%)</td><td>132.40 <b>(+20.69%)</b></td><td>22.60 <b>(-22.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>153.62 (n/a)</td><td>167.00 (n/a)</td><td>109.70 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-8.05%)</td><td>0.03 (-7.15%)</td><td>0.03 (-6.80%)</td><td>0.03 (-5.39%)</td><td>0.01 (-9.06%)</td><td>206.60 (+5.68%)</td><td>179.60 (+7.62%)</td><td>183.20 (+7.26%)</td><td>143.20 (+8.73%)</td><td>24.85 (+5.95%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>166.88 (n/a)</td><td>170.80 (n/a)</td><td>131.70 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-15.07%)</td><td>0.03 (-11.71%)</td><td>0.04 (-9.64%)</td><td>0.02 <b>(-28.00%)</b></td><td>0.01 (-12.79%)</td><td>293.50 <b>(+38.84%)</b></td><td>194.58 (+14.46%)</td><td>175.20 (+10.68%)</td><td>158.90 (+17.79%)</td><td>56.03 <b>(+46.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>170.00 (n/a)</td><td>158.30 (n/a)</td><td>134.90 (n/a)</td><td>38.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 <b>(-24.49%)</b></td><td>0.03 (-11.05%)</td><td>0.03 (-2.49%)</td><td>0.03 (-6.11%)</td><td>0.00 <b>(-72.44%)</b></td><td>203.20 (+6.50%)</td><td>192.40 (+11.00%)</td><td>189.90 (+2.59%)</td><td>184.30 <b>(+32.40%)</b></td><td>8.46 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>173.34 (n/a)</td><td>185.10 (n/a)</td><td>139.20 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+0.21%)</td><td>0.04 (-2.17%)</td><td>0.04 (+4.28%)</td><td>0.02 <b>(-38.03%)</b></td><td>0.01 <b>(+72.27%)</b></td><td>347.00 <b>(+61.40%)</b></td><td>186.98 (+13.01%)</td><td>156.20 (-4.11%)</td><td>132.10 (-0.23%)</td><td>90.76 <b>(+184.29%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>165.46 (n/a)</td><td>162.90 (n/a)</td><td>132.40 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 <b>(+23.55%)</b></td><td>0.03 (+9.62%)</td><td>0.03 (+5.19%)</td><td>0.03 (+19.89%)</td><td>0.01 <b>(+42.35%)</b></td><td>202.50 (-16.60%)</td><td>182.88 (-8.15%)</td><td>194.70 (-4.93%)</td><td>130.60 (-19.03%)</td><td>29.70 (-5.48%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.80 (n/a)</td><td>199.10 (n/a)</td><td>204.80 (n/a)</td><td>161.30 (n/a)</td><td>31.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-7.79%)</td><td>0.04 (+16.70%)</td><td>0.04 <b>(+28.68%)</b></td><td>0.03 <b>(+32.34%)</b></td><td>0.00 <b>(-58.88%)</b></td><td>187.90 <b>(-24.45%)</b></td><td>168.28 (-16.97%)</td><td>162.20 <b>(-22.28%)</b></td><td>153.10 (+8.43%)</td><td>14.07 <b>(-65.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.70 (n/a)</td><td>202.68 (n/a)</td><td>208.70 (n/a)</td><td>141.20 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (-0.33%)</td><td>0.07 (+1.13%)</td><td>0.07 (-4.00%)</td><td>0.06 (+8.25%)</td><td>0.01 <b>(-29.45%)</b></td><td>190.10 (-7.63%)</td><td>166.46 (-2.56%)</td><td>169.80 (+4.17%)</td><td>137.10 (+0.37%)</td><td>19.55 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>170.84 (n/a)</td><td>163.00 (n/a)</td><td>136.60 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (+8.14%)</td><td>0.08 (+1.56%)</td><td>0.07 (-9.01%)</td><td>0.06 (-4.36%)</td><td>0.02 <b>(+25.65%)</b></td><td>199.40 (+4.51%)</td><td>158.06 (-0.16%)</td><td>168.50 (+9.92%)</td><td>111.40 (-7.55%)</td><td>35.72 (+16.58%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>158.32 (n/a)</td><td>153.30 (n/a)</td><td>120.50 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (-12.28%)</td><td>0.08 (+0.18%)</td><td>0.08 (-7.30%)</td><td>0.07 <b>(+33.47%)</b></td><td>0.00 <b>(-69.84%)</b></td><td>174.70 <b>(-25.09%)</b></td><td>163.64 (-3.84%)</td><td>163.40 (+7.93%)</td><td>148.60 (+13.96%)</td><td>10.21 <b>(-74.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>170.18 (n/a)</td><td>151.40 (n/a)</td><td>130.40 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 <b>(+35.91%)</b></td><td>0.08 (+6.45%)</td><td>0.07 (-9.07%)</td><td>0.06 (-14.76%)</td><td>0.03 <b>(+170.27%)</b></td><td>212.50 (+17.34%)</td><td>162.62 (+1.04%)</td><td>186.70 (+9.95%)</td><td>94.50 <b>(-26.46%)</b></td><td>48.14 <b>(+134.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.10 (n/a)</td><td>160.94 (n/a)</td><td>169.80 (n/a)</td><td>128.50 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (+10.24%)</td><td>0.07 (+7.86%)</td><td>0.07 (-0.09%)</td><td>0.06 (+9.04%)</td><td>0.01 <b>(+35.28%)</b></td><td>201.40 (-8.29%)</td><td>179.08 (-6.91%)</td><td>186.40 (+0.05%)</td><td>153.50 (-9.33%)</td><td>21.56 (+11.22%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>192.38 (n/a)</td><td>186.30 (n/a)</td><td>169.30 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(+26.95%)</b></td><td>0.07 (+2.70%)</td><td>0.06 (-10.12%)</td><td>0.06 (-2.99%)</td><td>0.02 <b>(+178.85%)</b></td><td>204.20 (+3.08%)</td><td>174.44 (+0.15%)</td><td>190.90 (+11.31%)</td><td>124.70 <b>(-21.23%)</b></td><td>33.13 <b>(+123.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>174.18 (n/a)</td><td>171.50 (n/a)</td><td>158.30 (n/a)</td><td>14.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(+35.85%)</b></td><td>0.07 (+16.78%)</td><td>0.07 (+3.95%)</td><td>0.05 (-9.65%)</td><td>0.02 <b>(+244.08%)</b></td><td>249.40 (+10.70%)</td><td>179.06 (-10.82%)</td><td>182.70 (-3.84%)</td><td>139.20 <b>(-26.39%)</b></td><td>44.85 <b>(+175.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>200.78 (n/a)</td><td>190.00 (n/a)</td><td>189.10 (n/a)</td><td>16.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 <b>(+45.42%)</b></td><td>0.08 (+12.95%)</td><td>0.08 (+9.58%)</td><td>0.04 <b>(-23.10%)</b></td><td>0.03 <b>(+154.91%)</b></td><td>320.70 <b>(+30.05%)</b></td><td>182.24 (-2.17%)</td><td>160.00 (-8.78%)</td><td>113.80 <b>(-31.20%)</b></td><td>81.10 <b>(+137.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.60 (n/a)</td><td>186.28 (n/a)</td><td>175.40 (n/a)</td><td>165.40 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 <b>(+32.45%)</b></td><td>0.14 (+9.59%)</td><td>0.14 (+8.47%)</td><td>0.10 (-12.77%)</td><td>0.04 <b>(+142.02%)</b></td><td>256.80 (+14.64%)</td><td>180.04 (-4.84%)</td><td>173.50 (-7.81%)</td><td>124.60 <b>(-24.48%)</b></td><td>47.83 <b>(+112.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>189.20 (n/a)</td><td>188.20 (n/a)</td><td>165.00 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 <b>(+28.07%)</b></td><td>0.18 <b>(+21.07%)</b></td><td>0.19 <b>(+25.16%)</b></td><td>0.14 <b>(+20.41%)</b></td><td>0.03 <b>(+35.81%)</b></td><td>178.50 (-16.94%)</td><td>143.42 (-16.89%)</td><td>129.60 <b>(-20.10%)</b></td><td>111.90 <b>(-21.91%)</b></td><td>29.10 (-8.43%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.90 (n/a)</td><td>172.56 (n/a)</td><td>162.20 (n/a)</td><td>143.30 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (-3.24%)</td><td>0.14 (+0.13%)</td><td>0.13 (+4.59%)</td><td>0.11 (-1.16%)</td><td>0.02 (-12.24%)</td><td>228.30 (+1.15%)</td><td>184.82 (-0.62%)</td><td>184.50 (-4.40%)</td><td>144.60 (+3.36%)</td><td>29.87 (-7.17%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>225.70 (n/a)</td><td>185.98 (n/a)</td><td>193.00 (n/a)</td><td>139.90 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (+10.33%)</td><td>0.15 (+14.60%)</td><td>0.15 (+18.34%)</td><td>0.13 (+8.53%)</td><td>0.02 (+1.78%)</td><td>195.70 (-7.86%)</td><td>168.50 (-12.87%)</td><td>167.20 (-15.47%)</td><td>145.80 (-9.38%)</td><td>18.42 (-15.30%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>193.38 (n/a)</td><td>197.80 (n/a)</td><td>160.90 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (-10.84%)</td><td>0.12 (-13.76%)</td><td>0.13 (-9.89%)</td><td>0.07 <b>(-35.72%)</b></td><td>0.03 <b>(+26.00%)</b></td><td>352.60 <b>(+55.60%)</b></td><td>216.82 <b>(+21.67%)</b></td><td>193.90 (+10.99%)</td><td>164.90 (+12.10%)</td><td>77.11 <b>(+135.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>226.60 (n/a)</td><td>178.20 (n/a)</td><td>174.70 (n/a)</td><td>147.10 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+1.58%)</td><td>0.12 (-7.10%)</td><td>0.12 (-16.65%)</td><td>0.10 (-10.56%)</td><td>0.03 <b>(+34.31%)</b></td><td>256.30 (+11.82%)</td><td>205.38 (+9.50%)</td><td>209.60 (+19.98%)</td><td>153.20 (-1.54%)</td><td>42.17 <b>(+45.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>187.56 (n/a)</td><td>174.70 (n/a)</td><td>155.60 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (-11.97%)</td><td>0.13 (-8.25%)</td><td>0.12 (-16.44%)</td><td>0.10 (+17.96%)</td><td>0.03 <b>(-32.22%)</b></td><td>251.70 (-15.22%)</td><td>197.48 (+4.41%)</td><td>202.60 (+19.67%)</td><td>149.50 (+13.60%)</td><td>40.15 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>296.90 (n/a)</td><td>189.14 (n/a)</td><td>169.30 (n/a)</td><td>131.60 (n/a)</td><td>64.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+17.81%)</td><td>0.12 (+4.11%)</td><td>0.11 (-9.57%)</td><td>0.08 (-3.58%)</td><td>0.03 <b>(+53.14%)</b></td><td>301.80 (+3.71%)</td><td>217.16 (-0.89%)</td><td>229.30 (+10.56%)</td><td>149.80 (-15.13%)</td><td>60.85 <b>(+31.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>291.00 (n/a)</td><td>219.12 (n/a)</td><td>207.40 (n/a)</td><td>176.50 (n/a)</td><td>46.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.37 (-2.99%)</td><td>0.30 (-6.19%)</td><td>0.29 (-2.62%)</td><td>0.26 (-0.11%)</td><td>0.05 (-15.45%)</td><td>190.60 (+0.11%)</td><td>168.78 (+5.95%)</td><td>169.20 (+2.67%)</td><td>131.30 (+3.14%)</td><td>23.93 (-12.12%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>190.40 (n/a)</td><td>159.30 (n/a)</td><td>164.80 (n/a)</td><td>127.30 (n/a)</td><td>27.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.38 (+8.36%)</td><td>0.31 (+4.53%)</td><td>0.30 (+1.48%)</td><td>0.21 (-8.93%)</td><td>0.07 <b>(+55.99%)</b></td><td>229.30 (+9.82%)</td><td>165.28 (-1.89%)</td><td>164.50 (-1.44%)</td><td>127.80 (-7.66%)</td><td>40.54 <b>(+54.87%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>208.80 (n/a)</td><td>168.46 (n/a)</td><td>166.90 (n/a)</td><td>138.40 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.38 (+7.57%)</td><td>0.30 (+0.72%)</td><td>0.27 (-10.69%)</td><td>0.25 (+1.35%)</td><td>0.06 <b>(+43.77%)</b></td><td>198.80 (-1.34%)</td><td>168.08 (+0.49%)</td><td>181.50 (+11.97%)</td><td>130.10 (-7.07%)</td><td>29.09 <b>(+29.85%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>201.50 (n/a)</td><td>167.26 (n/a)</td><td>162.10 (n/a)</td><td>140.00 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.37 (+2.17%)</td><td>0.29 (+5.58%)</td><td>0.29 (+11.05%)</td><td>0.23 (+10.57%)</td><td>0.06 (-18.20%)</td><td>216.30 (-9.57%)</td><td>175.32 (-7.25%)</td><td>169.80 (-9.92%)</td><td>134.50 (-2.11%)</td><td>34.58 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>239.20 (n/a)</td><td>189.02 (n/a)</td><td>188.50 (n/a)</td><td>137.40 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.32 (+6.66%)</td><td>0.29 (+10.44%)</td><td>0.30 <b>(+20.10%)</b></td><td>0.23 (+4.15%)</td><td>0.03 (-0.38%)</td><td>209.90 (-3.98%)</td><td>173.34 (-9.53%)</td><td>164.80 (-16.77%)</td><td>154.00 (-6.21%)</td><td>21.73 (-7.37%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>218.60 (n/a)</td><td>191.60 (n/a)</td><td>198.00 (n/a)</td><td>164.20 (n/a)</td><td>23.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 (+7.71%)</td><td>0.29 (+2.78%)</td><td>0.28 (-2.77%)</td><td>0.23 (+8.32%)</td><td>0.05 (+11.49%)</td><td>214.40 (-7.71%)</td><td>174.42 (-2.65%)</td><td>177.90 (+2.89%)</td><td>144.10 (-7.15%)</td><td>28.43 (-8.07%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>232.30 (n/a)</td><td>179.16 (n/a)</td><td>172.90 (n/a)</td><td>155.20 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.35 <b>(+39.88%)</b></td><td>0.30 <b>(+28.31%)</b></td><td>0.30 <b>(+22.82%)</b></td><td>0.26 <b>(+30.87%)</b></td><td>0.04 <b>(+85.65%)</b></td><td>189.60 <b>(-23.58%)</b></td><td>165.72 <b>(-21.54%)</b></td><td>165.90 (-18.56%)</td><td>140.10 <b>(-28.52%)</b></td><td>21.91 (+1.53%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>248.10 (n/a)</td><td>211.22 (n/a)</td><td>203.70 (n/a)</td><td>196.00 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.43 <b>(+50.18%)</b></td><td>0.29 (+17.35%)</td><td>0.26 (-0.27%)</td><td>0.20 (+19.07%)</td><td>0.08 <b>(+80.73%)</b></td><td>243.80 (-16.02%)</td><td>179.28 (-12.73%)</td><td>186.70 (+0.27%)</td><td>115.20 <b>(-33.41%)</b></td><td>46.58 (-4.17%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>290.30 (n/a)</td><td>205.42 (n/a)</td><td>186.20 (n/a)</td><td>173.00 (n/a)</td><td>48.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-17.17%)</td><td>0.02 (-11.17%)</td><td>0.02 (-0.93%)</td><td>0.01 (+0.73%)</td><td>0.00 <b>(-54.68%)</b></td><td>189.00 (-0.74%)</td><td>171.06 (+10.26%)</td><td>165.30 (+0.92%)</td><td>150.00 <b>(+20.68%)</b></td><td>16.20 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.40 (n/a)</td><td>155.14 (n/a)</td><td>163.80 (n/a)</td><td>124.30 (n/a)</td><td>28.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-16.21%)</td><td>0.02 (-13.09%)</td><td>0.02 <b>(-20.32%)</b></td><td>0.01 (-7.21%)</td><td>0.00 <b>(-29.75%)</b></td><td>183.90 (+7.73%)</td><td>161.36 (+13.60%)</td><td>173.30 <b>(+25.49%)</b></td><td>125.60 (+19.39%)</td><td>24.81 (-12.30%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.70 (n/a)</td><td>142.04 (n/a)</td><td>138.10 (n/a)</td><td>105.20 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-8.65%)</td><td>0.02 (+4.63%)</td><td>0.02 <b>(+34.93%)</b></td><td>0.01 (+0.13%)</td><td>0.00 (-11.71%)</td><td>194.60 (-0.15%)</td><td>148.94 (-5.07%)</td><td>127.80 <b>(-25.87%)</b></td><td>120.80 (+9.52%)</td><td>34.66 (-3.84%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>156.90 (n/a)</td><td>172.40 (n/a)</td><td>110.30 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-17.66%)</td><td>0.01 (+4.55%)</td><td>0.01 (+5.95%)</td><td>0.01 <b>(+67.11%)</b></td><td>0.00 <b>(-66.47%)</b></td><td>205.70 <b>(-40.15%)</b></td><td>183.92 (-13.12%)</td><td>190.10 (-5.61%)</td><td>154.80 <b>(+21.51%)</b></td><td>19.06 <b>(-76.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>343.70 (n/a)</td><td>211.70 (n/a)</td><td>201.40 (n/a)</td><td>127.40 (n/a)</td><td>81.36 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-14.09%)</td><td>0.01 (-9.98%)</td><td>0.01 (-8.72%)</td><td>0.01 (-19.36%)</td><td>0.00 (-8.45%)</td><td>249.20 <b>(+23.98%)</b></td><td>186.70 (+11.62%)</td><td>188.10 (+9.55%)</td><td>144.10 (+16.40%)</td><td>43.83 <b>(+24.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.00 (n/a)</td><td>167.26 (n/a)</td><td>171.70 (n/a)</td><td>123.80 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 <b>(+26.07%)</b></td><td>0.02 (+12.24%)</td><td>0.02 <b>(+20.96%)</b></td><td>0.01 (-3.80%)</td><td>0.00 <b>(+134.62%)</b></td><td>205.20 (+3.95%)</td><td>158.78 (-8.09%)</td><td>147.00 (-17.32%)</td><td>121.20 <b>(-20.68%)</b></td><td>35.89 <b>(+98.20%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>172.76 (n/a)</td><td>177.80 (n/a)</td><td>152.80 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-10.59%)</td><td>0.01 (+0.45%)</td><td>0.01 (+2.23%)</td><td>0.01 (+8.33%)</td><td>0.00 <b>(-26.37%)</b></td><td>225.00 (-7.71%)</td><td>191.94 (-2.05%)</td><td>206.90 (-2.17%)</td><td>159.80 (+11.83%)</td><td>30.00 <b>(-25.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>243.80 (n/a)</td><td>195.96 (n/a)</td><td>211.50 (n/a)</td><td>142.90 (n/a)</td><td>40.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.01 (-1.96%)</td><td>0.01 (-3.24%)</td><td>0.01 (-2.01%)</td><td>0.01 (-9.90%)</td><td>0.00 <b>(+40.13%)</b></td><td>244.60 (+10.98%)</td><td>211.88 (+4.14%)</td><td>212.80 (+2.06%)</td><td>178.70 (+2.00%)</td><td>27.54 <b>(+61.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>220.40 (n/a)</td><td>203.46 (n/a)</td><td>208.50 (n/a)</td><td>175.20 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-1.49%)</td><td>0.03 (-6.71%)</td><td>0.03 (-11.94%)</td><td>0.02 (+1.26%)</td><td>0.01 (-0.09%)</td><td>219.80 (-1.21%)</td><td>179.72 (+7.08%)</td><td>186.30 (+13.53%)</td><td>124.80 (+1.55%)</td><td>35.08 (-3.94%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>167.84 (n/a)</td><td>164.10 (n/a)</td><td>122.90 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-7.20%)</td><td>0.03 (-7.90%)</td><td>0.03 (-2.10%)</td><td>0.03 (-13.07%)</td><td>0.00 (-11.91%)</td><td>194.20 (+15.05%)</td><td>163.86 (+8.47%)</td><td>170.40 (+2.16%)</td><td>135.40 (+7.80%)</td><td>24.55 (+7.68%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>168.80 (n/a)</td><td>151.06 (n/a)</td><td>166.80 (n/a)</td><td>125.60 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 <b>(+23.57%)</b></td><td>0.03 (+3.79%)</td><td>0.03 (+1.32%)</td><td>0.03 (-6.41%)</td><td>0.01 <b>(+119.87%)</b></td><td>205.30 (+6.87%)</td><td>172.32 (-0.71%)</td><td>181.10 (-1.31%)</td><td>121.40 (-19.07%)</td><td>35.85 <b>(+93.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>173.56 (n/a)</td><td>183.50 (n/a)</td><td>150.00 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 <b>(+32.75%)</b></td><td>0.03 (+4.99%)</td><td>0.03 (-8.11%)</td><td>0.02 (+3.25%)</td><td>0.01 <b>(+142.64%)</b></td><td>212.60 (-3.14%)</td><td>186.10 (-2.60%)</td><td>198.00 (+8.85%)</td><td>131.10 <b>(-24.66%)</b></td><td>31.86 <b>(+69.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>191.06 (n/a)</td><td>181.90 (n/a)</td><td>174.00 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (+8.69%)</td><td>0.03 (+6.90%)</td><td>0.03 (-3.56%)</td><td>0.03 (+4.25%)</td><td>0.01 <b>(+44.06%)</b></td><td>186.90 (-4.06%)</td><td>159.16 (-4.74%)</td><td>175.20 (+3.73%)</td><td>118.20 (-7.94%)</td><td>32.85 <b>(+32.29%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>167.08 (n/a)</td><td>168.90 (n/a)</td><td>128.40 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-7.61%)</td><td>0.03 (-10.17%)</td><td>0.03 <b>(-20.84%)</b></td><td>0.02 <b>(+24.21%)</b></td><td>0.00 <b>(-43.45%)</b></td><td>239.90 (-19.50%)</td><td>196.32 (+5.87%)</td><td>193.80 <b>(+26.34%)</b></td><td>160.10 (+8.18%)</td><td>31.02 <b>(-51.52%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>298.00 (n/a)</td><td>185.44 (n/a)</td><td>153.40 (n/a)</td><td>148.00 (n/a)</td><td>63.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 <b>(+26.41%)</b></td><td>0.03 (+6.52%)</td><td>0.03 (+4.15%)</td><td>0.02 (+2.38%)</td><td>0.01 <b>(+100.00%)</b></td><td>210.00 (-2.33%)</td><td>179.20 (-4.07%)</td><td>185.70 (-3.98%)</td><td>130.80 <b>(-20.92%)</b></td><td>33.73 <b>(+60.73%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.00 (n/a)</td><td>186.80 (n/a)</td><td>193.40 (n/a)</td><td>165.40 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+13.95%)</td><td>0.03 (+11.97%)</td><td>0.02 (-4.20%)</td><td>0.02 <b>(+55.14%)</b></td><td>0.00 <b>(-39.62%)</b></td><td>222.50 <b>(-35.54%)</b></td><td>204.20 (-13.81%)</td><td>213.40 (+4.35%)</td><td>171.20 (-12.25%)</td><td>21.10 <b>(-66.41%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>345.20 (n/a)</td><td>236.92 (n/a)</td><td>204.50 (n/a)</td><td>195.10 (n/a)</td><td>62.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (-0.75%)</td><td>0.06 (-6.41%)</td><td>0.06 (-11.85%)</td><td>0.05 (-5.26%)</td><td>0.01 (+3.27%)</td><td>196.20 (+5.54%)</td><td>171.48 (+6.97%)</td><td>177.00 (+13.46%)</td><td>131.10 (+0.69%)</td><td>24.13 (+4.08%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>185.90 (n/a)</td><td>160.30 (n/a)</td><td>156.00 (n/a)</td><td>130.20 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(+45.62%)</b></td><td>0.07 (+14.04%)</td><td>0.07 (+11.29%)</td><td>0.06 (+4.27%)</td><td>0.02 <b>(+249.20%)</b></td><td>183.10 (-4.09%)</td><td>152.64 (-9.83%)</td><td>150.40 (-10.16%)</td><td>108.80 <b>(-31.31%)</b></td><td>28.32 <b>(+122.20%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>169.28 (n/a)</td><td>167.40 (n/a)</td><td>158.40 (n/a)</td><td>12.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(+32.88%)</b></td><td>0.07 (+12.98%)</td><td>0.07 (+2.67%)</td><td>0.05 (+4.20%)</td><td>0.01 <b>(+72.57%)</b></td><td>227.70 (-4.05%)</td><td>164.04 (-9.46%)</td><td>161.00 (-2.60%)</td><td>121.60 <b>(-24.71%)</b></td><td>40.02 <b>(+25.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>181.18 (n/a)</td><td>165.30 (n/a)</td><td>161.50 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (+10.89%)</td><td>0.07 (+5.61%)</td><td>0.08 <b>(+29.47%)</b></td><td>0.04 (-12.29%)</td><td>0.02 <b>(+69.80%)</b></td><td>234.60 (+13.99%)</td><td>169.26 (-0.36%)</td><td>137.60 <b>(-22.74%)</b></td><td>122.90 (-9.83%)</td><td>54.03 <b>(+81.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>169.88 (n/a)</td><td>178.10 (n/a)</td><td>136.30 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (+19.75%)</td><td>0.07 <b>(+24.70%)</b></td><td>0.08 <b>(+65.89%)</b></td><td>0.05 (+5.02%)</td><td>0.02 <b>(+36.24%)</b></td><td>219.90 (-4.81%)</td><td>157.02 (-18.26%)</td><td>130.30 <b>(-39.73%)</b></td><td>117.70 (-16.52%)</td><td>45.43 (+8.59%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>192.10 (n/a)</td><td>216.20 (n/a)</td><td>141.00 (n/a)</td><td>41.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (-5.72%)</td><td>0.06 <b>(+23.12%)</b></td><td>0.06 <b>(+30.82%)</b></td><td>0.05 <b>(+70.81%)</b></td><td>0.01 <b>(-54.32%)</b></td><td>198.10 <b>(-41.46%)</b></td><td>167.56 <b>(-25.16%)</b></td><td>167.10 <b>(-23.56%)</b></td><td>140.50 (+6.12%)</td><td>21.87 <b>(-71.46%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>338.40 (n/a)</td><td>223.90 (n/a)</td><td>218.60 (n/a)</td><td>132.40 (n/a)</td><td>76.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (+14.55%)</td><td>0.07 (+11.57%)</td><td>0.07 (+11.09%)</td><td>0.06 (+5.40%)</td><td>0.01 <b>(+52.87%)</b></td><td>183.50 (-5.12%)</td><td>154.32 (-9.47%)</td><td>157.00 (-9.98%)</td><td>126.40 (-12.71%)</td><td>24.71 <b>(+25.86%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>170.46 (n/a)</td><td>174.40 (n/a)</td><td>144.80 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 <b>(+21.16%)</b></td><td>0.05 (+9.65%)</td><td>0.05 (+8.31%)</td><td>0.03 (-16.81%)</td><td>0.01 <b>(+134.18%)</b></td><td>329.70 <b>(+20.20%)</b></td><td>221.44 (-4.86%)</td><td>203.30 (-7.67%)</td><td>175.60 (-17.44%)</td><td>63.09 <b>(+138.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>274.30 (n/a)</td><td>232.74 (n/a)</td><td>220.20 (n/a)</td><td>212.70 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+1.55%)</td><td>0.14 (+5.00%)</td><td>0.14 (+4.49%)</td><td>0.10 (-10.54%)</td><td>0.03 <b>(+22.46%)</b></td><td>216.20 (+11.79%)</td><td>156.10 (-3.43%)</td><td>153.00 (-4.32%)</td><td>127.60 (-1.54%)</td><td>35.95 <b>(+34.25%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>193.40 (n/a)</td><td>161.64 (n/a)</td><td>159.90 (n/a)</td><td>129.60 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+16.42%)</td><td>0.11 (-9.59%)</td><td>0.12 (-5.47%)</td><td>0.06 <b>(-52.39%)</b></td><td>0.04 <b>(+377.01%)</b></td><td>379.70 <b>(+110.01%)</b></td><td>208.58 <b>(+25.06%)</b></td><td>174.80 (+5.81%)</td><td>131.00 (-14.10%)</td><td>97.84 <b>(+843.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>180.80 (n/a)</td><td>166.78 (n/a)</td><td>165.20 (n/a)</td><td>152.50 (n/a)</td><td>10.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+7.97%)</td><td>0.12 (-8.77%)</td><td>0.13 (+2.28%)</td><td>0.06 <b>(-52.43%)</b></td><td>0.04 <b>(+249.85%)</b></td><td>381.30 <b>(+110.20%)</b></td><td>201.74 <b>(+25.84%)</b></td><td>157.20 (-2.18%)</td><td>130.90 (-7.36%)</td><td>102.87 <b>(+619.69%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>160.32 (n/a)</td><td>160.70 (n/a)</td><td>141.30 (n/a)</td><td>14.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (-5.94%)</td><td>0.12 (+6.19%)</td><td>0.12 (+16.22%)</td><td>0.09 (-6.89%)</td><td>0.02 <b>(-22.02%)</b></td><td>221.30 (+7.38%)</td><td>177.98 (-6.49%)</td><td>174.30 (-13.93%)</td><td>146.40 (+6.32%)</td><td>27.05 (-8.26%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>206.10 (n/a)</td><td>190.34 (n/a)</td><td>202.50 (n/a)</td><td>137.70 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (+13.97%)</td><td>0.13 (+1.74%)</td><td>0.12 (-3.24%)</td><td>0.10 (+5.23%)</td><td>0.02 <b>(+20.02%)</b></td><td>207.20 (-5.00%)</td><td>169.90 (-1.47%)</td><td>169.00 (+3.30%)</td><td>133.10 (-12.26%)</td><td>26.27 (-2.47%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>218.10 (n/a)</td><td>172.44 (n/a)</td><td>163.60 (n/a)</td><td>151.70 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (+9.38%)</td><td>0.13 (+18.86%)</td><td>0.13 (+13.02%)</td><td>0.12 <b>(+48.73%)</b></td><td>0.01 <b>(-49.08%)</b></td><td>172.00 <b>(-32.76%)</b></td><td>159.26 (-17.94%)</td><td>162.80 (-11.52%)</td><td>141.40 (-8.60%)</td><td>11.97 <b>(-69.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>255.80 (n/a)</td><td>194.08 (n/a)</td><td>184.00 (n/a)</td><td>154.70 (n/a)</td><td>39.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (-6.09%)</td><td>0.12 (+3.27%)</td><td>0.11 (-5.08%)</td><td>0.10 <b>(+30.41%)</b></td><td>0.03 <b>(-28.25%)</b></td><td>220.60 <b>(-23.32%)</b></td><td>178.56 (-7.33%)</td><td>188.20 (+5.38%)</td><td>130.80 (+6.43%)</td><td>35.09 <b>(-42.82%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>287.70 (n/a)</td><td>192.68 (n/a)</td><td>178.60 (n/a)</td><td>122.90 (n/a)</td><td>61.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (-6.89%)</td><td>0.10 (-9.56%)</td><td>0.10 (-12.49%)</td><td>0.07 (-19.70%)</td><td>0.02 (-4.93%)</td><td>312.40 <b>(+24.56%)</b></td><td>222.42 (+11.41%)</td><td>212.70 (+14.23%)</td><td>173.00 (+7.39%)</td><td>54.16 <b>(+30.99%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>250.80 (n/a)</td><td>199.64 (n/a)</td><td>186.20 (n/a)</td><td>161.10 (n/a)</td><td>41.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>236.50 (n/a)</td><td>192.90 (n/a)</td><td>193.90 (n/a)</td><td>157.30 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>165.04 (n/a)</td><td>155.70 (n/a)</td><td>148.40 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>220.50 (n/a)</td><td>240.90 (n/a)</td><td>154.60 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>210.90 (n/a)</td><td>184.48 (n/a)</td><td>187.70 (n/a)</td><td>149.00 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>365.90 (n/a)</td><td>199.48 (n/a)</td><td>146.90 (n/a)</td><td>128.00 (n/a)</td><td>99.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>180.76 (n/a)</td><td>182.20 (n/a)</td><td>157.00 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>204.40 (n/a)</td><td>201.50 (n/a)</td><td>177.70 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>279.10 (n/a)</td><td>227.70 (n/a)</td><td>222.20 (n/a)</td><td>199.00 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.90 (n/a)</td><td>166.06 (n/a)</td><td>173.20 (n/a)</td><td>135.70 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>214.90 (n/a)</td><td>164.68 (n/a)</td><td>168.50 (n/a)</td><td>126.00 (n/a)</td><td>38.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>197.18 (n/a)</td><td>201.70 (n/a)</td><td>169.80 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>240.20 (n/a)</td><td>204.58 (n/a)</td><td>206.30 (n/a)</td><td>163.60 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (-5.77%)</td><td>0.25 (+0.58%)</td><td>0.25 (-9.41%)</td><td>0.24 <b>(+67.94%)</b></td><td>0.02 <b>(-75.59%)</b></td><td>204.60 <b>(-40.44%)</b></td><td>194.22 (-7.27%)</td><td>197.10 (+10.42%)</td><td>177.90 (+6.08%)</td><td>11.19 <b>(-85.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>343.50 (n/a)</td><td>209.44 (n/a)</td><td>178.50 (n/a)</td><td>167.70 (n/a)</td><td>75.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>230.90 (n/a)</td><td>185.42 (n/a)</td><td>185.50 (n/a)</td><td>152.80 (n/a)</td><td>29.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>214.00 (n/a)</td><td>185.12 (n/a)</td><td>181.20 (n/a)</td><td>151.70 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>230.50 (n/a)</td><td>200.92 (n/a)</td><td>199.40 (n/a)</td><td>174.10 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.60 (n/a)</td><td>196.12 (n/a)</td><td>169.50 (n/a)</td><td>119.60 (n/a)</td><td>80.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>179.40 (n/a)</td><td>181.80 (n/a)</td><td>152.50 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>184.90 (n/a)</td><td>197.50 (n/a)</td><td>129.70 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>183.64 (n/a)</td><td>181.20 (n/a)</td><td>151.90 (n/a)</td><td>35.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>190.92 (n/a)</td><td>194.10 (n/a)</td><td>152.90 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>181.92 (n/a)</td><td>178.10 (n/a)</td><td>165.10 (n/a)</td><td>13.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>189.56 (n/a)</td><td>190.20 (n/a)</td><td>163.10 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>229.80 (n/a)</td><td>210.98 (n/a)</td><td>217.90 (n/a)</td><td>191.60 (n/a)</td><td>17.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>167.80 (n/a)</td><td>169.50 (n/a)</td><td>138.00 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>197.38 (n/a)</td><td>196.50 (n/a)</td><td>166.20 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>190.08 (n/a)</td><td>192.20 (n/a)</td><td>159.10 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>195.42 (n/a)</td><td>190.40 (n/a)</td><td>177.70 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>182.60 (n/a)</td><td>158.50 (n/a)</td><td>156.70 (n/a)</td><td>134.30 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>191.30 (n/a)</td><td>191.20 (n/a)</td><td>169.00 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>225.70 (n/a)</td><td>200.40 (n/a)</td><td>204.90 (n/a)</td><td>156.10 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.30 (n/a)</td><td>170.66 (n/a)</td><td>171.90 (n/a)</td><td>143.40 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>160.32 (n/a)</td><td>144.70 (n/a)</td><td>134.60 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.70 (n/a)</td><td>150.62 (n/a)</td><td>161.20 (n/a)</td><td>122.80 (n/a)</td><td>23.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>154.20 (n/a)</td><td>139.80 (n/a)</td><td>121.70 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>185.88 (n/a)</td><td>188.60 (n/a)</td><td>152.00 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>316.80 (n/a)</td><td>201.12 (n/a)</td><td>166.30 (n/a)</td><td>144.20 (n/a)</td><td>69.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.30 (n/a)</td><td>178.36 (n/a)</td><td>184.50 (n/a)</td><td>150.70 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.30 (n/a)</td><td>195.78 (n/a)</td><td>175.40 (n/a)</td><td>153.50 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>160.20 (n/a)</td><td>148.00 (n/a)</td><td>141.10 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>154.10 (n/a)</td><td>167.70 (n/a)</td><td>126.70 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.60 (n/a)</td><td>209.40 (n/a)</td><td>198.50 (n/a)</td><td>127.50 (n/a)</td><td>62.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>185.76 (n/a)</td><td>185.40 (n/a)</td><td>126.90 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>184.76 (n/a)</td><td>187.40 (n/a)</td><td>149.50 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>186.90 (n/a)</td><td>186.60 (n/a)</td><td>148.00 (n/a)</td><td>29.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>187.48 (n/a)</td><td>183.30 (n/a)</td><td>129.20 (n/a)</td><td>42.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.70 (n/a)</td><td>233.62 (n/a)</td><td>209.10 (n/a)</td><td>196.30 (n/a)</td><td>62.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>178.80 (n/a)</td><td>180.20 (n/a)</td><td>162.10 (n/a)</td><td>12.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>163.90 (n/a)</td><td>167.40 (n/a)</td><td>148.30 (n/a)</td><td>12.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.90 (n/a)</td><td>155.54 (n/a)</td><td>167.40 (n/a)</td><td>116.90 (n/a)</td><td>30.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.60 (n/a)</td><td>136.66 (n/a)</td><td>124.90 (n/a)</td><td>118.60 (n/a)</td><td>28.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>168.80 (n/a)</td><td>154.26 (n/a)</td><td>153.30 (n/a)</td><td>136.00 (n/a)</td><td>13.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.20 (n/a)</td><td>163.22 (n/a)</td><td>154.80 (n/a)</td><td>132.20 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>167.20 (n/a)</td><td>151.58 (n/a)</td><td>157.90 (n/a)</td><td>130.10 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>198.00 (n/a)</td><td>204.60 (n/a)</td><td>180.50 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>217.80 (n/a)</td><td>179.58 (n/a)</td><td>172.20 (n/a)</td><td>158.20 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>224.60 (n/a)</td><td>187.48 (n/a)</td><td>186.60 (n/a)</td><td>131.50 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>187.10 (n/a)</td><td>151.84 (n/a)</td><td>139.10 (n/a)</td><td>126.00 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.60 (n/a)</td><td>158.62 (n/a)</td><td>160.40 (n/a)</td><td>127.10 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>189.44 (n/a)</td><td>193.30 (n/a)</td><td>156.80 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>166.20 (n/a)</td><td>155.60 (n/a)</td><td>151.60 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>196.56 (n/a)</td><td>194.70 (n/a)</td><td>167.90 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.92 (+14.00%)</td><td>4.24 (+4.87%)</td><td>4.17 (+2.64%)</td><td>3.73 (-0.30%)</td><td>0.45 <b>(+118.15%)</b></td><td>2523.80 (+0.30%)</td><td>2238.82 (-4.02%)</td><td>2254.20 (-2.57%)</td><td>1912.90 (-12.28%)</td><td>227.90 <b>(+89.59%)</b></td><td>1933.89 (+14.00%)</td><td>1666.65 (+4.87%)</td><td>1641.11 (+2.64%)</td><td>1465.82 (-0.30%)</td><td>175.92 <b>(+118.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>4.31 (n/a)</td><td>4.04 (n/a)</td><td>4.06 (n/a)</td><td>3.74 (n/a)</td><td>0.21 (n/a)</td><td>2516.20 (n/a)</td><td>2332.68 (n/a)</td><td>2313.70 (n/a)</td><td>2180.70 (n/a)</td><td>120.21 (n/a)</td><td>1696.41 (n/a)</td><td>1589.20 (n/a)</td><td>1598.88 (n/a)</td><td>1470.25 (n/a)</td><td>80.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.10 (+4.61%)</td><td>0.85 (-7.79%)</td><td>0.89 (-12.45%)</td><td>0.59 (-12.81%)</td><td>0.22 <b>(+38.42%)</b></td><td>375.10 (+14.67%)</td><td>274.84 (+11.83%)</td><td>249.50 (+14.24%)</td><td>201.70 (-4.41%)</td><td>76.21 <b>(+53.30%)</b></td><td>46.78 (+4.61%)</td><td>36.43 (-7.79%)</td><td>37.83 (-12.45%)</td><td>25.16 (-12.81%)</td><td>9.51 <b>(+38.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.05 (n/a)</td><td>0.93 (n/a)</td><td>1.01 (n/a)</td><td>0.68 (n/a)</td><td>0.16 (n/a)</td><td>327.10 (n/a)</td><td>245.76 (n/a)</td><td>218.40 (n/a)</td><td>211.00 (n/a)</td><td>49.71 (n/a)</td><td>44.72 (n/a)</td><td>39.51 (n/a)</td><td>43.21 (n/a)</td><td>28.85 (n/a)</td><td>6.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.13 (-4.15%)</td><td>1.04 (-0.84%)</td><td>1.02 (-0.69%)</td><td>0.98 (+10.93%)</td><td>0.06 <b>(-48.30%)</b></td><td>225.40 (-9.84%)</td><td>213.94 (+0.14%)</td><td>216.30 (+0.70%)</td><td>195.10 (+4.33%)</td><td>11.29 <b>(-52.33%)</b></td><td>48.38 (-4.15%)</td><td>44.22 (-0.84%)</td><td>43.63 (-0.69%)</td><td>41.87 (+10.93%)</td><td>2.46 <b>(-48.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.18 (n/a)</td><td>1.05 (n/a)</td><td>1.03 (n/a)</td><td>0.88 (n/a)</td><td>0.11 (n/a)</td><td>250.00 (n/a)</td><td>213.64 (n/a)</td><td>214.80 (n/a)</td><td>187.00 (n/a)</td><td>23.68 (n/a)</td><td>50.48 (n/a)</td><td>44.59 (n/a)</td><td>43.94 (n/a)</td><td>37.75 (n/a)</td><td>4.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.52 (+0.00%)</td><td>0.52 (+0.02%)</td><td>0.52 (+0.02%)</td><td>0.52 (-0.02%)</td><td>0.00 (-2.98%)</td><td>48771.60 (+0.02%)</td><td>48669.50 (-0.02%)</td><td>48640.20 (-0.02%)</td><td>48618.90 (-0.00%)</td><td>64.01 (-2.92%)</td><td>353.36 (+0.00%)</td><td>352.99 (+0.02%)</td><td>353.20 (+0.02%)</td><td>352.25 (-0.02%)</td><td>0.46 (-2.97%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48759.80 (n/a)</td><td>48679.28 (n/a)</td><td>48651.10 (n/a)</td><td>48620.40 (n/a)</td><td>65.94 (n/a)</td><td>353.35 (n/a)</td><td>352.92 (n/a)</td><td>353.12 (n/a)</td><td>352.34 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (+0.51%)</td><td>0.21 (+0.44%)</td><td>0.21 (+0.52%)</td><td>0.21 (+0.20%)</td><td>0.00 <b>(+30.28%)</b></td><td>118923.00 (-0.20%)</td><td>117833.10 (-0.44%)</td><td>117774.60 (-0.52%)</td><td>116817.60 (-0.51%)</td><td>841.23 <b>(+29.41%)</b></td><td>147.07 (+0.51%)</td><td>145.80 (+0.44%)</td><td>145.87 (+0.52%)</td><td>144.46 (+0.20%)</td><td>1.04 <b>(+30.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119161.50 (n/a)</td><td>118350.20 (n/a)</td><td>118387.10 (n/a)</td><td>117411.90 (n/a)</td><td>650.06 (n/a)</td><td>146.32 (n/a)</td><td>145.16 (n/a)</td><td>145.12 (n/a)</td><td>144.17 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.89 (-0.51%)</td><td>0.89 (-0.48%)</td><td>0.89 (-0.18%)</td><td>0.88 (-0.47%)</td><td>0.01 (+18.38%)</td><td>28716.80 (+0.47%)</td><td>28396.52 (+0.48%)</td><td>28242.80 (+0.18%)</td><td>28132.10 (+0.52%)</td><td>287.80 (+19.64%)</td><td>610.69 (-0.51%)</td><td>605.05 (-0.48%)</td><td>608.29 (-0.18%)</td><td>598.25 (-0.47%)</td><td>6.11 (+18.38%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28583.00 (n/a)</td><td>28259.88 (n/a)</td><td>28191.70 (n/a)</td><td>27987.90 (n/a)</td><td>240.56 (n/a)</td><td>613.83 (n/a)</td><td>607.96 (n/a)</td><td>609.39 (n/a)</td><td>601.05 (n/a)</td><td>5.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.61 (+2.94%)</td><td>3.50 (+1.92%)</td><td>3.51 (+0.53%)</td><td>3.35 (+1.02%)</td><td>0.10 (+1.55%)</td><td>7512.10 (-1.01%)</td><td>7196.24 (-1.88%)</td><td>7161.00 (-0.53%)</td><td>6971.20 (-2.85%)</td><td>201.31 (-1.77%)</td><td>2464.39 (+2.94%)</td><td>2388.81 (+1.92%)</td><td>2399.08 (+0.53%)</td><td>2286.97 (+1.02%)</td><td>65.79 (+1.55%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.51 (n/a)</td><td>3.43 (n/a)</td><td>3.50 (n/a)</td><td>3.32 (n/a)</td><td>0.09 (n/a)</td><td>7588.50 (n/a)</td><td>7334.38 (n/a)</td><td>7199.10 (n/a)</td><td>7175.90 (n/a)</td><td>204.95 (n/a)</td><td>2394.10 (n/a)</td><td>2343.82 (n/a)</td><td>2386.40 (n/a)</td><td>2263.93 (n/a)</td><td>64.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.26 (+3.30%)</td><td>3.01 (+5.94%)</td><td>2.97 (+6.04%)</td><td>2.75 (+2.97%)</td><td>0.21 (+7.88%)</td><td>9156.60 (-2.89%)</td><td>8400.96 (-5.58%)</td><td>8471.10 (-5.70%)</td><td>7719.70 (-3.19%)</td><td>575.29 (+1.89%)</td><td>2225.46 (+3.30%)</td><td>2052.67 (+5.94%)</td><td>2028.05 (+6.04%)</td><td>1876.23 (+2.97%)</td><td>140.38 (+7.88%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.16 (n/a)</td><td>2.84 (n/a)</td><td>2.80 (n/a)</td><td>2.67 (n/a)</td><td>0.19 (n/a)</td><td>9428.90 (n/a)</td><td>8897.32 (n/a)</td><td>8983.20 (n/a)</td><td>7974.30 (n/a)</td><td>564.61 (n/a)</td><td>2154.39 (n/a)</td><td>1937.50 (n/a)</td><td>1912.45 (n/a)</td><td>1822.04 (n/a)</td><td>130.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.31 (-0.90%)</td><td>3.21 (-1.30%)</td><td>3.21 (-0.92%)</td><td>3.13 (-0.88%)</td><td>0.07 (-10.87%)</td><td>8051.40 (+0.88%)</td><td>7833.44 (+1.31%)</td><td>7834.10 (+0.93%)</td><td>7602.40 (+0.91%)</td><td>169.78 (-8.99%)</td><td>2259.79 (-0.90%)</td><td>2193.97 (-1.30%)</td><td>2192.95 (-0.92%)</td><td>2133.78 (-0.88%)</td><td>47.66 (-10.87%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.34 (n/a)</td><td>3.26 (n/a)</td><td>3.24 (n/a)</td><td>3.15 (n/a)</td><td>0.08 (n/a)</td><td>7980.90 (n/a)</td><td>7732.38 (n/a)</td><td>7761.90 (n/a)</td><td>7533.80 (n/a)</td><td>186.55 (n/a)</td><td>2280.36 (n/a)</td><td>2222.84 (n/a)</td><td>2213.37 (n/a)</td><td>2152.63 (n/a)</td><td>53.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.78 (-0.00%)</td><td>0.78 (-0.07%)</td><td>0.78 (-0.01%)</td><td>0.78 (-0.21%)</td><td>0.00 <b>(+453.90%)</b></td><td>96695.00 (+0.21%)</td><td>96538.14 (+0.07%)</td><td>96468.70 (+0.01%)</td><td>96447.10 (+0.00%)</td><td>113.16 <b>(+455.10%)</b></td><td>712.51 (-0.00%)</td><td>711.84 (-0.07%)</td><td>712.35 (-0.01%)</td><td>710.68 (-0.21%)</td><td>0.83 <b>(+453.87%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96492.70 (n/a)</td><td>96466.54 (n/a)</td><td>96459.50 (n/a)</td><td>96443.60 (n/a)</td><td>20.39 (n/a)</td><td>712.54 (n/a)</td><td>712.37 (n/a)</td><td>712.42 (n/a)</td><td>712.17 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.73 (-0.37%)</td><td>0.73 (-0.16%)</td><td>0.73 (-0.14%)</td><td>0.73 (-0.11%)</td><td>0.00 <b>(-40.33%)</b></td><td>103907.10 (+0.11%)</td><td>103752.34 (+0.16%)</td><td>103774.80 (+0.14%)</td><td>103622.90 (+0.37%)</td><td>123.25 <b>(-40.02%)</b></td><td>663.17 (-0.37%)</td><td>662.34 (-0.16%)</td><td>662.20 (-0.14%)</td><td>661.36 (-0.11%)</td><td>0.79 <b>(-40.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103793.10 (n/a)</td><td>103586.80 (n/a)</td><td>103632.00 (n/a)</td><td>103240.70 (n/a)</td><td>205.49 (n/a)</td><td>665.62 (n/a)</td><td>663.40 (n/a)</td><td>663.11 (n/a)</td><td>662.08 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.70 (-0.61%)</td><td>0.70 (-0.05%)</td><td>0.70 (+0.15%)</td><td>0.69 (+0.03%)</td><td>0.00 <b>(-63.32%)</b></td><td>108896.20 (-0.03%)</td><td>108597.56 (+0.04%)</td><td>108551.30 (-0.15%)</td><td>108430.20 (+0.61%)</td><td>175.36 <b>(-63.08%)</b></td><td>633.77 (-0.61%)</td><td>632.79 (-0.05%)</td><td>633.06 (+0.15%)</td><td>631.05 (+0.03%)</td><td>1.02 <b>(-63.32%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108928.70 (n/a)</td><td>108550.08 (n/a)</td><td>108713.80 (n/a)</td><td>107770.90 (n/a)</td><td>475.02 (n/a)</td><td>637.64 (n/a)</td><td>633.08 (n/a)</td><td>632.11 (n/a)</td><td>630.87 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.08 (-5.39%)</td><td>6.76 (-3.17%)</td><td>7.03 (+1.63%)</td><td>6.16 (-2.91%)</td><td>0.41 (-10.07%)</td><td>1446.10 (+3.00%)</td><td>1322.72 (+3.23%)</td><td>1267.30 (-1.60%)</td><td>1258.40 (+5.69%)</td><td>84.07 (-2.23%)</td><td>426.64 (-5.39%)</td><td>407.15 (-3.17%)</td><td>423.64 (+1.63%)</td><td>371.24 (-2.91%)</td><td>24.98 (-10.07%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.49 (n/a)</td><td>6.98 (n/a)</td><td>6.92 (n/a)</td><td>6.35 (n/a)</td><td>0.46 (n/a)</td><td>1404.00 (n/a)</td><td>1281.34 (n/a)</td><td>1287.90 (n/a)</td><td>1190.60 (n/a)</td><td>85.99 (n/a)</td><td>450.94 (n/a)</td><td>420.48 (n/a)</td><td>416.85 (n/a)</td><td>382.37 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.91 (-0.90%)</td><td>6.46 (+0.42%)</td><td>6.28 (-7.37%)</td><td>6.10 <b>(+20.28%)</b></td><td>0.37 <b>(-53.48%)</b></td><td>1460.30 (-16.86%)</td><td>1383.24 (-1.56%)</td><td>1418.80 (+7.97%)</td><td>1290.00 (+0.91%)</td><td>77.48 <b>(-61.51%)</b></td><td>416.16 (-0.90%)</td><td>389.12 (+0.42%)</td><td>378.41 (-7.37%)</td><td>367.65 <b>(+20.28%)</b></td><td>22.17 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.97 (n/a)</td><td>6.43 (n/a)</td><td>6.78 (n/a)</td><td>5.07 (n/a)</td><td>0.79 (n/a)</td><td>1756.50 (n/a)</td><td>1405.22 (n/a)</td><td>1314.10 (n/a)</td><td>1278.40 (n/a)</td><td>201.29 (n/a)</td><td>419.95 (n/a)</td><td>387.50 (n/a)</td><td>408.53 (n/a)</td><td>305.65 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.57 (+1.87%)</td><td>5.82 (-2.05%)</td><td>5.79 (-6.10%)</td><td>4.72 (-2.62%)</td><td>0.71 (+13.26%)</td><td>1887.10 (+2.69%)</td><td>1552.34 (+2.38%)</td><td>1538.80 (+6.49%)</td><td>1357.20 (-1.84%)</td><td>205.87 (+12.66%)</td><td>395.57 (+1.87%)</td><td>350.35 (-2.05%)</td><td>348.88 (-6.10%)</td><td>284.49 (-2.62%)</td><td>42.70 (+13.26%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.45 (n/a)</td><td>5.94 (n/a)</td><td>6.17 (n/a)</td><td>4.85 (n/a)</td><td>0.63 (n/a)</td><td>1837.70 (n/a)</td><td>1516.32 (n/a)</td><td>1445.00 (n/a)</td><td>1382.60 (n/a)</td><td>182.74 (n/a)</td><td>388.32 (n/a)</td><td>357.69 (n/a)</td><td>371.55 (n/a)</td><td>292.14 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.93 (-6.21%)</td><td>7.61 (-1.87%)</td><td>7.80 (-0.60%)</td><td>7.26 (+1.21%)</td><td>0.32 <b>(-40.25%)</b></td><td>4802.50 (-1.20%)</td><td>4586.98 (+1.67%)</td><td>4471.20 (+0.61%)</td><td>4398.70 (+6.62%)</td><td>194.98 <b>(-37.17%)</b></td><td>488.21 (-6.21%)</td><td>468.84 (-1.87%)</td><td>480.29 (-0.60%)</td><td>447.16 (+1.21%)</td><td>19.68 <b>(-40.25%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.45 (n/a)</td><td>7.76 (n/a)</td><td>7.84 (n/a)</td><td>7.17 (n/a)</td><td>0.53 (n/a)</td><td>4860.70 (n/a)</td><td>4511.80 (n/a)</td><td>4444.30 (n/a)</td><td>4125.40 (n/a)</td><td>310.34 (n/a)</td><td>520.55 (n/a)</td><td>477.78 (n/a)</td><td>483.20 (n/a)</td><td>441.80 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.57 (-5.09%)</td><td>7.32 (-3.48%)</td><td>7.38 (-3.06%)</td><td>7.02 (+2.35%)</td><td>0.26 <b>(-39.63%)</b></td><td>4964.40 (-2.29%)</td><td>4769.94 (+3.42%)</td><td>4725.40 (+3.15%)</td><td>4604.00 (+5.37%)</td><td>173.10 <b>(-38.24%)</b></td><td>466.44 (-5.09%)</td><td>450.68 (-3.48%)</td><td>454.46 (-3.06%)</td><td>432.57 (+2.35%)</td><td>16.25 <b>(-39.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.98 (n/a)</td><td>7.58 (n/a)</td><td>7.61 (n/a)</td><td>6.86 (n/a)</td><td>0.44 (n/a)</td><td>5081.00 (n/a)</td><td>4612.26 (n/a)</td><td>4580.90 (n/a)</td><td>4369.50 (n/a)</td><td>280.26 (n/a)</td><td>491.47 (n/a)</td><td>466.91 (n/a)</td><td>468.79 (n/a)</td><td>422.65 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.32 (-2.79%)</td><td>7.20 (-1.64%)</td><td>7.28 (-1.49%)</td><td>6.86 (+0.50%)</td><td>0.19 <b>(-32.81%)</b></td><td>5079.20 (-0.50%)</td><td>4847.50 (+1.60%)</td><td>4790.40 (+1.52%)</td><td>4760.90 (+2.87%)</td><td>131.24 <b>(-31.42%)</b></td><td>451.07 (-2.79%)</td><td>443.26 (-1.64%)</td><td>448.29 (-1.49%)</td><td>422.80 (+0.50%)</td><td>11.61 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>7.53 (n/a)</td><td>7.32 (n/a)</td><td>7.39 (n/a)</td><td>6.83 (n/a)</td><td>0.28 (n/a)</td><td>5104.50 (n/a)</td><td>4771.02 (n/a)</td><td>4718.90 (n/a)</td><td>4628.10 (n/a)</td><td>191.37 (n/a)</td><td>464.01 (n/a)</td><td>450.67 (n/a)</td><td>455.08 (n/a)</td><td>420.70 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.79 (+0.33%)</td><td>0.79 (+0.04%)</td><td>0.79 (+0.00%)</td><td>0.79 (-0.02%)</td><td>0.00 <b>(+166.36%)</b></td><td>95916.80 (+0.02%)</td><td>95727.14 (-0.04%)</td><td>95740.10 (-0.00%)</td><td>95396.80 (-0.32%)</td><td>206.68 <b>(+165.42%)</b></td><td>720.35 (+0.33%)</td><td>717.87 (+0.04%)</td><td>717.77 (+0.00%)</td><td>716.45 (-0.02%)</td><td>1.55 <b>(+166.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95902.10 (n/a)</td><td>95765.88 (n/a)</td><td>95740.70 (n/a)</td><td>95707.20 (n/a)</td><td>77.87 (n/a)</td><td>718.02 (n/a)</td><td>717.58 (n/a)</td><td>717.77 (n/a)</td><td>716.56 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.73 (+0.05%)</td><td>0.73 (-0.03%)</td><td>0.73 (+0.00%)</td><td>0.73 (-0.21%)</td><td>0.00 <b>(+376.59%)</b></td><td>103157.80 (+0.21%)</td><td>102949.30 (+0.03%)</td><td>102917.10 (-0.00%)</td><td>102832.00 (-0.05%)</td><td>122.53 <b>(+377.40%)</b></td><td>668.27 (+0.05%)</td><td>667.51 (-0.03%)</td><td>667.72 (+0.00%)</td><td>666.16 (-0.21%)</td><td>0.79 <b>(+376.67%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102942.40 (n/a)</td><td>102914.40 (n/a)</td><td>102918.50 (n/a)</td><td>102884.80 (n/a)</td><td>25.67 (n/a)</td><td>667.93 (n/a)</td><td>667.73 (n/a)</td><td>667.71 (n/a)</td><td>667.55 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.70 (+0.13%)</td><td>0.70 (-0.05%)</td><td>0.70 (-0.05%)</td><td>0.70 (-0.22%)</td><td>0.00 <b>(+117.92%)</b></td><td>108231.40 (+0.22%)</td><td>107895.50 (+0.05%)</td><td>107904.60 (+0.05%)</td><td>107559.90 (-0.13%)</td><td>237.77 <b>(+118.13%)</b></td><td>638.90 (+0.13%)</td><td>636.91 (-0.05%)</td><td>636.85 (-0.05%)</td><td>634.93 (-0.22%)</td><td>1.40 <b>(+117.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107990.30 (n/a)</td><td>107843.24 (n/a)</td><td>107855.00 (n/a)</td><td>107695.50 (n/a)</td><td>109.00 (n/a)</td><td>638.09 (n/a)</td><td>637.22 (n/a)</td><td>637.15 (n/a)</td><td>636.35 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.11 (+0.84%)</td><td>3.47 (-5.02%)</td><td>3.32 (-9.08%)</td><td>2.93 (-9.96%)</td><td>0.58 <b>(+100.06%)</b></td><td>2751.30 (+11.06%)</td><td>2375.06 (+7.11%)</td><td>2431.20 (+9.98%)</td><td>1960.90 (-0.83%)</td><td>389.54 <b>(+119.59%)</b></td><td>1078.02 (+0.84%)</td><td>910.09 (-5.02%)</td><td>869.49 (-9.08%)</td><td>768.34 (-9.96%)</td><td>153.07 <b>(+100.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>4.08 (n/a)</td><td>3.65 (n/a)</td><td>3.65 (n/a)</td><td>3.25 (n/a)</td><td>0.29 (n/a)</td><td>2477.20 (n/a)</td><td>2217.42 (n/a)</td><td>2210.60 (n/a)</td><td>1977.40 (n/a)</td><td>177.40 (n/a)</td><td>1069.06 (n/a)</td><td>958.22 (n/a)</td><td>956.28 (n/a)</td><td>853.35 (n/a)</td><td>76.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.50 <b>(+43.52%)</b></td><td>0.35 (+7.93%)</td><td>0.32 (+0.57%)</td><td>0.29 (-6.16%)</td><td>0.08 <b>(+402.98%)</b></td><td>4363.10 (+6.57%)</td><td>3691.44 (-4.10%)</td><td>3894.90 (-0.56%)</td><td>2510.00 <b>(-30.32%)</b></td><td>697.98 <b>(+256.41%)</b></td><td>26.74 <b>(+43.52%)</b></td><td>18.85 (+7.93%)</td><td>17.23 (+0.57%)</td><td>15.38 (-6.16%)</td><td>4.50 <b>(+402.98%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.02 (n/a)</td><td>4094.20 (n/a)</td><td>3849.40 (n/a)</td><td>3916.90 (n/a)</td><td>3602.20 (n/a)</td><td>195.84 (n/a)</td><td>18.63 (n/a)</td><td>17.47 (n/a)</td><td>17.13 (n/a)</td><td>16.39 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.27 (-1.37%)</td><td>4.77 (-0.16%)</td><td>4.74 (-0.75%)</td><td>3.44 (+4.58%)</td><td>1.00 (-7.56%)</td><td>1931.10 (-4.38%)</td><td>1444.34 (-0.61%)</td><td>1403.50 (+0.75%)</td><td>1060.30 (+1.39%)</td><td>311.65 (-11.49%)</td><td>1938.34 (-1.37%)</td><td>1475.08 (-0.16%)</td><td>1464.34 (-0.75%)</td><td>1064.24 (+4.58%)</td><td>310.20 (-7.56%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.36 (n/a)</td><td>4.78 (n/a)</td><td>4.78 (n/a)</td><td>3.29 (n/a)</td><td>1.09 (n/a)</td><td>2019.60 (n/a)</td><td>1453.18 (n/a)</td><td>1393.00 (n/a)</td><td>1045.80 (n/a)</td><td>352.12 (n/a)</td><td>1965.27 (n/a)</td><td>1477.40 (n/a)</td><td>1475.40 (n/a)</td><td>1017.65 (n/a)</td><td>335.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.30 <b>(+24.90%)</b></td><td>0.21 (+11.46%)</td><td>0.19 (+6.07%)</td><td>0.17 (+8.74%)</td><td>0.05 <b>(+59.99%)</b></td><td>0.30 <b>(+24.90%)</b></td><td>0.21 (+11.46%)</td><td>0.18 (+6.07%)</td><td>0.17 (+8.74%)</td><td>0.05 <b>(+59.99%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.32 (+0.40%)</td><td>13.10 (+7.54%)</td><td>13.21 (+9.88%)</td><td>12.55 (+14.87%)</td><td>0.32 <b>(-68.99%)</b></td><td>13.32 (+0.40%)</td><td>13.10 (+7.54%)</td><td>13.21 (+9.88%)</td><td>12.54 (+14.87%)</td><td>0.32 <b>(-68.99%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.27 (n/a)</td><td>12.19 (n/a)</td><td>12.03 (n/a)</td><td>10.92 (n/a)</td><td>1.02 (n/a)</td><td>13.26 (n/a)</td><td>12.18 (n/a)</td><td>12.02 (n/a)</td><td>10.92 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>25.16 (+3.84%)</td><td>24.88 (+6.18%)</td><td>24.94 (+3.43%)</td><td>24.58 (+16.51%)</td><td>0.23 <b>(-82.65%)</b></td><td>25.15 (+3.84%)</td><td>24.87 (+6.18%)</td><td>24.92 (+3.43%)</td><td>24.56 (+16.51%)</td><td>0.23 <b>(-82.65%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>24.23 (n/a)</td><td>23.44 (n/a)</td><td>24.11 (n/a)</td><td>21.09 (n/a)</td><td>1.34 (n/a)</td><td>24.22 (n/a)</td><td>23.42 (n/a)</td><td>24.10 (n/a)</td><td>21.08 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>43.03 (+4.66%)</td><td>37.82 (-5.44%)</td><td>40.81 (+2.67%)</td><td>22.72 <b>(-41.26%)</b></td><td>8.53 <b>(+742.63%)</b></td><td>43.00 (+4.66%)</td><td>37.80 (-5.44%)</td><td>40.79 (+2.67%)</td><td>22.71 <b>(-41.26%)</b></td><td>8.52 <b>(+742.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>41.11 (n/a)</td><td>40.00 (n/a)</td><td>39.75 (n/a)</td><td>38.68 (n/a)</td><td>1.01 (n/a)</td><td>41.09 (n/a)</td><td>39.98 (n/a)</td><td>39.73 (n/a)</td><td>38.66 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>44.53 (-1.21%)</td><td>43.01 (-1.54%)</td><td>42.57 (-1.76%)</td><td>42.05 (-0.91%)</td><td>1.01 (-15.23%)</td><td>44.50 (-1.21%)</td><td>42.99 (-1.54%)</td><td>42.55 (-1.76%)</td><td>42.03 (-0.91%)</td><td>1.01 (-15.23%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>45.07 (n/a)</td><td>43.69 (n/a)</td><td>43.34 (n/a)</td><td>42.44 (n/a)</td><td>1.19 (n/a)</td><td>45.04 (n/a)</td><td>43.66 (n/a)</td><td>43.31 (n/a)</td><td>42.41 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.44 (+0.37%)</td><td>12.70 (+0.78%)</td><td>12.95 (-1.72%)</td><td>11.27 (+0.92%)</td><td>0.87 (-11.57%)</td><td>13.43 (+0.37%)</td><td>12.69 (+0.78%)</td><td>12.94 (-1.72%)</td><td>11.26 (+0.92%)</td><td>0.87 (-11.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.39 (n/a)</td><td>12.60 (n/a)</td><td>13.17 (n/a)</td><td>11.16 (n/a)</td><td>0.98 (n/a)</td><td>13.38 (n/a)</td><td>12.59 (n/a)</td><td>13.16 (n/a)</td><td>11.16 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>24.41 (-0.10%)</td><td>23.83 (+0.19%)</td><td>24.05 (-0.47%)</td><td>23.09 (+2.61%)</td><td>0.53 <b>(-35.00%)</b></td><td>24.40 (-0.10%)</td><td>23.82 (+0.19%)</td><td>24.03 (-0.47%)</td><td>23.08 (+2.61%)</td><td>0.53 <b>(-35.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>24.43 (n/a)</td><td>23.78 (n/a)</td><td>24.16 (n/a)</td><td>22.50 (n/a)</td><td>0.82 (n/a)</td><td>24.42 (n/a)</td><td>23.77 (n/a)</td><td>24.15 (n/a)</td><td>22.49 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>44.31 (+7.07%)</td><td>40.84 (+1.67%)</td><td>40.20 (+1.58%)</td><td>38.30 (-2.19%)</td><td>2.26 <b>(+110.13%)</b></td><td>44.29 (+7.07%)</td><td>40.81 (+1.67%)</td><td>40.17 (+1.58%)</td><td>38.28 (-2.19%)</td><td>2.25 <b>(+110.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>41.39 (n/a)</td><td>40.17 (n/a)</td><td>39.57 (n/a)</td><td>39.16 (n/a)</td><td>1.07 (n/a)</td><td>41.36 (n/a)</td><td>40.14 (n/a)</td><td>39.55 (n/a)</td><td>39.14 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>45.28 (+0.54%)</td><td>42.59 (-2.87%)</td><td>43.41 (-2.84%)</td><td>39.03 (-7.08%)</td><td>2.62 <b>(+91.91%)</b></td><td>45.26 (+0.54%)</td><td>42.56 (-2.87%)</td><td>43.39 (-2.84%)</td><td>39.01 (-7.08%)</td><td>2.62 <b>(+91.91%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>45.04 (n/a)</td><td>43.84 (n/a)</td><td>44.68 (n/a)</td><td>42.00 (n/a)</td><td>1.37 (n/a)</td><td>45.01 (n/a)</td><td>43.82 (n/a)</td><td>44.65 (n/a)</td><td>41.98 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.57 (+3.06%)</td><td>8.86 (+0.17%)</td><td>8.77 (-3.11%)</td><td>8.05 (-1.93%)</td><td>0.56 (+14.70%)</td><td>9.55 (+3.06%)</td><td>8.84 (+0.17%)</td><td>8.75 (-3.11%)</td><td>8.04 (-1.93%)</td><td>0.56 (+14.70%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.29 (n/a)</td><td>8.84 (n/a)</td><td>9.05 (n/a)</td><td>8.21 (n/a)</td><td>0.49 (n/a)</td><td>9.27 (n/a)</td><td>8.83 (n/a)</td><td>9.04 (n/a)</td><td>8.20 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.98 (+7.50%)</td><td>0.85 (+4.59%)</td><td>0.79 (-1.44%)</td><td>0.70 (-1.22%)</td><td>0.12 <b>(+62.38%)</b></td><td>0.97 (+7.50%)</td><td>0.83 (+4.59%)</td><td>0.78 (-1.44%)</td><td>0.69 (-1.22%)</td><td>0.12 <b>(+62.38%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.71 (n/a)</td><td>0.07 (n/a)</td><td>0.90 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.28 (+4.60%)</td><td>1.17 (+2.17%)</td><td>1.19 (+1.27%)</td><td>1.02 (-3.39%)</td><td>0.10 <b>(+29.74%)</b></td><td>1.27 (+4.60%)</td><td>1.16 (+2.17%)</td><td>1.18 (+1.27%)</td><td>1.01 (-3.39%)</td><td>0.10 <b>(+29.74%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.23 (n/a)</td><td>1.15 (n/a)</td><td>1.18 (n/a)</td><td>1.06 (n/a)</td><td>0.08 (n/a)</td><td>1.21 (n/a)</td><td>1.13 (n/a)</td><td>1.17 (n/a)</td><td>1.04 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>17.66 (+3.69%)</td><td>15.65 (+4.75%)</td><td>15.92 (+9.85%)</td><td>12.91 (+2.78%)</td><td>1.74 (-3.55%)</td><td>17.46 (+3.69%)</td><td>15.47 (+4.75%)</td><td>15.74 (+9.85%)</td><td>12.76 (+2.78%)</td><td>1.72 (-3.55%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>17.03 (n/a)</td><td>14.94 (n/a)</td><td>14.49 (n/a)</td><td>12.56 (n/a)</td><td>1.80 (n/a)</td><td>16.84 (n/a)</td><td>14.77 (n/a)</td><td>14.33 (n/a)</td><td>12.42 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>12.48 (+1.90%)</td><td>12.10 (+8.62%)</td><td>12.11 (+0.30%)</td><td>11.73 <b>(+63.71%)</b></td><td>0.32 <b>(-85.69%)</b></td><td>12.26 (+1.90%)</td><td>11.89 (+8.62%)</td><td>11.89 (+0.30%)</td><td>11.53 <b>(+63.71%)</b></td><td>0.31 <b>(-85.69%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>12.24 (n/a)</td><td>11.14 (n/a)</td><td>12.07 (n/a)</td><td>7.17 (n/a)</td><td>2.22 (n/a)</td><td>12.03 (n/a)</td><td>10.95 (n/a)</td><td>11.86 (n/a)</td><td>7.04 (n/a)</td><td>2.18 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>7.55 (-14.47%)</td><td>6.61 (-19.58%)</td><td>6.98 (-17.10%)</td><td>5.57 <b>(-20.42%)</b></td><td>0.81 (+12.58%)</td><td>7.42 (-14.47%)</td><td>6.50 (-19.58%)</td><td>6.86 (-17.10%)</td><td>5.48 <b>(-20.42%)</b></td><td>0.80 (+12.58%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.82 (n/a)</td><td>8.22 (n/a)</td><td>8.42 (n/a)</td><td>7.00 (n/a)</td><td>0.72 (n/a)</td><td>8.67 (n/a)</td><td>8.08 (n/a)</td><td>8.28 (n/a)</td><td>6.88 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>6.59 (+5.80%)</td><td>5.77 (+5.17%)</td><td>5.82 (+4.95%)</td><td>5.12 (+8.42%)</td><td>0.58 (+8.63%)</td><td>6.49 (+5.80%)</td><td>5.68 (+5.17%)</td><td>5.73 (+4.95%)</td><td>5.03 (+8.42%)</td><td>0.58 (+8.63%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.23 (n/a)</td><td>5.49 (n/a)</td><td>5.55 (n/a)</td><td>4.72 (n/a)</td><td>0.54 (n/a)</td><td>6.13 (n/a)</td><td>5.40 (n/a)</td><td>5.46 (n/a)</td><td>4.64 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>164.30 (n/a)</td><td>163.00 (n/a)</td><td>123.00 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>156.94 (n/a)</td><td>149.80 (n/a)</td><td>115.50 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.00 (n/a)</td><td>191.74 (n/a)</td><td>184.70 (n/a)</td><td>132.80 (n/a)</td><td>53.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.50 (n/a)</td><td>164.28 (n/a)</td><td>153.00 (n/a)</td><td>139.20 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>163.34 (n/a)</td><td>160.60 (n/a)</td><td>118.40 (n/a)</td><td>39.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>332.70 (n/a)</td><td>203.52 (n/a)</td><td>172.30 (n/a)</td><td>158.60 (n/a)</td><td>72.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>180.18 (n/a)</td><td>183.30 (n/a)</td><td>144.70 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.60 (n/a)</td><td>222.16 (n/a)</td><td>218.20 (n/a)</td><td>203.50 (n/a)</td><td>16.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.00 (n/a)</td><td>202.30 (n/a)</td><td>206.10 (n/a)</td><td>178.70 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.90 (n/a)</td><td>190.64 (n/a)</td><td>190.10 (n/a)</td><td>165.00 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>181.52 (n/a)</td><td>179.80 (n/a)</td><td>155.90 (n/a)</td><td>25.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>312.40 (n/a)</td><td>211.32 (n/a)</td><td>219.90 (n/a)</td><td>108.00 (n/a)</td><td>73.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>185.08 (n/a)</td><td>169.80 (n/a)</td><td>146.60 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>186.26 (n/a)</td><td>178.00 (n/a)</td><td>141.90 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.80 (n/a)</td><td>171.10 (n/a)</td><td>174.50 (n/a)</td><td>151.00 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.20 (n/a)</td><td>202.74 (n/a)</td><td>189.90 (n/a)</td><td>137.90 (n/a)</td><td>53.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.20 (n/a)</td><td>167.50 (n/a)</td><td>174.00 (n/a)</td><td>122.90 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>201.30 (n/a)</td><td>207.10 (n/a)</td><td>169.70 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>171.32 (n/a)</td><td>170.20 (n/a)</td><td>154.70 (n/a)</td><td>11.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.30 (n/a)</td><td>199.00 (n/a)</td><td>201.80 (n/a)</td><td>126.70 (n/a)</td><td>45.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.80 (n/a)</td><td>177.98 (n/a)</td><td>167.60 (n/a)</td><td>132.10 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.20 (n/a)</td><td>194.22 (n/a)</td><td>198.80 (n/a)</td><td>152.80 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>182.22 (n/a)</td><td>190.10 (n/a)</td><td>157.00 (n/a)</td><td>17.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>343.50 (n/a)</td><td>206.86 (n/a)</td><td>184.00 (n/a)</td><td>141.00 (n/a)</td><td>78.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 <b>(+39.92%)</b></td><td>0.19 (+16.44%)</td><td>0.19 (+15.87%)</td><td>0.15 (-2.19%)</td><td>0.03 <b>(+437.39%)</b></td><td>212.40 (+2.26%)</td><td>173.44 (-12.17%)</td><td>169.60 (-13.69%)</td><td>135.20 <b>(-28.54%)</b></td><td>29.44 <b>(+293.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>197.48 (n/a)</td><td>196.50 (n/a)</td><td>189.20 (n/a)</td><td>7.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.00 (n/a)</td><td>165.78 (n/a)</td><td>156.50 (n/a)</td><td>127.70 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>239.30 (n/a)</td><td>184.90 (n/a)</td><td>183.20 (n/a)</td><td>150.20 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>259.40 (n/a)</td><td>194.26 (n/a)</td><td>192.00 (n/a)</td><td>119.20 (n/a)</td><td>58.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>235.80 (n/a)</td><td>187.20 (n/a)</td><td>212.00 (n/a)</td><td>124.90 (n/a)</td><td>49.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.60 (n/a)</td><td>188.52 (n/a)</td><td>184.60 (n/a)</td><td>148.40 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>200.36 (n/a)</td><td>194.50 (n/a)</td><td>159.70 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.40 (n/a)</td><td>201.26 (n/a)</td><td>190.10 (n/a)</td><td>169.20 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-15.61%)</td><td>0.02 (+0.14%)</td><td>0.02 (-0.02%)</td><td>0.02 <b>(+29.54%)</b></td><td>0.00 <b>(-56.36%)</b></td><td>205.80 <b>(-22.81%)</b></td><td>180.12 (-4.42%)</td><td>184.30 (+0.00%)</td><td>157.90 (+18.54%)</td><td>19.57 <b>(-61.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>266.60 (n/a)</td><td>188.44 (n/a)</td><td>184.30 (n/a)</td><td>133.20 (n/a)</td><td>50.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-7.81%)</td><td>0.02 (-9.53%)</td><td>0.02 (-18.15%)</td><td>0.02 (-0.64%)</td><td>0.00 (-12.46%)</td><td>203.60 (+0.64%)</td><td>169.00 (+9.98%)</td><td>177.40 <b>(+22.18%)</b></td><td>133.90 (+8.51%)</td><td>26.94 (-8.43%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>153.66 (n/a)</td><td>145.20 (n/a)</td><td>123.40 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+11.38%)</td><td>0.02 (+3.81%)</td><td>0.03 (+8.50%)</td><td>0.02 (-14.62%)</td><td>0.00 <b>(+46.67%)</b></td><td>229.50 (+17.15%)</td><td>169.52 (-1.97%)</td><td>159.70 (-7.85%)</td><td>134.40 (-10.22%)</td><td>35.82 <b>(+60.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>172.92 (n/a)</td><td>173.30 (n/a)</td><td>149.70 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 <b>(-24.75%)</b></td><td>0.02 <b>(-21.29%)</b></td><td>0.02 (-17.19%)</td><td>0.02 (-19.20%)</td><td>0.00 <b>(-39.67%)</b></td><td>229.80 <b>(+23.75%)</b></td><td>193.98 <b>(+26.06%)</b></td><td>193.70 <b>(+20.76%)</b></td><td>165.60 <b>(+32.91%)</b></td><td>24.29 (+0.62%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>153.88 (n/a)</td><td>160.40 (n/a)</td><td>124.60 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+14.14%)</td><td>0.03 (+0.78%)</td><td>0.02 (-10.22%)</td><td>0.02 (-7.39%)</td><td>0.01 <b>(+115.02%)</b></td><td>195.40 (+8.02%)</td><td>164.96 (+1.86%)</td><td>181.70 (+11.40%)</td><td>127.80 (-12.35%)</td><td>32.53 <b>(+103.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.90 (n/a)</td><td>161.94 (n/a)</td><td>163.10 (n/a)</td><td>145.80 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+18.27%)</td><td>0.03 (+6.06%)</td><td>0.03 (+14.81%)</td><td>0.02 (-10.73%)</td><td>0.01 <b>(+215.38%)</b></td><td>205.60 (+12.04%)</td><td>164.02 (-2.94%)</td><td>145.70 (-12.91%)</td><td>131.60 (-15.42%)</td><td>33.69 <b>(+203.73%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.50 (n/a)</td><td>168.98 (n/a)</td><td>167.30 (n/a)</td><td>155.60 (n/a)</td><td>11.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+5.68%)</td><td>0.02 (+1.37%)</td><td>0.02 <b>(-20.37%)</b></td><td>0.02 <b>(+72.13%)</b></td><td>0.01 <b>(-30.76%)</b></td><td>212.80 <b>(-41.91%)</b></td><td>179.50 (-9.89%)</td><td>191.70 <b>(+25.54%)</b></td><td>132.30 (-5.36%)</td><td>34.69 <b>(-63.44%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>199.20 (n/a)</td><td>152.70 (n/a)</td><td>139.80 (n/a)</td><td>94.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-11.45%)</td><td>0.02 (-12.99%)</td><td>0.02 (-16.95%)</td><td>0.01 <b>(-25.28%)</b></td><td>0.00 (+12.15%)</td><td>337.00 <b>(+33.84%)</b></td><td>238.02 (+17.09%)</td><td>228.50 <b>(+20.39%)</b></td><td>194.50 (+12.95%)</td><td>57.99 <b>(+72.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.80 (n/a)</td><td>203.28 (n/a)</td><td>189.80 (n/a)</td><td>172.20 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+6.95%)</td><td>0.05 (-2.07%)</td><td>0.05 (-8.15%)</td><td>0.04 (-6.32%)</td><td>0.01 <b>(+38.38%)</b></td><td>200.10 (+6.78%)</td><td>160.70 (+4.00%)</td><td>170.90 (+8.85%)</td><td>119.70 (-6.56%)</td><td>34.34 <b>(+38.79%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.40 (n/a)</td><td>154.52 (n/a)</td><td>157.00 (n/a)</td><td>128.10 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-19.56%)</td><td>0.05 (-7.96%)</td><td>0.05 (+0.15%)</td><td>0.04 (-12.53%)</td><td>0.01 <b>(-40.32%)</b></td><td>210.20 (+14.30%)</td><td>173.52 (+7.62%)</td><td>165.50 (-0.18%)</td><td>158.30 <b>(+24.35%)</b></td><td>20.83 (-14.45%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>161.24 (n/a)</td><td>165.80 (n/a)</td><td>127.30 (n/a)</td><td>24.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-15.58%)</td><td>0.05 (-2.08%)</td><td>0.05 (+2.72%)</td><td>0.04 <b>(+31.84%)</b></td><td>0.00 <b>(-68.46%)</b></td><td>196.30 <b>(-24.18%)</b></td><td>175.58 (-2.47%)</td><td>174.40 (-2.68%)</td><td>158.40 (+18.47%)</td><td>13.51 <b>(-72.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.90 (n/a)</td><td>180.02 (n/a)</td><td>179.20 (n/a)</td><td>133.70 (n/a)</td><td>48.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+9.13%)</td><td>0.05 (+1.28%)</td><td>0.05 (-1.84%)</td><td>0.04 (-7.79%)</td><td>0.01 <b>(+60.08%)</b></td><td>228.60 (+8.44%)</td><td>175.28 (+1.56%)</td><td>172.70 (+1.83%)</td><td>131.50 (-8.36%)</td><td>42.63 <b>(+56.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>172.58 (n/a)</td><td>169.60 (n/a)</td><td>143.50 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+8.33%)</td><td>0.05 <b>(-20.75%)</b></td><td>0.04 <b>(-27.19%)</b></td><td>0.03 <b>(-48.14%)</b></td><td>0.02 <b>(+131.87%)</b></td><td>319.90 <b>(+92.83%)</b></td><td>200.58 <b>(+38.71%)</b></td><td>198.20 <b>(+37.35%)</b></td><td>116.60 (-7.68%)</td><td>75.24 <b>(+321.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.90 (n/a)</td><td>144.60 (n/a)</td><td>144.30 (n/a)</td><td>126.30 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+6.29%)</td><td>0.05 (+3.92%)</td><td>0.05 (-9.85%)</td><td>0.04 <b>(+83.51%)</b></td><td>0.01 <b>(-58.82%)</b></td><td>184.70 <b>(-45.52%)</b></td><td>173.26 (-11.48%)</td><td>179.10 (+10.97%)</td><td>144.70 (-5.98%)</td><td>16.18 <b>(-79.84%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>339.00 (n/a)</td><td>195.72 (n/a)</td><td>161.40 (n/a)</td><td>153.90 (n/a)</td><td>80.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+0.45%)</td><td>0.05 (-8.29%)</td><td>0.04 (-18.17%)</td><td>0.04 (+9.64%)</td><td>0.01 (-0.73%)</td><td>209.20 (-8.77%)</td><td>177.02 (+8.51%)</td><td>184.60 <b>(+22.25%)</b></td><td>130.30 (-0.46%)</td><td>32.97 (-13.66%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>163.14 (n/a)</td><td>151.00 (n/a)</td><td>130.90 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-2.17%)</td><td>0.04 (-15.28%)</td><td>0.04 <b>(-26.19%)</b></td><td>0.03 <b>(-22.16%)</b></td><td>0.01 <b>(+23.05%)</b></td><td>275.00 <b>(+28.44%)</b></td><td>210.76 <b>(+21.34%)</b></td><td>219.40 <b>(+35.43%)</b></td><td>136.00 (+2.18%)</td><td>54.09 <b>(+54.23%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>173.70 (n/a)</td><td>162.00 (n/a)</td><td>133.10 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-15.35%)</td><td>0.04 (-18.90%)</td><td>0.04 <b>(-23.45%)</b></td><td>0.03 <b>(-28.69%)</b></td><td>0.01 (+12.68%)</td><td>283.90 <b>(+40.27%)</b></td><td>216.52 <b>(+26.10%)</b></td><td>216.50 <b>(+30.58%)</b></td><td>159.00 (+18.13%)</td><td>50.69 <b>(+82.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>171.70 (n/a)</td><td>165.80 (n/a)</td><td>134.60 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-0.75%)</td><td>0.04 (+4.08%)</td><td>0.04 (+2.70%)</td><td>0.03 <b>(+54.17%)</b></td><td>0.01 <b>(-48.53%)</b></td><td>242.90 <b>(-35.14%)</b></td><td>213.76 (-9.70%)</td><td>217.20 (-2.60%)</td><td>173.50 (+0.75%)</td><td>26.43 <b>(-67.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>374.50 (n/a)</td><td>236.72 (n/a)</td><td>223.00 (n/a)</td><td>172.20 (n/a)</td><td>81.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 <b>(-20.35%)</b></td><td>0.09 (-18.38%)</td><td>0.09 (-18.41%)</td><td>0.08 (-13.45%)</td><td>0.01 <b>(-42.84%)</b></td><td>208.80 (+15.55%)</td><td>176.54 <b>(+20.95%)</b></td><td>178.90 <b>(+22.53%)</b></td><td>150.30 <b>(+25.56%)</b></td><td>22.09 (-14.98%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.70 (n/a)</td><td>145.96 (n/a)</td><td>146.00 (n/a)</td><td>119.70 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (-3.48%)</td><td>0.11 (+5.97%)</td><td>0.11 (+8.40%)</td><td>0.09 (+7.69%)</td><td>0.02 (-0.82%)</td><td>186.20 (-7.13%)</td><td>154.26 (-5.56%)</td><td>151.70 (-7.73%)</td><td>119.50 (+3.64%)</td><td>31.33 (+2.07%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>163.34 (n/a)</td><td>164.40 (n/a)</td><td>115.30 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (-3.99%)</td><td>0.10 (+8.38%)</td><td>0.10 (+7.09%)</td><td>0.08 <b>(+82.85%)</b></td><td>0.02 <b>(-39.72%)</b></td><td>207.50 <b>(-45.31%)</b></td><td>160.96 (-18.20%)</td><td>157.80 (-6.63%)</td><td>130.20 (+4.16%)</td><td>32.41 <b>(-68.82%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>379.40 (n/a)</td><td>196.78 (n/a)</td><td>169.00 (n/a)</td><td>125.00 (n/a)</td><td>103.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(-28.72%)</b></td><td>0.08 <b>(-23.67%)</b></td><td>0.08 (-15.47%)</td><td>0.05 <b>(-30.27%)</b></td><td>0.02 <b>(-33.46%)</b></td><td>302.30 <b>(+43.41%)</b></td><td>211.42 <b>(+30.75%)</b></td><td>199.60 (+18.32%)</td><td>173.50 <b>(+40.37%)</b></td><td>52.60 <b>(+42.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.80 (n/a)</td><td>161.70 (n/a)</td><td>168.70 (n/a)</td><td>123.60 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(-22.22%)</b></td><td>0.09 (-3.53%)</td><td>0.09 (-4.99%)</td><td>0.08 <b>(+47.22%)</b></td><td>0.01 <b>(-71.54%)</b></td><td>198.60 <b>(-32.06%)</b></td><td>182.28 (-3.14%)</td><td>180.20 (+5.26%)</td><td>167.00 <b>(+28.56%)</b></td><td>14.93 <b>(-76.06%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>292.30 (n/a)</td><td>188.18 (n/a)</td><td>171.20 (n/a)</td><td>129.90 (n/a)</td><td>62.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (-6.20%)</td><td>0.09 (+2.96%)</td><td>0.09 (+1.31%)</td><td>0.08 (+19.03%)</td><td>0.01 <b>(-49.71%)</b></td><td>198.60 (-15.99%)</td><td>187.20 (-4.35%)</td><td>192.60 (-1.33%)</td><td>165.90 (+6.62%)</td><td>13.84 <b>(-54.60%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>195.72 (n/a)</td><td>195.20 (n/a)</td><td>155.60 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (+7.84%)</td><td>0.09 (-8.15%)</td><td>0.08 (-16.70%)</td><td>0.07 (-11.73%)</td><td>0.02 <b>(+54.82%)</b></td><td>226.50 (+13.25%)</td><td>195.86 (+10.53%)</td><td>203.30 <b>(+20.01%)</b></td><td>142.40 (-7.29%)</td><td>32.49 <b>(+54.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>177.20 (n/a)</td><td>169.40 (n/a)</td><td>153.60 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (-1.52%)</td><td>0.08 (+1.14%)</td><td>0.08 (-1.08%)</td><td>0.07 (+8.15%)</td><td>0.01 (-13.73%)</td><td>235.20 (-7.55%)</td><td>206.56 (-1.57%)</td><td>205.10 (+1.08%)</td><td>179.80 (+1.58%)</td><td>23.44 (-19.85%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>209.86 (n/a)</td><td>202.90 (n/a)</td><td>177.00 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-8.02%)</td><td>0.20 (-8.95%)</td><td>0.20 (-19.09%)</td><td>0.17 (+18.97%)</td><td>0.03 <b>(-45.25%)</b></td><td>190.70 (-15.95%)</td><td>162.80 (+6.07%)</td><td>163.50 <b>(+23.58%)</b></td><td>138.60 (+8.71%)</td><td>21.01 <b>(-50.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>226.90 (n/a)</td><td>153.48 (n/a)</td><td>132.30 (n/a)</td><td>127.50 (n/a)</td><td>42.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (-15.75%)</td><td>0.19 (-7.56%)</td><td>0.18 (-9.81%)</td><td>0.16 (-8.33%)</td><td>0.03 <b>(-22.65%)</b></td><td>210.90 (+9.05%)</td><td>174.40 (+7.46%)</td><td>177.40 (+10.88%)</td><td>147.70 (+18.63%)</td><td>27.02 (-4.04%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>193.40 (n/a)</td><td>162.30 (n/a)</td><td>160.00 (n/a)</td><td>124.50 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 <b>(+30.64%)</b></td><td>0.22 (+5.07%)</td><td>0.23 (+4.46%)</td><td>0.12 <b>(-24.84%)</b></td><td>0.08 <b>(+104.01%)</b></td><td>269.40 <b>(+33.04%)</b></td><td>164.60 (+3.89%)</td><td>144.30 (-4.31%)</td><td>95.10 <b>(-23.49%)</b></td><td>66.05 <b>(+111.19%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.50 (n/a)</td><td>158.44 (n/a)</td><td>150.80 (n/a)</td><td>124.30 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (-8.99%)</td><td>0.17 <b>(-20.16%)</b></td><td>0.19 (-15.52%)</td><td>0.09 <b>(-42.60%)</b></td><td>0.06 <b>(+83.99%)</b></td><td>354.90 <b>(+74.23%)</b></td><td>215.76 <b>(+37.30%)</b></td><td>176.10 (+18.43%)</td><td>148.50 (+9.84%)</td><td>87.90 <b>(+228.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>203.70 (n/a)</td><td>157.14 (n/a)</td><td>148.70 (n/a)</td><td>135.20 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 <b>(+30.53%)</b></td><td>0.19 (+2.36%)</td><td>0.19 (-1.62%)</td><td>0.13 (-18.72%)</td><td>0.06 <b>(+138.86%)</b></td><td>257.30 <b>(+23.05%)</b></td><td>183.70 (+3.16%)</td><td>176.30 (+1.67%)</td><td>117.80 <b>(-23.36%)</b></td><td>52.15 <b>(+123.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>178.08 (n/a)</td><td>173.40 (n/a)</td><td>153.70 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (-18.76%)</td><td>0.18 (-11.15%)</td><td>0.17 <b>(-21.31%)</b></td><td>0.16 (+1.64%)</td><td>0.02 <b>(-47.22%)</b></td><td>208.00 (-1.61%)</td><td>188.72 (+10.57%)</td><td>197.90 <b>(+27.10%)</b></td><td>166.60 <b>(+23.13%)</b></td><td>19.54 <b>(-38.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.40 (n/a)</td><td>170.68 (n/a)</td><td>155.70 (n/a)</td><td>135.30 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (-9.41%)</td><td>0.15 (-11.19%)</td><td>0.15 (-11.35%)</td><td>0.13 (-12.67%)</td><td>0.02 (+8.29%)</td><td>253.10 (+14.52%)</td><td>218.60 (+13.16%)</td><td>212.60 (+12.79%)</td><td>189.60 (+10.36%)</td><td>30.31 <b>(+37.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.00 (n/a)</td><td>193.18 (n/a)</td><td>188.50 (n/a)</td><td>171.80 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+12.88%)</td><td>0.03 (+8.88%)</td><td>0.02 (+8.12%)</td><td>0.02 (-2.33%)</td><td>0.00 <b>(+39.81%)</b></td><td>204.10 (+2.41%)</td><td>165.08 (-7.24%)</td><td>173.20 (-7.53%)</td><td>134.40 (-11.40%)</td><td>28.58 <b>(+24.64%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.30 (n/a)</td><td>177.96 (n/a)</td><td>187.30 (n/a)</td><td>151.70 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 <b>(+20.27%)</b></td><td>0.03 (-2.24%)</td><td>0.02 (-16.36%)</td><td>0.02 (-6.58%)</td><td>0.01 <b>(+42.70%)</b></td><td>249.00 (+7.05%)</td><td>170.60 (+6.13%)</td><td>176.00 (+19.57%)</td><td>105.20 (-16.84%)</td><td>55.28 <b>(+26.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>160.74 (n/a)</td><td>147.20 (n/a)</td><td>126.50 (n/a)</td><td>43.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-15.21%)</td><td>0.02 (+1.33%)</td><td>0.02 (+12.92%)</td><td>0.02 (+7.59%)</td><td>0.00 <b>(-67.99%)</b></td><td>238.80 (-7.05%)</td><td>216.58 (-3.25%)</td><td>211.60 (-11.43%)</td><td>207.40 (+17.97%)</td><td>12.70 <b>(-64.93%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.90 (n/a)</td><td>223.86 (n/a)</td><td>238.90 (n/a)</td><td>175.80 (n/a)</td><td>36.22 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-6.54%)</td><td>0.02 (-0.82%)</td><td>0.02 (+0.13%)</td><td>0.01 (-14.59%)</td><td>0.00 (+6.80%)</td><td>286.20 (+17.10%)</td><td>212.46 (+1.59%)</td><td>195.90 (-0.15%)</td><td>186.60 (+7.00%)</td><td>41.51 <b>(+34.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.40 (n/a)</td><td>209.14 (n/a)</td><td>196.20 (n/a)</td><td>174.40 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (+11.58%)</td><td>0.03 (+18.81%)</td><td>0.03 <b>(+23.16%)</b></td><td>0.02 (+9.59%)</td><td>0.01 (+4.05%)</td><td>191.50 (-8.77%)</td><td>141.30 (-16.21%)</td><td>132.60 (-18.80%)</td><td>106.40 (-10.36%)</td><td>31.66 (-14.17%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>168.64 (n/a)</td><td>163.30 (n/a)</td><td>118.70 (n/a)</td><td>36.88 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 <b>(+30.88%)</b></td><td>0.03 (+6.20%)</td><td>0.02 (+4.76%)</td><td>0.02 (+4.75%)</td><td>0.01 <b>(+82.14%)</b></td><td>202.90 (-4.52%)</td><td>167.62 (-3.04%)</td><td>168.70 (-4.53%)</td><td>107.10 <b>(-23.61%)</b></td><td>37.54 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>172.88 (n/a)</td><td>176.70 (n/a)</td><td>140.20 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+8.83%)</td><td>0.03 <b>(+20.51%)</b></td><td>0.03 <b>(+25.68%)</b></td><td>0.02 <b>(+29.58%)</b></td><td>0.00 (-19.96%)</td><td>181.10 <b>(-22.80%)</b></td><td>147.08 (-18.17%)</td><td>139.60 <b>(-20.41%)</b></td><td>132.70 (-8.10%)</td><td>19.47 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.60 (n/a)</td><td>179.74 (n/a)</td><td>175.40 (n/a)</td><td>144.40 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+2.70%)</td><td>0.03 (+1.10%)</td><td>0.02 (-0.84%)</td><td>0.02 <b>(+28.58%)</b></td><td>0.00 <b>(-36.35%)</b></td><td>188.40 <b>(-22.21%)</b></td><td>166.82 (-4.80%)</td><td>173.40 (+0.87%)</td><td>127.70 (-2.59%)</td><td>22.98 <b>(-51.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.20 (n/a)</td><td>175.24 (n/a)</td><td>171.90 (n/a)</td><td>131.10 (n/a)</td><td>47.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 <b>(+24.23%)</b></td><td>0.02 (+15.91%)</td><td>0.03 <b>(+36.64%)</b></td><td>0.02 (+3.38%)</td><td>0.01 <b>(+41.42%)</b></td><td>232.90 (-3.24%)</td><td>174.10 (-12.25%)</td><td>157.10 <b>(-26.79%)</b></td><td>125.90 (-19.50%)</td><td>42.11 (+14.80%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.70 (n/a)</td><td>198.40 (n/a)</td><td>214.60 (n/a)</td><td>156.40 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-9.27%)</td><td>0.02 (-14.21%)</td><td>0.02 (-10.07%)</td><td>0.02 <b>(-24.95%)</b></td><td>0.00 <b>(+22.65%)</b></td><td>237.80 <b>(+33.22%)</b></td><td>186.08 (+18.04%)</td><td>183.70 (+11.20%)</td><td>151.40 (+10.19%)</td><td>32.68 <b>(+85.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.50 (n/a)</td><td>157.64 (n/a)</td><td>165.20 (n/a)</td><td>137.40 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-18.89%)</td><td>0.02 (-9.75%)</td><td>0.02 (+3.39%)</td><td>0.02 (-6.54%)</td><td>0.00 <b>(-39.83%)</b></td><td>213.90 (+7.00%)</td><td>179.60 (+8.14%)</td><td>180.30 (-3.27%)</td><td>146.00 <b>(+23.31%)</b></td><td>29.69 <b>(-21.54%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>166.08 (n/a)</td><td>186.40 (n/a)</td><td>118.40 (n/a)</td><td>37.85 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 <b>(+27.39%)</b></td><td>0.03 (+11.90%)</td><td>0.02 (+5.95%)</td><td>0.02 (-2.53%)</td><td>0.00 <b>(+124.37%)</b></td><td>218.60 (+2.58%)</td><td>167.26 (-8.47%)</td><td>165.30 (-5.60%)</td><td>129.60 <b>(-21.55%)</b></td><td>34.34 <b>(+79.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>182.74 (n/a)</td><td>175.10 (n/a)</td><td>165.20 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 <b>(-24.95%)</b></td><td>0.02 <b>(-28.28%)</b></td><td>0.02 <b>(-34.81%)</b></td><td>0.01 <b>(-25.43%)</b></td><td>0.00 <b>(-30.11%)</b></td><td>288.20 <b>(+34.11%)</b></td><td>246.52 <b>(+38.82%)</b></td><td>262.60 <b>(+53.39%)</b></td><td>186.50 <b>(+33.21%)</b></td><td>39.34 <b>(+20.21%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.90 (n/a)</td><td>177.58 (n/a)</td><td>171.20 (n/a)</td><td>140.00 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 <b>(-24.26%)</b></td><td>0.02 (-10.89%)</td><td>0.02 (-12.84%)</td><td>0.02 (-5.04%)</td><td>0.00 <b>(-42.11%)</b></td><td>218.60 (+5.30%)</td><td>187.78 (+10.34%)</td><td>196.90 (+14.74%)</td><td>158.60 <b>(+32.06%)</b></td><td>26.07 (-17.91%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>170.18 (n/a)</td><td>171.60 (n/a)</td><td>120.10 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-0.99%)</td><td>0.03 (+1.67%)</td><td>0.02 (-7.67%)</td><td>0.02 (-2.61%)</td><td>0.01 (+11.28%)</td><td>223.00 (+2.67%)</td><td>172.20 (-0.52%)</td><td>179.80 (+8.31%)</td><td>121.90 (+0.99%)</td><td>42.70 (+14.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>173.10 (n/a)</td><td>166.00 (n/a)</td><td>120.70 (n/a)</td><td>37.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-7.12%)</td><td>0.02 (+4.49%)</td><td>0.02 (-6.86%)</td><td>0.02 <b>(+27.08%)</b></td><td>0.00 <b>(-76.06%)</b></td><td>198.30 <b>(-21.31%)</b></td><td>184.86 (-7.53%)</td><td>182.20 (+7.37%)</td><td>177.50 (+7.64%)</td><td>8.83 <b>(-79.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.00 (n/a)</td><td>199.92 (n/a)</td><td>169.70 (n/a)</td><td>164.90 (n/a)</td><td>43.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+2.26%)</td><td>0.05 (-1.03%)</td><td>0.05 (+2.44%)</td><td>0.04 (-15.14%)</td><td>0.01 <b>(+31.32%)</b></td><td>227.40 (+17.82%)</td><td>176.86 (+2.41%)</td><td>171.30 (-2.39%)</td><td>135.90 (-2.23%)</td><td>33.09 <b>(+53.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>172.70 (n/a)</td><td>175.50 (n/a)</td><td>139.00 (n/a)</td><td>21.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+15.88%)</td><td>0.05 (+8.71%)</td><td>0.05 (+3.40%)</td><td>0.04 (+4.70%)</td><td>0.01 <b>(+56.96%)</b></td><td>231.10 (-4.46%)</td><td>171.42 (-6.01%)</td><td>168.00 (-3.34%)</td><td>130.10 (-13.73%)</td><td>42.07 <b>(+21.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>182.38 (n/a)</td><td>173.80 (n/a)</td><td>150.80 (n/a)</td><td>34.75 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+1.17%)</td><td>0.05 (+15.21%)</td><td>0.05 (+15.24%)</td><td>0.04 <b>(+34.39%)</b></td><td>0.00 <b>(-69.18%)</b></td><td>187.20 <b>(-25.57%)</b></td><td>176.96 (-14.59%)</td><td>173.70 (-13.24%)</td><td>170.10 (-1.16%)</td><td>7.00 <b>(-77.38%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.50 (n/a)</td><td>207.18 (n/a)</td><td>200.20 (n/a)</td><td>172.10 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 <b>(+28.12%)</b></td><td>0.05 (+15.91%)</td><td>0.04 (+3.62%)</td><td>0.04 <b>(+26.03%)</b></td><td>0.01 <b>(+49.27%)</b></td><td>202.60 <b>(-20.67%)</b></td><td>182.94 (-13.42%)</td><td>196.20 (-3.49%)</td><td>148.60 <b>(-21.91%)</b></td><td>23.00 (-9.66%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>255.40 (n/a)</td><td>211.30 (n/a)</td><td>203.30 (n/a)</td><td>190.30 (n/a)</td><td>25.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+3.54%)</td><td>0.05 (-1.42%)</td><td>0.05 (+5.65%)</td><td>0.04 (-19.52%)</td><td>0.01 <b>(+37.38%)</b></td><td>232.40 <b>(+24.28%)</b></td><td>168.64 (+4.29%)</td><td>155.20 (-5.31%)</td><td>119.90 (-3.38%)</td><td>43.18 <b>(+65.21%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.00 (n/a)</td><td>161.70 (n/a)</td><td>163.90 (n/a)</td><td>124.10 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-13.26%)</td><td>0.05 (-12.33%)</td><td>0.05 (-13.63%)</td><td>0.04 (+0.73%)</td><td>0.01 <b>(-28.84%)</b></td><td>215.60 (-0.74%)</td><td>183.48 (+12.52%)</td><td>180.90 (+15.74%)</td><td>144.40 (+15.24%)</td><td>26.12 <b>(-21.98%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>163.06 (n/a)</td><td>156.30 (n/a)</td><td>125.30 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+1.02%)</td><td>0.05 (+10.67%)</td><td>0.05 (+7.55%)</td><td>0.04 (+11.33%)</td><td>0.01 <b>(-21.64%)</b></td><td>188.40 (-10.16%)</td><td>167.68 (-10.28%)</td><td>174.30 (-6.99%)</td><td>144.80 (-1.03%)</td><td>17.56 <b>(-29.82%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>186.90 (n/a)</td><td>187.40 (n/a)</td><td>146.30 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+14.08%)</td><td>0.05 (-4.36%)</td><td>0.04 (-17.37%)</td><td>0.04 (-3.03%)</td><td>0.01 <b>(+23.65%)</b></td><td>226.60 (+3.14%)</td><td>172.44 (+6.26%)</td><td>183.80 <b>(+21.00%)</b></td><td>111.90 (-12.37%)</td><td>44.40 (+12.72%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>162.28 (n/a)</td><td>151.90 (n/a)</td><td>127.70 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+7.05%)</td><td>0.05 (-1.89%)</td><td>0.05 (-0.00%)</td><td>0.04 (-1.39%)</td><td>0.01 <b>(+38.73%)</b></td><td>187.90 (+1.40%)</td><td>158.66 (+2.83%)</td><td>151.80 (+0.00%)</td><td>127.20 (-6.54%)</td><td>24.63 <b>(+30.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>154.30 (n/a)</td><td>151.80 (n/a)</td><td>136.10 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-8.19%)</td><td>0.05 (-14.12%)</td><td>0.05 (-12.90%)</td><td>0.04 (-18.21%)</td><td>0.01 <b>(+20.00%)</b></td><td>200.00 <b>(+22.32%)</b></td><td>161.06 (+17.37%)</td><td>153.80 (+14.86%)</td><td>136.70 (+8.92%)</td><td>24.21 <b>(+59.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.50 (n/a)</td><td>137.22 (n/a)</td><td>133.90 (n/a)</td><td>125.50 (n/a)</td><td>15.15 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-5.24%)</td><td>0.05 (+6.07%)</td><td>0.05 (+1.99%)</td><td>0.05 <b>(+29.04%)</b></td><td>0.00 <b>(-62.06%)</b></td><td>167.40 <b>(-22.50%)</b></td><td>151.06 (-8.10%)</td><td>149.40 (-1.90%)</td><td>140.10 (+5.58%)</td><td>10.18 <b>(-69.09%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>164.38 (n/a)</td><td>152.30 (n/a)</td><td>132.70 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-16.57%)</td><td>0.05 (+1.83%)</td><td>0.05 (+12.76%)</td><td>0.04 (+6.92%)</td><td>0.00 <b>(-61.09%)</b></td><td>183.00 (-6.44%)</td><td>162.94 (-3.79%)</td><td>159.80 (-11.32%)</td><td>149.00 (+19.87%)</td><td>12.49 <b>(-54.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>169.36 (n/a)</td><td>180.20 (n/a)</td><td>124.30 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-6.99%)</td><td>0.05 (-9.47%)</td><td>0.05 (-8.85%)</td><td>0.04 (-11.52%)</td><td>0.01 (+9.20%)</td><td>225.20 (+13.05%)</td><td>184.34 (+11.07%)</td><td>174.10 (+9.70%)</td><td>152.10 (+7.49%)</td><td>28.43 <b>(+32.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>165.96 (n/a)</td><td>158.70 (n/a)</td><td>141.50 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+16.81%)</td><td>0.04 (-8.35%)</td><td>0.04 (-16.46%)</td><td>0.04 (-18.89%)</td><td>0.01 <b>(+250.52%)</b></td><td>221.50 <b>(+23.26%)</b></td><td>191.58 (+12.87%)</td><td>207.20 (+19.77%)</td><td>132.10 (-14.39%)</td><td>36.85 <b>(+268.69%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.70 (n/a)</td><td>169.74 (n/a)</td><td>173.00 (n/a)</td><td>154.30 (n/a)</td><td>10.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 <b>(-22.45%)</b></td><td>0.04 (-17.92%)</td><td>0.05 (-7.42%)</td><td>0.03 (-14.59%)</td><td>0.01 <b>(-30.27%)</b></td><td>253.00 (+17.08%)</td><td>191.70 <b>(+20.20%)</b></td><td>180.00 (+8.04%)</td><td>145.60 <b>(+28.96%)</b></td><td>45.45 (+8.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>159.48 (n/a)</td><td>166.60 (n/a)</td><td>112.90 (n/a)</td><td>42.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+7.90%)</td><td>0.06 (+14.25%)</td><td>0.06 (+15.44%)</td><td>0.05 <b>(+30.45%)</b></td><td>0.01 <b>(-22.61%)</b></td><td>172.10 <b>(-23.34%)</b></td><td>149.78 (-13.53%)</td><td>141.00 (-13.34%)</td><td>134.60 (-7.30%)</td><td>16.03 <b>(-46.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>173.22 (n/a)</td><td>162.70 (n/a)</td><td>145.20 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (+2.06%)</td><td>0.12 (+16.18%)</td><td>0.11 (+8.27%)</td><td>0.10 <b>(+47.73%)</b></td><td>0.02 <b>(-26.57%)</b></td><td>164.60 <b>(-32.32%)</b></td><td>142.06 (-17.35%)</td><td>154.50 (-7.65%)</td><td>108.60 (-1.99%)</td><td>23.89 <b>(-50.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>243.20 (n/a)</td><td>171.88 (n/a)</td><td>167.30 (n/a)</td><td>110.80 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (+7.04%)</td><td>0.11 (+8.24%)</td><td>0.13 (+14.41%)</td><td>0.07 (-7.83%)</td><td>0.03 <b>(+36.17%)</b></td><td>238.30 (+8.52%)</td><td>160.38 (-5.10%)</td><td>129.80 (-12.65%)</td><td>127.80 (-6.58%)</td><td>48.52 <b>(+33.35%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>169.00 (n/a)</td><td>148.60 (n/a)</td><td>136.80 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 <b>(-24.92%)</b></td><td>0.08 (-2.36%)</td><td>0.08 (+0.13%)</td><td>0.07 <b>(+39.00%)</b></td><td>0.00 <b>(-80.28%)</b></td><td>234.30 <b>(-28.06%)</b></td><td>216.66 (-3.31%)</td><td>217.70 (-0.14%)</td><td>205.30 <b>(+33.23%)</b></td><td>11.78 <b>(-81.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>325.70 (n/a)</td><td>224.08 (n/a)</td><td>218.00 (n/a)</td><td>154.10 (n/a)</td><td>63.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (-15.58%)</td><td>0.07 (-16.27%)</td><td>0.07 (-13.89%)</td><td>0.07 (-15.32%)</td><td>0.01 <b>(-36.20%)</b></td><td>248.40 (+18.12%)</td><td>221.12 (+18.77%)</td><td>221.50 (+16.15%)</td><td>189.90 (+18.39%)</td><td>20.80 (-11.15%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>186.18 (n/a)</td><td>190.70 (n/a)</td><td>160.40 (n/a)</td><td>23.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(-31.71%)</b></td><td>0.09 (-17.46%)</td><td>0.09 (-15.75%)</td><td>0.08 (-7.36%)</td><td>0.01 <b>(-71.37%)</b></td><td>195.50 (+7.89%)</td><td>176.62 (+18.86%)</td><td>173.90 (+18.70%)</td><td>168.50 <b>(+46.39%)</b></td><td>11.05 <b>(-54.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.20 (n/a)</td><td>148.60 (n/a)</td><td>146.50 (n/a)</td><td>115.10 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(-43.73%)</b></td><td>0.08 <b>(-32.36%)</b></td><td>0.08 <b>(-24.08%)</b></td><td>0.07 <b>(-31.63%)</b></td><td>0.01 <b>(-64.53%)</b></td><td>230.60 <b>(+46.23%)</b></td><td>198.94 <b>(+44.98%)</b></td><td>195.90 <b>(+31.74%)</b></td><td>176.20 <b>(+77.80%)</b></td><td>22.27 (-7.94%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>157.70 (n/a)</td><td>137.22 (n/a)</td><td>148.70 (n/a)</td><td>99.10 (n/a)</td><td>24.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(-27.77%)</b></td><td>0.09 (-11.12%)</td><td>0.09 (-5.65%)</td><td>0.07 (+16.97%)</td><td>0.01 <b>(-59.92%)</b></td><td>228.40 (-14.49%)</td><td>183.82 (+5.84%)</td><td>177.90 (+5.96%)</td><td>156.60 <b>(+38.46%)</b></td><td>26.92 <b>(-52.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>267.10 (n/a)</td><td>173.68 (n/a)</td><td>167.90 (n/a)</td><td>113.10 (n/a)</td><td>57.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (-16.07%)</td><td>0.09 <b>(-24.28%)</b></td><td>0.08 <b>(-26.08%)</b></td><td>0.08 <b>(-26.98%)</b></td><td>0.01 (+15.39%)</td><td>211.40 <b>(+36.92%)</b></td><td>184.76 <b>(+33.36%)</b></td><td>195.60 <b>(+35.27%)</b></td><td>145.50 (+19.16%)</td><td>26.45 <b>(+89.25%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>154.40 (n/a)</td><td>138.54 (n/a)</td><td>144.60 (n/a)</td><td>122.10 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (-18.16%)</td><td>0.09 (-9.45%)</td><td>0.09 (-14.93%)</td><td>0.07 <b>(+41.65%)</b></td><td>0.01 <b>(-58.23%)</b></td><td>233.50 <b>(-29.41%)</b></td><td>187.62 (+0.82%)</td><td>187.00 (+17.54%)</td><td>161.10 <b>(+22.23%)</b></td><td>28.01 <b>(-65.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>330.80 (n/a)</td><td>186.10 (n/a)</td><td>159.10 (n/a)</td><td>131.80 (n/a)</td><td>81.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (+6.14%)</td><td>0.09 (-8.06%)</td><td>0.09 (-15.94%)</td><td>0.08 (+4.18%)</td><td>0.01 (+19.16%)</td><td>200.50 (-4.02%)</td><td>184.16 (+9.10%)</td><td>191.30 (+18.97%)</td><td>142.30 (-5.76%)</td><td>23.75 (+2.91%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>168.80 (n/a)</td><td>160.80 (n/a)</td><td>151.00 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (+8.06%)</td><td>0.10 (-5.94%)</td><td>0.09 (-7.24%)</td><td>0.09 (-1.84%)</td><td>0.02 <b>(+20.05%)</b></td><td>192.10 (+1.86%)</td><td>170.78 (+6.95%)</td><td>178.80 (+7.78%)</td><td>124.60 (-7.43%)</td><td>26.44 (+12.04%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>159.68 (n/a)</td><td>165.90 (n/a)</td><td>134.60 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(-29.56%)</b></td><td>0.08 <b>(-26.54%)</b></td><td>0.08 <b>(-22.79%)</b></td><td>0.07 <b>(-28.45%)</b></td><td>0.01 <b>(-40.02%)</b></td><td>231.00 <b>(+39.75%)</b></td><td>199.08 <b>(+35.65%)</b></td><td>197.80 <b>(+29.54%)</b></td><td>171.70 <b>(+42.02%)</b></td><td>21.38 (+19.93%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>165.30 (n/a)</td><td>146.76 (n/a)</td><td>152.70 (n/a)</td><td>120.90 (n/a)</td><td>17.83 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (-12.47%)</td><td>0.08 (-9.96%)</td><td>0.08 (-5.25%)</td><td>0.07 (-13.50%)</td><td>0.01 (-13.30%)</td><td>225.30 (+15.60%)</td><td>201.92 (+11.05%)</td><td>197.40 (+5.56%)</td><td>188.70 (+14.23%)</td><td>13.90 (+16.89%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>181.82 (n/a)</td><td>187.00 (n/a)</td><td>165.20 (n/a)</td><td>11.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 (-14.07%)</td><td>0.08 (-18.80%)</td><td>0.08 <b>(-20.25%)</b></td><td>0.06 (-19.17%)</td><td>0.01 (-5.99%)</td><td>277.70 <b>(+23.70%)</b></td><td>213.48 <b>(+23.84%)</b></td><td>202.70 <b>(+25.43%)</b></td><td>164.70 (+16.40%)</td><td>41.70 <b>(+32.86%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>172.38 (n/a)</td><td>161.60 (n/a)</td><td>141.50 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 <b>(-34.63%)</b></td><td>0.08 <b>(-23.59%)</b></td><td>0.08 (-17.21%)</td><td>0.06 <b>(-22.62%)</b></td><td>0.02 <b>(-42.55%)</b></td><td>277.40 <b>(+29.26%)</b></td><td>204.64 <b>(+28.20%)</b></td><td>199.40 <b>(+20.78%)</b></td><td>154.30 <b>(+52.92%)</b></td><td>49.25 (+15.80%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>159.62 (n/a)</td><td>165.10 (n/a)</td><td>100.90 (n/a)</td><td>42.53 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(-22.62%)</b></td><td>0.08 (-16.31%)</td><td>0.08 (-19.48%)</td><td>0.08 (+15.31%)</td><td>0.01 <b>(-72.30%)</b></td><td>204.70 (-13.26%)</td><td>196.50 (+15.68%)</td><td>201.10 <b>(+24.21%)</b></td><td>176.60 <b>(+29.19%)</b></td><td>11.68 <b>(-70.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>169.86 (n/a)</td><td>161.90 (n/a)</td><td>136.70 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 <b>(-21.54%)</b></td><td>0.18 <b>(-21.95%)</b></td><td>0.18 <b>(-22.51%)</b></td><td>0.12 <b>(-35.88%)</b></td><td>0.05 (+0.79%)</td><td>262.60 <b>(+55.94%)</b></td><td>188.46 <b>(+31.59%)</b></td><td>184.00 <b>(+29.03%)</b></td><td>134.60 <b>(+27.46%)</b></td><td>49.91 <b>(+101.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>168.40 (n/a)</td><td>143.22 (n/a)</td><td>142.60 (n/a)</td><td>105.60 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 <b>(-22.01%)</b></td><td>0.18 (-8.42%)</td><td>0.19 (-5.29%)</td><td>0.14 (-4.04%)</td><td>0.03 <b>(-34.13%)</b></td><td>237.60 (+4.21%)</td><td>185.82 (+7.06%)</td><td>173.60 (+5.60%)</td><td>149.20 <b>(+28.18%)</b></td><td>37.12 (-10.36%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>228.00 (n/a)</td><td>173.56 (n/a)</td><td>164.40 (n/a)</td><td>116.40 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (+11.97%)</td><td>0.15 (+7.49%)</td><td>0.16 (+9.04%)</td><td>0.09 <b>(-21.33%)</b></td><td>0.03 <b>(+103.82%)</b></td><td>345.70 <b>(+27.14%)</b></td><td>228.00 (-3.12%)</td><td>204.50 (-8.30%)</td><td>185.00 (-10.67%)</td><td>66.41 <b>(+140.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>271.90 (n/a)</td><td>235.34 (n/a)</td><td>223.00 (n/a)</td><td>207.10 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 <b>(+27.87%)</b></td><td>0.17 (+3.17%)</td><td>0.16 (-1.86%)</td><td>0.12 (-9.06%)</td><td>0.05 <b>(+90.79%)</b></td><td>267.40 (+9.95%)</td><td>201.60 (+0.76%)</td><td>209.20 (+1.90%)</td><td>126.60 <b>(-21.80%)</b></td><td>50.46 <b>(+57.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>243.20 (n/a)</td><td>200.08 (n/a)</td><td>205.30 (n/a)</td><td>161.90 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 <b>(-21.98%)</b></td><td>0.18 (-16.23%)</td><td>0.17 (-18.15%)</td><td>0.16 (-1.81%)</td><td>0.01 <b>(-59.44%)</b></td><td>201.70 (+1.87%)</td><td>185.74 (+17.56%)</td><td>188.50 <b>(+22.16%)</b></td><td>168.10 <b>(+28.13%)</b></td><td>13.28 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>198.00 (n/a)</td><td>158.00 (n/a)</td><td>154.30 (n/a)</td><td>131.20 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-12.17%)</td><td>0.20 (-4.80%)</td><td>0.20 (-6.83%)</td><td>0.18 (+19.46%)</td><td>0.02 <b>(-54.37%)</b></td><td>182.60 (-16.32%)</td><td>164.56 (+1.37%)</td><td>167.70 (+7.36%)</td><td>142.20 (+13.85%)</td><td>17.58 <b>(-55.31%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.20 (n/a)</td><td>162.34 (n/a)</td><td>156.20 (n/a)</td><td>124.90 (n/a)</td><td>39.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.30 <b>(+22.75%)</b></td><td>0.21 (-1.64%)</td><td>0.22 (-0.52%)</td><td>0.10 <b>(-44.28%)</b></td><td>0.08 <b>(+129.18%)</b></td><td>343.30 <b>(+79.46%)</b></td><td>177.72 (+16.19%)</td><td>146.50 (+0.48%)</td><td>107.50 (-18.50%)</td><td>94.15 <b>(+275.94%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.30 (n/a)</td><td>152.96 (n/a)</td><td>145.80 (n/a)</td><td>131.90 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.29 (-2.97%)</td><td>0.21 (+2.98%)</td><td>0.20 (-2.36%)</td><td>0.15 (+16.63%)</td><td>0.05 <b>(-23.70%)</b></td><td>213.00 (-14.25%)</td><td>163.80 (-7.45%)</td><td>161.70 (+2.41%)</td><td>114.10 (+3.07%)</td><td>39.63 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>248.40 (n/a)</td><td>176.98 (n/a)</td><td>157.90 (n/a)</td><td>110.70 (n/a)</td><td>61.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-9.22%)</td><td>0.20 (+0.75%)</td><td>0.20 (+2.58%)</td><td>0.16 (+13.26%)</td><td>0.02 <b>(-38.84%)</b></td><td>200.50 (-11.71%)</td><td>167.64 (-2.66%)</td><td>167.30 (-2.56%)</td><td>145.00 (+10.18%)</td><td>20.71 <b>(-40.65%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>227.10 (n/a)</td><td>172.22 (n/a)</td><td>171.70 (n/a)</td><td>131.60 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-6.95%)</td><td>0.19 (-4.22%)</td><td>0.19 (-12.81%)</td><td>0.17 (+17.87%)</td><td>0.02 <b>(-47.25%)</b></td><td>189.50 (-15.14%)</td><td>171.30 (+1.52%)</td><td>175.30 (+14.65%)</td><td>143.20 (+7.51%)</td><td>18.13 <b>(-52.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>168.74 (n/a)</td><td>152.90 (n/a)</td><td>133.20 (n/a)</td><td>38.05 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.30 <b>(+24.66%)</b></td><td>0.21 (+8.90%)</td><td>0.20 (+8.49%)</td><td>0.15 (+9.06%)</td><td>0.05 <b>(+26.99%)</b></td><td>214.00 (-8.31%)</td><td>163.42 (-7.60%)</td><td>166.70 (-7.85%)</td><td>110.60 (-19.80%)</td><td>36.82 (-6.48%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>233.40 (n/a)</td><td>176.86 (n/a)</td><td>180.90 (n/a)</td><td>137.90 (n/a)</td><td>39.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (-7.25%)</td><td>0.20 (+0.42%)</td><td>0.21 (+16.52%)</td><td>0.17 (-3.16%)</td><td>0.02 (-12.58%)</td><td>188.90 (+3.28%)</td><td>165.22 (-0.61%)</td><td>153.70 (-14.18%)</td><td>147.40 (+7.83%)</td><td>20.01 (-2.91%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.90 (n/a)</td><td>166.24 (n/a)</td><td>179.10 (n/a)</td><td>136.70 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (+11.72%)</td><td>0.18 (+2.64%)</td><td>0.17 (+7.91%)</td><td>0.13 (-11.45%)</td><td>0.04 <b>(+52.55%)</b></td><td>257.70 (+12.93%)</td><td>195.96 (+0.02%)</td><td>190.10 (-7.31%)</td><td>134.60 (-10.51%)</td><td>45.71 <b>(+56.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>228.20 (n/a)</td><td>195.92 (n/a)</td><td>205.10 (n/a)</td><td>150.40 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 <b>(+20.85%)</b></td><td>0.21 (+9.92%)</td><td>0.20 (+8.63%)</td><td>0.15 (+2.63%)</td><td>0.05 <b>(+44.86%)</b></td><td>213.50 (-2.56%)</td><td>164.58 (-7.10%)</td><td>161.30 (-7.93%)</td><td>115.60 (-17.25%)</td><td>40.74 (+18.52%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.10 (n/a)</td><td>177.16 (n/a)</td><td>175.20 (n/a)</td><td>139.70 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (+5.72%)</td><td>0.17 (-7.62%)</td><td>0.16 (-5.62%)</td><td>0.11 <b>(-28.91%)</b></td><td>0.06 <b>(+88.46%)</b></td><td>310.80 <b>(+40.70%)</b></td><td>219.86 (+18.87%)</td><td>199.80 (+5.94%)</td><td>130.60 (-5.43%)</td><td>82.71 <b>(+172.35%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>220.90 (n/a)</td><td>184.96 (n/a)</td><td>188.60 (n/a)</td><td>138.10 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-9.25%)</td><td>0.20 (+6.48%)</td><td>0.20 (+16.36%)</td><td>0.17 (+5.00%)</td><td>0.03 <b>(-30.53%)</b></td><td>198.30 (-4.76%)</td><td>168.76 (-7.76%)</td><td>166.60 (-14.08%)</td><td>134.80 (+10.22%)</td><td>26.57 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>208.20 (n/a)</td><td>182.96 (n/a)</td><td>193.90 (n/a)</td><td>122.30 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (-0.87%)</td><td>0.21 (-0.24%)</td><td>0.21 (-0.15%)</td><td>0.20 (-0.00%)</td><td>0.00 <b>(-58.66%)</b></td><td>40927.70 (+0.00%)</td><td>40844.62 (+0.24%)</td><td>40876.60 (+0.15%)</td><td>40735.60 (+0.88%)</td><td>88.57 <b>(-58.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>40926.30 (n/a)</td><td>40746.78 (n/a)</td><td>40814.60 (n/a)</td><td>40379.30 (n/a)</td><td>212.12 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (+0.58%)</td><td>0.21 (+0.20%)</td><td>0.21 (+0.15%)</td><td>0.21 (+0.07%)</td><td>0.00 <b>(+218.29%)</b></td><td>40855.20 (-0.07%)</td><td>40769.98 (-0.20%)</td><td>40802.00 (-0.15%)</td><td>40574.50 (-0.57%)</td><td>112.29 <b>(+216.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40884.00 (n/a)</td><td>40851.58 (n/a)</td><td>40864.40 (n/a)</td><td>40807.90 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (+0.02%)</td><td>0.13 (-0.01%)</td><td>0.13 (-0.00%)</td><td>0.13 (-0.05%)</td><td>0.00 <b>(+328.75%)</b></td><td>321919.00 (+0.05%)</td><td>321727.02 (+0.01%)</td><td>321696.20 (+0.00%)</td><td>321590.20 (-0.02%)</td><td>140.93 <b>(+328.53%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321748.80 (n/a)</td><td>321699.70 (n/a)</td><td>321689.00 (n/a)</td><td>321662.60 (n/a)</td><td>32.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-8.13%)</td><td>0.03 (+10.53%)</td><td>0.03 <b>(+24.25%)</b></td><td>0.03 <b>(+20.78%)</b></td><td>0.00 <b>(-43.49%)</b></td><td>159.60 (-17.18%)</td><td>141.30 (-11.48%)</td><td>134.20 (-19.50%)</td><td>128.00 (+8.84%)</td><td>15.40 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>159.62 (n/a)</td><td>166.70 (n/a)</td><td>117.60 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (-4.35%)</td><td>0.04 (-13.38%)</td><td>0.04 (-13.62%)</td><td>0.03 (-18.71%)</td><td>0.01 <b>(+53.54%)</b></td><td>201.90 <b>(+22.96%)</b></td><td>171.94 (+16.79%)</td><td>172.90 (+15.73%)</td><td>135.70 (+4.55%)</td><td>24.59 <b>(+95.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>164.20 (n/a)</td><td>147.22 (n/a)</td><td>149.40 (n/a)</td><td>129.80 (n/a)</td><td>12.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-0.89%)</td><td>0.03 (+2.71%)</td><td>0.03 (-2.52%)</td><td>0.02 <b>(+33.00%)</b></td><td>0.00 <b>(-45.99%)</b></td><td>187.10 <b>(-24.83%)</b></td><td>157.80 (-7.77%)</td><td>158.20 (+2.59%)</td><td>126.10 (+0.88%)</td><td>22.00 <b>(-58.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>171.10 (n/a)</td><td>154.20 (n/a)</td><td>125.00 (n/a)</td><td>53.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (-0.05%)</td><td>0.03 (+1.21%)</td><td>0.03 (+1.55%)</td><td>0.02 (-13.78%)</td><td>0.01 <b>(+22.15%)</b></td><td>261.00 (+16.00%)</td><td>171.64 (+1.53%)</td><td>151.10 (-1.56%)</td><td>129.50 (+0.08%)</td><td>54.91 <b>(+38.41%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>169.06 (n/a)</td><td>153.50 (n/a)</td><td>129.40 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 <b>(+21.03%)</b></td><td>0.03 (+2.56%)</td><td>0.03 (+0.80%)</td><td>0.01 <b>(-40.46%)</b></td><td>0.01 <b>(+67.92%)</b></td><td>338.00 <b>(+67.99%)</b></td><td>181.20 (+10.45%)</td><td>163.20 (-0.79%)</td><td>90.00 (-17.43%)</td><td>92.82 <b>(+137.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>164.06 (n/a)</td><td>164.50 (n/a)</td><td>109.00 (n/a)</td><td>39.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.04 (+8.17%)</td><td>0.03 (-8.55%)</td><td>0.03 (-13.06%)</td><td>0.02 <b>(-30.19%)</b></td><td>0.01 <b>(+120.30%)</b></td><td>275.20 <b>(+43.26%)</b></td><td>192.86 (+15.36%)</td><td>184.10 (+14.99%)</td><td>134.50 (-7.56%)</td><td>55.92 <b>(+188.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>167.18 (n/a)</td><td>160.10 (n/a)</td><td>145.50 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+5.48%)</td><td>0.02 (-11.78%)</td><td>0.02 (-12.72%)</td><td>0.01 <b>(-27.80%)</b></td><td>0.01 <b>(+34.81%)</b></td><td>292.50 <b>(+38.49%)</b></td><td>207.20 (+18.68%)</td><td>218.20 (+14.54%)</td><td>120.40 (-5.20%)</td><td>62.99 <b>(+70.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>174.58 (n/a)</td><td>190.50 (n/a)</td><td>127.00 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-2.32%)</td><td>0.03 (+0.33%)</td><td>0.03 (+0.90%)</td><td>0.02 (+0.60%)</td><td>0.00 (-12.89%)</td><td>204.00 (-0.63%)</td><td>170.88 (-0.77%)</td><td>158.00 (-0.88%)</td><td>149.10 (+2.40%)</td><td>23.67 (-12.59%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>172.20 (n/a)</td><td>159.40 (n/a)</td><td>145.60 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-18.74%)</td><td>0.02 (-3.14%)</td><td>0.02 (-2.94%)</td><td>0.02 <b>(+55.35%)</b></td><td>0.00 <b>(-83.60%)</b></td><td>188.10 <b>(-35.63%)</b></td><td>176.84 (-3.78%)</td><td>177.10 (+3.03%)</td><td>166.40 <b>(+23.08%)</b></td><td>7.79 <b>(-87.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>292.20 (n/a)</td><td>183.78 (n/a)</td><td>171.90 (n/a)</td><td>135.20 (n/a)</td><td>62.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-8.77%)</td><td>0.02 (-13.82%)</td><td>0.03 (-14.20%)</td><td>0.02 <b>(-20.38%)</b></td><td>0.01 <b>(+33.64%)</b></td><td>242.10 <b>(+25.57%)</b></td><td>194.32 (+18.59%)</td><td>183.50 (+16.58%)</td><td>149.00 (+9.64%)</td><td>41.65 <b>(+87.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.80 (n/a)</td><td>163.86 (n/a)</td><td>157.40 (n/a)</td><td>135.90 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 <b>(-20.35%)</b></td><td>0.02 (+3.58%)</td><td>0.02 (+14.44%)</td><td>0.02 <b>(+22.90%)</b></td><td>0.00 <b>(-62.02%)</b></td><td>225.10 (-18.62%)</td><td>194.14 (-7.90%)</td><td>189.60 (-12.63%)</td><td>167.80 <b>(+25.50%)</b></td><td>21.02 <b>(-58.94%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>276.60 (n/a)</td><td>210.80 (n/a)</td><td>217.00 (n/a)</td><td>133.70 (n/a)</td><td>51.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (+13.83%)</td><td>0.03 (+11.63%)</td><td>0.02 (+7.81%)</td><td>0.02 <b>(+22.56%)</b></td><td>0.00 (-5.51%)</td><td>198.30 (-18.40%)</td><td>173.96 (-11.08%)</td><td>179.50 (-7.28%)</td><td>141.70 (-12.15%)</td><td>20.90 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.00 (n/a)</td><td>195.64 (n/a)</td><td>193.60 (n/a)</td><td>161.30 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-17.25%)</td><td>0.02 (-15.31%)</td><td>0.02 (-10.91%)</td><td>0.02 (-14.42%)</td><td>0.00 <b>(-28.68%)</b></td><td>218.60 (+16.84%)</td><td>193.36 (+17.82%)</td><td>185.40 (+12.23%)</td><td>175.70 <b>(+20.84%)</b></td><td>17.34 (+1.98%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.10 (n/a)</td><td>164.12 (n/a)</td><td>165.20 (n/a)</td><td>145.40 (n/a)</td><td>17.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.03 (-4.14%)</td><td>0.02 (+1.79%)</td><td>0.03 (+8.74%)</td><td>0.02 (+6.60%)</td><td>0.01 (-13.53%)</td><td>252.00 (-6.18%)</td><td>187.40 (-3.40%)</td><td>171.60 (-8.09%)</td><td>130.30 (+4.32%)</td><td>47.31 (-14.28%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>194.00 (n/a)</td><td>186.70 (n/a)</td><td>124.90 (n/a)</td><td>55.19 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.02 (-11.01%)</td><td>0.02 (+0.53%)</td><td>0.02 (+1.12%)</td><td>0.02 (+7.40%)</td><td>0.00 <b>(-65.42%)</b></td><td>216.70 (-6.88%)</td><td>208.84 (-1.51%)</td><td>212.00 (-1.12%)</td><td>194.40 (+12.37%)</td><td>8.69 <b>(-63.80%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>212.04 (n/a)</td><td>214.40 (n/a)</td><td>173.00 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 <b>(-22.34%)</b></td><td>0.05 (-12.19%)</td><td>0.05 (-3.64%)</td><td>0.03 <b>(-27.27%)</b></td><td>0.01 <b>(-22.97%)</b></td><td>260.30 <b>(+37.51%)</b></td><td>178.20 (+14.27%)</td><td>164.90 (+3.78%)</td><td>142.90 <b>(+28.85%)</b></td><td>47.02 <b>(+39.73%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>155.94 (n/a)</td><td>158.90 (n/a)</td><td>110.90 (n/a)</td><td>33.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 (+13.33%)</td><td>0.08 (+3.22%)</td><td>0.07 (-4.80%)</td><td>0.06 (+11.71%)</td><td>0.01 <b>(+27.26%)</b></td><td>199.20 (-10.51%)</td><td>167.36 (-2.56%)</td><td>164.40 (+5.05%)</td><td>134.60 (-11.74%)</td><td>30.02 (+1.45%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>171.76 (n/a)</td><td>156.50 (n/a)</td><td>152.50 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+14.32%)</td><td>0.05 (-2.79%)</td><td>0.05 (+0.18%)</td><td>0.03 <b>(-21.96%)</b></td><td>0.01 <b>(+113.37%)</b></td><td>247.70 <b>(+28.14%)</b></td><td>182.04 (+8.31%)</td><td>176.30 (-0.17%)</td><td>126.90 (-12.48%)</td><td>51.37 <b>(+143.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>168.08 (n/a)</td><td>176.60 (n/a)</td><td>145.00 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.08 (+13.22%)</td><td>0.06 (+6.33%)</td><td>0.06 (+4.58%)</td><td>0.03 (+0.54%)</td><td>0.02 (+8.17%)</td><td>293.60 (-0.54%)</td><td>186.28 (-5.40%)</td><td>165.20 (-4.40%)</td><td>132.10 (-11.70%)</td><td>62.30 (+2.51%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.20 (n/a)</td><td>196.92 (n/a)</td><td>172.80 (n/a)</td><td>149.60 (n/a)</td><td>60.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-8.80%)</td><td>0.05 (+5.82%)</td><td>0.05 (-1.19%)</td><td>0.05 <b>(+33.75%)</b></td><td>0.00 <b>(-59.10%)</b></td><td>176.50 <b>(-25.24%)</b></td><td>162.80 (-9.64%)</td><td>169.00 (+1.20%)</td><td>139.80 (+9.65%)</td><td>14.83 <b>(-67.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>180.16 (n/a)</td><td>167.00 (n/a)</td><td>127.50 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (-2.57%)</td><td>0.05 (+0.38%)</td><td>0.05 (-3.96%)</td><td>0.05 <b>(+32.63%)</b></td><td>0.00 <b>(-59.52%)</b></td><td>212.60 <b>(-24.58%)</b></td><td>198.18 (-2.93%)</td><td>193.00 (+4.16%)</td><td>181.90 (+2.65%)</td><td>13.76 <b>(-68.79%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>281.90 (n/a)</td><td>204.16 (n/a)</td><td>185.30 (n/a)</td><td>177.20 (n/a)</td><td>44.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (-0.26%)</td><td>0.05 (+12.75%)</td><td>0.05 (+11.81%)</td><td>0.05 <b>(+30.61%)</b></td><td>0.01 <b>(-21.99%)</b></td><td>181.30 <b>(-23.47%)</b></td><td>157.22 (-13.79%)</td><td>170.80 (-10.58%)</td><td>115.90 (+0.26%)</td><td>28.10 <b>(-37.00%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.90 (n/a)</td><td>182.36 (n/a)</td><td>191.00 (n/a)</td><td>115.60 (n/a)</td><td>44.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+15.86%)</td><td>0.05 (+11.95%)</td><td>0.05 (+10.70%)</td><td>0.04 (+15.03%)</td><td>0.01 <b>(+20.60%)</b></td><td>216.90 (-13.03%)</td><td>181.26 (-10.52%)</td><td>189.00 (-9.70%)</td><td>137.10 (-13.66%)</td><td>29.94 (-10.67%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>202.56 (n/a)</td><td>209.30 (n/a)</td><td>158.80 (n/a)</td><td>33.51 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+11.59%)</td><td>0.04 (+4.64%)</td><td>0.05 (+15.49%)</td><td>0.02 <b>(-32.79%)</b></td><td>0.01 <b>(+77.57%)</b></td><td>375.60 <b>(+48.75%)</b></td><td>207.90 (+4.92%)</td><td>172.00 (-13.44%)</td><td>133.90 (-10.37%)</td><td>95.92 <b>(+159.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>198.16 (n/a)</td><td>198.70 (n/a)</td><td>149.40 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.07 (+19.29%)</td><td>0.05 (+7.93%)</td><td>0.05 (+1.85%)</td><td>0.04 <b>(+37.47%)</b></td><td>0.01 (-6.95%)</td><td>216.40 <b>(-27.26%)</b></td><td>175.20 (-10.14%)</td><td>181.20 (-1.79%)</td><td>124.30 (-16.18%)</td><td>33.43 <b>(-45.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.50 (n/a)</td><td>194.96 (n/a)</td><td>184.50 (n/a)</td><td>148.30 (n/a)</td><td>60.95 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+0.97%)</td><td>0.05 (-3.73%)</td><td>0.04 (-14.49%)</td><td>0.04 (+7.38%)</td><td>0.01 <b>(-21.25%)</b></td><td>209.10 (-6.86%)</td><td>183.22 (+2.06%)</td><td>185.30 (+16.98%)</td><td>138.70 (-1.00%)</td><td>27.78 <b>(-31.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>179.52 (n/a)</td><td>158.40 (n/a)</td><td>140.10 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+17.63%)</td><td>0.05 (+19.99%)</td><td>0.04 (+1.85%)</td><td>0.04 <b>(+68.96%)</b></td><td>0.01 (-11.77%)</td><td>223.40 <b>(-40.82%)</b></td><td>196.94 (-19.58%)</td><td>213.50 (-1.79%)</td><td>162.10 (-15.00%)</td><td>31.31 <b>(-58.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>377.50 (n/a)</td><td>244.88 (n/a)</td><td>217.40 (n/a)</td><td>190.70 (n/a)</td><td>75.35 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.06 (+15.75%)</td><td>0.05 (+8.50%)</td><td>0.05 (+11.31%)</td><td>0.04 (+0.38%)</td><td>0.01 <b>(+50.96%)</b></td><td>216.40 (-0.37%)</td><td>173.98 (-6.51%)</td><td>168.80 (-10.16%)</td><td>132.40 (-13.63%)</td><td>32.87 <b>(+31.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.20 (n/a)</td><td>186.10 (n/a)</td><td>187.90 (n/a)</td><td>153.30 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+14.93%)</td><td>0.04 (-0.28%)</td><td>0.04 (-3.96%)</td><td>0.03 (-18.03%)</td><td>0.01 <b>(+194.22%)</b></td><td>274.30 <b>(+21.97%)</b></td><td>209.34 (+3.25%)</td><td>210.20 (+4.11%)</td><td>163.20 (-13.01%)</td><td>43.49 <b>(+208.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.90 (n/a)</td><td>202.76 (n/a)</td><td>201.90 (n/a)</td><td>187.60 (n/a)</td><td>14.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.05 (+13.87%)</td><td>0.04 (+7.20%)</td><td>0.04 (+7.39%)</td><td>0.03 <b>(-22.87%)</b></td><td>0.01 <b>(+77.14%)</b></td><td>325.40 <b>(+29.64%)</b></td><td>211.88 (-2.26%)</td><td>193.60 (-6.92%)</td><td>151.40 (-12.23%)</td><td>66.97 <b>(+109.16%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.00 (n/a)</td><td>216.78 (n/a)</td><td>208.00 (n/a)</td><td>172.50 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (-2.34%)</td><td>0.10 (+1.95%)</td><td>0.09 (-0.11%)</td><td>0.09 (+4.12%)</td><td>0.01 (-9.73%)</td><td>192.10 (-3.95%)</td><td>167.80 (-2.23%)</td><td>175.00 (+0.11%)</td><td>146.20 (+2.38%)</td><td>20.14 (-12.91%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>171.62 (n/a)</td><td>174.80 (n/a)</td><td>142.80 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 <b>(+21.05%)</b></td><td>0.14 (+6.44%)</td><td>0.14 (+7.30%)</td><td>0.12 (+0.31%)</td><td>0.02 <b>(+119.36%)</b></td><td>203.80 (-0.29%)</td><td>175.88 (-4.67%)</td><td>173.60 (-6.77%)</td><td>136.90 (-17.43%)</td><td>26.45 <b>(+81.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>184.50 (n/a)</td><td>186.20 (n/a)</td><td>165.80 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (-6.25%)</td><td>0.10 (+10.77%)</td><td>0.10 (+13.82%)</td><td>0.09 <b>(+26.26%)</b></td><td>0.02 <b>(-31.35%)</b></td><td>188.90 <b>(-20.80%)</b></td><td>162.32 (-12.42%)</td><td>163.60 (-12.14%)</td><td>130.10 (+6.64%)</td><td>26.78 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>238.50 (n/a)</td><td>185.34 (n/a)</td><td>186.20 (n/a)</td><td>122.00 (n/a)</td><td>44.48 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 <b>(+20.18%)</b></td><td>0.12 (+6.62%)</td><td>0.12 (+7.25%)</td><td>0.10 (+0.10%)</td><td>0.02 <b>(+105.07%)</b></td><td>198.80 (-0.10%)</td><td>172.90 (-4.76%)</td><td>169.00 (-6.73%)</td><td>132.90 (-16.83%)</td><td>27.09 <b>(+72.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>181.54 (n/a)</td><td>181.20 (n/a)</td><td>159.80 (n/a)</td><td>15.73 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (-7.57%)</td><td>0.10 (+5.00%)</td><td>0.10 (+2.24%)</td><td>0.09 (+18.92%)</td><td>0.01 <b>(-43.15%)</b></td><td>180.20 (-15.91%)</td><td>161.80 (-6.97%)</td><td>163.70 (-2.21%)</td><td>135.10 (+8.25%)</td><td>17.67 <b>(-47.98%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.30 (n/a)</td><td>173.92 (n/a)</td><td>167.40 (n/a)</td><td>124.80 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (-14.55%)</td><td>0.10 (-8.50%)</td><td>0.10 (+3.31%)</td><td>0.07 <b>(-25.89%)</b></td><td>0.02 (+14.62%)</td><td>280.10 <b>(+34.92%)</b></td><td>210.74 (+10.64%)</td><td>195.70 (-3.17%)</td><td>184.50 (+16.99%)</td><td>39.48 <b>(+84.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>190.48 (n/a)</td><td>202.10 (n/a)</td><td>157.70 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (-12.23%)</td><td>0.09 (-13.38%)</td><td>0.10 (-12.76%)</td><td>0.07 (-16.96%)</td><td>0.02 (-13.66%)</td><td>227.90 <b>(+20.45%)</b></td><td>182.84 (+15.46%)</td><td>171.80 (+14.61%)</td><td>145.90 (+13.98%)</td><td>31.51 (+16.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>158.36 (n/a)</td><td>149.90 (n/a)</td><td>128.00 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 <b>(+41.44%)</b></td><td>0.13 <b>(+30.85%)</b></td><td>0.14 <b>(+34.10%)</b></td><td>0.10 (+15.26%)</td><td>0.03 <b>(+180.25%)</b></td><td>184.10 (-13.24%)</td><td>143.60 <b>(-21.62%)</b></td><td>132.80 <b>(-25.39%)</b></td><td>117.00 <b>(-29.31%)</b></td><td>29.52 <b>(+67.31%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>183.22 (n/a)</td><td>178.00 (n/a)</td><td>165.50 (n/a)</td><td>17.65 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.10 <b>(-21.57%)</b></td><td>0.08 <b>(-24.43%)</b></td><td>0.08 <b>(-27.65%)</b></td><td>0.06 <b>(-34.67%)</b></td><td>0.02 <b>(+26.55%)</b></td><td>279.20 <b>(+53.07%)</b></td><td>208.16 <b>(+35.61%)</b></td><td>203.50 <b>(+38.25%)</b></td><td>166.20 <b>(+27.55%)</b></td><td>46.40 <b>(+139.37%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>153.50 (n/a)</td><td>147.20 (n/a)</td><td>130.30 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (+1.14%)</td><td>0.11 (+5.14%)</td><td>0.12 (+11.83%)</td><td>0.07 (-16.09%)</td><td>0.02 <b>(+35.24%)</b></td><td>276.30 (+19.15%)</td><td>183.48 (-2.31%)</td><td>156.90 (-10.55%)</td><td>153.50 (-1.10%)</td><td>52.76 <b>(+59.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>231.90 (n/a)</td><td>187.82 (n/a)</td><td>175.40 (n/a)</td><td>155.20 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (-1.31%)</td><td>0.10 (-10.81%)</td><td>0.10 (-10.72%)</td><td>0.09 (-15.52%)</td><td>0.01 <b>(+63.53%)</b></td><td>190.80 (+18.36%)</td><td>168.44 (+13.31%)</td><td>172.30 (+12.03%)</td><td>136.80 (+1.33%)</td><td>22.58 <b>(+99.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>161.20 (n/a)</td><td>148.66 (n/a)</td><td>153.80 (n/a)</td><td>135.00 (n/a)</td><td>11.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (+0.05%)</td><td>0.09 (+1.29%)</td><td>0.09 (-1.76%)</td><td>0.08 (-4.85%)</td><td>0.01 <b>(+36.39%)</b></td><td>220.00 (+5.11%)</td><td>188.78 (-0.38%)</td><td>198.70 (+1.79%)</td><td>156.90 (-0.06%)</td><td>28.10 <b>(+44.15%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>189.50 (n/a)</td><td>195.20 (n/a)</td><td>157.00 (n/a)</td><td>19.49 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (+5.68%)</td><td>0.10 (-7.12%)</td><td>0.10 (-2.09%)</td><td>0.06 <b>(-38.59%)</b></td><td>0.02 <b>(+203.62%)</b></td><td>270.00 <b>(+62.85%)</b></td><td>175.18 (+14.09%)</td><td>157.10 (+2.15%)</td><td>129.00 (-5.36%)</td><td>55.01 <b>(+399.78%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>165.80 (n/a)</td><td>153.54 (n/a)</td><td>153.80 (n/a)</td><td>136.30 (n/a)</td><td>11.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (+1.83%)</td><td>0.10 (+6.71%)</td><td>0.10 (+11.56%)</td><td>0.09 (+7.53%)</td><td>0.01 (-15.78%)</td><td>193.00 (-6.99%)</td><td>173.94 (-6.70%)</td><td>174.50 (-10.37%)</td><td>149.10 (-1.78%)</td><td>17.76 <b>(-22.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>186.44 (n/a)</td><td>194.70 (n/a)</td><td>151.80 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.09 <b>(-24.67%)</b></td><td>0.07 <b>(-23.05%)</b></td><td>0.08 (-13.91%)</td><td>0.05 <b>(-29.32%)</b></td><td>0.02 (+0.04%)</td><td>338.20 <b>(+41.45%)</b></td><td>239.46 <b>(+32.62%)</b></td><td>202.60 (+16.17%)</td><td>192.70 <b>(+32.71%)</b></td><td>62.32 <b>(+78.56%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.10 (n/a)</td><td>180.56 (n/a)</td><td>174.40 (n/a)</td><td>145.20 (n/a)</td><td>34.90 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-6.88%)</td><td>0.19 (-10.73%)</td><td>0.17 (-19.14%)</td><td>0.14 (-9.21%)</td><td>0.04 (+17.58%)</td><td>226.20 (+10.13%)</td><td>179.24 (+13.27%)</td><td>191.10 <b>(+23.69%)</b></td><td>142.20 (+7.40%)</td><td>35.99 <b>(+28.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.40 (n/a)</td><td>158.24 (n/a)</td><td>154.50 (n/a)</td><td>132.40 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (-6.34%)</td><td>0.19 (-14.78%)</td><td>0.18 <b>(-28.04%)</b></td><td>0.15 (+7.41%)</td><td>0.04 <b>(-31.65%)</b></td><td>216.60 (-6.88%)</td><td>180.60 (+13.66%)</td><td>183.70 <b>(+38.96%)</b></td><td>131.70 (+6.73%)</td><td>30.91 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.60 (n/a)</td><td>158.90 (n/a)</td><td>132.20 (n/a)</td><td>123.40 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.31 (-6.56%)</td><td>0.24 (+0.04%)</td><td>0.24 (+6.89%)</td><td>0.17 (-8.63%)</td><td>0.06 (+9.49%)</td><td>240.50 (+9.42%)</td><td>183.10 (+1.74%)</td><td>170.30 (-6.43%)</td><td>133.30 (+7.07%)</td><td>48.30 <b>(+34.02%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>219.80 (n/a)</td><td>179.96 (n/a)</td><td>182.00 (n/a)</td><td>124.50 (n/a)</td><td>36.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-0.07%)</td><td>0.21 (+17.02%)</td><td>0.22 (+10.18%)</td><td>0.17 <b>(+58.73%)</b></td><td>0.03 <b>(-44.97%)</b></td><td>195.90 <b>(-36.99%)</b></td><td>158.58 <b>(-20.99%)</b></td><td>148.60 (-9.22%)</td><td>135.60 (+0.07%)</td><td>25.60 <b>(-65.59%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>310.90 (n/a)</td><td>200.70 (n/a)</td><td>163.70 (n/a)</td><td>135.50 (n/a)</td><td>74.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.35 <b>(+40.59%)</b></td><td>0.26 (+16.61%)</td><td>0.23 (+7.21%)</td><td>0.19 (-5.47%)</td><td>0.07 <b>(+315.22%)</b></td><td>214.50 (+5.82%)</td><td>168.94 (-9.52%)</td><td>174.60 (-6.73%)</td><td>117.90 <b>(-28.89%)</b></td><td>43.88 <b>(+217.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>202.70 (n/a)</td><td>186.72 (n/a)</td><td>187.20 (n/a)</td><td>165.80 (n/a)</td><td>13.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-6.83%)</td><td>0.20 (+3.99%)</td><td>0.19 (+10.22%)</td><td>0.16 (+14.93%)</td><td>0.03 <b>(-31.28%)</b></td><td>205.40 (-13.00%)</td><td>168.92 (-6.27%)</td><td>169.00 (-9.24%)</td><td>137.40 (+7.34%)</td><td>27.52 <b>(-35.42%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.10 (n/a)</td><td>180.22 (n/a)</td><td>186.20 (n/a)</td><td>128.00 (n/a)</td><td>42.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (-9.85%)</td><td>0.22 (-2.74%)</td><td>0.20 (-3.52%)</td><td>0.18 <b>(+22.11%)</b></td><td>0.05 <b>(-31.30%)</b></td><td>199.70 (-18.09%)</td><td>170.48 (-1.00%)</td><td>188.90 (+3.68%)</td><td>132.70 (+10.95%)</td><td>32.96 <b>(-35.36%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>243.80 (n/a)</td><td>172.20 (n/a)</td><td>182.20 (n/a)</td><td>119.60 (n/a)</td><td>50.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (-15.31%)</td><td>0.20 (-4.02%)</td><td>0.20 (-7.45%)</td><td>0.18 (+13.47%)</td><td>0.02 <b>(-58.85%)</b></td><td>185.90 (-11.90%)</td><td>166.32 (+1.51%)</td><td>161.20 (+8.04%)</td><td>149.60 (+18.07%)</td><td>14.11 <b>(-57.52%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.00 (n/a)</td><td>163.84 (n/a)</td><td>149.20 (n/a)</td><td>126.70 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (+11.15%)</td><td>0.22 (+19.03%)</td><td>0.23 <b>(+34.52%)</b></td><td>0.18 (+12.03%)</td><td>0.02 (-2.88%)</td><td>207.50 (-10.75%)</td><td>173.18 (-16.29%)</td><td>163.60 <b>(-25.64%)</b></td><td>153.10 (-10.05%)</td><td>21.47 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>232.50 (n/a)</td><td>206.88 (n/a)</td><td>220.00 (n/a)</td><td>170.20 (n/a)</td><td>27.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 (+3.90%)</td><td>0.18 (-6.66%)</td><td>0.19 (-1.59%)</td><td>0.15 (-18.89%)</td><td>0.03 <b>(+233.47%)</b></td><td>220.70 <b>(+23.30%)</b></td><td>184.58 (+9.01%)</td><td>171.30 (+1.60%)</td><td>155.70 (-3.77%)</td><td>28.81 <b>(+301.50%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>179.00 (n/a)</td><td>169.32 (n/a)</td><td>168.60 (n/a)</td><td>161.80 (n/a)</td><td>7.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (+1.23%)</td><td>0.19 (+1.93%)</td><td>0.18 (-2.58%)</td><td>0.16 (+15.69%)</td><td>0.04 <b>(-22.89%)</b></td><td>218.70 (-13.56%)</td><td>184.86 (-5.16%)</td><td>189.50 (+2.65%)</td><td>131.60 (-1.20%)</td><td>33.94 <b>(-38.26%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>253.00 (n/a)</td><td>194.92 (n/a)</td><td>184.60 (n/a)</td><td>133.20 (n/a)</td><td>54.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 <b>(-26.10%)</b></td><td>0.17 (-1.81%)</td><td>0.17 (+11.20%)</td><td>0.13 (+17.66%)</td><td>0.03 <b>(-58.14%)</b></td><td>259.20 (-15.02%)</td><td>196.38 (-6.32%)</td><td>187.70 (-10.11%)</td><td>162.10 <b>(+35.31%)</b></td><td>36.89 <b>(-49.59%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>305.00 (n/a)</td><td>209.62 (n/a)</td><td>208.80 (n/a)</td><td>119.80 (n/a)</td><td>73.17 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (+2.09%)</td><td>0.19 (+15.16%)</td><td>0.21 (+15.62%)</td><td>0.14 <b>(+38.03%)</b></td><td>0.03 <b>(-28.42%)</b></td><td>247.90 <b>(-27.56%)</b></td><td>184.56 (-17.07%)</td><td>167.90 (-13.54%)</td><td>156.30 (-2.07%)</td><td>37.45 <b>(-49.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>342.20 (n/a)</td><td>222.56 (n/a)</td><td>194.20 (n/a)</td><td>159.60 (n/a)</td><td>73.68 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 (+19.52%)</td><td>0.17 (-6.04%)</td><td>0.16 (-13.96%)</td><td>0.15 (-13.35%)</td><td>0.04 <b>(+221.13%)</b></td><td>218.50 (+15.36%)</td><td>195.42 (+9.80%)</td><td>209.20 (+16.22%)</td><td>132.60 (-16.34%)</td><td>35.41 <b>(+206.16%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>177.98 (n/a)</td><td>180.00 (n/a)</td><td>158.50 (n/a)</td><td>11.57 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 (-1.40%)</td><td>0.13 (-6.47%)</td><td>0.13 (-3.73%)</td><td>0.11 (-14.09%)</td><td>0.02 <b>(+38.02%)</b></td><td>194.30 (+16.42%)</td><td>163.38 (+8.64%)</td><td>162.50 (+3.90%)</td><td>128.00 (+1.43%)</td><td>30.45 <b>(+64.92%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>166.90 (n/a)</td><td>150.38 (n/a)</td><td>156.40 (n/a)</td><td>126.20 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 <b>(-27.37%)</b></td><td>0.10 (-19.70%)</td><td>0.10 <b>(-21.08%)</b></td><td>0.09 (-15.89%)</td><td>0.01 <b>(-54.28%)</b></td><td>225.50 (+18.87%)</td><td>207.16 <b>(+23.02%)</b></td><td>213.40 <b>(+26.72%)</b></td><td>178.60 <b>(+37.70%)</b></td><td>17.90 <b>(-25.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.70 (n/a)</td><td>168.40 (n/a)</td><td>168.40 (n/a)</td><td>129.70 (n/a)</td><td>24.06 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (-19.72%)</td><td>0.11 (-17.01%)</td><td>0.12 (-6.23%)</td><td>0.09 <b>(-27.63%)</b></td><td>0.02 (-1.08%)</td><td>236.80 <b>(+38.16%)</b></td><td>187.54 <b>(+21.94%)</b></td><td>173.20 (+6.65%)</td><td>149.40 <b>(+24.60%)</b></td><td>35.71 <b>(+75.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>171.40 (n/a)</td><td>153.80 (n/a)</td><td>162.40 (n/a)</td><td>119.90 (n/a)</td><td>20.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (-3.02%)</td><td>0.12 (-8.72%)</td><td>0.12 (-9.42%)</td><td>0.10 (-17.32%)</td><td>0.02 <b>(+21.58%)</b></td><td>215.10 <b>(+20.98%)</b></td><td>170.30 (+10.70%)</td><td>169.00 (+10.39%)</td><td>135.90 (+3.11%)</td><td>29.14 <b>(+53.35%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.80 (n/a)</td><td>153.84 (n/a)</td><td>153.10 (n/a)</td><td>131.80 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.13 (-9.67%)</td><td>0.12 (+0.67%)</td><td>0.12 (-0.46%)</td><td>0.11 (+13.38%)</td><td>0.01 <b>(-38.33%)</b></td><td>193.70 (-11.79%)</td><td>171.76 (-1.99%)</td><td>175.90 (+0.46%)</td><td>154.40 (+10.76%)</td><td>17.00 <b>(-41.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>175.24 (n/a)</td><td>175.10 (n/a)</td><td>139.40 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (-4.91%)</td><td>0.12 (-2.25%)</td><td>0.12 (+3.33%)</td><td>0.09 (-6.93%)</td><td>0.02 (-5.14%)</td><td>229.40 (+7.45%)</td><td>177.82 (+2.40%)</td><td>170.90 (-3.23%)</td><td>150.40 (+5.17%)</td><td>31.60 (+9.76%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>213.50 (n/a)</td><td>173.66 (n/a)</td><td>176.60 (n/a)</td><td>143.00 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.16 <b>(+25.95%)</b></td><td>0.12 (+16.70%)</td><td>0.12 <b>(+22.35%)</b></td><td>0.08 (+2.05%)</td><td>0.03 <b>(+72.92%)</b></td><td>251.70 (-2.02%)</td><td>181.28 (-11.56%)</td><td>167.30 (-18.27%)</td><td>126.30 <b>(-20.62%)</b></td><td>48.67 <b>(+36.35%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>256.90 (n/a)</td><td>204.98 (n/a)</td><td>204.70 (n/a)</td><td>159.10 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (+14.49%)</td><td>0.11 (+3.69%)</td><td>0.10 (+0.58%)</td><td>0.09 (+15.87%)</td><td>0.02 (+11.21%)</td><td>220.10 (-13.69%)</td><td>191.72 (-3.65%)</td><td>202.80 (-0.59%)</td><td>138.50 (-12.67%)</td><td>34.54 (-12.99%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>255.00 (n/a)</td><td>198.98 (n/a)</td><td>204.00 (n/a)</td><td>158.60 (n/a)</td><td>39.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (-17.71%)</td><td>0.14 (-13.80%)</td><td>0.15 (-5.94%)</td><td>0.07 <b>(-36.44%)</b></td><td>0.04 (+9.80%)</td><td>328.90 <b>(+57.29%)</b></td><td>195.98 <b>(+22.24%)</b></td><td>166.00 (+6.27%)</td><td>139.50 <b>(+21.52%)</b></td><td>76.36 <b>(+125.14%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>209.10 (n/a)</td><td>160.32 (n/a)</td><td>156.20 (n/a)</td><td>114.80 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (+18.22%)</td><td>0.14 (+12.22%)</td><td>0.14 (-2.31%)</td><td>0.12 <b>(+47.21%)</b></td><td>0.03 (-4.43%)</td><td>213.00 <b>(-32.08%)</b></td><td>175.98 (-13.32%)</td><td>181.60 (+2.37%)</td><td>140.10 (-15.40%)</td><td>32.54 <b>(-47.86%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>313.60 (n/a)</td><td>203.02 (n/a)</td><td>177.40 (n/a)</td><td>165.60 (n/a)</td><td>62.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.18 (-10.81%)</td><td>0.15 (-8.34%)</td><td>0.14 (-0.95%)</td><td>0.11 (-15.37%)</td><td>0.03 (+3.32%)</td><td>215.20 (+18.18%)</td><td>173.48 (+10.01%)</td><td>172.20 (+1.00%)</td><td>139.90 (+12.10%)</td><td>33.21 <b>(+34.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>182.10 (n/a)</td><td>157.70 (n/a)</td><td>170.50 (n/a)</td><td>124.80 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 <b>(-23.73%)</b></td><td>0.14 (-0.39%)</td><td>0.15 (+1.00%)</td><td>0.14 <b>(+33.85%)</b></td><td>0.01 <b>(-81.74%)</b></td><td>177.50 <b>(-25.29%)</b></td><td>169.92 (-4.03%)</td><td>169.20 (-0.99%)</td><td>159.20 <b>(+31.03%)</b></td><td>7.64 <b>(-81.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>237.60 (n/a)</td><td>177.06 (n/a)</td><td>170.90 (n/a)</td><td>121.50 (n/a)</td><td>41.78 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (-2.91%)</td><td>0.14 (+4.40%)</td><td>0.13 (-6.32%)</td><td>0.11 <b>(+50.43%)</b></td><td>0.03 <b>(-22.07%)</b></td><td>229.10 <b>(-33.54%)</b></td><td>184.96 (-9.78%)</td><td>191.60 (+6.74%)</td><td>131.30 (+2.98%)</td><td>41.72 <b>(-49.31%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>344.70 (n/a)</td><td>205.02 (n/a)</td><td>179.50 (n/a)</td><td>127.50 (n/a)</td><td>82.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.17 (-18.03%)</td><td>0.14 (-12.13%)</td><td>0.13 (-13.84%)</td><td>0.12 (+8.93%)</td><td>0.02 <b>(-48.59%)</b></td><td>199.90 (-8.18%)</td><td>175.82 (+10.23%)</td><td>182.60 (+16.01%)</td><td>141.80 <b>(+22.03%)</b></td><td>21.82 <b>(-43.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>217.70 (n/a)</td><td>159.50 (n/a)</td><td>157.40 (n/a)</td><td>116.20 (n/a)</td><td>38.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (+5.60%)</td><td>0.13 (-1.53%)</td><td>0.12 (-1.33%)</td><td>0.11 (+4.55%)</td><td>0.04 (+7.13%)</td><td>230.60 (-4.36%)</td><td>194.50 (+1.76%)</td><td>208.00 (+1.32%)</td><td>128.60 (-5.30%)</td><td>42.21 (-2.04%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>241.10 (n/a)</td><td>191.14 (n/a)</td><td>205.30 (n/a)</td><td>135.80 (n/a)</td><td>43.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 <b>(+41.16%)</b></td><td>0.15 (+4.20%)</td><td>0.15 (+4.98%)</td><td>0.10 <b>(-21.74%)</b></td><td>0.04 <b>(+486.94%)</b></td><td>235.70 <b>(+27.75%)</b></td><td>174.82 (+1.56%)</td><td>163.20 (-4.73%)</td><td>115.90 <b>(-29.20%)</b></td><td>46.06 <b>(+434.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>172.14 (n/a)</td><td>171.30 (n/a)</td><td>163.70 (n/a)</td><td>8.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (+1.47%)</td><td>0.12 (+3.81%)</td><td>0.12 (+8.46%)</td><td>0.11 (-1.85%)</td><td>0.01 (+9.94%)</td><td>174.10 (+1.87%)</td><td>154.48 (-3.56%)</td><td>153.20 (-7.82%)</td><td>136.40 (-1.45%)</td><td>14.60 (+11.49%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>170.90 (n/a)</td><td>160.18 (n/a)</td><td>166.20 (n/a)</td><td>138.40 (n/a)</td><td>13.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 <b>(-30.11%)</b></td><td>0.09 (-19.56%)</td><td>0.08 <b>(-26.83%)</b></td><td>0.07 (+3.65%)</td><td>0.01 <b>(-56.79%)</b></td><td>254.90 (-3.52%)</td><td>211.38 (+17.16%)</td><td>218.30 <b>(+36.69%)</b></td><td>171.70 <b>(+43.08%)</b></td><td>34.00 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>264.20 (n/a)</td><td>180.42 (n/a)</td><td>159.70 (n/a)</td><td>120.00 (n/a)</td><td>58.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (-8.63%)</td><td>0.10 (-17.87%)</td><td>0.10 (-12.59%)</td><td>0.07 <b>(-30.00%)</b></td><td>0.03 <b>(+38.63%)</b></td><td>248.80 <b>(+42.82%)</b></td><td>194.04 <b>(+26.82%)</b></td><td>190.90 (+14.38%)</td><td>131.80 (+9.47%)</td><td>52.14 <b>(+122.71%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>174.20 (n/a)</td><td>153.00 (n/a)</td><td>166.90 (n/a)</td><td>120.40 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (+18.69%)</td><td>0.10 (-4.50%)</td><td>0.09 (-14.96%)</td><td>0.06 <b>(-35.63%)</b></td><td>0.03 <b>(+279.52%)</b></td><td>293.50 <b>(+55.37%)</b></td><td>198.88 (+13.14%)</td><td>210.10 (+17.57%)</td><td>132.30 (-15.73%)</td><td>64.37 <b>(+379.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>175.78 (n/a)</td><td>178.70 (n/a)</td><td>157.00 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.15 (+4.16%)</td><td>0.11 (-15.96%)</td><td>0.10 <b>(-24.08%)</b></td><td>0.08 (-13.39%)</td><td>0.02 <b>(+32.49%)</b></td><td>217.70 (+15.49%)</td><td>180.38 <b>(+20.85%)</b></td><td>181.50 <b>(+31.71%)</b></td><td>126.80 (-4.01%)</td><td>33.83 <b>(+42.12%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>188.50 (n/a)</td><td>149.26 (n/a)</td><td>137.80 (n/a)</td><td>132.10 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.12 (-9.17%)</td><td>0.10 (-12.14%)</td><td>0.10 (-11.25%)</td><td>0.08 (-12.50%)</td><td>0.01 (-6.15%)</td><td>237.40 (+14.30%)</td><td>193.38 (+13.98%)</td><td>188.90 (+12.64%)</td><td>157.20 (+10.08%)</td><td>28.73 (+17.72%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>169.66 (n/a)</td><td>167.70 (n/a)</td><td>142.80 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.11 (-19.64%)</td><td>0.10 (-7.53%)</td><td>0.10 (-1.34%)</td><td>0.09 (+11.59%)</td><td>0.01 <b>(-55.29%)</b></td><td>210.00 (-10.37%)</td><td>188.50 (+5.11%)</td><td>182.30 (+1.33%)</td><td>164.00 <b>(+24.43%)</b></td><td>19.70 <b>(-48.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>179.34 (n/a)</td><td>179.90 (n/a)</td><td>131.80 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (+11.29%)</td><td>0.11 (+8.08%)</td><td>0.10 (-0.51%)</td><td>0.08 <b>(+21.27%)</b></td><td>0.02 (-13.50%)</td><td>226.60 (-17.54%)</td><td>178.26 (-9.49%)</td><td>176.30 (+0.46%)</td><td>135.10 (-10.17%)</td><td>32.57 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>274.80 (n/a)</td><td>196.96 (n/a)</td><td>175.50 (n/a)</td><td>150.40 (n/a)</td><td>51.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.75 <b>(+31.32%)</b></td><td>0.54 (+8.13%)</td><td>0.51 (+4.59%)</td><td>0.45 (+9.14%)</td><td>0.12 <b>(+85.21%)</b></td><td>218.50 (-8.35%)</td><td>188.36 (-5.80%)</td><td>194.40 (-4.38%)</td><td>131.20 <b>(-23.85%)</b></td><td>33.60 <b>(+25.81%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>238.40 (n/a)</td><td>199.96 (n/a)</td><td>203.30 (n/a)</td><td>172.30 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.58 (-1.89%)</td><td>0.56 (+6.79%)</td><td>0.56 (+2.88%)</td><td>0.53 <b>(+24.38%)</b></td><td>0.02 <b>(-74.91%)</b></td><td>184.40 (-19.62%)</td><td>175.44 (-7.64%)</td><td>174.70 (-2.84%)</td><td>169.90 (+1.92%)</td><td>5.47 <b>(-79.33%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.59 (n/a)</td><td>0.53 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>229.40 (n/a)</td><td>189.96 (n/a)</td><td>179.80 (n/a)</td><td>166.70 (n/a)</td><td>26.45 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.65 (-12.08%)</td><td>0.56 (-5.06%)</td><td>0.54 (-5.99%)</td><td>0.52 (+5.40%)</td><td>0.05 <b>(-50.57%)</b></td><td>190.00 (-5.09%)</td><td>176.16 (+3.54%)</td><td>181.60 (+6.32%)</td><td>152.10 (+13.76%)</td><td>14.68 <b>(-48.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.74 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.10 (n/a)</td><td>200.20 (n/a)</td><td>170.14 (n/a)</td><td>170.80 (n/a)</td><td>133.70 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.62 (-0.83%)</td><td>0.51 (+4.43%)</td><td>0.50 (+6.02%)</td><td>0.44 <b>(+23.15%)</b></td><td>0.07 <b>(-37.11%)</b></td><td>224.10 (-18.80%)</td><td>193.48 (-6.66%)</td><td>196.20 (-5.67%)</td><td>159.00 (+0.82%)</td><td>23.43 <b>(-49.05%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>276.00 (n/a)</td><td>207.28 (n/a)</td><td>208.00 (n/a)</td><td>157.70 (n/a)</td><td>45.99 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.45 <b>(-21.78%)</b></td><td>0.38 (+0.50%)</td><td>0.39 (+1.46%)</td><td>0.32 <b>(+71.62%)</b></td><td>0.05 <b>(-62.69%)</b></td><td>227.10 <b>(-41.74%)</b></td><td>195.48 (-11.43%)</td><td>188.70 (-1.41%)</td><td>162.90 <b>(+27.86%)</b></td><td>26.44 <b>(-73.47%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>389.80 (n/a)</td><td>220.70 (n/a)</td><td>191.40 (n/a)</td><td>127.40 (n/a)</td><td>99.66 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.42 <b>(-24.55%)</b></td><td>0.38 (-17.45%)</td><td>0.40 (-19.06%)</td><td>0.31 (-10.24%)</td><td>0.04 <b>(-48.51%)</b></td><td>238.50 (+11.40%)</td><td>197.28 (+18.87%)</td><td>183.50 <b>(+23.57%)</b></td><td>175.80 <b>(+32.48%)</b></td><td>25.57 <b>(-24.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>214.10 (n/a)</td><td>165.96 (n/a)</td><td>148.50 (n/a)</td><td>132.70 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.47 (-15.76%)</td><td>0.39 (-16.23%)</td><td>0.38 (-15.38%)</td><td>0.30 <b>(-24.20%)</b></td><td>0.06 (+0.68%)</td><td>242.90 <b>(+31.94%)</b></td><td>193.74 <b>(+20.37%)</b></td><td>194.60 (+18.15%)</td><td>158.40 (+18.74%)</td><td>33.36 <b>(+56.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>184.10 (n/a)</td><td>160.96 (n/a)</td><td>164.70 (n/a)</td><td>133.40 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.41 (-5.94%)</td><td>0.37 (-3.63%)</td><td>0.36 (-2.03%)</td><td>0.34 (+2.49%)</td><td>0.03 <b>(-29.96%)</b></td><td>219.00 (-2.41%)</td><td>202.76 (+3.16%)</td><td>205.70 (+2.03%)</td><td>178.30 (+6.32%)</td><td>17.63 <b>(-25.95%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>224.40 (n/a)</td><td>196.54 (n/a)</td><td>201.60 (n/a)</td><td>167.70 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (+10.57%)</td><td>0.19 (-4.83%)</td><td>0.19 (-7.38%)</td><td>0.15 (-6.75%)</td><td>0.05 <b>(+56.60%)</b></td><td>247.10 (+7.25%)</td><td>201.66 (+7.66%)</td><td>196.10 (+7.93%)</td><td>138.80 (-9.58%)</td><td>43.67 <b>(+51.76%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>230.40 (n/a)</td><td>187.32 (n/a)</td><td>181.70 (n/a)</td><td>153.50 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (-11.23%)</td><td>0.21 (+3.35%)</td><td>0.21 (+9.42%)</td><td>0.19 <b>(+26.16%)</b></td><td>0.01 <b>(-70.30%)</b></td><td>191.30 <b>(-20.72%)</b></td><td>176.36 (-6.35%)</td><td>178.30 (-8.61%)</td><td>164.50 (+12.67%)</td><td>10.76 <b>(-72.83%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>241.30 (n/a)</td><td>188.32 (n/a)</td><td>195.10 (n/a)</td><td>146.00 (n/a)</td><td>39.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.21 <b>(-29.45%)</b></td><td>0.19 <b>(-23.83%)</b></td><td>0.19 <b>(-26.34%)</b></td><td>0.18 (-14.75%)</td><td>0.01 <b>(-64.92%)</b></td><td>209.10 (+17.34%)</td><td>194.78 <b>(+29.59%)</b></td><td>193.00 <b>(+35.72%)</b></td><td>178.10 <b>(+41.80%)</b></td><td>12.56 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>178.20 (n/a)</td><td>150.30 (n/a)</td><td>142.20 (n/a)</td><td>125.60 (n/a)</td><td>21.67 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (-10.37%)</td><td>0.22 (+5.35%)</td><td>0.20 (+6.93%)</td><td>0.17 (+1.03%)</td><td>0.04 (-17.83%)</td><td>214.80 (-1.01%)</td><td>175.08 (-6.06%)</td><td>188.60 (-6.45%)</td><td>136.80 (+11.58%)</td><td>34.17 (-8.89%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>217.00 (n/a)</td><td>186.38 (n/a)</td><td>201.60 (n/a)</td><td>122.60 (n/a)</td><td>37.50 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 <b>(+54.44%)</b></td><td>0.22 <b>(+27.68%)</b></td><td>0.22 <b>(+30.08%)</b></td><td>0.15 (+0.08%)</td><td>0.05 <b>(+309.25%)</b></td><td>242.80 (-0.08%)</td><td>178.64 (-18.32%)</td><td>169.80 <b>(-23.13%)</b></td><td>130.70 <b>(-35.23%)</b></td><td>43.89 <b>(+167.32%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>243.00 (n/a)</td><td>218.70 (n/a)</td><td>220.90 (n/a)</td><td>201.80 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-0.95%)</td><td>0.20 (+8.89%)</td><td>0.19 (+8.44%)</td><td>0.17 <b>(+23.66%)</b></td><td>0.03 <b>(-29.08%)</b></td><td>213.50 (-19.16%)</td><td>183.66 (-9.94%)</td><td>190.40 (-7.80%)</td><td>158.00 (+0.96%)</td><td>23.80 <b>(-43.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>264.10 (n/a)</td><td>203.92 (n/a)</td><td>206.50 (n/a)</td><td>156.50 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-1.06%)</td><td>0.20 (-3.96%)</td><td>0.21 (+2.73%)</td><td>0.16 (-9.39%)</td><td>0.03 <b>(+48.89%)</b></td><td>228.30 (+10.34%)</td><td>189.36 (+5.49%)</td><td>178.10 (-2.62%)</td><td>160.20 (+1.07%)</td><td>31.83 <b>(+66.61%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>179.50 (n/a)</td><td>182.90 (n/a)</td><td>158.50 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (-10.36%)</td><td>0.21 (-11.23%)</td><td>0.19 <b>(-25.00%)</b></td><td>0.17 (-0.49%)</td><td>0.04 (-5.60%)</td><td>211.60 (+0.47%)</td><td>178.74 (+12.56%)</td><td>198.30 <b>(+33.27%)</b></td><td>138.50 (+11.51%)</td><td>33.71 (+2.64%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>210.60 (n/a)</td><td>158.80 (n/a)</td><td>148.80 (n/a)</td><td>124.20 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (-6.29%)</td><td>0.23 (+10.70%)</td><td>0.24 <b>(+28.64%)</b></td><td>0.18 (+8.54%)</td><td>0.03 <b>(-26.42%)</b></td><td>223.80 (-7.86%)</td><td>184.78 (-11.12%)</td><td>171.40 <b>(-22.27%)</b></td><td>156.30 (+6.69%)</td><td>29.22 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>242.90 (n/a)</td><td>207.90 (n/a)</td><td>220.50 (n/a)</td><td>146.50 (n/a)</td><td>40.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-18.60%)</td><td>0.23 (-6.91%)</td><td>0.22 (-5.12%)</td><td>0.21 (+15.28%)</td><td>0.01 <b>(-68.93%)</b></td><td>192.60 (-13.28%)</td><td>181.52 (+4.91%)</td><td>185.60 (+5.39%)</td><td>168.80 <b>(+22.85%)</b></td><td>10.59 <b>(-67.18%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>222.10 (n/a)</td><td>173.02 (n/a)</td><td>176.10 (n/a)</td><td>137.40 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 <b>(-33.07%)</b></td><td>0.22 (-16.77%)</td><td>0.22 (-18.41%)</td><td>0.21 (+2.36%)</td><td>0.01 <b>(-87.81%)</b></td><td>196.00 (-2.29%)</td><td>186.00 (+15.20%)</td><td>185.10 <b>(+22.58%)</b></td><td>178.30 <b>(+49.46%)</b></td><td>6.37 <b>(-82.96%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>200.60 (n/a)</td><td>161.46 (n/a)</td><td>151.00 (n/a)</td><td>119.30 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 <b>(-26.68%)</b></td><td>0.21 <b>(-28.64%)</b></td><td>0.21 <b>(-30.82%)</b></td><td>0.19 (-14.65%)</td><td>0.02 <b>(-54.76%)</b></td><td>215.40 (+17.13%)</td><td>196.36 <b>(+38.36%)</b></td><td>193.80 <b>(+44.52%)</b></td><td>172.20 <b>(+36.34%)</b></td><td>16.66 <b>(-29.77%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>183.90 (n/a)</td><td>141.92 (n/a)</td><td>134.10 (n/a)</td><td>126.30 (n/a)</td><td>23.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (-11.19%)</td><td>0.22 (+3.47%)</td><td>0.23 (+10.77%)</td><td>0.19 (+9.49%)</td><td>0.02 <b>(-37.35%)</b></td><td>216.50 (-8.65%)</td><td>189.98 (-4.44%)</td><td>180.40 (-9.71%)</td><td>173.20 (+12.61%)</td><td>19.61 <b>(-34.34%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>237.00 (n/a)</td><td>198.80 (n/a)</td><td>199.80 (n/a)</td><td>153.80 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.31 (-2.65%)</td><td>0.25 (+0.01%)</td><td>0.24 (+5.51%)</td><td>0.21 (+2.62%)</td><td>0.04 (-11.03%)</td><td>196.70 (-2.58%)</td><td>169.34 (-0.53%)</td><td>171.30 (-5.25%)</td><td>131.10 (+2.74%)</td><td>26.45 (-9.73%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>201.90 (n/a)</td><td>170.24 (n/a)</td><td>180.80 (n/a)</td><td>127.60 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 <b>(-23.36%)</b></td><td>0.19 <b>(-35.00%)</b></td><td>0.17 <b>(-43.85%)</b></td><td>0.15 <b>(-20.07%)</b></td><td>0.05 <b>(-22.45%)</b></td><td>282.00 <b>(+25.11%)</b></td><td>228.98 <b>(+52.98%)</b></td><td>244.90 <b>(+78.11%)</b></td><td>146.50 <b>(+30.45%)</b></td><td>50.96 (+15.16%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>225.40 (n/a)</td><td>149.68 (n/a)</td><td>137.50 (n/a)</td><td>112.30 (n/a)</td><td>44.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.34 (-5.27%)</td><td>0.23 (-2.97%)</td><td>0.21 (-1.26%)</td><td>0.16 (-13.39%)</td><td>0.07 (-3.67%)</td><td>248.90 (+15.50%)</td><td>184.50 (+3.63%)</td><td>192.60 (+1.26%)</td><td>121.20 (+5.57%)</td><td>47.10 (+17.03%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>215.50 (n/a)</td><td>178.04 (n/a)</td><td>190.20 (n/a)</td><td>114.80 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.20 (-14.64%)</td><td>0.18 (-3.54%)</td><td>0.18 (-1.75%)</td><td>0.14 (+9.14%)</td><td>0.02 <b>(-38.21%)</b></td><td>249.40 (-8.38%)</td><td>201.76 (+1.18%)</td><td>188.30 (+1.78%)</td><td>173.70 (+17.13%)</td><td>30.85 <b>(-34.51%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>272.20 (n/a)</td><td>199.40 (n/a)</td><td>185.00 (n/a)</td><td>148.30 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 (+1.91%)</td><td>0.20 (+0.37%)</td><td>0.18 (+1.83%)</td><td>0.15 (-9.15%)</td><td>0.04 (+11.63%)</td><td>224.90 (+10.03%)</td><td>182.96 (+0.34%)</td><td>190.50 (-1.75%)</td><td>132.80 (-1.85%)</td><td>33.82 (+17.81%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>204.40 (n/a)</td><td>182.34 (n/a)</td><td>193.90 (n/a)</td><td>135.30 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.25 <b>(+42.00%)</b></td><td>0.21 <b>(+31.48%)</b></td><td>0.20 <b>(+34.65%)</b></td><td>0.17 (+16.87%)</td><td>0.03 <b>(+113.57%)</b></td><td>208.50 (-14.44%)</td><td>170.34 <b>(-23.06%)</b></td><td>170.40 <b>(-25.72%)</b></td><td>137.90 <b>(-29.61%)</b></td><td>25.95 <b>(+29.88%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>221.38 (n/a)</td><td>229.40 (n/a)</td><td>195.90 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.26 <b>(+20.64%)</b></td><td>0.20 <b>(+20.06%)</b></td><td>0.19 (+14.61%)</td><td>0.18 <b>(+37.11%)</b></td><td>0.04 (+10.67%)</td><td>197.80 <b>(-27.09%)</b></td><td>174.86 (-17.31%)</td><td>178.70 (-12.74%)</td><td>131.80 (-17.11%)</td><td>26.79 <b>(-33.37%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>271.30 (n/a)</td><td>211.46 (n/a)</td><td>204.80 (n/a)</td><td>159.00 (n/a)</td><td>40.21 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.22 (+5.16%)</td><td>0.20 (+14.73%)</td><td>0.20 (+14.09%)</td><td>0.19 <b>(+33.44%)</b></td><td>0.01 <b>(-54.53%)</b></td><td>183.50 <b>(-25.07%)</b></td><td>174.04 (-13.88%)</td><td>173.50 (-12.33%)</td><td>161.00 (-4.90%)</td><td>8.74 <b>(-68.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>244.90 (n/a)</td><td>202.10 (n/a)</td><td>197.90 (n/a)</td><td>169.30 (n/a)</td><td>27.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.24 (+14.70%)</td><td>0.20 (+11.33%)</td><td>0.20 (+8.37%)</td><td>0.18 (+15.83%)</td><td>0.02 (+1.74%)</td><td>193.50 (-13.65%)</td><td>172.30 (-10.39%)</td><td>173.30 (-7.72%)</td><td>147.20 (-12.80%)</td><td>16.67 <b>(-24.57%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>192.28 (n/a)</td><td>187.80 (n/a)</td><td>168.80 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.23 (-10.73%)</td><td>0.19 (-11.07%)</td><td>0.18 (-14.84%)</td><td>0.16 (+2.71%)</td><td>0.03 <b>(-28.13%)</b></td><td>224.20 (-2.65%)</td><td>190.00 (+10.81%)</td><td>192.80 (+17.42%)</td><td>153.10 (+12.00%)</td><td>28.94 <b>(-22.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>230.30 (n/a)</td><td>171.46 (n/a)</td><td>164.20 (n/a)</td><td>136.70 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.19 (-11.96%)</td><td>0.15 <b>(-25.28%)</b></td><td>0.14 <b>(-32.89%)</b></td><td>0.11 <b>(-36.10%)</b></td><td>0.03 <b>(+66.52%)</b></td><td>319.10 <b>(+56.50%)</b></td><td>240.22 <b>(+38.47%)</b></td><td>245.00 <b>(+49.03%)</b></td><td>179.70 (+13.52%)</td><td>56.13 <b>(+191.22%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>203.90 (n/a)</td><td>173.48 (n/a)</td><td>164.40 (n/a)</td><td>158.30 (n/a)</td><td>19.28 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.88 (-5.03%)</td><td>0.80 (+2.68%)</td><td>0.81 (+7.81%)</td><td>0.73 (+1.66%)</td><td>0.07 <b>(-21.60%)</b></td><td>178.70 (-1.65%)</td><td>163.86 (-2.90%)</td><td>162.50 (-7.25%)</td><td>148.90 (+5.30%)</td><td>13.60 (-18.12%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.72 (n/a)</td><td>0.09 (n/a)</td><td>181.70 (n/a)</td><td>168.76 (n/a)</td><td>175.20 (n/a)</td><td>141.40 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.03 (+4.97%)</td><td>0.83 (+18.10%)</td><td>0.84 <b>(+21.04%)</b></td><td>0.60 (+11.54%)</td><td>0.18 (+0.07%)</td><td>220.10 (-10.35%)</td><td>165.34 (-15.97%)</td><td>156.50 (-17.41%)</td><td>127.10 (-4.72%)</td><td>38.41 (-16.54%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.98 (n/a)</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.53 (n/a)</td><td>0.18 (n/a)</td><td>245.50 (n/a)</td><td>196.76 (n/a)</td><td>189.50 (n/a)</td><td>133.40 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.00 (+1.22%)</td><td>0.83 (+11.45%)</td><td>0.85 (+16.66%)</td><td>0.65 (+19.88%)</td><td>0.13 <b>(-23.75%)</b></td><td>201.00 (-16.60%)</td><td>160.72 (-12.02%)</td><td>153.80 (-14.27%)</td><td>130.70 (-1.21%)</td><td>25.75 <b>(-36.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.99 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.54 (n/a)</td><td>0.17 (n/a)</td><td>241.00 (n/a)</td><td>182.68 (n/a)</td><td>179.40 (n/a)</td><td>132.30 (n/a)</td><td>40.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.00 (+0.00%)</td><td>0.00 (+0.93%)</td><td>0.00 (+2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (-10.56%)</td><td>976.40 (-0.56%)</td><td>946.58 (-0.68%)</td><td>940.94 (-0.22%)</td><td>930.36 (+0.03%)</td><td>17.56 (-19.91%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>981.91 (n/a)</td><td>953.07 (n/a)</td><td>942.97 (n/a)</td><td>930.12 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.01 (-1.22%)</td><td>0.01 (-1.75%)</td><td>0.01 (-2.47%)</td><td>0.01 (+2.67%)</td><td>0.00 <b>(-42.61%)</b></td><td>1064.01 (-2.70%)</td><td>1039.70 (+1.30%)</td><td>1031.92 (+1.92%)</td><td>1011.24 (+0.84%)</td><td>22.13 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1093.54 (n/a)</td><td>1026.35 (n/a)</td><td>1012.48 (n/a)</td><td>1002.84 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.96 (+0.16%)</td><td>0.94 (-0.21%)</td><td>0.94 (+0.38%)</td><td>0.92 (-0.95%)</td><td>0.02 <b>(+47.57%)</b></td><td>2281.14 (+0.96%)</td><td>2234.02 (+0.23%)</td><td>2227.07 (-0.38%)</td><td>2182.25 (-0.16%)</td><td>40.85 <b>(+49.16%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.01 (n/a)</td><td>2259.54 (n/a)</td><td>2228.92 (n/a)</td><td>2235.58 (n/a)</td><td>2185.66 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.71 (+1.51%)</td><td>4.63 (+6.34%)</td><td>4.69 (+9.70%)</td><td>3.16 (-9.24%)</td><td>0.94 (+15.37%)</td><td>331.30 (+10.18%)</td><td>235.62 (-4.72%)</td><td>223.70 (-8.84%)</td><td>183.60 (-1.45%)</td><td>56.56 <b>(+32.02%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.63 (n/a)</td><td>4.35 (n/a)</td><td>4.27 (n/a)</td><td>3.49 (n/a)</td><td>0.81 (n/a)</td><td>300.70 (n/a)</td><td>247.28 (n/a)</td><td>245.40 (n/a)</td><td>186.30 (n/a)</td><td>42.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.14 (-1.28%)</td><td>4.44 (-6.44%)</td><td>4.67 (-3.95%)</td><td>3.66 (-9.52%)</td><td>0.61 <b>(+41.98%)</b></td><td>286.30 (+10.50%)</td><td>240.06 (+7.81%)</td><td>224.40 (+4.08%)</td><td>204.10 (+1.29%)</td><td>34.47 <b>(+57.49%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.20 (n/a)</td><td>4.74 (n/a)</td><td>4.86 (n/a)</td><td>4.05 (n/a)</td><td>0.43 (n/a)</td><td>259.10 (n/a)</td><td>222.66 (n/a)</td><td>215.60 (n/a)</td><td>201.50 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.68 <b>(-21.53%)</b></td><td>4.28 (-12.33%)</td><td>4.22 (-12.97%)</td><td>3.71 (-1.23%)</td><td>0.38 <b>(-62.66%)</b></td><td>282.70 (+1.25%)</td><td>246.58 (+10.80%)</td><td>248.20 (+14.91%)</td><td>224.20 <b>(+27.39%)</b></td><td>22.95 <b>(-51.11%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.96 (n/a)</td><td>4.88 (n/a)</td><td>4.85 (n/a)</td><td>3.76 (n/a)</td><td>1.01 (n/a)</td><td>279.20 (n/a)</td><td>222.54 (n/a)</td><td>216.00 (n/a)</td><td>176.00 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>4.75 <b>(-26.25%)</b></td><td>4.24 (-13.70%)</td><td>4.16 (-13.74%)</td><td>3.75 (-6.47%)</td><td>0.42 <b>(-55.01%)</b></td><td>279.30 (+6.93%)</td><td>249.48 (+13.87%)</td><td>251.90 (+15.92%)</td><td>220.60 <b>(+35.59%)</b></td><td>24.30 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>6.44 (n/a)</td><td>4.91 (n/a)</td><td>4.83 (n/a)</td><td>4.01 (n/a)</td><td>0.92 (n/a)</td><td>261.20 (n/a)</td><td>219.10 (n/a)</td><td>217.30 (n/a)</td><td>162.70 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.17 (-6.79%)</td><td>7.53 (-7.88%)</td><td>7.41 (-8.28%)</td><td>7.05 (-7.42%)</td><td>0.42 (-17.41%)</td><td>297.30 (+7.99%)</td><td>279.26 (+8.48%)</td><td>282.80 (+9.02%)</td><td>256.60 (+7.27%)</td><td>15.30 (-4.62%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.77 (n/a)</td><td>8.17 (n/a)</td><td>8.08 (n/a)</td><td>7.62 (n/a)</td><td>0.51 (n/a)</td><td>275.30 (n/a)</td><td>257.44 (n/a)</td><td>259.40 (n/a)</td><td>239.20 (n/a)</td><td>16.04 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.61 (+2.09%)</td><td>7.39 (-2.79%)</td><td>7.26 (-4.04%)</td><td>6.48 (-6.35%)</td><td>0.77 <b>(+39.54%)</b></td><td>323.80 (+6.76%)</td><td>286.36 (+3.30%)</td><td>288.70 (+4.22%)</td><td>243.50 (-2.05%)</td><td>28.72 <b>(+44.72%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.44 (n/a)</td><td>7.60 (n/a)</td><td>7.57 (n/a)</td><td>6.92 (n/a)</td><td>0.55 (n/a)</td><td>303.30 (n/a)</td><td>277.22 (n/a)</td><td>277.00 (n/a)</td><td>248.60 (n/a)</td><td>19.84 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>8.65 (+1.14%)</td><td>7.69 (+1.88%)</td><td>7.50 (-2.50%)</td><td>6.77 (+9.10%)</td><td>0.86 (+0.78%)</td><td>309.90 (-8.31%)</td><td>275.36 (-1.97%)</td><td>279.50 (+2.53%)</td><td>242.60 (-1.14%)</td><td>30.52 (-11.65%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.55 (n/a)</td><td>7.55 (n/a)</td><td>7.69 (n/a)</td><td>6.20 (n/a)</td><td>0.85 (n/a)</td><td>338.00 (n/a)</td><td>280.88 (n/a)</td><td>272.60 (n/a)</td><td>245.40 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.38 (+3.25%)</td><td>8.44 (-2.83%)</td><td>8.18 (-9.10%)</td><td>7.70 (-3.59%)</td><td>0.69 <b>(+33.45%)</b></td><td>272.30 (+3.69%)</td><td>249.72 (+3.14%)</td><td>256.40 (+10.00%)</td><td>223.50 (-3.12%)</td><td>19.77 <b>(+34.17%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.09 (n/a)</td><td>8.69 (n/a)</td><td>9.00 (n/a)</td><td>7.99 (n/a)</td><td>0.51 (n/a)</td><td>262.60 (n/a)</td><td>242.12 (n/a)</td><td>233.10 (n/a)</td><td>230.70 (n/a)</td><td>14.74 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.60 (-6.02%)</td><td>8.18 (-4.40%)</td><td>8.62 (+5.72%)</td><td>6.04 (-16.33%)</td><td>1.34 (+13.80%)</td><td>347.50 (+19.54%)</td><td>263.06 (+5.69%)</td><td>243.20 (-5.41%)</td><td>218.60 (+6.43%)</td><td>50.18 <b>(+50.39%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>10.21 (n/a)</td><td>8.55 (n/a)</td><td>8.16 (n/a)</td><td>7.21 (n/a)</td><td>1.18 (n/a)</td><td>290.70 (n/a)</td><td>248.90 (n/a)</td><td>257.10 (n/a)</td><td>205.40 (n/a)</td><td>33.37 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.14 (-5.30%)</td><td>8.43 (-1.56%)</td><td>8.55 (+0.05%)</td><td>6.87 (-9.62%)</td><td>0.92 (+14.63%)</td><td>305.20 (+10.66%)</td><td>251.58 (+1.99%)</td><td>245.40 (-0.04%)</td><td>229.50 (+5.61%)</td><td>31.03 <b>(+35.41%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>9.65 (n/a)</td><td>8.56 (n/a)</td><td>8.54 (n/a)</td><td>7.60 (n/a)</td><td>0.80 (n/a)</td><td>275.80 (n/a)</td><td>246.68 (n/a)</td><td>245.50 (n/a)</td><td>217.30 (n/a)</td><td>22.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>12.76 (+3.89%)</td><td>11.63 (-3.12%)</td><td>11.37 (-4.38%)</td><td>10.61 (-9.98%)</td><td>1.01 <b>(+352.54%)</b></td><td>395.30 (+11.10%)</td><td>362.94 (+3.82%)</td><td>368.90 (+4.59%)</td><td>328.60 (-3.75%)</td><td>31.23 <b>(+383.40%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>12.29 (n/a)</td><td>12.00 (n/a)</td><td>11.89 (n/a)</td><td>11.79 (n/a)</td><td>0.22 (n/a)</td><td>355.80 (n/a)</td><td>349.60 (n/a)</td><td>352.70 (n/a)</td><td>341.40 (n/a)</td><td>6.46 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.44 (+3.14%)</td><td>11.61 (+0.87%)</td><td>11.46 (-4.13%)</td><td>9.96 (-1.97%)</td><td>1.26 (+4.60%)</td><td>421.20 (+2.01%)</td><td>364.82 (-0.81%)</td><td>365.80 (+4.31%)</td><td>312.10 (-3.04%)</td><td>39.52 (+1.57%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.03 (n/a)</td><td>11.51 (n/a)</td><td>11.96 (n/a)</td><td>10.16 (n/a)</td><td>1.21 (n/a)</td><td>412.90 (n/a)</td><td>367.80 (n/a)</td><td>350.70 (n/a)</td><td>321.90 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.10 (-3.04%)</td><td>11.94 (-0.97%)</td><td>11.59 (-5.61%)</td><td>11.19 (+8.23%)</td><td>0.85 <b>(-31.10%)</b></td><td>374.90 (-7.59%)</td><td>352.70 (+0.50%)</td><td>362.00 (+5.94%)</td><td>320.20 (+3.12%)</td><td>24.60 <b>(-34.30%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>13.51 (n/a)</td><td>12.06 (n/a)</td><td>12.27 (n/a)</td><td>10.34 (n/a)</td><td>1.24 (n/a)</td><td>405.70 (n/a)</td><td>350.94 (n/a)</td><td>341.70 (n/a)</td><td>310.50 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>15.44 (+3.43%)</td><td>13.97 (+4.47%)</td><td>14.16 (+7.53%)</td><td>11.71 (-0.56%)</td><td>1.39 (+11.61%)</td><td>358.00 (+0.56%)</td><td>302.76 (-4.12%)</td><td>296.20 (-7.00%)</td><td>271.60 (-3.31%)</td><td>32.87 (+11.22%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.93 (n/a)</td><td>13.38 (n/a)</td><td>13.17 (n/a)</td><td>11.78 (n/a)</td><td>1.24 (n/a)</td><td>356.00 (n/a)</td><td>315.76 (n/a)</td><td>318.50 (n/a)</td><td>280.90 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.60 (-2.87%)</td><td>13.01 (-2.67%)</td><td>12.91 (-3.91%)</td><td>12.72 (+2.52%)</td><td>0.34 <b>(-42.75%)</b></td><td>329.70 (-2.46%)</td><td>322.50 (+2.63%)</td><td>324.80 (+4.07%)</td><td>308.30 (+2.94%)</td><td>8.31 <b>(-43.10%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.01 (n/a)</td><td>13.37 (n/a)</td><td>13.44 (n/a)</td><td>12.41 (n/a)</td><td>0.60 (n/a)</td><td>338.00 (n/a)</td><td>314.24 (n/a)</td><td>312.10 (n/a)</td><td>299.50 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>13.65 (-4.14%)</td><td>12.15 (-4.95%)</td><td>12.42 (-6.06%)</td><td>10.44 (-7.79%)</td><td>1.28 (+2.71%)</td><td>401.60 (+8.45%)</td><td>348.54 (+5.36%)</td><td>337.70 (+6.46%)</td><td>307.20 (+4.31%)</td><td>37.84 (+15.31%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>14.24 (n/a)</td><td>12.78 (n/a)</td><td>13.22 (n/a)</td><td>11.33 (n/a)</td><td>1.25 (n/a)</td><td>370.30 (n/a)</td><td>330.80 (n/a)</td><td>317.20 (n/a)</td><td>294.50 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>14.83 (-7.93%)</td><td>13.60 (+4.86%)</td><td>13.05 (+0.42%)</td><td>12.77 <b>(+32.99%)</b></td><td>1.02 <b>(-55.59%)</b></td><td>328.60 <b>(-24.81%)</b></td><td>309.72 (-6.80%)</td><td>321.30 (-0.43%)</td><td>282.80 (+8.64%)</td><td>22.73 <b>(-64.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>16.11 (n/a)</td><td>12.97 (n/a)</td><td>13.00 (n/a)</td><td>9.60 (n/a)</td><td>2.31 (n/a)</td><td>437.00 (n/a)</td><td>332.32 (n/a)</td><td>322.70 (n/a)</td><td>260.30 (n/a)</td><td>64.26 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>14.89 (-2.16%)</td><td>11.98 (-10.56%)</td><td>12.70 (-4.02%)</td><td>9.00 (-17.49%)</td><td>2.39 <b>(+44.59%)</b></td><td>465.90 <b>(+21.17%)</b></td><td>362.22 (+14.13%)</td><td>330.10 (+4.17%)</td><td>281.70 (+2.21%)</td><td>75.94 <b>(+80.24%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>15.22 (n/a)</td><td>13.39 (n/a)</td><td>13.24 (n/a)</td><td>10.91 (n/a)</td><td>1.65 (n/a)</td><td>384.50 (n/a)</td><td>317.38 (n/a)</td><td>316.90 (n/a)</td><td>275.60 (n/a)</td><td>42.13 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.08 (+2.30%)</td><td>2.61 (-1.64%)</td><td>2.54 (-2.53%)</td><td>2.31 (-7.83%)</td><td>0.29 <b>(+40.00%)</b></td><td>227.30 (+8.50%)</td><td>202.98 (+2.13%)</td><td>206.60 (+2.58%)</td><td>170.40 (-2.29%)</td><td>20.80 <b>(+47.63%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.01 (n/a)</td><td>2.65 (n/a)</td><td>2.60 (n/a)</td><td>2.50 (n/a)</td><td>0.20 (n/a)</td><td>209.50 (n/a)</td><td>198.74 (n/a)</td><td>201.40 (n/a)</td><td>174.40 (n/a)</td><td>14.09 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>5.98 (+4.08%)</td><td>4.70 (+0.79%)</td><td>4.46 (+0.35%)</td><td>3.91 (+2.30%)</td><td>0.78 (+1.63%)</td><td>268.40 (-2.26%)</td><td>227.56 (-0.90%)</td><td>235.00 (-0.34%)</td><td>175.30 (-3.95%)</td><td>34.38 (-6.12%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>5.75 (n/a)</td><td>4.66 (n/a)</td><td>4.45 (n/a)</td><td>3.82 (n/a)</td><td>0.77 (n/a)</td><td>274.60 (n/a)</td><td>229.62 (n/a)</td><td>235.80 (n/a)</td><td>182.50 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>9.19 (+4.24%)</td><td>8.00 (-0.71%)</td><td>7.80 (-4.21%)</td><td>6.92 (-5.64%)</td><td>1.10 <b>(+86.12%)</b></td><td>302.80 (+5.95%)</td><td>265.98 (+1.80%)</td><td>269.00 (+4.38%)</td><td>228.10 (-4.08%)</td><td>36.19 <b>(+87.58%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>8.82 (n/a)</td><td>8.06 (n/a)</td><td>8.14 (n/a)</td><td>7.34 (n/a)</td><td>0.59 (n/a)</td><td>285.80 (n/a)</td><td>261.28 (n/a)</td><td>257.70 (n/a)</td><td>237.80 (n/a)</td><td>19.29 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>3.95 (+9.72%)</td><td>3.08 (+5.76%)</td><td>2.85 (-1.75%)</td><td>2.61 (+17.10%)</td><td>0.54 (-4.73%)</td><td>200.90 (-14.62%)</td><td>174.32 (-6.32%)</td><td>184.00 (+1.77%)</td><td>132.80 (-8.85%)</td><td>27.51 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>3.60 (n/a)</td><td>2.91 (n/a)</td><td>2.90 (n/a)</td><td>2.23 (n/a)</td><td>0.57 (n/a)</td><td>235.30 (n/a)</td><td>186.08 (n/a)</td><td>180.80 (n/a)</td><td>145.70 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.28 (+14.08%)</td><td>0.23 (+14.53%)</td><td>0.22 (+14.60%)</td><td>0.20 (+13.18%)</td><td>0.03 (+3.02%)</td><td>164.70 (-11.69%)</td><td>142.76 (-12.99%)</td><td>147.90 (-12.74%)</td><td>116.60 (-12.33%)</td><td>17.98 <b>(-22.07%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>186.50 (n/a)</td><td>164.08 (n/a)</td><td>169.50 (n/a)</td><td>133.00 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.27 (+3.62%)</td><td>0.21 (+4.23%)</td><td>0.21 (+10.91%)</td><td>0.17 (+11.03%)</td><td>0.03 (-14.22%)</td><td>192.00 (-9.94%)</td><td>157.52 (-5.15%)</td><td>153.30 (-9.82%)</td><td>123.10 (-3.53%)</td><td>24.94 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.20 (n/a)</td><td>166.08 (n/a)</td><td>170.00 (n/a)</td><td>127.60 (n/a)</td><td>33.44 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.49 (+9.04%)</td><td>0.39 (+4.26%)</td><td>0.43 (+3.88%)</td><td>0.18 (-18.95%)</td><td>0.12 <b>(+34.51%)</b></td><td>362.10 <b>(+23.42%)</b></td><td>192.78 (+2.46%)</td><td>154.00 (-3.75%)</td><td>132.80 (-8.29%)</td><td>95.39 <b>(+57.56%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>293.40 (n/a)</td><td>188.16 (n/a)</td><td>160.00 (n/a)</td><td>144.80 (n/a)</td><td>60.54 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.51 (-7.76%)</td><td>0.41 (+3.84%)</td><td>0.43 <b>(+25.38%)</b></td><td>0.28 (-4.26%)</td><td>0.08 <b>(-23.88%)</b></td><td>231.20 (+4.47%)</td><td>167.30 (-5.51%)</td><td>152.40 <b>(-20.21%)</b></td><td>127.50 (+8.42%)</td><td>39.34 (-12.03%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>221.30 (n/a)</td><td>177.06 (n/a)</td><td>191.00 (n/a)</td><td>117.60 (n/a)</td><td>44.72 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.51 <b>(+23.76%)</b></td><td>0.41 (+17.65%)</td><td>0.38 (+11.20%)</td><td>0.37 (+15.32%)</td><td>0.06 <b>(+66.45%)</b></td><td>177.50 (-13.29%)</td><td>160.76 (-14.28%)</td><td>174.00 (-10.03%)</td><td>127.40 (-19.21%)</td><td>22.22 (+19.68%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.04 (n/a)</td><td>204.70 (n/a)</td><td>187.54 (n/a)</td><td>193.40 (n/a)</td><td>157.70 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.30 <b>(+21.85%)</b></td><td>0.87 (+6.62%)</td><td>0.78 (+6.75%)</td><td>0.49 <b>(-20.59%)</b></td><td>0.31 <b>(+57.72%)</b></td><td>268.80 <b>(+25.96%)</b></td><td>167.92 (+0.10%)</td><td>167.20 (-6.33%)</td><td>100.80 (-17.98%)</td><td>64.48 <b>(+66.90%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.07 (n/a)</td><td>0.82 (n/a)</td><td>0.73 (n/a)</td><td>0.61 (n/a)</td><td>0.20 (n/a)</td><td>213.40 (n/a)</td><td>167.76 (n/a)</td><td>178.50 (n/a)</td><td>122.90 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.05 (+1.25%)</td><td>0.84 (+1.67%)</td><td>0.82 (+12.93%)</td><td>0.67 (+3.36%)</td><td>0.14 <b>(-23.28%)</b></td><td>195.90 (-3.26%)</td><td>159.24 (-3.17%)</td><td>159.80 (-11.42%)</td><td>124.50 (-1.19%)</td><td>25.90 <b>(-24.75%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>1.04 (n/a)</td><td>0.83 (n/a)</td><td>0.73 (n/a)</td><td>0.65 (n/a)</td><td>0.18 (n/a)</td><td>202.50 (n/a)</td><td>164.46 (n/a)</td><td>180.40 (n/a)</td><td>126.00 (n/a)</td><td>34.41 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.05 (+8.25%)</td><td>0.75 (+5.01%)</td><td>0.78 <b>(+25.30%)</b></td><td>0.48 (-6.52%)</td><td>0.23 (+16.47%)</td><td>273.90 (+6.99%)</td><td>189.28 (-2.77%)</td><td>167.30 <b>(-20.18%)</b></td><td>124.60 (-7.57%)</td><td>59.87 (+19.73%)</td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.97 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.19 (n/a)</td><td>256.00 (n/a)</td><td>194.68 (n/a)</td><td>209.60 (n/a)</td><td>134.80 (n/a)</td><td>50.00 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>1.00 (+2.23%)</td><td>0.76 (-7.80%)</td><td>0.76 (-3.81%)</td><td>0.57 <b>(-22.87%)</b></td><td>0.15 <b>(+66.98%)</b></td><td>229.30 <b>(+29.69%)</b></td><td>177.42 (+10.90%)</td><td>173.00 (+3.97%)</td><td>131.20 (-2.24%)</td><td>34.92 <b>(+114.01%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.98 (n/a)</td><td>0.83 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.09 (n/a)</td><td>176.80 (n/a)</td><td>159.98 (n/a)</td><td>166.40 (n/a)</td><td>134.20 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>dac2841</code> — 2026-07-24 21:23:00</td><td>0.14 (+11.25%)</td><td>0.11 (-2.19%)</td><td>0.10 (-0.86%)</td><td>0.09 (-5.77%)</td><td>0.02 <b>(+46.76%)</b></td><td>191.90 (+6.14%)</td><td>159.76 (+3.94%)</td><td>158.40 (+0.83%)</td><td>117.00 (-10.14%)</td><td>30.74 <b>(+44.28%)</b></td>
</tr>
<tr>
<td><code>2bc7f53</code> — 2026-07-24 15:19:12</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>153.70 (n/a)</td><td>157.10 (n/a)</td><td>130.20 (n/a)</td><td>21.31 (n/a)</td>
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
