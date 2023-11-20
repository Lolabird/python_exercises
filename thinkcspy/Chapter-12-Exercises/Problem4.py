# Runestone.Academy thinkcspy course
# Chapter 12
# Problem 4

aliceBook = open("alice_in_wonderland.txt", "r")
aliceDict = {}

for line in aliceBook:
    words = line.split()

    for word in words:
        word = word.lower()
        newWord = ""

        for char in word:
            if char.isalpha():
                newWord += char

        if newWord != "":
            word = newWord            

        if word not in aliceDict:
            aliceDict[word] = 1
        else:
            aliceDict[word] += 1

aliceList = list(aliceDict.items())

maxnum = 0
maxWord = ""

for item in aliceList:
    if len(item[0]) > maxnum:
        maxnum = len(item[0])
        maxWord = item[0]

print(maxWord, "-", maxnum)

aliceBook.close()
