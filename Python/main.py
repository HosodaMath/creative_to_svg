from mathematics import vector as vt
from testBaseSVG import TestSVG
from testPoint import Point2Test


def testSVG1(init_width: float, init_height: float) -> None:
    """
    生base_svg.pyのテスト
    :param init_width: float svg画像の横幅
    :param init_height: float svg画像の高さ
    :return:
    """
    svg = TestSVG(init_width, init_height)
    svg.testSVG1()


if __name__ == '__main__':
    width = 512
    height = 512
    testSVG1(width, height)

