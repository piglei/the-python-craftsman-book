# -*- coding: utf-8 -*-
from itertools import islice


def parse_titles(filename):
    """从隔行数据文件中读取 reddit 主题名称"""
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp):
            # 跳过无意义的 '---' 分隔符
            if i % 2 == 0:
                yield line.strip()


def parse_titles_v2(filename):
    with open(filename, 'r') as fp:
        # 设置 step=2，跳过无意义的 '---' 分隔符
        for line in islice(fp, 0, None, 2):
            yield line.strip()


print(list(parse_titles('reddit_titles.txt')))
print(list(parse_titles_v2('reddit_titles.txt')))
