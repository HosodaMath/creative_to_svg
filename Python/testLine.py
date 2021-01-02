from mathematics.vector import Vector2
from geometry import line as li
from testBaseSVG import TestSVG


class Line2Test:
    def __init__(self, init_position1: Vector2, init_position2: Vector2) -> None:
        """
        line test lineテストの定義クラス
        :param init_position1: line1の座標
        :param init_position2: line2の座標
        """
        self.line1 = init_position1
        self.line2 = init_position2

    def test_line1(self) -> None:
        """
        line1 and line2座標出力のテスト
        :return: None
        """
        line = li.BaseLine2(self.line1, self.line2)
        print(line.drawline1())
        line.drawline2()

    def test_line2(self, init_size: Vector2) -> None:
        """
        lineのsvg形式のフォーマット出力のテスト(生の出力(コンソール出力))

        :param init_size: Vector2 SVG画像のサイズ
        :return: None
        """
        svg = TestSVG(init_size.get_x(), init_size.get_y())
        line = li.Line(self.line1, self.line2)
        line_tag = line.render_line1("#000000", 1.0)
        svg.testSVG2(line_tag)

    def test_line3(self, init_size: Vector2) -> None:
        """
        lineのsvg形式のフォーマット出力のテスト(svg形式での出力)
        :param init_size: Vector2 SVG画像のサイズ
        :return:
        """
        svg = TestSVG(init_size.get_x(), init_size.get_y())
        line = li.Line(self.line1, self.line2)
        line_tag = line.render_line1("#000000", 1.0)
        svg.testSVG3("testLine3", line_tag)


def line_test1(init_position1: Vector2, init_position2: Vector2) -> None:
    """
    line1 and line2座標出力のテス
    :param init_position1:
    :param init_position2:
    :return:
    """
    line = Line2Test(init_position1, init_position2)
    line.test_line1()


def line_test2(init_position1: Vector2, init_position2: Vector2, init_size: Vector2) -> None:
    """
    lineのsvg形式のフォーマット出力のテスト(生の出力(コンソール出力))
    line1 and line2座標出力のテスト
    :param init_size: 
    :param init_position1:
    :param init_position2:
    :return:
    """
    line = Line2Test(init_position1, init_position2)
    line.test_line2(init_size)


def line_test3(init_position1: Vector2, init_position2: Vector2, init_size: Vector2) -> None:
    """
    lineのsvg形式のフォーマット出力のテスト(生の出力(コンソール出力))
    line1 and line2座標出力のテスト
    :param init_size:
    :param init_position1:
    :param init_position2:
    :return:
    """
    line = Line2Test(init_position1, init_position2)
    line.test_line3(init_size)


if __name__ == '__main__':
    width: float = 512
    height: float = 512
    position1 = Vector2(width / 4, height / 2)
    position2 = Vector2(width - width / 4, height / 2)
    line_test1(position1, position2)

    size: Vector2 = Vector2(width, height)
    line_test2(position1, position2, size)

    line_test3(position1, position2, size)
