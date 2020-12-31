//
// Created by HosodaMath on 2020/12/31.
//

#include "setLine.hpp"
namespace set::line {

    [[nodiscard]] std::string set::line::SetLine::set_start() noexcept {
        std::string start = "<line";
        return start;
    }

    [[nodiscard]] std::string set::line::SetLine::set_end() noexcept {
        std::string end = "/>\n";
        return end;
    }

    [[nodiscard]] std::string set::line::SetLine::set_x() const noexcept {
        std::string line_start_x1 = " x1=\"";
        std::string location_x1 = std::to_string(location1.get_x());
        std::string line_end_x1 = "\"";
        std::string line_x1 = line_start_x1 + location_x1 + line_end_x1;

        std::string line_start_x2 = " x2=\"";
        std::string location_x2 = std::to_string(location2.get_x());
        std::string line_end_x2 = "\"";
        std::string line_x2 = line_start_x2 + location_x2 + line_end_x2;

        std::string line_x = line_x1 + line_x2;

        return line_x;

    }

    [[nodiscard]] std::string set::line::SetLine::set_y() const noexcept {
        std::string line_start_y1 = " y1=\"";
        std::string location_y1 = std::to_string(location1.get_y());
        std::string line_end_y1 = "\"";
        std::string line_y1 = line_start_y1 + location_y1 + line_end_y1;

        std::string line_start_y2 = " y2=\"";
        std::string location_y2 = std::to_string(location2.get_y());
        std::string line_end_y2 = "\"";
        std::string line_y2 = line_start_y2 + location_y2 + line_end_y2;

        std::string line_y = line_y1 + line_y2;

        return line_y;
    }

    [[nodiscard]] std::string set::line::SetLine::set_stroke(const std::string &stroke_color,double stroke_width ,double stroke_opacity) noexcept {
        std::string s0 = " stroke=\"";
        const std::string &s1 = stroke_color;
        std::string s2 = "\"";

        std::string sw0 = " stroke-width=\"";
        std::string sw = std::to_string(stroke_width);
        std::string sw1 = "\"";

        std::string so1 = " stroke-opacity=\"";
        std::string so = std::to_string(stroke_opacity);
        std::string so2 = "\"";

        std::string fill = s0 + s1 + s2 + sw0 + sw + sw1 + so1 + so + so2;

        return fill;
    }

}