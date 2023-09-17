# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 11

import turtle

def drawStar(t, numSides, sideLength):
    angle = 180 - 180/numSides
    
    t.up()
    t.goto(sideLength/2,0)
    t.down()
    
    for i in range(numSides):
        t.left(angle)
        t.forward(sideLength)

def checkSides(tt, sides, length):
    if sides >= 3 and sides % 2 != 0:
        print("What a beautiful star!")
        drawStar(tt, sides, length)
    else:
        print("Oops! Your star must have an ODD number of at least 3 sides. Let's try that again!")

    
wn = turtle.Screen()
wn.bgcolor("tan")

stella = turtle.Turtle()
stella.color("purple")
stella.pensize(2)
stella.speed(0)

a = int(input("Help Stella draw a star! How many points does the star have?"))
b = int(input("How long is each side?"))        

checkSides(stella, a, b)

wn.exitonclick()