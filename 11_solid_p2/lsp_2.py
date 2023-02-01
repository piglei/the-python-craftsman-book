# -*- coding: utf-8 -*-
from typing import Iterable, List
import logging


logger = logging.getLogger(__name__)


class DeactivationNotSupported(Exception):
    """当用户不支持停用时抛出"""


class User(Model):
    """普通用户模型类"""

    def __init__(self, username: str):
        self.username = username

    def allow_deactivate(self) -> bool:
        """否允许被停用"""
        return True

    def deactivate(self):
        """停用当前用户

        :raises: 当用户不支持被停用时，抛出 DeactivationNotSupported 异常
        """
        self.is_active = True
        self.save()


class Admin(User):
    """管理员用户类"""

    def deactivate(self):
        """停用当前用户

        :raises: 当用户不支持被停用时，抛出 DeactivationNotSupported 异常
        """
        raise DeactivationNotSupported('admin can not be deactivated')

    def allow_deactivate(self) -> bool:
        # 管理员用户不允许被停用
        return False


def deactivate_users(users: Iterable[User]):
    """批量停用多个用户"""
    for user in users:
        if not user.allow_deactivate():
            logger.info(
                f'user {user.username} does not allow deactivating, skip.'
            )
            continue

        user.deactivate()


def deactivate_users(users: Iterable[User]):
    """批量停用多个用户"""
    for user in users:
        try:
            user.deactivate()
        except DeactivationNotSupported:
            logger.info(
                f'user {user.username} does not allow deactivating, skip.'
            )
