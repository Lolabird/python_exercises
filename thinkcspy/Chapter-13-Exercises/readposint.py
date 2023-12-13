def readposint(num):
    try:
        val = int(num)
        if val > 0:
            print("You entered '{}'. That's a positive number!".format(val))
        else:
            print("'{}' is not a positive number.".format(val))
    except Exception:
        print("'{}' is not a number.".format(num))  

readposint(input("Please enter a positive number: "))