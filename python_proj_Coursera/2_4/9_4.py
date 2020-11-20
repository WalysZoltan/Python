fh = input("Enter a file ")
fd = open(fh, "r")
list = list()
counts = dict()
for line in fd:
    line = line.strip()
    list = line.split()
    if list == []: continue
    if list[0] == "From":
        counts[list[1]] = counts.get(list[1], 0) + 1
max_count = None
max_word = None
for word, count in counts.items():
    if max_word is None or count > max_count:
        max_word = word
        max_count = count
print(max_word, max_count)
