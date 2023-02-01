# -*- coding: utf-8 -*-


class DuckWithProperty:
    @property
    def color(self):
        return 'gray'


class DuckWithStaticMethod:
    @staticmethod
    def color():
        return 'gray'