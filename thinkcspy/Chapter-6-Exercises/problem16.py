# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 16

import math

def myPi(iters):
    # Calculate an approximation of PI using the Madhava
    # approximation with iters number of iterations

    #your code here
    apprPi = 0
    
    for i in range(iters):
        term = (-1)**i/((2*i+1)*3**i)
        apprPi += term
    
    return apprPi * math.sqrt(12)
        
print(myPi(10))