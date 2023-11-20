# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 3

def is_prime(n):
    # your code 
        
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(25))