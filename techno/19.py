base = [
    1, 1, 1, 1, 1,
    2, 2, 2, 2, 2,
    3, 3, 3, 3, 3,
    5, 5, 5, 5, 5,
    6, 6, 6, 6, 6,
    7, 7, 7, 7, 7,
]

def foo(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return lst[n//2]
    else:
        return (lst[n//2 - 1] + lst[n//2]) / 2
print(int(foo(base)))
