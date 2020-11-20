#find the sum of all integers hidden in the file using regex
import re
fh = input("Enter a file: ")
fd = open(fh, "r")
sum = 0
for line in fd:
    list_parsed = re.findall('[0-9]+', line)
    if list_parsed != []:
        for num in list_parsed:
            i_num = int(num)
            sum = sum + i_num
print(sum)
