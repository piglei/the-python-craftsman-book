"""通过 iTunes API 搜索歌手发布过的第一张专辑"""
import sys
from json.decoder import JSONDecodeError

import requests
from requests.exceptions import HTTPError

ITUNES_API_ENDPOINT = 'https://itunes.apple.com/search'


def command_first_album():
    """通过脚本输入查找并打印歌手第一张专辑信息"""
    if not len(sys.argv) == 2:
        print(f'usage: python {sys.argv[0]} {{SEARCH_TERM}}')
        sys.exit(1)

    term = sys.argv[1]
    resp = requests.get(
        ITUNES_API_ENDPOINT,
        {
            'term': term,
            'media': 'music',
            'entity': 'album',
            'attribute': 'artistTerm',
            'limit': 200,
        },
    )
    try:
        resp.raise_for_status()
    except HTTPError as e:
        print(f'Error: failed to call iTunes API, {e}')
        sys.exit(2)
    try:
        albums = resp.json()['results']
    except JSONDecodeError:
        print(f'Error: response is not valid JSON format')
        sys.exit(2)
    if not albums:
        print(f'Error: no albums found for artist "{term}"')
        sys.exit(1)

    sorted_albums = sorted(albums, key=lambda item: item['releaseDate'])
    first_album = sorted_albums[0]
    # 去除发布日期里的小时与分钟信息
    release_date = first_album['releaseDate'].split('T')[0]

    # 打印结果
    print(f"{term}'s first album: ")
    print(f"  * Name: {first_album['collectionName']}")
    print(f"  * Genre: {first_album['primaryGenreName']}")
    print(f"  * Released at: {release_date}")


if __name__ == '__main__':
    command_first_album()
