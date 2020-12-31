//
// Created by HosodaMath on 2020/12/29.
//

#include "Point.hpp"
namespace svg {
    [[nodiscard]] std::string Point::drawPoint() const noexcept {
        set::circle::SetCircle circle_set(location);

        auto start = set::circle::SetCircle::set_start();
        auto cx = circle_set.set_cx();
        auto cy = circle_set.set_cy();
        auto r = set::circle::SetCircle::set_r(3.0);
        auto fill_color = set::circle::SetCircle::set_fill("#000000", 1.0);
        auto end = set::circle::SetCircle::set_end();

        auto ans = start + cx + cy + r + fill_color + end;

        return ans;
    }
}