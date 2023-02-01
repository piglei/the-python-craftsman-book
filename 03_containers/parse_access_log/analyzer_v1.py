# -*- coding: utf-8 -*-
from enum import Enum


class PagePerfLevel(str, Enum):
    LT_100 = 'Less than 100 ms'
    LT_300 = 'Between 100 and 300 ms'
    LT_1000 = 'Between 300 ms and 1 s'
    GT_1000 = 'Greater than 1 s'


def analyze_v1():
    path_groups = {}
    with open("logs.txt", "r") as fp:
        for line in fp:
            path, time_cost_str = line.strip().split()

            # 根据页面耗时计算性能级别
            time_cost = int(time_cost_str)
            if time_cost < 100:
                level = PagePerfLevel.LT_100
            elif time_cost < 300:
                level = PagePerfLevel.LT_300
            elif time_cost < 1000:
                level = PagePerfLevel.LT_1000
            else:
                level = PagePerfLevel.GT_1000

            # 如果路径第一次出现，存入初始值
            if path not in path_groups:
                path_groups[path] = {}

            # 如果性能 level 第一次出现，存入初始值 1
            try:
                path_groups[path][level] += 1
            except KeyError:
                path_groups[path][level] = 1

    for path, result in path_groups.items():
        print(f'== Path: {path}')
        total = sum(result.values())
        print(f'   Total requests: {total}')
        print(f'   Performance:')

        # 在输出结果前，按照“性能级别”在 PagePerfLevel 里面的顺序排列，小于 100 毫秒
        # 的在最前面
        sorted_items = sorted(result.items(), key=lambda pair: list(PagePerfLevel).index(pair[0]))
        for level_name, count in sorted_items:
            print(f'     - {level_name}: {count}')


if __name__ == "__main__":
    analyze_v1()