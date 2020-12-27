pub mod polygon {
  use crate::point::point::Point;
  use crate::utility::convert_str::*;
  ///# Polygonを表す構造体
  pub struct Polygon {
      pub data: Vec<Point>,
  }

  impl Polygon {
      /// ## 変数の初期化を行う(コンストラクタ)
     /// ### variable
     /// init_data : Vec<Point> ポリゴンデータの初期化
     /// ### Example
     /// let polygon1 = Polygon::new(0.0, 0.0)
     ///
      pub fn new(init_data: Vec<Point>) -> Polygon {

          Polygon { data: init_data }
      }
  }


  impl Polygon {
      /// ## ポリゴンタグデータの取得
      /// 設定パラメータ fill fill-opacity
      /// fill_color: fill
      /// fill_opacity: fill-opacity
      ///
      pub fn render_polygon1(self, fill_color: String, fill_opacity: f64) -> String{
          let str_data = format_one(self.data);
          let start = "<polygon";
          let location_data = format!("points=\"{}\"", str_data);
          let fill_set = format!("fill=\"{}\" fill-opacity=\"{}\"",
                                 fill_color, fill_opacity);
          let end = "/>\n";
          let poly1 = format!("{} {} {} {}", start, location_data, fill_set, end);

          return poly1;
      }
  }

  impl Polygon {
      /// ## ポリゴンタグデータの取得
      /// 設定パラメータ fill fill-opacity stroke stroke-width stroke-opacity
      /// fill_color: String fill
      /// fill_opacity: f64 fill-opacity
      /// stroke_color: String stroke
      /// stroke_width: f64 stroke-width
      /// stroke_opacity: f64 stroke-opacity
      ///
      pub fn render_polygon2(self, fill_color: String, fill_opacity: f64,
                             stroke_color: String, stroke_width: f64, stroke_opacity: f64) -> String{
          let str_data = format_one(self.data);
          let start = "<polygon";
          let location_data = format!("points=\"{}\"", str_data);
          let fill_set = format!("fill=\"{}\" fill-opacity=\"{}\"",
                                 fill_color, fill_opacity);
          let stroke_set = format!("stroke=\"{}\" stroke-width=\"{}\" stroke-opacity=\"{}\"",
                                   stroke_color, stroke_width, stroke_opacity);
          let end = "/>\n";
          let poly2 = format!("{} {} {} {} {}", start, location_data, fill_set, stroke_set, end);

          return poly2;
      }
  }

  impl Polygon {
      /// ## ポリゴンタグデータの取得
      /// 設定パラメータ stroke stroke-width stroke-opacity
      /// stroke_color: String stroke
      /// stroke_width: f64 stroke-width
      /// stroke_opacity: f64 stroke-opacity
      pub fn render_polygon3(self, stroke_color: String, stroke_width: f64, stroke_opacity: f64) -> String{
          let str_data = format_one(self.data);
          let start = "<polygon";
          let location_data = format!("points=\"{}\"", str_data);
          let fill_set = format!("fill=\"transparent\"");
          let stroke_set = format!("stroke=\"{}\" stroke-width=\"{}\" stroke-opacity=\"{}\"",
                                   stroke_color, stroke_width, stroke_opacity);
          let end = "/>\n";
          let poly3 = format!("{} {} {} {} {}", start, location_data, fill_set, stroke_set, end);

          return poly3;
      }
  }
}