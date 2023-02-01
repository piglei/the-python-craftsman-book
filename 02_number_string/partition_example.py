# -*- coding: utf-8 -*-


def extract_value(s):
    items = s.split(':')
    # 因为 s 不一定会包含 ':'，所以需要对结果长度进行判断
    if len(items) == 2:
        return items[1]
    else:
        return ''


print(repr(extract_value('name:piglei')))
print(repr(extract_value('name')))


def extract_value_v2(s):
    # 当 s 包含分隔符 : 时，元组最后一个成员刚好是 value。
    # 若是没有分隔符，最后一个成员默认是空字符串 ''
    return s.partition(':')[-1]


print(repr(extract_value_v2('name:piglei')))
print(repr(extract_value_v2('name')))


with open('temp', 'w', encoding='gbk') as fp:
    fp.write('你好，世界。')