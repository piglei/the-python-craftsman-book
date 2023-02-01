def sum_even_only(numbers):
    """对 numbers 里面所有的偶数求和"""
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result


def even_only(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


def sum_even_only_v2(numbers):
    """对 numbers 里面所有的偶数求和"""
    result = 0
    for num in even_only(numbers):
        result += num
    return result

    # return sum(only_even(numbers))


numbers = [1, 2, 8, 9, 13, -1]
print(sum_even_only(numbers))
print(sum_even_only_v2(numbers))
