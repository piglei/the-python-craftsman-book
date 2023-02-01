from typing import AsyncGenerator


class Duck:
    """一只鸭子

    :param name: 鸭子的名字
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'<Duck name="{self.name}">'


class Person:
    """人

    :param name: 姓名
    :param age: 年龄
    :param favorite_color: 最喜欢的颜色
    """

    def __init__(self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def get_simple_display(self):
        return f'{self.name}({self.age})'

    def get_long_display(self):
        return f'{self.name} is {self.age} years old.'


class Person:
    """人

    :param name: 姓名
    :param age: 年龄
    :param favorite_color: 最喜欢的颜色
    """

    def __init__(self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{cls_name}(name={name!r}, age={age!r}, favorite_color={color!r})'.format(
            cls_name=self.__class__.__name__,
            name=self.name,
            age=self.age,
            color=self.favorite_color,
        )

    def __format__(self, format_spec):
        """定义对象在字符串格式化时的行为

        :param format_spec: 需要的格式，默认为 ''
        """
        if format_spec == 'verbose':
            return f'{self.name}({self.age})[{self.favorite_color}]'
        elif format_spec == 'simple':
            return f'{self.name}({self.age})'
        return self.name
