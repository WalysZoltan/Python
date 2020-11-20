#byte operations
a = [
    2 & 1,
    2 & 2,
    2 & 3,
    2 | 1,
    2 | 2,
    2 | 3,
    2 ^ 1,
    2 ^ 2,
    2 ^ 3,
]
result = 0
for x in a:
    result += x
print(result)
