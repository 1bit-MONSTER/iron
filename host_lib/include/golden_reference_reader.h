/*
 * SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef GOLDEN_MODEL_READER_H
#define GOLDEN_MODEL_READER_H

#include <any>
#include <fstream>
#include <map>
#include <stdfloat>
#include <string>
#include <utility>
#include <vector>

constexpr uint16_t golden_reference_magic = 0x507D;

struct __attribute__((packed)) GoldenReferenceBufferHeader {
    char name[48];
    uint16_t dtype;
    uint64_t len; // length of the following data in bytes
};

struct __attribute__((packed)) GoldenReferenceHeader {
    uint16_t magic;
    uint64_t len; // total file length, including this header
    uint16_t nReferences;
};

struct GoldenReference {
    struct Buffer {
        enum class DType { Bf16 = 1, F32 = 2, Ui8 = 3 };

        DType dtype;
        std::any data;
    };
    std::map<std::string, Buffer> references;

    static GoldenReference fromFile(std::string path);
    template <typename T> std::vector<T> *get(std::string name);
};

GoldenReference GoldenReference::fromFile(std::string path)
{
    GoldenReference ret = {};
    std::ifstream in_file(path, std::ios::binary);
    in_file.exceptions(std::ifstream::failbit | std::ifstream::badbit);
    if (!in_file.is_open()) {
        throw std::invalid_argument(path + ": unable to open file");
    }
    size_t pos = 0;
    struct GoldenReferenceHeader header = {};
    in_file.read(reinterpret_cast<char *>(&header), sizeof(header));
    pos += sizeof(header);
    if (golden_reference_magic != header.magic) {
        throw std::invalid_argument(path + ": Not a golden reference file (bad magic number)");
    }
    while (pos < header.len) {
        struct GoldenReferenceBufferHeader buf_header = {};
        if (pos + sizeof(buf_header) >= header.len) {
            throw std::invalid_argument(path + ": Malformed file (remaining file shorter than next buffer header)");
        }
        in_file.read(reinterpret_cast<char *>(&buf_header), sizeof(buf_header));
        pos += sizeof(buf_header);
        if (pos >= header.len) {
            throw std::invalid_argument(path + ": Malformed file (remaining file shorter than next buffer)");
        }
        std::string name = buf_header.name;
        if (ret.references.count(name) > 0) {
            throw std::invalid_argument(path + ": Duplicate definition of buffer '" + buf_header.name + "'");
        }
        ret.references[name] = {.dtype = static_cast<Buffer::DType>(buf_header.dtype), .data = {}};
        char *data_ptr = nullptr;
        switch (ret.references[name].dtype) {
        case Buffer::DType::Bf16:
            ret.references[name].data =
                std::any(std::vector<std::bfloat16_t>(buf_header.len / sizeof(std::bfloat16_t)));
            data_ptr = reinterpret_cast<char *>(
                std::any_cast<std::vector<std::bfloat16_t>>(&ret.references[buf_header.name].data)->data());
            break;
        case Buffer::DType::F32:
            ret.references[name].data = std::any(std::vector<float>(buf_header.len / sizeof(float)));
            data_ptr = reinterpret_cast<char *>(
                std::any_cast<std::vector<float>>(&ret.references[buf_header.name].data)->data());
            break;
        case Buffer::DType::Ui8:
            ret.references[name].data = std::any(std::vector<std::uint8_t>(buf_header.len / sizeof(std::uint8_t)));
            data_ptr = reinterpret_cast<char *>(
                std::any_cast<std::vector<std::uint8_t>>(&ret.references[buf_header.name].data)->data());
            break;
        default:
            throw std::invalid_argument(path + ": invalid data type (" + std::to_string(buf_header.dtype) + ")");
            break;
        }
        in_file.read(data_ptr, buf_header.len);
        pos += buf_header.len;
    }
    return ret;
}

template <typename T> std::vector<T> *GoldenReference::get(std::string name)
{
    return std::any_cast<std::vector<T>>(&references[name].data);
}

#endif