# -*- coding: utf-8 -*-

movie = {'name': 'Burning', 'type': 'movie', 'year': 2018}

# 通过 key 来获取某个 value，如果 Key 不存在会抛出 KeyError
print(movie['year'])

# 字典是一种可变类型，所以你可以给它增加新的 key
movie['rating'] = '10'

# 最常用的两种遍历方式：
#
#   遍历字典的所有 key
for key in movie:
    print(key)
#   遍历字典的所有 key/value 键值对：
for key, value in movie.items():
    print(key, value)


# 判断某个 key 是否存在
# 返回：True / False
'some_key' in movie

# 尝试获取某个值，如不存在时返回 default 默认值
movie.get('some_key', default='DEFAULT')

# 批量修改字典内容
movie.update(year=2020, rating=1)


from collections import OrderedDict

d = OrderedDict()
# d = {}
d['FIRST_KEY'] = 1
d['SECOND_KEY'] = 2

for key in d:
    print(key)
