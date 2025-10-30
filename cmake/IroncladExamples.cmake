# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


include_guard()

include(${PROJECT_SOURCE_DIR}/cmake/IroncladCompilerOptions.cmake)

function(ironclad_add_example TARGET)
    add_executable(${TARGET} ${ARGN})
    target_link_libraries(${TARGET} PRIVATE ironclad::ironclad)
    ironclad_compiler_warnings(${TARGET})
    ironclad_compiler_options(${TARGET})
endfunction()
