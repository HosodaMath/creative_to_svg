pub mod point {
  ///# 点を表す構造体
  pub struct Point {
      x : f64,
      y : f64,
  }
  impl Point {
      /// ## 変数の初期化を行う(コンストラクタ)
      /// ### variable
      /// init_x : f64 x座標の初期化
      /// init_y : f64 y座標の初期化
      /// ### Example
      /// let point1 = Point::new(0.0, 0.0)
      ///
      pub fn new(init_x: f64, init_y: f64) -> Point{
          Point{x: init_x, y: init_y}
      }
  }

  impl Point {
      ///# ゲッター
      /// xとyの座標を取得
      pub fn get_x(&self) -> f64 {
          return self.x;
      }

      pub fn get_y(&self) -> f64 {
          return self.y;
      }
  }

  impl Point {
      ///# pointのsvgコードを出力
      ///## Example
      ///### 出力したい場合
      /// let point1 = Point::new(0.0, 0.0);
      /// println!(point1.point());
      /// ### svg形式で出したい場合は
      /// let point1 = Point::new(0.0, 0.0);
      /// data = point1.point()
      pub fn draw_point(&self) -> String {
          let start = format!("<circle");
          let location = format!(" cx=\"{}\" cy=\"{}\"", self.x, self.y);
          let others = format!(" r=\"{}\" fill=\"black\"", 3,);
          let end = format!(" />\n");
          let point_draw  = start + &*location + &*others + &*end;

          return point_draw;
      }
  }
}