# -*- coding: utf-8 -*-


class A:
    def say(self):
        print("I'm A")


class B(A):
    pass


class C(A):
    def say(self):
        print("I'm C")


class D(B, C):
    pass