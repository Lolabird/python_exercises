# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 13

def createTriangle(numRows):
    if numRows < 0:
        return
    else:     
        for i in range(numRows+1):
            spaces = ("  "*(numRows-i)) 
            nums = f"{createRow(i)}"
            print(spaces + nums + spaces)


def createRow(currentRow):
    row = []

    for i in range(currentRow + 1):
        coefficient = getbinomial(currentRow, i)
        row.append(coefficient)

    result = "  ".join(map(str, row))

    return result

def getbinomial(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator // denominator


def factorial(number):
    if number < 0:
        return
    elif number > 1:
        number *= factorial(number - 1)
        return number
    else:
        return 1
        


createTriangle(10)


