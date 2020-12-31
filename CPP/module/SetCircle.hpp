//
// Created by HosodaMath on 2020/12/29.
//
#pragma once
#include <iostream>
#include <string>
#include "Vector.hpp"
namespace set::circle {
        class SetCircle {
        private:
            math::Vector2 location;
        public:
            constexpr SetCircle() = default;

            constexpr explicit SetCircle(math::Vector2 init_location) : location(init_location) {}

            [[nodiscard]] static std::string set_start() noexcept;

            [[nodiscard]] static std::string set_end() noexcept;

            [[nodiscard]] std::string set_cx() const noexcept;

            [[nodiscard]] std::string set_cy() const noexcept;

            [[nodiscard]] static std::string set_r(double r) noexcept;

            [[nodiscard]] static std::string set_fill(const std::string &fill_color, double fill_opacity) noexcept;
        };
    }