# -*- coding: utf-8 -*-
import random

PATHS = (
    "/",
    "/",
    "/",
    "/",
    "/about/",
    "/about/",
    "/articles/15-thinking-in-edge-cases/",
    "/articles/15-thinking-in-edge-cases/",
    "/articles/what-celeste-teaches-me-about-programming/",
    "/articles/three-tips-on-writing-file-related-codes/",
    "/articles/write-solid-python-codes-part-1/",
    "/admin/",
)

for i in range(10000):
    path = random.choice(PATHS)
    time_cost = random.randint(10, 2000)
    print(f"{path} {time_cost}")
