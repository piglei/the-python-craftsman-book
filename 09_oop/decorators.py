# -*- coding: utf-8 -*-

import random


class Duck:
    def __init__(self, color):
        self.color = color

    def quack(self):
        # print(f"Hi, I'm a {self.color} duck!")
        pass

    @classmethod
    def create_random(cls):
        """创建一只随机颜色鸭子"""
        color = random.choice(['yellow', 'white', 'gray'])
        return cls(color=color)


class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        sound = self.get_sound()
        print(f'{self.name}: {sound}...')

    @staticmethod
    def get_sound():
        repeats = random.randrange(1, 10)
        return ' '.join(['Meow'] * repeats)


import os


class FilePath:
    def __init__(self, path):
        self.path = path

    @property
    def basename(self):
        """获取文件名"""
        return self.path.rsplit(os.sep, 1)[-1]

    @basename.setter
    def basename(self, name):
        """修改当前路径里的文件名部分"""
        new_path = self.path.rsplit(os.sep, 1)[:-1] + [name]
        self.path = os.sep.join(new_path)

    @basename.deleter
    def basename(self):
        raise RuntimeError('Can not delete basename!')
