# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 11

def remove(substr,theStr):
    # your code here
    pos1 = 0
    pos2 = len(substr)
    found = False
    newStr = theStr
    
    while pos1 < len(newStr) and not found:
        currentPos = newStr[pos1:pos2]
        
        if substr == currentPos:
            newStr = newStr[:pos1] + newStr[pos2:]
            found = True
        else:
            pos1 += 1
            pos2 += 1
    
    return newStr

print(remove("e", "tree"))
print(remove("iss", "Mississippi"))
print(remove("an", "banana"))
print(remove("e", "treeeleee"))