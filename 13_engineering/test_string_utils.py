import pytest
from string_utils import string_upper


# def test_string_upper():
#     assert string_upper('foo') == 'FOO'
#
# def test_string_empty(): <.>
#     assert string_upper('') == ''
#
# def test_string_mixed_cases():
#     assert string_upper('foo BAR') == 'FOO BAR'
#
import pytest
import string
import random


@pytest.fixture(scope='session')
def random_token() -> str:
    """生成随机 token"""
    token_l = []
    char_pool = string.ascii_lowercase + string.digits
    for _ in range(32):
        token_l.append(random.choice(char_pool))
    return ''.join(token_l)


@pytest.fixture
def db_connection():
    """创建并返回一个数据库连接"""
    conn = create_db_conn()
    yield conn
    conn.close()


# @pytest.fixture(autouse=True)
# def prepare_data():
#     # 在测试开始前，创建两个用户
#     User.objects.create(...)
#     User.objects.create(...)
#     yield
#     # 在测试结束时，创建两个用户
#     User.objects.all().delete()


@pytest.mark.parametrize(
    's,expected',
    [
        ('foo', 'FOO'),
        ('', ''),
        ('foo BAR', 'FOO BAR'),
    ],
)
def test_string_upper(s, expected, random_token):
    print(random_token)
    assert string_upper(s) == expected


def test_foo(random_token):
    print(random_token)
