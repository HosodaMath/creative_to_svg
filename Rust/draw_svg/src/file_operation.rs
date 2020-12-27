pub mod svg2 {
  use std::fs::File;
  use std::io::Write;

  pub struct SVG2 {
      pub file: File,
  }

  impl SVG2 {
      pub fn new(init_file_path: File) -> SVG2{
          SVG2 {file: init_file_path }
      }
  }

  impl SVG2 {
      pub fn plot_start2(&mut self, init_width: f64, init_height: f64 ) {
          write!(self.file, "<svg xmlns=\"http://www.w3.org/2000/svg\" ").expect("cannot write.");
          write!(
              self.file,
              "version=\"1.1\" width=\"{}\" height=\"{}\">\n",
              init_width, init_height
          ).expect("cannot write.");
      }
  }

  impl SVG2 {
      pub fn draw(&mut self, svg_tag_data : String){
          write!(self.file, "{}",svg_tag_data).expect("cannot write.");
      }
  }

  impl SVG2 {
      pub fn draw2(&mut self, svg_tag_data : Vec<String>){
          for count in 0..svg_tag_data.len() {
              write!(self.file, "{}",svg_tag_data[count]).expect("cannot write.");
          }
      }
  }

  impl  SVG2 {
      pub fn plot_end2(&mut self) {
          write!(self.file, "</svg>\n").expect("cannot write.");
      }
  }
}


