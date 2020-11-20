#string order
s = ''
base_sing = 'helloworld'

for char in base_sing:
    if char < 'h':
        s += char
    if char < 'e':
        s += char
    if char < 'd':
        s += char

print(s)
