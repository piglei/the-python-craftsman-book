# -*- coding: utf-8 -*-


def append_value(value, items=[]):
    """往 items 列表中追加内容，并返回列表"""
    items.append(value)
    return items


def append_value(value, items=None):
    # 在函数内部进行判断，保证参数默认每次都使用一个新的空列表
    if items is None:
        items = []
    items.append(value)
    return items


def query_users(limit, offset, *, min_followers_count, include_profile):
    """查询用户

    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    """
    ...


query_users(20, 0, 100, True)
query_users(limit=20, offset=0, min_followers_count=100, include_profile=True)
