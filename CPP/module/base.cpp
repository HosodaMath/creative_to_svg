//
// Created by HosodaMath on 2020/12/31.
//

#include "base.hpp"
namespace svg {

    std::string Base::drawStart() const noexcept {
        std::string start = "<svg xmlns=\"http://www.w3.org/2000/svg\"";
        std::string version = " version=\"1.1\"";
        std::string set_base = start + version;

        std::string set_width1 = " width=\"";
        std::string set_size_width = std::to_string(width);
        std::string set_width2 = "\"";
        std::string set_width = set_width1 + set_size_width + set_width2;

        std::string set_height1 = " height=\"";
        std::string set_size_height = std::to_string(height);
        std::string set_height2 = "\"";
        std::string set_height = set_height1 + set_size_height + set_height2;

        std::string end = ">\n";

        auto set_start = set_base + set_width + set_height + end;

        return set_start;

    }

    std::string Base::drawEnd() noexcept {
        return "</svg>\n";
    }
}