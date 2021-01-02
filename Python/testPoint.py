from mathematics import vector as vt
from geometry import point as po
from testBaseSVG import TestSVG


class Point2Test:
    def __init__(self, init_position: vt.Vector2) -> None:
        """
        point test pointテストの定義クラス
        :param init_position: テストに使う座標の初期化
        """
        self.position = init_position

    def test_point1(self) -> None:
        """
        ポイント座標出力のテスト
        :return: None
        """
        point2 = po.BasePoint2(self.position)
        print(point2.draw_point1())
        point2.draw_point2()

    def test_point2(self, init_width: float, init_height: float) -> None:
        """
        ポイントのsvg形式のフォーマット出力のテスト(生の出力(コンソール出力))
        testBaseSVG.pyのそのまま出力するコード(testSVG2)を使っている。

        :param init_width: float svg画像の横幅
        :param init_height: float svg画像の高さ
        :return: None
        """
        svg = TestSVG(init_width, init_height)
        point2 = po.Point(self.position)
        svg.testSVG2(point2.render_point1())

    def test_point3(self, init_width: float, init_height: float) -> None:
        """
        ポイントのsvg形式のフォーマット出力のテスト(svg形式での出力)
        :param init_width:
        :param init_height:
        :return:
        """
        svg = TestSVG(init_width, init_height)
        point2 = po.Point(self.position)
        svg.testSVG3("testPoint3", point2.render_point1())


def testPoint1(position: vt.Vector2) -> None:
    """
    testPoint.py(point.py)のテスト
    ポイント座標出力のテスト
    :param position: vt.Vector2 座標の初期化
    :return: None
    """
    point = Point2Test(position)
    point.test_point1()


def testPoint2(position: vt.Vector2, init_width: float, init_height: float) -> None:
    """
    ポイントのsvg形式のフォーマット出力のテスト(生の出力(コンソール出力))
    testBaseSVG.py(base_svg.py) testPoint.py(point.py)のテスト
    :param position: vt.Vector2 座標の初期化
    :param init_width: float svg画像の横幅
    :param init_height: float svg画像の高さ
    :return: None
    """
    point_svg = Point2Test(position)
    point_svg.test_point2(init_width, init_height)


def testPoint3(position: vt.Vector2, init_width: float, init_height: float):
    """
    ポイントのsvg形式のフォーマット出力のテスト(svg形式での出力)
    testBaseSVG.py(base_svg.py) testPoint.py(point.py)のテスト
    :param position: vt.Vector2 座標の初期化
    :param init_width: float svg画像の横幅
    :param init_height: float svg画像の高さ
    :return: None
    :return:
    """
    point_svg = Point2Test(position)
    point_svg.test_point3(init_width, init_height)


if __name__ == '__main__':
    width = 512
    height = 512

    testPosition1 = vt.Vector2(0, 0)
    testPoint1(testPosition1)

    testPosition2 = vt.Vector2(width / 2, height / 2)
    testPoint2(testPosition2, width, height)

    testPoint3(testPosition2, width, height)
