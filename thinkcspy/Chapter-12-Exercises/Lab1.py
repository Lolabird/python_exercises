# Runestone.Academy thinkcspy course
# Chapter 12
# Lab 1
 
def countAll(text):
    wordDict = {}
    
    for char in text:
        if char not in wordDict and char.isalpha():
            wordDict[char] = text.count(char)
    
    return wordDict
            

print(countAll("banana"))
print(countAll("curly fries 123!"))