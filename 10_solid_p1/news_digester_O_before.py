# -*- coding: utf-8 -*-
import io
import sys
from typing import List, Iterable

from urllib import parse
import requests
from lxml import etree


class Post:
    """HN(https://news.ycombinator.com/) 上的条目

    :param title: 标题
    :param link: 链接
    :param points: 当前得分
    :param comments_cnt: 评论数
    """

    def __init__(self, title: str, link: str, points: str, comments_cnt: str):
        self.title = title
        self.link = link
        self.points = int(points)
        try:
            self.comments_cnt = int(comments_cnt)
        except ValueError:
            self.comments_cnt = 0


class HNTopPostsSpider:
    """抓取 HackerNews Top 内容条目

    :param limit: 限制条目数，默认为 5
    """

    items_url = 'https://news.ycombinator.com/'

    def __init__(self, limit: int = 5):
        self.limit = limit

    def fetch(self) -> Iterable[Post]:
        """从 HN 抓取 Top 内容"""
        resp = requests.get(self.items_url)

        # 使用 XPath 可以方便的从页面解析出你需要的内容，以下均为页面解析代码
        # 如果你对 xpath 不熟悉，可以忽略这些代码，直接跳到 yield Post() 部分
        html = etree.HTML(resp.text)
        items = html.xpath('//table[@class="itemlist"]/tr[@class="athing"]')
        counter = 0
        for item in items:
            if counter >= self.limit:
                break

            node_title = item.xpath('./td[@class="title"]/a')[0]
            node_detail = item.getnext()
            points_text = node_detail.xpath('.//span[@class="score"]/text()')
            comments_text = node_detail.xpath('.//td/a[last()]/text()')[0]
            link = node_title.get('href')

            # 只关注来自 github.com 的内容
            parsed_link = parse.urlparse(link)
            if parsed_link.netloc == 'github.com':
                counter += 1
                yield Post(
                    title=node_title.text,
                    link=link,
                    # 条目可能会没有评分
                    points=points_text[0].split()[0] if points_text else '0',
                    comments_cnt=comments_text.split()[0],
                )


def write_posts_to_file(posts: List[Post], fp: TextIO, title: str):
    """负责将帖子列表写入文件"""
    fp.write(f'# {title}\n\n')
    for i, post in enumerate(posts, 1):
        fp.write(f'> TOP {i}: {post.title}\n')
        fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
        fp.write(f'> 地址：{post.link}\n')
        fp.write('------\n')


def main():
    crawler = HNTopPostsSpider()

    posts = list(crawler.fetch())
    file_title = 'Top news on HN'
    write_posts_to_file(posts, sys.stdout, file_title)


if __name__ == '__main__':
    main()
