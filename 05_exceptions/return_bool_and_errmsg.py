# -*- coding: utf-8 -*-

MAX_LENGTH_OF_NAME = 12
MAX_ITEMS_QUOTA = 10


def get_current_items():
    return []


class Item:
    def __init__(self, name):
        self.name = name


def create_item(name):
    """接收名称，创建 Item 对象

    :return: (对象，错误信息)，成功时错误信息为 ''
    """
    if len(name) > MAX_LENGTH_OF_NAME:
        return None, 'name of item is too long'
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
        return None, 'items is full'
    return Item(name=name), ''


def create_from_input():
    name = input()
    item, err_msg = create_item(name)
    if err_msg:
        print(f'create item failed: {err_msg}')
    else:
        print('item<{name}> created')
