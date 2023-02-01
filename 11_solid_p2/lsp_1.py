# -*- coding: utf-8 -*-
from typing import Iterable, List
import logging


class GitRepository:
    """Git 仓库对象"""

    def __init__(self, repo_url: str):
        self.repo_url = repo_url

    def clone(self, local_dir: str):
        """将 Git 仓库内容 Clone 到本地目录

        :param local_dir: 本地目录
        """
        ...

    def push(self):
        """将本地改动推送到远程地址"""
        ...


class ReadOnlyGitRepository(GitRepository):
    """只读 Git 仓库对象"""

    def push(self):
        ...


logger = logging.getLogger(__name__)


class User(Model):
    """用户类，包含普通用户的相关操作"""

    ...

    def deactivate(self):
        """停用当前用户"""
        self.is_active = False
        self.save()


class Admin(User):
    """管理员用户类"""

    ...

    def deactivate(self):
        # 管理员用户不允许被停用
        raise RuntimeError('admin can not be deactivated!')


def deactivate_users(users: Iterable[User]):
    """批量停用多个用户

    :param users: 可迭代的用户对象 User
    """
    for user in users:
        user.deactivate()


def deactivate_users(users: Iterable[User]):
    """批量停用多个用户"""
    for user in users:
        # 管理员用户不支持 deactivate 方法，跳过
        if isinstance(user, Admin):
            logger.info(f'skip deactivating admin user {user.username}')
            continue

        user.deactivate()
