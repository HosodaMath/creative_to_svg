//
// Created by HosodaMath on 2020/12/29.
//

#include "Line.hpp"
namespace svg {
    [[nodiscard]] std::string Line::drawLine(const std::string& stroke_color, double stroke_width, double stroke_opacity) const noexcept {
        set::line::SetLine line(location1, location2);
        auto start = set::line::SetLine::set_start();
        auto end = set::line::SetLine::set_end();
        auto location_x = line.set_x();
        auto locaiton_y = line.set_y();
        auto stroke = set::line::SetLine::set_stroke(stroke_color, stroke_width,stroke_opacity);

        auto draw_line = start + location_x + locaiton_y + stroke + end;

        return draw_line;
    }
}