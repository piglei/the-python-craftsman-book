# -*- coding: utf-8 -*-


class StringList:
    """用于保存多个字符串的数据类，实现了 read() 和可迭代接口"""

    def __init__(self, strings):
        self.strings = strings

    def read(self):
        return ''.join(self.strings)

    def __iter__(self):
        for s in self.strings:
            yield s


def count_vowels(fp):
    """统计某个文件中，包含元音字母(aeiou)的数量"""
    if not hasattr(fp, 'read'):
        raise TypeError('must provide a valid file object')

    VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for line in fp:
        for char in line:
            if char.lower() in VOWELS_LETTERS:
                count += 1
    return count


from io import StringIO

print(count_vowels(StringIO('Hello, world!')))
