# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 17

import turtle

def drawSprite(t, numSides, legLength):
    angle = 360/numSides
    
    for i in range(numSides):
        t.forward(legLength)
        t.up()
        t.forward(-legLength)    
        t.right(angle)
        t.down()

def fancySquare(tt, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        drawSprite(tt, int(sz/10), int(sz/20))
        tt.forward(sz)
        tt.left(90)

wn = turtle.Screen()
wn.bgcolor("lightblue")

alex = turtle.Turtle()
alex.color("maroon")
alex.pensize(2)

fancySquare(alex, 100)