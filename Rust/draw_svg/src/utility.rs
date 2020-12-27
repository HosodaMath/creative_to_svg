pub mod convert_str {
  use crate::point::point::Point;

  ///## ポリゴンデータを1列の連結された文字列に変換する。
  ///
  pub fn format_one(data: Vec<Point>) -> String {
      let size = data.len();
      let x = data[0].get_x();
      let y = data[0].get_y();
      let sx = format!("{}", x);
      let sy = format!("{}", y);
      let mut tmp = sx + " " + &*sy;

      for count in 1..size  {
          let tmp_x = data[count].get_x();
          let tmp_y = data[count].get_y();
          let tmp_sx = format!("{}", tmp_x);
          let tmp_sy = format!("{}", tmp_y);
          tmp = tmp + " " + &*tmp_sx + " " + &*tmp_sy
      }

      return tmp;
  }
}