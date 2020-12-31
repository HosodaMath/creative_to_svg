//
// Created by HosodaMath on 2020/12/31.
//

#include "file_operation.h"

void FileOperation::file_write1(const std::string& svg_tag_data) {
    std::ofstream out_svg(file_name);
    if(!out_svg) {
        std::cerr << "Error";
    } else {
        out_svg << svg_tag_data;
        //out_svg.close();
    }


}

void FileOperation::file_write2(const std::vector<std::string>& svg_tag_data) {
    std::ofstream out_svg(file_name);
    if(!out_svg) {
        std::cerr << "Error";
    } else {
        for(auto & count : svg_tag_data) {
            out_svg << count;
        }
        //out_svg.close();
    }
}
