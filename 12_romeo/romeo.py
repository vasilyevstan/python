fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lineWords = line.split()
    print(line.rstrip())

    for word in lineWords :
        if word not in lst :
            lst.append(word)

lst.sort()
print(lst)
