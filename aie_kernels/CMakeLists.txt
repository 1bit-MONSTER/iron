# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

add_subdirectory(aie1)
if (IRONCLAD_AIE_TARGET STREQUAL "aie2")
  add_subdirectory(aie2)
endif ()
if (IRONCLAD_AIE_TARGET STREQUAL "aie2p")
  add_subdirectory(aie2p)
endif ()
add_subdirectory(generic)