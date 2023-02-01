# -*- coding: utf-8 -*-

MAX_LENGTH_OF_NAME = 12
MAX_ITEMS_QUOTA = 10


def get_current_items():
    return []


class Item:
    def __init__(self, name):
        self.name = name


class CreateItemError(Exception):
    """创建 Item 失败"""


def create_item(name):
    """创建一个新的 Item

    :raises: 当无法创建时抛出 CreateItemError
    """
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError('name of item is too long')
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
        raise CreateItemError('items is full')
    return Item(name=name)


def create_from_input():
    name = input()
    try:
        item = create_item(name)
    except CreateItemError as e:
        print(f'create item failed: {e}')
    else:
        print(f'item<{name}> created')


class CreateItemError(Exception):
    """创建 Item 失败"""


class CreateErrorItemsFull(CreateItemError):
    """当前的 Item 容器已满"""


class CreateItemError(Exception):
    """创建 Item 失败

    :param error_code: 错误代码
    :param message: 错误信息
    """

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(f'{self.error_code} - {self.message}')


raise CreateItemError('name_too_long', 'name of item is too long')
raise CreateItemError('items_full', 'items is full')
