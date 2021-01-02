class DrawSVG:
    def __init__(self, width: str, height: str) -> None:
        """
        仮のコード
        :param width: svg画像の横幅
        :param height: svg画像の高さ
        """
        self.width = width
        self.height = height

    def svgStart1(self) -> str:
        """
        svg描画開始
        :return base1 + base2: str
        """
        base1 = "<svg xmlns=\"http://www.w3.org/2000/svg\" "
        base2 = "version=\"1.1\" width=\"{0}\" height=\"{1}\">".format(self.width, self.height)

        return base1 + base2

    def svgStart2(self) -> str:
        """
        svg描画開始
        :return base1 + base2: str
        """
        base1 = "<svg xmlns=\"http://www.w3.org/2000/svg\" "
        base2 = "version=\"1.1\" width=\"{0}\" height=\"{1}\">\n".format(self.width, self.height)

        return base1 + base2

    @staticmethod
    def svgEnd() -> str:
        """
        svg描画終了
        :return end: str
        """
        end = "</svg>\n"
        return end

