# 为所有性别为女性，或者级别大于 3 的活跃用户发放 10000 个金币
if user.is_active and (user.sex == 'female' or user.level > 3):
    user.add_coins(10000)
    return