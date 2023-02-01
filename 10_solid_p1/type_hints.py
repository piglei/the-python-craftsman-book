import random


class Duck:
    """鸭子类

    :param color: 鸭子颜色
    """

    def __init__(self, color):
        self.color = color

    def quack(self):
        print(f"Hi, I'm a {self.color} duck!")


def create_random_ducks(number):
    """创建一批随机颜色鸭子

    :param number: 需要创建的鸭子数量
    """
    ducks = []
    for _ in number:
        color = random.choice(['yellow', 'white', 'gray'])
        ducks.append(Duck(color=color))
    return ducks


# type hints
from typing import List


class Duck:
    def __init__(self, color: str):
        self.color = color

    def quack(self) -> None:
        print(f"Hi, I'm a {self.color} duck!")


def create_random_ducks(number: int) -> List[Duck]:
    """创建一批随机颜色鸭子

    :param number: 需要创建的鸭子数量
    """
    ducks: List[Duck] = []
    for _ in number:
        color = random.choice(['yellow', 'white', 'gray'])
        ducks.append(Duck(color=color))
    return ducks
