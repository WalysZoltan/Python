# find distribution of messages by hours from the file mbox-short.txt

fh = input("Enter a file ")
fd = open(fh, "r")
dict = dict()
for line in fd:
    line = line.strip()
    line = line.split()
    if line == []: continue
    if line[0] == "From":
        #line = line[5]
        #line = line.split(":")
        #line = line[0]
        #print(line)
        #dict[line] = dict.get(line, 0) + 1
#print(dict)
        dict[line[5].split(":")[0]] = dict.get(line[5].split(":")[0], 0) + 1
for (k, v) in sorted(dict.items()):
    print(k, v)
