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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (+8.91%)</td><td>0.04 (+1.23%)</td><td>0.04 (-5.05%)</td><td>0.03 (-1.95%)</td><td>0.01 (+12.01%)</td><td>208.50 (+2.01%)</td><td>164.92 (-0.88%)</td><td>160.50 (+5.31%)</td><td>133.00 (-8.15%)</td><td>27.54 (+7.24%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>166.38 (n/a)</td><td>152.40 (n/a)</td><td>144.80 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(+62.47%)</b></td><td>0.04 (+9.15%)</td><td>0.03 (-14.51%)</td><td>0.03 (-7.63%)</td><td>0.02 <b>(+351.55%)</b></td><td>198.30 (+8.30%)</td><td>157.46 (-0.57%)</td><td>180.20 (+16.94%)</td><td>87.00 <b>(-38.47%)</b></td><td>44.74 <b>(+189.61%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.10 (n/a)</td><td>158.36 (n/a)</td><td>154.10 (n/a)</td><td>141.40 (n/a)</td><td>15.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (+2.36%)</td><td>0.04 (-8.37%)</td><td>0.03 (-6.95%)</td><td>0.03 (-11.00%)</td><td>0.01 (+11.23%)</td><td>214.70 (+12.35%)</td><td>176.10 (+9.98%)</td><td>184.60 (+7.45%)</td><td>127.80 (-2.29%)</td><td>32.25 <b>(+22.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>160.12 (n/a)</td><td>171.80 (n/a)</td><td>130.80 (n/a)</td><td>26.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-13.18%)</td><td>0.04 (-9.89%)</td><td>0.04 (-10.76%)</td><td>0.03 <b>(-21.12%)</b></td><td>0.01 (+3.74%)</td><td>221.00 <b>(+26.79%)</b></td><td>173.04 (+12.06%)</td><td>174.70 (+12.06%)</td><td>138.50 (+15.22%)</td><td>32.65 <b>(+50.87%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>174.30 (n/a)</td><td>154.42 (n/a)</td><td>155.90 (n/a)</td><td>120.20 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-1.37%)</td><td>0.03 (-2.05%)</td><td>0.04 (-1.60%)</td><td>0.03 (-1.24%)</td><td>0.00 (-0.22%)</td><td>206.70 (+1.27%)</td><td>180.98 (+2.14%)</td><td>172.30 (+1.59%)</td><td>155.60 (+1.43%)</td><td>24.08 (+3.87%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>177.18 (n/a)</td><td>169.60 (n/a)</td><td>153.40 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-0.41%)</td><td>0.03 (-6.11%)</td><td>0.03 (-11.46%)</td><td>0.03 (-0.98%)</td><td>0.01 (+4.85%)</td><td>214.80 (+0.99%)</td><td>185.74 (+6.82%)</td><td>201.80 (+12.93%)</td><td>140.10 (+0.43%)</td><td>31.79 (+8.12%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>173.88 (n/a)</td><td>178.70 (n/a)</td><td>139.50 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-5.47%)</td><td>0.03 (-4.47%)</td><td>0.03 (-8.70%)</td><td>0.03 (+3.00%)</td><td>0.00 <b>(-20.53%)</b></td><td>221.80 (-2.89%)</td><td>193.48 (+3.99%)</td><td>188.10 (+9.55%)</td><td>169.80 (+5.79%)</td><td>24.54 (-17.82%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>186.06 (n/a)</td><td>171.70 (n/a)</td><td>160.50 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-10.73%)</td><td>0.03 (-6.01%)</td><td>0.03 (-0.37%)</td><td>0.03 (-2.42%)</td><td>0.00 <b>(-35.27%)</b></td><td>225.20 (+2.46%)</td><td>200.72 (+5.13%)</td><td>206.40 (+0.34%)</td><td>173.90 (+12.05%)</td><td>23.37 <b>(-25.48%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>190.92 (n/a)</td><td>205.70 (n/a)</td><td>155.20 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(-32.38%)</b></td><td>0.06 <b>(-20.45%)</b></td><td>0.06 (-14.13%)</td><td>0.05 <b>(-23.19%)</b></td><td>0.01 <b>(-40.95%)</b></td><td>238.00 <b>(+30.20%)</b></td><td>206.52 <b>(+24.70%)</b></td><td>204.60 (+16.45%)</td><td>176.10 <b>(+47.86%)</b></td><td>30.67 (+16.32%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>182.80 (n/a)</td><td>165.62 (n/a)</td><td>175.70 (n/a)</td><td>119.10 (n/a)</td><td>26.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (-11.07%)</td><td>0.07 (-14.86%)</td><td>0.07 (-17.86%)</td><td>0.05 <b>(-21.14%)</b></td><td>0.01 (+8.01%)</td><td>227.70 <b>(+26.85%)</b></td><td>184.44 (+18.76%)</td><td>177.60 <b>(+21.73%)</b></td><td>142.50 (+12.47%)</td><td>34.80 <b>(+50.98%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>155.30 (n/a)</td><td>145.90 (n/a)</td><td>126.70 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 <b>(-21.22%)</b></td><td>0.07 (-14.20%)</td><td>0.07 <b>(-23.04%)</b></td><td>0.06 (+4.49%)</td><td>0.01 <b>(-51.98%)</b></td><td>195.40 (-4.26%)</td><td>176.54 (+13.38%)</td><td>186.80 <b>(+29.99%)</b></td><td>151.30 <b>(+26.93%)</b></td><td>20.23 <b>(-42.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>155.70 (n/a)</td><td>143.70 (n/a)</td><td>119.20 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (+1.13%)</td><td>0.07 (+4.29%)</td><td>0.07 (+3.77%)</td><td>0.06 <b>(+31.10%)</b></td><td>0.01 <b>(-31.65%)</b></td><td>215.50 <b>(-23.72%)</b></td><td>181.88 (-7.81%)</td><td>182.10 (-3.65%)</td><td>139.90 (-1.13%)</td><td>29.41 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>282.50 (n/a)</td><td>197.28 (n/a)</td><td>189.00 (n/a)</td><td>141.50 (n/a)</td><td>56.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (-5.39%)</td><td>0.07 (-5.46%)</td><td>0.07 (-7.26%)</td><td>0.07 (+9.10%)</td><td>0.01 (-19.29%)</td><td>183.80 (-8.33%)</td><td>170.54 (+4.77%)</td><td>179.40 (+7.81%)</td><td>130.80 (+5.65%)</td><td>22.32 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>162.78 (n/a)</td><td>166.40 (n/a)</td><td>123.80 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 <b>(-48.65%)</b></td><td>0.06 <b>(-26.78%)</b></td><td>0.07 <b>(-20.02%)</b></td><td>0.05 (-0.60%)</td><td>0.01 <b>(-77.18%)</b></td><td>227.20 (+0.62%)</td><td>195.10 <b>(+24.20%)</b></td><td>188.30 <b>(+25.03%)</b></td><td>163.30 <b>(+94.64%)</b></td><td>24.44 <b>(-53.01%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>225.80 (n/a)</td><td>157.08 (n/a)</td><td>150.60 (n/a)</td><td>83.90 (n/a)</td><td>52.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (-16.16%)</td><td>0.06 (-11.28%)</td><td>0.07 (+4.59%)</td><td>0.04 <b>(-36.63%)</b></td><td>0.01 (+10.27%)</td><td>312.90 <b>(+57.87%)</b></td><td>203.18 (+16.52%)</td><td>180.60 (-4.39%)</td><td>156.90 (+19.22%)</td><td>62.53 <b>(+118.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>174.38 (n/a)</td><td>188.90 (n/a)</td><td>131.60 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-14.30%)</td><td>0.06 (+6.90%)</td><td>0.06 (+9.78%)</td><td>0.06 <b>(+60.88%)</b></td><td>0.00 <b>(-83.54%)</b></td><td>206.50 <b>(-37.82%)</b></td><td>196.82 (-11.94%)</td><td>199.70 (-8.94%)</td><td>188.50 (+16.72%)</td><td>7.79 <b>(-88.30%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>332.10 (n/a)</td><td>223.50 (n/a)</td><td>219.30 (n/a)</td><td>161.50 (n/a)</td><td>66.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.17 (-2.44%)</td><td>0.14 (-5.54%)</td><td>0.14 (-4.44%)</td><td>0.13 (-1.03%)</td><td>0.01 (-17.80%)</td><td>187.80 (+1.02%)</td><td>175.54 (+5.53%)</td><td>180.80 (+4.63%)</td><td>148.60 (+2.55%)</td><td>15.73 (-15.26%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>166.34 (n/a)</td><td>172.80 (n/a)</td><td>144.90 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (-12.25%)</td><td>0.13 (-9.91%)</td><td>0.13 (-9.17%)</td><td>0.12 (-12.81%)</td><td>0.01 (+8.72%)</td><td>210.50 (+14.65%)</td><td>187.48 (+11.26%)</td><td>186.70 (+10.08%)</td><td>170.20 (+13.92%)</td><td>17.52 <b>(+42.17%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>168.50 (n/a)</td><td>169.60 (n/a)</td><td>149.40 (n/a)</td><td>12.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 <b>(-28.40%)</b></td><td>0.12 (-13.99%)</td><td>0.13 (-5.13%)</td><td>0.09 (-14.19%)</td><td>0.02 <b>(-46.24%)</b></td><td>272.20 (+16.52%)</td><td>203.28 (+13.07%)</td><td>196.00 (+5.38%)</td><td>163.00 <b>(+39.67%)</b></td><td>41.21 (-7.39%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>233.60 (n/a)</td><td>179.78 (n/a)</td><td>186.00 (n/a)</td><td>116.70 (n/a)</td><td>44.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-8.33%)</td><td>0.15 (+5.50%)</td><td>0.15 (+9.29%)</td><td>0.14 <b>(+21.98%)</b></td><td>0.01 <b>(-71.81%)</b></td><td>176.40 (-18.03%)</td><td>166.76 (-7.69%)</td><td>168.20 (-8.49%)</td><td>157.80 (+9.05%)</td><td>8.43 <b>(-74.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>215.20 (n/a)</td><td>180.66 (n/a)</td><td>183.80 (n/a)</td><td>144.70 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.17 (-0.01%)</td><td>0.14 (+4.25%)</td><td>0.14 (+13.33%)</td><td>0.13 (+9.42%)</td><td>0.02 <b>(-30.29%)</b></td><td>196.00 (-8.62%)</td><td>174.98 (-5.46%)</td><td>177.50 (-11.78%)</td><td>145.20 (+0.07%)</td><td>20.45 <b>(-36.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.50 (n/a)</td><td>185.08 (n/a)</td><td>201.20 (n/a)</td><td>145.10 (n/a)</td><td>32.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 <b>(-32.67%)</b></td><td>0.11 (-18.96%)</td><td>0.12 (-14.10%)</td><td>0.07 (+8.09%)</td><td>0.02 <b>(-48.87%)</b></td><td>340.00 (-7.48%)</td><td>230.86 (+13.96%)</td><td>201.40 (+16.42%)</td><td>187.10 <b>(+48.49%)</b></td><td>62.68 <b>(-33.65%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>367.50 (n/a)</td><td>202.58 (n/a)</td><td>173.00 (n/a)</td><td>126.00 (n/a)</td><td>94.47 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (-1.06%)</td><td>0.13 (-4.90%)</td><td>0.14 (-3.90%)</td><td>0.10 (-14.64%)</td><td>0.02 <b>(+41.00%)</b></td><td>253.10 (+17.18%)</td><td>188.26 (+6.82%)</td><td>177.50 (+4.11%)</td><td>160.70 (+1.07%)</td><td>38.08 <b>(+65.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.00 (n/a)</td><td>176.24 (n/a)</td><td>170.50 (n/a)</td><td>159.00 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-7.19%)</td><td>0.12 (-8.67%)</td><td>0.12 (-13.52%)</td><td>0.08 (-0.71%)</td><td>0.03 (-18.48%)</td><td>310.50 (+0.71%)</td><td>214.90 (+7.22%)</td><td>199.00 (+15.63%)</td><td>150.00 (+7.76%)</td><td>59.00 (-11.61%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>308.30 (n/a)</td><td>200.42 (n/a)</td><td>172.10 (n/a)</td><td>139.20 (n/a)</td><td>66.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(-24.67%)</b></td><td>0.24 <b>(-28.25%)</b></td><td>0.26 <b>(-22.99%)</b></td><td>0.15 <b>(-51.13%)</b></td><td>0.06 <b>(+93.13%)</b></td><td>338.70 <b>(+104.65%)</b></td><td>215.68 <b>(+47.22%)</b></td><td>188.10 <b>(+29.90%)</b></td><td>172.60 <b>(+32.77%)</b></td><td>69.27 <b>(+447.25%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.03 (n/a)</td><td>165.50 (n/a)</td><td>146.50 (n/a)</td><td>144.80 (n/a)</td><td>130.00 (n/a)</td><td>12.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.34 (-8.77%)</td><td>0.26 <b>(-20.06%)</b></td><td>0.27 <b>(-22.43%)</b></td><td>0.15 <b>(-33.91%)</b></td><td>0.07 (+15.90%)</td><td>319.10 <b>(+51.30%)</b></td><td>201.20 <b>(+30.18%)</b></td><td>181.20 <b>(+28.88%)</b></td><td>143.60 (+9.62%)</td><td>68.11 <b>(+104.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>210.90 (n/a)</td><td>154.56 (n/a)</td><td>140.60 (n/a)</td><td>131.00 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(-21.45%)</b></td><td>0.25 (-7.28%)</td><td>0.26 (-0.66%)</td><td>0.21 (-11.99%)</td><td>0.03 <b>(-41.59%)</b></td><td>238.60 (+13.67%)</td><td>196.64 (+6.68%)</td><td>188.90 (+0.69%)</td><td>175.60 <b>(+27.25%)</b></td><td>25.00 (-13.08%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>209.90 (n/a)</td><td>184.32 (n/a)</td><td>187.60 (n/a)</td><td>138.00 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (-11.21%)</td><td>0.27 (-8.00%)</td><td>0.27 (-11.23%)</td><td>0.23 (-3.59%)</td><td>0.02 <b>(-29.85%)</b></td><td>218.00 (+3.76%)</td><td>184.54 (+8.11%)</td><td>179.70 (+12.66%)</td><td>170.80 (+12.66%)</td><td>19.20 (-18.10%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>210.10 (n/a)</td><td>170.70 (n/a)</td><td>159.50 (n/a)</td><td>151.60 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (+2.25%)</td><td>0.26 (-6.63%)</td><td>0.26 (-8.16%)</td><td>0.19 (-16.21%)</td><td>0.05 <b>(+39.05%)</b></td><td>263.90 (+19.36%)</td><td>196.02 (+8.92%)</td><td>186.70 (+8.93%)</td><td>154.70 (-2.15%)</td><td>40.48 <b>(+65.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>221.10 (n/a)</td><td>179.96 (n/a)</td><td>171.40 (n/a)</td><td>158.10 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 (-6.98%)</td><td>0.27 (-1.33%)</td><td>0.28 (+5.92%)</td><td>0.25 (-0.86%)</td><td>0.02 (-12.19%)</td><td>197.80 (+0.87%)</td><td>180.78 (+1.25%)</td><td>172.60 (-5.63%)</td><td>165.80 (+7.52%)</td><td>15.42 (-2.28%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>178.54 (n/a)</td><td>182.90 (n/a)</td><td>154.20 (n/a)</td><td>15.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (-5.97%)</td><td>0.26 (-2.68%)</td><td>0.30 (+9.80%)</td><td>0.17 (-17.72%)</td><td>0.06 (+4.69%)</td><td>284.60 <b>(+21.52%)</b></td><td>196.20 (+4.20%)</td><td>163.70 (-8.90%)</td><td>157.50 (+6.35%)</td><td>54.01 <b>(+33.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>234.20 (n/a)</td><td>188.30 (n/a)</td><td>179.70 (n/a)</td><td>148.10 (n/a)</td><td>40.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (+5.77%)</td><td>0.25 (+5.95%)</td><td>0.25 (+14.15%)</td><td>0.16 <b>(-22.12%)</b></td><td>0.06 <b>(+65.35%)</b></td><td>311.40 <b>(+28.41%)</b></td><td>206.32 (-1.62%)</td><td>194.70 (-12.38%)</td><td>157.10 (-5.48%)</td><td>62.38 <b>(+104.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>242.50 (n/a)</td><td>209.72 (n/a)</td><td>222.20 (n/a)</td><td>166.20 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-5.49%)</td><td>0.02 (-2.40%)</td><td>0.02 (+11.97%)</td><td>0.01 (-8.45%)</td><td>0.00 <b>(+23.73%)</b></td><td>180.50 (+9.20%)</td><td>149.74 (+3.74%)</td><td>133.30 (-10.72%)</td><td>122.70 (+5.78%)</td><td>28.20 <b>(+50.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.30 (n/a)</td><td>144.34 (n/a)</td><td>149.30 (n/a)</td><td>116.00 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-5.70%)</td><td>0.02 (-7.37%)</td><td>0.02 (-6.42%)</td><td>0.01 (-2.31%)</td><td>0.00 (-12.98%)</td><td>210.90 (+2.38%)</td><td>173.56 (+7.53%)</td><td>164.90 (+6.87%)</td><td>142.30 (+6.04%)</td><td>29.40 (-2.92%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.00 (n/a)</td><td>161.40 (n/a)</td><td>154.30 (n/a)</td><td>134.20 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-7.39%)</td><td>0.02 (-1.83%)</td><td>0.02 (+10.46%)</td><td>0.01 (-3.67%)</td><td>0.00 (-8.34%)</td><td>194.80 (+3.78%)</td><td>156.92 (+1.74%)</td><td>140.30 (-9.48%)</td><td>120.30 (+7.99%)</td><td>33.32 (+5.59%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>187.70 (n/a)</td><td>154.24 (n/a)</td><td>155.00 (n/a)</td><td>111.40 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-12.13%)</td><td>0.02 (-5.83%)</td><td>0.02 (-2.43%)</td><td>0.01 (-7.49%)</td><td>0.00 <b>(-22.42%)</b></td><td>214.60 (+8.11%)</td><td>173.82 (+5.35%)</td><td>161.40 (+2.54%)</td><td>139.00 (+13.84%)</td><td>29.80 (-5.53%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.50 (n/a)</td><td>165.00 (n/a)</td><td>157.40 (n/a)</td><td>122.10 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (+13.41%)</td><td>0.02 (+0.46%)</td><td>0.02 (-7.98%)</td><td>0.01 (-9.40%)</td><td>0.00 <b>(+93.95%)</b></td><td>200.90 (+10.38%)</td><td>163.88 (+1.26%)</td><td>170.90 (+8.72%)</td><td>127.10 (-11.80%)</td><td>27.68 <b>(+85.46%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>182.00 (n/a)</td><td>161.84 (n/a)</td><td>157.20 (n/a)</td><td>144.10 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (+9.57%)</td><td>0.01 (-3.08%)</td><td>0.01 (-10.15%)</td><td>0.01 (-16.17%)</td><td>0.00 <b>(+82.06%)</b></td><td>242.10 (+19.26%)</td><td>189.44 (+5.83%)</td><td>192.00 (+11.30%)</td><td>145.20 (-8.74%)</td><td>39.91 <b>(+93.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>203.00 (n/a)</td><td>179.00 (n/a)</td><td>172.50 (n/a)</td><td>159.10 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-8.72%)</td><td>0.01 (-1.84%)</td><td>0.02 (-3.03%)</td><td>0.01 (-0.94%)</td><td>0.00 <b>(-29.23%)</b></td><td>210.40 (+0.96%)</td><td>176.78 (+1.16%)</td><td>170.20 (+3.15%)</td><td>158.10 (+9.56%)</td><td>19.93 <b>(-20.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>208.40 (n/a)</td><td>174.76 (n/a)</td><td>165.00 (n/a)</td><td>144.30 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.01 (+3.29%)</td><td>0.01 <b>(+23.04%)</b></td><td>0.01 <b>(+21.01%)</b></td><td>0.01 <b>(+62.19%)</b></td><td>0.00 <b>(-70.87%)</b></td><td>227.20 <b>(-38.33%)</b></td><td>207.34 <b>(-22.96%)</b></td><td>206.10 (-17.36%)</td><td>191.20 (-3.19%)</td><td>12.86 <b>(-82.38%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>368.40 (n/a)</td><td>269.14 (n/a)</td><td>249.40 (n/a)</td><td>197.50 (n/a)</td><td>72.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (+3.43%)</td><td>0.03 (-0.62%)</td><td>0.03 (-1.75%)</td><td>0.02 (-13.70%)</td><td>0.01 <b>(+38.31%)</b></td><td>224.90 (+15.87%)</td><td>164.40 (+2.93%)</td><td>154.90 (+1.77%)</td><td>126.50 (-3.29%)</td><td>40.00 <b>(+52.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>159.72 (n/a)</td><td>152.20 (n/a)</td><td>130.80 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (+0.36%)</td><td>0.03 (+2.52%)</td><td>0.03 (-7.37%)</td><td>0.03 <b>(+21.62%)</b></td><td>0.00 <b>(-37.23%)</b></td><td>195.20 (-17.78%)</td><td>162.12 (-5.97%)</td><td>159.40 (+7.92%)</td><td>129.40 (-0.38%)</td><td>23.54 <b>(-49.40%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>172.42 (n/a)</td><td>147.70 (n/a)</td><td>129.90 (n/a)</td><td>46.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 <b>(-30.84%)</b></td><td>0.02 <b>(-26.88%)</b></td><td>0.03 <b>(-24.87%)</b></td><td>0.01 <b>(-37.17%)</b></td><td>0.01 <b>(-20.89%)</b></td><td>364.00 <b>(+59.16%)</b></td><td>226.68 <b>(+39.70%)</b></td><td>197.10 <b>(+33.09%)</b></td><td>183.10 <b>(+44.51%)</b></td><td>77.02 <b>(+87.40%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>162.26 (n/a)</td><td>148.10 (n/a)</td><td>126.70 (n/a)</td><td>41.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-0.16%)</td><td>0.03 (-9.84%)</td><td>0.03 (-17.35%)</td><td>0.02 (+3.80%)</td><td>0.00 (-17.27%)</td><td>213.40 (-3.66%)</td><td>192.76 (+10.26%)</td><td>197.20 <b>(+20.98%)</b></td><td>158.00 (+0.19%)</td><td>20.63 <b>(-23.17%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>174.82 (n/a)</td><td>163.00 (n/a)</td><td>157.70 (n/a)</td><td>26.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-15.22%)</td><td>0.03 (-13.66%)</td><td>0.03 (-15.03%)</td><td>0.02 (-1.29%)</td><td>0.00 <b>(-39.20%)</b></td><td>231.80 (+1.31%)</td><td>191.32 (+13.76%)</td><td>192.40 (+17.68%)</td><td>162.80 (+17.89%)</td><td>26.30 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>168.18 (n/a)</td><td>163.50 (n/a)</td><td>138.10 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-16.99%)</td><td>0.02 (-18.01%)</td><td>0.02 (-17.60%)</td><td>0.02 <b>(-20.10%)</b></td><td>0.00 <b>(-25.25%)</b></td><td>240.80 <b>(+25.16%)</b></td><td>214.80 <b>(+21.85%)</b></td><td>211.30 <b>(+21.37%)</b></td><td>194.30 <b>(+20.46%)</b></td><td>16.87 (+13.25%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.40 (n/a)</td><td>176.28 (n/a)</td><td>174.10 (n/a)</td><td>161.30 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-4.08%)</td><td>0.03 (-4.15%)</td><td>0.03 (-3.99%)</td><td>0.02 (-16.14%)</td><td>0.01 (+14.52%)</td><td>248.00 (+19.23%)</td><td>186.32 (+5.72%)</td><td>173.30 (+4.15%)</td><td>144.50 (+4.26%)</td><td>40.86 <b>(+40.35%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>176.24 (n/a)</td><td>166.40 (n/a)</td><td>138.60 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-18.64%)</td><td>0.03 (-7.12%)</td><td>0.03 (-12.52%)</td><td>0.02 <b>(+24.76%)</b></td><td>0.00 <b>(-73.79%)</b></td><td>221.00 (-19.84%)</td><td>207.56 (+3.40%)</td><td>208.20 (+14.33%)</td><td>188.10 <b>(+22.86%)</b></td><td>12.42 <b>(-74.65%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.70 (n/a)</td><td>200.74 (n/a)</td><td>182.10 (n/a)</td><td>153.10 (n/a)</td><td>49.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-3.23%)</td><td>0.06 (-14.73%)</td><td>0.06 (-19.20%)</td><td>0.05 (-9.74%)</td><td>0.01 <b>(+23.70%)</b></td><td>194.10 (+10.79%)</td><td>177.18 (+17.99%)</td><td>184.70 <b>(+23.79%)</b></td><td>140.10 (+3.39%)</td><td>21.96 <b>(+39.42%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>175.20 (n/a)</td><td>150.16 (n/a)</td><td>149.20 (n/a)</td><td>135.50 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(-20.93%)</b></td><td>0.06 (-18.71%)</td><td>0.06 (-16.72%)</td><td>0.05 <b>(-25.95%)</b></td><td>0.01 (+2.71%)</td><td>226.40 <b>(+35.08%)</b></td><td>187.52 <b>(+23.63%)</b></td><td>178.10 <b>(+20.01%)</b></td><td>170.20 <b>(+26.54%)</b></td><td>22.82 <b>(+77.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>167.60 (n/a)</td><td>151.68 (n/a)</td><td>148.40 (n/a)</td><td>134.50 (n/a)</td><td>12.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-18.33%)</td><td>0.06 (-17.44%)</td><td>0.06 (-18.93%)</td><td>0.06 (-9.94%)</td><td>0.00 <b>(-46.94%)</b></td><td>189.20 (+11.03%)</td><td>175.42 <b>(+20.53%)</b></td><td>174.20 <b>(+23.37%)</b></td><td>160.10 <b>(+22.40%)</b></td><td>10.53 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>170.40 (n/a)</td><td>145.54 (n/a)</td><td>141.20 (n/a)</td><td>130.80 (n/a)</td><td>14.94 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (+5.61%)</td><td>0.07 (-9.26%)</td><td>0.07 (-9.36%)</td><td>0.05 <b>(-36.19%)</b></td><td>0.02 <b>(+232.47%)</b></td><td>230.60 <b>(+56.76%)</b></td><td>162.30 (+16.90%)</td><td>158.60 (+10.29%)</td><td>119.00 (-5.33%)</td><td>46.76 <b>(+369.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>147.10 (n/a)</td><td>138.84 (n/a)</td><td>143.80 (n/a)</td><td>125.70 (n/a)</td><td>9.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 <b>(-24.43%)</b></td><td>0.06 <b>(-26.10%)</b></td><td>0.06 <b>(-28.41%)</b></td><td>0.05 <b>(-22.09%)</b></td><td>0.02 <b>(-22.07%)</b></td><td>206.90 <b>(+28.35%)</b></td><td>177.16 <b>(+35.61%)</b></td><td>183.80 <b>(+39.67%)</b></td><td>118.30 <b>(+32.33%)</b></td><td>35.26 <b>(+34.64%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>161.20 (n/a)</td><td>130.64 (n/a)</td><td>131.60 (n/a)</td><td>89.40 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(-32.07%)</b></td><td>0.06 <b>(-22.77%)</b></td><td>0.06 <b>(-25.06%)</b></td><td>0.05 (-5.95%)</td><td>0.01 <b>(-63.40%)</b></td><td>219.50 (+6.35%)</td><td>191.36 <b>(+26.11%)</b></td><td>188.80 <b>(+33.43%)</b></td><td>174.10 <b>(+47.17%)</b></td><td>18.24 <b>(-44.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>151.74 (n/a)</td><td>141.50 (n/a)</td><td>118.30 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-16.57%)</td><td>0.05 (-18.91%)</td><td>0.05 <b>(-23.96%)</b></td><td>0.04 (-9.26%)</td><td>0.01 <b>(-39.61%)</b></td><td>249.00 (+10.18%)</td><td>201.84 <b>(+21.18%)</b></td><td>199.60 <b>(+31.49%)</b></td><td>165.80 (+19.88%)</td><td>30.25 (-18.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>166.56 (n/a)</td><td>151.80 (n/a)</td><td>138.30 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 <b>(-25.98%)</b></td><td>0.04 <b>(-21.26%)</b></td><td>0.05 (-15.71%)</td><td>0.03 <b>(-34.34%)</b></td><td>0.01 (-9.63%)</td><td>353.30 <b>(+52.28%)</b></td><td>247.06 <b>(+29.05%)</b></td><td>222.50 (+18.67%)</td><td>205.30 <b>(+35.15%)</b></td><td>60.23 <b>(+93.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>191.44 (n/a)</td><td>187.50 (n/a)</td><td>151.90 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 <b>(-29.75%)</b></td><td>0.11 <b>(-23.44%)</b></td><td>0.12 (-15.54%)</td><td>0.09 (-17.13%)</td><td>0.01 <b>(-44.82%)</b></td><td>221.70 <b>(+20.62%)</b></td><td>186.44 <b>(+29.11%)</b></td><td>173.90 (+18.38%)</td><td>166.60 <b>(+42.39%)</b></td><td>24.20 (-6.21%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>144.40 (n/a)</td><td>146.90 (n/a)</td><td>117.00 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-2.89%)</td><td>0.13 (-9.10%)</td><td>0.11 (-10.88%)</td><td>0.11 (-6.05%)</td><td>0.02 (+0.67%)</td><td>189.60 (+6.46%)</td><td>169.86 (+10.26%)</td><td>184.20 (+12.18%)</td><td>131.80 (+2.97%)</td><td>24.65 (+12.57%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>178.10 (n/a)</td><td>154.06 (n/a)</td><td>164.20 (n/a)</td><td>128.00 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (-15.88%)</td><td>0.12 (-7.38%)</td><td>0.12 (-1.79%)</td><td>0.09 (-15.36%)</td><td>0.02 (-17.47%)</td><td>232.50 (+18.14%)</td><td>182.78 (+7.89%)</td><td>170.90 (+1.79%)</td><td>149.30 (+18.87%)</td><td>33.41 (+17.25%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>169.42 (n/a)</td><td>167.90 (n/a)</td><td>125.60 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (-14.02%)</td><td>0.11 (-4.37%)</td><td>0.12 (+4.59%)</td><td>0.09 (+14.62%)</td><td>0.02 <b>(-41.53%)</b></td><td>239.40 (-12.76%)</td><td>190.58 (+0.32%)</td><td>182.20 (-4.41%)</td><td>149.40 (+16.26%)</td><td>32.95 <b>(-40.46%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>274.40 (n/a)</td><td>189.98 (n/a)</td><td>190.60 (n/a)</td><td>128.50 (n/a)</td><td>55.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (-19.39%)</td><td>0.12 (-12.28%)</td><td>0.12 (-1.97%)</td><td>0.10 (+0.93%)</td><td>0.01 <b>(-48.45%)</b></td><td>202.60 (-0.88%)</td><td>180.42 (+11.98%)</td><td>170.70 (+2.03%)</td><td>159.20 <b>(+24.08%)</b></td><td>19.88 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>161.12 (n/a)</td><td>167.30 (n/a)</td><td>128.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (+1.84%)</td><td>0.12 (-5.45%)</td><td>0.11 (-7.07%)</td><td>0.10 (-0.88%)</td><td>0.02 (+14.44%)</td><td>207.90 (+0.92%)</td><td>182.32 (+6.32%)</td><td>183.50 (+7.56%)</td><td>136.10 (-1.80%)</td><td>29.08 (+13.10%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>206.00 (n/a)</td><td>171.48 (n/a)</td><td>170.60 (n/a)</td><td>138.60 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 <b>(-38.18%)</b></td><td>0.10 <b>(-26.68%)</b></td><td>0.10 (-16.84%)</td><td>0.08 <b>(-31.13%)</b></td><td>0.01 <b>(-45.51%)</b></td><td>265.20 <b>(+45.16%)</b></td><td>218.90 <b>(+35.39%)</b></td><td>200.90 <b>(+20.30%)</b></td><td>193.10 <b>(+61.73%)</b></td><td>32.80 <b>(+27.16%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>182.70 (n/a)</td><td>161.68 (n/a)</td><td>167.00 (n/a)</td><td>119.40 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 <b>(-27.17%)</b></td><td>0.08 <b>(-24.47%)</b></td><td>0.08 <b>(-21.29%)</b></td><td>0.06 <b>(-28.35%)</b></td><td>0.02 <b>(-20.32%)</b></td><td>329.40 <b>(+39.58%)</b></td><td>265.24 <b>(+33.13%)</b></td><td>259.30 <b>(+27.05%)</b></td><td>208.90 <b>(+37.34%)</b></td><td>51.78 <b>(+52.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.00 (n/a)</td><td>199.24 (n/a)</td><td>204.10 (n/a)</td><td>152.10 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>155.02 (n/a)</td><td>158.70 (n/a)</td><td>121.10 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.60 (n/a)</td><td>156.16 (n/a)</td><td>158.00 (n/a)</td><td>126.90 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>210.30 (n/a)</td><td>177.26 (n/a)</td><td>169.40 (n/a)</td><td>154.30 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.40 (n/a)</td><td>184.98 (n/a)</td><td>159.40 (n/a)</td><td>133.00 (n/a)</td><td>50.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.80 (n/a)</td><td>160.00 (n/a)</td><td>140.20 (n/a)</td><td>126.80 (n/a)</td><td>38.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>184.84 (n/a)</td><td>174.40 (n/a)</td><td>123.80 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>193.98 (n/a)</td><td>203.60 (n/a)</td><td>158.90 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>182.60 (n/a)</td><td>174.60 (n/a)</td><td>157.30 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>200.20 (n/a)</td><td>174.40 (n/a)</td><td>177.70 (n/a)</td><td>131.40 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>231.50 (n/a)</td><td>180.74 (n/a)</td><td>183.30 (n/a)</td><td>132.10 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.40 (n/a)</td><td>174.52 (n/a)</td><td>165.00 (n/a)</td><td>121.10 (n/a)</td><td>45.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>230.30 (n/a)</td><td>188.68 (n/a)</td><td>209.70 (n/a)</td><td>116.50 (n/a)</td><td>48.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.36 (+16.98%)</td><td>0.25 (-8.70%)</td><td>0.24 (-7.71%)</td><td>0.14 <b>(-38.93%)</b></td><td>0.08 <b>(+190.11%)</b></td><td>342.00 <b>(+63.79%)</b></td><td>218.72 (+18.90%)</td><td>202.90 (+8.39%)</td><td>135.50 (-14.51%)</td><td>76.74 <b>(+318.11%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>208.80 (n/a)</td><td>183.96 (n/a)</td><td>187.20 (n/a)</td><td>158.50 (n/a)</td><td>18.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>216.00 (n/a)</td><td>174.50 (n/a)</td><td>182.60 (n/a)</td><td>127.10 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>179.80 (n/a)</td><td>155.24 (n/a)</td><td>155.40 (n/a)</td><td>117.30 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>230.70 (n/a)</td><td>188.64 (n/a)</td><td>197.20 (n/a)</td><td>140.30 (n/a)</td><td>42.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>146.38 (n/a)</td><td>135.90 (n/a)</td><td>116.60 (n/a)</td><td>27.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>187.90 (n/a)</td><td>198.50 (n/a)</td><td>103.70 (n/a)</td><td>51.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>217.00 (n/a)</td><td>183.38 (n/a)</td><td>181.20 (n/a)</td><td>151.70 (n/a)</td><td>25.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.60 (n/a)</td><td>167.20 (n/a)</td><td>167.40 (n/a)</td><td>132.30 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>271.90 (n/a)</td><td>181.14 (n/a)</td><td>166.00 (n/a)</td><td>125.10 (n/a)</td><td>61.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>359.00 (n/a)</td><td>192.74 (n/a)</td><td>167.60 (n/a)</td><td>111.10 (n/a)</td><td>99.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>169.40 (n/a)</td><td>164.60 (n/a)</td><td>153.70 (n/a)</td><td>19.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>174.54 (n/a)</td><td>162.30 (n/a)</td><td>155.80 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>155.08 (n/a)</td><td>141.10 (n/a)</td><td>113.90 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>186.70 (n/a)</td><td>168.04 (n/a)</td><td>178.40 (n/a)</td><td>119.90 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>182.80 (n/a)</td><td>185.10 (n/a)</td><td>142.10 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>251.10 (n/a)</td><td>193.36 (n/a)</td><td>181.10 (n/a)</td><td>125.90 (n/a)</td><td>53.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>205.30 (n/a)</td><td>182.20 (n/a)</td><td>175.70 (n/a)</td><td>160.00 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>224.50 (n/a)</td><td>183.32 (n/a)</td><td>181.90 (n/a)</td><td>118.70 (n/a)</td><td>41.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>195.90 (n/a)</td><td>159.02 (n/a)</td><td>170.30 (n/a)</td><td>115.90 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.70 (n/a)</td><td>150.26 (n/a)</td><td>155.80 (n/a)</td><td>119.00 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>161.50 (n/a)</td><td>150.58 (n/a)</td><td>148.40 (n/a)</td><td>143.00 (n/a)</td><td>7.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>277.10 (n/a)</td><td>165.36 (n/a)</td><td>149.10 (n/a)</td><td>116.90 (n/a)</td><td>64.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>149.94 (n/a)</td><td>141.40 (n/a)</td><td>125.50 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>162.78 (n/a)</td><td>155.60 (n/a)</td><td>131.80 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>172.86 (n/a)</td><td>166.20 (n/a)</td><td>152.20 (n/a)</td><td>22.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>156.34 (n/a)</td><td>157.90 (n/a)</td><td>107.20 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.70 (n/a)</td><td>187.64 (n/a)</td><td>194.50 (n/a)</td><td>168.80 (n/a)</td><td>16.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>146.22 (n/a)</td><td>143.50 (n/a)</td><td>127.30 (n/a)</td><td>21.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.90 (n/a)</td><td>164.84 (n/a)</td><td>152.80 (n/a)</td><td>129.10 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>356.90 (n/a)</td><td>192.52 (n/a)</td><td>168.80 (n/a)</td><td>130.40 (n/a)</td><td>94.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>227.00 (n/a)</td><td>175.26 (n/a)</td><td>174.40 (n/a)</td><td>109.00 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>183.16 (n/a)</td><td>181.20 (n/a)</td><td>123.40 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>188.42 (n/a)</td><td>172.40 (n/a)</td><td>130.30 (n/a)</td><td>46.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>207.62 (n/a)</td><td>208.30 (n/a)</td><td>170.10 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>248.40 (n/a)</td><td>230.40 (n/a)</td><td>238.70 (n/a)</td><td>197.40 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>162.98 (n/a)</td><td>165.40 (n/a)</td><td>132.10 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.00 (n/a)</td><td>165.82 (n/a)</td><td>152.30 (n/a)</td><td>133.50 (n/a)</td><td>41.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.80 (n/a)</td><td>158.62 (n/a)</td><td>165.80 (n/a)</td><td>116.30 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>168.50 (n/a)</td><td>158.10 (n/a)</td><td>146.80 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>161.22 (n/a)</td><td>165.20 (n/a)</td><td>124.20 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>191.42 (n/a)</td><td>197.60 (n/a)</td><td>160.00 (n/a)</td><td>18.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>177.62 (n/a)</td><td>174.60 (n/a)</td><td>156.80 (n/a)</td><td>21.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>288.90 (n/a)</td><td>219.26 (n/a)</td><td>214.30 (n/a)</td><td>186.70 (n/a)</td><td>41.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.30 (n/a)</td><td>172.52 (n/a)</td><td>175.30 (n/a)</td><td>143.30 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>222.50 (n/a)</td><td>175.28 (n/a)</td><td>180.00 (n/a)</td><td>127.50 (n/a)</td><td>35.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.30 (n/a)</td><td>170.70 (n/a)</td><td>177.70 (n/a)</td><td>125.30 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>269.00 (n/a)</td><td>195.08 (n/a)</td><td>195.30 (n/a)</td><td>122.40 (n/a)</td><td>59.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.90 (n/a)</td><td>171.52 (n/a)</td><td>167.10 (n/a)</td><td>129.30 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>245.50 (n/a)</td><td>205.60 (n/a)</td><td>239.50 (n/a)</td><td>132.40 (n/a)</td><td>53.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>187.52 (n/a)</td><td>190.80 (n/a)</td><td>171.90 (n/a)</td><td>11.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>214.58 (n/a)</td><td>209.00 (n/a)</td><td>202.80 (n/a)</td><td>12.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>4.80 (-2.53%)</td><td>4.24 (-1.59%)</td><td>4.12 (-4.73%)</td><td>4.02 (+16.03%)</td><td>0.32 <b>(-44.91%)</b></td><td>2336.80 (-13.82%)</td><td>2229.52 (+0.47%)</td><td>2285.10 (+4.97%)</td><td>1959.60 (+2.60%)</td><td>153.61 <b>(-51.83%)</b></td><td>1887.83 (-2.53%)</td><td>1666.20 (-1.59%)</td><td>1618.93 (-4.73%)</td><td>1583.06 (+16.03%)</td><td>125.53 <b>(-44.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>4.92 (n/a)</td><td>4.30 (n/a)</td><td>4.32 (n/a)</td><td>3.47 (n/a)</td><td>0.58 (n/a)</td><td>2711.50 (n/a)</td><td>2219.16 (n/a)</td><td>2177.00 (n/a)</td><td>1910.00 (n/a)</td><td>318.90 (n/a)</td><td>1936.80 (n/a)</td><td>1693.06 (n/a)</td><td>1699.31 (n/a)</td><td>1364.33 (n/a)</td><td>227.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.23 (+1.58%)</td><td>0.96 (-13.16%)</td><td>0.93 (-13.35%)</td><td>0.65 <b>(-35.03%)</b></td><td>0.21 <b>(+125.36%)</b></td><td>339.40 <b>(+53.92%)</b></td><td>241.42 (+19.68%)</td><td>238.60 (+15.43%)</td><td>179.40 (-1.54%)</td><td>60.14 <b>(+254.10%)</b></td><td>52.61 (+1.58%)</td><td>40.86 (-13.16%)</td><td>39.56 (-13.35%)</td><td>27.81 <b>(-35.03%)</b></td><td>9.08 <b>(+125.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.21 (n/a)</td><td>1.10 (n/a)</td><td>1.07 (n/a)</td><td>1.00 (n/a)</td><td>0.09 (n/a)</td><td>220.50 (n/a)</td><td>201.72 (n/a)</td><td>206.70 (n/a)</td><td>182.20 (n/a)</td><td>16.98 (n/a)</td><td>51.79 (n/a)</td><td>47.06 (n/a)</td><td>45.65 (n/a)</td><td>42.80 (n/a)</td><td>4.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.10 (-9.72%)</td><td>0.99 (-10.07%)</td><td>1.06 (-4.02%)</td><td>0.65 <b>(-33.63%)</b></td><td>0.19 <b>(+64.57%)</b></td><td>339.90 <b>(+50.66%)</b></td><td>232.58 (+14.79%)</td><td>208.20 (+4.20%)</td><td>201.10 (+10.74%)</td><td>60.13 <b>(+179.76%)</b></td><td>46.93 (-9.72%)</td><td>42.26 (-10.07%)</td><td>45.32 (-4.02%)</td><td>27.76 <b>(-33.63%)</b></td><td>8.15 <b>(+64.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.22 (n/a)</td><td>1.10 (n/a)</td><td>1.11 (n/a)</td><td>0.98 (n/a)</td><td>0.12 (n/a)</td><td>225.60 (n/a)</td><td>202.62 (n/a)</td><td>199.80 (n/a)</td><td>181.60 (n/a)</td><td>21.49 (n/a)</td><td>51.98 (n/a)</td><td>47.00 (n/a)</td><td>47.22 (n/a)</td><td>41.83 (n/a)</td><td>4.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.52 (+0.10%)</td><td>0.52 (+0.00%)</td><td>0.52 (+0.17%)</td><td>0.51 (-0.30%)</td><td>0.00 <b>(+139.31%)</b></td><td>48920.00 (+0.31%)</td><td>48709.80 (+0.00%)</td><td>48651.10 (-0.17%)</td><td>48595.90 (-0.10%)</td><td>132.46 <b>(+139.91%)</b></td><td>353.53 (+0.10%)</td><td>352.70 (+0.00%)</td><td>353.12 (+0.17%)</td><td>351.18 (-0.30%)</td><td>0.96 <b>(+139.31%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48771.00 (n/a)</td><td>48709.56 (n/a)</td><td>48735.50 (n/a)</td><td>48645.90 (n/a)</td><td>55.21 (n/a)</td><td>353.16 (n/a)</td><td>352.70 (n/a)</td><td>352.51 (n/a)</td><td>352.26 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-1.58%)</td><td>0.21 (+0.02%)</td><td>0.21 (+0.54%)</td><td>0.21 (+1.22%)</td><td>0.00 <b>(-73.42%)</b></td><td>118512.10 (-1.20%)</td><td>117764.04 (-0.04%)</td><td>117586.10 (-0.53%)</td><td>117110.20 (+1.61%)</td><td>536.56 <b>(-73.30%)</b></td><td>146.70 (-1.58%)</td><td>145.89 (+0.02%)</td><td>146.10 (+0.54%)</td><td>144.96 (+1.22%)</td><td>0.66 <b>(-73.42%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119956.70 (n/a)</td><td>117809.10 (n/a)</td><td>118217.80 (n/a)</td><td>115259.70 (n/a)</td><td>2009.89 (n/a)</td><td>149.05 (n/a)</td><td>145.86 (n/a)</td><td>145.32 (n/a)</td><td>143.22 (n/a)</td><td>2.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.89 (-0.46%)</td><td>0.88 (-0.23%)</td><td>0.89 (-0.22%)</td><td>0.87 (-0.04%)</td><td>0.01 (-6.15%)</td><td>28801.80 (+0.04%)</td><td>28445.98 (+0.23%)</td><td>28392.50 (+0.22%)</td><td>28216.50 (+0.46%)</td><td>242.32 (-5.86%)</td><td>608.86 (-0.46%)</td><td>603.98 (-0.23%)</td><td>605.09 (-0.22%)</td><td>596.49 (-0.04%)</td><td>5.12 (-6.15%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28791.50 (n/a)</td><td>28381.98 (n/a)</td><td>28330.20 (n/a)</td><td>28087.40 (n/a)</td><td>257.41 (n/a)</td><td>611.66 (n/a)</td><td>605.35 (n/a)</td><td>606.41 (n/a)</td><td>596.70 (n/a)</td><td>5.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.63 (+2.64%)</td><td>3.52 (+4.27%)</td><td>3.54 (+6.22%)</td><td>3.35 (+2.83%)</td><td>0.11 (-6.62%)</td><td>7522.60 (-2.75%)</td><td>7147.38 (-4.11%)</td><td>7111.50 (-5.86%)</td><td>6939.60 (-2.57%)</td><td>230.91 (-11.11%)</td><td>2475.64 (+2.64%)</td><td>2405.62 (+4.27%)</td><td>2415.79 (+6.22%)</td><td>2283.77 (+2.83%)</td><td>75.82 (-6.62%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.53 (n/a)</td><td>3.38 (n/a)</td><td>3.33 (n/a)</td><td>3.25 (n/a)</td><td>0.12 (n/a)</td><td>7735.30 (n/a)</td><td>7453.58 (n/a)</td><td>7554.10 (n/a)</td><td>7122.90 (n/a)</td><td>259.78 (n/a)</td><td>2411.93 (n/a)</td><td>2307.18 (n/a)</td><td>2274.26 (n/a)</td><td>2220.97 (n/a)</td><td>81.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.16 (+10.28%)</td><td>2.88 (+2.08%)</td><td>2.83 (-0.05%)</td><td>2.73 (-1.55%)</td><td>0.16 <b>(+288.80%)</b></td><td>9233.90 (+1.57%)</td><td>8757.44 (-1.81%)</td><td>8900.20 (+0.05%)</td><td>7970.10 (-9.32%)</td><td>472.73 <b>(+254.07%)</b></td><td>2155.53 (+10.28%)</td><td>1966.56 (+2.08%)</td><td>1930.27 (-0.05%)</td><td>1860.53 (-1.55%)</td><td>111.76 <b>(+288.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>2.86 (n/a)</td><td>2.82 (n/a)</td><td>2.83 (n/a)</td><td>2.77 (n/a)</td><td>0.04 (n/a)</td><td>9091.00 (n/a)</td><td>8919.30 (n/a)</td><td>8895.80 (n/a)</td><td>8789.20 (n/a)</td><td>133.51 (n/a)</td><td>1954.67 (n/a)</td><td>1926.49 (n/a)</td><td>1931.23 (n/a)</td><td>1889.76 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.32 (+0.88%)</td><td>3.24 (+1.63%)</td><td>3.28 (+3.72%)</td><td>3.14 (+0.68%)</td><td>0.09 <b>(+37.82%)</b></td><td>8001.90 (-0.68%)</td><td>7773.72 (-1.58%)</td><td>7661.80 (-3.59%)</td><td>7581.10 (-0.88%)</td><td>208.18 <b>(+36.74%)</b></td><td>2266.16 (+0.88%)</td><td>2211.26 (+1.63%)</td><td>2242.28 (+3.72%)</td><td>2146.97 (+0.68%)</td><td>58.74 <b>(+37.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.29 (n/a)</td><td>3.19 (n/a)</td><td>3.17 (n/a)</td><td>3.12 (n/a)</td><td>0.06 (n/a)</td><td>8056.60 (n/a)</td><td>7898.20 (n/a)</td><td>7946.90 (n/a)</td><td>7648.10 (n/a)</td><td>152.24 (n/a)</td><td>2246.29 (n/a)</td><td>2175.82 (n/a)</td><td>2161.85 (n/a)</td><td>2132.39 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.79 (+0.41%)</td><td>0.78 (+0.13%)</td><td>0.78 (+0.02%)</td><td>0.78 (+0.19%)</td><td>0.00 <b>(+81.20%)</b></td><td>96500.40 (-0.19%)</td><td>96373.40 (-0.13%)</td><td>96433.70 (-0.02%)</td><td>96054.40 (-0.40%)</td><td>180.84 <b>(+80.06%)</b></td><td>715.42 (+0.41%)</td><td>713.06 (+0.13%)</td><td>712.61 (+0.02%)</td><td>712.12 (+0.19%)</td><td>1.34 <b>(+81.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96679.30 (n/a)</td><td>96500.66 (n/a)</td><td>96453.90 (n/a)</td><td>96445.00 (n/a)</td><td>100.44 (n/a)</td><td>712.53 (n/a)</td><td>712.11 (n/a)</td><td>712.46 (n/a)</td><td>710.80 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.73 (-0.04%)</td><td>0.73 (-0.07%)</td><td>0.73 (-0.18%)</td><td>0.73 (+0.02%)</td><td>0.00 (-19.29%)</td><td>103905.00 (-0.02%)</td><td>103803.30 (+0.07%)</td><td>103824.30 (+0.18%)</td><td>103652.50 (+0.04%)</td><td>108.84 (-19.25%)</td><td>662.98 (-0.04%)</td><td>662.02 (-0.07%)</td><td>661.88 (-0.18%)</td><td>661.37 (+0.02%)</td><td>0.69 (-19.29%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103925.40 (n/a)</td><td>103726.50 (n/a)</td><td>103642.30 (n/a)</td><td>103615.60 (n/a)</td><td>134.79 (n/a)</td><td>663.22 (n/a)</td><td>662.51 (n/a)</td><td>663.04 (n/a)</td><td>661.24 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.70 (-0.15%)</td><td>0.69 (-0.26%)</td><td>0.69 (-0.27%)</td><td>0.69 (-0.27%)</td><td>0.00 <b>(+31.76%)</b></td><td>109189.20 (+0.27%)</td><td>108981.00 (+0.26%)</td><td>109042.80 (+0.27%)</td><td>108616.30 (+0.15%)</td><td>237.63 <b>(+32.34%)</b></td><td>632.68 (-0.15%)</td><td>630.57 (-0.26%)</td><td>630.21 (-0.27%)</td><td>629.36 (-0.27%)</td><td>1.38 <b>(+31.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108895.10 (n/a)</td><td>108698.66 (n/a)</td><td>108753.60 (n/a)</td><td>108450.20 (n/a)</td><td>179.56 (n/a)</td><td>633.65 (n/a)</td><td>632.20 (n/a)</td><td>631.88 (n/a)</td><td>631.06 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.64 (+1.07%)</td><td>7.28 (+5.58%)</td><td>7.51 (+6.24%)</td><td>6.82 (+9.39%)</td><td>0.38 <b>(-26.93%)</b></td><td>1307.10 (-8.59%)</td><td>1226.82 (-5.52%)</td><td>1186.20 (-5.87%)</td><td>1166.90 (-1.05%)</td><td>65.98 <b>(-34.13%)</b></td><td>460.09 (+1.07%)</td><td>438.62 (+5.58%)</td><td>452.61 (+6.24%)</td><td>410.73 (+9.39%)</td><td>23.16 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.56 (n/a)</td><td>6.90 (n/a)</td><td>7.07 (n/a)</td><td>6.23 (n/a)</td><td>0.53 (n/a)</td><td>1429.90 (n/a)</td><td>1298.46 (n/a)</td><td>1260.20 (n/a)</td><td>1179.30 (n/a)</td><td>100.17 (n/a)</td><td>455.23 (n/a)</td><td>415.43 (n/a)</td><td>426.03 (n/a)</td><td>375.47 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.82 (-3.13%)</td><td>6.41 (+0.20%)</td><td>6.32 (-7.31%)</td><td>6.13 <b>(+33.78%)</b></td><td>0.30 <b>(-71.10%)</b></td><td>1454.60 <b>(-25.25%)</b></td><td>1392.98 (-2.64%)</td><td>1410.20 (+7.88%)</td><td>1307.80 (+3.23%)</td><td>63.64 <b>(-78.05%)</b></td><td>410.52 (-3.13%)</td><td>386.06 (+0.20%)</td><td>380.70 (-7.31%)</td><td>369.09 <b>(+33.78%)</b></td><td>17.92 <b>(-71.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.04 (n/a)</td><td>6.40 (n/a)</td><td>6.82 (n/a)</td><td>4.58 (n/a)</td><td>1.03 (n/a)</td><td>1946.00 (n/a)</td><td>1430.68 (n/a)</td><td>1307.20 (n/a)</td><td>1266.90 (n/a)</td><td>289.90 (n/a)</td><td>423.78 (n/a)</td><td>385.29 (n/a)</td><td>410.71 (n/a)</td><td>275.88 (n/a)</td><td>62.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.07 (+0.49%)</td><td>6.41 (+2.50%)</td><td>6.64 (+0.83%)</td><td>5.15 (+7.71%)</td><td>0.73 (-18.53%)</td><td>1729.40 (-7.16%)</td><td>1406.96 (-3.14%)</td><td>1343.00 (-0.82%)</td><td>1259.80 (-0.49%)</td><td>184.53 <b>(-23.69%)</b></td><td>426.16 (+0.49%)</td><td>386.20 (+2.50%)</td><td>399.74 (+0.83%)</td><td>310.43 (+7.71%)</td><td>44.14 (-18.53%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.04 (n/a)</td><td>6.25 (n/a)</td><td>6.58 (n/a)</td><td>4.78 (n/a)</td><td>0.90 (n/a)</td><td>1862.70 (n/a)</td><td>1452.64 (n/a)</td><td>1354.10 (n/a)</td><td>1266.00 (n/a)</td><td>241.82 (n/a)</td><td>424.08 (n/a)</td><td>376.77 (n/a)</td><td>396.47 (n/a)</td><td>288.22 (n/a)</td><td>54.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>8.01 (-1.99%)</td><td>7.58 (-0.53%)</td><td>7.44 (+0.67%)</td><td>7.15 (-1.15%)</td><td>0.39 (-9.70%)</td><td>4877.50 (+1.16%)</td><td>4608.74 (+0.49%)</td><td>4683.40 (-0.67%)</td><td>4351.50 (+2.03%)</td><td>237.73 (-7.67%)</td><td>493.51 (-1.99%)</td><td>466.96 (-0.53%)</td><td>458.53 (+0.67%)</td><td>440.29 (-1.15%)</td><td>24.28 (-9.70%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.17 (n/a)</td><td>7.62 (n/a)</td><td>7.39 (n/a)</td><td>7.23 (n/a)</td><td>0.44 (n/a)</td><td>4821.50 (n/a)</td><td>4586.20 (n/a)</td><td>4714.80 (n/a)</td><td>4265.00 (n/a)</td><td>257.47 (n/a)</td><td>503.51 (n/a)</td><td>469.46 (n/a)</td><td>455.48 (n/a)</td><td>445.40 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.74 (-1.57%)</td><td>7.46 (-1.33%)</td><td>7.51 (-0.76%)</td><td>7.00 (-4.52%)</td><td>0.28 <b>(+39.75%)</b></td><td>4984.00 (+4.74%)</td><td>4678.76 (+1.41%)</td><td>4642.90 (+0.77%)</td><td>4507.10 (+1.60%)</td><td>179.90 <b>(+50.36%)</b></td><td>476.47 (-1.57%)</td><td>459.51 (-1.33%)</td><td>462.53 (-0.76%)</td><td>430.88 (-4.52%)</td><td>17.04 <b>(+39.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.86 (n/a)</td><td>7.56 (n/a)</td><td>7.57 (n/a)</td><td>7.33 (n/a)</td><td>0.20 (n/a)</td><td>4758.50 (n/a)</td><td>4613.84 (n/a)</td><td>4607.60 (n/a)</td><td>4436.20 (n/a)</td><td>119.65 (n/a)</td><td>484.08 (n/a)</td><td>465.70 (n/a)</td><td>466.08 (n/a)</td><td>451.29 (n/a)</td><td>12.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.69 (+4.21%)</td><td>7.36 (+2.77%)</td><td>7.28 (-0.84%)</td><td>7.18 (+5.69%)</td><td>0.20 <b>(-28.09%)</b></td><td>4855.00 (-5.39%)</td><td>4736.86 (-2.76%)</td><td>4788.30 (+0.84%)</td><td>4532.10 (-4.04%)</td><td>126.43 <b>(-34.63%)</b></td><td>473.84 (+4.21%)</td><td>453.62 (+2.77%)</td><td>448.48 (-0.84%)</td><td>442.32 (+5.69%)</td><td>12.38 <b>(-28.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.38 (n/a)</td><td>7.17 (n/a)</td><td>7.34 (n/a)</td><td>6.79 (n/a)</td><td>0.28 (n/a)</td><td>5131.40 (n/a)</td><td>4871.06 (n/a)</td><td>4748.20 (n/a)</td><td>4722.70 (n/a)</td><td>193.42 (n/a)</td><td>454.72 (n/a)</td><td>441.41 (n/a)</td><td>452.28 (n/a)</td><td>418.50 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.79 (-0.36%)</td><td>0.79 (-0.01%)</td><td>0.79 (+0.12%)</td><td>0.79 (+0.04%)</td><td>0.00 <b>(-71.74%)</b></td><td>95868.50 (-0.04%)</td><td>95756.80 (+0.01%)</td><td>95741.60 (-0.12%)</td><td>95692.40 (+0.36%)</td><td>65.98 <b>(-71.63%)</b></td><td>718.13 (-0.36%)</td><td>717.65 (-0.01%)</td><td>717.76 (+0.12%)</td><td>716.81 (+0.04%)</td><td>0.49 <b>(-71.74%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95902.40 (n/a)</td><td>95747.94 (n/a)</td><td>95858.10 (n/a)</td><td>95348.40 (n/a)</td><td>232.61 (n/a)</td><td>720.72 (n/a)</td><td>717.72 (n/a)</td><td>716.89 (n/a)</td><td>716.56 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.73 (-0.02%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.03%)</td><td>0.73 (-0.11%)</td><td>0.00 <b>(+185.04%)</b></td><td>103051.20 (+0.11%)</td><td>102960.16 (+0.04%)</td><td>102946.00 (+0.03%)</td><td>102918.70 (+0.02%)</td><td>52.12 <b>(+185.96%)</b></td><td>667.71 (-0.02%)</td><td>667.44 (-0.04%)</td><td>667.53 (-0.03%)</td><td>666.85 (-0.11%)</td><td>0.34 <b>(+185.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102937.80 (n/a)</td><td>102918.70 (n/a)</td><td>102914.70 (n/a)</td><td>102900.00 (n/a)</td><td>18.23 (n/a)</td><td>667.83 (n/a)</td><td>667.71 (n/a)</td><td>667.73 (n/a)</td><td>667.58 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.70 (+0.04%)</td><td>0.70 (+0.05%)</td><td>0.70 (+0.06%)</td><td>0.70 (+0.16%)</td><td>0.00 (-16.80%)</td><td>107950.60 (-0.16%)</td><td>107799.20 (-0.05%)</td><td>107830.20 (-0.06%)</td><td>107508.30 (-0.04%)</td><td>178.99 (-16.95%)</td><td>639.20 (+0.04%)</td><td>637.48 (+0.05%)</td><td>637.29 (+0.06%)</td><td>636.58 (+0.16%)</td><td>1.06 (-16.80%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>108125.60 (n/a)</td><td>107849.78 (n/a)</td><td>107890.60 (n/a)</td><td>107546.90 (n/a)</td><td>215.53 (n/a)</td><td>638.97 (n/a)</td><td>637.18 (n/a)</td><td>636.94 (n/a)</td><td>635.55 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>4.11 (-2.86%)</td><td>3.73 (-0.72%)</td><td>3.62 (-8.55%)</td><td>3.49 <b>(+25.86%)</b></td><td>0.24 <b>(-60.11%)</b></td><td>2311.00 <b>(-20.55%)</b></td><td>2170.50 (-1.41%)</td><td>2224.00 (+9.35%)</td><td>1959.10 (+2.95%)</td><td>134.28 <b>(-67.85%)</b></td><td>1079.03 (-2.86%)</td><td>977.06 (-0.72%)</td><td>950.52 (-8.55%)</td><td>914.72 <b>(+25.86%)</b></td><td>63.25 <b>(-60.11%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>4.24 (n/a)</td><td>3.75 (n/a)</td><td>3.96 (n/a)</td><td>2.77 (n/a)</td><td>0.60 (n/a)</td><td>2908.70 (n/a)</td><td>2201.48 (n/a)</td><td>2033.80 (n/a)</td><td>1903.00 (n/a)</td><td>417.65 (n/a)</td><td>1110.82 (n/a)</td><td>984.15 (n/a)</td><td>1039.40 (n/a)</td><td>726.75 (n/a)</td><td>158.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.38 <b>(-23.66%)</b></td><td>0.32 (-11.51%)</td><td>0.32 (-6.58%)</td><td>0.29 (-6.14%)</td><td>0.04 <b>(-53.47%)</b></td><td>4319.00 (+6.54%)</td><td>3889.50 (+10.70%)</td><td>3922.90 (+7.04%)</td><td>3242.80 <b>(+31.00%)</b></td><td>403.72 <b>(-33.57%)</b></td><td>20.69 <b>(-23.66%)</b></td><td>17.42 (-11.51%)</td><td>17.11 (-6.58%)</td><td>15.54 (-6.14%)</td><td>1.97 <b>(-53.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>4053.80 (n/a)</td><td>3513.42 (n/a)</td><td>3664.80 (n/a)</td><td>2475.50 (n/a)</td><td>607.71 (n/a)</td><td>27.11 (n/a)</td><td>19.68 (n/a)</td><td>18.31 (n/a)</td><td>16.55 (n/a)</td><td>4.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.33 (-1.44%)</td><td>4.41 (-9.21%)</td><td>3.95 (-15.71%)</td><td>3.26 (-12.01%)</td><td>1.22 <b>(+24.15%)</b></td><td>2040.30 (+13.65%)</td><td>1592.74 (+12.76%)</td><td>1682.60 (+18.64%)</td><td>1051.40 (+1.46%)</td><td>385.91 <b>(+43.37%)</b></td><td>1954.74 (-1.44%)</td><td>1361.93 (-9.21%)</td><td>1221.46 (-15.71%)</td><td>1007.29 (-12.01%)</td><td>376.03 <b>(+24.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.42 (n/a)</td><td>4.86 (n/a)</td><td>4.69 (n/a)</td><td>3.71 (n/a)</td><td>0.98 (n/a)</td><td>1795.30 (n/a)</td><td>1412.56 (n/a)</td><td>1418.20 (n/a)</td><td>1036.30 (n/a)</td><td>269.17 (n/a)</td><td>1983.19 (n/a)</td><td>1500.15 (n/a)</td><td>1449.16 (n/a)</td><td>1144.75 (n/a)</td><td>302.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.27 (n/a)</td><td>12.68 (n/a)</td><td>13.15 (n/a)</td><td>11.07 (n/a)</td><td>0.93 (n/a)</td><td>13.26 (n/a)</td><td>12.67 (n/a)</td><td>13.14 (n/a)</td><td>11.07 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>24.96 (-1.14%)</td><td>24.17 (+0.04%)</td><td>24.27 (+1.35%)</td><td>22.87 (-3.02%)</td><td>0.82 <b>(+28.77%)</b></td><td>24.95 (-1.14%)</td><td>24.16 (+0.04%)</td><td>24.25 (+1.35%)</td><td>22.86 (-3.02%)</td><td>0.82 <b>(+28.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>25.25 (n/a)</td><td>24.16 (n/a)</td><td>23.94 (n/a)</td><td>23.59 (n/a)</td><td>0.64 (n/a)</td><td>25.23 (n/a)</td><td>24.14 (n/a)</td><td>23.93 (n/a)</td><td>23.57 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>42.01 (+1.77%)</td><td>39.63 (+1.47%)</td><td>39.35 (-1.41%)</td><td>38.16 (+9.22%)</td><td>1.43 <b>(-42.40%)</b></td><td>41.98 (+1.77%)</td><td>39.61 (+1.47%)</td><td>39.32 (-1.41%)</td><td>38.14 (+9.22%)</td><td>1.43 <b>(-42.40%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>41.28 (n/a)</td><td>39.06 (n/a)</td><td>39.91 (n/a)</td><td>34.94 (n/a)</td><td>2.48 (n/a)</td><td>41.25 (n/a)</td><td>39.03 (n/a)</td><td>39.88 (n/a)</td><td>34.92 (n/a)</td><td>2.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>44.39 (-2.05%)</td><td>42.37 (-4.17%)</td><td>42.45 (-3.24%)</td><td>39.77 (-8.01%)</td><td>1.71 <b>(+103.36%)</b></td><td>44.36 (-2.05%)</td><td>42.34 (-4.17%)</td><td>42.42 (-3.24%)</td><td>39.74 (-8.01%)</td><td>1.71 <b>(+103.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>45.31 (n/a)</td><td>44.21 (n/a)</td><td>43.87 (n/a)</td><td>43.23 (n/a)</td><td>0.84 (n/a)</td><td>45.29 (n/a)</td><td>44.19 (n/a)</td><td>43.84 (n/a)</td><td>43.20 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.32 (n/a)</td><td>13.13 (n/a)</td><td>13.11 (n/a)</td><td>12.95 (n/a)</td><td>0.15 (n/a)</td><td>13.31 (n/a)</td><td>13.13 (n/a)</td><td>13.10 (n/a)</td><td>12.95 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>24.96 (-3.66%)</td><td>23.64 (-3.34%)</td><td>23.91 (-3.01%)</td><td>21.77 (-3.62%)</td><td>1.40 (+14.94%)</td><td>24.95 (-3.66%)</td><td>23.63 (-3.34%)</td><td>23.90 (-3.01%)</td><td>21.76 (-3.62%)</td><td>1.39 (+14.94%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>25.91 (n/a)</td><td>24.46 (n/a)</td><td>24.66 (n/a)</td><td>22.59 (n/a)</td><td>1.21 (n/a)</td><td>25.89 (n/a)</td><td>24.44 (n/a)</td><td>24.64 (n/a)</td><td>22.58 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>40.65 (-3.13%)</td><td>38.85 (-4.35%)</td><td>38.20 (-5.90%)</td><td>37.89 (-4.31%)</td><td>1.19 <b>(+35.02%)</b></td><td>40.63 (-3.13%)</td><td>38.82 (-4.35%)</td><td>38.18 (-5.90%)</td><td>37.87 (-4.31%)</td><td>1.19 <b>(+35.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>41.96 (n/a)</td><td>40.61 (n/a)</td><td>40.60 (n/a)</td><td>39.60 (n/a)</td><td>0.88 (n/a)</td><td>41.94 (n/a)</td><td>40.59 (n/a)</td><td>40.58 (n/a)</td><td>39.58 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>44.89 (-6.81%)</td><td>41.23 (-4.92%)</td><td>41.13 (-1.48%)</td><td>38.00 (-3.39%)</td><td>2.77 <b>(-23.04%)</b></td><td>44.86 (-6.81%)</td><td>41.21 (-4.92%)</td><td>41.11 (-1.48%)</td><td>37.98 (-3.39%)</td><td>2.76 <b>(-23.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>48.17 (n/a)</td><td>43.37 (n/a)</td><td>41.75 (n/a)</td><td>39.33 (n/a)</td><td>3.59 (n/a)</td><td>48.14 (n/a)</td><td>43.34 (n/a)</td><td>41.73 (n/a)</td><td>39.31 (n/a)</td><td>3.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.52 (+2.07%)</td><td>9.13 (+3.97%)</td><td>9.04 (+0.13%)</td><td>8.81 (+10.81%)</td><td>0.31 <b>(-43.06%)</b></td><td>9.50 (+2.07%)</td><td>9.12 (+3.97%)</td><td>9.02 (+0.13%)</td><td>8.79 (+10.81%)</td><td>0.31 <b>(-43.06%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.33 (n/a)</td><td>8.78 (n/a)</td><td>9.03 (n/a)</td><td>7.95 (n/a)</td><td>0.55 (n/a)</td><td>9.31 (n/a)</td><td>8.77 (n/a)</td><td>9.01 (n/a)</td><td>7.94 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.96 (+4.98%)</td><td>0.90 (+8.72%)</td><td>0.94 (+12.39%)</td><td>0.80 (+3.24%)</td><td>0.07 <b>(+22.74%)</b></td><td>0.94 (+4.98%)</td><td>0.89 (+8.72%)</td><td>0.93 (+12.39%)</td><td>0.78 (+3.24%)</td><td>0.07 <b>(+22.74%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.06 (n/a)</td><td>0.90 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.76 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.15 (+15.35%)</td><td>1.06 <b>(+24.01%)</b></td><td>1.04 (+17.65%)</td><td>1.01 <b>(+53.86%)</b></td><td>0.06 <b>(-50.08%)</b></td><td>1.13 (+15.35%)</td><td>1.05 <b>(+24.01%)</b></td><td>1.03 (+17.65%)</td><td>0.99 <b>(+53.86%)</b></td><td>0.06 <b>(-50.08%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.99 (n/a)</td><td>0.86 (n/a)</td><td>0.89 (n/a)</td><td>0.65 (n/a)</td><td>0.12 (n/a)</td><td>0.98 (n/a)</td><td>0.85 (n/a)</td><td>0.88 (n/a)</td><td>0.65 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>15.34 (+1.84%)</td><td>14.94 (+4.04%)</td><td>14.96 (+4.47%)</td><td>14.34 (+6.05%)</td><td>0.38 <b>(-36.28%)</b></td><td>15.17 (+1.84%)</td><td>14.77 (+4.04%)</td><td>14.79 (+4.47%)</td><td>14.17 (+6.05%)</td><td>0.37 <b>(-36.28%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.07 (n/a)</td><td>14.36 (n/a)</td><td>14.32 (n/a)</td><td>13.52 (n/a)</td><td>0.59 (n/a)</td><td>14.89 (n/a)</td><td>14.20 (n/a)</td><td>14.16 (n/a)</td><td>13.37 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.83 (-4.21%)</td><td>10.70 (-11.62%)</td><td>11.63 (-4.11%)</td><td>6.84 <b>(-41.72%)</b></td><td>2.16 <b>(+751.22%)</b></td><td>11.62 (-4.21%)</td><td>10.51 (-11.62%)</td><td>11.42 (-4.11%)</td><td>6.72 <b>(-41.72%)</b></td><td>2.12 <b>(+751.21%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.35 (n/a)</td><td>12.10 (n/a)</td><td>12.12 (n/a)</td><td>11.74 (n/a)</td><td>0.25 (n/a)</td><td>12.13 (n/a)</td><td>11.89 (n/a)</td><td>11.91 (n/a)</td><td>11.53 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.55 <b>(+21.00%)</b></td><td>7.30 (+1.44%)</td><td>7.30 (+5.55%)</td><td>4.99 <b>(-27.45%)</b></td><td>1.73 <b>(+294.58%)</b></td><td>9.38 <b>(+21.00%)</b></td><td>7.17 (+1.44%)</td><td>7.17 (+5.55%)</td><td>4.90 <b>(-27.45%)</b></td><td>1.70 <b>(+294.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>7.89 (n/a)</td><td>7.19 (n/a)</td><td>6.92 (n/a)</td><td>6.88 (n/a)</td><td>0.44 (n/a)</td><td>7.75 (n/a)</td><td>7.07 (n/a)</td><td>6.80 (n/a)</td><td>6.76 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.83 (+5.96%)</td><td>5.58 (-3.32%)</td><td>5.67 (-1.29%)</td><td>4.65 (-6.90%)</td><td>0.83 <b>(+48.26%)</b></td><td>6.72 (+5.96%)</td><td>5.49 (-3.32%)</td><td>5.58 (-1.29%)</td><td>4.58 (-6.90%)</td><td>0.81 <b>(+48.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.45 (n/a)</td><td>5.78 (n/a)</td><td>5.74 (n/a)</td><td>5.00 (n/a)</td><td>0.56 (n/a)</td><td>6.34 (n/a)</td><td>5.68 (n/a)</td><td>5.65 (n/a)</td><td>4.92 (n/a)</td><td>0.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.27 (n/a)</td><td>12.61 (n/a)</td><td>12.54 (n/a)</td><td>11.94 (n/a)</td><td>0.61 (n/a)</td><td>13.26 (n/a)</td><td>12.60 (n/a)</td><td>12.53 (n/a)</td><td>11.93 (n/a)</td><td>0.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.47 (n/a)</td><td>12.78 (n/a)</td><td>13.10 (n/a)</td><td>11.19 (n/a)</td><td>0.92 (n/a)</td><td>13.46 (n/a)</td><td>12.78 (n/a)</td><td>13.09 (n/a)</td><td>11.18 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.30 (n/a)</td><td>137.54 (n/a)</td><td>127.90 (n/a)</td><td>122.20 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>158.70 (n/a)</td><td>144.80 (n/a)</td><td>127.60 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>155.12 (n/a)</td><td>157.80 (n/a)</td><td>112.40 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>310.50 (n/a)</td><td>181.46 (n/a)</td><td>153.90 (n/a)</td><td>135.30 (n/a)</td><td>72.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.70 (n/a)</td><td>147.02 (n/a)</td><td>148.10 (n/a)</td><td>128.90 (n/a)</td><td>18.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>156.00 (n/a)</td><td>160.70 (n/a)</td><td>136.00 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>188.52 (n/a)</td><td>186.50 (n/a)</td><td>132.60 (n/a)</td><td>41.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>301.90 (n/a)</td><td>215.22 (n/a)</td><td>221.00 (n/a)</td><td>157.60 (n/a)</td><td>56.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>354.70 (n/a)</td><td>207.70 (n/a)</td><td>178.30 (n/a)</td><td>130.00 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>154.86 (n/a)</td><td>159.40 (n/a)</td><td>122.00 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.20 (n/a)</td><td>178.64 (n/a)</td><td>153.80 (n/a)</td><td>148.20 (n/a)</td><td>46.60 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.70 (n/a)</td><td>221.48 (n/a)</td><td>191.00 (n/a)</td><td>158.70 (n/a)</td><td>87.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>159.94 (n/a)</td><td>149.90 (n/a)</td><td>134.00 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>190.52 (n/a)</td><td>183.90 (n/a)</td><td>156.10 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>189.06 (n/a)</td><td>182.20 (n/a)</td><td>124.40 (n/a)</td><td>46.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.40 (n/a)</td><td>224.94 (n/a)</td><td>219.30 (n/a)</td><td>176.60 (n/a)</td><td>49.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>175.10 (n/a)</td><td>180.90 (n/a)</td><td>122.90 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.70 (n/a)</td><td>159.30 (n/a)</td><td>149.20 (n/a)</td><td>132.00 (n/a)</td><td>24.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.80 (n/a)</td><td>188.48 (n/a)</td><td>194.20 (n/a)</td><td>135.30 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>309.30 (n/a)</td><td>215.76 (n/a)</td><td>222.20 (n/a)</td><td>151.00 (n/a)</td><td>62.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>204.80 (n/a)</td><td>165.90 (n/a)</td><td>174.40 (n/a)</td><td>109.10 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>289.20 (n/a)</td><td>207.34 (n/a)</td><td>191.00 (n/a)</td><td>136.10 (n/a)</td><td>58.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>223.80 (n/a)</td><td>192.48 (n/a)</td><td>185.00 (n/a)</td><td>148.50 (n/a)</td><td>31.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.90 (n/a)</td><td>218.94 (n/a)</td><td>226.60 (n/a)</td><td>175.10 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>189.56 (n/a)</td><td>190.30 (n/a)</td><td>157.40 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>262.40 (n/a)</td><td>199.72 (n/a)</td><td>196.10 (n/a)</td><td>160.60 (n/a)</td><td>41.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.00 (n/a)</td><td>185.88 (n/a)</td><td>185.40 (n/a)</td><td>165.00 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>238.10 (n/a)</td><td>176.82 (n/a)</td><td>175.80 (n/a)</td><td>121.10 (n/a)</td><td>44.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.00 (n/a)</td><td>171.26 (n/a)</td><td>164.10 (n/a)</td><td>142.50 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.20 (n/a)</td><td>180.26 (n/a)</td><td>183.60 (n/a)</td><td>149.50 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>220.20 (n/a)</td><td>169.82 (n/a)</td><td>150.40 (n/a)</td><td>144.90 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>298.70 (n/a)</td><td>233.28 (n/a)</td><td>216.30 (n/a)</td><td>177.80 (n/a)</td><td>49.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 <b>(+31.11%)</b></td><td>0.03 (+5.92%)</td><td>0.02 (-8.16%)</td><td>0.02 (-18.22%)</td><td>0.01 <b>(+169.48%)</b></td><td>227.60 <b>(+22.30%)</b></td><td>167.84 (+1.65%)</td><td>191.00 (+8.89%)</td><td>102.90 <b>(-23.78%)</b></td><td>51.81 <b>(+148.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.10 (n/a)</td><td>165.12 (n/a)</td><td>175.40 (n/a)</td><td>135.00 (n/a)</td><td>20.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+15.27%)</td><td>0.02 (-1.24%)</td><td>0.02 (-10.23%)</td><td>0.02 (-9.56%)</td><td>0.01 <b>(+124.20%)</b></td><td>202.70 (+10.52%)</td><td>171.88 (+4.27%)</td><td>181.70 (+11.40%)</td><td>123.40 (-13.22%)</td><td>34.79 <b>(+119.68%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.40 (n/a)</td><td>164.84 (n/a)</td><td>163.10 (n/a)</td><td>142.20 (n/a)</td><td>15.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+19.66%)</td><td>0.03 (+18.99%)</td><td>0.03 (+19.37%)</td><td>0.02 <b>(+22.00%)</b></td><td>0.00 <b>(+34.15%)</b></td><td>175.60 (-18.06%)</td><td>146.74 (-15.67%)</td><td>146.00 (-16.24%)</td><td>123.10 (-16.43%)</td><td>23.64 (-9.92%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.30 (n/a)</td><td>174.00 (n/a)</td><td>174.30 (n/a)</td><td>147.30 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-13.36%)</td><td>0.02 (+7.79%)</td><td>0.02 (+10.57%)</td><td>0.02 <b>(+46.51%)</b></td><td>0.00 <b>(-49.82%)</b></td><td>218.10 <b>(-31.74%)</b></td><td>170.84 (-13.60%)</td><td>165.00 (-9.54%)</td><td>145.40 (+15.40%)</td><td>28.03 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>319.50 (n/a)</td><td>197.74 (n/a)</td><td>182.40 (n/a)</td><td>126.00 (n/a)</td><td>72.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+1.01%)</td><td>0.02 (-5.54%)</td><td>0.02 (-10.56%)</td><td>0.02 (+3.38%)</td><td>0.01 (-5.51%)</td><td>237.70 (-3.26%)</td><td>177.56 (+5.11%)</td><td>165.30 (+11.76%)</td><td>128.30 (-1.00%)</td><td>44.96 (-7.57%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.70 (n/a)</td><td>168.92 (n/a)</td><td>147.90 (n/a)</td><td>129.60 (n/a)</td><td>48.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+13.17%)</td><td>0.02 (+2.20%)</td><td>0.02 (-6.78%)</td><td>0.02 (+4.22%)</td><td>0.00 <b>(+31.85%)</b></td><td>215.80 (-4.05%)</td><td>174.58 (-1.39%)</td><td>179.70 (+7.28%)</td><td>138.50 (-11.67%)</td><td>31.03 (+9.85%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.90 (n/a)</td><td>177.04 (n/a)</td><td>167.50 (n/a)</td><td>156.80 (n/a)</td><td>28.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+5.36%)</td><td>0.02 (+11.35%)</td><td>0.02 (+0.05%)</td><td>0.02 <b>(+57.52%)</b></td><td>0.00 <b>(-44.51%)</b></td><td>194.60 <b>(-36.51%)</b></td><td>180.14 (-14.27%)</td><td>186.80 (-0.05%)</td><td>146.60 (-5.11%)</td><td>19.36 <b>(-67.81%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>306.50 (n/a)</td><td>210.12 (n/a)</td><td>186.90 (n/a)</td><td>154.50 (n/a)</td><td>60.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-1.50%)</td><td>0.02 (+0.05%)</td><td>0.02 (-8.52%)</td><td>0.02 (+1.90%)</td><td>0.00 (-3.17%)</td><td>215.50 (-1.87%)</td><td>191.20 (-0.20%)</td><td>203.70 (+9.34%)</td><td>160.00 (+1.52%)</td><td>25.66 (-6.68%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>191.58 (n/a)</td><td>186.30 (n/a)</td><td>157.60 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (+2.47%)</td><td>0.05 (-1.23%)</td><td>0.05 (-12.99%)</td><td>0.04 (+7.45%)</td><td>0.01 (-3.88%)</td><td>187.40 (-6.95%)</td><td>158.76 (+0.76%)</td><td>165.00 (+14.98%)</td><td>124.20 (-2.44%)</td><td>27.01 (-13.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>157.56 (n/a)</td><td>143.50 (n/a)</td><td>127.30 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (+16.32%)</td><td>0.06 (+16.30%)</td><td>0.06 <b>(+23.39%)</b></td><td>0.04 (+10.88%)</td><td>0.01 <b>(+51.38%)</b></td><td>183.60 (-9.78%)</td><td>152.30 (-13.10%)</td><td>145.60 (-18.98%)</td><td>123.80 (-14.03%)</td><td>26.25 <b>(+20.78%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>175.26 (n/a)</td><td>179.70 (n/a)</td><td>144.00 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-4.79%)</td><td>0.05 (-13.66%)</td><td>0.05 (-18.55%)</td><td>0.03 <b>(-32.42%)</b></td><td>0.01 <b>(+53.44%)</b></td><td>245.80 <b>(+47.98%)</b></td><td>174.22 (+19.90%)</td><td>175.60 <b>(+22.80%)</b></td><td>131.60 (+5.11%)</td><td>45.02 <b>(+135.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.10 (n/a)</td><td>145.30 (n/a)</td><td>143.00 (n/a)</td><td>125.20 (n/a)</td><td>19.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (+5.62%)</td><td>0.05 (-9.49%)</td><td>0.04 (-19.29%)</td><td>0.04 (-16.60%)</td><td>0.01 <b>(+42.42%)</b></td><td>229.90 (+19.93%)</td><td>182.38 (+13.93%)</td><td>188.10 <b>(+23.91%)</b></td><td>124.00 (-5.34%)</td><td>45.82 <b>(+61.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>160.08 (n/a)</td><td>151.80 (n/a)</td><td>131.00 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(+20.59%)</b></td><td>0.05 (+12.55%)</td><td>0.05 (+0.66%)</td><td>0.04 (+4.38%)</td><td>0.01 <b>(+104.70%)</b></td><td>205.50 (-4.20%)</td><td>165.14 (-8.37%)</td><td>180.30 (-0.66%)</td><td>122.80 (-17.03%)</td><td>37.56 <b>(+58.45%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>180.22 (n/a)</td><td>181.50 (n/a)</td><td>148.00 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+13.70%)</td><td>0.05 (+15.20%)</td><td>0.05 <b>(+20.80%)</b></td><td>0.04 (+2.54%)</td><td>0.01 <b>(+33.14%)</b></td><td>231.90 (-2.48%)</td><td>173.46 (-12.37%)</td><td>166.10 (-17.24%)</td><td>147.90 (-12.02%)</td><td>34.31 (+17.87%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>197.94 (n/a)</td><td>200.70 (n/a)</td><td>168.10 (n/a)</td><td>29.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+12.66%)</td><td>0.05 (+9.73%)</td><td>0.05 (+11.01%)</td><td>0.04 (+3.02%)</td><td>0.01 <b>(+76.65%)</b></td><td>185.40 (-2.93%)</td><td>166.62 (-8.39%)</td><td>170.70 (-9.92%)</td><td>147.80 (-11.28%)</td><td>17.01 <b>(+49.43%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.00 (n/a)</td><td>181.88 (n/a)</td><td>189.50 (n/a)</td><td>166.60 (n/a)</td><td>11.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(+22.15%)</b></td><td>0.05 (+12.36%)</td><td>0.05 (+13.99%)</td><td>0.04 (-0.69%)</td><td>0.01 <b>(+270.52%)</b></td><td>202.50 (+0.70%)</td><td>173.18 (-9.42%)</td><td>168.80 (-12.27%)</td><td>145.30 (-18.14%)</td><td>27.00 <b>(+211.54%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>191.18 (n/a)</td><td>192.40 (n/a)</td><td>177.50 (n/a)</td><td>8.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (+4.44%)</td><td>0.04 (-7.48%)</td><td>0.04 (-13.69%)</td><td>0.04 (-7.32%)</td><td>0.01 <b>(+45.30%)</b></td><td>210.90 (+7.88%)</td><td>193.14 (+8.87%)</td><td>199.60 (+15.84%)</td><td>153.10 (-4.19%)</td><td>23.24 <b>(+45.01%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>177.40 (n/a)</td><td>172.30 (n/a)</td><td>159.80 (n/a)</td><td>16.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-5.57%)</td><td>0.04 (+3.58%)</td><td>0.04 (+1.50%)</td><td>0.04 (+14.65%)</td><td>0.00 <b>(-50.30%)</b></td><td>224.60 (-12.81%)</td><td>201.48 (-4.60%)</td><td>198.40 (-1.49%)</td><td>189.60 (+5.86%)</td><td>13.76 <b>(-54.26%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.60 (n/a)</td><td>211.20 (n/a)</td><td>201.40 (n/a)</td><td>179.10 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-8.67%)</td><td>0.10 (-1.54%)</td><td>0.09 (-5.28%)</td><td>0.08 (-4.22%)</td><td>0.02 (-11.78%)</td><td>205.80 (+4.41%)</td><td>170.70 (+1.21%)</td><td>182.00 (+5.57%)</td><td>133.70 (+9.50%)</td><td>30.30 (-0.61%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>197.10 (n/a)</td><td>168.66 (n/a)</td><td>172.40 (n/a)</td><td>122.10 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-4.36%)</td><td>0.09 (-5.45%)</td><td>0.09 (+2.99%)</td><td>0.07 (-7.60%)</td><td>0.02 (+1.04%)</td><td>224.80 (+8.23%)</td><td>179.38 (+6.36%)</td><td>176.70 (-2.91%)</td><td>135.60 (+4.63%)</td><td>37.53 (+16.88%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>168.66 (n/a)</td><td>182.00 (n/a)</td><td>129.60 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (+12.24%)</td><td>0.10 (+4.13%)</td><td>0.09 (+2.63%)</td><td>0.08 (+11.83%)</td><td>0.02 (+7.73%)</td><td>201.70 (-10.59%)</td><td>172.18 (-4.12%)</td><td>174.90 (-2.56%)</td><td>135.80 (-10.89%)</td><td>24.84 (-14.96%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>179.58 (n/a)</td><td>179.50 (n/a)</td><td>152.40 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-1.27%)</td><td>0.09 (-5.79%)</td><td>0.09 (-7.85%)</td><td>0.08 (-10.91%)</td><td>0.01 (+18.06%)</td><td>216.10 (+12.26%)</td><td>182.66 (+6.69%)</td><td>180.80 (+8.52%)</td><td>148.10 (+1.30%)</td><td>24.53 <b>(+31.70%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>171.20 (n/a)</td><td>166.60 (n/a)</td><td>146.20 (n/a)</td><td>18.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (+16.51%)</td><td>0.11 (+6.47%)</td><td>0.11 (+17.35%)</td><td>0.08 (-13.84%)</td><td>0.02 <b>(+97.88%)</b></td><td>209.60 (+16.06%)</td><td>157.94 (-3.62%)</td><td>144.20 (-14.78%)</td><td>123.80 (-14.15%)</td><td>34.19 <b>(+100.22%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.60 (n/a)</td><td>163.88 (n/a)</td><td>169.20 (n/a)</td><td>144.20 (n/a)</td><td>17.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-1.49%)</td><td>0.09 (+2.50%)</td><td>0.09 (-3.55%)</td><td>0.08 (+17.05%)</td><td>0.01 <b>(-27.49%)</b></td><td>201.20 (-14.56%)</td><td>177.24 (-3.81%)</td><td>174.60 (+3.68%)</td><td>154.00 (+1.52%)</td><td>21.93 <b>(-36.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.50 (n/a)</td><td>184.26 (n/a)</td><td>168.40 (n/a)</td><td>151.70 (n/a)</td><td>34.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (+10.06%)</td><td>0.09 (+2.56%)</td><td>0.08 (-12.00%)</td><td>0.08 (+17.18%)</td><td>0.01 <b>(-20.22%)</b></td><td>215.60 (-14.65%)</td><td>191.42 (-3.82%)</td><td>199.70 (+13.66%)</td><td>154.20 (-9.19%)</td><td>23.57 <b>(-37.93%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>199.02 (n/a)</td><td>175.70 (n/a)</td><td>169.80 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (+11.96%)</td><td>0.08 (+2.55%)</td><td>0.07 (-2.01%)</td><td>0.07 (-4.53%)</td><td>0.01 <b>(+117.41%)</b></td><td>231.10 (+4.76%)</td><td>207.98 (-1.29%)</td><td>221.50 (+2.03%)</td><td>167.40 (-10.72%)</td><td>27.93 <b>(+108.06%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>210.70 (n/a)</td><td>217.10 (n/a)</td><td>187.50 (n/a)</td><td>13.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-4.24%)</td><td>0.19 (-4.20%)</td><td>0.20 (+7.12%)</td><td>0.15 (-10.08%)</td><td>0.03 (+15.20%)</td><td>213.90 (+11.17%)</td><td>178.18 (+5.10%)</td><td>163.50 (-6.62%)</td><td>152.90 (+4.44%)</td><td>27.83 <b>(+36.05%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>169.54 (n/a)</td><td>175.10 (n/a)</td><td>146.40 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (+17.90%)</td><td>0.20 (-1.23%)</td><td>0.18 (-10.52%)</td><td>0.17 (+3.92%)</td><td>0.04 <b>(+58.40%)</b></td><td>194.90 (-3.80%)</td><td>171.78 (+2.57%)</td><td>180.20 (+11.72%)</td><td>123.60 (-15.17%)</td><td>28.16 <b>(+24.53%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>167.48 (n/a)</td><td>161.30 (n/a)</td><td>145.70 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (-11.74%)</td><td>0.19 (-12.67%)</td><td>0.20 (-12.20%)</td><td>0.16 (-16.74%)</td><td>0.03 <b>(+23.54%)</b></td><td>208.60 <b>(+20.09%)</b></td><td>175.60 (+15.83%)</td><td>167.20 (+13.90%)</td><td>145.90 (+13.36%)</td><td>29.12 <b>(+70.24%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>173.70 (n/a)</td><td>151.60 (n/a)</td><td>146.80 (n/a)</td><td>128.70 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(+25.61%)</b></td><td>0.21 (+15.75%)</td><td>0.20 (+12.88%)</td><td>0.15 (+8.53%)</td><td>0.05 <b>(+53.94%)</b></td><td>215.70 (-7.82%)</td><td>160.44 (-12.21%)</td><td>160.70 (-11.41%)</td><td>115.90 <b>(-20.34%)</b></td><td>36.02 (+11.47%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>234.00 (n/a)</td><td>182.76 (n/a)</td><td>181.40 (n/a)</td><td>145.50 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (+9.46%)</td><td>0.18 (+3.89%)</td><td>0.18 (-1.32%)</td><td>0.14 (+6.84%)</td><td>0.04 <b>(+39.53%)</b></td><td>233.60 (-6.41%)</td><td>189.22 (-2.41%)</td><td>187.10 (+1.30%)</td><td>146.60 (-8.60%)</td><td>39.77 (+16.75%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>249.60 (n/a)</td><td>193.90 (n/a)</td><td>184.70 (n/a)</td><td>160.40 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (+14.23%)</td><td>0.20 (+16.32%)</td><td>0.20 (+19.18%)</td><td>0.17 (+12.44%)</td><td>0.02 <b>(+36.43%)</b></td><td>189.30 (-11.04%)</td><td>169.40 (-13.82%)</td><td>164.70 (-16.10%)</td><td>153.10 (-12.46%)</td><td>17.27 (+5.02%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>196.56 (n/a)</td><td>196.30 (n/a)</td><td>174.90 (n/a)</td><td>16.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (+2.86%)</td><td>0.16 (+7.73%)</td><td>0.17 (+12.74%)</td><td>0.14 (+1.53%)</td><td>0.02 (-3.52%)</td><td>239.70 (-1.52%)</td><td>202.02 (-7.28%)</td><td>193.90 (-11.30%)</td><td>180.10 (-2.75%)</td><td>22.66 (-6.58%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>243.40 (n/a)</td><td>217.88 (n/a)</td><td>218.60 (n/a)</td><td>185.20 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+9.73%)</td><td>0.03 (+0.65%)</td><td>0.03 (+4.07%)</td><td>0.02 (-7.08%)</td><td>0.00 <b>(+171.38%)</b></td><td>176.30 (+7.63%)</td><td>156.08 (+0.48%)</td><td>150.60 (-3.89%)</td><td>131.40 (-8.88%)</td><td>19.61 <b>(+176.13%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>163.80 (n/a)</td><td>155.34 (n/a)</td><td>156.70 (n/a)</td><td>144.20 (n/a)</td><td>7.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+15.57%)</td><td>0.03 (+6.55%)</td><td>0.03 (+4.98%)</td><td>0.02 (+9.46%)</td><td>0.00 <b>(+27.28%)</b></td><td>177.50 (-8.65%)</td><td>147.48 (-5.84%)</td><td>139.50 (-4.78%)</td><td>123.60 (-13.51%)</td><td>21.44 (+0.08%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.30 (n/a)</td><td>156.62 (n/a)</td><td>146.50 (n/a)</td><td>142.90 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 <b>(-27.05%)</b></td><td>0.02 (-0.63%)</td><td>0.02 (+2.39%)</td><td>0.02 <b>(+69.04%)</b></td><td>0.00 <b>(-74.94%)</b></td><td>226.70 <b>(-40.84%)</b></td><td>198.74 (-9.97%)</td><td>188.80 (-2.33%)</td><td>182.90 <b>(+37.11%)</b></td><td>18.17 <b>(-80.92%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>383.20 (n/a)</td><td>220.74 (n/a)</td><td>193.30 (n/a)</td><td>133.40 (n/a)</td><td>95.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+16.09%)</td><td>0.02 (+10.85%)</td><td>0.02 (+10.52%)</td><td>0.02 (+6.15%)</td><td>0.00 <b>(+53.23%)</b></td><td>203.20 (-5.80%)</td><td>179.60 (-9.47%)</td><td>181.20 (-9.49%)</td><td>156.20 (-13.84%)</td><td>17.03 <b>(+24.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>198.38 (n/a)</td><td>200.20 (n/a)</td><td>181.30 (n/a)</td><td>13.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-7.42%)</td><td>0.03 (-2.24%)</td><td>0.03 (+0.86%)</td><td>0.02 (-6.11%)</td><td>0.00 <b>(-21.07%)</b></td><td>195.40 (+6.49%)</td><td>154.72 (+1.19%)</td><td>152.70 (-0.84%)</td><td>118.20 (+8.04%)</td><td>27.53 (-11.17%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>152.90 (n/a)</td><td>154.00 (n/a)</td><td>109.40 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-6.79%)</td><td>0.02 (-10.03%)</td><td>0.02 (-11.61%)</td><td>0.02 <b>(-21.56%)</b></td><td>0.00 <b>(+46.72%)</b></td><td>224.50 <b>(+27.48%)</b></td><td>178.24 (+12.37%)</td><td>173.70 (+13.16%)</td><td>156.90 (+7.32%)</td><td>27.05 <b>(+104.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.10 (n/a)</td><td>158.62 (n/a)</td><td>153.50 (n/a)</td><td>146.20 (n/a)</td><td>13.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-12.60%)</td><td>0.02 (-12.32%)</td><td>0.02 (-3.99%)</td><td>0.02 (-14.94%)</td><td>0.00 (-9.90%)</td><td>230.10 (+17.58%)</td><td>200.90 (+14.21%)</td><td>196.30 (+4.14%)</td><td>163.50 (+14.42%)</td><td>27.60 <b>(+22.78%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.70 (n/a)</td><td>175.90 (n/a)</td><td>188.50 (n/a)</td><td>142.90 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-19.24%)</td><td>0.02 (-5.80%)</td><td>0.02 (+3.62%)</td><td>0.02 (+0.74%)</td><td>0.01 <b>(-25.37%)</b></td><td>225.20 (-0.75%)</td><td>177.02 (+4.68%)</td><td>163.90 (-3.53%)</td><td>137.20 <b>(+23.83%)</b></td><td>39.84 (-4.06%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>169.10 (n/a)</td><td>169.90 (n/a)</td><td>110.80 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-0.42%)</td><td>0.02 (-7.32%)</td><td>0.02 (-19.85%)</td><td>0.02 <b>(+30.65%)</b></td><td>0.01 (-12.39%)</td><td>219.60 <b>(-23.43%)</b></td><td>181.80 (+4.18%)</td><td>196.00 <b>(+24.76%)</b></td><td>123.60 (+0.41%)</td><td>40.70 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>174.50 (n/a)</td><td>157.10 (n/a)</td><td>123.10 (n/a)</td><td>64.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-3.93%)</td><td>0.02 (-6.33%)</td><td>0.02 (-7.46%)</td><td>0.02 (-7.74%)</td><td>0.01 (-11.26%)</td><td>229.90 (+8.39%)</td><td>177.42 (+5.91%)</td><td>182.30 (+8.00%)</td><td>122.30 (+4.09%)</td><td>39.35 (-3.69%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>167.52 (n/a)</td><td>168.80 (n/a)</td><td>117.50 (n/a)</td><td>40.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-15.75%)</td><td>0.02 (-2.05%)</td><td>0.02 (-7.58%)</td><td>0.02 <b>(+55.48%)</b></td><td>0.00 <b>(-46.87%)</b></td><td>229.80 <b>(-35.70%)</b></td><td>197.74 (-6.27%)</td><td>202.70 (+8.22%)</td><td>150.40 (+18.71%)</td><td>33.61 <b>(-61.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>357.40 (n/a)</td><td>210.96 (n/a)</td><td>187.30 (n/a)</td><td>126.70 (n/a)</td><td>86.51 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-15.40%)</td><td>0.02 <b>(-20.87%)</b></td><td>0.02 <b>(-29.95%)</b></td><td>0.02 (-16.30%)</td><td>0.01 (-2.26%)</td><td>256.60 (+19.46%)</td><td>206.30 <b>(+28.07%)</b></td><td>224.60 <b>(+42.78%)</b></td><td>147.30 (+18.22%)</td><td>49.93 <b>(+37.92%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>161.08 (n/a)</td><td>157.30 (n/a)</td><td>124.60 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-11.99%)</td><td>0.02 (-10.23%)</td><td>0.02 (+0.26%)</td><td>0.02 (-14.79%)</td><td>0.00 (-7.66%)</td><td>227.60 (+17.38%)</td><td>192.96 (+11.74%)</td><td>182.90 (-0.27%)</td><td>152.40 (+13.65%)</td><td>32.02 <b>(+25.87%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>172.68 (n/a)</td><td>183.40 (n/a)</td><td>134.10 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-3.13%)</td><td>0.02 (-7.38%)</td><td>0.02 (-5.29%)</td><td>0.02 <b>(-21.31%)</b></td><td>0.00 <b>(+44.50%)</b></td><td>258.90 <b>(+27.04%)</b></td><td>200.42 (+9.56%)</td><td>189.50 (+5.57%)</td><td>163.30 (+3.22%)</td><td>35.88 <b>(+92.22%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>182.94 (n/a)</td><td>179.50 (n/a)</td><td>158.20 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-13.68%)</td><td>0.02 (-8.89%)</td><td>0.02 (-12.87%)</td><td>0.02 (-10.16%)</td><td>0.00 <b>(-28.36%)</b></td><td>239.70 (+11.28%)</td><td>198.12 (+8.81%)</td><td>195.20 (+14.82%)</td><td>167.40 (+15.85%)</td><td>28.08 (-11.07%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.40 (n/a)</td><td>182.08 (n/a)</td><td>170.00 (n/a)</td><td>144.50 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-6.00%)</td><td>0.02 (+3.57%)</td><td>0.02 (+1.73%)</td><td>0.02 <b>(+21.63%)</b></td><td>0.00 <b>(-49.04%)</b></td><td>192.50 (-17.77%)</td><td>175.00 (-5.31%)</td><td>179.10 (-1.70%)</td><td>153.40 (+6.38%)</td><td>14.60 <b>(-55.99%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.10 (n/a)</td><td>184.82 (n/a)</td><td>182.20 (n/a)</td><td>144.20 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-7.85%)</td><td>0.05 (+4.98%)</td><td>0.05 (+2.74%)</td><td>0.05 <b>(+27.35%)</b></td><td>0.01 <b>(-44.50%)</b></td><td>175.50 <b>(-21.44%)</b></td><td>162.54 (-6.97%)</td><td>173.60 (-2.64%)</td><td>142.00 (+8.56%)</td><td>16.87 <b>(-51.93%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>174.72 (n/a)</td><td>178.30 (n/a)</td><td>130.80 (n/a)</td><td>35.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-1.49%)</td><td>0.05 (+1.32%)</td><td>0.05 (+0.43%)</td><td>0.04 (+6.83%)</td><td>0.01 (-15.61%)</td><td>198.20 (-6.42%)</td><td>166.68 (-1.93%)</td><td>166.80 (-0.42%)</td><td>138.10 (+1.47%)</td><td>21.48 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>169.96 (n/a)</td><td>167.50 (n/a)</td><td>136.10 (n/a)</td><td>27.05 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 <b>(+22.94%)</b></td><td>0.04 <b>(+21.70%)</b></td><td>0.05 <b>(+25.95%)</b></td><td>0.04 (+15.26%)</td><td>0.00 <b>(+83.98%)</b></td><td>225.20 (-13.22%)</td><td>192.96 (-17.42%)</td><td>180.90 <b>(-20.62%)</b></td><td>175.70 (-18.66%)</td><td>20.95 <b>(+28.55%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>259.50 (n/a)</td><td>233.66 (n/a)</td><td>227.90 (n/a)</td><td>216.00 (n/a)</td><td>16.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-8.78%)</td><td>0.05 (+4.17%)</td><td>0.05 (+11.79%)</td><td>0.04 (+8.78%)</td><td>0.01 <b>(-32.27%)</b></td><td>215.50 (-8.10%)</td><td>180.62 (-5.72%)</td><td>180.00 (-10.54%)</td><td>151.40 (+9.63%)</td><td>25.86 <b>(-31.18%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>191.58 (n/a)</td><td>201.20 (n/a)</td><td>138.10 (n/a)</td><td>37.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (+7.60%)</td><td>0.06 (+2.50%)</td><td>0.05 (-1.66%)</td><td>0.04 (-6.25%)</td><td>0.01 <b>(+60.17%)</b></td><td>193.70 (+6.66%)</td><td>153.30 (+0.41%)</td><td>158.40 (+1.67%)</td><td>114.90 (-7.11%)</td><td>36.86 <b>(+54.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.60 (n/a)</td><td>152.68 (n/a)</td><td>155.80 (n/a)</td><td>123.70 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(+29.58%)</b></td><td>0.05 (+6.86%)</td><td>0.05 (-0.83%)</td><td>0.05 (-5.44%)</td><td>0.01 <b>(+305.42%)</b></td><td>180.70 (+5.73%)</td><td>154.92 (-3.96%)</td><td>161.60 (+0.87%)</td><td>115.60 <b>(-22.83%)</b></td><td>27.51 <b>(+233.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>170.90 (n/a)</td><td>161.30 (n/a)</td><td>160.20 (n/a)</td><td>149.80 (n/a)</td><td>8.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-5.93%)</td><td>0.05 (-0.66%)</td><td>0.06 (-2.73%)</td><td>0.04 (-4.40%)</td><td>0.01 (-10.77%)</td><td>209.20 (+4.60%)</td><td>154.38 (+0.21%)</td><td>145.30 (+2.76%)</td><td>122.70 (+6.33%)</td><td>34.09 (-1.09%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>154.06 (n/a)</td><td>141.40 (n/a)</td><td>115.40 (n/a)</td><td>34.47 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-4.87%)</td><td>0.05 (-2.90%)</td><td>0.05 (+2.15%)</td><td>0.04 (-0.09%)</td><td>0.01 (-6.29%)</td><td>190.80 (+0.10%)</td><td>166.30 (+2.92%)</td><td>160.10 (-2.14%)</td><td>135.90 (+5.10%)</td><td>23.33 (+2.19%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>161.58 (n/a)</td><td>163.60 (n/a)</td><td>129.30 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-4.63%)</td><td>0.05 (-5.56%)</td><td>0.05 (+7.10%)</td><td>0.04 (-12.69%)</td><td>0.01 (-7.26%)</td><td>229.80 (+14.56%)</td><td>181.76 (+6.01%)</td><td>173.10 (-6.63%)</td><td>142.50 (+4.86%)</td><td>33.70 (+13.35%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>171.46 (n/a)</td><td>185.40 (n/a)</td><td>135.90 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-17.94%)</td><td>0.04 (-14.00%)</td><td>0.04 (-16.59%)</td><td>0.04 (+4.09%)</td><td>0.01 <b>(-42.29%)</b></td><td>212.00 (-3.90%)</td><td>186.26 (+12.94%)</td><td>203.10 (+19.89%)</td><td>146.30 <b>(+21.82%)</b></td><td>28.37 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>164.92 (n/a)</td><td>169.40 (n/a)</td><td>120.10 (n/a)</td><td>40.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-15.52%)</td><td>0.05 (-14.31%)</td><td>0.05 (-16.54%)</td><td>0.04 (+8.12%)</td><td>0.00 <b>(-50.89%)</b></td><td>210.60 (-7.51%)</td><td>180.80 (+13.57%)</td><td>174.20 (+19.89%)</td><td>161.30 (+18.34%)</td><td>20.27 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>159.20 (n/a)</td><td>145.30 (n/a)</td><td>136.30 (n/a)</td><td>38.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+12.79%)</td><td>0.05 (-3.36%)</td><td>0.05 (-11.15%)</td><td>0.04 (-12.43%)</td><td>0.01 <b>(+48.10%)</b></td><td>229.60 (+14.23%)</td><td>178.50 (+5.27%)</td><td>178.40 (+12.56%)</td><td>132.20 (-11.33%)</td><td>35.24 <b>(+49.80%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>169.56 (n/a)</td><td>158.50 (n/a)</td><td>149.10 (n/a)</td><td>23.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(+22.47%)</b></td><td>0.04 (+11.28%)</td><td>0.04 (+2.89%)</td><td>0.04 (+5.02%)</td><td>0.01 <b>(+86.75%)</b></td><td>228.10 (-4.80%)</td><td>192.18 (-8.40%)</td><td>203.80 (-2.81%)</td><td>146.40 (-18.35%)</td><td>36.15 <b>(+45.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>239.60 (n/a)</td><td>209.80 (n/a)</td><td>209.70 (n/a)</td><td>179.30 (n/a)</td><td>24.87 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-12.26%)</td><td>0.04 (-19.58%)</td><td>0.04 (-15.37%)</td><td>0.03 <b>(-34.09%)</b></td><td>0.01 <b>(+54.04%)</b></td><td>273.80 <b>(+51.69%)</b></td><td>201.96 <b>(+27.18%)</b></td><td>188.40 (+18.12%)</td><td>162.50 (+13.96%)</td><td>42.19 <b>(+179.47%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>180.50 (n/a)</td><td>158.80 (n/a)</td><td>159.50 (n/a)</td><td>142.60 (n/a)</td><td>15.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(-24.39%)</b></td><td>0.05 (-11.01%)</td><td>0.05 (-7.13%)</td><td>0.03 (-6.64%)</td><td>0.01 <b>(-26.10%)</b></td><td>261.80 (+7.12%)</td><td>182.88 (+10.53%)</td><td>170.30 (+7.72%)</td><td>136.20 <b>(+32.23%)</b></td><td>52.69 (+2.03%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>244.40 (n/a)</td><td>165.46 (n/a)</td><td>158.10 (n/a)</td><td>103.00 (n/a)</td><td>51.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 <b>(-20.32%)</b></td><td>0.05 (-14.12%)</td><td>0.05 (-15.21%)</td><td>0.04 (-10.92%)</td><td>0.00 <b>(-46.67%)</b></td><td>195.10 (+12.26%)</td><td>168.62 (+15.05%)</td><td>170.50 (+17.99%)</td><td>149.20 <b>(+25.48%)</b></td><td>17.38 <b>(-25.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>146.56 (n/a)</td><td>144.50 (n/a)</td><td>118.90 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (+4.84%)</td><td>0.10 (+7.05%)</td><td>0.11 (+16.36%)</td><td>0.07 (-9.82%)</td><td>0.02 <b>(+68.20%)</b></td><td>220.60 (+10.91%)</td><td>168.06 (-5.10%)</td><td>151.30 (-14.08%)</td><td>146.90 (-4.61%)</td><td>31.27 <b>(+77.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>177.10 (n/a)</td><td>176.10 (n/a)</td><td>154.00 (n/a)</td><td>17.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 <b>(+23.28%)</b></td><td>0.11 (+16.24%)</td><td>0.12 <b>(+28.73%)</b></td><td>0.08 (-1.20%)</td><td>0.02 <b>(+102.48%)</b></td><td>208.40 (+1.21%)</td><td>154.36 (-11.48%)</td><td>139.10 <b>(-22.33%)</b></td><td>124.10 (-18.89%)</td><td>36.56 <b>(+66.46%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>174.38 (n/a)</td><td>179.10 (n/a)</td><td>153.00 (n/a)</td><td>21.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (-19.71%)</td><td>0.07 <b>(-20.48%)</b></td><td>0.08 (-18.16%)</td><td>0.06 <b>(-26.78%)</b></td><td>0.01 (-4.84%)</td><td>289.60 <b>(+36.54%)</b></td><td>226.48 <b>(+26.75%)</b></td><td>215.00 <b>(+22.23%)</b></td><td>188.40 <b>(+24.60%)</b></td><td>39.36 <b>(+64.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>178.68 (n/a)</td><td>175.90 (n/a)</td><td>151.20 (n/a)</td><td>23.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (-18.05%)</td><td>0.07 (-17.07%)</td><td>0.07 (-14.32%)</td><td>0.06 (-15.53%)</td><td>0.01 (-12.28%)</td><td>267.30 (+18.38%)</td><td>228.00 <b>(+20.85%)</b></td><td>229.60 (+16.67%)</td><td>190.00 <b>(+22.03%)</b></td><td>36.26 <b>(+27.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>188.66 (n/a)</td><td>196.80 (n/a)</td><td>155.70 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 <b>(+34.08%)</b></td><td>0.11 (+9.20%)</td><td>0.09 (-8.78%)</td><td>0.08 (+2.35%)</td><td>0.03 <b>(+140.07%)</b></td><td>202.30 (-2.32%)</td><td>163.44 (-4.82%)</td><td>181.20 (+9.62%)</td><td>110.30 <b>(-25.42%)</b></td><td>38.52 <b>(+72.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>171.72 (n/a)</td><td>165.30 (n/a)</td><td>147.90 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-12.12%)</td><td>0.11 (+11.05%)</td><td>0.11 (+3.68%)</td><td>0.09 <b>(+128.27%)</b></td><td>0.01 <b>(-70.63%)</b></td><td>177.80 <b>(-56.19%)</b></td><td>154.66 <b>(-23.88%)</b></td><td>150.90 (-3.58%)</td><td>137.90 (+13.78%)</td><td>15.74 <b>(-86.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>405.80 (n/a)</td><td>203.18 (n/a)</td><td>156.50 (n/a)</td><td>121.20 (n/a)</td><td>115.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (+8.73%)</td><td>0.09 <b>(-20.94%)</b></td><td>0.09 <b>(-27.68%)</b></td><td>0.05 <b>(-39.32%)</b></td><td>0.04 <b>(+77.30%)</b></td><td>339.30 <b>(+64.79%)</b></td><td>219.88 <b>(+40.57%)</b></td><td>190.10 <b>(+38.25%)</b></td><td>118.60 (-8.06%)</td><td>88.84 <b>(+174.84%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.90 (n/a)</td><td>156.42 (n/a)</td><td>137.50 (n/a)</td><td>129.00 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (+14.05%)</td><td>0.12 (+3.11%)</td><td>0.11 (+1.47%)</td><td>0.09 (-12.61%)</td><td>0.02 <b>(+106.80%)</b></td><td>174.00 (+14.40%)</td><td>141.94 (-1.35%)</td><td>144.50 (-1.43%)</td><td>109.00 (-12.38%)</td><td>23.44 <b>(+106.07%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>152.10 (n/a)</td><td>143.88 (n/a)</td><td>146.60 (n/a)</td><td>124.40 (n/a)</td><td>11.37 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 <b>(-25.29%)</b></td><td>0.10 (-4.09%)</td><td>0.10 (-0.06%)</td><td>0.09 (+7.73%)</td><td>0.01 <b>(-61.32%)</b></td><td>186.20 (-7.18%)</td><td>162.34 (+1.00%)</td><td>158.90 (+0.06%)</td><td>147.70 <b>(+33.91%)</b></td><td>16.32 <b>(-50.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.60 (n/a)</td><td>160.74 (n/a)</td><td>158.80 (n/a)</td><td>110.30 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (+12.65%)</td><td>0.09 (-0.85%)</td><td>0.08 (-14.92%)</td><td>0.07 <b>(+54.07%)</b></td><td>0.02 <b>(-21.68%)</b></td><td>239.50 <b>(-35.09%)</b></td><td>191.46 (-6.28%)</td><td>196.90 (+17.55%)</td><td>133.80 (-11.27%)</td><td>37.91 <b>(-59.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>369.00 (n/a)</td><td>204.30 (n/a)</td><td>167.50 (n/a)</td><td>150.80 (n/a)</td><td>92.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-6.36%)</td><td>0.10 (-2.19%)</td><td>0.10 (-4.22%)</td><td>0.08 (-3.75%)</td><td>0.02 (-6.46%)</td><td>197.20 (+3.90%)</td><td>164.82 (+2.17%)</td><td>161.60 (+4.46%)</td><td>134.30 (+6.76%)</td><td>26.92 (+2.89%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.80 (n/a)</td><td>161.32 (n/a)</td><td>154.70 (n/a)</td><td>125.80 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-16.09%)</td><td>0.10 (-11.55%)</td><td>0.10 (-0.51%)</td><td>0.08 (-16.23%)</td><td>0.01 <b>(-40.68%)</b></td><td>210.90 (+19.35%)</td><td>171.58 (+11.68%)</td><td>166.30 (+0.54%)</td><td>147.80 (+19.19%)</td><td>23.41 (-12.57%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>153.64 (n/a)</td><td>165.40 (n/a)</td><td>124.00 (n/a)</td><td>26.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (-9.19%)</td><td>0.09 (-0.88%)</td><td>0.10 (-3.05%)</td><td>0.07 <b>(+24.82%)</b></td><td>0.01 <b>(-42.62%)</b></td><td>228.70 (-19.87%)</td><td>179.20 (-3.09%)</td><td>165.40 (+3.12%)</td><td>163.40 (+10.11%)</td><td>27.95 <b>(-50.87%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>285.40 (n/a)</td><td>184.92 (n/a)</td><td>160.40 (n/a)</td><td>148.40 (n/a)</td><td>56.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (+0.00%)</td><td>0.10 (-2.10%)</td><td>0.10 (-7.12%)</td><td>0.09 (+16.16%)</td><td>0.02 <b>(-24.94%)</b></td><td>183.50 (-13.93%)</td><td>160.50 (+0.19%)</td><td>165.70 (+7.67%)</td><td>124.20 (+0.00%)</td><td>22.63 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.20 (n/a)</td><td>160.20 (n/a)</td><td>153.90 (n/a)</td><td>124.20 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 <b>(+25.86%)</b></td><td>0.10 (+1.14%)</td><td>0.09 (-9.41%)</td><td>0.09 (-4.29%)</td><td>0.02 <b>(+163.42%)</b></td><td>192.60 (+4.50%)</td><td>168.64 (+1.22%)</td><td>180.50 (+10.40%)</td><td>120.30 <b>(-20.54%)</b></td><td>28.67 <b>(+112.12%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.30 (n/a)</td><td>166.60 (n/a)</td><td>163.50 (n/a)</td><td>151.40 (n/a)</td><td>13.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 <b>(+27.13%)</b></td><td>0.11 <b>(+21.13%)</b></td><td>0.11 (+14.59%)</td><td>0.10 <b>(+39.07%)</b></td><td>0.02 (+9.25%)</td><td>166.50 <b>(-28.08%)</b></td><td>147.86 (-18.04%)</td><td>152.90 (-12.78%)</td><td>119.40 <b>(-21.34%)</b></td><td>18.85 <b>(-39.45%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>180.40 (n/a)</td><td>175.30 (n/a)</td><td>151.80 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (+1.43%)</td><td>0.22 (+0.73%)</td><td>0.22 (-3.27%)</td><td>0.18 (+3.60%)</td><td>0.03 <b>(-20.98%)</b></td><td>183.80 (-3.47%)</td><td>151.38 (-2.03%)</td><td>148.10 (+3.42%)</td><td>124.30 (-1.43%)</td><td>23.91 <b>(-24.95%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>190.40 (n/a)</td><td>154.52 (n/a)</td><td>143.20 (n/a)</td><td>126.10 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (-10.57%)</td><td>0.21 (-5.59%)</td><td>0.20 (+2.67%)</td><td>0.18 (-3.53%)</td><td>0.04 <b>(-24.21%)</b></td><td>186.00 (+3.68%)</td><td>160.12 (+4.74%)</td><td>163.70 (-2.62%)</td><td>127.50 (+11.84%)</td><td>26.55 (-11.84%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>179.40 (n/a)</td><td>152.88 (n/a)</td><td>168.10 (n/a)</td><td>114.00 (n/a)</td><td>30.11 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (-7.38%)</td><td>0.17 (+7.51%)</td><td>0.18 (+19.12%)</td><td>0.16 (+16.80%)</td><td>0.01 <b>(-57.29%)</b></td><td>208.40 (-14.41%)</td><td>191.24 (-8.74%)</td><td>184.90 (-16.03%)</td><td>177.90 (+7.95%)</td><td>13.49 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>243.50 (n/a)</td><td>209.56 (n/a)</td><td>220.20 (n/a)</td><td>164.80 (n/a)</td><td>34.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (+0.57%)</td><td>0.17 (-0.38%)</td><td>0.17 (+5.13%)</td><td>0.15 (+1.41%)</td><td>0.02 (-16.65%)</td><td>218.50 (-1.40%)</td><td>195.30 (-0.09%)</td><td>197.00 (-4.88%)</td><td>163.90 (-0.55%)</td><td>21.91 (-17.31%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.60 (n/a)</td><td>195.48 (n/a)</td><td>207.10 (n/a)</td><td>164.80 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (-6.05%)</td><td>0.21 (-0.45%)</td><td>0.19 (-5.02%)</td><td>0.17 (+10.77%)</td><td>0.05 (-13.14%)</td><td>191.50 (-9.71%)</td><td>160.88 (-0.67%)</td><td>171.60 (+5.28%)</td><td>115.70 (+6.44%)</td><td>33.02 (-13.27%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>212.10 (n/a)</td><td>161.96 (n/a)</td><td>163.00 (n/a)</td><td>108.70 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (+10.31%)</td><td>0.22 (+6.06%)</td><td>0.22 (+8.30%)</td><td>0.16 (-11.24%)</td><td>0.05 <b>(+67.12%)</b></td><td>207.20 (+12.67%)</td><td>157.70 (-3.29%)</td><td>148.10 (-7.67%)</td><td>119.60 (-9.39%)</td><td>35.67 <b>(+71.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>183.90 (n/a)</td><td>163.06 (n/a)</td><td>160.40 (n/a)</td><td>132.00 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (-11.79%)</td><td>0.20 (-1.60%)</td><td>0.18 (-10.02%)</td><td>0.17 (+15.77%)</td><td>0.04 <b>(-23.51%)</b></td><td>196.40 (-13.63%)</td><td>167.50 (-0.40%)</td><td>183.50 (+11.14%)</td><td>129.70 (+13.37%)</td><td>31.32 <b>(-24.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>227.40 (n/a)</td><td>168.18 (n/a)</td><td>165.10 (n/a)</td><td>114.40 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (-8.13%)</td><td>0.21 (-3.71%)</td><td>0.22 (-1.94%)</td><td>0.16 (+5.76%)</td><td>0.04 (-19.83%)</td><td>199.80 (-5.44%)</td><td>159.60 (+2.37%)</td><td>148.30 (+1.99%)</td><td>123.40 (+8.82%)</td><td>31.04 (-17.06%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>211.30 (n/a)</td><td>155.90 (n/a)</td><td>145.40 (n/a)</td><td>113.40 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (-1.37%)</td><td>0.21 (+5.60%)</td><td>0.19 (+10.01%)</td><td>0.17 <b>(+24.42%)</b></td><td>0.04 <b>(-27.68%)</b></td><td>188.80 (-19.66%)</td><td>160.82 (-9.01%)</td><td>174.50 (-9.07%)</td><td>117.40 (+1.38%)</td><td>30.24 <b>(-39.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>235.00 (n/a)</td><td>176.74 (n/a)</td><td>191.90 (n/a)</td><td>115.80 (n/a)</td><td>50.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 <b>(-23.78%)</b></td><td>0.21 (-12.16%)</td><td>0.21 (-12.60%)</td><td>0.17 (+0.81%)</td><td>0.03 <b>(-56.92%)</b></td><td>193.30 (-0.82%)</td><td>158.60 (+9.45%)</td><td>152.60 (+14.48%)</td><td>140.90 <b>(+31.19%)</b></td><td>21.23 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>194.90 (n/a)</td><td>144.90 (n/a)</td><td>133.30 (n/a)</td><td>107.40 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 <b>(-20.29%)</b></td><td>0.20 (-5.26%)</td><td>0.19 (-4.44%)</td><td>0.18 (+18.54%)</td><td>0.02 <b>(-61.68%)</b></td><td>186.90 (-15.66%)</td><td>167.88 (+2.20%)</td><td>171.20 (+4.65%)</td><td>151.50 <b>(+25.41%)</b></td><td>14.55 <b>(-60.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.60 (n/a)</td><td>164.26 (n/a)</td><td>163.60 (n/a)</td><td>120.80 (n/a)</td><td>36.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-5.98%)</td><td>0.19 (-3.94%)</td><td>0.19 (+2.02%)</td><td>0.15 (-6.95%)</td><td>0.02 (-7.38%)</td><td>218.20 (+7.49%)</td><td>177.88 (+4.12%)</td><td>171.80 (-2.00%)</td><td>156.10 (+6.41%)</td><td>24.24 (+8.73%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.00 (n/a)</td><td>170.84 (n/a)</td><td>175.30 (n/a)</td><td>146.70 (n/a)</td><td>22.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (-6.68%)</td><td>0.17 (-8.96%)</td><td>0.17 (-7.46%)</td><td>0.13 (-11.46%)</td><td>0.03 (+7.72%)</td><td>247.80 (+12.94%)</td><td>197.40 (+10.58%)</td><td>191.00 (+8.03%)</td><td>164.50 (+7.17%)</td><td>34.87 <b>(+30.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.40 (n/a)</td><td>178.52 (n/a)</td><td>176.80 (n/a)</td><td>153.50 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (+12.85%)</td><td>0.18 (+0.61%)</td><td>0.18 (-1.24%)</td><td>0.13 (-11.51%)</td><td>0.03 <b>(+76.47%)</b></td><td>242.90 (+13.03%)</td><td>190.34 (+1.02%)</td><td>185.70 (+1.25%)</td><td>149.30 (-11.34%)</td><td>33.56 <b>(+78.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>188.42 (n/a)</td><td>183.40 (n/a)</td><td>168.40 (n/a)</td><td>18.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-18.69%)</td><td>0.18 (+5.02%)</td><td>0.18 (+12.22%)</td><td>0.17 <b>(+68.86%)</b></td><td>0.02 <b>(-72.69%)</b></td><td>195.90 <b>(-40.76%)</b></td><td>181.96 (-13.54%)</td><td>185.40 (-10.87%)</td><td>157.20 <b>(+23.00%)</b></td><td>15.27 <b>(-80.31%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>330.70 (n/a)</td><td>210.46 (n/a)</td><td>208.00 (n/a)</td><td>127.80 (n/a)</td><td>77.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-12.29%)</td><td>0.18 (-3.70%)</td><td>0.19 (-0.65%)</td><td>0.15 (+0.73%)</td><td>0.02 <b>(-27.58%)</b></td><td>221.40 (-0.72%)</td><td>184.74 (+2.83%)</td><td>172.20 (+0.70%)</td><td>158.80 (+14.00%)</td><td>26.09 (-17.74%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.00 (n/a)</td><td>179.66 (n/a)</td><td>171.00 (n/a)</td><td>139.30 (n/a)</td><td>31.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-0.71%)</td><td>0.21 (-0.18%)</td><td>0.21 (-0.16%)</td><td>0.21 (+0.01%)</td><td>0.00 <b>(-62.77%)</b></td><td>40884.20 (-0.01%)</td><td>40806.58 (+0.18%)</td><td>40830.30 (+0.16%)</td><td>40723.20 (+0.71%)</td><td>65.73 <b>(-62.46%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40888.80 (n/a)</td><td>40732.90 (n/a)</td><td>40765.20 (n/a)</td><td>40434.80 (n/a)</td><td>175.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (-0.85%)</td><td>0.21 (-0.41%)</td><td>0.21 (-0.30%)</td><td>0.20 (-0.10%)</td><td>0.00 <b>(-78.13%)</b></td><td>40933.10 (+0.10%)</td><td>40894.88 (+0.41%)</td><td>40886.00 (+0.30%)</td><td>40857.00 (+0.86%)</td><td>31.18 <b>(-77.91%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>40894.10 (n/a)</td><td>40726.96 (n/a)</td><td>40764.20 (n/a)</td><td>40508.40 (n/a)</td><td>141.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (+0.02%)</td><td>0.13 (+0.02%)</td><td>0.13 (+0.03%)</td><td>0.13 (+0.02%)</td><td>0.00 (-5.75%)</td><td>321847.40 (-0.02%)</td><td>321661.14 (-0.02%)</td><td>321640.00 (-0.03%)</td><td>321487.60 (-0.02%)</td><td>132.78 (-5.75%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.00 (n/a)</td><td>321910.70 (n/a)</td><td>321718.26 (n/a)</td><td>321736.90 (n/a)</td><td>321561.70 (n/a)</td><td>140.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 <b>(+36.28%)</b></td><td>0.03 <b>(+26.25%)</b></td><td>0.02 (+19.52%)</td><td>0.02 <b>(+54.44%)</b></td><td>0.01 <b>(+31.52%)</b></td><td>233.20 <b>(-35.26%)</b></td><td>170.44 <b>(-22.03%)</b></td><td>164.40 (-16.29%)</td><td>118.10 <b>(-26.65%)</b></td><td>49.87 <b>(-39.18%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>360.20 (n/a)</td><td>218.60 (n/a)</td><td>196.40 (n/a)</td><td>161.00 (n/a)</td><td>82.00 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (+18.75%)</td><td>0.04 <b>(+20.00%)</b></td><td>0.04 <b>(+32.13%)</b></td><td>0.03 (+11.68%)</td><td>0.01 <b>(+43.65%)</b></td><td>209.40 (-10.44%)</td><td>168.52 (-15.92%)</td><td>156.80 <b>(-24.32%)</b></td><td>137.20 (-15.78%)</td><td>29.74 (+10.70%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>233.80 (n/a)</td><td>200.44 (n/a)</td><td>207.20 (n/a)</td><td>162.90 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 <b>(+23.42%)</b></td><td>0.03 (+17.66%)</td><td>0.03 (+16.29%)</td><td>0.03 <b>(+20.37%)</b></td><td>0.00 <b>(+41.25%)</b></td><td>160.90 (-16.93%)</td><td>148.02 (-14.92%)</td><td>146.30 (-13.99%)</td><td>134.80 (-18.99%)</td><td>10.55 (-5.56%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>173.98 (n/a)</td><td>170.10 (n/a)</td><td>166.40 (n/a)</td><td>11.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 <b>(-26.42%)</b></td><td>0.03 (-12.92%)</td><td>0.03 (-11.68%)</td><td>0.02 (-3.95%)</td><td>0.00 <b>(-61.34%)</b></td><td>216.10 (+4.14%)</td><td>191.10 (+12.56%)</td><td>191.30 (+13.20%)</td><td>175.80 <b>(+35.86%)</b></td><td>16.21 <b>(-45.00%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>169.78 (n/a)</td><td>169.00 (n/a)</td><td>129.40 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+16.20%)</td><td>0.03 (+10.08%)</td><td>0.03 (+10.17%)</td><td>0.02 (+8.94%)</td><td>0.00 <b>(+24.80%)</b></td><td>194.00 (-8.23%)</td><td>158.36 (-8.90%)</td><td>154.40 (-9.23%)</td><td>131.10 (-13.98%)</td><td>22.67 (-1.33%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.40 (n/a)</td><td>173.84 (n/a)</td><td>170.10 (n/a)</td><td>152.40 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.04 (-0.18%)</td><td>0.04 (-2.66%)</td><td>0.03 (-7.61%)</td><td>0.03 (-0.98%)</td><td>0.01 (+3.23%)</td><td>193.40 (+0.99%)</td><td>150.04 (+2.89%)</td><td>153.90 (+8.23%)</td><td>118.20 (+0.17%)</td><td>29.25 (+2.55%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>145.82 (n/a)</td><td>142.20 (n/a)</td><td>118.00 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+13.75%)</td><td>0.03 (+17.46%)</td><td>0.03 (+11.55%)</td><td>0.03 <b>(+30.52%)</b></td><td>0.00 <b>(-34.72%)</b></td><td>148.60 <b>(-23.36%)</b></td><td>140.50 (-15.79%)</td><td>146.30 (-10.36%)</td><td>124.90 (-12.10%)</td><td>10.16 <b>(-56.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>166.84 (n/a)</td><td>163.20 (n/a)</td><td>142.10 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+13.05%)</td><td>0.03 (+11.47%)</td><td>0.03 (+8.69%)</td><td>0.02 (+4.81%)</td><td>0.00 <b>(+32.42%)</b></td><td>203.50 (-4.59%)</td><td>170.88 (-9.97%)</td><td>170.00 (-8.01%)</td><td>149.80 (-11.57%)</td><td>21.00 (+11.51%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>189.80 (n/a)</td><td>184.80 (n/a)</td><td>169.40 (n/a)</td><td>18.83 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+16.41%)</td><td>0.03 <b>(+35.61%)</b></td><td>0.03 <b>(+24.15%)</b></td><td>0.03 <b>(+135.51%)</b></td><td>0.00 <b>(-79.92%)</b></td><td>154.10 <b>(-57.55%)</b></td><td>148.62 <b>(-32.45%)</b></td><td>150.40 (-19.49%)</td><td>138.70 (-14.12%)</td><td>6.05 <b>(-92.78%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>363.00 (n/a)</td><td>220.00 (n/a)</td><td>186.80 (n/a)</td><td>161.50 (n/a)</td><td>83.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-2.88%)</td><td>0.03 (+3.76%)</td><td>0.03 (+5.48%)</td><td>0.02 (+12.61%)</td><td>0.00 <b>(-54.12%)</b></td><td>194.20 (-11.20%)</td><td>176.22 (-5.12%)</td><td>174.60 (-5.21%)</td><td>162.00 (+2.99%)</td><td>12.31 <b>(-57.33%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>185.72 (n/a)</td><td>184.20 (n/a)</td><td>157.30 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+14.18%)</td><td>0.02 (+15.37%)</td><td>0.03 <b>(+22.80%)</b></td><td>0.02 (+10.32%)</td><td>0.00 (+6.82%)</td><td>218.00 (-9.36%)</td><td>167.68 (-13.42%)</td><td>159.40 (-18.55%)</td><td>137.70 (-12.40%)</td><td>30.00 (-10.93%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.50 (n/a)</td><td>193.68 (n/a)</td><td>195.70 (n/a)</td><td>157.20 (n/a)</td><td>33.68 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (-10.11%)</td><td>0.02 (-0.77%)</td><td>0.02 (+4.37%)</td><td>0.02 (-0.00%)</td><td>0.00 <b>(-23.19%)</b></td><td>209.80 (+0.00%)</td><td>189.78 (+0.41%)</td><td>187.00 (-4.20%)</td><td>170.80 (+11.27%)</td><td>18.66 (-11.77%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>189.00 (n/a)</td><td>195.20 (n/a)</td><td>153.50 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.03 (+8.56%)</td><td>0.02 (+9.75%)</td><td>0.02 (+11.72%)</td><td>0.02 (+15.15%)</td><td>0.00 (+0.56%)</td><td>205.70 (-13.17%)</td><td>176.24 (-9.27%)</td><td>171.70 (-10.53%)</td><td>146.90 (-7.90%)</td><td>27.87 (-17.12%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.90 (n/a)</td><td>194.24 (n/a)</td><td>191.90 (n/a)</td><td>159.50 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-15.39%)</td><td>0.02 (+0.83%)</td><td>0.02 (+3.16%)</td><td>0.02 <b>(+39.04%)</b></td><td>0.00 <b>(-46.98%)</b></td><td>243.80 <b>(-28.08%)</b></td><td>210.24 (-5.81%)</td><td>198.50 (-3.08%)</td><td>176.20 (+18.18%)</td><td>31.42 <b>(-55.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>339.00 (n/a)</td><td>223.20 (n/a)</td><td>204.80 (n/a)</td><td>149.10 (n/a)</td><td>70.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.02 (-0.19%)</td><td>0.02 (+1.43%)</td><td>0.02 (+2.19%)</td><td>0.02 (-2.50%)</td><td>0.00 (-4.12%)</td><td>232.90 (+2.60%)</td><td>201.28 (-1.48%)</td><td>193.90 (-2.17%)</td><td>179.80 (+0.17%)</td><td>20.99 (-2.78%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.00 (n/a)</td><td>204.30 (n/a)</td><td>198.20 (n/a)</td><td>179.50 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+2.72%)</td><td>0.05 (+6.74%)</td><td>0.05 (+11.43%)</td><td>0.04 (-1.77%)</td><td>0.01 (+6.40%)</td><td>182.10 (+1.79%)</td><td>154.18 (-6.17%)</td><td>154.10 (-10.25%)</td><td>128.90 (-2.64%)</td><td>20.09 (+6.80%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>164.32 (n/a)</td><td>171.70 (n/a)</td><td>132.40 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 <b>(+48.60%)</b></td><td>0.07 <b>(+30.16%)</b></td><td>0.08 <b>(+27.69%)</b></td><td>0.04 (-0.73%)</td><td>0.02 <b>(+118.91%)</b></td><td>321.70 (+0.72%)</td><td>187.24 (-17.20%)</td><td>160.50 <b>(-21.67%)</b></td><td>124.30 <b>(-32.70%)</b></td><td>79.48 <b>(+47.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>319.40 (n/a)</td><td>226.14 (n/a)</td><td>204.90 (n/a)</td><td>184.70 (n/a)</td><td>53.94 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 <b>(+20.45%)</b></td><td>0.05 (+3.94%)</td><td>0.05 (+4.56%)</td><td>0.05 (-4.00%)</td><td>0.01 <b>(+177.19%)</b></td><td>179.70 (+4.17%)</td><td>159.66 (-2.68%)</td><td>158.30 (-4.41%)</td><td>128.60 (-16.98%)</td><td>19.82 <b>(+137.75%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>172.50 (n/a)</td><td>164.06 (n/a)</td><td>165.60 (n/a)</td><td>154.90 (n/a)</td><td>8.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-14.79%)</td><td>0.06 (-0.04%)</td><td>0.06 (+4.29%)</td><td>0.05 (+17.78%)</td><td>0.01 <b>(-43.04%)</b></td><td>195.80 (-15.09%)</td><td>166.66 (-3.30%)</td><td>170.20 (-4.11%)</td><td>141.50 (+17.43%)</td><td>23.97 <b>(-43.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>172.34 (n/a)</td><td>177.50 (n/a)</td><td>120.50 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+0.08%)</td><td>0.06 (+10.99%)</td><td>0.06 (+9.04%)</td><td>0.05 <b>(+38.36%)</b></td><td>0.00 <b>(-54.73%)</b></td><td>154.20 <b>(-27.71%)</b></td><td>142.68 (-12.05%)</td><td>146.60 (-8.32%)</td><td>127.70 (-0.08%)</td><td>10.11 <b>(-68.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>162.22 (n/a)</td><td>159.90 (n/a)</td><td>127.80 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 (-14.75%)</td><td>0.06 (-6.50%)</td><td>0.06 (-5.83%)</td><td>0.05 (-5.76%)</td><td>0.01 <b>(-32.30%)</b></td><td>194.90 (+6.10%)</td><td>172.28 (+6.24%)</td><td>177.10 (+6.24%)</td><td>147.90 (+17.29%)</td><td>18.71 (-13.59%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>162.16 (n/a)</td><td>166.70 (n/a)</td><td>126.10 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+13.36%)</td><td>0.05 (+8.55%)</td><td>0.06 <b>(+20.38%)</b></td><td>0.04 (-7.57%)</td><td>0.01 <b>(+148.00%)</b></td><td>205.60 (+8.21%)</td><td>161.92 (-6.10%)</td><td>144.30 (-16.93%)</td><td>139.00 (-11.80%)</td><td>28.85 <b>(+134.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.00 (n/a)</td><td>172.44 (n/a)</td><td>173.70 (n/a)</td><td>157.60 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(+23.76%)</b></td><td>0.05 (+4.11%)</td><td>0.06 (+2.37%)</td><td>0.03 <b>(-23.97%)</b></td><td>0.02 <b>(+148.24%)</b></td><td>273.20 <b>(+31.54%)</b></td><td>184.60 (+3.08%)</td><td>165.80 (-2.36%)</td><td>123.50 (-19.23%)</td><td>61.77 <b>(+160.59%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>179.08 (n/a)</td><td>169.80 (n/a)</td><td>152.90 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.07 <b>(+29.18%)</b></td><td>0.05 (+4.41%)</td><td>0.05 (-8.99%)</td><td>0.04 (+0.12%)</td><td>0.01 <b>(+123.33%)</b></td><td>199.80 (-0.10%)</td><td>169.12 (-1.64%)</td><td>181.30 (+9.88%)</td><td>116.10 <b>(-22.55%)</b></td><td>32.52 <b>(+65.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>171.94 (n/a)</td><td>165.00 (n/a)</td><td>149.90 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (-18.75%)</td><td>0.05 (-4.37%)</td><td>0.05 (+4.72%)</td><td>0.04 (+10.61%)</td><td>0.01 <b>(-57.18%)</b></td><td>205.60 (-9.63%)</td><td>182.44 (+0.96%)</td><td>181.20 (-4.48%)</td><td>154.30 <b>(+23.05%)</b></td><td>19.29 <b>(-52.13%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>180.70 (n/a)</td><td>189.70 (n/a)</td><td>125.40 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-10.24%)</td><td>0.04 (-3.24%)</td><td>0.04 (+13.86%)</td><td>0.03 <b>(-25.46%)</b></td><td>0.01 (+9.18%)</td><td>306.10 <b>(+34.14%)</b></td><td>211.42 (+5.70%)</td><td>187.90 (-12.20%)</td><td>160.90 (+11.43%)</td><td>57.31 <b>(+71.84%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.20 (n/a)</td><td>200.02 (n/a)</td><td>214.00 (n/a)</td><td>144.40 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 <b>(-37.44%)</b></td><td>0.05 (-13.06%)</td><td>0.04 (-10.54%)</td><td>0.04 (+3.90%)</td><td>0.00 <b>(-74.88%)</b></td><td>199.70 (-3.76%)</td><td>186.42 (+9.08%)</td><td>195.50 (+11.78%)</td><td>168.10 <b>(+59.79%)</b></td><td>16.08 <b>(-60.29%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>207.50 (n/a)</td><td>170.90 (n/a)</td><td>174.90 (n/a)</td><td>105.20 (n/a)</td><td>40.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.06 (+15.73%)</td><td>0.04 (-3.73%)</td><td>0.04 (-8.15%)</td><td>0.03 (-18.72%)</td><td>0.01 <b>(+85.62%)</b></td><td>285.30 <b>(+23.03%)</b></td><td>202.26 (+8.31%)</td><td>193.90 (+8.87%)</td><td>133.80 (-13.57%)</td><td>54.87 <b>(+93.09%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>186.74 (n/a)</td><td>178.10 (n/a)</td><td>154.80 (n/a)</td><td>28.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-5.03%)</td><td>0.04 (-6.11%)</td><td>0.04 (-4.92%)</td><td>0.04 (-7.95%)</td><td>0.00 (+11.45%)</td><td>226.20 (+8.65%)</td><td>207.42 (+6.66%)</td><td>204.90 (+5.18%)</td><td>185.40 (+5.28%)</td><td>16.19 <b>(+28.12%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>194.46 (n/a)</td><td>194.80 (n/a)</td><td>176.10 (n/a)</td><td>12.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.05 (-3.88%)</td><td>0.04 (+11.12%)</td><td>0.04 (+19.92%)</td><td>0.04 (+12.84%)</td><td>0.00 <b>(-38.57%)</b></td><td>214.40 (-11.37%)</td><td>184.82 (-11.50%)</td><td>184.10 (-16.58%)</td><td>158.20 (+4.01%)</td><td>20.19 <b>(-41.40%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.90 (n/a)</td><td>208.84 (n/a)</td><td>220.70 (n/a)</td><td>152.10 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 <b>(-24.86%)</b></td><td>0.09 (-12.79%)</td><td>0.09 (-7.67%)</td><td>0.08 (+7.98%)</td><td>0.01 <b>(-72.68%)</b></td><td>205.70 (-7.38%)</td><td>186.40 (+8.49%)</td><td>190.70 (+8.29%)</td><td>163.60 <b>(+33.01%)</b></td><td>15.76 <b>(-65.85%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.10 (n/a)</td><td>171.82 (n/a)</td><td>176.10 (n/a)</td><td>123.00 (n/a)</td><td>46.14 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 <b>(-20.82%)</b></td><td>0.14 (-6.14%)</td><td>0.14 (-0.74%)</td><td>0.13 (+0.96%)</td><td>0.01 <b>(-67.17%)</b></td><td>190.10 (-0.94%)</td><td>175.68 (+4.58%)</td><td>176.30 (+0.74%)</td><td>164.70 <b>(+26.30%)</b></td><td>10.58 <b>(-59.67%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.90 (n/a)</td><td>167.98 (n/a)</td><td>175.00 (n/a)</td><td>130.40 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (+10.99%)</td><td>0.10 (-11.71%)</td><td>0.08 <b>(-22.61%)</b></td><td>0.07 (-15.25%)</td><td>0.03 <b>(+73.33%)</b></td><td>236.20 (+17.98%)</td><td>184.70 (+19.44%)</td><td>195.20 <b>(+29.27%)</b></td><td>114.70 (-9.90%)</td><td>53.41 <b>(+87.43%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.20 (n/a)</td><td>154.64 (n/a)</td><td>151.00 (n/a)</td><td>127.30 (n/a)</td><td>28.49 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 <b>(-21.81%)</b></td><td>0.11 (-14.75%)</td><td>0.11 (-13.72%)</td><td>0.10 (+15.23%)</td><td>0.01 <b>(-57.68%)</b></td><td>209.90 (-13.23%)</td><td>185.50 (+11.95%)</td><td>190.60 (+15.87%)</td><td>152.30 <b>(+27.88%)</b></td><td>21.70 <b>(-54.29%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>241.90 (n/a)</td><td>165.70 (n/a)</td><td>164.50 (n/a)</td><td>119.10 (n/a)</td><td>47.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 <b>(-21.33%)</b></td><td>0.08 (-6.05%)</td><td>0.08 (+5.97%)</td><td>0.06 (+1.54%)</td><td>0.02 <b>(-39.53%)</b></td><td>295.10 (-1.50%)</td><td>206.30 (+1.75%)</td><td>195.90 (-5.64%)</td><td>150.70 <b>(+27.07%)</b></td><td>53.40 (-19.51%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>299.60 (n/a)</td><td>202.76 (n/a)</td><td>207.60 (n/a)</td><td>118.60 (n/a)</td><td>66.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (-10.96%)</td><td>0.12 (+9.66%)</td><td>0.12 (+19.21%)</td><td>0.11 <b>(+34.02%)</b></td><td>0.01 <b>(-68.96%)</b></td><td>189.20 <b>(-25.39%)</b></td><td>174.84 (-12.03%)</td><td>171.50 (-16.10%)</td><td>160.50 (+12.32%)</td><td>11.30 <b>(-73.59%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>253.60 (n/a)</td><td>198.76 (n/a)</td><td>204.40 (n/a)</td><td>142.90 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-7.86%)</td><td>0.09 (-10.57%)</td><td>0.08 (-9.49%)</td><td>0.08 (-0.05%)</td><td>0.01 <b>(-32.04%)</b></td><td>196.60 (+0.05%)</td><td>181.78 (+10.21%)</td><td>194.70 (+10.50%)</td><td>141.80 (+8.58%)</td><td>23.20 <b>(-25.13%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>164.94 (n/a)</td><td>176.20 (n/a)</td><td>130.60 (n/a)</td><td>30.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-7.72%)</td><td>0.10 (-2.24%)</td><td>0.09 (-11.01%)</td><td>0.09 (+2.26%)</td><td>0.02 (-4.01%)</td><td>212.30 (-2.21%)</td><td>185.12 (+2.22%)</td><td>202.90 (+12.35%)</td><td>152.00 (+8.34%)</td><td>29.80 (+0.24%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.10 (n/a)</td><td>181.10 (n/a)</td><td>180.60 (n/a)</td><td>140.30 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-12.90%)</td><td>0.10 (+2.96%)</td><td>0.10 (+17.61%)</td><td>0.08 <b>(+22.05%)</b></td><td>0.01 <b>(-48.77%)</b></td><td>201.30 (-18.04%)</td><td>168.24 (-6.20%)</td><td>156.30 (-14.96%)</td><td>150.60 (+14.79%)</td><td>21.48 <b>(-51.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.60 (n/a)</td><td>179.36 (n/a)</td><td>183.80 (n/a)</td><td>131.20 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (+12.91%)</td><td>0.12 (+10.95%)</td><td>0.12 (+13.29%)</td><td>0.08 (-16.84%)</td><td>0.03 <b>(+104.83%)</b></td><td>230.10 <b>(+20.22%)</b></td><td>156.22 (-6.31%)</td><td>149.30 (-11.71%)</td><td>123.30 (-11.49%)</td><td>43.34 <b>(+123.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>166.74 (n/a)</td><td>169.10 (n/a)</td><td>139.30 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-10.56%)</td><td>0.08 (-5.88%)</td><td>0.08 (-2.29%)</td><td>0.06 (-14.00%)</td><td>0.02 (-8.27%)</td><td>284.80 (+16.29%)</td><td>210.30 (+6.59%)</td><td>204.10 (+2.31%)</td><td>149.50 (+11.82%)</td><td>55.28 (+15.87%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.90 (n/a)</td><td>197.30 (n/a)</td><td>199.50 (n/a)</td><td>133.70 (n/a)</td><td>47.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-13.68%)</td><td>0.10 (+10.61%)</td><td>0.10 (+3.11%)</td><td>0.09 <b>(+70.40%)</b></td><td>0.01 <b>(-65.69%)</b></td><td>192.20 <b>(-41.31%)</b></td><td>174.58 (-17.71%)</td><td>175.10 (-3.05%)</td><td>146.70 (+15.88%)</td><td>17.51 <b>(-77.34%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>327.50 (n/a)</td><td>212.14 (n/a)</td><td>180.60 (n/a)</td><td>126.60 (n/a)</td><td>77.26 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.11 (-10.13%)</td><td>0.10 (-4.06%)</td><td>0.10 (-5.66%)</td><td>0.09 (+5.66%)</td><td>0.01 <b>(-50.17%)</b></td><td>190.50 (-5.32%)</td><td>172.30 (+2.19%)</td><td>171.80 (+6.05%)</td><td>148.50 (+11.24%)</td><td>15.43 <b>(-49.72%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.20 (n/a)</td><td>168.60 (n/a)</td><td>162.00 (n/a)</td><td>133.50 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.10 (-1.20%)</td><td>0.09 (-6.75%)</td><td>0.09 (+0.16%)</td><td>0.07 <b>(-20.03%)</b></td><td>0.01 <b>(+153.42%)</b></td><td>239.00 <b>(+25.07%)</b></td><td>200.84 (+8.71%)</td><td>189.20 (-0.16%)</td><td>172.10 (+1.18%)</td><td>28.60 <b>(+223.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>191.10 (n/a)</td><td>184.74 (n/a)</td><td>189.50 (n/a)</td><td>170.10 (n/a)</td><td>8.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.09 (-4.90%)</td><td>0.08 (+13.46%)</td><td>0.08 (+16.51%)</td><td>0.07 <b>(+34.45%)</b></td><td>0.01 <b>(-48.45%)</b></td><td>227.00 <b>(-25.62%)</b></td><td>203.28 (-14.46%)</td><td>206.30 (-14.18%)</td><td>174.30 (+5.13%)</td><td>20.54 <b>(-58.54%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>305.20 (n/a)</td><td>237.64 (n/a)</td><td>240.40 (n/a)</td><td>165.80 (n/a)</td><td>49.54 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.21 (+8.79%)</td><td>0.17 (-1.92%)</td><td>0.17 (+2.14%)</td><td>0.14 (-8.04%)</td><td>0.03 <b>(+61.84%)</b></td><td>230.90 (+8.76%)</td><td>195.50 (+3.23%)</td><td>190.80 (-2.10%)</td><td>153.40 (-8.09%)</td><td>30.13 <b>(+63.27%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.30 (n/a)</td><td>189.38 (n/a)</td><td>194.90 (n/a)</td><td>166.90 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 <b>(-26.27%)</b></td><td>0.17 (-17.21%)</td><td>0.16 (-5.32%)</td><td>0.12 (-19.57%)</td><td>0.03 <b>(-42.98%)</b></td><td>270.50 <b>(+24.37%)</b></td><td>202.34 (+18.11%)</td><td>201.20 (+5.67%)</td><td>164.60 <b>(+35.58%)</b></td><td>41.56 (-0.55%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>217.50 (n/a)</td><td>171.32 (n/a)</td><td>190.40 (n/a)</td><td>121.40 (n/a)</td><td>41.79 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (+16.63%)</td><td>0.24 (-0.18%)</td><td>0.20 (-12.16%)</td><td>0.18 (-13.65%)</td><td>0.06 <b>(+138.24%)</b></td><td>224.50 (+15.84%)</td><td>182.78 (+4.67%)</td><td>202.50 (+13.89%)</td><td>128.50 (-14.28%)</td><td>44.65 <b>(+136.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>193.80 (n/a)</td><td>174.62 (n/a)</td><td>177.80 (n/a)</td><td>149.90 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(+38.25%)</b></td><td>0.21 <b>(+33.30%)</b></td><td>0.21 <b>(+21.31%)</b></td><td>0.16 <b>(+45.16%)</b></td><td>0.04 <b>(+20.44%)</b></td><td>198.60 <b>(-31.11%)</b></td><td>158.04 <b>(-25.93%)</b></td><td>155.90 (-17.60%)</td><td>118.00 <b>(-27.70%)</b></td><td>30.88 <b>(-40.71%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>288.30 (n/a)</td><td>213.38 (n/a)</td><td>189.20 (n/a)</td><td>163.20 (n/a)</td><td>52.09 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 <b>(+25.34%)</b></td><td>0.22 (-0.30%)</td><td>0.20 (-7.09%)</td><td>0.17 (-18.03%)</td><td>0.05 <b>(+301.05%)</b></td><td>246.30 <b>(+21.99%)</b></td><td>197.56 (+4.09%)</td><td>207.00 (+7.64%)</td><td>137.80 <b>(-20.21%)</b></td><td>41.31 <b>(+286.27%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>189.80 (n/a)</td><td>192.30 (n/a)</td><td>172.70 (n/a)</td><td>10.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (+12.64%)</td><td>0.20 <b>(+25.99%)</b></td><td>0.21 <b>(+39.94%)</b></td><td>0.17 <b>(+26.47%)</b></td><td>0.02 <b>(-24.75%)</b></td><td>196.00 <b>(-20.94%)</b></td><td>163.40 <b>(-22.12%)</b></td><td>159.70 <b>(-28.51%)</b></td><td>141.10 (-11.26%)</td><td>21.19 <b>(-47.21%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>247.90 (n/a)</td><td>209.80 (n/a)</td><td>223.40 (n/a)</td><td>159.00 (n/a)</td><td>40.13 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 <b>(-21.63%)</b></td><td>0.20 (-7.33%)</td><td>0.18 (-9.18%)</td><td>0.16 (-2.56%)</td><td>0.04 <b>(-36.46%)</b></td><td>225.40 (+2.64%)</td><td>192.80 (+5.55%)</td><td>204.50 (+10.12%)</td><td>155.10 <b>(+27.65%)</b></td><td>33.15 (-18.48%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>219.60 (n/a)</td><td>182.66 (n/a)</td><td>185.70 (n/a)</td><td>121.50 (n/a)</td><td>40.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (+17.75%)</td><td>0.18 (-0.27%)</td><td>0.17 (-3.18%)</td><td>0.13 (-18.88%)</td><td>0.04 <b>(+261.78%)</b></td><td>243.60 <b>(+23.28%)</b></td><td>192.90 (+3.45%)</td><td>191.00 (+3.24%)</td><td>145.50 (-15.06%)</td><td>39.29 <b>(+278.23%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>186.46 (n/a)</td><td>185.00 (n/a)</td><td>171.30 (n/a)</td><td>10.39 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(+26.14%)</b></td><td>0.21 (+12.15%)</td><td>0.19 (-0.31%)</td><td>0.18 (+19.58%)</td><td>0.04 <b>(+66.47%)</b></td><td>201.00 (-16.39%)</td><td>176.88 (-9.69%)</td><td>192.50 (+0.31%)</td><td>130.90 <b>(-20.71%)</b></td><td>30.89 (+10.36%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>240.40 (n/a)</td><td>195.86 (n/a)</td><td>191.90 (n/a)</td><td>165.10 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 <b>(+35.22%)</b></td><td>0.20 (+16.26%)</td><td>0.18 (+7.17%)</td><td>0.17 (+5.97%)</td><td>0.05 <b>(+126.05%)</b></td><td>194.90 (-5.66%)</td><td>166.38 (-11.62%)</td><td>180.20 (-6.68%)</td><td>113.40 <b>(-26.03%)</b></td><td>32.39 <b>(+57.43%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>188.26 (n/a)</td><td>193.10 (n/a)</td><td>153.30 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (+4.78%)</td><td>0.17 (-5.59%)</td><td>0.16 (-11.44%)</td><td>0.14 (+1.54%)</td><td>0.03 (+6.32%)</td><td>246.20 (-1.52%)</td><td>211.16 (+6.00%)</td><td>223.90 (+12.91%)</td><td>156.70 (-4.57%)</td><td>33.79 (-2.07%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>250.00 (n/a)</td><td>199.20 (n/a)</td><td>198.30 (n/a)</td><td>164.20 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 <b>(+25.13%)</b></td><td>0.20 (+13.38%)</td><td>0.19 (+14.63%)</td><td>0.15 (-3.85%)</td><td>0.04 <b>(+84.32%)</b></td><td>211.80 (+3.98%)</td><td>164.68 (-10.10%)</td><td>168.90 (-12.71%)</td><td>126.70 <b>(-20.06%)</b></td><td>31.99 <b>(+54.24%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.70 (n/a)</td><td>183.18 (n/a)</td><td>193.50 (n/a)</td><td>158.50 (n/a)</td><td>20.74 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.22 (+6.33%)</td><td>0.19 (+1.99%)</td><td>0.18 (-9.58%)</td><td>0.16 (+8.29%)</td><td>0.02 <b>(-20.19%)</b></td><td>216.50 (-7.64%)</td><td>189.94 (-2.83%)</td><td>193.10 (+10.60%)</td><td>160.60 (-5.97%)</td><td>22.14 <b>(-30.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>234.40 (n/a)</td><td>195.48 (n/a)</td><td>174.60 (n/a)</td><td>170.80 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (+13.80%)</td><td>0.17 (+9.62%)</td><td>0.16 (+6.99%)</td><td>0.15 (+6.38%)</td><td>0.02 <b>(+39.35%)</b></td><td>221.40 (-5.99%)</td><td>196.00 (-8.42%)</td><td>202.60 (-6.55%)</td><td>162.80 (-12.14%)</td><td>21.96 (+14.37%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>235.50 (n/a)</td><td>214.02 (n/a)</td><td>216.80 (n/a)</td><td>185.30 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (-2.82%)</td><td>0.12 (-14.49%)</td><td>0.12 (-17.45%)</td><td>0.09 <b>(-23.12%)</b></td><td>0.02 <b>(+51.08%)</b></td><td>227.20 <b>(+30.05%)</b></td><td>175.24 (+19.36%)</td><td>177.90 <b>(+21.10%)</b></td><td>135.10 (+2.89%)</td><td>34.92 <b>(+101.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>174.70 (n/a)</td><td>146.82 (n/a)</td><td>146.90 (n/a)</td><td>131.30 (n/a)</td><td>17.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (-17.94%)</td><td>0.11 (-11.33%)</td><td>0.11 (-19.01%)</td><td>0.10 (+18.87%)</td><td>0.01 <b>(-61.27%)</b></td><td>208.10 (-15.89%)</td><td>183.72 (+7.69%)</td><td>178.70 <b>(+23.50%)</b></td><td>160.10 <b>(+21.84%)</b></td><td>19.22 <b>(-60.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>247.40 (n/a)</td><td>170.60 (n/a)</td><td>144.70 (n/a)</td><td>131.40 (n/a)</td><td>48.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (+14.06%)</td><td>0.13 (+7.25%)</td><td>0.13 (+4.86%)</td><td>0.10 (+1.47%)</td><td>0.02 <b>(+40.30%)</b></td><td>212.10 (-1.44%)</td><td>164.36 (-5.74%)</td><td>160.70 (-4.69%)</td><td>127.60 (-12.30%)</td><td>31.22 <b>(+20.41%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>174.36 (n/a)</td><td>168.60 (n/a)</td><td>145.50 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 <b>(+30.93%)</b></td><td>0.13 <b>(+20.52%)</b></td><td>0.13 (+16.96%)</td><td>0.11 (+8.14%)</td><td>0.02 <b>(+112.77%)</b></td><td>194.90 (-7.54%)</td><td>156.20 (-15.81%)</td><td>157.20 (-14.52%)</td><td>129.50 <b>(-23.60%)</b></td><td>26.06 <b>(+50.28%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>185.54 (n/a)</td><td>183.90 (n/a)</td><td>169.50 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-4.77%)</td><td>0.12 (-15.55%)</td><td>0.12 (-15.76%)</td><td>0.10 (-11.15%)</td><td>0.02 (-2.58%)</td><td>200.50 (+12.58%)</td><td>170.02 (+18.68%)</td><td>172.50 (+18.72%)</td><td>126.90 (+4.96%)</td><td>26.86 (+13.86%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>178.10 (n/a)</td><td>143.26 (n/a)</td><td>145.30 (n/a)</td><td>120.90 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (-5.04%)</td><td>0.11 (-7.57%)</td><td>0.11 (-6.25%)</td><td>0.09 (-14.91%)</td><td>0.01 <b>(+32.10%)</b></td><td>230.10 (+17.52%)</td><td>193.68 (+9.08%)</td><td>193.40 (+6.67%)</td><td>161.70 (+5.27%)</td><td>26.94 <b>(+64.25%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>177.56 (n/a)</td><td>181.30 (n/a)</td><td>153.60 (n/a)</td><td>16.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (-13.76%)</td><td>0.11 (-5.00%)</td><td>0.10 (-9.76%)</td><td>0.09 (+18.71%)</td><td>0.02 <b>(-45.35%)</b></td><td>222.50 (-15.75%)</td><td>190.30 (+1.33%)</td><td>195.80 (+10.87%)</td><td>151.90 (+15.95%)</td><td>25.96 <b>(-48.16%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>264.10 (n/a)</td><td>187.80 (n/a)</td><td>176.60 (n/a)</td><td>131.00 (n/a)</td><td>50.07 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 <b>(-30.52%)</b></td><td>0.11 (-17.09%)</td><td>0.11 (-9.81%)</td><td>0.09 (-14.88%)</td><td>0.01 <b>(-54.08%)</b></td><td>222.20 (+17.44%)</td><td>184.58 (+17.88%)</td><td>179.10 (+10.90%)</td><td>155.50 <b>(+43.98%)</b></td><td>24.83 (-18.96%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>189.20 (n/a)</td><td>156.58 (n/a)</td><td>161.50 (n/a)</td><td>108.00 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (-9.91%)</td><td>0.15 (-8.73%)</td><td>0.16 (+1.32%)</td><td>0.12 (-19.23%)</td><td>0.02 (+13.63%)</td><td>206.90 <b>(+23.82%)</b></td><td>164.48 (+10.52%)</td><td>152.40 (-1.30%)</td><td>138.30 (+11.00%)</td><td>26.74 <b>(+59.97%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>167.10 (n/a)</td><td>148.82 (n/a)</td><td>154.40 (n/a)</td><td>124.60 (n/a)</td><td>16.72 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (+7.14%)</td><td>0.15 (-5.62%)</td><td>0.14 (-14.98%)</td><td>0.07 <b>(-45.92%)</b></td><td>0.06 <b>(+99.41%)</b></td><td>359.70 <b>(+84.94%)</b></td><td>195.24 <b>(+20.27%)</b></td><td>178.20 (+17.62%)</td><td>122.80 (-6.62%)</td><td>97.10 <b>(+226.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.50 (n/a)</td><td>162.34 (n/a)</td><td>151.50 (n/a)</td><td>131.50 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-10.06%)</td><td>0.15 (-3.55%)</td><td>0.15 (-2.52%)</td><td>0.12 (-10.52%)</td><td>0.02 (-8.59%)</td><td>204.20 (+11.77%)</td><td>167.76 (+3.75%)</td><td>160.60 (+2.62%)</td><td>152.10 (+11.18%)</td><td>21.17 (+14.24%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.70 (n/a)</td><td>161.70 (n/a)</td><td>156.50 (n/a)</td><td>136.80 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 (+0.60%)</td><td>0.16 (+4.37%)</td><td>0.16 (+6.32%)</td><td>0.13 <b>(+28.48%)</b></td><td>0.03 (-19.16%)</td><td>194.70 <b>(-22.18%)</b></td><td>161.70 (-6.62%)</td><td>156.30 (-5.96%)</td><td>122.90 (-0.57%)</td><td>28.84 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>250.20 (n/a)</td><td>173.16 (n/a)</td><td>166.20 (n/a)</td><td>123.60 (n/a)</td><td>47.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 <b>(-22.42%)</b></td><td>0.12 <b>(-21.70%)</b></td><td>0.12 (-17.13%)</td><td>0.07 <b>(-43.12%)</b></td><td>0.03 (-3.94%)</td><td>364.70 <b>(+75.76%)</b></td><td>220.32 <b>(+33.59%)</b></td><td>196.80 <b>(+20.66%)</b></td><td>156.10 <b>(+28.90%)</b></td><td>83.18 <b>(+128.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>207.50 (n/a)</td><td>164.92 (n/a)</td><td>163.10 (n/a)</td><td>121.10 (n/a)</td><td>36.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.16 (-10.18%)</td><td>0.14 (-13.83%)</td><td>0.13 (-9.63%)</td><td>0.12 (-14.27%)</td><td>0.02 (-12.75%)</td><td>206.40 (+16.61%)</td><td>183.08 (+16.03%)</td><td>183.80 (+10.66%)</td><td>154.50 (+11.31%)</td><td>20.15 (+15.57%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>177.00 (n/a)</td><td>157.78 (n/a)</td><td>166.10 (n/a)</td><td>138.80 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.20 <b>(+23.22%)</b></td><td>0.16 (+11.54%)</td><td>0.14 (-6.45%)</td><td>0.13 (+12.65%)</td><td>0.03 <b>(+73.50%)</b></td><td>196.10 (-11.23%)</td><td>163.08 (-8.84%)</td><td>178.20 (+6.83%)</td><td>125.80 (-18.84%)</td><td>31.56 <b>(+21.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.90 (n/a)</td><td>178.90 (n/a)</td><td>166.80 (n/a)</td><td>155.00 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.18 (+10.71%)</td><td>0.15 (+12.32%)</td><td>0.15 (+13.68%)</td><td>0.12 (+18.84%)</td><td>0.03 (+19.00%)</td><td>211.30 (-15.85%)</td><td>170.98 (-10.79%)</td><td>167.30 (-12.04%)</td><td>134.90 (-9.65%)</td><td>33.37 (-11.03%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>251.10 (n/a)</td><td>191.66 (n/a)</td><td>190.20 (n/a)</td><td>149.30 (n/a)</td><td>37.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (+5.15%)</td><td>0.11 (+5.35%)</td><td>0.11 (+9.50%)</td><td>0.09 (+0.00%)</td><td>0.02 (+8.11%)</td><td>204.00 (+0.00%)</td><td>165.06 (-4.91%)</td><td>162.60 (-8.70%)</td><td>130.80 (-4.94%)</td><td>26.05 (+4.29%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>173.58 (n/a)</td><td>178.10 (n/a)</td><td>137.60 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-13.69%)</td><td>0.10 (-19.49%)</td><td>0.09 <b>(-23.17%)</b></td><td>0.09 (-15.69%)</td><td>0.01 (+7.10%)</td><td>205.90 (+18.61%)</td><td>191.30 <b>(+24.64%)</b></td><td>199.60 <b>(+30.12%)</b></td><td>156.70 (+15.90%)</td><td>20.06 <b>(+44.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>173.60 (n/a)</td><td>153.48 (n/a)</td><td>153.40 (n/a)</td><td>135.20 (n/a)</td><td>13.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 (-8.87%)</td><td>0.12 (-12.38%)</td><td>0.11 (-19.84%)</td><td>0.09 (-15.82%)</td><td>0.02 (+13.14%)</td><td>209.90 (+18.79%)</td><td>165.26 (+15.65%)</td><td>166.40 <b>(+24.74%)</b></td><td>126.60 (+9.71%)</td><td>34.22 <b>(+44.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>176.70 (n/a)</td><td>142.90 (n/a)</td><td>133.40 (n/a)</td><td>115.40 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 <b>(+28.35%)</b></td><td>0.12 <b>(+20.84%)</b></td><td>0.13 <b>(+21.24%)</b></td><td>0.09 (+7.73%)</td><td>0.02 <b>(+88.46%)</b></td><td>212.90 (-7.19%)</td><td>157.86 (-15.50%)</td><td>141.00 (-17.54%)</td><td>131.50 <b>(-22.05%)</b></td><td>34.97 <b>(+34.63%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>186.82 (n/a)</td><td>171.00 (n/a)</td><td>168.70 (n/a)</td><td>25.97 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.15 <b>(+22.07%)</b></td><td>0.11 (-4.45%)</td><td>0.10 (-14.96%)</td><td>0.08 (-17.98%)</td><td>0.03 <b>(+146.56%)</b></td><td>231.20 <b>(+21.94%)</b></td><td>183.82 (+10.22%)</td><td>184.20 (+17.62%)</td><td>120.90 (-18.03%)</td><td>48.50 <b>(+152.10%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>166.78 (n/a)</td><td>156.60 (n/a)</td><td>147.50 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.14 (-8.08%)</td><td>0.12 (+0.38%)</td><td>0.11 (-4.19%)</td><td>0.10 (+10.73%)</td><td>0.02 <b>(-23.10%)</b></td><td>179.30 (-9.72%)</td><td>161.86 (-1.37%)</td><td>174.90 (+4.42%)</td><td>131.60 (+8.85%)</td><td>22.39 <b>(-20.70%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.60 (n/a)</td><td>164.10 (n/a)</td><td>167.50 (n/a)</td><td>120.90 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (-2.90%)</td><td>0.09 (-4.82%)</td><td>0.09 (-2.70%)</td><td>0.08 (-6.56%)</td><td>0.01 (+6.71%)</td><td>229.80 (+7.03%)</td><td>204.48 (+5.41%)</td><td>207.60 (+2.77%)</td><td>160.10 (+2.96%)</td><td>27.88 (+18.35%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>193.98 (n/a)</td><td>202.00 (n/a)</td><td>155.50 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.13 (+7.37%)</td><td>0.11 (+6.84%)</td><td>0.10 (+2.03%)</td><td>0.09 (+12.03%)</td><td>0.02 (+10.58%)</td><td>206.40 (-10.73%)</td><td>175.54 (-6.42%)</td><td>180.10 (-2.01%)</td><td>145.40 (-6.91%)</td><td>24.28 (-10.50%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>187.58 (n/a)</td><td>183.80 (n/a)</td><td>156.20 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.76 (+3.30%)</td><td>0.58 (-10.37%)</td><td>0.57 (-10.75%)</td><td>0.48 (-15.95%)</td><td>0.11 <b>(+78.13%)</b></td><td>205.50 (+18.99%)</td><td>173.96 (+13.60%)</td><td>173.10 (+12.04%)</td><td>128.90 (-3.23%)</td><td>28.81 <b>(+101.36%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.57 (n/a)</td><td>0.06 (n/a)</td><td>172.70 (n/a)</td><td>153.14 (n/a)</td><td>154.50 (n/a)</td><td>133.20 (n/a)</td><td>14.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.67 (-12.02%)</td><td>0.58 (-7.94%)</td><td>0.56 (-11.42%)</td><td>0.53 (+11.74%)</td><td>0.05 <b>(-48.83%)</b></td><td>187.20 (-10.52%)</td><td>170.26 (+6.61%)</td><td>174.00 (+12.84%)</td><td>146.70 (+13.63%)</td><td>14.78 <b>(-50.48%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.76 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.47 (n/a)</td><td>0.11 (n/a)</td><td>209.20 (n/a)</td><td>159.70 (n/a)</td><td>154.20 (n/a)</td><td>129.10 (n/a)</td><td>29.84 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.77 (-2.51%)</td><td>0.57 (-10.65%)</td><td>0.57 (-5.56%)</td><td>0.40 <b>(-25.32%)</b></td><td>0.14 <b>(+29.09%)</b></td><td>247.60 <b>(+33.91%)</b></td><td>182.42 (+14.93%)</td><td>172.70 (+5.89%)</td><td>127.90 (+2.65%)</td><td>44.92 <b>(+76.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.60 (n/a)</td><td>0.53 (n/a)</td><td>0.11 (n/a)</td><td>184.90 (n/a)</td><td>158.72 (n/a)</td><td>163.10 (n/a)</td><td>124.60 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.66 (-19.37%)</td><td>0.55 (-18.54%)</td><td>0.54 (-18.98%)</td><td>0.47 (-9.53%)</td><td>0.08 <b>(-25.66%)</b></td><td>210.70 (+10.55%)</td><td>183.30 <b>(+22.13%)</b></td><td>182.90 <b>(+23.41%)</b></td><td>149.10 <b>(+24.04%)</b></td><td>27.07 (+2.98%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.52 (n/a)</td><td>0.11 (n/a)</td><td>190.60 (n/a)</td><td>150.08 (n/a)</td><td>148.20 (n/a)</td><td>120.20 (n/a)</td><td>26.29 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.55 (-2.20%)</td><td>0.45 (+0.16%)</td><td>0.42 (-15.53%)</td><td>0.40 <b>(+99.61%)</b></td><td>0.06 <b>(-58.44%)</b></td><td>182.60 <b>(-49.92%)</b></td><td>167.14 (-12.48%)</td><td>175.80 (+18.38%)</td><td>133.10 (+2.23%)</td><td>20.20 <b>(-79.58%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.50 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>364.60 (n/a)</td><td>190.98 (n/a)</td><td>148.50 (n/a)</td><td>130.20 (n/a)</td><td>98.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.55 (+6.70%)</td><td>0.46 (+7.48%)</td><td>0.43 (+3.35%)</td><td>0.42 <b>(+34.10%)</b></td><td>0.05 <b>(-32.73%)</b></td><td>175.30 <b>(-25.44%)</b></td><td>162.86 (-8.83%)</td><td>170.00 (-3.24%)</td><td>134.20 (-6.28%)</td><td>16.54 <b>(-53.95%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>235.10 (n/a)</td><td>178.64 (n/a)</td><td>175.70 (n/a)</td><td>143.20 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.59 (+0.81%)</td><td>0.46 (-12.67%)</td><td>0.41 <b>(-23.28%)</b></td><td>0.32 <b>(-29.29%)</b></td><td>0.12 <b>(+102.50%)</b></td><td>230.30 <b>(+41.46%)</b></td><td>169.96 (+19.69%)</td><td>180.80 <b>(+30.35%)</b></td><td>125.80 (-0.87%)</td><td>44.08 <b>(+172.11%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.58 (n/a)</td><td>0.52 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.06 (n/a)</td><td>162.80 (n/a)</td><td>142.00 (n/a)</td><td>138.70 (n/a)</td><td>126.90 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.47 (-8.10%)</td><td>0.37 (-4.61%)</td><td>0.35 (-3.75%)</td><td>0.32 (-1.64%)</td><td>0.06 <b>(-20.78%)</b></td><td>227.90 (+1.70%)</td><td>203.14 (+4.07%)</td><td>208.10 (+3.89%)</td><td>157.40 (+8.78%)</td><td>26.90 (-13.11%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>224.10 (n/a)</td><td>195.20 (n/a)</td><td>200.30 (n/a)</td><td>144.70 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (-1.06%)</td><td>0.23 (+1.57%)</td><td>0.25 (+10.58%)</td><td>0.17 (-8.71%)</td><td>0.05 <b>(+35.62%)</b></td><td>215.00 (+9.53%)</td><td>167.94 (+0.74%)</td><td>145.80 (-9.55%)</td><td>130.60 (+1.08%)</td><td>40.42 <b>(+54.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>196.30 (n/a)</td><td>166.70 (n/a)</td><td>161.20 (n/a)</td><td>129.20 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (+7.25%)</td><td>0.19 (-2.77%)</td><td>0.21 (+8.51%)</td><td>0.11 <b>(-25.30%)</b></td><td>0.06 <b>(+69.04%)</b></td><td>335.00 <b>(+33.89%)</b></td><td>211.52 (+10.16%)</td><td>173.20 (-7.87%)</td><td>147.90 (-6.81%)</td><td>79.55 <b>(+111.60%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>250.20 (n/a)</td><td>192.02 (n/a)</td><td>188.00 (n/a)</td><td>158.70 (n/a)</td><td>37.59 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (-3.06%)</td><td>0.21 (-11.26%)</td><td>0.21 (-11.40%)</td><td>0.16 <b>(-24.13%)</b></td><td>0.05 <b>(+93.91%)</b></td><td>232.70 <b>(+31.77%)</b></td><td>183.50 (+16.21%)</td><td>175.20 (+12.81%)</td><td>141.40 (+3.21%)</td><td>40.46 <b>(+164.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>176.60 (n/a)</td><td>157.90 (n/a)</td><td>155.30 (n/a)</td><td>137.00 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (-11.47%)</td><td>0.21 (-10.47%)</td><td>0.22 (-3.80%)</td><td>0.16 (-8.64%)</td><td>0.04 (-17.94%)</td><td>234.90 (+9.46%)</td><td>177.58 (+11.07%)</td><td>166.80 (+3.93%)</td><td>138.90 (+13.02%)</td><td>37.09 (+3.44%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>214.60 (n/a)</td><td>159.88 (n/a)</td><td>160.50 (n/a)</td><td>122.90 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (-3.34%)</td><td>0.19 (-9.11%)</td><td>0.20 (-6.81%)</td><td>0.16 (-8.63%)</td><td>0.03 <b>(+27.29%)</b></td><td>228.90 (+9.42%)</td><td>196.48 (+10.82%)</td><td>186.40 (+7.31%)</td><td>163.30 (+3.49%)</td><td>27.61 <b>(+43.70%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>209.20 (n/a)</td><td>177.30 (n/a)</td><td>173.70 (n/a)</td><td>157.80 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.30 <b>(+20.06%)</b></td><td>0.21 (-2.99%)</td><td>0.19 (-4.06%)</td><td>0.17 (-7.02%)</td><td>0.05 <b>(+56.60%)</b></td><td>218.10 (+7.54%)</td><td>185.52 (+5.30%)</td><td>193.20 (+4.21%)</td><td>123.00 (-16.72%)</td><td>36.46 <b>(+36.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>202.80 (n/a)</td><td>176.18 (n/a)</td><td>185.40 (n/a)</td><td>147.70 (n/a)</td><td>26.70 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(+20.98%)</b></td><td>0.19 (-5.60%)</td><td>0.18 (-14.54%)</td><td>0.14 <b>(-23.09%)</b></td><td>0.05 <b>(+167.66%)</b></td><td>266.30 <b>(+30.03%)</b></td><td>204.38 (+11.18%)</td><td>209.80 (+17.01%)</td><td>133.70 (-17.37%)</td><td>50.89 <b>(+179.02%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>183.82 (n/a)</td><td>179.30 (n/a)</td><td>161.80 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.23 (+5.77%)</td><td>0.18 (-11.24%)</td><td>0.19 (-5.95%)</td><td>0.13 <b>(-36.69%)</b></td><td>0.04 <b>(+475.31%)</b></td><td>291.50 <b>(+57.99%)</b></td><td>209.16 (+16.97%)</td><td>192.40 (+6.36%)</td><td>163.10 (-5.45%)</td><td>49.34 <b>(+794.31%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>178.82 (n/a)</td><td>180.90 (n/a)</td><td>172.50 (n/a)</td><td>5.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (-18.09%)</td><td>0.18 <b>(-25.43%)</b></td><td>0.18 <b>(-32.02%)</b></td><td>0.13 (+5.79%)</td><td>0.04 <b>(-42.48%)</b></td><td>314.00 (-5.48%)</td><td>233.72 <b>(+25.56%)</b></td><td>229.50 <b>(+47.12%)</b></td><td>170.20 <b>(+22.01%)</b></td><td>52.17 <b>(-36.37%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>332.20 (n/a)</td><td>186.14 (n/a)</td><td>156.00 (n/a)</td><td>139.50 (n/a)</td><td>81.99 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.32 (+7.96%)</td><td>0.26 (-0.38%)</td><td>0.27 (-4.20%)</td><td>0.20 (-6.92%)</td><td>0.04 <b>(+27.17%)</b></td><td>206.10 (+7.40%)</td><td>159.24 (+1.28%)</td><td>153.70 (+4.34%)</td><td>129.30 (-7.38%)</td><td>28.61 <b>(+30.32%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>191.90 (n/a)</td><td>157.22 (n/a)</td><td>147.30 (n/a)</td><td>139.60 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (-5.11%)</td><td>0.23 (-6.46%)</td><td>0.20 <b>(-20.19%)</b></td><td>0.20 <b>(+36.12%)</b></td><td>0.05 <b>(-25.64%)</b></td><td>209.30 <b>(-26.56%)</b></td><td>182.66 (+2.42%)</td><td>201.50 <b>(+25.31%)</b></td><td>132.70 (+5.40%)</td><td>34.15 <b>(-44.82%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>285.00 (n/a)</td><td>178.34 (n/a)</td><td>160.80 (n/a)</td><td>125.90 (n/a)</td><td>61.89 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (-0.30%)</td><td>0.22 (-10.91%)</td><td>0.22 (-13.45%)</td><td>0.16 <b>(-22.06%)</b></td><td>0.05 <b>(+58.94%)</b></td><td>259.20 <b>(+28.32%)</b></td><td>191.76 (+15.80%)</td><td>185.10 (+15.54%)</td><td>140.60 (+0.36%)</td><td>46.43 <b>(+101.61%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>202.00 (n/a)</td><td>165.60 (n/a)</td><td>160.20 (n/a)</td><td>140.10 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.31 (-18.99%)</td><td>0.25 (-11.17%)</td><td>0.23 (-15.60%)</td><td>0.19 (-15.32%)</td><td>0.06 (-12.34%)</td><td>220.50 (+18.10%)</td><td>172.14 (+12.92%)</td><td>179.20 (+18.52%)</td><td>132.20 <b>(+23.44%)</b></td><td>38.57 <b>(+22.79%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>186.70 (n/a)</td><td>152.44 (n/a)</td><td>151.20 (n/a)</td><td>107.10 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 (-14.46%)</td><td>0.24 (+5.50%)</td><td>0.23 (+3.53%)</td><td>0.21 <b>(+25.71%)</b></td><td>0.03 <b>(-49.28%)</b></td><td>197.70 <b>(-20.44%)</b></td><td>173.64 (-8.88%)</td><td>180.50 (-3.42%)</td><td>147.40 (+16.89%)</td><td>21.93 <b>(-52.51%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>248.50 (n/a)</td><td>190.56 (n/a)</td><td>186.90 (n/a)</td><td>126.10 (n/a)</td><td>46.18 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.26 (-12.56%)</td><td>0.21 (-11.93%)</td><td>0.20 (-16.78%)</td><td>0.17 (+12.04%)</td><td>0.04 <b>(-27.54%)</b></td><td>236.50 (-10.75%)</td><td>200.08 (+10.92%)</td><td>201.30 <b>(+20.18%)</b></td><td>157.00 (+14.35%)</td><td>36.22 <b>(-27.44%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>265.00 (n/a)</td><td>180.38 (n/a)</td><td>167.50 (n/a)</td><td>137.30 (n/a)</td><td>49.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.36 <b>(+21.27%)</b></td><td>0.25 (+1.69%)</td><td>0.26 (+4.43%)</td><td>0.13 <b>(-41.01%)</b></td><td>0.09 <b>(+171.26%)</b></td><td>326.70 <b>(+69.54%)</b></td><td>183.08 (+10.50%)</td><td>160.50 (-4.24%)</td><td>113.80 (-17.54%)</td><td>84.26 <b>(+299.78%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>192.70 (n/a)</td><td>165.68 (n/a)</td><td>167.60 (n/a)</td><td>138.00 (n/a)</td><td>21.08 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.27 (+0.32%)</td><td>0.23 (-3.52%)</td><td>0.24 (-0.32%)</td><td>0.17 (-19.87%)</td><td>0.04 <b>(+87.64%)</b></td><td>200.00 <b>(+24.77%)</b></td><td>153.66 (+5.56%)</td><td>145.90 (+0.34%)</td><td>129.80 (-0.31%)</td><td>28.08 <b>(+135.76%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>160.30 (n/a)</td><td>145.56 (n/a)</td><td>145.40 (n/a)</td><td>130.20 (n/a)</td><td>11.91 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (+1.48%)</td><td>0.20 (-3.53%)</td><td>0.19 (-7.44%)</td><td>0.17 (-1.41%)</td><td>0.03 (+1.72%)</td><td>201.40 (+1.46%)</td><td>177.48 (+3.64%)</td><td>179.70 (+7.99%)</td><td>141.50 (-1.46%)</td><td>21.99 (-2.32%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>198.50 (n/a)</td><td>171.24 (n/a)</td><td>166.40 (n/a)</td><td>143.60 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 <b>(+24.60%)</b></td><td>0.22 (+13.43%)</td><td>0.22 (+0.11%)</td><td>0.16 (+9.69%)</td><td>0.05 (+13.71%)</td><td>215.20 (-8.85%)</td><td>163.82 (-12.23%)</td><td>158.00 (-0.13%)</td><td>118.40 (-19.73%)</td><td>35.80 (-19.61%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>236.10 (n/a)</td><td>186.64 (n/a)</td><td>158.20 (n/a)</td><td>147.50 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.25 (-12.16%)</td><td>0.21 (-6.60%)</td><td>0.20 (-8.23%)</td><td>0.16 (+7.20%)</td><td>0.03 <b>(-46.29%)</b></td><td>219.20 (-6.72%)</td><td>172.28 (+2.29%)</td><td>172.50 (+8.97%)</td><td>139.00 (+13.84%)</td><td>29.74 <b>(-40.15%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>235.00 (n/a)</td><td>168.42 (n/a)</td><td>158.30 (n/a)</td><td>122.10 (n/a)</td><td>49.69 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.28 <b>(+25.28%)</b></td><td>0.23 (+11.32%)</td><td>0.23 (+9.67%)</td><td>0.16 (-15.37%)</td><td>0.05 <b>(+207.29%)</b></td><td>217.90 (+18.17%)</td><td>155.60 (-6.96%)</td><td>151.70 (-8.83%)</td><td>122.80 <b>(-20.21%)</b></td><td>37.44 <b>(+196.52%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>167.24 (n/a)</td><td>166.40 (n/a)</td><td>153.90 (n/a)</td><td>12.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (+1.64%)</td><td>0.19 (-11.80%)</td><td>0.16 (-16.13%)</td><td>0.15 (-6.10%)</td><td>0.06 (+10.38%)</td><td>229.90 (+6.48%)</td><td>193.68 (+15.09%)</td><td>218.70 (+19.25%)</td><td>119.50 (-1.65%)</td><td>47.87 <b>(+20.39%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>215.90 (n/a)</td><td>168.28 (n/a)</td><td>183.40 (n/a)</td><td>121.50 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.29 (+14.01%)</td><td>0.23 (+14.50%)</td><td>0.22 (+11.17%)</td><td>0.20 <b>(+22.10%)</b></td><td>0.04 (+3.87%)</td><td>178.50 (-18.08%)</td><td>153.76 (-13.14%)</td><td>160.30 (-10.04%)</td><td>119.80 (-12.30%)</td><td>22.54 <b>(-25.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>217.90 (n/a)</td><td>177.02 (n/a)</td><td>178.20 (n/a)</td><td>136.60 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (-4.79%)</td><td>0.20 (-2.22%)</td><td>0.22 (+4.23%)</td><td>0.10 <b>(-33.60%)</b></td><td>0.06 <b>(+44.62%)</b></td><td>337.10 <b>(+50.63%)</b></td><td>192.78 (+9.62%)</td><td>159.70 (-4.08%)</td><td>143.80 (+5.04%)</td><td>81.75 <b>(+134.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>223.80 (n/a)</td><td>175.86 (n/a)</td><td>166.50 (n/a)</td><td>136.90 (n/a)</td><td>34.85 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.90 (+2.30%)</td><td>0.82 (+4.88%)</td><td>0.86 (+10.82%)</td><td>0.69 (-0.38%)</td><td>0.08 (+8.14%)</td><td>188.90 (+0.37%)</td><td>161.30 (-4.56%)</td><td>152.80 (-9.80%)</td><td>145.70 (-2.28%)</td><td>17.74 (+6.44%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.08 (n/a)</td><td>188.20 (n/a)</td><td>169.00 (n/a)</td><td>169.40 (n/a)</td><td>149.10 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.99 (+9.68%)</td><td>0.84 (+4.91%)</td><td>0.87 (+10.98%)</td><td>0.62 (-6.37%)</td><td>0.14 <b>(+42.12%)</b></td><td>212.20 (+6.79%)</td><td>160.44 (-3.45%)</td><td>151.00 (-9.90%)</td><td>133.10 (-8.77%)</td><td>30.54 <b>(+44.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.90 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.66 (n/a)</td><td>0.10 (n/a)</td><td>198.70 (n/a)</td><td>166.18 (n/a)</td><td>167.60 (n/a)</td><td>145.90 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.97 (+15.40%)</td><td>0.84 (+16.03%)</td><td>0.81 (+14.91%)</td><td>0.71 <b>(+20.44%)</b></td><td>0.11 (+6.60%)</td><td>184.40 (-16.97%)</td><td>158.60 (-14.08%)</td><td>161.70 (-12.97%)</td><td>135.80 (-13.34%)</td><td>21.14 <b>(-23.06%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.84 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.59 (n/a)</td><td>0.11 (n/a)</td><td>222.10 (n/a)</td><td>184.60 (n/a)</td><td>185.80 (n/a)</td><td>156.70 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.00 (+0.00%)</td><td>0.00 (-2.29%)</td><td>0.00 (+0.00%)</td><td>0.00 (-6.98%)</td><td>0.00 <b>(+103.10%)</b></td><td>1024.39 (+7.14%)</td><td>962.74 (+2.35%)</td><td>954.02 (+0.18%)</td><td>918.52 (+0.32%)</td><td>39.72 <b>(+102.17%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>956.12 (n/a)</td><td>940.64 (n/a)</td><td>952.34 (n/a)</td><td>915.56 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.01 (+2.41%)</td><td>0.01 (-0.49%)</td><td>0.01 (+0.00%)</td><td>0.01 (-5.00%)</td><td>0.00 <b>(+174.40%)</b></td><td>1076.09 (+4.58%)</td><td>1007.62 (+0.30%)</td><td>998.63 (-0.05%)</td><td>959.98 (-2.79%)</td><td>44.77 <b>(+158.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1028.95 (n/a)</td><td>1004.56 (n/a)</td><td>999.10 (n/a)</td><td>987.56 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.96 (-0.01%)</td><td>0.94 (+0.23%)</td><td>0.94 (+0.96%)</td><td>0.91 (-1.59%)</td><td>0.02 <b>(+40.43%)</b></td><td>2294.87 (+1.62%)</td><td>2233.82 (-0.22%)</td><td>2223.22 (-0.95%)</td><td>2192.48 (+0.00%)</td><td>38.47 <b>(+43.43%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.01 (n/a)</td><td>2258.34 (n/a)</td><td>2238.75 (n/a)</td><td>2244.60 (n/a)</td><td>2192.40 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.25 <b>(+23.38%)</b></td><td>5.00 <b>(+21.45%)</b></td><td>4.51 (+15.07%)</td><td>3.99 (+7.08%)</td><td>1.03 <b>(+92.18%)</b></td><td>262.80 (-6.61%)</td><td>216.56 (-15.93%)</td><td>232.60 (-13.11%)</td><td>167.80 (-18.98%)</td><td>42.52 <b>(+46.03%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.06 (n/a)</td><td>4.12 (n/a)</td><td>3.92 (n/a)</td><td>3.73 (n/a)</td><td>0.54 (n/a)</td><td>281.40 (n/a)</td><td>257.58 (n/a)</td><td>267.70 (n/a)</td><td>207.10 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.80 (-9.76%)</td><td>4.68 (-5.66%)</td><td>4.39 (-9.49%)</td><td>3.97 (+0.63%)</td><td>0.81 (-12.03%)</td><td>264.20 (-0.64%)</td><td>229.08 (+5.68%)</td><td>238.60 (+10.46%)</td><td>180.90 (+10.78%)</td><td>37.35 (-0.04%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>6.42 (n/a)</td><td>4.96 (n/a)</td><td>4.85 (n/a)</td><td>3.94 (n/a)</td><td>0.92 (n/a)</td><td>265.90 (n/a)</td><td>216.76 (n/a)</td><td>216.00 (n/a)</td><td>163.30 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.63 (+7.14%)</td><td>4.77 (+5.13%)</td><td>4.53 (-1.42%)</td><td>4.43 (+13.19%)</td><td>0.49 (-7.64%)</td><td>236.40 (-11.66%)</td><td>221.70 (-5.20%)</td><td>231.30 (+1.45%)</td><td>186.30 (-6.66%)</td><td>20.54 <b>(-25.33%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.25 (n/a)</td><td>4.53 (n/a)</td><td>4.60 (n/a)</td><td>3.92 (n/a)</td><td>0.54 (n/a)</td><td>267.60 (n/a)</td><td>233.86 (n/a)</td><td>228.00 (n/a)</td><td>199.60 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>6.06 (+10.85%)</td><td>4.51 (-9.53%)</td><td>4.65 (-9.63%)</td><td>2.95 <b>(-34.16%)</b></td><td>1.33 <b>(+200.54%)</b></td><td>355.90 <b>(+51.90%)</b></td><td>250.92 (+18.47%)</td><td>225.40 (+10.65%)</td><td>172.90 (-9.81%)</td><td>78.65 <b>(+309.50%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.47 (n/a)</td><td>4.98 (n/a)</td><td>5.15 (n/a)</td><td>4.48 (n/a)</td><td>0.44 (n/a)</td><td>234.30 (n/a)</td><td>211.80 (n/a)</td><td>203.70 (n/a)</td><td>191.70 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.24 (+4.12%)</td><td>7.96 (+4.64%)</td><td>8.40 (+11.55%)</td><td>5.70 (-15.51%)</td><td>1.42 <b>(+60.19%)</b></td><td>367.70 (+18.35%)</td><td>271.38 (-2.54%)</td><td>249.70 (-10.37%)</td><td>227.00 (-3.98%)</td><td>57.25 <b>(+82.62%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.87 (n/a)</td><td>7.61 (n/a)</td><td>7.53 (n/a)</td><td>6.75 (n/a)</td><td>0.89 (n/a)</td><td>310.70 (n/a)</td><td>278.46 (n/a)</td><td>278.60 (n/a)</td><td>236.40 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.98 <b>(+21.29%)</b></td><td>8.41 (+5.36%)</td><td>7.94 (+0.23%)</td><td>6.90 (-12.04%)</td><td>1.38 <b>(+804.10%)</b></td><td>304.10 (+13.68%)</td><td>254.60 (-3.08%)</td><td>264.30 (-0.23%)</td><td>210.10 (-17.54%)</td><td>40.89 <b>(+726.77%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.23 (n/a)</td><td>7.99 (n/a)</td><td>7.92 (n/a)</td><td>7.84 (n/a)</td><td>0.15 (n/a)</td><td>267.50 (n/a)</td><td>262.68 (n/a)</td><td>264.90 (n/a)</td><td>254.80 (n/a)</td><td>4.95 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.30 (+1.49%)</td><td>8.14 (+3.00%)</td><td>8.28 (+5.02%)</td><td>7.13 (+7.62%)</td><td>0.88 (-5.13%)</td><td>294.20 (-7.08%)</td><td>259.98 (-3.10%)</td><td>253.20 (-4.81%)</td><td>225.60 (-1.44%)</td><td>28.16 (-12.86%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.16 (n/a)</td><td>7.91 (n/a)</td><td>7.89 (n/a)</td><td>6.62 (n/a)</td><td>0.93 (n/a)</td><td>316.60 (n/a)</td><td>268.30 (n/a)</td><td>266.00 (n/a)</td><td>228.90 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>10.70 <b>(+21.65%)</b></td><td>8.37 (-1.28%)</td><td>7.64 (-9.82%)</td><td>7.48 (-7.23%)</td><td>1.36 <b>(+352.67%)</b></td><td>280.50 (+7.80%)</td><td>255.28 (+3.07%)</td><td>274.60 (+10.90%)</td><td>195.90 (-17.79%)</td><td>35.63 <b>(+301.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.80 (n/a)</td><td>8.48 (n/a)</td><td>8.47 (n/a)</td><td>8.06 (n/a)</td><td>0.30 (n/a)</td><td>260.20 (n/a)</td><td>247.68 (n/a)</td><td>247.60 (n/a)</td><td>238.30 (n/a)</td><td>8.88 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>10.20 (+12.96%)</td><td>8.48 (+2.87%)</td><td>8.15 (-4.12%)</td><td>7.67 (+14.74%)</td><td>1.00 (+3.92%)</td><td>273.50 (-12.84%)</td><td>249.76 (-3.01%)</td><td>257.40 (+4.29%)</td><td>205.50 (-11.50%)</td><td>26.16 <b>(-21.98%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.03 (n/a)</td><td>8.24 (n/a)</td><td>8.50 (n/a)</td><td>6.68 (n/a)</td><td>0.96 (n/a)</td><td>313.80 (n/a)</td><td>257.52 (n/a)</td><td>246.80 (n/a)</td><td>232.20 (n/a)</td><td>33.53 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>9.54 (-1.55%)</td><td>8.16 (-1.65%)</td><td>8.56 (+2.32%)</td><td>6.45 (-1.55%)</td><td>1.35 (+19.82%)</td><td>325.00 (+1.59%)</td><td>263.18 (+2.42%)</td><td>245.00 (-2.27%)</td><td>219.90 (+1.57%)</td><td>46.07 <b>(+20.49%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>9.69 (n/a)</td><td>8.29 (n/a)</td><td>8.36 (n/a)</td><td>6.55 (n/a)</td><td>1.13 (n/a)</td><td>319.90 (n/a)</td><td>256.96 (n/a)</td><td>250.70 (n/a)</td><td>216.50 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.78 (-4.36%)</td><td>10.96 (-0.64%)</td><td>10.87 (-1.39%)</td><td>10.38 (+4.13%)</td><td>0.51 <b>(-49.24%)</b></td><td>404.30 (-3.94%)</td><td>383.22 (+0.16%)</td><td>386.00 (+1.42%)</td><td>356.10 (+4.55%)</td><td>17.42 <b>(-49.69%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.31 (n/a)</td><td>11.03 (n/a)</td><td>11.02 (n/a)</td><td>9.96 (n/a)</td><td>1.01 (n/a)</td><td>420.90 (n/a)</td><td>382.62 (n/a)</td><td>380.60 (n/a)</td><td>340.60 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.80 (+2.91%)</td><td>11.63 (+1.24%)</td><td>11.33 (-1.44%)</td><td>10.71 (+6.23%)</td><td>0.99 (+10.08%)</td><td>391.50 (-5.87%)</td><td>362.58 (-1.17%)</td><td>370.20 (+1.45%)</td><td>327.60 (-2.82%)</td><td>30.36 (-0.12%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.44 (n/a)</td><td>11.49 (n/a)</td><td>11.49 (n/a)</td><td>10.09 (n/a)</td><td>0.90 (n/a)</td><td>415.90 (n/a)</td><td>366.88 (n/a)</td><td>364.90 (n/a)</td><td>337.10 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>11.88 (-5.23%)</td><td>10.73 (-7.21%)</td><td>10.88 (-8.20%)</td><td>9.72 (-7.43%)</td><td>0.87 (+7.50%)</td><td>431.30 (+8.01%)</td><td>392.92 (+7.91%)</td><td>385.60 (+8.96%)</td><td>353.10 (+5.53%)</td><td>31.62 <b>(+22.57%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>12.54 (n/a)</td><td>11.56 (n/a)</td><td>11.85 (n/a)</td><td>10.50 (n/a)</td><td>0.81 (n/a)</td><td>399.30 (n/a)</td><td>364.12 (n/a)</td><td>353.90 (n/a)</td><td>334.60 (n/a)</td><td>25.80 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.92 (-7.26%)</td><td>12.78 (-2.18%)</td><td>12.75 (-1.31%)</td><td>11.25 (-5.68%)</td><td>1.09 (-8.87%)</td><td>372.80 (+6.03%)</td><td>330.12 (+2.21%)</td><td>329.10 (+1.32%)</td><td>301.30 (+7.84%)</td><td>28.99 (+4.57%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.01 (n/a)</td><td>13.07 (n/a)</td><td>12.91 (n/a)</td><td>11.93 (n/a)</td><td>1.20 (n/a)</td><td>351.60 (n/a)</td><td>322.98 (n/a)</td><td>324.80 (n/a)</td><td>279.40 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.73 (-13.14%)</td><td>12.45 (-5.68%)</td><td>12.44 (-6.54%)</td><td>12.06 (+7.73%)</td><td>0.26 <b>(-79.14%)</b></td><td>347.80 (-7.18%)</td><td>337.02 (+5.23%)</td><td>337.20 (+7.01%)</td><td>329.60 (+15.12%)</td><td>7.20 <b>(-78.14%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>14.65 (n/a)</td><td>13.20 (n/a)</td><td>13.31 (n/a)</td><td>11.19 (n/a)</td><td>1.26 (n/a)</td><td>374.70 (n/a)</td><td>320.26 (n/a)</td><td>315.10 (n/a)</td><td>286.30 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>12.89 (-18.47%)</td><td>11.79 (-9.24%)</td><td>11.75 (-14.22%)</td><td>10.74 (+11.08%)</td><td>0.85 <b>(-63.28%)</b></td><td>390.50 (-9.98%)</td><td>357.36 (+7.58%)</td><td>357.10 (+16.59%)</td><td>325.50 <b>(+22.65%)</b></td><td>25.86 <b>(-60.20%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>15.81 (n/a)</td><td>12.99 (n/a)</td><td>13.69 (n/a)</td><td>9.67 (n/a)</td><td>2.33 (n/a)</td><td>433.80 (n/a)</td><td>332.18 (n/a)</td><td>306.30 (n/a)</td><td>265.40 (n/a)</td><td>64.98 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.61 (-15.39%)</td><td>12.20 (-11.78%)</td><td>11.98 (-9.00%)</td><td>10.56 (-19.29%)</td><td>1.34 (+4.67%)</td><td>397.20 <b>(+23.89%)</b></td><td>347.08 (+13.76%)</td><td>350.20 (+9.88%)</td><td>308.30 (+18.21%)</td><td>38.41 <b>(+50.92%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>16.08 (n/a)</td><td>13.83 (n/a)</td><td>13.16 (n/a)</td><td>13.08 (n/a)</td><td>1.28 (n/a)</td><td>320.60 (n/a)</td><td>305.10 (n/a)</td><td>318.70 (n/a)</td><td>260.80 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>13.01 (-13.09%)</td><td>11.40 (-10.37%)</td><td>12.68 (-1.34%)</td><td>9.10 (-3.64%)</td><td>2.02 (-1.01%)</td><td>460.70 (+3.76%)</td><td>378.06 (+11.93%)</td><td>330.80 (+1.35%)</td><td>322.50 (+15.06%)</td><td>71.69 (+14.29%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>14.96 (n/a)</td><td>12.72 (n/a)</td><td>12.85 (n/a)</td><td>9.45 (n/a)</td><td>2.04 (n/a)</td><td>444.00 (n/a)</td><td>337.76 (n/a)</td><td>326.40 (n/a)</td><td>280.30 (n/a)</td><td>62.73 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.47 (+17.74%)</td><td>2.85 (+7.65%)</td><td>2.68 (-1.60%)</td><td>2.56 (+18.76%)</td><td>0.37 <b>(+22.43%)</b></td><td>205.10 (-15.80%)</td><td>186.12 (-7.08%)</td><td>195.90 (+1.61%)</td><td>150.90 (-15.08%)</td><td>21.86 (-14.99%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>2.95 (n/a)</td><td>2.65 (n/a)</td><td>2.72 (n/a)</td><td>2.15 (n/a)</td><td>0.31 (n/a)</td><td>243.60 (n/a)</td><td>200.30 (n/a)</td><td>192.80 (n/a)</td><td>177.70 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>5.40 (-6.50%)</td><td>4.69 (-4.69%)</td><td>4.60 (-12.28%)</td><td>4.38 <b>(+28.90%)</b></td><td>0.41 <b>(-55.97%)</b></td><td>239.60 <b>(-22.41%)</b></td><td>224.62 (+1.85%)</td><td>227.80 (+14.01%)</td><td>194.20 (+6.94%)</td><td>17.90 <b>(-65.04%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>5.77 (n/a)</td><td>4.93 (n/a)</td><td>5.25 (n/a)</td><td>3.40 (n/a)</td><td>0.93 (n/a)</td><td>308.80 (n/a)</td><td>220.54 (n/a)</td><td>199.80 (n/a)</td><td>181.60 (n/a)</td><td>51.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>7.96 (-8.59%)</td><td>7.40 (+2.39%)</td><td>7.47 (+0.19%)</td><td>6.72 (+18.84%)</td><td>0.47 <b>(-58.56%)</b></td><td>312.10 (-15.85%)</td><td>284.26 (-3.99%)</td><td>280.90 (-0.18%)</td><td>263.40 (+9.39%)</td><td>18.40 <b>(-62.19%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>8.71 (n/a)</td><td>7.23 (n/a)</td><td>7.45 (n/a)</td><td>5.65 (n/a)</td><td>1.13 (n/a)</td><td>370.90 (n/a)</td><td>296.08 (n/a)</td><td>281.40 (n/a)</td><td>240.80 (n/a)</td><td>48.67 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>3.47 (+12.80%)</td><td>2.88 (+0.95%)</td><td>2.74 (-2.54%)</td><td>2.28 (-10.13%)</td><td>0.47 <b>(+121.63%)</b></td><td>230.10 (+11.27%)</td><td>186.30 (+0.77%)</td><td>191.20 (+2.63%)</td><td>151.20 (-11.37%)</td><td>30.84 <b>(+116.99%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>3.07 (n/a)</td><td>2.85 (n/a)</td><td>2.81 (n/a)</td><td>2.54 (n/a)</td><td>0.21 (n/a)</td><td>206.80 (n/a)</td><td>184.88 (n/a)</td><td>186.30 (n/a)</td><td>170.60 (n/a)</td><td>14.21 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (+1.84%)</td><td>0.20 (+4.29%)</td><td>0.19 (+5.30%)</td><td>0.17 (+18.97%)</td><td>0.03 (-17.30%)</td><td>194.20 (-15.97%)</td><td>170.52 (-5.27%)</td><td>173.00 (-5.00%)</td><td>139.00 (-1.77%)</td><td>24.66 <b>(-29.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>231.10 (n/a)</td><td>180.00 (n/a)</td><td>182.10 (n/a)</td><td>141.50 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.24 (+0.81%)</td><td>0.21 (+6.72%)</td><td>0.23 (+17.39%)</td><td>0.17 (+8.49%)</td><td>0.04 (+3.02%)</td><td>191.80 (-7.83%)</td><td>158.34 (-6.33%)</td><td>141.00 (-14.80%)</td><td>134.90 (-0.81%)</td><td>28.58 (-5.22%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>208.10 (n/a)</td><td>169.04 (n/a)</td><td>165.50 (n/a)</td><td>136.00 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.39 (-18.40%)</td><td>0.36 (-5.82%)</td><td>0.34 (-3.75%)</td><td>0.33 (-0.53%)</td><td>0.03 <b>(-54.07%)</b></td><td>199.90 (+0.50%)</td><td>184.94 (+4.75%)</td><td>191.90 (+3.90%)</td><td>168.30 <b>(+22.58%)</b></td><td>14.19 <b>(-43.89%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>198.90 (n/a)</td><td>176.56 (n/a)</td><td>184.70 (n/a)</td><td>137.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.46 (+1.59%)</td><td>0.36 (+0.55%)</td><td>0.34 (+3.34%)</td><td>0.28 (-8.54%)</td><td>0.07 (+16.04%)</td><td>237.50 (+9.35%)</td><td>189.18 (+0.32%)</td><td>194.00 (-3.24%)</td><td>143.40 (-1.58%)</td><td>35.20 <b>(+25.56%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.06 (n/a)</td><td>217.20 (n/a)</td><td>188.58 (n/a)</td><td>200.50 (n/a)</td><td>145.70 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.53 <b>(+21.82%)</b></td><td>0.43 (+9.92%)</td><td>0.46 (+15.07%)</td><td>0.32 (-12.52%)</td><td>0.08 <b>(+224.06%)</b></td><td>203.90 (+14.29%)</td><td>155.42 (-6.50%)</td><td>143.20 (-13.05%)</td><td>124.00 (-17.94%)</td><td>31.66 <b>(+208.86%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.02 (n/a)</td><td>178.40 (n/a)</td><td>166.22 (n/a)</td><td>164.70 (n/a)</td><td>151.10 (n/a)</td><td>10.25 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.89 (-17.62%)</td><td>0.68 (-19.51%)</td><td>0.67 <b>(-23.03%)</b></td><td>0.52 <b>(-20.54%)</b></td><td>0.14 <b>(-26.46%)</b></td><td>254.50 <b>(+25.87%)</b></td><td>198.78 <b>(+23.21%)</b></td><td>195.60 <b>(+29.97%)</b></td><td>146.60 <b>(+21.36%)</b></td><td>38.27 (+7.44%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.09 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.65 (n/a)</td><td>0.19 (n/a)</td><td>202.20 (n/a)</td><td>161.34 (n/a)</td><td>150.50 (n/a)</td><td>120.80 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.01 (+7.36%)</td><td>0.81 (+16.38%)</td><td>0.83 (+15.25%)</td><td>0.53 <b>(+27.51%)</b></td><td>0.19 (-3.68%)</td><td>248.70 <b>(-21.57%)</b></td><td>170.60 (-16.11%)</td><td>157.40 (-13.23%)</td><td>129.10 (-6.92%)</td><td>47.12 <b>(-30.94%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.72 (n/a)</td><td>0.41 (n/a)</td><td>0.19 (n/a)</td><td>317.10 (n/a)</td><td>203.36 (n/a)</td><td>181.40 (n/a)</td><td>138.70 (n/a)</td><td>68.23 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>1.11 (+0.14%)</td><td>0.85 (+2.00%)</td><td>0.81 (+2.85%)</td><td>0.65 (-5.38%)</td><td>0.17 (+3.45%)</td><td>200.90 (+5.68%)</td><td>158.20 (-1.60%)</td><td>161.10 (-2.78%)</td><td>117.70 (-0.17%)</td><td>29.86 (+12.06%)</td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>1.11 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.16 (n/a)</td><td>190.10 (n/a)</td><td>160.78 (n/a)</td><td>165.70 (n/a)</td><td>117.90 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.95 <b>(+36.69%)</b></td><td>0.71 (+9.69%)</td><td>0.74 (+12.74%)</td><td>0.49 (-18.57%)</td><td>0.17 <b>(+328.51%)</b></td><td>269.50 <b>(+22.84%)</b></td><td>192.18 (-4.74%)</td><td>177.80 (-11.32%)</td><td>138.10 <b>(-26.85%)</b></td><td>48.47 <b>(+294.96%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.69 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.60 (n/a)</td><td>0.04 (n/a)</td><td>219.40 (n/a)</td><td>201.74 (n/a)</td><td>200.50 (n/a)</td><td>188.80 (n/a)</td><td>12.27 (n/a)</td>
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
<td><code>c42605d</code> — 2026-07-31 23:21:39</td><td>0.12 (+3.09%)</td><td>0.10 (+11.73%)</td><td>0.09 (+4.57%)</td><td>0.09 <b>(+32.72%)</b></td><td>0.01 <b>(-29.65%)</b></td><td>182.40 <b>(-24.66%)</b></td><td>164.78 (-12.14%)</td><td>172.50 (-4.38%)</td><td>140.50 (-2.97%)</td><td>18.64 <b>(-48.99%)</b></td>
</tr>
<tr>
<td><code>2df13d5</code> — 2026-07-31 22:32:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.10 (n/a)</td><td>187.54 (n/a)</td><td>180.40 (n/a)</td><td>144.80 (n/a)</td><td>36.54 (n/a)</td>
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
