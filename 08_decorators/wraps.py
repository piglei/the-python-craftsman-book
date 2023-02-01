# -*- coding: utf-8 -*-

import time
import random
from functools import wraps


def timer(func):
    """装饰器：记录并打印函数耗时"""

    @wraps(func)
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('function took: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


def calls_counter(func):
    """装饰器：记录函数被调用了多少次

    使用 `func.print_counter()` 可以打印统计到的信息
    """
    counter = 0

    @wraps(func)
    def decorated(*args, **kwargs):
        nonlocal counter
        counter += 1
        return func(*args, **kwargs)

    def print_counter():
        print(f'Counter: {counter}')

    decorated.print_counter = print_counter
    return decorated


@calls_counter
@timer
def random_sleep():
    """随机睡眠一小会"""
    time.sleep(random.random())


random_sleep()