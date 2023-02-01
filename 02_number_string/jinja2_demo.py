def render_movies(username, movies):
    """
    文本方式展示电影列表信息
    """
    welcome_text = 'Welcome, {}.\n'.format(username)
    text_parts = [welcome_text]
    for name, rating in movies:
        # 没有提供评分的电影，以 [NOT RATED] 代替
        rating_text = rating if rating else '[NOT RATED]'
        movie_item = '* {}, Rating: {}'.format(name, rating_text)
        text_parts.append(movie_item)
    return '\n'.join(text_parts)


from jinja2 import Template

_MOVIES_TMPL = '''\
Welcome, {{username}}.
{%for name, rating in movies %}
* {{ name }}, Rating: {{ rating|default("[NOT RATED]", True) }}
{%- endfor %}
'''


def render_movies_j2(username, movies):
    tmpl = Template(_MOVIES_TMPL)
    return tmpl.render(username=username, movies=movies)


movies = [
    ('The Shawshank Redemption', '9.3'),
    ('The Prestige', '8.5'),
    ('Mulan', None),
]

print(render_movies('piglei', movies))
print(render_movies_j2('piglei', movies))
