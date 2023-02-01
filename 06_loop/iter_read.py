# -*- coding: utf-8 -*-


def count_digits(fname):
    """计算文件里包含多少个数字字符"""
    count = 0
    with open(fname) as file:
        for line in file:
            for s in line:
                if s.isdigit():
                    count += 1
    return count


def count_digits_v2(fname):
    """计算文件里包含多少个数字字符，每次读取 8kb"""
    count = 0
    block_size = 1024 * 8
    with open(fname) as file:
        while True:
            chunk = file.read(block_size)
            # 当文件没有更多内容时，read 调用将会返回空字符串 ''
            if not chunk:
                break
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count


from functools import partial


def count_digits_v3(fname):
    count = 0
    block_size = 1024 * 8
    with open(fname) as fp:
        # 使用 functools.partial 构造一个新的无需参数的函数
        _read = partial(fp.read, block_size)

        # 利用 iter() 构造一个不断调用 _read 的迭代器
        for chunk in iter(_read, ''):
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count


def read_file_digits(fp, block_size=1024 * 8):
    """生成器函数：分块读取文件内容，返回其中的数字字符"""
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ''):
        for s in chunk:
            if s.isdigit():
                yield s


def count_digits_v4(fname):
    count = 0
    with open(fname) as file:
        for num in read_file_digits(file):
            count += 1
    return count


from collections import defaultdict


def count_even_groups(fname):
    """分别统计文件里每个偶数字符出现的个数"""
    counter = defaultdict(int)
    with open(fname) as file:
        for num in read_file_digits(file):
            if int(num) % 2 == 0:
                counter[int(num)] += 1
    return counter


print(count_digits('small_file.txt'))
print(count_digits_v2('small_file.txt'))
print(count_digits_v3('small_file.txt'))
print(count_digits_v4('small_file.txt'))
print(count_even_groups('small_file.txt'))