# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 3

import string

def count(p):
    # your code here
    abc = 0
    e = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    for achar in p:
        for alphaChar in alphabet:
            if achar == alphaChar:
                abc += 1
        if achar == "e" or achar == "E":
            e += 1
            
    if abc != 0:        
        ePerAbc = e / abc * 100
    else:
        ePerAbc = 0
    
    finalMsg = "Your text contains {} alphabetic characters, of which {} ({:.1f}%) are 'e'.".format(abc, e, ePerAbc)
            
    return finalMsg
    
text = "Bell of the ball"
print(count(text))