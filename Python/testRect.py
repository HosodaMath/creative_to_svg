from mathematics.vector import Vector2
from geometry.rect import BaseRect, Rect
from testBaseSVG import TestSVG


class TestBaseRect:
    def __init__(self, init_location: Vector2, init_size: Vector2) -> None:
        """
        座標と面積計算の出力
        :param init_location: Vector2 座標の初期化(x, y)
        :param init_size: Vector2 大きさの初期化(width, height)
        """
        self.location = init_location
        self.size = init_size

    def test_rect0(self) -> None:
        """
        座標の出力
        :return: None
        """
        rect = BaseRect(self.location, self.size)
        print(rect.drawRect1())
        rect.drawRect2()
        print(rect.calcRect())

    def test_rect0_calc(self) -> None:
        """
        面積計算の出力
        :return: None
        """
        rect = BaseRect(self.location, self.size)
        rect.drawRect2()
        print(rect.calcRect())


class TestRectSVG1(TestBaseRect):
    def __init__(self, init_location: Vector2, init_size: Vector2) -> None:
        """
        svg出力テスト1 fill fill-opacity
        :param init_location: Vector2 座標の初期化(x, y)
        :param init_size: Vector2 大きさの初期化(width, height)
        """
        TestBaseRect.__init__(self, init_location, init_size)

    def test_rect1(self, window_size: Vector2) -> None:
        """
        単にsvgコードを出力する
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect1("#000000", 1.0)
        svg.testSVG2(rect1)

    def test_rect2(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する fill #000000 fill-opacity 1.0
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect1("#000000", 1.0)
        svg.testSVG3("rectSVG/testRect1_2SVG", rect1)

    def test_rect3(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する fill #000000 fill-opacity 0.5
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect1("#000000", 0.5)
        svg.testSVG3("rectSVG/testRect1_3SVG", rect1)


class TestRectSVG2(TestRectSVG1):
    def __init__(self, init_location: Vector2, init_size: Vector2) -> None:
        """
        svg出力テスト2 fill fill-opacity stroke stroke-width stroke-opacity
        :param init_location: Vector2 座標の初期化(x, y)
        :param init_size: Vector2 大きさの初期化(width, height)
        """
        TestBaseRect.__init__(self, init_location, init_size)

    def test_rect1(self, window_size: Vector2) -> None:
        """
        単にsvgコードを出力する
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect2("#000000", 1.0, "#ff0000", 5.0, 1.0)
        svg.testSVG2(rect1)

    def test_rect2(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する
        fill #000000 fill-opacity 1.0
        stroke #ff0000 stroke-width 5.0 stroke-opacity 1.0
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect2("#000000", 1.0, "#ff0000", 5.0, 1.0)
        svg.testSVG3("rectSVG/testRect2_2SVG", rect1)

    def test_rect3(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する
        fill #000000 fill-opacity 0.5
        stroke #ff0000 stroke-width 5.0 stroke-opacity 1.0
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect2("#000000", 0.5, "#ff0000", 5.0, 1.0)
        svg.testSVG3("rectSVG/testRect2_3SVG", rect1)


class TestRectSVG3(TestRectSVG2):
    def __init__(self, init_location: Vector2, init_size: Vector2) -> None:
        """
        svg出力テスト3 stroke stroke-width stroke-opacity
        :param init_location: Vector2 座標の初期化(x, y)
        :param init_size: Vector2 大きさの初期化(width, height)
        """
        TestBaseRect.__init__(self, init_location, init_size)

    def test_rect1(self, window_size: Vector2) -> None:
        """
        単にsvgコードを出力する
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect3("#ff0000", 10.0, 0.7)
        svg.testSVG2(rect1)

    def test_rect2(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する
        stroke #ff0000 stroke-width 10.0 stroke-opacity 0.7
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect3("#ff0000", 10.0, 0.7)
        svg.testSVG3("rectSVG/testRect3_2SVG", rect1)

    def test_rect3(self, window_size: Vector2) -> None:
        """
        svgファイルを出力する
        stroke #ff0000 stroke-width 5.0 stroke-opacity 0.7
        :param window_size: Vector2 画像サイズ(width, height)
        :return: None
        """
        svg = TestSVG(window_size.get_x(), window_size.get_y())
        rect = Rect(self.location, self.size)
        rect1 = rect.render_rect3("#ff0000", 10.0, 0.7)
        svg.testSVG3("rectSVG/testRect3_3SVG", rect1)


def test_rect0() -> None:
    width = 512
    height = 512
    location1 = Vector2(width / 2, height / 2)
    size1 = Vector2(width, height)
    test1 = TestBaseRect(location1, size1)
    test1.test_rect0()
    test1.test_rect0_calc()


def test_rect1() -> None:
    width = 512
    height = 512
    init_location = Vector2(width / 4, height / 4)
    init_size = Vector2(256, 256)
    window_size = Vector2(512, 512)

    test1 = TestRectSVG1(init_location, init_size)
    test1.test_rect1(window_size)
    test1.test_rect2(window_size)
    test1.test_rect3(window_size)


def test_rect2() -> None:
    width = 512
    height = 512
    init_location = Vector2(width / 4, height / 4)
    init_size = Vector2(256, 256)
    window_size = Vector2(512, 512)

    test1 = TestRectSVG2(init_location, init_size)
    test1.test_rect1(window_size)
    test1.test_rect2(window_size)
    test1.test_rect3(window_size)


def test_rect3() -> None:
    width = 512
    height = 512
    init_location = Vector2(width / 4, height / 4)
    init_size = Vector2(256, 256)
    window_size = Vector2(512, 512)

    test1 = TestRectSVG3(init_location, init_size)
    test1.test_rect1(window_size)
    test1.test_rect2(window_size)
    test1.test_rect3(window_size)


if __name__ == '__main__':
    # test_rect0()
    # test_rect1()
    # test_rect2()
    test_rect3()
