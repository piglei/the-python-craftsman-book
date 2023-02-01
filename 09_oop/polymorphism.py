# -*- coding: utf-8 -*-
from enum import Enum, auto


class OutputType(int, Enum):
    FILE = auto()
    REDIS = auto()
    ES = auto()


class FancyLogger:
    """日志类：支持往文件、Redis、ES 等服务输出日志"""

    _redis_max_length = 1024

    def __init__(self, output_type=OutputType.FILE):
        self.output_type = output_type
        ...

    def log(self, message):
        """打印日志"""
        if self.output_type == OutputType.FILE:
            ...
        elif self.output_type == OutputType.REDIS:
            ...
        elif self.output_type == OutputType.ES:
            ...
        else:
            raise TypeError('output type invalid')

    def pre_process(self, message):
        """预处理日志"""
        # REDIS 对日志最大长度有限制，需要进行裁剪
        if self.output_type == OutputType.REDIS:
            return message[: self._redis_max_length]


class FileWriter:
    def write(self, message):
        ...


class RedisWriter:
    max_length = 1024

    def _pre_process(self, message):
        # REDIS 对日志最大长度有限制，需要进行裁剪
        return message[: self.max_length]

    def write(self, message):
        message = self._pre_process(message)
        ...


class EsWriter:
    def write(self, message):
        ...


class FancyLogger:
    """日志类：支持往文件、Redis、ES 等服务输出日志"""

    def __init__(self, output_writer=None):
        self._writer = output_writer or FileWriter()
        ...

    def log(self, message):
        self._writer.write(message)
