from mathematics.vector import Vector2


class BaseLine2:
    location1: Vector2
    location2: Vector2

    def __init__(self, location1: Vector2, location2: Vector2):
        """
        lineの座標を出力するクラス ベクトル形式のみの座標
        :param location1: Vector2 座標1の初期化
        :param location2: Vector2 座標2の初期化
        """
        self.location1 = location1
        self.location2 = location2

    def drawline1(self) -> str:
        """
        座標を文字列で返す
        :return new_position: str
        """
        new_position = "({0},{1}) ({2},{3})" \
            .format(self.location1.get_x(), self.location1.get_y(),
                    self.location2.get_x(), self.location2.get_y())

        return new_position

    def drawline2(self) -> None:
        """
        座標を返す
        :return: None
        """
        print("({0},{1}) ({2},{3})".format(self.location1.get_x(), self.location1.get_y(),
                                           self.location2.get_x(), self.location2.get_y()))


class Line(BaseLine2):
    def __init__(self, location1: Vector2, location2: Vector2):
        """
         lineのSVGコードを出力するクラス
        :param location1: Vector2
        :param location2: Vector2
        """
        BaseLine2.__init__(self, location1, location2)

    def render_line1(self, stroke_color: str, stroke_width: float) -> str:
        """
        svg形式のフォーマットされた文字列を返す
        :param stroke_color: str
        :param stroke_width: float
        :return render: str
        """
        # location setup
        par_location = "<line x1=\"{0}\" x2=\"{1}\" y1=\"{2}\" y2= \"{3}\"".format(self.location1.get_x(),
                                                                                   self.location2.get_x(),
                                                                                   self.location1.get_y(),
                                                                                   self.location2.get_y())
        # color setup
        par_color = " fill=\"transparent\" stroke=\"{0}\" stroke-width=\"{1}\"/>".format(stroke_color, stroke_width)

        line = par_location + par_color

        return line

    def render_line2(self, stroke_color: str, stroke_width: float) -> None:
        """
        svg形式のフォーマットされた文字列をその場で出力する
        :param stroke_color: str
        :param stroke_width: float
        :return render: str
        """
        par_location = "<line x1=\"{0}\" x2=\"{1}\" y1=\"{2}\" y2= \"{3}\"".format(self.location1.get_x(),
                                                                                   self.location2.get_x(),
                                                                                   self.location1.get_y(),
                                                                                   self.location2.get_y())
        # color setup
        par_color = " fill=\"transparent\" stroke=\"{0}\" stroke-width=\"{1}\"/>".format(stroke_color, stroke_width)

        line = par_location + par_color

        print(line)


class BaseLine2:
    location1: Vector2
    location2: Vector2

    def __init__(self, location1: Vector2, location2: Vector2):
        """
        lineの座標を出力するクラス ベクトル形式のみの座標
        :param location1: Vector2 座標1の初期化
        :param location2: Vector2 座標2の初期化
        """
        self.location1 = location1
        self.location2 = location2

    def drawline1(self) -> str:
        """
        座標を文字列で返す
        :return new_position: str
        """
        new_position = "({0},{1}) ({2},{3})" \
            .format(self.location1.get_x(), self.location1.get_y(),
                    self.location2.get_x(), self.location2.get_y())

        return new_position

    def drawline2(self) -> None:
        """
        座標を返す
        :return: None
        """
        print("({0},{1}) ({2},{3})".format(self.location1.get_x(), self.location1.get_y(),
                                           self.location2.get_x(), self.location2.get_y()))
