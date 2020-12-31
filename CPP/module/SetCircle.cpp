//
// Created by HosodaMath on 2020/12/29.
//

#include "SetCircle.hpp"

namespace set::circle {
        [[nodiscard]]  std::string SetCircle::set_start() noexcept {
            std::string start = "<circle";
            return start;
        }

        [[nodiscard]] std::string SetCircle::set_cx() const noexcept {
            std::string cx0 = " cx=\"";
            std::string cx1 = std::to_string(location.get_x());
            std::string cx2 = "\"";
            std::string cx = cx0 + cx1 + cx2;

            return cx;
        }

        [[nodiscard]] std::string SetCircle::set_cy() const noexcept {
            std::string cy0 = " cy=\"";
            std::string cy1 = std::to_string(location.get_y());
            std::string cy2 = "\"";
            std::string cy = cy0 + cy1 + cy2;

            return cy;
        }

        [[nodiscard]] std::string SetCircle::set_r(const double r) noexcept {
            std::string r0 = " r=\"";
            std::string r1 = std::to_string(r);
            std::string r2 = "\"";
            std::string radius = r0 + r1 + r2;

            return radius;
        }

        [[nodiscard]] std::string SetCircle::set_fill(const std::string &fill_color, double fill_opacity) noexcept {
            std::string f0 = " fill=\"";
            const std::string &f1 = fill_color;
            std::string f2 = "\"";

            std::string fo1 = " fill-opacity=\"";
            std::string fo = std::to_string(fill_opacity);
            std::string fo2 = "\"";

            std::string fill = f0 + f1 + f2 + fo1 + fo + fo2;

            return fill;
        }

        [[nodiscard]] std::string SetCircle::set_end() noexcept {
            std::string end = "/>\n";
            return end;
        }
    }