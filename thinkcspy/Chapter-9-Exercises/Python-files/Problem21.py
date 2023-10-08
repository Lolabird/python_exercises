# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 21

import string

def rot13(mess):
    # Your code here
    alpha = string.ascii_lowercase
    newStr = ""
    pos = 0
    mess = mess.lower()
    
    for char in mess:
        if char in alpha:
            pos = alpha.index(char)
            
            if pos <= 12:
                pos += 13
            else:
                pos = pos % 13
           
            newStr += alpha[pos]
            
        else:
            newStr += char    # no rules apply so keep the character
        
    return newStr

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('Since rot13 is symmetric you should see this message')))