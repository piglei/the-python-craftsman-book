with open('hello.txt', 'r') as fp:
    print(fp.read())

# with open('hello.txt', 'r', encoding='gbk') as fp:
#     print(fp.read())

with open('hello.txt', 'rb') as fp:
    print(fp.read())


with open('output.txt', 'w', encoding='gbk') as fp:
    fp.write('你好，中国')
    # fp.write('你好，中国'.encode('utf-8'))


def upper_s(s):
    """把输入字符串里的所有 "s" 都转为大写"""
    return s.replace('s', 'S')


bin_obj = b'super sunflowers.'
str_obj = bin_obj.decode('utf-8')
print(upper_s(str_obj))


with open('output.txt', 'wb') as fp:
    str_obj = upper_s('super sunflowers.')
    bin_obj = str_obj.encode('utf-8')
    fp.write(bin_obj)
