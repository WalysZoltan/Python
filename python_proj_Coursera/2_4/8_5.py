fh = input("Enter a file ")
fd = open(fh, "r")
count = 0
list = list()
for line in fd:
    line = line.strip()
    list = line.split()
    if list == []: continue
    if list[0] == "From":
        print(list[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
