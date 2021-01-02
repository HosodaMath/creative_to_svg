from mathematics.vector import Vector2
from typing import List
from utility.convert_str import format_one


class BasePolygon:
    def __init__(self, init_data: List[Vector2]) -> None:
        """
        多角形の出力
        :param init_data: List[Vector2] ポリゴンデータの初期化
        """
        self.data = init_data

    def draw_polygon1(self) -> List[str]:
        """
        ポリゴンの座標を取得
        :return: List[str]
        """
        str_poly_data: List[str] = []
        for count in self.data:
            tmp = "({0}, {1})".format(count.get_x(), count.get_y())
            str_poly_data.append(tmp)

        return str_poly_data

    def draw_polygon2(self) -> None:
        """
        ポリゴンの座標を出力
        :return: None
        """
        for count in self.data:
            print("({0}, {1})".format(count.get_x(), count.get_y()))


class Polygon(BasePolygon):
    def __init__(self, init_data: List[Vector2]) -> None:
        """
        polygonのsvgコードを出力するコード
        :param init_data: List[Vector2] ポリゴン座標の初期化
        """
        BasePolygon.__init__(self, init_data)

    def render_polygon1(self, fillColor: str, fillOpacity: float) -> str:
        """
        ポリゴンタグデータの取得
        設定パラメータ fill fill-opacity
        :param fillColor: fill
        :param fillOpacity: fill-opacity
        :return: str
        """
        str_data = format_one(self.data)
        tmp = "<polygon points=\"{0}\" fill=\"{1}\" fill-opacity=\"{2}\" />\n".format(str_data, fillColor, fillOpacity)

        return tmp

    def render_polygon2(self, fillColor: str, fillOpacity: float,
                        strokeColor: str, strokeWidth: float, strokeOpacity: float) -> str:
        """
        ポリゴンタグデータの取得
        設定パラメータ fill fill-opacity stroke stroke-width stroke-opacity
        :param fillColor: str fill
        :param fillOpacity: float fill-opacity
        :param strokeColor: str stroke
        :param strokeWidth: float stroke-width
        :param strokeOpacity: float stroke-opacity
        :return set_polygon: str
        """
        str_data = format_one(self.data)

        start = "<polygon"
        location_data = " points=\"{0}\"".format(str_data)
        fill_set = " fill=\"{0}\" fill-opacity=\"{1}\"".format(fillColor, fillOpacity)
        stroke_set = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(strokeColor,
                                                                                          strokeWidth, strokeOpacity)
        end = " />\n"
        set_polygon = start + location_data + fill_set + stroke_set + end

        return set_polygon

    def render_polygon3(self, strokeColor: str, strokeWidth: float, strokeOpacity: float) -> str:
        """
        ポリゴンタグデータの取得
        設定パラメータ stroke stroke-width stroke-opacity
        :param strokeColor: str stroke
        :param strokeWidth: float stroke-width
        :param strokeOpacity: float stroke-opacity
        :return set_polygon: str
        """
        str_data = format_one(self.data)

        start = "<polygon"
        location_data = " points=\"{0}\"".format(str_data)
        fill_set = " fill=\"none\""
        stroke_set = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(
            strokeColor, strokeWidth, strokeOpacity)
        end = " />\n"
        set_polygon = start + location_data + fill_set + stroke_set + end

        return set_polygon


def poly_data(width: float, height: float) -> List[Vector2]:
    data: List[Vector2] = []
    x = [0.0, width / 2.0, width]
    y = [height, 0.0, height]
    if len(x) == len(y):
        for count in range(0, 3):
            tmp = Vector2(x[count], y[count])
            data.append(tmp)

    return data


if __name__ == '__main__':
    init_width = 512.0
    init_height = 512.0
    tmp_data: List[Vector2] = poly_data(init_width, init_height)

    poly = BasePolygon(tmp_data)
    print(poly.draw_polygon1())
    poly.draw_polygon2()

    poly2 = Polygon(tmp_data)
    print(poly2.render_polygon1("#000000", 1.0))
    print(poly2.render_polygon2("#000000", 1.0, "#ffff00", 10.0, 1.0))
    print(poly2.render_polygon3("#ffff00", 10.0, 1.0))
