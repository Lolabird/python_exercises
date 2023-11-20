# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 12

def remove_all(substr,theStr):
    # your code here
    pos1 = 0
    pos2 = len(substr)
    newStr = theStr
    
    while pos1 < len(newStr):
        currentPos = newStr[pos1:pos2]
        
        if substr == currentPos:
            newStr = newStr[:pos1] + newStr[pos2:]
        else:
            pos1 += 1
            pos2 += 1
       
    return newStr


print(remove_all("e", "treeeleee"))