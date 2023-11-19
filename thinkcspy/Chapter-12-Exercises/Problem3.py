aliceBook = open("thinkcspy/Chapter-12-Exercises/alice_in_wonderland.txt", "r")
aliceDict = {}

for line in aliceBook:
    words = line.split()

    for word in words:
        word = word.lower()
        newWord = ""

        for char in word:
            if char.isalpha():
                newWord += char

        word = newWord            

        if word not in aliceDict:
            aliceDict[word] = 1
        else:
            aliceDict[word] += 1

print(aliceDict)

aliceBook.close()
