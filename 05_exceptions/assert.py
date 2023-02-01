# -*- coding: utf-8 -*-


def print_string(s):
    assert isinstance(s, str), 's must be string'
    print(s)


print_string(3)
print_string('foo')


def print_string(s):
    if not isinstance(s, str):
        raise TypeError('s must be string')
    print(s)
