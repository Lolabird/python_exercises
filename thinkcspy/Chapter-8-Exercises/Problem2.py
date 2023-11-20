# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 2

def print_triangular_numbers(n):
    # your code here
    i = 1

    while i <= n:
        trinum = 0
        bound = i
        
        while bound > 0:
            trinum += bound
            bound -= 1

        print(i, "\t", trinum)
        i += 1
    
print_triangular_numbers(5)