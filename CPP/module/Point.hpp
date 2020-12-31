//
// Created by HosodaMath on 2020/12/29.
//

#pragma once
#include <iostream>
#include <string>
#include "SetCircle.hpp"

namespace svg {

    class Point {
    private:
        math::Vector2 location;

    public:
        ///点を表すデフォルトクラス
        Point() noexcept = default;

        ///点を表すクラス
        ///example
        ///double width = 512.0;
        ///double height = width;
        ///math::Vector2 location(width, height);
        ///svg::Point point(location);
        constexpr explicit Point(math::Vector2 init_location) : location(init_location) {}

        ///点を描く
        [[nodiscard]] std::string drawPoint() const noexcept;

    };
}