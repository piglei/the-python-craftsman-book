# -*- coding: utf-8 -*-


def safe_close(fp):
    # 操作类函数，默认返回 None
    try:
        fp.close()
    except IOError:
        logger.warning('error closing file, ignore.')