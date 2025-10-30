# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

# Configuration variables
set(num_KV_heads 0)

set(heads 1)
set(S_q 2048)
set(S_kv 2048)
set(d 64)
set(B_q 64)
set(k 64)
set(B_kv 64)
set(dtype "bf16")

set(verbose 1)
set(trace_size 65536)
set(device_name "npu2")
set(design_name "mha")

set(currentDesignTarget ${design_name})

# Derived variables
set(target_suffix "${heads}_${S_q}_${S_kv}_${d}_${B_q}x${d}x${B_kv}")

set(mm_kernel "mm_${B_q}x${d}x${B_kv}_${dtype}_${dtype}")
set(softmax_kernel "softmax_${B_kv}_${dtype}_${dtype}")
set(mha_kernel "mha_${heads}_${S_q}_${S_kv}_${d}_${B_q}x${d}x${B_kv}_${dtype}")
set(passthrough_kernel "passthrough_${B_q}x${B_kv}_${dtype}")

set(build_dir "${CMAKE_BINARY_DIR}/aie")

if(verbose STREQUAL "1")
    set(verbose_string "--verbose")
else()
    set(verbose_string "")
endif()

# Data type mappings
set(dtype_cpp "std::bfloat16_t")

# Display configuration
message(STATUS "Registering Executable: ${currentDesignTarget}")
message(STATUS "    Heads: ${heads}")
message(STATUS "    Number of KV Heads: ${num_KV_heads}")
message(STATUS "    Sequence Length Q: ${S_q}")
message(STATUS "    Sequence Length KV: ${S_kv}")
message(STATUS "    Embedding Dimension d: ${d}")
message(STATUS "    Tile dimensions: ${B_q}x${d}x${B_kv}")
message(STATUS "    Data type: ${dtype}")
message(STATUS "    Device: ${device_name}")
message(STATUS "    Design: ${design_name}")
message(STATUS "    Verbose mode: ${verbose}")

set(CMAKE_C_COMPILER gcc-13)
set(CMAKE_CXX_COMPILER g++-13)
set(XRT_INC_DIR /opt/xilinx/xrt/include CACHE STRING "Path to XRT include")
set(XRT_LIB_DIR /opt/xilinx/xrt/lib CACHE STRING "Path to XRT libraries")

# Find required tools
find_program(python_executable python REQUIRED)
find_program(aiecc_executable aiecc.py REQUIRED)

# Path configuration
set(kernels_dir_aie2 "${CMAKE_SOURCE_DIR}/aie_kernels/aie2")
set(kernels_dir "${CMAKE_SOURCE_DIR}/aie_kernels/aie2p")
set(kernels_generic_dir "${CMAKE_SOURCE_DIR}/aie_kernels/generic")

find_program(aieopt_dir aie-opt)

if(aieopt_dir)
    # Get the parent directory of the binary
    get_filename_component(mlir_aie_bin_dir ${aieopt_dir} DIRECTORY)
    # Get the parent directory of the parent directory
    get_filename_component(mlir_aie_dir ${mlir_aie_bin_dir} DIRECTORY)
else()
    message(FATAL_ERROR "aie-opt not found in PATH")
endif()

# Build artifact paths
set(golden_ref_header "${build_dir}/golden_reference.h")
set(mlir_target "${build_dir}/aie_${target_suffix}.mlir")
set(xclbin_target "${build_dir}/mha.xclbin")
set(insts_target "${build_dir}/mha.bin")

set(kernels_archive "${build_dir}/kernels.a")

### Kernel compilation ###
add_aie_kernel(${mm_kernel} SOURCES ${kernels_dir}/mm.cc DEFINES 
    "B_COL_MAJ"
    "${dtype}_${dtype}_ONLY"
    "DIM_M=${B_q}"
    "DIM_K=${d}"
    "DIM_N=${B_kv}"
    "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16"
    OUTPUT_OBJECT MM_OBJ
)

