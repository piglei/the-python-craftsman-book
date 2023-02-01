class UserCollection:
    """用户保存多个用户的集合工具类"""

    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)


users = UserCollection(['piglei', 'raymond'])

# 仅当用户列表里面有数据时，打印语句
if len(users.items) > 0:
    print("There's some users in collection!")

# 定义了 __len__ 方法后，UserCollection 对象本身就可以被用于布尔判断了
if users:
    print("There's some users in collection!")


class ScoreJudger:
    """仅当分数大于 60 时为真"""

    def __init__(self, score):
        self.score = score

    def __bool__(self):
        return self.score >= 60
