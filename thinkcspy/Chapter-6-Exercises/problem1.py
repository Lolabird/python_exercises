# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 1

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")
alex.pensize(2)


def drawManySquares(tt, num):
    for i in range(num):
        drawSquare(tt, 20)
        tt.up()
        tt.forward(30)
        tt.down()
        

drawManySquares(alex, 5)        
        

wn.exitonclick()