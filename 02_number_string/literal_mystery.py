# -*- coding: utf-8 -*-


def add_daily_points(user):
    """当用户每天第一次登录后，为其增加积分"""
    if user.type == 13:
        return
    if user.type == 3:
        user.points += 120
        return
    user.points += 100
    return


DAILY_POINTS_REWARDS = 100
VIP_EXTRA_POINTS = 20

from enum import Enum


class UserType(int, Enum):
    # VIP 用户
    VIP = 3
    # 小黑屋用户
    BANNED = 13


def add_daily_points(user):
    """当用户每天第一次登录后，为其增加积分"""
    if user.type == UserType.BANNED:
        return
    if user.type == UserType.VIP:
        user.points += DAILY_POINTS_REWARDS + VIP_EXTRA_POINTS
        return
    user.points += DAILY_POINTS_REWARDS
    return


UserType.XX
