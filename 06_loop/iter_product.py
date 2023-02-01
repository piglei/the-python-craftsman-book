# -*- coding: utf-8 -*-
numbers_1 = [1, 0, 5, 13]
numbers_2 = [3, 4, -1, 2]
numbers_3 = [9, 0, 3, -4]


def find_twelve(num_list1, num_list2, num_list3):
    """从 3 个数字列表中，寻找是否存在和为 12 的 3 个数"""
    for num1 in num_list1:
        for num2 in num_list2:
            for num3 in num_list3:
                if num1 + num2 + num3 == 12:
                    return num1, num2, num3


print(find_eight(numbers_1, numbers_2, numbers_3))


from itertools import product


def find_twelve_v2(num_list1, num_list2, num_list3):
    for num1, num2, num3 in product(num_list1, num_list2, num_list3):
        if num1 + num2 + num3 == 12:
            return num1, num2, num3


print(find_eight_v2(numbers_1, numbers_2, numbers_3))
