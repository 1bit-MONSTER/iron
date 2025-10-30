# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

add_aie_kernel(add.o SOURCES add.cc)
add_aie_kernel(axpy.o SOURCES axpy.cc)
add_aie_kernel(mul.o SOURCES mul.cc)
add_aie_kernel(mv.o SOURCES mv.cc)
add_aie_kernel(mem_copy.o SOURCES passThrough.cc)
add_aie_kernel(rope_0.o SOURCES rope.cc DEFINES "TWO_HALVES")
add_aie_kernel(rope_1.o SOURCES rope.cc DEFINES "INTERLEAVED")