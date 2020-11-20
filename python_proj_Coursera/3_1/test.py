import re
for line in ["This file contains the sample data", "", "", "Why should you learn to write programs?", "", "Writing programs (or programming) is a very creative and rewarding activity.", "", "You can write programs for 3036 many reasons, ranging from making your living to solving 7209"]
print(line)
line_parsed = re.findall('[0-9]+', line)
print(line_parsed)
