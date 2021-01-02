from mathematics.vector import Vector2
from geometry.circle import Circle
from testBaseSVG import TestSVGMulti
from typing import List


class TestCircle:
    def __init__(self, init_window_size: Vector2) -> None:
        """
        円のSVG出力のテスト
        :param init_window_size: Vector2 画像サイズ
        """
        self.window_size = init_window_size

    def test_circle1(self, location1: Vector2, radius1: float) -> str:
        """
        private
        fill fill-opacityのテスト
        :param location1: Vector2 座標の初期化
        :param radius1: float 半径
        :return: str
        """
        circle1 = Circle(location1, radius1)
        tmp = circle1.render_circle1("#000000", 1.0)

        return tmp

    def test_circle2(self, location1: Vector2, radius1: float) -> str:
        """
        private
        fill fill-opacity stroke stroke-width stroke-opacityのテスト
        :param location1: Vector2 座標の初期化
        :param radius1: float 半径
        :return: str
        """
        circle1 = Circle(location1, radius1)
        tmp = circle1.render_circle2("#000000", 1.0, "#ffff00", 5.0, 1.0)

        return tmp

    def test_circle3(self, location1: Vector2, radius1: float) -> str:
        """
        private
        stroke stroke-width stroke-opacityのテスト
        :param location1: Vector2 座標の初期化
        :param radius1: float 半径
        :return: str
        """
        circle1 = Circle(location1, radius1)
        tmp = circle1.render_circle3("#ffff00", 5.0, 1.0)

        return tmp

    def svg_pre_build(self):
        radius = 100
        xy1 = Vector2(100, 500)
        circle1 = self.test_circle1(xy1, radius)

        xy2 = Vector2(400, 500)
        circle2 = self.test_circle2(xy2, radius)

        xy3 = Vector2(700, 500)
        circle3 = self.test_circle3(xy3, radius)

        data: List[str] = [circle1, circle2, circle3]
        test = TestSVGMulti(self.window_size.get_x(), self.window_size.get_y())
        test.testSVG2(data)

    def svg_file_build(self):
        radius = 100
        xy1 = Vector2(100, 500)
        circle1 = self.test_circle1(xy1, radius)

        xy2 = Vector2(400, 500)
        circle2 = self.test_circle2(xy2, radius)

        xy3 = Vector2(700, 500)
        circle3 = self.test_circle3(xy3, radius)

        data: List[str] = [circle1, circle2, circle3]
        test = TestSVGMulti(self.window_size.get_x(), self.window_size.get_y())
        test.testSVG3("circleSVG/testCircle1", data)


def svg_test1() -> None:
    size = Vector2(1024, 1024)
    circle = TestCircle(size)
    circle.svg_pre_build()


def svg_test2() -> None:
    size = Vector2(1024, 1024)
    circle = TestCircle(size)
    circle.svg_file_build()


if __name__ == '__main__':
    # svg_test1()
    svg_test2()
