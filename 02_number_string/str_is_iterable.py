usernames = ['piglei', 'raymondzhu']

for username in usernames:
    print(username)


chars = 'abc'

# 展开赋值为多个变量，就好像 a, b, c = ['a', 'b', 'c'] 一样
a, b, c = chars

# 循环整个字符串
for ch in chars:
    print(ch)

# 对字符串做切片
print(chars[:2])
# 输出：
# ab

# 调用 join 方法拼接
print('_'.join(chars))
# 输出：
# a_b_c

# 用星号表达式展开
print('{}{}{}'.format(*chars))
# 输出：
# abc
