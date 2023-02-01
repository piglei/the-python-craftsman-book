# -*- coding: utf-8 -*-


def get_rectangle():
    """返回长方形的宽和高"""
    width = 100
    height = 20
    return width, height


result = get_rectangle()
print(result, type(result))

rectangle = (100, 20)
print(rectangle[0])
print(rectangle[1])


from collections import namedtuple

Rectangle = namedtuple('Rectangle', 'width,height')

from typing import NamedTuple


class Rectangle1(NamedTuple):
    width: int
    height: int


# rect = rectangle(100, 20)
rect = Rectangle(width=100, height=20)
# 可以像普通元组一样，通过数字索引访问成员
print(rect[0])

# 也能通过字段名称来访问
print(rect.width)
print(rect.height)

rect_str = Rectangle('string', 'not_a_number')


# rect.width += 1
# namedtuple 同样不允许被修改，执行后报错：
#   attributeerror: can't set attribute