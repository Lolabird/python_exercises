# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 18

import string

def encrypt(msg, code):
    alpha = string.ascii_lowercase
    newStr = ""
    pos = 0
    msg = msg.lower()
    
    for char in msg:
        if char in alpha:
            pos = alpha.index(char)
            newStr += newAlpha[pos]
        else:
            newStr += char    # no rules apply so keep the character

    return newStr

newAlpha = "qwertyuiopasdfghjklzxcvbnm"

print(encrypt("Hello World!", newAlpha))