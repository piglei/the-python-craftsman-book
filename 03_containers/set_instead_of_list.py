# -*- coding: utf-8 -*-
# 这个例子不是特别恰当，因为当目标集合特别小时，使用集合还是列表对效率的影响微乎其微
# 但这不是重点 :)

VALID_NAMES = ["piglei", "raymond", "jack", "bojack"]

# 转换为集合类型专门用于成员判断
VALID_NAMES_SET = set(VALID_NAMES)


def validate_name(name):
    if name not in VALID_NAMES_SET:
        raise ValueError(f"{name} is not a valid name!")
