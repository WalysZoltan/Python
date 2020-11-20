line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
list = list()
list = line.split()
count = 0
print(list)
print(list[0])
if list[0] == "From":
    count = count + 1
print(count)
