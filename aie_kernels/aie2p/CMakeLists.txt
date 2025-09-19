# Licensed under the Apache License, Version 2.0 (the License); you may
# not use this file except in compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


# SPDX-FileCopyrightText:	Copyright (c) 2025, Advanced Micro Devices, Inc. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

add_aie_kernel(silu.o SOURCES silu.cc)
add_aie_kernel(rms_norm.o SOURCES rms_norm.cc)
add_aie_kernel(rope.o SOURCES rope.cc)
add_aie_kernel(softmax.o SOURCES softmax.cc) 
add_aie_kernel(layer_norm.o SOURCES layer_norm.cc) 
add_aie_kernel(relu.o SOURCES relu.cc)
add_aie_kernel(mv.o SOURCES mv.cc)
add_aie_kernel(gelu.o SOURCES gelu.cc)
