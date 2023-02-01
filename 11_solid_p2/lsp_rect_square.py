class Rectangle:
    """长方形

    :param width: 宽度
    :param height: 高度
    """

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    def get_area(self) -> int:
        """返回当前长方形的面积"""
        return self.width * self.height


class Square(Rectangle):
    """正方形

    :param length: 边长
    """

    def __init__(self, length: int):
        self._width = length
        self._height = length

    @property
    def width(self):
        return super().width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._height = value

    @property
    def height(self):
        return super().height

    @height.setter
    def height(self, value: int):
        self._width = value
        self._height = value


def test_rectangle_get_area(r: Rectangle):
    r.width = 3
    r.height = 5
    assert r.get_area() == 15