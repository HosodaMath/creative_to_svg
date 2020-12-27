pub mod rect {
  use crate::point::point::Point;
  ///# rectのSVGコードを出力するクラス
  pub struct Rect {
    location: Point,
    length: Point,
  }

  impl Rect {
    /// ## 変数の初期化を行う(コンストラクタ)
    ///
    /// ### variable 必要な変数
    /// init_location : Point 座標の初期化
    /// init_length : Point 矩形の横幅と高さの定義の初期化
    ///
    /// ### Example
    /// let location = Point::new(0.0, 0.0);
    /// let length = Point::new(256.0, 256.0);
    /// let rect = Rect::new(location, length);
    ///
    pub fn new(init_location: Point, init_length: Point) -> Rect{
      Rect {location: init_location, length: init_length}
    }
  }

  impl Rect {
    /// ### svg形式のフォーマットされた文字列を返す
    /// fill_color: String 塗りつぶしの色
    /// fill_opacity: f64 色の透明度
    pub fn draw_rect1(&self, fill_color: String, fill_opacity: f64) -> String{
      let start = format!("<rect");
      let location_svg = format!(" x=\"{}\" y=\"{}\"", self.location.get_x(), self.location.get_y());
      let length_svg = format!(" width=\"{}\" height=\"{}\"", self.length.get_x(), self.length.get_y());
      let set_fill = format!(" fill=\"{}\" fill-opacity=\"{}\"",fill_color, fill_opacity);
      let end = format!(" />\n");
      let rect_draw = start + &*location_svg + &*location_svg + &*length_svg + &*set_fill + &*end;

      return rect_draw;
    }
    
    /// ### svg形式のフォーマットされた文字列を返す
    /// fill_color: String 塗りつぶしの色
    /// fill_opacity: f64 色の透明度
    /// stroke_color: String ふちの色
    /// stroke_width: f64 ふちの太さ
    /// stroke_opacity: f64 ふちの色の透明度
    pub fn draw_rect2(&self, fill_color: String, fill_opacity: f64, stroke_color: String, stroke_width: f64, stroke_opacity: f64) -> String{
      let start = format!("<rect");
      let location_svg = format!(" x=\"{}\" y=\"{}\"", self.location.get_x(), self.location.get_y());
      let length_svg = format!(" width=\"{}\" height=\"{}\"", self.length.get_x(), self.length.get_y());
      let set_fill = format!(" fill=\"{}\" fill-opacity=\"{}\"",fill_color, fill_opacity);
      let set_stroke = format!(" stroke=\"{}\" stroke-width=\"{}\" stroke-opacity=\"{}\"", stroke_color, stroke_width, stroke_opacity);
      let end = format!(" />\n");
      let rect_draw = start + &*location_svg + &*location_svg + &*length_svg + &*set_fill + &*set_stroke + &*end;

      return rect_draw;
    }

    /// ### svg形式のフォーマットされた文字列を返す
    /// stroke_color: String ふちの色
    /// stroke_width: f64 ふちの太さ
    /// stroke_opacity: f64 ふちの色の透明度
    pub fn draw_rect3(&self, stroke_color: String, stroke_width: f64, stroke_opacity: f64) -> String{
      let start = format!("<rect");
      let location_svg = format!(" x=\"{}\" y=\"{}\"", self.location.get_x(), self.location.get_y());
      let length_svg = format!(" width=\"{}\" height=\"{}\"", self.length.get_x(), self.length.get_y());
      let set_fill = format!(" fill=\"none\"");
      let set_stroke = format!(" stroke=\"{}\" stroke-width=\"{}\" stroke-opacity=\"{}\"", stroke_color, stroke_width, stroke_opacity);
      let end = format!(" />\n");
      let rect_draw = start + &*location_svg + &*location_svg + &*length_svg + &*set_fill + &*set_stroke + &*end;

      return rect_draw;
    }
  }
}

