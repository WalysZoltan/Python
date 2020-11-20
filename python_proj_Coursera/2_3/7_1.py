fname = input("Enter file name: ")
try:
    fd = open(fname, "r")
except:
    print("Wrong file name")
for line in fd:
    line = line.rstrip().upper()
    print(line)
