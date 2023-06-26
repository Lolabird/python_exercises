# Runestone.Academy thinkcspy course
# Chapter 4
# Problem 10

import turtle
wn = turtle.Screen()

wn.bgcolor("lightgreen")

stella = turtle.Turtle()
stella.color("blue")
stella.shape("turtle")

avery = turtle.Turtle()
avery.color("blue")

stella.up()
avery.up()

stella.stamp()

for i in range(12):
    stella.forward(100)
    stella.stamp()
    
    avery.forward(70)
    avery.down()
    avery.forward(10)
    avery.up()
    
    stella.forward(-100)    
    avery.forward(-80)    
    
    stella.right(30)
    avery.right(30)
    
wn.exitonclick()