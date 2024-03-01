# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 1

def computeFactorial(number):
    if number < 0:
        return
    elif number > 1:
        number *= computeFactorial(number - 1)
        return number
    else:
        return 1