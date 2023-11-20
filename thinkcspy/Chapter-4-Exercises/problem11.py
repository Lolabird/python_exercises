# Runestone.Academy thinkcspy course
# Chapter 4
# Problem 11

import turtle
wn = turtle.Screen()

wn.bgcolor("black")

stella = turtle.Turtle()
stella.color("lightblue")
stella.speed(10)

avery = turtle.Turtle()
avery.color("purple")
avery.speed(10)
avery.up()
avery.right(90)
avery.down()

missy = turtle.Turtle()
missy.color("purple")
missy.speed(10)
missy.up()
missy.left(90)
missy.down()

dun = turtle.Turtle()
dun.color("gold")
dun.speed(10)
dun.up()
dun.left(90)
dun.forward(30)
dun.right(90)
dun.down()

for i in range(8):
    stella.left(135)
    stella.forward(-120)
    
    avery.right(45)
    avery.forward(-50)

for i in range(30, -32, -1):
    missy.forward(i)
    missy.left(20)

dun.forward(120)
dun.left(120)
dun.forward(70)
for i in range(2):
    dun.left(120)
    dun.forward(30)
    dun.right(120)
    dun.forward(30)
dun.left(120)
dun.forward(70)
    
wn.exitonclick()