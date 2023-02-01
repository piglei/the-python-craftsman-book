# -*- coding: utf-8 -*-


class ThreeFactory:
    """在被迭代时不断生产 3

    :param repeat: 重复次数
    """

    def __init__(self, repeat):
        self.repeat = repeat

    def __iter__(self):
        for _ in range(self.repeat):
            yield 3