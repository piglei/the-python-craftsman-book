# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    DateTime,
    Boolean,
)
from sqlalchemy.sql import select


metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(32)),
    Column('gender', Integer, default=0),
    Column('level', Integer, default=1),
    Column('has_membership', Boolean, default=False),
    Column('updated', DateTime, default=datetime.datetime.now),
    Column('created', DateTime, default=datetime.datetime.now),
)


GENDER_FEMALE = 0
GENDER_MALE = 1


def fetch_users(
    conn,
    min_level=None,
    gender=None,
    has_membership=False,
    sort_field="created",
):
    """获取用户列表

    :param min_level: 要求的最低用户级别，默认为所有级别
    :type min_level: int, optional
    :param gender: 筛选用户性别，默认为所有性别
    :type gender: int, optional
    :param has_membership: 筛选会员或非会员用户，默认为 False，代表非会员
    :type has_membership: bool, optional
    :param sort_field: 排序字段，默认为 "created"，代表按用户创建日期排序
    :type sort_field: str, optional
    :return: 一个包含用户信息的列表：[(User ID, User Name), ...]
    """
    # 一种古老的 SQL 拼接技巧，使用 "WHERE 1=1" 来简化字符串拼接操作
    statement = "SELECT id, name FROM users WHERE 1=1"
    params = []
    if min_level is not None:
        statement += " AND level >= ?"
        params.append(min_level)
    if gender is not None:
        statement += " AND gender >= ?"
        params.append(gender)
    if has_membership:
        statement += " AND has_membership = true"
    else:
        statement += " AND has_membership = false"

    statement += " ORDER BY ?"
    params.append(sort_field)
    # 将查询参数 params 作为位置参数传递，避免 SQL 注入问题
    return list(conn.execute(statement, params))


def fetch_users_v2(
    conn,
    min_level=None,
    gender=None,
    has_membership=False,
    sort_field="created",
):
    """获取用户列表"""
    query = select([users.c.id, users.c.name])
    if min_level != None:
        query = query.where(users.c.level >= min_level)
    if gender != None:
        query = query.where(users.c.gender == gender)
    query = query.where(users.c.has_membership == has_membership).order_by(users.c[sort_field])
    return list(conn.execute(query))


def main():
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata.create_all(engine)

    conn = engine.connect()
    conn.execute(
        users.insert(),
        [
            {
                "name": "piglei",
                "gender": 1,
                "level": 2,
                "has_membership": False,
            },
            {
                "name": "cotton",
                "gender": 0,
                "level": 4,
                "has_membership": True,
            },
            {"name": "zyx", "gender": 0, "level": 1, "has_membership": True},
        ],
    )

    for func in (fetch_users, fetch_users_v2):
        print(func(conn))
        print(func(conn, min_level=2, has_membership=True))
        print(func(conn, min_level=2, gender=1))


if __name__ == '__main__':
    main()
