from typing import List
from geometry.definition import start_definition, end_definition
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


def set_gradient_id(gradient_id: str) -> str:
    tmp = "url(#{})".format(gradient_id)

    return tmp


def generate_gradient_data() -> List[List[str]]:
    init_gradient_data: List[List[str]] = []
    class_data: List[str] = ["0%", "50%", "100"]
    offset_data: List[str] = ["#000000", "#d8d8d8", "#ffffff"]
    if len(class_data) == len(offset_data):
        init_gradient_data: List[List[str]] = [class_data, offset_data]

    return init_gradient_data


def test_linear_gradient1(id_name: str, gradient_data: List[List[str]]) -> None:
    linear_gradient1 = LinearGradient1(id_name, gradient_data)
    tmp = linear_gradient1.linear_gradient1()
    for count in tmp:
        print(count)


def test_linear_gradient2(id_name: str, gradient_data: List[List[str]]) -> None:
    linear_gradient2 = LinearGradient1(id_name, gradient_data)
    x = Vector2(0, 0)
    y = Vector2(0, 1)
    tmp = linear_gradient2.linear_gradient2(x, y)
    for count in tmp:
        print(count)


if __name__ == '__main__':
    init_id_name1 = "gradient1"
    init_id_name2 = "gradient2"
    print(start_definition())
    tmp_init_gradient_data = generate_gradient_data()
    test_linear_gradient1(init_id_name1, tmp_init_gradient_data)
    test_linear_gradient2(init_id_name2, tmp_init_gradient_data)
    print(end_definition())
