
from base_svg import base_svg as bs
from typing import List


class TestSVG:
    def __init__(self, width, height) -> None:
        """
        svg描画の初期値
        :param width: svg画像の横幅
        :param height: svg画像の高さ
        """
        self.width = width
        self.height = height

    def testSVG1(self) -> None:
        """
        そのまま出力するコード
        start and endの出力のみ
        :return: None
        """
        svg = bs.DrawSVG(self.width, self.height)
        print(svg.svgStart1())
        print(svg.svgEnd())

    def testSVG2(self, data: str) -> None:
        """
        そのまま出力するコード
        :param data: str 何らかのsvgタグデータを入れる
        :return: None
        """
        svg = bs.DrawSVG(self.width, self.height)
        print(svg.svgStart1())
        print(data)
        print(svg.svgEnd())

    def testSVG3(self, file_name: str, data: str) -> None:
        """
        svg形式で出力するコード
        :param file_name: str ファイル名
        :param data: str 何らかのsvgタグデータを入れる
        :return: None
        """
        svg = bs.DrawSVG(self.width, self.height)
        fileName = "{0}.svg".format(file_name)
        start = svg.svgStart2()
        svg_tag1 = data
        end = svg.svgEnd()
        with open(fileName, 'w') as fileObject:
            fileObject.write(start)
            fileObject.write(svg_tag1)
            fileObject.write(end)


class TestSVGMulti(TestSVG):
    def __init__(self, width, height) -> None:
        TestSVG.__init__(self, width, height)

    def testSVG2(self, data: List[str]) -> None:
        """
        そのまま出力するコード
        :param data: List[str] 何らかのsvgタグデータを入れる
        :return: None
        """
        svg = bs.DrawSVG(self.width, self.height)
        print(svg.svgStart1())
        for count in data:
            print(count)
        print(svg.svgEnd())

    def testSVG3(self, file_name: str, data: List[str]) -> None:
        """
        svg形式で出力するコード
        :param file_name: str ファイル名
        :param data: List[str] 何らかのsvgタグデータを入れる
        :return: None
        """
        svg = bs.DrawSVG(self.width, self.height)
        fileName = "{0}.svg".format(file_name)
        with open(fileName, 'w') as fileObject:
            start = svg.svgStart2()

            fileObject.write(start)
            for count in data:
                fileObject.write(count)

            end = svg.svgEnd()
            fileObject.write(end)
