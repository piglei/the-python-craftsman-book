# -*- coding: utf-8 -*-


def incr_by_one(value):
    """对输入整数 + 1 ，返回新的值

    :param value: 整型，或者可以转成整型的字符串
    :return: 整型结果
    """
    if isinstance(value, int):
        return value + 1
    elif isinstance(value, str) and value.isdigit():
        return int(value) + 1
    else:
        print(f'Unable to perform incr for value: "{value}"')


def incr_by_one(value):
    """对输入整数 + 1 ，返回新的值

    :param value: 整型，或者可以转成整型的字符串
    :return: 整型结果
    """
    try:
        return int(value) + 1
    except (TypeError, ValueError) as e:
        print(f'Unable to perform incr for value: "{value}", error: {e}')


def main():
    print(incr_by_one(5))
    print(incr_by_one('73'))
    print(incr_by_one('not_a_number'))
    print(incr_by_one(object()))


if __name__ == '__main__':
    main()
