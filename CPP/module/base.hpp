//
// Created by HosodaMath on 2020/12/31.
//
#pragma once
#include <iostream>
#include <string>
#include <vector>
namespace svg {

    class Base {
    private:
        double width;
        double height;

    public:
        Base() noexcept = default;
        constexpr Base(double init_width, double init_height) : width(init_width), height(init_height) {}
        [[nodiscard]] std::string drawStart() const noexcept;
        [[nodiscard]] static std::string drawEnd() noexcept;

    };

}