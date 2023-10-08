# Runestone.Academy thinkcspy course
# Chapter 9
# Problem 4

# your code here

num1 = 1
product = 0

for n in range(12):
    num2 = 1
    row = ""

    for x in range(12):
        product = num1 * num2
        row += "{} \t".format(product)
        num2 += 1

    print(row)
    num1 += 1