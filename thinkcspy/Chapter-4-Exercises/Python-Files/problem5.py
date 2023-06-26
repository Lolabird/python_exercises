# Runestone.Academy thinkcspy course
# Chapter 4
# Problem 5

import turtle
wn = turtle.Screen()
avery = turtle.Turtle()
avery.color("blue")
dun = turtle.Turtle()
dun.color("pink")
elliot = turtle.Turtle()
elliot.color("lime")
missy = turtle.Turtle()
missy.color("yellow")

for i in range(3):
    avery.forward(50)
    avery.left(120) 
    
for i in range(4):
    dun.backward(70)
    dun.left(90)
    
for i in range(6):
    elliot.left(60)
    elliot.forward(40)
    
for i in range(8):
    missy.right(45)
    missy.backward(80)
    
wn.exitonclick()