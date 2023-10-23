# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname) #"mbox_short.txt")#
countLines = 0
sumSpamConfidence = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    sumSpamConfidence = float(sumSpamConfidence) + float(line[len(line)-7:])
    countLines = countLines + 1

print("Done", sumSpamConfidence/countLines)
