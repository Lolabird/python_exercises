# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 

def numDigits(n):
    # your code here
    toText = str(n)
    count = 0
    
    for i in range (len(toText)):
        count += 1
        
    return count
    
print(numDigits(13))