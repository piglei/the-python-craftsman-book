# -*- coding: utf-8 -*-
import time


def delayed_start(func=None, *, duration=1):
    """装饰器：在执行被装饰函数前，等待一段时间

    :param duration: 需要等待的秒数
    """

    def decorator(_func):
        def wrapper(*args, **kwargs):
            print(f'Wait for {duration} second before starting...')
            time.sleep(duration)
            return _func(*args, **kwargs)

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)


@delayed_start
def hello():
    print('Hello, World!')


hello()


@delayed_start(duration=2)
def hello():
    print('Hello, World!')


hello()


@delayed_start()
def hello():
    print('Hello, World!')


hello()