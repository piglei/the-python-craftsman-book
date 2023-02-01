# -*- coding: utf-8 -*-
import requests
import re


def save_website_title(url, filename):
    """获取某个地址的网页标题，然后将其写入到文件中

    :return: 如果成功保存，返回 True，否则打印错误，返回 False
    """
    try:
        resp = requests.get(url)
        obj = re.search(r'<title>(.*)</title>', resp.text)
        if not obj:
            print('save failed: title tag not found in page content')
            return False

        title = obj.grop(1)
        with open(filename, 'w') as fp:
            fp.write(title)
            return True
    except Exception:
        print(f'save failed: unable to save title of {url} to {filename}')
        return False


from requests.exceptions import RequestException


def save_website_title(url, filename):
    """获取某个地址的网页标题，然后将其写入到文件中"""
    try:
        resp = requests.get(url)
    except RequestException as e:
        print(f'save failed: unable to get page content: {e}')
        return False

    # 这段正则操作本身就是不应该抛出异常的，所以我们没必要使用 try 语句块
    # 假如 group 被误打成了 grop 也没关系，程序马上就会通过 AttributeError 来
    # 告诉我们。
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not found in page content')
        return False
    title = obj.group(1)

    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')
    save_website_title('https://localha23r232l3kj4l2j34.com', 'qq_title.txt')
    save_website_title('https://www.qq.com', '/qq_title.txt')


if __name__ == '__main__':
    main()
