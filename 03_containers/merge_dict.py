# -*- coding: utf-8 -*-


def merge_dict(d1, d2):
    # 因为字典是可被修改的对象，为了避免修改原对象，此处需要复制一个 d1 的备份
    result = d1.copy()
    result.update(d2)
    return result


print(merge_dict({"name": "piglei"}, {"movies": ["Fight Club"]}))
user = {**{"name": "piglei"}, **{"movies": ["Fight Club"]}}
print(user)
