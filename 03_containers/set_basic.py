# -*- coding: utf-8 -*-

# 集合字面量的语法和字典很像，都是使用大括号，但是不是 "key: value" 的格式
fruits = {'apple', 'orange', 'apple', 'pineapple'}
print(fruits)
# >>>
# 集合的效果：重复的 'apple' 消失了，顺序也被打乱了。
# {'pineapple', 'orange', 'apple'}

# 注意：{} 表示的是一个空字典，而不是一个空集合
# empty_set = {}

# 正确初始化一个空集合
empty_set = set()

# 通过可迭代对象创建一个新集合
new_set = set(['foo', 'foo', 'bar'])


fruits_1 = {'apple', 'orange', 'pineapple'}
fruits_2 = {'tomato', 'orange', 'grapes', 'mango'}

# 求交集：两个集合中都有的东西
print(fruits_1 & fruits_2)
print(fruits_1.intersection(fruits_2))
# >>>
# {'orange'}

# 求并集：两个集合的东西合起来
print(fruits_1 | fruits_2)
print(fruits_1.union(fruits_2))
# >>>
# {'mango', 'orange', 'grapes', 'pineapple', 'apple', 'tomato'}

# 求差集：一个有，另一个没有的东西
print(fruits_1 - fruits_2)
print(fruits_1.difference(fruits_2))
# >>>
# {'apple', 'pineapple'}


valid_set = set(['apple', 30, 1.3, ('foo')])
# 可以成功初始化

invalid_set = set(['foo', [1, 2, 3]])
# >>>
# 报错：TypeError: unhashable type: 'list'