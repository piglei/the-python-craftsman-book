# -*- coding: utf-8 -*-
class UpperDict(dict):
    """总是把 key 转为大写"""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)