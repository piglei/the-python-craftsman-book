# -*- coding: utf-8 -*-
import re


def mosaic(s):
    """把输入字符串替换为等长的星号字符"""
    return '*' * len(s)


import re


def mosaic_string(s):
    """用 * 替换输入字符串里面所有的连续数字"""
    return re.sub(r'\d+', '*', s)


def mosaic_matchobj(matchobj):
    """将匹配到的模式替换为等长星号字符串"""
    length = len(matchobj.group())
    return '*' * length


def mosaic_string(s):
    """用等长的 * 替换输入字符串里面所有的连续数字"""
    return re.sub(r'\d+', mosaic_matchobj, s)


_mosaic_char_index = 0


def mosaic_global_var(matchobj):
    """
    将匹配到的模式替换为其他字符，使用全局变量实现轮换字符效果
    """
    global _mosaic_char_index
    mosaic_chars = ['*', 'x']

    char = mosaic_chars[_mosaic_char_index]
    # 递增马赛克字符索引值
    _mosaic_char_index = (_mosaic_char_index + 1) % len(mosaic_chars)

    length = len(matchobj.group())
    return char * length


def make_cyclic_mosaic():
    """
    将匹配到的模式替换为其他字符，使用闭包实现轮换字符效果
    """
    char_index = 0
    mosaic_chars = ['*', 'x']

    def _mosaic(matchobj):
        nonlocal char_index
        char = mosaic_chars[char_index]
        char_index = (char_index + 1) % len(mosaic_chars)

        length = len(matchobj.group())
        return char * length

    return _mosaic


class CyclicMosaic:
    """使用会轮换的屏蔽字符，基于类实现"""

    _chars = ['*', 'x']

    def __init__(self):
        self._char_index = 0

    def generate(self, matchobj):
        char = self._chars[self._char_index]
        self._char_index = (self._char_index + 1) % len(self._chars)
        length = len(matchobj.group())
        return char * length


# print(re.sub(r'\d+', mosaic, 'reference 20, not group 2'))

print(re.sub(r'\d+', mosaic_global_var, '商店共 100 个苹果，小明用 12 块的价格买走了 8 个'))
print(re.sub(r'\d+', make_cyclic_mosaic(), '商店共 100 个苹果，小明用 12 块的价格买走了 8 个'))
print(re.sub(r'\d+', CyclicMosaic().generate, '商店共 100 个苹果，小明用 12 块的价格买走了 8 个'))
