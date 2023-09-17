# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 10

import turtle

def drawStar(t):
    for i in range(5):
        t.left(144)
        t.forward(-100)

def drawFiveStars(tt):
    tt.up()
    tt.goto(-180,50)
    tt.down()
    
    for i in range(5):
        drawStar(tt)
        tt.up()
        tt.forward(350)
        tt.right(144)
        tt.down()
    
wn = turtle.Screen()
wn.bgcolor("tan")

stella = turtle.Turtle()
stella.color("purple")
stella.pensize(2)
stella.speed(10)
    
drawFiveStars(stella)

wn.exitonclick()