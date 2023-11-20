# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 12

import turtle

def drawSprite(t, numSides, legLength):
    angle = 360/numSides
    
    for i in range(numSides):
        t.forward(legLength)
        t.up()
        t.forward(-legLength)    
        t.right(angle)
        t.down()


wn = turtle.Screen()

wn.bgcolor("tan")

avery = turtle.Turtle()
avery.color("brown")

drawSprite(avery, 15, 120)

    
wn.exitonclick()