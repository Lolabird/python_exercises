# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 13

def createTriangle(numRows):
    triangle = []

    if numRows < 0:
        return
    else:     
        for i in range(numRows+1):
            triangle.append(createRow(i))

        lastRow = triangle[-1]
        numWidth = len(str(max(lastRow))) + 1
        triWidth = numWidth * len(lastRow)

        for row in triangle:
            triStr = ""

            for num in row:
                numStr = str(num)
                triStr += numStr + " " * (numWidth - len(numStr))
            
            print(triStr.center(triWidth))


def createRow(currentRow):
    row = []

    for i in range(currentRow + 1):
        coefficient = getbinomial(currentRow, i)
        row.append(coefficient)

    return row

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


