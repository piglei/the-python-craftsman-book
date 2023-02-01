# -*- coding: utf-8 -*-
from functools import lru_cache


@lru_cache(maxsize=None)
def calculate_score(class_id):
    print(f'Calculating score for class: {class_id}...')
    return 42


calculate_score(100)
calculate_score(100)
