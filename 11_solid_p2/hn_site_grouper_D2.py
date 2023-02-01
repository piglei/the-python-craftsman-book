import requests
import datetime
from lxml import etree
from typing import Dict
from collections import Counter
from abc import abstractmethod, ABC


class ContentOnlyHNWebPage(ABC):
    """抽象类：Hacker New 站点页面（仅提供内容）"""

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()


class HNWebPage(ABC):
    """抽象类：Hacker New 站点页面（含元数据）"""

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_size(self) -> int:
        """获取页面大小"""
        raise NotImplementedError()

    @abstractmethod
    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""
        raise NotImplementedError()


class RemoteHNWebPage(HNWebPage):
    """远程页面，通过请求 HN 站点返回内容"""

    def __init__(self, url: str):
        self.url = url
        # 保存当前请求结果
        self._resp = None
        self._generated_at = None

    def get_text(self) -> str:
        """获取页面内容"""
        self._request_on_demand()
        return self._resp.text

    def get_size(self) -> int:
        """获取页面大小"""
        return len(self.get_text())

    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""
        self._request_on_demand()
        return self._generated_at

    def _request_on_demand(self):
        """请求远程地址，并避免重复"""
        if self._resp is None:
            self._resp = requests.get(self.url)
            self._generated_at = datetime.datetime.now()


class LocalHNWebPage(HNWebPage):
    """本地页面，根据本地文件返回页面内容"""

    def __init__(self, path: str):
        self.path = path

    def get_text(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()

    def get_size(self) -> int:
        return 0

    def get_generated_at(self) -> datetime.datetime:
        raise NotImplementedError("local web page can not provide generate_at info")


class SiteSourceGrouper:
    """对 HN 页面的新闻来源站点进行分组统计"""

    def __init__(self, page: HNWebPage):
        self.page = page

    def get_groups(self) -> Dict[str, int]:
        """获取 (域名, 个数) 分组"""
        html = etree.HTML(self.page.get_text())
        # 通过 xpath 语法筛选新闻域名标签
        elems = html.xpath('//table[@class="itemlist"]//span[@class="sitestr"]')

        groups = Counter()
        for elem in elems:
            groups.update([elem.text])
        return groups


class SiteAchiever:
    """将不同时间点的 HN 页面归档"""

    def save_page(self, page: HNWebPage):
        """将页面保存到后端数据库"""
        data = {
            "content": page.get_text(),
            "generated_at": page.get_generated_at(),
            "size": page.get_size(),
        }
        # 将 data 保存到数据库中
        # ...


def main():
    # 实例化 page，传入 SiteSourceGrouper
    page = RemoteHNWebPage(url="https://news.ycombinator.com/")
    grouper = SiteSourceGrouper(page).get_groups()
    for key, value in grouper.most_common(3):
        print(f'Site: {key} | Count: {value}')

    page = LocalHNWebPage(path="./static_hn.html")
    grouper = SiteSourceGrouper(page).get_groups()
    for key, value in grouper.most_common(3):
        print(f'Site: {key} | Count: {value}')


if __name__ == '__main__':
    main()
