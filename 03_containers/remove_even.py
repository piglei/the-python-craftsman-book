# -*- coding: utf-8 -*-


def remove_even(numbers):
    """去掉列表里所有的偶数"""
    # for i, number in enumerate(numbers):
    #     if number % 2 == 0:
    #         # 有问题的代码
    #         del numbers[i]
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)


numbers = [1, 2, 7, 4, 8, 11]
remove_even(numbers)
print(numbers)
# OUTPUT: [1, 7, 8, 11]
