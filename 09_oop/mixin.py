# -*- coding: utf-8 -*-
import sys


class InfoDumperMixin:
    """Mixin：输出当前实例信息"""

    def dump_info(self):
        d = self.__dict__
        print("Number of members: {}".format(len(d)))
        print("Details:")
        for key, value in d.items():
            print(f'  - {key}: {value}')


class Person(InfoDumperMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age