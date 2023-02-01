QUALIFIED_POINTS = 80


class CreateUserPointError(Exception):
    """创建得分纪录失败时抛出"""


class UserPoint:
    """用户得分记录"""

    def __init__(self, username, points):
        self.username = username
        self.points = points

    def is_qualified(self):
        """返回得分是否合格"""
        return self.points >= QUALIFIED_POINTS


def make_userpoint(point_string):
    """从字符串初始化一条得分记录

    :param point_string: 形如 "piglei 1" 的表示得分记录的字符串
    :return: UserPoint 对象
    :raises: 当输入数据不合法时返回 CreateUserPointError
    """
    try:
        username, points = point_string.split()
        points = int(points)
    except ValueError:
        raise CreateUserPointError('input must follow pattern "{username} {points}"')

    if points < 0:
        raise CreateUserPointError('points can not be negative')
    return UserPoint(username=username, points=points)


def calc_qualified_count(points_data):
    """计算得分合格的总人数

    :param points_data: 字符串格式的用户得分列表
    """
    result = 0
    for point_string in points_data:
        try:
            point_obj = make_userpoint(point_string)
        except CreateUserPointError:
            pass
        else:
            result += point_obj.is_qualified()
    return result


data = [
    'piglei 96',
    'nobody 61',
    'cotton 83',
    'invalid_data',
    'roland $invalid_points',
    'alfred -3',
]

print(calc_qualified_count(data))
