f = input("Enter a file ")
fd = open(f, "r")
list = list()
for line in fd:
    for buf in line.rstrip().split():
        if buf in list: continue
        list.append(buf)
list.sort()
print(list)
