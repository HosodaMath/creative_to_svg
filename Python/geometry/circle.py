from mathematics.vector import Vector2


class BaseCircle:
    def __init__(self, init_location1: Vector2, init_radius1: float) -> None:
        """
        円の座標と半径の出力
        :param init_location1: Vector2 座標の初期化
        :param init_radius1: float 半径
        """
        self.location1 = init_location1
        self.radius1 = init_radius1

    def drawCircle1(self) -> str:
        tmp = "({},{}), {}".format(self.location1.get_x(), self.location1.get_y(),
                                   self.radius1)
        return tmp

    def drawCircle2(self) -> None:
        tmp = "({},{}), {}".format(self.location1.get_x(), self.location1.get_y(),
                                   self.radius1)
        print(tmp)


class BaseEllipse(BaseCircle):
    def __init__(self, init_location1: Vector2, init_radius1: float, init_radius2: float) -> None:
        """
        楕円の座標と半径の出力
        :param init_location1: Vector2 座標の初期化
        :param init_radius1: float 半径x
        :param init_radius2: float 半径y
        """
        self.radius2 = init_radius2
        self.radius = Vector2(self.radius1, self.radius2)
        BaseCircle.__init__(self, init_location1, init_radius1)

    def drawEllipse1(self) -> str:
        tmp = "({},{}),({},{})".format(self.location1.get_x(), self.location1.get_y(),
                                       self.radius.get_x(), self.radius.get_y())
        return tmp

    def drawEllipse2(self) -> None:
        tmp = "({},{}),({},{})".format(self.location1.get_x(), self.location1.get_y(),
                                       self.radius.get_x(), self.radius.get_y())
        print(tmp)


class Circle(BaseCircle):
    def __init__(self, init_location1: Vector2, init_radius1: float) -> None:
        """
        circleのsvgコードを出力するコード
        :param init_location1: Vector2
        :param init_radius1: float
        """
        BaseCircle.__init__(self, init_location1, init_radius1)

    def render_circle1(self, fillColor: str, fillOpacity: float) -> str:
        """
        設定パラメータ fill fill-opacity
        :param fillColor: fill
        :param fillOpacity: fill-opacity
        :return: str
        """
        start = " <circle"
        location = " cx=\"{0}\" cy=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        radius = " r=\"{0}\"".format(self.radius1)
        fill_color = " fill=\"{0}\" fill-opacity=\"{1}\"".format(fillColor, fillOpacity)
        end = " />\n"
        circle = start + location + radius + fill_color + end

        return circle

    def render_circle2(self, fillColor: str, fillOpacity: float,
                       strokeColor: str, strokeWidth: float, strokeOpacity) -> str:
        """
        設定パラメータ fill fill-opacity stroke stroke-width stroke-opacity
        :param fillColor: str fill
        :param fillOpacity: float fill-opacity
        :param strokeColor: str stroke
        :param strokeWidth: float stroke-width
        :param strokeOpacity: float stroke-opacity
        :return: str
        """
        start = " <circle"
        location = " cx=\"{0}\" cy=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        radius = " r=\"{0}\"".format(self.radius1)
        fill_color = " fill=\"{0}\" fill-opacity=\"{1}\"".format(fillColor, fillOpacity)
        stroke_color = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(strokeColor,
                                                                                            strokeWidth, strokeOpacity)
        end = " />\n"
        circle = start + location + radius + fill_color + stroke_color + end

        return circle

    def render_circle3(self, strokeColor: str, strokeWidth: float, strokeOpacity) -> str:
        """
        設定パラメータ stroke stroke-width stroke-opacity
        :param strokeColor: str stroke
        :param strokeWidth: float stroke-width
        :param strokeOpacity: float stroke-opacity
        :return: str
        """
        start = " <circle"
        location = " cx=\"{0}\" cy=\"{1}\"".format(self.location1.get_x(), self.location1.get_y())
        radius = " r=\"{0}\"".format(self.radius1)
        fill_color = " fill=\"none\""
        stroke_color = " stroke=\"{0}\" stroke-width=\"{1}\" stroke-opacity=\"{2}\"".format(strokeColor,
                                                                                            strokeWidth, strokeOpacity)
        end = " />\n"
        circle = start + location + radius + fill_color + stroke_color + end

        return circle


if __name__ == '__main__':
    location1 = Vector2(100, 500)
    init_radius = 100
    circle1 = Circle(location1, init_radius)
    print(circle1.render_circle1("#000000", 1.0))

    location2 = Vector2(400, 500)
    circle2 = Circle(location2, init_radius)
    print(circle2.render_circle2("#000000", 1.0, "#ffff00", 5.0, 1.0))

    location3 = Vector2(700, 500)
    circle3 = Circle(location3, init_radius)
    print(circle3.render_circle3("#ffff00", 5.0, 1.0))
