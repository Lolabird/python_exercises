# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 13

def sumTo(n):
    # your code here
    runningTotal = 0
    
    for counter in range(n):
        runningTotal = runningTotal + (n+1)/2
        
    return runningTotal

print(sumTo(10))