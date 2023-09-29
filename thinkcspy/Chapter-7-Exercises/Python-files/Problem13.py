# Runestone.Academy thinkcspy course
# Chapter 7
# Problem 13

def isLeap(year):
    # your code here
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: 
        return False

def easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
        
    if year >= 1900 and year <= 2099:
        if isLeap(year):
            dateofeaster = 22 + d + e - 7
        else:
            dateofeaster = 22 + d + e 
    else:
        dateofeaster = 0    

    return dateofeaster

def convertDate(year):
    date = easter(year)
    
    if date == 0:
        print("Error: Date is out of range.")
    elif date <= 30:
        print("In", year, "Easter falls on March", date - 1, ".")
    else:
        print("In", year, "Easter falls on April", date - 31, ".")

userYear = int(input("Enter a year between 1900 and 2099."))

convertDate(userYear)
