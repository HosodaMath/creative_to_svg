#include "svg.hpp"
void testPoint(double width, double height){

    FileOperation file("test_point1.svg");

    svg::Base base(width, height);
    auto start = base.drawStart();

    std::cout << start << std::endl;

    math::Vector2 location(width / 2.0, height / 2.0);
    svg::Point point(location);
    auto ans = point.drawPoint();
    std::cout << ans << std::endl;

    auto end = svg::Base::drawEnd();
    std::cout << end << std::endl;

    std::vector<std::string> tag_data;
    tag_data.push_back(start);
    tag_data.push_back(ans);
    tag_data.push_back(end);
    file.file_write2(tag_data);
}

void testLine(double width, double height){
    FileOperation file("test_line1.svg");
    math::Vector2 location1(0, 0);
    math::Vector2 location2(width, height);

    svg::Base base(width, height);
    auto start = base.drawStart();
    std::cout << start << std::endl;

    svg::Line line(location1, location2);
    auto ans = line.drawLine("#000000", 5.0,1.0);
    std::cout << ans << std::endl;

    auto end = svg::Base::drawEnd();
    std::cout << end << std::endl;

    std::vector<std::string> tag_data;
    tag_data.push_back(start);
    tag_data.push_back(ans);
    tag_data.push_back(end);
    file.file_write2(tag_data);
}

int main() {
    double width = 512.0;
    double height = width;
    //testPoint(width, height);
    testLine(width, height);

    return 0;
}
