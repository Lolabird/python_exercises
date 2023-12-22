def pascal(row):
    num = 0

    if row < 0:
        return
    else:     
        for i in range(row+1):
            spaces = ("  "*(row-i)) 
            nums = f"{getbinomial(num, i)} "
            print(spaces + nums + spaces)

    # if row == 0 or 1: num = 1
    # the first and last instance of i always == 1
    #elif row % 2 == 0:
    #   increase until the middle number then decrease
    #elif row % 2 == 1:
    #   increase until the halfway point, then decrease


def getbinomial(num, iters):
   
   return f"{num+iters}   " * iters

pascal(8)


