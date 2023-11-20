# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 14

def replace(s, old, new):
    # your code here
    newStr = s.split(old)
    newStr = new.join(newStr)
    
    return newStr


s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace('Mississippi', 'i', 'I'))
print(replace(s, 'om', 'am'))
print(replace(s, 'o', 'a'))