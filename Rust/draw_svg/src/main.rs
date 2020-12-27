use draw_svg::file_operation::svg2::SVG2;
use draw_svg::point::point::Point;
//use draw_svg::line::line::Line;
use draw_svg::rect::rect::Rect;
use std::fs::File;

/*
fn render_point(width: f64, height: f64){
    let file_path_name = "svg_data_point/point1.svg";
    let file = File::create(file_path_name).expect("file not found.");
    let mut svg = SVG2::new(file);
    
    let point = Point::new(width / 2.0, height / 2.0);
    let tmp = point.draw_point();
    svg.plot_start2(width, height);
    svg.draw(tmp);
    svg.plot_end2();
}

fn render_line1(width: f64, height: f64){
    let file_path_name = "svg_data_line/line1.svg";
    let file = File::create(file_path_name).expect("file not found.");
    let mut svg = SVG2::new(file);
    
    let point1 = Point::new(0.0, height / 2.0);
    let point2 = Point::new(width, height / 2.0);
    let line1 = Line::new(point1, point2);
    let tmp_data1 = line1.draw_line("#000000".to_string(), 3.0, 1.0);

    let point3 = Point::new(width / 2.0, 0.0);
    let point4 = Point::new(width / 2.0, height);
    let line2 = Line::new(point3, point4);
    let tmp_data2 = line2.draw_line("#000000".to_string(), 3.0, 1.0);

    svg.plot_start2(width, height);
    svg.draw(tmp_data1);
    svg.draw(tmp_data2);
    svg.plot_end2();
}
*/

fn render_rect1(width: f64, height: f64){
    let file_path_name = "svg_data_rect/rect1.svg";
    let file = File::create(file_path_name).expect("file not found.");
    let mut svg = SVG2::new(file);

    let location = Point::new(128.0, 128.0);
    let length = Point::new(256.0, 256.0);
    let rect = Rect::new(location, length);
    let tmp_rect_data = rect.draw_rect1("#7fffd4".to_string(), 1.0);

    svg.plot_start2(width, height);
    svg.draw(tmp_rect_data);
    svg.plot_end2();
}   

fn render_rect2(width: f64, height: f64){
    let file_path_name = "svg_data_rect/rect2.svg";
    let file = File::create(file_path_name).expect("file not found.");
    let mut svg = SVG2::new(file);

    let location = Point::new(128.0, 128.0);
    let length = Point::new(256.0, 256.0);
    let rect = Rect::new(location, length);
    let tmp_rect_data = rect.draw_rect2("#7fffd4".to_string(), 1.0, "#000000".to_string(), 5.0, 1.0);

    svg.plot_start2(width, height);
    svg.draw(tmp_rect_data);
    svg.plot_end2();
}   

fn render_rect3(width: f64, height: f64){
    let file_path_name = "svg_data_rect/rect3.svg";
    let file = File::create(file_path_name).expect("file not found.");
    let mut svg = SVG2::new(file);

    let location = Point::new(128.0, 128.0);
    let length = Point::new(256.0, 256.0);
    let rect = Rect::new(location, length);
    let tmp_rect_data = rect.draw_rect3("#000000".to_string(), 5.0, 1.0);

    svg.plot_start2(width, height);
    svg.draw(tmp_rect_data);
    svg.plot_end2();
}   

fn main() {
    let width = 512.0;
    let height = width;
    //render_point(width, height);
    //render_line1(width, height);
    render_rect1(width, height);
    render_rect2(width, height);
    render_rect3(width, height);
}