#construct array
result = []
base = [
    100, 80, 70, 60, 50,
    49, 48, 47, 46, 45, 44, 43, 42, 41, 40,
    39, 38, 37, 36, 35, 34, 33, 32, 31, 30,
    29, 28, 27, 26, 25, 24, 23, 22, 21, 20,
    19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
    100,
]
for x in base:
    if x > sum(result) / 2:
        result.append(x)
print(sum(result))
