# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 3

import turtle

def drawPolygon(t, sideLength, numSides):
    """Make turtle t draw a polygon."""
    angle = 360/numSides
    
    for i in range(numSides):
        t.forward(sideLength)
        t.left(angle)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink")
tess.pensize(2)

drawPolygon(tess,50,8) 

wn.exitonclick()