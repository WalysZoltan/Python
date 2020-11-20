#concept of None
a = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    11, 12, 13, 14, 15,
    6, 7, 8, 9, 10,
    1, 2, 3, 4, 5,
    5, 5, 5, 5, 5,
]

result = 0
prev_x = None
for x in a:
    if prev_x is None or prev_x > x:
        result += 1
        prev_x = x
print(result)
