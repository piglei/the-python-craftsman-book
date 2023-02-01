# -*- coding: utf-8 -*-

_validators = {}


class ValidatorMeta(type):
    """元类：将所有校验器类统一注册起来，方便后续使用"""

    def __new__(cls, name, bases, attrs):
        ret = super().__new__(cls, name, bases, attrs)
        _validators[attrs['name']] = ret
        return ret


class StringValidator(metaclass=ValidatorMeta):
    name = 'string'


class IntegerValidator(metaclass=ValidatorMeta):
    name = 'int'


print(_validators)

_validators = {}


def register(cls):
    """装饰器：将所有校验器类统一注册起来，方便后续使用"""
    _validators[cls.name] = cls
    return cls


@register
class StringValidator:
    name = 'string'


@register
class IntegerValidator:
    name = 'int'


print(_validators)