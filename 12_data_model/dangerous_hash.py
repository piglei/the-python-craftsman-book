# -*- coding: utf-8 -*-


class HashByValue:
    """根据 value 属性计算哈希值"""

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)