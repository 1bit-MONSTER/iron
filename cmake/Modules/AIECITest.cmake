# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

include_guard()
include(${PROJECT_SOURCE_DIR}/cmake/IroncladCompilerOptions.cmake)

set(AIE_CI_TESTS "")
set(AIE_CI_TEST_PATHS "")

# Add a CI test for this repository that will check pass/no-pass and record some metrics.
#
# Args:
#     TARGET_NAME (string): A unique name for this test.
#     RUN (string): A command to execute as this test.
#     CHECK (string; optional): Consider the test as "passing" if all of the given regular expressions match the command output.
#     METRICS (string; optional): Format is a list of "metric_name 'metric_regex'". Capture the metrics given as regular expressions; use regex group "metric" as the metric.
#     
function(add_aie_ci_test
    TARGET_NAME  # Output target name
)

    set(options)
    set(oneValueArgs RUN)
    set(multiValueArgs CHECK METRICS)

    cmake_parse_arguments(ADD_AIE_CI_TEST "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(FILE_CONTENT "run = \'${ADD_AIE_CI_TEST_RUN}\'\n")
    set(FILE_CONTENT "${FILE_CONTENT}checks = \[\n")
    if(ADD_AIE_CI_TEST_CHECK)
        foreach(CHECK IN LISTS ADD_AIE_CI_TEST_CHECK)
            set(FILE_CONTENT "${FILE_CONTENT}    '${CHECK}',\n")
        endforeach()
    endif()
    set(FILE_CONTENT "${FILE_CONTENT}\]\n")
    set(FILE_CONTENT "${FILE_CONTENT}metrics = \[\n")
    if(ADD_AIE_CI_TEST_METRICS)
        while(ADD_AIE_CI_TEST_METRICS)
            list(POP_FRONT ADD_AIE_CI_TEST_METRICS METRIC_NAME)
            list(POP_FRONT ADD_AIE_CI_TEST_METRICS METRIC_REGEX)
            set(FILE_CONTENT "${FILE_CONTENT}    ('${METRIC_NAME}', r\"${METRIC_REGEX}\"),\n")
        endwhile()
    endif()
    set(FILE_CONTENT "${FILE_CONTENT}\]\n")

    file(GENERATE OUTPUT "${TARGET_NAME}.py" CONTENT "${FILE_CONTENT}")
    get_property(AIE_CI_TESTS GLOBAL PROPERTY AIE_CI_TESTS)
    list(APPEND AIE_CI_TESTS "${TARGET_NAME}")
    set_property(GLOBAL PROPERTY AIE_CI_TESTS ${AIE_CI_TESTS})
    get_property(AIE_CI_TEST_PATHS GLOBAL PROPERTY AIE_CI_TEST_PATHS)
    list(APPEND AIE_CI_TEST_PATHS "${CMAKE_CURRENT_BINARY_DIR}")
    set_property(GLOBAL PROPERTY AIE_CI_TEST_PATHS ${AIE_CI_TEST_PATHS})

    separate_arguments(ADD_AIE_CI_TEST_RUN)
    add_custom_target(${TARGET_NAME}_run
        COMMAND ${ADD_AIE_CI_TEST_RUN}
        DEPENDS ${TARGET_NAME}
        COMMENT "Running ${TARGET_NAME} test with ${ADD_AIE_CI_TEST_RUN}"
    )

endfunction()

function(generate_aie_ci_test_list PATH)
    get_property(AIE_CI_TESTS GLOBAL PROPERTY AIE_CI_TESTS)
    get_property(AIE_CI_TEST_PATHS GLOBAL PROPERTY AIE_CI_TEST_PATHS)
    set(FILE_CONTENT "tests = \[\n")

    foreach(TEST IN LISTS AIE_CI_TESTS)
        set(FILE_CONTENT "${FILE_CONTENT}    '${TEST}',\n")
    endforeach()
    
    set(FILE_CONTENT "${FILE_CONTENT}\]")
    set(FILE_CONTENT "${FILE_CONTENT}\npaths = \[\n")
    
    foreach(PATH IN LISTS AIE_CI_TEST_PATHS)
        set(FILE_CONTENT "${FILE_CONTENT}    '${PATH}',\n")
    endforeach()
    
    set(FILE_CONTENT "${FILE_CONTENT}\]\n")
    file(GENERATE OUTPUT "${PATH}" CONTENT "${FILE_CONTENT}")
endfunction()

function(add_golden_reference_generator TARGET_NAME PYTHON_SCRIPT_PATH GOLDEN_VALUES_PATH)
    # Parse additional arguments as python script arguments
    set(PYTHON_ARGS ${ARGN})
    
    add_custom_command(
        OUTPUT ${GOLDEN_VALUES_PATH}/golden_reference.h
        COMMAND ${Python3_EXECUTABLE} ${PYTHON_SCRIPT_PATH}
                ${PYTHON_ARGS}
                --output ${GOLDEN_VALUES_PATH}/golden_reference.h
        DEPENDS ${PYTHON_SCRIPT_PATH}
        COMMENT "Generating golden reference file: ${GOLDEN_VALUES_PATH}/golden_reference.h"
    )
    add_custom_target(${TARGET_NAME}_generate_golden_reference
        DEPENDS ${GOLDEN_VALUES_PATH}/golden_reference.h
        COMMENT "Generating golden reference for ${TARGET_NAME}"
    )
    add_dependencies(${TARGET_NAME} ${TARGET_NAME}_generate_golden_reference)
    target_include_directories(${TARGET_NAME} PRIVATE ${GOLDEN_VALUES_PATH})
endfunction()