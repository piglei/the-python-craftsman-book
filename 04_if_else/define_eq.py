# -*- coding: utf-8 -*-


class EqualWithAnything:
    """与任何对象相等"""

    def __eq__(self, other):
        # 方法里的 other 方法代表 == 操作时右边的对象，比如
        # x == y 会调用 x 的 __eq__ 方法，other 参数为 y
        return True