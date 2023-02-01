# -*- coding: utf-8 -*-
import bisect
import random

movies = [
    {'name': 'The Dark Knight', 'year': 2008, 'rating': '9'},
    {'name': 'Kaili Blues', 'year': 2015, 'rating': '7.3'},
    {'name': 'Citizen Kane', 'year': 1941, 'rating': '8.3'},
    {'name': 'Project Gutenberg', 'year': 2018, 'rating': '6.9'},
    {'name': 'Burning', 'year': 2018, 'rating': '7.5'},
    {'name': 'The Shawshank Redemption ', 'year': 1994, 'rating': '9.3'},
]


class Movie:
    """电影对象数据类"""

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @property
    def rank(self):
        """
        按照评分对电影分级
        """
        # 已经排好序的评级分界点
        breakpoints = (6, 7, 8, 8.5)
        # 各评分区间级别名
        grades = ('D', 'C', 'B', 'A', 'S')

        index = bisect.bisect(breakpoints, float(self.rating))
        return grades[index]


def get_sorted_movies(movies, sorting_type):
    """对电影列表进行排序并返回

    :param movies: Movie 对象列表
    :param sorting_type: 排序选项，可选值
        name（名称）、rating（评分）、year（年份）、random（随机乱序）
    """
    sorting_algos = {
        # sorting_type: (key_func, reverse)
        'name': (lambda movie: movie.name.lower(), False),
        'rating': (lambda movie: float(movie.rating), True),
        'year': (lambda movie: movie.year, True),
        'random': (lambda movie: random.random(), False),
    }
    try:
        key_func, reverse = sorting_algos[sorting_type]
    except KeyError:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')

    sorted_movies = sorted(movies, key=key_func, reverse=reverse)
    return sorted_movies


all_sorting_types = ('name', 'rating', 'year', 'random')


def main():
    # 接收用户输入的排序选项
    sorting_type = input('Please input sorting type: ')
    if sorting_type not in all_sorting_types:
        print(
            'Sorry, "{}" is not a valid sorting type, please choose from '
            '"{}", exit now'.format(
                sorting_type,
                '/'.join(all_sorting_types),
            )
        )
        return

    # 初始化电影数据对象
    movie_items = []
    for movie_json in movies:
        movie = Movie(**movie_json)
        movie_items.append(movie)

    # 排序并输出电影列表
    sorted_movies = get_sorted_movies(movie_items, sorting_type)
    for movie in sorted_movies:
        print(f'- [{movie.rank}] {movie.name}({movie.year}) | rating: {movie.rating}')


if __name__ == '__main__':
    main()
