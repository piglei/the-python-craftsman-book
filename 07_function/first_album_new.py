"""通过 iTunes API 搜索歌手发布过的第一张专辑"""
import sys
from json.decoder import JSONDecodeError

import requests
from requests.exceptions import HTTPError

ITUNES_API_ENDPOINT = 'https://itunes.apple.com/search'


class GetFirstAlbumError(Exception):
    """获取第一张专辑失败"""


class QueryAlbumsError(Exception):
    """获取专辑列表失败"""


def command_first_album():
    """通过输入参数查找并打印歌手第一张专辑信息"""
    if not len(sys.argv) == 2:
        print(f'usage: python {sys.argv[0]} {{SEARCH_TERM}}')
        sys.exit(1)

    artist = sys.argv[1]
    try:
        album = get_first_album(artist)
    except GetFirstAlbumError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)

    print(f"{artist}'s first album: ")
    print(f"  * Name: {album['name']}")
    print(f"  * Genre: {album['genre_name']}")
    print(f"  * Released at: {album['release_date']}")


def get_first_album(artist):
    """根据专辑列表获取第一张专辑

    :param artist: 歌手名称
    :return: 第一张专辑
    :raises: 获取失败时抛出 GetFirstAlbumError
    """
    try:
        albums = query_all_albums(artist)
    except QueryAlbumsError as e:
        raise GetFirstAlbumError(str(e))

    sorted_albums = sorted(albums, key=lambda item: item['releaseDate'])
    first_album = sorted_albums[0]
    # 去除发布日期里的小时与分钟信息
    release_date = first_album['releaseDate'].split('T')[0]
    return {
        'name': first_album['collectionName'],
        'genre_name': first_album['primaryGenreName'],
        'release_date': release_date,
    }


def query_all_albums(artist):
    """根据歌手名称搜索所有专辑列表

    :param artist: 歌手名称
    :return: 专辑列表，List[Dict]
    :raises: 获取专辑失败时抛出 GetAlbumsError
    """
    resp = requests.get(
        ITUNES_API_ENDPOINT,
        {
            'term': artist,
            'media': 'music',
            'entity': 'album',
            'attribute': 'artistTerm',
            'limit': 200,
        },
    )
    try:
        resp.raise_for_status()
    except HTTPError as e:
        raise QueryAlbumsError(f'failed to call iTunes API, {e}')
    try:
        albums = resp.json()['results']
    except JSONDecodeError:
        raise QueryAlbumsError('response is not valid JSON format')
    if not albums:
        raise QueryAlbumsError(f'no albums found for artist "{artist}"')
    return albums


if __name__ == '__main__':
    command_first_album()
