def import_users_from_file(fp):
    """尝试从文件对象读取用户，然后导入到数据库中

    :param fp: 可读文件对象
    :return: 成功与失败数量
    """
    # 初始化变量：重复用户、黑名单用户、正常用户
    duplicated_users, banned_users, normal_users = [], [], []
    for line in fp:
        parsed_user = parse_user(line)
        # ... 进行判断处理，修改上面定义的 {X}_users 变量

    succeeded_count, failed_count = 0, 0
    # ... 读取 {X}_users 变量，写入数据库并修改成功失败数量
    return succeeded_count, failed_count


class ImportedSummary:
    """保存导入结果摘要的数据类"""

    def __init__(self):
        self.succeeded_count = 0
        self.failed_count = 0


class ImportingUserGroup:
    """用于暂存用户导入处理的数据类"""

    def __init__(self):
        self.duplicated = []
        self.banned = []
        self.normal = []


def import_users_from_file(fp):
    """尝试从文件对象读取用户，然后导入到数据库中

    :param fp: 可读文件对象
    :return: 成功与失败数量
    """
    importing_user_group = ImportingUserGroup()
    for line in fp:
        parsed_user = parse_user(line)
        # ... 进行判断处理，修改上面定义的 importing_user_group 变量

    summary = ImportedSummary()
    # ... 读取 importing_user_group，写入数据库并修改成功失败数量
    return summary.succeeded_count, summary.failed_count
