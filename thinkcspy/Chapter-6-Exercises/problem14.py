# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 14

def mySqrt(n):
    # your code here
    oldGuess = n/2
    
    while oldGuess**2 != n:
        oldGuess = (1/2)*(oldGuess+(n/oldGuess))
    
    return oldGuess
    
print(mySqrt(10000))