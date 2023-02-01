# -*- coding: utf-8 -*-

users_visited_puket = [
    {
        "first_name": "Sirena",
        "last_name": "Gross",
        "phone_number": "650-568-0388",
        "date_visited": "2018-03-14",
    },
    {
        "first_name": "James",
        "last_name": "Ashcraft",
        "phone_number": "412-334-4380",
        "date_visited": "2014-09-16",
    },
    {
        "first_name": "Melissa",
        "last_name": "Dubois",
        "phone_number": "630-225-8829",
        "date_visited": "2019-01-04",
    },
    {
        "first_name": "Albert",
        "last_name": "Potter",
        "phone_number": "702-249-3714",
        "date_visited": "2014-03-18",
    },
    {
        "first_name": "Marcel",
        "last_name": "May",
        "phone_number": "315-794-3895",
        "date_visited": "2012-12-12",
    },
]

users_visited_nz = [
    {
        "first_name": "Justin",
        "last_name": "Malcom",
        "phone_number": "267-282-1964",
        "date_visited": "2011-03-13",
    },
    {
        "first_name": "Albert",
        "last_name": "Potter",
        "phone_number": "702-249-3714",
        "date_visited": "2013-09-11",
    },
    {
        "first_name": "James",
        "last_name": "Ashcraft",
        "phone_number": "412-334-4380",
        "date_visited": "2009-04-18",
    },
    {
        "first_name": "Marcel",
        "last_name": "May",
        "phone_number": "938-121-9321",
        "date_visited": "2016-07-12",
    },
    {
        "first_name": "Barbara",
        "last_name": "Davis",
        "phone_number": "716-801-3922",
        "date_visited": "2018-03-12",
    },
]


def find_potential_customers_v1():
    """找到去过普吉岛但是没去过新西兰的人

    :return: 通过 Generator 返回符合条件的旅客记录
    """
    for puket_record in users_visited_puket:
        is_potential = True
        for nz_record in users_visited_nz:
            if (
                puket_record['first_name'] == nz_record['first_name']
                and puket_record['last_name'] == nz_record['last_name']
                and puket_record['phone_number'] == nz_record['phone_number']
            ):
                is_potential = False
                break

        if is_potential:
            yield puket_record


for record in find_potential_customers_v1():
    print(record['first_name'], record['last_name'], record['phone_number'])


def find_potential_customers_v2():
    """找到去过普吉岛但是没去过新西兰的人，性能改进版"""
    # 首先，遍历所有新西兰访问记录，创建查找索引
    nz_records_idx = {
        (rec['first_name'], rec['last_name'], rec['phone_number'])
        for rec in users_visited_nz
    }

    for rec in users_visited_puket:
        key = (rec['first_name'], rec['last_name'], rec['phone_number'])
        if key not in nz_records_idx:
            yield rec


for record in find_potential_customers_v2():
    print(record['first_name'], record['last_name'], record['phone_number'])


class VisitRecord:
    """旅游记录

    :param first_name: 名
    :param last_name: 姓
    :param phone_number: 联系电话
    :param date_visited: 旅游时间

    - 当两条访问记录的名字与电话号相等时，判定二者相等。
    """

    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited

    def __hash__(self):
        return hash(self.comparable_fields)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.comparable_fields == other.comparable_fields
        return False

    @property
    def comparable_fields(self):
        """获取用于对比对象的字段值"""
        return (self.first_name, self.last_name, self.phone_number)


def find_potential_customers_v3():
    # 转换为 VisitRecord 对象后，计算集合差值
    return set(VisitRecord(**r) for r in users_visited_puket) - set(
        VisitRecord(**r) for r in users_visited_nz
    )


for record in find_potential_customers_v3():
    print(record.first_name, record.last_name, record.phone_number)


from dataclasses import dataclass, field


@dataclass(frozen=True)
class VisitRecordDC:
    first_name: str
    last_name: str
    phone_number: str
    date_visited: str = field(compare=False)


def find_potential_customers_v4():
    return set(VisitRecordDC(**r) for r in users_visited_puket) - set(
        VisitRecordDC(**r) for r in users_visited_nz
    )


print('---')
for record in find_potential_customers_v4():
    print(record.first_name, record.last_name, record.phone_number)
