import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_441602.txt"
#"regex_sum_42.txt"
handle = open(name)

listAll = list()

for line in handle :
    lineList = re.findall('[0-9]+', line)
    listAll = listAll + lineList

count = 0
for val in listAll :
    count = count + int(val)

print(count)
