# -*- coding: utf-8 -*-


class Square:
    """正方形

    :param length: 边长
    """

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def __eq__(self, other):
        # 在判断两对象是否相等时，先检验 other 是否同为当前类型
        if isinstance(other, self.__class__):
            return self.length == other.length
        return False

    def __ne__(self, other):
        # “不等”运算的结果一般会直接对“等于”取反
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.length < other.length
        # 当对象不支持某种运算时，可以返回 NotImplemented 值
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.length > other.length
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


from functools import total_ordering


@total_ordering
class Square:
    """正方形

    :param length: 边长
    """

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.length < other.length
        return NotImplemented