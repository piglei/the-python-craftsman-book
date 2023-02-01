# -*- coding: utf-8 -*-
import dis


def do_something(delta_seconds):
    # 如果时间已经过去11 天(或者更久)，不做任何事
    if delta_seconds < 11 * 24 * 3600:
        return
    ...


dis.dis(do_something)
