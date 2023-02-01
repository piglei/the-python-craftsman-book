# -*- coding: utf-8 -*-


class InfoDescriptor:
    """打印帮助信息的描述符"""

    def __get__(self, instance, owner=None):
        print(f'Calling __get__, instance: {instance}, owner: {owner}')
        if not instance:
            print('Calling without instance...')
            return self
        return 'informative descriptor'

    def __set__(self, instance, value):
        print(f'Calling __set__, instance: {instance}, value: {value}')

    def __delete__(self, instance):
        raise RuntimeError('Deletion not supported!')


class Foo:
    bar = InfoDescriptor()
