# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 5

def fibonacci(number):
    if number < 0:
        return
    elif number == 0 or number == 1:
        return number
    else:
        number = fibonacci(number - 1) + fibonacci(number - 2)
        return number
    
print(fibonacci(10))