# -*- coding: utf-8 -*-
import random


class ignore_closed:
    """忽略已经关闭的连接"""

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == AlreadyClosedError:
            return True
        return False


with ignore_closed():
    close_conn(conn)


class DummyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__ 会在进入管理器时被调用，同时可以返回结果
        # 返回一个增加了随机后缀的 name
        return f'{self.name}-{random.random()}'

    def __exit__(self, exc_type, exc_value, traceback):
        # __exit__ 会在退出管理器时被调用
        print('Exiting DummyContext')
        return False


with DummyContext('foo') as name:
    print(f'Name: {name}')


conn = create_conn(host, port, timeout=None)
try:
    conn.send_text('Hello, world!')
except Exception as e:
    print(f'Unable to use connection: {e}')
finally:
    conn.close()


class create_conn_obj:
    """创建连接对象，并在退出上下文时自动关闭"""

    def __init__(self, host, port, timeout=None):
        self.conn = create_conn(host, port, timeout=timeout)

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出管理器时关闭连接
        self.conn.close()
        return False


with create_conn_obj(host, port, timeout=None) as conn:
    try:
        conn.send_text('Hello, world!')
    except Exception as e:
        print(f'Unable to use connection: {e}')


try:
    close_conn(conn)
except AlreadyClosedError:
    pass

from contextlib import contextmanager


@contextmanager
def create_conn_obj(host, port, timeout=None):
    """创建连接对象，并在退出上下文时自动关闭"""
    conn = create_conn(host, port, timeout=timeout)
    try:
        yield conn
    finally:
        conn.close()
