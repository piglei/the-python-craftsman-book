# -*- coding: utf-8 -*-


def magic_bubble_sort_2(numbers):
    """有魔力的冒泡排序算法，所有的偶数都被认为比奇数大"""
    j = len(numbers) - 1
    while j > 0:
        for i in range(j):
            if numbers[i] % 2 == 0 and numbers[i + 1] % 2 == 1:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                continue
            elif (numbers[i + 1] % 2 == numbers[i] % 2) and numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                continue
        j -= 1
    return numbers


from typing import List


def magic_bubble_sort(numbers: List[int]):
    """有魔力的冒泡排序算法，所有的偶数都被认为比奇数大

    :param numbers: 需要排序的列表，函数将会直接修改原始列表
    """
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            # 交换位置的两个条件：
            # - 前面是偶数，后面是奇数
            # - 前面和后面同为奇数或者偶数，但是前面比后面大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        stop_position -= 1
    return numbers


if __name__ == "__main__":
    l = [23, 32, 1, 3, 4, 19, 20, 2, 4]
    print(magic_bubble_sort(l))
    print(magic_bubble_sort_2(l))
