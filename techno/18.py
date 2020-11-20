#underscore means nothing
x = 'ab'
a = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9,
]
for _ in a:
    x += x
#print(x)
print(len(x))
