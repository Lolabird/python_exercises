def readposint(num):
    try:
        val = int(num)
        if val > 0:
            print("You entered '{}'.".format(val))
        else:
            print("'{}' is not a positive.".format(val))
    except Exception:
        print("'{}' is not a number.".format(num))  

readposint(input("Please enter a positive number: "))