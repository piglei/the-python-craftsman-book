numbers = [1, 2, 4, 5, 7]

count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1

print(count)

count = sum(i % 2 == 0 for i in numbers)
print(count)
