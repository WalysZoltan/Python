#рекурсия
def foo(depth, value):
    if depth:
        foo(depth - 1, value * 2)
    else:
        print(value)
foo(10, 1)
