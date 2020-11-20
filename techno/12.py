#nested for
result = None

a = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    11, 12, 13, 14, 15,
    6, 7, 8, 9, 10,
    1, 2, 3, 4, 5,
    16, 17, 18, 19, 20,
]

for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            result = i
print(result)
