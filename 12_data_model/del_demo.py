# -*- coding: utf-8 -*-


class Foo:
    def __del__(self):
        print(f'cleaning up {self}...')