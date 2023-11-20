# Runestone.Academy thinkcspy course
# Chapter 12
# Problem 3 

aliceBook = open("alice_in_wonderland.txt", "r")
aliceDict = {}
outfile = open("alice_words.txt", "w")

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
aliceList.sort()

offset = 30 - len("word")
spaces = " " * offset
outfile.write("WORD" + spaces + "COUNT\n" )

for item in aliceList:
    offset = 30 - len(item[0])
    spaces = " " * offset
    outfile.write(item[0] + spaces + str(item[1]) + "\n" )

aliceBook.close()
