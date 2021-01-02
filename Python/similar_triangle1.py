from mathematics.vector import Vector2
from geometry.polygon import Polygon
from testBaseSVG import TestSVGMulti, TestSVG
from typing import List


class SimilarTriangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def triangle_data1(self) -> List[Vector2]:
        """
        小さい三角形を描くデータ
        :return:
        """
        shift_x = 1.0
        shift_y = shift_x
        x: List[float] = [
            0.0 + shift_x,
            self.width / 2.0 - shift_x / 2.0,
            self.width / 2.0 - shift_x / 2.0
        ]

        y: List[float] = [
            self.height - shift_y,
            self.height - shift_y,
            0.0 + self.height / 2.0 + shift_y / 2.0]

        data: List[Vector2] = []
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    @staticmethod
    def render_triangle1(triangle_data: List[Vector2]) -> str:
        """
        小さい三角形の生成
        :param triangle_data: List[Vector] 三角形のデータ
        :return: str
        """
        triangle = Polygon(triangle_data)
        tmp = triangle.render_polygon3("#000000", 2.0, 1.0)

        return tmp

    def triangle_data2(self) -> List[Vector2]:
        """
        大きい三角形の生成を描くデータ
        :return:
        """
        shift_x = 1.0
        shift_y = shift_x
        x: List[float] = [
            0.0 + shift_x,
            self.width - shift_x,
            self.width - shift_x
        ]

        y: List[float] = [
            self.height - shift_y,
            self.height - shift_y,
            0.0 + shift_y]
        data: List[Vector2] = []
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    @staticmethod
    def render_triangle2(triangle_data: List[Vector2]) -> str:
        """
        大きい三角形の生成
        :param triangle_data: List[Vector] 三角形のデータ
        :return: str
        """
        triangle = Polygon(triangle_data)
        tmp = triangle.render_polygon3("#000000", 2.0, 1.0)

        return tmp

    def svg_file_build(self):
        data: List[str] = []

        tmp_data1: List[Vector2] = self.triangle_data1()
        poly1 = self.render_triangle1(tmp_data1)

        tmp_data2: List[Vector2] = self.triangle_data2()
        poly2 = self.render_triangle2(tmp_data2)

        data.append(poly1)
        data.append(poly2)

        triangle_build = TestSVGMulti(self.width, self.height)
        triangle_build.testSVG3("triangle/similar_triangle1_1", data)


if __name__ == '__main__':
    init_width = 600.0
    init_height = 600.0

    triangle1 = SimilarTriangle(init_width, init_height)
    triangle1.svg_file_build()
