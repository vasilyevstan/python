name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

histogram = dict()

for line in handle :
    if not "From " in line : continue

    words = line.split()
    email = words[1]
    histogram[email] = histogram.get(email, 0) + 1

resultEmail = ''
resultCount = 0
for email, count in histogram.items() :
    if count > resultCount :
        resultEmail = email
        resultCount = count

print(resultEmail, resultCount)
