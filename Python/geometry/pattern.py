from mathematics.vector import Vector2
from utility.convert_str import format_id


class Pattern:
    def __init__(self, init_id: str, init_data: Vector2, init_size: Vector2) -> None:
        """
        Pattern generator class
        :param init_id: str init_id
        :param init_data: Vector2 init location data
        :param init_size: Vector2 init size data
        """
        self.id = init_id
        self.data = init_data
        self.size = init_size

    def start_pattern1(self) -> str:
        """
        Pattern start
        :return:
        """
        start = "<pattern "
        id_str = "id=\"{0}\" ".format(self.id)
        location_str = "x=\"{0}\" y=\"{1}\" ".format(self.data.get_x(), self.data.get_y())
        size_str = "width=\"{0}\" height=\"{1}\" ".format(self.size.get_x(), self.size.get_y())
        end = ">\n"
        init_pattern1 = start + id_str + location_str + size_str + end

        return init_pattern1

    def start_pattern2(self, patternUnits="userSpaceOnUse", patternContentUnits="userSpaceOnUse") -> str:
        """
        Pattern unit and spacing size
        :param patternUnits: str pattern unit
        :param patternContentUnits: str pattern space unit
        :return:
        """
        start = "<pattern "
        id_str = "id=\"{0}\" ".format(self.id)
        location_str = "x=\"{0}\" y=\"{1}\" ".format(self.data.get_x(), self.data.get_y())
        size_str = "width=\"{0}\" height=\"{1}\" ".format(self.size.get_x(), self.size.get_y())
        space_str = "patternUnits=\"{0}\" patternContentUnit=\"{1}\" ".format(patternUnits, patternContentUnits)
        end = ">\n"
        init_pattern2 = start + id_str + location_str + size_str + space_str + end

        return init_pattern2

    @staticmethod
    def end_pattern() -> str:
        """
        Patten end
        :return:
        """
        return "</pattern>\n"


def set_pattern_id(init_id: str):
    return format_id(init_id)


if __name__ == '__main__':
    init_name_id = "id1"
    init_location_data = Vector2(0, 0)
    init_size_data = Vector2(0.25, 0.25)
    pattern1 = Pattern(init_name_id, init_location_data, init_size_data)

    print(pattern1.start_pattern1())
    print(pattern1.end_pattern())

    print(pattern1.start_pattern2())
    print(pattern1.end_pattern())
