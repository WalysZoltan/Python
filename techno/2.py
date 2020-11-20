#как проходит сравнение
x = 12
result = 0

if x % 3 or x % 4 and x % 5:
    result += 1

if x % 3 and x % 4 or x % 5:
    result += 1

if x % 3 and x % 4 and x % 5:
    result += 1

if x % 3 or x % 4 or x % 5:
    result += 1

print(result)
