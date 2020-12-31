//
// Created by HosodaMath on 2020/12/31.
//

#pragma once
#include <iostream>
#include <string>
#include "Vector.hpp"
namespace set::line {
    class SetLine {
    private:
        math::Vector2 location1;
        math::Vector2 location2;
    public:
        constexpr SetLine() = default;

        constexpr explicit SetLine(math::Vector2 init_location1, math::Vector2 init_location2) :
            location1(init_location1), location2(init_location2) {}

        [[nodiscard]] static std::string set_start() noexcept;

        [[nodiscard]] static std::string set_end() noexcept;

        [[nodiscard]] std::string set_x() const noexcept;

        [[nodiscard]] std::string set_y() const noexcept;

        [[nodiscard]] static std::string set_stroke(const std::string &stroke_color,double stroke_width, double stroke_opacity) noexcept;
    };
}