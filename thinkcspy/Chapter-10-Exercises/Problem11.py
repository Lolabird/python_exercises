# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 11

def sumUntilEven(lst):
    # your code here
    sumlist = 0
    
    for num in lst:
        if num % 2 != 0:
            sumlist += num
        else:
            return sumlist
        
    return sumlist

mylist = [15, 85, 11, 20, 27, 38, 13]
oddlist = [13, 11, 29, 37]

print(sumUntilEven(mylist))
print(sumUntilEven(oddlist))