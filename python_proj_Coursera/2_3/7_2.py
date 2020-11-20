fname = input("Enter file name: ")
fd = open(fname, "r")
s = float(0)
count = 0
for line in fd:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    f = float(line[19:].strip())
    s = s + f
    count = count + 1
print(s / count)
