pub mod line {
  use crate::point::point::Point;
  ///# lineのSVGコードを出力するクラス
  pub struct Line {
    point1: Point,
    point2: Point,
  }

  impl Line {
    /// ## 変数の初期化を行う(コンストラクタ)
    ///
    /// ### variable 必要な変数
    /// init_point1 : Point 座標1の初期化
    /// init_point2 : Point 座標2の初期化
    ///
    /// ### Example
    /// let point1 = Point::new(0.0, 0.0);
    /// let point2 = Point::new(256.0, 256.0);
    /// let line1 = Line::new(0.0, 0.0);
    ///
    pub fn new(init_point1: Point, init_point2: Point) -> Line{
      Line {point1: init_point1, point2: init_point2}
    }
  }

  impl Line {
    /// ### svg形式のフォーマットされた文字列を返す
    /// stroke_color: String
    /// stroke_width: f64
    pub fn draw_line(&self, stroke_color: String, stroke_width: f64, stroke_opacity: f64) -> String{
      let start = format!("<line");
      let location_x = format!(" x1=\"{}\" x2=\"{}\"", self.point1.get_x(), self.point2.get_x());
      let location_y = format!(" y1=\"{}\" y2=\"{}\"", self.point1.get_y(), self.point2.get_y());
      let set_stroke = format!(" stroke=\"{}\" stroke-width=\"{}\" stroke-opacity=\"{}\"", stroke_color, stroke_width, stroke_opacity);
      let end = format!(" />\n");
      let line_draw = start + &*location_x + &*location_y + &*set_stroke + &*end;

      return line_draw;
    }
  }
}