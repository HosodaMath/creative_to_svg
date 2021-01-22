from typing import List
from geometry.definition import start_definition, end_definition
from utility.convert_str import format_id
from mathematics.vector import Vector2


# stop-opacityを後で追加する
# css対応を行う

class LinearGradient1:
    def __init__(self, init_id: str, init_data: List[List[str]]) -> None:
        """
        線形グラデーションのクラス
        :param init_id: str gradient idの初期化
        :param init_data: List[List[str]] class and offset dataの初期化
        """
        self.id = init_id
        self.data = init_data

    def linear_gradient1(self) -> List[str]:
        """
        グラデーションの方向指定はなし
        :return: List[str] グラデーションのタグデータを返す
        """
        data: List[str] = []

        start_linear_gradient = "<linearGradient id=\"{}\">\n".format(self.id)
        data.append(start_linear_gradient)

        n = len(self.data[0])
        m = len(self.data[1])
        if n == m:
            for count in range(0, n):
                gradient_data = "<stop offset=\"{}\" stop-color=\"{}\"/>\n".format(
                    self.data[0][count], self.data[1][count])
                data.append(gradient_data)

        end_linear_gradient = "</linearGradient>\n"
        data.append(end_linear_gradient)

        return data

    def linear_gradient2(self, init_x: Vector2, init_y: Vector2) -> List[str]:
        """
         グラデーションの方向指定あり
        :param init_x: Vector2 x1とx2
        :param init_y: Vector2 y1とy2
        :return: List[str] グラデーションのタグデータを返す
        """
        data: List[str] = []

        start_linear_gradient = "<linearGradient id=\"{}\" x1=\"{}\" x2=\"{}\" y1=\"{}\" y2=\"{}\">\n".format(
            self.id, init_x.get_x(), init_x.get_y(), init_y.get_x(), init_y.get_y())
        data.append(start_linear_gradient)

        n = len(self.data[0])
        m = len(self.data[1])
        if n == m:
            for count in range(0, n):
                gradient_data = "<stop offset=\"{}\" stop-color=\"{}\"/>\n".format(
                    self.data[0][count], self.data[1][count])
                data.append(gradient_data)

        end_linear_gradient = "</linearGradient>\n"
        data.append(end_linear_gradient)

        return data


class RadialGradient1:
    def __init__(self, init_id: str, init_data: List[List[str]]) -> None:
        """
        放射型グラデーションのクラス
        :param init_id: str gradient idの初期化
        :param init_data: List[List[str]] class and offset dataの初期化
        """
        self.id = init_id
        self.data = init_data

    def radial_gradient1(self) -> List[str]:
        """
        グラデーションの方向指定はなし
        :return: List[str] グラデーションのタグデータを返す
        """
        data: List[str] = []

        start_radial_gradient = "<radialGradient id=\"{}\">\n".format(self.id)
        data.append(start_radial_gradient)

        n = len(self.data[0])
        m = len(self.data[1])
        if n == m:
            for count in range(0, n):
                gradient_data = "<stop offset=\"{}\" stop-color=\"{}\"/>\n".format(
                    self.data[0][count], self.data[1][count])
                data.append(gradient_data)

        end_radial_gradient = "</radialGradient>\n"
        data.append(end_radial_gradient)

        return data


def set_gradient_id(gradient_id: str) -> str:
    tmp = format_id(gradient_id)

    return tmp
