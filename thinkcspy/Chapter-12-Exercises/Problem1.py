# Runestone.Academy thinkcspy course
# Chapter 12
# Problem 1

def countAll(text):
    wordDict = {}
    text = text.lower()

    for char in text:
        if char not in wordDict and char.isalpha():
            wordDict[char] = text.count(char)
    
    return wordDict


def sortList(text):
    wordDict = countAll(text)
    alphaList = list(wordDict.items())
    alphaList.sort()
    
    return alphaList


def printResult(text):    
    alphaList = sortList(text)
        
    print("You inputed: " + text)

    for char in alphaList:
        print(char[0] + ": " + str(char[1]))


printResult(input("What word(s) would you like sorted?"))