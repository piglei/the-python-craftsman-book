# -*- coding: utf-8 -*-
from enum import Enum
from collections import defaultdict
from collections.abc import MutableMapping


class PagePerfLevel(str, Enum):
    LT_100 = 'Less than 100 ms'
    LT_300 = 'Between 100 and 300 ms'
    LT_1000 = 'Between 300 ms and 1 s'
    GT_1000 = 'Greater than 1 s'


class PerfLevelDict(MutableMapping):
    """存储响应时间性能级别的字典"""

    def __init__(self):
        self.data = defaultdict(int)

    def __getitem__(self, key):
        """当某个级别不存在时，默认返回 0"""
        return self.data[self.compute_level(key)]

    def __setitem__(self, key, value):
        """将 key 转换为对应的性能级别，然后设置值"""
        self.data[self.compute_level(key)] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def items(self):
        """按照顺序返回性能级别数据"""
        return sorted(
            self.data.items(),
            key=lambda pair: list(PagePerfLevel).index(pair[0]),
        )

    def total_requests(self):
        """返回总请求数"""
        return sum(self.values())

    @staticmethod
    def compute_level(time_cost_str):
        """根据响应时间计算性能级别"""
        # 假如已经是性能等级，不做转换直接返回
        if time_cost_str in list(PagePerfLevel):
            return time_cost_str

        time_cost = int(time_cost_str)
        if time_cost < 100:
            return PagePerfLevel.LT_100
        elif time_cost < 300:
            return PagePerfLevel.LT_300
        elif time_cost < 1000:
            return PagePerfLevel.LT_1000
        return PagePerfLevel.GT_1000


def analyze_v2():
    path_groups = defaultdict(PerfLevelDict)
    with open("logs.txt", "r") as fp:
        for line in fp:
            path, time_cost = line.strip().split()
            path_groups[path][time_cost] += 1

    for path, result in path_groups.items():
        print(f'== Path: {path}')
        print(f'   Total requests: {result.total_requests()}')
        print(f'   Performance:')
        for level_name, count in result.items():
            print(f'     - {level_name}: {count}')


if __name__ == '__main__':
    analyze_v2()