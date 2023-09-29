# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 6

import random
import turtle
import math

def isInScreen(w, t, lBound, rBound, bBound, tBound):
    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rBound or turtleX < lBound:
        stillIn = False
    if turtleY > tBound or turtleY < bBound:
        stillIn = False

    return stillIn


def randGoto(t, num1, num2):
    return random.randrange(num1, num2)


def randPos(t, lBound, rBound, bBound, tBound):
    xpos = randGoto(t, lBound, rBound)
    ypos = randGoto(t, bBound, tBound)
    t.up()
    t.goto(xpos, ypos)
    t.down()

    
def spaceBetween(num1, num2):
    if math.sqrt(num1**2 + num2**2) < 5:
        return True
    else: 
        return False
    
    
def randMove(wn, t1, t2, lBound, rBound, bBound, tBound):
    randPos(t1, lBound, rBound, bBound, tBound)
    randPos(t2, lBound, rBound, bBound, tBound)
    
    while isInScreen(wn, t1, lBound, rBound, bBound, tBound) and isInScreen(wn, t2, lBound, rBound, bBound, tBound):
        t1x = t1.xcor()
        t1y = t1.ycor()
        t2x = t2.xcor()
        t2y = t2.ycor()
        coin = random.randrange(0, 2)
        
        if spaceBetween(t1x, lBound) or spaceBetween(t1x, rBound) or spaceBetween(t1y, bBound) or  spaceBetween(t1y, tBound):
            t1.right(170)
        if spaceBetween(t2x, lBound) or spaceBetween(t2x, rBound) or spaceBetween(t2y, bBound) or  spaceBetween(t2y, tBound):
            t2.right(170) 
        if spaceBetween(t1x, t2x) or spaceBetween(t1y, t2y):
            t1.left(170)
            t2.right(170)
            
        if coin == 0:
            t1.left(random.randrange(1,180))
            t2.left(random.randrange(1,180))
        else:
            t1.right(random.randrange(1,180))
            t2.right(random.randrange(1,180))

        t1.forward(50)
        t2.forward(50)        
        
        

wn = turtle.Screen()
wn.bgcolor("lightblue")

x1 = -wn.window_width() / 2
x2 = wn.window_width() / 2
y1 = -wn.window_height() / 2
y2 = wn.window_height() / 2

ella = turtle.Turtle()
ella.color("pink")
ella.shape('turtle')

micah = turtle.Turtle()
micah.color("green")
micah.shape('turtle')

randMove(wn, ella, micah, x1, x2, y1, y2)


wn.exitonclick()