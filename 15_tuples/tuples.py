name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

histogram = dict()
for line in handle :
    if not "From " in line : continue

    words = line.split()
    time = words[5]

    timeDetails = time.split(':')
    hour = timeDetails[0]

    histogram[hour] = histogram.get(hour, 0) + 1

sortedList = sorted( histogram.items() )
for item in sortedList :
    print(item[0], item[1] )
