<<<<<<< HEAD:Algorithm/PythonSVG/geometry/point.py
from mathematics.vector import Vector2


class BasePoint2:
    def __init__(self, location: Vector2):
        """
        点の座標を出力するクラス ベクトル形式のみの座標
        :param location: Vector2
        """
        self.location = location

    def draw_point1(self) -> str:
        """
        座標を文字列で返す
        :return new_position: str
        """
        new_position = "({0},{1})" \
            .format(self.location.get_x(), self.location.get_y())

        return new_position

    def draw_point2(self) -> None:
        """
        座標を返す
        :return: None
        """
        print("({0},{1})".format(self.location.get_x(), self.location.get_y()))


class Point(BasePoint2):
    def __init__(self, location: Vector2):
        """
         pointのSVGコードを出力するクラス ベクトル形式のみの座標
         ここではそれ以上のSVG形式を取り扱わない。ファイル制御も行わない。
        :param location:
        """
        BasePoint2.__init__(self, location)

    def render_point1(self) -> str:
        """
        svg形式のフォーマットされた文字列を返す
        :return render: str
        """
        render = "<circle cx=\"{0}\" cy=\"{1}\" r=\"3\" fill=\"black\" />\n" \
            .format(self.location.get_x(), self.location.get_y())

        return render

    def render_point2(self) -> None:
        """
        svg形式のフォーマットされた文字列を(生の出力(コンソール出力))
        :return: None
        """
        print("<circle cx=\"{0}\" cy=\"{1}\" r=\"3\" fill=\"black\" />"
              .format(self.location.get_x(), self.location.get_y()))
=======
from mathematics.vector import Vector2


class BasePoint2:
    def __init__(self, location: Vector2):
        """
        点の座標を出力するクラス ベクトル形式のみの座標
        :param location: Vector2
        """
        self.location = location

    def draw_point1(self) -> str:
        """
        座標を文字列で返す
        :return new_position: str
        """
        new_position = "({0},{1})" \
            .format(self.location.get_x(), self.location.get_y())

        return new_position

    def draw_point2(self) -> None:
        """
        座標を返す
        :return: None
        """
        print("({0},{1})".format(self.location.get_x(), self.location.get_y()))


class Point(BasePoint2):
    def __init__(self, location: Vector2):
        """
         pointのSVGコードを出力するクラス ベクトル形式のみの座標
         ここではそれ以上のSVG形式を取り扱わない。ファイル制御も行わない。
        :param location:
        """
        BasePoint2.__init__(self, location)

    def render_point1(self) -> str:
        """
        svg形式のフォーマットされた文字列を返す
        :return render: str
        """
        render = "<circle cx=\"{0}\" cy=\"{1}\" r=\"3\" fill=\"black\" />\n" \
            .format(self.location.get_x(), self.location.get_y())

        return render

    def render_point2(self) -> None:
        """
        svg形式のフォーマットされた文字列を(生の出力(コンソール出力))
        :return: None
        """
        print("<circle cx=\"{0}\" cy=\"{1}\" r=\"3\" fill=\"black\" />"
              .format(self.location.get_x(), self.location.get_y()))
>>>>>>> 4d944fdcf288d8c4f352efcfd1a3ce6e952a71b9:Algorithm/SVG/geometry/point.py
