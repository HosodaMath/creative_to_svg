from mathematics.vector import Vector2
from geometry.polygon import Polygon
from test_base_svg import TestSVGMulti
from typing import List


class TestPolygon:
    def __init__(self, init_window_size: Vector2) -> None:
        """
        polygonのSVG出力のテスト
        :param init_window_size: Vector2 画像サイズ
        """
        self.window_size = init_window_size

    def test_polygon1(self, poly_data: List[Vector2]) -> str:
        """
        private
        設定パラメータ fill fill-opacityのテスト
        :param poly_data: List[Vector2] 座標の初期化
        :return: str
        """
        poly = Polygon(poly_data)
        tmp = poly.render_polygon1("#000000", 1.0)

        return tmp

    def test_polygon2(self, poly_data: List[Vector2]) -> str:
        """
        private
        設定パラメータ fill fill-opacity stroke stroke-width stroke-opacityのテスト
        :param poly_data: List[Vector2] 座標の初期化
        :return: str
        """
        poly = Polygon(poly_data)
        tmp = poly.render_polygon2("#000000", 1.0, "#ffff00", 10.0, 1.0)

        return tmp

    def test_polygon3(self, poly_data: List[Vector2]) -> str:
        """
        private
        設定パラメータ stroke stroke-width stroke-opacity
        :param poly_data: List[Vector2] 座標の初期化
        :return: str
        """
        poly = Polygon(poly_data)
        tmp = poly.render_polygon3("#ffff00", 10.0, 1.0)

        return tmp

    def triangle_data1(self) -> List[Vector2]:
        data: List[Vector2] = []
        x = [0.0, self.window_size.get_x() / 2.0, self.window_size.get_x()]
        y = [self.window_size.get_y(), 0.0, self.window_size.get_y()]
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    def triangle_data2(self) -> List[Vector2]:
        data: List[Vector2] = []
        x = [100.0, self.window_size.get_x() / 2.0, self.window_size.get_x() - 100.0]
        y = [self.window_size.get_y() - 100.0, 0.0, self.window_size.get_y() - 100.0]
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    def triangle_data3(self) -> List[Vector2]:
        data: List[Vector2] = []
        x = [200.0, self.window_size.get_x() / 2.0, self.window_size.get_x() - 200.0]
        y = [self.window_size.get_y() - 200.0, 0.0, self.window_size.get_y() - 200.0]
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    def svg_file_build(self):
        tmp_data1: List[Vector2] = self.triangle_data1()
        poly1 = self.test_polygon1(tmp_data1)

        tmp_data2: List[Vector2] = self.triangle_data2()
        poly2 = self.test_polygon2(tmp_data2)

        tmp_data3: List[Vector2] = self.triangle_data3()
        poly3 = self.test_polygon3(tmp_data3)

        data: List[str] = [poly1, poly2, poly3]
        test = TestSVGMulti(self.window_size.get_x(), self.window_size.get_y())
        test.testSVG3("test_polygon_svg/testPolygon1", data)


def svg_test1() -> None:
    size = Vector2(1024, 1024)
    poly = TestPolygon(size)
    poly.svg_file_build()


if __name__ == '__main__':
    svg_test1()
