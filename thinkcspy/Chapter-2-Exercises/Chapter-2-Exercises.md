Problem 3
---------

_Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 3


currentTime = input('What time is it?')
currentTime = int(currentTime)

waitTime = input('In how many hours do you need to wake up?')
waitTime = int(waitTime)

print('It is currently', currentTime,'.')
print('You need to wake up in', waitTime, 'hours.')

# My solution was more long winded than the actual answer, but it still works!
totalTime = currentTime + waitTime
time24hr = totalTime // 24
alarmTime = totalTime - 24 * time24hr

print('The alarm has been set for', alarmTime, '.')
```

Problem 4
---------

_It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on._

```text-x-python
Runestone.Academy thinkcspy course
# Chapter 2
# Problem 4

currentDay = input('''Enter the current day using one of the following numbers:
Sunday    = 0
Monday    = 1
Tuesday   = 2
Wednesday = 3
Thursday  = 4
Friday    = 5
Saturday  = 6''')
currentDay = int(currentDay)

stayLength = input('How long is your stay?')
stayLength = int(stayLength)

# Improved upon the long windedness of my answer this time by following the example of the solution 
# in the previous problem
stay = currentDay + stayLength
returnDay = stay % 7

print('It is currently Day', currentDay,'.')
print('Your stay is ', stayLength, 'days long.')
print('You will return on Day', returnDay, '.')
print('''Sunday    = 0
Monday    = 1
Tuesday   = 2
Wednesday = 3
Thursday  = 4
Friday    = 5
Saturday  = 6''')
```

Problem 7
---------

_The formula for computing the final amount if one is earning compound interest is given on Wikipedia as_

_![formula for compound interest](api/images/9sYRfd0tfbOC/compoundInterest.png)_

_Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 7

P = 10000 
n = 12
r = 0.08
n = 12

# Noticed that they gave separate variables to the inputs problem 3 and
# the converted ints so decided to do the same here.
t_string = input('For how many years will your principal be earning interest?')
t = int(t_string)

A = P*(1+r/n)**(n*t)

print('The final amount after you will earn after', t, 'years is', A)
```

Problem 8
---------

_Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 8

r_string = input('Enter the radius of the circle')
r = int(r_string)
pi = 3.14

area = pi * r**2

print('The approximate area of the circle with', r, 'radius is', area, '.')
```

Problem 9
---------

_Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 9

width = input('What is the width of the rectangle?')
w = int(width)

height = input('What is the height of the rectangle?')
h = int(height)

area = w*h

print('The area of the rectangle with a width of', w, 'and a height of', h, 'is', area, '.')
```

Problem 10
----------

_Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 10

miles =  input('How many miles did you drive before refueling?')
mi = int(miles)

gallons = input('How many gallons did you use to refuel your vehicle?')
gal = int(gallons)

mpg = mi / gal

print('Your fuel efficiency is', mpg, 'MPG.')
```

Problem 11
----------

_Write a program that will convert degrees celsius to degrees fahrenheit._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 11

celcius = input('What is the temperature in degrees celsius?')
C = int(celcius)

F = (C * 9/5) + 32

print(C, 'degrees celcius is equivalent to', F, 'degrees fahrenheit.')
```

Problem 12
----------

_Write a program that will convert degrees fahrenheit to degrees celsius._

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 2
# Problem 12

fahrenheit = input('What is the temperature in degrees fahrenheit?')
F = int(fahrenheit)

C = (F - 32) * 5/9

print(F, 'degrees fahrenheit is equivalent to', C, 'degrees celcius.')
```