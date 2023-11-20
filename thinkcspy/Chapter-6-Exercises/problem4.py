# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 4

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)
alex.speed(10)


def drawCircleSquares(tt, num):
    for i in range(num):
        drawSquare(tt, 80)
        tt.right(15)
        

drawCircleSquares(alex, 25)        
        

wn.exitonclick()