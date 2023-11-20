# Runestone.Academy thinkcspy course
# Chapter 12
# Problem 5

def translator(english):

    pirate = {}
    pirate['sir'] = 'matey'
    pirate['hotel'] = 'fleabag inn'
    pirate['student'] = 'swabbie'
    pirate['boy'] = 'matey'
    pirate['restaurant'] = 'galley'
    pirate['hello'] = 'avast'
    pirate['madam'] = 'proud beauty'
    pirate['professor'] = 'foul blaggart'
    pirate['your'] = 'yer'
    pirate['excuse'] = 'arr'
    pirate['are'] = 'be'
    pirate['lawyer'] = 'foul blaggart'
    pirate['the'] = 'th\''
    pirate['restroom'] = 'head'
    pirate['my'] = 'me'
    pirate['is'] = 'be'
    pirate['man'] = 'matey'
    
    englishList = english.split() + [' ']
    
    for i in range(len(englishList) - 1):
        word = englishList[i]
        word = word.lower()
        newWord = ""
        lengthy = len(newWord) - 1
        lengthier = len(word) - 1
        lengthiest = len(word) - 2

        for char in word:
            if char.isalpha():
                newWord += char
                
        if newWord[lengthy] == 's':
            newWord = newWord[0:lengthy]

        if newWord in pirate:
            if newWord != word:
                if word[lengthier] == 's' or word[lengthiest] == 's':
                    englishList[i] = pirate[newWord] + 's'

                    if not word[lengthier].isalpha():
                        englishList[i] = pirate[newWord] + 's' + word[lengthier]

                elif not word[lengthier].isalpha():
                    englishList[i] = pirate[newWord] + word[lengthier]
            else:        
                englishList[i] = pirate[newWord]
                

    translation = " ".join(englishList)
        
    return translation


print(translator(input("What would you like to say?")))

