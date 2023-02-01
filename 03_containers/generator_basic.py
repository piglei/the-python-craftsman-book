# -*- coding: utf-8 -*-


def simple_gen():
    """一个简单生成器，返回数字 123"""
    yield 1
    yield 2
    yield 3


def generate_even(max_number):
    """一个简单生成器，返回 0 到 max_number 之间的所有偶数"""
    for i in range(0, max_number):
        # yield 和 return 最大的不同之处在于，return 会直接中断整个函数执行，
        # 返回结果，而 yield 会由循环语句触发，一步一步的往外生成多个结果
        if i % 2 == 0:
            yield i


for i in generate_even(10):
    print(i)
