def get_users() -> str:
    # users 本身是一个 Dict
    users = {"data": ["piglei", "raymond"]}
    # 尝试复用 users 这个变量，把它变成 List 类型
    users = []
    return users


if __name__ == "__main__":
    get_users()
