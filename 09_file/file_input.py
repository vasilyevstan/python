fh = open("words2.txt", "r")

countLines = 0
wordCount = 0
uniqueWords = dict()

for line in fh:
    #print(line.strip())
    countLines = countLines + 1
    words = line.split()
    for word in words :
        wordCount = wordCount + 1
        uniqueWords[word.lower()] = uniqueWords.get(word.lower(), 0) + 1

checkNumWords = 0;
for word in uniqueWords :
    checkNumWords = checkNumWords + uniqueWords[word]

print("Check", checkNumWords)

print(countLines, "Lines", wordCount, "Words", len(uniqueWords), "Unique words")
#for word in uniqueWords.keys() :
#    print(word, uniqueWords[word])
print(uniqueWords)
