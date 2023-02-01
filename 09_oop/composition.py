# -*- coding: utf-8 -*-
import re


class UniqueVisitorAnalyzer:
    """统计某日的独立访客数

    :param date: 需要统计的日期
    """

    def __init__(self, date):
        self.date = date

    def analyze(self):
        """通过解析与分析 API 访问日志，返回独立访客数量

        :return: 独立访客数
        """
        for entry in self.get_log_entries():
            ...  # 省略：根据 entry.user_id 统计 UV 并返回结果

    def match_news_pattern(self, path):
        """判断 API 路径是不是在访问新闻

        :param path: API 访问路径
        :return: bool
        """
        return re.match(r'^/news/[^/]*?/$', path)

    def get_log_entries(self):
        """获取当天所有日志记录"""
        for line in self.read_log_lines():
            entry = self.parse_log(line)
            if not self.match_news_pattern(entry.path):
                continue
            yield entry

    def read_log_lines(self):
        """逐行获取访问日志"""
        ...  # 省略：根据日志 self.date 读取日志文件并返回结果

    def parse_log(self, line):
        """将纯文本格式的日志解析为结构化对象

        :param line: 纯文本格式日志
        :return: 结构化的日志条目 LogEntry 对象
        """
        ...  # 省略：复杂的日志解析过程
        return LogEntry(
            time=...,
            ip=...,
            path=...,
            user_agent=...,
            user_id=...,
        )


import re


class Top10CommentsAnalyzer(UniqueVisitorAnalyzer):
    """获取某日点赞量最高的 10 条评论

    :param date: 需要统计的日期
    """

    limit = 10

    def analyze(self):
        """通过解析与统计 API 访问日志，返回点赞量最高的评论

        :return: 评论 ID 列表
        """
        for entry in self.get_log_entries():
            comment_id = self.extract_comment_id(entry.path)
            ...  # 省略：统计过程与返回结果

    def extract_comment_id(self, path):
        """
        根据日志访问路径，获取评论 ID。
        有效的评论点赞 API 路径格式："/comments/<ID>/up_votes/"

        :return: 仅当路径是评论点赞 API 时，返回 ID，否则返回 None
        """
        matched_obj = re.match('/comments/(.*)/up_votes/', path)
        return matched_obj and matched_obj.group(1)
