# AF: Ask for Forgiveness
# 要做就做，如果抛出异常了，再处理异常
def counter_af(l):
    result = {}
    for key in l:
        try:
            result[key] += 1
        except KeyError:
            result[key] = 1
    return result


# AP: Ask for Permission
# 做之前，先问问能不能做，可以做再做
def counter_ap(l):
    result = {}
    for key in l:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result
