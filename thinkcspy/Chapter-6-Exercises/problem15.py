# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 15

def myPi(iters):    
    # Calculate an approximation of PI using the Leibniz
    # approximation with iters number of iterations
    
    # your code here  
    apprPi = 0
    
    for i in range(iters):
        term = (-1)**i/(2*i+1)
        apprPi += term
    
    return apprPi * 4
        
print(myPi(1000000))