#summing 2 arrays element to element
def foo(a1, a2):
    result = []
    for i in range(len(a1)):
        result.append(a1[i] + a2[i])

    return(result)

x = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    6, 7, 8, 9, 10,
    1, 2, 3, 4, 5,
]
y = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    11, 12, 13, 14, 15,
    6, 7, 8, 9, 10,
    1, 2, 3, 4, 5,
]
print(foo(x, y)[15])
