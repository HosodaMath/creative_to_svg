//
// Created by HosodaMath on 2020/12/29.
//
#pragma once
#include "setLine.hpp"
namespace svg {

    class Line {
    private:
        math::Vector2 location1;
        math::Vector2 location2;
    public:
        Line() noexcept = default;

        ///Lineを表すクラス
        ///\author Shingo Hosoda
        ///\param init_location1 : Vector 座標1の初期化
        ///\param init_location2 : Vector 座標2の初期化
        ///\example
        ///double width = 512.0;
        ///double height = width;
        ///math::Vector2 location1(0, 0);
        ///math::Vector2 location2(width, height);
        ///svg::Line line(location1, location2);
        ///auto ans = line.drawLine("#000000", 1.0);
        constexpr Line(math::Vector2 init_location1, math::Vector2 init_location2) : location1(init_location1),
                                                                                     location2(init_location2) {}
        ///線を描く
        ///\param stroke_color : std::string 線の色
        ///\param stroke_width : double 線の太さ
        ///\param stroke_opacity : double アルファ値
        [[nodiscard]] std::string drawLine(const std::string& stroke_color, double stroke_width,double stroke_opacity) const noexcept;
    };

}