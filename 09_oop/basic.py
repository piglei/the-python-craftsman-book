# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, name, value):
        # 不允许设置年龄小于 0
        if name == 'age' and value < 0:
            raise ValueError(f'Invalid age value: {value}')
        super().__setattr__(name, value)

    def say(self):
        print(f"Hi, My name is {self.name}, I'm {self.age}")
