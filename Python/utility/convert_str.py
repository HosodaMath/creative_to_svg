from mathematics.vector import Vector2
from typing import List


def format_one(data: List[Vector2]) -> str:
    n = len(data)
    x, y = data[0].get_x(), data[0].get_y()
    sx, sy = "{0}".format(x), "{0}".format(y)
    t = sx + " " + sy
    for count in range(1, n):
        tmp_x = data[count].get_x()
        tmp_y = data[count].get_y()
        tmp_sx = "{0}".format(tmp_x)
        tmp_sy = "{0}".format(tmp_y)
        t = t + " " + tmp_sx + " " + tmp_sy

    return t
