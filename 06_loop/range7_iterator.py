# -*- coding: utf-8 -*-


names = ['foo', 'bar', 'foobar']

for name in names:
    print(name)

iterator = iter(names)
while True:
    try:
        name = next(iterator)
        print(name)
    except StopIteration:
        break


class Range7:
    """生成一段范围内的可被 7 整除或包含 7 的整数

    :param start: 开始数字
    :param end: 结束数字
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        # 使用 current 保存当前所处的位置
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            # 当已经到达边界时，抛出异常终止迭代
            if self.current >= self.end:
                raise StopIteration

            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def num_is_valid(self, num):
        """判断数字是否满足要求"""
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


class _Range7:
    """生成一段范围内的可被 7 整除，或包含 7 的数字"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # 返回一个新的迭代器对象
        return Range7Iterator(self)


class Range7Iterator:
    def __init__(self, range_obj):
        self.range_obj = range_obj
        self.current = range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current >= self.range_obj.end:
                raise StopIteration

            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def num_is_valid(self, num):
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


numbers = Range7(0, 20)
# print(next(numbers))
# print(list(numbers))
# print(list(numbers))

for n in numbers:
    print(n)
