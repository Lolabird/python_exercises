# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 2

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


def drawStackedSquares(tt, num):
    for i in range(num):
        drawSquare(tt, 20*(i+1))
        tt.up()
        tt.backward(10)
        tt.left(90)
        tt.backward(10)
        tt.right(90)
        tt.down()
        

drawStackedSquares(alex, 5)        
        

wn.exitonclick()