add_aie_kernel(${mm_kernel}_rowmaj SOURCES ${kernels_dir}/mm.cc DEFINES
    "${dtype}_${dtype}_ONLY"
    "DIM_M=${B_q}"
    "DIM_K=${d}"
    "DIM_N=${B_kv}"
    "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16"
    OUTPUT_OBJECT MM_ROWMAJ_OBJ
)

add_aie_kernel(${softmax_kernel} SOURCES ${kernels_dir}/softmax.cc
    OUTPUT_OBJECT SOFTMAX_OBJ
)

add_aie_kernel(${mha_kernel} SOURCES ${kernels_dir}/mha.cc
    OUTPUT_OBJECT MHA_OBJ
)

add_aie_kernel(${passthrough_kernel} SOURCES ${kernels_generic_dir}/passThrough.cc DEFINES
    "BIT_WIDTH=16"
    OUTPUT_OBJECT PASSTHROUGH_OBJ
)

# Rename symbols in row-major object file
add_custom_command(
    OUTPUT ${MM_ROWMAJ_OBJ}_renamed
    COMMAND llvm-objcopy-18 --redefine-sym matmul_bf16_bf16=matmul_bf16_bf16_rowmaj
    --redefine-sym matmul_scalar_bf16_bf16=matmul_scalar_bf16_bf16_rowmaj
    --redefine-sym zero_bf16=zero_bf16_rowmaj
    --redefine-sym zero_scalar_bf16=zero_scalar_bf16_rowmaj
    ${MM_ROWMAJ_OBJ} ${MM_ROWMAJ_OBJ}_renamed
    DEPENDS ${MM_ROWMAJ_OBJ}
    COMMENT "Renaming matmul_bf16_bf16 to matmul_bf16_bf16_rowmaj"
    )
    
set(KERNEL_OBJ_LIST
    ${MM_OBJ}
    ${MM_ROWMAJ_OBJ}_renamed
    ${SOFTMAX_OBJ}
    ${MHA_OBJ}
    ${PASSTHROUGH_OBJ}
)

add_custom_command(
        OUTPUT ${kernels_archive}
        COMMAND ar rvs ${kernels_archive} ${KERNEL_OBJ_LIST} > /dev/null
        DEPENDS ${KERNEL_OBJ_LIST}
        COMMENT "Creating kernels archive"
)

add_custom_target("kernels.a" DEPENDS ${kernels_archive})

add_aie_executable(${currentDesignTarget} 
    HOST test.cpp
    PYTHON mha.py
    PYTHON_FLAGS 
        --heads ${heads}
        --S_q ${S_q} --S_kv ${S_kv} -d ${d}
        --B_q ${B_q} --B_kv ${B_kv}
        --num_KV_heads ${num_KV_heads}
        --trace_size 0 ${verbose_string}
        --output-file-path ${build_dir}/${currentDesignTarget}.mlir
    AIE_CORE_KERNELS "kernels.a"
    OUTPUT_HOST MHA_HOST
    OUTPUT_XCLBIN MHA_XCLBIN
    OUTPUT_INSTS MHA_INSTS
)

add_golden_reference_generator(${currentDesignTarget} 
    ${CMAKE_CURRENT_SOURCE_DIR}/mha_golden.py
    ${build_dir}
    --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d}
    --num_KV_heads ${num_KV_heads}
    --dtype ${dtype}
    ${verbose_string}
)

add_aie_ci_test(${currentDesignTarget}
    RUN
        "${MHA_HOST} -x ${MHA_XCLBIN} -i ${MHA_INSTS} -k ${currentDesignTarget} --heads ${heads} --S_q ${S_q} --S_kv ${S_kv} -d ${d} -v 2 --warmup 1 --iters 1 --verbosity ${verbose}"
    CHECK
        "PASS!"
    METRICS
        "Latency" [=[Avg NPU matmul time: (?P<metric>\d+)us]=]
        "Bandwidth" [=[Avg Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=]
        "GFLOP/s" [=[Avg NPU gflops: (?P<metric>[\d\.e\+-]+)]=]
)
