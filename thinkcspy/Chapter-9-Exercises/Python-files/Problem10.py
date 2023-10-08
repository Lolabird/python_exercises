# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 10

def count(substr,theStr):
    # your code here
    count = 0
    charCount = 0
    pos1 = 0
    pos2 = len(substr)
    charPos = len(substr)
    
    while charCount < len(theStr):
        if charPos == 1 and substr == theStr[pos1] and (pos2 == len(theStr) or substr != theStr[pos2]):
            count += 1
            charCount += 1
        elif  substr == theStr[pos1:pos2]:
            count += 1
            charCount += charPos + 1
        else:
            charCount += 1
            

        pos1 += 1
        pos2 += 1
                
    return count

print(count("e", "treeleee"))