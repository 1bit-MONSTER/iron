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


include_guard()

option(IRONCLAD_WERROR "Make all warnings into errors." ON)


function(ironclad_compiler_options TARGET)
    set_target_properties(${TARGET}
        PROPERTIES
            CXX_STANDARD                23
            CXX_STANDARD_REQUIRED       ON
            CXX_EXTENSIONS              OFF
            CXX_VISIBILITY_PRESET       hidden
            HIP_STANDARD                23
            HIP_STANDARD_REQUIRED       ON
            HIP_EXTENSIONS              OFF
            VISIBILITY_INLINES_HIDDEN   ON
            POSITION_INDEPENDENT_CODE   ON
    )
    target_compile_features(${TARGET}
        PUBLIC
            cxx_std_23)
endfunction()

function(ironclad_compiler_warnings TARGET)
    target_compile_options(${TARGET} INTERFACE
        $<$<CXX_COMPILER_ID:MSVC>:/W4 /WX>
        $<$<NOT:$<CXX_COMPILER_ID:MSVC>>:-Wall -Wextra -Wpedantic $<$<BOOL:${IRONCLAD_WERROR}>:-Werror>>
    )
endfunction()
