#subtracting average from any member of the row
m = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [11, 12, 13, 14, 15],
    [6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5]
]

for row in m:
    s = sum(row)
    avg = s / len(row)
    for index, value in enumerate(row):
        row[index] = value - avg

print(int(m[0][2]))
#print(m)
