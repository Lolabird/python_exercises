# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 19

import string

def decrypt(msg, code):
    alpha = string.ascii_lowercase
    newStr = ""
    pos = 0
    msg = msg.lower()
    
    for char in msg:
        if char in alpha:
            pos = newAlpha.index(char)
            newStr += alpha[pos]
        else:
            newStr += char    # no rules apply so keep the character

    return newStr

newAlpha = "qwertyuiopasdfghjklzxcvbnm"

print(decrypt("itssg vgksr!", newAlpha))