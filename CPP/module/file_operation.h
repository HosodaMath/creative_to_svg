//
// Created by HosodaMath on 2020/12/31.
//

#pragma once
#include <iostream>
#include <vector>
#include <fstream>
#include <utility>

class FileOperation {
private:
    std::string file_name;
public:
    FileOperation() noexcept = default;

    /// constexprは使えない
    explicit FileOperation(std::string init_file_name) : file_name(std::move(init_file_name)) {}
    ///一つずつ書き込む
    void file_write1(const std::string& svg_tag_data);
    void file_write2(const std::vector<std::string>& svg_tag_data);
};