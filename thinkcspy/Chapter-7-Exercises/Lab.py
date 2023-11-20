# Runestone.Academy thinkcspy course
# Chapter 7
# Lab

import turtle
#import math
import random


fred = turtle.Turtle()
clara = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.bgcolor("tan")
wn.tracer(100)

clara.dot()
print(clara.pos())
clara.up()
clara.goto(0,1)
clara.down()
clara.circle(-1)
print(clara.pos())
print(clara.distance(0.0,0.0))

fred.up()

numdarts = 100000
insideCount = 0

for i in range(numdarts):
    randx = random.random()*2-1
    randy = random.random()*2-1
    
    fred.goto(randx,randy)
    dist = fred.distance(0.0, 0.0)
        
    if dist < 1:
        color = "red"
        insideCount += 1
        place = "in"
    else:
        color = "blue"
        place = "out"
   
    fred.down()
    fred.dot(10,color)
    fred.up()


mypi = 4 * (insideCount / numdarts)
print(insideCount,"out of", numdarts, "darts made it into the circle.")    
print("The value of Pi based on the numbers number of darts that made it into the circle is", mypi, ".")

wn.exitonclick()