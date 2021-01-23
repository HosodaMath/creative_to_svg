from mathematics.vector import Vector2
from geometry.rect import Rect
from geometry.definition import start_definition, end_definition
from geometry.gradient import LinearGradient1, set_gradient_id
from geometry.pattern import Pattern, set_pattern_id
from test_base_svg import TestSVGMulti
from typing import List


def set_gradient_data() -> List[List[str]]:
    """
    グラデーションのカラー設定
    位置とカラーの設定を行う
    :return: List[List[str]]
    """
    init_gradient_data: List[List[str]] = []
    class_data: List[str] = ["0%", "50%", "100"]
    offset_data: List[str] = ["#f8f886", "#ffffb5", "#ffffff"]
    if len(class_data) == len(offset_data):
        init_gradient_data: List[List[str]] = [class_data, offset_data]

    return init_gradient_data


class Test1_LinearGradient1:
    def __init__(self, init_width: float, init_height: float):
        """
        線形グラデーションのテスト1
        矩形に対して線形グラデーションの適用を行う
        :param init_width: float 画像の横幅
        :param init_height: float 画像の高さ
        """
        self.width = init_width
        self.height = init_height

    def test_linear_gradient(self) -> List[str]:
        """
        グラデーションだけではだめで改めて組み直す必要がある。 -> SVG生成にはまとめてビルドが必要なため
        具体的にはdefsタグを先頭と後方に追加する必要がある。
        そのあとにグラデーションを適用するプリミティブ(例えばrectなどを適用する)
        :return: List[str]
        """
        linear_gradient_pattern_tag_data: List[str] = []

        # ここから線形グラデーションとパターンの定義

        start = start_definition()
        linear_gradient_pattern_tag_data.append(start)

        # ここからパターンの定義
        # ここからパターンスタート
        pattern_id = "linear_gradient_pattern1"
        start_location_data = Vector2(0, 0)
        size_data = Vector2(0.1, 0.1)
        pattern1 = Pattern(pattern_id, start_location_data, size_data)
        start_pattern = pattern1.start_pattern1()
        linear_gradient_pattern_tag_data.append(start_pattern)

        linear_gradient_id = "linear_gradient1"

        # 線形グラデーションデータを呼び出している。グラデーションデータの定義はclass外で行っている。
        linear_gradient_data = set_gradient_data()
        linear_gradient = LinearGradient1(linear_gradient_id, linear_gradient_data)

        # ここでsvgビルドのために線形グラデーションタグを改めて組み直すために再度格納している
        tmp_linear_gradient_tag_data = linear_gradient.linear_gradient1()
        for count_data in tmp_linear_gradient_tag_data:
            linear_gradient_pattern_tag_data.append(count_data)

        # ここでグラデーションの適用を行う矩形の定義を行う
        rect_location = Vector2(0, 0)
        rect_size = Vector2(50, 50)
        rect = Rect(rect_location, rect_size)
        new_color = set_gradient_id(linear_gradient_id)
        tmp_rect = rect.render_rect1(new_color, 1.0)
        linear_gradient_pattern_tag_data.append(tmp_rect)

        # ここでパターンの定義終了
        end_pattern = pattern1.end_pattern()
        linear_gradient_pattern_tag_data.append(end_pattern)

        # ここでグラデーションパターンの定義を終了
        end = end_definition()
        linear_gradient_pattern_tag_data.append(end)

        # この下にパターンの適用を行うrectの定義を行う
        rect_location = Vector2(0, 0)
        rect_size = Vector2(self.width, self.height)
        rect = Rect(rect_location, rect_size)
        new_color = set_pattern_id(pattern_id)
        tmp_rect = rect.render_rect1(new_color, 1.0)
        linear_gradient_pattern_tag_data.append(tmp_rect)

        return linear_gradient_pattern_tag_data

    def svg_data_build(self):
        build = TestSVGMulti(self.width, self.height)
        tmp_test = self.test_linear_gradient()
        file_name = "test_pattern_svg/svg/test1_linear_gradient_pattern1"
        build.testSVG3(file_name, tmp_test)
        # n = len(tmp_test)
        # for count in range(0, n):
        #    print(tmp_test[count])


if __name__ == '__main__':
    tmp_test1 = Test1_LinearGradient1(256, 256)
    tmp_test1.svg_data_build()

