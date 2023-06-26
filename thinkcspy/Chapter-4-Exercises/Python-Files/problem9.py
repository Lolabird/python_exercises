# Runestone.Academy thinkcspy course
# Chapter 4
# Problem 9

import turtle
wn = turtle.Screen()

stella = turtle.Turtle()
stella.color("yellow")

stella.up()
stella.forward(-50)
stella.down()

for i in range(5):
    stella.left(144)
    stella.forward(-100)

wn.exitonclick()