from mathematics.vector import Vector2


class BaseRect:
    location1: Vector2
    size: Vector2

    def __init__(self, init_location1: Vector2, init_size: Vector2) -> None:
        """
        矩形の座標と大きさを出力するクラス
        :param init_location1:
        :param init_size:
        """
        self.location1 = init_location1
        self.size = init_size

    def drawRect1(self) -> str:
        """
        座標を文字列で返す
        :return new_position: str
        """
        new_position = "({0},{1}) ({2},{3})" \
            .format(self.location1.get_x(), self.location1.get_y(),
                    self.size.get_x(), self.size.get_y())

        return new_position

    def drawRect2(self) -> None:
        """
        座標を返す
        :return: None
        """
        print("({0},{1}) ({2},{3})".format(self.location1.get_x(), self.location1.get_y(),
                                           self.size.get_x(), self.size.get_y()))

    def calcRect(self) -> str:
        """
        矩形の面積計算結果を返す
        :return ans: str
        """
        ans = "{0}".format(self.size.get_x() * self.size.get_y())

        return ans


class Rect(BaseRect):
    def __init__(self, init_location: Vector2, init_size: Vector2) -> None:
        """
        rectのSVGコードを出力するクラス
        :param init_location: Vector2 座標の初期化(x, y)
        :param init_size: Vector2 大きさの初期化(width, height)
        :return :None
        """
        BaseRect.__init__(self, init_location, init_size)

    def render_rect1(self, fillColor: str, fillAlpha: float) -> str:
        """
        矩形の描画
        :param fillColor: str 矩形の塗りつぶし
        :param fillAlpha: float 塗りつぶしの透明度
        :return: str rect文字列として返す
        """
        front = "<rect"
        location_xy = " x=\"{0}\" y=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        size_xy = " width=\"{0}\" height=\"{1}\"".format(self.size.get_x(), self.size.get_y())
        color = " fill=\"{0}\" fill-opacity=\"{1}\"".format(fillColor, fillAlpha)
        back = " />"
        rect = front + location_xy + size_xy + color + back

        return rect

    def render_rect2(self,
                     fillColor: str, fillAlpha: float,
                     strokeColor: str, strokeWidth: float, strokeAlpha: float) -> str:
        """
        矩形の描画
        :param fillColor: str 矩形の塗りつぶし
        :param fillAlpha: float 塗りつぶしの透明度
        :param strokeColor: str ふちの色
        :param strokeWidth: float ふちの太さ
        :param strokeAlpha: float ふちの透明度
        :return: str rect文字列として返す
        """
        front = "<rect"
        location_xy = " x=\"{0}\" y=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        size_xy = " width=\"{0}\" height=\"{1}\"".format(self.size.get_x(), self.size.get_y())
        fill_color = " fill=\"{0}\" fill-opacity=\"{1}\"".format(fillColor, fillAlpha)
        stroke_color = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(strokeColor, strokeWidth,
                                                                                            strokeAlpha)
        back = " />"
        rect = front + location_xy + size_xy + fill_color + stroke_color + back

        return rect

    def render_rect3(self, strokeColor: str, strokeWidth: float, strokeAlpha: float) -> str:
        """
        矩形の描画
        :param strokeColor: str ふちの色
        :param strokeWidth: float ふちの太さ
        :param strokeAlpha: float ふちの透明度
        :return: str rect文字列として返す
        """
        front = "<rect"
        location_xy = " x=\"{0}\" y=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        size_xy = " width=\"{0}\" height=\"{1}\"".format(self.size.get_x(), self.size.get_y())
        fill_color = " fill=\"none\""
        stroke_color = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(strokeColor, strokeWidth,
                                                                                            strokeAlpha)
        back = " />"
        rect = front + location_xy + size_xy + fill_color + stroke_color + back

        return rect


def test_rect0(init_location: Vector2, init_size: Vector2):
    rect = BaseRect(init_location, init_size)
    print(rect.drawRect1())
    rect.drawRect2()
    print(rect.calcRect())


def test_rect1(init_location: Vector2, init_size: Vector2):
    rect = Rect(init_location, init_size)
    print(rect.render_rect1("#000000", 1.0))


def test_rect2(init_location: Vector2, init_size: Vector2):
    rect = Rect(init_location, init_size)
    print(rect.render_rect2("#000000", 1.0, "#ff0000", 5.0, 1.0))


def test_rect3(init_location: Vector2, init_size: Vector2):
    rect = Rect(init_location, init_size)
    print(rect.render_rect3("#ff0000", 5.0, 1.0))


if __name__ == '__main__':
    size = 200.0
    location1 = Vector2(250.0, 0.0)
    size1 = Vector2(size, size)
    test_rect0(location1, size1)
    test_rect1(location1, size1)

    location2 = Vector2(250, 250)
    size2 = Vector2(size, size)
    test_rect2(location2, size2)

    location3 = Vector2(250, 500)
    size3 = Vector2(size, size)
    test_rect3(location3, size3)
