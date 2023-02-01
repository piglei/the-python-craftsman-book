# -*- coding: utf-8 -*-


def remove_odd_mul_100(numbers):
    """剔除奇数并乘 100"""
    results = []
    for number in numbers:
        if number % 2 == 1:
            continue
        results.append(number * 100)
    return results


numbers = [3, 4, 12, 17]

print(remove_odd_mul_100(numbers))


results = [n * 100 for n in numbers if n % 2 == 0]
print(results)

results = [
    n * 100 if str(n).startswith('3') else n * 1000
    for n in numbers
    if n % 2 == 0
]
print(results)


results = [
    task.result if task.result_version == VERSION_2 else get_legacy_result(task)
    for tasks_group in tasks
    for task in in tasks_group
    if task.is_active() and task.has_completed()
]

results = []
for tasks_group in tasks:
    for task in tasks_group:
        if not (task.is_active() and task.has_completed()):
            continue

        if task.result_version == VERSION_2:
            result = task.result
        else:
            result = get_legacy_result(task)
        results.append(result)
        


print([(i, j) for i in range(2) for j in range(10)])
