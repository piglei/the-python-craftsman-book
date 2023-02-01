users = {"tom": 19, "jenny": 13, "jack": None, "andrew": 43}


def sort_users(users):

    # 普通写法：生成一份复合排序 key：（是否没有年龄，年龄）
    def key_func(username):
        age = users[username]
        # 当年龄为空时，第一个元素值为 True，永远会被排在最后面
        return age is None, age

    return sorted(users.keys(), key=key_func)


def sort_users_inf(users):
    def key_func(username):
        age = users[username]
        # 当年龄为空时，返回正无穷大做为 key，因此就会被排到最后面
        return age if age is not None else float('inf')

    return sorted(users.keys(), key=key_func)


print(sort_users(users))
print(sort_users_inf(users))
