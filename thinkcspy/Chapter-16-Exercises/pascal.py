def pascal(row):
    num = 0

    if row < 0:
        return
    else:
        if row <= 2:
            num = 1
        #elif row > 2 print 
        
        for i in range(row+1):
            if i == 0:
                continue
            else:
                print((" "*(row-i)) + (f"{num} "*i) + (" "*(row-i)))
    

pascal(8)


