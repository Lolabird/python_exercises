# Runestone.Academy thinkcspy course
# Chapter 5
# Lab

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

turtle.setworldcoordinates(0, -1.25, 360, 1.25)

fred = turtle.Turtle()
fred.speed(10)
fred.color('red')

george = turtle.Turtle()
george.speed(10)
george.color('blue')

for angle in range(361):
    x = angle
    y = math.sin(math.radians(angle))
    fred.goto(x,y)
    
for angle in range(361):
    x = angle
    y = math.cos(math.radians(angle))
    george.goto(x,y)

wn.exitonclick()