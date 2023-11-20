# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 12

def count(lst):
    # your code here
    wordCount = 0
    
    for item in lst:
        if type(item) is str:
            if item != "sam":
                wordCount += 1
            else:
                wordCount += 1
                return wordCount
            
    return wordCount

myList = ["apple", 5, 6, True, "purple", False, "mushroom", 11, "gen-x", "sam", 7, 10, "cause", "interim"]

print(count(myList))