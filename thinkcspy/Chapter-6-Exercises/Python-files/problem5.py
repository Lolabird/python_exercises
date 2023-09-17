# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 5

import turtle

def drawSquareSpiral(t, sz, num, angle):
    """Get turtle t to draw a square of sz side"""
    
    for i in range(num):
        t.forward(sz*i)
        t.left(angle)

wn = turtle.Screen()
wn.setworldcoordinates(-300,-300,300,300)
wn.bgcolor("lightgreen")


alex = turtle.Turtle()
alex.color("blue")
alex.speed(0)
alex.up()
alex.goto(-150,0)
alex.down()

tess = turtle.Turtle()
tess.color("purple")
tess.speed(0)
tess.up()
tess.goto(150,0)
tess.down()

drawSquareSpiral(alex,2,100,90)

drawSquareSpiral(tess,2,100,91)
        

wn.exitonclick()