from mathematics.vector import Vector2
from geometry.polygon import Polygon
from testBaseSVG import TestSVG
from typing import List


class Triangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def triangle_data(self) -> List[Vector2]:
        """
        三角形を描くデータ
        :return:
        """
        x: List[float] = [10.0, self.width - 10.0, self.width - 10.0]
        y: List[float] = [self.height - 10, self.height - 10, 10.0]
        data: List[Vector2] = []
        if len(x) == len(y):
            for count in range(0, 3):
                tmp = Vector2(x[count], y[count])
                data.append(tmp)

        return data

    @staticmethod
    def render_triangle1(triangle_data: List[Vector2]) -> str:
        """

        :param triangle_data: List[Vector] 三角形のデータ
        :return: str
        """
        triangle = Polygon(triangle_data)
        tmp = triangle.render_polygon3("#000000", 5.0, 1.0)

        return tmp

    def svg_file_build(self):
        tmp_data1: List[Vector2] = self.triangle_data()
        poly1 = self.render_triangle1(tmp_data1)
        triangle_build = TestSVG(self.width, self.height)
        triangle_build.testSVG3("triangle/triangle1", poly1)


if __name__ == '__main__':
    init_width = 512.0
    init_height = 512.0

    triangle1 = Triangle(init_width, init_height)
    triangle1.svg_file_build()