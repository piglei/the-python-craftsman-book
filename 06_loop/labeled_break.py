# -*- coding: utf-8 -*-


def print_first_word(fp, prefix):
    """找到文件里，第一个以指定前缀开头的单词，并打印出来

    :param fp: 可读文件对象
    :param prefix: 需要寻找的单词前缀
    """
    first_word = None
    for line in fp:
        for word in line.split():
            if word.startswith(prefix):
                first_word = word
                # 注意：此处的 break 只能跳出最内层循环
                break
        # 一定要在外层加一个额外的 break 语句来判断是否结束循环
        if first_word:
            break

    if first_word:
        print(f'Found the first word startswith "{prefix}": "{first_word}"')
    else:
        print(f'Word starts with "{prefix}" was not found.')


def find_first_word(fp, prefix):
    """找到文件里，第一个以指定前缀开头的单词，并打印出来

    :param fp: 可读文件对象
    :param prefix: 需要寻找的单词前缀
    """
    for line in fp:
        for word in line.split():
            if word.startswith(prefix):
                return word
    return None


def print_first_word(fp, prefix):
    first_word = find_first_word(fp, prefix)
    if first_word:
        print(f'Found the first word startswith "{prefix}": "{first_word}"')
    else:
        print(f'Word starts with "{prefix}" was not found.')


with open('python_doc.txt') as fp:
    print_first_word(fp, 're')
