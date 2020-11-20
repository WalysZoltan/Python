#summing all values with same keys from 2 dicts
def foo(d1, d2):
    result = {}
    for key in d1:
        if key in d2:
            result[key] = d1[key] + d2[key]
    return result

x = dict(
    a=1, b=2, c=3, d=4,
    e=5, f=6, g=7, h=8,
    i=9, j=10, k=11, l=12,
    m=13, n=14, o=15
)
y = dict(
    z=1, y=2, x=3, w=4,
    v=5, u=6, t=7, s=8,
    r=9, q=10, p=11, o=12,
)
print(sum(foo(x, y).values()))
