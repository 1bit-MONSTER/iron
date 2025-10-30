# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

function(add_aie_gemm_design M K N m k n NUM_COLUMNS TRACE_SIZE ARCHIVE_NAME)

    set(EXAMPLE "gemm_${M}_M_${K}_K_${N}_N_${NUM_COLUMNS}_cols_${TRACE_SIZE}")
    set(GOLDEN_VALUES_PATH "${CMAKE_BINARY_DIR}/example/gemm/golden_${EXAMPLE}")
    set(INPUT_DATA_TYPE_PYTHON bf16)
    set(OUTPUT_DATA_TYPE_PYTHON bf16)
    set(INPUT_DATA_TYPE_CPP bfloat16_t)
    set(OUTPUT_DATA_TYPE_CPP bfloat16_t)
    
    set(PY_FLAGS "--dev" "${DEVICE}" "-M" "${M}" "-K" "${K}" "-N" "${N}" "-m" "${m}" "-k" "${k}" "-n" "${n}" "--n-aie-cols" "${NUM_COLUMNS}" "--dtype_in" "${INPUT_DATA_TYPE_PYTHON}" "--dtype_out" "${OUTPUT_DATA_TYPE_PYTHON}" "--trace_size" "${TRACE_SIZE}" "--prio-accuracy")
    add_aie_executable(${EXAMPLE} 
                       HOST gemm.cpp
                       HOST_FLAGS DTYPE_IN=${INPUT_DATA_TYPE_CPP} DTYPE_OUT=${OUTPUT_DATA_TYPE_CPP}
                       PYTHON gemm.py
                       PYTHON_FLAGS --dev ${DEVICE} -M ${M} -K ${K} -N ${N} -m ${m} -k ${k} -n ${n} --n-aie-cols ${NUM_COLUMNS} --dtype_in ${INPUT_DATA_TYPE_PYTHON} --dtype_out ${OUTPUT_DATA_TYPE_PYTHON} --trace_size ${TRACE_SIZE} ${EMULATE_STR} --prio-accuracy ${PRIO_ACCURACY} --output-file-path ${CMAKE_BINARY_DIR}/aie/${EXAMPLE}.mlir
                       AIE_CORE_KERNELS ${ARCHIVE_NAME}
                       OUTPUT_HOST GEMM_HOST
                       OUTPUT_XCLBIN GEMM_XCLBIN
                       OUTPUT_INSTS GEMM_INSTS)
                       
    add_golden_reference_generator(${EXAMPLE} 
        ${CMAKE_CURRENT_SOURCE_DIR}/gemm_golden.py
        ${GOLDEN_VALUES_PATH}
        -M ${M}
        -K ${K}
        -N ${N}
    )

    add_aie_ci_test(${EXAMPLE}
                    RUN 
                        "${GEMM_HOST} -k ${EXAMPLE} -x ${GEMM_XCLBIN} -i ${GEMM_INSTS} --rows ${M} --inner ${K} --columns ${N}"
                    CHECK
                        "PASS!"
                    METRICS 
                        "Latency" [=[Latency \(us\): (?P<metric>\d+)]=]
                        "Bandwidth" [=[Effective Bandwidth: (?P<metric>[\d\.e\+-]+) GB/s]=])
endfunction()

# TODO: Do we need to add support for col major?
# set(B_COL_MAJ_LIST "0" "1")
# set(C_COL_MAJ_LIST "0" "1")

set(M_LIST "2048")
set(K_LIST "2048")
set(N_LIST "2048")

# Fix the AIE core tile dimensions
# TODO: Do we need to sweep through a list of them instead?  
set(m "64")
set(k "64")
set(n "64")

set(ARCHIVE_NAME "gemm_${m}x${k}x${n}_archive.a")
set(AIE_BUILD_DIR ${CMAKE_BINARY_DIR}/aie)
set(ARCHIVE_PATH "${AIE_BUILD_DIR}/${ARCHIVE_NAME}")

set(EMULATE_BFLOAT16_MMUL_WITH_BFP16 False)

if (EMULATE_BFLOAT16_MMUL_WITH_BFP16)
    set(EMULATE_STR --emulate-bf16-mmul-with-bfp16)
    add_aie_kernel("gemm_${m}x${k}x${n}" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/aie2p/mm.cc DEFINES "DIM_M=${m}" "DIM_K=${k}" "DIM_N=${n}" "bf16_f32_ONLY" "AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16" OUTPUT_OBJECT MM_OBJ)
else()
    add_aie_kernel("gemm_${m}x${k}x${n}" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/aie2p/mm.cc DEFINES "DIM_M=${m}" "DIM_K=${k}" "DIM_N=${n}" "bf16_f32_ONLY" OUTPUT_OBJECT MM_OBJ)
endif()

add_aie_kernel("convert_copy" SOURCES ${CMAKE_SOURCE_DIR}/aie_kernels/aie2p/convert_copy.cc OUTPUT_OBJECT CONVERT_OBJ)

set(KERNEL_OBJ_LIST
    ${MM_OBJ}
    ${CONVERT_OBJ}
)

add_custom_command(
    OUTPUT ${ARCHIVE_PATH}
    COMMAND ${CMAKE_AR} rvs ${ARCHIVE_PATH} ${KERNEL_OBJ_LIST}
    DEPENDS ${KERNEL_OBJ_LIST}
    COMMENT "Creating static library ${ARCHIVE_PATH}"
    VERBATIM
)

add_custom_target(${ARCHIVE_NAME} DEPENDS ${ARCHIVE_PATH})

set(TRACE_SIZE "0")
if(EXTENSIVE_TESTING) 
    list(APPEND K_LIST 8192)
    list(APPEND K_LIST 64)
    list(APPEND N_LIST 8192)
endif()

# Determine max cores based on device
if(IRONCLAD_AIE_TARGET STREQUAL aie2p)
    set(AIE_COLS_LIST 1 2 4 8)
else()
    set(AIE_COLS_LIST 1 2 4)
endif()

foreach(M IN LISTS M_LIST)
    foreach(K IN LISTS K_LIST)
        foreach(N IN LISTS N_LIST)
            # GEMM of {sequence length}*8192*8192 doesn't occur with the model, so skipping it to save time
            if(N EQUAL 8192 AND K EQUAL 8192)
                continue()
            endif()

            # Calculate matrix dimensions
            math(EXPR N_REDUCTIONS "${N} / ${n}")
            set(NUM_COLUMNS 0)

            foreach(V IN LISTS AIE_COLS_LIST)
                math(EXPR RESULT "${N_REDUCTIONS} % ${V}")
                if(RESULT EQUAL 0)
                    set(NUM_COLUMNS ${V})
                endif()
            endforeach()
            add_aie_gemm_design(${M} ${K} ${N} ${m} ${k} ${n} ${NUM_COLUMNS} ${TRACE_SIZE} ${ARCHIVE_NAME})
        endforeach()
    endforeach()
endforeach()