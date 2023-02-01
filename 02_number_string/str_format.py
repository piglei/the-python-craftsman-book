username, score = 'piglei', 100

# f-string
print(f'Welcome {username}, your score is {score:d}')

# str.format
print('Welcome {}, your score is {:d}'.format(username, score))
# C 风格格式化
print('Welcome %s, your score is %d' % (username, score))


print('{:>20}'.format(username))
print(f'{username:>20}')


print('{0}: name={0} score={1}'.format(username, score))
