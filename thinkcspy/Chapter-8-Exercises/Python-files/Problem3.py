# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 3

import math

def is_prime(n):
    # your code here
    
    x = 3
  
    if abs(n) > 2:
        while x < math.sqrt(n):
            if n % 2 == 0:
                return False
            elif n % x == 0:
                return False
            else:
                x += 2
        return True
    else:
        return True

print(is_prime(4813))