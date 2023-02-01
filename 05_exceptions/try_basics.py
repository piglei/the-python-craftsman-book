# -*- coding: utf-8 -*-


def safe_int(value):
    """尝试把输入转换为整数"""
    try:
        return int(value)
    except TypeError:
        # 当某类异常被抛出时，将会执行对应 except 下的语句
        print(f'type error: {type(value)} is invalid')
    except ValueError:
        # 你可以在一个 try 语句块下写多个 except
        print(f'value error: {value} is invalid')
    else:
        print('====================')
    finally:
        # finally 里的语句，无论如何都会被执行，哪怕 try 里直接 return
        print('function completed')


def incr_by_key(d, key):
    try:
        d[key] += 1
    except KeyError:
        print(f'key {key} does not exists, re-raise the exception')
        raise


safe_int(3)
safe_int(None)
safe_int('asdf')

incr_by_key({'foo': 1}, 'bar')