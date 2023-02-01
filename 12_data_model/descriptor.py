# -*- coding: utf-8 -*-


class Person:
    """
    人

    :name: 姓名
    :age: 年龄
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """设置年龄，只允许 0-150 之间的数值"""
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError('value is not a valid integer!')

        if not (0 < value < 150):
            raise ValueError('value must between 0 and 150!')
        self._age = value


class IntegerField:
    """整型字段，只允许一定范围的整型值

    :param min_value: 允许的最小值
    :param max_value: 允许的最大值
    """

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner=None):
        # 当不是通过实例访问时，直接返回描述符对象，这是最常见的做法
        if not instance:
            return self
        # 返回保存在实例字典里的值
        return instance.__dict__['_integer_field']

    def __set__(self, instance, value):
        # 校验后将值保存在实例字典里
        value = self._validate_value(value)
        instance.__dict__['_integer_field'] = value

    def _validate_value(self, value):
        """校验值是否为符合要求的整数"""
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError('value is not a valid integer!')

        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f'value must between {self.min_value} and {self.max_value}!'
            )
        return value


class IntegerField:
    """整型字段，只允许一定范围的整型值

    :param min_value: 允许的最小值
    :param max_value: 允许的最大值
    """

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        # 将绑定属性名保存在描述符对象中
        # 对于 age = IntegerField(...) 来说，此处的 name 就是 "age"
        # self._name = name
        pass

    def __get__(self, instance, owner=None):
        if not instance:
            return self
        # 在数据存取时，使用动态的 self._name
        return instance.width
        # return instance.__dict__[self._name]

    def __set__(self, instance, value):
        value = self._validate_value(value)
        instance.width = value
        # instance.__dict__[self._name] = value

    def _validate_value(self, value):
        """校验值是否为符合要求的整数"""
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError(f'{self._name} is not a valid integer!')

        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f'{self._name} must between {self.min_value} and {self.max_value}!'
            )
        return value


class Person:
    age = IntegerField(min_value=0, max_value=150)

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Rectangle:
    width = IntegerField(min_value=1, max_value=10)
    height = IntegerField(min_value=1, max_value=5)

    def __init__(self, width, height):
        self.width = width
        self.height = height
