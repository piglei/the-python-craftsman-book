# -*- coding: utf-8 -*-

def counter():
    value = 0
    def _counter():
        # nonlocal 用来标注变量来自上层作用域
        nonlocal value

        value += 1
        return value
    return _counter
